# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a3_shizune:
    label .force_feedback:
        scene bg school_hallway3
        with locationchange

        nvl clear
        nvl show dissolve

        $ renpy.music.set_volume(0.5, 0.0, channel="music")
        play music music_normal fadein 3.0

        n "{vspace=60}The following days pass uneventfully and with surprising quickness. I find renewed motivation to learn sign language. It seems that I have a knack for learning sign, so it would be a waste to not do it, and falling behind would be even more unacceptable."

        n "Summer break is coming up. Even though I figured that student council work would see a drop-off proportional to how lethargic my classes are becoming, it doesn't happen that way. Every day, I get swamped under increasingly meaningless work."

        n "Despite how much I want to, I don't have even a free second to talk to Shizune nowadays. Every time I look at her, her face is buried in some book of records or some stack of papers that need to be checked over in triplicate."

        n "{vspace=60}Today, I woke up early to come to school before everyone else, hoping to catch Shizune. She has a habit of coming in first thing in the morning, to be more punctual than all the other students. Unfortunately, I think I am earlier than her."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl clear
        nvl hide dissolve

        play sound sfx_doorclose

        "Hearing the student council room door click closed to my right tells me that isn't the case. I guess I got here just behind her."

        play sound sfx_dooropen

        scene bg school_council
        with locationchange

        "I enter the room and tap Shizune on the shoulder to get her attention."

        show shizu behind_smile at center
        with charaenter

        "Maybe she expects a conversation, which is why she puts down the carton of orange juice in her hand."

        ssh "Good morning."

        his "Where's your better half?"

        show shizu adjust_frown
        with charachange

        ssh "We are separate individuals."

        "Thinking about it, they must get that quite a bit. I can think of no other way to explain how ready she was with that answer."

        show shizu basic_normal
        with charachange

        ssh "You're here early. That's good, you can help me look over some handouts. They're going out later today."

        his "I came here early specifically so I could see you without having to do work."

        show shizu behind_smile
        with charachange

        ssh "According to Misha, being early isn't new for you."

        his "It's not new for you either."

        show shizu adjust_happy
        with charachange

        ssh "Are you saying you want to race?"

        "Shizune adjusts her glasses nonchalantly, a gesture that belies how giddy she is inside about the thought of having something very petty to take competitively and seriously. I think the smaller the matter is, the more it excites her."

        his "It's not a race. Do you want to make it a contest? I don't."

        "I almost forget to add the last part, the most important part."

        show shizu behind_smile
        with charachange

        ssh "…Well, that's fine. There are too many days left in the school year, I'd get tired of it anyway."

        "With that, Shizune picks up her juice and finishes it off. I wonder if she's going to try and shoot the empty container into the trash, but she doesn't. In fact, she seems puzzled as to why I seem so disappointed. I'd better get to the point."

        his "I just wanted to talk. Our break is practically here, you know."

        his "And we should spend more time together, anyway. I was thinking that we could do that over the summer."

        show shizu adjust_blush
        with charachange

        "Shizune's face turns as red as mine must be, and she starts adjusting her glasses, flustered. What an all-purpose gesture. She taps her fingers together in thought, considering her next words carefully."

        show shizu basic_normal
        with charachange

        ssh "You mean like a date?"

        his "Just because we're going out somewhere, that instantly makes it a date?"

        show shizu behind_blank
        with charachange

        ssh "It's not?"

        show shizu adjust_frown
        with charachange

        ssh "I want it to be a date."

        his "Then it is one."

        show shizu basic_happy
        with charachange

        "Shizune approvingly claps her hands once, before adding on to my statement:"

        show shizu behind_blank
        with charachange

        ssh "But not today."

        show shizu basic_normal2
        with charachange

        ssh "I'm going away for a week to visit my family."

        "That is an oddly formal way of putting it, and for that reason, my interest is piqued. Maybe her family is the prim and proper, traditional kind, living in a giant old-timey mansion with a little stream and koi pond, where everyone wears kimonos all the time."

        "It's a wild assumption, but it's fun to speculate sometimes. I wonder if Shizune puts on the appearance of being a calm and mature good daughter like Lilly when she is with her family."

        "I can't imagine it, but if there's even a possibility that it's true, then I must see it."

        his "Only a week? It must not be that far of a trip, then."

        show shizu behind_frustrated
        with charachange

        ssh "Of course not, they're still in Japan, after all."

        his "Really…"

        show shizu adjust_happy
        with charachange

        ssh "It isn't like you can come with me. Is that what you're trying to say?"

        his "Why can't I?"

        show shizu basic_normal2
        with charachange

        ssh "It isn't like you would enjoy it."

        his "You don't know that. It could be fun."

        his "Ah, I almost forgot: you didn't answer my question. Are you going alone, or is Misha going with you? Does your family know sign?"

        show shizu behind_blank
        with charachange

        ssh "Misha is coming along."

        "The part of the question left unanswered is the most telling."

        "If Shizune's family can't communicate with her, I have to wonder what her childhood was like. She probably wrote everything on that pad she carries around and still produces out of nowhere sometimes."

        "Usually, it's when neither Misha nor I are around. I can notice her from far away when she pulls it out like a last resort, grimacing the whole time."

        his "If Misha is going, then I'm going to go, too."

        show shizu basic_normal
        with charachange

        ssh "Do you like Misha?"

        his "It's the principle of the thing."

        "I entertain the notion that Shizune might actually be jealous, but I doubt it. She usually wears her emotions pretty plainly on her face, and I don't see anything that would support my theory right now."

        show shizu adjust_frown
        with charachange

        ssh "I think you're just bored."

        show shizu behind_smile
        with charachange

        ssh "That's okay, though. All right, we'll all go together. It's what I hoped for in the first place."

        show shizu adjust_smug
        with charachange

        ssh "You can't skip out on Student Council today to pack your bags, just because you're coming with us on such short notice, it's no excuse!"

        his "It's okay, I hardly have anything to pack anyway."

        show shizu basic_normal
        with charachange

        "Shizune pauses, tenting her fingers thoughtfully."

        show shizu behind_blank
        with charachange

        ssh "You must have come to this school on very short notice."

        if not side_lilly and wait_for_shizu or _in_replay:
            "It could be that she is thinking back to the time when she and Misha unexpectedly shoved themselves into my room and caught a glimpse of all my medicines. That was an awkward moment I'd like to forget, and I don't like revisiting it."

            "The way she tiptoes around the issue even now only makes me more uncomfortable."

        his "I did. It was kind of an on-the-spot decision. It worked out better than I expected, though."

        "I hope Shizune won't pursue the matter, and to my relief, she doesn't."

        show shizu adjust_happy
        with charachange

        ssh "My home is in a particularly beautiful part of Saitama."

        show shizu behind_smile
        with charachange

        ssh "We'll be leaving early in the morning, so be ready. Let's talk about it more later, okay? For now, those handouts won't look over themselves, and you're going to help me."

        stop music fadeout 3.0

        hide shizu
        with charaexit

        "As Shizune dives into her work, pulling me along with her, I think that she seems almost, but not quite, excited to go."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .united_nations:
        scene bg school_dormhallway
        with locationchange

        play music music_daily fadein 0.5

        "When Shizune and Misha arrive early the next morning to pick me up, they are dressed in something other than the school uniform I've grown used to seeing them in."

        show shizu behind_blank_cas at center
        with charaenter

        "It makes sense, since we're on holiday, but it's still jarring. Shizune's dress is sharp and fashionable, almost too much for a quiet place like Yamaku. Thinking back to what she wore at the Tanabata festival, I'm starting to notice a trend with her."

        "All of her clothes are very tasteful and mature; very well thought out. So, then, I wonder why she herself is so immature."

        show bg at bgright
        show shizu at tworight
        with charamove

        show misha perky_smile_cas at twoleft
        with charaenter

        "Well, at least Misha's clothes reflect her inner self on the outside."

        show shizu adjust_frown_cas
        with charachange

        ssh "You're bringing so little."

        hi "I said I would. I said there wasn't much to pack."

        show shizu basic_frown_cas
        with charachange

        "Shizune pouts and rocks her own, rather large collection of luggage with her foot as if embarrassed. Misha only has one suitcase with her, but it's almost larger than she is. She looks self-conscious about it as well."

        "God, that suitcase is as big as a compact car. The pea green color is unsettling, too. It's like something used to transport bodies. The way they look right now makes me want to tease them a little."

        hi "Aw, that's bad luck for you and Misha, isn't it? Having to carry those huge bags. Gotta pack light next time, like me. Everything fits into one little suitcase."

        show misha hips_grin_cas
        with charachange

        mi "Like James Bond~!"

        hi "Yes, exactly like James Bond."

        show shizu adjust_frown_cas
        with charachange

        shi "…"

        "Shizune gently tugs at her glasses in concentration."

        show shizu basic_normal_cas
        with charachange

        ssh "We should split the amount we carry equally."

        show misha sign_smile_cas
        with charachange

        mi "Wow~! That's a great idea, Shicchan~!"

        hi "What? No."

        show shizu adjust_smug_cas
        with charachange

        ssh "It would benefit us all."

        show misha cross_laugh_cas
        with charachange

        mi "Yup~! Wahaha~!"

        hi "I'm going to have to say no."

        show shizu cross_angry_cas
        with charachange

        ssh "You're outvoted!"

        "She almost lunges forth as she signs it. Terrifying."

        hi "Ah, well. I was just kidding. I don't mind carrying a few extra. I just thought it would be fun to mess with you both."

        hi "But, if you were going to try and make me carry it all, I was going to ride that giant green case down the mountain like a sled."

        show shizu adjust_smug_cas
        with charachange

        shi "…"

        "That seems to make Shizune laugh, and she holds a hand up to her mouth to hold it back. It's like she is hiding it. I wonder if she can laugh. If not, that might be why she does that. That kind of makes me feel sad."

        stop music fadeout 3.0

        scene bg city_station
        with locationskip

        "With that taken care of, we head for the train station, and a very uneventful ride follows. Shizune and Misha manage to fall asleep almost instantly, but I find myself unable to. That's never happened before. Maybe it's my medication."

        scene bg shizu_houseext
        with shorttimeskip

        play music music_soothing fadein 0.5

        "When we arrive at Shizune's house, it's quite a bit larger than I'd envisioned it would be. I don't think huge would be much of an overstatement."

        hi "You live in a mansion?"

        show shizu cross_angry_cas at center
        with charaenter

        "Shizune indignantly stands up on her tiptoes so that we're at eye level, and frowns deeply, having had my comment translated to her by Misha. It's as if she's saying, 'how can you even suggest such a thing?'"

        show shizu basic_frown_cas
        with charachange

        ssh "This is just a normal house. Nothing as ostentatious as a mansion."

        "I believe our definitions of those terms are quite different, then."

        show bg at bgright
        show shizu at tworight
        with charamove

        show misha hips_grin_cas at twoleft
        with charaenter

        mi "Wahaha~. Hicchan, are you surprised? Do you want me to point out where you'll be staying?"

        show shizu behind_blank_cas
        with charachange

        ssh "I think we have a guest room, but I'm not sure if we have two. I'll check."

        show misha sign_smile_cas
        with charachange

        mi "Hm~, it's no problem, though, Hicchan~! Shicchan and I can share a room if we have to. Well~, unless hers is being used for something else now."

        hide shizu
        with charaexit

        hide misha
        with charaexit

        stop music fadeout 5.0

        "'Not sure?' I'm starting to think Shizune doesn't spend a lot of time at home. Before I can make a joke of it at her expense, Shizune vanishes into the house, and Misha goes with her, leaving me alone on the grounds."

        "I don't want to follow them inside just yet. I put my bag down by the front door, and take the opportunity to look around the grounds, just making a quick lap around the house."

        show hideaki bored at center
        with shorttimeskip

        "Even though it takes just a few minutes, when I get back the first thing I notice is that my bag is gone, and a tiny girl is in its place. She looks a lot like Shizune, although Shizune wouldn't wear red shorts and star-and-moon stockings."

        hi "Hi! Are you Shizune's little sister or something?"

        show hideaki normal
        with charachange

        hh "No. I'm her little brother. My name is Hideaki."

        show hideaki thinking
        with charachange

        hh "It's nice to meet you."

        play music music_happiness fadein 2.0

        "The voice that responds is straightforward, monotone, and also definitely male. I feel embarrassed to the point where I could almost turn around and leave right now, if I could remember my way back to the train."

        show hideaki serious
        with charachange

        hh "Are you the second person that my sister brought with her?"

        hi "'Brought with her?' I'm not luggage."

        hi "Anyway, I'm Hisao. Did you take my bag?"

        show hideaki triangle
        with charachange

        hh "Yes, it is my right to keep anything I find on my property."

        hi "No, it's not. That's not how it works at all."

        "I guess even particularly well-spoken little kids believe in the law of finders keepers. Even though I call him little, he doesn't seem that much younger, now that I think about it. Maybe two or three years younger, at most."

        show hideaki normal
        with charachange

        hh "I gave it to Shizune. It's inside. Are you on the Student Council?"

        hi "Yeah, how did you know? Does she bring it up often?"

        "I almost said 'does she talk about it often?' That could have been bad."

        show hideaki bored
        with charachange

        hh "Yes, all the time. Do you get along with her?"

        hi "Get along? That's a weird question. I wouldn't be on the Student Council if I couldn't get along with her. What about you, do you two get along well?"

        "Even though he has a monotone voice, his face is as expressive as Shizune's, and belies how he really feels. It must run in the family. Looks like he isn't happy about my question, for whatever reason."

        show hideaki thinking
        with charachange

        hh "I'm sorry. I was only asking because you both act so much alike."

        "I don't know why, but it feels like he's teasing me. Unfortunately, it works. I don't like being compared to Shizune."

        hi "You're a lot more like Shizune, but that's to be expected. I mistook you for her little sister, even. If you don't want people to make that mistake, you should dress more appropriately."

        show hideaki confused
        with charachange

        hh "I don't understand, my clothes are perfectly seasonal."

        hi "What's with the stockings?"

        show hideaki angry_up
        with charachange

        hh "They are cool."

        show hideaki disapproves
        with charachange

        hh "You act like my sister. Eventually people will start mistaking you for her."

        "I guess my comment hit him harder than I thought. That would explain this attempt at turning it around."

        hi "I hate being compared to other people."

        show hideaki evil
        with charachange

        hh "Shizune doesn't like it when she is compared to others either."

        "I'd thought that Hideaki was a little more mature than Shizune, but they have the same competitive streak and inclination to provoke people. I wonder if he's like this because of Shizune, or if it's the other way around."

        hi "And neither do you, right? Okay, I get it. I shouldn't be so petty."

        show hideaki normal
        with charachange

        stop music fadeout 4.0

        "Especially to little kids. Hideaki seems to accept this as an acknowledgment of defeat, which is something that I feel like I can't let go. Nevertheless, I'll just have to let it go while I have the chance."

        scene bg shizu_living
        with locationchange

        "I can hear Misha's laughter bouncing through the halls the moment I step through the door to the house, and follow it into what I would guess is the living room. It holds more people than I'd expected."

        show lilly basic_displeased_cas:
            center
            ypos 1.17 xpos 0.55
        show akira basic_boo:
            tworight
            ypos 1.15 xpos 0.72
        show hideaki bored:
            center
            xpos 0.92
            easein 1.0 ypos 1.1
        show shizu behind_blank_cas:
            twoleft
            ypos 1.11 xpos 0.27
        show misha perky_smile_cas:
            center
            ypos 1.1 xpos 0.08
        with charaenter

        play music music_another fadein 4.0

        "Among them I spot a distinctive and familiar blonde ponytail. I'm more confused by why Lilly is here than surprised. Shizune seems just as surprised. Lilly doesn't look ecstatic about this chance meeting either."

        "Sitting next to Lilly is a tall, androgynous looking woman in a sharp suit. I'd like to assume that it's her older sister, but I don't want to risk it."

        show lilly basic_listen_cas
        with charachange

        li "I didn't expect that you would arrive so early."

        "At first I think she's talking to me, but it turns out that she's referring to Shizune. I don't think Lilly even notices my presence. I've clearly walked in on them mid-conversation, and it looks like with her focus on Shizune, she couldn't hear me."

        show shizu basic_frown_cas
        with charachange

        ssh "I should have rearranged my entire schedule for you."

        show misha sign_smile_cas
        with charachange

        mi "Shicchan says: I should have rearranged my schedule just for you~!"

        show lilly basic_displeased_cas
        with charachange

        li "That would have been nice, but I would not expect you to do such a thing."

        show misha hips_smile_cas
        with charachange

        mi "Oh, hi, Hicchan~! You're finally here."

        hi "Yeah. Hello, Lilly."

        show lilly basic_surprised_cas
        with charachange

        li "Oh, Hisao? This is quite a surprise. Akira, this is Hisao, a schoolmate. Hisao, this is Akira, my sister."

        show akira basic_smile
        with charachange

        aki "Yo."

        "She holds up her hand in a brief and quite casual gesture of greeting. So she is the older sister after all."

        show akira basic_boo
        show lilly basic_weaksmile_cas
        with charachange

        aki "I hope we're not messing up any of your plans. Since we're only going to be here for one more day, Lilly and I thought she may as well come with me."

        "Akira turns to me, like she feels compelled to explain. I'm grateful for that."

        show akira basic_ending
        with charachange

        aki "I suppose my position here would be best described as a babysitter."

        show hideaki disapproves
        with charachange

        "Akira ruffles Hideaki's hair as he carries on with his pastime of looking displeased."

        hh "That is demeaning."

        show akira basic_smile
        with charachange

        aki "Really? Maybe I'll change my title once you get a few more years on you. Or at least a few centimeters."

        "They make an interesting pair, although Akira looks more like a lawyer than a babysitter. I'm still not really sure why both she and Lilly are here, though."

        "Taking a glance around the room, there are tennis rackets, golf clubs, and even a stack of fishing poles and tackle boxes secreted here and there."

        "Behind every chair, in every corner, and under every table there is some piece of outdoor hobbyist equipment. I pick up one of the fishing rods and play with it."

        hi "This is a nice house."

        hi "Shizune, it looks like your dad has a lot of hobbies."

        show misha sign_smile_cas
        with charachangealways

        show misha perky_smile_cas
        with charachangealways

        "For a moment I forget to sign what I say, but Misha's already in the process of interpreting what I said for her. I'm still a little impressed at how automatic interpreting is for Misha."

        show hideaki normal
        with charachange

        hh "Do you fish?"

        hi "No, I don't know how. I kind of want to learn, as I heard it's relaxing."

        show shizu behind_blank_cas
        with charachange

        ssh "There is a river only a short drive away, my whole family knows how to fish. If you want, we could go there sometime."

        show akira basic_laugh
        with charachange

        aki "You and Hideaki can fish? I didn't expect people your age to know, considering it's always seemed like a hobby for old men."

        show akira basic_ending
        with charachange

        aki "Y'know, Lilly is great at cooking. If we had some fresh fish…"

        "It's not hard to follow Akira's train of thought."

        show lilly basic_displeased_cas
        with charachange

        li "If you want to eat fish, we could go to the store."

        "Lilly's voice sounds slightly more authoritative than usual. She really doesn't seem to share her sister's enthusiasm for the idea."

        show shizu basic_happy_cas
        with charachange

        shi "…"

        show misha hips_grin_cas
        with charachange

        mi "It's more fun to go fishing; we could even make it like a game and try to see who catches the biggest one~! That would be exciting, right? Yeah~! Hicchan, what do you think? It sounds fun, doesn't it?"

        hi "Yeah, it definitely could be."

        show akira basic_smile
        with charachange

        aki "Sounds like a plan. I don't know how to fish either, so now's as good a time as any to learn."

        show akira basic_boo
        with charachange

        "Her eyes shift towards Lilly, who remains unmoved. This sours Akira's smile a bit, and makes me wonder why Lilly's being so obstinate about this."

        show hideaki normal
        with charachange

        hh "I don't think we have enough fishing equipment for everyone."

        show shizu behind_smile_cas
        with charachange

        ssh "We can take turns. It'll be a team battle."

        show hideaki confused
        with charachange

        hh "What is she saying?"

        hi "We can take turns. She also wants to make it a contest."

        show akira basic_laugh
        with charachange

        aki "Come on Lilly, we may as well make the most of it."

        show akira basic_boo
        with charachange

        aki "So is this going to be a competition to see who can catch the biggest fish, or the most?"

        show shizu adjust_smug_cas
        with charachange

        ssh "It looks like the older sister understands better, as always."

        show shizu basic_normal_cas
        with charachange

        shi "…"

        show misha sign_smile_cas
        with charachange

        mi "Shicchan says that she supposes Lilly would prefer to go to the store, right~? It's much less work, so it's natural that she would! Going fishing would be more fun, though, and save money. Akira, you have the right idea~!"

        show akira basic_smile
        with charachange

        "Akira gives a gracious, if slightly stilted, smile. Shizune's praise wasn't her goal, after all."

        show lilly basic_sleepy_cas
        with charachange

        li "…"

        show lilly basic_weaksmile_cas
        with charachange

        li "Isn't the river quite far away?"

        show akira basic_ending
        with charachange

        aki "I don't think it's that far, and I can drive if we have to. I'm okay with it, as long as you catch something."

        hi "Can your car fit this many people, and a whole lot of fishing gear on top of that?"

        show akira basic_boo
        with charachange

        "She purses her lips as her fingers subtly move, counting up the amount of passengers and the required cargo. If we're going to be taking me, Shizune, Misha, Lilly, Akira, and Hideaki…"

        show akira basic_lost
        with charachange

        aki "Six people. Damn, my car can only take five."

        show akira basic_ending
        with charachange

        aki "Actually, if Hideaki sat on my lap, we could—"

        show hideaki angry_up
        with charachange

        hh "I'm not sitting on your lap."

        show akira basic_resigned
        with charachange

        aki "Aw."

        show shizu adjust_happy_cas
        with charachange

        shi "…"

        show misha hips_smile_cas
        with charachange

        mi "Shicchan says that her father's car would be big enough."

        show akira basic_lost
        with charachange

        aki "What, the Fuga? If he doesn't mind us using it, then I guess we have no other choice. Feels kinda bad forsaking my car, considering I won't have it for much longer."

        "Despite Lilly's obstinacy, and Hideaki's questions of whether or not we'd prefer to eat first than bet on a fish dinner that might fail to ever materialize, there is no way to dissuade Akira and Shizune as they agree on the transport plan."

        stop music fadeout 5.0

        scene ev shizune_car
        with shorttimeskip

        play ambient sfx_businterior fadein 1.0

        "My expectations of a somewhat relaxing drive through the countryside are fulfilled. Akira's driving is as smooth and peaceful as the surroundings, to the point where Misha falls asleep during the trip."

        "I thought this trip would have been rather too slow-paced for Shizune's liking, but she seems to genuinely enjoy it. Even with Hideaki awkwardly sandwiched between her and the door, she just keeps looking out of the window and smiling."

        stop ambient fadeout 0.5

        scene bg shizu_fishing at left
        with shorttimeskip

        play ambient sfx_parkambience fadein 0.5

        "The area surrounding the river is quite beautiful. Akira and Shizune head off for the river so quickly that we have no choice but to chase them. We would be left in the dust, otherwise."

        show lilly basic_weaksmile_cas at left
        show hideaki bored at center
        show misha hips_grin_cas at right
        with charaenter

        "I can see Hideaki and Lilly are just humoring their siblings, Lilly being the more unenthusiastic of the two. Misha seems as happy as ever, though. Looks like she managed to latch onto some of Shizune and Akira's excitement."

        "As for myself, I'd rather eat now, but the thought of fresh fish prepared by Lilly is appealing."

        "The river is larger than I'd imagined, although very scenic and peaceful. Other than a small pier apparently built just to fish off of, this place looks untouched by civilization, and it makes me realize how much greenery I've seen lately."

        show shizu basic_happy_cas:
            center alpha 0.0
            ease 1.5 xpos 0.37 alpha 1.0
        show akira basic_smile:
            center xpos 0.8 alpha 0.0
            ease 1.5 xpos 0.8 alpha 1.0
        show misha perky_confused_cas:
            left alpha 0.0
            ease 1.5 alpha 1.0
        show lilly:
            left alpha 0.0
            ease 1.5 xpos -0.6 alpha 1.0
        show hideaki:
            ease 1.5 offscreenleft alpha 0.0
        with None

        show misha
        show shizu
        show akira

        show bg at right
        with charamove

        show shizu:
            center
            xpos 0.37
        show akira:
            center
            xpos 0.8
        show misha at left
        show lilly:
            left
            xpos -0.6
        show hideaki:
            offscreenleft
            alpha 0.0

        "Shizune pulls Misha away so that they can explain how to fish to Akira. Lilly and Hideaki are talking between themselves, so I decide to join the enthusiastic trio."

        show akira basic_ending
        with charachange

        aki "Hmm… so which one of these lures should I use then? Can I use this cute little one?"

        show shizu basic_frown_cas
        show misha sign_smile_cas
        with charachange

        mi "Wait, wait~! This is a contest, we need to pick teams first! Shicchan and I will be on one team, of course. Hicchan, you're going to be on our team too, won't you? We can be the Student Council team~!"

        hi "Okay."

        show akira basic_laugh
        with charachange

        aki "All right, then. That makes me, Hideaki, and Lilly on the other team. Lilly, what should we call ourselves?"

        stop music fadeout 2.0

        play sound sfx_flash

        show lilly basic_sleepy_cas:
            ease 0.5 twoleft alpha 1.0
        show hideaki bored:
            ease 0.5 tworight alpha 1.0
        show misha:
            ease 0.5 xpos 0.85 alpha 0.0
        show shizu:
            ease 0.5 offscreenright alpha 0.0
        show akira:
            ease 0.5 center xpos 1.5 alpha 0.0

        show bg at left
        with charamovefast

        show lilly at twoleft
        show hideaki at tworight
        show misha:
            center
            xpos 0.85 alpha 0.0
        show shizu:
            offscreenright
            alpha 0.0
        show akira:
            offscreenright
            alpha 0.0

        call screen doublespeak(li, _("I don't see why it matters."), hh, _("I don't think it matters."))

        play sound sfx_flash

        show lilly:
            ease 0.5 xpos -0.6 alpha 0.0
        show hideaki:
            ease 0.5 offscreenleft alpha 0.0
        show misha perky_confused_cas:
            ease 0.5 left alpha 1.0
        show shizu basic_angry_cas:
            center
            ease 0.5 xpos 0.37 alpha 1.0
        show akira basic_ending:
            center
            ease 0.5 xpos 0.8 alpha 1.0

        show bg at right
        with charamovefastest

        hide lilly
        hide hideaki

        show misha at left
        show shizu:
            center
            xpos 0.37
        show akira:
            center
            xpos 0.8

        show akira basic_lost
        with charachangealways

        aki "Team No-Enthusiasm it is…"

        play music music_comedy fadein 0.5

        "Yet again, Akira's best efforts are rebuffed. Shizune and Misha, on the other hand, have no lack of enthusiasm whatsoever."

        show misha hips_smile_cas
        show shizu behind_frown_cas
        with charachange

        ssh "Hisao! You can be our point man, please try hard to catch as many, or the biggest, fish possible."

        hi "Why me? No one's even taught me how to fish yet."

        show misha hips_grin_cas
        show shizu behind_blank_cas
        with charachange

        mi "We can do that now~."

        "After a quick tutorial, Shizune immediately tries to draw us into a discussion about the strategy in a tag team fishing competition."

        "Somehow, competition doesn't seem particularly applicable to a sport where you spend hours sitting down and hoping a fish bites a worm."

        show shizu adjust_happy_cas
        with charachange

        ssh "It looks like Hideaki got stuck with the spare rod. You know it's just a string tied to a bamboo pole, right? That means when deciding the order, you should go against him."

        hi "What, why me?"

        show misha sign_smile_cas
        with charachange

        mi "You have the least experience here, Hicchan~."

        hi "Yeah? So who's the best here? Shizune? Hideaki is your brother, he's probably just as good. He probably fishes all the time, since he lives closer to a lake. He might even be better."

        show akira basic_annoyed
        with charachange

        aki "Watching you three makes my head hurt. You know I'm only hearing two thirds of a conversation, right? What's this about?"

        hi "Picking our lineup."

        "Akira makes a troubled face. She's getting impatient, which probably isn't too unreasonable."

        show shizu basic_sparkle_cas
        with charachange

        ssh "If you're impatient, that only makes me more excited. Now I want to play for higher stakes."

        show akira basic_lost
        with charachange

        aki "What's she saying?"

        hi "She wants to play for higher stakes."

        show akira basic_laugh
        with charachange

        aki "I wouldn't be too hasty; we have beginner's luck twice over on our side, after all. The only way you'll be able to beat that is by catching a whole ocean."

        show shizu adjust_happy_cas
        with charachange

        shi "…"

        show misha hips_grin_cas
        with charachange

        mi "This is a freshwater body of water, you marine biologist~."

        "A weird insult, delivered with unblinking and innocent good cheer. Akira doesn't seem bothered. She laughs it off, and Shizune looks like her usual mischievous self again. I'm glad they get along."

        show akira basic_smile
        with charachange

        aki "So are we going to pick teams, or what? I'm getting kinda hungry…"

        show shizu basic_normal_cas
        with charachange

        ssh "Hisao, Misha, and I are on one team, and Lilly, Hideaki, and you are on the other, aren't you?"

        show akira basic_ending
        with charachange

        aki "I suppose that's the most obvious arrangement. Wouldn't mixing it up a little be more fun, though? Eh?"

        show misha perky_smile_cas
        with charachange

        mi "Hmm~, you don't want to fish with your own sister?"

        show akira basic_boo
        with charachange

        aki "Well, neither of us know how to fish, so putting both of us on the same team is kinda…"

        "Well, it sounds like I've heard something kind of dangerous. I try to change the subject before Shizune can turn that incredulous look on her face into anything more."

        hi "So, I guess you and Shizune know each other?"

        show akira basic_smile
        with charachange

        aki "Sure do. We go way back."

        show shizu basic_normal2_cas
        with charachange

        "Akira throws a knowing grin at Shizune. It's not until Misha's finished translating what she's said that Shizune gains a troubled face."

        "Akira sure is different from Lilly. Aside from how they look, she's much more informal and laid back. I expected Lilly's family to all be proper and formal like her, so this is a surprise. But, I feel like she's easy to talk to."

        show akira basic_laugh
        with charachange

        aki "As much as I like talking about catching fish, we should probably actually do it sometime."

        show shizu behind_blank_cas
        with charachange

        ssh "Would you suggest that there should be a lineup, like in baseball? Or should it be everyone-at-once, or a tag battle style?"

        show shizu basic_sparkle_cas
        with charachange

        ssh "Can everyone sit wherever they want, or do teams have to stick together? Do we call where we fish? What fish sizes will we be counting?"

        show akira basic_lost
        with charachange

        "Seeing Akira groan after Misha dutifully translates for her, Shizune rubs her glasses, laughing silently."

        show shizu adjust_happy_cas
        with charachange

        stop music fadeout 4.0

        ssh "Never mind. Let's just fish, then."

        show shizu behind_smile_cas
        with charachange

        ssh "It can be an individual contest."

        stop ambient fadeout 2.0

        scene ev shizu_fishing_ah
        with shorttimeskip

        play music music_ease

        "I sit down, ready to fish, although I'm not feeling very confident. Everyone else is already sitting, except Akira, who takes a seat next to me and throws her line out after taking off her suit jacket and rolling up her sleeves."

        "Misha and Hideaki end up sitting on the shore and fishing together, as there's not enough room on the pier for everyone. Truth be told, I'd rather be sitting next to Shizune, but Akira seems approachable enough."

        aki "Careful there, you're a little close. Don't tangle our lines, 'kay?"

        hi "So, you've never fished before?"

        aki "No, but I've seen a bit of it on TV. I always wanted to catch one of those big fish with a sword for a face. Marlin, I think."

        li "If I recall correctly, those are from the ocean; they are saltwater fish."

        aki "I know that. Why's everyone acting like I don't know the difference between freshwater and saltwater fish?"

        li "If you aren't careful, you'll scare off the fish, saltwater or not."

        "Akira's voice is somewhat loud between her attempts to both egg on Shizune and keep Lilly entertained, so she may have a point. My line doesn't seem to be picking up anything, but I don't know how much of that is down to Akira."

        "Shizune does her best to relax in the sun, and pulls the look off very well, but I can tell that she'd be slightly put off by not knowing what's being talked about. Not having Misha around can be a real problem."

        ssh "Hisao, what's the score so far? Are we winning? I hope we are, given that I've entrusted you with our team's success."

        "I manage to do some awkward signing with creative placement of my rod. It's probably close to being gibberish in spoken terms."

        hi "You're like, right there. Can't you tell?"

        ssh "Disappointing; you let yourself get distracted. You have to stay focused."

        hi "Should have known. Well, it's 0-0 in any case."

        "Akira chuckles, although it's clear that really took the wind out of her sails."

        hi "Is it just numbers now, or are we keeping track of size, too?"

        ssh "Both; grading matters."

        hi "Who's going to be grading them? Are you a certified fish judge?"

        "Shizune shakes her head to signify that she isn't."

        ssh "…But it doesn't seem like it would be very hard. Tell Misha to stop flailing her hands around like that, it's scaring all the fish away. And ask Hideaki why he hasn't even bothered to cast yet."

        "I look over to the two and yell what Shizune said to them."

        mi "Shicchan, I think he's upset that he's stuck with the backup rod~!"

        "Since Misha is largely unable to sign anything coherently right now, she only gets a puzzled look from Shizune for a reply. Shizune just sighs after I translate it for her."

        aki "Hey, even if you're depressed about it, you've got to try. You could catch the big one, for all you know. But you won't catch anything unless you do!"

        "I feel that at least half of her encouragement is because if Hideaki does catch 'the big one,' she wants to be there to eat it, and having six people fishing just leads to better chances of catching something than having five."

        "The constant awkward shuffling I have to do to communicate with Shizune, not to mention her increasing fidgeting, make me think it might be good to give her a go at fishing."

        hi "Hey guys, can we switch over now?"

        aki "Sure. Lilly?"

        li "No, no, please. I have no idea how to fish."

        "I sign what they say, given that I seem to have taken Misha's place as Shizune's interpreter right now."

        ssh "How magnanimous of you, Lilly."

        "Oh boy, here we go. I don't bother translating what she says for fear of sparking another fight."

        hi "Shizune says you should at least try. It might even turn out to be fun."

        li "Very well. Akira, how do you use this?"

        aki "It's pretty simple…"

        "I wonder how ethical it is to purposely completely change what Shizune said like that. At least it paid off."

        scene ev shizu_fishing_sl
        with shorttimeskip

        li "…I think I understand. What bait do you think would be the best to use? I'd prefer something that wouldn't hurt the fish too much."

        aki "If you're putting a hook through their mouth, I don't think the bait's going to hurt them much more."

        hi "And letting it go…? No, no, don't do that."

        li "But if it isn't big, there's little point in killing it…"

        "With my hands freed, it's much easier for me to interpret what everyone's saying. Now Shizune's the one that has to deal with her hands being full, but she seems to take it in her stride."

        ssh "That's so arrogant. Okay, I'll only reel in the big ones too, from now on."

        aki "What's she saying?"

        "Akira just sighs after I interpret for her."

        aki "No, I don't like that 'only.' You know, a fish is a fish, and you take what you can get."

        "Unfortunately, Shizune can't hear her and Lilly doesn't seem to be paying much attention now."

        "Lilly's taking to fishing easily; it is a very relaxed activity, after all. It isn't long before they both catch a fish, and surprisingly, Lilly is just as interested in which is the bigger of the two as Shizune is."

        stop music fadeout 3.0

        "As the hours pass, it seems like they're even starting to have fun."

        scene bg shizu_fishing_ss
        with shorttimeskip

        play ambient sfx_parkambience fadein 4.0
        play music music_tranquil fadein 3.0

        "At the end of the day, we have several good-sized fish between us. Even Hideaki and Misha managed to catch one. No one brings up that we were competing to see who could catch more. I don't think it matters to anyone any more."

        show akira basic_smile_ss at center
        with charaenter

        "Shizune and Misha are talking between themselves some distance away, and Lilly and Hideaki are doing the same. I decide to take advantage of the quiet moment to talk with Akira."

        hi "Lilly and Shizune got on well today. I didn't really expect it, after seeing how they act towards each other in school."

        show akira basic_boo_ss
        with charachange

        "She gives an amused snort. It looks like she doesn't take their feuding as seriously as I do."

        aki "They've got their reasons. Lilly and I are going away for a while tomorrow, so we thought we'd just pop by."

        show akira basic_ending_ss
        with charachange

        aki "In the end, I'm glad we did."

        "After a brief silence, she stretches loudly and then claps her hands to get everyone's attention."

        show akira basic_smile_ss
        with charachange

        aki "Well, that looks like enough to feed everyone. We should be getting back, now."

        show bg at bgright
        show akira at tworight
        with charamove

        show lilly basic_weaksmile_cas_ss at twoleft
        with charaenter

        "Lilly nods, but then hesitates. Even with her face clouding a bit, she still looks to be in a better mood than this morning. Akira really seems to know how to handle her, and defused her antipathy towards Shizune pretty well."

        show akira basic_ending_ss
        with charachange

        aki "Today's catch looks delicious, I kinda wish I had some soy sauce so I could just eat it now."

        show lilly basic_surprised_cas_ss
        with charachange

        li "I thought you wanted me to cook it…"

        show akira basic_laugh_ss
        with charachange

        aki "You don't think eating it raw would be okay?"

        "Despite Akira's protests, or joking as I can't tell which, we decide to wait to at least cook the fish before eating it."

        stop ambient fadeout 2.0

        scene bg shizu_houseext_lights
        with shorttimeskip

        stop music fadeout 3.0

        "It's already become pretty late while we were out, and by the time we arrive back at Shizune's house, it's a good time for dinner."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .use_mention_distinction:
        scene bg shizu_guesthisao
        with locationchange

        play music music_pearly fadein 5.0

        "Some of my pills spilled out all over the bottom of my bag, which I didn't realize until minutes before I was set to go to bed last night. I spent quite a bit of time scraping them out of my luggage."

        "By the time I get up, I'm already starting the day with a migraine from a combination of trouble falling asleep and waking up late."

        scene bg shizu_living
        show hideaki normal_up at center
        with locationchange

        "When I step into the living room, Hideaki is there finishing up his breakfast. His fork raised midway to his mouth, he seems unsure whether he should continue eating or greet me. Maybe I should back out of the room."

        show hideaki triangle
        with charachange

        hh "Good morning."

        hi "Morning."

        show hideaki thinking
        with charachange

        hh "What do you think we should have for breakfast?"

        hi "'We?' Aren't you eating breakfast right now?"

        show hideaki normal
        with charachange

        hh "Yes. Everyone else ate already."

        "Despite that, he repeats his question again. He's just trying to be nice. It's an odd way to show it, but I appreciate it nonetheless, and I am feeling pretty hungry."

        "I try to make some conversation with him while I'm getting my breakfast, to fill in the silence."

        hi "That fishing trip yesterday was fun. Do the Hakamichis and Satous often get together like that?"

        show hideaki bored
        with charachange

        hh "Not really."

        hi "I see."

        "I don't, really. There's a brief pause before Hideaki deigns to fill me in a little more."

        show hideaki thinking
        with charachange

        hh "Family issues. Our fathers are brothers-in-law, and do not like each other."

        "Hearing that gives me plenty to think about. It puts the way Shizune and Lilly deal with each other into context, and makes me even more wary of getting involved."

        hi "Ah. Family issues can be troublesome."

        show hideaki normal
        with charachange

        "Hideaki simply nods as I sit at the table with my breakfast. I wish he were a little easier to converse with."

        "While I'm eating, I notice that the house seems oddly quiet for a place with Misha in it. If Shizune and Misha ate breakfast already, it can't be because they're asleep. I ask Hideaki where they are."

        show hideaki bored
        with charachange

        hh "Shizune and Misha left to run some errands for our dad. The local businesspeople love dealing with Misha, so he insisted."

        hi "Well, she's got a nice and cheerful personality. I can see why they would. Maybe you should start taking lessons from her, you could increase your business connections."

        show hideaki confused
        with charachange

        hh "Are you serious?"

        "He sounds serious. I don't know what kind of business connections a little kid would need. Maybe he wants to have the best bake sale fundraiser ever."

        "It's a shame I'll eventually have to leave here and won't be around to see whatever he is planning."

        "I wonder what kind of person Shizune's dad is again, other than relatively outdoorsy. What I know so far is that he asks his business partners and friends of his daughter to do favors for him."

        "I'm assuming he's extremely shy or extremely lazy. Maybe it's a rude call to make so early, but it would certainly explain a large chunk of Shizune's personality."

        show hideaki triangle
        with charachange

        hh "Do you want to go anywhere?"

        hi "Not really. Why, do you?"

        show hideaki normal
        with charachange

        hh "I thought there might be somewhere you would want to go. You don't want to do some sightseeing, or eat at a specific restaurant?"

        hi "I don't know. I've never been here before."

        show hideaki thinking
        with charachange

        hh "I see."

        "I was just about to ask him about what Shizune was like when she was younger, but he's managed to sidetrack me with just one question. This appears to be as awkward a conversation for him as it is for me."

        hi "You're sure eager to please today. Why are you being so nice? Are you showing your secret nice side now that your sister isn't around?"

        show hideaki bored
        with charachange

        hh "You're sort of right. Shizune wanted me to keep you company today."

        "I don't want to trouble him, and try to make him see that, but Hideaki is as stubborn as his sister and feels as if this is his duty. He also seems to be earnestly trying to be nice."

        "Quickly, I start to realize that Hideaki's idea of fun is fishing, collecting cameras, and making esoteric puns. Fishing is fun, but it's something I would rather do than discuss. The same goes for cameras; I'd rather handle them than collect them."

        "This is something Hideaki picks up on himself."

        show hideaki normal_up
        with charachange

        hh "Are you bored?"

        hi "I'm not bored at all."

        "I almost yawn the words, so Hideaki ignores them entirely."

        show hideaki sad
        with charachange

        hh "You are bored. Shizune said to be entertaining, and I think I don't know how to do that."

        hi "I am entertained."

        show hideaki serious
        with charachange

        hh "You don't sound entertained."

        hi "I am!"

        show hideaki normal
        with charachange

        hh "Why do you yell? I hope you do not yell so much around Shizune."

        "It's hard to tell if he's joking. Either way, I'm a bit surprised. I try to play it off and change the subject."

        hi "Do you just collect cameras, or are you into photography, too?"

        show hideaki bored
        with charachange

        hh "Not really. If I did, there would be more photos in this house than there currently are. What is there to take pictures of?"

        hi "I don't know. Birds? Architecture? One of those restaurants you were talking about? I thought this city had tons of cool stuff. How can you live in a place with so much to do and do nothing?"

        show hideaki triangle
        with charachange

        hh "I thought you didn't know what there was to do here. Suddenly you have many ideas and are an authority on how interesting it is. You are like our board of tourism. Do you want to go watch birds or buildings?"

        hi "Okay, okay, no need to get so mad."

        show hideaki normal
        with charachange

        hh "…I'm not mad. I just think that if you feel that strongly about it, then we should go to an amusement park."

        hi "Why?"

        show hideaki confused
        with charachange

        hh "So that you can be amused. It will be fun."

        "Will he have this same flat, un-fun expression on his face while we're riding roller coasters and drop towers? It would sure bring the fun levels down. The thought does not convince me that it's worth the trip."

        hi "I don't know, it always sounded to me like going to an amusement park meant you spend more time waiting in lines than actually doing stuff. You'd have to go earlier than this just to skip the lines."

        show hideaki normal
        with charachange

        hh "Have you ever been to one?"

        hi "No, but it seems like that is what it's like."

        show hideaki bored
        with charachange

        hh "…Fine. What about a regular park? There is one nearby that Shizune likes going to. Maybe she will be there, and I can unload you onto her."

        hi "What do you mean 'unload?' I'm not luggage."

        show hideaki triangle
        with charachange

        hh "You don't want to go to an amusement park. I don't know what to do."

        "He looks as though I've hurt his feelings by refusing to go with him. I am already rationalizing my decision. I don't like waiting in lines. It would be too much like a date. I'd rather go with Shizune. It would be too tiring."

        hi "It's nothing personal, it's just that I kinda wanted Shizune to show me around town instead."

        stop music fadeout 2.0

        "And I don't think that with my condition going to an amusement park would be such a hot idea."

        scene bg shizu_park
        with locationskip

        play music music_soothing fadein 0.5

        "The park is close enough that their property could almost be considered an extension of it. Both it and Shizune's backyard look about the same, except that the park has benches and more people."

        "That said, it's quite nice. There are even people out walking their dogs, and children flying kites that can be seen lazily drifting back and forth over trees in the distance. I could sit here in a relaxing and scenic place like this forever."

        show hideaki bored at center
        with charaenter

        "Hideaki, on the other hand, looks like he's extremely bored. I want to poke him to see if he is still alive. But, would he react either way?"

        hi "Are you bored?"

        show hideaki normal
        with charachange

        hh "No. Are you going to jog or play frisbee with dogs like everyone else? Is that what people do in parks?"

        hi "Well, you go to parks to get back to nature and enjoy the atmosphere. That's why you jog in the park, instead of just on the sidewalk or something. You can jog anywhere."

        hi "I can't believe I am having this conversation. How can you not know this? You shouldn't have brought that up, it's too weird. Haven't you ever heard of 'children should be seen, not heard?'"

        show hideaki bored
        with charachange

        hh "Yes."

        show hideaki triangle
        with charachange

        hh "I lied. I'm bored. Would you like to play a game?"

        "I groan audibly enough to hope that he understands I don't want to. He doesn't care. In fact, he's already toying with a deck of playing cards."

        show hideaki serious
        with charachange

        hh "Why are you upset? That is why we are here."

        hi "I thought we were here to look for Shizune."

        show hideaki happy
        with charachange

        hh "Exactly. That is why we should play a game. It's a Shizune trap. You can trap anything, including people."

        show hideaki thinking
        with charachange

        hh "If we compete against each other in the spirit of competition and in a sportsmanly manner, she will be drawn here to challenge the winner, like a shark. Then I will defeat her like a safari hunter. Then take a photo of the award ceremony."

        "Sharks do not go around challenging people to games of chance like dojo breakers."

        hi "When did you bring that camera? Anyway, no. I get enough games hanging out with your sister."

        show hideaki normal
        with charachange

        hh "No, come on. It will be fun. We can play chess."

        hi "Please, no. Besides, playing chess in the park is something old people do, like fishing. You're going to get old too fast if you keep doing all this old man stuff."

        show hideaki darkside
        with charachange

        "Hideaki freezes like I've suddenly started speaking a foreign language. Maybe I've offended him again. Maybe he's secretly 50 years old and has just aged incredibly well. Him being Shizune's brother could be a cover story."

        show hideaki disapproves
        with charachange

        hh "What about checkers, or go? Or even backgammon is fine, even though I don't like it. If board games aren't your thing, we can play card games. Anything other than seven card, because it is for wimps."

        show hideaki evil
        with charachange

        hh "Are you afraid that you will lose? If you can beat me I'll give you candy."

        hi "Hideaki, you are just like Shizune. I'm starting to think this is all a pretense to play games."

        show hideaki thinking
        with charachange

        hh "No. That is not true."

        hi "You are! I bet that competitive streak is genetic. I'll sell you to science."

        show hideaki normal
        with charachange

        hh "No one can own a human being."

        hi "How about I teach you some sign language instead?"

        hi "When Shizune asked me if I wanted to come here, we talked a little, and it seemed like you and your dad don't use sign language. I'm just guessing, but if you don't, I could teach you some. I'm not a master at it, though."

        hi "I think it might be good for you to move your arms more, anyway."

        "He barely moves his arms. Most of the time they just hang limply at his sides. How unnerving."

        "It's been bothering me that Shizune's entire family apparently doesn't know how to sign. I wonder what she did before she met Misha. Did they just hire translators for her? Did she write out everything on that pad she carries around?"

        "The second is the most likely, or she could type it out on a phone. That would explain why she dislikes using the pad so much. Sad as it is, I can sort of see why Hideaki or her dad might not have bothered to learn sign language."

        "It probably was too much of a hassle at the time. It's very easy to think that. From what I've seen so far, though, neither of them hold it against each other or are too badly affected by it. It could be that I'm overthinking the situation."

        hi "Come on. Well, to be honest, I'm still learning sign language myself. I brought all my books along with me so I can keep up, you know? Still, I can at least teach you the alphabet. It's pretty simple. This is 'kite.'"

        "I feel really corny right now, and even more so when Hideaki stares back at me blankly as if the entire concept of learning is alien to him."

        show hideaki bored
        with charachange

        hh "Shizune liked flying kites here as well."

        "This is his attempt to salvage the conversation, and I'm happy to oblige."

        hi "Fishing, and now kites, too? Shizune really likes all these relaxing hobbies?"

        show hideaki thinking
        with charachange

        hh "Fighter kites. Actually, about Shizune—{w=0.5}{nw}"

        stop music fadeout 0.3

        show misha cross_grin_cas behind hideaki:
            center
            ypos 1.1 alpha 0.0
            linear 0.2 center alpha 1.0
        show hideaki ohshit
        with vpunch

        show misha at center

        "Hideaki freezes as Misha appears behind him and puts her hands over his eyes."

        play music music_comedy fadein 0.5

        mi "Hi hi~! Guess who~!"

        "He seemed to finally be loosening up, too."

        hi "Hi, Misha. Is Shizune with you?"

        mi "Hicchan, no spoilers! Don't spoil it, don't ruin the surprise, okay~?"

        show hideaki thinking
        with charachange

        hh "Misha."

        show bg at bgright
        show hideaki normal at tworight
        show misha perky_confused_cas at twoleft
        with charamovechangefaster

        mi "Bingo~! That's right! But~, it was too easy, somehow."

        "I don't know what she means by 'somehow.'"

        show misha hips_frown_cas
        with charachange

        mi "Too many people can tell it's me! I want to surprise someone! I thought for sure that Hideaki would be fooled~. Why weren't you, hm~?"

        show hideaki bored
        with charachange

        hh "You are the only person who does that. You, and kidnappers."

        show misha cross_laugh_cas
        with charachange

        mi "Really? Wahaha~!"

        show hideaki serious
        with charachange

        hh "Why do you laugh?"

        show shizu basic_angry_cas:
            center xpos 0.1 alpha 0.0
            ease 1.0 center alpha 1.0
        with None

        show shizu

        show bg at left
        show misha:
            twoleft
            xpos 0.4
        show hideaki:
            tworight
            xpos 0.8
        with charamovefaster

        show shizu at center

        ssh "Are you giving Hisao trouble? I thought you would take him somewhere more exciting than the park. It isn't even that far from home. You are so lazy."

        show misha hips_frown_cas
        with charachange

        mi "Hideaki, are you giving Hicchan trouble? You should have taken him somewhere more exciting! The park is too close to home, Shicchan says you're lazy~."

        show hideaki bored
        with charachange

        hh "He wanted to come here. Why are you so argumentative?"

        show shizu behind_frown_cas
        with charachange

        ssh "I have to keep my little brother in line."

        show hideaki triangle
        with charachange

        hh "What is she saying?"

        hi "You must be kept in line."

        show hideaki serious
        with charachange

        hh "Really…"

        "They're ready to go at each others' throats this quickly. On one hand, I've heard that siblings fighting so much isn't uncommon, and the fact that they fight at all proves there has to be some level of communication going on. So, it's nice they get along."

        scene bg shizu_houseext
        with locationskip

        stop music fadeout 4.0

        "They argue all the way back home. Misha translates for Shizune, and I for Hideaki. So it looks more like we're the ones arguing instead, except not really. Nobody could listen to Misha and believe that."

        "The day got entertaining in the end, at least."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .family_plot:
        scene bg shizu_guesthisao
        with openeye

        "Despite having only been here for two days, it feels like it's been much longer. I wake up feeling more tired than refreshed. Maybe because I've been moving around almost constantly since I got here."

        "Whatever the reason, it's making me get up unusually late each day. I like sleeping in, but it could be inconvenient if it ends up becoming a habit."

        "I can hear a deep, male voice shouting loudly in the background. It must be Shizune's dad. Or maybe, with the size of this place, it's creditors. More likely the former, since the yelling doesn't seem angry, just loud."

        scene bg shizu_living
        show hideaki normal:
            center
        show misha perky_smile_cas:
            center
            xpos 0.3
        show shizu basic_normal_cas:
            center
            xpos 0.08
        show jigoro smug:
            center
            xpos 0.87
        with charaenter

        play music music_another fadein 0.5

        "Shizune, Misha, and Hideaki are sitting in the living room, having a one-sided conversation with a giant bear-man who alternates between shoveling away food from a plate balanced on his leg and twirling a sword."

        "From what Shizune and Hideaki are like, I'd expected their dad to be a very reserved, clean-cut, possibly androgynous person, so I'm pretty surprised. I'm surprised for a while, until he starts talking to me."

        show jigoro laugh
        with charachange

        hx_ "Hello! You must be Shizune's other friend. Did you have a good night's rest? The guest rooms are a bit sparse, if there is anything you need, feel free to tell me."

        hi "Thanks. You must be Shizune's father. It's nice to meet you. I'm Shizune's classmate, Hisao Nakai."

        show jigoro neutral
        with charachange

        hx_ "The pleasure is mine. I've wanted to meet you, after hearing that I would have a second guest in my house. Unexpected. You hear something like that, and obviously you want to see what that person is like. Would you like my business card?"

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        show jigorocard:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0

        pause 1.0

        show jigorocard at truecenter

        "He holds up a case full of them for a second and I can see that his name is Jigoro and that his office hours are from eight to six. They also say that he's a 'consultant'. What a prepared guy, carrying his card case around in his own home."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        show jigorocard:
            easeout 1.0 ypos 0.7 alpha 0.0

        pause 1.0

        hide jigorocard

        show jigoro smug
        with charachange

        hx "We're just sitting down to a slightly late lunch, you're just in time to join us. Good. Pick a place to sit down and I'll bring you a plate. I hope you don't mind eating bear liver."

        "I thought that bear liver was toxic. Either way, the thought of eating a bear liver doesn't appeal to me other than for the ability to tell people I've eaten bear liver. I suppose it wouldn't hurt to try it. But Shizune's dad merely laughs."

        show jigoro laugh
        with charachange

        hx "I'm just making a joke. Although, maybe it wouldn't be such a bad idea to cook up some bear livers for you kids. They will make you strong."

        show jigoro neutral
        with charachange

        hx "We're actually having omelettes. I'll make you one right now. Is that unusual for you, having an omelette for lunch?"

        show hideaki triangle
        with charachange

        hh "Very unusual."

        hi "No, not at all."

        hide jigoro
        with charaexit

        "Jigoro vanishes to where the kitchen must be. I'm surprised that despite living in this place, he has to cook my lunch. Maybe he only cooks because he likes to."

        show jigoro smug:
            center
            xpos 0.87
        with shorttimeskip

        "My steaming plate of food is done in a very short time. It smells really good."

        hx "Are you in the Student Council, like Shizune? Is the Student Council that busy, that Shizune has to drag her friends along with her everywhere she goes?"

        show shizu behind_blank_cas:
            center
            xpos 0.12
        with charamovechangefastest

        ssh "Sometimes a vacation is just a vacation."

        hi "You're right about the student council part. I think we're just here for fun, though."

        show jigoro neutral
        with charachange

        hx "I see. Is that right? When I was young, our student councils had so much work that I don't think we could have afforded going on vacation. It must be nice, having so much free time. Should give you plenty of time to think about your future."

        "I do not like the direction this discussion is taking, and start thinking about how to avoid it."

        hx "Have you thought about that? About what you want to do?"

        hi "No, I haven't given it much thought recently. What do you do, if you don't mind me asking? It must be something pretty cool, if it can get you a house like this."

        show jigoro angry
        with charachange

        hx "Why do you want to know that? Children aren't interested in business. What business of yours is my business? Suspicious. Are you some kinda tax man, boy?"

        "I guess he really does not like being asked questions."

        show misha hips_grin_cas
        with charachange

        mi "Hicchan isn't a tax collector's boy, I think~. Hicchan, what do your parents do? You never told us~!"

        hx "You, be quiet. Don't interrupt me. I hate being interrupted. Rude."

        show misha perky_sad_cas
        with charachange

        mi "Aah~…"

        show shizu basic_normal2_cas:
            center
            xpos 0.08
        with charamovechangefastest

        "Shizune doesn't look too happy with this turn of events. Even with Misha unable to sign to her what's going on, she can read the mood easily. Her glare becomes more smoldering as Jigoro continues to rant."

        hx "One more thing. My fishing equipment. I came home and it was just in a big pile in the corner. Rods just stacked haphazardly on top of tackle."

        show hideaki thinking
        with charachange

        hh "That was me."

        "I can't remember if it actually was him. If it wasn't, I appreciate that he's willing to take one for the team. It doesn't matter because Jigoro ignores him without skipping a beat."

        show jigoro smug
        with charachange

        hx "Well, anyway, I'm glad that my fishing equipment could provide so much entertainment for my daughter's friends. Did not even tell me you were going to be using them. Those are expensive, custom-made poles. Not for dilettantes."

        "I suddenly become aware of the eggshell fragments in my omelette. Is he just a bad cook? Does he eat them for the calcium? Were they purposely added there to give me even more discomfort?"

        "Though confused, I'm not as unnerved as I think I would normally be. Then again, my life has been pretty strange lately, and I keep running into all sorts of different people. Nothing surprises me any more."

        show jigoro angry
        with charachange

        hx "Didn't even properly clean them after use. Terrible."

        hx "Do you even know how to fish? Unlikely. There are not enough poles here for all of you. How does that work? Did you all share? One person baits the hook, and another casts? Two people to reel? Incompetent."

        hi "Well, six of us went, so we couldn't all do it at the same time. First it was just me, Akira, Hideaki, and Misha."

        hx "Stop talking. That sounds unspeakably dirty. I have had enough of your filth. How vulgar. Make sure that your statements are not so embarrassingly, carelessly worded next time."

        hi "What…?"

        hx "'What?' You are so disrespectful. Amazing. Are all delinquent types like this? Even the way you dress shows flippant disregard for authority. Sweater vest. Disgraceful…"

        hi "Delinquent? I'm on the Student Council."

        "I'm hurt by his comment on my sweater vest, especially when it's coming from a guy in such a tacky shirt. I guess I can't really say anything, though. He has a sword. He might also kill bears."

        stop music fadeout 0.3
        play sound sfx_impact
        with vpunch

        "Misha loudly puts her plate down on the table."

        show misha hips_smile_cas
        with charachange

        mi "That was delicious~! Shicchan and I are done now. Hicchan, you are too, right~? We should get going!"

        "What a simple, yet effective exit strategy."

        scene bg shizu_houseext
        with locationchange

        "I barely have the time to put down my plate before they pull me up and out of there, and finally outside."

        show shizu behind_frustrated_cas at tworight
        show misha perky_confused_cas at twoleft
        with charaenter

        shi "…"

        show misha sign_confused_cas
        with charachange

        mi "Unbelievable~! It's like I'm really watching an interrogation~! This is not a cop show! Guests definitely have responsibilities, but hasn't he ever heard of being a gracious host~? Really~!"

        "Misha attempts to sloppily mimic Shizune's angry, chopping gestures as best as she can. She has the expression down too, but the tone of her voice is the same as ever, thus lacking the anger necessary to bring it all together."

        show misha hips_smile_cas
        with charachange

        mi "Wahaha~. Don't take it too hard, Hicchan~! Shicchan's dad does this to everyone, I think it's like a joke~."

        hi "That was the most aggressive joke possible."

        "I'm also not at all convinced that it was a joke, considering this hastily staged retreat, but this isn't a good moment to discuss how Shizune's father might be a jerk."

        play music music_shizune fadein 4.0

        show misha sign_smile_cas
        with charachange

        mi "Hicchan, let's go shopping!"

        show shizu adjust_happy_cas
        with charachange

        ssh "You haven't been to town yet, have you? It'll be fun. We can see the sights, and go to an amusement park, maybe eat at a good restaurant."

        hi "We just had lunch."

        "Even though I didn't eat much."

        show shizu behind_smile_cas
        with charachange

        ssh "It's okay, in that case, we just have to make sure that today is so busy that by the time we're done, it will be time for dinner."

        show misha cross_grin_cas
        with charachange

        mi "It works out perfectly~! Come on, Hicchan~!"

        show shizu behind_smile_cas_close at closeright
        show misha cross_smile_cas_close at closeleft
        with characlose

        "They immediately flank me and hook my arms with theirs, Shizune taking one arm and Misha taking the other. At first, we almost trip over each other. Shizune walks at a very brisk pace, and Misha has an unusually bouncy way of moving around."

        scene bg shizu_park
        with locationchange

        "We get the hang of it soon enough, and I notice we're going to town by cutting through the park. It doesn't seem efficient, so I'm guessing this is the scenic route."

        "Walking this way hinders how we can communicate with each other significantly. I can't talk to Shizune at all. Shizune and Misha are down to one handed gestures only. It feels nice, though, so I don't mind too much."

        "When I make a crack about it to Misha, she responds with mild confusion."

        show misha perky_confused_cas_close at closeleft
        with charaenter

        mi "Really, Hicchan~? Hm… If you really want Shicchan's attention, you can tell me, and then I can tap her on the shoulder for you."

        hi "You could just let me go and I'll do it myself. How are you going to tap her on the shoulder from over there?"

        show misha hips_grin_cas_close
        with charachange

        mi "Like this~!"

        with vpunch

        show shizu behind_frustrated_cas_close behind misha at closeright
        with charachange

        "She suddenly stops in her tracks roughly, and tries to reach behind her back and across my shoulders to get Shizune's attention. She succeeds, but only because when Misha stopped, I had to as well or we'd all fall over."

        show misha hips_laugh_cas_close
        with charachangealways

        show shizu adjust_blush_cas_close
        with charachangealways

        "Obviously, Shizune had to jerk to a halt too. The sight makes Misha let out one of her characteristic laughs, which shakes us around more, and Shizune starts flailing her free hand to get her to stop, which only causes her to laugh harder."

        "It is pretty funny to watch her getting so flustered, and I start laughing too."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .pangrammatic_window:
        scene bg shizu_guesthisao
        with locationchange

        play music music_dreamy fadein 2.0

        "I've been neglecting my sign language studies, so I should probably spend some time studying up on it. Although, I think I've learned a lot just by osmosis. I'm very proud of that, and will have to be careful not to brag about it."

        "Most of the books I brought with me aren't manuals on learning sign language, but studies about different signing 'dialects.' I know Shizune has some secret signals with Misha that only the two of them know the meaning of."

        "After seeing a couple of them, this book caught my eye in the school library."

        "Maybe I should incorporate some examples into my own signing, to mess with them, because I'm pretty sure that they have started using their code words more when I started learning sign language. That will teach them."

        "After a quick break for a shower, I resume practicing my signing in the guest room mirror. Yesterday, I crashed my fingers against each other pretty hard. It still smarts, and I don't want a repeat of that to happen again."

        play sound sfx_doorknock2

        show hideaki normal at center
        with charaenter

        "I hear knocking on the door behind me and turn to find Hideaki standing inside the doorway, staring at me. How polite of him to knock, but usually you don't open the door first."

        show hideaki triangle
        with charachange

        hh "What are you doing?"

        hi "I'm practicing sign language. How long have you been standing there?"

        show hideaki thinking
        with charachange

        hh "I did not see anything."

        "That isn't the point. I don't even know what he means by that. It's not like I was doing something that I would be ashamed to have people see me doing."

        "Although, sign language must look strange to most people. I'm only used to it from being around Shizune and Misha so much."

        hi "I'm brushing up on my sign language, and reading about it too. Stuff like the history of it, even though they cover it in sign language class."

        show hideaki normal
        with charachange

        hh "Your school teaches sign language as a class?"

        hi "Yeah. One of the first things they brought up was that it's not very common to do that. I guess we're very international, or something."

        show hideaki serious
        with charachange

        hh "It looks fun."

        hi "Well, I wouldn't call it fun."

        show hideaki bored
        with charachange

        hh "If you do not enjoy this, it seems like a lot of work to go through just to talk to my sister."

        hi "Why does everyone keep saying that?"

        show hideaki happy
        with charachange

        "Hideaki's mouth twitches like he was about to laugh, but he restrains himself. Come to think of it, he hasn't laughed once since I've met him. I could take it as a compliment that he doesn't laugh at me, but I'm curious to see it."

        hi "Laugh."

        show hideaki thinking
        with charachange

        stop music fadeout 4.0

        hh "…"

        show hideaki bored
        with charachange

        hh "Why?"

        "It was the fastest and most direct way I could think of towards accomplishing my goal."

        show hideaki normal_up
        with charachange

        hh "Can you teach me sign language?"

        "He says it plainly, but his body language is nervous, showing that he clearly needs to put some effort in to ask. I guess Hideaki likes his sister after all. I'd think Misha is a lot more approachable though, so I wonder why he didn't ask her."

        "Secretly, I'm shouting 'yes!' inside. I had thought he wanted to learn sign language and even brought it up, but he had evaded the subject skillfully. It turns out I was right after all. I don't really know why this makes me so pleased."

        hi "Sure."

        "But now that I think about it, I'm not a sign language teacher. I don't even know where to start. In class, I'd be learning stuff gradually over a week. Does Hideaki expect me to teach him anything usable in a one-day crash course?"

        show hideaki normal
        with shorttimeskip

        play music music_normal fadein 3.0

        "My teacher spent a couple days just giving a history of sign language. I decide to start off with that, to buy some time while I figure out how I can segue it into the hard stuff. Five minutes in, Hideaki raises his hand."

        show hideaki serious_up
        with charachange

        hh "I don't understand what you are doing."

        hi "Uh… well, you can't just jump into teaching, you know. You have to ease into it. It's like when you go swimming, you don't just jump in the lake like in some movie."

        show hideaki triangle
        with charachange

        hh "I do not swim."

        "It's like scientists managed to create a process to suck out all the hyperactive, infuriating, and childish qualities of a small child and then implant them into the dad, creating a raging jerk dad, and leaving behind Hideaki."

        "I begin to feel claustrophobic, despite the fact that the guest room is three times bigger than my dorm room and there's just the two of us in here. It's all in my head, I know it, and I don't care. I still use it as an excuse to move the lesson outside."

        scene bg shizu_garden
        with locationskip

        "It's a lot easier to concentrate out here. Even the precious few seconds it took to relocate managed to allow me to sort my thoughts. There were no questions during this time. Hideaki can't seem to talk and walk at the same time."

        "Eventually, however, I start to realize that if I'm going to teach him anything I have to keep the lesson constantly moving. The second there's an opening for it, he'll ask a question, which will lead to more questions. Then there's no end to it."

        "The second time he asks me why a certain hand motion means what it does, and I have to reach deep into my memory to look for etymology I don't know about a gesture I only knew about a month longer than him, I start looking for an out."

        hi "Hideaki, let's take a break."

        show hideaki bored
        with charachange

        hh "Okay."

        show hideaki serious
        with charachange

        hh "What is your school like?"

        "This kid is like a little reporter, but it makes sense for someone his age to be curious, and this is one question I don't mind."

        hi "What's it like? I never really thought about it. It's on top of this mountain, so it feels kind of isolated and lonely up there sometimes, even though that's also why it has a pretty great view."

        hi "The students there are interesting. Actually, I felt bad at first. You know what kind of school it is, right?"

        show hideaki normal
        with charachange

        hh "Yes."

        hi "I felt bad because I didn't want to go there. I don't even remember exactly what I was thinking at the time. Probably it was something like, a school for crippled people would be a depressing place. They were telling me to go be forgotten there."

        hi "Then, everyone there was just living their lives, for the most part. So I felt even worse. It wasn't different at all, so I felt like kind of a jerk."

        hi "Shizune was the first person I met. She's in most of my classes. Misha, too, they're always together. I guess the school is accommodating enough to pair them up as much as possible. There's this girl in my class, Hanako, whom I feel bad for."

        hi "She has these burns, and seems to have a complex about them. But I think she looks fine. She's a cute girl. And friends with Lilly, too. You know Lilly, right? Does she bring up Hanako?"

        show hideaki thinking
        with charachange

        hh "Yes, sometimes."

        hi "I'm trying to remember who else is interesting. We have a little track star ace who runs on these prosthetics."

        hi "There's this one girl, Rin, who doesn't have arms, but she's a great painter. All her art has this harsh, alive quality. Have you ever been to Yamaku? You've probably seen some of it hanging around."

        hi "A little weird, sometimes, but I've always heard that artistic and creative types are like that. That reminds me, the guy who lives across the hall from me is pretty weird, too. But he can be interesting, at least."

        show hideaki normal
        with charachange

        hh "You are also interesting."

        hi "Is that bad? And what's with that tone? What does that even mean? Are you saying I'm weird, Hideaki?"

        show hideaki triangle
        with charachange

        hh "You talk a lot."

        "My first instinct is to go on the defensive, but the more I think about it, he has a point."

        hi "That's right, I do talk a lot. I don't think I used to."

        hi "I think… It's probably because of all the time I spend around Shizune and Misha. Talking with them, I get caught up in all their circular logic and just how they do everything. I feel like I'm going to be drowned out, or left behind."

        show hideaki confused
        with charachange

        hh "My sister can drown you out?"

        hi "It's not like she's literally talking over me and stuff, obviously. It's hard to explain. They have more energy than I do. It's like, an aggressiveness. I don't feel like I have to match it, but I want to. I think maybe your sister has that effect on people."

        show hideaki thinking
        with charachange

        hh "…"

        hi "Do you look up to your sister?"

        show hideaki normal_up
        with charachange

        "He stares at me blankly, tense and confused as to how to react to the question."

        show hideaki angry_up
        with charachange

        stop music fadeout 5.0

        hh "I will be better than Shizune."

        hi "Better at what?"

        show hideaki angry
        with charachange

        hh "At… everything."

        hi "Like what?"

        show hideaki triangle
        with charachange

        hh "I can do magic tricks."

        hi "You mean like telling people you've got their nose, or more like the kind of magic where you pull a rabbit out of your ass?"

        "He doesn't look happy. Someday, I will see Hideaki laugh. I might just try tickling him, if I have to."

        play sound sfx_doorslam

        show hideaki surprise
        with vpunch

        show hideaki thinking at twoleft
        show bg at bgleft
        with charamovechangefaster

        show jigoro neutral at tworight
        with charaenter

        "The back door flies open and Jigoro strides out of it, keeping his back straight and taking giant, slow, regal strides, like either a king or a huge jackass."

        "I try to turn away, using the train of logic that if I can't see him, he can't see me. Unfortunately, it doesn't pan out and he comes over so fast it's like he appeared out of the air over my shoulder."

        show jigoro laugh
        with charachange

        play music music_happiness fadein 2.0

        hx "Oho. What's up here? What are you two doing, flailing your hands around? Playing cat's cradle like a bunch of girls?"

        hi "I'm teaching Hideaki some sign language. What about you, Mr. Hakamichi?"

        show jigoro angry
        with charachange

        "He narrows his eyes suspiciously, as if he's not used to people being polite to him."

        hx "I am writing an autobiography of my life and times. And by 'writing' I mean I am dictating it to my biographer. Unfortunately, she is running late. Unprofessional."

        show jigoro smug
        with charachange

        hx "Perhaps you should read it when it is published later this year. I can put you on the waiting list. Maybe it will give you the moral compass you seem to lack in your life, and inspire you to stop sucking."

        "It can't be sustainable for him to be so casually insulting to everyone. Though, Hideaki is likely too detached to even notice, Shizune is deaf, and most of the insults must fly over Misha's head. But surely Akira must have an opinion on this."

        "I try not to think about it. If he is doing this to psyche me out, then I have to stay calm or he wins. He must absolutely, definitely not win. This must be how Shizune feels."

        hi "How old are you?"

        show jigoro neutral
        with charachange

        hx "Forty-six."

        hi "That doesn't seem old enough to justify writing a biography. I mean, that's not even old. Don't most people start writing their memoirs a lot later than that?"

        show jigoro angry
        with charachange

        hx "Shut up, boy. I am going to give you advice: do not talk about matters of age with people older than you. You are less than half my age, you have no right to talk about old. I have an ulcer older than you."

        "He should get that checked out. He might have a point though, he is definitely older than I am."

        show jigoro laugh
        with charachange

        hx "…Either way, even if we were the same age, I wouldn't have to explain myself to you, sweater vest."

        hi "Eugh."

        show jigoro angry
        with charachange

        hx "Why do you make that noise? Are you mad? Well, obviously. Good. Your sweater is terrible, and I want you to feel bad about it. The burn tells me it's working."

        hi "I like my sweater."

        show jigoro smug
        with charachange

        hx "I'm sure you like huffing glue, too. That doesn't make it right."

        hi "I don't huff glue. Where did you get the impression I do?"

        show hideaki normal
        with charachange

        hh "That is slander."

        "I wonder how Hideaki knows what slander is. Maybe Jigoro is a lawyer. I can sort of see that, although I thought only TV lawyers were this antagonistic. I don't know if I should take the chance and ask if that's his job."

        hi "He's right. It is slander. Are you a lawyer?"

        show jigoro neutral
        with charachange

        hx "I was guessing, a guess based on the fact that you are stupid. It's like how you are assuming I am a lawyer, except you have no reason to think that. If you want to know what I do so badly, why don't you preorder my autobiography?"

        show jigoro angry
        with charachange

        hx "Now you are insulting my book, and, by extension, my entire life. What gives you the right to do that? Arrogant. I'm trying to think of how I could make you understand my struggle. Maybe by beating you. With my autobiography."

        hx "I hope you walk away from the beating having learned a valuable lesson, like not making assumptions."

        show hideaki bored
        with charachange

        hh "Assault…"

        "But he made an assumption too, that I huffed glue. I consider calling him out on this glaring example of hypocrisy, but I don't think it's worth it. He would probably explain his way out of it by saying 'Shut up, boy.'"

        show jigoro smug
        with charachange

        hx "Back in my day, children were seen and not heard, and to be an adult meant having experienced many hardships. With even a glance, people could instantly judge a man's character. Childhood existed only to temper you for adulthood."

        hx "When you look at me, can you not see the catalogue of my experiences even at a glance?"

        hi "Uh… maybe. Were you a swordfighter?"

        "He could also be Hawaiian, and a werewolf."

        hi "Wait, didn't you tell me before not to make assumptions? Now, you just asked me to assume stuff. And you're saying everyone when you were my age did it. And that had to be in, like, the '80s. That wasn't even that long ago!"

        "I'm ready to give him a piece of my mind, for talking like he had to walk fifteen miles in the snow to ride a coal train, that he had to shovel coal into himself, before climbing up a mountain while fighting ogres to get to school."

        "But, now that I finally want a fight, Jigoro is happy to have a good thing going just continuing to ramble about how difficult it was growing up one generation ago, twirling his sword like a baton and stopping occasionally to yawn or check the time."

        "The tardiness of his autobiographer is still foremost in his mind. That means the whole time he's been insulting me, he must have been doing it just to pass the time. To add insult to insult, his watch is also really nice."

        show jigoro angry
        with charachange

        hx "…When I was your age, kids had responsibilities. Not like today. Sickening. No one thinks about the consequences of their actions any more. They just do whatever they want, thinking no one will hold them accountable since they are young."

        "It's odd, that description could fit Shizune and Misha. I thought something similar only yesterday. But it only fits them slightly."

        hx "Look at yourself. An amoral, directionless, delinquent glue-huffer, with a complete lack of etiquette and absolutely no fashion sense. You are tomorrow's Japan. Disgraceful. Is this the future of this once-great country?"

        hi "I know someone you would get along well with."

        hx "Don't interrupt! Who? One of your friends? Why would I want to talk to some awful teenager? Have you even been listening? Why are you so rude, boy? Your attitude is not one that will make you a lot of friends."

        hi "I wish you would stop giving me so much advice."

        "Or at least, I wish he would give me advice that he would have the decency to adhere to himself."

        show jigoro neutral
        with charachange

        hx "Where have you been?"

        hi "Huh?"

        show jigoro angry
        with charachange

        stop music fadeout 3.0

        hx "Not you, idiot."

        show jigoro:
            tworight
            xpos 0.85
        show hideaki normal:
            twoleft
            xpos 0.45
        show bg at center
        with charamovechangefaster

        show shizu behind_blank_cas behind hideaki:
            twoleft
            xpos 0.2
        with charaenter

        shi "…"

        hi "Oops. I didn't notice you there."

        show shizu adjust_happy_cas
        with charachange

        "Shizune smiles and gives a short wave. Her arrival made Jigoro stop talking, so I'm already happy to see her for that reason alone."

        show shizu basic_normal2_cas
        with charachange

        ssh "Misha and I decided to go into town again. Hisao, I noticed you were looking at some clothes yesterday in a store window, and I thought I would go back and buy some of them for you. It was supposed to be a surprise, though."

        "She looks annoyed that the surprise is ruined, even though she ruined it herself."

        show shizu behind_blank_cas
        with charachange

        ssh "Here you go!"

        hi "Thanks."

        show shizu basic_normal_cas
        with charachange

        ssh "Misha wanted to cut her hair. I told her not to, but she said it was too hot for the summer."

        hi "Yeah? I don't know, that makes a lot of sense to me. It must be like an oven under there. I want to see it. Where is Misha, anyway?"

        mi "Over here~! Hi, Hicchan~! Hi, Mr. Shicchan's-father~! Hi, Hideaki~!"

        show jigoro smug
        with charachange

        hx "…"

        play music music_running

        show mishashort hips_grin_cas at offscreenleft
        with None

        show shizu:
            xpos 0.3
        show jigoro:
            xpos 0.95
        show hideaki:
            xpos 0.55
        show mishashort:
            center
            xpos 0.1
        show bg:
            xpos 0.55
        with charamovefaster

        "Misha runs around us once in a wide circle before stopping next to Shizune."

        "For the first time, she hasn't put her hands over my eyes, although now I see she has bags of her own to carry, so it's not like she could have even if she wanted to. Although I am positive she's tried before."

        "Her meticulously styled curls are gone now, in favor of a much shorter, sportier look. Misha looks even happier than usual, probably because she knows she won't have to wake up at the crack of dawn every morning just to do her hair."

        show jigoro angry
        with charachange

        hx "What is that haircut? You look like an intern. Your old haircut merely made you look like you were wearing a pink judge wig. Judge to intern is a huge demotion."

        show shizu behind_frown_cas
        with charachange

        ssh "Hisao, is he saying something insulting? Tell him not to insult my friends!"

        hi "Don't insult my friends."

        hx "Which one of you is talking?"

        hi "Both of us. I agree with her."

        show mishashort hips_smile_cas
        with charachange

        mi "Hehehe~! What do you think, Hicchan?"

        show shizu adjust_frown_cas
        with charachange

        ssh "You should have kept it like it was."

        show mishashort perky_sad_cas
        with charachange

        mi "Aw~… Hicchan, you look disappointed, you don't like it either?"

        hi "Well, yeah, I'll admit I kind of liked your old haircut more, but I think this one is nice too. It suits you."

        show mishashort hips_grin_cas
        with charachange

        mi "Aw, thanks, Hicchan~!"

        hx "Touching. If you like it so much, maybe you two should trade."

        hi "You can't trade a haircut."

        hx "What a shame. Even her old haircut would suit you so much more than your current, slacker haircut. Awful. As for you…"

        show jigoro laugh
        with charachange

        hx "Hmmm… Actually, this is much less garish than your other haircut. I like it."

        show mishashort cross_laugh_cas
        with charachange

        mi "Ahahahaha~! Really? Thanks, Mr. Shizune's-dad~!"

        show jigoro angry
        with charachange

        hx "It's Mr. Hakamichi. Talk like a normal person."

        show mishashort perky_smile_cas
        with charachange

        mi "Hm~? I don't understand~! Okay, okay okay~! I'll call you Mr. Hakamichi!"

        hx "Agh, it's like speaking to a slide whistle. Contemptible. Where's my biographer? Hideaki!"

        show jigoro:
            alpha 0.0
        show shizu basic_normal_cas
        show hideaki bored
        with charaexit

        "He starts quietly muttering to himself and walks off. I guess a wannabe-cranky old man like Jigoro would at the very least be hesitant to yell at girls. Suddenly, he doubles back, unable to resist his urge to have the last word."

        show jigoro:
            alpha 1.0
        with charaenter

        hx "And another thing, you do not have to be so loud. I do not like being shouted at."

        show mishashort hips_grin_cas
        with charachange

        mi "What? Shouting~? I'm not shouting~!"

        "I can't think of anyone more unqualified to talk about what's garish or to chastise someone else on shouting at people. It's like a parade of hypocrisies and the hits just keep coming."

        "An unusual reaction seems to be taking place. Misha apparently finds Jigoro funny and laughs pretty much every time he says something, which only makes him berate her harder. I guess this is what they call a vicious circle."

        "Misha's voice is punctuated with explosions of laughter and seems to come from everywhere. On the other hand Jigoro's is booming and directed like a cannon. In any case, they are both unbelievably loud."

        "The more they talk to each other, the more they seem to play off each other's volume and get louder."

        show mishashort perky_sad_cas
        with charachange

        mi "Ow~! My ears hurt~!"

        hx "WHY ARE YOU SHOUTING?"

        show black
        with hands_in

        "Shizune's hands wrap around my eyes from behind, something I'm so used to Misha doing that for the first time I find myself confused by it, since Misha is in front of me."

        show shizu adjust_happy_cas
        show hideaki bored
        with None

        hide black
        with hands_out

        "She lets go and holds a finger up to her lips."

        show shizu behind_smile_cas
        with charachange

        ssh "What a perfect distraction! Now's our opportunity. Let's sneak off."

        his "Why do we have to sneak off? Why not just walk off?"

        show shizu adjust_smug_cas
        with charachange

        ssh "It wouldn't be as fun."

        show shizu basic_happy_cas
        with charachange

        ssh "It's decided: it's a secret mission. Escape without being detected. Extract Hideaki for bonus points."

        hide shizu
        with charaexit

        stop music fadeout 3.0

        "Already, she has simplified the situation into a game. Shizune quietly slides away from the scene and begins edging towards the house. I walk towards it, normally."

        if _in_replay:
            return

    label .closer:
        scene bg shizu_living
        with locationskip

        "I can't find Shizune at first, but eventually she walks into the main part of the house, sipping a glass of ice water and dangling her glasses back and forth from her free hand. She whips them on as soon as she sees me."

        show shizu basic_normal2_cas at center
        with charaenter

        play music music_ease fadein 4.0

        ssh "You didn't rescue Hideaki. That means you don't get the bonus points. If you were also being graded on style, I'd have to deduct points for a booooooring escape."

        his "It looked like you wanted to talk to me, I didn't know I had to be stylish about it. You know, some say that the most stylish people are the ones that don't try too hard to look cool."

        show shizu cross_wut_cas
        with charachange

        ssh "You're really cool."

        "I wonder how is it that I can pick up on her sarcasm so easily, and how hard it might have been for her to learn the concept of sarcasm without being able to hear. I can't imagine it."

        his "You seem like you're in a good mood."

        "Although I guess it isn't really a good mood. It's more that she seems very excited."

        show shizu behind_frown_cas
        with charachange

        ssh "I'm in a bad mood."

        show shizu basic_normal2_cas:
            center
            ypos 1.1
        with charamovechangefaster

        "Setting her drink down, Shizune sits down on the couch."

        show shizu behind_frown_cas
        with charachange

        ssh "I liked her regular hairstyle so much more. It looked so pretty. It was refined and meticulous. Now she looks too sporty and tomboyish."

        his "I wouldn't call Misha refined and meticulous. That sounds more like you. You should give it a chance. Grow your hair out and make it look like drills."

        his "Hm… actually, maybe this suits you just fine."

        show shizu adjust_frown_cas
        with charachange

        "Shizune rubs the frame of her glasses roughly, looking annoyed at the implications behind what I just signed to her. That's fine, because I was totally implying that. She moves a little closer to me when I take a seat."

        show shizu basic_angry_cas
        with charachange

        ssh "I'm a tomboy?"

        his "Well, no one would call you a tomboy. …Based on appearances."

        "Shizune glares at me, unamused. I have to fight to keep a straight face."

        his "Maybe you two should trade haircuts anyway."

        shi "…"

        show shizu behind_frown_cas
        with charachange

        ssh "You sound like my father."

        show shizu adjust_smug_cas at center
        with Dissolvemove(0.2)

        "It's true. Shizune giggles noiselessly when she sees my displeasure at the realization. Jumping to her feet, she twirls an invisible sword in her left hand while standing up militarily straight and grimacing. A terrifyingly accurate impression."

        show shizu basic_frown_cas
        with charachange

        ssh "Anyway, I don't take advice from anyone who wears a blue sweater with brown pants. Where's your sense of color coordination? Dreadful."

        show shizu adjust_smug_cas
        with charachange

        ssh "…But changing my haircut, that might be fun. Wouldn't it be? I want to see how everyone would react."

        his "You must really like playing with people. Sometimes, I think, a little too much."

        show shizu adjust_frown_cas
        with charachange

        "No answer. The way she fiddles with her glasses, brow furrowed, tells me that it's because she can't."

        show shizu behind_blank_cas
        with charachange

        ssh "It's fun."

        "Then, with more confidence and while pulling herself closer to me:"

        show shizu basic_happy_cas
        with charachange

        ssh "It's fun to drag more and more people into my life."

        his "Oh, I see."

        "I wonder if I'm included in that number. I want to ask, but am not even sure how I would."

        show shizu adjust_happy_cas
        with charachange

        "Shizune wags a finger preemptively, indicating that she won't be answering such a question anyway."

        stop music fadeout 0.5

        show shizu adjust_blush_cas_close
        with vpunch

        "She reaches for her glass, but doesn't seem to realize how far she's managed to inch away from it all this time. To prevent herself from tipping over clumsily, Shizune tries to grab on to me, and ends up pulling me on top of her."

        scene ev shizu_couch
        with vpunch

        play music music_serene fadein 9.0

        "As I lean over her, I can feel the heat coming off her body and realize how close we are. I can hear her soft breathing and the slight rustling of her clothes as she momentarily fidgets about."

        "A blush starts to creep into her cheeks, but her eyes stare straight into mine, dark and unblinking."

        "It's the same look from the first time I saw her, piercing and devoid of any clear emotions. Just waiting to see what will happen next, like the eyes of a cat. It makes me feel uncomfortable, being looked at in such a way."

        "This is the first time I've been so close to her for an extended period of time, and the mood is different now. The situation now isn't the same as a passing touching of hands or her and Misha's usual games."

        "Shizune's fingers weave together tentatively, but she makes no move to sign. The look in her eyes isn't just nothing, like I'd thought. It's more like expectation. I wonder if maybe I've been following the string of her expectations this entire time."

        scene bg shizu_living
        with vpunch

        show shizu behind_blank_cas_close at center
        with charaenter

        "I feel her grabbing me by the shoulders and then gently, but firmly, pushing me off of her. I roll sideways onto the soft couch and pull myself into a sitting position less than a foot from her. The way I feel, she might as well have thrown me ten yards."

        "When I think about it, this is perhaps one of the biggest drawbacks to sign language. Shizune said that the fact that you have to sign your words out with your hands means you have time to reflect on what you say before you say it."

        "But on the other hand, it also means that what would normally just be an awkward silence becomes an insurmountable wall. I'd just blurt out something, anything, to try and dispel the tension I'm feeling right now if I could, but I can't."

        "Ordinarily, I think that what would be normal would be to apologize, and maybe leave. But right now, I wonder if that is even applicable. I can't get past how guilty such an action would seem. Like I were just slinking away."

        "Of course, it's not like I can just play it off like nothing happened, either. That would just be insulting to both of us. So, as much as I don't want to, I apologize quickly, so quickly I forget to sign it. Then I go back to my room."

        scene bg shizu_guesthisao_ss
        with locationskip

        play sound sfx_pillow
        with vpunch

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        show black
        with shuteye

        "Sighing, I let myself fall backwards into bed. I wish I could just go to sleep right now, but I feel wide awake."

        play sound sfx_doorclose
        $ renpy.music.set_volume(1.0, 3.0, channel="music")

        pause 3.0

        show shizu basic_normal2_cas_close
        hide black
        with openeye

        "I sit up when I hear the door closing and open my eyes to see Shizune sitting in the chair in front of me."

        show shizu behind_blank_cas_close
        with charachange

        shi "…"

        "She asks a question that goes right over my head, due to my surprise. It's not a feeling I'm good at concealing, and I don't think it's what she intended. Whatever she was saying, she backs off, and doesn't attempt to sign again for a while."

        show shizu adjust_happy_cas_close
        with charachange

        ssh "This is the first time I've been in your room."

        "Shizune tents her fingers and puts on an exaggerated attempt to make herself look embarrassed and modest at the thought. I can't appreciate the joke, just the fact that she's here has me feeling a bit scattered."

        his "Very funny. It isn't even my room. It's your guest room."

        if not side_lilly and wait_for_shizu or _in_replay:
            his "Besides, you and Misha barged into my room once before."

            show shizu behind_blank_cas_close
            with charachange

            "It seems as if she expects me to say more. I remember feeling very panicked when they burst into my room, afraid of what conclusions they would jump to seeing the wall of pills lining the place. I don't think that Shizune remembers, though."

            show shizu basic_normal_cas_close
            with charachange

            ssh "It made you nervous."
        else:
            ssh "You still looked startled when I came in."

        "The way she says it so factually stings me."

        his "A lot of things make me nervous."

        his "You're one of them."

        show shizu behind_blank_cas_close
        with charachange

        shi "…?"

        his "Because you're overeager to always get people involved in… whatever you're doing. Whether it's joining the Student Council, or even taking a break. Whether they want to or not."

        show shizu basic_angry_cas_close
        with charachange

        shi "…"

        show shizu adjust_happy_cas_close
        with charachange

        shi "… … … …"

        show shizu basic_normal2_cas_close
        with charachange

        shi "… …"

        "She signs almost at a crawl, her hands pausing mid-sentence far too much, causing the words to dissipate formlessly before I can even begin to try to understand them. I try not to let on that this is the case."

        "It seems to work, but she looks a little sad, and I regret that I have nothing to say to snap her from the strangely wistful and distant expression she is wearing. All I can do is wait for her to come out of it."

        show shizu behind_sad_cas_close
        with charachange

        ssh "You are right. I want to drag everyone into my life. But, lately, I'm no longer sure if it's the right thing to do."

        his "I enjoyed you taking me to your favorite restaurant the other night."

        show shizu basic_normal_cas_close
        with charachange

        ssh "It's not like that was my favorite restaurant… I have others I like. I might even be able to rank them by number."

        his "Really…"

        show shizu adjust_frown_cas_close
        with charachange

        ssh "This chair is so hard. I want to sit on the bed."

        "Motioning to her to go ahead, I wait for her to get off the chair and take her place when she does. Though I didn't intend for it to be, she finds it amusing."

        show shizu behind_smile_cas_close
        with charachange

        stop music fadeout 5.0

        ssh "Close your eyes."

        his "Why?"

        show shizu adjust_smug_cas_close
        with charachange

        ssh "It's a surprise."

        show black
        with shuteye

        "I decide to humor her and close them. I can feel her leaning over me, and suddenly, something soft and moist touches my lips. My body tenses up in surprise. Fortunately, not as awkward a reaction as I could have made."

        "It was just a quick peck, and I almost think that's the end of it, but then she kisses me again, more deeply this time. Her hands slide onto my shoulders, up to my neck, and then back down again. Then across my shoulders and down my arms."

        "I can feel the weight of her body on my legs, and the eroticism of the situation isn't lost on me. At this point, I'm ready to try and open my eyes just a crack, but as if expecting it, she puts her fingers on my eyelids."

        play sound sfx_rustling

        "Seconds later, something ties my hands together at the wrists, and I panic, not knowing what to make of this. My first thought is to ask Shizune what she's thinking. Even though she can't hear me, I'm sure she gets the gist of it."

        "She won't let go of my hands, tracing her fingers over them, from the lines of my palms, over my knuckles, and to my wrists."

        scene evh shizune_hcg_tied_stare:
            yalign 0.0 xalign 1.0
            easein 6.0 xalign 0.7 zoom 0.5 yalign 0.345
            truecenter
            zoom 1.0
            "evh shizune_hcg_tied_stare_small"
        with whiteout

        play music music_heart fadein 5.0

        hi "Hey, what are you doing? What's this?"

        "Or course, with my hands tied behind my back, I might as well be gagged. A part of me can't help but think that this is what she intended."

        scene evh shizune_hcg_tied_smile_small
        with charachangeev

        "As if reading my thoughts, a mischievous expression lights up her face, but her blushing doesn't fade. In fact, it only deepens when our eyes meet."

        "Embarrassed, she leans deeper into our partial embrace, hiding her face by burying it in my shoulder and neck. Her hair is soft and tickles me, and I let out a laugh knowing that she won't hear me; won't be offended."

        scene evh shizune_hcg_tied_blush_small
        with charachangeev

        "Shizune's hands move downwards to the fly of my pants, covered by her skirt. Her hands disappear from view, only to jerk back on touching my erection. Shizune almost falls off me from nervousness. It's like she didn't expect it to be there."

        "The sudden display of naivety is the starkest contrast yet to how forward she has been so far, and I find it amusing. Suddenly, she seems very immature again. A high-school girl playing the role of a more aggressive woman."

        scene evh shizune_hcg_tied_blush:
            yalign 0.0 xalign 0.8
        show evh_hi shizune_hcg_tied_hisao2:
            yalign 0.0 xalign 0.8
        with flash

        "She pokes at my penis curiously with her index finger, her face reddening as she runs the rest of her fingers down its underside. Her movements are soft and curious, and they belie the embarrassed look on her face."

        scene evh shizune_hcg_tied_stare
        with charachangeev

        "It's likely Shizune is as nervous as I am, so I'm a bit relieved when she stops her exploratory prodding, but then I think about what's next to come."

        "She might try and unbutton my shirt. Who knows what she would say, seeing the scar on my chest. I'm still self-conscious about it, and I can imagine the concern on her face on seeing it; the tenting of her fingers in thought."

        "Luckily, in this position, she couldn't take off my sweater without ripping it off me. The fear fades from my mind. Now, I'm only experiencing a strange, uncomfortable mix of anticipation and nervousness."

        scene evh shizune_hcg_tied_blush
        with charachangeev

        "A newfound lightness on my knees brings me back to reality, and I can see Shizune standing on the tips of her toes to slide her underwear down her thighs. When she sees me looking at her, she tries to cover my eyes with one hand."

        "I wonder exactly when it was that I started being attracted to her. Not just attracted to her physically, but drawn to her. And, I wonder why. She's pretty, but then, also very combative. Not just that, but she seems to like being that way."

        scene evh shizune_hcg_tied_blush_small
        with charachangeev

        "The way she's acting now, however, and at other times, doesn't really fit that image. I'm starting to think that maybe her tying my hands might have been for more reasons than just the most obvious."

        "Still, that aggressiveness that she flashes around as comfortably as a business card is real. I don't know whether or not that kind of attitude could be considered dangerous. If it is, I wonder what kind of person that makes me."

        hi "It was probably the first week I was here. A week doesn't sound so long when I think about it, but at the time it did. Even though I pretty much thought my days were numbered that week, it still seemed to go by so slowly."

        "Even if she can't hear me, it puts me at ease."

        hi "I started to realize that I didn't have that much to complain about. But there's still…"

        hi "Well, never mind."

        scene evh shizune_hcg_tied_stare_small
        with charachangeev

        "She glances at me, for no reason other than that I'm talking. Because she can't understand what I'm saying, Shizune becomes increasingly flustered, but doesn't sign anything in reply."

        scene evh shizune_hcg_tied_close_small
        show evh_hi shizune_hcg_tied_hisao2_small
        with charachangeev

        "Shizune sucks in her breath sharply as she lowers herself onto my penis, trying to keep herself upright as she teeters on top of me."

        "The skirt of her dress covers both of our intimate parts, and traps our body heat under it like a tent. Under it, I feel unbearably hot, and Shizune's hand guiding me into her only adds to it."

        show evh shizune_hcg_tied_kinky3_small
        with flash

        "The second that I penetrate her, Shizune winces, then nearly falls on top of me. The sudden sensation is mind-numbing, and I feel waves of pleasure radiate through me from both ends of my body."

        "It feels as if my entire lower body is enveloped in the warmth and wetness of Shizune's body, able to feel her every twitch and shudder as she starts moving."

        show evh shizune_hcg_tied_kinky2_small
        with charachangeev

        "Shizune begins rocking her hips back and forth, at first slowly, but with her tempo increasing each time she pulls herself almost completely off of me only to plunge back down at the last second."

        scene evh shizune_hcg_tied_kinky2:
            zoom 1.0 yalign 0.1 xalign 0.7
            acdc_warp 6.0 xalign 0.9
        with flash

        "Being so close to her, I can see the sweat beading on her skin and the fog that forms on her glasses when they slide down her nose and too close to her mouth before she pushes them back up."

        "Her fingertips press into my shoulders, holding on to them to steady herself, pushing against them to pull herself off of me, and then running down my arms and grasping for my wrists and hands as she pushes herself back down."

        scene evh shizune_hcg_tied_close_small
        with flash

        "Maneuvering around like this is difficult at best. Shizune tries to brace herself against me while pushing herself up and down with her feet. I attempt to kiss her, but only manage to succeed in touching our foreheads together, at least not painfully."

        "My thoughts wander briefly to whether or not the door is locked. If it were to open now, I'd probably have a heart attack, literally. And then there's the question of who would be opening the door."

        "The sense of danger only serves to make Shizune's movements more torturous, and I wish she would speed up, but from this position, it may not even be possible."

        show evh shizune_hcg_tied_kinky1_small
        show evh_hi shizune_hcg_tied_hisao2_small
        with charachangeev

        "I start moving my hips upwards in rhythm with her, trying to drive myself deeper into her. It doesn't matter to me that my movements are shaking the chair we're on, creating a loud knock as the wooden chair raps against the wooden floor."

        show evh shizune_hcg_tied_kinky3_small
        with charachangeev

        shi "…nn…!"

        "Her breathing grows louder, and even sounds like suppressed moans escape her throat. Though it's obvious that she wants to hold them in, they're still loud enough that they would be audible to anyone standing outside the door."

        "I stop thrusting into Shizune, partly because it's harder to keep up with her as she starts getting more and more into it and moving faster than I can manage to match while under her."

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.4)

        "My heart races so quickly that I can almost hear the blood pounding in my temples, and more worryingly, I can feel a dull throb in my chest. I stop thinking about the pressure I feel between my thighs, if only for a moment."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        scene white
        with whiteout

        "That moment, though, is enough. Combined with the tightness of her squeezing herself around me and the sensation of her skin rubbing against mine, I tense up and fire off inside Shizune. A fleeting feeling of power and flight."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")
        $ renpy.music.play(music_heart, fadein=2.0, if_changed=True)

        scene evh shizune_hcg_tied_close:
            yalign 0.1 xalign 0.8
        show evh_hi shizune_hcg_tied_hisao2:
            yalign 0.1 xalign 0.8
        with Dissolve(2.0)

        "Afterwards, I listen to the sound of my heartbeat slowing down until it reaches its normal rhythm. I listen to the sound of Shizune's breathing as it does the same."

        hide evh_hi
        with charachangeev

        "Her glasses are slightly askew, and this is the first time she isn't messing around with them in some way. I want to straighten them for her, but the second I try, I'm reminded that I can't. Shizune seems to have forgotten it as well."

        stop music fadeout 7.0

        scene evh shizune_hcg_tied_close_small:
            truecenter
            zoom 1.2
            easein 10.0 zoom 1.0
        with Dissolve(2.0)

        "Instead of getting up, she presses herself against me in the chair to extend her reach. It's almost as if this is the only position she can think to untie my hands from. That is what I think as I feel her unbinding my wrists."

        "However, she doesn't get off me. Her fingers gently stroke against mine, occasionally bending inwards to run over my palms. It's funny, but I feel more connected to Shizune through this simple act than before."

        "Shizune stays pressed against me like this for some time. It's a little uncomfortable, but it makes me feel happy, as if I could stay like this for hours."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .confrontation:
        scene bg shizu_guesthisao
        with locationchange

        play music music_daily fadein 0.5

        "The days since then have passed so quickly that time seemed to slip through my fingers like water. Every time I've tried to talk with Shizune, she has been out running errands or with Misha. I feel as if she's avoiding me."

        "I'm not surprised. Of course it bothers me, but I think the way she's acting seems pretty natural. Then again, it's not like I've been through this before."

        scene bg shizu_living at left
        show mishashort perky_smile_cas at center
        with locationskip

        "Whenever I can't find Shizune, I end up running into Misha, and when I do I ask her to help me with my signing. However, she always ends up squirming out of it. We're leaving after today, so I'm determined not to let her escape this time."

        "Once we head back to school, we're probably going to have to start grinding through more student council affairs in preparation for school restarting. I want to brush up on my signing as much as possible by then, even if it's a day's worth."

        hi "Come on, it's pretty much just having a couple sign language conversations! You do that all the time. Actually, you're doing it right now."

        show mishashort cross_laugh_cas
        with charachange

        mi "Wahaha~, really, Hicchan? That's funny!"

        "Misha temporarily stops her unconscious signing in order to wave her hands in front of her face in denial, but then quickly resumes gesturing everything the both of us are saying to no one in particular."

        show mishashort sign_confused_cas
        with charachange

        mi "Hicchan, you're so persistent. Suddenly being interested in sign language again… could it be that Hicchan wants to make a career out of it? That's not fair, that was my idea first~!"

        show mishashort cross_frown_cas
        with charachange

        mi "You should be careful, Hicchan. Times change too quickly~… By the time I decided I wanted to be a sign language interpreter, they had cell phones that people could type out whole paragraphs on. Amazing~! Not very good for me, though!"

        "As if she knows that another deferral isn't going to cut it this time, Misha changes her tune pretty quickly to a more apologetic one."

        show mishashort perky_sad_cas
        with charachange

        mi "I'm sorry, Hicchan, I'm just so~ tired~! Especially lately, even though being with Shicchan is fun, she has way more energy than me! Teaching on top of that would be too~ tiring; I don't have that much stamina! Sorry~!"

        "She doesn't seem very tired, shouting the statement with her usual cheer and vigor. I know it's wrong of me to keep pestering her like this, though."

        show mishashort sign_smile_cas
        with charachange

        mi "Actually~, Shicchan and I were planning on going shopping today! It's our last chance to pick up some souvenirs."

        hi "Souvenirs, huh? I almost forgot that I was on vacation."

        hi "I understand what you're saying. Teaching doesn't seem so easy. Hideaki asked me to teach him how to sign and I was unbelievably lost the whole time."

        hi "Well, I wonder how it'll work out for you when you become a sign language teacher. You can't get tired too easily doing that."

        show mishashort perky_confused_cas
        with charachange

        mi "Yeah, right, right~! I hope not!"

        show mishashort hips_smile_cas
        with charachange

        mi "Hicchan, now I'm kind of worried. But~, souvenirs! So~!, some other time, Hicchan. Aha hahaha~. Do you want us to get you something, too?"

        "Just because I understand doesn't mean I don't want her to teach me. I suppose I can't press her any further now, though. Even I'm bothered by how selfish it would seem to do so. I give up."

        hi "No. Don't get me anything. I'm serious, don't surprise me with a funny shirt or something, okay?"

        show mishashort cross_grin_cas
        with charachange

        mi "Heheheh~."

        "I don't like the sound of that."

        hide mishashort
        with charaexit

        "Slipping on her shoes, she yells goodbye to the otherwise empty house and opens the door to leave, letting a cool breath of fresh air into the hallway. A tuft of dark hair peeking from the door frame tells me Shizune is waiting for her outside."

        hi "Good morning."

        show mishashort perky_smile_cas:
            center xpos 0.8 alpha 0.0
            ease 2.0 center alpha 1.0
        show shizu adjust_happy_cas:
            center xpos 1.0 alpha 0.0
            ease 2.0 tworight alpha 1.0
        with None

        show mishashort

        show bg at right
        with charamove

        show mishashort at center
        show shizu at tworight

        "Misha translates for me from beyond the doorway, and Shizune turns around to give me a small wave."

        "Even though it's different from her usual offhand greetings in the smallest ways, there is an unmistakable hesitation there. It leaves me with a vaguely empty and distant feeling."

        show shizu behind_blank_cas
        with charachange

        shi "…"

        show mishashort hips_grin_cas
        with charachange

        mi "Hicchan, you're up early~! Am I interrupting a conversation?"

        hi "I was trying to get Misha to teach me how to talk to you, but I guess I was being impatient, and it can wait. You two were planning on going shopping today, anyway."

        "Having Misha there, I forget to sign my words as I say them. Unfortunately, since Shizune moved to fill the doorway, Misha is behind her. This brief misalignment in our positions means that what I'm saying is totally lost on her."

        show shizu basic_angry_cas
        with charachange

        ssh "I don't understand you at all."

        "There are things I want to say that I can't put in a way she would understand, and there are entire conversations that she could have that would go right over my head. I want to tell her now that it won't be that way for much longer."

        hide shizu
        hide mishashort
        with charaexit

        "Instead, I just say 'never mind' and tell them to have a good time, then wave them off."

        "It seems like everyone is out for the day, so I sit down on the biggest and most comfortable-looking chair in the living room with a book. Not a sign language book, but one of the novels I checked out of the library my first week."

        "That was so long ago. I should really start chipping at that pile of books I borrowed, or at least return them."

        stop music fadeout 2.0

        show jigoro neutral at center
        with charaenter

        "Sixteen pages in, Jigoro walks into the room, a stack of papers in one hand and his sword twirling idly like a baton in the other, casually shaking water from a recent shower from his hair."

        show jigoro angry:
            center
            ypos 1.15
        with charamovechange

        "Upon being seen doing something so ungentlemanly, he freezes like a deer in the headlights, and slowly moves on to smoldering with powerful but baseless fury as he sits down on the couch a few feet away."

        "This is only the third time I've met him and I'm already starting to feel nauseous on reaction. I guess in a way this could be considered a kind of charisma."

        "I haven't even said anything and he already seems less than pleased. It's likely a bad idea to provoke him, and just talking to him may count as provoking him. However, I can't help thinking of the alternative situations that could play out."

        "Let's say I don't open my mouth at all and walk away, maybe to go read in my room or outside. That would definitely go down as an unforgivable insult. He would probably tell me to hold it and destroy me. Either way, not too polite on my part."

        hi "What are you reading?"

        show jigoro smug
        with charachange

        play music music_another fadein 6.0

        hx "The draft for my autobiography. It is the story of a man who wakes up to find an uninvited guest in his living room, sitting in his chair and reading shallow literary dreck."

        "I've barely started reading the book, I don't even have an opinion on it yet. I can already see how this conversation is going to play out, so I might as well try to steer it in a different direction."

        hi "Where's Hideaki?"

        show jigoro angry
        with charachange

        hx "You even ask questions rudely. Disgraceful. That aside, why would you even ask me such a stupid question? How would I know? Am I my son's keeper?"

        "'Well, you are his dad, and it seems like he does live here, so…' But, I guess I can't say that, tempting as it is."

        "I give up. I already tried to make small talk with him and failed. It's like trying to talk to a brick wall that also hates you. That is my cue to leave and sift through my wallet to see if I have enough money to go to a movie."

        "As I'm about to stand, I have second thoughts. I'm too tired to go through trying to smooth over my problematic situations by trying to continuously walk away from them."

        "It's hypocritical of me to get upset at Misha for trying to defer things when I even run from my own girlfriend. When Jigoro attempts to stop me, I'm almost glad, even though I no longer have any intention to leave."

        show jigoro neutral
        with charachange

        hx "Wait."

        "He says it with plenty of authority but nothing else, as if it's just a particularly commanding afterthought. Only a very powerful or very arrogant person can tell someone to hold on in such a manner. I'm sort of impressed."

        show jigoro smug
        with charachange

        hx "You are in the Student Council with Shizune, aren't you? What is your job there?"

        hi "I don't think there are specific roles, other than president. Shizune is always trying to round people up to help out here and there. Usually we might get like, one person to pitch in, but otherwise the three of us do whatever needs to be done."

        "It's crossed my mind a couple times, around when I first met her, that Shizune's disquietingly analytical stare might be because of her deafness, but it turns out it's a trait shared by everyone else in her family."

        show jigoro neutral
        with charachange

        hx "And that is okay with you?"

        hi "Why wouldn't it be?"

        show jigoro laugh
        with charachange

        hx "You, Shizune, and that pink-haired girl? Is that really your entire Student Council?"

        show jigoro smug
        with charachange

        hx "With a Student Council that small, they wouldn't even bother to hold elections. I am going to take a guess and say that you didn't join the Student Council, Shizune drafted you into it. You said you do not know exactly what your title is."

        hx "That makes sense. I suppose if you weren't even elected, you couldn't be expected to know. After all, if you are not elected, you aren't really anything."

        show jigoro laugh
        with charachange

        hx "No one is going to respect a Student Council like that. An unelected body of three people trying to scrounge up the equivalent of temp workers? It must be a sorry school if three kids having a tea party can handle every issue."

        hi "What's how small it is have to do with anything? If the Student Council gets things done, isn't that enough?"

        hi "It's not just a game, either. Maybe you should actually come to the school one day. If you get there on the right days, you might even be able to see what Shizune is able to accomplish."

        show jigoro angry
        with charachange

        hx "Do you think that I have so much free time, that I can afford to waltz over to your boondocks and watch my daughter's feats of self-aggrandizement? I have never been more disgusted in my life."

        hi "What you're saying is they might as well not have a Student Council, but the fact remains there is one. And Shizune got elected to it, and for her it isn't a meaningless position. In fact, she works very hard for it."

        show jigoro laugh
        with charachange

        hx "You sound like someone who voted for her."

        hi "No, I wasn't there for that."

        show jigoro neutral
        with charachange

        hx "Ha. You didn't even vote for her. Well, besides that - why don't you ask Hideaki about this?"

        show jigoro smug
        with charachange

        hx "Shizune has wanted to be a high school Student Council president since middle school. She would have him read all her practice speeches, wasting his time. For what reason?"

        "This whole time, he hasn't even looked up from thumbing through his manuscript. It's getting increasingly frustrating."

        hi "Because it isn't a game; we don't run the school, but it's not like we're just playing at it and not taking it seriously."

        "I wonder if it is so wrong to not be a purist."

        show jigoro angry
        with charachange

        hx "I have been to your school. Really… The students there…"

        "I can already think of about a million things he might say, and I'm preparing for my heart to sink on hearing any of them. It's funny, they are probably things I've thought before."

        hx "They don't even have cleaning duty."

        "That was not what I expected at all. He's also wrong."

        hi "They do. I should know, I get to skip out on it since I'm in the Student Council."

        show jigoro neutral
        with charachange

        "The concept of being wrong confuses Jigoro. I should take this opportunity to go on the attack. It's really odd that I am thinking this way about a simple conversation."

        hi "It sounds like the last time you were there was really some time ago."

        hi "If you can leisurely write some memoirs, you can talk to Shizune now and then. Don't you think that she has stuff she is proud of?"

        hi "That's how young people are. We have things to be proud of. If you're writing an autobiography, you should get that."

        "Such an opportunity, and I blew it. I don't know how I was expecting him to react. Maybe introspectively, but Jigoro only grows angrier by the second. Yet as he does, he also seems calmer, in a way. More sure of himself and in control."

        show jigoro angry
        with charachange

        hx "Who do you think you are to assume that my life is so easy? You haven't even read my biography, yet you are able to tell me how I should handle all my affairs, including dealing with my own daughter. You could never understand."

        hx "Even if I were to get up from this couch, walk over to you right now, and punch you in the forehead with brass knuckles with a condensed edition of my life story on them, leaving my biography imprinted in your face, you would not understand."

        hx "For twelve years, Shizune did not even talk to me, even though I hired multiple tutors and interpreters of all sorts for her to try and get her to become normal. It isn't as simple as you think it is."

        show jigoro smug
        with charachange

        hx "If she does not want to bother with me, then fine. I assume that is normal. When was the last time you talked to your parents?"

        "It has been a while, and I feel ashamed. More so that he caught me than at how easily I could have dropped my parents a phone call or sent them an e-mail, or even a letter, and haven't. This knowledge only makes me feel more ashamed."

        show jigoro laugh
        with charachange

        hx "I thought so."

        hi "If I wanted to see my parents, I couldn't. This is different. You aren't that far from her, it's one train ride away!"

        show jigoro neutral
        with charachange

        hx "That is enough. No means no. You are very persistent. If only it was about something that mattered. I can't see what you may have learned from my daughter aside from that and how to backtalk people. Is that it?"

        stop music fadeout 10.0

        "The answer is yes. I wasn't this persistent or argumentative before meeting Shizune and Misha. After all, prior to meeting them, I'd just experienced a small death. It's a mystery as to why I refused to join the Student Council in the first place."

        if wanted_introduce or _in_replay:
            "It took monumental effort just to introduce myself on my first day there. I might have rolled over for anyone and any cause. It might have just been chance that Student Council appealed to me so little that I would fight it."

        "Possibly it was from trying to get away from their nagging so much that I was able to get my energy back. It's a cute idea."

        "I think again about why I'm still here. Arguing with Jigoro is pointless, yet I think I almost looked forward to it. And he is right, I cannot understand him. Even if I did, he wouldn't care. I'm a louse that crawls on a whale: wholly insignificant."

        "He has a confidence that I don't have. Shizune does, and it could be that the reason why I am here now, in an almost-shouting match with her father, is because some of that bravery has rubbed off onto me. However, I don't have anything to keep it going."

        "Still, I hate him. I don't know what I can do. A few months ago, I think I would have punched him and let the consequences play out as they may. But now, I can't risk it. If he were to hit me back, he'd likely kill me."

        "So in the end, the only thing I can do is look at Jigoro in silence, knowing that I have no reply, and hate him, and feel completely at a loss. Oddly, he takes it as defiance."

        show jigoro angry
        with charachange

        hx "Hmph. Fine, then. Have fun with that."

        show jigoro:
            ease 1.0 center alpha 0.0

        pause 1.0

        "Picking up his sword and using it to pull himself to his feet, he turns and casually saunters out of the room. I want to throw my book after him, but I'm happy to finally be alone, even if I'm not in the mood to read any longer."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .the_anchor:
        scene bg city_station
        with locationchange

        "Our return trip to the school keeps getting delayed in one way or another. Shizune and Misha come back so late that there's no use even leaving and we end up staying another day."

        "The morning after, we miss the train by a single minute and then the next two don't arrive. We miss the fourth train because I wandered off to get a drink in the meantime. Shizune wasn't very happy about that."

        scene bg school_dormhisao
        with shorttimeskip

        play music music_dreamy fadein 2.0

        "By the time I finally get back to my room, I feel so tired, even though I spent most of the ride back sleeping. I can't say it's only because of today; this seems like a familiar symptom of traveling. It's not the first time it's happened."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        scene black
        with shuteye

        "If no one has beaten me to it, I could do a thesis on it, maybe get in a medical journal. 'Returning From A Trip Syndrome.' Not very creative. I fall asleep before I can think of a better name."

        play sound sfx_doorknock

        pause 1.0

        scene bg school_dormhisao
        with openeye

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        "A loud knock on my door wakes me up only a few hours into my nap. I'm annoyed because I had just been in the middle of a dream that I can't remember, having been woken up in the middle of it. But I'm sure it was a good one."

        "I briefly wonder who it could be, but it's not like I get many visitors, so I'm sure it's Kenji. I hope he is just rolling out the welcome wagon and not going to hit me up for money again. If that was the case I'd be almost touched."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        scene black
        with shuteye

        "Not touched enough to fight off the urge to roll over and go back to sleep, though."

        stop music fadeout 5.0

        pause 4.0

        scene bg school_dormhisao
        with openeye

        "A few hours after that, I wake up again and immediately spot an envelope on the floor."

        "It must be something that came in the mail while I was away. That's Shizune and Misha's department, so I wonder if they dropped by to give it to me, or maybe someone filled in for them in their absence and told Kenji to pass it along…"

        show letter_insert:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0

        pause 1.0

        show letter_insert at truecenter

        $ renpy.music.set_volume(1.0, 0.0, channel="music")
        play music music_rain fadein 4.0

        "When I pick it up, any remnants of sleepiness in me instantly vanish."

        "Even if the name of the sender wasn't on it, I would have known whom it was from by looking at the envelope itself, realizing why it looked so familiar. By recognizing the delicate handwriting addressing it."

        "It's from Iwanako. At first, I can't believe it, but it wouldn't be too hard for her to track me down if she wanted to."

        "Of course, I hadn't thought that she would want to. She was maybe my girlfriend for all of five seconds. After that, we barely spoke to each other."

        show letter_insert:
            easeout 1.0 ypos 0.7 alpha 0.0

        pause 1.0

        hide letter_insert

        "It would be too easy to put this letter away somewhere and forget about it. A part of me wants to do that. Or throw it away, unread. Why I want to do these things, I don't know. It would be easy to do them. Easier than to read it."

        scene ev hisao_letter_open
        with locationchange

        "Slitting the envelope open with the tip of a pen, I'm surprised by the length of the letter that spills out."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        call screen written_note(_("Dear Hisao,\n\nHow are you? I hope you are well and happy at your new school. Everyone here misses you. Almost all of our second-year class got put together in class 3-1 for the final year, so we are pretty comfortable right from the beginning of the year. I'm sure you would've been assigned to this class as well."))

        call screen written_note(_("The mood among the third-years seems to be very anxious about the final exams, even though they are so far away. The teachers are badgering us about it all the time - even old Mr. Tachibana who is, by the way, our homeroom teacher this year. Would you believe it? I was sure that he'd retire after our second year, but here he is, nagging everyone about studying for exams.\n"))

        call screen written_note(_("I think things like that are the main reason why the mood among the third-years is so nervous. I must admit that I'm somehow losing confidence in myself as well, even though I've always fared reasonably well in exams.{vspace=150}"))

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        "The small talk makes me feel nostalgic. It's almost like I'm in the hospital again. Every now and then Iwanako would drop by and give me the gist of what was going on in a class that, even then, I had an inkling that I would never return to."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        call screen written_note(_("It's so weird to think we are already seniors, isn't it? Time has really flown past. I wonder where it went. The new first-years seem so young and somehow really innocent. I keep wondering if I was like them in my first year. I've been feeling nostalgic like this for the whole first trimester.{vspace=90}"))

        show ev hisao_letter_open:
            "ev hisao_letter_open_2" with locationchange

        call screen written_note(_("There are other things I want to say. I'm writing to you because I felt that there are things I should've said after the incident back in winter. I really regret that I wasn't able to say them in person, and I have no excuse for it.{vspace=150}"))

        call screen written_note(_("The truth is, the times when I visited you at the hospital made me worried about you. I am not talking about your health. You seemed to become more distant and disheartened. It was natural after something like that happened, I'm sure, but somehow I got the feeling that you had given up on something back then. Happiness, maybe?\n"))

        call screen written_note(_("I wanted to somehow express my feelings, but the right words didn't come to me. I couldn't say anything to comfort you. I am really sorry for not being able to support you when it mattered the most, even though I like you so much. At least now, finally, I can be more honest.{vspace=120}"))

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        "What a convenient time for her to rediscover her sincerity. Well, even as I think that, I know she's right. 'Distant and disheartened' is a good way to describe it. And maybe I had given up, too."

        "It weighs on my heart when I think back to when I was lying in the hospital, feeling so bitter when she finally stopped showing up. I wasn't surprised, and I had no right to be. How could she not stop coming when it was the only expectation I had of her?"

        "She dropped by only for all of six weeks after the incident. If I drifted away from her, it was because I could feel her already moving herself away from me the moment she showed up."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        call screen written_note(_("If I could go back to those quiet days in February and March, I'd tell you to not give up on yourself. That's what I would say. Maybe you wouldn't have drifted so far away if I had just said something. I hope you've managed to get back on your feet on your own.{vspace=120}"))

        call screen written_note(_("Now that the distance between us is also physical, it also feels more final, somehow. I wonder if we will meet again. Perhaps it's for the best if we don't? Still, if you would like to correspond with me, by all means write me back. I'd very much like to hear about your new school and how you are doing. I wish you all the best.\n\nSincerely, Iwanako"))

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        "It's a strange feeling. I know that I'm never going to hear from her again."

        "If she really wanted to keep in touch, she wouldn't have picked a medium like snail mail to do it through. If she could get my address, then my e-mail or phone number wouldn't have been much more work, had she wanted them. This is only a goodbye."

        stop music fadeout 4.0

        "I exhale, only just now becoming aware that I had been reading with bated breath. Now who's being distant, Iwanako? But maybe it really is for the best."

        "For her to pick up a pen and write this letter to me, it can only be because she felt guilty about how things ended. That she was hurt by how we floated out of each other's lives makes me feel a sort of wistful happiness."

        "I almost want to thank her, and I only don't because I know she wouldn't want me to reply."

        play sound sfx_doorknock

        scene bg school_dormhisao
        with locationchange

        "There's a knock at my door, then it opens anyway about a millisecond later. I forgot to lock it, stupidly."

        ke "Sup, man? Why's your door open?"

        "I run to the door faster than is probably medically safe for me to do so I can prevent Kenji from seeing the mountains of pills just a couple feet away from him, blocked from his sight only by the door."

        "Then there's the letter I'm holding. If he asks about it, I don't think I could make up anything convincing."

        "About two feet away from him I realize that his vision is so bad that it was probably never an issue. He didn't even see me about to practically tackle him back through the door frame."

        scene bg school_dormhallway
        show kenji tsun_close at center
        with locationchange

        play music music_kenji fadein 0.5

        ke "Hey, what the hell, man?"

        hi "What are you talking about? Your room has a billion locks on it, yet you just barge right through other people's doors."

        hi "You didn't even wait a second after knocking before you tried the door, it was like, simultaneous. You were already opening the door while you were knocking on it."

        show kenji happy_close
        with charachange

        ke "See? That's exactly why I have all those locks. It's a cold and uncaring world out there, a gate crasher's world. Now you also understand."

        show kenji neutral_close
        with charachange

        ke "I just taught you a valuable lesson, dude. Knowledge is power. Why are you yelling at me? I'm a hero."

        show kenji tsun_close
        with charachange

        ke "Look at you… you didn't even lock your door. The average woman could have killed you a billion times already, then replaced you with a female clone indistinguishable from the original. It almost happened to me."

        "Ignoring the latter part, since it's too confusing, it's funny he should say that. He was unable to stop me from tackling him head-on, yet apparently a woman could have killed me a billion times. If this man is a hero, we are all doomed."

        show kenji happy_close
        with charachange

        ke "What's that you've got there?"

        "Somehow, he is able to see the letter still in my hand. With how I've been waving it around, that is no surprise. I fold it back up quickly, but take care not to whip it behind my back or anything else. That would be too suspicious."

        "It seems like I'm jumpier than I'd thought about Iwanako writing to me."

        hi "I got a letter."

        show kenji neutral_close
        with charachange

        ke "Oh, yeah, I put that there. I was sleeping, then I woke up because I heard explosions."

        ke "I put on my helmet and then peeked outside to see what was going on, but it was just that Student Council woman banging on your door. It was the one without pink hair."

        show kenji tsun_close
        with charachange

        ke "She was knocking so loudly that it was obvious she was filled with murderous rage. Rage at you. Then she somehow sensed me behind her, and I tried to escape, but it was too late. She caught me and started pointing at the door."

        "I open my mouth to tell him that she's deaf, but decide not to. For various reasons."

        ke "I didn't really get it, and she got more and more pissed off, like an old man trying to use a touchscreen phone."

        show kenji happy_close
        with charachange

        ke "She was going to kill me. Kill me and replace me with a woman version of me. But then the sunlight reflected off my glasses and blinded her, saving my life."

        show kenji neutral_close
        with charachange

        ke "It was like, behold, optic blast. I don't get how someone with glasses can be hurt by glasses. She uses them too, she should be immune to their death rays… but whatever. She gave me this envelope with your name on it and just left."

        show kenji happy_close
        with charachange

        ke "Clearly, she was out for blood, so I lied and said you were away. I think you were away, right? I've been trying to ask you if you wanted to help me with my homework for a week now, but kept getting no answer. …Welcome back, man!"

        hi "Thanks."

        show kenji neutral_close
        with charachange

        ke "Yeah, so she gave me this envelope and it had your name on it. I didn't want to hold on to it, because, what if it was a bomb? So I just shoved it under your door when she was gone."

        ke "I was going to tell you, but you got back before I could. At least it's not a bomb."

        hi "Gee, thanks. I'm not going to help you out with your math homework, because, what if your math textbook is a bomb?"

        show kenji tsun_close
        with charachange

        "He looks devastated, and also like he's considering the possibility that it really could be a bomb. I guess it is possible, since no one really uses their math book all that much."

        scene bg school_dormhisao
        with locationchange

        "I throw the letter on the dresser behind me and turn to leave, swinging the door shut behind me as I do. It collides against the tip of Kenji's shoe and bounces back open, while he hops around for a bit, acting like it hurt way more than it should have."

        show kenji neutral at center
        with charaenter

        "Before I know it, he's already inside my room. I'm powerless to stop him before he scoops up the letter, strangely ignoring the towers of pill bottles surrounding it."

        hi "Don't just read mail that isn't your own."

        show kenji happy
        with charachange

        ke "C'mon, what is it? A love letter from your girlfriend? Did she include any photos? Sexy photos?"

        play sound sfx_dropstuff
        stop music fadeout 4.0

        "Reclining against the dresser and paying no mind to the bottles he sends all over the floor by doing so, Kenji quietly reads through Iwanako's letter."

        "The process takes seemingly forever, and with how close he holds it up to his face, makes it look like he's trying to eat it."

        show kenji tsun
        with charachange

        ke "Who's 'Iwanako?'"

        hi "My ex-girlfriend."

        play music music_night fadein 4.0

        show kenji neutral
        with charachange

        ke "Ex-girlfriend, huh? This is the breakup letter, then. I thought they were a myth."

        hi "No. I guess it is, but really, she's been my ex-girlfriend for a while. Anyway, I think I'm already over it."

        "Kenji gives a thumbs up, clearly relieved that I'm not going to take this into an awkward direction, although I almost want to since I told him not to read it."

        show kenji happy
        with charachange

        ke "Yeah, that's a good attitude. It's all right, I had a bad breakup, too, but you can't let it get you down. I mean, just look at me."

        hi "Uhhhh…"

        ke "But, hey, she wrote you a letter. Maybe she wants to get back together, huh? It says right there, write her back. You should do it. Is she cute?"

        "For a guy who thinks feminists are working to enslave men everywhere, he really is interested in cute girls."

        hi "I have a girlfriend. Besides, look at the context, she doesn't want me to write back. Just because that's what it says, that isn't what she means."

        show kenji neutral
        with charachange

        ke "But that's what she wrote. This rock-fish-kid chick totally still wants you. It even says it right there."

        hi "I read it, I know what it says. I told you, you have to look at the context. She said I drifted away from her, and everything there shows she accepted that."

        hi "I think the reason she wrote to me is that she just wants to, I guess, part amicably. But we're done, she doesn't want to get back together or whatever you're thinking."

        "As I think about it more, it sounds to me like I'm just trying to make excuses for myself. That's not a good place to be."

        "I'm positive that she doesn't want me to write her back. I can live with that. If I were to write her back and get a less than desirable response, or no response, then I would just be crushed."

        "Perhaps the fear of that is why I'm trying to justify my decision. It could be, but I don't want to think about it. The thought is oddly repulsive."

        hi "Why is this such a big deal to you, anyway?"

        show kenji happy
        with charachange

        ke "Because you should write back to her. She wants you to. I want to see what the response is going to be."

        show kenji neutral
        with charachange

        ke "Damn, it doesn't even have to be a nice letter. That's cool too, but you could write an angry letter and call her out. That's my new attack strategy, I'm just going to call women out. You should try it."

        hi "Even if she wrote me a letter, you have to understand what that means. Writing someone a letter is different now. It's not something you just do. Not in this kind of situation."

        hi "You can pick up your phone and call someone across the world in an instant, and talk to them almost like they were there with you. Or send them an email; they'll be notified instantly that they got it and can reply back, just like that."

        hi "A letter can be a personal thing, but she wanted to keep me at an arm's distance. It's not like I can pop over there and visit her."

        hi "If I had her number, I could call her, or if I had her mail, I could mail her. If she really wanted to hear back from me, she would have dropped one of those in there."

        "I feel silly for continuously reassuring myself that I'm not fazed by Iwanako writing to me, when it's so obvious that I am."

        show kenji tsun
        with charachange

        ke "It could be like a gradual thing for her. She might be too shy to call you up. I remember my girlfriend would always send me text messages because she was so shy. It was annoying as hell, man."

        ke "I didn't really give a shit about phones so I didn't have the thing, and it turns out I had to pay for every single one. But I don't like phones so I couldn't even call her back to tell her to cut that out."

        show kenji neutral
        with charachange

        ke "I did it anyway, though. I called her out. I even used a phone. It was literally the call out."

        hi "I guess it was."

        "Even if he's right, it means that Iwanako still wants to keep her distance from me. She's 'not ready' to chat with me comfortably."

        "Why? Am I some kind of freak? I'm not reassured by her actions anyway, in that case. Maybe I am overthinking it, but I just don't know."

        "Kenji can't think of anything to say to that, and the silence that follows is so awkward and thick that I start to count the seconds until he makes up a reason to leave and excuses himself."

        show kenji tsun
        with charachange

        ke "I miss her…"

        hi "Your ex?"

        ke "Yeah. Even if she was insane, it was nice being with her."

        ke "My back hurts. If she were still around I could tell her to massage it. I don't know how to use an oven, either. I miss baked food. And we would go bowling in the hallway sometimes. I miss that, too. I had to bowl all by myself during that last festival."

        hi "You bowl in the hallway? You're going to hit someone."

        ke "She used to say that all the time…"

        "Kenji sighs nostalgically, clearly not appreciating just how badly someone can get hurt by slipping on a bowling pin. Apparently, neither did his girlfriend, since she bowled with him. What a strange definition of love, but I guess it's something."

        hi "Maybe you should write her a letter. If she writes back, you can get married."

        stop music fadeout 0.3

        show kenji rage
        with charachange

        ke "Married?! No. No no no. No."

        hi "Okay, fine. But why not? You clearly like her, even though you hate women."

        show kenji tsun
        with charachange

        play music music_kenji fadein 2.0

        ke "Feminists! Not women, feminists. There's a difference. There are non-feminist women. Damn, your discrimination is incredible. Correlation doesn't equal causation. Even if she is insane and a woman, it doesn't mean she is a feminist insane woman."

        show kenji neutral
        with charachange

        ke "It's like how the absence of evidence isn't the evidence of absence. If it's true, then by the relative property, the presence of evidence doesn't equal the evidence of presence."

        hi "Actually, I think it is. And I don't think it's called the relative property."

        show kenji tsun
        with charachange

        ke "No, shut up, it's mathematics! Are you saying math is wrong?"

        "I think he is wrong."

        "So even Kenji has someone that he likes. I'm tempted to ask why he and his ex broke up, or to dig for more information in general, but I shouldn't. Not only would it be prying, but he might reverse the question back to me."

        stop music fadeout 8.0

        "This conversation makes me think about Shizune, although the thoughts I'm having are scattered and wispy. Just questions."

        "I wonder if I even had the chance to love Iwanako, and this whole situation with her still stings me, a sour note in the back of my mind."

        "I like Shizune much more. Yet it feels like I am chasing her, even now. I don't mind the chase, but I want to close that distance between us."

        "Iwanako's letter is responsible, but I've also felt this way for a while. I've come closer, but it's not enough. I want to try again, right now."

        hide kenji
        with charaexit

        "I tell Kenji to get out so I can change, and then head for the student council room."

        scene bg school_courtyard
        with locationskip

        "The grounds are mostly deserted today, which is a shame, because it's so nice out."

        scene bg school_hallway3
        with locationskip

        play sound sfx_doorknock2

        "No one answers when I knock. I try to go in anyway, but it's locked. When I pull my hand away from the doorknob, it's covered in dust. It looks like no one's been here since we left."

        "Since I'm already out here and dressed, I might as well get something to eat in town. My wallet is back in my room, though."

        scene ev misha_sad:
            truecenter
            zoom 1.05
            easein 10.0 zoom 1.0
        with locationskip

        "On the way back there, I stumble across Misha sitting down behind the main building."

        "Her eyes are closed in sleep, and she looks very tranquil. It's always been hard to picture her not constantly bouncing around or hopping on the tips of her toes impatiently."

        "My first instinct is to call out to her and ask her if she has seen Shizune, or if she wants to go to town with me, but now that I've seen her I don't feel like disturbing her. I leave her alone."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .roadmap:
        scene bg school_council_bw
        with locationchange

        $ renpy.music.set_volume(0.5, 0.0, channel="music")
        play music music_pearly

        nvl clear
        nvl show dissolve

        n "{vspace=90}For the first few days after I was back, I almost forgot that I was in the Student Council. I managed to pick up here and there that the Student Council usually gets swamped with work around the end of the break, but it didn't have to be the case."

        n "The few times when I managed to catch Shizune or Misha, they were in too much of a hurry for me to get a chance to ask if they needed help. Anytime they weren't, I'd only be able to get ahold of Misha."

        n "{vspace=30}Shizune would say something about how there was work, but it was so little that involving either Misha or I would only bore us."

        n "{vspace=60}After awhile, the idea of having some free time again had started to grow on me, though there were still periods when I felt like I had too much of it."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl hide dissolve
        nvl clear

        scene bg school_council
        show shizu basic_normal2 at center
        with locationchange

        "Just when I was getting used to it, though, things changed again. Now I find myself back in the student council room, arguing with Shizune about whether tissue boxes make good ballot boxes or not."

        hi "I'm telling you, they work just fine, as long as we get the cube-shaped ones, not the rectangular ones."

        hi "Misha, can you sign that to her? I've kind of got my hands full. …On second thought, forget it."

        "She is busy cutting out ballot slips, so if she were to make one errant movement she would probably send those scissors flying into someone's head."

        "I drop the box of poster paints I'm carrying onto my little table in the student council room, and cough as a wave of dust hits me in the face. It really has been a while."

        show shizu behind_blank
        with charachange

        ssh "Do you think we should change the size of the ballot slips?"

        show bg at bgright
        show shizu at tworight
        with charamove

        show mishashort sign_confused at twoleft
        with charaenter

        mi "What~? But Shicchan, I already cut out so many of them…"

        show shizu basic_normal
        with charachange

        ssh "We can make them smaller. It will be more efficient. We just have to shrink the font. More ballots will fit in a single box that way. We'll only need half the amount of paper, then."

        show shizu behind_smile
        with charachange

        ssh "The format for voting can be changed. It could be more like a real election; then we might be able to get away with buying less boxes."

        show shizu adjust_happy
        with charachange

        ssh "With the money left over, we can get a pizza, or maybe Chinese, or a cake, or three bowls of the new ramen bowl I want to try."

        "Shizune excitedly rubs a finger along the frame of her glasses as she ponders more ways to cut even a half-yen of spending off of our budget."

        "Since I think she is the only one who even knows what our budget is, I'm scared to ask just how tiny is it for her to have to do this."

        hi "What about all the ballot slips Misha already cut out?"

        show shizu basic_happy
        with charachange

        ssh "Don't worry, don't worry. I can make them into memo pads and sell them in the school store."

        show mishashort perky_confused
        with charachange

        mi "Shicchan, they don't look very cute, though~…"

        show shizu adjust_frown
        with charachange

        "Shizune seems to disagree. Now they're arguing, but it looks like it consists of nothing more than signing 'Yes, they do' and 'No, they don't' at each other until they're so tired of it they are just taking turns pointing at each other commandingly."

        "It's strange, partly because it looks kind of ridiculous, but also because I've never seen them disagree."

        "Then again, both of them have looked very stressed these past few days."

        "Shizune has been increasingly absorbed in the idea of student council elections, though they're months away. I imagine this is how politicians act when they realize a regime change is imminent and their era is over."

        "I'm having trouble taking student council matters seriously at all, even now, as I practice my calligraphy on signs that won't go up for weeks, but I can understand why Shizune does."

        "After all, she has been Student Council president for three years. According to her dad, she has wanted the job for even longer. I guess three years is too short a career for her to leave feeling satisfied."

        hi "Did the last Student Council go through this much trouble to make it a smooth transition for you?"

        show shizu behind_frustrated
        with charachange

        "Shizune makes a chagrined face that tells me they weren't very helpful at all."

        hi "I guess you're doing all this to set a good example, then?"

        show shizu basic_frown
        with charachange

        shi "…"

        show mishashort hips_frown
        with charachange

        mi "That only comes into play if they learn anything from it, Hicchan~! If they don't, I'll be hyper mad~! If they turn out to be the flaky type, I'll definitely be hard on them~."

        "It doesn't sound very threatening when Misha is saying it."

        hi "So, you've already met them?"

        show shizu adjust_smug
        with charachange

        shi "…"

        show mishashort hips_grin
        with charachange

        mi "Ahaha~. Hicchan, there are no candidates yet~!"

        hi "What? None?"

        show shizu behind_smile
        show mishashort hips_smile
        with charachange

        ssh "Not even for Student Council president. That is why I am trying to drum up interest for the position. What do you think?"

        "She proudly holds up a poster she has been working on herself. It looks very, uh, military."

        hi "You might be taking this a little too seriously, then."

        show shizu adjust_frown
        with charachange

        "Shizune frowns and plays with her glasses, offended."

        ssh "Is that weird?"

        hi "Yes."

        show shizu behind_smile
        with charachange

        "She looks oddly happy that I'm disagreeing with her, and I think that if she weren't genuinely focused on what she was doing, she would try to argue with me just because it would be interesting to her."

        show shizu basic_normal
        with charachange

        ssh "What's weird about it?"

        show shizu adjust_smug
        with charachange

        "It looks like she will do that after all. But then, Shizune waves her hand dismissively, like she is trying to catch the words in the air and delete them. Instead, she catapults into insulting her future successors."

        hi "Well, one thing that's weird is that in my old school the elections would happen in about six months, since, you know, we're graduating in March. It's pretty weird to think about them so early."

        show shizu behind_blank
        with charachange

        ssh "It's a little different here."

        show shizu adjust_frown
        with charachange

        shi "…"

        show mishashort sign_smile
        with charachange

        mi "Hicchan, I'll be discouraged if we don't have any replacements when I have to go~! Shicchan says."

        show mishashort hips_grin
        with charachange

        mi "But~!, it isn't like the school will stop running without a Student Council. It will be harder for them to hand out forms, though~!"

        show mishashort cross_laugh
        with charachange

        mi "Hahaha~."

        show shizu basic_normal2
        show mishashort cross_smile
        with charachange

        "Shizune isn't laughing, however. Misha's joke causes her to flinch, as if she were stung. Though Misha didn't mean for it to come out that way, her quip had a callous cruelty to it in the end."

        show shizu adjust_frown
        with charachange

        ssh "Hmph. I'm trying to get more people to run, but everyone is so lazy. They think they can take it easy just because there are no deadlines yet. Slackers, not taking the early game advantage."

        show shizu cross_angry
        with charachange

        ssh "'Still' six months away? If they aren't making their move now, they don't deserve a vote!"

        show mishashort sign_smile
        with charachange

        mi "Do they really think it's such an easy job that they can do everything at the last minute and just coast into the role~? Insulting~! Really~, really~!"

        show mishashort hips_frown
        with charachange

        mi "They're going to be eaten alive once they have to sit at this tiny desk and see just how much work they have to do~!"

        show shizu behind_frustrated
        with charachange

        ssh "If this were a real election, they would be in deep trouble. I was reading about Japanese campaigning laws the other day. Only the bad ones, for some reason."

        hi "For some reason."

        "For a second, Shizune was 'talking' like her father there, and it was coming out of Misha's mouth. Creepy."

        hi "Well, first off, shadow shogun, you can't really make that call. They'll be elected. Second, it's just a school election. It's not like running for city council, or the Diet. I don't think Japanese campaigning laws apply."

        "Third, although I don't want to say it, I'm nervous that Shizune is so enthusiastic about this, talking of elections and votes."

        "According to her dad, she wasn't even elected herself. Come to think of it, I can't remember Shizune ever saying she was elected, either."

        "Then, did she get this position by being recruited into the Student Council, and having it fall apart until she was the only one left? Somehow, I'd never considered it."

        "I don't know what to think about that, but it wouldn't surprise me. We're only three people strong now."

        "If the circumstances behind her becoming the Student Council president were that sad, I wonder if there will be a vote at all. Interest could just be that low; or nonexistent, really. Then all her energy would be going towards nothing."

        "I slap an exclamation mark on the end of the poster I'm working on. It's a little plain, so I think adding one is okay. Actually, it still might be a little too plain. I make the mark twice as large."

        hi "I still say you need to slow down. If this stuff isn't going to be relevant for months, maybe you're working a little too hard on it. That's what I think. You're worrying too much."

        "I don't know how to sign the word 'relevant.' I try, and only end up flicking a long line of paint where I didn't intend to. There is no way I can fix that."

        hi "Misha, can you ask her that?"

        show mishashort sign_smile
        with charachangealways

        show shizu adjust_happy
        with charachangealways

        "Shizune giggles silently, clenching her teeth so that no sound actually comes out."

        show shizu behind_blank
        with charachange

        ssh "Because there is a lot to worry about."

        hi "Like what?"

        show shizu basic_normal
        with charachange

        ssh "Like… usually the boxes end up looking very pretty, so people take them. Have to plan for that."

        show mishashort hips_grin
        with charachange

        mi "Wahaha~! We should make them funny-looking this time, then, so no one will take them! How about that, Shicchan~?"

        hi "We can draw some weird faces on them. Or we can put a little picture of Shizune on each one saying 'Stealing is wrong.'"

        show shizu behind_frown
        with charachange

        ssh "No. It's not funny! It's not the only problem, either. There is voter turnout, of course…"

        show shizu basic_normal2
        with charachange

        ssh "…And then the worst case scenario would be not having any candidates."

        "Although it seems she meant it jokingly, from the way she smiles as she signs it, that isn't how it comes out."

        show mishashort cross_laugh
        with charachange

        "Even Misha understands that the possibility is very real, and though she tries to salvage the mood by punctuating Shizune's statement with a laugh, it doesn't work."

        show shizu behind_frustrated
        with charachange

        shi "…"

        show shizu basic_angry
        with charachange

        ssh "What is wrong with both of you?"

        show shizu adjust_frown
        with charachange

        ssh "I was just making a joke. There actually is some interest this year. If there wasn't, would I be doing all this work? I'm not stupid."

        show shizu behind_smile
        with charachange

        ssh "When the elections are over, I'll buy everyone dinner. I'm already planning it."

        hi "Even the new Student Council?"

        show shizu adjust_smug
        with charachange

        ssh "No, they can buy their own celebration dinner. It will only be for the current Student Council. I'll be happy once I'm through having to do these thankless jobs all the time."

        show mishashort hips_grin
        with charachange

        mi "A dinner just for us~? Yay~! It's like a little party, Shicchan~!"

        stop music fadeout 3.0

        "Though her cheerfulness is obviously forced, I say nothing. For the rest of the period, which fortunately isn't very long, we work in silence."

        scene bg school_hallway3
        with shorttimeskip

        play music music_daily fadein 0.5

        "After classes, I find the student council room locked. It's strange, because Shizune was so busy earlier that I would expect her to continue working after school. It would be what she would normally do."

        "Maybe she listened to my suggestion and decided to take a break. I'm hoping it's that simple."

        scene bg school_courtyard_ss
        with locationskip

        "Feeling a little uneasy, I take a brief stroll around the school. It's only half-conscious; I can't remember when I started moving my feet, but I've already covered enough of the campus that I'm starting to feel tired. Not that that means anything, now."

        "Just a short stroll around the school grounds, and I'm already winded. Really pathetic."

        scene bg school_hallway3
        with locationskip

        "Before I know it, I'm back in front of the student council office. There's someone else, too, this time."

        show mishashort hips_smile at center
        with charaenter

        mi "Hi, Hicchan~!"

        hi "It's locked."

        "Seeing a can of lemonade in her hand, I reflexively start looking for a vending machine nearby. I'm so thirsty."

        show mishashort sign_smile
        with charachange

        mi "I know that, Hicchan~! Shicchan is somewhere else, I guess~!"

        hi "Weird."

        show mishashort hips_grin
        with charachange

        mi "Ahahaha~. We aren't stuck together, Hicchan~."

        "Misha takes a long drink from her lemonade, eventually just tipping it over and pouring the rest into her mouth. I feel like I am being mocked."

        show mishashort perky_smile
        with charachange

        mi "Do you want one, Hicchan~?"

        hi "No, it's okay. I can't take someone else's drink, it's rude. Besides, you're making fun of me, aren't you? I just saw you inhale all of that."

        show mishashort sign_smile
        with charachange

        mi "I have another one in my bag~! I was prepared, see~, see~? I'm just like Shicchan~!"

        hi "She's a little too prepared. It's good some of that is rubbing off on you, anyway. After what, two years?"

        show mishashort cross_laugh
        with charachange

        mi "Wahaha~!"

        "The way she stares at me as I drink it is a little disconcerting, but I'm too grateful to care much about it."

        hi "You and Shizune always end up treating me to something. It's starting to embarrass me."

        show mishashort hips_smile
        with charachange

        mi "Really~, Hicchan? Ahaha~. Buy me lunch sometime, then, okay~? Then~!, we'll be even."

        hi "Well, it's funny you should say that. I was going to ask you if you wanted to eat in town…"

        show mishashort hips_grin
        with charachange

        mi "Yeah~ yeah~! I'm really hungry today, Hicchan! Thanks!"

        show mishashort:
            ease 1.0 tworight alpha 0.0

        pause 1.0

        hide mishashort

        stop music fadeout 3.0

        "…Yesterday. I was going to ask her yesterday. Misha cuts me off before I can finish the sentence, and I can't find an opening to correct her as she dashes enthusiastically around me, laughing, her arms flapping excitedly at her sides."

        scene bg suburb_roadcenter_ss
        with locationskip

        play music music_dreamy fadein 2.0

        "I already have my wallet with me, so I start walking towards town with Misha trailing behind me, playing idly with her hands and loudly wondering to herself where we should go eat. At least, I think so. She could be asking me."

        hi "Do you have anywhere specific where you want to go?"

        show mishashort hips_smile_ss at center
        with charaenter

        mi "Hmmm~. I want to go to the teahouse, they have a really big parfait there."

        hi "I saw you eat a parfait there last time, it looked really big."

        show mishashort hips_grin_ss
        with charachange

        mi "No no no~! This one is really, really~ big! It's also really expensive~!"

        hi "Really, really~ expensive?"

        show mishashort cross_laugh_ss
        with charachange

        mi "Hahaha~! A little~…"

        hi "Jeez. Well, you and Shizune paid for my food a bunch of times, so it's fine."

        show mishashort perky_confused_ss
        with charachange

        mi "Hicchan, I don't think I ever did that~. Are you sure it wasn't just Shicchan?"

        hi "Are you really arguing against a free meal? Don't worry about it."

        scene bg suburb_shanghaiint
        with locationskip

        "We go to the Shanghai, and are seated by a waitress who is surprisingly not Yuuko."

        "Misha is very eager to eat that parfait, because she shouts her order as soon as she walks through the door. When it arrives, I can see that it is both very big and very expensive-looking."

        show mishashort perky_confused_close at center
        with charaenter

        mi "Aren't you going to order anything, Hicchan~? If you're hungry, we can share."

        hi "Nah. I don't like parfaits. I don't like pralin."

        show mishashort sign_smile_close
        with charachange

        mi "You can pick it out~!"

        hi "You can't just pick out pralin; don't be silly."

        show mishashort perky_smile_close
        with charachange

        "Even if I could, Misha is mashing her food together to the point where it is no longer possible. It also looks kind of gross."

        "I wonder if that many flavors can even blend together well. Can she really taste anything in that goop? She is acting like it's delicious, anyway."

        show mishashort hips_grin_close
        with charachange

        mi "Mm~. Parfaits are the best~, I have sensitive teeth, so ice cream is a no-no~. Cake is too soft, though, and if there is too much icing, I get bored. Parfait is interesting."

        show mishashort perky_smile_close
        with charachange

        mi "How many cafés have parfaits here~? I think, ten! I've tried them all, I like this one the best. It has a little flan~!"

        hi "You sound like you're some kind of dessert expert."

        show mishashort hips_smile_close
        with charachange

        mi "Not just dessert~! I want to eat all kinds of delicious things~."

        show mishashort hips_grin_close
        with charachange

        mi "Someday, I'll have enough money to buy a two kilogram Matsusaka beef steak~!"

        hi "That's like over a hundred thousand yen… I guess this kind of decadent food is kind of your hobby then, huh?"

        "A hobby isn't something that should take months to learn about someone. I've been very rude, in retrospect. Also, that is one pricey hobby."

        show mishashort perky_confused_close
        with charachange

        mi "I guess so~! …Decadent~?"

        hi "Yeah."

        show mishashort hips_grin_close
        with charachange

        "Misha giggles, raising her hand to her face. It looks like some ice cream accidentally got on her nose. She doesn't notice it. I can't stop noticing it. I wish she would wipe it off. I'm about to tell her about it, but she suddenly says,"

        show mishashort perky_confused_close
        with charachange

        mi "I don't know what that means."

        hi "Oh. I guess that's a bad word, anyway. It has implications. Epicurean is better. It means, someone who enjoys eating nice food. That's the adjective, though. So, epicure is the word for it."

        show mishashort cross_laugh_close
        with charachange

        mi "Wahaha~!"

        show mishashort cross_grin_close
        with charachange

        mi "Hicchan, you're too wordy."

        hi "Sorry."

        show mishashort perky_smile_close
        with charachange

        mi "Hahaha~. I think that is what Shicchan likes about you."

        hi "Because I'm wordy? I need to buy some thesauruses, then."

        show mishashort hips_grin_close
        with charachange

        mi "Wahaha~! No, not like that, Hicchan~!"

        "I decide to order some coffee after all, but it takes a while to get the waitress to notice, and I think actually getting my coffee will take about as long."

        "The tea shop is filling up. No surprise, as we've already been here for almost an hour while she was chipping at that dessert. I order my coffee to go, but Misha orders one as well, so it seems that we're going to be here longer than I thought."

        hi "I really wish it was that easy. It's hard to talk to her lately."

        show mishashort sign_smile_close
        with charachange

        mi "Shicchan's been busy because of the elections~!"

        hi "I know we can't have fun all the time. It's just that there's a lot I want to say to her, I think. I always screw up when the time comes, though. And I don't even have the time now. Because of the elections."

        hi "They're not for a while, though."

        show mishashort hips_frown_close
        with charachange

        mi "Hicchan, do you think that Shicchan is avoiding you?"

        "Misha sounds angry. That's to be expected, but I don't feel that way at all."

        hi "No."

        show mishashort perky_sad_close
        with charachange

        mi "Is that so~…"

        "The dreamy way in which she says it makes me think that Misha is disappointed with my answer. In that case, it could be how she feels. I'm uneasy asking such a question, but I trust Misha would answer it honestly. Otherwise, I wouldn't even dream of it."

        hi "Do you?"

        show mishashort hips_smile_close
        with charachange

        mi "No, of course not, Hicchan~! But~! …It's frustrating, sometimes~. Shicchan has so much energy, and is always trying to make people feel as excited about things as she is~."

        show mishashort perky_sad_close
        with charachange

        mi "But it's like Shicchan doesn't know how to handle things when everyone gets really hyped up. Or~! I think that she wants to make sure nothing goes wrong. When I want to help out, Shicchan always pushes me away."

        mi "It's frustrating."

        show mishashort hips_grin_close
        with charachange

        mi "I'm just overthinking it, probably~! Right~?"

        "Misha takes a big gulp from her cup of coffee, then sticks her tongue out."

        show mishashort hips_laugh_close
        with charachange

        mi "Ow~! Hot~ hot~ hot~… thought it would have cooled down by now~!"

        hi "Has it really been that long?"

        "I check my watch. It hasn't been very long at all, but looking outside, the sun is already starting to set."

        hi "Not really. Huh, it got dark out pretty quickly today, though, so I could understand why you might think that."

        show mishashort perky_sad_close
        with charachange

        "At my words, Misha looks outside and yawns almost immediately. She looks sleepy. That's funny, because…"

        hi "Are you sleepy? You were wide awake like, just two seconds ago."

        show mishashort sign_sad_close
        with charachange

        mi "I feel tired when it gets dark, Hicchan~."

        hi "Just like that? Are you a bird?"

        show mishashort perky_smile_close
        with charachange

        mi "Ahahaha~."

        "I pick up my own coffee and have a sip. It's not very hot at all, but very tasty. I down it as quickly as possible, because now I want to get back to my dorm room as well. Misha tries to emulate me, but it's still too hot for her."

        "While I wait for her to finish, I start to wonder what she meant back then about Shizune liking something about me. Suddenly, I'm very curious, but dragging that back up now feels like an unnecessary action."

        show mishashort hips_grin_close
        play sound sfx_impact
        with vpunch

        "I try to weigh the option again, but am interrupted by Misha slamming her empty cardboard cup down on the table with a loud pop."

        show mishashort cross_grin_close
        with charachange

        mi "Done~!"

        "She lets out a short laugh, seeming very pleased with herself. Kind of like a toddler. I wonder if she had that drill-shaped haircut when she was little, too. Or was it something more like her current look? It would make more sense."

        hi "I guess we should head back then. I can't see the waitress. Try not to fall asleep while I pay for the sundae, okay?"

        show mishashort sign_smile_close
        with charachange

        mi "Not a sundae; It's a parfait, Hicchan."

        show mishashort cross_laugh_close
        with charachange

        mi "Wahaha~."

        hi "You have ice cream on your nose."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .acute_triangle:
        scene bg school_scienceroom at right
        with locationchange

        play sound sfx_paper
        play music music_normal fadein 3.0

        "In class the next afternoon, I'm two problems into a math logic worksheet when a folded up piece of paper hits me in the head. I'm sure I know whom it's from, but I quickly look around the classroom anyway, just in case."

        show shizu behind_blank:
            left alpha 0.0
            ease 1.0 center alpha 1.0
        with None

        show bg at left
        with charamovefaster

        "No one in this classroom is good at acting casual. I can tell that everyone saw who threw it at me, and looking at the culprit herself it was obviously Shizune. She isn't even trying to be coy about it."

        "The countryside is so different. At my old school I would have no idea who it was right now."

        "Opening up the note, it says:"

        call screen written_note(_("Misha is absent! Help me out today after school!"))

        hi "I don't understand what's with the note, why can't you just use sign language?"

        "A large part of how I learned sign language was by copying Misha's style of signing her words as she speaks, so I end up blurting the sentence out loud as I sign it to Shizune. A slight laugh goes around the room. How awkward."

        his "I'll help if I don't have to do a lot."

        show shizu basic_angry
        with charachange

        ssh "That's silly, obviously if Misha is absent you have to help as much as two people."

        "I don't know if that really means anything. After all, Misha was complaining yesterday mostly about how Shizune wouldn't let her help her. I don't do much as-is, either."

        "After pretending to think it over for a bit, I write her a note back telling her I will. I'm actually happy that she asked me, because I've been meaning to talk to her for a while."

        "It's a good opportunity, but I feel I should at least make it look like I'm putting up some resistance to the idea."

        hide shizu
        with charaexit

        "I go back to my worksheet and immediately get stuck on the third problem. After trying to work around it, I casually toss my own note over to Shizune. It says:"

        call screen written_note(_("Why is Misha absent? And what's the answer to question 3?"))

        show shizu behind_blank at center
        with charaenter

        ssh "She told me that she was sick and her stomach hurt. Misha gets stomachaches a lot, but I wish she'd picked a better time for it this week."

        show shizu basic_normal2
        with charachange

        ssh "Use sign language."

        "I'd think she has a stomachache because of the way she sucked down a parfait larger than her head the other day."

        "If she gets them quite often, though, either it's a coincidence or she has a habit of eating things that can put her in debilitating pain."

        "I notice the teacher staring at us disapprovingly. I don't blame him. We're 'talking' in class, and with sign language, in quite a visible and distracting way. I try clearing my throat to back out of our conversation, but Shizune doesn't get the hint."

        "Well, obviously. Before I try to get the message across again with my hands, however, I can see Shizune notices what's up, she just doesn't care."

        show shizu adjust_smug
        with charachange

        ssh "Do you still want to know the answer to question 3? I will tell you, but you have to give me the answer for question 25."

        his "Hey, I was just thinking about how a teacher who didn't know sign language could think we were abusing it and using it to cheat, if he were to assume the worst. I can't believe you're actually doing that! And, I'm not up to 25."

        show shizu behind_frown
        with charachange

        ssh "You wanted to know what the answer to 3 was; you asked first. Hypocrite."

        his "You're the Student Council president, you can't cheat."

        "I don't have time for this, and I think I'm trying the teacher's patience to the breaking point. I'd like to continue taking potshots at her while working on the math problems in front of me, but it would require at least two extra hands."

        show shizu basic_normal
        with charachange

        "Shizune is a bit more creative, and gets around this limitation by using long, semi-broken strings of simpler words. I take a couple mental notes in between being dizzied by a couple of particularly long equations."

        show shizu adjust_smug
        with charachange

        play sound sfx_impact2
        with vpunch

        "Right before the bell rings, she caps her pen and triumphantly slams it on her desk with an ear-popping crack that makes the whole room jump, quickly forgotten because everyone would rather go to lunch than question its origin."

        stop music fadeout 6.0

        show shizu basic_normal_close at twoleft
        with characlose

        "After a couple brief stretches, she gets up and hovers around my left shoulder."

        show shizu behind_frown_close
        with charachange

        ssh "Are you still not done? I was going to ask if you wanted me to hand in yours too, while I was up."

        his "Someone distracted me. I had to beg the teacher to give me nine minutes between now and the end of passing to finish it. It's not easy to solve this one-handed while having a conversation, by the way."

        "He wasn't happy with the request, wanting to get out of here as much as I do."

        "Since I'm only one problem away from finishing, it looks like Shizune doesn't really believe me. The second that I'm done handing it in, I find myself being dragged to the student council room."

        scene bg school_council
        with locationskip

        play music music_happiness fadein 2.0

        "It's eerily and annoyingly clean. I can't find what I was working on yesterday."

        his "Where is everything?"

        show shizu behind_blank at center
        with charaenter

        ssh "I did some cleaning."

        his "That doesn't tell me anything. See, it's like you forgot where you even put the stuff you put away. Oh well, If I can't find it, I guess I'll just go home."

        show shizu basic_normal2
        with charachange

        ssh "It's in the drawer right there."

        "Shizune sulks as I pull out the posters I was working on, and then shuffle them around a little, since she stacked them by color. It's not that I'm taunting her; I just have my own system, although I doubt she would believe me if I were to tell her."

        his "I like it when things are a little messy. It's more natural. And a time saver. It's all right where I left it, and I don't have to go looking through shelves just to find what I was working on yesterday."

        show shizu adjust_frown
        with charachange

        ssh "Lazy."

        his "That's not true. I'm not lazy, you just always go too far."

        "I quickly glance at her desk. A memo pad neatly placed at one corner, behind it a small desk calendar with each box filled with notes in a neat, but microscopic handwriting. On the right, three boxes of pens, in blue, black, and red."

        his "Look, you even put the pens back in their original box at the end of each day, all color-coded and everything. I don't think that can even be called being a neat freak."

        show shizu behind_frown
        with charachange

        ssh "What do you do with them, throw them in a mug on your desk?"

        his "Hey, I think that's being organized enough."

        show shizu basic_frown
        with charachange

        ssh "You're so disorganized, you can't even comb your hair down properly."

        his "That hurts…"

        "It's not like I don't try; it just won't stay flat. I pick up a box of pens and quickly pop it open to see if she also puts them in so that they're all facing the same direction. She understands what I'm thinking, and doesn't look very amused."

        play sound sfx_dropstuff

        "It turns out that the box wasn't closed properly on the bottom, and as soon as I pick it up, they immediately pour out of it like a waterfall."

        his "My fault. I'll get them, don't worry."

        stop music fadeout 4.0
        play sound sfx_impact

        show shizu adjust_blush_close
        with vpunch

        "I bend down to pick up the pens, forgetting that with her attention focused on them, she couldn't have possibly seen me signing to her. Shizune's head bumps into my chest; not very hard, but it unbalances me enough to make me fall over."

        show shizu adjust_blush
        with charadistant

        "I laugh it off, and expect her to do the same. When she stiffens and backs away from me instead, a feeling of dread begins to creep over me."

        "That is a weird reaction. I start to think about why she would have such a strange reaction. It's pretty obvious: she just bumped headfirst into someone with a heart condition."

        if not side_lilly and wait_for_shizu or _in_replay:
            "Shizune would know I have one, having seen the rows and rows of pills lining the edge of my dresser. Or at the very least, she would know I have something severe enough to require that much medication, but not visible at a glance."
        else:
            "Shizune would know I have one, maybe thanks to the records her student council duties give her access to. Or at the very least, she would know I have something severe enough to need monitoring."

        "So she is treating me like I'm made of glass. For her, it's the natural way to react. I haven't forgotten how she freaked out back when Emi knocked into me. Why would it be any different for her?"

        show shizu basic_normal
        with charachange

        "I'm sure she is remembering that, right now. I can see it on her face. She looks angry at herself."

        "It would be a good opportunity to bring up that time. Even though I don't want to drag that back up, it would be a good idea to. It would clear the air."

        "Still, I'm afraid, and end up saying nothing. Partly because as I imagine having to draw her attention from the floor, and then having to sign what kind of a cripple I am to her one gesture at a time, the idea begins to seem more and more depressing."

        hide shizu
        with charaexit

        "Taking a seat, I decide to just try and finish up these posters to get my mind off of it. There are some that I don't remember making. From the wall-to-wall text and ultra-neat handwriting, I can tell Shizune must have done these."

        "That means that the remainder must have been done by Misha. They are a lot more visual, with cute little stylized pictures of us on them. I don't know how I feel about being used as a mascot character, but I'm not really thrilled by it."

        scene bg school_council_ss
        with shorttimeskip

        play music music_tranquil fadein 3.0

        "Some time passes; long enough for the sun to start setting. I hear Shizune putting down her pen and cracking her knuckles methodically, one at a time. It's so loud in the silence of the room that I look up, wondering if she is trying to get my attention."

        show shizu behind_blank_ss
        with charaenter

        "Although it wasn't what she intended, when she notices me looking at her, Shizune begins to sign without skipping a beat."

        show shizu basic_normal_ss
        with charachange

        ssh "Let's take a break."

        his "I'm surprised you would say that."

        show shizu adjust_happy_ss
        with charachange

        ssh "It's okay. I'm almost done, anyway. And I'm hungry. Aren't you?"

        his "A little."

        show shizu basic_normal2_ss
        with charachange

        ssh "I'm really hungry."

        his "We could order something."

        show shizu behind_smile_ss
        with charachange

        ssh "I was thinking of you. I already have something to eat."

        his "Where?"

        show shizu adjust_smug_ss
        with charachange

        "She produces a cinnamon bun from under her desk, raising it to head level slowly, like a magician levitating a rock."

        show shizu behind_smile_ss
        with charachange

        ssh "But!"

        show shizu basic_sparkle_ss
        with charachange

        ssh "There is only one. Not enough for both of us."

        "Ah, how dramatic. I can tell what this means. A feeling of déjà vu briefly washes over me."

        his "We could just split it."

        show shizu adjust_frown_ss
        with charachange

        ssh "That's. No. Fun. So boring. Let's play shogi for it."

        "She already has the board out. That desk must have everything in it."

        his "Not chess?"

        show shizu behind_smile_ss
        with charachange

        ssh "Chess has boring promotions, this is better."

        his "I don't know about that. Well, I'm actually pretty decent at shogi, so this is fine."

        show shizu basic_happy_ss
        with charachange

        ssh "Is that so? Okay, we can make it a little more interesting, then. Each move has to be completed in thirty seconds. You can add a rule, too."

        his "No thanks, anything I could add would only hurt me more than it would help. A thirty-second time limit is already too tight for me."

        his "You're making me regret thinking it was all right to brag a little."

        scene bg school_council_ss
        show shizu basic_normal_close_ss at center
        with shorttimeskip

        "After Shizune wins the right to go first in a quick coin toss, she immediately starts playing with the aim of promoting all of her pieces as soon as possible. It seems like a very basic playstyle, and I can't help thinking it might be a trap of some sort."

        "It's not, though. The draw of this game to Shizune appears to be the fact that she can upgrade her pieces, and steal mine. She's very good at it, but it makes her predictable. I end up doing a little better than I'd expected to."

        "The 30-second time limit is pretty painful, though. The game ends in a draw. At this point, I think you're supposed to either go for a rematch or tally the pieces for points."

        "Shizune doesn't want to go again in the interest of time, but winning on points clearly doesn't satisfy her."

        show shizu adjust_frown_close_ss
        with charachange

        stop music fadeout 4.0

        "She sits there, shifting a silver general from one edge to the other as she contemplates which of those two options she'll go for. It takes so long that I think she has forgotten about the bet."

        "Eventually, she stops fiddling with the shogi piece and puts it down."

        show shizu behind_blank_close_ss
        with charachange

        ssh "Is Misha angry at me?"

        "That really came out of nowhere."

        play music music_pearly fadein 5.0

        "Shizune's frankness is disorienting, because with her, any kind of candor is a sign of total seriousness. There is no playful smile on her face, instead it's her usual stoic mask of concentration, ready to try and see if I'm about to tell her the truth."

        "I'm upset that she thinks that I would tell her anything else, but I also know now that they have probably fought recently, out of my sight, and it makes me feel warm to know that they both care about each other so much."

        his "No. I strongly doubt it."

        his "Did you know that she thinks you're angry at her?"

        show shizu behind_sad_close_ss
        with charachange

        "Shizune nods slowly and uncomfortably."

        show shizu basic_normal2_close_ss
        with charachange

        ssh "Yes."

        his "She was more roundabout with the question than you. Kind of surprising, because I thought that you were the one who liked playing games."

        show shizu behind_blank_close_ss
        with charachange

        ssh "Not all the time."

        "…"

        his "Are you two having some kind of fight?"

        show shizu adjust_frown_close_ss
        with charachange

        ssh "No."

        "She is very quick to deny it, and not happy with the thought. I feel like I've stepped on a landmine."

        show shizu behind_sad_close_ss
        with charachange

        ssh "Sorry. Actually, yes. Just a tiny one."

        show shizu behind_blank_close_ss
        with charachange

        ssh "I know that she has no interest in the Student Council. She only joined because of me. I'm still grateful. I'm so happy she's my friend. But I don't understand what she is upset about this time."

        his "Why don't you just ask her?"

        show shizu basic_normal2_close_ss
        with charachange

        ssh "She won't tell me. I'll figure it out by myself, instead. I was sure that I was very perceptive, even if I can't hear. That was dumb. I know better now."

        show shizu behind_sad_close_ss
        with charachange

        ssh "It is probably something that is my fault."

        stop music fadeout 8.0

        "Shizune doesn't elaborate further on what it could have been. I'm sure that it is because she does not fully understand the situation herself."

        "It's odd to think that Shizune, usually so sure of everything, could be scared by a little argument with a friend. But the more I think about it, the more it makes sense."

        "They're a lot closer to each other than normal friends, and Shizune is pretty isolated from other people, in a way. The fact that she is deaf is no small part of it."

        "But I get the feeling that she uses Misha as a buffer between other people of her own will, not just because it's been forced onto her. She can communicate well enough with her little pad. She just hates it."

        "After such a long time of talking through another person, I guess you start to lose touch. It seems unavoidable. It isn't such a far-out idea to think that she isn't that great with people."

        hide shizu
        with charaexit

        "I return to working, kind of wanting to eat that cinnamon bun more as time drags on, but when I count the shogi pieces still left out on Shizune's table, I can tell at a glance she would win."

        "I'm also too hungry to concentrate if we were to have a rematch. Motivated by my desire to wrap up and eat something, I put the finishing touches on the last of the posters."

        his "Done. I think this many is enough. Too many can be a bad thing."

        play music music_shizune fadein 3.0

        show shizu behind_blank_ss at center
        with charaenter

        ssh "Okay."

        his "That's it? Just 'okay?'"

        show shizu adjust_frown_ss
        with charachange

        shi "…?"

        show shizu behind_blank_ss
        with charachange

        ssh "…I'll probably do some myself, after I'm done picking what voting format to go with."

        his "Arrgghh. Too many posters is bad, too. Haven't you ever heard of oversaturation?"

        his "I really think you're trying too hard."

        show shizu basic_normal_ss
        with charachange

        "Tenting her fingers, Shizune looks like she could almost admit it."

        show shizu behind_blank_ss
        with charachange

        ssh "Maybe."

        his "It's what Misha thinks, too."

        show shizu basic_normal2_ss
        with charachange

        "I watch as her fingers continue uneasily twining around and pulling at each other in a miniature tug-of-war."

        his "I don't mind, but I asked around in a couple classes today and interest is low. It's like you said. So…"

        show shizu adjust_frown_ss
        with charachange

        ssh "Does that make it wrong?"

        his "No. But… it does make it kind of pointless."

        show shizu basic_angry_ss
        with charachange

        ssh "It's not."

        "Yeah, but to who? I doubt even Shizune truly believes that."

        show shizu behind_frustrated_ss
        with charachange

        ssh "I'm not doing all this work just for my own ego."

        his "That isn't what I mean."

        "The first chance to be alone with her in days, and I have already really cocked it up. Still, she doesn't actually look angry."

        "It's more like she's frustrated that she can't express herself clearly enough. Since she's an expert in sign language, I wouldn't think that would be the case."

        "I wonder what advantage being able to speak would offer her, and if she has ever thought about it."

        show shizu basic_frown_ss
        with charachange

        ssh "It's another project of mine. Just like the festivals. I'm going to do it, because it's my job. It's just that a student council election isn't as fun as a festival, so no one cares."

        "She briefly touches her fingertips together, as if to say 'but, maybe…' There is some truth to it, but Shizune doesn't want to say anything that could be boiled down into something so glib."

        show shizu behind_frown_ss
        with charachange

        ssh "But I don't care. I want to get people riled up, but it isn't about me. I don't want to be involved at all."

        his "What do you mean? You go to like, every single festival."

        show shizu adjust_frown_ss
        with charachange

        "Shizune waves her hand in mock indignation."

        show shizu behind_blank_ss
        with charachange

        ssh "Well… I have to have fun, too. But you know, it's not the same thing."

        "Her spirits seem to have improved, if she can manage to crack a joke."

        show shizu basic_normal2_ss
        with charachange

        ssh "I don't want anyone to make a point of me being involved. It's a hassle. I don't want that responsibility."

        show shizu adjust_frown_ss
        with charachange

        ssh "Things are becoming too complicated now as-is. The more I try to hype up the elections, the more involved I have to be. No one wants to play their hand yet, and it doesn't feel like my time is over, even though it should."

        show shizu behind_frustrated_ss
        with charachange

        "Crossing her arms and leaning back, she grinds her teeth together in frustration."

        show shizu cross_angry_ss
        with charachange

        ssh "They're all so lazy; it's impossible to get them to do anything. Anywhere else, the elections would be an exciting event. It's illogical, why does everyone have to be so different? If only there was some way to punish them…"

        show shizu adjust_angry_ss
        with charachange

        ssh "…Like chaining the school to their desks. Voting is mandatory. If you don't vote, you get whipped."

        "Terrifying. I wonder how hypocritical it would be if I were to stay in bed on election day. With the flu. And a cold. And strep throat. And a sprained ankle."

        his "You should put yourself on one of these."

        his "Not as punishment. Don't misunderstand."

        "I hold up one of Misha's posters."

        his "Like this. It's kind of a neat idea. Misha was on to something. It's a lot cuter than just text. I'd think you would like it. Having cute mascots would drum up some excitement."

        show shizu basic_normal_ss
        with charachange

        ssh "Maybe if it's just Misha."

        his "Why not me? Someone told me that this school has slightly more girls than boys… you have to cater to that demographic, too."

        show shizu adjust_blush_ss
        with charachange

        "Shizune giggles, audibly this time. I'm surprised, and when she sees my face, so is she. Her face flushes pink, embarrassed to have let out a sound. Which is really confusing, to say the least."

        his "Why don't you put yourself on it?"

        "She just waves my question away."

        show shizu basic_angry_ss
        with charachange

        ssh "It's troublesome."

        his "What do you mean, troublesome? Everyone knows that you're in the Student Council."

        "My stomach growls, making me realize that I'm hungrier than I'd thought. Shizune uses the moment to deflect my question by changing the subject."

        show shizu behind_blank_ss
        with charachange

        ssh "Is something wrong?"

        his "No. My stomach growled."

        show shizu basic_normal_ss
        with charachange

        ssh "I see."

        "She looks at the forgotten pastry on her desk then frowns, finding it inadequate for two people."

        show shizu adjust_happy_ss
        with charachange

        ssh "Let's go to the Shanghai, if you are that hungry. It might be a little busy this late, but Yuuko is working there today. We will definitely get a table."

        "There is something worryingly underhanded in that smile."

        his "I'll pass. I've already been there twice this week, back to back."

        show shizu basic_frown_ss
        with charachange

        "Shizune pouts, leaning back against her desk and scrunching up her posture in protest."

        his "What?"

        show shizu adjust_frown_ss
        with charachange

        ssh "I'm disappointed you said no."

        his "Well, I can't agree with you on everything."

        show shizu behind_frown_ss
        with charachange

        ssh "You don't give your opinion often enough, anyway. It would be easiest for me if it was like that, but not very interesting, right? There are some decisions you should disagree with me on, then. You have a duty to."

        his "How am I supposed to know which is which?"

        show shizu basic_normal_ss
        with charachange

        ssh "It's easy."

        his "No, it's not. Sometimes it's hard for me to tell whether you're joking or serious."

        stop music fadeout 9.0

        "Although, since she communicates entirely in sign language, that would seem pretty obvious. I wouldn't say that that's all there is to it, though."

        "I remember when I had my heart attack, Iwanako wouldn't stop talking, at first. Eventually, I wished that she would just shut up. Or I would have, if I hadn't been happy to have any kind of company at all. Gradually, I stopped being so grateful."

        "When we talked, I felt like it was nothing more than ritualized exchanges of politeness. Iwanako tried extremely hard to obfuscate how she felt, which was that I was hopeless. In the end, her outer behavior matched her inner feelings."

        "For that reason, I was able to accept it when one day she stopped showing up. I was no longer surprised by the time it happened. Even though she considered herself a master at hiding her feelings, I was not surprised."

        "I've heard that games like shogi and chess can tell you a lot about a person. I wish I knew what Shizune thought they said about me."

        "It could be that I'm a little more like Iwanako than I'd like to think, if I can only tie with Shizune by retreating. I suggest that we should order out."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .dewey_decimated:
        scene bg school_hallway2
        with locationchange

        "The next day, I walk up to my usual vending machine at lunch only to find that it's out of my favorite drink. Secreted so far away from most of the classrooms, between a storeroom and the library, it's like no one knew about it."

        "I'd expected a vending machine so close to the library to be booming with customers, but then again, the library is empty most of the time, and anyone who goes there is only doing it to look for stuff to pad a paper with."

        "No one stays there longer than they absolutely have to. For the past month, it's been working out in my favor, but the trade-off with a vending machine no one knows about is that it's never restocked."

        play sound sfx_can

        "Settling for a can of orange soda, I decide on drinking it here instead of waiting until I get to the cafeteria, when the library door opens next to me."

        show yuuko worried_down at center
        with charaenter

        yu "Ah…"

        show yuuko worried_up
        with charachange

        yu "I've been looking for you!"

        play music music_happiness fadein 2.0

        "Yuuko seems to be acting a lot more assertive than usual today, although it isn't enough to keep her from going back to mumbling immediately afterwards."

        show yuuko worried_down
        with charachange

        yu "R-return your books, please. I mean… the library's books. The books you checked out are really overdue. Some of them are on waiting lists…"

        hi "Oops. I forgot. I keep checking out new ones, and forget the return the old ones."

        show yuuko neurotic_up
        with charachange

        yu "That happens to me all the time at the university library, it's so embarrassing."

        hi "Do they send someone to try and get you to bring them back?"

        show yuuko worried_up
        with charachange

        yu "No… The university library is bigger, they don't notice if I happen to borrow something longer than normal. It's convenient, because their policy on keeping the books too long is… really strict, stricter than here…"

        "I like how despite what she said, Yuuko has no problem with borrowing books for longer than she is supposed to anyway. It makes her being so on top of my own lateness a little hypocritical. It takes a thief, I guess."

        "Catching on to the meaning of her words around the same time I do, Yuuko clams up and starts backpedaling furiously."

        show yuuko panic_up
        with charachange

        yu "…Um… ah… That's different… from this situation! It's totally different…"

        "Yuuko stares at her nails for a second as if she really wants to bite them, but is too self-conscious to do so."

        show yuuko worried_down
        with charachange

        yu "For instance, how long it's been… You checked out some of these books months ago, Hisao. Sorry… It's just that, other people want to read them, too. If you're a slow reader, that's okay, though…"

        hi "No, it's a total screw-up on my part. To be honest, I haven't even read some of them. I shouldn't keep taking out books when I have a backlog."

        yu "That's not good…"

        hi "Yeah, it really isn't…"

        "Now I'm starting to copy her habit of trailing off quietly. Her awkwardness is very contagious, for some reason."

        "That said, I'm surprised. Yuuko seems almost normal today, although every now and then, her waitress-y nervous tics keep popping back up."

        "Come to think of it, she didn't act this way when I first met her. She was a little clumsy and neurotic, but it wasn't anywhere near this severe until Shizune, Misha, and I ran into her at the Shanghai."

        "It could be that Yuuko has a complex about having kids from the school seeing her waitressing."

        "I guess it was a little odd for her to pick the closest café to the school to work in, then. In that case, maybe the place having so few customers could be considered a lucky break."

        hi "Well, I get it. I'll return them right after school."

        show yuuko smile_up
        with charachange

        yu "As soon as possible, please."

        show yuuko worried_up
        with charachange

        yu "Um… wait, can I ask you for one more thing?"

        hi "Sure, what is it?"

        show yuuko worried_down
        with charachange

        yu "I… I have to go for a while, but I can't just leave the library empty… Sorry, but can I ask you to watch it while I'm gone? Just for a little bit, I'll be right back as soon as possible! You're in the Student Council, so I'm sure if you did it, it would be okay."

        hi "All right, I'll do it, don't worry ab—"

        show yuuko closedhappy_up
        with charachange

        yu "Thank you!"

        show yuuko neurotic_up
        with vpunch

        "Yuuko quickly slides forward as if she's so grateful she is about to give me a hug, but she stops two centimeters into it, which ultimately just makes the gesture look extremely confusing."

        "I'm also surprised that she can control her momentum so well, since she seems kind of clumsy."

        hide yuuko
        with charaexit

        stop music fadeout 6.0

        "Before I can say as much as 'You're welcome,' she is already dashing off with the urgency of someone late to an appointment."

        "That could be the case, but I wouldn't feel safe assuming so. It's Yuuko, and she seems like the kind of person to treat everything that way."

        scene bg school_library
        with locationchange

        "Now that I'm in the library, I feel a bit silly. I don't really know what I'm supposed to do. Should I sit down like I normally would and read? It probably would do, but wouldn't meet Yuuko's high standards."

        "Maybe I should sit at the librarian's desk, and give anyone who comes in a stern and analytical glare. I use Shizune's as a starting point, and practice it a couple times in the mirrored surface of a pen."

        "I think it looks pretty good. Frustratingly, no one comes in, so I give up on the idea quickly, and decide to just go looking for Hanako instead."

        "It's deserted. I think I see someone, but the second I blink, whoever it is is gone. As soon as I return to Yuuko's desk and crack open an interesting-looking book, a familiar person swings in front of me like a falling pendulum."

        show kenji tsun:
            center xpos 0.4 alpha 0.0
            ease 1.0 center alpha 1.0

        pause 1.0

        show kenji at center

        play music music_kenji fadein 0.5

        ke "Yo, librarian, I've been looking for you for like, ten minutes. What?! It's you? Man, you must really get around, or the Student Council makes you get around. Those bitches! How could they?"

        show kenji rage
        with charachange

        ke "Slave drivers!"

        "He must be exaggerating, because it took me thirty seconds just to do a slow walk around the whole place. The thought is overridden by my surprise to see him."

        hi "Where did you come from? What are you doing here?"

        show kenji tsun
        with charachange

        ke "What, can't a guy go to the library now? I can't even go to the library without some young buck like you giving me the third degree over it. I see some girl coming in here all the time, but no one ever asks her what she's doing here."

        ke "Is it because she reads and I don't?"

        "He must be talking about Hanako. Although I suppose they both avoid people, I want to tell him that reading is what you usually do in a library. So if he's not reading, whatever he's doing is bound to make him look way more suspicious than her."

        "In the end, though, I'm too surprised by him practically appearing out of thin air."

        hi "That— that doesn't tell me what you are doing here."

        show kenji neutral
        with charachange

        ke "I'm here because of you."

        "His response makes me feel confused. Maybe I fell asleep and this is all just some weird dream, and this Kenji isn't real, but really my subconscious. Is he going to start giving me deep but vaguely-worded advice now?"

        show kenji tsun
        with charachange

        ke "Because of you, I got chased out of my dorm by feminists. Now, I wander this library, like a soldier without a country, or a ghost. I should haunt you, for ruining things for me."

        "It's a shame, it would have been an interesting dream, but it seems like this is the real deal."

        ke "Yeah, you had to start working with women, and that brought them to my door. You remember that? You should, since you were there. After that day, I knew they were on to me. I should have trusted my instincts, but I was young and stupid."

        hi "That wasn't even a week ago."

        ke "Then, my dad called and said one of my letters hadn't been delivered. The post office couldn't have lost it, so it must have been intercepted. Information warfare!"

        show kenji neutral
        with charachange

        ke "That's when I knew my secret hideout was compromised. Now I'm on the run, like a fugitive. It's code red. "

        hi "Dorm rooms aren't secret, they put your name and number on a board right in the doorway."

        show kenji rage
        with charachange

        ke "I know, I saw that. They're diabolical. Why not just put up a big Wild West wanted poster, if they're gonna be like that?! 'Wanted: Dead or Alive!' Probably alive, so they can clone me or turn me into a grasshopper."

        show kenji tsun:
            center
            ypos 1.15
        with Dissolvemove(0.5)

        "Jumping without warning into the empty chair opposite me, Kenji takes out a cigarette and starts spinning it between his fingers. I've never seen him smoking before, so it must be for effect."

        ke "I can't even live where I want to any more. This is where it all begins."

        ke "The tactical brilliance… I mean, once they're in your home, it's over, like termites. If the feminist plan for dominance STARTS there, where the fuck can we go?"

        show kenji happy
        with charachange

        ke "The only question is how they could take a page out of the termite playbook when women are naturally repelled by wood."

        hi "'You can never go home again.' Is that how the saying goes?"

        show kenji neutral
        with charachange

        ke "Man, I don't know about never. I was just there. I don't know anywhere else I can shower and get new clothes. And eat, and use the bathroom. And watch TV. I have to keep watching the news, to keep informed."

        "For someone ousted from his dorm room and living on the run, he sure has no qualms about going back there several times a day for long periods of time."

        "But by now he's slowly turned away from me and is talking to a revolving display of murder mysteries. There's really no point in interrupting him, I guess."

        play sound sfx_can_clatter

        "I finish off my soda and throw the can into the basket near the door. It hits the rim, but goes in anyway. I silently pump my fist."

        show kenji at center
        with charamovefaster

        "Kenji quickly gets up and starts to head towards the door. I wasn't really paying attention; I hope I didn't fist pump at an inappropriate moment."

        hi "Where are you going?"

        show kenji tsun
        with charachange

        ke "You kept sucking down that juice."

        hi "So? It wasn't even juice, it was soda. And it's gone now. And what do you mean, 'sucking it down?' I had two sips."

        ke "Yeah, right, you had like fifty million sips."

        hi "That's not even possible."

        show kenji neutral
        with charachange

        ke "Maybe for you; I go beyond the impossible all the time. Okay, whatever, now I'm thirsty too. I'm going to get my own juice, I'll be right back."

        show kenji:
            ease 1.0 xpos 0.4 alpha 0.0

        pause 1.5

        show kenji:
            ease 1.0 center alpha 1.0

        pause 1.0

        "He does come almost right back, so quickly that I suspect he knows about my secret vending machine."

        ke "I got you one, too. Hope you like grape juice. We're even for the pizza, now."

        hi "Thanks."

        show kenji:
            center
            ypos 1.15
        with charamove

        "I want to tell him that I lent him nearly ten times the cost of a can of grape juice, but that might make me seem petty. Unopposed, Kenji sits down and starts furiously drinking juice like a man with a vendetta against grapes."

        show kenji happy
        with charachange

        ke "You know, it's a lucky break for me that I managed to run into you here, man. I kinda need you to do me a favor."

        "Although it's cynical, I wonder if him getting me juice was so he could ask me for this favor. If so, it's very transparent, and poorly timed. I doubt Kenji would think about something so deeply, though. Just asking for things straight out is more his style."

        ke "I need you to recommend me some books."

        hi "But I thought you didn't read."

        show kenji neutral
        with charachange

        ke "How did you know?"

        hi "You told me. You said you think people discriminate against you because you don't read."

        show kenji happy
        with charachange

        ke "Well, they do. And I do read, I read audio books, because that's the way of the future."

        show kenji neutral
        with charachange

        ke "I have to read a book a month for Literary Studies, though, and I found out that the school doesn't really accept such classics as 'Advanced Cryptography.' If I don't read a bunch of books, they're gonna fail me."

        show kenji tsun
        with charachange

        ke "I can't fail Literary Studies… that would make me illiterate. That would mean my mom was right. My mom can't be right. I'll just have to study literacy as much as possible."

        hi "What about doing some extra credit?"

        ke "No thanks. It's bad enough I'm gonna have to carry around these stupid things now."

        "He picks up a dictionary, flips through it, and places it on the murder mystery rack behind him."

        ke "I can't believe this is actually the medium that our ancestors used to look at porn."

        "I spit my drink all over the book I'm still holding, damaging it beyond any hope of repair. I quickly check the back and see its suggested retail price is 7900 yen. I think I might have a heart attack."

        show kenji happy
        with charachange

        ke "Wow, destroyed. Shouldn't have done that, though, they take vandalism super seriously here. You're gonna get caned."

        "He chortles, amused, before taking an extremely long, loud sip from his can of juice."

        hi "It's not vandalism, I didn't do it on purpose. You made me do it, with your words."

        hi "And what do you mean caned? I don't want to be caned."

        show kenji neutral
        with charachange

        ke "Wait, chill out, I didn't mean they actually cane you, they just make you pay for it, and really, really yell at you. It's like they were going to bite my ass off. Still not that big a deal."

        hi "I don't care if it's figurative, I don't want to get caned, or get my ass bitten off, or any kind of punishment, you… you dumbass."

        hi "What am I going to do? I'm the only person in here. That she knows of, anyway. I can't even throw the book in the trash. It will be found. Then she'll know."

        show kenji tsun
        with charachange

        ke "Damn, dude, stop being so weird."

        hi "How is it weird to not want to be fined?"

        ke "Man, stop flipping out, man."

        hi "I'm not flipping out, I'm trying to save money."

        ke "So cheap."

        show kenji:
            ease 0.5 center alpha 0.0

        pause 0.5

        hide kenji

        stop music fadeout 1.0

        "I'm about to strangle him when I hear Misha's 'wahaha' coming up the hallway. Apparently, Kenji hears it too, and uses the opportunity to quickly vanish behind the autobiography section. Like the wind."

        show mishashort hips_grin at center
        with charaenter

        play music music_comedy fadein 0.5

        mi "Hi, Hicchan~!"

        show bg at bgleft
        show mishashort at twoleft
        with charamove

        show yuuko neurotic_down at tworight
        with charaenter

        "Misha shouts exuberantly, dragging an embarrassed Yuuko behind her."

        show mishashort sign_confused
        with charachange

        mi "Hicchan~! Were you talking to yourself?"

        "On one hand, saying yes could make me look kind of crazy. On the other hand, if I blow Kenji's cover, he might go off and make me look crazy by association."

        hi "Yes."

        show mishashort cross_grin
        with charachange

        mi "Ahaha~! That's okay~! Don't be embarrassed, Hicchan; I do it too, sometimes, when I'm alone! La~ la~ la~."

        show yuuko worried_up
        with charachange

        yu "Um… nothing happened while I was gone?"

        hi "Absolutely nothing."

        show yuuko worried_down
        with charachange

        yu "It smells like… grapes."

        hi "I'm wearing grape-scented cologne."

        "I lie brazenly and obviously. From her reaction, I'm going to assume that she knows I'm lying, or thinks I have an abysmal sense for colognes."

        "Since the can of grape juice I drank from is still right there, it's likely to be the former. Fortunately, she doesn't ask any follow-up questions."

        hi "What are you two doing together?"

        show mishashort sign_smile
        with charachange

        mi "We had lunch together~! Strictly business, a business lunch~!"

        "I try to picture Misha in a suit, having a business lunch with anyone. Somehow, I just can't see it."

        hi "What kind of business?"

        show yuuko panic_up
        with charachange

        yu "You don't know?"

        show mishashort hips_grin
        with charachange

        mi "Ahaha~! It's nothing~, nothing~. It's normal for one part of the Student Council to not know what the other is doing~!"

        hi "Hey, don't 'nothing, nothing' something like that. That isn't normal at all. In fact, it's bad. We're only three people."

        show yuuko neurotic_up
        with charachange

        "Yuuko laughs nervously. She must be terrified."

        show yuuko worried_down
        with charachange

        yu "Misha says that you want to put posters in the library… for the elections. Um… even though they are really far away, I guess it's okay. I didn't know that I could even decide those kinds of things…"

        show mishashort cross_laugh
        with charachange

        mi "You can~! Isn't that great~? Ahaha~! Aren't you happy? Yay~ yay~!"

        show yuuko panic_up
        with vpunch

        "Misha grabs Yuuko's hands and forces her to clap joyously for herself. Yuuko doesn't look very happy about learning that she has more responsibility and power than she'd previously thought."

        show mishashort sign_smile
        with charachange

        mi "Hicchan~! Since you're here, you can help me put them up!"

        "Pulling out a giant stack of posters from her bag, she cuts them in half like a deck of cards and passes me the slightly smushed half."

        show mishashort hips_smile
        with charachange

        mi "Shicchan had a really good idea~! We can put some flyers inside books, too~! Then, even if they try to ignore us, they won't be able to! They could even be spring loaded!"

        "Misha tries her best to convey the same tone Shizune used. It sounds close to the real thing, and also a little menacing."

        hi "She was probably kidding."

        show mishashort perky_confused
        with charachange

        mi "I liked it~."

        show yuuko cry_up
        with charachange

        yu "N-no… please… not that…"

        show mishashort cross_smile
        with charachange

        mi "A super ultra aggressive marketing blitz~! We're going to start going door to door, too~!"

        hi "That's a terrible idea."

        show mishashort cross_frown
        with charachange

        "Misha pouts in her best Shizune impression, fingertips tapping together rapidly in annoyance."

        mi "Hicchan~! You think every idea is terrible…"

        hi "Yeah, but that idea is too terrible, too terrible to ignore. I can't have that."

        show mishashort hips_smile
        with charachange

        mi "Wahaha~! Hicchan, that sounds like a challenge. Mutiny~, mutiny~!"

        show yuuko cry_down
        with charachange

        yu "M-mutiny is bad… Don't fight."

        show mishashort hips_grin
        with charachange

        mi "Wahaha~! It was just a joke~!"

        show yuuko worried_down
        with charachange

        yu "Okay…"

        show yuuko worried_up
        with charachange

        yu "Don't fight."

        show mishashort cross_laugh
        with charachange

        mi "Aha~ ha~ ha~."

        "The way Yuuko sounds when she's trying to be firm makes me think of a kindergarten teacher. I suppose that makes her very persuasive in her own way."

        hide mishashort
        hide yuuko
        with charaexit

        stop music fadeout 5.0

        "Putting up the posters is surprisingly hard, simply because the library is already plastered with bulletin boards and flyers lining every couple meters, some of them in places so unlikely that I'd never noticed them before."

        play sound sfx_warningbell

        "Deciding which of them to peel off in favor of our own adds a lot of time to an otherwise simple job. By the time the bell rings to signal the end of lunch, Misha and I still have a sizable amount of posters left."

        "As we leave, I decide to stick one right by the door. It must be one that Misha did; it has a little drawing of Shizune on the bottom."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .tongue_tied:
        scene bg school_scienceroom
        with locationchange

        "A couple days later, Shizune heads off to go eat lunch by herself and doesn't come back. She must really be swamped with student council work, although I know that she probably made most of that work for herself."

        scene bg school_hallway3
        with shorttimeskip

        "When I get to the student council room, I find the door unlocked. Before opening it, I hold back for a second, to see if I'll hear Misha's laughing through it. Nothing."

        "I'd almost take that as a sign that no one's in, but Shizune wouldn't leave the door unlocked in that case."

        play sound sfx_dooropen

        scene bg school_council
        with locationchange

        "She's at her desk, sleeping in her chair with her arms folded over her chest. What a stiff pose; if it weren't for her eyes being closed, there would be no way to tell that she was asleep. In fact, I can't even be sure that she is asleep now."

        "Normally, I'd tap a desk to wake anyone else up, but it wouldn't work with her. I immediately start thinking of tricks I could play on her if she's sleeping. It's disappointing that my train of thought goes in those kinds of directions."

        show shizu basic_normal at center
        with charaenter

        ssh "Hello. Good afternoon."

        play music music_shizune fadein 3.0

        "She signs one greeting with each hand. It's really confusing."

        his "Hey, what were you doing? Secretly slacking off?"

        show shizu behind_smile
        with charachange

        "Shizune smiles, but lowers her head to conceal it, and tries her best to look annoyed instead."

        show shizu adjust_frown
        with charachange

        ssh "Don't just stand there, it makes me nervous if I'm sitting down and you're not."

        "I take a seat in the nearest chair while Shizune pauses to adjust her glasses on the bridge of her nose like she's fine-tuning an instrument."

        show shizu adjust_angry
        with charachange

        ssh "Why are you so far away?"

        his "Does that make you nervous, too?"

        "Pursing her lips, Shizune doesn't look too amused at my taunting her."

        his "I had some free time, so I thought I would drop by and see if you were still busy."

        show shizu behind_blank
        with charachange

        ssh "Do you want to help me?"

        his "Yeah."

        show shizu adjust_smug
        with charachange

        ssh "Too bad."

        show shizu behind_smile
        with charachange

        ssh "I'm grateful, but it's not necessary. I just finished the last of it, and now everything that needed to be done is done."

        his "So formal. Misha was just as businesslike yesterday. Are you both getting serious for official student council business?"

        show shizu basic_normal2
        with charachange

        ssh "I'm always serious. Like the student council candidates should be."

        "That was fast. From zero to immediately criticizing people who aren't even her colleagues yet before I've had the chance to stretch my legs."

        show shizu behind_frown
        with charachange

        ssh "At least the presidents. They need initiative, then maybe they can motivate everyone else, or at least strongarm them along. But even though there's a bunch of them, they're all so wishy-washy."

        show shizu basic_angry
        with charachange

        ssh "There's no one running for vice president. So, they all want the big prize, but none of them have the right drive for it. And then the treasurers are always so flaky, I've decided to use my power to just eliminate the position."

        his "Wait a sec, please. Can you even do that? I don't think it works that way."

        show shizu adjust_frown
        with charachange

        ssh "It is how it is."

        "With that, Shizune stares grimly into the distance, rubbing the frame of her glasses. That doesn't answer the question, future dictator."

        show shizu behind_frown
        with charachange

        ssh "I'm disappointed. They should want me out of here faster, because they want the job, or at least disagree with me having the job. If I can't mobilize a bunch of student council wannabes for either reason, all my work will have been for nothing."

        show shizu adjust_angry
        with charachange

        ssh "If they are going to be so slow about it, I'll just hold on to my office as long as possible!"

        play sound sfx_snap

        "Shizune punctuates the sentence with a snap of her fingers, creating a sound as sharp as a gunshot. I wonder if she knows how loud she can do that."

        "It's definitely an attention-grabber, so I could only see it as invaluable to a mute. She might have practiced it because of that."

        his "'All of it,' huh? That's too harsh."

        show shizu behind_blank
        with charachange

        ssh "I always thought this is the real test. Leaving a lasting impression is important. It's why I don't build sand castles, they crumble when you leave."

        his "Maybe, but if I see an especially neat one, I still think it's impressive. I'll say it's impressive."

        his "I kind of admire you. So, to me, it wasn't for nothing."

        show shizu adjust_happy
        with charachange

        "She tugs at her glasses as if she wants to take them off, smiling wryly."

        show shizu basic_normal
        with charachange

        ssh "Sorry."

        show shizu behind_blank
        with charachange

        ssh "I was careless, and something selfish slipped out."

        show shizu basic_normal
        with charachange

        ssh "I've always wanted to stand at the top. It didn't matter what it was, as long as I was the best at it, and understood it completely, and made it my own."

        show shizu adjust_happy
        with charachange

        ssh "Like when you hear a song and dream of being a musician, or see a plane and wish you could be a pilot. Have you ever had a dream like that?"

        his "Yeah."

        "The first time I played soccer, I'd wondered if maybe I could ever get good enough to wow people. That was just a fantasy, though. As soon as I saw the gap between me and people with real talent, I put those dreams behind me."

        "Well, with my heart the way it is, I can't play soccer any more, anyway."

        his "Do you still have dreams like that?"

        show shizu basic_normal2
        with charachange

        ssh "No, they're unrealistic. I realized it very quickly. There is always someone better."

        "A nostalgic expression crosses her face. She looks oddly mature right now, as if the days of competing vigorously against others for supremacy are long behind her."

        "Of course, I know that nothing could be further from the truth. Just last week, she wanted to see which one of us could blow the biggest bubble with a piece of gum. It could be that she was even worse when she was younger; a terrifying thought."

        show shizu behind_smile
        with charachange

        ssh "I liked that. That there was always someone better. When someone greater than me would appear, I'd get so excited. I'd want to challenge them."

        show shizu adjust_frown
        with charachange

        ssh "Even though in the end, they would usually turn out to be better, and I would be left in awe. There are some people who are on a different level, completely. After a while, I got jealous. I wanted something like that for myself."

        his "Is that what the Student Council is, the thing just for you?"

        show shizu basic_normal
        with charachange

        ssh "No, no. Even though it feels like that, sometimes, that wasn't why I decided to do it. That is another story entirely."

        show shizu adjust_happy
        with charachange

        ssh "But… I like being Student Council president. Even if the work is hard and I'm always biting off more than I can chew, that is what keeps it exciting. People at the top shouldn't be able to be comfortable all the time, anyway."

        his "You sound like a farmer."

        "Although they wouldn't suit her, Shizune would look cute in overalls and a straw hat."

        his "So, if that wasn't the reason, why did you run for the job?"

        show shizu behind_frown
        with charachange

        ssh "I didn't, but afterwards, I decided to stick with it anyway. I wanted to be the Student Council president because the old Student Council was stupid."

        show shizu basic_normal
        with charachange

        ssh "And I want to stir people up, so that they will be able to say, 'That was interesting. Today was interesting.' That kind of thing. Memorable experiences."

        show shizu behind_smile
        with charachange

        ssh "I'm happy, because I think we succeeded. You, and Misha, and me."

        show shizu basic_normal2
        with charachange

        ssh "I have a selfish desire too, though. At first it was something I thought would only be a nice bonus, but I've gotten greedy."

        show shizu behind_blank
        with charachange

        ssh "That is why it would make me happy if the elections go smoothly. It would be the only way that I could see that my wish was granted."

        his "What is it, then?"

        show shizu adjust_blush
        with charachange

        ssh "It's a secret."

        "Sensing that I might not be ready to let such a weak dodge slide by so easily, Shizune quickly waves down any attempt at a follow-up, embarrassment coloring her face. It's something she wants to keep to herself only because it's too silly to do otherwise."

        "I start to feel a pang of hunger, and check my watch. It's earlier than it looks. Too early for dinner."

        his "Do you have any kind of food in your desk?"

        show shizu cross_wut
        with charachange

        "For a second, it looks like the question confuses her, but she recovers quickly."

        show shizu behind_frustrated
        with charachange

        ssh "Desks are for supplies."

        his "Food is supplies."

        show shizu basic_normal
        with charachange

        ssh "You should have eaten lunch."

        his "I didn't think it would be a problem if I didn't. If I was working, I wouldn't have to think about it. I'd be too busy to be hungry."

        show shizu adjust_happy
        with charachange

        "She puts her hand up to her mouth in a poor attempt to conceal a laugh, and tries to hide it further by pretending to use it to push her glasses further up the bridge of her nose."

        his "I guess you're not, since you already ate."

        "I'm not good enough to sign the appropriate words, so I settle for pointing at the stack of Chinese food containers leaning precariously out of the top of her trash can."

        show shizu basic_normal
        with charachange

        ssh "Those are from yesterday."

        his "Then we're both hungry. Let's get something to eat."

        his "Not from the cafeteria. There wasn't anything good at lunch, so I really doubt there will be anything good left over. Order something?"

        show shizu behind_frown
        with charachange

        ssh "Ordering out two days in a row is unnatural. Only in case of emergencies. That is my personal policy."

        "This is why she should think of putting some snacks in her desk, it would be an easier way of dealing with these kinds of 'emergencies.' I want to tell her, but signing out how hungry I am like five times has made me too tired to be a smartass."

        "The temptation is really great, though."

        mi "Hi~! Hi, hi!"

        "Misha's distinctive up-and-down voice sounds muffled through the door. She bursts in a second later."

        show shizu behind_blank at tworight
        show bg at bgright
        with charamovechangefaster

        show mishashort perky_confused at twoleft
        with charaenter

        mi "…"

        show mishashort perky_smile
        with charachange

        mi "Hicchan~! You're here, too~!"

        hi "'Too?' How did you know there was already someone in here?"

        show mishashort sign_smile
        with charachange

        mi "If it opens, someone is inside~."

        show mishashort cross_laugh
        with charachange

        mi "Wahaha~!"

        show mishashort hips_grin
        with charachange

        mi "Am I interrupting~?"

        show shizu basic_normal
        with charachange

        "Shizune shakes her head."

        show mishashort hips_smile
        with charachange

        mi "Great~! That's really great~! But~! I was sure I would be. Is this a break?"

        hi "I thought so, too, but it turns out everything student council related is over, for now. Is that why you're here?"

        show mishashort perky_smile
        with charachange

        mi "Wahaha~! Yeah~! That's right, Hicchan!"

        ssh "Sorry to disappoint you. We were just discussing whether or not to order out for dinner."

        show mishashort hips_grin
        with charachange

        mi "That sounds fun~."

        hi "Shizune isn't being very fun about it, though. She says that she can't order food two days in a row. Are you hungry, too? Because if you are, we could outvote her."

        show mishashort hips_smile
        with charachange

        mi "Hm~ hm~, that sounds fun, Hicchan! And, I am a little hungry…"

        hi "I thought you would say it sounds like mutiny."

        show shizu adjust_frown
        with charachange

        "Shizune pinches the frame of her glasses, clearly thinking that it does seem like mutiny, but being outvoted by a clean 2-to-1 margin, there is nothing she can do. Misha already has her phone out. It's awfully garish."

        show mishashort sign_smile
        with charachange

        mi "Shicchan, you promised we would have a student council thing, just for us, right~? Right, right~! This can be it~!"

        show shizu behind_frown
        with charachange

        "Shizune only shakes her head. The last party she will be able to attend as Yamaku's Student Council president is too special to her to put that label on our spur-of-the-moment early dinner."

        stop music fadeout 3.0

        "Even though I'm sure the real thing will be just like this: a meal like any other, with the three of us."

        scene bg school_dormext_full_ss
        with shorttimeskip

        "After we finish eating and clean up, I say goodbye to them and head to my dorm. Although I don't feel particularly tired, I think I'll just go straight to sleep tonight."

        "If I were back home, my mom would nag me not to go to bed right after eating, but what she doesn't know won't hurt her."

        scene bg school_dormhisao_ss
        with locationskip

        "I take a look at the clock as soon as I get in, and realize that it's a lot later than I'd thought."

        "It also feels a bit silly checking the clock when I have a phone and a wristwatch. I take off my watch and hold it in one hand, while holding my phone in the other. It makes me feel powerful, and stupid."

        play sound sfx_doorknock

        "I try unsuccessfully to go to sleep, and am glad when someone interrupts me by knocking on my door after only a few minutes. I figure that it couldn't be anyone but Kenji, which is why I'm surprised when it ends up being Misha."

        play sound sfx_dooropen

        scene bg school_dormhallway
        show mishashort hips_smile at center
        with locationchange

        mi "Hi, Hicchan~!"

        show mishashort perky_sad
        with charachange

        mi "You don't look happy to see me~…"

        hi "No, I'm just kind of surprised. Did Shizune remember something that she wants me to do after all?"

        hi "It's late, but… whatever. I guess it's good that I didn't change."

        show mishashort sign_smile
        with charachange

        mi "Nope~. I just thought I'd follow you back, Hicchan~!"

        hi "For fun?"

        "No, of course not. It's because she wants to talk. It must be about something important, and something she doesn't want Shizune to know about."

        hi "Do you want to come in?"

        show mishashort hips_grin
        with charachange

        mi "Yeah~, thanks, Hicchan!"

        scene bg school_dormhisao_ss
        with locationchange

        show mishashort perky_smile_ss:
            center alpha 0.0
            ease 1.0 ypos 1.13 alpha 1.0

        show mishashort

        pause 1.0

        show mishashort:
            center
            ypos 1.13

        play sound sfx_doorclose

        "She walks in and immediately takes a seat in the chair. The natural thing to do, but I'd expected her to sit on the bed."

        show mishashort cross_frown_ss
        with charachange

        mi "Hicchan…"

        "Misha frowns harshly, arms folded over her chest. It's like she's trying to play a grim interrogator. All that's missing is the mustache and the dangling, flickering lightbulb on a string."

        mi "Did you make Shicchan sad?"

        play music music_drama fadein 6.0

        hi "What do you mean?"

        show mishashort hips_frown_ss
        with charachange

        mi "When I went to the office today, Shicchan couldn't hear me coming. That's why~, when I opened the door, I saw a really confusing expression on her face. Shicchan looked happy and sad, and~ I wanted to know why."

        hi "Well, it wasn't because of me. I didn't even see it."

        hi "I think she's depressed that she won't be Student Council president any more in a few months."

        show mishashort perky_confused_ss
        with charachange

        mi "Hm~… When I asked Shicchan about it, she said that it was okay~!"

        hi "That's meaningless. Shizune would say that, but it's ridiculous to think that she would let it go that easily."

        hi "I mean, there are times when she'll want to fight me over the last apple, or chocolate milk, or whatever. And that is stuff that doesn't even matter."

        show mishashort hips_frown_ss
        with charachange

        mi "Chocolate milk is important."

        hi "Okay, it is. Don't get mad. But not as much as Student Council is to her. She wouldn't just wave it off so easily."

        show mishashort hips_grin_ss
        with charachange

        mi "Wahaha~. You're right~."

        "I thought that this was supposed to be an interrogation, but it appears Misha has already forgotten about it."

        show mishashort sign_smile_ss
        with charachange

        mi "But~! I don't want Shicchan to lie to me to make me feel better."

        show mishashort hips_grin_ss
        with charachange

        mi "Hahaha~! Most people don't know how serious Shicchan is and think she's just putting on a show. I'm happy that you understand her, Hicchan."

        hi "It's obvious. Especially with how she talked about it today."

        "Misha leans in closer with interest, resting her head on her palms."

        show mishashort cross_smile_ss
        with charachange

        mi "Really~? What did she say?"

        "They are close enough that I don't think much of how she is prying."

        hi "Why she joined the Student Council. Sort of. She started, but then decided that some stuff should just stay classified. And signed, 'It's a secret.' So, I guess that's what she told me: it's a secret."

        show mishashort sign_smile_ss
        with charachange

        mi "Well~, if someone tells you that they have a secret, you can sort of call that a secret by itself, Hicchan~!"

        hi "Just like how, according to you, luck is a skill?"

        show mishashort hips_grin_ss
        with charachange

        mi "It can be!"

        show mishashort cross_laugh_ss
        with charachange

        mi "Wahaha~!"

        hi "Be careful, not so loud."

        show mishashort perky_confused_ss
        with charachange

        mi "Why, Hicchan?"

        hi "You're going to wake up half the people in the building, and on top of that, dorms aren't co-ed."

        show mishashort hips_frown_ss
        with charachange

        mi "Hicchan, are you thinking something dirty?"

        hi "Stop being weird."

        show mishashort hips_grin_ss
        with charachange

        mi "Ahahaha~."

        show mishashort hips_smile_ss
        with charachange

        mi "If you are, it's okay, I think."

        "Hearing that makes me realize how easy it's been for me to talk to Misha all this time, that I would be able to go this long without feeling the need to be on guard. This is the first time I have."

        show mishashort perky_sad_ss
        with charachange

        mi "I feel sad, Hicchan."

        mi "It's funny, the happier Shicchan gets, the more depressed I feel. Even though I should be happy for Shicchan. I still am… But~, I can't talk about my problems with her."

        hi "Why not?"

        show mishashort sign_sad_ss
        with charachange

        mi "Just like Shicchan can't talk about her problems to me. It's the same thing, Hicchan. If we have that kind of problem, then I'm not sure any more what I should do. I wonder… if I'm a bad friend."

        show mishashort perky_sad_close_ss at center
        with characlose

        stop music fadeout 2.0

        "Misha gets up and quickly drops herself on the bed, until we're sitting only a few inches apart. Just a couple seconds later, she pushes her head forward, and gives me a light kiss. It misses my lips, more due to bad aim on her part than because of me."

        hi "What are you doing?"

        "Although it's just a formality. I'd be stupid to not know what she is getting at, it's just that it seems so unlikely that I'm hoping there will be some way I won't have to deal with it."

        show mishashort hips_grin_close_ss
        with charachange

        "Now she decides to be shy, and giggles, embarrassed."

        mi "…"

        show mishashort perky_smile_close_ss
        with charachange

        mi "Do you like me, Hicchan?"

        hi "Yeah."

        "Her head is buried in my chest. It feels like she's talking into my scar. She might be able to feel it brushing against her cheek."

        "I'd tried too hard to hide it from both of them before. It seems like such a dumb thing to have worried so much about, in retrospect."

        show mishashort perky_sad_close_ss
        with charachange

        menu:
            with menueffect
            mi "Please comfort me, Hicchan. Just for today."

            "Comfort Misha.":
                $ refuse_misha = False

                call a3sc1o1
            "Refuse." if True:
                $ refuse_misha = True

                call a3sc1o2

        if _in_replay:
            return

    if refuse_misha:
        label .look_ahead:
            call aside_and_ahead_1

            "I'd grown so used to seeing Shizune and Misha together that I hadn't realized until yesterday how much that hasn't been the case lately."

            "And it's a shame, because the empty seat next to her reminds me that they are a pair. So, yesterday is something I'll take to my grave."

            "If I feel this way about it, I wonder how Misha must feel. Just as regretful? When she came on to me, she was more depressed than sexy to start with. I can only imagine how much worse it would be now."

            "Thinking about it like that, I want to see her again. But only halfheartedly. The other half of me is still terrified, even though I hate to use that word."

            "It makes me feel ashamed, but I'm sure it's the only way to describe myself right now."

            call aside_and_ahead_2

            stop music fadeout 0.5
            $ renpy.music.set_volume(0.0, 0.5, channel="ambient")

            "Misha presses herself harder against the fence at her back, as if hoping to slip right through it."

            scene bg school_roof_ss
            show mishashort perky_confused_close_ss at center
            with vpunch

            $ renpy.music.set_volume(1.0, 6.0, channel="ambient")

            "Without really thinking about it, I grab her hand. My reflexes are terrible, and I manage to only grasp onto a few of her fingers, but it's unimportant."

            play music music_rain fadein 6.0

            hi "Sorry. It's just that you said something pretty weird just now."

            show mishashort perky_sad_close_ss
            with charachange

            mi "Hahaha~. Yeah~, I guess that's right, Hicchan."

            hi "Yeah."

            hi "Do you want to know what I think?"

            hi "Shizune is the type of person who won't let anyone close to her except on her terms. It's frustrating, sometimes it's even infuriating."

            hi "That probably would have bothered me, when I was in the hospital and anyone who shut me out was dead to me. I'd forgotten all about it until recently. I got a letter, and it was all about that."

            hi "I was mad. I thought, 'How can you accuse me of closing myself off from everyone and giving up? Isn't that what everyone else did to me? What else am I supposed to do? What can I do?'"

            hi "Yeah, even now, I know that's how it happened, but… she was right, too. I did close myself off."

            hi "So, I made up my mind that I'm not going to let that be the case ever again."

            show mishashort perky_confused_close_ss
            with charachange

            if not side_lilly and wait_for_shizu or _in_replay:
                mi "The hospital? Hicchan… is that what those pills are for?"
            else:
                mi "The hospital? Hicchan… what are you…"

            hi "Just listen, please."

            hi "Shizune is the opposite of how I was. She has always wanted to draw people closer to her. That's the only reason Shizune was interested in me in the first place, I think. And I think I was determined to not let that happen, in a way."

            "Misha casts her eyes downwards, understanding perfectly."

            hi "I never realized how hard that can be."

            hi "And now, I feel like I'm going to return the favor, even if it takes twice as long. I already learned a second language just to get this far."

            hi "It wasn't as hard as I thought, but it was definitely hard. Sometimes, I felt like I was clawing my way up a mountain, with how my hands hurt."

            hi "And you did the same thing. And it was for the same reason, wasn't it? That's really amazing. Which is why it makes me sad, and a little angry, that you would say a stupid thing like that."

            mi "…"

            hi "That's just what I believe, anyway."

            show mishashort perky_sad_close_ss
            with charachange

            "Her shoulders slump, and Misha almost slides to the floor, like she is drained of all energy."

            mi "You're too dramatic, Hicchan."

            "She says, while looking away, turning her head almost as if she wants to look out at the school grounds, but not turning it enough to do so."

            mi "Wahaha~."

            call aside_and_ahead_3

            show mishashort hips_grin_close_ss
            with charachange

            play music music_comfort fadein 5.0

            "Misha laughs, managing to let out a restrained 'wahaha.' That Shizune can't see it makes me feel better. It means that it wasn't only for her benefit."

            show shizu behind_smile_ss
            with charachange

            ssh "I was thinking that you both actually could help me with something. What else is there? We can't go out to eat. We already ordered in yesterday, and that was already breaking policy. Three days in a row would be unforgivable."

            show mishashort perky_smile_close_ss
            with charachange

            mi "But~! That was ordering in, Shicchan~! Going out to eat is different."

            hi "Yeah, totally different."

            show shizu adjust_frown_ss
            with charachange

            ssh "You're both kidding yourselves."

            show shizu basic_normal_close_ss at closeright
            with characlose

            "Before I can reply, Shizune grabs my hand, limiting my ability to do so. My options cut down so drastically, I have no choice but to settle for making a face at her instead. She makes one back, before extending her hand to Misha as well."

            "When Misha is reluctant to take it, I walk forward as far as holding onto Shizune at the same time will allow me, and take her hand myself."

            show mishashort hips_smile_close_ss
            with charachange

            mi "…Hahaha."

            "She only has a second to smile before Shizune starts pulling us impatiently towards the door, binding us together, like a human chain."

            stop ambient fadeout 1.0

            scene ev shizu_hands
            with locationskip

            "Although it's dangerous, none of us seem to think of letting go any step of the way through the school, out of the doors, and across the grounds."

            "This feels familiar, as if we've walked like this before. The three of us, hand in hand. Of course, the mood was a lot happier then."

            "I can see the lingering sadness on their faces, and it makes me wonder if anything has really changed. If this is all just a distraction or not. But I think it's just me slipping back into being cynical because of the moment. It's a start."

            stop music fadeout 3.0

            if _in_replay:
                return
    else:
        label .look_aside:
            call aside_and_ahead_1

            "It's strange that I should be running from the thought of having to talk to Shizune after spending so much time trying to do just that, but I can't think of any other way I should feel. I had sex with her best friend."

            "If I feel this way about it, I wonder how Misha must feel. Just as regretful? When she came on to me, she was more depressed than sexy to start with. I can only imagine how much worse it would be now."

            "Thinking about it like that, I want to see her again. But only halfheartedly. The other half of me is still terrified, even though I hate to use that word."

            "It makes me feel ashamed, but I'm sure it's the only way to describe myself right now. It's not a good feeling."

            call aside_and_ahead_2

            scene ev misha_roof_closed
            with charachangeev

            mi "After all, I've even done something really terrible, now. Unforgivably terrible."

            "Misha presses herself harder against the fence at her back, as if hoping to slip right through it."

            hi "Don't be stupid."

            "I'm surprised by the tone of my voice."

            hi "Sorry."

            hi "I realized, I hate it when I'm left feeling regretful, over anything. Even so, it's impossible for me to not end up regretting something."

            hi "Yesterday, I did a stupid thing. That's probably part of the reason why I'm here right now, so I could figure out if I could maybe… make it right, somehow."

            hi "Do you ever feel that way? You said you've done some terrible things. You can try fixing them."

            scene ev misha_roof_normal
            with charachangeev

            mi "Hicchan~, isn't that…"

            "I know that she's thinking that I'm saying this more for me than for her."

            hi "No. It's not."

            hi "I just think that killing yourself is the biggest regret a person could end up with."

            mi "…"

            mi "Hicchan, you're so dramatic."

            scene ev misha_roof_closed
            with charachangeev

            "Whether she was serious, I'll never know. I don't try to find out; as she lets out a sigh and closes her eyes as if going to sleep, I feel that the dangerous mood I was picking up from her has passed."

            call aside_and_ahead_3

            show shizu behind_smile_ss
            with charachange

            ssh "It's not a trick. I promise. It will be something fun."

            show mishashort perky_sad_close_ss
            with charachange

            play music music_rain fadein 4.0

            "Misha contrasts the genial smile on Shizune's face with a lonely expression of her own."

            "If Misha is really jealous of me for stealing Shizune away from her, then it'd only make it worse if all three of us were together. I imagine it'd be like rubbing salt in an open wound. So I get the idea to let them spend time together."

            "I'm not so idealistic that I think a single afternoon to themselves will solve everything, but it might help. It seems like the better option than going with them, because my presence definitely wouldn't help at all."

            hi "You two can go have fun, then. I'm going to go to bed early."

            show shizu basic_normal_ss
            with charachange

            ssh "Are you sure? It's barely past lunch."

            hi "I told you, I don't feel too good today. I think I'm coming down with something."

            show shizu adjust_frown_ss
            with charachange

            ssh "I thought that you said excuses like that won't work."

            "She has me there."

            show shizu basic_normal2_ss
            with charachange

            ssh "It's okay. But refusing someone's invitation is rude. I'll expect you to make it up to me."

            show shizu adjust_happy_ss
            with charachange

            "Shizune turns around and smiles at Misha, and starts signing something that I can't see. I assume it's along the lines of 'it looks like it's just going to be the two of us.'"

            stop music fadeout 3.0

            "That's good."

            stop ambient fadeout 2.0

            if _in_replay:
                return

    return

