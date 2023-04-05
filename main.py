#MTA4MjI5MDA5MDc4NjY5NzIyNw.GgK0xe.n3rIYqKreBJD5W_7towF1gfJ7MCKS55gt6sBJo
import os
import discord
from discord.ext import commands
import pytube
import openai

TOKEN = 'MTA4MjI5MDA5MDc4NjY5NzIyNw.GgK0xe.n3rIYqKreBJD5W_7towF1gfJ7MCKS55gt6sBJo'

openai.api_key = "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"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('Bot conectado a discord')

@client.event
async def on_message(message):
  if message.content.startswith('!hello'):
    await message.channel.send('holi')
    
  if message.content.startswith('!sumar'):
    numeros = message.content.split()[1:]
    resultado = sum([float(numeros) for num in numeros])
    await message.channel.send(f'El resultado de la suma es {resultado}')   

  if message.content.startswith('!download'):
      url = message.content.split()[1]
      yt = pytube.YouTube(url)
      stream = yt.streams.get_highest_resolution()
      filename = stream.download()
      await message.channel.send(f'Video desacargado como {filename}')
      os.system(f'start{filename}')

  if message.content.startswith('!AI'):
    prompt = message.content
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=2048)
    answer = response.choices[0].text
    await message.channel.send(answer)
          
    
client.run(TOKEN)