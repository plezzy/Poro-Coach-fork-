from discord.ext import commands
import discord

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 5):
        """Borra una cantidad específica de mensajes en el canal."""
        await ctx.channel.purge(limit=amount + 1)
        confirm = await ctx.send(f"🧹 Se eliminaron {amount} mensajes.")
        await confirm.delete(delay=3)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("🚫 No tienes permisos para usar este comando.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("⚠️ Debes especificar un número válido.")
        else:
            await ctx.send("❌ Ocurrió un error inesperado.")

# FUNCIÓN OBLIGATORIA PARA CARGAR EL COG
async def setup(bot):
    await bot.add_cog(Admin(bot))
