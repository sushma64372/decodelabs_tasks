-- 1. Display all records
SELECT * FROM orders;

-- 2. Display first 10 records
SELECT * FROM orders
LIMIT 10;

-- 3. Count total orders
SELECT COUNT(*) FROM orders;

-- 4. Find total sales
SELECT SUM(TotalPrice) FROM orders;

-- 5. Find average order value
SELECT AVG(TotalPrice) FROM orders;
-- 6. Find delivered orders
SELECT * FROM orders
WHERE OrderStatus = 'Delivered';

-- 7. Find orders with price greater than 1000
SELECT * FROM orders
WHERE TotalPrice > 1000;

-- 8. Sort orders by highest price
SELECT * FROM orders
ORDER BY TotalPrice DESC;

-- 9. Find all laptop orders
SELECT * FROM orders
WHERE Product = 'Laptop';

-- 10. Find top 5 expensive orders
SELECT * FROM orders
ORDER BY TotalPrice DESC
LIMIT 5;
-- 11. Count orders by product
SELECT Product, COUNT(*)
FROM orders
GROUP BY Product;

-- 12. Total sales by product
SELECT Product, SUM(TotalPrice)
FROM orders
GROUP BY Product;

-- 13. Average price by product
SELECT Product, AVG(TotalPrice)
FROM orders
GROUP BY Product;

-- 14. Orders by payment method
SELECT PaymentMethod, COUNT(*)
FROM orders
GROUP BY PaymentMethod;

-- 15. Orders by status
SELECT OrderStatus, COUNT(*)
FROM orders
GROUP BY OrderStatus;
-- 16. Products having more than 170 orders
SELECT Product, COUNT(*) AS TotalOrders
FROM orders
GROUP BY Product
HAVING COUNT(*) > 170;
-- 17. Percentage contribution of each product in total sales
SELECT
    Product,
    ROUND(SUM(TotalPrice), 2) AS ProductSales,
    ROUND(
        SUM(TotalPrice) * 100.0 / (SELECT SUM(TotalPrice) FROM orders),
        2
    ) AS SalesPercentage
FROM orders
GROUP BY Product
ORDER BY SalesPercentage DESC;