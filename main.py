import discord

TOKEN = "ODQwMTg4NzY1Mzc2ODcyNDQ4.YJUkww.oskeMMmJNsF-EcdXlMQnVuidbGc"

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
     
  if message.content.startswith('$hello'):
    await message.channel.send('Hello Gamers!')

client.run(TOKEN)