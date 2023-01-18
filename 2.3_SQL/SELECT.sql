/* Задача 1 */
SELECT name, date_created FROM albums
WHERE date_created  BETWEEN '2018-01-01' AND '2018-12-31';

/* Задача 2 */
SELECT name, time FROM tracks
ORDER BY time desc
limit 1;

/* Задача 3 */
SELECT name, time FROM tracks
WHERE time >= 210;

/* Задача 4 */
SELECT name, date_created from collections
WHERE date_created BETWEEN '2018-01-01' AND '2020-12-31';

/* Задача 5 */
SELECT name from artists
where name not like '% %';

/* Задача 6 */
SELECT name, time from tracks
where name like '%Мой%';