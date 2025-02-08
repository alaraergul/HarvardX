SELECT first_name, last_name, debut AS "Debut Date"
FROM players
WHERE birth_state = 'CA' AND debut > '1990-01-01'
ORDER BY debut, first_name;
