import discord
question=""
key=""
import random
import algorithm
import typefinderfill
import responsesfill
bot = discord.Client()
chat = bot.get_channel(850968229677367326)

username = ['alpha212', 'techie112', 'cooldude334', 'dumbman38', 'yoyoman133', 'dumbotuser1212', 'dominictorreto69', 'bitchman420']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
movies = ['Fast and furious tokyo drift', 'Interstellar', 'Venom', 'Predator', 'Avengers Endgame']
friends = ['Rachel', 'Ross', 'Joey', 'Phoebe']
tbbt = ['Sheldon', 'Leonard', 'Amy', 'Bernadette', 'Penny', 'Rajesh']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','November','December','October']
mine = ['Steve', 'Cow', 'Creeper', 'Zombie', 'Trader', 'Skeleton', 'Llamas', 'Spider', 'Enderman', 'Pig', 'Rabbit']
drink = ['Sprite', 'Coca Cola', 'Fanta', 'Tea', 'Coffee', 'Fruit Juice', 'Ask your girlfriend', 'Water', 'Bitch you are obese']
music = ['Ritviz' , 'twenty one pilots', 'Ed Sheeran', 'Arijit Singh', 'Eminem', 'A R Rahman', 'The Weeknd', 'Alan Walker']
song = ['Stressed out', 'Rap God', 'Blinding Lights', 'Dynamite', 'Kun faya Kun', 'Teriyaki boys', 'See you Again', 'Good Life', 'Birthday Suit']

@bot.event
async def on_ready():
    chat=bot.get_channel(850968229677367326)
    await chat.send("Hello Martians")
    chat=bot.get_channel(851408196723539998)
    await chat.send("Ask a question")
@bot.event
async def on_disconnect():
    chat=bot.get_channel(850968229677367326)
    await chat.send("I Will be Back!!")
