import discord
import os
import random
import requests
import sqlite3
from dotenv import load_dotenv

load_dotenv()

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
        # use query parameters instead
        if msg[0] == f'{PREFIX}m':
            if len(msg) in range(2, 4):
                if len(msg) == 2:
                    m = random.choice(cur.execute(f'SELECT * FROM db WHERE mod=\'{msg[1].upper()}\'').fetchall())
                elif len(msg) == 3:
                    try:
                        m = random.choice(cur.execute(f'SELECT * FROM db WHERE mod=\'{msg[1].upper()}\' AND SR >= {msg[2]} AND SR <= {int(msg[2]) + 1}').fetchall())
                    except IndexError:
                        m = []
                try:
                    embed = discord.Embed(
                        title=f'{m[3]} - {m[4]} [{m[5]}]',
                        description=f'{m[0]} | {m[1]} | {m[2]}\n'
                        f'**SR**: {round(float(m[6]), 2)} | **Length**: {int(m[7]) // 60}:{int(m[7]) % 60} | **Combo**: {m[8]}x\n'
                        f'**BPM**: {m[9]} | **CS**: {m[10]} | **AR**: {m[11]} | **OD**: {m[12]}',
                        url=f'https://osu.ppy.sh/beatmapsets/{m[13]}#osu/{m[2]}',
                    )
                    embed.set_image(url=f'https://assets.ppy.sh/beatmaps/{m[13]}/covers/cover.jpg')
                    await message.channel.send(embed=embed)
                except IndexError:
                    await message.channel.send('404 not found')
            else:
                await message.channel.send('?')

        
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