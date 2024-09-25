create database VIRTUAL_ART_GALLERY;
use VIRTUAL_ART_GALLERY;

-- Create the Artists table
CREATE TABLE Artists (
 ArtistID INT PRIMARY KEY,
 Name VARCHAR(255) NOT NULL,
 Biography TEXT,
 Nationality VARCHAR(100)); -- Create the Categories table
CREATE TABLE Categories (
 CategoryID INT PRIMARY KEY,
 Name VARCHAR(100) NOT NULL); -- Create the Artworks table
CREATE TABLE Artworks (
 ArtworkID INT PRIMARY KEY,
 Title VARCHAR(255) NOT NULL,
 ArtistID INT,
 CategoryID INT,
 Year INT,
 Description TEXT,
 ImageURL VARCHAR(255),
 FOREIGN KEY (ArtistID) REFERENCES Artists (ArtistID),
 FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)); -- Create the Exhibitions table
CREATE TABLE Exhibitions (
 ExhibitionID INT PRIMARY KEY,
 Title VARCHAR(255) NOT NULL,
 StartDate DATE,
 EndDate DATE,
 Description TEXT); -- Create a table to associate artworks with exhibitions
CREATE TABLE ExhibitionArtworks (
 ExhibitionID INT,
 ArtworkID INT,
 PRIMARY KEY (ExhibitionID, ArtworkID),
 FOREIGN KEY (ExhibitionID) REFERENCES Exhibitions (ExhibitionID),
 FOREIGN KEY (ArtworkID) REFERENCES Artworks (ArtworkID));

 -- Insert sample data into the Artists table
INSERT INTO Artists (ArtistID, Name, Biography, Nationality) VALUES
 (1, 'Pablo Picasso', 'Renowned Spanish painter and sculptor.', 'Spanish'),
 (2, 'Vincent van Gogh', 'Dutch post-impressionist painter.', 'Dutch'),
 (3, 'Leonardo da Vinci', 'Italian polymath of the Renaissance.', 'Italian');
-- Insert sample data into the Categories table
INSERT INTO Categories (CategoryID, Name) VALUES
 (1, 'Painting'),
 (2, 'Sculpture'),
 (3, 'Photography');

 -- Insert sample data into the Artworks table
INSERT INTO Artworks (ArtworkID, Title, ArtistID, CategoryID, Year, Description, ImageURL) VALUES
 (1, 'Starry Night', 2, 1, 1889, 'A famous painting by Vincent van Gogh.', 'starry_night.jpg'),
 (2, 'Mona Lisa', 3, 1, 1503, 'The iconic portrait by Leonardo da Vinci.', 'mona_lisa.jpg'),
 (3, 'Guernica', 1, 1, 1937, 'Pablo Picassos powerful anti-war mural.', 'guernica.jpg'); -- Insert sample data into the Exhibitions table
INSERT INTO Exhibitions (ExhibitionID, Title, StartDate, EndDate, Description) VALUES
 (1, 'Modern Art Masterpieces', '2023-01-01', '2023-03-01', 'A collection of modern art masterpieces.'),
 (2, 'Renaissance Art', '2023-04-01', '2023-06-01', 'A showcase of Renaissance art treasures.');

 -- Insert artworks into exhibitions
INSERT INTO ExhibitionArtworks (ExhibitionID, ArtworkID) VALUES
 (1, 1),
 (1, 2),
 (1, 3),
 (2, 2);

 --Quereys

 --1

SELECT * FROM Artists;
SELECT * FROM	ExhibitionArtworks;
SELECT * FROM Artworks;

SELECT a.Name , COUNT(b.ArtworkID) AS NumberOfArtworks
FROM Artists a , Artworks b
WHERE a.ArtistID = b.ArtistID
GROUP BY a.Name
ORDER BY NumberOfArtworks DESC;

--2

SELECT a.Title ,a.Year, b.Name , b.Nationality 

FROM Artworks a , Artists b
WHERE a.ArtistID = b.ArtistID
AND b.Nationality = 'Dutch' OR b.Nationality = 'Spanish'
ORDER BY a.Year;

--3

SELECT a.Name , b.Name , COUNT(b.CategoryID) AS NumberOfArtWork
FROM Artists a , Categories b , Artworks c
WHERE b.CategoryID = c.CategoryID
AND c.ArtistID = a.ArtistID
AND b.Name = 'Painting'
GROUP BY a.Name,b.Name;

--4

SELECT a.Name AS Artist ,e.Title AS ArtName, b.Name AS Category , c.Title
FROM Artists a , Categories b , Exhibitions c , ExhibitionArtworks d ,Artworks e
WHERE c.ExhibitionID = d.ExhibitionID
AND d.ArtworkID = e.ArtworkID
AND e.ArtistID = a.ArtistID
AND e.CategoryID = b.CategoryID
AND c.Title = 'Modern Art Masterpieces';

--5

