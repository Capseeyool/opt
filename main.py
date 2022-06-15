import discord
import os
import random
import requests
import sqlite3

con = sqlite3.connect('db.db')
cur = con.cursor()

API_KEY = os.environ['API_KEY']
TOKEN = os.environ['TOKEN']

PREFIX = '.'

class OPT(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    
    async def on_message(self, message):
        msg = message.content.split(' ')
        # TODO
        # list all tournaments instead of only 1 per map
        # calculate cs/ar/od changes
        if msg[0] == f'{PREFIX}m':
            m = random.choice(cur.execute(f'SELECT * FROM db WHERE mod=\'{msg[1].upper()}\'').fetchall())
            if (all(m)):
                embed = discord.Embed(
                    title=f'{m[3]} - {m[4]} [{m[5]}]',
                    description=f'{m[0]} | {m[1]} | {m[2]}\n'
                    f'**SR**: {round(float(m[6]), 2)} | **Length**: {int(m[7]) // 60}:{int(m[7]) % 60} | **Combo**: {m[8]}x\n'
                    f'**BPM**: {m[9]} | **CS**: {m[10]} | **AR**: {m[11]} | **OD**: {m[12]}',
                    url=f'https://osu.ppy.sh/beatmapsets/{m[13]}#osu/{m[2]}',
                )
            else:
                r = requests.get(f'https://osu.ppy.sh/api/get_beatmaps?k={API_KEY}&b={m[2]}&m=0').json()[0]
                cur.execute(f'''INSERT INTO db (artist, title, diff, SR, length, combo, BPM, CS, AR, OD, beatmapsetID) VALUES (
                    \'{r["artist"]}\',
                    \'{r["title"]}\',
                    \'{r["version"]}\',
                    \'{r["difficultyrating"]}\',
                    \'{r["total_length"]}\',
                    \'{r["max_combo"]}\',
                    \'{r["bpm"]}\',
                    \'{r["diff_size"]}\',
                    \'{r["diff_approach"]}\',
                    \'{r["diff_overall"]}\',
                    \'{r["beatmapset_id"]}\'
                )''')
                embed = discord.Embed(
                    title=f'{r["artist"]} - {r["title"]} [{r["version"]}]',
                    description=f'{m[0]} | {m[1]} | {m[2]}\n'
                    f'**SR**: {round(float(r["difficultyrating"]), 2)} | **Length**: {int(r["total_length"]) // 60}:{int(r["total_length"]) % 60} | **Combo**: {r["max_combo"]}x\n'
                    f'**BPM**: {r["bpm"]} | **CS**: {r["diff_size"]} | **AR**: {r["diff_approach"]} | **OD**: {r["diff_overall"]}',
                    url=f'https://osu.ppy.sh/beatmapsets/{r["beatmapset_id"]}#osu/{m[2]}',
                )
                embed.set_image(url=f'https://assets.ppy.sh/beatmaps/{r["beatmapset_id"]}/covers/cover.jpg')
            await message.channel.send(embed=embed)
        
        elif msg[0] == f'{PREFIX}mappool':
            pool = cur.execute(f'SELECT mod, ID FROM db WHERE tournament=\'{message.content[9:]}\'').fetchall()
            if pool:
                embed = discord.Embed(
                    title=message.content[9:],
                    description='\n'.join([f'{i[0]}: {i[1]}' for i in pool])
                )
                await message.channel.send(embed=embed)
            else:
                pools = cur.execute('SELECT DISTINCT tournament FROM db').fetchall()
                embed = discord.Embed(
                    title='List of available mappools:',
                    description='\n'.join([i[0] for i in pools])
                )
                await message.channel.send(embed=embed)

if __name__ == '__main__':
    client = OPT()
    client.run(TOKEN)