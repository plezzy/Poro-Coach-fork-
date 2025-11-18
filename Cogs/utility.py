from discord.ext import commands
import discord

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 🔹 Ping mejorado con latencia real
    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"🏓 Pong! Latencia: {latency} ms")

    # 🔹 Avatar de un usuario
    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title=f"Avatar de {member.name}", color=discord.Color.blue())
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)

    # 🔹 Información de un usuario
    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title=f"Información de {member.name}", color=discord.Color.green())
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Cuenta creada", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
        embed.add_field(name="Se unió al servidor", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.send(embed=embed)

    # 🔹 Información del servidor
    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title=f"Servidor: {guild.name}", color=discord.Color.gold())
        embed.add_field(name="Miembros", value=guild.member_count)
        embed.add_field(name="Dueño", value=guild.owner.mention)
        embed.set_thumbnail(url=guild.icon.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))