SELECT  a.Name , COUNT(b.ArtworkID) AS NumberOfArtWork
FROM Artists a , ExhibitionArtworks b , Artworks c 
WHERE b.ArtworkID = c.ArtworkID
AND a.ArtistID = c.ArtistID
 
GROUP BY a.Name 
HAVING COUNT(b.ArtworkID) > 2 ;

--6

SELECT b.Title AS ArtworkTitle
FROM Artworks b
JOIN ExhibitionArtworks c ON b.ArtworkID = c.ArtworkID
JOIN Exhibitions a ON c.ExhibitionID = a.ExhibitionID
WHERE a.Title = 'Modern Art Masterpieces'
AND b.ArtworkID IN (
    SELECT b2.ArtworkID
    FROM Artworks b2
    JOIN ExhibitionArtworks c2 ON b2.ArtworkID = c2.ArtworkID
    JOIN Exhibitions a2 ON c2.ExhibitionID = a2.ExhibitionID
    WHERE a2.Title = 'Renaissance Art'
);

--7

SELECT b.Name , COUNT(a.CategoryID) Category 
FROM Categories b
LEFT JOIN Artworks a ON a.CategoryID = b.CategoryID
GROUP BY b.Name;

--8

SELECT a.Name AS Artist_Name , COUNT(b.ArtworkID) AS NumberOfArt
FROM Artists a , Artworks b
WHERE a.ArtistID = b.ArtistID
GROUP BY  a.Name
HAVING COUNT(b.ArtworkID) >3

--9

SELECT a.Name AS Artist_Name , a.Nationality , b.Title
FROM Artists a , Artworks b
WHERE a.ArtistID = b.ArtistID
AND a.Nationality = 'Spanish';

--10

SELECT e.Title AS ExhibitionTitle
FROM Exhibitions e
JOIN ExhibitionArtworks ea ON e.ExhibitionID = ea.ExhibitionID
JOIN Artworks a ON ea.ArtworkID = a.ArtworkID
JOIN Artists ar ON a.ArtistID = ar.ArtistID
WHERE ar.Name = 'Vincent van Gogh'
AND e.ExhibitionID IN (
    SELECT e2.ExhibitionID
    FROM Exhibitions e2
    JOIN ExhibitionArtworks ea2 ON e2.ExhibitionID = ea2.ExhibitionID
    JOIN Artworks a2 ON ea2.ArtworkID = a2.ArtworkID
    JOIN Artists ar2 ON a2.ArtistID = ar2.ArtistID
    WHERE ar2.Name = 'Leonardo da Vinci'
);

--11

SELECT Title AS ArtworkTitle
FROM Artworks
WHERE ArtworkID NOT IN (
    SELECT ArtworkID
    FROM ExhibitionArtworks
);

--12

SELECT a.Name as ArtistName , COUNT(b.CategoryID) AS CategoriesPresent
FROM  Artists a , Categories b , Artworks c
WHERE a.ArtistID = c.ArtistID
AND b.CategoryID = c.CategoryID
GROUP BY a.Name
HAVING COUNT(b.CategoryID)=3

--13
SELECT a.Name , count(b.ArtworkID) AS TotalNumberOfArtwork

FROM Categories a left join Artworks b on a.CategoryID= b.CategoryID
GROUP BY a.Name;

--14
SELECT a.Name AS Artist , COUNT(b.ArtworkID)
FROM Artists a , Artworks b
WHERE a.ArtistID = b.ArtistID
GROUP BY  a.Name
HAVING COUNT(b.ArtworkID)=2;

--15
SELECT c.Name AS CategoryName, AVG(a.Year) AS AverageYear
FROM Categories c
JOIN Artworks a ON c.CategoryID = a.CategoryID
GROUP BY c.CategoryID, c.Name
HAVING COUNT(a.ArtworkID) > 1;

--16
SELECT  ar.Title , e.Title AS Exhibittion
FROM Artworks ar , Exhibitions e , ExhibitionArtworks ea
WHERE e.ExhibitionID = ea.ExhibitionID
AND ea.ArtworkID = ar.ArtworkID
AND e.Title = 'Modern Art Masterpieces' ;

--17
SELECT c.Name AS CategoryName, AVG(a.Year) AS AverageCategoryYear
FROM Categories c
JOIN Artworks a ON c.CategoryID = a.CategoryID
GROUP BY c.Name
HAVING AVG(a.Year) > (SELECT AVG(Year) FROM Artworks);

--18
SELECT * 
FROM Artworks a
WHERE a.ArtworkID
NOT IN (SELECT ea.ArtworkID FROM ExhibitionArtworks ea);

--19
SELECT a.Name , b.Title
FROM Artists a , Artworks b
WHERE a.ArtistID = b.ArtistID 
AND b.Title = 'Mona lisa';

--20
SELECT a.Name , COUNT(ar.ArtworkID) AS Number_OF_ART
FROM Artists a , Artworks ar
WHERE a.ArtistID = ar.ArtistID
GROUP BY a.Name;