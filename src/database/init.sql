CREATE DATABASE IF NOT EXISTS administrator_db;

USE administrator_db;

CREATE TABLE Project (
                         id INT AUTO_INCREMENT PRIMARY KEY,
                         name VARCHAR(100) NOT NULL,
                         created_at DATETIME NOT NULL,
                         updated_at DATETIME NOT NULL
);

CREATE TABLE Task (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      project_id INT NOT NULL,
                      name VARCHAR(100) NOT NULL,
                      created_at DATETIME NOT NULL,
                      updated_at DATETIME NOT NULL,
                      FOREIGN KEY (project_id) REFERENCES Project(id) ON DELETE CASCADE
);
