DROP DATABASE kapperapp;
DROP USER 'kapper'@'localhost';

CREATE DATABASE kapperapp;

USE kapperapp;

CREATE USER 'kapper'@'localhost' IDENTIFIED BY '0123';
GRANT ALL PRIVILEGES ON * . * TO 'kapper'@'localhost';

CREATE TABLE klant (
  id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, 
  naam VARCHAR(256) NOT NULL,
  email VARCHAR(256) NOT NULL,
  telefoon VARCHAR(11) NOT NULL,
  behandeling VARCHAR(256) NOT NULL,
  tijdstip DATETIME NOT NULL
);



