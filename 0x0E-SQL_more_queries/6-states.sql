-- Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on MySQL server.
-- states description:
--              id INT unique, auto generated, can’t be null and is a primary key
--              name VARCHAR(256) can’t be null
-- Script does not fail if the database hbtn_0d_usa already exist.
-- Script does not fail if the table states already exist.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256));