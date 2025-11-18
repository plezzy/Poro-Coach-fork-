from discord.ext import commands
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx):
        embed = discord.Embed(
            title="📘 Lista de Comandos — Poro-Coach",
            description="Aquí tienes los comandos disponibles organizados por categoría.",
            color=discord.Color.purple()
        )

        # General
        embed.add_field(
            name="🌟 General",
            value="`!ping` — Latencia\n"
                  "`!team` — Equipo\n"
                  "`!info` — Información del bot",
            inline=False
        )

        # Utility
        embed.add_field(
            name="🧰 Utilidad",
            value="`!avatar @user` — Ver su avatar\n"
                  "`!userinfo @user` — Información del usuario\n"
                  "`!serverinfo` — Info del servidor",
            inline=False
        )

        # Admin
        embed.add_field(
            name="🛠 Admin",
            value="`!clear <n>` — Borra mensajes (requiere permisos)",
            inline=False
        )

        embed.set_footer(text="Poro-Coach | Proyecto académico de Miguel y Juan Pablo")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
