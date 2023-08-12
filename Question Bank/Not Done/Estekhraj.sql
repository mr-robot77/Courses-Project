-- Section1
SELECT id AS order_id 
FROM orders 
WHERE status = 'warehouse'
ORDER BY id DESC;

-- Section2
SELECT id AS customer_id, name AS customer_name
FROM customers
WHERE id NOT IN (SELECT DISTINCT customer_id FROM orders)
ORDER BY name ASC;

-- Section3
SELECT DATE(created_at) AS date, FORMAT(COUNT(*) / (SELECT COUNT(*) FROM orders WHERE status != 'canceled' AND EXISTS(SELECT 1 FROM customers WHERE is_blocked = 0))), 2) * 100, 2) AS cancellation_rate
FROM orders 
JOIN customers ON orders.customer_id = customers.id AND is_blocked = 0 AND status = 'canceled'
GROUP BY DATE(created_at);