from postgres import Postgres
import pandas as pd

if __name__ == "__main__":
    database = Postgres()
    database.connect()
    database.cursor()

    # Query to get data
    query = "SELECT * FROM users ORDER BY name DESC"
    df = pd.read_sql(query,database.conn)
    print(df.iloc[0])
    database.commit()
    database.close()
