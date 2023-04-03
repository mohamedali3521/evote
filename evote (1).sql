-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 23, 2023 at 07:33 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `evote`
--

-- --------------------------------------------------------

--
-- Table structure for table `addcandidate`
--

CREATE TABLE `addcandidate` (
  `id` int(11) NOT NULL,
  `candidatename` varchar(25) NOT NULL,
  `partyname` varchar(50) NOT NULL,
  `cityname` varchar(15) NOT NULL,
  `electiontype` varchar(25) NOT NULL,
  `partylogo` varchar(50) NOT NULL,
  `candidatephoto` varchar(50) NOT NULL,
  `aadharphoto` varchar(50) NOT NULL,
  `vote` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addcandidate`
--

INSERT INTO `addcandidate` (`id`, `candidatename`, `partyname`, `cityname`, `electiontype`, `partylogo`, `candidatephoto`, `aadharphoto`, `vote`) VALUES
(5, 'Yogesh', 'victory', 'tanjore', 'General Election', 'homepage.png', 'viewcandidate.png', 'usermodules.png', 3),
(8, 'harrish', 'jghjm', 'trichy', 'State Assembly ', 'line.png', 'login.png', 'addc.png', 0),
(9, 'harrish', 'hello', 'tanjore', 'General Election', 'login.png', 'login.png', 'login.png', 12);

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `aadharno` varchar(12) NOT NULL,
  `username` varchar(50) NOT NULL,
  `age` int(3) NOT NULL,
  `city` varchar(50) NOT NULL,
  `phoneno` varchar(10) NOT NULL,
  `password` varchar(16) NOT NULL,
  `file` varchar(200) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `aadharno`, `username`, `age`, `city`, `phoneno`, `password`, `file`, `status`) VALUES
(10, '123456789123', 'yogesh', 22, 'tanjore', '8525001254', '12345678', 'Screenshot 2023-02-26 204713.png', 'VOTED'),
(9, '123456789124', 'harrish', 22, 'tanjore', '8525001254', 'ffhgcghfjfj', 'login.png', 'APPROVED'),
(11, '336034968828', 'harrish', 22, 'tanjore', '8525001254', 'hhhhhhhh', 'login.png', 'VOTED'),
(12, '336730968811', 'harrish', 22, 'chennai', '8525944374', 'hhhhhhhh', 'Screenshot 2023-03-17 040551.png', 'APPROVED');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addcandidate`
--
ALTER TABLE `addcandidate`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`aadharno`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addcandidate`
--
ALTER TABLE `addcandidate`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
