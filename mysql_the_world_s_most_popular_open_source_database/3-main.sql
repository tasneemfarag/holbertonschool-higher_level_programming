\! echo "\nList of TVShows ordered by name (A-Z) with more than or equal 4 seasons?"
#List of TVShows ordered by name (A-Z) with more than or equal 4 seasons?
SELECT name 
FROM TVShow, Season
WHERE number >= 4 AND TVShow.id = tvshow_id
GROUP BY name
ORDER BY name;

\! echo "\nList of TVShows ordered by name (A-Z) with the Genre 'Comedy'?"
#List of TVShows ordered by name (A-Z) with the Genre 'Comedy'?
SELECT TVShow.name as name  
FROM TVShow, Genre, TVShowGenre
WHERE Genre.name = 'Comedy' AND Genre.id = TVShowGenre.genre_id AND TVShow.id = TVShowGenre.tvshow_id
GROUP BY TVShow.name
ORDER BY TVShow.name;

\! echo "\nList of Actors ordered by name (A-Z) for the TVShow 'The Big Bang Theory'?"
#List of Actors ordered by name (A-Z) for the TVShow 'The Big Bang Theory'?
SELECT Actor.name as name
FROM Actor, TVShow, TVShowActor
WHERE TVShow.name = 'The Big Bang Theory' AND Actor.id = TVShowActor.actor_id AND TVShow.id = TVShowActor.tvshow_id
GROUP BY Actor.name
ORDER BY Actor.name;

\! echo "Top 10 of Actors by number of TVShows where they are? (with alias nb_tvshows, without Actor name order => can be random)"
#Top 10 of Actors by number of TVShows where they are? (with alias nb_tvshows, without Actor name order => can be random)
SELECT Actor.name, count(tvshow_id) as nb_tvshows
FROM Actor, TVShowActor
WHERE Actor.id = TVShowActor.actor_id
GROUP BY Actor.name
ORDER BY nb_tvshows DESC
LIMIT 10;