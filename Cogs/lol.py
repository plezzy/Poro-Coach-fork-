import discord
from discord.ext import commands
import requests
import os

class LoL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # 🔹 Regiones pequeñas (PLATFORM ROUTING)
        # LAN = la1  | LAS = la2 | NA = na1 | BR = br1 | EUW = euw1 | EUNE = eun1 | KR = kr
        self.platform_region = "la1"

        # 🔹 Región grande (REGIONAL ROUTING)
        # LAN, LAS, NA, BR -> americas
        self.regional_region = "americas"

        # 🔹 API Key
        self.api_key = os.getenv("RIOT_API_KEY")

    # ===========================
    #       SUMMONER DATA
    # ===========================
    def get_summoner(self, name):
        """Obtiene información de un invocador por nombre."""
        url = f"https://{self.platform_region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}"
        headers = {"X-Riot-Token": self.api_key}
        r = requests.get(url, headers=headers)
        return r.json() if r.status_code == 200 else None

    @commands.command()
    async def summoner(self, ctx, *, name):
        """Muestra nivel e ID del invocador."""
        data = self.get_summoner(name)

        if data is None:
            return await ctx.send("❌ No encontré ese invocador.")

        embed = discord.Embed(
            title=f"Invocador: {data['name']}",
            color=discord.Color.blue()
        )
        embed.add_field(name="Nivel", value=data["summonerLevel"])
        embed.add_field(name="ID", value=data["id"], inline=False)

        await ctx.send(embed=embed)

    # ===========================
    #       RANKED DATA
    # ===========================
    def get_rank(self, summoner_id):
        url = f"https://{self.platform_region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"
        headers = {"X-Riot-Token": self.api_key}
        r = requests.get(url, headers=headers)
        return r.json() if r.status_code == 200 else None

    @commands.command()
    async def rank(self, ctx, *, name):
        """Muestra el rango de un invocador."""
        summoner = self.get_summoner(name)
        if summoner is None:
            return await ctx.send("❌ No encontré ese invocador.")

        rank_data = self.get_rank(summoner["id"])
        if not rank_data:
            return await ctx.send("❌ Este invocador no tiene rank.")

        ranked = rank_data[0]

        embed = discord.Embed(
            title=f"Rank de {summoner['name']}",
            color=discord.Color.gold()
        )
        embed.add_field(name="Tier", value=f"{ranked['tier']} {ranked['rank']}")
        embed.add_field(name="LP", value=f"{ranked['leaguePoints']} LP")
        wr = round(ranked["wins"] / (ranked["wins"] + ranked["losses"]) * 100)
        embed.add_field(name="Winrate", value=f"{wr}%")

        await ctx.send(embed=embed)

    # ===========================
    #       MASTERIES
    # ===========================
    def get_mastery(self, summoner_id):
        url = f"https://{self.platform_region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}"
        headers = {"X-Riot-Token": self.api_key}
        r = requests.get(url, headers=headers)
        return r.json() if r.status_code == 200 else None

    @commands.command()
    async def mastery(self, ctx, *, name):
        """Muestra los 3 campeones con más maestría."""
        summoner = self.get_summoner(name)
        if summoner is None:
            return await ctx.send("❌ No encontré ese invocador.")

        mastery_data = self.get_mastery(summoner["id"])
        if not mastery_data:
            return await ctx.send("❌ No encontré datos de maestría.")

        top3 = mastery_data[:3]

        embed = discord.Embed(
            title=f"Top 3 Maestrías de {summoner['name']}",
            color=discord.Color.purple()
        )

        for i, champ in enumerate(top3, start=1):
            embed.add_field(
                name=f"#{i} Campeón ID {champ['championId']}",
                value=f"Maestría: {champ['championPoints']}",
                inline=False
            )

        await ctx.send(embed=embed)

    # ===========================
    #       MATCH HISTORY
    # ===========================
    def get_match_list(self, puuid):
        url = f"https://{self.regional_region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?count=5"
        headers = {"X-Riot-Token": self.api_key}
        r = requests.get(url, headers=headers)
        return r.json() if r.status_code == 200 else None

async def setup(bot):
    await bot.add_cog(LoL(bot))
