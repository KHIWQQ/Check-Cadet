-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2022 at 10:19 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `check_cadet`
--

-- --------------------------------------------------------

--
-- Table structure for table `batt`
--

CREATE TABLE `batt` (
  `lname` varchar(255) NOT NULL,
  `uname` varchar(255) DEFAULT NULL,
  `stay` int(11) DEFAULT NULL,
  `outc` int(11) DEFAULT NULL,
  `com` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `batt`
--

INSERT INTO `batt` (`lname`, `uname`, `stay`, `outc`, `com`) VALUES
('a', 'X', 0, 1, 1),
('AA', 'AA', 1, 0, 2),
('Kaa\n', 'Fah', 1, 0, 3),
('Kubb', 'Ing', 1, 0, 2),
('Na', 'Eak', 1, 0, 1),
('Q', 'Q', 0, 1, 1),
('Traisiwakul', 'Parinya', 0, 1, 3),
('Yz', 'X', 0, 1, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `batt`
--
ALTER TABLE `batt`
  ADD PRIMARY KEY (`lname`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
