import psycopg2 as db

class Postgres:
    param = {
        "host": "localhost",
        "database": "dataengineering",
        "user": "postgres",
        "password": "saurav",
    }

    def connect(self):
        """Connectioin to postgres database"""
        self.conn = None
        try:
            print("Connecting to postgres db ...")
            self.conn = db.connect(**self.param)
        except (Exception, db.DatabaseError) as error:
            print(error)
        print("Connection successful")

    def commit(self):
        """Commiting to database"""
        self.conn.commit()

    def close(self):
        """Closing the conneciton"""
        print("Closing the connection......")
        self.conn.close()
        print("Connection closed")

    def cursor(self):
        """Cursor for the connection"""
        print("Cursor created")
        self.curr = self.conn.cursor()

    def execute_query(self, query, data):
        print("Executing the query...")
        self.curr.executemany(query, data)

    def get_data(self, query):
        print("Executing the query to get data...")
        self.curr.execute(query)
        result_list = []
        for record in self.curr:
            result_list.append(record)
        return record


