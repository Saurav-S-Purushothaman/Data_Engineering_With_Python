from faker import Faker
from postgres import Postgres


if __name__ == "__main__":
    # Connect to database
    database = Postgres()
    database.connect()
    database.cursor()

    # Query for database
    query = "INSERT INTO users (name, age, street_address,city) VALUES (%s,%s,%s,%s)"
    fake = Faker()
    data = []
    for x in range(1000):
        tup = (
            fake.name(),
            fake.random_int(min=18, max=80, step=1),
            fake.street_address(),
            fake.city(),
        )
        data.append(tup)

    data = tuple(data)
    database.execute_query(query, data)

    database.commit()
    database.close()