label aside_and_ahead_1:
    scene bg school_dormhisao
    with locationchange

    play music music_night fadein 4.0

    "The following morning, I wake up thinking that most of my time is going to be spent trying to avoid Shizune and Misha."

    "What happened last evening still makes me feel uneasy. I'd thought that sleeping on it would help alleviate that feeling. I feel like an idiot for believing it would be that easy."

    "I think about whether or not Misha might feel the same way. If so, she probably won't show up to school today. I'd considered doing the same, but it would be pretty suspicious, and staying inside all day in fear doesn't appeal to me. It never really has."

    scene bg school_scienceroom
    with locationskip

    "Like I thought, Misha isn't in class this morning. Shizune is, but today is a busier day than most, so she gives her all concentrating on her classwork, and that means there's little idle time for her to start up a conversation with me."

    return

label aside_and_ahead_2:
    scene bg school_library
    with shorttimeskip

    "I spend the next couple periods in the library, not in the mood to sit in classes for the rest of the day, but unwilling to walk back to the dorms."

    show shizu:
        center
        ease 1.0 ypos 1.14
    with Dissolve(1.0)

    "While I'm lazily flipping through the pages of an uninteresting historical fiction novel, Shizune drops herself into the chair across from me, pouting."

    show shizu adjust_frown
    with charachange

    ssh "I think it's sort of pointless to come to school and then skip every class."

    his "Sorry."

    show shizu behind_frustrated
    with charachange

    ssh "At least tell everyone that you're sick."

    his "I'm just not feeling it today. Yesterday I was fine, though. Tomorrow, I'll probably be fine. Taking a sick day in the middle of the week is just too suspicious. That '24-hour flu' thing or whatever won't fly."

    show shizu adjust_frown
    with charachange

    ssh "It's not suspicious."

    his "It is."

    show shizu basic_angry
    with charachange

    "I turn back to my book, but Shizune gently pulls it down, in contrast with her expression, which straddles the line between concern and anger."

    show shizu behind_blank
    with charachange

    ssh "Is something wrong?"

    his "What?"

    show shizu basic_normal2
    with charachange

    ssh "Is something bothering you? Because you're acting a little suspicious today, in a different way."

    show shizu behind_blank
    with charachange

    ssh "If there is, just tell me, or I'll be mad. I'm not good at reading people."

    "What a ridiculous thing to say, after picking up my mood so easily."

    "She is only half-kidding, but there is some truth in it. After all, she can't hear tone, and has to rely on reading to communicate with others."

    "It's as if you could only ever have conversations with someone through text messages. That has to mess with you in some way."

    "It's probably why she stares so intently at people, in order to gauge their reaction. Or maybe it's why she pushes people so hard, to get them to react."

    "I've thought about it before, but it's too hard to say for sure what Shizune's exact motivations are for anything."

    "So, I wonder how much of that was a joke. Sometimes, it's easy to tell. This time, it isn't. Assuming it wasn't a joke, I can't tell her anyway. Because it's sign language, there is enough time to collect myself and lie effectively."

    his "Nothing."

    show shizu cross_wut
    with charachange

    shi "…"

    his "I've just been thinking a lot about the Student Council's future, lately. I believe Misha is doing the same… well, in her own way."

    show shizu behind_frustrated
    with charachange

    ssh "So am I, but she isn't here today. I wish she would have let me know something, because I might need her help later today. Yours too, unless you're busy."

    his "I'm not…"

    show shizu basic_normal
    with charachange

    ssh "Thank you."

    show shizu behind_sad
    with charachange

    ssh "I feel like I'm losing a lot of people close to me, lately."

    "I can't think of a good way to respond to that. Something reassuring and confident, telling her not to worry. 'I'm here for you. I'm not one of those people.'"

    "Then, who is? And it seems so forced. I manage a wave of my hand that seems extremely callous as soon as I do it."

    his "You shouldn't feel that way."

    show shizu basic_normal2
    with charachange

    shi "…"

    his "I might be just a little sick, not enough to go through the trouble of making it official. It's just easier for me this way."

    show shizu behind_frown
    with charachange

    ssh "It's the wrong way."

    "I've heard the hard way and the right way are usually the same thing, so it's not a big stretch to say that the opposite is true."

    show shizu basic_normal
    with charachange

    ssh "Well, fine. If you say you are all right, that's good enough for me."

    his "Wait."

    show shizu behind_blank
    with charachange

    shi "…?"

    his "You asked me, so I'm turning it around. Is everything okay with you?"

    show shizu basic_normal2
    with charachange

    ssh "Yes."

    stop music fadeout 3.0

    "She signs it without a moment's hesitation. After that, Shizune waits to see if I'm going to follow up on it."

    show shizu:
        ease 1.0 center alpha 0.0

    pause 1.0

    hide shizu

    "I don't, and she leaves. I feel like an idiot for not going further, even though I think it's better that I didn't."

    "I've been in the library for quite a while, and decide to go up to the roof for a change of pace."

    play sound sfx_door_creak
    play ambient sfx_rooftop fadein 1.0

    scene bg school_roof_ss
    with locationskip

    "A fresh breeze hits me the second I open the door. This is really my favorite area of the school, I think. Then I see that I'm not the only one here. I can see a girl with bubblegum-pink hair in front of me."

    "Her back is to me, but I don't have to see her face to know who it is. I'm sure Misha is the only person in the world with hair like that."

    "I get the feeling that I've stumbled on her at a bad moment. She obviously wants to be alone, and I wonder if she hasn't noticed my presence. If so, I'll leave right now. But she has, and turns to face me."

    $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

    scene ev misha_roof_normal:
        yalign 1.0 xalign 0.5
        easein 12.0 yalign 0.0
    with whiteout

    play music music_sadness fadein 8.0

    mi "Oh, Hicchan. I thought someone was behind me, but I didn't think it was going to be you. This time, you surprised me."

    "If she's referring to her habit of sneaking up behind me and asking me to guess who it is… I've never been surprised by that."

    hi "I'm surprised, too. But this is good. I had something I wanted to talk to you about, anyway."

    mi "…"

    hi "Not that…"

    hi "What's going on between you and Shizune? She won't tell me, so I'm asking you."

    "'Because you're easier to get an answer out of, since the same sign language that gives me the leeway to lie to her gives her a cushion against my questions, so that she can more easily brush them off.' When she hesitates, I push her harder."

    hi "Give me an honest answer, please."

    mi "It's complicated, Hicchan… It's because of something that happened a long time ago. I thought I could just forget about it, but~… it's really hard. So~, that and graduation coming up made me want to spend more time with Shicchan~!"

    scene ev misha_roof_sad
    with charachangeev

    mi "But Shicchan is always busy now. So~! We've been fighting. But, I'm tired of it now."

    mi "Because~… I like Shicchan."

    hi "So do I."

    scene ev misha_roof_normal
    with charachangeev

    mi "Wahaha~. No, no~. I know you like her, Hicchan. I mean that I like Shicchan in the same way."

    scene ev misha_roof_closed
    with charachangeev

    mi "I want her to be my girlfriend."

    "Misha closes her eyes, like a condemned criminal confessing the last of their sins in front of the executioner. It only makes it harder for me to think of a response, and I know I have to give one."

    hi "I see. I never knew."

    scene ev misha_roof_normal
    with charachangeev

    mi "I didn't really want to come to this school, Hicchan~. But it sounded interesting, and even if everyone hated me, at least it felt like they would leave me alone. I was learning sign language, but wasn't very good at it~."

    mi "Shicchan was trying to get people to join the Student Council, because it was only her and Lilly. Then, she came up to me. I couldn't understand her at all~."

    scene ev misha_roof_angry
    with charachangeev

    mi "But~! Shicchan wouldn't use her pen and paper. She knew that I was taking sign language classes. I was exposed quickly, I didn't know any~… That only made her try harder, and I hated Shicchan and thought she was making fun of me."

    scene ev misha_roof_normal
    with charachangeev

    mi "That wasn't the reason, though~…"

    mi "So~! I slowly fell in love with Shicchan, and I told her… that I loved her."

    scene ev shizu_flashback:
        truecenter
        zoom 1.15
        easein 30.0 zoom 1.0
    with whiteout

    mi "It was in the student council room, you know. When it was just the two of us."

    mi "I had these fantasies of Shicchan staying alone in the office, trying to put everything together all by herself. It seemed so lonely to me, and so sad~. I think I wanted it to be that way~."

    mi "That way, I could be there for Shicchan, and maybe Shicchan would like me. Even though there was no reason for me to believe it, I did anyway. I wanted it to be true, so I was okay with letting myself believe it, even though I think I knew."

    mi "That day was really, really~ beautiful, too, Hicchan~. We were done with everything, and I was looking out through the window. Even through the window, the light was so warm~… I wanted to stay like that forever, next to Shicchan."

    mi "But~! Then I looked at Shicchan, and she had her back to the window and was still working on something, blocking out the rest of the world. The light was on her shoulders, like when I would put a blanket on my shoulders as a little kid."

    "Misha stops for a second as if trying to hold onto the image of Shizune in her mind."

    mi "Shicchan looked… hm~… It was like, Shicchan looked in a way that made me want to be with her… But it felt like it would be hard for that to happen."

    mi "Wahaha~. That was~, a really~ long~ time ago. My hair was different back then, too. A little messy~? I cut it because Shicchan was always talking about it."

    mi "Anyway~! I told her, right then and there; I confessed~."

    scene ev misha_roof_sad
    with whiteout

    mi "I was rejected~."

    mi "So~, I thought that that was it, Hicchan. But Shicchan was always trying to find me, and I hated Shicchan again for it. And when I asked her why she was doing it, it was because I was her friend."

    "Her cheeks have a hint of red in them. I wonder how much experience she has had with crying, that she can keep herself from doing it so well. If she didn't pause to wipe her eyes, I might never have noticed."

    scene ev misha_roof_closed
    with charachangeev

    mi "Having Shicchan say that made me happy, but also sad, and even though she never meant to hurt me, it still hurts. Even now…"

    mi "Shicchan has a way of manipulating people, Hicchan. Sometimes she wants to, and sometimes she doesn't really, but it happens anyway~. And sometimes I'm just not sure… exactly which one it is. And I feel doubt…"

    mi "I just wish that Shicchan liked me instead of you. It made me wonder if I was starting to hate you and Shicchan… just a little. I… didn't like that."

    hi "So you were thinking, maybe it would be better if I weren't here at all?"

    scene ev misha_roof_normal
    with charachangeev

    "She looks confused. The thought has never crossed her mind."

    mi "That's not it, Hicchan."

    scene ev misha_roof_sad
    with charachangeev

    mi "I thought about it a lot these last few days, and I don't want to hate anyone. You, or Shicchan. It's so stupid that I ever felt like that, isn't it, Hicchan? I don't want to think about that kind of stuff ever again."

    mi "And missing people, and being apart from them; I'm tired of it, and don't want to think about it any more."

    mi "I already did, though. So~! …I'm still really the worst kind of person. I wasn't thinking that it would be better if Hicchan had never come to this school. I was thinking… wouldn't it be better if I just died?"

    return

