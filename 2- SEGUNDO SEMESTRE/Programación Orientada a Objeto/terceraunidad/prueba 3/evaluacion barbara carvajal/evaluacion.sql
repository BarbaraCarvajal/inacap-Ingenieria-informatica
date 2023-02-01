-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-10-2022 a las 18:26:41
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `evaluacion`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `celulares`
--

CREATE TABLE `celulares` (
  `marca` varchar(60) NOT NULL,
  `modelo` varchar(60) NOT NULL,
  `numero_serie` int(11) NOT NULL,
  `precio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `celulares`
--

INSERT INTO `celulares` (`marca`, `modelo`, `numero_serie`, `precio`) VALUES
('Xiaomi', 'redmi pro xd', 1211, 250000),
('Motorola', 'x50', 1234, 120000),
('Iphone', '14 pro', 3456, 1000000000),
('Samsung', 'Galaxy ', 5554, 450000);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `celulares`
--
ALTER TABLE `celulares`
  ADD PRIMARY KEY (`numero_serie`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
