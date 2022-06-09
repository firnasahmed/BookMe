-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 09, 2021 at 04:27 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bookme`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_information`
--

CREATE TABLE `admin_information` (
  `id` int(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `admin_information`
--

INSERT INTO `admin_information` (`id`, `name`, `username`, `password`) VALUES
(1, 'a', 'a', 'a');

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `booking_id` int(11) NOT NULL,
  `id` int(11) DEFAULT NULL,
  `vehicle_name` varchar(255) NOT NULL,
  `car_id` int(11) DEFAULT NULL,
  `van_id` int(11) DEFAULT NULL,
  `lorry_id` int(11) DEFAULT NULL,
  `truck_id` int(11) DEFAULT NULL,
  `tw_id` int(11) DEFAULT NULL,
  `day` int(11) NOT NULL,
  `month` varchar(255) NOT NULL,
  `year` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`booking_id`, `id`, `vehicle_name`, `car_id`, `van_id`, `lorry_id`, `truck_id`, `tw_id`, `day`, `month`, `year`) VALUES
(7, NULL, 'Truck', NULL, NULL, NULL, NULL, NULL, 10, 'September', 2021),
(8, NULL, 'Truck', NULL, NULL, NULL, NULL, NULL, 19, 'October', 2021);

-- --------------------------------------------------------

--
-- Table structure for table `car`
--

CREATE TABLE `car` (
  `car_id` int(6) NOT NULL,
  `car_name` varchar(255) NOT NULL,
  `car_cooler` varchar(10) NOT NULL,
  `car_count` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `car`
--

INSERT INTO `car` (`car_id`, `car_name`, `car_cooler`, `car_count`) VALUES
(3, 'Benz', 'AC', 4),
(4, 'BMW', 'AC', 4),
(5, 'Toyota', 'Non AC', 3),
(8, 'Vezzel', 'AC', 4);

-- --------------------------------------------------------

--
-- Table structure for table `lorry`
--

CREATE TABLE `lorry` (
  `lorry_id` int(6) NOT NULL,
  `lorry_name` varchar(255) NOT NULL,
  `lorry_load` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `lorry`
--

INSERT INTO `lorry` (`lorry_id`, `lorry_name`, `lorry_load`) VALUES
(1, 'Buddy Lorry', 2500),
(2, 'AVG Lorry', 3500),
(4, 'ASAS', 2500);

-- --------------------------------------------------------

--
-- Table structure for table `threewheel`
--

CREATE TABLE `threewheel` (
  `tw_id` int(6) NOT NULL,
  `tw_name` varchar(255) NOT NULL,
  `tw_count` int(4) NOT NULL DEFAULT 3
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `threewheel`
--

INSERT INTO `threewheel` (`tw_id`, `tw_name`, `tw_count`) VALUES
(1, 'Bajaj 4ST', 3),
(2, 'TVS King', 3),
(3, 'Piaggio', 3);

-- --------------------------------------------------------

--
-- Table structure for table `truck`
--

CREATE TABLE `truck` (
  `truck_id` int(6) NOT NULL,
  `truck_name` varchar(255) NOT NULL,
  `truck_size` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `truck`
--

INSERT INTO `truck` (`truck_id`, `truck_name`, `truck_size`) VALUES
(1, 'Tow Truck', 7),
(2, 'Tracktor', 12),
(3, 'Troo', 12);

-- --------------------------------------------------------

--
-- Table structure for table `user_information`
--

CREATE TABLE `user_information` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `age` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_information`
--

INSERT INTO `user_information` (`id`, `first_name`, `last_name`, `age`, `gender`, `city`, `address`, `username`, `password`) VALUES
(15, 'Firnas', 'Ahamed', '23', '', 'Kandy', 'Gelioya', 'findy', '123456'),
(16, 'a', 'b', '719', '', 'a', 'a', 'a', 'a');

-- --------------------------------------------------------

--
-- Table structure for table `van`
--

CREATE TABLE `van` (
  `van_id` int(4) NOT NULL,
  `van_name` varchar(255) NOT NULL,
  `van_cooler` varchar(10) NOT NULL,
  `van_count` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `van`
--

INSERT INTO `van` (`van_id`, `van_name`, `van_cooler`, `van_count`) VALUES
(1, 'KDH', 'AC', 8),
(2, 'Buddy', 'Non AC', 6),
(4, 'Dolphin', 'Non AC', 8);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_information`
--
ALTER TABLE `admin_information`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`booking_id`),
  ADD KEY `id` (`id`),
  ADD KEY `car_id` (`car_id`),
  ADD KEY `lorry_id` (`lorry_id`),
  ADD KEY `truck_id` (`truck_id`),
  ADD KEY `tw_id` (`tw_id`),
  ADD KEY `van_id` (`van_id`);

--
-- Indexes for table `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`car_id`);

--
-- Indexes for table `lorry`
--
ALTER TABLE `lorry`
  ADD PRIMARY KEY (`lorry_id`);

--
-- Indexes for table `threewheel`
--
ALTER TABLE `threewheel`
  ADD PRIMARY KEY (`tw_id`);

--
-- Indexes for table `truck`
--
ALTER TABLE `truck`
  ADD PRIMARY KEY (`truck_id`);

--
-- Indexes for table `user_information`
--
ALTER TABLE `user_information`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `van`
--
ALTER TABLE `van`
  ADD PRIMARY KEY (`van_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_information`
--
ALTER TABLE `admin_information`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `car`
--
ALTER TABLE `car`
  MODIFY `car_id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `lorry`
--
ALTER TABLE `lorry`
  MODIFY `lorry_id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `threewheel`
--
ALTER TABLE `threewheel`
  MODIFY `tw_id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `truck`
--
ALTER TABLE `truck`
  MODIFY `truck_id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user_information`
--
ALTER TABLE `user_information`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `van`
--
ALTER TABLE `van`
  MODIFY `van_id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bookings`
--
ALTER TABLE `bookings`
  ADD CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user_information` (`id`),
  ADD CONSTRAINT `bookings_ibfk_2` FOREIGN KEY (`car_id`) REFERENCES `car` (`car_id`),
  ADD CONSTRAINT `bookings_ibfk_3` FOREIGN KEY (`lorry_id`) REFERENCES `lorry` (`lorry_id`),
  ADD CONSTRAINT `bookings_ibfk_4` FOREIGN KEY (`truck_id`) REFERENCES `truck` (`truck_id`),
  ADD CONSTRAINT `bookings_ibfk_5` FOREIGN KEY (`tw_id`) REFERENCES `threewheel` (`tw_id`),
  ADD CONSTRAINT `bookings_ibfk_6` FOREIGN KEY (`van_id`) REFERENCES `van` (`van_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
