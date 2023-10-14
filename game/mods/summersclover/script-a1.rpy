# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label summersclover_intro:
    stop music fadeout 2.0

    pause 1.0

    show text "An unauthorised Katawa Shoujo spin off" with dissolve

    pause 3.0

    hide text with dissolve

    pause 1.0

    scene bg splash with dissolve

    pause 5.0

    scene black with dissolve

    pause 2.0

    scene black


    n "{cps=60}I've always believed that there are many kinds of people.{/cps}"

    n "{vspace=100}{cps=60}Those who calmly stroll through their uneventful lives, the ones who meander from this interest to another, they who walk in the shadow of others more notable than themselves, and so on.{/cps}"

    n "{vspace=100}{cps=60}As for me... I was the type who ran. The people I wanted to be with, what I wanted to do with my life, where I wanted to be, I knew the answers to all those questions.{/cps}"

    n "{vspace=100}{cps=60}I had my worries and concerns, of course, but those meant nothing when living with such purpose. My ambition was what set me free. For those fleeting years of my childhood, I was unstoppable.{/cps}"

    n "{vspace=100}{cps=60}Three years ago, that world ended.{/cps}"


    nvl hide dissolve

    nvl clear

    scene black with fadeslow
    stop music
    pause 1.0
    play music sfx_tcard
    show neutral with fade
    show act1card with passingact
    pause 10.0
    stop music fadeout 2.0

    return


label summersclover_ch1:
    scene bg school_gardens_ss #black
    with dissolve

    play music music_tranquil fadein 6.0 ##was Miki's theme in original script # start with Miki's theme
    $ persistent.song2 = True

    window show

    play sound sfx_can_clatter

    "The rattle of a can hitting the vending machine rings out across the empty school grounds. With the orange of sunset settling over the campus, everyone's retreated to their dormitories and homes for an early start to their studying and various hobbies."

    "Without much else to do, I wander through the gardens while drinking to make the best of the unusually quiet surrounds."

    "Summer's biting particularly hard this year. At least, that's what everybody's been complaining about lately. I don't really see the problem, but I've always been more used to hot weather than others."

    "With little around me to think about, beyond the occasional sip from the can, my mind turns to something that has been bugging me."

    "Every day feels the same. The school week begins, I attend classes, school week ends. Laze around for the weekend, and then it all repeats once more. 'Stagnant' is probably the best word for it."

    "It's not that I hate such a life. Compared to how I've lived before now, it's something I feel I should probably treasure."

    "But my life is also finite. No matter how blissfully unaware I am of it, time still passes. Maybe it's summer holidays that've focused my thinking, or maybe the exams beforehand. Either way, this way of living will end."

    scene bg school_track_ss
    with locationchange

    play ambient sfx_parkambience fadein 1.5
    $ renpy.music.set_volume(0.5, 1.5, channel="music")

    "Emerging through the line of trees separating the track from the main grounds, the movement of a lone person immediately catches my eye."

    "His figure casts a long shadow in the evening's light as he slowly runs along the far side of the track. Looks like it's hard going, with his arms swaying to and fro as he valiantly pushes himself onwards."

    "I idle up to the side of the track and take another swig. It's a welcome distraction from my troubling thoughts."

    "As he comes around the corner, it's possible to finally get a good look at him."

    "I'd recognise those disheveled locks of Hisao's anywhere. While his natural habitat may be the classroom, I've seen him spluttering around the track alongside Emi a couple of times before."

    "Dressed, as always, in his shirt without the bothersome jacket, it's clear that he has a nice build. That said, despite his solid chest and broad shoulders, there's an unassuming air to him. Perhaps it's due to his rather plain face, or just his subdued nature from having recently changed schools."

    "Without anything in particular to say to the boy, I just take another sip of my drink as he continues up the track."

    "Maybe the normal thing to do here would be to cheer him on for throwing himself at the track with such gusto, but it really doesn't look like he's enjoying the ordeal."

    "His running form is becoming worse and worse, and his speed is noticeably slowing. Even the bird that's swooped down to peck at something left in the grass doesn't bother moving as he runs by."

    "It reminds me of how I used to throw myself at the track, running however many laps I could before I broke from exhaustion."

    "I move to take another swig from my can as he comes back around, only to find it lacking. With my attention briefly diverted from Hisao to my sadly empty drink, I'm take mildly off guard as he stumbles off the track and comes to a haphazard stop just ahead of me."

    #stop music fadeout 2.0

    $ renpy.music.set_volume(1.0, 4.0, channel="music") # restoring music volume

    show hisao_talk_small_u with dissolve
    $ renpy.music.set_volume(0.5, 1.5, channel="music")
    #play music music_pearly fadein 1.0 #this is so loud it drowns out the park sfx :/ ##was afternoon music in original script

    hi "Can I... help you...?"

    "Not knowing if he'd even be able to hear me past his panting, I let him collect himself for a few seconds before answering."

    mk "Just watchin'."

    hi "Yeah... I can see that."

    show hisao_wtf_u with charachange
    hide hisao_talk_small_u

    stop music fadeout 1.0
    stop ambient fadeout 1.0

    "He clutches at his knees and tries his best to regulate his breathing, but it's in vain. It's when he clutches at his chest and his breathing noticeably rises in pitch that I start to get a bit worried."

    mk "You okay? Looks like you kinda overdid it, there."

    hi "I'm fine. Totally fine."

    "If he's going to be like that, all that I can do is take a step back and let him recuperate."

    "Beyond his breathing and a slight breeze in the trees, there's nothing to be heard. It reminds me just how alone we are, likely being the only two people in the entire school grounds right now."

    show hisao_erm_u with charachange
    hide hisao_wtf_u

    play music music_pearly fadein 1.0
    play ambient sfx_parkambience fadein 1.0
    $ persistent.song3 = True

    "After who knows how much time, he finally manages to compose himself and stand upright, sweat still tricking down the side of his face. There's a sickly wheeze to his breathing, but I don't think he wants to be reminded of it."

    hi "Miura, right? I'm Hisao Nakai."

    mk "The mysterious transfer student himself. Pleased to meet ya."

    hi "What brings you out here, anyway?"

    mk "Just grabbin' a drink. You?"

    hi "Missed my morning run. E... I mean, Ibarazaki, said I should run in the evening to make up for it."

    mk "Don't worry, I know Emi. Damn near all the school does."

    "I nod towards the track, the bird still out there trying to drag a left over food packet away."

    mk "Just how long have you been out here?"

    hi "A while. I should probably just cut my losses and get dinner, but she'd kill me if I skipped out."

    mk "Man, just give up."

    "Come to think of it, this might be a good chance. Dinner alone is boring, and if I can twist him into paying for a meal, all the better."

    mk "If you're hungry, I know a good place if you're up for it."

    show hisao_talk_small_u with charachange
    hide hisao_erm_u

    "He looks a little startled by the suggestion, running a hand through his hair as he tries to settle himself down and think things through. I can practically see the gears turning in his head as he selects his choice."

    mk "C'mon, a hot girl's asking you to eat with her. You're gonna refuse that?"

    show hisao_heh_u with charachange
    hide hisao_talk_small_u

    hi "They say modesty is a virtue."

    mk "Never said I was a virtuous person."

    "May as well wait things out as he continues with his deliberation, as I'm pretty confident I know what the reply will be. Sure enough, he finally comes up with an answer."

    show hisao_smile_u with charachange
    hide hisao_heh_u

    hi "Fine, I'll go along with you."

    stop ambient fadeout 2.0
    stop music fadeout 2.0

    $ renpy.music.set_volume(1.0, 4.0, channel="music") # restoring music volume

    #centered "~ Timeskip ~" with dissolve
    scene bg suburb_shanghaiext_ss
    with shorttimeskip #locationchange

    "The Shanghai's location within the nearby town has always been convenient. I had thought even this might be too much for Hisao given his exhaustion, but he managed to drag himself here just fine."

    play sound sfx_storebell

    scene bg suburb_shanghaiint
    with locationchange

    play music music_miki fadein 1.0
    $ persistent.song4 = True

    $ renpy.music.set_volume(0.5, .5, channel="ambient")
    play ambient sfx_crowd_indoors fadein 1.0

    show hisao_erm_u at centersit
    with dissolve
    hide hisao_heh_u

    "I like the uniforms they have here, even if they do strike me as a little unconventional. Our meals placed before us, the waitress takes her leave to attend to a handful of other customers at the opposite end of the cafe."
    "Not being especially hungry, my meal's just a slice of pie and a drink. Hisao's pack of sandwiches don't look like it'll last for long, one of them already having disappeared into his mouth."

    "He catches me staring, awkwardly holding the next midair while looking mildly embarrassed."

    hi "Sorry, I just..."

    mk "It's normal to be hungry after exercise, man. Go ahead and stuff your face."

    show hisao_talk_small_u at centersit with charachange
    hide hisao_erm_u at centersit

    "Hisao obediently does so, though with a touch more delicacy than before."

    mk "So what's the story with Emi, anyway?"

    hi "She just pushes me to exercise with her sometimes. Guess she enjoys the company. I mean, like you do now."

    mk "Doesn't seem like you enjoy the experience much."

    hi "Well, I do want to get back into shape. As much as I can, anyway."

    show hisao_frown_u at centersit with charachange
    hide hisao_talk_small_u at centersit

    "He pulls his cuff up his arm a little, taking a loose flab of skin from his forearm and giving it a pinch as he frowns. He sure is pale under his shirt, though maybe I'm not the best judge of that."

    mk "You sure found the right person if you want to be whipped into shape. Just make sure she doesn't kill you first."

    hi "Believe me, she's come close."

    "His tone is way too serious for a throwaway joke. Surely she's not that much of a slave driver."

    "Taking a bite into my own food, it turns out I'm surprisingly hungry myself. The two of us end up stuffing down our food in no time, crumbs littering the table in the aftermath."

    show hisao_erm_u at centersit with charachange
    hide hisao_frown_u at centersit

    "With dinner finished, Hisao leans back in his seat and contentedly pats his stomach. I run my finger around the inside of my mouth to work out the remnants stuck to my teeth, savouring the taste of the last little bits I manage to find."

    "At first I take Hisao's staring out the window to be a sign of boredom, but one careless glance gives his game away. He's trying to distract himself from the bandaged stump resting on the table."

    "I'd hardly think worse of someone for looking at it; being distracted by something out of the ordinary is completely normal. I just give a smile, hoping to make him relax a bit."

    hi "Sorry."

    mk "Believe me, you're not the first to notice. It's not like a missing hand is exactly subtle."

    "Hoping, and succeeding, to defuse the situation a bit, I grin and waggle my stump in the air a little to emphasise the point. It's delightfully easy to read Hisao's emotions, even when he's trying his best to suppress them."

    hi "I still have no idea what to make of this place."

    mk "Town, or Yamaku?"

    "He just raises an eyebrow."

    mk "What's the problem with it?"

    hi "Hmm... I think 'confronting' would probably be the right word."

    hi "It's not every day you see someone with half their face heavily scarred, or have to try and communicate with someone who can't hear. Then there's the obvious example of Emi."

    mk "Well, I mean, you're not wrong. Being a transfer student would make that a lot worse, too."

    mk "Try coming at that from another angle, though - what're we doing now?"

    hi "Chatting at a cafe?"

    mk "And what'd you do today before that?"

    hi "Woke up, got dressed, went to classes, had lunch and tea in a club room, more classes, went to run on the track, and then started chatting with you."

    mk "Isn't that a pretty normal high school day?"

    show hisao_talk_small_u at centersit with charachange
    hide hisao_erm_u at centersit
    show hisao_erm_u at centersit with charachange #followed by hisao_erm to make an opne-close mouth animation
    hide hisao_talk_small_u at centersit

    "He moves to protest, but finds himself searching for words. However reluctantly it may be, he backs down once he realises that I have a point."

    mk "You'll get used to it soon enough. If everyone else at school seems cool with it, that's only because we all had a head start of years."

    show hisao_talk_small_u at centersit with charachange
    hide hisao_erm_u at centersit

    hi "And if I accidentally offend someone? I almost did just then, remember?"

    mk "Then... so what? Just find someone else to talk to. There's hundreds of people here to pick from. Hell, you're talking to me easily enough."

    show hisao_erm_u at centersit with charachange
    hide hisao_talk_small_u at centersit

    hi "A pretty normal high school, huh..."

    mk "Exactly. Just pick up some friends, find your groove, and ride the rest of the year out. You'll be fine."

    "He turns to look out the window, reflecting on the conversation. That expression of contemplation suits him well."

    "Evidently coming to a conclusion, he gives a nod before turning back to me."

    show hisao_smile_u at centersit with charachange
    hide hisao_erm_u at centersit

    hi "Thanks. I'll keep that in mind."

    stop music fadeout 1.0

    "The smile he gives me is kinda sweet. Weak, but terribly sincere. All I can do in response is give a satisfied grin back."

    "Such a chance meeting might not change much for me, but if I can help Hisao get on the right track, at least I'll have been useful to someone."

    "The weather really is nice today."

    ##stop music fadeout 2.5

    stop ambient fadeout 2.5
    $ renpy.music.set_volume(1.0, .5, channel="ambient")

    window hide

    scene black with dissolve


