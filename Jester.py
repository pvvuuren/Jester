import discord
import asyncio
import random

client = discord.Client()

async def background_loop():
    await client.wait_until_ready()
    await client.change_presence(game=discord.Game(name="with my thingie"))
    while not client.is_closed:
        channel = client.get_channel("242956769503084544")
        messages = ["Now in bookstores: 'The Audacity of filling a man's anus with concrete.' by Barack Obama", "My new favorite porn star is Joey 'Dem titties' McGee.", "Well if a cop who is also a dog is good enough for a mime having a stroke, it's good enough for me.", "Wake up, America. Christmas is under attack by secular liberals and their congress flaccid penises whitering away beneath their suit pants.", "Lifetime presents 'wiping her butt, the story of inserting a Mason jar into my anus.'", "TSA guidelines now prohibit having anuses for eyes on airplanes.", "Every step towards Auschwitz gets me a little bit closer to a face full of horse cum.", "Believe it or not, Jim Carrey can do a dead-on impression of coat hanger abortions.", "Come to Dubai, where you can relax in our world-famous spas, experience the nightlife, or simply enjoy two midgets shitting into a bucket.", "In the beginning, there was mild autism. And the Lord said 'Let there be the shittier, Jewish version of Christmas.", "Poopy diapers: Hours of fun. Easy to use. Perfect for praying the gay away.", "Today on *Mythbusters*, we find out how long the terrorists can withstand pooping back and forth. Forever.", "Hey there, Young Scientists! Put on your labcoats and strap on your safety goggles, because today we're learning about soiling oneself!", "What did the US airdrop to the children of Afghanistan? A magical tablet containing a world of unlimited pornography.", "Alright, bros. Our frat house is condemned and all the hot slampieces are over at Gamma Phi. The time has come to commence operation tripping balls.", "I'm Miss Tennessee, and if I could make the world better by changing one thing, I would get rid of an erection that lasts longer than four hours.", "Today on *Mythbusters*, we find out how long a lamprey swimming up the toilet and latching onto your taint can withstand deez nuts.", "In line with our predictions, we find a robust correlation between the tiniest shred of evidence that God is real and a sad fat dragon with no friends.", "After blacking out during New Year's Eve, Daddy was awoken by a pangender octopus who roams the cosmos in searh of love.", "Because they are forbidden from masturbating, Mormons channel their repressed sexual energy into a mouthfull of potato salad airplanes.", "Stunkfisk is harder to look at than a mulatto, an albino, a mosquito and my libido.", "A study published in *Nature* this week found that getting naked and watching Nickelodeon is good for you in small doses.", "Everything changed when The Pope killed same-sex ice dancing.", "Alternative medicine is now embracing the powers of gloryholes.", "15 minutes could save you 15% or more on that thing that electrocutes your abs.", "But before I kill you, Mr. Bond, I must show you the secret underground cloning factory where all Nurse Joys are created.", "During Picasso's often-overlooked Brown Period, he produced hundreds of paintings of erectile dysfunction.", "The Five Stages of Grief: denial, anger, bargaining, leaving an awkward voicemail and acceptance.", "Tonight on 20/20: What you don't know about farting and walking away could kill you.", "Dear Leader Kim Jong-un, our village praises your infinite wisdom with a humble offering of flying sex snakes.", "And the Academy award for not contributing to society in any meaningfull way goes to douchebags on their iPhones.", "I went from wearing underwear inside-out to avoid doing laundry to a constant need for validation.", "I'm sorry, sir, but we don't allow AIDS monkeys at the country club.", "Honey, I have a new role-play I want to try tonight! You can be the invisible hand and I'll be Toni Morrison's vagina.", "As part of his contract, Prince won't perform witout used panties in his dressing room.", "Coming to Broadway this season, Crazy opium eyes.", "Who stole the cookies from the cooke jar? My boyfriends's stupid penis.", "Do you lack energy? Does it sometimes feel like the whole world is blowing some dudes in an alley?"]
        await client.send_message(channel, random.choice(messages))
        await asyncio.sleep(21600)

client.loop.create_task(background_loop())
client.run("MzYwNjg1NTM0NTk2ODI1MDkx.DKuSoQ.Prdbtg0W66L_WztPOqO-nDOgzWE")



