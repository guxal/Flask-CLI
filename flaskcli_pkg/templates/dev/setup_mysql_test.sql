-- Creates database <[app-lower]>_test_db
CREATE DATABASE IF NOT EXISTS <[app-lower]>_test_db;
USE <[app-lower]>_test_db;
CREATE USER IF NOT EXISTS '<[app-lower]>_test'@'localhost' IDENTIFIED BY '<[app-lower]>_test_pwd';
GRANT ALL PRIVILEGES ON <[app-lower]>_test_db.* TO '<[app-lower]>_test'@'localhost';
GRANT SELECT ON performance_schema.* TO '<[app-lower]>_test'@'localhost';
