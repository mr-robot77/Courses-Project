create table events(
    id bigint unsigned auto_increment primary key,
    name varchar(255),
    description text,
    date datetime,
    created_at datetime default current_timestamp
);

create table event_user(
    user_id bigint unsigned,
    event_id bigint unsigned,
    foreign key (user_id) references users(id) on delete cascade,
    foreign key (event_id) references events(id)
);