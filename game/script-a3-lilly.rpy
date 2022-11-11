# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a3_lilly:
    label .day_by_day:
        scene black
        with dissolve

        scene bg misc_sky:
            xalign 0.0
            warp acdc_warp 10.0 xalign 1.0
        with locationchange

        $ renpy.music.set_volume(1.0, 0.0, channel="music")
        play music music_normal fadein 3.0

        "I rest my chin on my hand as I absentmindedly look out the window, yet another of Mutou's lectures droning on and on as if it were endless."

        "The summer sky is almost alluring in its bright cerulean splendor. Only the odd passing cloud breaks up the deep blue expanse."

        "This feeling of longing is probably the outdoors side of me yearning to escape."

        mu "Nakai, could you answer this?"

        "That side of me's lost to the past now, though."

        scene bg school_scienceroom
        show muto normal at center
        with locationchange

        hi "In that case… I think it would use the -ane suffix?"

        show muto smile
        with charachange

        mu "Correct. Moving on, the suffix for…"

        "As my attention towards Mutou slips once again, I spot Misha giving me an enthusiastic thumbs-up, and nod at her to settle her down."

        scene bg school_scienceroom
        with shorttimeskip

        "It's been a handful of days since Lilly left for Scotland, days which have passed relatively peacefully."

        "Life largely continued as usual, in contrast to what I'd expected. While thoughts of her have danced around on the edge of my mind since she left, present events manage to subdue them. At least for the time being."

        "So I find myself idly chatting with Hanako, as usual, when lunchtime finally rolls by."

        show hanako basic_normal at center
        with charaenter

        ha "Are the later ones in the series good as well?"

        hi "Not really. You're probably best off just sticking to the original. His later books didn't live up to it, other than maybe 'God Emperor.'"

        show hanako basic_bashful
        with charachange

        ha "Thanks, I wasn't really sure if…"

        show misha hips_smile at offscreenleft
        show shizu behind_blank at offscreenleft
        with None

        show hanako defarms_shock at right
        show shizu at center
        show misha at left
        show bg at bgright
        with charamovechangefaster

        "As Hanako steps to the side, I see Shizune stride up in her typically businesslike manner, flanked by her ever-present bright-haired shadow."

        "Try as I might, I can't read any hint of their intent from their faces. Shizune's poker face and Misha's seemingly boundless cheerfulness are a devilish combination."

        hi "'Morning Shizune, Misha."

        show hanako emb_timid
        with charachange

        ha "Um… hi."

        show shizu basic_normal
        with charachange

        "I accentuate the greeting with a nod to Shizune in order to get the point across. She promptly and curtly returns the gesture to both of us."

        "It's been a long while since I've really talked to either of them. For a while I thought they might be avoiding me, but I eventually came to the conclusion that Shizune really isn't the type to do so."

        show shizu adjust_happy
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "'Morning~! Shicchan says that Mutou wants to see you sometime."

        "Because of this statement, my face contorts as if I'd just eaten spoiled food, giving Misha no end of amusement."

        show misha cross_laugh
        with charachange

        mi "Wahahaha~! Anyone'd think you were in trouble, Hicchan!"

        show shizu behind_smile
        with charachange

        shi "…"

        show misha perky_smile
        with charachange

        mi "You may not be aware of it, but you have the least to worry about out of anyone in the class."

        show hanako emb_smile
        with charachange

        "What an unexpected vote of confidence. Even Hanako nods hesitantly to affirm the point."

        hi "Thanks, I'll keep that in mind. There was something I wanted to ask you, though."

        show shizu basic_normal
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "And what might that be, Hicchan?"

        "I have a feeling this won't go over well, but here goes…"

        hi "Is there any reason why you and Lilly don't get along? It seems like even a little civility would help you both in your duties."

        show shizu cross_angry
        with charachange

        "Shizune's cold stare after Misha happily signs the words stops me in my tracks. In hindsight, I really could have worded that better."

        show hanako emb_sad:
            xpos 1.05
        with charamovechangefaster

        "Out of the corner of my eye, I'm sure I see Hanako move back. Just a little."

        show shizu basic_angry
        with charachange

        "Thankfully, Shizune notices this and lets her temper dissipate as she forcefully runs her hand through her hair to let off steam. Perfectly on cue, Misha begins interpreting the second Shizune's arms begin to move."

        show shizu behind_frown
        with charachange

        shi "…"

        show misha hips_frown
        with charachange

        mi "I would say that such matters aren't relevant to you, but since you seem to have befriended Lilly…"

        show shizu adjust_frown
        with charachange

        "She pauses to adjust her glasses, evidently attempting to articulate her point in the best possible manner."

        show shizu basic_angry
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "While I assume the same of her, I cannot call my own views on the matter unbiased. Suffice to say, we were closer before than we are now."

        show shizu behind_frown
        show misha sign_confused
        with charachange

        "Shizune makes a quick gesture to Misha to stop her from interpreting, then has a quick meeting with her before proceeding. The fact that the two can communicate so easily yet so secretly right in front of us is slightly disconcerting."

        show hanako basic_normal
        show shizu basic_normal2
        show misha sign_sad
        with charachange

        "Hanako seems to share my curiosity at the proceedings, looking on with thinly-masked interest. As they finish their opaque conversation, Misha looks slightly deflated. I guess her opinion on the matter wasn't followed."

        show misha perky_confused
        with charachange

        mi "Shicchan says you should ask Lilly about it, as she doesn't want to be the one that gets you involved."

        "Ah well. I'll just have to ask her after she gets back. At least I got some information out of Shizune; the two having been on close terms means that they weren't always at each other's throats, or at least not quite to this extent."

        hi "I understand. Thanks anyway."

        stop music fadeout 8.0

        show shizu at offscreenleft
        show misha at offscreenleft
        show hanako at center
        show bg at center
        with charamovefaster

        hide shizu
        hide misha

        "With a nod and a farewell the two break away and walk out the door, no doubt headed straight for the student council room."

        hi "…Could have gone worse, I suppose."

        show hanako cover_bashful
        with charachange

        "Hanako lets out a long breath, relieved at the confrontation's resolution. I can't say I blame her."

        show hanako basic_bashful
        with charachange

        ha "I'll see you later, then?"

        hi "Yeah, I'll meet you in the tea room. Seeya."

        hide hanako
        with charaexit

        "With that, she waves and joins the trickle of students leaving the classroom."

        show muto normal at center
        with charaenter

        mu "Nakai, could I speak with you for a moment?"

        "Delivered in his typical monotone manner. He apparently decided that I need a reminder to see him already."

        hide muto
        with charaexit

        "Eventually I finish packing up my things. By the time I reach his desk the classroom is close to empty."

        hi "Uh… yes, sir?"

        play music music_happiness fadein 5.0

        show muto normal at center
        with charaenter

        "He looks up, taking measure of my face before giving an awkward, rather obviously acted, chuckle."

        show muto smile
        with charachange

        mu "No need to feel guilty, you're not in any trouble. I just want to ask you something I've asked a few of the other students so far."

        "That's something at least. For a moment, I'd thought my maxim of keeping my head down and pen up had failed me."

        hi "So what did you want to talk about?"

        show muto normal
        with charachange

        mu "To start with, what do you think of your progress in this class, so far? Good? Bad?"

        "I detest that kind of question. For a fair amount of time I try to think of a response that is neither pathetically humble, nor cocky."

        hi "I'd say I'm doing okay. The work doesn't seem too hard, and I'm doing better on the tests than I thought I would."

        show muto smile
        with charachange

        mu "That's a good answer. A correct one, too."

        "I give a mental sigh of relief at his satisfaction. To say that I don't gain a little pride from his comment would be a blatant lie."

        "In the maelstrom of thoughts clouding my mind after learning that I'd be transferring to Yamaku, my school grades seemed utterly unimportant."

        "Being entirely clueless as to what skill level would be assumed of me, once I actually got here I was hugely relieved when I found out that I understood well enough the schoolwork we'd be doing."

        show muto normal
        with charachange

        mu "I know your circumstances might have thrown a wrench in the works, but have you given any thought to your future?"

        hi "My future?"

        mu "What you'd like to do as a profession. Do you have any thoughts of where you'd like to be in ten or twenty years' time?"

        mu "I wouldn't be surprised if you covered this ground in your previous school, but I don't have any record of it if you have."

        "I suppose the last year of high school is the time when students would need to be thinking about such things. To be honest, I really haven't lent it much thought, compared to my immediate situation."

        "Catching on to my thinking, Mutou speaks up."

        mu "It's okay if you haven't decided on anything specific yet. I wouldn't be surprised if a lot of your classmates were still undecided, after all. Maybe pursue one of your talents?"

        "He's rather obviously trying to squeeze an answer out of me, and something about his previous wording makes me suspicious."

        "He didn't seem to be intent on asking everybody like this, so he must have some kind of selection criteria. At a guess, our grades in his class."

        hi "Well, something in science might be the path of least resistance."

        "His face brightens, no doubt pleased at the thought of a prized student following his subject as a career path."

        show muto smile
        with charachange

        mu "Good. Having a general idea is the first step. I would advise you to think on it, though."

        hi "I will. Things are kinda settling down, which will help."

        mu "Good to hear. Oh, and I've noticed that Ikezawa's attendance and grades have improved since you came to be friends. I'd like to thank you for that."

        hi "I'm surprised you noticed we knew each other."

        "He gives a chuckle as awkward as his smile."

        "This guy really has no idea how to properly act around others. Every facial movement seems like an act of careful but misdirected choreography."

        show muto normal
        with charachange

        mu "You could say that having a general idea of who knows whom is part of a teacher's job."

        "Catching himself before he goes off on a tangent, he loudly coughs into his hand."

        mu "I'm sure you have things to do, though, so I'll stop there. Please do think about where you're headed from here, as you don't have long to go before you finish high school."

        hi "I will. Thanks."

        stop music fadeout 4.0

        scene bg school_hallway3
        with locationchange

        "The brief talk ended, I take my leave. He goes back to fussing with the teaching materials on his desk."

        "This is one of the times I'm envious of Lilly, almost maddeningly so. To have one's future so clear and so assured, yet working towards it from such a young age…"

        "It's an idea so utterly irreconcilable with my own thoughts, mired in the present day just as they've always been."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .minor_discord:
        scene bg school_lobby
        with locationchange

        "Walking through the lobby to the cafeteria, I silently rue my daily routine having been completely thrown off."

        "It had seemed like a normal day; I arrived in class before most, due to waking early and having become quite adept at chucking down my pills without choking as I get ready for the day."

        "But as students trickled in, one never materialized. Hanako."

        play ambient sfx_crowd_indoors fadein 0.5
        scene bg school_cafeteria at right
        show crowd at left
        with locationchange

        "I step inside, my eyes scanning the expanse of the cafeteria in search of a suitable place to take a seat. It's a task made more difficult by the groups of students moving about and busily talking."

        play sound sfx_impact2
        with vpunch
        $ renpy.music.set_volume(0.5, 0.3, channel="ambient")

        hi "Geh!"

        "A hand pounds my back hard a couple of times, severely winding me."

        $ renpy.music.set_volume(0.0, 0.0, channel="ambient")
        scene black
        with shuteyefast

        "I couldn't care less about the culprit as I focus my thoughts on my chest in a near-automatic reaction."

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.2)

        "My hand instinctively tightens on my breast, and I start going through the steps I rehearse in my mind every other day."

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.2)

        "Breathe steadily… in… and out…"

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.7)

        "With a measure of relief, I can slowly feel my chest becoming less tense. By the time I look back up, my face is covered in sweat from the experience."

        $ renpy.music.set_volume(1.0, 5.0, channel="ambient")

        scene bg school_cafeteria at right
        show crowd at right
        show kenji happy_close at center
        with openeye

        ke "Hey… man, are you okay?"

        hi "GODDAMNIT! Don't {b}do{/b} that, you idiot!"

        show kenji tsun
        with charadistant

        "He retreats back, an expression of unease written on his face. In hindsight, I probably shouldn't have barked at him, considering he had no way to know."

        "I give a sigh and right myself with some difficulty."

        hi "Sorry. I just have some… chest problems. Sharp knocks aren't good."

        "It seems strange to see him so upset. The fact that I can't do anything about it irritates me."

        hi "Let's get lunch."

        show kenji neutral
        with charachange

        ke "Okay. It's good to have some company, for once."

        hide kenji
        with charaexit

        show bg at left
        show crowd at left
        with charamove

        "We start off to the serving line. One good thing is that Kenji and I can make small talk nowadays, as opposed to my only interaction with him being anti-feminist lectures."

        hi "Seems like it'd be hard to find an empty table."

        show kenji neutral at center
        with charaenter

        ke "There's a few people I wouldn't mind sitting with. Nobody's like you, though."

        $ renpy.music.set_volume(0.0, 0.5, channel="ambient")

        "I feel a shiver run through my spine."

        hi "Clarify that now."

        play music music_kenji fadein 2.0

        show kenji tsun
        with charachange

        ke "They don't listen. Their minds are closed. It's the media, man, the Goddamn brainwashing mainstream feminist Fascist media."

        "He takes a breath, and I savor the second of silence."

        $ renpy.music.set_volume(1.0, 10.0, channel="ambient")

        ke "Damn, they control everything. Everything but you and me."

        "I relax a little while we grab our food and drink."

        show kenji happy
        with charachange

        ke "So, what've you got for me?"

        hi "Huh?"

        show kenji neutral
        with charachange

        ke "Come on, you've been hanging around Satou and that other chick for ages now. Rumors are all over my class, and probably some of the others too."

        hi "Eavesdropping isn't a good habit."

        show kenji happy
        with charachange

        ke "Let me guess, you never do it? Not even when you're bored? Really?"

        hi "Well… I… uh…"

        hi "Fine. Point taken."

        hide kenji
        with charaexit

        "Both of us stop to have soup ladled into a couple of small bowls and placed onto our trays. The concoction that lands into the bowl looks pretty questionable, but at least it smells reasonably good."

        stop ambient fadeout 1.0

        show bg at center
        show crowd at center:
            linear 1.0 alpha 0.0
        show kenji neutral:
            center alpha 0.0
        with charamovechangefaster

        show kenji:
            ypos 1.14
            ease 1.0 alpha 1.0
        hide crowd

        "As we take our seats at a miraculously free table, I try to think of something that would actually interest him at all. I hope I can come up with an acceptable topic."

        hi "I found an answer to that question you asked a couple of weeks back. Where Lilly's non-Japanese half comes from, that is."

        show kenji happy
        with charachange

        ke "Good man. It's Russia, right? Totally Russia."

        hi "Scotland."

        show kenji tsun
        with charachange

        "He's visibly stopped in his tracks."

        ke "…Scotland?"

        hi "Yeah, that was my reaction too. She can speak English fluently and everything."

        show kenji rage
        with charachange

        ke "…Damn it! Do you realize what this means? How terrifying this news is to me?"

        menu:
            with menueffect
            "I think he's hyperventilating. Passing out for a little while would probably make him more relaxed than he normally is."

            "Humor him.":
                call a3lc1o1

            "Ignore his insane ramblings.":
                call a3lc1o2

        hi "You're kidding me. You made a bet about her nationality?"

        show kenji tsun
        with charachange

        ke "One of the dudes in my class was bugging me about it. I gave him some of my wisdom, and he had the audacity to say my logic was wrong."

        hi "So what did he think?"

        ke "Eh, Germany or something. It doesn't matter. What matters is my 1000 yen."

        show kenji rage
        with charachange

        ke "Damn, this day is ruined thanks to her. What a bitch."

        show kenji tsun
        with charachange

        "He looks utterly devastated as he wolfs down several clumps of his soggy soy-soaked rice. It only takes a few mouthfuls before he pokes his chopsticks at me, stabbing the air repeatedly in revelation."

        ke "Why… mm… mm… would… mm…"

        hi "Didn't your mother ever tell you not to speak with your mouth full?"

        "He gives me a dirty look before choking down the rest of the food left in his mouth and taking a gulp of juice. It's rather unsightly."

        "Remembering my own food sitting in front of me, I decide to get the task of eating the cafeteria food over and done with as fast as possible. The sooner I do so, the sooner the experience will be over."

        show kenji neutral
        with charachange

        ke "So as I was saying,"

        show kenji tsun
        with charachange

        ke "Why would anyone want to live in that place anyway? I mean, what is there to see? Grassy plains. That's it. Lots and lots of grassy plains."

        ke "And men in kilts."

        "I'm not sure which is worse, this food or his world view. I can feel my face being dragged down by their combined weight. Not that he'd notice, or care."

        hi "It's not that bad. Why do you care about her so much anyway? She's just your class representative, after all."

        show kenji neutral
        with charachange

        "He gives a malevolent chuckle. Were this anyone but Kenji, I'd feel uneasy at how he sounds."

        ke "I finally found the chink in the feminist legion's armor. It took a while, but I'm confident that this is going to be how we can bring down the whole system."

        show kenji happy
        with charachange

        ke "I'm about to blow your mind. Are you ready?"

        stop music fadeout 2.0

        "I tune out his rambling for a moment as I finish my rice and start on the unappetizing soup. One taste is enough to confirm that it's cold."

        hi "Ready as I'll ever be."

        show kenji happy
        with charachange

        ke "I confirmed that Lilly is in the Mafia."

        play music music_kenji

        hi "What."

        show kenji neutral
        with charachange

        ke "All right, stay with me for a second here, and I'll describe the scene."

        "I wish I could do otherwise."

        ke "Lilly's there, walking down the street after school."

        hi "You're not stalking her, are you?"

        show kenji tsun
        with charachange

        ke "No! Damn man, I do have some sense of self-preservation."

        "But not dignity, or morals, or social standards…"

        show kenji neutral
        with charachange

        ke "Anyway, as I was saying. This car pulls up next to her, and guess who steps out? A man in a pinstripe suit. Waves her in, then the two leave just like that. I tell you man, she's under protection. Under. Protection."

        "A man in a… oh. I can see where this is going now. It takes effort not to sigh in exasperation."

        hi "Let me guess; this man was about average height, had a slightly slender build, had blonde hair, looked foreign, and smiled a lot?"

        show kenji rage
        with charachange

        "He looks positively stunned. I take advantage of the moment of quiet to quickly gulp a mouthful of cold soup."

        show kenji tsun
        with charachange

        ke "It seems you're more observant than I thought."

        show kenji neutral
        with charachange

        ke "Yes, I have chosen well."

        "He giggles a little, and nods to himself so dramatically that it looks comical. I can't tell whether that's intentional or not, and that fact makes me frown."

        show kenji happy
        with charachange

        ke "This has important ramifications, you know. If she really is connected to people like them, and we're smart about what we do with this information, we could turn this into our greatest weapon against the Student Council."

        show kenji:
            2.0
            "kenji neutral" with Dissolve(0.5)
            3.0
            "kenji happy" with Dissolve(0.5)
            1.0
            "kenji neutral" with Dissolve(0.5)
            4.0
            "kenji tsun" with Dissolve(0.5)
            repeat

        "Once he starts rambling into conspiracy territory, my juice suddenly becomes of much more importance."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=120}Only half-listening to his pontifications, my mind drifts to the matter of Lilly and her antipathy for Shizune."

        n "The past between them is steadily becoming more coherent, but I'm not even sure if I should be learning of her past this way. Indeed, even if I do work out what went on, it really doesn't seem like my business to go and interfere."

        n "…Damn, not having Lilly around is making my thoughts wander. I'm noticeably more bored and sullen without her company, and the same goes for Hanako. All we do during lunch any more is eat and play chess."

        n "Come to think of it, I need to go check on Hanako after school, too. Considering her much improved attendance, I'm guessing she's come down with something."

        stop music fadeout 2.0
        $ renpy.music.set_volume(1.0, 6.0, channel="music")

        nvl clear

        nvl hide dissolve

        scene bg school_scienceroom
        with shorttimeskip

        play sound sfx_normalbell

        mu "Oh, Nakai?"

        show muto normal at center
        with charaenter

        "I stop as I'm about to leave the classroom, turning on the ball of my heel to meet Mutou. He's holding out to me a couple of the worksheets we'd worked on during the day with his long, lanky arm."

        show muto smile
        with charachange

        mu "Would you mind giving these to Ikezawa? I'd normally ask one of the girls to do it, but I assume you'll be checking on her."

        "For a moment I briefly consider the possibility of that being more than an innocent prediction. I quickly discard the idea though, as it's hard to think of him acting in such a Machiavellian way. It's not in his nature."

        hi "Sure, no problem."

        scene bg school_girlsdormhall
        with locationskip

        play music music_night fadein 1.0

        "Walking up the hallway of the girl's dormitory, several ideas of why Hanako's been absent float around my head. The most obvious of them is just a simple cold."

        "That said, she may not even be sick at all. It's been almost a week since Lilly left, and despite her at least appearing to be normal, I've suspected she's somewhat more insecure about it than she's letting on."

        show bg at right
        with charamove

        "Eventually I come to Hanako's dormitory room, its simple brown door separating us. Her room's position next to Lilly's is extremely convenient, and probably a large contributor to their meeting in the first place."

        $ renpy.music.set_volume(0.5, 0.0, channel="sound")
        play sound sfx_doorknock2

        "Grimacing slightly at the prospect of her being sick, I rap my knuckles on the door."

        "…Silence. I listen intently for any sound of shuffling coming from inside, but I can't hear a thing."

        $ renpy.music.set_volume(1.0, 0.0, channel="sound")
        play sound sfx_doorknock2

        "I knock on the door again, slightly harder."

        "Still no answer. How strange."

        $ renpy.music.set_volume(0.5, 0.0, channel="sound")
        play sound sfx_dooropen

        show bg at center
        with charamove

        "A door opens behind me. A freckled and somewhat scrawny underclassman I don't recognize comes out and is briefly taken off guard by my presence."

        menu:
            with menueffect
            "Girl" "Uh… hi."

            "Ask about Hanako.":
                call a3lc2o1

            "Keep it to myself.":
                call a3lc2o2

        show bg at right
        with charamove

        $ renpy.music.set_volume(1.0, 0.0, channel="sound")
        play sound sfx_doorknock2

        "Scratching my head, I make one last attempt at getting Hanako to answer as I knock on the door one final time."

        hi "Hanako, it's just me. Mutou said to give you some stuff."

        "For a while, the attempt seems just as unsuccessful as the last. Just before I slip the sheets under her door, though, I can hear the handle rattling."

        play sound sfx_dooropen

        pause 1.5

        show hanagown distant at offscreenright
        with None

        show hanagown:
            xpos 1.0 xanchor 0.75
        with charamove

        "As the door opens halfway, I do my best to look Hanako over as quickly as possible. It's a task made somewhat more difficult by her oversized gown hiding so much of her body."

        "She doesn't look sick, or at least not immediately so. To be honest, I'd have preferred that to her expression right now."

        hi "Hi, Hanako. Mutou wanted me to give you these since you weren't in class today."

        "I hold out the loose sheets, which she tentatively takes in her hands. The way she moves is weird, devoid of thought, as if she's some kind of mechanical automaton rather than a living being."

        hi "Are you… okay? If you're feeling sick or anything, I could get the nurse."

        "It feels almost pitiful to put on such a routine 'get well soon' act. I can't think of anything else I could possibly do for her, though."

        show hanagown normal:
            xanchor 0.7
        with charamovechangefaster

        "She seems to collect herself a little at the notion… but only a little."

        show hanagown distant_blush
        with charachange

        ha "I'm fine."

        hi "Okay."

        stop music fadeout 6.0

        pause 2.0

        show hanagown at offscreenright
        with charamovefaster

        hide hanagown

        play sound sfx_doorclose

        "An awkward silence follows, eventually ended by her nodding solemnly in farewell and closing the door. The entire experience feels surreal."

        "More than a little put off, I wander back to my room and hope that she'll be better by tomorrow, despite not knowing exactly what's wrong with her."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .dissonance:
        show bg school_girlsdormhall at right
        with locationchange

        "Once again, I find myself in front of Hanako's door after another of her unexplained absences from class."

        play sound sfx_doorknock2

        "…"

        play sound sfx_doorknock2

        "…"

        "Nothing. Considering this is the second day in a row she's been like this, I'm starting to worry about her."

        "Summoning my willpower, I decide to try one last way to get her to respond."

        hi "Hanako, if you don't say anything I'll go get the nurse for you."

        ha "…Go away."

        play music music_hanako fadein 10.0

        "Wh… what? It's hard to tell whether her tone's one of depression, anger, or both. What in the world can I actually do to help her, if she doesn't even want help?"

        "The message is clear enough. I can't just leave her like this, though; just sitting in her room for days on end."

        "Rubbing my temples in thought, I withdraw to my own room to think about how to proceed. Rationality is what's needed here, as an overreaction may just make matters worse."

        scene bg school_dormhisao
        with shorttimeskip

        "I dig around drawer after drawer of my desk, looking for where I put that damned piece of paper."

        "Before she left, Lilly told me the number to call her on while in Scotland and I wrote it down. Now that I need it though, the damned thing is—"

        "Ah. Here."

        "I probably should have just entered it directly into my cell phone, come to think of it. Without further ado, I enter the numbers and anxiously press the call button."

        scene bg school_dormhisao_blurred
        show phone mobile:
            truecenter
            alpha 0.0 ypos 0.7
            easein 1.0 truecenter alpha 1.0
        with locationchange

        pause 0.5

        "The fact the phone rings at all shows that I got the prefix for a call to Scotland right at least. I've never made an international call before, so that's some comfort."

        "Eventually the phone picks up, a feminine voice I don't recognize on the other end. It's probably Lilly's mother."

        $ renpy.music.set_volume(0.5, 0.2, channel="music")

        mystery "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou {image=vfx/garbage.png}?"

        "English? Suddenly finding myself unprepared, I realize I can't understand a word she says, either due to my limited vocabulary or her heavy accent. I should have anticipated this, since according to Lilly, her mother is a native Scot."

        "I soldier on in the hope that she must know some Japanese, considering it's her daughter's native language."

        hi "Um, it's Hisao Nakai… speaking…"

        "An enthusiastic sound of realization can be heard as she recognizes the language. My feeling of relief is immense."

        "Mrs. Satou" "Ah, you must be one of Lilly's friends from school, correct?"

        "Even so, her accent means I have to concentrate to work out what she's saying."

        hi "Yes, that's right. Pleased to speak to you, Mrs. Satou."

        "Mrs. Satou" "It's so nice of her to find someone so polite! Lilly dear, it's for you!"

        "Her mother seems nice, if a little overenthusiastic given the mundane situation."

        "There's a small silence as Lilly takes her time getting to the phone. In the distance, I can just make out her mother scolding her playfully for just getting up."

        $ renpy.music.set_volume(1.0, 5.0, channel="music")

        li "Hello, Lilly speaking."

        hi "You sound awful."

        "She makes a sound somewhere between a dying animal and a yawn."

        "The one thing I did remember to check before calling was the time zone. It'd be pretty late in the morning over there, so she really has no excuse."

        hi "Not feeling well?"

        li "Just tired. What time is it there?"

        hi "Late afternoon. School finished for the day not long ago."

        hi "You're really not a morning person, are you?"

        li "I don't need you making fun of it as well…"

        "It takes me a measure of restraint not to laugh at her pained groan. Poor girl."

        hi "How're you doing over there then, bar the mornings?"

        li "It's been enjoyable. After not meeting them for so long, just having a meal together with my parents is nice."

        li "Though the pool and the sheer size of the house might have something to do with that as well."

        "Even if they're not in Japan, from the way it sounds her family must be pretty wealthy to live so luxuriously."

        li "Are things all right with you and Hanako?"

        stop music fadeout 0.3

        "Damn, I was hoping that wouldn't be brought up quite so quickly."

        "I take a moment to try and sort out exactly how to describe the situation without causing her undue worry, but she picks up on that without a word being said."

        play music music_moonlight fadein 2.0

        li "Hanako's not well, is she?"

        hi "How did you know?"

        li "Because today is her birthday. I'd hoped she might have gotten at least a little better after coming to know you, but…"

        li "How is she right now?"

        hi "She missed school yesterday and seemed out of sorts when I checked up on her. Today she missed school again, and just told me to go away."

        hi "I've really got no idea what to make of it. Has this happened in the past? Is it related to her scarring in some way?"

        li "Unfortunately so. Roughly the same thing happened last year when her birthday came up."

        li "As far as I can tell, it's because her parents died in the accident that caused her scarring, and Hanako blames herself for their deaths."

        "What she says does seem to make sense. If she's blaming herself on her birthday, she may well be ruing that she was ever born."

        "The fact that Lilly seems so in the dark about it though, almost to the extent that I am, is a surprise."

        hi "So that's why she lives in the student dormitories, as well. Has she told you any more about the accident?"

        li "As close as we've come… she's very barely told me anything about what happened. What I know about it is largely conjecture."

        "She sounds depressed, almost defeated. Considering the trauma Hanako must have gone through, I really can't fault Lilly for not knowing. Nevertheless, she still seems to consider it a personal failing."

        hi "Don't blame yourself, Lilly. With everything she's gone through…"

        li "I know. Thank you, Hisao. I'm sorry I can't be of more help to you."

        hi "It's fine, I'll just give it some more thought. Thanks, and have a good time in Scotland."

        li "Um, I…"

        hi "Hmm?"

        li "It's nothing. Thank you for taking care of Hanako."

        hi "…Okay. Bye."

        li "Goodbye."

        stop music fadeout 4.0

        "And with that, the line goes silent."

        show phone:
            easeout 1.0 ypos 0.7 alpha 0.0

        scene bg school_dormhisao
        show phone mobile:
            truecenter
            easeout 1.0 ypos 0.7 alpha 0.0
        with locationchange

        pause 0.5

        hide phone

        "Amid the seemingly only increased number of questions I can't answer, the most immediate is what Lilly was going to say."

        "Oh. Oh no."

        "I'm an idiot. She must have thought I was calling to talk with her, but I only asked for help with Hanako."

        "Even more shameful than that thought is the fact that such an appraisal would be largely correct."

        "Well… first things first. For now, I need to at least sort out Hanako and make sure that she's actually eating okay."

        scene bg school_girlsdormhall
        with shorttimeskip

        "The occasional passing students give badly hidden glances at the plate of food I carry to the female dormitories."

        "It's hardly a meal to be proud of, only being an instant microwave meal from the convenience store, but it should at least fill her up."

        show bg at right
        with charamove

        "Eventually I arrive outside of her room, after having to ward off a couple of girls who jokingly tried to pilfer the food I'd taken so long to procure."

        "I decide to forgo knocking, since it was proven to be an utterly useless measure and it's somewhat difficult to do with my hands full."

        hi "Hanako, it's Hisao."

        hi "I know you're listening. I got some food for you."

        "Silence. As I expected."

        hi "I'll leave it beside your door. Please eat it at least, okay?"

        "There. I've said my piece. Now it's up to her."

        show bg at center
        with charamove

        "Putting the plate down, I walk back to my own room to eat my dinner."

        with shorttimeskip

        "By the time I return to Hanako's dormitory, a good hour's passed."

        "Thankfully, there isn't anything to be seen beside her door. I walk back at least somewhat happier that she's eating."

        "If she intends to get through this by herself, then being able to help, even if it's just in such a small way, is at least something."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .a_world_away:
        scene bg school_library_ss
        with locationchange

        play music music_pearly

        "I sit reading in the library after school, turning page after page, barely registering the words written on each out of sheer boredom."

        "With my cheek resting in my hand, I can't help noticing the slightly rough feeling against my palm. It won't be long before I'll need to get a razor."

        "Giving up on reading, I simply let my head drop onto the book in front of me."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=90}Things have quieted down considerably since Hanako began attending school again."

        n "When she first returned to class, nothing was said nor done that wasn't part of the usual routine, and it's been the same way since. Neither of us desired to bring up her accident, so there simply wasn't any point in pursuing it."

        n "Thus a few days went by, the daily grind continuing just as it had before."

        n "It's only natural that my mind would wander to other places, and more importantly, other people. The Lilly-shaped hole in the daily life of Hanako and me has been pretty noticeable for a while now."

        n "I'd be pleased to say that this has allowed me time to refine just what my thoughts on her exactly are, but alas, I've had no such luck."

        n "It doesn't help that many attempts to do so have led to the troublesome topic of Iwanako. Every time my thoughts drift into that direction, I reflexively try to think about something else."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")

        nvl clear

        nvl hide dissolve

        hi "Why did this have to happen now…"

        yu "Um…"

        show yuuko worried_up_ss at center
        with charaenter

        "I turn and look up to the source of the tentative voice coming from behind me."

        hi "Ah, sorry. I didn't mean to disturb anyone."

        show yuuko worried_down_ss
        with charachange

        yu "That's… not it."

        hi "Ah…"

        "I glance around the orange-tinted room, quickly realizing how silly my apology must have sounded. In the time I've spent thinking and lazing about in here, everyone's well and truly left."

        hi "Library closing?"

        show yuuko neurotic_down_ss
        with charachange

        yu "If you don't want to go, I could keep it open a bit longer. It's no trouble at all."

        hi "Don't worry, I should get going anyway. Thanks."

        show yuuko worried_down_ss
        with charachange

        "As I get up and begin to move off, I feel Yuuko's eyes drilling into my back."

        hi "Is there something wrong?"

        show yuuko worried_up_ss
        with charachange

        yu "You look depressed. Are you okay?"

        "Yuuko nervously twists her fingers as she says this, unsure whether she's overstepping her boundaries or not. I really can't tell if she's more worried about my mood or about bothering me."

        "Normally I'd just shrug it off and assure her that I'm fine, but my reflective mood gets the better of me. Despite being staff, she really doesn't feel as much like an authority figure as the others."

        hi "It's just… I guess the best term for it would be relationship problems."

        show yuuko worried_down_ss
        with charachange

        yu "Oh. I'm… not too good with that kind of thing. My only relationship ended a bit abruptly."

        show yuuko smile_down_ss
        with charachange

        yu "But if you want to talk about it, I mean, I could listen. I think."

        "Now I feel kind of bad for bringing it up. She's not that old, though, so at least she has a good chance of finding another partner."

        hi "It isn't like we're in a bad situation right now. We have spent many days together as friends, sometimes going out to do stuff… that kind of thing."

        hi "But I'm starting to want to do more for her, learn more about her, and be with her more. I'm not sure whether it's actually love or not, though, and our friendship as it stands is enjoyable."

        show yuuko panic_up_ss
        with charachange

        yu "You shouldn't let that stop you!"

        show yuuko worried_down_ss
        with charachange

        yu "Ah… sorry."

        show yuuko worried_up_ss
        with charachange

        yu "How to say this… um…"

        show yuuko neutral_down_ss
        with charachange

        yu "I think that it's nice that you have a good friendship, but school is going to eventually end. Do you think you'll be fine with not knowing if it could have gone further after you've graduated?"

        hi "I guess that's the crux of the problem. I really have no idea what the answer to that question is."

        show yuuko worried_down_ss
        with charachange

        yu "Well, I can't really help there. What your true feelings are is something you have to decide for yourself. But I think that if you do love her, you should definitely say something."

        show yuuko smile_down_ss
        with charachange

        yu "After thinking about it really hard, I decided that even though my relationship didn't work out, it's still better that way than never knowing if it might have or not."

        "I never expected Yuuko to sound so wise. It only makes sense that, with more life experience than I, she'd have a better idea about this."

        "While I suppose not very much was actually answered, talking to her has helped get it off my chest, and I have no doubt that I should confess if I really do like Lilly."

        "I give a slightly frustrated sigh."

        hi "If only reading so much actually helped when it comes to situations like this."

        show yuuko closedhappy_up_ss
        with charachange

        "She gives a girlish giggle, which only reinforces my view of her as being different from the usual staff here."

        stop music fadeout 9.0

        nvl clear
        nvl show dissolve

        n "{vspace=180}In the end, it all comes down to what will happen after school finishes once again."

        n "Considering what happened before I came to Yamaku, it feels like being asked to keep up with a field of runners despite having started from a dozen yards behind them."

        n "It's just one more motive to move on from the past. The last thing I need right now is to get too caught up in that and getting homesick while I'm at it."

        nvl clear
        nvl hide dissolve

        scene bg school_dormhisao_ss
        with locationskip

        "Once again, I find myself calling Lilly. My phone bill is going to be horrific, considering this is international."

        "But it's worth it. I don't only want to smooth over her feelings from the last time I called, I genuinely want to talk to her again."

        scene bg school_dormhisao_blurred_ss
        show phone mobile:
            truecenter
            alpha 0.0 ypos 0.7
            easein 1.0 truecenter alpha 1.0
        with locationchange

        pause 0.5

        "When the phone finally picks up, I easily recognize the voice on the other end."

        "Mrs. Satou" "{image=vfx/garbage.png} {image=vfx/garbage.png} Satou {image=vfx/garbage.png}?"

        hi "<Hello, Mrs. Satou. May I… uh… speak…>"

        "Damn. I've forgotten how the rest is supposed to go. It's not encouraging to forget such a small amount of words, even if I didn't spend that long trying to memorize them."

        hi "May I speak with Lilly, please?"

        "Mrs. Satou" "Hello again, Hisao. Are you teaching yourself English?"

        hi "Just a little. I don't think I'm too good at languages in general."

        "Mrs. Satou" "Oh, don't say that. Your pronunciation was good! I'll get Lilly for you, just wait a moment."

        "I obediently wait as she goes off in search of Lilly, the other end going silent."

        "Eventually a much more awake-sounding Lilly than last time answers, the time over there being past noon by now."

        play music music_comfort fadein 12.0

        li "Hisao, are you there?"

        hi "Yeah, I'm here. Hi."

        li "Good afternoon. Sorry for taking so long, I was outside in the garden."

        hi "Gardening?"

        li "Unfortunately I've found I'm no good at it, so I just smell the flowers. I think my fingers appreciate it more."

        li "I take it Hanako's recovered a bit?"

        hi "Yeah. I just made sure she was eating, and eventually she righted herself. Thanks for the help the other day."

        li "I don't think I was really that much help. The main thing is that she's better, though."

        hi "True. How's life over there, then? It sounds like you've been living in nothing short of a mansion."

        li "I wouldn't call it a mansion…"

        "'But it is rather large' is obviously what she wants to say, though modesty stops her. I'm a little envious, but it is her holiday."

        li "It's a nice house to stay in, though. There's a beach near here too, which Akira's especially fond of."

        hi "She's a swimmer?"

        li "She's constantly dragging me there to have swimming competitions. Which she wins. Every time."

        "Lilly doesn't strike me as very athletic at all, so not being adept at swimming seems logical enough."

        "The fastest I've ever seen her move is her understandably relaxed pace during her walks to and from the suburbs down the hill from the school. It makes the image of her swimming hard to imagine."

        hi "The beaches there must look nice. They'd be less crowded than the ones around here at least."

        li "Indeed, Akira says the area around here looks beautiful because it's so far outside the city."

        "I only realize what I've said after I say it, but it doesn't bother her at all. It's still easy to forget that she can't see when she's not around, despite the time we've been friends."

        li "That said, the local accent sometimes makes communication a bit hard. It's a constant reminder that this isn't home."

        "While the fact that she doesn't consider her parents' residence to be her home makes good sense, it makes me realize that I can't really answer whether the same goes for me."

        "Graduation from Yamaku is distant enough to be difficult to view objectively, and I've spent so much time in this small room. I've come to accept the dormitory as my new home surprisingly quickly."

        hi "I guess that would be hard to deal with. Is your knowledge of English holding up?"

        li "Thankfully. I may be fluent, but being in a position where I have to use it often helps in curbing my Japanese accent, so it's been useful practice."

        li "I hear you're trying to teach yourself English?"

        hi "More like memorizing a few lines, and failing at even that much. I'm really not cut out for learning another language."

        "My admission of defeat draws an amused giggle."

        li "I believe that there are things one chooses to do in life, and also things that are chosen for one to do in life."

        li "You can take comfort in the fact you're better than me in science and math, at least."

        hi "All that's helped in is making me Mutou's star student…"

        li "I wouldn't worry about it. They're useful skills for many jobs, right?"

        hi "That's what he tells me. His face veritably lit up when I said I'd probably go into a career involving either."

        "We both share a warm laugh at the events that have befallen each other on opposite ends of the world. It's nice, and reminds me of our simple smalltalk that I've been missing since she left."

        "As each of us waits for the other to begin speaking, I decide to push ahead with my feelings. I can feel my throat tightening slightly."

        hi "We… um, I… miss you."

        "The silence on the other end of the phone tells me she's given the words their due weight, but as it goes on I can't help feeling more and more apprehensive."

        "Thankfully the silence ends, almost as quickly as it had begun."

        li "I miss you too, Hisao."

        li "Goodbye."

        hi "Goodbye, Lilly."

        stop music fadeout 6.0

        "Once again, the phone is hung up; simply and without any further ado."

        show phone:
            easeout 1.0 ypos 0.7 alpha 0.0

        scene bg school_dormhisao_ss
        show phone mobile:
            truecenter
            easeout 1.0 ypos 0.7 alpha 0.0
        with locationchange

        pause 0.5

        hide phone

        "That light, tentative, almost shy voice. Her warm and soft tone… I'd simply be lying to myself if I were to say that I don't recognize this feeling for what it is."

        "With thoughts of Lilly dancing on my mind, I start anticipating her return. Today has been a most excellent day."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .renewal:
        scene bg school_scienceroom
        with locationchange

        "I sit listening to another of Mutou's long-winded lectures, my mind wandering far from the scribbles on the dirty blackboard."

        play music music_tranquil fadein 4.0

        nvl clear
        nvl show dissolve

        n "{vspace=60}Since I called Lilly, my mind's been drawn in two directions. Both, roughly, lead to the same conclusion; I've started to feel oddly detached from my past life."

        n "It's only been a month and a half since I arrived here, yet this school's become a second home. I've gained new friends and contacts, managed to get to grips with the school's lifestyle and culture, and become accustomed to the quirks of my classmates."

        n "To become used to a school where disabilities are the norm, rather than the rare exception, still catches me off guard sometimes when I think on it. The same school that's populated by burn victims, amputees, the blind, the deaf and all manner of disabilities inbetween."

        n "If someone had described this school to me before I'd come, I'd have shrugged it off as an overactive imagination. Even when I first arrived I felt like the Dutch, coming to this strange new land for the first time."

        n "It's amazing how quickly one becomes used to the environment they're forced to live in, really. And now I've even found someone that's got me entirely smitten. What a strange life."

        nvl clear
        nvl hide dissolve

        "Before my mind can wander any further, though, I find a page of lined paper slipped under my distracted face. The garish, bright pink ink has no doubt been penned by Misha."

        show misha hips_grin_close at offscreenleft
        with None

        show misha:
            xpos 0.1 xanchor 0.5
        show bg at left
        with charamove

        call screen written_note(_("{color=#FF2AAA}Don't look so bored, Hicchan! School's nearly over! Three-day holiday!{/color}"))

        "Oh, right, we get Saturday and Monday off. Can't complain about having less school, I suppose."

        "I uncap my pen and scribble on the page before covertly passing it back to her, flicking my eyes to the front of the class every now and then. Mutou continues scrawling away arcane equations and formulas on the board."

        call screen written_note(_("I'm guessing you have something planned?"))

        show misha perky_smile_close
        with charachange

        "Misha takes the paper back and hunches over it comically, even for her, with her tongue poking through the side of her mouth. Did she misinterpret my expression as depressed, and is she trying to cheer me up?"

        show misha sign_smile_close
        with charachange

        call screen written_note(_("{color=#FF2AAA}Student council work with Shicchan, of course.{/color}"))

        call screen written_note(_("You're not still brooding over that, surely?"))

        show misha hips_frown_close
        with charachange

        call screen written_note(_("{color=#FF2AAA}But Hicchan could have helped us poor, lonely girls."))

        call screen written_note(_("I'd lend you a hand for today if I weren't going to be busy."))

        show misha hips_grin_close
        with charachange

        call screen written_note(_("{color=#FF2AAA}Ooh, naughty naughty Hicchan!{/color}"))

        call screen written_note(_("I'm just going to meet Lilly with Hanako. I don't know what you've got going through your head."))

        show misha perky_smile_close
        with charachange

        call screen written_note(_("{color=#FF2AAA}So Lilly's back?{/color}"))

        call screen written_note(_("Yeah, she's coming on the evening flight with her sister, so she'll be back in school next week."))

        show misha hips_grin_close
        with charachange

        "As she takes the note back and begins to write, I look up to see an unwelcome sight."

        stop music fadeout 2.0

        show muto irritated behind misha:
            alpha 0.0 xpos 0.8 xanchor 0.5 yalign 1.0
            easein 1.0 xpos 0.6 alpha 1.0

        pause 0.5

        "While I frantically try to silently catch Misha's attention, Mutou confidently strides though the gap between the desks from the front of the class, his intent gaze focused directly on her."

        show muto:
            xpos 0.6 xanchor 0.5 yalign 1.0

        show misha perky_confused_close
        with charachange

        "She suddenly stops writing as his tall figure casts an impossibly long shadow over the page."

        show misha sign_confused_close
        with charachange

        mi "Ah… I…"

        "He silently takes the piece of paper from her and begins to read."

        "Sweating bullets, I quickly glance around the class, noting their complete silence. Of course, it would just have to be the one thing that actually gets their attention during the lesson."

        play sound sfx_impact
        show misha perky_sad_close
        with vpunch

        "After a scant few seconds examining the page, he rolls the paper up into a small tube and lightly bops Misha over the head with it."

        show muto normal
        with charachange

        mu "Half an hour until you can hop off to the Student Council. I think you can hold on until then."

        play music music_ease

        "Misha's face cracks as the entire class erupts into laughter. He might well be awkward, but he knows how to handle her excellently."

        "I'd probably feel sorry for her if I weren't as busy stifling my own laughter."

        scene bg hosp_ext at right
        show hanako basic_distant_cas at center
        with shorttimeskip

        play ambient sfx_rooftop fadein 2.0

        ha "Hisao, is that one it?"

        hi "No, I think that's some foreign airline."

        "And so, the third aircraft they're not on comes in to land."

        "For the past half hour we've been whiling away the time with small snippets of pointless chatter. Lilly and Akira's flight has been delayed, and at this rate it'll probably be dark before their plane arrives."

        show hanako def_worry_cas at twoleft
        with shorttimeskip

        ha "Is that one it?"

        hi "No, the company colors are wrong."

        show hanako basic_distant_cas
        with charachangealways

        show hanako basic_normal_cas
        with charachangealways

        "Hanako's eyes flutter left and right, following the trickle of people in and out of the huge glass doors ahead of us. Fortunately nobody pays her much heed, their attention apparently directed towards greater things."

        show hanako emb_timid_cas at tworight
        with shorttimeskip

        ha "Maybe that one is it?"

        hi "No, I think that's… hold on a minute, I think that one might be it after all."

        show hanako cover_distant_cas at center
        with shorttimeskip

        "It takes still some more time before the billboard changes their flight's status to 'disembarking.'"

        "A loud yawn sneaks up on me, not allowing enough time to stifle it. My sleep patterns have, once again, been all over the place; likely due to a mix of worrying about Hanako and the side-effects of my medications."

        show hanako emb_smile_cas
        with charachange

        ha "Hisao, over there…"

        "I look to Hanako, then follow her gaze to the airport door."

        aki "Hmm? Oh, Lilly, they're here!"

        li "Really?"

        show akira basic_smile:
            xanchor 0.5 xpos -0.3
        show lilly basic_cheerful_cas at offscreenleft
        with None

        show akira at left
        show lilly:
            xanchor 0.5 xpos 0.4
        show hanako at tworight
        show bg at center
        with charamove

        "We all call out to each other in greeting, quickly shuffling over to the side to avoid blocking the passage of others."

        ha "Lilly!"

        show hanako emb_downsmile_cas at center
        with charamovechangefaster

        "Hanako jumps forward to hug Lilly, a wide smile on her face being all that's needed to see her happiness at Lilly's return. Lilly simply smiles in return, her voice soft."

        show lilly basic_smileclosed_cas
        with charachange

        li "It's wonderful to meet you again, Hanako."

        show akira at twoleft
        show lilly:
            xpos 0.6
        show hanako at tworight
        show bg:
            xpos 0.55
        with charamove

        "As the two give each other a hug, well deserved after all that's happened while she was gone, I turn to Akira."

        show akira basic_ending
        with charachange

        aki "Yo."

        hi "You're pretty late."

        show akira basic_annoyed
        with charachange

        aki "Yeah, there was a really bad storm over the airport. We got drenched just going from the car to the door."

        hi "I guess you'll appreciate the weather here more, then. Welcome back to you too, Lilly."

        stop music fadeout 4.0

        show hanako basic_smile_cas:
            xpos 0.8
        show akira basic_smile
        show lilly basic_weaksmile_cas
        with charamovechangefaster

        "Hanako breaks off from Lilly as I speak. For a long time, neither of us says a word."

        "Contrary to what I'd thought her homecoming would be like, the atmosphere feels awkward, almost stifling. Both of us try to guess each other's feelings, not quite sure about what should be said."

        "Damn. This is exactly what I feared when I'd thought of trying to move things forward between us. Lilly runs her hand through her fair hair and awkwardly twirls one of her bangs in her fingers, clearly trying to think of how best to react."

        "Eventually, thankfully, Lilly gives a small sigh and breaks the silence."

        show lilly basic_smile_cas
        with charachange

        play music music_lilly fadein 6.0

        li "Thank you, Hisao. It's nice to be back."

        show hanako basic_worry_cas
        with charachange

        ha "Are you okay? You look tired."

        "Evidently not recollecting herself all that well, she quickly waves her hand in front of her face to stave off any concern Hanako may have over her."

        show lilly basic_weaksmile_cas
        with charachange

        li "I'm okay, really. It's just a bit of jet lag."

        show akira basic_laugh
        with charachange

        aki "Weak."

        hi "You don't have any?"

        show akira basic_ending
        with charachange

        "She simply gives a big grin, puffing out her modest chest."

        aki "I feel absolutely fine!"

        show lilly basic_sleepy_cas
        with charachange

        li "That's not fair…"

        show akira basic_smile
        show hanako basic_normal_cas
        with charachange

        aki "Haha, ah well. Ya shouldn't take too long to get rid of it."

        show lilly basic_smile_cas
        with charachange

        li "Ah! That's right, Hisao?"

        hi "Yeah?"

        show lilly basic_smileclosed_cas
        with charachange

        li "Don't we have a holiday from school soon?"

        hi "I'd have forgotten if Misha hadn't reminded me this morning. We've got a three-day weekend starting from tomorrow."

        show akira basic_laugh
        with charachange

        "Akira playfully bumps her elbow lightly into Lilly's side, grinning."

        show akira basic_smile
        with charachange

        aki "Told ya you wouldn't miss it."

        hi "You have something planned?"

        show lilly basic_smile_cas
        with charachange

        li "If neither you nor Hanako are busy…"

        hi "I've got no plans, so something to do would be appreciated. Hanako?"

        show hanako basic_smile_cas
        with charachange

        ha "No, nothing."

        show lilly basic_cheerful_cas
        with charachange

        li "That's good. I was thinking we could go to my family's summerhouse for a bit of quiet over the break. We've rarely used it recently, though, so we'd have to dust things off a little while we're there."

        hi "Oh? Where is it?"

        show akira basic_ending
        with charachange

        aki "Up north, in Hokkaido. The place is practically deserted, so it should be a nice quiet break for you guys."

        hi "You're not coming?"

        show akira basic_smile
        with charachange

        aki "Nah. Got a little holiday of my own set up with my boyfriend."

        "I lower my eyes at her, suspicious of her intentions."

        hi "It sounds like we're just cleaning up the summerhouse for you."

        show lilly basic_displeased_cas
        with charachange

        li "That's… perhaps a valid conclusion…"

        "Both of us zero in on Akira, her face somewhat evasive. Looks like we were right."

        show akira basic_boo
        with charachange

        aki "That's just a convenient bonus. Really. Me and the guy left it in pretty good condition last we were there, I promise."

        show akira basic_smile
        with charachange

        aki "Now then, I'm outta here."

        show lilly basic_reminisce_cas
        with charachange

        li "Already? Akira…"

        "She quickly turns and walks away, her hand held high."

        show akira basic_laugh
        with charachange

        aki "See ya in a few days, guys."

        show akira:
            offscreenleft
            linear 2.0 alpha 0.0
        with charamove

        hide akira

        show lilly:
            xpos 0.4
        show hanako:
            xpos 0.6
        show bg at bgleft
        with charamove

        "Lilly and I can only sigh at her hasty retreat."

        show hanako cover_bashful_cas
        with charachange

        ha "It does sound like it would be a nice place to go."

        show lilly basic_smileclosed_cas
        with charachange

        "Lilly gives an enthusiastic nod, taking her carry bag in one hand and placing her other on Hanako's shoulder for guidance as we begin to make our way to the taxi area."

        "After the fracas of the past few days, spending a weekend in the country alone with her and Hanako sounds like a dream."

        "The more I think about it, the more sure I am. This will be the right time and place to confess my feelings to her."

        stop music fadeout 2.0
        stop ambient fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .northern_sojourn:
        scene bg city_station
        with locationchange

        play music music_daily fadein 7.0

        "The morning chill wraps itself around my shivering body. I huff into my cupped hands to desperately try and stave off the cold as we mill about on the station platform."

        "Lilly's clothing looks rather ill-suited for the temperature around us. I can only hope it's indicative of what she expects the weather to be like at our destination."

        show lilly basic_sleepy_cas at twoleft
        show hanako basic_distant_cas at tworight
        with charaenter

        hi "Dammit, Lilly, why'd we have to get here so early?"

        show lilly basic_displeased_cas
        with charachange

        li "Unfortunately the train schedule is against us. The next train to Hokkaido is at two in the afternoon."

        hi "Great. Just great."

        "I pause a moment to wipe some sleep out of my eyes, and Lilly promptly takes advantage of the opening."

        show lilly basic_weaksmile_cas
        with charachange

        li "Cheer up, Hisao. Once we get there it'll be much warmer."

        hi "Why not just take the bullet train? A normal train's going to take hours to get us there, so we may as well take the Shinkansen line as far north as it goes, and just switch at the end."

        show lilly basic_smile_cas
        with charachange

        li "There's a certain charm to older trains, wouldn't you agree?"

        hi "I'd agree if I weren't freezing in the morning cold because we decided to take one."

        show hanako emb_timid_cas
        with charachange

        ha "I'm… sorry, Hisao."

        hi "Sorry? What for?"

        show hanako emb_downtimid_cas
        with charachange

        ha "I was… the one who suggested taking a normal train."

        "Way to make me feel guilty. All I can do is sigh and cover my face with my hand."

        hi "It's fine, I'm just grumbling."

        show lilly basic_ara_cas
        with charachange

        li "My my, Hanako, you needn't shoulder all the blame yourself. Even without your suggestion, I'd still have opted for the same thing."

        show hanako emb_smile_cas
        with charachange

        hide hanako
        hide lilly
        with charaexit

        "Thankful for the quick interception from Lilly, I take a quick gander around the station."

        "Aside from us, the train platform's all but deserted, the morning dew settling on the empty benches. I guess no one else was masochistic enough to brave the very early morning."

        "Though if someone was, they'd more than notice the huge bags both Lilly and Hanako brought with them."

        hi "Just what did you have to pack into those things, anyway?"

        show lilly basic_listen_cas at center
        with charaenter

        li "The bags? Hmm…"

        "She pauses a moment and tilts her head in thought."

        show lilly basic_smileclosed_cas
        with charachange

        li "A change of clothing, raincoat, underwear, sleepwear, a number of books… I think that's most of it."

        hi "You make it sound as if I'm unprepared."

        show lilly basic_surprised_cas
        with charachange

        li "You brought less?"

        hi "Underwear and a pack of cards. That's it."

        "And my pills, but never mind that."

        li "No pajamas?"

        hi "Damn. I knew I forgot something."

        "As I ruffle my hair in frustration, Lilly sighs."

        show lilly basic_weaksmile_cas
        with charachange

        li "There should be clothes you could use there. Akira still occasionally goes there, after all, and I think some of our parents' clothing is still in storage."

        show lilly basic_smile_cas
        with charachange

        li "I don't think there'll be any problem with you borrowing a set of pajamas, if need be."

        hi "Thanks. Still, I don't mind just sleeping in my normal clothing."

        show lilly basic_surprised_cas
        with charachange

        li "For two days?"

        hi "Good point."

        "Not really. Though two days would be borderline, it's more that looking even a little like a slob would be unacceptable while in the presence of two girls."

        hide lilly
        with charaexit

        "As we leisurely talk on the station platform an announcement sounds from the loudspeakers, loudly heralding our ride's arrival."

        "Looking past Lilly and Hanako, though, the train's still well out of sight. A quick check of my watch is enough to see that it's the one we'll be taking."

        hi "The five-thirty train was ours, right?"

        show lilly basic_smileclosed_cas at twoleft
        show hanako basic_distant_cas at tworight
        with charaenter

        li "Correct."

        hi "Either of you want me to take your bags? Mine's not exactly heavy."

        show lilly basic_ara_cas
        with charachange

        li "My my, that's very gentlemanly of you, Hisao."

        hi "Don't accept too reluctantly, now."

        "As I bend down to pick up Lilly's large bag, I look up to see Hanako picking up hers."

        hi "You fine with that?"

        show hanako basic_normal_cas
        with charachange

        "A silent nod's the only answer. I'm starting to get the feeling that by the trip's end, I'll be able to count every sentence she said on one hand."

        stop music fadeout 5.0
        play ambient sfx_trainint fadein 5.0

        scene train_scenery
        show train_scenery_fg
        show evfg lilly_trainride at train_shake
        with shorttimeskip

        "With the morning landscape passing by the window and the occasional rattle of the train bumping the carriage around, I try to focus my attention on the aging playing cards held in my hands."

        hi "I'll raise you five."

        ha "Um… I…"

        "She scrunches her face up and leans over to Lilly conspiratorially, the two exchanging a few whispered words. Considering how often this has happened so far, I'm coming to doubt Hanako's grasp of how to play poker."

        "It doesn't seem to disturb Lilly's reading though, her hands flitting over each page with only occasional corrections to account for the train's bumping and rocking."

        "My collection of chess pieces that we're using as chips is steadily growing anyway, so it doesn't really bother me."

        "Looking around us, our carriage is almost as empty as the station platform we'd waited for the train itself on. Only a handful of people can be seen, looking mostly like tourists and couples on holiday."

        "While the two continue their less-than-clandestine strategizing, a small boy looks over the seat and stares at me. Hoping he doesn't begin to stare at Hanako, I simply give him a wave and a smile."

        "Thankfully, he retreats back to his seat after finding me far too boring to waste his attention on."

        ha "I'll see you and raise you… another five."

        hi "Damn, you got me. I fold."

        "I've been bluffing, and she's caught me. Hanging my head, I push over a large portion of my winnings."

        show evfg lilly_trainride_smiles
        with charachange

        "Hanako looks absolutely delighted, and even if Lilly keeps her attention focused on her reading material, I can see the smirk on her face. They're both extremely pleased."

        "For a moment I try to work out what Lilly's reading, but the cover is too faded to read beyond the fact that Roman letters are on it. A pity I can't read the Braille above the printed title."

        hi "What're you reading, Lilly? The title looks like it's in English."

        li "That's right. It's 'And Then There Were None', an old British story. I could read it to you if you'd like."

        "She extends the offer with a grin, obviously in jest."

        hi "I think I'll pass, thanks."

        stop ambient fadeout 2.0

        scene bg hok_houseext:
            xalign 1.0
            warp acdc_warp 10.0 xalign 0.0
        with shorttimeskip

        play music music_tranquil fadein 3.0
        play ambient sfx_parkambience fadein 4.0

        "After a seemingly endless trip, we finally reach the promised land of the Satou summerhouse. Even after the train trip, the walk up seemed to take forever."

        "Despite my grumblings though, I'd have never guessed the sight that would be in store for us once we traveled that long, deserted road."

        "It looks more like a farmhouse than the everyday house I'd imagined, small in size and surrounded by trees and bushes."

        "An empty expanse of wheat fields and farming land can be seen as we walk up, the fencing only consisting of rickety old wooden planks."

        "It really drives home how far we are from the major cities and is a sight that feels antithetical to the environment I grew up in."

        "The only thing that doesn't surprise me is its Western styling."

        show bg at left

        hi "Wow, it's amazing out here…"

        show lilly basic_smileclosed_cas at twoleft
        show hanako basic_bashful_cas at tworight
        with charaenter

        ha "Mm, it's wonderful."

        show lilly basic_smile_cas
        with charachange

        li "That's nice to hear. While Akira may have said that she's kept the house in reasonable condition, I was worried that we might have different standards of 'reasonable.'"

        hi "It looks like there isn't another soul for miles. I thought Akira would be the type to keep to the city."

        show lilly basic_listen_cas
        with charachange

        "Lilly furrows her brow in thought, seemingly recalling almost forgotten knowledge."

        show lilly basic_weaksmile_cas
        with charachange

        li "Hmm, from memory there's a small town not too far ahead. Other than that though, this is largely just old farmland."

        show lilly basic_smile_cas
        with charachange

        li "Akira and I stayed in our parents' house which was in the nearest city for a while, but after they left we decided to move into a smaller, more easily maintainable, house."

        hi "To find a place like this in Japan nowadays… it's kind of anachronistic."

        show lilly basic_smileclosed_cas
        with charachange

        li "Well, this town does have quite a bit of history."

        "I look down the street one last time before getting back to the task at hand."

        hi "Shall we go in, then? I'm parched."

        show hanako basic_normal_cas
        with charachange

        ha "It was a long walk to get here."

        show lilly basic_smile_cas
        with charachange

        "Lilly gives an enthusiastic nod, the three of us lugging our bags into the house."

        stop ambient fadeout 1.0
        $ renpy.music.set_volume(0.7, 1.0, channel="music")

        scene bg hok_lounge
        with locationchange

        "As soon as we set foot inside, Hanako and I start looking around, taking in every detail of where we'll be staying for the next few days."

        "All the artifacts of another's life stopped mid-motion are around the house, such as the television guide lying beside the counter it was on, and pans in the adjoining kitchen still sitting on the stove."

        "It's a strange feeling, really; as if we were stepping into Akira's life for a brief moment, before leaving in a couple of days just as we'd come. Of course, the more mundane reality is that she just hasn't cleaned up after herself that well."

        hi "Where should we put our bags?"

        show lilly basic_smileclosed_cas at twoleft
        show hanako basic_normal_cas at tworight
        with charaenter

        li "I'll show Hanako our bedroom. You can put yours here, if you like."

        hi "You mean I don't have the same bedroom as you two?"

        show hanako emb_blushing_cas
        show lilly basic_emb_cas
        with charachange

        "Hanako flowers into a full blush as Lilly takes her cheek in her hand."

        show lilly basic_ara_cas
        show hanako emb_emb_cas
        with charachange

        li "Oh my, how bold."

        "You two…"

        hi "Hold on, if I'm to leave my bags here, where will I be sleeping?"

        show lilly basic_weaksmile_cas
        with charachange

        li "Well, seeing as we lack a guest bedroom…"

        hi "The convertible futon, huh?"

        show lilly basic_concerned_cas
        with charachange

        li "Sorry, Hisao."

        "I sigh, lamenting my place on the bottom rung of sleeping location priorities."

        hi "I guess there's no other choice."

        hide lilly
        hide hanako
        with charaexit

        "Lilly leaves to show Hanako to their bedroom, so I take a small tour of my surroundings after I drop my bag on the floor."

        scene bg hok_kitchen
        with locationchange

        "The kitchen, just like the living room, is fairly modest. The rustic nature of the wooden furnishings drives home just how far we are from civilization."

        scene bg hok_lounge
        with locationchange

        "Returning to the living room, I decide to try out the television until they get back. With a touch of the remote it immediately flickers to life, apparently set to a news channel."

        "Almost flopping down from exhaustion rather than sitting, I lay back and watch."

        stop music fadeout 5.0
        $ renpy.music.set_volume(1.0, 8.0, channel="music")

        "And watch."

        "And watch…"

        scene black
        with shuteye

        pause 4.0

        ha "Hisao…"

        play ambient sfx_cicadas fadein 5.0

        scene bg hok_lounge_ni
        show lilly basic_smileclosed_cas at twoleft
        show hanako basic_normal_cas at tworight
        with openeye

        "I quickly blink to wake myself up, Lilly and Hanako having returned minus their bags."

        "From the Hokkaido night sky visible outside the windows, it looks like I drifted off to sleep. Looking to the wall-mounted clock, it's already ten."

        show lilly basic_weaksmile_cas
        with charachange

        li "You've found the television, then."

        hi "Yeah. It really does feel nice and homey, here."

        show lilly basic_smile_cas
        with charachange

        li "I'm glad you like it."

        show lilly basic_giggle_cas
        with charachange

        li "You were already out like a light when we came back after unpacking our things, so we didn't have the heart to wake you sooner."

        "Judging from her giggle, I must sound funny when I sleep. I swiftly decide not to inquire."

        show hanako emb_smile_cas
        with charachange

        ha "There's some dinner waiting for you in the kitchen…"

        show hanako emb_downtimid_cas
        with charachange

        "Hanako gives a deep yawn, only just remembering to cover her mouth at the last second. "

        show lilly basic_weaksmile_cas
        with charachange

        li "My my, are you tired?"

        show hanako emb_timid_cas
        with charachange

        ha "Ah, mm. I didn't get much sleep last night."

        hi "I'm pretty tired too. It was a long walk up here, and it's getting late."

        show lilly basic_smileclosed_cas
        with charachange

        li "If that's the case, I suppose we should retire for the night. Good night, Hisao."

        show hanako basic_smile_cas
        with charachange

        ha "Good night."

        hi "'Night."

        hide hanako
        hide lilly
        with charaexit

        "With that, they quietly turn and walk back to their bedroom."

        "Rubbing my eyes, I sigh. I wonder if I'll be able to get back to sleep after being woken up."

        "I suppose I'll eat something and watch some more TV quietly before going to bed."

        stop ambient fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .prelude:
        scene black
        with dissolve

        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
        play ambient sfx_parkambience fadein 6.0

        ha "Is he still sleeping?"

        li "I think so."

        "I'm not. I am, however, incredibly tired."

        ha "It's getting late in the morning…"

        "I know that."

        li "He likely stayed up to watch television. I could hear it from our bedroom."

        "Only because I couldn't get to sleep."

        ha "Should we wake him?"

        "Don't do that, Hanako. Please."

        li "No, we should leave him. I doubt he'd want to be woken early if he didn't get much sleep during the night."

        "Thank you, Lilly."

        li "Besides, he sounds so peaceful. It would be a shame to wake him when he's like this."

        "Keep a straight face, Hisao. It is nice she cares so much, though."

        ha "Um…"

        li "Hanako, could you go to the fridge and fish out what's needed to make lunch?"

        ha "All right, just the vegetables and rice?"

        li "Mm, that should be enough. We only need something simple, as we can eat in town later."

        "Hanako's footsteps on the carpeted floor can be heard, moving away from the living room. As they do, I feel Lilly's hand gently rest on my chest."

        "It takes a titanic effort not to react, but something about her makes me think she knows I'm awake."

        "A long silence passes."

        "The only thought in my mind is of that gentle, outstretched hand laying upon my chest. After an indiscernible amount of time, Lilly withdraws her hand."

        li "Good morning, Hisao."

        $ renpy.music.set_volume(1.0, 3.0, channel="ambient")
        play music music_dreamy fadein 8.0

        scene bg hok_lounge
        show lilly basic_smileclosed_cas at center
        with openeye

        "Conceding defeat all too easily, I prop myself up and rub my eyes."

        hi "How'd you know?"

        show lilly basic_weaksmile_cas
        with charachange

        li "Your breathing was off."

        "While that makes sense, she couldn't have needed that long to work it out. Knowing her hearing, she likely knew before laying her hand on me."

        show lilly basic_displeased_cas
        with charachange

        li "If you want to sleep more, you should really go to bed earlier. I heard the television going long into the night."

        hi "Sorry about that. My medications have been interfering with my sleep for a while now. Even if I'm tired I have trouble actually sleeping."

        show lilly basic_oops_cas
        with charachange

        li "I'm… sorry for bringing it up, Hisao."

        menu:
            with menueffect
            "I sigh. This is exactly the kind of thing I wish others wouldn't do."

            "Address it." if True:
                $ address_it = True

                call a3lc3o1
            "Wave her off." if True:
                $ address_it = False

                call a3lc3o2

        "For a while I sit and watch television in an attempt to wake myself a little more, but it's futile. I don't have anything better to do, so I follow Lilly's lead."

        stop ambient fadeout 5.0

        scene bg hok_kitchen
        with locationchange

        "As I round the corner, I see Hanako and Lilly, backs turned, quietly cutting food on the granite-colored counter."

        "I am temporarily engrossed as I watch Lilly guiding the knife down carefully with a finger on the cabbage she's cutting, each slice delivered slowly but with precision."

        "She seems a little slow, but considering that she can't see what she's doing it's a small wonder she can cook at all, let alone for both her and Hanako."

        hi "Hi Hanako, Lilly. Want any help?"

        show lilly back_surprise_cas at twoleft
        show hanako basic_normal_cas at tworight
        with charaenter

        stop music fadeout 0.3

        call screen doublespeak(li, _("Is that Hisa— ah!"), ha, _("Oh, 'morning Hisao."))

        show lilly basic_oops_cas
        with charachange

        "Lilly jerks back in surprise before turning around, her yelp immediately drawing Hanako and me to her side."

        hi "What's… ah."

        "A small trickle of scarlet falls downward from her pale fingertip, the knife having cut just deep enough to draw blood."

        "With the television's sound masking my footsteps, she must not have noticed me coming. To compensate for having to use touch to guide everything she does during cooking, she must need to pay extra attention."

        show hanako defarms_shock_cas
        with charachange

        play music music_dreamy fadein 8.0

        ha "Lilly!"

        show lilly basic_weaksmile_cas
        with charachange

        li "Don't worry, Hanako. It's just a small wound."

        hi "You should still get a band-aid on it, at least until it stops bleeding. First aid stuff would be in the bathroom, right?"

        show lilly basic_sleepy_cas
        with charachange

        li "I think so. Will you be okay here, Hanako?"

        show hanako cover_worry_cas
        with charachange

        "I frown at how little heed she's paying to herself as Hanako gives a quick, almost automatic, nod."

        show hanako basic_worry_cas
        with charachange

        ha "It's fine, I can keep making lunch."

        scene bg hok_bath
        with locationskip

        "An awkward silence reigns as I set the bottle of antiseptic and box of band-aids on the side of the sink, Lilly's finger held out for me to treat."

        "The lid of the bottle comes off with a minimum of resistance, and the small ball of cotton I soak in the liquid stains a pale green."

        hi "Okay, hold still. This'll probably hurt a bit."

        show lilly basic_weaksmile_cas_close at center
        with charaenter

        "She gives a small nod as I take hold of her hand to steady it. With all the tenderness I can muster, I gently bring the dampened wad to the small red line."

        show lilly basic_oops_cas_close
        with charachange

        li "Ah!"

        hi "What? I've barely touched it."

        show lilly basic_reminisce_cas_close
        with charachange

        li "Sorry…"

        "I give a sigh, both at her reaction and to settle my own nerves. Her pain tolerance is startlingly low."

        hi "I would tell you to man up, but I can't really do that."

        show lilly basic_weaksmile_cas_close
        with charachange

        "As she gives a small giggle, I take advantage of her momentary distraction and gently press the cotton against her finger a few times. Thankfully, it's enough to do the job."

        "We both settle somewhat as I bring the band-aid over the tip of her finger, covering the wound while making sure not to get it stuck to her fingernail."

        hi "There, finished. You can move now."

        "Taking her hand from mine, she gently clasps it in the other."

        show lilly basic_smileclosed_cas_close
        with charachange

        li "Thank you."

        hi "It's no problem. It's the least I can do after causing you to hurt yourself, after all."

        show lilly basic_emb_cas_close
        with charachange

        "She lowers her head slightly at the apology, absentmindedly rubbing her hand in what seems to be embarrassment."

        show lilly basic_weaksmile_cas_close
        with charachange

        li "I really don't mind."

        stop music fadeout 5.0

        "Her answer doesn't seem to make much sense, given that what happened is pretty clearly my fault."

        "I can't help grimacing at her, despite the fact that her dainty smile still holds. She must not like being reminded of the limitations her lack of sight imposes on her."

        "It's something I can't possibly fault her for. I've fallen prey to the same kind of feelings before, despite my condition not being nearly as ubiquitous in my life."

        "Neither of us any the happier, we head back to the various smells of cooking food coming from the kitchen."

        scene bg hok_lounge
        with shorttimeskip

        play music music_another fadein 8.0

        "I lay out the plates of food, steam slowly rising from the well-cooked rice and curry dishes, while Hanako lays out the cutlery."

        "Knife one side, fork on the other. Western. How perfectly fitting for someone like Lilly."

        "As we take our seats, taking careful heed of the dark red tablecloth hanging below our knees, Lilly emerges from the kitchen."

        "In her hands are three glasses and… a bottle of wine?"

        "As I recall our previous run-in with that devilish elixir, I hide my face in my palm."

        hi "Alcohol? Seriously?"

        show lilly basic_cheerful_cas at center
        with charaenter

        "She pauses as she reaches the table, a playful grin perched on her face."

        show lilly basic_giggle_cas
        with charachange

        li "Akira specifically gave permission to take a bottle from her collection."

        "Not only does she give alcohol to minors, she even lets them pilfer their own? The perfect model of a responsible adult Akira is not."

        "More to the point, though, is that this is hardly a meal deserving of alcohol. I'm starting to think Lilly's the type to easily become hooked on things."

        hi "That's not really the problem. I don't really have any qualms with it, but didn't you have a bad experience with it last time?"

        show lilly basic_smileclosed_cas
        with charachange

        li "Last time was likely due to drinking too much, so a single glass shouldn't prove a problem."

        show lilly basic_smile_cas
        with charachange

        li "Think of it as a learning experience."

        hi "I can't recall many learning experiences that made me feel rotten before putting me to sleep, but I'll take your word for it."

        show lilly basic_smileclosed_cas
        with charachange

        "She dips an uninjured finger inside to feel the liquid level, tip against the bottom as the liquid rises up."

        "The white of her finger almost seems to glow as the sunlight hits it, the delicate outline blurred and refracted by the glass."

        "Her fingers are definitely longer than mine, the kind I'd think more suited to a pianist than a teacher. She'd likely have done well if she'd learned how to play."

        hide lilly
        with charaexit

        "We quickly dig into our meal, forks and knives clattering against plates."

        "None of us are particularly eager to speak while eating, Lilly altogether too reserved for such a thing, Hanako probably too shy to start conversation, and I too busy savoring the food."

        "Such a pedestrian activity, eating together at a table. It seems so utterly normal, yet it makes me realize how long it's been since I've done something like this."

        "Just the three of us, sitting around a single table eating as if we were a malformed family. Maybe this trip, as far away from everything as we are, was worth it."

        with shorttimeskip

        "It takes quite a long time, but eventually we all finish our surprisingly filling meal. The wine, thankfully, has little effect given we've only had a glass or two each."

        "I slump back into the seat, rubbing my stomach contentedly."

        hi "I'm stuffed."

        show lilly basic_smileclosed_cas at twoleft
        show hanako basic_smile_cas at tworight
        with charaenter

        "Lilly pats her mouth with a napkin. Twice, only twice, and with evenly timed intervals in between. It's hard to tell sometimes whether how she acts is a well-trained routine or a well-rehearsed act."

        show lilly basic_satisfied_cas
        with charachange

        li "I think I must be as well. Did you like it, Hanako?"

        show hanako cover_bashful_cas
        with charachange

        ha "Mm, it was nice."

        show lilly basic_smileclosed_cas
        with charachange

        li "Now that we're well fed, shall we be off?"

        hi "Off? Where?"

        show lilly basic_weaksmile_cas
        with charachange

        li "Ah, you weren't privy to the discussion between Hanako and me earlier."

        "I get the impression that she's having a subtle dig at my sleeping in."

        show hanako basic_bashful_cas
        with charachange

        ha "We'll be going into the town nearby."

        "I guess I should have expected two girls to take a holiday as an excuse to go shopping, no matter where on the planet they may be."

        "I am interested to see more around the north though, so this can only be a good thing."

        hi "Sounds good. How long's the walk in, then?"

        show lilly basic_smile_cas
        with charachange

        li "It's supposed be around a mile to a mile and a half."

        stop music fadeout 4.0

        hi "Nearby, huh? Great."

        "Just great."

        scene bg hok_road at bgright
        with shorttimeskip

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        play ambient sfx_parkambience fadein 6.0
        play music music_soothing fadein 0.5

        "As we climb up the path surrounded by trees and undergrowth, I watch Lilly and Hanako walking ahead."

        "The slight breeze all but whisks away the sound of Lilly's cane gently tapping on the ground. I notice that Lilly's since removed the bandaid now that the bleeding of her finger has stopped."

        "A deep, lung-filling breath of the fresh country air makes me wish all the harder that the air around home had been quite so clean."

        "It can't have even been half a mile, but I'm already working up a sweat. It isn't a pleasantly cool day, though, so I shouldn't be too hard on myself for it."

        hi "Hey Lilly, how well do you know this town, anyway?"

        show lilly back_smileclosed_cas at center
        show lillyprop back_cane
        with charaenter

        li "Since I spent quite a few of my vacations here up until I entered Yamaku, I'd say I know it fairly well. We used to drive there once a weekend then."

        "How I wish Akira was here to drive us now."

        "I quickly take a moment to rub my hands a couple of times, staving off the oddly cold feeling in them."

        hi "Did you like it up here?"

        show lilly cane_weaksmile_cas
        hide lillyprop
        with charachange

        li "I'd say it was nice during winter, but as you can work out, summers get a little too hot for comfort. It's nice and quiet, at least."

        li "My family's real house is quite far south. When they left Japan, my parents gave it to Akira and me. Only Akira lives there now, after my moving into Yamaku."

        hi "Well, quiet certainly describes this place."

        "Though lonely is how I'd put it."

        "Other than the prophesied small town, there isn't another soul for miles around. Coming from a home nestled deep within the big city, it's certainly different."

        "I think that if I'd not come to Yamaku, staying out in the country like this would be too much of a change to get used to."

        "After getting accustomed to the school's isolation, though, the idea of living in a place such as this has become almost inviting. To be somewhere away from the hustle and bustle of the metropolitan centers."

        show lilly cane_smile_cas
        with charachange

        li "So Hisao, have you been to Hokkaido before?"

        hi "Nah. I used to live down south, and we never had any field trips or holidays up this far."

        show lilly cane_cheerful_cas
        with charachange

        li "Well, it's a new experience for you then."

        hi "Yeah, it is. I'm surprised at how nice it feels here."

        hi "How about you, Hanako?"

        show lilly at twoleft
        show bg at center
        with charamove

        show hanako emb_smile_cas at tworight
        with charaenter

        "She shakes her head from side to side."

        show hanako basic_bashful_cas
        with charachange

        ha "It's my first time too."

        "As we continue walking, I begin to feel pins and needles in my legs. It's a little disturbing, given there's no reason for it to be happening."

        stop ambient fadeout 9.0
        stop music fadeout 4.0

        hi "Could you two hold on a moment? I just need to…"

        show lilly cane_surprised_cas
        with charachange

        li "Is anything wrong?"

        hi "Nah, I've just got pins and needles in…"

        play sound sfx_heartslow

        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.2)

        pause 0.7

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.8)

        pause 0.05

        play sound sfx_heartstop
        show heartattack alpha
        with Dissolve (0.1)

        show heartattack residual
        with Dissolve (0.8)

        play music music_tragic fadein 0.5

        "My vocal cords suddenly become taut as my chest tightens instantaneously. I quickly pull my upper arm over it, trying to quell the shot of pain spreading throughout my entire body."

        show lilly cane_reminisce_cas
        show hanako defarms_strain_cas
        with charachange

        li "Hisao?"

        "Lilly's face is only mildly concerned, not knowing the sight which Hanako's recoiling from."

        hi "I'm fine, I'm… fine. Just… tired…"

        "I remove my arm from my chest and force myself to begin walking again. It's just a minor heart flutter, so it'll pass like the others."

        play sound sfx_heartslow

        show heartattack alpha
        with Dissolve (0.1)

        show heartattack residual
        with Dissolve (0.8)

        "It only takes a couple of steps before my body violently revolts against me, my legs suddenly beginning to give way underneath me and all tension in my knees seeming to evaporate."

        scene bg hok_road:
            xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
            linear 0.1 rotate -6 zoom 1.2
        show lilly cane_reminisce_cas:
            xanchor 0.5 xpos 0.3 yalign 0.52 rotate 0 zoom 1.0
            linear 0.1 xpos 0.25 rotate -6 zoom 1.2
        show hanako defarms_strain_cas:
            xanchor 0.5 xpos 0.7 yalign 0.52 rotate 0 zoom 1.0
            linear 0.1 xpos 0.75 rotate -6 zoom 1.2
        show heartattack residual
        play sound sfx_pillow
        with vpunch

        "Before I can react they uselessly give way under my weight, leaving me only just enough time to brace myself and fall onto all fours."

        hi "Ah, damn…"

        show hanako defarms_shock_cas
        with charachange

        ha "Hisa… AAAAH!"

        "As I look up to her I realize my face is still taut with pain, only adding that much more to her worrying."

        show lilly cane_oops_cas
        with charachange

        li "Hisao!? Hanako, tell me what's going on!"

        li "Hanako, tell me!"

        show hanako def_strain_cas_close
        with characlose

        "Hanako quickly moves to my side as Lilly almost panics, having little clue as to exactly how bad a condition I'm in. While she stands there petrified, I lower my face and take a deep breath."

        scene black
        show heartattack alpha
        with shuteyefast

        "I come to a realization that makes me endlessly irritated with my stupid self. With all the excitement of my new surroundings, I'd entirely neglected to take my medications last night or even this morning."

        stop music fadeout 9.0

        hide heartattack
        with Dissolve(3.0)

        "Taking another breath, the acute pain in my chest begins to die down as suddenly as it had arrived."

        "Thank God. Thank God. Thank God, thank God, thank God."

        play ambient sfx_parkambience fadein 6.0

        scene bg hok_road
        show lilly cane_oops_cas at twoleft
        show hanako def_strain_cas_close at tworight
        with openeye

        "As it does, I become acutely aware of the sweat by now pouring off my face and the two scared girls around me."

        show lilly cane_reminisce_cas
        with charachange

        li "Hisao!"

        hi "I'm fine, Lilly. I'm… fine."

        show hanako defarms_strain_cas_close
        play sound sfx_impact
        with vpunch

        "I screw up my brow in an effort to lever myself up, Hanako's arms quickly moving to catch me if I fall as I stumble a bit before regaining my balance."

        "I look to Lilly and Hanako, worry written on both their faces. I feel awful. Utterly awful."

        show lilly cane_sad_cas
        with charachange

        li "I think we should go back."

        hi "I…"

        "Realizing the futility of protesting, I look away in frustration."

        hi "Fine."

        stop ambient fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .crescendo:
        scene bg hok_lounge_ss
        with openeye

        $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
        play ambient sfx_cicadas fadein 2.0

        "I open my eyes groggily, completely bereft of energy."

        "For a while, I simply lie down lifelessly, staring at the ceiling as I review the events of the morning in an attempt to organize my thoughts."

        "We went to walk to town. My heart nearly gave way. We came back. I took my pills. I slept."

        "I can only remember each period of time as a snapshot, but the timeline is clear enough. The memory of the girls' faces as I struggled to stand is an unpleasant one, stinging my feelings harshly."

        "If I look at the ceiling hard enough, I can imagine the tile edges and small dimples of the ceiling in the hospital. That fact alone is enough to make me sit up and try to pull myself together."

        "I scratch the back of my disheveled hair, glancing around the room. Lilly and Hanako are nowhere to be seen, and the television's turned off."

        "The clock above it says it's pretty late in the afternoon. The noticeably reddened sky outside the windows confirms it further."

        "I turn and pick myself off the futon, swaying slightly as I put my arms out for balance. I suppose I'd better go look for the girls to see if they're… all right…"

        "As I look out the window, I faintly see something in the distance."

        "Straining my eyes, I can just make out the shape of a person's figure. Her long blonde hair, swaying in the faint breeze, makes her almost seem to melt into the bright yellow of the wheat field."

        "Without a second thought, I leave the room to follow that lone apparition."

        stop ambient fadeout 2.0
        play music music_innocence fadein 14.0

        scene bg hok_wheat_ss:
            xalign 0.0
            warp acdc_warp 8.0 xalign 1.0
        with Fade(0.5, 0.2, 3.0, color="#fff")

        "The brightness of the setting sun assaults my freshly woken eyes, forcing me to avert them until they adjust."

        "The long, yellow strands of wheat brush against my legs as I wade through them, the densely-grown field making it hard to advance."

        "Regardless, my eyes stay fixed ahead, true to that solitary figure. Within minutes I reach her, meters behind her turned back."

        hi "Lilly?"

        scene bg hok_wheat_ss at right
        show lilly back_pout_cas_ss at center
        with charaenter

        "She simply nods."

        hi "Where's Hanako?"

        show lilly back_listen_cas_ss
        with charachange

        li "She's in bed. She went to sleep after I calmed her down."

        "She says it matter-of-factly and with as few words as possible, as if saying any more was strictly forbidden."

        "There's something different about her. Her normally confident figure seems oddly fragile, her body offering no resistance to the breeze blowing her skirt."

        "The strands of wheat sway from side to side while a deafening pause passes, the only sound being their rustling."

        "As we stand in the field alone, I know what I have to ask."

        hi "What's wrong, Lilly? You're not acting like you usually do."

        show lilly back_sad_cas_ss
        with charachange

        li "Remember when I talked of my family, Hisao?"

        hi "Your family…"

        "I look downwards in thought, sifting through my scattered memories. The event seems to leap ready to hand when I search for it, rising to the surface as soon as it was recalled."

        hi "After Hanako's birthday party?"

        "She gives a single, simple nod."

        show lilly back_pout_cas_ss
        with charachange

        li "It was nice… back then. You and I, celebrating with Hanako. Simply sharing presents, talking, having fun together. It was almost as if we were a family. One small, misshapen family."

        show lilly back_sad_cas_ss
        with charachange

        li "I thought that could just go on forever. Just the three of us, happily together."

        "She takes a long breath, a slight shakiness to it just barely audible through the moving air."

        show lilly back_pout_cas_ss
        with charachange

        li "Even if my family was so far away… as long as we were together, that was all I needed. I don't want to lose you, Hisao."

        li "I didn't even realize how afraid I was of losing someone else until today. Until…"

        hi "I'm sorry, Lilly. I know my body's weak, but even then I make the most stupid of mistakes."

        stop music fadeout 4.0

        show lilly back_sad_cas_ss
        with charachange

        li "Don't apologize… please don't apologize…"

        hi "Lilly…?"

        show lilly basic_concerned_cas_ss
        with charachange

        "She turns to face me, her pale cheeks stained with tears."

        show lilly basic_concerned_cas_close_ss
        with characlose

        "One misguided step after another she stumbles towards me, her arms held out in search of so much as a faint brush against me."

        play music music_romance fadein 2.0

        scene unlock_ev lilly_wheat_close
        show ev lilly_wheat_large:
            yalign 0.5 xalign 0.0
            easein 20.0 xalign 1.0
        show ovl lilly_wheat_foreground:
            yalign 0.5 xalign 0.0
            easein 20.0 xalign 1.0
        with GenericWhiteout(1.0, 0.0, 4.0)

        "My heart doesn't race nor pound as I step towards Lilly, gently taking and steadying her in my arms as she quickly clutches to me, sobbing."

        "With her face trembling against my shoulder, the next words from her mouth are the last I expected."

        li "I love you, Hisao. I love you, I love you, I love you, I love you, I love you!"

        li "Don't go away, I beg of you. Never, ever go away. I love you, so please…!"

        "So… that's why she's been acting like this. That tender voice when I called her, her thoughtless concern at the slightest pain I might feel…"

        "After having been left in Japan without her family, and with only Akira, Hanako and me around, she was afraid of losing yet another person who was close to her. She was genuinely worried for me."

        "It's a strange feeling. A mix of surprise and sorrow, yet also of the deepest gratitude I think I've ever felt. The only reaction I can muster among my conflicting emotions is a calm sigh."

        hi "You idiot."

        li "Hi… sao?"

        "For a fleeting moment, I feel her body become still. The only movement to be felt is the calm afternoon breeze."

        hi "I said it before, didn't I? It's only natural to feel concerned about those around you."

        hi "I'm still here, and I'll always be here, because I want to see you more each day. To share in your happiness, to support you in your sadness…"

        hi "But most of all, I'll still be here because I want to see your smile. Your true smile."

        "A single gust of wind rustles the long strands of wheat, a second's silence passes."

        hi "Smile when you want to smile. Cry when you want to cry. I love you, Lilly. So you don't have to hold back any more."

        "With that, her arms clutch my back as tightly as she can, her face buried beside mine."

        scene ev lilly_wheat_small:
            xalign 0.5 yalign 0.5 zoom 1.1
            ease 16.0 zoom 1.0
        with whiteout

        "Her tears fall down my back and she cries unrestrainedly as the last of her resistance melts away."

        li "Hisao! Hisao! Hisao!"

        "I close my eyes and bring my head down to her shoulder, holding her shaking frame tightly."

        hi "It's okay, Lilly. I'll never go away."

        hi "I promise."

        stop music fadeout 6.0

        if _in_replay:
            return

    label .diminuendo:
        scene bg hok_lounge_ss
        with locationskip

        "We slowly walk back to the house, holding each other tightly as we take a seat inside. Lilly leans her head onto my shoulder as I put my arm around her waist."

        "Neither of us has any want to break the silence."

        "With her eyes shut it's hard to work out whether she's fallen asleep. Not that I mind: the warmth of her body leaning against me, the softness of her hand delicately held in mine…"

        "For a long, long time we sit leaning against one another, sharing our warmth and feelings as night eventually begins to settle in."

        "Lilly's gentle, soft voice ends the silence."

        show lilly basic_smileclosed_cas_close_ss at center
        with charaenter

        play music music_twinkle fadein 6.0

        li "Thank you, Hisao."

        hi "Thank you?"

        show lilly basic_smile_cas_close_ss
        with charachange

        li "For returning my feelings."

        hi "Did you think I wouldn't?"

        show lilly basic_weaksmile_cas_close_ss
        with charachange

        li "There was the possibility."

        "I take a deep breath in thought. That much was only my fault."

        hi "It's funny, actually. I was thinking of telling you about my own feelings sometime soon."

        hi "I guess, in that way, you saved me the effort."

        show lilly basic_giggle_cas_close_ss
        with charachange

        "She raises her head a little and gives a tiny, amused giggle. I smile at how earnest it is, so girlish in its lightness. She collects herself soon afterward, her hair resting against my shoulder."

        hi "Feeling a bit better?"

        show lilly basic_smileclosed_cas_close_ss
        with charachange

        "She gives a small nod."

        show lilly basic_smile_cas_close_ss
        with charachange

        li "You are thoughtful, Hisao. That's why I like you."

        hi "I'm sorry I'm like this. As much as I didn't want to make you concerned for me, I couldn't do anything to prevent it."

        show lilly basic_concerned_cas_close_ss
        with charachange

        li "Don't apologize for it. Please don't."

        hi "Lilly?"

        show lilly basic_reminisce_cas_close_ss
        with charachange

        li "Have I ever apologized for my blindness, even once? You can't help the way you were born, Hisao. There's no point in apologizing for who you are."

        "She says this with surprising conviction. In the end, it was perhaps this mentality which spurred her to befriend me in such a short time, in addition to her motherly instincts."

        "She did seem to become trusting very quickly, but I'd never questioned why. Now it seems obvious that she did so to help me as I went through one of the lowest points of my life."

        "I move to respond, but cut myself off as I feel her fingers run gently through my hair. I feel their soft and delicate touch moving downwards to trace the contours of my face, her palm finally settling on my cheek."

        show lilly basic_weaksmile_cas_close_ss
        with charachange

        li "You are a beautiful person, Hisao. Please, don't ever apologize for that."

        "For a moment, I'm utterly speechless. I slowly bend my head down, placing a tender kiss on her light, voluminous hair."

        hi "We're a couple of right old fools, aren't we?"

        show lilly basic_cheerful_cas_close_ss
        with charachange

        li "…We are."

        "After a long calm, she speaks again."

        show lilly basic_smile_cas_close_ss
        with charachange

        li "Hisao?"

        hi "Yes?"

        show lilly basic_smileclosed_cas_close_ss
        with charachange

        li "I…"

        stop music fadeout 4.0

        show lilly basic_weaksmile_cas_close_ss
        with charachange

        li "I wouldn't mind if you…"

        "I feel her hand tensing under mine, trembling slightly. My mouth opens, but try as I might I can't formulate a response to her proposition."

        hi "Lilly…"

        "Before I can say another word, she slips her hand from under mine and tenderly holds the side of my face once more."

        show lilly basic_pout_cas_close_ss
        with charachange

        li "Please."

        "I give a peaceful smile, holding her hand against my cheek as I nod a single time."

        hi "Okay."

        play music music_heart fadein 0.5

        show lilly basic_smileclosed_cas_close_ss
        with charachange

        "As I look into her eyes, she leans towards me. Her delicate lips touch mine as she guides herself with her hand."

        "She breaks off not a second later, faintly smiling."

        show lilly basic_smile_cas_close_ss
        with charachange

        li "I love you, Hisao."

        show lilly basic_smileclosed_cas_close_ss
        with charachange

        "We kiss again, this time with both of us meeting the other."

        "While the previous kiss was one of love, this is one of lust, our tongues meeting and our breathing heavy. After precious seconds we part, both our faces well and truly flushed."

        "Both of us bring our fingers to our lips in unison, recalling that fleeting feeling, rapidly becoming buried both by our urges and bashfulness."

        show lilly basic_pout_cas_close_ss
        with charachange

        "Lilly is the first to shift uncomfortably, though."

        hi "What is it?"

        show lilly basic_weaksmile_cas_close_ss
        with charachange

        li "Should we… get more comfortable?"

        hi "Hmm? Ah, o-okay…"

        "Now that she mentions it, this futon would be a bit too narrow to do much on. Considering the thoughts running through both our minds, it's no small wonder one of us has any measure of foresight left."

        show lilly:
            ease 1.0 ypos 1.2 alpha 0.0

        pause 1.0

        hide lilly
        with vpunch

        "I take her hands and guide her sideways as I move, the brief and awkward dance ending with both of us tentatively sitting on the floor opposite each other."

        "As I reach forward to pull her top up, she stops after she moves her hands to do the same."

        show lilly basic_concerned_cas_close_ss:
            center
            ypos 1.17
        with charaenter

        li "You're shaking…"

        "I pause for a moment and look at my hands."

        "Sure enough, they're quivering slightly. Whether it's from nervousness or excitement, I'm not sure."

        hi "Uh… I guess I am."

        show lilly basic_weaksmile_cas_close_ss
        with charachange

        li "So you're as nervous as I am, then?"

        "I withdraw my hands and sigh, steadying myself. We have plenty of time, so there's no need to rush this."

        hi "Sorry. It's my first time, so I'm a bit…"

        show lilly basic_cheerfulblush_cas_close_ss
        with charachange

        "She giggles shakily, all but confirming what I reasonably deduced by now."

        show lilly basic_smile_cas_close_ss
        with charachange

        li "It's the same for me. I'm happy… we could share this together."

        "I match her smile twofold, leaning forward and taking her body in my arms as she reaches to hug me back."

        hi "I love you, Lilly."

        show lilly basic_smileclosed_cas_close_ss
        with charachange

        li "You already said that."

        "I can't help grinning. Even in such a situation, she still has her wits about her."

        hide lilly
        with charaexit

        "Breaking our embrace, we decide to take off our own clothing. While it's easier this way, I don't doubt it's just an attempt to distract ourselves from our nerves."

        "With slightly stiff hands, I begin to slide the first button out from my shirt."

        "Once we remove the last of our clothes, which end up haphazardly piled behind us, my breath is taken by the sight in front of me."

        show lilly behind_reminisce_nak_ss at center
        with charaenter

        "Her long, shapely legs, full hips and her breasts, plump but dainty… her slightly blushing face, delicate and reserved, is framed by the bangs of her hair."

        "Her hands, tightly held behind her, only serve to further accentuate her chest. Her tall and pale body is beautiful when bared."

        "This girl in front of me, reserved yet playful, astute yet hospitable, is the girl I've fallen in love with."

        "I lean forward, delicately taking her shoulders in my hands."

        show lilly behind_listen_nak_close_ss
        with charachange

        "As I do, she brings her hands to my chest. With a slightly uneven breath, we lean into a deep kiss."

        "I feel one of Lilly's hands slowly slide up to my shoulder, it and her head very gently moving forwards. Assuming her intent, I lean back onto the floor."

        hi "Ah…"

        scene evhunlock lilly_handjob_chest_normal_small
        show evh lilly_handjob_chest_normal:
            xalign 0.7 yalign 1.0
            ease 8.0 xalign 0.4 yalign 0.2
        with whiteout

        "She lowers herself beside me, one hand stroking my hair as the other moves across my chest. The feeling of her breast against it is enough to excite me."

        "This must be her way of taking in what I've already seen of her; despite her lack of sight, she engraves every detail of my bare body and chest into her mind."

        "When her middle finger falls into the slight recess of my chest scar, a lingering effect of my operation so many months ago, she slowly runs her hand down its length."

        show evhunlock lilly_handjob_chest_frown_small
        show evh lilly_handjob_chest_frown:
            xalign 0.4 yalign 0.2
        with charachangeev

        li "This is…"

        hi "The scar, from my surgery. They had to do this in order to operate on my heart."

        "For a moment she's lost for words, the idea of such extensive scarring adding a new worry for her. Her expression changes from curiosity to apprehension."

        li "Should we… really be doing this kind of thing…?"

        "Those words bother me beyond what is rational. Lilly's face breaks my heart more than even her words possibly could, yet I don't even know the answer to her question."

        "I can't let this condition dominate me forever. It may not even be medically advisable, but I outright refuse to live my life in such a prison."

        hi "It's okay, Lilly. This much will be okay."

        show evh lilly_handjob_chest_normal
        with charachangeev

        "Her troubled expression holds for a moment longer, but she eventually acquiesces, her hand moving to my lower chest and then my thigh."

        show evh:
            zoom 1.0 xalign 0.4 yalign 0.2
            ease 4.0 zoom 0.667 xalign 0.5 yalign 0.5
        with None
        show evh lilly_handjob_stroke_normopen:
            zoom 1.0 xalign 0.4 yalign 0.2
            ease 4.0 zoom 0.667 xalign 0.5 yalign 0.5
        with charachangeev

        "With a look of slight surprise, she slowly moves her hands downwards, her breath catching as she brushes the side of my lower hair."

        "She tentatively moves her hand sideways, delicately touching the most honest part of my body."

        show evh lilly_handjob_stroke_normshut_small:
            truecenter
            zoom 1.0
        with charachangeev

        li "Th… this is…"

        hi "Y-yeah."

        "Our nervousness peaks as the act begins, her hand gently patting up and down as lightly as if it would break if breathed upon."

        "I'm not sure whether it's just to steady myself or because I want to steady her, but I take my free hand and hold the side of her face in it. The feeling of her hair and soft skin is nice, and it seems to lighten her mood a bit."

        "The mere fact that I'm being touched by her is surprisingly erotic. I feel my body relaxing as I submit to the pleasure overwhelming me."

        "Long minutes pass in almost total silence, our heavy breathing the only sound to be heard in the house. Lilly's fingers stop affectionately stroking my hair and she opens her lips once again."

        show evh lilly_handjob_stroke_flustopen_small
        with charachangeev

        li "Hisao…"

        "I wait a second for the rest of the sentence, but none is forthcoming. She may be trying to take the lead, but she's still incredibly nervous."

        "I can't help smiling as I stroke her hair from her face a couple of times, reassuring her. As nervous as she may be, I'm thankful that Lilly's taking the lead. I'd probably be just as anxious as she if I were attending to her."

        show evh lilly_handjob_stroke_normopen_small
        with charachangeev

        hi "Okay."

        "She pauses a moment before giving a small nod, sitting up and shifting her legs over mine. Once again my breath is stolen by the magnificent sight of her body over mine."

        show evh lilly_cowgirl_smile_small
        with whiteout

        "I can only look on frozen as she delicately lowers herself, resting her reddened lips over me. She slowly begins to move her hips downwards, her softness enveloping my consciousness."

        show evh lilly_cowgirl_weaksmile_small
        with charachangeev

        "She takes a deep breath to collect herself, her face remaining steady. With her hands taking in my body in lieu of sight, the intimate situation muddles her usual efforts to compensate for lack of eye contact."

        "She gradually lowers herself onto me, her knees and hands supporting her as she does. Her entire body tenses as I enter, her expression obviously one of stifled pain."

        "Despite that, I can't help savoring the soft, warm feeling enveloping my consciousness, the surge of pleasure overcoming all my senses."

        "The last vestiges of it all but disappear inside her while her nails slightly scrape into my chest in an effort to stop herself from yelping in pain. A pained moan, too much for her to suppress completely, escapes from her lips."

        "As I open my mouth to comfort her, I see the barely visible red drops from between her legs."

        hi "Lilly, if it's too much…"

        scene evh lilly_cowgirl_strain_small
        with charachangeev

        "She clenches her mouth tightly, quickly and forcefully shaking her head from side to side in defiance. After a couple of seconds she relaxes her body slightly, though she's still obviously far from being comfortable."

        li "I… it's okay… I'm okay."

        scene evh lilly_cowgirl_frown_small
        with charachangeev

        "She swallows hard, trying to collect herself."

        "Lifting herself slowly and bringing herself back down, she relaxes a little more as the feelings of pleasure begin to overtake those of pain."

        scene evh lilly_cowgirl_strain_small
        with charachangeev

        "Her breathing starts to match the same ragged patterns as mine, her body moving almost teasingly slowly. She looks as if she's slowly beginning to enjoy the act, my feelings finally reaching her."

        "I'm not sure if she's keeping herself at this speed for her sake or for mine, but either way… with this slow and steady pace, I think I can… keep my body in check. It's funny, in a way, that even now I'm depending on her."

        "For us to be joined together like this, our feelings so close… it makes me glad. To be sharing our first moment together like this… is an almost… overwhelming… feeling…"

        hi "I love you… Lilly…"

        scene evh lilly_cowgirl_cry_small
        with charachangeev

        li "Hisao… Hisao…!"

        "I can feel her body tensing, her breathing and movements becoming steadily less carefully controlled. I'm happy to be making her feel so good, but as my thoughts become increasingly focused, I can feel myself rapidly nearing my limit."

        scene white
        with Dissolve(3.0)

        "Control of my body is instantaneously wrested from my mind as I grit my teeth hard, a loud moan escaping as I climax and my hips hit hers. Her body hunches over at the same moment, her breasts touching on my chest."

        "We stay locked in all-encompassing ecstasy for a brief moment, my mind completely taken by the feeling for a precious few seconds."

        scene evh lilly_cowgirl_weaksmile_small
        with charachangeev

        "It ends all too soon and our bodies collapse in exhaustion with Lilly barely staying on top of me."

        "I lifelessly manage to wrap my arms around her limp, sweating body, and for minutes we simply lay there, silently savoring the contact with each other while we recover from the experience."

        "Neither of us had thought ourselves prepared for such a thing, of that much I'm certain."

        "Entirely drained, far past the point of conversation, I look at her tired face. It looks as if the exertion, both physical and mental, has almost forced her to the verge of collapse."

        hi "I love you, Lilly."

        scene evh lilly_cowgirl_smile_small
        with charachangeev

        "She nods weakly, rubbing my hair with her left hand. If we could simply remain together like this for an eternity, it would be a paradise like no other."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .gray_outlook:
        scene bg hok_lounge_rn
        with locationchange

        $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
        play ambient sfx_rain fadein 1.0

        "After being woken by a sound, I open my eyes with a measure of reluctance."

        "Turning my head to the left, I find the rain outside sweeps against the windows loudly. Spray after wind-blown spray lashes against the glass, as if trying its hardest to make up for the summer's previous heat."

        "I sit up in the futon, holding the back of my neck to try and subdue the pain from my awkward sleeping position."

        "By all accounts I should be lamenting the turn in the weather, given that this is our last day here. The events of yesterday refuse to stop flooding my mind, though."

        "The feeling of holding Lilly's crying body in my arms. The rush of lust and hormones that flowed through us as we spent the night together. It seems almost futile to try and rationalize everything that happened."

        "In an attempt to distract myself, I groan and lean over to retrieve my bag without standing. Pulling out one bottle after another, I take the daily regimen's worth of pills from their containers and swallow them without further ado."

        $ renpy.music.set_volume(0.1, 1.0, channel="ambient")

        nvl show dissolve

        nvl clear

        n "{vspace=120}It took a surprisingly short amount of time to get used to swallowing pills without water. That said, I suppose the same thing goes for getting used to living in a school for disabled students."

        n "Remembering Yamaku, I become all the more grateful for having the chance to get away, even if it's just for the shortest of times."

        n "I appreciate the chance to spend time alone with Lilly and Hanako, away from the bustle of school life, even considering the latest complications."

        n "I never thought I'd say it, but the idea of living away from the city in a nice, tranquil area is an inviting one. It's a thought that, barely a year ago, would have seemed simply ludicrous."

        $ renpy.music.set_volume(0.2, 1.0, channel="ambient")

        nvl clear
        nvl hide dissolve

        "A flash of pink, no doubt Hanako's gown, peeks from around the corner. Realizing I must look a sight since I've only just woken up, I slap the remaining pills into my mouth and run a hand through my hair."

        show hanagown smile_rn at center
        with charaenter

        ha "Good morning, Hisao."

        hi "Ah, go— ack!"

        $ renpy.music.set_volume(0.0, 0.2, channel="ambient")

        with vpunch

        "I reply to her completely forgetting that I'm in the middle of swallowing a particularly large pill. Coughing and spluttering, I violently gag on it."

        show hanagown worry_rn
        with charachange

        ha "Ah, Hisao!"

        $ renpy.music.set_volume(0.2, 10.0, channel="ambient")

        "After sputtering loudly and tapping my chest a couple of times to force it down, I manage to recover."

        hi "I'm fine. Sorry, forgot I was swallowing."

        play music music_happiness fadein 5.0

        show hanagown distant_rn
        with charachange

        ha "Sorry, I didn't mean to—"

        "I hold my hand up, gesturing for Hanako to stop."

        hi "I gagged. It's my fault. 'Morning, Hanako."

        "She pauses a moment before bowing in reply."

        show hanagown distant_rn at tworight
        show bg hok_lounge_rn at bgright
        with charamove

        show lilly basic_sleepy_paj_rn at twoleft
        with charaenter

        "Walking, no, staggering in behind Hanako is the familiar figure of Lilly, also dressed in her pajamas. With her eyes full of sleep and hair bedraggled, she's a sight to behold."

        hi "Hi, Lilly."

        show lilly basic_weaksmile_paj_rn at twoleft
        with charaenter

        li "Good morning… Hisao."

        "For a while, a silence hangs in the air as neither of us knows what to do."

        "Given what happened last night, we both have more than enough reason to be finding the situation awkward; just how are we meant to react to meeting each other after something like… that?"

        "The best course of action would probably be to talk to Lilly alone, to set things in order."

        hi "Um, I'll… start making breakfast."

        "Lilly evidently catches on to my train of thought."

        show lilly basic_smileclosed_paj_rn
        with charachange

        li "I'll help. Hanako, could you set the table?"

        "She nods, her head disappearing into a cupboard as she quickly goes about her assigned task."

        $ renpy.music.set_volume(0.1, 0.5, channel="ambient")

        scene bg hok_kitchen_rn
        with locationchange

        "I rub a little more sleep out of my eyes as I wander over to the fridge and take out some milk, and Lilly grabs various brightly colored boxes from some of the lower cupboards to my side."

        "While we make the rather bland-looking meal, I whisper somewhat more quietly than usual. Knowing Lilly's hearing, she won't have any trouble catching what I say."

        hi "Are you okay, Lilly? After last night…"

        show lilly basic_reminisce_paj_rn at center
        with charaenter

        "She gives a delicate nod, her expression weak."

        "Though her tiredness surely plays a part, she seems genuinely unsure about what's happened between us, and how to move ahead. I can't say I blame her, considering my feelings are the same."

        show lilly basic_sad_paj_rn
        with charachange

        li "I'm sorry, Hisao. I wasn't thinking straight yesterday. I never stopped to consider you or Hanako, and I even went as far as…"

        "She's winding herself up. With her hands and voice both tightening, I give her a gentle bump to try and lighten up the situation."

        hi "You don't have to apologize. I said I liked you as well, after all."

        show lilly basic_oops_paj_rn
        with charachange

        li "But I…"

        "As her composure begins to falter, it becomes obvious there's no alternative."

        show lilly basic_sad_paj_close_rn
        with characlose

        "Turning to Lilly, I gently embrace her tall frame. She offers no resistance at all, thankfully pulling back, just, from the edge of her emotions."

        show lilly at twoleft
        show bg at bgleft
        with charamove

        show hanagown normal_rn at tworight
        with charaenter

        "Despite our reassuring embrace lasting only a matter of seconds, I notice Hanako wordlessly watching. The plate in her hand hovers inches above the table, her action halted midway by the sight."

        stop music fadeout 2.0

        scene bg hok_lounge_rn
        show hanagown distant_rn:
            tworight
            ypos 1.15
        show lilly basic_sleepy_paj_rn:
            twoleft
            ypos 1.17
        with shorttimeskip

        $ renpy.music.set_volume(0.2, 0.5, channel="ambient")

        "The clatter of utensils against plates is the only sound to be heard as we silently eat. Whereas before only two of us may have been unsure of ourselves, the entire situation has changed."

        "After weeks of blissful friendship, whiling away the days with shared meals and chatter with little meaning, the relationship of Lilly and me, no, that of all of us, has irreversibly changed."

        "I can't take this."

        hi "Lilly…"

        stop ambient fadeout 25.0

        show lilly basic_listen_paj_rn
        with charachange

        "She solemnly nods, gently laying her spoon onto the plate in front of her. Neither of us knows exactly how we regard each other, let alone how Hanako would view us."

        show lilly basic_weaksmile_paj_rn
        with charachange

        li "This might seem abrupt but… I've confessed to Hisao."

        show hanagown distant_blush_rn
        with charachange

        "For a moment, Hanako looks almost confused; precisely the reaction I'd thought she would have. She eventually nods, her spoon still in her mouth as she does."

        show hanagown normal_blush_rn
        with charachange

        ha "Did you accept?"

        hi "I did."

        show hanagown smile_rn
        with charachange

        "She gives a smile so large, and so earnest, I find myself blushing. I think it's the brightest I've ever seen her expression look."

        play music music_serene fadein 6.0

        ha "Then I'm happy. I'm really, really happy."

        show lilly basic_sleepy_paj_rn
        with charachange

        li "I'm sorry for not telling you anything about it before. Things have been…"

        "Hanako shakes her head from side to side emphatically, apparently forgetting in her rush that Lilly couldn't possibly notice."

        show hanagown distant_blush_rn
        with charachange

        "She begins fiddling with her fingers, looking a little more nervous than she did before."

        ha "To be honest, I began to think you might like each other a while ago. At first I didn't really know what to think about it… but I…"

        show hanagown smile_rn
        with charachange

        ha "I decided in the end that… if my friends are happy, then I'm happy."

        ha "I was really glad to have another friend when we met Hisao, so you finding love through him is even better… right?"

        "A feeling of relief at her acceptance of our relationship falls over me like a wave. The same happens to Lilly, judging by her expression."

        show lilly basic_weaksmile_paj_rn
        with charachange

        li "Thank you, Hanako. I really appreciate you being so understanding."

        show hanagown distant_rn
        with charachange

        "Lilly's voice still sounds slightly apologetic, or at least unsure. This doesn't escape Hanako, who appears lost in thought for a few moments before turning to me."

        show hanagown smile_rn
        with charachange

        ha "Hisao, do you mind if Lilly and I go outside for a bit?"

        hi "Ah, no, feel free…"

        show lilly basic_surprised_paj_rn
        with charachange

        li "Hanako?"

        show hanagown smile_rn at tworight
        with charamove

        show lilly basic_surprised_paj_rn at twoleft
        with charamove

        hide lilly
        hide hanagown
        with charaexit

        stop ambient
        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")

        "Hanako gets up from her seat, taking Lilly's hand and almost dragging her from the table in her excitement. Considering Lilly's typically slow and steady pace, Hanako's haste makes her footing awkward and she almost loses her balance a couple of times."

        "It's a pretty amusing sight, leaving me wordless as I watch them disappear out the door. It's only now that I realize the rain's stopped, being replaced by a sky seemingly all the more vivid and bright to make up for the morning's drab gray expanse."

        "For Hanako, this must be a pretty big revelation. Lilly and I are really the only people she associates with, almost as if we were parents in her own's stead."

        "I suppose that might well be the best way to describe the relationship we share. A father, mother and daughter, all playing around in our little make-believe family as if it could last forever."

        "It might be a strange dynamic, and one that certainly can't last for long… but maybe, just for this one small moment, it's okay."

        "As I stand from the table and go to join Lilly and Hanako in the fields outside, I nod to myself in affirmation."

        "This one small moment of happiness, no matter how brief, will last with me, with all of us, forever."

        stop music fadeout 2.0

        if _in_replay:
            return

    label .rhapsody_in_blue:
        scene bg hok_bath
        show steam
        with shorttimeskip

        "Submerged deep in the hot water, I let a drawn-out sigh escape my lips. The feeling of seemingly every muscle in my body relaxing is euphoric."

        "I have no idea how long it's been since I had a genuine hot bath, but right now I can hardly be bothered trying to remember."

        play music music_dreamy fadein 2.0

        nvl clear
        nvl show dissolve

        n "Maybe I'm giving the simple fact that for once I get to have a real bath more credit than it's due; the chance to just calm down, allow myself to unwind and have some time to myself is a welcome one."

        n "Hanako, Lilly and I wandered about outside, exploring the extent of the surprisingly large tract of land surrounding the house. Then we spent the majority of the afternoon resting, watching television, reading, and playing cards."

        n "It may not have been the most exciting finale to the trip, but such tranquil peacefulness is something to savor. Even after we return to the school tomorrow, I think I'll remember this little house in Hokkaido for a long time."

        n "It's a pity we only have a couple more hours to spend here before going to get the train back."

        n "All I can do is yawn contentedly while I watch the steam slowly rising from the clear water's placid surface, my eyes eventually locking onto the ceiling."

        n "Our exams are imminent. I've barely studied at all for them."

        n "On top of that, I don't even know what I'll do after graduation. Passing exams is all well and good, but to what end?"

        n "Also now, of all times, I'm getting into a relationship."

        nvl clear
        nvl hide dissolve

        hi "What the hell am I doing?"

        "…"

        "…I guess I shouldn't think like that. What's done is done, and maybe this could be viewed as just another aspect of my new life that I'm working on."

        "I enjoy being with Lilly, and there's more to life than school and a career after all."

        "As I busily attempt to rationalize all that's happened, I hear a series of raps on the door. I pick myself up and sit upright, trying to figure out the source."

        "Three, no more and no less. Light yet assertive in their tapping, and timed regularly enough to tune a metronome. I'd be extremely surprised if it wasn't Lilly."

        li "May I… come in?"

        "Yeah, it's Lilly."

        hi "I'm still in the bath, I'll be out in a sec."

        li "…I know."

        stop music fadeout 3.0

        "The voice coming from the other side of the door freezes me. After a second's thought, I rest on the side of the bath and let my arms dangle over the side."

        "Despite trying my best to play it off, I can't help letting my mind wander."

        hi "S-sure, come in."

        show lilly basic_smileclosed_cas:
            center
            xpos 0.4 alpha 0.0
            easein 1.0 center alpha 1.0

        pause 1.0

        show lilly at center

        "With that she opens the door, slowly walking into the room and closing it behind her. She looks oddly calm, countering my racing heart."

        hi "Ah… h-hey… Lilly."

        play music music_one fadein 9.0

        show lilly basic_smile_cas
        with charachange

        li "Do you mind if I take a bath with you?"

        hi "I don't mind. Go ahead."

        show lilly basic_listen_cas
        with charachange

        "With a small nod she begins to lift her sweater off her shoulders, baring her chest little by little."

        hi "I could do that for you, if you'd like."

        show lilly basic_emb_cas
        with charachange

        li "Refused."

        hi "Why?"

        show lilly basic_pout_cas
        with charachange

        li "…"

        "Her face shows she's still not overly comfortable with letting me attend to her. I can't say I blame her."

        hide lilly
        with charaexit

        play sound sfx_rustling

        "She continues undressing, her shirt and skirt falling to the floor and leaving her in her white lace bra and panties. Eventually, she stands bare in the center of the room."

        show lilly behind_sleepy_nak at center
        with charaenter

        "Compared to last time, it's a lot easier to take in her entire figure. It's a wonderful sight."

        li "Hisao?"

        hi "Hmm?"

        show lilly behind_pout_nak
        with charaenter

        li "You're thinking perverted thoughts, aren't you?"

        hi "Give me a break, you're undressing in front of me."

        show lilly behind_weaksmile_nak
        with charachange

        "She furrows her brow in thought."

        li "I guess this would be somewhat more erotic for you than me."

        hi "Why?"

        hi "…Ah."

        show lilly behind_giggle_nak
        with charachange

        "She gives a small, lighthearted chuckle, which seems to settle her nerves a little."

        show lilly behind_smile_nak
        with charachange

        li "If this is too much for you, Hisao, I can come back later."

        hi "No, no, this is fine. I'm just a bit… well…"

        hi "You're really beautiful, you know."

        show lilly behind_emb_nak
        with charachange

        "My earnest comment draws a vivid red blush from Lilly."

        li "Hisao…"

        "I give a small grin. She's cute when she's taken off guard."

        show lilly behind_smileclosed_nak
        with charachange

        li "In any case, may I come in?"

        hi "Ah, sure."

        hide lilly
        with charaexit

        "I lean forwards and take her soft hands in mine, helping her over the side of the bath."

        "She feels out the side of the bathtub then slowly lowers herself in, my breath catching when she sits and leans her back onto my front, her legs inside mine. I'd expected her to sit at the other end."

        scene evh lilly_bath_smile_small
        with whiteout

        "Letting out a long breath to calm myself, I rest my arms on the sides of the bath as I struggle to control my urges."

        "Far from missing the sight of her… assets, the feeling of her body against mine is surprisingly relaxing. If Lilly's so sensitive to touch, it must be all the more so for her."

        li "You run your baths quite hot, don't you?"

        hi "A bit. Do you want me to run some cold water to cool it down a bit?"

        "She gives a small shake of her head."

        li "No, this is fine."

        hi "Okay."

        "The conversation comes to an abrupt end, silence taking over."

        show evh lilly_bath_emb_small
        with charachangeev

        "A very long, and very awkward, silence."

        li "Maybe this was a bit too…"

        hi "Don't worry, it's okay."

        "The situation only becomes even more awkward. As if to distract herself, Lilly runs her free hand over her legs while holding one over her breasts for modesty."

        "I sit idly watching the wall ahead of me and the rising steam, every now and again stealing a glimpse at her body."

        "The white of her skin glistens as she keeps sliding her hand over her legs, their length and tone all the more obvious."

        hi "You know, compared to Akira, you look a lot more foreign."

        li "I took after my mother's side, genetically. Akira took after my father's more."

        hi "I guess that makes sense. How on Earth did a native Scot and a Japanese businessman meet, anyway?"

        li "My mother was a journalist. She met my father while he was at a conference in Inverness."

        hi "Ah, I see. Taking after your Scottish side would also explain your height, I suppose."

        "I look back down at her as she nods, and sigh at the ridiculousness of the situation."

        hi "This really is too much, isn't it?"

        show evh lilly_bath_smile_small
        with charachangeev

        li "You're enjoying it though, aren't you?"

        hi "In some ways, yes. I guess things turned out okay, in the end."

        hi "Everything's settled down, Hanako took our relationship well, and we'll be going back to school tomorrow."

        li "Indeed. It's a shame to be going back so soon, but we'll still have our memories of this place."

        hi "Memories, huh? I suppose so. We'll have to see how everything goes once we get back, but for now… I'm just glad you like me."

        hi "I've been winding myself up for weeks about that, so I'm thankful for things turning out like this."

        "She nods, leaning into me as we share the warmth of our bodies."

        "I'm not sure whether she'll be okay with it or not, but my temptation rapidly begins to get the better of my self-restraint."

        hi "Hey, Lilly?"

        li "Yes?"

        hi "How was it? Last night, that is."

        "She pauses in thought before looking down slightly. A delicate smile finds its way onto her lips as she blushes, her body becoming more relaxed. It's more than enough to answer the question."

        "Even as I give a small nod in response, thoughts of last night run through my mind. Considering the situation, I don't really think anyone'd blame me."

        li "Hisao, your heart's beating…"

        "Her voice is cut off as I delicately place a hand on her thigh. While I'd resisted before, the memory of our first time is enough to make me give in."

        "She lets her body lean into mine without a word of protest, an invitation that I'd be hard put to ignore. I place a small kiss on her neck to accept, before slowly moving my hand over her smooth legs."

        li "Hisao, please…"

        "Even as she says it, her mouth curls upward into a smile, her tone caught between embarrassment and awkward giggling."

        show evh lilly_bath_open_small
        with charachangeev

        "Eventually she takes one of my hands in hers, guiding it to her right breast. I greatly appreciate the tentative guidance she's willing to give me."

        show evh lilly_bath_grab_small
        with charachangeev

        "All signs of tension in her body give way. I continue to take in the feeling of her soft skin, redoubled as my other hand slips between her legs."

        "I wonder if the feeling of my hands on her is exaggerated by her lack of sight, since her other senses are so finely tuned."

        "She does seem to be enjoying it to a surprising extent, after all. It gives me a somewhat odd feeling, but a pleasurable one."

        show evh lilly_bath_moan_small
        with charachangeev

        "It only takes a few minutes before her body starts to squirm ever so slightly, her efforts to stifle her moaning becoming visible as she purses her lips. Her lighthearted, whispered protestations become noticeably more quiet."

        "This makes me realize that all her squirming against my body's made me increasingly excited as well."

        hi "Lilly…"

        show evh lilly_bath_smile_small
        with charachangeev

        "I withdraw my hands to give her addled senses time to respond. Nodding, she shakily stands and offers her hands for me to lead her out of the cramped bathtub."

        scene evh lilly_afterbath_open_small
        with locationchange

        "She maneuvers herself out of the bath as I do, our hands holding each other's."

        "Eventually I sit beside the bathtub, the two of us fussing around a little until we get comfortable. With a small gasp, desperately constrained to avoid being audible outside, she lowers herself onto me once again."

        "The way she moves makes it obvious that she must still be on the verge of her climax."

        "She slowly starts to move her hips up and down, her tongue finding mine as she holds my face upwards. I realize just how much pleasuring her has excited me."

        scene evh lilly_afterbath_shut_small
        with locationchange

        li "Hisao… Hisao…"

        "Despite her clouded eyes being shut, her tightening grip on my shoulders show that she's nearing the end of her endurance."

        "As our breathing becomes more and more ragged, I rapidly feel my limit approaching as well."

        "A series of harsh breaths is the only warning before her final gasp of ecstasy, her entire body tensing and her fingernails digging into my shoulders."

        "My loins hit hers, both of us frozen against each other in climax."

        with Fade(0.5,1.0,4.0, color="#FFF")
        stop music fadeout 8.0

        "In a few precious seconds, it's all over, Lilly slumping forward onto me as I try to regain myself."

        hi "That was… good…"

        "She takes a gulp of air before replying, steadying herself as she nods."

        li "Mm…"

        "She bows her head down to give me a small kiss, my hand reaching up to hold strands of her disheveled hair as we once again sit in blissful silence."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .the_momentary_present:
        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
        play ambient sfx_trainint fadein 5.0

        scene ev lilly_trainride_ni
        show train_scenery_ni
        show train_scenery_fg_ni
        show lilly_trainride_ni norm at train_shake
        with locationchange

        "After a chaotic dash to the station and finding our seats in the otherwise deserted carriage, we promptly crashed. Looking at the time - close to midnight - it's little surprise that few take this particular train."

        "Hanako is fast asleep on Lilly's shoulder and I can only barely muster the energy to stay awake. The excitement we had a while ago probably didn't help."

        "I'd probably be pretty depressed about going back to school if my brain was actually working."

        "As it is, though, the sight of the night-time scenery scrolling by is surprisingly beautiful."

        "My loud yawn is nearly wholly drowned out by the clacking of the train tracks and the old carriage's rattling."

        hi "So tired…"

        play music music_comfort fadein 2.0

        show lilly_trainride_ni ara
        with charachange

        li "And whose fault is that, Hisao?"

        "She really does toe the line between insulting and amusing sometimes, though I manage to wring out a weary smile."

        "I look back out the window, my reflection just visible on the clear pane. Truth be told, she's perfectly correct. If it weren't for that little interlude a few hours ago, both of us would have a lot more energy."

        "On top of that, we both had to take another bath, very nearly making us late for the train's departure."

        hi "Yeah, yeah, it was mine. Still, getting into a bath with a guy is a dangerous thing to do."

        show lilly_trainride_ni smile
        with charachange

        li "Evidently."

        hi "Sorry. I guess I kind of took advantage of the situation back there."

        show lilly_trainride_ni weaksmile
        with charachange

        li "Well… I didn't exactly hate it…"

        "As she trails off, I look back to her. My eyes narrow as I see her slightly reddened cheeks and small grin, her mind obviously elsewhere."

        hi "Say it."

        li "I… knew the possibility of it happening… was there."

        hi "I knew it. You're just as dirty-minded as I am."

        "She quickly coughs into her free hand, making her disapproval crystal clear."

        show lilly_trainride_ni pout
        with charachange

        li "That's a rather crude way of putting it."

        hi "Oh? And you would suggest?"

        li "I merely have a healthy adolescent sex drive."

        hi "So in other words, dirty-minded."

        "Almost seeming to sense the moment, Hanako mumbles quietly as she furrows her brow in Lilly's lap."

        show lilly_trainride_ni opensmile
        with charachange

        "Lilly's look of disapproval melts away as she gently smiles and strokes her hand on Hanako's long, dark hair."

        "All I can do is watch. Watch and smile."

        "If someone were to ask me when I fell in love with her, I wouldn't be able to answer. The best I'd be able to come up with is 'it just happened at some point, but I didn't realize it.'"

        "If someone were to ask me why I love her, though, then I could answer much more easily."

        hi "You really love Hanako, don't you?"

        show lilly_trainride_ni smile
        with charachange

        "She gives a deep nod, smiling warmly."

        menu:
            with menueffect
            li "It's a pity we have to return to school. She seemed to relax so much while we were all away."

            "Talk about Hanako.":
                call a3lc4o1

            "Talk about school.":
                call a3lc4o2

        hi "On the bright side, it won't take long for the summer holidays to arrive after our exams are finished. We could come back here during the summer holidays if you want."

        "For a moment she thinks on the notion, her face becoming somewhat distant. I can only guess she's reflecting on all that's happened here."

        show lilly_trainride_ni opensmile
        with charachange

        li "That would be… good, I think."

        "I nod approvingly, smiling at her."

        "Summer, together with Lilly. This idea seems like the perfect way to spend our holiday."

        stop music fadeout 3.0
        stop ambient fadeout 3.0

        if _in_replay:
            return

    return

