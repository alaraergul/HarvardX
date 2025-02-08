SELECT title
FROM episodes
WHERE strftime('%m', air_date) = '12' AND topic IS NULL;
