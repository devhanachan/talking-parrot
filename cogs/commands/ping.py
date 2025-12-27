import discord
from discord.ext import commands
from discord import app_commands

class ping ( commands.Cog ):
    def __init__ ( self, bot: commands.Bot ):
        self.bot = bot

    @app_commands.command(name="ping",description="test if bot works")
    async def ping (self, i: discord.Interaction ):
        await i.response.defer(thinking=True)

        hello="pong"
        await i.followup.send(hello)

async def setup(bot: commands.Bot ):
    await bot.add_cog( ping (bot))