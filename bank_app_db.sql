create database if not exists banking_db;
use banking_db;
create table if not exists banking_app_tb (Code varchar(10), Name varchar(10), Amount bigint default 0);