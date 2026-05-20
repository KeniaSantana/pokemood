-- --------------------------------------------------------
-- TABLA estado_animo
-- --------------------------------------------------------

CREATE TABLE estado_animo (

    id_estado INT AUTO_INCREMENT PRIMARY KEY,

    nombre_estado VARCHAR(50) NOT NULL,

    descripcion TEXT

);

-- --------------------------------------------------------
-- TABLA pokemon
-- --------------------------------------------------------

CREATE TABLE pokemon (

    id_pokemon INT AUTO_INCREMENT PRIMARY KEY,

    nombre VARCHAR(50) NOT NULL,

    numero_pokedex INT NOT NULL,

    tipo VARCHAR(50),

    rareza VARCHAR(50),

    descripcion TEXT,

    motivo_asignacion TEXT,

    id_estado INT,

    FOREIGN KEY (id_estado)
    REFERENCES estado_animo(id_estado)

);

-- --------------------------------------------------------
-- TABLA usuario
-- --------------------------------------------------------

CREATE TABLE usuario (

    id_usuario INT AUTO_INCREMENT PRIMARY KEY,

    nombre VARCHAR(100) NOT NULL,

    correo VARCHAR(100) NOT NULL UNIQUE,

    contraseña VARCHAR(255) NOT NULL

);

-- --------------------------------------------------------
-- TABLA historial
-- --------------------------------------------------------

CREATE TABLE historial (

    id_historial INT AUTO_INCREMENT PRIMARY KEY,

    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,

    id_usuario INT,

    id_estado INT,

    id_pokemon INT,

    FOREIGN KEY (id_usuario)
    REFERENCES usuario(id_usuario),

    FOREIGN KEY (id_estado)
    REFERENCES estado_animo(id_estado),

    FOREIGN KEY (id_pokemon)
    REFERENCES pokemon(id_pokemon)

);

-- --------------------------------------------------------
-- INSERTAR USUARIO
-- --------------------------------------------------------

INSERT INTO usuario (

    nombre,
    correo,
    contraseña

)

VALUES (

    'Kenia Santana',
    '23308060610371@cetis61.edu.mx',
    '123456'

);