# SQL - More queries

ALX project done to facilitate completion of Full Stack Software Engineering course.

## Learnng Objectives

- Creating a new MySQL user.
- Manage privileges for a user to a database or table.
- `PRIMARY KEY` and `FOREIGN KEY`
- Using `NOT NULL` and `UNIQUE` constraints.
- Retrieving datas from multiple tables in one request.
- Subqueries
- `JOIN` and `UNION`

## Technologies

- MySQL 8.0.28.
- Tested on Ubuntu 20.04 LTS.

## Files

All the following files are scripts of MySQL:

| Filename                              | Description                                                                               |
| ------------------------------------- | ----------------------------------------------------------------------------------------- |
| `0-privileges.sql`                    | Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server.       |
| `1-create_user.sql`                   | Creates the MySQL server user `user_0d_1`                                                 |
| `2-create_read_user.sql`              | Creates the database `hbtn_0d_2` and the user `user_0d_2`                                 |
| `3-force_name.sql`                    | Creates the table `force_name` on your MySQL server                                       |
| `4-never_empty.sql`                   | Creates the table `id_not_null` on your MySQL serve                                       |
| `5-unique_id.sql`                     | Creates the table `unique_id` on your MySQL server                                        |
| `6-states.sql`                        | Creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) |
| `7-cities.sql`                        | Creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) |
| `8-cities_of_california_subquery.sql` | Lists all the cities of California that can be found in the database `hbtn_0d_usa`        |
| `9-cities_by_state_join.sql`          | Lists all cities contained in the database `hbtn_0d_usa`                                  |
| `10-genre_id_by_show.sql`             | Lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked        |
| `11-genre_id_all_shows.sql`           | Lists all shows contained in the database `hbtn_0d_tvshows`                               |
| `12-no_genre.sql`                     | Lists all shows contained in `hbtn_0d_tvshows` without a genre linked                     |
| `13-count_shows_by_genre.sql`         | Lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each   |
| `14-my_genres.sql`                    | Uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`              |
| `15-comedy_only.sql`                  | Lists all Comedy shows in the database `hbtn_0d_tvshows`                                  |
| `16-shows_by_genre.sql`               | Lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`  |
| `100-not_my_genres.sql`               | Uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`    |
| `101-not_a_comedy.sql`                | Lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`              |
| `102-rating_shows.sql`                | Lists all shows from `hbtn_0d_tvshows_rate` by their rating                               |
| `103-rating_genres.sql`               | Lists all genres in the database `hbtn_0d_tvshows_rate` by their rating                   |

## Comments for your SQL file:

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

## Install MySQL 8.0 on Ubuntu 20.04 LTS

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

## Connect to your MySQL server:

```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

## Use “container-on-demand” to run MySQL

In the container, credentials are root/root

- Ask for container Ubuntu 20.04
- Connect via SSH
- OR connect via the Web terminal
- In the container, you should start MySQL before playing with it:

```
$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$
```

In the container, credentials are root/root

## How to import a SQL dump

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

<p align="center">
  <img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230215%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230215T084231Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9cc4ddc8cb13a4ed9612cdc48e2ae4d7c46d5f03ac9b21d278f69366af7d2e12"
       alt="CHEATSHEET SQL JOINS"
  >
</p>
