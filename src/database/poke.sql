-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.28-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.15.0.7171
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para poke
CREATE DATABASE IF NOT EXISTS `poke` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `poke`;

-- Volcando estructura para tabla poke.estado_animo
CREATE TABLE IF NOT EXISTS `estado_animo` (
  `id_estado` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_estado` varchar(50) NOT NULL,
  `descripcion` text DEFAULT NULL,
  PRIMARY KEY (`id_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla poke.estado_animo: ~5 rows (aproximadamente)
INSERT INTO `estado_animo` (`id_estado`, `nombre_estado`, `descripcion`) VALUES
	(1, 'Feliz', 'Estado de alegría'),
	(2, 'Triste', 'Estado de tristeza'),
	(3, 'Enojado', 'Estado de enojo'),
	(4, 'Ansioso', 'Estado de ansiedad'),
	(5, 'Relajado', 'Estado de calma');

-- Volcando estructura para tabla poke.historial
CREATE TABLE IF NOT EXISTS `historial` (
  `id_historial` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime DEFAULT current_timestamp(),
  `id_usuario` int(11) DEFAULT NULL,
  `id_estado` int(11) DEFAULT NULL,
  `id_pokemon` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_historial`),
  KEY `id_usuario` (`id_usuario`),
  KEY `id_estado` (`id_estado`),
  KEY `id_pokemon` (`id_pokemon`),
  CONSTRAINT `historial_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`),
  CONSTRAINT `historial_ibfk_2` FOREIGN KEY (`id_estado`) REFERENCES `estado_animo` (`id_estado`),
  CONSTRAINT `historial_ibfk_3` FOREIGN KEY (`id_pokemon`) REFERENCES `pokemon` (`id_pokemon`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla poke.historial: ~0 rows (aproximadamente)

-- Volcando estructura para tabla poke.pokemon
CREATE TABLE IF NOT EXISTS `pokemon` (
  `id_pokemon` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `numero_pokedex` int(11) NOT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `rareza` varchar(50) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `motivo_asignacion` text DEFAULT NULL,
  `id_estado` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_pokemon`),
  KEY `id_estado` (`id_estado`),
  CONSTRAINT `pokemon_ibfk_1` FOREIGN KEY (`id_estado`) REFERENCES `estado_animo` (`id_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla poke.pokemon: ~0 rows (aproximadamente)

-- Volcando estructura para tabla poke.usuario
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `correo` (`correo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla poke.usuario: ~1 rows (aproximadamente)
INSERT INTO `usuario` (`id_usuario`, `nombre`, `correo`, `contraseña`) VALUES
	(1, 'Kenia Santana', '23308060610371@cetis61.edu.mx', '123456');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
