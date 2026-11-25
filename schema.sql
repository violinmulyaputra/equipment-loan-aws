-- Database
CREATE DATABASE IF NOT EXISTS loanapp;
USE loanapp;

-- Table
CREATE TABLE IF NOT EXISTS equipment (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  status VARCHAR(20) DEFAULT 'available',
  borrower VARCHAR(100)
);

-- Seed
INSERT INTO equipment (name) VALUES ('Proyektor');
SELECT * FROM equipment;
