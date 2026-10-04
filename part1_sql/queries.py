import sqlite3

conn = sqlite3.connect("data/meesho_reseller.db")
cursor = conn.cursor()

query1 = """
SELECT 
    month,
    category,
    ROUND(SUM(quantity * unit_price), 2) AS total_revenue
FROM orders
GROUP BY month, category
ORDER BY month, category;
"""

cursor.execute(query1)
results = cursor.fetchall()

print("Monthly Category Revenue:")
for row in results:
    print(row)

with open("part1_sql/output/query1_monthly_category_revenue.txt", "w") as f:
    f.write("Monthly Category Revenue:\n")
    for row in results:
        f.write(str(row) + "\n")
query2 = """
SELECT 
    r.region,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_revenue
FROM orders o
JOIN resellers r ON o.reseller_id = r.reseller_id
GROUP BY r.region
ORDER BY r.region;
"""

cursor.execute(query2)
results2 = cursor.fetchall()

print("\nRegion-wise Revenue:")
for row in results2:
    print(row)

with open("part1_sql/output/query2_region_revenue.txt", "w") as f:
    f.write("Region-wise Revenue:\n")
    for row in results2:
        f.write(str(row) + "\n")
query3 = """
SELECT 
    r.reseller_id,
    r.reseller_name,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_spend
FROM orders o
JOIN resellers r ON o.reseller_id = r.reseller_id
GROUP BY r.reseller_id, r.reseller_name
HAVING total_spend > 50000
ORDER BY total_spend DESC;
"""

cursor.execute(query3)
results3 = cursor.fetchall()

print("\nTop Resellers (spend > 50000):")
for row in results3:
    print(row)

with open("part1_sql/output/query3_top_resellers.txt", "w") as f:
    f.write("Top Resellers (spend > 50000):\n")
    for row in results3:
        f.write(str(row) + "\n") 
query4 = """
SELECT 
    r.reseller_id,
    r.reseller_name,
    COUNT(*) AS count_star,
    COUNT(o.order_id) AS count_order_id
FROM resellers r
LEFT JOIN orders o ON r.reseller_id = o.reseller_id
GROUP BY r.reseller_id, r.reseller_name
HAVING count_order_id = 0;
"""

cursor.execute(query4)
results4 = cursor.fetchall()

print("\nZero-order Reseller:")
for row in results4:
    print(row)

with open("part1_sql/output/query4_zero_order_reseller.txt", "w") as f:
    f.write("Zero-order Reseller:\n")
    for row in results4:
        f.write(str(row) + "\n")   
query5 = """
SELECT 
    ROUND(SUM(o.quantity * o.unit_price) * 1.0 / COUNT(*), 2) AS aov
FROM orders o
WHERE o.month = 'June' AND o.status = 'Delivered';
"""

cursor.execute(query5)
results5 = cursor.fetchall()

print("\nJune Delivered AOV:")
for row in results5:
    print(row)

with open("part1_sql/output/query5_june_delivered_aov.txt", "w") as f:
    f.write("June Delivered AOV:\n")
    for row in results5:
        f.write(str(row) + "\n")                    
query1b = """
SELECT month, category, ROUND(SUM(quantity * unit_price), 2) AS revenue, COUNT(*) AS n_orders
FROM orders
GROUP BY month, category
ORDER BY month, category;
"""
cursor.execute(query1b)
results1b = cursor.fetchall()

with open("part2_engine/fixtures/monthly_category_revenue.csv", "w", newline="") as f:
    f.write("month,category,revenue,n_orders\n")
    for row in results1b:
        f.write(f"{row[0]},{row[1]},{row[2]},{row[3]}\n")
check = cursor.execute("SELECT reseller_id, reseller_name, region FROM resellers WHERE reseller_id='RS019'").fetchall()
print(check)
for month_name in ["April", "May", "June"]:
    q = """
    SELECT month, category, ROUND(SUM(quantity * unit_price), 2) AS revenue, COUNT(*) AS n_orders
    FROM orders
    WHERE month = ?
    GROUP BY month, category
    ORDER BY category;
    """
    cursor.execute(q, (month_name,))
    rows = cursor.fetchall()
    filename = f"part4_agent/fixtures/{month_name.lower()}_feed.csv"
    with open(filename, "w", newline="") as f:
        f.write("month,category,revenue,n_orders\n")
        for row in rows:
            f.write(f"{row[0]},{row[1]},{row[2]},{row[3]}\n")
conn.close()
