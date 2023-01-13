insert into artists(name)
values ('artist_1'),
       ('artist_2'),
       ('artist_3'),
       ('artist_4'),
       ('artist_5'),
       ('artist_6'),
       ('artist_7'),
       ('artist_8');


insert into genres(name)
values ('rock'),
       ('rap'),
       ('cock'),
       ('kek'),
       ('lol'),
       ('mda');



insert into albums(name)
values ('album_1'),
       ('album_2'),
       ('album_3'),
       ('album_4'),
       ('album_5'),
       ('album_6'),
       ('album_7'),
       ('album_8');



insert into tracks(name, id_album)
values ('track_1', 36),
       ('track_2', 35),
       ('track_3', 36),
       ('track_4', 35),
       ('track_5', 42),
       ('track_6', 41),
       ('track_7', 40),
       ('track_8', 38),
       ('track_9', 38),
       ('track_10', 40),
       ('track_11', 38),
       ('track_12', 42),
       ('track_13', 41),
       ('track_14', 39);


insert into collections(name)
values ('collection_1'),
       ('collection_2'),
       ('collection_4'),
       ('collection_5'),
       ('collection_6'),
       ('collection_7'),
       ('collection_8'),
       ('collection_9');


insert into album_artists(id_album, id_artist)
values (35,11),
       (36,12),
       (37,12),
       (38,15),
       (39,14),
       (40,15),
       (41,16),
       (42,17),
       (35,18),
       (37,18),
       (36,18),
       (38,11);


insert into genres_artists(id_genre, id_artists)
values (1,11),
       (1,12),
       (1,13),
       (2,11),
       (2,13),
       (3,15),
       (3,14),
       (4,15),
       (5,16),
       (5,17),
       (6,17),
       (4,18);

insert into tracks_collections(id_track, id_collection)
values (19,1),
       (20,1),
       (21,2),
       (22,2),
       (23,2),
       (24,3),
       (25,3),
       (26,4),
       (27,4),
       (28,4),
       (29,5),
       (30,5),
       (31,5),
       (32,6);