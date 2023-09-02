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
        try:
            print("Executing the query...")
            self.curr = self.conn.cursor()
            formated_q = self.curr.mogrify(query,data)
            self.curr.execute(formated_q)
        except e:
            print(f"Exception {e} occurred")
        print("Executed query")


if __name__ == "__main__":  
    database = Postgres()
    database.connect()
    
    query = "insert into users (name, age) values (%s, %s)"
    data = ("John" , 30)
   
    database.execute_query(query, data)

    database.commit()
    database.close()
