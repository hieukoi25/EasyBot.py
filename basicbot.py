#discord
import discord
from discord.ext import commands
#built in
import os
#self
import eb_ui

async def cog(client):
#cogs detection
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    cogs = [f for f in os.listdir('./cogs') if f.endswith('.py')]
    if len(cogs) >= 5:
        print('This may take a while... please wait patiently')
    for cog in cogs:
        cog = cog.replace('.py', '')
        try:
            client.load_extension(f'cogs.{cog}')
            print(f'{cog} is loaded successfully')
        except discord.ext.commands.ExtensionAlreadyLoaded:
            print(f'{cog} is already loaded; There may be a duplicate file or another version present')
        except Exception as e:
            print(f'There was an error with {cog} with the error: {e}\n {cog} will be skipped')

#bot main
def main(token, prefix):
    def __init__(self, client):
        self.client = client
    
    bot = commands.Bot(command_prefix=prefix)

    #embed help command
    class helpcommand(commands.MinimalHelpCommand):
        async def send_pages(self):
            destination = self.get_destination()
            e = discord.Embed(color=0x1ABC9C, description='')
            for page in self.paginator.pages:
                e.description += page
            await destination.send(embed=e)
    bot.help_command = helpcommand()

    #on boot
    @bot.event
    async def on_ready():
        eb_ui.sys_message('Successfully booted')
        await cog(bot)
        print(f'USN:{bot.user.name}\nUID:{bot.user.id}\nInvite: https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8 \n')
        presense =  f" your call using {prefix}"
        if prefix.endswith(' '):
            presense = presense + f'; Note: there is a space following {prefix[:-1]}'
        await bot.change_presence(activity=discord.Activity (type=discord.ActivityType.listening, name=presense))

    #error response
    @bot.event
    async def on_command_error(ctx, error):
        await ctx.send(error)

    #start bot
    try:
        bot.run(token)
    except Exception as e:
        #will state when an invalid token has been used
        eb_ui.sys_message(e)
        return