# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

# Leer variables de entorno
TOKEN = os.getenv("DISCORD_TOKEN")  # 👈 debe coincidir con el nombre en tu archivo .env
PREFIX = os.getenv("PREFIX", "!")

# Verificar si el token se cargó
print("TOKEN desde .env:", TOKEN is not None)  # solo dirá True/False, sin mostrarlo

# Configurar permisos básicos (intents)
intents = discord.Intents.default()
intents.message_content = True

# Crear el bot
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 ¡Pong!")

# Ejecutar el bot
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ ERROR: No se pudo leer el token desde .env")
