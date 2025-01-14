import os
import nextcord
import requests
from nextcord.ext import commands
from server import server_on

ADMIN = 'men0name' # ชื่อดิสแอดมิน (กันคนใช้คำสั่ง)


bot = commands.Bot(
    command_prefix='!',
    intents=nextcord.Intents.all(),
    help_command=None
)

class Button(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @nextcord.ui.button(
        label='แสดงรูปภาพ',
        style= nextcord.ButtonStyle.green
    )
    async def send(self, button: nextcord.Button, interaction: nextcord.Interaction):
        msg = await interaction.response.send_message('## > [+] โปรดรอสักครู่...', ephemeral=True)
        api = 'https://api.waifu.pics/nsfw/waifu'

        url = requests.get(api).json()['url']

        await msg.edit(content=f'{url}')


@bot.event
async def on_ready():
    bot.add_view(Button())
    print('Bot Ready!')
    await bot.change_presence(activity=nextcord.Game(name="Random `Anime18+`"))


@bot.command(pass_context = True)
async def StartGen(interaction: nextcord.Interaction):
    await interaction.message.delete()
    if interaction.author.name == ADMIN:
        embed = nextcord.Embed(
            title='คลิกปุ่มเพื่อสุ่มรูปอนิเมะ 18+',
            description='อย่ากดดูบ่อยล่ะ ห่วงสุขภาพ🤗',
            color=None
        )
        embed.set_image(url='https://c.tenor.com/JbnLKar05tAAAAAC/tenor.gif')
        await interaction.send(embed=embed, view=Button())

server_on()

bot.run(os.getenv('TOKEN'))
