select m.movie_id,title,budget,revenue,currency,unit,
case 
    when unit = "Thousands" then round((revenue-budget)/1000,1)
    when unit = "billions" then round((revenue-budget)*1000,1)
    else round((revenue-budget),1)
end as profit_mln
from movies m join financials f on m.movie_id = f.movie_id where industry = "Bollywood" order by profit_mln desc ;