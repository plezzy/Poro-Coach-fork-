import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class Scraper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def build(self, ctx, *, champion: str):
        """Devuelve la build recomendada de un campeón (OP.GG)."""
        champion = champion.replace(" ", "").lower()
        url = f"https://www.op.gg/champions/{champion}/build"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        try:
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                return await ctx.send("❌ No se pudo obtener la información (intenta otro campeón).")

            soup = BeautifulSoup(response.text, "html.parser")

            # Buscar items principales
            items = soup.select("div.build-items img")

            if not items:
                return await ctx.send("😿 No encontré información del campeón.")

            item_names = [img["alt"] for img in items[:6]]

            embed = discord.Embed(
                title=f"Build recomendada para {champion.capitalize()}",
                color=discord.Color.purple()
            )

            embed.add_field(
                name="🛡 Items principales",
                value="\n".join([f"- {item}" for item in item_names])
            )

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"⚠️ Error interno: {e}")

async def setup(bot):
    await bot.add_cog(Scraper(bot))
