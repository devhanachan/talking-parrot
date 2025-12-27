import discord
from discord.ext import commands
from discord import app_commands
from discord import VoiceClient
import os

class voice(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="join",
        description="to join users channel"
    )
    async def join_vc (self, i:discord.Interaction):
        await i.response.defer(thinking=True)
        # _______
        u_vc = i.user.voice
        
        if not u_vc:
            return await i.followup.send("You need to join a voice channel first")
        
        ch=u_vc.channel
        vc=i.guild.voice_client
        ### i want it to disconnect and reconnect again for some reason while debugging
        if vc:
            await vc.disconnect()
        await ch.connect()
        await i.followup.send(f" I'm in ! {i.user.mention}")

        # play mp3
        vc: VoiceClient = i.guild.voice_client
        if vc and vc.is_playing(): #if any file in queue il stop it 
            vc.stop()
        
        ### have to remove this because no longer need
        # view = UIButtonspeakTest()
        # await i.followup.send(view=view)

        ### I used to test the bot if it acutally can play the mp3 files
        # sr = os.path.join("sound_effect", "green.mp3")
        # vc.play(discord.FFmpegPCMAudio(sr))
        
### I built this UI view to play my voice to test if the bot is really can speak
### with out any problem 

#############################################
def selectingPath(whichFile):
        path = os.path.join("sound_effect", whichFile)
        if not path:
            print("there is no file selected ")
            return
        return path

song_q = []
def play_next(i):
    if len(song_q) > 0:
        next_song = song_q.pop(0)
        vc=i.guild.voice_client
        if vc:
            print(f"playing file: {next_song}")
            vc.play(discord.FFmpegPCMAudio(next_song), after=lambda e:play_next(i))
        else:
            print("no queue")
#######################################            
##### I used to built this to test the speaker feature
# class UIButtonspeakTest(discord.ui.View):
#     def __init__(self):
#         super().__init__(timeout=100)

#     async def handle_click(self, i:discord.Interaction, filename: str):
#         vc: VoiceClient = i.guild.voice_client
#         target_f = selectingPath(filename)
#         if not vc:
#             return await i.response.send_message("join vc first!")
#         if not target_f:
#             return await i.response.send_message(f"file {filename} not found!")
#         if vc.is_playing():
#             song_q.append(target_f)
#             await i.response.send_message(f"add **{filename}** down to q) q:{len(song_q)}")
#         else:
#             await i.response.send_message(f"playing **{filename}** ",delete_after=3)
#         vc.play(discord.FFmpegPCMAudio(target_f), after=lambda e: play_next(i))

#     ### it doesn't work bruh (anyone can help me?)
#     # ### delete itself after timeout
#     # async def on_timeout(self):
#     #     if hasattr(self, 'message'):
#     #         await self.message.edit(view=None)

#     @discord.ui.button(label='Green', style=discord.ButtonStyle.success) 
#     async def greenButton(self, i: discord.Interaction, button: discord.ui.Button):
#         await self.handle_click(i, "green.mp3")

#     @discord.ui.button(label='Red', style=discord.ButtonStyle.danger) 
#     async def redButton(self, i: discord.Interaction, button: discord.ui.Button):
#         await self.handle_click(i, "red.mp3")

#     @discord.ui.button(label='Blue', style=discord.ButtonStyle.primary)
#     async def blueButton(self, i: discord.Interaction, button: discord.ui.Button):
#         await self.handle_click(i, "blue.mp3")

#     @discord.ui.button(label='Grey', style=discord.ButtonStyle.secondary)
#     async def greyButton(self, i: discord.Interaction, button: discord.ui.Button):
#         await self.handle_click(i, "grey.mp3")

async def setup(bot:commands.Bot):
    await bot.add_cog(voice(bot))

    