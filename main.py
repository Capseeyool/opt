import discord
import os
import random
import requests
import sqlite3
from dotenv import load_dotenv

load_dotenv()
con = sqlite3.connect('db.db')
cur = con.cursor()

API_KEY = os.getenv('API_KEY')
PREFIX = '.'

class OPT(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    
    async def on_message(self, message):
        msg = message.content.split(' ')
        if msg[0] == f'{PREFIX}m':
            m = random.choice(cur.execute(f'SELECT * FROM db WHERE mod=\'{msg[1].upper()}\'').fetchall())
            r = requests.get(f'https://osu.ppy.sh/api/get_beatmaps?k={API_KEY}&b={m[0]}&m=0').json()[0]
            embed = discord.Embed(
                title=f'{r["title"]} [{r["version"]}]',
                description=f'{m[2]}: {m[1]}\nID: {m[0]}',
                url=f'https://osu.ppy.sh/beatmapsets/{r["beatmapset_id"]}#osu/{m[0]}',
            )
            embed.set_image(url=f'https://assets.ppy.sh/beatmaps/{r["beatmapset_id"]}/covers/cover.jpg')
            await message.channel.send(embed=embed)

if __name__ == '__main__':
    client = OPT()
    client.run(os.getenv('token'))