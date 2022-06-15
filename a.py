import random
import sqlite3

con = sqlite3.connect('db.db')
cur = con.cursor()

m = random.choice(cur.execute(f'SELECT * FROM db WHERE mod=\'NM1\'').fetchall())
print(all(m))