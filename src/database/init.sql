CREATE DATABASE IF NOT EXISTS administrator_db;

USE administrator_db;

CREATE TABLE project (
                         id INT AUTO_INCREMENT PRIMARY KEY,
                         name VARCHAR(100) NOT NULL,
                         created_at DATETIME NOT NULL,
                         updated_at DATETIME NOT NULL
);

CREATE TABLE task (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      project_id INT NOT NULL,
                      name VARCHAR(100) NOT NULL,
                      created_at DATETIME NOT NULL,
                      updated_at DATETIME NOT NULL,
                      FOREIGN KEY (project_id) REFERENCES project(id) ON DELETE CASCADE
);


-- Insertar datos de prueba en la tabla project
INSERT INTO project (name, created_at, updated_at) VALUES
                                                       ('Project Alpha', '2024-06-01 10:00:00', '2024-06-01 10:00:00'),
                                                       ('Project Beta', '2024-06-02 11:00:00', '2024-06-02 11:00:00'),
                                                       ('Project Gamma', '2024-06-03 12:00:00', '2024-06-03 12:00:00');

-- Insertar datos de prueba en la tabla task
INSERT INTO task (project_id, name, created_at, updated_at) VALUES
                                                                (1, 'Task 1 for Alpha', '2024-06-01 11:00:00', '2024-06-01 11:00:00'),
                                                                (1, 'Task 2 for Alpha', '2024-06-01 12:00:00', '2024-06-01 12:00:00'),
                                                                (2, 'Task 1 for Beta', '2024-06-02 12:00:00', '2024-06-02 12:00:00'),
                                                                (2, 'Task 2 for Beta', '2024-06-02 13:00:00', '2024-06-02 13:00:00'),
                                                                (3, 'Task 1 for Gamma', '2024-06-03 13:00:00', '2024-06-03 13:00:00'),
                                                                (3, 'Task 2 for Gamma', '2024-06-03 14:00:00', '2024-06-03 14:00:00');
