import discord
from discord.ext import commands
from scrapers.champion_scraper import load_champions

class ChampionsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="champions", help="Muestra la lista de campeones scrapeados.")
    async def champions(self, ctx):
        await ctx.send("⏳ Obteniendo datos de campeones, esto puede tardar...")

        champs = load_champions()

        text = "\n".join([f"- **{c['name'].title()}** ({c['category']})" for c in champs])
        await ctx.send(f"**Campeones encontrados:**\n{text}")

async def setup(bot):
    await bot.add_cog(ChampionsCog(bot))
