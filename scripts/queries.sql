-- QUERY_TITLES_PER_COUNTRY
SELECT country, COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY country
ORDER BY total_titles DESC;

-- QUERY_TITLES_BY_YEAR
SELECT 
    YEAR(STR_TO_DATE(date_added, '%M %d, %Y')) AS year, 
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE date_added IS NOT NULL
GROUP BY year
ORDER BY year DESC;

-- QUERY_TITLES_BY_RATING
SELECT rating, COUNT(*) AS total
FROM netflix_titles
GROUP BY rating
ORDER BY total DESC;
