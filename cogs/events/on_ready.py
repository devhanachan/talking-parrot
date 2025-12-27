import discord
from discord.ext import commands
from datetime import datetime
import os
from dotenv import load_dotenv

class wakeup ( commands.Cog ):
    def __init__ (self, bot:commands.Bot ):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print ( f"I'm up ! {self.bot.user.name} at : {datetime.now()}")
        load_dotenv()
        debug_ch=(int(os.getenv("DEBUG_ROOM")))
        sendHello=self.bot.get_channel(debug_ch)
        if sendHello:
            print(os.getenv("DEBUG_ROOM"))
            await sendHello.send("I'm up! ")
        else:
            print("error there is something wrong in sendHello")
            print( f" the variables debug_ch {debug_ch} type {type(debug_ch)}")

        
async def setup (bot:commands.Bot ):
    await bot.add_cog ( wakeup (bot))