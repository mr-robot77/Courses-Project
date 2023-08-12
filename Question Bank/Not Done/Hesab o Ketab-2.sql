-- Section1
SELECT * 
FROM Customers 
WHERE CustomerName LIKE 'A%' 
ORDER BY CustomerName ASC;
-- Section2
DELETE FROM Customers 
WHERE Country IN (
    SELECT Country 
    FROM (
        SELECT Country 
        FROM Customers 
        GROUP BY Country
        HAVING COUNT(DISTINCT CustomerID) < 5
    ) AS subquery
);
-- Section3
SELECT DISTINCT CustomerName
FROM Customers 
WHERE CustomerID IN (
    SELECT CustomerID 
    FROM Orders
    WHERE OrderID IN (
        SELECT OrderID 
        FROM OrderDetails
        WHERE ProductID IN (
            SELECT ProductID 
            FROM Products 
            ORDER BY Price ASC 
            LIMIT 5
        )
    )
)
ORDER BY CustomerName ASC;
-- Section4
SELECT DISTINCT Quantity AS Sales
FROM OrderDetails 
WHERE OrderID IN (
    SELECT OrderID 
    FROM Orders 
    WHERE MONTH(OrderDate)= MONTH(CURRENT_DATE) 
    AND YEAR(OrderDate) = YEAR(CURRENT_DATE)
)
ORDER BY Sales DESC
LIMIT 10;
