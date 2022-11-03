-- a script that lists all shows contained in hbtn_0d_tvshows without a genre linked

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
-- since genres id is null, no genre linked
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
