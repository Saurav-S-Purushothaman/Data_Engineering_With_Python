import psycopg2 as db
from faker import Faker

class Postgres:
    param = {
        "host":"localhost",
        "database":"dataengineering",
        "user":"postgres",
        "password":"saurav"
        }

    def connect(self):
       """Connectioin to postgres database"""
       self.conn = None
       try:
           print("Connecting to postgres db ...")
           self.conn = db.connect(**self.param)
       except(Exception, db.DatabaseError) as error:
           print(error)
       print("Connection successful")

    def commit(self):
        """Commiting to database"""
        self.conn.commit()
       
    def close(self): 
       """Closing the conneciton"""
       print("Closing the connection......")
       self.conn.close()
       print("Connection closed....")

    def execute_query(self, query,data):
            print("Executing the query...")
            self.curr = self.conn.cursor()
            self.curr.executemany(query,data)
        

if __name__ == "__main__":  
    # Connect to database
    database = Postgres()
    database.connect()
    
    # Query for database
    query = "insert into users (name, age, street_address,city) values (%s,%s,%s,%s)"
    data = [] 

    fake = Faker()
    for x in range(1000):
        tup = (fake.name(),fake.random_int
        (min=18, max=80, step=1),
        fake.street_address(),
        fake.city())
        data.append(tup)
    
    data = tuple(data)
    database.execute_query(query, data)

    database.commit()
    database.close()