@bot.event
async def on_message(message):
    Message=message.content.replace("?","")
    Message=message.content.replace("!","")
    if message.author.name != "DumBot":
        if(message.channel.id==851408196723539998):
            global key
            if key=="":
                key=typefinderfill.filltype(Message)
                chat=bot.get_channel(851408196723539998)
                await chat.send("whats the answer then?")
            else:
                responsesfill.fillresponse(key,Message)
                chat=bot.get_channel(851408196723539998)
                key=""
                await chat.send("ok")
                await chat.send("Ask a question")
        if(message.channel.id==850968229677367326):
            Message=message.content.lower()
            if(Message=="buy dogecoin"):
                chat=bot.get_channel(850968229677367326)
                await chat.send("https://www.binance.com/en/buy-Dogecoin-Doge")
            elif(Message=="monkey"):
                chat=bot.get_channel(850968229677367326)
                await chat.send("<https://www.pinterest.com/pin/717479784385119788/>")
            elif (Message == "what song should i listen to"):
                chat = bot.get_channel(850968229677367326)
                await chat.send(random.choice(song))
            elif (Message == "whom should i listen to"):
                chat = bot.get_channel(850968229677367326)
                await chat.send(random.choice(music))
            elif (Message == "suggest me a drink"):
                chat = bot.get_channel(850968229677367326)
                await chat.send(random.choice(drink))
            elif (Message == "what am i from minecraft"):
                chat = bot.get_channel(850968229677367326)
                await chat.send(random.choice(mine))
            elif (Message == "ygrr"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("<https://www.youtube.com/watch?v=xvFZjo5PgG0>")
            elif (Message == "do a barrel roll"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("<https://elgoog.im/doabarrelroll/?10000>")
                # help cmds
            elif (Message == "covid19"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("https://www.who.int/")
            elif (Message == "prevent covid"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("https://www.cowin.gov.in/home")
            elif (Message == "covid19 help"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("https://discord.gg/kza7e4Jz")
            elif (Message == "what is covid 19"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Covid 19 is a SarS-Cov2 Virus")
            elif (Message == "how does it spread"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("It spreads through touch, cough, contact with an infected person")
            elif (Message == "can mosquito spread covid19"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("No, It spreads through touch, cough, contact with an infected person")
            elif (Message == "how can i protect myself"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("By wearing masks, using sanitizers, maintaining social distancing")
            elif (Message == "are vaccines safe"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Yes")
            elif (Message == "whatif i contract covid19"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Follow instructions given by doctors\n"
                                "isolate yourself\n"
                                "take proper nutrition")
            elif (Message == "any alphabet"):
                chat = bot.get_channel(850968229677367326)
                await chat.send(random.choice(alphabet))
            elif (Message == "give me a username"):
                chat = bot.get_channel(850968229677367326)
                await chat.send(random.choice(username))
            elif (Message == "roll the dice"):
                chat = bot.get_channel(850968229677367326)
                await chat.send(random.randint(1, 6))
            elif (Message == "how do i learn guitar"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Watch Justin Guitar tutorials.")
            elif (Message == "should i learn guitar"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Maybe")
            elif (Message == "guess the number"):
                chat = bot.get_channel(850968229677367326)
                await chat.send(random.randint(0, 10))
            elif (Message == "should i buy cryptocurrency"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Don't buy them mine them")
            elif (Message == "tell me a month"):
                chat = bot.get_channel(850968229677367326)
                await chat.send(random.choice(months))
            elif (Message == "guess my name"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("check your email id")
                # capitals
            elif (Message == "what is the capital of india"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("New Delhi")
            elif (Message == "what is the capital of usa"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Washington D C")
            elif (Message == "what is the capital of russia"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Moscow")
            elif (Message == "what is the capital of canada"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Ottawa")
            elif (Message == "what is the capital of russia"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Moscow")
            elif (Message == "what is the capital of japan"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Tokyo")
            elif (Message == "what is the capital of china"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Beijing")
            elif (Message == "what is the capital of uk"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("London")
            elif (Message == "what is the capital of france"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Paris")
            elif (Message == "what is the capital of spain"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Madrid")
            elif (Message == "what is the capital of portugal"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Lisbon")
            elif (Message == "what is the capital of uae"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Abu Dhabi")
            elif (Message == "what is the capital of mexico"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Mexico City")
            elif (Message == "what is the capital of saudi arabia"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Riyadh")
            elif (Message == "what is the capital of australia"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Canberra")
            elif(Message == "what is the capital of bangladesh"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Dhaka")
            elif (Message == "what is the capital of pakistan"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Islamabad")
            elif (Message == "what is the capital of taiwan"):
                chat = bot.get_channel(850968229677367326)
                await chat("Taipei")
            elif (Message == "what is the capital of thailand"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Bangkok")
            elif (Message == "what is the capital of brazil"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Brasilia")
            elif (Message == "what is the capital of argentina"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Bueneos Aires")
            elif (Message == "what is the capital of germany"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Berlin")
            elif (Message == "what is the capital of italy"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Rome")
            elif (Message == "what is the capital of poland"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Warsaw")
            elif (Message == "what is the capital of south africa"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Johannesburg")
            elif (Message == "what is the capital of egypt"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Cairo")
            elif (Message == "what is the capital of qatar"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Doha")
            elif (Message == "what is the capital of yemen"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Yana")
            elif (Message == "what is the capital of oman"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Muscat")
            elif (Message == "what is the capital of singapore"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Singapore City")
            elif (Message == "what is the capital of israel"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Jerusalem")
            elif (Message == "what is the capital of mongolia"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Ulaan Bataar")
            elif (Message == "what is the capital of malayasia"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Kuala Lumpur")
            elif (Message == "what is the capital of indonesia"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Jakarta")
            elif (Message == "what is the capital of italy"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Rome")
            elif (Message == "what is the capital of italy"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Rome")
            elif (Message == "suggest me a story book"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Malgudi Days")
            elif (Message == "suggest me a sad movie"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("The Fault in our Stars")
            elif (Message == "tell me a fact"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("When the moon is directly overhead, you will weigh slightly less.")
            elif (Message == "tell me a another fact"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("I Am is the shortest complete sentence in the English language.")
            elif (Message == "tell me an indian capital"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Karnataka - Bangalore")
            elif (Message == "do you belive in god"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Yes")
            elif (Message == "when will covid19 end"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("When you start wearing masks")
            elif (Message == "do you laugh"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("HeHe🤣")
            elif (Message == "why did they make you"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Its a tough question")
            elif (Message == "suggest me a movie"):
                chat = bot.get_channel(850968229677367326)
                await chat.send(random.choice(movies))
            elif (Message == "what is mitochodria"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("its the powerhouse of the cell")
            elif (Message == "what is the einstein equation"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("E = mc^2")
            elif (Message == "who made evolution"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Charles Darwin")
            elif (Message == "science quote"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("give me a lever and i shall move the world - Archimedes")
            elif (Message == "what is newton's 3rd law"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("every action has equal and opposite reaction")
            elif (Message == "what is newton's 2rd law"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("rate of momentum is directly propotional to applied unbalanced force")
            elif (Message == "which is the liquid metal"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("mercury")
            elif (Message == "tell me one character from friends"):
                chat = bot.get_channel(850968229677367326)
                await chat.send(random.choice(friends))
            elif (Message == "tell me one character from big bang theory"):
                chat = bot.get_channel(850968229677367326)
                await chat.send(random.choice(tbbt))
            elif (Message == "tell me a joke"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Who kept the second leg on moon \nIts Neil Armstrong himself because he wasn't handicapped.LOL")
            elif (Message == "suggest me a book"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("The Alchemist by Paulo Cohelo")
            elif (Message == "suggest me a action movie"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Terminator 2 Judgement Day")
            elif (Message == "when were you born"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("26 May 2021")
            elif (Message == "who is your favourite singer"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Ritviz")
            elif (Message == "tell me a secret"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("my developers are way too lazy")
            elif (Message == "are you a real person"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("may or may not be :)")
            elif (Message == "memes1"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("https://i.kym-cdn.com/editorials/icons/mobile/000/002/795/time_travel.jpg")
            elif (Message == "memes2"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("https://knowyourmeme.com/photos/2113348-haha-jonathan-you-are-banging-my-daughter")
            elif (Message == "memes3"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("https://i.kym-cdn.com/photos/images/newsfeed/002/114/558/277.jpg")
            elif (Message == "😊"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("😊")
            elif (Message == "😂"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("🤣")
            elif (Message == "❤"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("xOxO")
            elif (Message == "😎"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Nice Shades!")
            elif (Message == "😃"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("😀")
            elif (Message == "😅"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("Oops!!")
            elif (Message == "😋"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("😋")
            elif (Message == "😖"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("why are you scared???🤔")
            elif (Message == "😆"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("HaHaHa, nice one!!!😄")
            elif (Message == "🤩"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("starry eyes..🤩")
            elif (Message == "🤑"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("money!!😋")
            elif (Message == "😤"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("😧 what happened")
            elif (Message == "🥵"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("why are you hot??")
            elif (Message == "🤓"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("you look smart!!!")
                # embeds
            elif (Message == "who are your developer"):
                chat = bot.get_channel(850968229677367326)
                myEmbed1 = discord.Embed(title="Current developers", description="Adithya and Vineeth", color=0x00ff00)
                myEmbed1.add_field(name="Registered Under", value="Skripton", inline=False)
                myEmbed1.add_field(name="Created on:", value="May 24, 2021", inline=False)
                myEmbed1.set_footer(text="Beta.Ver 1.00.25")
                await chat.send(embed=myEmbed1)
            elif (Message == "commands"):
                chat = bot.get_channel(850968229677367326)
                myEmbed2 = discord.Embed(title="Custom Commands", color=0xff0000)
                myEmbed2.add_field(name="Meme commands", value=" monkey \n"
                                                            " do a barrel roll\n"
                                                            "  ygrr ", inline=True)
                myEmbed2.add_field(name="Help commands", value=" covid19 \n"
                                                            " prevent covid\n"
                                                            " covid19 help ", inline=True)
                myEmbed2.set_footer(text="Ver 1.00.25")
                await chat.send(embed=myEmbed2)
            elif (Message == "profile_dev1"):
                chat = bot.get_channel(850968229677367326)
                myEmbed3 = discord.Embed(title="Adithya P S", description="Developer at Skripton", color=0xFF00FF)
                myEmbed3.add_field(name="ID", value="756415043679158324")
                myEmbed3.set_thumbnail(url="https://image.shutterstock.com/image-vector/light-bulb-rays-shine-energy-260nw-1300389562.jpg")
                await chat.send(embed=myEmbed3)
            elif (Message == "minecraft tip"):
                chat = bot.get_channel(850968229677367326)
                myEmbed3 = discord.Embed(title="Minecraft Tip", description="The best fuel source is Lava it can smelt 100 items.", color=0xFF00FF)
                myEmbed3.set_thumbnail(url="https://www.freepnglogos.com/uploads/minecraft-logo-17.png")
                await chat.send(embed=myEmbed3)
            elif (Message == "profile_dev2"):
                chat = bot.get_channel(850968229677367326)
                myEmbed3 = discord.Embed(title="Vineeth Rao", description="CEO at Skripton", color=0x0000FF)
                myEmbed3.add_field(name="ID", value="724847448950046720")
                myEmbed3.set_thumbnail(url="https://image.shutterstock.com/image-vector/light-bulb-rays-shine-energy-260nw-1300389562.jpg")
                await chat.send(embed=myEmbed3)
            elif (Message == "games"):
                chat = bot.get_channel(850968229677367326)
                myEmbed4 = discord.Embed(title="Gamelinks", description="Mobile Games", color=0xFFFF00)
                myEmbed4.add_field(name="PUBG Mobile", value="https://bit.ly/3fMwCtX", inline=False)
                myEmbed4.add_field(name="Minecraft Ver 1.11.00.42", value="https://bit.ly/3bSljPV", inline=False)
                myEmbed4.add_field(name="Among Us Mod", value="https://bit.ly/2Tqf1kh", inline=False)
                await chat.send(embed=myEmbed4)
            elif (Message == "memes"):
                chat = bot.get_channel(850968229677367326)
                myEmbed5 = discord.Embed(title="Memes", color=0x00FFFF)
                myEmbed5.add_field(name="Meme Link", value="https://memes.com/")
                myEmbed5.set_thumbnail(url="https://images.pexels.com/photos/321552/pexels-photo-321552.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
                await chat.send(embed=myEmbed5)
            elif (Message == "skripton"):
                chat = bot.get_channel(850968229677367326)
                myEmbed6 = discord.Embed(title="Recent Videos by ", description="Skripton",color=0x5E1489)
                myEmbed6.add_field(name="I made a book scream", value="https://www.youtube.com/watch?v=v3fLWR9JQQI")
                myEmbed6.add_field(name="Google Car", value="https://www.youtube.com/watch?v=XiKroaBnu70")
                myEmbed6.add_field(name="I made a Whatsapp Bot", value="https://www.youtube.com/watch?v=t0A8Zhpb-X8")
                await chat.send(embed=myEmbed6)
            elif (Message == "pc games"):
                chat = bot.get_channel(850968229677367326)
                myEmbed7 = discord.Embed(title="PC Games ", description="Not Verelified", color=0x6A23E5)
                myEmbed7.add_field(name="FelifA 21", value="https://gamingbeasts.com/felifa-21-pc-free-game-download/")
                myEmbed7.add_field(name="GTA V", value="https://se7en.ws/gta-v/?lang=en")
                myEmbed7.add_field(name="Resident Evil 4", value="https://worldofpcgames.co/resident-evil-4-free-download/")
                myEmbed7.set_thumbnail(url="https://images.pexels.com/photos/4522999/pexels-photo-4522999.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
                await chat.send(embed=myEmbed7)
            elif (Message == "adrenaline"):
                chat = bot.get_channel(850968229677367326)
                myEmbed8 = discord.Embed(title="Adrenaline Rush playlist ", description="Handpicked Songs", color=0xFFEC00)
                myEmbed8.add_field(name="Rap God by Eminem",value="https://www.spotelify.com/us/")
                myEmbed8.add_field(name="Venom by Eminem",value="https://www.spotelify.com/us/")
                myEmbed8.add_field(name="Godzilla by Juice WRLD ",value="https://www.spotelify.com/us/")
                myEmbed8.add_field(name="Gangster Paradise by Coolie",value="https://www.spotelify.com/us/")
                myEmbed8.add_field(name="We Will Rock You by Queen",value="https://www.spotelify.com/us/")
                myEmbed8.set_thumbnail(url="https://images.pexels.com/photos/675960/mic-music-sound-singer-675960.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
                await chat.send(embed=myEmbed8)
                # please change the hexadecimal color code accordingly from embed8 and embed9
            elif (Message == "pop"):
                chat = bot.get_channel(850968229677367326)
                myEmbed9 = discord.Embed(title="Old and New Pop ", description="Handpicked Songs", color=0x009000)
                myEmbed9.add_field(name="Self Control by Laura Branigan",value="https://www.spotelify.com/us/")
                myEmbed9.add_field(name="Blinding Lights by The Weeknd",value="https://www.spotelify.com/us/")
                myEmbed9.add_field(name="MONTERO by Lil Nas X",value="https://www.spotelify.com/us/")
                myEmbed9.add_field(name="Dynamite by BTS",value="https://www.spotelify.com/us/")
                myEmbed9.add_field(name="Mood by 24kGoldn",value="https://www.spotelify.com/us/")
                myEmbed9.set_thumbnail(url="https://images.pexels.com/photos/675960/mic-music-sound-singer-675960.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
                await chat.send(embed=myEmbed9)
            elif (Message == "sad"):
                chat = bot.get_channel(850968229677367326)
                myEmbed10 = discord.Embed(title="Sad Songs ", description="Handpicked Songs", color=0x444444)
                myEmbed10.add_field(name="Drivers Licence by Olivia Rodrigo",value="https://www.spotelify.com/us/")
                myEmbed10.add_field(name="Tears from Heaven by Eric Clapton",value="https://www.spotelify.com/us/")
                myEmbed10.add_field(name="See you Again by Wiz Khalifa ",value="https://www.spotelify.com/us/")
                myEmbed10.add_field(name="Hurt by Johnny Cash" ,value="https://www.spotelify.com/us/")
                myEmbed10.set_thumbnail(url="https://images.pexels.com/photos/675960/mic-music-sound-singer-675960.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")
                await chat.send(embed=myEmbed10)
            elif (Message == "music commands"):
                chat = bot.get_channel(850968229677367326)
                myEmbed11 = discord.Embed(title="Music Recommendation Commands ", description="Type these to receive "
                                                                                            "handpicked songs", color=0xFF00FF)
                myEmbed11.add_field(name="sad",value="Sad songs")
                myEmbed11.add_field(name="pop",value="Old and new pop")
                myEmbed11.add_field(name="adrenaline ",value="Top Adrenaline rush songs")
                await chat.send(embed=myEmbed11)
            elif (Message == "what is your version"):
                chat = bot.get_channel(850968229677367326)
                myEmbed12 = discord.Embed(title="Current Version", description="Beta.Ver 1.00.25", color=0x00ff00)
                myEmbed12.add_field(name="Next Update on", value="August 2021", inline=False)
                myEmbed12.add_field(name="Created on:", value="May 24, 2021", inline=False)
                await chat.send(embed=myEmbed12)
            elif (Message == "new word"):
                chat = bot.get_channel(850968229677367326)
                myEmbed13 = discord.Embed(title="BENEVOLET", description="Charitable, Performing good deeds", color=0x0000FF)
                myEmbed13.add_field(name="New Words Every Week", value="Source:merriam_webster", inline=False)
                await chat.send(embed=myEmbed13)
            elif (Message == "covid19 faq"):
                chat = bot.get_channel(850968229677367326)
                myEmbed13 = discord.Embed(title="COVID19 FAQ", description="Type these to get results", color=0x0000FF)
                myEmbed13.add_field(name="Frequent Questions", value="#1 what is covid 19\n"
                                                                    "#2 how does it spread\n"
                                                                    "#3 how can i protect myself\n"
                                                                    "#4 is it okay to donate blood\n"
                                                                    "#5 are vaccines safe\n"
                                                                    "#5 what if i contract covid19", inline=True)
            elif (Message == "bot help"):
                chat = bot.get_channel(850968229677367326)
                myEmbed15 = discord.Embed(title="Troubleshooting and FAQs", description="If the question is missing type\n"
                                                                                        "Question and we will reach out to you.", color=0x00ff00)
                myEmbed15.add_field(name="Bot doesn't respond", value="The reason for this is either the bot offline\n"
                                                                    "or the question you have typed is not present/wrong.", inline=False)
                myEmbed15.add_field(name="Bot gives wrong reply", value="This is because a programming error.", inline=False)
                myEmbed15.add_field(name="Command Help", value="Type in general commands f1 for Ai chats", inline=False)
                myEmbed15.add_field(name="It spams or gives same output", value="Report to the developer or\n"
                                                                                "if utmost necessary KICK the bot", inline=False)
                myEmbed15.add_field(name="For any of the Above", value="Report or Tg the Developer", inline=False)
                await chat.send(embed=myEmbed15)
            elif (Message == "general commands f1 for ai chats"):
                chat = bot.get_channel(850968229677367326)
                myEmbed14 = discord.Embed(title="General and Specific Commands", description="Type these in LOWER CASE letters", color=0xF000FF)
                myEmbed14.add_field(name="who are your developer", value="Developer Information", inline=False)
                myEmbed14.add_field(name="commands", value="Specific Commands", inline=False)
                myEmbed14.add_field(name="profile_dev1", value="Developer Profile", inline=False)
                myEmbed14.add_field(name="profile_dev2", value="Developer Profile", inline=False)
                myEmbed14.add_field(name="games", value="Links to Mobile Games", inline=False)
                myEmbed14.add_field(name="memes", value="Meme Page Link", inline=False)
                myEmbed14.add_field(name="new word", value="Add to your Vocabulary", inline=False)
                myEmbed14.add_field(name="what is your version", value="Version Information", inline=False)
                myEmbed14.add_field(name="music commands", value="Music Recommendations", inline=False)
                myEmbed14.add_field(name="skripton", value="Channel Information", inline=False)
                myEmbed14.add_field(name="pc games", value="Super Cool PC Games", inline=False)
                myEmbed14.add_field(name="Ask Science Questions", value="e.g:what is the einstein equation\n"
                                                                        "who made evolution", inline=False)
                myEmbed14.add_field(name="Ask Capitals", value="Major World Capitals\n"
                                                            "what is the capital of -country-", inline=False)
                myEmbed14.add_field(name="Ask Suggestions or General Questions", value="e.g:do you belive in god\n"
                                                                                    "suggest me a good movie", inline=False)
                myEmbed14.add_field(name="Rules to be Followed", value="Use correct form of comprehension\n"
                                                                    "Don't use punctuation\n"
                                                                    "Limited Database may not answer your question\n"
                                                                    "it can even reply emojis\n"
                                                                    "Do not overlap the questions\n"
                                                                    "The bot is still under development", inline=False)
                myEmbed14.add_field(name="covid19 faq", value="FAQ about covid19", inline=False)
                myEmbed14.add_field(name="Dumbot can roll dice", value="Type 'roll the dice'", inline=False)
                myEmbed14.add_field(name="Ask any Alphabet", value="Type 'any alphabet'", inline=False)
                myEmbed14.add_field(name="Guesser", value="Type 'guess the number'\n"
                                                        "and think of any number between 1 to 10\n"
                                                        "and it will guess it.", inline=False)
                myEmbed14.add_field(name="bot help", value="It provides you the troubleshooting\n"
                                                        "and FAQs about the Bot.", inline=False)
                myEmbed14.add_field(name="dumbcoin introduction", value="Provides you Information about\n"
                                                                        "DumbCoin.", inline=False)
                myEmbed14.add_field(name="news", value="Provides you latest news", inline=False)
                myEmbed14.add_field(name="memes1\memes2\memes3", value="Provides you funniest memes", inline=False)
                myEmbed14.add_field(name="Ask characters from F.R.I.E.N.D.S or Big Bang Theory", value="tell me one character from -insert show-", inline=False)
                myEmbed14.add_field(name="It can tell you a month", value="Type tell me a month", inline=False)
                myEmbed14.add_field(name="Check what are you from minecraft", value="Type what am i form minecraft", inline=False)
                myEmbed14.add_field(name="It can provide useful minecraft tips", value="Type minecraft tip", inline=False)
                myEmbed14.add_field(name="what song should i listen to", value="Good Old Songs", inline=False)
                myEmbed14.add_field(name="whom should i listen to", value="Favourite Authors", inline=False)
                myEmbed14.add_field(name="suggest me a drink", value="Suggests you a Drink", inline=False)
                myEmbed14.add_field(name="give me a username", value="Gives you a temporary Username", inline=False)
                myEmbed14.add_field(name="suggest me a movie", value="Movies", inline=False)
                await chat.send(embed=myEmbed14)
            elif (Message == "news"):
                chat = bot.get_channel(850968229677367326)
                myEmbed12 = discord.Embed(title="", description="", color=0x00ff00)
                myEmbed12.add_field(name="Petrol/Diesel Price Hikes", value="https://www.msn.com/en-in/money/news/petrol-diesel-prices-at-all-time-high-after-fresh-hike-check-latest-rates/ar-AAKH0Kx?ocid=uxbndlbing", inline=False)
                myEmbed12.add_field(name="Monsoon to start by Tomorrow", value="https://www.msn.com/en-in/news/other/monsoon-to-reach-tamil-nadu-coastal-karnataka-by-tomorrow/ar-AAKGQMn?ocid=BingNews", inline=False)
                myEmbed12.add_field(name="12th Board Cancellation", value="https://www.msn.com/en-in/news/other/pm-took-student-centric-step-in-cancelling-class-12-exams/ar-AAKGk91?ocid=BingNews")
                await chat.send(embed=myEmbed12)
            elif (Message == "dumbcoin"):
                chat = bot.get_channel(850968229677367326)
                myEmbed1 = discord.Embed(title="Welcome to DumbCoin", description="DumbCoin is a non valued cryptocurrency\n"
                                                                                "Used in the Dumbot server\n"
                                                                                "You can buy them, sell or hold them\n"
                                                                                "There are lots of option added for your\n"
                                                                                "Convenience.\n"
                                                                                "Most of your DumbCoin earning are through\n"
                                                                                "chats and active participation.", color=0x00ff00)
                myEmbed1.add_field(name="Commands for Cryptocurrency", value="Use PREFIX '$'", inline=False)
                myEmbed1.add_field(name="Commands", value="$add\n"
                                                        "$sell\n"
                                                        "$withdraw\n"
                                                        "$open account\n"
                                                        "$giveaway\n"
                                                        "$value", inline=False)

                myEmbed1.add_field(name="$add", value="This command adds DumbCoin to your account", inline=False)
                myEmbed1.add_field(name="$sell", value="This command reduces you account balance", inline=False)
                myEmbed1.add_field(name="$withdraw", value="This command helps you convert amount to dollars", inline=False)
                myEmbed1.add_field(name="$open account", value="This command opens a new crypto wallet for you", inline=False)
                myEmbed1.add_field(name="$giveaway", value="This command is a lottery chance", inline=False)
                myEmbed1.add_field(name="$value", value="This command show the value graph of the cryptocurrency", inline=False)
                myEmbed1.set_thumbnail(url="https://pixabay.com/illustrations/blockchain-bitcoin-bit-coin-3041480/")
                myEmbed1.add_field(name="Dumbot.Inc", value="✔", inline=False)
                myEmbed1.set_footer(text="Ver 1.25")
                await chat.send(embed=myEmbed1)

            elif (Message == "$add"):
                chat = bot.get_channel(850968229677367326)
                myEmbed1 = discord.Embed(title="DumbCoin Transfer", description="Adding DumbCoins to your Account...\n"
                                                                                "Please Select the Denominations\n"
                                                                                "100 DumbCoins\n"
                                                                                "200 DumbCoins\n"
                                                                                "500 DumbCoins", color=0x00ff00)
                myEmbed1.add_field(name="How to Add", value="$add -denomination- dumbcoins", inline=False)
                myEmbed1.add_field(name="Dumbot.Inc", value="💲", inline=False)
                await chat.send(embed=myEmbed1)

            elif (Message == "$add 100 dumbcoins"):
                chat = bot.get_channel(850968229677367326)
                myEmbed1 = discord.Embed(title="Adding 100 Dumbcoins", description="Adding Amount to your Account...",color=0x00ff00)
                myEmbed1.set_footer(text="Amount will be Added within 2 Days")
                await chat.send(embed=myEmbed1)
            elif (Message == "$add 200 dumbcoins"):
                chat = bot.get_channel(850968229677367326)
                myEmbed1 = discord.Embed(title="Adding 200 Dumbcoins", description="Adding Amount to your Account...",color=0x00ff00)
                myEmbed1.set_footer(text="Amount will be Added within 2 Days")
                await chat.send(embed=myEmbed1)
            elif (Message == "$add 300 dumbcoins"):
                chat = bot.get_channel(850968229677367326)
                myEmbed1 = discord.Embed(title="Adding 300 Dumbcoins", description="Adding Amount to your Account...",color=0x00ff00)
                myEmbed1.set_footer(text="Amount will be Added within 2 Days")
                await chat.send(embed=myEmbed1)

            elif (Message == "$sell"):
                chat = bot.get_channel(850968229677367326)
                myEmbed1 = discord.Embed(title="Selling Dumbcoin", description="Reducing Amount from your Account...", color=0x00ff00)
                myEmbed1.set_footer(text="Amount will be reduced within 2 Days")
                myEmbed1.add_field(name="Dumbot.Inc", value="❎", inline=False)
                await chat.send(embed=myEmbed1)

            elif (Message == "$withdraw"):
                chat = bot.get_channel(850968229677367326)
                myEmbed1 = discord.Embed(title="Withdrawing Dumbcoin", description="Converting Amount from your Account...",color=0x00ff00)
                myEmbed1.add_field(name="Only 100  DumbCoins will be debited", value="")
                myEmbed1.set_footer(text="Amount will be Converted within 2 Days")
                myEmbed1.add_field(name="Dumbot.Inc", value="💱", inline=False)
                await chat.send(embed=myEmbed1)


            elif (Message == "$open account"):
                chat = bot.get_channel(850968229677367326)
                myEmbed1 = discord.Embed(title="New Account Opening", description="The new account shall be opened in 2-3 Days\n"
                                                                                "Add your name and the amount you want to start\n"
                                                                                "with and tag the Developer.",color=0x00ff00)
                myEmbed1.add_field(name="Dumbot.Inc", value="🌐", inline=False)
                myEmbed1.add_field(name="NOTE", value="Your Account will close after 1 month", inline=False)
                myEmbed1.set_footer(text="Ver 1.25")
                await chat.send(embed=myEmbed1)

            elif (Message == "$giveaway"):
                chat = bot.get_channel(850968229677367326)
                myEmbed1 = discord.Embed(title="Giveaway option is currently under Development", description="It shall be functioning in the\n"
                                                                                                            "next update of Dumbot",color=0x00ff00)
                await chat.send(embed=myEmbed1)

            elif (Message == "$value"):
                chat = bot.get_channel(850968229677367326)
                await chat.send("1 DBC = $0.50")

            elif (Message == "$warning"):
                chat = bot.get_channel(850968229677367326)
                myEmbed1 = discord.Embed(title="DumbCoin Cautions", description="Regulations to DumbCoin", color=0x00ff00)
                myEmbed1.add_field(name="#1", value="Do not overclock the DumbCoin System.")
                myEmbed1.add_field(name="#2", value="Current System can handle only 5 DumbCoin Wallets/Accounts.")
                myEmbed1.add_field(name="#3", value="The Transfer/Withdraw process may take sometime.")
                myEmbed1.add_field(name="#4", value="Most of the real life values are imaginary.")
                myEmbed1.add_field(name="#5", value="The account opening fuction needs human interaction\n"
                                                    "so please follow the steps and wait.")
                myEmbed1.set_footer(text="DumbCoins will be transferred within 2 Days")
                myEmbed1.add_field(name="Dumbot.Inc", value="🚫", inline=False)
                await chat.send(embed=myEmbed1)

            elif (Message == "$account_adithya"):
                chat = bot.get_channel(850968229677367326)
                myEmbed1 = discord.Embed(title="DumbCoin Account Holder", description="Adithya",color=0x00ff00)
                myEmbed1.add_field(name="Available Balance", value="150 DBC", inline=False)
                myEmbed1.add_field(name="Balance in Dollars", value="$0.0000", inline=False)
                myEmbed1.add_field(name="Last Transaction", value="4/6/2021", inline=False)
                myEmbed1.add_field(name="DumbCoin HelpCenter", value="If any unknown\n"
                                                                    "unusual transaction is found\n"
                                                                    "Tag the Developer to fix it.", inline=True)
                await chat.send(embed=myEmbed1)
            elif (Message == "$account_vineeth"):
                chat = bot.get_channel(850968229677367326)
                myEmbed1 = discord.Embed(title="DumbCoin Account Holder", description="Adithya", color=0x00ff00)
                myEmbed1.add_field(name="Available Balance", value="150 DBC", inline=False)
                myEmbed1.add_field(name="Balance in Dollars", value="$0.0000", inline=False)
                myEmbed1.add_field(name="Last Transaction", value="4/6/2021", inline=False)
                myEmbed1.add_field(name="DumbCoin HelpCenter", value="If any unknown\n"
                                                                    "unusual transaction is found\n"
                                                                    "Tag the Developer to fix it.", inline=True)
                myEmbed1.set_footer(text="Ver 1.25")
                await chat.send(embed=myEmbed1)

            else:
                global question
                chat = bot.get_channel(850968229677367326)
                if(question==""):
                    answer=algorithm.AI(Message)
                    if(answer=="takesecondinput"):
                        question=Message
                        await chat.send("I dont know the answer, what should it be?")
                    elif(answer=="sendmeme"):
                        fIle=["einstine.jpeg","elon.jpeg","meme1.png","meme2.png"]
                        await chat.send(file=discord.File(fIle[random.randint(0,len(fIle)-1)]))
                    else:
                        await chat.send(answer)
                else:
                    algorithm.smart(question,Message)
                    await chat.send("ok, ask again")
                    question=""
    else:
        pass

bot.run("ODQ1NTgwNjM2OTc4MTUxNDQ0.YKjCVQ.errzBHrFqRPjmDw6XdwQHDzgxn8")
