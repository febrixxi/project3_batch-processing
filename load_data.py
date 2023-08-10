import psycopg2
import pandas as pd
from sqlalchemy import create_engine


def load(file, sheet_name, table_name):
    # read xlsx
    data = pd.read_excel(file, sheet_name=sheet_name)

    user =
    passwd =
    hostname =
    database =

    conn_string = f'postgresql://{user}:{passwd}@{hostname}:5432/{database}'

    db = create_engine(conn_string)
    conn = db.connect()

    data.to_sql(table_name, con=conn, if_exists='append',
                index=False)
    conn = psycopg2.connect(conn_string)
