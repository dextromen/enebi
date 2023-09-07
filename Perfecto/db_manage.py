import sqlite3

class DB_Manager:
    db = "new_db.db"



    def get_balance(self):
        conn = sqlite3.connect(self.db)

        cur = conn.cursor()

        cur.execute("""select balance from game""")
        data = cur.fetchone()[0]
        conn.close()

        conn.close()

        return data
    
    def update_balance(self, balance):
        conn = sqlite3.connect(self.db)

        cur = conn.cursor()

        cur.execute(f"""update game set balance = {balance}""")
        
        conn.commit()

        conn.close()

    def get_familiar(self,last_id):

        """PASS QUANTITY AS QUANTITY OF RESULTS BY ROWID"""
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM words WHERE id < {last_id} ")
        data = cur.fetchall()
        words = {}
        word_list=[]

        for row in data:
            words={
                "id":row[0],
                "geo":row[1],
                "en":row[2],
                "n":row[3],
                "current":row[4]
            }
            if row[6] == None:
                words['mistake'] = 0
            else:
                words['mistake'] = row[6]
            word_list.append(words)

        conn.commit()
        conn.close()
        return word_list

    def get_words():

        """PASS QUANTITY AS QUANTITY OF RESULTS BY ROWID"""
        conn = sqlite3.connect("db/database.db")
        cur = conn.cursor()
        cur.execute(f"SELECT geo, en FROM words WHERE current = 1 ORDER BY id")
        data = cur.fetchall()
        words = {}
        word_list=[]

        for row in data:
            words={
                "geo":row[0],
                "en":row[1]
            }
            word_list.append(words)

        conn.commit()
        conn.close()
        return word_list
    
    def get_current(self):

        """PASS QUANTITY AS QUANTITY OF RESULTS BY ROWID"""
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM words WHERE current = 1")
        data = cur.fetchall()
        words = {}
        word_list=[]

        for row in data:
            words={
                "id":row[0],
                "geo":row[1],
                "en":row[2],
                "n":row[3],
                "current":row[4]
            }
            if row[6] == None:
                words['mistake'] = 0
            else:
                words['mistake'] = row[6]
            word_list.append(words)

        conn.commit()
        conn.close()
        return word_list
    
    def get_last_id(self):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute(f"SELECT last_id FROM game ")
        data = cur.fetchall()
        return data[0][0]
    
    def update_last_id(self, last_id):
        conn = sqlite3.connect(self.db)

        cur = conn.cursor()

        cur.execute(f"""UPDATE game SET last_id = {last_id}""")
        
        conn.commit()

        conn.close()


    def add_new(self, last_id, quantity):
        uni = last_id + quantity
        """PASS QUANTITY AS QUANTITY OF RESULTS BY ROWID"""
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM words WHERE id BETWEEN {last_id+1} AND  {uni}")
        
        data = cur.fetchall()
        words = {}
        word_list=[]

        for row in data:
            words={
                "id":row[0],
                "geo":row[1],
                "en":row[2],
                "n":row[3],
                "current":row[4]
            }
            if row[6] == None:
                words['mistake'] = 0
            else:
                words['mistake'] = row[6]
            word_list.append(words)
        cur.execute(f"""UPDATE words SET current = {1} WHERE id BETWEEN {last_id+1} AND {uni}""")
        cur.execute(f"""UPDATE game SET last_id = {uni}""")
        conn.commit()
        conn.close()
        return word_list
    
    def change_mistake(self,id, mistake):

        conn = sqlite3.connect(self.db)

        cur = conn.cursor()

        cur.execute(f"""UPDATE words SET mistake = {mistake} WHERE id = {id}""")
        
        conn.commit()

        conn.close()

    def change_n(self,id, n):

        conn = sqlite3.connect(self.db)

        cur = conn.cursor()

        cur.execute(f"""UPDATE words SET n = {n} WHERE id = {id}""")
        
        conn.commit()

        conn.close()

    def add_current(self, id):
        conn = sqlite3.connect(self.db)

        cur = conn.cursor()

        cur.execute(f"""UPDATE words SET current = {1} WHERE id = {id}""")
        
        conn.commit()

        conn.close()

    def remove_current(self,id):
        conn = sqlite3.connect(self.db)

        cur = conn.cursor()

        cur.execute(f"""UPDATE words SET current = {0} WHERE id = {id}""")
        
        conn.commit()

        conn.close()