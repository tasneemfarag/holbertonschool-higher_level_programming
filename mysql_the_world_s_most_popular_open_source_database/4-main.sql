\! echo "\nList of all TVShows by all Genres ordered by genre name (A-Z)? (with aliases Genre name and TVShow name. If a genre has 0 TVShow, please display NULL)"
#List of all TVShows by all Genres ordered by genre name (A-Z)? (with aliases Genre name and TVShow name. If a genre has 0 TVShow, please display NULL)
SELECT GTSG.name as 'Genre name', IF(GTSG.tvshow_id IS NULL, 'NULL', TVShow.name) as 'TVShow name' 
From (SELECT * FROM Genre LEFT JOIN TVShowGenre ON Genre.id = TVShowGenre.genre_id) as GTSG LEFT JOIN TVShow ON TVShow.id = GTSG.tvshow_id
ORDER BY GTSG.name;

\! echo "\nName of the pilot (first episode of the first season) of each TVShow ordered by TVShow name (A-Z)?"
#Name of the pilot (first episode of the first season) of each TVShow ordered by TVShow name (A-Z)? (with aliases TVShow name and Episode name)
SELECT TVShow.name as 'TVShow name', Episode.name as 'Episode name'
FROM TVShow, Episode, Season
WHERE Season.number = 1 AND Episode.number = 1 AND Episode.season_id = Season.id AND TVShow.id = Season.tvshow_id 
ORDER BY TVShow.name;

\! echo "\nList of all Genres by all TVShows ordered by TVShow name (A-Z)? (with aliases TVShow name and Genre name. If a genre has 0 TVShow, please display NULL as TVShow name)"
#List of all Genres by all TVShows ordered by TVShow name (A-Z)? (with aliases TVShow name and Genre name. If a genre has 0 TVShow, please display NULL as TVShow name)
SELECT IF(GTSG.tvshow_id IS NULL, 'NULL', TVShow.name) as 'TVShow name', GTSG.name as 'Genre name'
From (SELECT * FROM Genre LEFT JOIN TVShowGenre ON Genre.id = TVShowGenre.genre_id) as GTSG LEFT JOIN TVShow ON TVShow.id = GTSG.tvshow_id
ORDER BY TVShow.name;