label summersclover_ch2:
    call summersclover_timeskip

    scene bg school_gardens3
    with dissolve
    $ renpy.music.set_volume(0.5, 1.5, channel="music")
    play music music_soothing fadein 0.25 # [str]
    $ persistent.song6 = True


    window show

    "I find myself lazily sitting at the base of a particularly tree in the school gardens, making the most of its shade while watching the goings on ahead."

    "With the events over and medals dispensed, the people gathered for the track meet have now fanned out over the grounds."
    
    "Runners excitedly talk with their friends and parents, with the handful who have romantic interests in the other participating school using the opportunity to catch up on more affectionate matters."

    "It's nice. In fact, I prefer this atmosphere to the competitive nature of the track meet itself. People just catching up with others, having a nice time as the importance of who won or lost whichever race fades away."

    "Without much else to do, I idly toy with the medal on my chest. First place was a lost cause; Emi's in another league when it comes to sprinting, after all. Silver still ain't bad, especially given that I'm hardly the competitive type to begin with."

    "I wonder what metal this thing is actually made of. Tin, maybe. I flick it a couple of times to try and gauge the sound, but it's no use."

    show rin relaxed_sleepy with moveinleft
    hide rin relaxed_sleepy with moveoutright

    "A shadow crossing my vision grabs my attention, but I needn't have bothered looking. The owner just keeps on walking towards the main building, her empty sleeves swaying in the breeze."

    "Looking back to where she came from, I see a familiar face slowly strolling around the grounds. Given that he isn't in gym uniform, he's probably only here because of Emi."

    "I feel a little bad for him. Sure, he's around the student council and Emi a lot, but that feels more like he's being bossed around than actually choosing to hang out with friends. Not that I'm innocent, I guess."

    "The thought of something some of the guys in the club had hastily arranged comes to mind as I mull over the situation."

    "I come to my feet after making my decision, striding past a gaggle of gossiping girls and calling out to him."

    show hisao_talk_small_u with charachange

    hi "Oh, Miura. Hey."

    mk "Got dragged here by the shortie, eh?"

    show hisao_disappoint_u with charachange

    "Hisao just hangs his head as I saunter up to him. He's pretty transparent."

    "It's always struck me how out of place Hisao seems around the track club and other sports stuff. He said he liked soccer when he introduced himself in class, but it's kinda hard to imagine such a passive and subdued lad running around a field and being boisterous."

    "It makes me wonder what he'd be doing with himself if Emi weren't dragging him around by the scruff of the neck."

    mk "Least she put on a show for you."

    show hisao_erm_u with charachange

    hi "Has she always been that good at sprinting?"

    mk "Yep. She puts in the hours on the track, so it ain't no surprise that it pays off. Fastest thing on no legs, and all that."

    hi "Still, it looks like you did fine yourself."

    mk "It's something. You hang around the club and look decently built; I'm surprised you didn't run in some race or another."

    show hisao_frown_u with charachange

    hi "You saw me the other day on the track, didn't you?"

    "The face he pulls makes me feel bad for bringing it up. This being Yamaku, it isn't hard to think up reasons why he might have problems in that area."

    mk "Forget I asked. There is another reason I wanted to talk with you, actually."

    mk "Most of the track club's going to a karaoke place this evening to hang out. There's space for you, if you wanna come."

    show hisao_wtf_u with charachange

    "Hisao looks genuinely startled, but I think it's in a good way."

    hi "I was going to study..."

    mk "C'mon, it'll be fun. Some of the other guys want to know who you really are too, y'know."

    show hisao_disappoint_u with charachange

    hi "I somehow doubt I'm that interesting."

    mk "Mysterious transfer student who keeps hanging around the track with Emi? What's there not to be curious about?"

    "He wavers a little, but eventually throws his arms up in surrender."

    show hisao_heh_u with charachange

    hi "Alright, you got me. I'll come."

    stop music fadeout 1.5

    scene bg city_karaokeint
    with shorttimeskip
    play music music_best_shot fadein 1.0
    $ persistent.song7 = True
    $ renpy.music.set_volume(0.5, .5, channel="ambient")
    play ambient sfx_crowd_indoors fadein 1.0

    "The moment we all entered the dimly-lit room, we started acting as if it were home. People laid on the couches, draped themselves over the arms and backs to talk to friends, threw snacks and drink bottles to each other, and generally made a din from all the arguing over the day's events."

    "Now that some time has passed, with the excitement and adrenaline of the track meet ebbing, things have finally settled down a little."
    
    "The dozen people around make-do with gossiping while lounging around on the garishly coloured seats, occasionally cheer or jeer at whoever's up front belting out some crappy song or another, and busily chat the night away."

    "Not that I'm excluded, with Hisao seated to my right and speaking up to be heard over the atrocious number being sung to a chorus of laughs and teasing."

    show hisao_talk_big_u at centersit with dissolve

    hi "If you don't mind me asking, where are the girls from club? I'm sure I saw a couple besides Emi at the track meet, but only the guys are here."

    mk "What, you lookin' to pick up?"

    hi "I just transferred in, I don't move that quickly."

    mk "Come on, you could do worse than the girls in the track club. Fitness does wonders for you-know-what, after all..."

    show hisao_blush_u at centersit with charachange
    hide hisao_talk_big_u at centersit

    "He gives me a flat face, but I detect a hint of embarrassment in it. Guess he's a bit of a prude."

    mk "They're just busy. Supposedly. Maybe it was too much of a sausage fest for them."

    stop music fadeout 4.0

    "He moves to say something, but as the guy singing ends his round, the next beckons for Hisao to join him as he walks up to the mic."

    "Yukio Hasegawa, nothing less than perhaps the most popular guy in track club. He's always cut graceful figure for a man, bearing slim, refined eyes, impeccably groomed hair, and a gentle face. "
    "Far from my type, but other girls seem to gush over him."

    "The others in the room, whether out of curiosity, friendliness, or teasing, quickly join in to try and make Hisao perform. The guy himself doesn't look enthused, but I suspect that's as much due to the pressure as the actual act."

    mk "You should do it. What've you got to lose?"

    show hisao_hmpf_u at centersit with charachange
    hide hisao_blush_u at centersit

    hi "My dignity. I can't sing, you know."

    mk "What, you think any of us can? Stop being lame and just have some fun."

    #show hisao_frown at centersit with charachange
    #hide hisao_hmpf
    with vpunch
    show hisao_hmpf_u at left with charamovefast

    "I put my hand on his back and give him a sharp push off his ass, jolting him into the center of the room."

    show hisao_wtf_u at left with charachange
    hide hisao_hmpf_u at left
    pause (0.5)
    show hisao_frown_u at left with charachange
    hide hisao_wtf_u at left

    "It's only momentary, but as he recovers, he throws an odd glance back to me afterwards. His anxious, almost scared, face leaves me speechless."

    hide hisao_frown_u with dissolve

    "Everything returns to normality in a flash, the boy taking a breath before marching around the table and up to the mic with back hunched and feet dragging, waving down the cheers of those around him as he does. Whatever was going on in his head, it was far beyond just being shy."

    "With nobody else seemingly having noticed, all I can do is sit back puzzled in my seat and take a swig from the soft drink in front of me."

    play music music_grease fadein 1.0
    $ persistent.song8 = True

    "As the music starts up and the vocals kick in, it becomes obvious that the two are far from practiced at this. Their voices might not be bad, but they're horrendously out of key."

    "Hisao's shyness is getting the better of him too, which only looks worse next to Yukio's confident demeanor."

    "From the corner of my eye, I notice the guy to my left leaning forward, his face turning to mine."

    show haru_basic at centersit with dissolve

    "Named Haruhiko, though everyone calls him Haru, he's a follow classmate who also had the misfortune of being stuck on the first row of tables. While he may be quite gifted physically, being decently tall and strong, he's far from the sharpest tool in the shed."

    "It matters little, though, as his endearing cheerful nature and eternal optimism cover for whatever shortcomings he may have."

    show haru_smile at centersit with charamove
    hide haru_basic at centersit

    har "So, what's the over/under on the new guy?"

    "I set the drink back on the table, my hand rubbing my neck as I lean back. I don't know what answers he's expecting, but I doubt I'll be able to give him any."

    mk "You're asking me?"

    show haru_serious at centersit with charamove
    hide haru_smile at centersit

    har "You're the one who invited him, you know."

    mk "He paid for my lunch, so I felt like I owed him. That's all there is to it."

    show haru_basic at centersit with charamove
    hide haru_serious at centersit

    "The corner of his mouth tugs upwards. Just a little."

    har "You being honorable. There's a first."

    mk "Prick."

    mk "So do you know anything about him? All I know is that he's a nerd who gets bossed around by the shortie and the student council."

    har "Heard he used to play soccer. Not half bad at it, either."

    mk "Used to?"

    show haru_serious at centersit with charamove
    hide haru_basic at centersit

    har "Somethin' wrong with this."

    "Haru glances to the two at the front of the room, both of them being far too distracted with their attempts to make something resembling a decent song to pay us much heed. Satisfied that we're communicating in private, he jabs at his chest with his thumb a couple of times."

    har "He had a heart attack. Real bad, too. Emi'd probably know more. Or the guy himself."

    "He adds the last suggestion as an afterthought, though understandably so. Plenty in Yamaku have their bugbears about what's happened to them in the past, though I'd be damn hypocritical to complain about it."

    mk "Come on, a heart attack? At that age?"

    har "It happens."

    "I expect him to admit that what he heard was some vague rumour or something, but he just shrugs and looks at me matter-of-factly."

    "What would Hisao be, 17? 18? That's the kind of thing you hear taking out frail old folks. Natural causes, and all that. Now that I think of it, maybe that explains why he got puffed so easily back when I saw him at the track."

    mk "Shit..."

    show haru_sad at centersit with charamove
    hide haru_serious at centersit

    "It's kind of pathetic, but that's all the response I can muster as I lean back in my seat. Haru just lets out a dissatisfied sigh, equally put off by the idea."

    hide haru_sad at centersit with dissolve

    "Looking back at the duo finishing up their song at the front of the room, I can't help but see him in a new light."

    stop music fadeout 2.0
    stop ambient fadeout 2.0

    window hide

    scene black
    with dissolve


