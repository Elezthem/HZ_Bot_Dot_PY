import discord
from discord.ext import commands

# Создаем объект бота
bot = commands.Bot(command_prefix='!')

# Событие запуска бота
@bot.event
async def on_ready():
    print(f'Бот запущен как {bot.user.name}')

# Простая команда
@bot.command(name='привет')
async def hello(ctx):
    await ctx.send('Привет!')

# Команда с аргументом
@bot.command(name='показать_аргумент')
async def show_argument(ctx, *, argument):
    await ctx.send(f'Вы передали аргумент: {argument}')

# Обработчик ошибки для команды с аргументом
@show_argument.error
async def argument_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Пожалуйста, укажите аргумент.')

# Запускаем бота с токеном вашего приложения Discord
bot.run('YOUR_BOT_TOKEN')
