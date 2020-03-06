-- Creates database <[app-lower]>_dev_db
CREATE DATABASE IF NOT EXISTS <[app-lower]>_dev_db;
USE <[app-lower]>_dev_db;
CREATE USER IF NOT EXISTS '<[app-lower]>_dev'@'localhost' IDENTIFIED BY '<[app-lower]>_dev_pwd';
GRANT ALL ON <[app-lower]>_dev_db.* TO '<[app-lower]>_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO '<[app-lower]>_dev'@'localhost';
