-- A script that creates the MySQL server user user_0d_1
-- and assign password and granted all privileges to it
CREATE USER IF NOT EXISTS 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1' WITH GRANT OPTION;
