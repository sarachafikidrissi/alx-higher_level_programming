-- create a database
-- create a table where it's id can't be null, unique, autogenarated
-- and primary key, and name can't be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL);
