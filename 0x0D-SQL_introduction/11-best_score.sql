-- A script that lists all records of the table second_table of the
-- database hbtn_0c_0 in a MySQL server order by score (top first)
-- if the score is equals or greater than 10

-- SELECT statement is used for displaying the rows of a table
SELECT score, name
FROM `second_table`
WHERE score >= 10
ORDER BY score DESC;
