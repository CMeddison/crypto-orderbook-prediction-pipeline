-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: kucoin_orderbook
-- ------------------------------------------------------
-- Server version	8.0.41



--
-- Table structure for table `order_book`
--


CREATE TABLE `order_book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `timestamp` datetime DEFAULT CURRENT_TIMESTAMP,
  `order_type` enum('buy','sell') DEFAULT NULL,
  `price` decimal(18,8) DEFAULT NULL,
  `amount` decimal(18,8) DEFAULT NULL,
  `total` decimal(18,8) DEFAULT NULL,
  `best_bid_price` decimal(18,8) DEFAULT NULL,
  `best_ask_price` decimal(18,8) DEFAULT NULL,
  `bid_ask_spread` decimal(18,8) DEFAULT NULL,
  `total_bid_volume` decimal(18,8) DEFAULT NULL,
  `total_ask_volume` decimal(18,8) DEFAULT NULL,
  `volume_imbalance` decimal(18,8) DEFAULT NULL,
  `mid_price` decimal(18,8) DEFAULT NULL,
  `price_movement` decimal(18,8) DEFAULT NULL,
  `price_movement_pct` double DEFAULT NULL,
  `last_price` decimal(18,8) DEFAULT '0.00000000',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1976499 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- Dump completed on 2025-04-13  0:07:01
