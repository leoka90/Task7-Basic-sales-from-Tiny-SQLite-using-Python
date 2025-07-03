#  Task 7 - Basic Sales Summary using SQLite in Python

##  Objective

To extract simple sales information (total quantity and total revenue) from a SQLite database using SQL in Python, and visualize the results using a bar chart.

---

## Tools Used

- **Python** (built-in `sqlite3`)
- **SQLite** (no external setup needed)
- **pandas** (for SQL query results and data manipulation)
- **matplotlib** (for visualization)

---

##  Dataset

A sample SQLite database (`sales_data.db`) is created with one table named `sales`, containing the following columns:

- `id` (INTEGER, auto-incremented primary key)
- `product` (TEXT)
- `quantity` (INTEGER)
- `price` (REAL)

### Sample Data Inserted

| product   | quantity | price |
|-----------|----------|-------|
| Product A | 10       | 15.5  |
| Product B | 5        | 25.0  |
| Product C | 8        | 12.0  |

---

##  SQL Query Used

```sql
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product;
