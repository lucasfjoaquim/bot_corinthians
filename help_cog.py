import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
Comandos gerais:
!help - help caralho
!p <palavra chave> - acha o video com palavra chave
!q - mostra queue
!skip - skips caralho
!clear - para musica
!leave - ele sai po
!pause - ele pausa po
!resume - ele volta a musica
```
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started    
    @commands.Cog.listener()
    async def on_ready(self):
        print("on_ready")
        for guild in self.bot.guilds:
            print(guild)
            for channel in guild.text_channels:
                if str(channel).strip() == "músicas-e-tabs":
                    print(channel)
                    self.text_channel_list.append(channel)

        await self.send_to_all(self.help_message)        

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        print("help")
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        print("send to all")
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)