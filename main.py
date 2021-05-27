import discord
import json
import pyfiglet
import time
import os
import aiohttp
import asyncio
import io
import random
import string
import colorama
import requests
import datetime
import math

from colorama import Fore
from time import sleep
from os import system, name
from discord.ext import commands

print("Genocide selfbot loading...")

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')
stream_url = config.get('stream_url')

version = "1.0"

genocide = commands.Bot(description="Genocide Selfbot", command_prefix=prefix, self_bot=True)
genocide.remove_command('help')

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def Init():
    token = config.get('token')
    try:
        clear()
        print(f'''

{Fore.RED}
                              ▄████ ▓█████  ███▄    █  ▒█████   ▄████▄   ██▓▓█████▄ ▓█████ 
                             ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▒██▒  ██▒▒██▀ ▀█  ▓██▒▒██▀ ██▌▓█   ▀ 
                            ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒██░  ██▒▒▓█    ▄ ▒██▒░██   █▌▒███   
                            ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░▒▓▓▄ ▄██▒░██░░▓█▄   ▌▒▓█  ▄ 
                            ░▒▓███▀▒░▒████▒▒██░   ▓██░░ ████▓▒░▒ ▓███▀ ░░██░░▒████▓ ░▒████▒
                             ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ░▒ ▒  ░░▓   ▒▒▓  ▒ ░░ ▒░ ░
                              ░   ░  ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░   ░  ▒    ▒ ░ ░ ▒  ▒  ░ ░  ░
                            ░ ░   ░    ░      ░   ░ ░ ░ ░ ░ ▒  ░         ▒ ░ ░ ░  ░    ░   
                                  ░    ░  ░         ░     ░ ░  ░ ░       ░     ░       ░  ░
                                                       ░             ░             
                                                    {Fore.GREEN}Prefix: {Fore.RED}{prefix}
{Fore.RESET}
        ''')
        os.system(f'title Genocide Selfbot V{version}')
        genocide.run(token, bot=False, reconnect=True)
        print(f'\n\n{Fore.RED}                                      Thanks for using Genocide Selfbot :){Fore.RESET}')
    except discord.errors.LoginFailure:
        clear()
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}]{Fore.RED} Improper token has been passed.{Fore.RESET}')
        os.system('pause >NUL')

@genocide.event
async def on_command_error(ctx, error):
    print(f'{Fore.GREEN}[{Fore.RESET}!{Fore.GREEN}] {Fore.RED}{error}{Fore.RESET}')

@genocide.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"help\"{Fore.RESET}')
        embed = discord.Embed(title="Genocide Selfbot <Categories>", description="<> = mandatory\n[] = optional", color=0xff0000)
        embed.add_field(name="`help general`", value="> Sends general commands.", inline=False)
        embed.add_field(name="`help account`", value="> Sends account commands.", inline=False)
        embed.add_field(name="`help moderation`", value="> Sends moderation commands.", inline=False)
        embed.add_field(name="`help text`", value="> Sends text commands.", inline=False)
        embed.add_field(name="`help image`", value="> Sends image commands.", inline=False)
        embed.add_field(name="`help social`", value="> Sends social commands.", inline=False)
        embed.set_thumbnail(url=genocide.user.avatar_url)
        await ctx.send(embed=embed)
    elif str(category).lower() == "general":
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"help {category}\"{Fore.RESET}')
        embed = discord.Embed(title="Genocide Selfbot <General>", description="<> = mandatory\n[] = optional", color=0xff0000)
        embed.add_field(name="`av [@mention]`", value="> Sends someone's avatar.", inline=False)
        embed.add_field(name="`whois [@mention]`", value="> Sends information about a user.", inline=False)
        embed.add_field(name="`ping`", value="> Sends the ping of the selfbot.", inline=False)
        embed.add_field(name="`pingweb`", value="> Sends the availability of the website. (http(s) needed.)", inline=False)
        embed.add_field(name="`adminservers`", value="> Sends all servers you have admin in.", inline=False)
        embed.add_field(name="`membercount`", value="> Sends the amount of members in the server it\'s used in.", inline=False)
        embed.add_field(name="`rolecolor <@mention>`", value="> Sends the hex color for the role. (IDs also work!)", inline=False)
        embed.add_field(name="`servers`", value="> Sends the amount of servers you\'re in.", inline=False)
        embed.add_field(name="`servericon`", value="> Sends icon of the server you\'re in.", inline=False)
        embed.add_field(name="`serverbanner`", value="> Sends banner of the server you\'re in.", inline=False)
        embed.set_thumbnail(url=genocide.user.avatar_url)
        await ctx.send(embed=embed)
    elif str(category).lower() == "moderation":
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"help {category}\"{Fore.RESET}')
        embed = discord.Embed(title="Genocide Selfbot <Moderation>", description="<> = mandatory\n[] = optional", color=0xff0000)
        embed.add_field(name="`ban <@mention> [reason]`", value="> Bans a member if you have the permissions to.", inline=False)
        embed.add_field(name="`kick <@mention> [reason]`", value="> Kicks a member if you have the permissions to.", inline=False)
        embed.add_field(name="`unban <id>`", value="> Unbans a member if you have the permissions to.", inline=False)
        embed.add_field(name="`unbanall`", value="> Unbans every banned member if you have the permissions to.", inline=False)
        embed.set_footer(text="Only works if the member is cached!")
        await ctx.send(embed=embed)
    elif str(category).lower() == "text":
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"help {category}\"{Fore.RESET}')
        embed = discord.Embed(title="Genocide Selfbot <Text>", description="<> = mandatory\n[] = optional", color=0xff0000)
        embed.add_field(name="`embed <message>`", value="> Displays text in an embed.", inline=False)
        embed.add_field(name="`ascii <message>`", value="> Displays text in ASCII.", inline=False)
        embed.add_field(name="`emojify <message>`", value="> Displays text in emojis. (WIP!)", inline=False)
        embed.add_field(name="`nitro`", value="> Sends an unchecked Nitro code.", inline=False)
        embed.add_field(name="`spam <amount> <message>`", value="> Spams the message the specified amount of times.", inline=False)
        embed.add_field(name="`purge <amount>`", value="> Purges your messages in the specified amount of messages.", inline=False)
        embed.add_field(name="`flood`", value="> Sends a really big message.", inline=False)
        embed.add_field(name="`reverse <message>`", value="> Reverses the message.", inline=False)
        embed.add_field(name="`bobux [@mention]`", value="> Generates bobux.", inline=False)
        embed.add_field(name="`fakeeveryone [message]`", value="> Sends a fake @everyone.", inline=False)
        embed.add_field(name="`randomtoken`", value="> Sends a random Discord token.", inline=False)
        embed.add_field(name="`empty`", value="> Sends an empty message.", inline=False)
        embed.add_field(name="`cum`", value="> Makes you cum.", inline=False)
        embed.add_field(name="`9/11`", value="> Need I say more?", inline=False)
        embed.add_field(name="`dogfact`", value="> Sends a fact about dogs.", inline=False)
        embed.add_field(name="`catfact`", value="> Sends a fact about cats.", inline=False)
        embed.add_field(name="`pandafact`", value="> Sends a fact about pandas.", inline=False)
        embed.add_field(name="`foxfact`", value="> Sends a fact about foxes.", inline=False)
        embed.add_field(name="`birbfact`", value="> Sends a fact about birbs.", inline=False)
        embed.add_field(name="`koalafact`", value="> Sends a fact about koalas.", inline=False)
        embed.set_thumbnail(url=genocide.user.avatar_url)
        await ctx.send(embed=embed)
    elif str(category).lower() == "account":
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"help {category}\"{Fore.RESET}')
        embed = discord.Embed(title="Genocide Selfbot <Account>", description="<> = mandatory\n[] = optional", color=0xff0000)
        embed.add_field(name="`stream <message>`", value="> Changes your status to streaming.", inline=False)
        embed.add_field(name="`game <message>`", value="> Changes your status to gaming.", inline=False)
        embed.add_field(name="`listening <message>`", value="> Changes your status to listening.", inline=False)
        embed.add_field(name="`watching <message>`", value="> Changes your status to watching.", inline=False)
        embed.add_field(name="`stopactivity`", value="> Changes your status back to normal.", inline=False)
        embed.add_field(name="`read`", value="> Marks every channel in the guild as read.", inline=False)
        embed.set_thumbnail(url=genocide.user.avatar_url)
        await ctx.send(embed=embed)
    elif str(category).lower() == "social":
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"help {category}\"{Fore.RESET}')
        embed = discord.Embed(title="Genocide Selfbot <Social>", description="<> = mandatory\n[] = optional", color=0xff0000)
        embed.add_field(name="`hug <@mention> [message]`", value="> Hugs a user.", inline=False)
        embed.add_field(name="`kiss <@mention> [message]`", value="> Kisses a user.", inline=False)
        embed.add_field(name="`pat <@mention> [message]`", value="> Pats a user.", inline=False)
        embed.add_field(name="`feed <@mention> [message]`", value="> Feeds a user.", inline=False)
        embed.add_field(name="`slap <@mention> [message]`", value="> Slaps a user.", inline=False)
        embed.set_footer(text="Only works if the member is cached!")
        embed.set_thumbnail(url=genocide.user.avatar_url)
        await ctx.send(embed=embed)
    elif str(category).lower() == "image":
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"help {category}\"{Fore.RESET}')
        embed = discord.Embed(title="Genocide Selfbot <Image>", description="<> = mandatory\n[] = optional", color=0xff0000)
        embed.add_field(name="`meme`", value="> Sends a meme.", inline=False)
        embed.add_field(name="`neko`", value="> Sends an image of a neko.", inline=False)
        embed.add_field(name="`dog`", value="> Sends an image of a dog.", inline=False)
        embed.add_field(name="`cat`", value="> Sends an image of a cat.", inline=False)
        embed.add_field(name="`panda`", value="> Sends an image of a panda.", inline=False)
        embed.add_field(name="`redpanda`", value="> Sends an image of a red panda.", inline=False)
        embed.add_field(name="`fox`", value="> Sends an image of a fox.", inline=False)
        embed.add_field(name="`birb`", value="> Sends an image of a birb.", inline=False)
        embed.add_field(name="`koala`", value="> Sends an image of a koala.", inline=False)
        embed.set_thumbnail(url=genocide.user.avatar_url)
        await ctx.send(embed=embed)

@genocide.command()
async def ascii(ctx, *, args: str = None):
    await ctx.message.delete()
    if args == None:
        embed = discord.Embed(title="Usage:", description="ascii <message>", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"ascii\"{Fore.RESET}')
    else:
        text = pyfiglet.figlet_format(args)
        await ctx.send(f'```{text}```')
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"ascii\"{Fore.RESET}')

@genocide.command()
async def embed(ctx, *, args: str = None):
    await ctx.message.delete()
    if args == None:
        embed = discord.Embed(title="Usage:", description="embed <message>", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"embed\"{Fore.RESET}')
    else:
        embed = discord.Embed(description=f"{args}", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"embed\"{Fore.RESET}')

@genocide.command(aliases=['emoji', 'emojified'])
async def emojify(ctx, *, args: str = None):
    await ctx.message.delete()
    if args == None:
        embed = discord.Embed(title="Usage:", description="emojify <message>", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"emojify\"{Fore.RESET}')
    else:
        emojified = ':regional_indicator_{}:'.format(args)
        await ctx.send(emojified)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"emojify\"{Fore.RESET}')

@genocide.command()
async def ilikecum(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="i like cum", description="like if you also like cum", color=0xff0000) #,color=Hex code
    message = await ctx.send(embed=embed)
    await message.add_reaction("👍")
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"ilikecum\"{Fore.RESET}')

@genocide.command(aliases=['robux, robuxgenerator, robuxgen, bobuxgenerator, bobuxgen'])
async def bobux(ctx, user: discord.User = None):
    await ctx.message.delete()
    if user == None:
        amount = random.randrange(start=100, stop=10000)
        embed = discord.Embed(title="Bobux generator", description=f'Sent {amount} bobux to your account!!!', color=0xff0000)
        embed.set_image(url="https://media.discordapp.net/attachments/745232386933129246/804368536352849960/bobux_generator.gif")
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"bobux\"{Fore.RESET}')
    else:
        amount = random.randrange(start=100, stop=10000)
        embed = discord.Embed(title="Bobux generator", description=f'Sent {amount} bobux to {user.mention}\'s account!!!', color=0xff0000)
        embed.set_image(url="https://media.discordapp.net/attachments/745232386933129246/804368536352849960/bobux_generator.gif")
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"bobux\"{Fore.RESET}')

@genocide.command()
async def nitro(ctx):
    await ctx.message.delete()
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    await ctx.send(f'https://discord.gift/{code}')
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"nitro\"{Fore.RESET}')

@genocide.command(aliases=['avatar', 'pfp', 'profilepicture'])
async def av(ctx, user:discord.User=None):
    await ctx.message.delete()
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"av\"{Fore.RESET}')
    if user == None:
        avatar = genocide.user.avatar_url
        embed = discord.Embed(title=f'{genocide.user.name}\'s avatar', color=0xff0000)
        embed.set_image(url=avatar)
        await ctx.send(embed=embed)
        return
    else:
        avatar = user.avatar_url
        embed = discord.Embed(title=f'{user.name}\'s avatar', color=0xff0000)
        embed.set_image(url=avatar)
        await ctx.send(embed=embed)

@genocide.command()
async def whois(ctx, *, user: discord.User = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.TextChannel):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention, color=0xff0000)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        await ctx.send(embed=em)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"whois\"{Fore.RESET}')
        return
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention, color=0xff0000)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        await ctx.send(embed=em)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"whois\"{Fore.RESET}')
        return

@genocide.command()
async def rolecolor(ctx, role: discord.Role = None):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.DMChannel):
        embed = discord.Embed(description="Cannot use this command in DMs", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"rolecolor\"{Fore.RESET}')
    elif isinstance(ctx.message.channel, discord.GroupChannel):
        embed = discord.Embed(description="Cannot use this command in a group chat", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"rolecolor\"{Fore.RESET}')
    elif isinstance(ctx.message.channel, discord.TextChannel):
        if role == None:
            embed = discord.Embed(title="Usage:", description="rolecolor <role>", color=0xff0000)
            embed.set_footer(text='IDs also work!')
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"rolecolor\"{Fore.RESET}')
        else:
            embed = discord.Embed(description=f'`{role.name}`: `{role.color}`', color=role.color.value)
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"rolecolor\"{Fore.RESET}')

@genocide.command(aliases=["guildinfo"])
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"`{len(ctx.guild.roles)}` Roles\n `{len(ctx.guild.text_channels)}` Text channels\n `{len(ctx.guild.voice_channels)}` Voice channels\n `{len(ctx.guild.categories)}` Categories",
                          timestamp=datetime.datetime.utcnow(), color=0xff0000)
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"serverinfo\"{Fore.RESET}')

@genocide.command(aliases=['guildpfp', 'serverpfp', 'guildicon'])
async def servericon(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=ctx.guild.name, color=0xff0000)
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"servericon\"{Fore.RESET}')

@genocide.command(aliases=['guildbanner'])
async def serverbanner(ctx):
    await ctx.message.delete()
    if ctx.guild.banner_url == False:
        embed = discord.Embed(description="Server doesn\'t have a banner!")
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"serverbanner\"{Fore.RESET}')
    else:
        embed = discord.Embed(title=ctx.guild.name, color=0xff0000)
        embed.set_image(url=ctx.guild.banner_url)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"serverbanner\"{Fore.RESET}')

@genocide.command(aliases=['members'])
async def membercount(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.DMChannel):
        embed = discord.Embed(description="Cannot use this command in DMs", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"membercount\"{Fore.RESET}')
    elif isinstance(ctx.message.channel, discord.GroupChannel):
        embed = discord.Embed(description="Cannot use this command in a group chat", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"membercount\"{Fore.RESET}')
    elif isinstance(ctx.message.channel, discord.TextChannel):
        embed = discord.Embed(title=f'`{ctx.guild.name}`\'s member count:', description=f'{ctx.guild.member_count}', color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"membercount\"{Fore.RESET}')
    else:
        embed = discord.Embed(description="Something went wrong", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"membercount\"{Fore.RESET}')

@genocide.command(aliases=["guilds", "servercount", "guildcount"])
async def servers(ctx):
    await ctx.message.delete()
    guildcount = len(genocide.guilds)
    embed = discord.Embed(description=f'{guildcount}', color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"servers\"{Fore.RESET}')

@genocide.command()
async def ban (ctx, member:discord.User=None, *, reason=None):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        embed = discord.Embed(description="Cannot ban in a group chat", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if isinstance(ctx.message.channel, discord.DMChannel):
        embed = discord.Embed(description="Cannot ban in DMs", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if member == None:
        embed = discord.Embed(title="Usage:", description="ban <@mention> [reason]", color=0xff0000)
        await ctx.channel.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"ban\"{Fore.RESET}')
        return
    if member == ctx.message.author:
        embed = discord.Embed(title="Usage:", description="ban <@mention> [reason]", color=0xff0000)
        await ctx.channel.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"ban\"{Fore.RESET}')
        return
    if reason == None:
        reason = "No reason given."
    await ctx.guild.ban(member, reason=reason, delete_message_days=0)
    embed = discord.Embed(description=f'`{member}` has been banned from `{ctx.guild.name}` for `{reason}`', color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"ban\"{Fore.RESET}')

@genocide.command()
async def kick (ctx, member:discord.User=None, *, reason=None):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        embed = discord.Embed(description="Cannot kick in a group chat", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if isinstance(ctx.message.channel, discord.DMChannel):
        embed = discord.Embed(description="Cannot kick in DMs", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if member == None:
        embed = discord.Embed(title="Usage:", description="kick <@mention> [reason]", color=0xff0000)
        await ctx.channel.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"kick\"{Fore.RESET}')
        return
    if member == ctx.message.author:
        embed = discord.Embed(title="Usage:", description="kick <@mention> [reason]", color=0xff0000)
        await ctx.channel.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"kick\"{Fore.RESET}')
        return
    if reason == None:
        reason = "No reason given."
    await ctx.guild.kick(member, reason=reason)
    embed = discord.Embed(description=f'`{member}` has been kicked from `{ctx.guild.name}` for `{reason}`', color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"kick\"{Fore.RESET}')

@genocide.command()
async def unban(ctx, member:discord.User=None):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        embed = discord.Embed(description="Cannot unban in a group chat", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"unban\"{Fore.RESET}')
    elif isinstance(ctx.message.channel, discord.DMChannel):
        embed = discord.Embed(description="Cannot unban in DMs", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"unban\"{Fore.RESET}')
    elif member == None:
        embed = discord.Embed(title="Usage:", description="unban <id>", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"unban\"{Fore.RESET}')
    else:
        await ctx.guild.unban(member)
        embed = discord.Embed(description=f'`{member.name}` has been unbanned from `{ctx.guild.name}`', color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"unban\"{Fore.RESET}')

@genocide.command()
async def unbanall(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        embed = discord.Embed(description="Cannot unban in a group chat", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"unbanall\"{Fore.RESET}')
    elif isinstance(ctx.message.channel, discord.DMChannel):
        embed = discord.Embed(description="Cannot unban in DMs", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"unbanall\"{Fore.RESET}')
    else:
        banned_users = await ctx.guild.bans()
        bancount = len(banned_users)
        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.guild.unban(user)
        embed = discord.Embed(description=f'`{bancount}` banned members have been unbanned!', color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"unbanall\"{Fore.RESET}')

@genocide.command()
async def purge(ctx, amount: int = None):
    await ctx.message.delete()
    if amount == None:
        embed = discord.Embed(title="Usage:", description="purge <amount>", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"purge\"{Fore.RESET}')
        return
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"purge\"{Fore.RESET}')
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == genocide.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass

@genocide.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"`{int(ping)} ms`")
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"ping\"{Fore.RESET}')

@genocide.command(aliases=['rtoken', 'dbtoken', 'rdmtoken'])
async def randomtoken(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/bottoken")
    res = r.json()
    embed = discord.Embed(title="Generated a random token.", description=res['token'], color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"randomtoken\"{Fore.RESET}')

@genocide.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in genocide.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)

@genocide.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"geoip\"{Fore.RESET}')
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    embed = discord.Embed(color=0xff0000)
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'Hostname', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
    ]
    for field in fields:
        if field['value']:
            embed.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=embed)

@genocide.command()
async def spam(ctx, amount: int = None, *, message: str = None):
    await ctx.message.delete()
    if amount == None:
        embed = discord.Embed(title="Usage:", description="spam <amount> <message>", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"spam\"{Fore.RESET}')
    elif message == None:
        embed = discord.Embed(title="Usage:", description="spam <amount> <message>", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"spam\"{Fore.RESET}')
    else:
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"spam\"{Fore.RESET}')
        for _i in range(amount):
            await ctx.send(message)

@genocide.command()
async def flood(ctx):
    await ctx.message.delete()
    await ctx.send("\u200b\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\u200b")
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"flood\"{Fore.RESET}')

@genocide.command()
async def pingweb(ctx, website=None):
    await ctx.message.delete()
    if website is None:
        embed = discord.Embed(title="Usage:", description="pingweb <website>", color=0xff0000)
        embed.set_footer(text="http(s) is required in the link!")
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"pingweb\"{Fore.RESET}')
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}{e}{Fore.RESET}")
        if r == 404:
            embed = discord.Embed(description=f'Website is down `{r}`', color=0xff0000)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f'Website is operational `{r}`', color=0xff0000)
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"pingweb\"{Fore.RESET}')

@genocide.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"cum\"{Fore.RESET}')
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(1)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(1)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(1)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(1)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(1)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(1)
    await message.edit(content='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(1)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(1)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')

@genocide.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"9/11\"{Fore.RESET}')
    invis = ""
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')

@genocide.command()
async def hug(ctx, user: discord.User = None, *, args: str = None):
    await ctx.message.delete()
    if user == None:
        embed = discord.Embed(title="Usage:", description="hug <@mention>", color=0xff0000)
        embed.set_footer(text="IDs work too!")
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"hug\"{Fore.RESET}')
        return
    else:
        if args == None:
            r = requests.get("https://nekos.life/api/v2/img/hug")
            res = r.json()
            embed = discord.Embed(description=f'{genocide.user.mention} hugged {user.mention}', color=0xff0000)
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"hug\"{Fore.RESET}')
        else:
            r = requests.get("https://nekos.life/api/v2/img/hug")
            res = r.json()
            embed = discord.Embed(description=f'{genocide.user.mention} hugged {user.mention}\nMessage: \"{args}\"', color=0xff0000)
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"hug\"{Fore.RESET}')

@genocide.command()
async def kiss(ctx, user: discord.User = None, *, args: str = None):
    await ctx.message.delete()
    if user == None:
        embed = discord.Embed(title="Usage:", description="kiss <@mention>", color=0xff0000)
        embed.set_footer(text="IDs work too!")
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"kiss\"{Fore.RESET}')
        return
    else:
        if args == None:
            r = requests.get("https://nekos.life/api/v2/img/kiss")
            res = r.json()
            embed = discord.Embed(description=f'{genocide.user.mention} kissed {user.mention}', color=0xff0000)
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"kiss\"{Fore.RESET}')
        else:
            r = requests.get("https://nekos.life/api/v2/img/kiss")
            res = r.json()
            embed = discord.Embed(description=f'{genocide.user.mention} kissed {user.mention}\nMessage: \"{args}\"', color=0xff0000)
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"kiss\"{Fore.RESET}')

@genocide.command()
async def slap(ctx, user: discord.User = None, *, args: str = None):
    await ctx.message.delete()
    if user == None:
        embed = discord.Embed(title="Usage:", description="slap <@mention>", color=0xff0000)
        embed.set_footer(text="IDs work too!")
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"slap\"{Fore.RESET}')
        return
    else:
        if args == None:
            r = requests.get("https://nekos.life/api/v2/img/slap")
            res = r.json()
            embed = discord.Embed(description=f'{genocide.user.mention} slapped {user.mention}', color=0xff0000)
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"slap\"{Fore.RESET}')
        else:
            r = requests.get("https://nekos.life/api/v2/img/slap")
            res = r.json()
            embed = discord.Embed(description=f'{genocide.user.mention} slapped {user.mention}\nMessage: \"{args}\"', color=0xff0000)
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"slap\"{Fore.RESET}')

@genocide.command()
async def pat(ctx, user: discord.User = None, *, args: str = None):
    await ctx.message.delete()
    if user == None:
        embed = discord.Embed(title="Usage:", description="pat <@mention>", color=0xff0000)
        embed.set_footer(text="IDs work too!")
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"pat\"{Fore.RESET}')
        return
    else:
        if args == None:
            r = requests.get("https://nekos.life/api/v2/img/pat")
            res = r.json()
            embed = discord.Embed(description=f'{genocide.user.mention} patted {user.mention}', color=0xff0000)
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"pat\"{Fore.RESET}')
        else:
            r = requests.get("https://nekos.life/api/v2/img/pat")
            res = r.json()
            embed = discord.Embed(description=f'{genocide.user.mention} patted {user.mention}\nMessage: \"{args}\"', color=0xff0000)
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"pat\"{Fore.RESET}')

@genocide.command()
async def feed(ctx, user: discord.User = None, *, args: str = None):
    await ctx.message.delete()
    if user == None:
        embed = discord.Embed(title="Usage:", description="feed <@mention>", color=0xff0000)
        embed.set_footer(text="IDs work too!")
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"feed\"{Fore.RESET}')
        return
    else:
        if args == None:
            r = requests.get("https://nekos.life/api/v2/img/feed")
            res = r.json()
            embed = discord.Embed(description=f'{genocide.user.mention} fed {user.mention}', color=0xff0000)
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"feed\"{Fore.RESET}')
        else:
            r = requests.get("https://nekos.life/api/v2/img/feed")
            res = r.json()
            embed = discord.Embed(description=f'{genocide.user.mention} fed {user.mention}\nMessage: \"{args}\"', color=0xff0000)
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"feed\"{Fore.RESET}')

@genocide.command()
async def smug(ctx, user: discord.User = None, *, args: str = None):
    await ctx.message.delete()
    if user == None:
        embed = discord.Embed(title="Usage:", description="smug <@mention>", color=0xff0000)
        embed.set_footer(text="IDs work too!")
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"smug\"{Fore.RESET}')
        return
    else:
        if args == None:
            r = requests.get("https://nekos.life/api/v2/img/smug")
            res = r.json()
            embed = discord.Embed(description=f'{genocide.user.mention} looks at {user.mention} with a smug grin', color=0xff0000)
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"smug\"{Fore.RESET}')
        else:
            r = requests.get("https://nekos.life/api/v2/img/smug")
            res = r.json()
            embed = discord.Embed(description=f'{genocide.user.mention} looks at {user.mention} with a smug grin\nMessage: \"{args}\"', color=0xff0000)
            embed.set_image(url=res['url'])
            await ctx.send(embed=embed)
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"smug\"{Fore.RESET}')

@genocide.command()
async def erofeet(ctx):
    await ctx.message.delete()
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"erofeet\"{Fore.RESET}')
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    embed = discord.Embed(color=0xff0000)
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed)

@genocide.command()
async def neko(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/neko")
    res = r.json()
    embed = discord.Embed(color=0xff0000)
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"neko\"{Fore.RESET}')

@genocide.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/dog")
    res = r.json()
    embed = discord.Embed(color=0xff0000)
    embed.set_image(url=res['link'])
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"dog\"{Fore.RESET}')

@genocide.command()
async def cat(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/cat")
    res = r.json()
    embed = discord.Embed(color=0xff0000)
    embed.set_image(url=res['link'])
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"cat\"{Fore.RESET}')

@genocide.command()
async def panda(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/panda")
    res = r.json()
    embed = discord.Embed(color=0xff0000)
    embed.set_image(url=res['link'])
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"panda\"{Fore.RESET}')

@genocide.command()
async def redpanda(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/red_panda")
    res = r.json()
    embed = discord.Embed(color=0xff0000)
    embed.set_image(url=res['link'])
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"redpanda\"{Fore.RESET}')

@genocide.command(aliases=['bird'])
async def birb(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/birb")
    res = r.json()
    embed = discord.Embed(color=0xff0000)
    embed.set_image(url=res['link'])
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"birb\"{Fore.RESET}')

@genocide.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/fox")
    res = r.json()
    embed = discord.Embed(color=0xff0000)
    embed.set_image(url=res['link'])
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"fox\"{Fore.RESET}')

@genocide.command()
async def koala(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/img/koala")
    res = r.json()
    embed = discord.Embed(color=0xff0000)
    embed.set_image(url=res['link'])
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"koala\"{Fore.RESET}')

@genocide.command()
async def dogfact(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/facts/dog")
    res = r.json()
    embed = discord.Embed(title="Dog fact!", description=res['fact'], color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"dogfact\"{Fore.RESET}')

@genocide.command()
async def catfact(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/facts/cat")
    res = r.json()
    embed = discord.Embed(title="Cat fact!", description=res['fact'], color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"catfact\"{Fore.RESET}')

@genocide.command()
async def pandafact(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/facts/panda")
    res = r.json()
    embed = discord.Embed(title="Panda fact!", description=res['fact'], color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"pandafact\"{Fore.RESET}')

@genocide.command()
async def foxfact(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/facts/fox")
    res = r.json()
    embed = discord.Embed(title="Fox fact!", description=res['fact'], color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"foxfact\"{Fore.RESET}')

@genocide.command(aliases=['birdfact'])
async def birbfact(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/facts/bird")
    res = r.json()
    embed = discord.Embed(title="Birb fact!", description=res['fact'], color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"birbfact\"{Fore.RESET}')

@genocide.command()
async def koalafact(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/facts/koala")
    res = r.json()
    embed = discord.Embed(title="Koala fact!", description=res['fact'], color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"koalafact\"{Fore.RESET}')

@genocide.command()
async def meme(ctx):
    await ctx.message.delete()
    r = requests.get("https://some-random-api.ml/meme")
    res = r.json()
    embed = discord.Embed(color=0xff0000)
    embed.set_image(url=res['image'])
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"meme\"{Fore.RESET}')

@genocide.command()
async def pokemon(ctx, *, args = None):
    await ctx.message.delete()
    if args == None:
        r = requests.get(f'https://some-random-api.ml/pokedex?pokemon=pikachu')
        res = r.json()
        embed = discord.Embed(title=res['name'], color=0xff0000)
        embed.add_field(name="Type(s):", value=res['type'], inline=False)
        embed.add_field(name="Abilities:", value=res['abilities'], inline=False)
        embed.add_field(name="Height:", value=res['height'], inline=False)
        embed.add_field(name="Weight:", value=res['weight'], inline=False)
        embed.add_field(name="Gender:", value=res['gender'], inline=False)
        embed.set_image(url=res['sprites']['animated'])
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"pokemon\"{Fore.RESET}')
    else:
        r = requests.get(f'https://some-random-api.ml/pokedex?pokemon={args}')
        res = r.json()
        embed = discord.Embed(title=res['name'], color=0xff0000)
        embed.add_field(name="Type(s):", value=res['type'], inline=False)
        embed.add_field(name="Abilities:", value=res['abilities'], inline=False)
        embed.add_field(name="Height:", value=res['height'], inline=False)
        embed.add_field(name="Weight:", value=res['weight'], inline=False)
        embed.add_field(name="Gender:", value=res['gender'], inline=False)
        embed.set_image(url=res['sprites']['animated'])
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"pokemon\"{Fore.RESET}')

@genocide.command()
async def lyrics(ctx, *, args = None):
    await ctx.message.delete()
    if args == None:
        r = requests.get (f'https://some-random-api.ml/lyrics?title=subway%20sexist') 
        res = r.json()
        embed = discord.Embed(title=res['title'], description=res['lyrics'], color=0xff0000)
        embed.add_field(name="Author(s):", value=res['author'], inline=False)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"lyrics\"{Fore.RESET}')
    else:
        r = requests.get(f'https://some-random-api.ml/lyrics?title={args}')
        res = r.json()
        embed = discord.Embed(title=res['title'], description=res['lyrics'], color=0xff0000)
        embed.add_field(name="Author:", value=res['author'], inline=False)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"lyrics\"{Fore.RESET}')

@genocide.command(aliases=['fakeveryone', 'everyone'])
async def fakeeveryone(ctx, *, args = None):
    if args == None:
        await ctx.message.edit(content="@everyone")
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"fakeeveryone\"{Fore.RESET}')
    elif args != None:
        await ctx.message.edit(content=f'@everyone {args}')
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"fakeeveryone\"{Fore.RESET}')
    else:
        embed = discord.Embed(description="Something went wrong", color=0xff0000)
        await ctx.send(embed=embed)

@genocide.command(aliases=['nothing'])
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(f'\u200b')
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"empty\"{Fore.RESET}')

@genocide.command(aliases=["streaming"])
async def stream(ctx, *, args: str = 'kowalski, analysis...'):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=args,
        url=stream_url, 
    )
    await genocide.change_presence(activity=stream)
    embed = discord.Embed(description=f'You are now streaming `{args}`', color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"stream\"{Fore.RESET}')

@genocide.command(aliases=["play", "playing"])
async def game(ctx, *, args: str = 'with my balls...'):
    await ctx.message.delete()
    game = discord.Game(
        name=args
    )
    await genocide.change_presence(activity=game)
    embed = discord.Embed(description=f'You are now playing `{args}`', color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"game\"{Fore.RESET}')

@genocide.command(aliases=["listen"])
async def listening(ctx, *, args: str = 'to you sleep...'):
    await ctx.message.delete()
    await genocide.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=args, 
        ))
    embed = discord.Embed(description=f'You are now listening to `{args}`', color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"listening\"{Fore.RESET}')

@genocide.command(aliases=["watch"])
async def watching(ctx, *, args: str = 'you through the window...'):
    await ctx.message.delete()
    await genocide.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=args
        ))
    embed = discord.Embed(description=f'You are now watching `{args}`', color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"watching\"{Fore.RESET}')

@genocide.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await genocide.change_presence(activity=None, status=discord.Status.dnd)
    embed = discord.Embed(description="Your status has been reset.", color=0xff0000)
    await ctx.send(embed=embed)
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"stopactivity\"{Fore.RESET}')

@genocide.command(aliases=["mark_as_read", "markasread", "readguild", "ack"])
async def read(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        embed = discord.Embed(description="Cannot use this command in a group chat", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"read\"{Fore.RESET}')
        return
    if isinstance(ctx.message.channel, discord.DMChannel):
        embed = discord.Embed(description="Cannot use this command in DMs", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"read\"{Fore.RESET}')
        return
    if isinstance(ctx.message.channel, discord.TextChannel):
        await ctx.guild.ack()
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"read\"{Fore.RESET}')

@genocide.command()
async def reverse(ctx, *, args: str = None):
    await ctx.message.delete()
    if args == None:
        embed = discord.Embed(title="Usage:", description="reverse <message>", color=0xff0000)
        await ctx.send(embed=embed)
        print(f'{Fore.GREEN}[{Fore.RESET}-{Fore.GREEN}] {Fore.RED}Failed to use command \"reverse\"{Fore.RESET}')
    else:
        message = args[::-1]
        await ctx.send(message)
        print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RED}Used command \"reverse\"{Fore.RESET}')

Init()