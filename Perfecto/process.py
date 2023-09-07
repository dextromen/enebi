import pandas as pd
import sqlite3

conn = sqlite3.connect('new_db.db')

cur = conn.cursor()



data = pd.read_csv('done.csv')

data = data.to_dict()

for i in data['Geo']:
    sql = f"""INSERT INTO  words  (geo, en, current, n ) VALUES (?, ?, ?,? )"""
    values = (data["Geo"][i], data["En"][i], 0, 5)
    cur.execute(sql,values)

    conn.commit()
    

conn.close()