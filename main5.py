import discord
import requests
import json
import translateText

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

TOKEN = "ODQwMTg4NzY1Mzc2ODcyNDQ4.YJUkww.oskeMMmJNsF-EcdXlMQnVuidbGc"
channel_id = 830863122545508372

client = discord.Client()

def get_quote(arg):
	response = requests.get(arg)
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " _" + json_data[0]['a']

	return quote

async def daily_quote():
  channel = client.get_channel(channel_id)
  quote = get_quote("https://zenquotes.io/api/today")
  text = translateText.translate_text(quote)
  await channel.send(text)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  # initializig scheduler
  scheduler = AsyncIOScheduler()

  # scheduling a daily message function
  scheduler.add_job(daily_quote, 'cron', hour=8)

  # starting scheduler
  scheduler.start()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$insp'):
    quote = get_quote("https://zenquotes.io/api/random")
    text = translateText.translate_text(quote)
    await message.channel.send(text)

client.run(TOKEN)