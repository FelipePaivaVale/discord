import discord
from discord.ext import commands
import random
from yarl import URL
from pytube import YouTube
import gerador

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='>', case_insensitive = True, intents = intents)

@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_member_join(member):
    canalboasvinda = client.get_channel(1037773857651699755)
    mensagem = await canalboasvinda.send(f"bem vindo {member.mention}!")

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("vez de <@" + str(player1.id) + "> jogar.")
        elif num == 2:
            turn = player2
            await ctx.send("vez de <@" + str(player2.id) + ">' jogar.")
    else:
        await ctx.send("Há um jogo em progresso, finalize antes de iniciar um novo.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                if gameOver == True:
                    await ctx.send(mark + " ganhou!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("empate!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("escolha um numero de 1 a 9 e que não esteja marcado.")
        else:
            await ctx.send("não é sua vez.")
    else:
        await ctx.send("inicie um jogo usando >tictactoe.")

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("mencione 2 pessoas para este comando.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("coloque a posição que deseje marcar.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")
    
@client.command()
async def sorteio(ctx,limite):
    escolha = random.randrange(1,int(limite))
    await ctx.send(f"número escolhido: {escolha}")

@client.command()
async def music(ctx,url):
    VIDEO_URL = (url)
    yt = YouTube(VIDEO_URL)
    audio = yt.streams.filter(only_audio=True)[0]
    await ctx.send(file=discord.File(audio.download()))

@client.command()
async def senha(ctx):
    minu = 'abcdefghijklmnopqrstuvwxyz'
    maiu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '123456789'
    simb = '!@#$%&*()'
    partes = minu + maiu + num + simb
    tamanho = 10
    senha = "".join(random.sample(partes,tamanho))
    await ctx.send(senha)

#de decimal para
@client.command()
async def bi(ctx,nume3):
    nume3 = int(nume3)
    await ctx.send(bin(nume3)[2:])
@client.command()
async def octa(ctx,nume2):
    nume2 = int(nume2)
    await ctx.send(oct(nume2)[2:])
@client.command()
async def hexa(ctx,nume1):
    nume1 = int(nume1)
    await ctx.send(hex(nume1)[2:])

#para decimal
@client.command()
async def hexpdecimal(ctx,nume4):
    nume4 = int(nume4,16)
    await ctx.send(nume4)  

@client.command()
async def octpdecimal(ctx,nume5):
    nume5 = int(nume5,8)
    await ctx.send(nume5)  

@client.command()
async def bipdecimal(ctx,nume6):
    nume6 = int(nume6,2)
    await ctx.send(nume6)

@client.command()
async def cpf(ctx):
    cpf = gerador.generate()
    cpf_formatado = gerador.formater(cpf)
    await ctx.send(cpf_formatado)

@client.command()
async def oi(ctx):
    nome = (ctx.author)
    await ctx.send(f'vai tomar no cu, {nome.mention}')

@client.command()
async def comandos(ctx):
    embed = discord.Embed(
        title ="Todos os comandos da misato",
        description = "somente umas das minhas utilidades!",
        color= discord.Color.red())
    embed.add_field(name="**>TicTacToe**", value="jogue o jogo da velha marcando você e seu amigo para começar", inline=False)
    embed.add_field(name="**>cpf**", value="gere um cpf validado aleatório", inline=False)
    embed.add_field(name="**>senha**", value="gere uma senha de 10 digitos incluindo números, letras e caracteres especiais", inline=False)
    embed.add_field(name="**>music**", value="baixe uma algum video direto do youtube apenas com um link", inline=False)
    embed.add_field(name="**>sorteio**", value="sortei um número até o limite que você definir", inline=False)
    embed.add_field(name="**>bi**", value="transforme um número decimal para binario", inline=False)
    embed.add_field(name="**>octa**", value="transforme um número decimal para octadecimal", inline=False)
    embed.add_field(name="**>hexa**", value="transforme um número decimal para hexadecimal", inline=False)
    await ctx.send(embed=embed)    
client.run('ODU3OTM3MzE2NTM3NTY1MjI0.YNW2Yw.mIgJH05a8dc9Y_0Gcqz7yfWXUmk')
