import pandas as pd
import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas


def load_snowflake(source_data_df, user, password, account, warehouse, database, schema):
    conn = snow.connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema
    )

    write_pandas(conn, source_data_df, "youtube")

    print('Load success')

    return True


if __name__ == '__main__':
    source_data_df = pd.read_csv('global_youtube_stat.csv', encoding='unicode_escape')

    user = ''
    password = ''
    account = ''
    warehouse = ''
    database = ''
    schema = ''

    load_snowflake(source_data_df, user, password, account, warehouse, database, schema)