label aside_and_ahead_3:
    $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

    scene bg school_roof_ss
    show mishashort perky_confused_close_ss at center
    with locationchange

    stop music fadeout 0.5
    $ renpy.music.set_volume(0.2, 0.0, channel="sound")
    play sound sfx_door_creak

    "The door behind us opens, the sound only barely able to be heard over the ambient breeze."

    show bg at bgleft
    show mishashort at closeleft
    with charamove

    show shizu behind_blank_ss at tworight
    with charaenter

    ssh "I've been looking everywhere for you two. Is this some secret meeting?"

    "She walks over to us, leaning against the fence next to Misha as if she needs to stop and catch her breath, before pushing herself off it and continuing."

    show shizu basic_normal_ss
    with charachange

    ssh "I'm bored sitting in the student council room every day now, without either of you ever coming by. Taking some time off is fine, but this is just too much."

    "Normally, Misha and I would be jokingly making excuses for ourselves at this point. This time, there's only silence. Shizune, always expecting resistance, is thrown off balance by the lack of it."

    $ renpy.music.set_volume(1.0, 0.0, channel="sound")
    play sound sfx_snap
    show shizu adjust_happy_ss
    with Dissolve(0.3)

    "A few seconds pass in uneasy silence, which Shizune breaks with an ear-shattering snap of her fingers, smiling as if to say 'eureka.'"

    show shizu basic_happy_ss
    with charachange

    ssh "Let's go do something together."

    hi "Like what?"

    show shizu behind_smile_ss
    with charachange

    ssh "Anything! We should go to the student council room first, and then figure it out from there."

    hi "That seems like a trick to get us to do work instead."

    show shizu basic_normal2_ss
    with charachange

    ssh "Very funny."

    return

