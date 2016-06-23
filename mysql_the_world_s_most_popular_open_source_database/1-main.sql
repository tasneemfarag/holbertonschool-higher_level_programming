\! echo "\nNumber of seasons by tvshow_id?"
#Number of seasons by tvshow_id?
SELECT tvshow_id, count(id)
FROM Season
GROUP BY tvshow_id;

\! echo "\nNumber of occurrences of the same episode number ordered by episode number?"
#Number of occurrences of the same episode number ordered by episode number?
SELECT number, COUNT(id)
FROM Episode
GROUP BY number
ORDER BY number;


\! echo "\nTop 3 of the Genre's occurrences in all TVShows ordered by this number?"
#Top 3 of the Genre's occurrences in all TVShows ordered by this number?
SELECT genre_id, count(tvshow_id) as occurrences_genre 
FROM TVShowGenre
GROUP BY genre_id
ORDER BY occurrences_genre DESC
LIMIT 3;

\! echo "\nSearch all TVShow with this letter sequence 'th' case insensitive and display with the name in lowercase?"
#Search all TVShow with this letter sequence 'th' case insensitive and display with the name in lowercase?
SELECT LOWER(name) as name
FROM TVShow
WHERE name REGEXP 'th';