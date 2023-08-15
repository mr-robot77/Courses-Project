create table users (
id bigint unsigned primary key auto_increment,
name varchar(255),
family varchar(255),
email varchar(50),
password varchar(255),
created_at datetime default current_timestamp
);