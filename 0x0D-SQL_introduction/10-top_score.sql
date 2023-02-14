-- Lists all records of the table second_table of the database hbtn_0c_0 in MySQL server.
-- Results displays both the score and the name.
-- Records is ordered by score (top first).
-- The database name will be passed as an argument of the mysql command.

SELECT score, name FROM second_table ORDER BY score DESC;
