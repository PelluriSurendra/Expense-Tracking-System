select m.title,group_concat(a.name separator " | ") as actors from movies m join movie_actor ma on m.movie_id = ma.movie_id 
join actors a on a.actor_id = ma.actor_id group by m.movie_id