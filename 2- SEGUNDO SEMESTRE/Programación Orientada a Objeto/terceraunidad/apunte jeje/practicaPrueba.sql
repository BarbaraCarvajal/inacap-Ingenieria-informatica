-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 27-10-2022 a las 05:18:44
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `practicaPrueba`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `automovilesPrueba`
--

CREATE TABLE `automovilesPrueba` (
  `marca` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `chasis` int(11) NOT NULL,
  `cilindrado` int(11) NOT NULL,
  `precio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `automovilesPrueba`
--

INSERT INTO `automovilesPrueba` (`marca`, `modelo`, `chasis`, `cilindrado`, `precio`) VALUES
('mercedes', '3000', 1111, 200, 20000000);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `automovilesPrueba`
--
ALTER TABLE `automovilesPrueba`
  ADD PRIMARY KEY (`chasis`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
