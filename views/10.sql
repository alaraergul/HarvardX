SELECT COUNT(*) AS "Prints with Color FF", contrast
FROM views
WHERE average_color LIKE 'ff%'
ORDER BY contrast DESC;
