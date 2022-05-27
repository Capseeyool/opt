import discord
import os
import random
import requests
import sqlite3
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()
con = sqlite3.connect('db.db')
cur = con.cursor()

API_KEY = os.getenv('API_KEY')
TOKEN = os.getenv('TOKEN')

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
            r = requests.get(f'https://osu.ppy.sh/api/get_beatmaps?k={API_KEY}&b={m[2]}&m=0').json()[0]
            embed = discord.Embed(
                title=f'{r["artist"]} - {r["title"]} [{r["version"]}]',
                description=f'{m[0]} | {m[1]} | {m[2]}\n'
                f'**SR**: {round(float(r["difficultyrating"]), 2)} | **Length**: {int(r["total_length"]) // 60}:{int(r["total_length"]) % 60} | **Combo**: {r["max_combo"]}x\n'
                f'**BPM**: {r["bpm"]} | **CS**: {r["diff_size"]} | **AR**: {r["diff_approach"]} | **OD**: {r["diff_overall"]}',
                url=f'https://osu.ppy.sh/beatmapsets/{r["beatmapset_id"]}#osu/{m[2]}',
            )
            embed.set_image(url=f'https://assets.ppy.sh/beatmaps/{r["beatmapset_id"]}/covers/cover.jpg')
            await message.channel.send(embed=embed)

if __name__ == '__main__':
    client = OPT()
    client.run(TOKEN)