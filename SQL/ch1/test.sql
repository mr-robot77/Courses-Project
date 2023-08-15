create database test;
use test;

create table users (
    id bigint(20) unsigned auto_increment primary key,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    biography longtext,
    role enum('user','admin') not null default 'user',
    created_at timestamp default current_timestamp
);

CREATE TABLE hospital (
    ProviderNumber INT(11),
    HospitalName VARCHAR(100),
    Address1 TEXT,
    City VARCHAR(100),
    State VARCHAR(100),
    ZipCode VARCHAR(20),
    HospitalOwner VARCHAR(100)
)

LOAD DATA LOCAL INFILE 'CSV_FILE_PATH'
INTO TABLE hospital
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(ProviderNumber, HospitalName, Address1, City, State, ZipCode, HospitalOwner)

describe  users;

drop table users;

drop table if exists users;

show tables;

alter table users rename to old_users;

alter table old_users rename to users;

alter table users change column biography bio longtext;
alter table users rename column bio to biography;
alter table users drop column biography;
alter table users add column biography longtext after last_name;

drop table if exists posts;

create table posts (
    id bigint unsigned auto_increment primary key,
    user_id bigint unsigned,
    title varchar(255) not null,
    body longtext not null,
    created_at timestamp default current_timestamp,
    foreign key (user_id) references users(id)
                   on delete cascade
                   on update cascade
);