label summersclover_ch3:
    call summersclover_timeskip

    scene bg school_library
    with dissolve
    $ renpy.music.set_volume(0.5, 1.5, channel="music")
    play music music_happiness fadein 1.0
    $ persistent.song9 = True

    window show

    "If I had to choose which room embodied the feeling of this school the most, it'd have to be the library."

    "It looks normal, at a glance. Large, sure, but otherwise normal."

    "It's only when you start walking through the aisles that you realise the odd little allowances for the students. Audiobooks, braille books, wider passages, and the like. Then there's the cane or two propped against the desks of reading students."

    "There's also the old-fashioned stuffiness, too. Doesn't help that the literature club students are all quiet as mice, but it's something more than that. The furniture, staff, and general mustiness of the older books are all stifling."

    show suzu_neutral at centersit
    with dissolve

    "My eyes eventually fall on the girl across the table from me. 'Unremarkable' would perhaps be the best description of how she appears, save for the bags under her eyes and brace on her knee. For Yamaku, though, that's doing pretty well."

    "If I had to choose which pose embodied the personality of Suzu the most, it'd have to be her chin resting on her hand as her eyes lazily scan the manga magazine in front of her."

    "The girl looks up, her eyes meeting my own. Her reaction, or lack thereof, is about what I'd expect."

    show suzu_speak at centersit with charamove
    hide suzu_neutral at centersit

    suz "Staring is rude."

    mk "I dunno how you put up with this place. Don't you have anything more exciting to do with yourself?"

    show suzu_neutral at centersit with charamove
    hide suzu_speak at centersit

    "She sighs as I start to rock back and forth on my chair to occupy myself. With nobody else willing to brave the heat, the track club's been largely abandoned for the day. I can think of better things to do than throw myself around an empty track."

    "Then again, the literature club sure makes a dull sight. The closest thing I can see to an actual club activity is half a dozen students sitting around a table quiet discussing some book or another."

    mk "Why don't you join them?"

    "Following my nod, she glances to her side and back with a minimum of effort, not even bothering to lift her head from her hand."

    show suzu_surprised at centersit with charamove
    hide suzu_neutral at centersit

    suz "Because I'm busy reading this."

    mk "Isn't literature club for discussing literature?"

    show suzu_concerned at centersit with charamove
    hide suzu_surprised at centersit

    suz "Most of us just read whatever. As long as we're quiet and in the library, nobody really cares."

    mk "So that's all you're gonna do? Read manga?"

    "I was sincerely hoping she'd suggest something for us to do, or maybe even socialise, but she simply shrugs and goes back to reading. It's hard to say whether it's out of apathy or being too tired to do much more than this."

    "Then again, I'd be more surprised if I could gauge her feelings. The kind way to describe her would be 'ambivalent', but after a year of being around her, I've settled on a diagnosis of 'possible lobotomy'. That air of quiet disapproval never seems to leave her."

    "As she slowly turns the page and continues her reading, a familiar voice draws my attention to the end of the library."

    "The tense voice of Ikezawa, hunched over on a beanbag in her usual little corner, isn't difficult to distinguish. Hisao sits on the floor beside her, a disarming smile on his face as he softly tries to chat."

    "I can't quite pick out their conversation, but the fact that they're having one at all is pretty impressive."

    "Suzu turns back around as I stop my gawking, her own interest apparently having been piqued."

    show suzu_surprised at centersit with charamove
    hide suzu_concerned at centersit

    suz "She seems to like him."

    mk "Yeah, they get on well."

    "I might say that, but I have my misgivings. There's more than one story of when girls have tried getting close to her, only for things to go bad for all involved. How much of that is actually true or just gossip, I have no idea, but it's plainly obvious she has a lot of baggage."

    "It might be rather hypocritical, but I don't have much want to get involved. With the way I am, it could only go badly."

    #show hisao _invis at rightedge
    #with None

    "Hisao comes to his feet as their conversation apparently ends, returning from their sanctuary at the end of the library. As he walks by us, a couple of thick novels held to his side, I give a short whistle and motion for him to come over."

    show suzu_surprised at twoleftsit with charamove
    #hide suzu_concerned at twoleftsit
    show suzu_concerned at twoleftsit with charamove
    hide suzu_surprised at twoleftsit

    show hisao_talk_small_u at right with moveinright

    hi "Odd to see you here."

    mk "Well aren't you quick on the uptake?"

    mk "C'mon, take a seat. I need someone for company who has still some life left in them."

    show hisao_talk_small_u at tworightsit with charachange

    "Hisao obediently does so, taking a seat and plopping his books down in front of him. A couple of sci-fi novels, by the looks of them. Not terrible taste. An improvement over Suzu's girly stuff, anyway."

    show suzu_surprised at twoleftsit with charamove
    hide suzu_concerned at twoleftsit

    "Suzu briefly takes her head from her chin to see the new face. I decide to seize the chance."

    mk "Hisao, this is Suzu Suzuki."

    show hisao_smile_u at tworightsit with charachange
    hide hisao_talk_small_u at tworightsit

    "He gives a warm greeting, to which Suzu simply gives a quiet nod, having reverted to her more shy self. He seems a little more sedate than the other friends from track club, so hopefully she'll open up to him a little more than them. Given time."

    show hisao_talk_small_u at tworightsit with charachange
    hide hisao_smile_u at tworightsit

    hi "So you're into manga?"

    show suzu_speak at twoleftsit with charamove
    hide suzu_surprised at twoleftsit

    suz "Are you?"

    hi "A little. To be honest, I don't really follow any of the serialised stuff anymore."

    suz "I see."

    show hisao_disappoint_u at tworightsit with charachange
    hide hisao_talk_small_u at tworightsit
    show suzu_concerned at twoleftsit with charachange
    hide suzu_speak at twoleftsit

    "With Suzu leaving no opening for the conversation to continue, Hisao leans back from the table in disappointment and reaches for one of his books. It's a little sad to see things end this way, and I have told her not to be so antisocial."

    show suzu_speak_close at twoleftsit with charamove
    hide suzu_concerned at twoleftsit

    "Frustrated, I lean over the table, close my fist, and begin rubbing my knuckles into the top of her head."

    #show suzu_speak_close at twoleftsit with charamove
    with vpunch
    #hide suzu_concerned at twoleftsit

    suz "Ow. Ow. Ow."

    show hisao_wtf_u at tworightsit with charachange
    hide hisao_disappoint_u at tworightsit

    hi "Uh, Miki..."

    mk "What have I told you about being like that?"

    "I'm not using much force at all, but her reaction's enough to make me back off rather quickly. The point's been made in any case."

    show suzu_angry at twoleftsit with charamove
    hide suzu_speak_close at twoleftsit
    show hisao_talk_small_u at tworightsit with charachange
    hide hisao_wtf_u at tworightsit

    hi "So you're into shoujo, then?"

    show suzu_embarrassed at twoleftsit with charachange
    hide suzu_angry at twoleftsit

    suz "Is that bad?"

    hi "It's normal enough. Watch the shows?"

    show suzu_normal at twoleftsit with charachange
    hide suzu_embarrassed at twoleftsit

    suz "Yeah. This one's getting an adaptation soon which I'll have to catch."

    hi "Doesn't that stuff air pretty late?"

    suz "My sleep schedule's all over the place anyway."

    show hisao_heh_u at tworightsit with charachange
    hide hisao_talk_small_u at tworightsit

    "He's clearly resisting snark given how tired she visibly looks, but wisely thinks better of it."

    mk "Didn't get much of that stuff on TV back where I came from."

    mk "So you used to read it, Hisao?"

    show hisao_erm_u at tworightsit with charachange
    hide hisao_heh_u at tworightsit

    hi "It was good for killing time while wandering town. Didn't spend much time at home."

    show suzu_concerned at twoleftsit with charachange #why is this not showing up?
    hide suzu_normal at twoleftsit

    suz "Your parents didn't mind?"

    hi "Both of them worked long hours, so not really."

    "There's a gulf between their concepts of what parents would allow, but it's understandable. For someone as pampered as Suzu, being let to wander so much must be a pretty strange idea. I suppose Hisao's a bit like me in that regard."

    mk "Well, at least someone's familiar with the scene. Had practically none of that stuff back home, so it's largely foreign to me."

    mk "Speaking of people's homes... I see you were visiting Hanako's little corner. Tryin' to make inroads with her?"

    show hisao_frown_u at tworightsit with charachange
    hide hisao_erm_u at tworightsit

    hi "'Trying' is the key word, there."

    mk "Don't look so beaten. You can hold a conversation with her, right? That's more than anyone else in the class has managed so far."

    hi "That's more to her friend's credit than mine."

    mk "You really need to learn how to accept praise."

    "My reply is a bit crabby, and admittedly not only because it's a bad habit. 'Hanako's friend' could only be referring to one person; the pretty blonde that she often meets after class. I'm a little jealous of him for getting so close to her so easily."

    mk "You know, you say it's weird to see me here, but what about you?"

    show hisao_smile_teeth_u at tworightsit with charachange
    hide hisao_frown_u at tworightsit

    hi "Reading's my main hobby."

    mk "And running?"

    show hisao_hmpf_u at tworightsit with charachange
    hide hisao_smile_teeth_u at tworightsit

    hi "That's... more like a sentence."

    show suzu_grin at twoleftsit with charachange
    hide suzu_concerned at twoleftsit

    "It's only because we're in the library that I stifle a laugh. Suzu might try to hide it, but the flicker of a smirk flashes on her face as well. True bonding, though the misery of others."

    show suzu_concerned at twoleftsit with charachange
    hide suzu_grin at twoleftsit

    mk "I guess you're all set for exams, then."

    show hisao_talk_small_u at tworightsit with charachange
    hide hisao_hmpf_u at tworightsit

    hi "Why do you say that?"

    mk "You're with Mutou all the time, you know. Guy's got high hopes. You get ridiculous marks for most of your subjects, too."

    show hisao_biggrin_u at tworightsit with charachange
    hide hisao_talk_small_u at tworightsit

    hi "That's because I work for them."

    "This guy catches on way, way too quickly. I might not pay attention in class, but he doesn't have to burn me like that. Suzu's attention is finally wrested from her reading material, looking genuinely impressed. As much as her stony face can, anyway."

    mk "That's harsh, man."

    suz "You're strongest in math and science, correct?"

    show hisao_talk_small_u at tworightsit with charachange
    hide hisao_biggrin_u at tworightsit

    hi "Yeah."

    suz "Could you look at something I couldn't get when we go back to class?"

    show hisao_smile_u at tworightsit with charachange

    hi "Sure, no problem. Doesn't hurt to work it all out before exams come up."

    "Exams. I hate that word. The mood of the class has already begun to sour thanks to the anxiety and stress they cause, and it's only going to get worse in the weeks ahead."

    "At least they're useful for something. If studying's going to be how she expands her social circle, then all the better. Given how hard she works for her rather average marks, maybe he can help turn things around."

    stop music fadeout 2.0
    window hide

    scene black
    with dissolve


