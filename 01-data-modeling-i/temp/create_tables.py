import psycopg2


table_drop = "DROP TABLE IF EXISTS events, actors, orgs"

table_create = """
    CREATE TABLE IF NOT EXISTS actors (
        id int,
        login text,
        display_login text,
        gravatar_id text,
        url text,
        avatar_url text,
        PRIMARY KEY (id)
    );
    CREATE TABLE IF NOT EXISTS orgs (
        id int,
        name text,
        PRIMARY KEY (id)
    );
    CREATE TABLE IF NOT EXISTS events (
        id text,
        actor_id int,
        created_at text,
        PRIMARY KEY (id)
    );
"""

create_table_queries = [
    table_create,
]
drop_table_queries = [
    table_drop,
]


def drop_tables(cur: PostgresCursor, conn: PostgresConn) -> None:
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur: PostgresCursor, conn: PostgresConn) -> None:
    """
    Creates each table using the queries in `create_table_queries` list.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database.
    - Establishes connection with the sparkify database and gets
    cursor to it.
    - Drops all the tables.
    - Creates all tables needed.
    - Finally, closes the connection.
    """
    conn = psycopg2.connect(
        "host=172.18.0.2 dbname=postgres user=postgres password=postgres"
    )
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
