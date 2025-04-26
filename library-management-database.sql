-- Create Database
CREATE DATABASE IF NOT EXISTS LibraryDB;
USE LibraryDB;

-- Authors Table
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE
);

-- Books Table
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    ISBN VARCHAR(20) UNIQUE NOT NULL,
    AuthorID INT,
    PublishedYear INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

-- Members Table
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15)
);

-- BorrowRecords Table (Many-to-Many between Members and Books)
CREATE TABLE BorrowRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,
    MemberID INT,
    BookID INT,
    BorrowDate DATE NOT NULL,
    ReturnDate DATE,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID)
);

-- Insert sample data into Authors
INSERT INTO Authors (Name, Email) VALUES
('George Orwell', 'orwell@example.com'),
('Jane Austen', 'austen@example.com');

-- Insert sample data into Books
INSERT INTO Books (Title, ISBN, AuthorID, PublishedYear) VALUES
('1984', '978-0451524935', 1, 1949),
('Pride and Prejudice', '978-1503290563', 2, 1813);

-- Insert sample data into Members
INSERT INTO Members (FullName, Email, Phone) VALUES
('John Doe', 'john@example.com', '1234567890'),
('Alice Smith', 'alice@example.com', '0987654321');

-- Insert sample data into BorrowRecords
INSERT INTO BorrowRecords (MemberID, BookID, BorrowDate) VALUES
(1, 1, '2025-04-01'),
(2, 2, '2025-04-02');
