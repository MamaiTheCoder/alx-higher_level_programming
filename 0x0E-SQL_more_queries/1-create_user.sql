-- Creates the MySQL server user user_0d_1.
-- user_0d_1 has all the privileges on MySQL server.
-- user_0d_1 password is set to user_0d_1_pwd.
-- Script does not fail If the user user_0d_1 already exists.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
