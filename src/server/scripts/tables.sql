CREATE TABLE posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100));

CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(100),
    password VARCHAR(100),
    post_id INTEGER,
    FOREIGN KEY(post_id)
        REFERENCES posts(id)
            ON DELETE NO ACTION);

CREATE TABLE client (
    id integer not null primary key unique,
    name varchar (20) not null unique,
    surname varchar(30) not null unique,
    number_telephone varchar(30) unique,
    address  varchar(30) unique,
    email varchar(30) unique);

CREATE TABLE executor (
    id integer not null primary key unique,
    name varchar(20) not null,
    surname varchar(30) not null,
    number_telephone varchar(30) unique,
    object_management varchar(100) );

CREATE TABLE type_repair(
    id integer not null primary key unique,
    type_repair varchar(100) );

CREATE TABLE orders (
    id integer not null primary key unique,
    date_create date not null,
    object varchar(40),
    type_repair varchar(40) unique,
    description_object varchar(100),
    client integer not null,
    date_end date,
    executor integer not null,
    foreign key (executor)
        references executor(id)
        on delete set null on update no action,
    foreign key (client)
        references client(id)
        on delete set null on update no action,
    foreign key (type_repair)
        references type_repair(id)
        on delete set null on update no action );
