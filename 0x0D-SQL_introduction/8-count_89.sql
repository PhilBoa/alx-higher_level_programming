-- A script that  displays the number of records with id = 89
-- in the table first_table of the database hbtn_0c_0 in a MySQL server

-- SELECT COUNT statement is used for the numver of records in a mysql table
SELECT COUNT(*)
FROM first_table
WHERE id = 89;
