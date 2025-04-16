import sqlite3

def initialize_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('delivery_app.db')
    cursor = conn.cursor()

    # Create a table for users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dim_dates (
            date INTEGER PRIMARY KEY AUTOINCREMENT,
            year STRING NOT NULL,
            month STRING NOT NULL,
            day STRING NOT NULL,
            isHoliday STRING NOT NULL,
            isWeekend STRING NOT NULL,  
            FOREIGN KEY (date) REFERENCES fact_orders (date)
        )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Database initialized and tables created.")

if __name__ == "__main__":
    initialize_database()