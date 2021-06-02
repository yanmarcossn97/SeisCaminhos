import discord
import requests
import json
import translateText
import schedule
import time
import asyncio

TOKEN = "ODQwMTg4NzY1Mzc2ODcyNDQ4.YJUkww.oskeMMmJNsF-EcdXlMQnVuidbGc"

client = discord.Client()

def get_quote(arg):
	response = requests.get(arg)
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " _" + json_data[0]['a']

	return quote

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  task = asyncio.create_task(daily_quote())
  await task
  print("Daily quote scheduled")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$insp'):
    quote = get_quote("https://zenquotes.io/api/random")
    text = translateText.translate_text(quote)
    await message.channel.send(text)

async def daily_quote():
  def job():
    print("yMarcius")

  schedule.every(15).seconds.do(job)
  # schedule.every().day.at("09:19").do(job)

  while True:
    schedule.run_pending()
    time.sleep(1)
    await asyncio.sleep(1)

client.run(TOKEN)