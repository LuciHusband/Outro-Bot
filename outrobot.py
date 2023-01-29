import os
import asyncio
import discord
from discord.ext import commands

def run_discord_bot():
    TOKEN = "<Your token here>" 

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix = ".", intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f"{bot.user} is now running!")

    @bot.command(name='outro')
    async def outro(ctx, member: discord.Member):
        try:
            vc = await member.voice.channel.connect()
            vc.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outro.mp3'))))

            await asyncio.sleep(15)
            await member.move_to(None)
            await asyncio.sleep(5)
            await vc.disconnect()
        except:
            await ctx.send("Mentioned user is not in a voice channel!") 
    bot.run(TOKEN)

if __name__ == "__main__":
    run_discord_bot()