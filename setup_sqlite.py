import sqlite3

conn = sqlite3.connect("demo.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  region TEXT
);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER REFERENCES customers(id),
  amount REAL,
  ordered_at TEXT
);
""")

cur.executemany(
    "INSERT INTO customers (name, region) VALUES (?, ?)",
    [("Acme", "west"), ("Globex", "east"), ("Initech", "east"), ("Umbrella", "south")],
)
cur.executemany(
    "INSERT INTO orders (customer_id, amount, ordered_at) VALUES (?, ?, ?)",
    [(1, 120.50, "2026-09-01"), (2, 300.00, "2026-09-03"), (1, 75.25, "2026-09-10"),
     (3, 410.00, "2026-09-12"), (2, 90.00, "2026-09-20")],
)
conn.commit()

for row in cur.execute("""
    SELECT c.name, SUM(o.amount) AS total
    FROM customers c JOIN orders o ON o.customer_id = c.id
    GROUP BY c.name ORDER BY total DESC
"""):
    print(row)

conn.close()