label a3sc1o1:
    play music music_moonlight fadein 4.0

    "As much as I pretend to protest, I've allowed things to come to this point. Even though I knew so far ahead of when she actually came out with it that this was what she was getting at."

    "At the very least, I was okay with this outcome. If I needed any more proof, it's simple: I still haven't turned her away."

    "I could have at any point, and it was wrong of me not to do it sooner, but now, not doing so is something beyond simple carelessness."

    show mishashort perky_sad_close_ss:
        linear 0.2 alpha 0.0 ypos 1.1
    with vpunch

    hide mishashort

    "Misha takes my silence as agreement, and squeezes herself against me tightly, as if she is trying to get into my clothes. My arms are enveloped by the softness of her skin and the warmth of her body. I roll over on reflex, and end up on top of her."

    "She looks at me, as if expecting me to take the lead, and closes her eyes nervously the second I return her gaze. I guess I have no choice, and I clumsily begin trying to undress her, something I've never done before."

    scene evh misha_naked:
        xalign 1.0
        easein 12.0 xalign 0.0
    with whiteout

    "After all, I've only had sex once before, and I was restrained to a chair. This time, I'm in control, like I'd wished then. But it's really kind of scary, now that I am. I start by unbuttoning her blouse, and slipping it off of her shoulders."

    "Her figure is curvier than I expected, and complements her cute face."

    "Her bra unhooks in the back, and I have trouble getting it off, partly because Misha seems ashamed of her breasts, and halfheartedly tries to cover them before I've even undone it."

    "When I unlatch her skirt and start pulling down her panties, she offers more moments of weak, fake resistance. It's just a formality."

    "I realize now that formalities are very important to Misha. It's why she always greets everyone so happily, even when she probably isn't happy to see them."

    "Her eyes are open now, and I run my hand up the inside of her thigh, almost laughing when she shudders and nearly crushes it when she tightens her legs. A genuine reaction, and a cute one."

    "Shizune was better at hiding her inexperience, even though she was just as embarrassed."

    hi "Are you ready?"

    "She nods without looking at me."

    scene evh misha_sex_aside:
        truecenter
        zoom 1.05
        easein 6.0 zoom 1.0
    with charachangeev

    "As I push myself into her, I can feel her becoming rigid with nervousness, which I start to feel as well when I meet a resistance inside her. I feel so tense that every time I move, it feels painfully mechanical."

    "I wonder if I should go more quickly, like Shizune did. But Shizune is pretty forward. It's a different situation now, one I regret getting myself into. I start pushing in slowly, and Misha winces in pain."

    mi "Please do it quickly…"

    scene evh misha_sex_closed
    with charachangeev

    mi "Ow…"

    "I stop."

    scene evh misha_sex_aside
    with charachangeev

    mi "No, it's okay."

    "And then I push myself even deeper into her, to the hilt, feeling Misha's hands clasp my arms, and then reach higher, as if she is trying to climb them."

    "Grabbing at my shoulders, she pulls herself against me, joining us more tightly together, and I can't do anything but push back."

    scene evh misha_sex_closed
    with charachangeev

    mi "Ah~… aaah…"

    "Hearing her moans, I speed up and find a rhythm. Her hands grip each other around my back, and I feel her elbows digging into the space under my ribs as I piston into her."

    "The blood pounds in my ears like the beating of a drum, until I can barely hear her."

    mi "Hnn~…"

    scene evh misha_sex_aside
    with charachangeev

    mi "This is my first time with a man. It's weird."

    "I wish she would stop talking. Her voice is so quiet and breathy that I have trouble understanding her, but the tone of sadness permeating it is unmistakable, and only makes me feel guiltier."

    "I'm supposed to be comforting her, but it's entirely physical, and if Misha is being reassured in any way by this, she isn't showing it. That makes me question whether my decision was the right one. I'm really starting to doubt it."

    scene evh misha_sex_closed
    with charachangeev

    "Despite that, her soft cooing in my ear makes me keep going, as does the hot, slick tightness around my member. Eventually, her leg twisting around mine, she tenses up in orgasm, her smooth neck rubbing across my cheek."

    scene evh misha_naked
    with whiteout

    stop music fadeout 6.0

    "It takes her a minute to separate herself from me. It gives me an opportunity to see her body fully, her pink skin blushing bright red and dabbed with sweat. I feel cold."

    mi "…Hicchan?"

    "I can't hear anything but the ticking of the clock, and the sound of my own breathing."

    mi "…Never mind, Hicchan."

    "I search around for Misha's hand with my own, and caress it. How light and delicate it seems, even as it grabs me so tightly around my wrist. The feeling is familiar."

    scene black
    with dissolve

    return

