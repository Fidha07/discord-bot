import discord.py

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        await message.channel.send('Hello!')


client.run('MTA1MzU2MjA5NjU5MzQxMjE5MA.G7T_zZ.kvWFZGYksl8khXDGFnlhQ_Ge5uRnFdN8MYWZm0 ')
