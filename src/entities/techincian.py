import sqlite3

class Technician:
    
    def __init__(self):
        self.TABLE = "technicians"
        
    def open(self):
        connection=sqlite3.connect("./bd_tkinter_tp.db")
        return connection
    
    def createTechniciansTable(self):
        connection=self.open()

        connection.execute("""CREATE TABLE if NOT EXISTS technicians (
                                id integer primary key autoincrement,
                                first_name text,
                                last_name text
                            )""")
        connection.close()
        
    def add(self, first_name, last_name):
        connection=self.open()
        cursor=connection.cursor()
        
        select_query = "SELECT * FROM technicians WHERE last_name = ?"
        cursor.execute(select_query, (last_name,))
        existing_technician = cursor.fetchone()
        
        if existing_technician:
            #Technician with the given last_name already exists
            cursor.close()
            connection.close()
            return
        
        insert_query=f"INSERT into {self.TABLE}(first_name, last_name) values (?,?)"
        cursor.execute(insert_query, (first_name, last_name))
        
        connection.commit()
        connection.close()
        
    def get_technicians(self):
        connection=self.open()
        cursor=connection.cursor()
        # SQL query to retrive all clients by first and last name.
        sql="SELECT last_name FROM technicians"
        # Executes the query and saves all results in the data variable using fetchall.
        cursor.execute(sql)
        data = cursor.fetchall()
        # Closes the connection and returns the data.
        connection.close()
        return data
    
    def get_technician_id(self, last_name):
        connection=self.open()
        cursor=connection.cursor()
        # SQL query to retrive id of technician
        sql="SELECT id FROM technicians WHERE last_name = ?"
        # Executes the query and saves the result in a variable.
        cursor.execute(sql, (last_name, ))
        result = cursor.fetchone()
        technicianId = result[0] if result else None
        # Closes the connection and returns the data.
        connection.close()
        return technicianId