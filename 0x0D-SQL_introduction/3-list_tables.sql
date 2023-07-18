-- Script that lists all tables in a passed mysql database

-- SELECT keyword is used to list tables in a mysql database
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = DATABASE();
