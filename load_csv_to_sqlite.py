import sqlite3
import csv
import os

def load_csv_to_sqlite(db_file, csv_file, table_name):
    print(f"Loading {csv_file} into table {table_name}...")
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        
        # Create table
        columns = ", ".join([f'"{h}" TEXT' for h in headers])
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        cursor.execute(f"CREATE TABLE {table_name} ({columns})")
        
        # Insert data
        placeholders = ", ".join(["?"] * len(headers))
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        
        for row in reader:
            cursor.execute(insert_query, row)
            
    conn.commit()
    conn.close()
    print(f"Finished loading {csv_file}")

if __name__ == '__main__':
    db_path = 'social_engine.db'
    
    users_csv = 'Social_Engine_Users.csv'
    posts_csv = 'Social_Engine_Posts.csv'
    
    load_csv_to_sqlite(db_path, users_csv, 'Users')
    load_csv_to_sqlite(db_path, posts_csv, 'Posts')
    print("Database creation complete.")