label summersclover_ch4:
    call summersclover_timeskip

    scene bg school_cafeteria
    #with shorttimeskip
    $ renpy.music.set_volume(0.5, 1.5, channel="music")
    play music music_ease fadein 1.0
    $ persistent.song10 = True
    $ renpy.music.set_volume(0.5, .5, channel="ambient")
    play ambient sfx_crowd_indoors fadein 0.5

    window show

    "I've always found the cafeteria to be a fun place to watch people."

    "Deftly manoeuvring through the rapidly filling room after being among the first to have their tray filled by the old ladies behind the counter, I can't help but glance around at the other students on my way to a free table."

    "By rights, the cafeteria should be a melting pot. Students from every club, class, condition, and year level are here, and with everyone in their uniforms, the differences between rich and poor, country and city, fashionable and unfashionable, fades to nothing."

    "But, people being people, they still find a way to stick to their cliques. The track club members form a clump as they playfully jostle one another, as do a bunch of the deaf students, huddling together in their impenetrable little social circle while signing in their silent second language."

    "There are the gaggles of popular girls with their posses, and the odd trio of less popular girls who stick to their few friends. The rowdy class clowns who loudly joke and act out, and the softly-spoke academics who keep to themselves while shuffling along."

    "Everyone has their niche, even if that niche consists of only one."

    "Setting down my tray at an empty table, I separate the disposable chopsticks using the tips of my fingers as always. Strength comes in surprisingly useful when you largely rely on one hand for manipulation, with the two conjoined sticks easily splitting apart."

    "While I'd hesitate to say it's great, the food here is still pretty good. Filling, and by far satisfying enough to live on for quite a while. Can't complain about the price, either."

    show suzu_neutral at centersit with dissolve

    "It doesn't take long for company to arrive after I've started eating, a familiar figure silently seating herself across the table from me."

    "Suzu simply begins to eat without a word. Such things aren't unusual with her, so I simply look down and continue with my own lunch."

    "As I shovel rice into my mouth, I find myself especially pleased with how they've cooked it today. Not too dry, not too sticky. Ditching the chopsticks and gulping down some soup, it turns out that they've done a good job on that too."

    "Whether Suzu's enjoying her lunch as much as I is, as always, a mystery."

    "Looking past her, two of the three stooges come into sight. With my hand taken, I end up waving my stump around in the air to get their attention. It does the job, with the duo changing course and heading our way."

    #show suzu_concerned at leftoffsit with charamove
    show haru_yo at right
    with moveinright

    har "'Afternoon Miki, Suzuki."

    show haru_yo at leftoff with charamove
    show haru_basic at leftoff with charamove
    show hisao_smile_u at rightedge with moveinright
    show hisao_smile_u at rightedgesit with charamove

    "Suzu pauses her eating to nod to the both of them, as do I. Hisao moves around to take a seat beside me with his juice and a packet of bread, while Haru manoeuvres himself to the end of the table holding a suspicious plain cardboard box with equally suspicious care."

    mk "What's with that?"

    show hisao_heh_u at rightedgesit with charachange
    hide hisao_smile_u at rightedgesit
    show haru_smile at leftoff with charamove
    hide haru_basic at leftoff

    "Hisao just shrugs as I lean over and ask him. Haru just gleams a smile in response, setting down the mystery box and lifting the top off with practiced ease."

    scene bg cake with dissolve

    "As the sides fall away, a gorgeous looking red and white sponge cake is revealed. A thick layer of cream separates the two layers of sponge, and another sits atop the cake. Big, succulent strawberries circle the outer rim, each sitting on its own further blob of cream. "
    "Finally, a light dusting of frosting covers the cake, like a thin shower of snow."

    "It's... beautiful. As expected of Haru."

    scene bg school_cafeteria with dissolve

    show hisao_smile_teeth_u at rightedgesit
    show suzu_grin at centersit
    show haru_smile at leftoff
    with dissolve

    hi "You're drooling."

    mk "Don't care, gimme that thing."

    "He might be criticizing me, but Suzu's attention is just as focused. Her sweet tooth is getting the better of her as the cafeteria food before her languishes."

    show haru_serious at leftoff with charamove
    hide haru_smile at leftoff

    har "Right, right, just hold on a moment."

    "He takes the plastic knife cunningly carried inside the box, and sets about cutting a few slices. Looks like the cake's already had a good third eaten."

    mk "So what's the story?"

    show hisao_talk_small_u at rightedgesit with charachange
    hide hisao_smile_teeth_u at rightedgesit

    hi "Who's?"

    mk "Let's start with the cake."

    show haru_basic at leftoff with charamove
    hide haru_serious at leftoff

    har "Made too much during home ec class. The teacher doesn't mind me baking my own stuff there as long as she gets some."

    hi "So you're into baking?"

    har "Sure am. Might not have many talents, but I'm good at the ones I have."

    "As he gets back to cutting it up, I look around for an answer to the second question on my mind; where the third stooge has gotten himself to."

    "As my eyes fall on him, I can't help but give a weak grin. Suzu notices my staring and twists her head around to see, but turns back to the cake in short measure."

    show suzu_concerned at centersit with charachange
    hide suzu_grin at centersit

    scene black with dissolve
    scene bg school_cafeteria

    #put in some girl sprites for Yukioto talk to
    show yukio_smile
    show aoi_smile at twoleft
    show saki at tworight

    "Sure enough, he's standing around chatting up a couple of girls. I might not see the appeal in his appearance, but I can admit that he pulls off an air of confidence well, even without hearing what he's saying."
    "Going by the bashful smile of the long-haired girl as she toys with her hair, and the other's excited chatting, he's making good progress with both."

    scene black with dissolve
    scene bg school_cafeteria

    #some kind of fade again
    #hide yukio_smile
    show hisao_talk_small_u at rightedgesit
    show suzu_neutral at centersit
    show haru_basic at leftoff
    with dissolve

    hi "Is he always like that? I swear he was with a couple of other girls last week."

    mk "Believe me, you have no idea."

    "Some people bake, some run, some study, and some pick up women."

    scene black with dissolve
    scene bg school_cafeteria

    #fade again and add girls
    #hide hisao_talk_small
    show yukio_huh
    show aoi_smile at twoleft
    show saki at tworight

    "As if he'd heard me, Yukio looks up from his companions to see Hisao and I staring. Sensing an escape, he nods to us and seemingly explains that he wants to come our way."

    #make a sad/worried saki maybe in previous shots flip eyes to look at yukio, and in this keep eyes like they were but flip mouth to make frown
    show aoi_surprised at twoleft with charachange
    hide aoi_smile at twoleft
    show saki_frown at tworight with charachange
    hide saki at tworight

    "The girl with longer hair is about to follow him over before her friend stops her, gesturing at me while frowning. It's hard to be hurt by something you deserve, and as they both quickly decide to walk off, I can take solace in that at least my reputation's helped Yukio."

    hide aoi_surprised with easeoutright
    hide saki_frown with easeoutright


    scene black with dissolve
    scene bg school_cafeteria


    #fade again and also find out of to move everyone a bit so 4 people can be onscreen
    show suzu_concerned at onerightsit
    show haru_basic at oneleftsit
    show hisao_erm_u at rightedgesit
    with dissolve
    show yukio_smile at leftoff
    with moveinleft

    yuk "And how are we today, ladies and gents?"

    hi "Good."

    har "Good."

    mk "Good."

    suz "Good."

    show yukio_notimpressed at leftoff with charachange

    yuk "Don't be too enthusiastic, now."

    show haru_basic at leftoffsit with charamove
    hide yukio_notimpressed at leftoff
    show yukio_smile at oneleftsit with charamove
    show suzu_unhappy at onerightsit with charachange
    hide suzu_concerned at onerightsit

    "He takes a seat beside Suzu, giving her a brief disarming smile as he does. She visibly wilts, despite doing her best to avoid doing so."

    show haru_serious at leftoffsit with charamove

    "Haru looks back to the cake, but frowns as he begins to cut another slice."

    har "Hmm. We'll have one more slice than we have people. Should've worked that out first."

    mk "Dibs on the double portion."

    show haru_annoyed at leftoffsit with charamove
    hide haru_serious at leftoffsit

    har "Piss off. Suzuki gets double."

    show suzu_embarrassed at onerightsit with charachange
    hide suzu_unhappy at onerightsit

    suz "Uh... thank you."

    mk "Hold on, what's the criteria here? Is it because she's a girl?"

    show haru_basic at leftoffsit with charamove
    hide haru_annoyed at leftoffsit

    har "A polite young girl, yes."

    mk "What about me? I'm a girl too."

    stop music fadeout 0.5
    play music music_tension fadein 0.5
    $ persistent.song11 = True

    show yukio_notimpressed at oneleftsit with charachange
    hide yukio_smile at oneleftsit

    yuk "Only when it suits you."

    "I get up out of my chair to get some height over him, which he responds to in kind."

    #get yukio closer/bigger somehow?
    hide yukio_notimpressed at oneleftsit
    show yukio_huh at oneleft with charachange

    mk "Oh yeah? How about you try having periods?"

    show yukio_angry at oneleft with charachange
    hide yukio_huh at oneleft

    yuk "Piss off, we have to-{w=.5}{nw}"

    mk "Look at me, I'm a man, oh no I have to shave my face, I have dreams that give me orgasms, how terrible~!"

    yuk "Well maybe you'd be treated like a girl if you actually acted like one!"

    mk "Huh? What's that? I can't hear you over bleeding from my genitals and feeling like I've been sucker-punched in the gut once a month!"

    yuk "You're making my point for me! If you didn't go on about your bloody periods while we're eating, we'd-!{w=.95}{nw}"

    mk "Maybe I'd act more like a girl once I got free crap for being one!"

    show hisao_frown_u at rightedgesit with charachange
    hide hisao_erm_u at rightedgesit
    show suzu_concerned at onerightsit with charachange
    hide suzu_embarrassed at onerightsit
    show haru_sad at leftoffsit with charamove
    hide haru_basic at leftoffsit

    hi "Miki, Yukio, please..."

    "Hisao looks to Suzu for help as we snarl at each other, but all she's doing is burying her face in her palm and trying not to exist."

    stop music fadeout 0.5
    stop ambient fadeout 0.5

    #shrink yukio back down

    "I want to thump Yukio for being an ass, but in contrast to the busy hum of students of before, the sudden silence around us reminds me that we're in the cafeteria."

    #hide yukio_angry at oneleft
    show yukio_angry at oneleftsit with charachange

    "Submitting to Hisao's begging, we both fall back into our seats, neither of us admitting that the argument is over."

    show haru_basic at leftoffsit with charamove
    hide haru_sad at leftoffsit
    show suzu_embarrassed at onerightsit with charachange
    hide suzu_concerned at onerightsit

    play ambient sfx_crowd_indoors fadein 1.0

    "As if the altercation had never happened, Haru passes the extra slice to Suzu, earning a shy nod of thanks. It only serves to make Yukio all the more pissed for some reason, but before I can step in to defuse the situation, Hisao does the job for me."

    show hisao_talk_small_u at rightedgesit with charachange
    hide hisao_frown_u at rightedgesit

    hi "What brings you here anyway, Yukio?"

    show yukio_notimpressed at oneleftsit with charachange
    hide yukio_angry ay oneleftsit
    play music music_ease fadein 1.5

    yuk "Oh, it's a woeful tale. A terrible curse has struck me yet again. Day after day this happens, and only so rarely can I find refuge from its grip."

    "He's totally making an ordeal out of it, clutching at his chest and emoting as hard as he can. Even if it's for an audience of one, he still likes to play the orator. It's a shame he stopped acting, really."

    yuk "I'm just... too popular."

    show hisao_erm_u at rightedgesit with charachange
    hide hisao_talk_small_u at rightedgesit

    hi "What."

    yuk "Girls just fall over themselves for me. It's been like this ever since high school started, and if anything it's only become worse."

    show yukio_blush at oneleftsit with charachange
    hide yukio_notimpressed at oneleftsit

    yuk "Oh, what I would do to get those women off me! I tell them I'm not interested, but it only makes them try all the harder."

    hi "You can't be serious."

    "Haru begins to come around each of our seats, setting down a slice before each of us before sitting beside Hisao. I quickly tuck into mine as soon as I can, the wonderful taste of cream and strawberries filling my mouth. Befriending this guy was one of the best decisions ever."

    show haru_smile at leftoffsit with charamove
    hide haru_basic at leftoffsit

    har "It's true. He ended up quitting drama and switching to the track club just to lower his profile." #changed this Mor to Har cause it makes sense -Niji [str]

    show hisao_smile_teeth_u at rightedgesit with charachange
    hide hisao_erm_u at rightedgesit
    play audio sfx_snap

    "Hisao suddenly clicks his fingers in a flash of insight."

    hi "Ah, that explains it! I knew that face on the posters was yours. You must still work for them sometimes, right?"

    show yukio_smile at oneleftsit with charachange
    hide yukio_blush at oneleftsit

    yuk "Yeah, though it's mostly organizing new recruits and helping with behind the scenes stuff. They probably just use my face to draw in a bigger crowd..."

    show yukio_eeh at oneleftsit with charachange
    hide yukio_smile at oneleftsit

    "His smile fails him as he looks down at his dessert, a cloud of despair hanging overhead. I wonder how many girls he'd get if he let this side of himself show through more often."

    yuk "Man, it really is a pain. Those girls are so loud and obnoxious, I can't stand any of them."

    mk "I might not the best judge, but I don't really understand your appeal. Physically, at least."

    show haru_basic at leftoffsit with charamove
    hide haru_smile at leftoffsit

    har "You don't?"

    mk "You do?"

    "I see an opportunity to both tease him and stroke my own ego, and so take it without hesitation."

    mk "Hmm... who do you think is hotter? Me, or Yukio?"

    show yukio_huh at oneleftsit with charachange
    hide yukio_eeh at oneleftsit

    "I lean around Hisao and stare intently at Haru, with Yukio reluctantly doing the same."

    show haru_serious at leftoffsit with charamove
    hide haru_smile at leftoffsit
    show hisao_erm_u at rightedgesit with charachange
    hide hisao_smile_teeth_u at rightedgesit
    show suzu_concerned at onerightsit with charachange
    hide suzu_embarrassed at onerightsit

    "Haru's taking this surprisingly seriously, his head moving between our faces with a look of total concentration as he brings his fingers to his stubbled chin. Seconds pass, with Hisao and Suzu's interest obviously piqued as they stare and eat at the same time."

    "Everybody's on tenterhooks as we await his judgment, with Yukio's face slowly moving further and further back."

    show yukio_eeh at oneleftsit with charachange
    hide yukio_huh at oneleftsit

    har "I'd have to say Yukio."

    "I'm a little disappointed in the answer, but the look on Yukio's face more than makes up for it."

    yuk "That's a joke... right?"

    show haru_basic at leftoffsit with charamove
    hide haru_serious at leftoffsit

    har "Not at all. I can definitely see why girls like you."

    show yukio_angry at oneleftsit with charachange
    hide yukio_eeh at oneleftsit

    yuk "You're the last person I wanted that kind of praise from."

    show hisao_smile_u at rightedgesit with charachange
    hide hisao_erm_u at rightedgesit

    "Smiling at his discomfort, Hisao finishes his cake and gives due compliments to Haru, which I hurriedly second."

    mk "Come to think of it, haven't you got lots of female friends, Hisao? Maybe you could give the stud here some tips on how to friendzone like a pro."

    show hisao_hmpf_u at rightedgesit with charachange
    hide hisao_smile_u at rightedgesit

    hi "Thanks..."

    yuk "I'm not interested in keeping them as friends, I just want them to piss off."

    show yukio_smile at oneleftsit with charachange
    hide yukio_angry at oneleftsit

    yuk "Here."

    "He plucks the strawberry off his dessert and plops it on top of Suzu's uneaten slice. She doesn't even notice, given her attention being focused on trying to get through the first without dropping crumbs everywhere."

    show yukio_huh at oneleftsit with charachange
    hide yukio_smile at oneleftsit

    "He waits for a reaction to his act of kindness before giving up and hanging his head in defeat. I don't think Yukio is having a good day."

    mk "Well, there you have it, Hisao. These are the losers I hang out with."

    show hisao_smile_u at rightedgesit with charachange
    hide hisao_hmpf_u at rightedgesit

    hi "They're not so bad."

    show haru_smile at leftoffsit with charamove
    hide haru_basic at leftoffsit

    "Haru clamps onto Hisao's shoulder and gives him a playful shake. It's nice to see Hisao loosening up, even if it is just a little."

    stop ambient fadeout 1.0
    stop music fadeout 1.0

    window hide

    scene black
    with dissolve


