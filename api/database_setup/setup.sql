DROP DATABASE IF EXISTS general;
CREATE DATABASE IF NOT EXISTS general;
USE general;

CREATE TABLE IF NOT EXISTS `users` (
    `id` int(10) NOT NULL  AUTO_INCREMENT,
    `name` varchar(50) DEFAULT NULL,
    `hash` varchar(82),
    PRIMARY KEY (`id`),
    UNIQUE (`name`),
    INDEX (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `test` (
    `id` int(10) NOT NULL AUTO_INCREMENT,
    `fk_name` varchar(50) DEFAULT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`fk_name`)
        REFERENCES `users`(`name`)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `users` (`name`) VALUES("Admin");
INSERT INTO `users` (`name`) VALUES("User1");
INSERT INTO `users` (`name`) VALUES("User2");

INSERT INTO `test` (`fk_name`) VALUES("Admin");
INSERT INTO `test` (`fk_name`) VALUES("User1");
INSERT INTO `test` (`fk_name`) VALUES("User2");
