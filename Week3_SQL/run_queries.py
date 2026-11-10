import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

with open("sql_queries.sql", "r") as file:
    queries = file.read()

# Remove SQL comments
lines = [
    line for line in queries.splitlines()
    if not line.strip().startswith("--")
]

clean_queries = "\n".join(lines)

for query in clean_queries.split(";"):

    query = query.strip()

    if query:
        cursor.execute(query)

        print("\nQuery:", query)

        if query.upper().startswith("SELECT"):
            results = cursor.fetchall()
            print("Result:", results[:10])

conn.close()

print("\nAll Queries Executed Successfully!")