label summersclover_ch5:
    call summersclover_timeskip

    scene bg school_scienceroom
    #with shorttimeskip
    play music music_normal fadein 1.0
    $ persistent.song12 = True

    window show

    "Walking into class, my gaze immediately falls to Suzu's desk. Each and every morning she enters class long before I do, and though I might have hoped to catch her out, today is no different than any other."

    "It's one of life's small wonders; I never did understand how someone in a perpetual state of sleep deficiency manages to get here on time every day. Well, it's not that I don't understand how, so much as why."

    "I suppose it's a lie to say that nothing at all is different, though. Her head may be resting in her hand as it always is, but rather than looking out the window, her eyes are on the guy casually speaking with her in front of her desk."

    "Suzu and Hisao took to each other surprisingly quickly. She doesn't seem particularly interested in actually conversing, but just giving him the time of day is more than she gives the other guys in the track and field club. 'Boorish', she calls them."

    "Which isn't wrong, really."

    mk "Yo."

    show hisao_talk_big_u at twoleft #make a surprised face for Hisao
    show suzu_surprised at tworight
    with charaenter

    "The two of them react in unison to the sound of my voice, Hisao turning his body towards me as Suzu moves little more than her eyes. Their normal morning greetings come to a halt almost as soon as they begin."

    hide suzu_surprised

    show hisao_erm_u at twoleft
    hide hisao_talk_big_u at twoleft
    show suzu_neutral at tworight
    hide suzu_surprised at tworight
    with charachange

    "Suzu just sighs as Hisao's face, as it so often does, turns to mild concern."

    hi "Are you... okay?"

    mk "Huh?"

    "He motions to his left cheek, my own fingers mirroring his out of reflex. It takes me a second to realize what he's referring to. I haven't looked in the mirror, but there'd no doubt be a nice big bruise there right about now."

    mk "Haha, this? I kinda got a bit rough with another club guy. We're cool, don't worry."

    show suzu_surprised at tworight with charachange
    hide suzu_neutral at tworight

    suz "Again?"

    hi "...This happens often?"

    show suzu_speak at tworight with charamove
    hide suzu_surprised

    suz "You have no idea."

    show suzu_concerned at tworight with charachange
    hide suzu_speak at tworight

    "I disarm him with a stupid grin as I scratch the back on my neck."

    hi "Both of you seem rather accident-prone."

    hi "Then again, maybe accident isn't the right term to use for you."

    play sound sfx_clap

    "The loud clapping of hands behind me would make me jump if it were less obvious who said hands belonged to. As Mutou clears his throat and tries to shepherd the gossiping class into their seats, Hisao obediently takes his leave of us and I turn to take my seat."

    hide suzu_concerned
    hide hisao_erm_u
    with charaexit

    "The fact he's addressing the class rather than me is cause for a mental sigh of relief. He wouldn't take kindly to casual talk of a scrap between students, and his classroom lectures are boring enough without being subjected to another on the subject."

    show muto irritated with charaenter

    mu "Oh, and Miura? I'll see you after class."

    "Damn it."

    stop music fadeout 2.0

    scene bg school_gate
    #with shorttimeskip
    show suzu_neutral at twoleft
    show hisao_erm_u at tworight
    with shorttimeskip
    play music music_tranquil fadein 1.0

    "Jogging past the school gates, Suzu and Hisao can be seen patiently waiting for me. By now the main throng of leaving students has passed, reduced to little more than the occasional person or two."

    show suzu_speak at twoleft with charamove
    hide suzu_neutral at twoleft

    suz "Have fun?"

    mk "Detention on Monday. What a pain in the ass."

    show hisao_talk_small_u at tworight with charachange
    hide hisao_erm_u at tworight

    hi "At least it's Saturday, right? You've got a stay of execution for a couple of days."

    mk "Whatever. Let's just get lunch."

    suz "Shanghai?"

    mk "Yeah. You okay with that, Hisao?"

    hi "Sounds good."

    "The decision made, we set off down the hill for the local town."

    scene bg school_road
    with locationchange
    show suzu_concerned at twoleft with charaenter
    hide suzu_speak at twoleft
    show hisao_erm_u at tworight with charaenter
    hide hisao_talk_small_u at tworight

    "I like this time of year. The weather, hot with decent but not overbearing humidity, reminds me of home. It also means being able to wear summer outfits, which are far more comfortable than winter clothing."

    "It's hard to tell if Suzu's fidgeting is because she's uncomfortable around Hisao, or just because she hates the heat. She's a winter kind of person after all, in every way."

    "Even Hisao, the rookie, looks more casual than she does. That said, he has the undeniable air of a tourist about him; eyes flitting about, pace just slightly slower than what looks natural, head turning this way and that."

    mk "Where you come from, anyway? You aren't a local, that's for sure."

    show hisao_talk_small_u at tworight with charachange
    hide hisao_erm_u at tworight

    hi "The city. The quiet of places like this is a big difference."

    mk "Hah, a city boy. Should've known."

    hi "I take it you're from somewhere else, then?"

    show suzu_speak at twoleft with charachange
    hide suzu_concerned at twoleft

    suz "She's a hick from up North."

    mk "Hey."

    show suzu_grin at twoleft with charachange
    hide suzu_speak at twoleft

    suz "Well, aren't you?"

    show hisao_heh_u at tworight with charachange
    hide hisao_talk_small_u at tworight

    "I don't want to let her get away with it, but from the interested face Hisao's making, she's already won this."

    mk "We can't all be dainty spoiled princesses..."

    show hisao_disappoint_u at tworight with charachange
    hide hisao_heh_u at tworight

    hi "You make it sound like you're from out in the sticks or something."

    mk "I am, dude. Tell you what, the first time wandering around the city near here was a big culture shock."

    show hisao_wtf_u at tworight with charachange
    hide hisao_disappoint_u at tworight
    show suzu_surprised at twoleft with charamove
    hide suzu_grin at twoleft

    "His reaction is kind of charming. He has no idea at all what a country life is like, no doubt desperately mining his brain for any images that he can muster."

    "Not that Suzu's any different. I don't really care to explain it to either of them; it's not something I take particular pride in, and bringing her there to visit would only cause problems."

    mk "Oh yeah, I noticed you chatting with the guys in the track club yesterday. You ever going to actually join, or what?"

    show hisao_erm_u at tworight with charachange
    hide hisao_wtf_u at tworight

    hi "Do I have to? I don't remember it being compulsory."

    mk "That's not what I'm asking! Urgh."

    show hisao_smile_teeth_u at tworight with charachange
    hide hisao_erm_u at tworight

    hi "Maybe I should just join the literature club and wash my hands of the whole thing."

    show suzu_grin at twoleft with charamove
    hide suzu_surprised at twoleft

    suz "Yes, do that. The school hardly needs another jock running about."

    mk "Oi, doesn't that make me a jock?"

    show hisao_biggrin_u at tworight with charachange
    hide hisao_smile_teeth_u at tworight

    hi "To be fair..."

    with vpunch
    show hisao_talk_big_u at tworight with charachange
    hide hisao_biggrin_u at tworight

    "I clap the boy over the head, drawing protests from him. The last thing I need is another Suzu on my case."

    show suzu_normal at twoleft with charachange
    hide suzu_grin at twoleft

    suz "So violent."

    show hisao_smile_teeth_u at tworight with charachange
    hide hisao_talk_big_u at tworight

    hi "Very violent."

    "I'm beginning to think I've created a monster by bringing these two together."

    stop music fadeout 2.0

    scene bg suburb_shanghaiext
    with locationchange

    "By the time we reach the Shanghai, I feel like I've run through a gauntlet with the both of them pecking away. Suzu throws the odd snark while alone, but she and Hisao egg each other on."

    "I don't really hate it, though. It's maybe even a little cute."

    play sound sfx_storebell

    scene bg suburb_shanghaiint
    with locationchange

    "The bell above the door gives its trademark rattle as we file in, the waitress's hurried shuffling towards us no less familiar. Look like the place is mostly empty, save for a handful of other patrons."

    "Maybe it's a good thing; if such a place can stay open for this many years and not shut down from the lack of customers, at least the staff aren't going to be too stressed. They keep their jobs, and the town keeps its little odd cafe."

    show yuukoshang happy_down at center with dissolve
    show yuukoshang happy_down at centersitlow with charamovefast
    show yuukoshang happy_down at center with charamovefast

    "When she reaches us, the waitress throws her upper body down in a sharp bow. Hisao flinches from how close she comes to head butting him."

    yu "Welcome to the Shanghai! Please take a seat."

    hide yuukoshang with dissolve
    show suzu_neutral at twoleft
    show hisao_erm_u at tworight
    with dissolve
    show suzu_neutral at twoleftsit with charamove
    show hisao_erm_u at tworightsit with charamove
    #looks better if they don't sit at the same time -Niji
    play music music_daily fadein 1.0
    $ persistent.song21 = True

    "I give a weak smile as we go, picking an empty window-side table from amongst the many. Suzu shuffles into her seat and I slide in next to her, Hisao being relegated to the other side."

    mk "You've been here a few times now, right? You like it?"

    hi "The fact that Yuuko's here still weirds me out a bit..."

    mk "Haha, yeah. Lots of people say that. She's pretty at least, right?"

    hi "Guess so."

    mk "You gotta loosen up, man. You're a teenage guy, nobody's gonna believe that you don't have an eye for the ladies."

    hi "How should I answer, then?"

    mk "I dunno. 'I like her tits', 'she's got nice thighs'. Whatever."

    show hisao_wtf_u at tworightsit with charachange
    hide hisao_erm_u at tworightsit

    hi "...Is Yuuko looking at us?"

    show suzu_veryembarrassed at twoleftsit with charamove
    hide suzu_neutral at twoleftsit

    suz "No, thank God."

    "I just smile at them. Looks like he's going to be just as easy to tease as Suzu is. Such prim and proper people, they are."

    show hisao_erm_u at tworightsit with charachange
    hide hisao_wtf_u at tworightsit
    show suzu_concerned at twoleftsit with charachange
    hide suzu_veryembarrassed at twoleftsit

    "As they both recover from their fit of modesty, a more important matter comes to mind. I want to help him back on his feet, but if he's going to be around me for any length of time, he'll have to get used to Suzu as well. And vice-versa."

    "I stare to my companion beside me, making her tilt her head."

    mk "Wanna show him your party trick?"

    show suzu_unhappy at twoleftsit with charachange
    hide suzu_concerned at twoleftsit

    "She pauses for a moment to work out what I'm referring to. By her increasingly hesitant face, she's got the right idea."

    "After thinking on it for a good while, with Hisao's face curiously looking on, she comes to the conclusion I'd been hoping for."

    show suzu_speak at twoleftsit with charachange
    hide suzu_unhappy at twoleftsit

    suz "If he's going to be hanging around, I guess we have to."

    hi "Show me what?"

    "I give him a disarming smile for a moment, before suddenly turning beside me."

    stop music

    mk "BOO!"

    show suzu_surprised at twoleftsit with charamove
    hide suzu_speak at twoleftsit

    "All she does is raise an eyebrow. I have to admit I'm holding back a little; my mental block against possibly hurting her isn't that easy to get around."

    suz "That isn't going to work if-"

    #shake the screen here maybe? -Niji
    show hisao_talk_big_u at tworightsit with charachange #and make hisao's and then Suzu's character jump up or something
    hide hisao_erm_u at tworightsit
    show hisao_talk_big_u at tworight with charamovefast
    show hisao_talk_big_u at tworightsit with charamovefast
    with vpunch
    play sound sfx_doorslam

    show suzu_speak at twoleftsit with charachange
    hide suzu_surprised at twoleftsit
    show suzu_speak at twoleft with charamovefast
    show suzu_speak at twoleftsit with charamovefast


    hi "ARGH!"

    "Hisao leaping out of his seat and hitting his fists to the table as he shouts, albeit in a careful way given we're in public, has the intended effect. Suzu immediately jumps in fright, my own heart skipping a beat in sheer startlement."

    show suzu_asleep at twoleftsitlow with charamove
    hide suzu_speak at twoleftsit
    play sound sfx_impact #with bang soundeffect

    "With barely a second's delay, the life seemingly goes out of her. A sigh as the air from her lungs lazily passes her lips is all to be heard as her small body goes limp in her seat. Her head jerks downward as all control goes out of her neck, before her entire upper body falls forwards."

    play music music_suzu
    $ persistent.song13 = True

    "With an audible thud, her forehead lands on the table without the slightest resistance. Her arms follow soon after, flopping haphazardly onto the surface. With the show over, the girl beside me now lies seemingly dead, save for the movement of her breathing."

    show hisao_wtf_u at tworightsit with charachange
    hide hisao_talk_big_u at tworightsit

    "Hisao looks mortified, as if he himself had fired a bullet into her. Shock from the sudden nature of what happened, and extreme discomfort from a human moving and remaining limp in such an unnatural way, are written on his face."

    "I have to admit, for all I may be trying to play it cool, it still puts me off a little. I've never truly gotten used to this."

    hi "Is she... okay...?"

    mk "She's fine. Welcome to cataplexy."

    mk "Her muscles stop working when she gets shocked or has big emotions. It's like, bang, you end up a lifeless doll."

    show hisao_talk_small_u at tworightsit with charachange
    hide hisao_talk_big_u at tworightsit

    hi "Part of her narcolepsy?"

    mk "Yep. It ain't always just sleeping, unfortunately."

    show hisao_disappoint_u at tworightsit with charachange
    hide hisao_talk_big_u at tworightsit

    hi "Cataplexy..."

    stop music fadeout 3.0

    "He says the word slowly and carefully, making sure he engraves it onto his mind. He gives the word a lot of weight in the way he says it, which is good to see."

    play music music_dreamy fadein 3.0
    $ persistent.song14 = True

    show hisao_erm_u at tworightsit with charachange
    hide hisao_disappoint_u at tworightsit

    hi "Is it always like this?"

    mk "Well, Suzu's case is.... not light, to put it one way. Usually it's just like, weak knees, or not being able to keep your head up."

    "I feel bad for saying it so plainly, even if Suzu would've done just the same if she were able to right now. She got dealt a really shitty hand, and saying so just makes it feel all the more real."

    show hisao_frown_u at tworightsit with charachange
    hide hisao_erm_u at tworightsit

    "He looks back to her for a moment, but doesn't last long before covering his face with his hands to try and recollect himself. I can't say I blame him."

    hi "Sorry, this is just..."

    mk "It's cool; I had the same reaction as you when I first saw it happen. Hell of a trick, eh?"

    hi "Does she need to be snapped out of it somehow?"

    mk "Give her a minute or two and she'll be right as ."

    show suzu_sleepy at twoleftsitlow with charachange
    hide suzu_asleep at twoleftsitlow
    show suzu_concerned at twoleftsit with charamoveslow
    hide suzu_sleepy at twoleftsitlow

    "No sooner do I say this, than Suzu begins to stir. Groaning slightly, she manages to move her arms to more comfortable positions before ever so slowly levering herself off the table."

    "With a bit of time to reorient herself and rub her eyes, she eventually comes back to the land of the living."

    suz "Don't be sorry about how you reacted. I'm used to it."

    hi "You heard everything?"

    suz "My muscles give out, not my senses. Which can be a pain all on it's own."

    show hisao_erm_u at tworightsit with charachange
    hide hisao_frown_u at tworightsit

    hi "How do you mean?"

    suz "When I get an attack, people often think I've had a seizure, fallen asleep, or fainted. It's not fun to be aware of what people are doing to your body while trying to wake you up, but unable to say anything."

    mk "And that's why it's handy to have someone around who knows all this when you get an attack."

    hi "Makes sense. To be honest, I had no idea narcolepsy included something like that."

    hi "How often does it happen, if you don't mind me asking?"

    "She just shrugs."

    show suzu_speak at twoleftsit with charachange
    hide suzu_concerned at twoleftsit

    suz "It varies."

    "Something's off about her answer. Whenever I've asked her questions about anything, but especially her narcolepsy, she always gives the most specific response she can. Partly because I pressured her into it so I could keep track."

    "Given she has no reason to be vague for his sake, it makes me concerned that her attacks are getting worse and she's trying not to tell me. It's the kind of terrible attempt at secrecy she'd try."

    hi "I'm guessing this is how you got the knee brace?"

    "A nod is her answer. Hisao's simpleminded curiosity is endearing, and Suzu dutifully doles out answers in her usual dull and encyclopedic manner. Talking about it in a generic way doesn't seem to bother her, at least as far as I can tell."

    show suzu_normal at twoleftsit with charachange
    hide suzu_speak at twoleftsit

    "With this, Hisao's line of questioning appears to be at an end. His sits back and thinks for a little, the footsteps of Yuuko approaching our table eventually reaching our ears."

    #move hisoa & suzu to right
    #show hisao_erm at right with charamove
    #show suzu_normal at centersit with charamove
    show yuukoshang happy_down at left with moveinleft
    #play music music_everyday_fantasy fadein 1.0

    yu "What would you like today?"

    show hisao_smile_u at tworightsit with charachange
    hide hisao_erm_u at tworightsit

    hi "Coffee and a slice of pie, thanks."

    mk "Same as him."

    suz "Just tea, please."

    yu "No problem, coming right up!"

    show yuukoshang happy_down at leftsit with charamovefast
    show yuukoshang happy_down at left with charamovefast
    hide yuukoshang with moveoutleft
    #move suzu back left

    "With her usual sharp bow, she scuttles off behind the counter. I still can't decide if the uniforms here are dorky or nice, but it suits her somehow. Not only because it shows off her nice legs, either. Her unusually chipper mood today makes her extra cute."

    show hisao_disappoint_u at tworightsit with charachange
    hide hisao_smile_u at tworightsit
    show suzu_neutral at twoleftsit with charamove
    hide suzu_normal at twoleftsit

    "The three of us end up waiting in silence for our drinks. Suzu takes out her phone and begins tapping away at it, the screen held in front of her as she browses whatever site she's on now. Hisao just looks out the window, his expression showing him to be deep in thought."

    "I kind of want to bug him so I can have a conversation partner, but I decide to leave him be. The boy has a lot to think about right now, after all."

    "Looking around the cafe proves about as boring as expected. A few old people who came to this town to live out a quiet retirement sit at a few of the tables, and a handful students from Yamaku populate the others."
    
    "I think I recognise the back of the class rep's head over the other side of the cafe, but I can't be sure."

    #move hisao and suzu right
    show yuukoshang happy_up at left with moveinleft

    "After what feels like forever, Yuuko emerges with three drinks and two pie slices on a platter. Suzu may live in her own world sometimes, but at least she's polite, putting down her phone as they're set down on the table in order to thank her."

    show yuukoshang happy_down at left with charachange
    play sound sfx_storebell
    pause
    hide yuukoshang with moveoutleft
    #move suzu and hisao back

    "The bell above the door rings out, with Yuuko giving the briefest of nods before quickly scooting off to the entering customers."

    mk "The town's pretty nice, isn't it?"

    show hisao_erm_u at tworightsit with charachange
    hide hisao_disappoint_u at tworightsit

    hi "Hmm? Oh, yeah, it is."

    show suzu_normal at twoleftsit with charamove
    hide suzu_neutral at twoleftsit

    stop music fadeout 1.0

    "Hisao's absentminded reply annoys me a little, but the tinkle of silverware on her teacup draws the attention of both Hisao and I. Suzu ladles teaspoon after teaspoon of sugar into her tea, only stopping after it becomes more a sweet dessert than a drink." #originally said tinker of silverware. Replaced with what I assume Suriko intended -Niji [str]

    show hisao_declare_u at tworightsit with charachange
    hide hisao_erm_u at tworightsit
    play music music_rain fadein 1.0
    $ persistent.song15 = True

    "After staring at his coffee for a bit afterwards, Hisao lets out a long breath before speaking up."

    hi "I wasn't going to mention this, but I probably should."

    "He already has the attention of Suzu and I after speaking, but the both of us become a lot more curious after he moves his tie to the side and begins unbuttoning the top of his shirt."

    "I briefly wonder how much of his chest I'm going to get to see, but he stops after undoing several of the topmost buttons. A shame; he looks like he'd have a nice chest on him."

    "Pulling his collar aside, what he intends to show us becomes clear. The top of a vertical line chasing up the very center of his chest, depressed just slightly into his flesh and shaded a little darker than the surrounding skin."

    show suzu_surprised at twoleftsit with charamove
    hide suzu_normal at twoleftsit

    suz "An operation?"

    show hisao_disappoint_u at tworightsit with charachange
    hide hisao_declare_u at tworightsit

    hi "For my heart. A few months ago I had a heart attack caused by arrhythmia. The scar's from when they cracked my chest open for surgery."

    "So what Haru said was true. I do my best to feign mild surprise, as the fact that I learned it before he was ready to do his show and tell makes me feel a little sheepish."

    "Then again, the fact that there's such a visual indication of what he's been through is a real surprise. I always thought of heart attacks as something you don't really see, but his large scar is impossible to miss. It's jarring."

    mk "That's... damn."

    show hisao_heh_u at tworightsit with charachange
    hide hisao_disappoint_u at tworightsit

    "I feel a bit bad for opening my mouth but failing to find something to say. He gives a weak smile to excuse me for it, but I'd have honestly preferred him to be annoyed with me than make a face like that."

    hi "There you have it. The reason I transferred to Yamaku, that is."

    "Hisao buttons up his shirt and blows on his coffee before beginning to drink it, the fact that none of us really have anything more to say about his revelation becoming obvious. Suzu and I briefly look to each other before doing the same."

    "The more I think about it, the more it makes sense. His inability to keep up with Emi at all on the track, constant resting, weirdness around joining in sports... Given his build, he was no couch potato before it happened."

    "I have to admit that it was a smooth move to show us that right now; I can see the gears turning in Suzu's head. Opening himself up to us like that, especially just after Suzu showed her condition to him so vividly, will go a long way in earning her trust."

    "He probably doesn't know it yet, but it looks like he'll be able to handle her just fine. Not many people can."

    stop music fadeout 2.0

    scene bg suburb_shanghaiint
    show suzu_sleepy at twoleftsit
    show hisao_erm_u at tworightsit
    with shorttimeskip

    "As I chow down the last of my pie, I notice a subtle movement from the corner of my eye. Turning to where it came from, I see Suzu's head beginning to slowly nod, her eyelids also having trouble staying up. She might be working to hide it, but the harder she tries, the more obvious it is."

    "If she's already this bad, she's probably been fighting to stay lucid for a while. Silly girl."

    mk "It's fine."

    suz "Sorry."

    "She looks annoyed, but only in the most routine of ways. It's far from the first time this has happened, after all."

    show suzu_asleep at twoleftsitlow with charamoveslow
    hide suzu_sleepy at twoleftsit

    "The world drops from her consciousness as she lowers herself down to the table, this time in a much more careful way than the last. I dutifully take her empty cup of tea and place it a few inches away as her arms come to rest around her head."

    "Hisao silently looks on, doing his best to appear nonplussed as he defers to my experience in dealing with her."

    "And just like that, Suzu's gone."

    mk "Whelp, she's out for the count."

    hi "This is just sleep, right?"

    mk "Yeah, just a nap. She's gonna be out for a while, most likely."

    hi "Do we wait for her, or...?"

    mk "Nah, I'll just carry her back."

    show hisao_talk_small_u at tworightsit with charachange
    hide hisao_erm_u at tworightsit

    hi "You sure? I can do it if you want."

    mk "Your chivalry is cute, but it's fine. There is something else you can do, though."

    hi "Yeah?"

    mk "Spot me the meal? Pretty please?"

    hi "And why should I do that?"

    mk "'Cause I'm cute."

    show hisao_hmpf_u at tworightsit with charachange
    hide hisao_talk_small_u at tworightsit

    "He just grimaces. I knew I should've gone with 'hot' or 'sexy'."

    show hisao_declare_u at tworightsit with charachange
    hide hisao_hmpf_u at tworightwit

    hi "Alright, I'll do it. That will work exactly once, understand?"

    "Excellent. I wonder how many times I can get him to do that with various excuses."

    "Acting fast before he can retract his offer, I smile and call Yuuko over. With the bill paid over Suzu's peacefully sleeping body, our little outing comes to an end."

    scene bg school_road_ss
    show hisao_erm_u
    with shorttimeskip
    play music music_tranquil fadein 1.0

    "The trudge up the hill back up to Yamaku from town is a journey I've made countless times by now. I'm pretty sure I've lost count of the number of times I've made it while carrying a slumbering girl on my back, too."

    "It's not much of a bother, to be honest. She's a light little thing, worryingly so at times, and it's good exercise for my upper body in any case."

    "Hisao tries his best to look like this is a routine thing, but it's in vain. A one-handed girl walking up a hill with her sleeping friend on her back is just too odd a sight to ignore, at least in the beginning."

    show hisao_talk_small_u with charachange
    hide hisao_erm_u

    hi "I've got no idea how you manage that."

    mk "It ain't so bad. I've been working out since forever anyway."

    "The thought of a girl being stronger than he is clearly dents his pride a little. That he's already breathing heavily while I'm not having much trouble at all just makes it worse."

    "At least he has a fair excuse, given what he said back there."

    hi "It's nice, though. You two must be really close."

    mk "Why do you say that?"

    hi "Suzu trusts you enough to be okay with you manhandling her, and you put yourself out to carry her around. You both seem to have a good handle on each other, too."

    "I think to myself a bit about his words. I suppose it's reasonable for an observer to think that, but I wouldn't really way we're close at all. I struggle for a bit to put our relationship into words, as much for me as for him."

    mk "It's... practical. Yeah, I think that's the best way to describe our relationship."

    show hisao_erm_u with charachange
    hide hisao_talk_small_u

    hi "You fell into each other's orbit."

    mk "Yeah, exactly. You're good with those word things."

    "I'm happy with that description, and I think Suzu would be too, if she could hear it. Hisao, on the other hand, looks quite put off even if he did suggest it. He probably made the assumption just because we were both girls."

    "It's not worth getting too attached at this point, anyway. She's going to get into some good university, just like Hisao is given his constant praise from Mutou. That path is closed for me. Things got a lot better when I stopped caring about that fact."

    stop music fadeout 1.0

    "But even now, as I carry her still body up the hill like this, I still feel the slightest bit comforted by her warmth."

    scene bg school_girlsdormhall
    with shorttimeskip

    "Having parted and gone our separate ways, Hisao to the male dormitory building - after telling me his room number, in case I decide to visit - and the two of us to the female one, I find myself shuffling up the hallway to Suzu's room."

    "It's the floor below my own, unfortunately; if we were neighbors, it'd be a lot more convenient."

    "With my left arm holding up Suzu, I manage to retrieve the key to her room from my pocket after some fiddling. Her convincing the staff to let me get a copy of her dorm room key cut for situations like this was one of her better moves."

    play sound sfx_dooropen

    "A quick flick of the hand, and the lock opens with a satisfying click. Manoeuvring around the door as I open it, the familiar smell of her room hits me before the view does."

    scene bg dormsuzu
    with locationchange

    "It's 'girly', for lack of a better word. I don't know exactly what makes up the scent, beyond probably nail polish remover and light perfume, but it's unmistakable and foreign nevertheless."

    "Closing the door behind us and turning to the room ahead, I slowly navigate the way to her bed, taking care to manoeuvre around the multitude of papers, books, clothes, manga, magazines, and toys scattered around the floor."

    "She has a desk, but that's largely dedicated to her big laptop, plus a few other toys around it."

    "My room might be far from spotless, but at least you can see the floor. Then again, maybe that's just because I don't have the money to constantly buy things."

    "Grunting a little, I turn around at the side of her bed and bend down at the knees, slowly lowering Suzu onto her bed. With the weight lifted from my shoulders, I turn back and set about organising the disheveled heap, moving her legs and arms around to whatever looks reasonably comfortable."

    show suzu_asleep with dissolve
    play music music_suzu

    "My work done, I stand back up and admire my work. I can't help but smile at the absurdity of it all, even after all this time. A perfect little spoiled princess, neatly arranged with her plush toys all around her on the bed to keep her company."

    "I reach down and brush a stray hair away from her closed eyes, my gaze lingering a little on her motionless face. It's almost painful how delicate she looks, like a china doll that could crumble any second."

    "She really is a real life Sleeping Beauty."

    "I shouldn't get so sentimental about it. Maybe it's because I've only ever hung around with guys that a girl who actually acts like one feels so strange. It could just be yearning for a side of me I've never had a chance to explore. Who knows."

    hide suzu_asleep with dissolve

    "Well, whatever. I turn and scratch the back of my head as I make to leave, trying to brush the thoughts from my head. It doesn't really matter what Hisao thinks about our relationship; I'm not the kind of person a girl like her should be around."

    scene hatsune with dissolve

    "I stop for a moment as I'm distracted by an actual doll on Suzu's shelf. An energetic-looking girl in bright clothes from some show she watched a while ago."

    "She has a lot more at home, but only brought a handful to her dorm. She might call them figures rather than dolls, but I don't really get the difference."

    "I poke at its head for something to do as I mull things over."

    "We really are from two different worlds. For all I try, I can't think of a damn thing we have in common. I'm envious of so many things about her, from her innocence, to her family, to her wealth, but I've never bothered mentioning it."

    "Some people pop out of the right set of legs, and others don't. Some people mess everything up, and others don't. That's life."

    suz "Don't..."

    scene bg dormsuzu
    show suzu_sleepy
    with dissolve

    "Suzu's voice, little more than a faint and mumbled whisper, draws my attention to her as I obediently stop tweaking at her doll. It looks like she's awake, albeit only by the most generous definition."

    "She rubs her eyes, but does little beyond stare at the ceiling. I've always thought it must be hard to constantly be waking up in different places than where you went to sleep, but she's never once complained about it."

    mk "You okay?"

    suz "I'm fine."

    "No, she's not. Her voice has a slightly miffed edge to it, which she's too groggy to try and cover for."

    "She's never worried about being a bother to me before. Not that I mind; being useful to at least one other person in the world is something I need. She's a total idiot socially, but I think even she managed to work that out for herself."

    "That leaves the only other person that was with us."

    "It's kind of cute, really, getting all rattled about her narcolepsy in front of a boy. I shouldn't smile, but it's hard to suppress. Having just transferred, it's unlikely Hisao would have a girlfriend right now, so she's in with a good chance."

    mk "Don't feel bad about it. Hisao's pretty understanding."

    show suzu_concerned with charachange
    hide suzu_sleepy

    suz "He's a total babe in the woods is what he is."

    mk "Haha, you got that right. He's totally helpless right now."

    mk "What do you think of the guy?"

    show suzu_surprised with charamove
    hide suzu_concerned

    "She looks at me a moment trying to ascertain my intentions. That was an amazingly direct way to try and gauge her feelings towards him, after all."

    show suzu_speak with charamove
    hide suzu_surprised

    suz "He's sensible. I don't mind him."

    "Well done, Hisao. That's one of the highest compliments someone could ever hope for from her."

    "She's not wrong, though. He might be a nerd, but he's comfortable dealing with the other club guys as friends. His sensitive side is enough to make Suzu lower her guard around him as well, which is someone none of those guys could ever do."

    "Looks like I'm stuck with him, then. There aren't many that can overcome Suzu's distrust of others, and as far as friends go, I could do a lot worse than Hisao. Having someone around who doesn't know about my past means a lot less baggage to deal with, too."

    suz "What are you smiling about?"

    mk "Nothin'. Just take it easy for today, alright? And eat a snack or something; don't think I missed you skipping lunch."

    show suzu_normal with charachange
    hide suzu_speak

    suz "Only if you promise to do your homework for once."

    mk "Alright, alright, I will. See you tomorrow."

    suz "See you."

    "With that, I give her a parting wave before leaving the room and its girly smell."

    scene bg school_girlsdormhall
    with locationchange
    stop music fadeout 1.0
    play sound sfx_doorclose

    "Entering the hallway and carefully closing her door behind me, all I can do is rest my back against it as I close my eyes and sigh. Looks like the last few months of my time here won't be as simple as I expected."

    window hide

    scene black
    with dissolve

    return
