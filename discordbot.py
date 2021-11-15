#
import discord
import os
import requests as req

token = os.getenv('ROSHAN_WEATHERDISCORDBOTTOKEN')

def getweather(city):
    base = "https://www.indranilsen.ca/cs-circle/weather/location"
    response = req.get(base + "?city=" + city)
    return (response.json()["main"]["temp"] - 273.15)

client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        print("said hello to " + str(message.author))
    
    if message.content.startswith('$help'):
        await message.channel.send('type $weather {city}')
        print("said hello to " + str(message.author))
    
    if message.content.startswith('$weather'):
        city = message.content.split(" ")[1]
        await message.channel.send(getweather(city))
        print("said hello to " + str(message.author))

client.run(token)


