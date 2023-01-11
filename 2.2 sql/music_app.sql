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
    name text
);

CREATE TABLE IF NOT EXISTS collections(
    id serial primary key,
    name text,
    date_created date default CURRENT_DATE
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

/*Пошли инсерты*/

insert into albums(name)
values ('album_1'),
       ('album_2'),
       ('album_3');

insert into tracks(name, id)
values ('track_1', 2),
       ('track_2', 3),
       ('track_3', 1);

insert into artists(name)
values ('artist_2'),
       ('artist_2');

insert into album_artists(id_album, id_artist)
values (1,2),
       (2,1),
       (3,2),
       (3,1);

insert into genres(name)
values ('rock'),
       ('rap'),
       ('cock');

insert into genres_artists(id_genre, id_artist)
values (1,2),
       (2,1),
       (3,1),
       (2,3);


insert into collections(name)
values ('collection_1'),
       ('collection_2'),
       ('collection_3');

insert into tracks_collections(id_track, id_collection)
values (1,2),
       (2,1),
       (3,1),
       (3,2);



