/* Задача 1 */

select name,  count(id_artists) from genres_artists
left join genres on genres_artists.id = genres.id
group by name;

/* Задача 2 */

select tracks.name, albums.date_created
from albums as albums
left join tracks as tracks on tracks.id_album = albums.id
where (albums.date_created >= '2019-01-01') and (albums.date_created <= '2020-12-31');


/* Задача 3 */

select albums.name, AVG(tracks.time) from albums
left join tracks on tracks.id_album = albums.id
group by albums.name
order by AVG(tracks.time);

/* Задача 4 */

select a.name
from artists as a
left join album_artists as aa on a.id = aa.id_artist
left join albums as al on (al.id = aa.id_album)
group by a.name, a.id
having count(case when al.date_created = 2020 then a.id end)=0
order by a.name

/* Задача 5 */

select distinct c.name from collections as c
left join tracks_collections as tc on c.id = tc.id_collection
left join tracks as t on t.id = tc.id_track
left join albums as a on a.id = t.id_album
left join album_artists as aa on t.id_album = a.id
left join artists as m on m.id = aa.id_artist
where m.name like '%%artist_1%%'
order by c.name;

/* Задача 6 */

select a.name from albums as a
left join album_artists as aa on a.id = aa.id_album
left join artists as ar on ar.id = aa.id_artist
left join genres_artists as ga on ar.id = ga.id_artists
left join genres as g on g.id = ga.id_genre
group by a.name
having count(distinct g.name) > 1
order by a.name;

/* Задача 7 */

select name from tracks
left join tracks_collections on tracks.id = tracks_collections.id_track
group by name
having count(id_collection) < 1;

/* Задача 8 */

select a.name, t.time
from tracks as t
left join albums as al on al.id = t.id_album
left join album_artists as aa on aa.id_album = al.id
left join artists as a on a.id = aa.id_artist
group by a.name, t.time
having t.time = (select min(time) from tracks)
order by a.name;

/* Задача 9 */

select distinct a.name
from albums as a
left join tracks as t on t.id_album = a.id
where t.id_album in (
    select id_album
    from tracks
    group by id_album
    having count(id) = (
        select count(id)
        from tracks
        group by id_album
        order by count
        limit 1
    )
)
order by a.name
