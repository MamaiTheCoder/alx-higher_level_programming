-- Lists all cities contained in the database hbtn_0d_usa.
-- Each records displays cities.id - cities.name - states.name.
-- Results are sorted in ascending order by cities.id
-- Only one SELECT statement is used.
-- The database name will be passed as an argument of the mysql command.

SELECT cities.id, cities.name, states.name FROM hbtn_0d_usa.cities INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC;