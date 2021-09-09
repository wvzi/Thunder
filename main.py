
thunder = """
████████╗██╗░░██╗██╗░░░██╗███╗░░██╗██████╗░███████╗██████╗░
╚══██╔══╝██║░░██║██║░░░██║████╗░██║██╔══██╗██╔════╝██╔══██╗
░░░██║░░░███████║██║░░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
░░░██║░░░██╔══██║██║░░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║╚██████╔╝██║░╚███║██████╔╝███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
"""

print(thunder)
import discord,json,os,random

from discord.ext import commands

with open("config.json") as file: # json loads
    info = json.load(file)
    token = info["token"]
    delete = info["autodelete"]
    prefix = info["prefix"]

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Thunder is running smooth!")
@bot.command() # Stock command
async def stock(ctx):
    stockmenu = discord.Embed(title="Account Stock",description="") # def stock
    for filename in os.listdir("Accounts"):
        with open("Accounts\\"+filename) as f: # checkfile
            ammount = len(f.read().splitlines()) # get lines
            name = (filename[0].upper() + filename[1:].lower()).replace(".txt","") 
            stockmenu.description += f"*{name}* - {ammount}\n" # add to embed
    await ctx.send(embed=stockmenu) # Embed var send



@bot.command() # main gen command
async def gen(ctx,name=None):
    if name == None:
        await ctx.send("Please, Specify what type of account you want") 
    else:
        name = name.lower()+".txt" #.txt ext
        if name not in os.listdir("Accounts"): # if
            await ctx.send(f"Account does not exist! `{prefix}stock`")
        else:
            with open("Accounts\\"+name) as file:
                lines = file.read().splitlines() #rlines
            if len(lines) == 0: 
                await ctx.send("Sorry! We do not have stock on these accountsd") 
            else:
                with open("Accounts\\"+name) as file:
                    account = random.choice(lines) # get a random line
                try: # try var
                    await ctx.author.send(f"`{str(account)}`\n\nMessage will delete in {str(delete)} seconds!",delete_after=delete)
                except: 
                    await ctx.send("Error, Please Turn on your DMs!")
                else: 
                    await ctx.send("Sent the account to your DMs!")
                    with open("Accounts\\"+name,"w") as file:
                        file.write("")
                    with open("Accounts\\"+name,"a") as file:
                        for line in lines: 
                            if line != account: 
                                file.write(line+"\n") 
bot.run(token)