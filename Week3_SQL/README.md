# DecodeLabs Week 3 – SQL Data Analysis

## Project Overview

This project focuses on analyzing sales data using SQL and SQLite. The dataset contains 1,200 records and 14 columns related to customer orders, products, payments, and order status.

## Tools Used

* Python
* SQLite
* SQL
* VS Code
* Pandas

## Dataset Information

* Total Records: 1,200
* Total Columns: 14
* Database Table: `orders`

## SQL Concepts Covered

1. SELECT
2. WHERE
3. ORDER BY
4. LIMIT
5. COUNT()
6. SUM()
7. AVG()
8. GROUP BY
9. HAVING
10. ROUND()
11. Subqueries

## Key Insights

* Total sales: 1,264,761.96
* Average order value: 1,053.97
* Total orders: 1,200
* Printer and Chair had the highest sales contribution, at approximately 15.47% each.
* Phone had the lowest sales contribution, at 12%.
* Online was the most frequently used payment method, with 258 orders.
* Cancelled orders were the most common order status, with 250 orders.

## Project Files

* `dataset.csv` – Original dataset
* `database.py` – Imports CSV data into SQLite
* `sales.db` – SQLite database
* `sql_queries.sql` – SQL queries
* `run_queries.py` – Executes SQL queries
* `screenshots/` – Project screenshots

## How to Run

1. Install Python and required libraries.
2. Keep all project files in the same folder.
3. Run `py database.py` to import the dataset.
4. Run `py run_queries.py` to execute all SQL queries.

## Conclusion

This project helped analyze sales data using SQL. It demonstrates data filtering, sorting, aggregation, grouping, and percentage-based sales analysis.
