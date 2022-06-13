import discord
from discord import Embed
from discord.ext import commands
from pycord.ext import menus

intents = discord.Intents.all()
intents.members=True
intents.message_content=True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(bot.user.name + ' is online')

class MyEmbedFieldPageSource(menus.ListPageSource):
    def __init__(self, data):
        super().__init__(data, per_page=2)

    async def format_page(self, menu, entries):
        embed = Embed(title="Entries")
        for entry in entries:
            embed.add_field(name=entry[0], value=entry[1], inline=True)
        embed.set_footer(text=f"Page {menu.current_page + 1}/{self.get_max_pages()}")
        return embed


@bot.command()
async def button_embed_field(ctx):
    data = [
        ("Black", "#000000"),
        ("Blue", "#0000FF"),
        ("Brown", "#A52A2A"),
        ("Green", "#00FF00"),
        ("Grey", "#808080"),
        ("Orange", "#FFA500"),
        ("Pink", "#FFC0CB"),
        ("Purple", "#800080"),
        ("Red", "#FF0000"),
        ("White", "#FFFFFF"),
        ("Yellow", "#FFFF00"),
    ]
    pages = menus.ButtonMenuPages(
        source=MyEmbedFieldPageSource(data),
        clear_buttons_after=True,
    )
    await pages.start(ctx)


@discord.slash_command(guild_ids=[882441738713718815])
async def page(ctx: discord.ApplicationContext):
    data = [
        ("Black", "#000000"),
        ("Blue", "#0000FF"),
        ("Brown", "#A52A2A"),
        ("Green", "#00FF00"),
        ("Grey", "#808080"),
        ("Orange", "#FFA500"),
        ("Pink", "#FFC0CB"),
        ("Purple", "#800080"),
        ("Red", "#FF0000"),
        ("White", "#FFFFFF"),
        ("Yellow", "#FFFF00"),
    ]
    pages = menus.ButtonMenuPages(
        source=MyEmbedFieldPageSource(data),
        clear_buttons_after=True,
    )
    await pages.start(ctx)

bot.run("OTUwOTYxODczNzIzOTk4MjM4.YigiQg.ZlxLg4O25G3Kej8ta3sY48hIf0Y")