label a3sc1o2:
    show mishashort perky_sad_close_ss:
        linear 0.2 alpha 0.0 ypos 1.1
    with vpunch

    hide mishashort

    play sound sfx_pillow

    "Before I can answer, she pushes her whole weight against me, and it unbalances me enough to send us both onto the bed. If I don't answer quickly, then the situation will only become more precarious."

    "I know that I should have never let things get as tangled as they already are."

    "So, even though it isn't the most tactful way to refuse her, I push her off of me. Misha falls backwards onto the sheets, so softly that it seems like she barely fell at all. Eyes closed, she stays like that for a while, before getting up with a hollow laugh."

    show mishashort perky_sad_ss:
        center ypos 1.2
        ease 1.0 center
    with Dissolve(1.0)

    play music music_moonlight fadein 6.0

    mi "You're right, Hicchan. I'm sorry."

    scene black
    with shuteye

    "I'm not sure how I feel. Regretful, slightly, even though I've grown to hate regret. Sad, for a multitude of reasons. I'm also a little angry, both at her and at myself. And in a way, it even seems like I'm not really feeling at all."

    hi "Don't be."

    mi "No, Hicchan. It's okay~. I am, really, really~."

    mi "But… just asking was enough for me, I think."

    mi "I'm happier that you said no."

    hi "Is that right? Well, that's good."

    mi "Yeah~, it is. Thanks, Hicchan."

    "She pulls herself up and leans against the wall. I'm assuming she is. My head hurts so much that I don't bother opening my eyes. I lie on my bed, listening to the rustle of my hair brushing against the sheets and the grass waving in the wind outside."

    "I guess that I should say more to reassure her, but I wonder if that would really help. Maybe it would be better to say nothing. I just don't know, although I think that in this situation, there's no one right thing I can do."

    mi "Goodnight, Hicchan."

    play sound sfx_doorclose

    stop music fadeout 4.0

    "With that, she leaves, the door clicking shut behind her like a guilty whisper."

    "Maybe it's because I'm eager to put today behind me, but after Misha is gone, I find it much easier to fall asleep. I do so almost instantly."

    scene black
    with dissolve

    return
