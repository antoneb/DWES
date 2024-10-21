DROP DATABASE IF EXISTS dbLibrosAnton;
CREATE DATABASE dbLibrosAnton;
USE dbLibrosAnton;
CREATE TABLE tUsuarios (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    apell VARCHAR(50),
    email VARCHAR(200) UNIQUE,
    pass VARCHAR(200)
);
CREATE TABLE tLibros (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100),
    imagen VARCHAR (200),
    anho YEAR,
    genero VARCHAR(200),
    autor VARCHAR(200)
);
CREATE TABLE tComentarios (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    comentario VARCHAR(2000),
    libro_id INTEGER NOT NULL,
    usuario_id INTEGER,
    FOREIGN KEY (libro_id) REFERENCES tLibros(id),
    FOREIGN KEY (usuario_id) REFERENCES tUsuarios(id)
);
INSERT INTO tLibros(titulo, imagen, autor, genero, anho)
VALUES (
        'El nombre del viento',
        'https://m.media-amazon.com/images/I/91PjnllfsxL._AC_UF894,1000_QL80_.jpg',
        'P.Rothfuss',
        'Fantasia',
        2007
    ),
    (
        'Miedo y Asco en Las Vegas',
        'https://m.media-amazon.com/images/I/81qlbvlo58L._UF1000,1000_QL80_.jpg',
        'Hunter S. Thompson',
        'Articulo',
        1971
    ),
    (
        'Hyperion',
        'https://m.media-amazon.com/images/I/91Ky9KCfAIL._UF1000,1000_QL80_.jpg',
        'Dan Simmons',
        'Ciencia Ficcion',
        1989
    ),
    (
        'Dai Dark',
        'https://content.eccediciones.com/productos/19819/sobrecubierta_dai_dark_num1_WEB.jpg',
        'Q Hayashida',
        'Manga',
        2019
    ),
    (
        'Guardias! Guardias!',
        'https://m.media-amazon.com/images/I/91di6iveLhL._AC_UF894,1000_QL80_.jpg',
        'Terry Pratchett',
        'Fantasía/Comentario Social',
        1989
    );
INSERT INTO tUsuarios(nombre, apell, email, pass)
VALUES ('Anton', 'EB', 'antoneb@mail.mail', '123'),
    ('Raul', 'PA', 'raulpa@mail.mail', '123');
INSERT INTO tComentarios(comentario, libro_id, usuario_id)
VALUES ("La mejor novela de fantasía del mundo", 1, 1),
    (
        "Famoso articulo de la revista Rolling Stone de 1971",
        2,
        1
    ),
    (
        "Primer libro de la antologia de ciencia ficcion de Dan Simmons",
        3,
        1
    ),
    (
        "El esperado nuevo manga de la autora de Dorohedoro",
        4,
        1
    ),
    (
        "Uno de los pilares fundacionales del universo del Mundodisco de Terry Pratchett",
        5,
        1
    );