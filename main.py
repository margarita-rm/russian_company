import json
import psycopg2.extras

db_table = "users"

with psycopg2.connect(
        host="localhost",
        database="russian_company",
        user="postgres",
        password="October94"
) as conn:
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(f"SELECT * FROM {db_table}")
        rows = cur.fetchall()
        result = [
            {
                key: str(value)
                for key, value in dict(row).items()
            }
            for row in rows
        ]
        with open("data.json", "w") as json_file:
            json.dump(result, json_file, indent=4)
