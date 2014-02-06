CREATE TABLE usuario(
	id_u  VARCHAR(25) NOT NULL PRIMARY KEY,
	name_u VARCHAR(120) ,
	screen_name VARCHAR(50) ,
	profile_image_url varchar(250) ,		
	estado boolean not null
	
 );

CREATE TABLE tweet(
     id_t VARCHAR(25) not null primary key,
     text_t text,
     created_at VARCHAR(35),
     source VARCHAR(10),
     latitud numeric,
     longitud numeric,
     imagen VARCHAR(120),
     estado boolean
   
 );
 create table usuario_tweet(
	id_u  VARCHAR(25) ,
	id_t varchar(25)
);

 alter table usuario_tweet
add constraint fk_id_u_usuario_tweet
Foreign key (id_u)
references usuario(id_u);


 alter table usuario_tweet
add constraint fk_id_t_usuario_tweet
Foreign key (id_t)
references tweet(id_t);


CREATE OR REPLACE FUNCTION registrar_tweet(
	_id_u  VARCHAR(25),
	_name_u VARCHAR(120) ,
	_screen_name VARCHAR(50) ,
	_profile_image_url VARCHAR(250) ,		
	_estado_u boolean,
	_id_t VARCHAR(25),
	_text_t text,
	_created_at VARCHAR(35),
	_source VARCHAR(10),
	_latitud numeric,
	_longitud numeric,
	_imagen VARCHAR(120),
	_estado_t boolean	
	)
RETURNS  BOOLEAN
AS $$
DECLARE
	_existe_usuario BOOLEAN;
	_existe_tweet BOOLEAN;	
	BEGIN
		_existe_usuario=(select exists(select 1 from usuario where id_u=_id_u));
		IF (_existe_usuario) THEN
			RAISE NOTICE 'EXISTE';
		ELSE
			INSERT INTO usuario(id_u, name_u, screen_name, profile_image_url, estado)
			VALUES (_id_u, _name_u, _screen_name, _profile_image_url, _estado_u);
		END IF;
		_existe_tweet=(select exists(select 1 from tweet where id_t=_id_t));
		IF (_existe_tweet) THEN
			RAISE NOTICE 'EXISTE TWEET';
		ELSE
			INSERT INTO tweet(id_t, text_t, created_at, source, latitud, longitud, imagen, estado)
			VALUES (_id_t, _text_t, _created_at, _source, _latitud, _longitud, _imagen, _estado_t);
			INSERT INTO usuario_tweet(id_u, id_t)  VALUES (_id_u, _id_t);

		END IF;				
		
	RETURN _existe_tweet;
	END;
$$ LANGUAGE plpgsql;

