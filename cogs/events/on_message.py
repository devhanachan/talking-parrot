import discord
from discord.ext import commands
from speaker_demo import generate_parrot_voice

class msg(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if message.author == self.bot.user:
            return

        # repeat ppl messages
        filename = "tts_output.mp3"
        path=await generate_parrot_voice(message.content, filename)
        if path:
            vc=message.guild.voice_client
            if not vc:
                vc=await message.author.voice.channel.connect()

            vc.play(discord.FFmpegPCMAudio(path))
        else:
            await message.channel.send("error in generate voice step")

async def setup(bot):
    await bot.add_cog(msg(bot))