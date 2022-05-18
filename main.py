import datetime
import os
import discord
import asyncio
import openpyxl


client = discord.Client()
token = "access_token"

yes = "⭕"
no = "❌"
reactions = [yes, no]


@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")



@client.event
async def on_message(message):
    if message.content == "안녕":
        await message.channel.send("반가워!")

    if message.content == "심심해":
        await message.channel.send("놀아줘~")




    if message.content == "!도움":
        embed = discord.Embed(title="무엇이 궁금하세요?", description="도움이 될만한 사항을 보여드릴게요!", inline=True)
        embed.add_field(name="닉네임 변경", value="양식 ELLA-__-닉네임", inline=True)
        embed.add_field(name="일반 게임", value="[구인구직](https://discord.com/channels/961086567689105479/961090167677026354)", inline=True)
        embed.add_field(name="경쟁 게임", value="[구인구직](https://discord.com/channels/961086567689105479/961090274543677470)", inline=True)



    if message.content == "!ㄱㄱ1":
        embed = discord.Embed(title="일반게임 1", description="같이 할사람?", inline=True)
        embed.add_field(name="⭕", value="[일반게임 1번방으로 가기](https://discord.com/channels/961086567689105479/963404252951220245)", inline=True)




        await message.channel.send(embed=embed)



    if message.content.startswith ("!먹어"):
        i = (message.author.guild_permissions.send_messages)


        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            msg = await message.channel.send(f"**엘라봇이 메세지를 먹었어요!**")
            await asyncio.sleep(5)
            await msg.delete()

        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 엘라봇이 배불러요.".format(message.author.mention))

async def on_member_join(member):
    fmt = '{ELLA CLAN} 에 오신걸 환영합니다!, {0.mention} 님'
    channel = member.server.get_channel("975935345751380008")
    await client.send_message(channel, fmt.format(member, member.server))
    await client.send_message(member, "클랜규정을 꼭 확인해주세요!")

async def on_member_remove(member):
    channel = member.server.get_channel("975935345751380008")
    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
    await client.send_message(channel, fmt.format(member, member.server))

access_token=os.environ["BOT_TOKEN"]
client.run(token)
