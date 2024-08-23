-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2024-08-23 08:23:05
-- 伺服器版本： 10.4.24-MariaDB
-- PHP 版本： 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫: `test`
--

-- --------------------------------------------------------

--
-- 資料表結構 `staff_info`
--

CREATE TABLE `staff_info` (
  `sf_pk` int(11) NOT NULL,
  `sf_name` varchar(16) COLLATE utf8_unicode_ci NOT NULL,
  `sf_account` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `sf_pwd` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `sf_level` varchar(15) COLLATE utf8_unicode_ci NOT NULL DEFAULT '0',
  `create_user` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `create_time` datetime NOT NULL DEFAULT current_timestamp(),
  `update_user` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `update_time` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `sf_del` int(1) NOT NULL DEFAULT 0 COMMENT '0=正常/1=刪除'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 傾印資料表的資料 `staff_info`
--

INSERT INTO `staff_info` (`sf_pk`, `sf_name`, `sf_account`, `sf_pwd`, `sf_level`, `create_user`, `create_time`, `update_user`, `update_time`, `sf_del`) VALUES
(1, 'Albert', 'albertet24', 'sahtysle24', '2', 'albertet24', '2024-07-10 13:59:53', 'system', '2024-07-25 22:29:10', 0),
(2, 'Ares', 'albertet15', 'sahtysle15', '0', 'albertet15', '2024-07-10 14:01:35', 'system', '2024-07-10 14:01:35', 0),
(3, 'Ares1', 'albertet1', 'sahtysle1', '0', 'albertet1', '2024-07-10 14:01:35', 'system', '2024-07-10 14:01:35', 0),
(4, 'Ares2', 'albertet2', 'sahtysle2', '0', 'albertet2', '2024-07-10 14:01:35', 'system', '2024-07-10 14:01:35', 0),
(5, 'Ares3', 'albertet3', 'sahtysle3', '0', 'albertet3', '2024-07-10 14:01:35', 'system', '2024-07-10 14:01:35', 0),
(6, 'Ares4', 'albertet4', 'sahtysle4', '0', 'albertet4', '2024-07-10 14:01:35', 'system', '2024-07-10 14:01:35', 0),
(7, 'ally', 'ally123', 'ssll123', '0', 'ally123', '2024-07-11 22:33:07', 'SYSTEM', '2024-07-11 22:33:07', 0),
(8, 'Chloe', 'chloe0702', '11223', '0', 'chloe0702', '2024-07-11 22:36:09', 'SYSTEM', '2024-07-11 22:36:09', 0),
(33, '2', '0', '000', '3', '0', '2024-07-26 15:21:55', 'SYSTEM', '2024-07-26 15:24:53', 0),
(40, '456', '123', '321', '1', '123', '2024-07-26 16:09:41', 'SYSTEM', '2024-07-26 16:13:42', 0);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `staff_info`
--
ALTER TABLE `staff_info`
  ADD PRIMARY KEY (`sf_pk`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `staff_info`
--
ALTER TABLE `staff_info`
  MODIFY `sf_pk` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
