from discord.ext import commands
import discord

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def team(self, ctx):
        """Muestra el nombre del equipo."""
        await ctx.send("🔥 Ultra Mega Dream Team 🔥")

    @commands.command()
    async def info(self, ctx):
        """Muestra información básica del bot."""
        embed = discord.Embed(
            title="Poro-Coach",
            description="Tu asistente personal para League of Legends",
            color=discord.Color.blue()
        )

        embed.add_field(name="Versión", value="1.0.0", inline=True)
        embed.add_field(
            name="Desarrolladores",
            value="Miguel Ángel Quintero Puentes\nJuan Pablo Sánchez Ibañez",
            inline=False
        )
        embed.add_field(name="Prefijo", value="!", inline=True)

        embed.set_footer(text="Proyecto educativo basado en discord.py")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))
