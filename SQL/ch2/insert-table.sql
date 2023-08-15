CREATE TABLE users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    level ENUM('user', 'admin') NOT NULL DEFAULT 'user',
    name VARCHAR(45) NOT NULL,
    family VARCHAR(45) NOT NULL,
    birth_date DATETIME
);

INSERT INTO users (level, name, family, birth_date)
VALUES
       (DEFAULT, 'abolfazl', 'mohajeri', '1991-08-07 00:00:00'),
       ('admin', 'nima', 'heydarinasab', '1989-03-22 00:00:00'),
       (DEFAULT, 'saleh', 'abednezhad', '1995-05-07 00:00:00');