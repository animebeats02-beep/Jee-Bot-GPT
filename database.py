import sqlite3

DB_NAME = "studyos.db"

def init_db():

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS homework(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        task TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_homework(
    subject,
    task
):

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO homework(
            subject,
            task
        )
        VALUES (?, ?)
        """,
        (
            subject,
            task
        )
    )

    conn.commit()
    conn.close()


def get_homework():

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute(
        """
        SELECT subject, task
        FROM homework
        """
    )

    rows = cur.fetchall()

    conn.close()

    return rows