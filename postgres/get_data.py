from postgres import Postgres


if __name__ == "__main__":
    database = Postgres()
    database.connect()
    database.cursor()

    # Query to get data
    query = "SELECT * FROM users ORDER BY name DESC"
    with open("result.csv", "w") as f:
        database.curr.copy_to(f, "users", sep=",")
    record = database.get_data(query)

    database.commit()
    database.close()
