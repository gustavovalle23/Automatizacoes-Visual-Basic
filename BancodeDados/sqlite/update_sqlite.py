import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def update_task(conn, task):
    sql = ''' UPDATE tasks
              SET priority = ? ,
                  begin_date = ? ,
                  end_date = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def main():
    database = 'pythonsqlite.db'

    # create a database connection
    conn = create_connection(database)
    with conn:
        update_task(conn, (2, '2020-01-04', '2020-01-06', 2))


if __name__ == '__main__':
    main()
