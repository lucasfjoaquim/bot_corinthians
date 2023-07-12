import discord
from discord.ext import commands
import os



#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with our token
print(os.getenv('TOKEN'))
bot.run('MTA3NjIxODM4NDUwMjQ5MzI1NA.G4FMwb.tBFCBszXjOwW4xx6MCEwE2vHsrPu6viXqZyj3I')
