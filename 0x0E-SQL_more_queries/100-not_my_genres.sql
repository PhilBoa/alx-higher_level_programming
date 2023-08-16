-- A script that uses the hbtn_0d_tvshows database to list all
-- genres not linked to the show Dexter
-- Each record displays: tv_genres.name
-- Results are sorted in ascending order by the genre name
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
	SELECT tv_show_genres.genre_id
	FROM tv_show_genres
	JOIN tv_shows ON tv_show_genres.show_id = tv_show.id
	WHERE tv_shows.title = 'Dexter'
) AS linked_genres ON tv_genres.id = linked_genres.genre_id
WHERE linked_genres.genre_id IS NULL
ORDER BY tv_genres.name ASC;
