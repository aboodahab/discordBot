import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


@bot.event
async def on_message(message):
    # Prevent the bot from replying to itself
    if message.author == bot.user:
        return

    # Example: respond to "hello"
    if message.content.lower() == 'hello':
        await message.channel.send(f'Hello {message.author.name}! 👋')

    # Make sure commands still work
    await bot.process_commands(message)
# Event triggered when someone joins
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN2")
print(TOKEN)
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")


@bot.event
async def on_member_join(member):
    # Get the default channel (you can specify a channel by ID instead)
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f"👋 Welcome to the server, {member.mention}!")


bot.run(TOKEN)
