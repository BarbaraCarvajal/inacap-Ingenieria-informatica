-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-10-2022 a las 13:02:40
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
-- Base de datos: `empresa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auto`
--

CREATE TABLE `auto` (
  `id` int(6) NOT NULL,
  `chasis` varchar(60) NOT NULL,
  `marca` varchar(15) NOT NULL,
  `modelo` varchar(15) NOT NULL,
  `cilindraje` int(4) NOT NULL,
  `precio` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auto`
--

INSERT INTO `auto` (`id`, `chasis`, `marca`, `modelo`, `cilindraje`, `precio`) VALUES
(12345, '<sha1 _hashlib.HASH object @ 0x00000209EDDCB070>', 'Hyundai', 'Oni-san', 1200, 4500000),
(54321, '<sha1 _hashlib.HASH object @ 0x000001ACD63DB010>', 'Toyota', 'Yaris E', 1200, 5000000),
(67890, '<sha1 _hashlib.HASH object @ 0x000001EBFE4B8390>', 'Peugeot', 'PT-2500', 1800, 7500000),
(246810, '<sha1 _hashlib.HASH object @ 0x0000017BE0CF9B90>', 'Susuki', 'Kawaii', 1400, 6000000);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auto`
--
ALTER TABLE `auto`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auto`
--
ALTER TABLE `auto`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=654323;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
