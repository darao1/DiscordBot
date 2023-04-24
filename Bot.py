import openai
import discord


#after Chat Gpt code
GUILD = "{Dara's Server}"  

client = discord.Client(intents=discord.Intents.default())

#making sure bot is on
@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break

# end (guild is another name for server)
#end of after section
	print(f'{client.user} has connected to Discord!')

#stopping the bot from talking to itself pt3
#@client.event
#async def on_message(message):
#	if message.author = client.user:
#		return 
#	#no matter what else means the bot will respond
	#else:
		#await message.channel.send("Hello!")

		
#	elif client.user.mentioned_in(message):
#		await message.channel.send("It's me!!") 

with open("keys.txt") as f:
	lines = f.read().split('\n')
	openai.api_key = lines[0]
	DISCORD_TOKEN = lines[1]
	#openai.api_base = lines[2]

f.close()

response = openai.ChatCompletion.create(
	model = "gpt-3.5-turbo", 
	messages = [
	{"role": "system", "content": "You are a sassy teenager, who wants the best for everyone."},
    {"role": "assistant", "content": "very sassy tone"},
    {"role": "user", "content": "Best way to make friends?"}
    ]
    )

print(response.choices[0].message.content)

#after
client.run(DISCORD_TOKEN)