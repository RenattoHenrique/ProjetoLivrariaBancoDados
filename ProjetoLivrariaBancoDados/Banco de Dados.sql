CREATE DATABASE IF NOT EXISTS livraria;
USE livraria;

CREATE TABLE IF NOT EXISTS livro
(
id int auto_increment primary key,
titulo varchar(80) not null,
genero varchar(50) not null,
autor varchar(80) not null,
publicacao date not null,
sinopse varchar(600) not null,
valor_compra float not null,
valor_revenda float not null
);


CREATE TABLE IF NOT EXISTS cliente
(
id int auto_increment primary key,
nome varchar(70) not null,
telefone varchar(11) not null,
email varchar(100) not null
);

CREATE TABLE IF NOT EXISTS venda
(
id int auto_increment primary key,
data_venda date not null,
quantidade int not null,
id_cliente int,
id_livro int,
lucro float not null,
FOREIGN KEY(id_cliente) REFERENCES cliente(id) ON DELETE CASCADE,
FOREIGN KEY(id_livro) REFERENCES livro(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS compra
(
id int auto_increment primary key,
id_livro int,
quantidade int not null,
data_compra date not null,
custo float not null,
foreign key(id_livro) references livro(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS avaliacao
(
id int auto_increment primary key,
comentario varchar(300) not null,
data_avaliacao date not null,
nota int(2) not null,
id_livro int,
id_cliente int,
foreign key(id_livro) references livro(id) ON DELETE CASCADE,
foreign key(id_cliente) references cliente(id) ON DELETE CASCADE
);

create table if not exists estoque
(
id_livro int,
quantidade int not null,
foreign key(id_livro) references livro(id) on delete cascade,
primary key(id_livro)
);