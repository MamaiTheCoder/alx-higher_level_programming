# MySQL - Introduction
ALX project done to facilitate completion of Full Stack Software Engineering course.

## Learning Objectives
* Databases
* Relational databases, 
* SQL
* Creation of database in MySQL
* DDL and DML.
* `CREATE` and `ALTER` a table
* `SELECT` data from a table.
* `INSERT`, `UPDATE`, or `DELETE` data.
* subqueries
* Using **MySQL** functions.

## Technologies
* MySQL 8.0.28.
* Tested on Ubuntu 20.04 LTS.

## Files

All the following files are scripts of MySQL:

| Filename | Description |
| -------- | ----------- |
| `0-list_databases.sql` | Lists all databases of a MySQL server |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` in a MySQL server |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` in a MySQL server |
| `3-list_tables.sql` | Lists all the tables of a database in a MySQL server |
| `4-first_table.sql` | Creates a table called `first_table` in the current database |
| `5-full_table.sql` | Prints the full description of the table `first_table` from the database `hbtn_0c_0`  |
| `6-list_values.sql` | Lists all rows of the table `first_table` from the database `hbtn_0c_0` |
| `7-insert_value.sql` | Inserts a new row in the table `first_table` of the database `hbtn_0c_0` |
| `8-count_89.sql` | Displays the number of records with `id=89` in the table `first_table` of the database `hbtn_0c_0` |
| `9-full_creation.sql` | Creates a table `second_table` in the database `hbtn_0c_0` |
| `10-top_score.sql` | Lists all records of the table `second_table` of the database `hbtn_0c_0` |
| `11-best_score.sql` | Lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` |
| `12-no_cheating.sql` | Updates the score of Bob to `10` in the table `second_table` |
| `13-change_class.sql` | Removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` |
| `14-average.sql` | Computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` |
| `15-groups.sql` | Lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` |
| `16-no_link.sql` | Lists all records of the table `second_table` of the database `hbtn_0c_0` |
| `100-move_to_utf8.sql` | Converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`)  |
| `101-avg_temperatures.sql` | Displays the average temperature (Fahrenheit) by city ordered by temperature (descending) |
| `102-top_city.sql` | Displays the top 3 of cities temperature during July and August ordered by temperature (descending) |
| `103-max_state.sql` | Displays the max temperature of each state (ordered by State name) |

## Comments for SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

## Install MySQL 8.0.28 on Ubuntu 20.04 LTS
```
sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.28-0ubuntu0.20.04.3 for Linux on x86_64 ((Ubuntu))    
```
# Connect to your MySQL server:
```
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 19
Server version: 8.0.28-0ubuntu0.20.04.3 (Ubuntu)

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its 
affiliates. Other names may be trademarks of their respective 
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> quit                                                  
Bye 
```

# Use “container-on-demand” to run MySQL
In the container, credentials are `root/root`
* Ask for container Ubuntu 20.04
* Connect via SSH
* OR connect via the Web terminal
* In the container, you should start MySQL before playing with it:
```
$ service mysql start
  * Starting MySQL database server mysqld                     [ OK ] 
$ cat 0-list_databases.sql | mysql -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
sys 
$
```
