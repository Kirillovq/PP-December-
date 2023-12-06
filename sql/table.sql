CREATE TABLE client (
    id_client integer not null primary key unique,
    name varchar (20) not null unique,
    surname varchar(30) not null unique,
    number_telephone varchar(30) unique,
    address  varchar(30) unique,
    email varchar(30) unique);

CREATE TABLE executor (
    id_executor integer not null primary key unique,
    name varchar(20) not null,
    surname varchar(30) not null,
    number_telephone varchar(30) unique,
    object_management varchar(100));

CREATE TABLE ordeer (
    id_ordeer integer not null primary key unique,
    date_create date not null,
    object varchar(40),
    type_repair varchar(40),
    description_object varchar(100),
    client integer not null,
    date_end date,
    executor integer not null,
    foreign key (executor)
        references executor(id_executor)
        on delete set null on update no action,
    foreign key (client)
        references client(id_client)
        on delete set null on update no action);