label a3lc1o1:
    hi "I have no idea what it means. Enlighten me."

    ke "I just lost 1000 yen, man! 1000 yen! Damn, this is the worst day ever."

    return

label a3lc1o2:
    "I dig into my food, hoping he'll take the hint from my silence."

    ke "I just lost 1000 yen, man! 1000 yen! Damn, this is the worst day ever."

    "No such luck."

    return

label a3lc2o1:
    "Actually, this may be a rather fortuitous meeting."

    hi "Hey. Excuse me, do you know if Hanako's come out of her room today or not? She doesn't seem to be answering."

    "Girl" "Ikezawa is Ikezawa. Her not answering the door is totally normal. That tall foreign girl's the only person she'll ever talk to, after all."

    "She gives a shrug before walking off down the hallway, having much more important matters to attend to than Hanako or me."

    "Her dismissive attitude annoys me."

    "Hanako must have a reputation as a hermit; a reputation that doesn't seem outright undeserved, at least in the time before we'd met."

    return

label a3lc2o2:
    hi "Hey. Sorry, don't mind me."

    "I think the situation with Hanako should be kept as private as possible, for her sake. I don't really know anything about what's happened to her, and my gut tells me that it's not physical sickness that's befallen her."

    "She doesn't need rumors about her going around. As much as it may pain me to think so, she'd likely prefer to keep her status as a strangely-ignored member of the class over having people talk behind her back."

    "Girl" "Whatever."

    "With that, she turns and walks down the hallway without a second thought. How rude."

    return

