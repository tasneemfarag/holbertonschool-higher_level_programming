\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
#Number of season by TVShow ordered by name (A-Z)
SELECT name, count(*) as nb_seasons
FROM TVShow, Season
WHERE tvshow_id = TVShow.id
GROUP BY name
ORDER BY name;

\! echo "\nList of Network by TVShow ordered by name (A-Z)?"
#List of Network by TVShow ordered by name (A-Z)? (with aliases TVShow name and Network name)
SELECT TVShow.name as 'TVShow name', Network.name as 'Network name'
FROM Network, TVShow
WHERE network_id = Network.id
GROUP BY TVShow.name
ORDER BY TVShow.name; 

\! echo "\nList of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?"
#List of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?
SELECT TVShow.name as name
FROM TVShow, Network
WHERE Network.name = 'Fox (US)' AND network_id = Network.id
ORDER BY TVShow.name;

\! echo "\nNumber of episodes by TVShows ordered by name (A-Z)?"
#Number of episodes by TVShows ordered by name (A-Z)?(with alias nb_episodes)
SELECT TVShow.name as name, count(*) as nb_episodes
FROM TVShow, Episode, Season
WHERE tvshow_id = TVShow.id AND Season.id = season_id
GROUP BY TVShow.name
ORDER BY TVShow.name;

