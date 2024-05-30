import sqlite3

DATABASE_FILE = './database.db'

def create_sqlite_database():
    """create a database connection to an SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_tables():
    sql_statements = [
        """CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY, 
                age INT NOT NULL
        );""",
    ]

    # create a database connection
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)

            conn.commit()
    except sqlite3.Error as e:
        print(e)


if __name__ == "__main__":
    create_sqlite_database()
    create_tables()