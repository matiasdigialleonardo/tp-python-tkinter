import sqlite3

class TechnicalProblem:
    
    def __init__(self):
        self.TABLE = "technical_problems"
        
    def open(self):
        connection=sqlite3.connect("./bd_tkinter_tp.db")
        return connection
    
    def createTechnicalProblemsTable(self):
        connection=self.open()
        
        connection.execute("""CREATE TABLE IF NOT EXISTS technical_problems (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            problem_description TEXT,
                            date DATE,
                            hour TIME,
                            client_id INTEGER,
                            technician_id INTEGER,
                            FOREIGN KEY (client_id) REFERENCES clients (id),
                            FOREIGN KEY (technician_id) REFERENCES technicians (id)
                            )""")
        connection.close()
        
    def add(self, data):
        connection=self.open()
        cursor=connection.cursor()
        sql=f"INSERT into {self.TABLE}(problem_description, client_id) values (?,?)"
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        
    def get_problems_id(self):
        connection=self.open()
        cursor=connection.cursor()
        # SQL query to retrive all clients by first and last name.
        sql="SELECT id FROM technical_problems"
        # Executes the query and saves all results in the data variable using fetchall.
        cursor.execute(sql)
        data = cursor.fetchall()
        # Closes the connection and returns the data.
        connection.close()
        return data
    
    def get_problem(self, problem_id):
        connection=self.open()
        cursor=connection.cursor()
        
        get_problem_query = "SELECT problem_description FROM technical_problems WHERE id = ?"
        cursor.execute(get_problem_query, (problem_id,))
        
        result = cursor.fetchone()
        problem_description = result[0] if result else None
        # Closes the connection and returns the data.
        connection.close()
        return problem_description
        
    def add_appointment(self, data):
        connection=self.open()
        cursor=connection.cursor()
        sql=f"UPDATE {self.TABLE} SET date = ?, hour = ?, technician_id = ? WHERE id = ?"
        cursor.execute(sql, data)
        connection.commit()
        connection.close()