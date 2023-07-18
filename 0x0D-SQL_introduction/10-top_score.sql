-- A script that lists all records of the table second_table of the
-- database hbtn_0c_0 in a MySQL server order by score (top first)

-- SELECT statement is used for displaying the rows of a table
SELECT score, name
FROM `second_table`
ORDER BY score DESC;
