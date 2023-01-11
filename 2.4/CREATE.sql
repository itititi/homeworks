/*Cоздаю базу данных*/

CREATE DATABASE IF NOT EXISTS musicapp;


/*Cоздаю таблицы*/

CREATE TABLE IF NOT EXISTS albums
(
        id serial primary key ,
        name text,
        date_created date default CURRENT_DATE

);


CREATE TABLE IF NOT EXISTS tracks(
    id serial primary key,
    name text,
    time int,
    id_album int references albums (id)
);

CREATE TABLE IF NOT EXISTS artists(
    id serial primary key,
    name text
);


CREATE TABLE IF NOT EXISTS genres(
    id serial primary key,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS collections(
    id serial primary key,
    name VARCHAR(100) NOT NULL,
    year INTEGER NOT NULL
);

/*Таблицы многие ко многим*/

CREATE TABLE IF NOT EXISTS album_artists(
    id serial primary key,
    id_album int references albums (id),
    id_artist int references artists (id)
);


CREATE TABLE IF NOT EXISTS genres_artists(
    id serial primary key,
    id_genre int references genres (id),
    id_artists int references artists (id)
);

CREATE TABLE IF NOT EXISTS tracks_collections(
    id serial primary key,
    id_track int references tracks (id),
    id_collection int references collections (id)
);