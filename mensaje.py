import discord
from discord.ext import commands
 
 
#Para hacer funcionar los mensajes privados deben de activar lo siguiente en la configuracion del bot: https://i.imgur.com/elsqnoA.png
#https://discord.com/developers/applications
 
#To make private messages work, you must activate the following in the bot configuration: https://i.imgur.com/elsqnoA.png
#https://discord.com/developers/applications
 
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)
 
 
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
 
@client.event
async def on_member_join(member):
    mbed = discord.Embed(
        color = discord.Color.magenta(),
        title = 'bienvenido a mi servidor =D',
        description = f'Bienvenido {member.mention}, espero que disfrutes =D!'
    )
    await member.send(embed=mbed)
    
    
bot.run("")   
