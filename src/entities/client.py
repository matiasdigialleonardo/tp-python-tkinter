import sqlite3

class Client:
    
    def __init__(self):
        self.TABLE = "clients"
        
    def open(self):
        connection=sqlite3.connect("./bd_tkinter_tp.db")
        return connection
    
    def createClientsTable(self):
        connection=self.open()

        connection.execute("""CREATE TABLE if NOT EXISTS clients (
                                id integer primary key autoincrement,
                                first_name text,
                                last_name text,
                                street_name text,
                                house_number integer
                            )""")
        connection.close()
        
    def add(self, data):
        connection=self.open()
        cursor=connection.cursor()
        sql=f"INSERT into {self.TABLE}(first_name, last_name, street_name, house_number) values (?,?,?,?)"
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def get_clients(self):
        connection=self.open()
        cursor=connection.cursor()
        # SQL query to retrive all clients by first and last name.
        sql="SELECT last_name FROM clients"
        # Executes the query and saves all results in the data variable using fetchall.
        cursor.execute(sql)
        data = cursor.fetchall()
        # Closes the connection and returns the data.
        connection.close()
        return data

    def get_client_id(self, data):
        connection=self.open()
        cursor=connection.cursor()
        sql="SELECT id FROM clients WHERE last_name = ?"
        # Executes the query and saves all results in the data variable using fetchone.
        cursor.execute(sql, (data, ))
        result = cursor.fetchone()
        clientId = result[0] if result else None
        # Closes the connection and returns the data.
        connection.close()
        return clientId