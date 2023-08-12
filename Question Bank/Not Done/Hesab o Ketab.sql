-- Section1
SELECT * FROM Customers WHERE CustomerName LIKE 'A%' ORDER BY CustomerName ASC;

-- Section2
DELETE FROM Customers 
WHERE Country IN (
    SELECT Country 
    FROM Customers 
    GROUP BY Country 
    HAVING COUNT(DISTINCT CustomerID) < 5
);

-- Section3
SELECT DISTINCT CustomerName 
FROM Customers c JOIN Orders o ON c.CustomerID = o.CustomerID 
WHERE EXISTS (
    SELECT *
    FROM OrderDetails od JOIN Products p ON od.ProductID = p.ProductID
    WHERE od.OrderID = o.OrderID AND p.Price <= ALL(
        SELECT Price FROM Products ORDER BY Price LIMIT 5)
)
ORDER BY CustomerName ASC;

-- Section4
SELECT ProductID, SUM(Quantity) AS Sales
FROM OrderDetails od JOIN Orders o ON od.OrderID = o.OrderId  
WHERE OrderDate BETWEEN DATE_FORMAT(NOW() ,'%Y-%m-01') AND LAST_DAY(NOW())
GROUP BY ProductId  
ORDER BY Sales DESC  
LIMIT 10;