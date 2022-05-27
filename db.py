# TODO
# table for map, table for mod, table for tournament
# one to many relationship for map to tournament
# idk think about it later
# need to account for different tournament same mod, different tournament different mod

import os
import sqlite3

def insert(id, mod, tournament):
    cur.execute(f'INSERT INTO db (ID, mod, tournament) VALUES ({id}, \'{mod}\', \'{tournament}\')')

def insert_pool(tournament, ids, nm=6, hd=3, hr=3, dt=4, fm=3, ez=0, ht=0, tb=1):
    mods = [f'NM{i}' for i in range(1, nm + 1)] + [f'HD{i}' for i in range(1, hd + 1)] + [f'HR{i}' for i in range(1, hr + 1)] + [f'DT{i}' for i in range(1, dt + 1)] + [f'FM{i}' for i in range(1, fm + 1)] + [f'EZ{i}' for i in range(1, ez + 1)] + [f'HT{i}' for i in range(1, ht + 1)] + [f'TB{i}' for i in range(1, tb + 1)]
    for i in zip(ids, mods):
        insert(i[0], i[1], tournament)

if os.path.exists('db.db'):
    os.remove('db.db')

con = sqlite3.connect('db.db')
cur = con.cursor()

cur.execute('CREATE TABLE db (ID INT NOT NULL, mod VARCHAR(3) NOT NULL, tournament VARCHAR(255) NOT NULL, PRIMARY KEY(ID))')

insert_pool('OWC 2021 GF',
[3333705, 3333669, 3333699, 3333703, 3333700, 3333701, 3145691, 3333793, 3333706, 3081546, 3331199, 3333660, 3333570, 3333586, 3333770, 3333734, 3333729, 3333760, 3333738, 3333745])
insert_pool('OWC 2021 Finals',
[2675756, 3322513, 3322521, 3322526, 3322566, 3322093, 2856086, 3322576, 2633747, 438187, 2947341, 3322603, 3320894, 3322598, 859667, 3322610, 3322611, 2643166, 3322445, 3322616])
insert_pool('OWC 2021 SF',
[3311170, 3310526, 3311309, 3311337, 3311312, 3311313, 3311238, 3311073, 2267887, 861381, 3311344, 3311036, 2643135, 3311366, 277274, 3311356, 3311891, 3311383, 3311376, 3311391])

con.commit()