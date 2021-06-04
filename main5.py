import discord
import requests
import json
import translateText

from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = # token of the bot
channel_id = # channel id

client = discord.Client()

def get_quote(arg):
	response = requests.get(arg)
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " _" + json_data[0]['a']

	return quote

async def daily_quote():
  channel = client.get_channel(channel_id)
  quote_en = get_quote("https://zenquotes.io/api/today")
  quote_pt = translateText.translate_text(quote_en)
  await channel.send(quote_pt)

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
    quote_en = get_quote("https://zenquotes.io/api/random")
    quote_pt = translateText.translate_text(quote_en)
    await message.channel.send(quote_pt)

client.run(TOKEN)