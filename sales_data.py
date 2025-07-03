import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert Data
cursor.executemany("""
INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)
""", [
    ('Product A', 10, 15.5),
    ('Product B', 5, 25.0),
    ('Product C', 8, 12.0)
])
conn.commit()

# Query
query = """
SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue 
FROM sales GROUP BY product
"""
df = pd.read_sql_query(query, conn)
print(df)

# Plot
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

conn.close()