label a3lc3o1:
    hi "Come on, you worry about me more than I do at times. It just means I have to sleep a bit longer, that's all."

    show lilly basic_reminisce_cas
    with charachange

    li "But still…"

    hi "I'd say that I look absolutely fine, but I guess that wouldn't have a lot of meaning for you."

    show lilly basic_displeased_cas
    with charachange

    "She gives a sigh of consternation before trailing off with an amused chuckle, giving up the point."

    show lilly basic_weaksmile_cas
    with charachange

    li "If you say so. Please do take care of yourself, Hisao."

    hi "Go on, Hanako could use some help."

    hide lilly
    with dissolve

    "She moves to protest, but reluctantly acquiesces and disappears into the kitchen, her hand running along the smooth white walls as she slowly walks."

    return

label a3lc3o2:
    hi "Hanako could… probably use some help."

    show lilly basic_displeased_cas
    with charachange

    hide lilly
    with dissolve

    "Lilly seems about to protest for a moment, but eventually acquiesces, nodding before leaving for the kitchen."

    return

label a3lc4o1:
    $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

    hi "I wouldn't worry. Hanako's been gaining confidence thanks to you, at least for as long as I've known you two."

    show lilly_trainride_ni weaksmile
    with charachange

    "She gives a self-deprecating sigh."

    li "I think I merely provided her with company and support. Since she came to know you she's opened up much more, even to me."

    "I get the feeling she's understating her influence on Hanako, especially given that before the two came to know each other, Hanako had no friends to speak of."

    "The friends I'd had in my previous school fulfilled what I'd have expected of them, for the most part simply being there for idle chatter, but in Hanako and Lilly there really feels to be more to their relationship."

    "A part of me envies it, but another can't ignore the fact that the school year will eventually end. After graduation, I really have no idea what Hanako will do. This trip has shown me just how much we've all come to depend on one another."

    "Indeed, we're all going to have to make decisions. Maybe that's the reason why, despite our return to school also heralding a return to the normalcy of everyday life, I can't help feeling a little restless."

    return

label a3lc4o2:
    $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

    hi "Indeed. Exams will be starting, too, which will be another thing to deal with. Think you're ready for them?"

    show lilly_trainride_ni weaksmile
    with charachange

    li "I think so. I don't think it will be a pleasant period at all, though."

    "I can't say I disagree with her. The exams had completely slipped my mind for a while now, and even though I may score well on most of our tests, I can't assume that I can pass easily with so little studying beforehand."

    "Lilly does seem more studious, or at least more regimented, than me. That said, she has to contend with doing rather badly in some subjects no matter how much she tries."

    hi "At least they'll only last a couple of weeks."

    return
