# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a1_monday:
    label .out_cold:
        scene bg op_snowywoods
        show snow
        with Dissolve(2.0)

        play music music_serene fadein 2.0

        "A light breeze causes the naked branches overhead to rattle like wooden windchimes."

        "This is a popular retreat for couples in the summer. The deciduous trees provide a beautiful green canopy, far out of sight of teachers and fellow students."

        "But now, in late winter, it feels like I'm standing under a pile of kindling."

        "I breathe into my cupped hands and rub them together furiously to prevent them from numbing in this cold."

        hi "Just how long am I expected to wait out here, anyway? I'm sure the note said 4:00 PM."

        "Ah yes… the note… slipped between the pages of my math book while I wasn't looking."

        "As far as clichés go, I'm more a fan of the letter-in-the-locker, but at least this way shows a bit of initiative."

        "As I ponder the meaning of the note, the snowfall gradually thickens."

        "The snowflakes silently falling from the white-painted sky are the only sign of time passing in this stagnant world."

        "Their slow descent upon the frozen forest makes it seem like time has slowed to a crawl."

        play sound sfx_rustling

        "The rustling of dry snow underfoot startles me, interrupting the quiet mood. Someone is approaching me from behind."

        mystery "Hi… Hisao? You came?"

        "A hesitating, barely audible question."

        "However, I recognize the owner of that dainty voice instantly."

        "I feel my heart skip a beat."

        "It's a voice I've listened to hundreds of times, but never as more than an eavesdropper to a conversation."

        "I turn to face this voice, the voice of my dreams, and my heart begins to race…"

        scene ev other_iwanako_start
        show snow
        with GenericWhiteout(0.5, 0.0, 5.0)

        hi "Iwanako? I got a note telling me to wait here… it was yours?"

        "Dammit. I spent all afternoon trying to come up with a good line and that was the result."

        "Pathetic."

        "Iwanako" "Ahmm… yes. I asked a friend to give you that note… I'm so glad you got it."

        "A shy, joyous smile that makes me so tense I couldn't move a single muscle even if I tried."

        stop music fadeout 10.0

        scene bg op_snowywoods
        show snow
        with GenericWhiteout(0.5, 0.0, 2.0)

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve(0.1)

        hide heartattack alpha
        with Dissolve(0.7)

        pause 0.7

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve(0.1)

        hide heartattack alpha
        with Dissolve(0.7)

        "My heart is pounding now, as if it were trying to burst out from my chest and claim this girl for itself."

        scene ev other_iwanako
        show snow
        with GenericWhiteout(0.5, 0.0, 3.0)

        hi "So… ah… here we are. Out in the cold…"

        "Once again, the wind stirs up the branches. The cacophonous noise is music to my ears."

        "Iwanako flinches ever so softly against the gust of wind."

        "As it passes, she rights herself, as if supported by some new confidence."

        "Her eyes lock with mine and she lazily twirls her long, dark hair around her finger."

        "All the while, the anxious beating of my heart grows louder."

        scene bg op_snowywoods
        show snow
        with GenericWhiteout(0.5, 0.0, 2.0)

        "My throat is tight; I doubt I could even force a word out if I tried."

        "Iwanako" "You see…"

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve(0.1)

        hide heartattack alpha
        with Dissolve(0.4)

        "Iwanako" "…I wanted to know…"

        stop music fadeout 0.5

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve(0.1)

        hide heartattack alpha
        with Dissolve(0.2)

        pause 0.7

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve(0.1)

        hide heartattack alpha
        with Dissolve(0.2)

        "Iwanako" "… if you'd go out with me…"

        "I stand there, motionless, save for my pounding heart."

        "I want to say something in reply, but my vocal cords feel like they've been stretched beyond the breaking point."

        play music music_tragic fadein 0.05

        "Iwanako" "… Hisao?"

        "I reach up to try to massage my throat, but this only sends spikes of blinding pain along my arms."

        "Iwanako" "Hisao?!"

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve(0.1)

        hide heartattack alpha
        with Dissolve(0.8)

        "My whole body freezes, save for my eyes, which shoot open in terror."

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve(0.1)

        hide heartattack alpha
        with Dissolve(0.8)

        pause 0.15

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve(0.1)

        hide heartattack alpha
        with Dissolve(0.8)

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve(0.1)

        hide heartattack alpha
        with Dissolve(0.8)

        pause 0.05

        play sound sfx_heartstop
        show heartattack alpha
        with Dissolve(0.1)

        stop music fadeout 0.3

        show heartattack residual
        with Dissolve(0.8)

        "Iwanako" "HISAO!"

        "The beating in my chest suddenly stops, and I go weak at the knees."

        show passoutOP1

        nvl show Dissolve(0.2)

        n "{vspace=210}The world around me - the canopy of bare branches, the dull winter sky, Iwanako running towards me - all these fade to black."

        n "{vspace=30}The last things I remember before slipping away are the sounds of Iwanako screaming for help and the incessant clatter of the branches above…"

        nvl hide Dissolve(3.0)

        nvl clear

        pause 1.0

        scene black

        if _in_replay:
            return

    call act_op("op_1_opus.webm")
    pause 1.0

    label .bundle_of_hisao:
        centered "It's been four months since my heart attack."
        with dissolve

        scene bg hosp_room
        show sakura
        show hospitalmask
        with Dissolve (1.5)

        $ renpy.music.set_volume(0.5, 0.0, channel="music")
        play music music_rain fadein 4.0

        nvl show dissolve

        n "{vspace=60}In that whole time, I can probably count the times I've left this hospital room unsupervised on one hand."

        n "Four months is a pretty long time when you're left alone with your thoughts. So, I've had plenty of time to come to terms with my situation."

        n "Arrhythmia."

        n "A strange word. A foreign, alien one. One that you don't want to be in the same room with."

        n "A rare condition. It causes the heart to act erratically and occasionally beat way too fast. It can be fatal."

        n "Apparently, I've had it for a long time. They said it was a miracle that I was able to go on so long without anything happening."

        n "Is that really a miracle? I guess it was supposed to make me feel better, more appreciative of my life."

        n "It really didn't do anything to cheer me up."

        nvl clear

        n "{vspace=150}My parents, I think, were hit harder by the news than I was. They practically had two hemorrhages apiece."

        n "{vspace=30}I had already had a full day by then to digest everything. To them, it was all fresh. They were even willing to sell our house in order to pay for a cure."

        n "{vspace=60}Of course there isn't a cure."

        nvl clear

        n "{vspace=30}Because of the late discovery of this… condition, I've had to stay at the hospital, to recuperate from the treatments."

        n "When I was first admitted, it felt as if I was missed…"

        n "For about a week, my room in the ward was full of flowers, balloons and cards."

        n "But, the visitors soon dwindled and all the get-well gifts began trickling down to nothing shortly after."

        n "I realized that the only reason I had gotten so many cards and flowers was because sending me their sympathy had been turned into a class project."

        n "Maybe some people were genuinely concerned, but I doubt it. Even in the beginning, I barely had visitors. By the end of the first month, only my parents came by on a regular basis."

        n "Iwanako was the last to stop visiting."

        n "After six weeks, I never saw her again. We never had that much to talk about when she visited, anyway."

        n "We didn't touch the subject that was between us on that snowy day ever again."

        nvl clear

        n "{vspace=30}The hospital?"

        n "It's not really a place I'd like to live in."

        n "The doctors and nurses feel so impersonal and faceless."

        n "I guess it's because they are in a hurry and they have a million other patients waiting for them, but it makes me feel uncomfortable."

        n "For the first month or so, I asked the head cardiologist every time I saw him for a rough estimate of when I'd be able to leave."

        n "He never answered anything in a straightforward way, but told me to wait and see if the treatment and surgeries worked."

        n "{vspace=30}So, I idly observed the scar that those surgeries had left on my chest slowly change its appearance over time, thinking of it as some kind of an omen."

        n "I still ask the head cardiologist about leaving, but my expectations are low enough now that I'm not disappointed any more when I don't get a reply. The way he shuffles around the answer shows that there is at least some hope."

        nvl clear

        n "{vspace=120}At some point I stopped watching TV. I don't know why, I just did."

        n "Maybe it was the wrong kind of escapism for my situation."

        n "{vspace=30}I started reading instead. There was a small 'library' at the hospital, although it was more like a storeroom for books. I began working my way through it, one small stack at a time. After consuming them, I would go back for more."

        n "I found that I liked reading and I think I even became a bit addicted. I started feeling naked without a book in my hands."

        n "{vspace=30}But I loved the stories."

        nvl clear

        n "{vspace=30}That was what my life was like."

        n "{vspace=30}The days became increasingly harder to distinguish from each other, differing only by the book I was reading and the weather outside. It felt like time blurred into some kind of gooey mass I was trapped inside, instead of moving within."

        n "A week could go by without me really noticing it."

        n "Sometimes, I'd pause in realization that I didn't know what day of the week it was."

        n "But other times, all the things that surrounded me would painfully crash into my consciousness, through the barrier of nonchalance I had set up for myself."

        n "The pages of my book would start to feel sharp and burning hot and the heaviness in my chest would become so hard to bear that I had to put the book aside and just lay down for a while, looking at the ceiling as if I was going to cry."

        n "But that happened only rarely."

        n "{vspace=30}And I couldn't even cry."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl hide dissolve

        nvl clear

        "Today, the doctor comes in and gives me a smile. He seems excited, but not very. It's like he is trying to make an effort to be happy on my behalf."

        "My parents are here. It's been a few days since I've last seen them. Both of them are even sort of dressed up. Is this supposed to be some kind of special occasion? It's not a party."

        "There is this ritual the head cardiologist has. He takes his time, sorting his papers, then setting them aside as if to make a point of the pointlessness of what he just did."

        "Then he casually sits down on the edge of the bed next to mine. He looks me in the eyes for a moment."

        "Doctor" "Hello, Hisao. How are you today?"

        "I don't answer him but I smile a little, back at him."

        "Doctor" "I believe that you can go home; your heart is stronger now, and with some precautions, you should be fine."

        "Doctor" "We have all your medication sorted out. I'll give your father the prescription."

        "The doctor hands a sheet of paper to my dad, whose expression turns wooden as he reads it quickly."

        "Dad" "So many…"

        "I take it from his hand and take a look myself, feeling numb. How am I supposed to react to this?"

        $ renpy.music.set_volume(0.5, 2.0, channel="music")

        scene white
        with Dissolve(2.0)

        show drugs:
            xpos 0 ypos 0
            easein 25.0 xanchor 0.5

        "The absurdly long list of medications staring back at me from the paper seems insurmountable. They all blend together in a sea of letters."

        "This is insane."

        "Side effects, adverse effects, contraindications and dosages are listed line after line with cold precision."

        "I try to read them, but it's so futile."

        "I can't understand any of it. Attempting to only makes me feel sicker."

        "All this… for the rest of my life, every day?"

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        scene bg hosp_room
        show sakura
        show hospitalmask
        with fade

        "Doctor" "I'm afraid that is the best we can do at this point."

        "Doctor" "However, new medications are always being developed, so I wouldn't be surprised to see that list fade over the years."

        "Years… What kind of confidence booster is that? I'd have felt better if he hadn't said anything at all…"

        "Doctor" "Also, I've spoken with your parents and we believe that it would be best if you don't return to your old school."

        "What!?"

        "Dad" "Please, calm down, Hisao. Listen to what the doctor has to say…"

        "Calm down? The way he says it tells me he knew full well that I wouldn't like it. Am I going to be home schooled?"

        "Whatever of my concern shows, it's ignored."

        "Doctor" "We all understand that your education is paramount; however, I don't think that it's wise for you to be without supervision."

        "Doctor" "At least not until we're sure that your medication is suitable."

        "Doctor" "So, I've spoken to your parents about a transfer."

        "Doctor" "It's a school called Yamaku Academy that specializes in dealing with disabled students."

        "Disabled? What? Am I…"

        "Doctor" "It has a 24-hour nursing staff and it's only a few minutes from a highly regarded general hospital. The majority of students live on the campus."

        "Doctor" "Think of it as a boarding school of sorts. It's designed to give students a degree of independence, while keeping help nearby."

        "Independence? It's a school for disabled kids. Don't try to disguise that fact."

        "If it was really that 'free,' there wouldn't be a 24-hour nursing staff, and you wouldn't make a hospital being nearby a selling point."

        "Dad" "Of course, that's only if you want to go. But… your mother and I aren't really able to home school you."

        "Dad" "We went out there and had a look a couple of weeks back; I think you'd like it."

        "It looks like I really don't have a choice."

        "Doctor" "Compared to other heart problems, people with your condition usually tend to live long lives. You'll need a job one day and this is a good opportunity to continue your education."

        "This isn't an opportunity, don't call it an opportunity. Don't call it a goddamned opportunity."

        "Doctor" "Well, you should be excited at the chance to go back to school. I remember you wanted to return to school, and while it's not the same one…"

        "A special school. That's…"

        "An insult. That is what I want to say. It's a step down."

        "Dad" "It's not what you think. All of the students there are pretty active, in their own sort of way."

        "Dad" "It's geared towards students that can still get around and learn, but just need a little help… in one way or another."

        "Doctor" "Your father's right. And many of the graduates of the school have gone on to do amazing things. A person doesn't have to be held back by their disability."

        "Doctor" "One of my colleagues in another hospital is a graduate."

        "I don't care. A person doesn't have to be held back by their disability? That's what a disability is."

        "I really hate that something so important was decided for me. But what can I do about it? A 'normal' life is out of the question now."

        stop music fadeout 10.0

        "It's funny, I had always thought my life was actually kind of boring, but now I miss it."

        "I want to protest. I want to blame this lack of reaction on shock, or fatigue. I could easily yell out something now - something about how I can go back to school anyway. But, no."

        "I don't say anything. The fact is that I know now it's futile."

        "I look around the room, feeling very tired of all this. The hospital, doctors, my condition, everything. I don't see anything that would make me feel any different."

        "There really isn't a choice. I know this, but the thought of going to a disabled school… what are those even like? As much as I try to put a positive spin on this, it's very difficult."

        "But let me try."

        "A clean slate isn't a bad thing."

        "That is all I can think of to get me through this. At least I still have something; even if it's a 'special school,' it's something. It's a fresh start, and my life isn't over. It would be a mistake to just resign myself to thinking that."

        "At the very least, I'll try to see what my new life will look like."

        if _in_replay:
            return

    call act_op("tc_act1_opus.webm")

    label .gateway_effect:
        scene bg school_gate
        with Dissolve(3.0)

        play music music_happiness

        "The gate looked far too pompous for what it was."

        "In fact, gates in general seem to do that, but this one especially so."

        "Red bricks, black wrought iron and gray plaster, assembled into a whole that didn't feel welcoming at all."

        "I wondered if it looked like what a gate for a school should look like, but couldn't really decide. Probably no."

        "Of course I didn't want to get stuck on thinking about the gate for too long, so I entered through it with a brisk pace that felt surprisingly good."

        "Moving forward feels good."

        scene bg school_courtyard
        with locationchange

        "So I walk towards the main building of Yamaku Academy with this brisk pace. I'm alone, as my parents are taking my stuff to the dorms, and there's supposed to be someone waiting for me."

        "The grounds are incredibly lush, filled with green."

        "It doesn't feel like the kind of grounds a school would have, more like a park, with a clean walkway going past trees and the smell of fresh-cut grass and all other park-like things."

        "Words like 'clean' and 'hygienic' pop into my mind. It makes me shudder."

        "I shake them off. Stay open-minded now. It's your new life. You have to take it as it comes."

        "That's what I tell myself."

        "A few big buildings loom behind the leafy canopies, too big and too many for just a school."

        "Everything seems off; it's different from what I thought I knew about schools."

        "It's an uncanny valley. Even though I was told this is my new school, in the back of my head it doesn't feel like one."

        "I wonder if the feeling is real or caused by my expectations of a school for the disabled."

        "Speaking of that, I don't see anyone else here. It's kinda eerie."

        "It makes me wish there was somebody here so I could anchor myself to something tangible instead of having this feeling that I stepped into another dimension."

        "The trees hum with the wind and the green hues flashing all around me catch my attention."

        "It makes me think about hospitals again, how they say that the operating rooms are painted green because green is a calming color."

        "So why am I feeling so anxious, despite all this greenery?"

        "…"

        "Only after I stand in front of the haughty main building, I surprise myself by realizing why the gate bothered me:"

        "It was the last chance I had to turn back, even if I had no life I could return to."

        "But still, after entering, there was absolutely no way I could go back any more."

        "Feeling nervous and with this realization set in my head, I open the front door."

        scene bg school_lobby
        with locationchange

        "A tall man with bad posture notices me as I enter. We're the only people in the lobby, so it's only logical."

        show muto normal at center
        with charaenter

        mu_ "You must be… Ni… Na… Niki?"

        hi "Nakai."

        show muto smile
        with charachange

        mu_ "So you are. Excellent. I'm your homeroom and science teacher. My name is Mutou."

        mu "Welcome."

        "We exchange a handshake that is neither firm nor sloppy, and he looks at his watch."

        show muto irritated
        with charachange

        mu "The head nurse asked you for a brief check-in visit, but there's no time for that now."

        hi "Oh. Should I go later?"

        show muto normal
        with charachange

        mu "Yes, afternoon is probably fine. We should get going and introduce you to the rest of the class. They're waiting already."

        "Waiting for me? I don't really like being the center of attention, but I guess it's inevitable in a situation like this."

        "Somehow, not knowing what is waiting for me makes me feel really nervous."

        "Thinking of this, I almost miss what the teacher is saying."

        menu:
            set choices
            with menueffect

            mu "Do you want to introduce yourself to the class?"

            "Why?":
                $ wanted_introduce = False

                call a1c1o1

            "Yeah, of course.":
                $ wanted_introduce = True
                $ attraction_sc += 1

                call a1c1o2

        scene bg school_staircase2
        with locationchange

        "My heart is pounding in my chest and it keeps me thinking about my condition as I follow the teacher up the stairs."

        scene bg school_hallway3
        show muto normal at center
        with locationchange

        "The third door down the third floor corridor is marked as the classroom for class 3-3."

        play sound sfx_dooropen

        "Mutou opens the door and enters."

        show muto:
            easeout 0.5 xpos 0.4 alpha 0.0

        pause 0.5

        hide muto

        mu "Good morning everyone, sorry I'm late again."

        stop music fadeout 2.0

        "I hesitate for a split second at the door, freezing on the spot."

        if _in_replay:
            return

    label .enter_stage_left:
        scene bg school_hallway3

        "Ah, get a grip! This is a big step, I know that… But there isn't any point to worrying so much about it, at least not this soon."

        scene ev hisao_class_start
        with fade

        play music music_normal fadein 0.5

        "I follow the teacher into the classroom and look around, partially so I won't have to meet the curious gazes of my new classmates."

        "It's pretty spacious; the ceiling is unusually high and there's lots of space left over around and inbetween the desks."

        "An entire wall taken up by blackboards and the high, old fashioned windows only make it seem larger."

        "The students' desks are just standard wooden desks with a shelf underneath for books and wooden chairs with metal frames. Simple and efficient."

        "I stop walking in front of the classroom and face the other students. They all look normal, like students in any other school. But then, why would they be here?"

        scene ev hisao_class_move

        "They're probably like me and have something wrong with them, only it's just not immediately obvious. Then, I notice that one of the girls seems to be missing the thumb of her right hand. It's a little jarring."

        "Despite the natural tendency to listen when someone's talking about you, I tune out the teacher's speech halfway through while he introduces me to the class."

        "I notice a flash of dark hair and see that someone is looking at me. A girl with really long, straight hair that is pretty eye-catching. As she sees me looking back at her, she covers her face with her hands as if it will make her invisible."

        "There is one boy with a cane leaning against the lockers at the rear of the class. It's weird seeing someone so young with a cane."

        "Another girl seems to be making some weird hand motions. Sign language? She peers at me over the rims of her glasses, then goes back to whatever she's doing."

        "She's kind of cute. So is the cheery-looking girl with pink hair sitting next to her. She's really hard to miss; I don't know how I didn't notice her the moment I walked in…"

        mu "…please welcome our newest classmate."

        "He claps his hands and so does everyone else, except one girl in the first row who has only one hand. I cringe a little, but hide it by bowing in thanks for this applause I did not deserve."

        if wanted_introduce or _in_replay:
            "A collective silence tells me that I should open my mouth now."

            hi "So… I'm Hisao Nakai."

            "And after that?"

            hi "My hobbies are reading and soccer. I hope to get along well with everyone even though I'm a new student."

            "And after that?"

            "I'm being so boring. This is exactly like every self-introduction ever. I should say something more. Something more exciting."

            "I end up saying nothing, and the teacher picks up from there."

            "Everyone seems to be satisfied even with what little I said, though. A few girls are whispering to each other, throwing glances at me. It could've gone worse."

            "…"
        else:
            "After the applause, there is a brief silence that nobody seems to want to be responsible for breaking."

            "The teacher soon realizes that he should probably say something. He opens up with some unintelligible noise, shuts up as he loses his momentum, and then starts introducing me."

            "Nobody seems to be too interested."

            "Maybe I should've said yes to the self-introduction thing."

            "Probably realizing he doesn't know anything about me, he just ends up saying my name wrong again, and asks me to write it on the blackboard."

            "I do that, and turn back to face the class, feeling awkward."

        scene ev hisao_class_end

        "I listen to the teacher as he drones about getting along while letting my gaze sweep across the classroom."

        "Everyone seems to be listening to him intently and when he's done, they clap their hands again which feels like a weird thing to do."

        "The first row girl claps on this round, with her one hand against her other wrist that ends in a bandaged stump."

        "It makes me feel a little bad."

        scene bg school_scienceroom at bgright
        show muto normal at center
        with fade

        mu "We're going to be doing some group work today, so that'll give you a chance to talk with everyone. Is that okay with you?"

        hi "Yeah, it's fine with me."

        show muto smile
        with charachange

        mu "That's good, you can work with Hakamichi. She is the class representative."

        mu "She can explain anything you might want to know. And who else would be able to do that better, right?"

        hide muto
        with charaexit

        "How could I know?"

        "The teacher passes out the day's assignments and announces that we will be working in groups of three."

        "It hits me that I don't know who Hakamichi is. Slow. The teacher seems to catch my helpless expression."

        mu "Oh, right. Hakamichi is right there, Shizune Hakamichi."

        show misha perky_smile at center
        with charaenter

        "As he calls out her name, the cute, bubbly looking girl with bright pink hair and gold eyes waves her hand at me. I take a seat next to her, by the window."

        hi "Hey, I guess you're Hakamichi, right? It's nice to meet you."

        stop music fadeout 1.0

        show misha cross_laugh
        with charachange

        mi_shi "Hahaha~!"

        "What? I'm caught off guard by her laughter."

        show misha hips_grin
        with charachange

        mi_shi "It's nice to meet you, too!{w=0.5} But~!"

        mi_not_shi "It's nice to meet you, too! But~!{fast}, I'm not Hakamichi, I'm Misha! This is Hakamichi. Shicchan~!"

        play music music_shizune fadein 1.0

        show misha at twoleft
        show bg at center
        with charamove

        show shizu basic_normal at tworight
        with charaenter

        "Giggling, Misha points to the girl next to her, the one I saw using sign language before. It looks like she has been staring at me this whole time. She nods once nonchalantly to show that she acknowledges my presence… but only barely."

        "She has short, yet carefully, neatly brushed hair, a pair of oval-shaped glasses balanced on the tip of a dainty nose, and dark blue eyes that seem to alternate every few seconds between analytical and slightly bored."

        hi "It's nice to meet you."

        show shizu behind_blank
        with charachange

        shi "…"

        show misha perky_smile
        with charachangealways

        show misha sign_smile
        with charachangealways

        show misha perky_smile
        with charachangealways

        "She immediately looks at Misha, who smiles and makes a few quick gestures with her hands."

        show shizu adjust_happy
        with charachangealways

        show shizu behind_smile
        with charachangealways

        "Hakamichi nods and makes a few gestures of her own."

        "I start to wonder if the teacher was messing with me, saying things like 'you'll be able to talk to people' and 'who better to explain things to you.'"

        show misha hips_smile
        with charachange

        mi "I can see you're a little confused, right?, right? But, I understand why you would think I was Shicchan!"

        mi "Shicchan is deaf, so I'm the person who translates things back and forth for her."

        show misha hips_grin
        with charachange

        mi "I'm like an interpreter~! She says it's nice to meet you, too!"

        show shizu basic_normal2
        with charachange

        shi "…"

        show misha perky_smile
        with charachange

        mi "You're the new student, aren't you? Well, Shicchan, of course he is! If he wasn't, he would have been standing up there for no reason, right? Right~!"

        if wanted_introduce or _in_replay:
            mi "He seems like a very interesting person, doesn't he~!"
        else:
            "Misha looks at me with a weird expression, then continues."

            mi "We don't know much about him, but maybe we'll find out later."

            "Maybe I should've introduced myself after all. Anything would've given a better first impression than the teacher's drone and fumbling with my name."

        mi "We knew there was going to be a new student, but we didn't know you would be here today. So soon! Hicchan, right?"

        "Hicchan…?"

        show misha hips_grin
        with charachange

        mi "Yup~! It fits, doesn't it?"

        "Did I say it out loud? It's just a surprise. I've never liked that nickname."

        hi "I don't really see how."

        show misha cross_grin
        with charachange

        mi "It fits~! You look just like I imagined!"

        show shizu adjust_smug
        with charachange

        shi "…"

        show misha cross_laugh
        show shizu adjust_happy
        with charachange

        mi "Hahahaha~! Yeah, you look just like a Hicchan!"

        hi "I wonder why everyone seems to think so…"

        shi "…"

        "Hakamichi taps her fingers on the desk to get Misha's attention. They gesture back and forth to each other excitedly, their hands a blur."

        show shizu adjust_happy
        with charachangealways

        show misha sign_smile
        with charachangealways

        show shizu behind_smile
        with charachangealways

        show misha perky_confused
        with charachangealways

        "Misha seems a little overwhelmed."

        show misha hips_grin
        with charachange

        mi "Ahaha~! Er, sorry about that!"

        show misha hips_smile
        with charachange

        mi "Shicchan wants you to know that she's the class rep, so if there is anything you need to know, you can feel free to ask her."

        show shizu behind_blank
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "Do you like the school so far? We can show you around a little if you haven't had the time to walk around and…{w=0.5}{nw}"

        show misha perky_smile:
            "misha perky_confused" with charachange

        extend " familiarize?{w=0.5}{nw}"

        show misha perky_confused:
            "misha perky_smile" with charachange

        extend " yourself with it!"

        "Misha stumbles with the hard word a bit, making it stick out in her otherwise fluid translation."

        hi "Thanks, that would be pretty helpful. Yeah, I just kind of came straight to class today."

        show shizu behind_frown
        with charachange

        shi "…"

        show misha hips_laugh
        with charachange

        mi "Hahaha~!"

        show misha hips_smile
        with charachange

        mi "That's no good! You should always try to learn as much as you can about where you're going before you go there. Not just with school, either~!"

        show misha hips_grin
        with charachange

        mi "Always! Even if it's a trip to the convenience store! Really, Shicchan? Hahaha~!"

        show misha perky_smile
        show shizu behind_smile
        with charachange

        "Learn about where you're going? I guess I didn't bother to do that, or just didn't care enough to do so."

        "I didn't look forward to this, even if I committed myself to go along with it half-assedly, but anyway."

        "I don't say anything, and Misha signs something that ends in a shrug. What was that? It seems like it was about me."

        "I feel like slumping over in my seat. Both of them are smiling, but that shrug hit me unexpectedly deeply."

        show misha perky_sad
        with charachange

        mi "You look down, are you okay?"

        show shizu basic_normal
        with charachange

        shi "…"

        show misha perky_smile
        with charachange

        mi "Don't take it the wrong way, please~! I hate it when people are afraid to ask questions! That's how people learn things, by asking~!"

        mi "Asking for help is perfectly normal, as much as needing help! Stop looking like you just failed a test!"

        show misha cross_laugh
        with charachange

        mi "Wahahaha~!"

        hi "All right."

        show shizu adjust_happy
        with charachange

        shi "…"

        show misha perky_smile
        with charachange

        mi "Ah, and another thing, you don't have to call Shicchan something so formal like 'Hakamichi' or 'class rep' all the time! Just call her Shicchan~!"

        stop music fadeout 0.5

        show shizu adjust_blush
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "Ahaha~! Okay, maybe that's too casual. Maybe 'Shizune' would be more appropriate?"

        show shizu basic_normal2
        with charachange

        shi "…"

        show misha hips_grin
        with charachange

        play music music_shizune fadein 5.0

        mi "Yup, yup~! 'Shizune' is fine!"

        hi "Heh. Okay, that would be a lot easier for me."

        "I feel a lot more at ease. Both of them seem so friendly, so I feel like an idiot for being so apprehensive earlier. Especially about Shizune, who I assumed would be all business."

        "Well, she still seems like that. Just less so, I guess."

        show shizu behind_frown
        with charachange

        shi "…!"

        show misha perky_confused
        with charachange

        mi "Huh? Oh, right, we haven't even touched the assignment! We should start work now, or Shicchan will get mad."

        hi "The assignment is also kind of long, so we should start now if we want to finish it before the end of class."

        show misha hips_laugh
        with charachange

        mi "Wahaha~! That too!"

        show shizu basic_frown
        with charachange

        shi "…"

        "Shizune glares at the two of us impatiently. I don't need to know sign language to understand that."

        hi "Okay, okay, I get the message."

        show shizu basic_normal
        with charachange

        shi "…"

        show misha perky_smile
        with charachange

        mi "After class, we can take a walk around the grounds together. It's a nice day today! Okay~?"

        "The assignment is actually very challenging to get through, combining aspects of being both difficult and unnecessarily long."

        stop music fadeout 6.0

        scene bg school_scienceroom
        with shorttimeskip

        "Still, we finish it a few minutes earlier than anyone else in the class, despite our late start. Shizune and Misha are really capable."

        "They're quite different, though. The class rep is as calm and professional as she looks, while Misha is a lot more playful and girlish. Not to mention a little more easily distracted."

        "To be honest, the two of them did most of the work. I feel guilty about that."

        play sound sfx_normalbell

        "The clock tower bells ring, signaling the end of the period. Time for lunch."

        scene bg school_hallway3
        with locationchange

        "Without knowing what else to do, I follow Misha, who is beckoning me into the hallway and down the stairs."

        if _in_replay:
            return

    label .in_the_nursery:
        scene bg school_staircase2
        with locationchange

        "We descend even below the lobby where I met Mutou, down to the bottom floor."

        play ambient sfx_crowd_indoors fadein 6.0

        scene bg school_cafeteria
        with locationchange

        "Just like everything in this school, the cafeteria seems too spacious and oddly modern in contrast to the classic exterior."

        "Its big windows open to the courtyard, towards the main gate."

        show misha hips_grin at center
        with charaenter

        play music music_ease

        mi "It's the cafeteria~!"

        "Her enthusiastic statement of the obvious makes people around us stare, but Misha doesn't seem to care so we proceed to the line."

        hide misha
        with charaexit

        "There is a rather long list of menu options, which seems great until I realize that many of them are to accommodate students who need special diets."

        "How nice. It almost feels like I'm back at the hospital, eating portions measured with scientific precision to meet the needs of the patients."

        "I pick something at random and follow Shizune to a table, sitting opposite of her."

        show misha hips_frown at twoleft
        show shizu basic_normal at tworight
        with charaenter

        "As I nibble indifferently at the food I'd rather not eat, Misha pokes me in the side to get my attention and points to Shizune."

        show misha perky_smile
        show shizu basic_frown
        with charachange

        shi "…"

        "I don't understand sign, so the point escapes me."

        "Maybe looking at a person who 'talks' to you is proper and polite?"

        show misha hips_smile
        show shizu behind_blank
        with charachange

        mi "Do you want to know something?"

        hi "What?"

        show misha hips_grin
        with charachange

        mi "About anything! We're your guides so you should ask if there is something~!"

        menu:
            set choices
            with menueffect

            hi "Hmm, I wonder…"
            "Ask about the library.":
                $ attraction_hanako += 1

                call a1c2o1

            "Ask about Shizune's deafness.":
                call a1c2o2

            "I think I got everything I need to know.":
                $ attraction_sc += 1

                call a1c2o3

        "Misha and Shizune sign back and forth very animatedly, throwing sideway glances at me but Misha refrains from translating."

        "Maybe they are talking about secret girl stuff or something."

        "…"

        stop music fadeout 3.0
        $ renpy.music.set_volume(1.0, .5, channel="ambient")
        stop ambient fadeout 3.0

        "I quickly notice a conversation in sign is not enough to fill a silence."

        scene bg school_scienceroom
        with shorttimeskip

        play music music_daily fadein 0.5

        "We arrive in the classroom early, but we're not the first."

        show hanako emb_downtimid:
            xpos 1.0 xanchor 0.8
        with charaenter

        "That dark haired girl I noticed before is slumped over her desk at the last row."

        show hanako defarms_shock
        with vpunch

        show hanako:
            ease 2.0 xpos 1.0 xanchor 0.6

        "She jumps a little when Misha crashes into the room with the elegance of a rhino."

        "She shrinks deeper into her seat. I can feel her tension all the way from here, as if she were slowly turning into stone just from our presence."

        "Misha and Shizune either don't notice or don't mind it, as they walk directly past her to their seats and begin to converse."

        show hanako at offscreenright
        with charamove

        hide hanako

        "I'm left wondering about her, even when the classroom slowly fills with other students and finally, the teacher."

        "Getting into the rhythm of school feels strange; it's as if my brain remembers how this is done, but my body doesn't."

        "Towards the end of the class I start yawning and counting the minutes left."

        "I shouldn't be this tired on my first day of school."

        "Maybe it's the long time spent in the hospital that made me like this. I'm even feeling physically weak and lifeless."

        scene bg school_scienceroom
        with shorttimeskip

        play sound sfx_normalbell

        "Before long, the final bell rings."

        "School is finally over for the day."

        "Beside me, Misha and Shizune are having a short conversation. After a bit of deliberation, Misha turns to me."

        show shizu behind_blank at tworight
        show misha perky_smile at twoleft
        with charaenter

        shi "…"

        mi "Unfortunately we can't stay and show you around today, Hicchan. We've got to hurry already, since there is a lot of work for us to do."

        show shizu basic_normal2
        with charachange

        shi "…"

        mi "You'll find your way around here, I'm sure of it."

        hi "Ah, wait! The teacher said I'd have to see the nurse. Where do I have to go?"

        show shizu behind_smile
        show misha hips_grin
        with charachange

        mi "Is that so? We can at least show you that much~!"

        mi "Come on, the nurses have their own building, so we have to go outside."

        hide shizu
        hide misha
        with charaexit

        scene bg school_hallway3
        with locationchange

        "We join the flow of students making their way down the stairwell and outside, with the girls pointing out other senior classrooms in the same hallway as ours."

        scene bg school_courtyard
        with locationskip

        "When we get outside, the girls make their way to the smaller building right next to the school."

        "It's built in the same style, so it looks like it's actually a part of the main building."

        show shizu behind_smile at tworight
        show misha perky_smile at twoleft
        with charaenter

        shi "…"

        mi "This is the auxiliary building here. There's a lot of official and important stuff inside, like the Yamaku Foundation office and all the nurses' offices. They even have a swimming pool!"

        hi "How is that official?"

        show shizu behind_frustrated
        with charachange

        shi "…"

        show misha hips_grin
        with charachange

        mi "Don't be silly, Hicchan! It's for physical therapy of course."

        show misha sign_smile
        with charachange

        mi "Anyway, all the nursing staff facilities are in there too. The head nurse's office is on the first floor."

        show misha hips_smile
        show shizu behind_smile
        with charachange

        mi "You'll be fine from here, right~? We'll be going, then! See you tomorrow!"

        hi "Yeah, thanks. Bye."

        stop music fadeout 5.0

        hide shizu
        hide misha
        with charaexit

        "A whole building for stuff that has nothing to do with the actual education?"

        "I guess it's necessary for a place like this."

        scene bg school_nursehall
        with locationchange

        "I walk in, hoping that this really will be only a quick visit like the teacher said."

        "On a white door on the left is a green cross with the text 'Head Nurse' and a nameplate."

        play sound sfx_doorknock2

        "A voice from the inside responds to my knock almost immediately, but I can't quite make it out."

        "It sounded a bit like an invitation to open the door, so I invite myself further in."

        play sound sfx_dooropen

        scene bg school_nurseoffice
        with locationchange

        "The room is not large and it smells strange. A friendly-looking man turns around on his office chair to face me as I enter."

        "His desk is neat and tidy, but the bin under the table is overflowing with used medical utensils and there are at least a dozen coffee-cup rings lingering on the desk."

        play music music_nurse fadein 0.5

        show nurse neutral at center
        with charaenter

        nk_ "Hello there. What can I do for you today?"

        "He is young-looking and sort of rugged, but the dimples in his cheeks wash that impression away when he smiles."

        hi "Erm, are you the nurse?"

        show nurse grin
        with charachange

        "He smiles like a person who has heard this very same question hundreds of times."

        nk_ "Why yes, I am. It says so on the door, no?"

        nk_ "You can call me by my name or just 'the nurse' like everyone else."

        "Of course. I shake off my confusion, realizing I probably should grab his extended hand.{w} His handshake is rather firm and friendly."

        hi "Right… err, I'm a new student and my homeroom teacher told me to come and meet you. My name is Hisao Nakai."

        play sound sfx_snap

        "His eyes light up with revelation and he snaps his fingers."

        show nurse fabulous
        with charachange

        nk "Oh you're THAT Nakai. I was just reading your file in the morning."

        nk "Some kind of chronic arrhythmia and related congenital heart muscle deficiency, right?"

        "He gestures me to sit down in a vacant armchair in front of his desk."

        hi "Eh, yes."

        show nurse neutral
        with charachange

        nk "Good. Well, you've probably been briefed about the school enough, so I'll just go over this quickly."

        nk "We have all kinds of facilities available, mostly physical therapy and such."

        nk "There's always someone from my staff around, even at night, so never hesitate to call us if there is a problem."

        "The famous twenty-four-hour nursing staff."

        hi "Wow, this is like a hospital."

        nk "Well, not exactly. For instance, we don't do brain surgery here."

        "His joke feels so out of place that I'm left thinking why he even said it."

        hi "Yeah… just that it's really weird to have so many medical people at a school."

        nk "You'll get used to it."

        "I'm not so sure of that myself but I don't let the nurse know it."

        nk "Now, let me just find your file again…"

        "While he searches for something from his computer and shuffles stacks of papers around, I let my gaze wander around the room."

        "It's the epitome of generic, I'd like to say."

        "Beige walls and ceiling, dark gray laminate flooring, and all the equipment you'd expect from a school nurse's office."

        "Even the ridiculous educational posters are hanging on all four walls, reminding me to eat properly - three times a day and from all the food groups."

        show nurse grin
        with charachange

        "Smiling, the nurse draws a thick file from a stack of similarly thick files and opens it."

        nk "So, you already have medication for the arrhythmia, just remember to take your pills every morning and evening or it won't be much help."

        show nurse fabulous
        with charachange

        nk "Apart from that… do you do any sports? Rash stuff like… I don't know, boxing?"

        "He grins to his own joke but I don't."

        hi "Eh, well. I played soccer occasionally with some classmates."

        nk "All right, I'm afraid I'm going to have to recommend you refrain from doing that. At least, for the time being."

        hi "Oh."

        "My lack of reaction makes him raise an eyebrow, but really, I'm not too bothered by him forbidding me to kick a ball around."

        "I guess I never did it out of burning passion for the sport. Just to have something to do."

        nk "Any kind of concussion might be very dangerous to your heart, and risking another attack is not a good idea."

        nk "Was the previous one caused by a sudden concussion to the chest area? There is no mention of the cause in your papers."

        hi "Err… not exactly."

        show nurse concern
        with charachange

        "I sidestep the question acceptably, and he glances at me over his papers, with a more serious expression on his face."

        nk "Still, you need to keep your body healthy so some exercise would do you good."

        nk "We have physical therapy and such available as I said, but I don't think you really need such heavy measures."

        nk "Just get some light exercise regularly."

        nk "Brisk walks or even light jogging, jumping rope, that sort of thing. Swimming, maybe? There's a pool here."

        hi "So I was told."

        show nurse neutral
        with charachange

        nk "You were? Very good."

        nk "At any rate, and I'm sure you've been told this before, you just need to take care not to overexert yourself."

        "He wags his finger to emphasize the point. No need really, I've heard this a thousand times already."

        show nurse concern
        with charachange

        nk "Absolutely no unnecessary risks. Take care of yourself."

        hi "Okay."

        "He goes over my papers one more time and sets them on the desk, obviously content."

        show nurse neutral
        with charachange

        nk "Good. That's it, then. Come meet me if you ever need something."

        scene bg school_nursehall
        with locationchange

        stop music fadeout 2.0

        "I'm ushered out before I even realize it. A quick visit, indeed."

        if _in_replay:
            return

    label .nobodys_room:
        scene bg school_courtyard
        with locationchange

        play music music_pearly fadein 4.0

        "I end up standing in front of the main building and the auxiliary building, although to my eyes, they still look one and the same."

        "It's the first real look I get at the other students, so I watch people coming out of the school, going towards the gate or the dorms."

        "Everyone seems to know where they are going."

        "And I still keep thinking that most of them don't look too special for being students at a special school. Then again, neither do I."

        "Does that make me one of them?{w} One of us?"

        "…"

        "I should go somewhere too, to prevent me from getting lost."

        "It's around dinnertime, but I feel tired instead of hungry."

        "The weariness in me only grows as I trudge towards the dorms, set a little way apart from the main building complex."

        scene bg school_gardens
        with locationchange

        "There is a garden of sorts between the school and the dorms; shrubbery, flowers and that overbearing smell of fresh cut grass that fills the atmosphere."

        "It dawns on my tired mind that the smell feels novel because I haven't been outside at all for so long."

        scene bg school_dormext_start at bgleft
        with locationchange

        "The dorm building is big and made of red brick. Like the others, it feels way too pompous for what it is, so I push forward, going inside."

        scene bg school_dormhallground
        with locationchange

        "It takes more time than necessary to fish out the key I was given from my pocket."

        hi "Room one-one-nine…"

        "Despite the ornate exterior, the inside of the dorm is fairly new, functional, and boring."

        "Just like in the main building, the halls and doors are wide to accommodate wheelchairs. The same goes for the elevators at the ends of the hallways."

        "I poke my head around the corner of the common room door."

        "Inside a few students are watching the television."

        "One nods and gives a quick 'hello' before turning back to the TV."

        "Seems that only the girls around here are sociable. I suppose that's perfectly fine with me."

        "I climb the stairs to the upper floor."

        scene bg school_dormhallway
        with locationchange

        "Here, small corridors branch off from the main hallway."

        "Each of these minor halls seems to have a toilet and shower, as well as four rooms."

        "About halfway down the hall, I spy room 119."

        "The name plates on the rooms adjacent to mine are blank. I guess there are just two of us here."

        play sound sfx_doorknock2
        stop music fadeout 3.0

        "Light shines from below the door of room 117, so I knock lightly."

        hi "Hello, is anyone home?"

        "From inside, I hear a few movements, then the clicking of way more locks than I thought these doors had. After a moment the door squeaks open."

        show kenji tsun:
            xpos 0.4 xanchor 0.5
            easein 0.5 center
        with charaenter

        show kenji at center

        play music music_kenji fadein 0.5

        "A bespectacled boy is standing in the doorway. He is looking at me very intently through his extremely thick eyeglasses."

        ke_ "Who is it?"

        "Blind? No, at least not completely, why would he have eyeglasses if he was?"

        show kenji tsun_close
        with characlose

        "He leans closer to me until our noses are almost touching. His breath stinks of garlic."

        hi "Hisao Nakai… I'm moving into the next room. I thought I should introduce my…"

        show kenji happy
        with charadistant

        "His face suddenly brightens in realization, and he stands back upright, thrusting his hand out in a smiling greeting, almost straight to my diaphragm."

        ke_ "Oh, 'sup dude? The name's Kenji."

        hi "Ah, hi."

        "I take Kenji's sweaty hand and shake it, still a little rattled by the sudden change of attitude and vehement welcome."

        ke "There were some suspicious-looking people going in and out of your room earlier."

        hi "It was probably my parents."

        show kenji tsun
        with charachange

        ke "Your parents? You sure? 'Cause they could've been some other people, too. You can't judge a book by its cover."

        "His out-of-place proverb is left hanging between us awkwardly as I try to think of some way to respond."

        hi "I'd say the chances are high enough."

        "He shudders and makes some exaggerated hand gestures."

        show kenji neutral
        with charachange

        ke "You're a brave man, Hisao."

        show kenji tsun
        with charachange

        ke "Me, I don't think I could trust the chances."

        ke "The only one I trust is myself."

        hi "Does that mean I shouldn't get to know you, either?"

        "He thinks about this for a while."

        show kenji neutral
        with charachange

        ke "A wise decision."

        show kenji happy
        with charachange

        ke "Damn, you are smarter than you look."

        ke "Probably."

        ke "What do you look like? I hope not smart."

        show kenji neutral_close
        with characlose

        "He squints his eyes and leans closer again, but I lean backwards to dodge it."

        show kenji tsun
        with charadistant

        ke "Never mind, it doesn't matter."

        hide kenji
        with charaexit

        stop music fadeout 3.0

        "With that, he turns, fumbles around for a moment in search of the door handle,{w=0.3}{nw}"

        play sound sfx_doorslam

        extend " and shuts the door behind him."

        "I slide the key into the lock of the door marked 119."

        scene bg school_dormhisao_ss
        with locationchange

        play music music_night fadein 1.0

        "Bleak beige walls, white linen, a desk made of some type of light wood. Ugly curtains."

        "It's no one's room; impersonal, like my hospital room was."

        "My bags are sitting at the foot of my bed, looking a lot emptier than they did this morning."

        "The closet is sitting open, stocked with my clothes."

        "Also, it seems that there are a number of school uniforms hanging there as well."

        "A note is pinned to the sleeve of one of the shirts."

        call screen written_note(_("Hi Hicchan. We've unpacked your things and made your bed.\nThey said that if these don't fit then you should go to the office tomorrow.\nIf you have any problems, you can always call us.\n\nLove, Mom and Dad"))

        "Well, at least I don't have to worry about unpacking."

        "I kind of hoped I would have, then there would be something to do."

        "It's still too early."

        "I put the note down on the desktop and lie down on the bed, feeling drained."

        "Lying there makes me want to read something, but I have nothing with me."

        "I wonder if the hospital conditioned me for wanting to read whenever I have nothing to do."

        "The restless urge just keeps growing until I have to stand up."

        "Maybe it's stress or something."

        "I was pretty nervous about it before coming and for the entire day today too. I still am, I think."

        "Damn, I have to distract myself somehow, so I won't be this unnatural all the time."

        "Tomorrow, I'll go borrow some books from the library."

        "Yeah, I'll do that."

        "But for now…"

        show pills:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0

        pause 1.0

        show pills:
            truecenter alpha 1.0

        "The bottles of medications neatly arranged on my night table catch my eye."

        "I pick up one and shake it just to hear the contents rattle inside, and then read the glued-on pharmacy label."

        show pills:
            easeout 1.0 ypos 0.7 alpha 0.0

        pause 1.0

        hide pills

        call screen written_note(_("Hisao Nakai\n\nTwo tablets daily to stay alive"), quiet=True)

        "It doesn't really say that, but it could just as well."

        "It's kinda twisted, having your life depend on chemicals like this. I resent it a little, but what choice do I have?"

        "With a sigh, I begin my new daily ritual of taking the right number of pills from each bottle, being careful to check the correct dosages."

        "…"

        "I lie down again, feeling hollow and uncertain, and after that I keep staring at the blank, unfamiliar ceiling for a long time."

        stop music fadeout 8.0

        scene bg school_dormhisao_ni
        with Dissolve(3.0)

        "It doesn't start looking any more familiar, not even after darkness falls and long shadows draw across my room like fingers."

        "The sheets feel slightly more comfortable, warm and nest-like against the chill that passes for room temperature here."

        "Soon the lighter shade of darkness that is the ceiling looks like every ceiling does at night, and it becomes the only thing I recognize any more."

        "The night beckons me to sleep, and I feel the coldness of unfamiliarity and fear creeping up my spine once again."

        "I keep drifting further away from the world I knew."

        scene black
        with shuteye

        if _in_replay:
            return

    return

label a1c1o1:
    hi "Why? Do I have to?"

    mu "Of course not. That's why I asked."

    hi "Right."

    mu "Let's go then."

    return

label a1c1o2:
    hi "Yeah, sure. I mean, isn't that normal?"

    mu "Of course. But not everyone likes to be at the center of attention."

    "I'm probably one of those people, but I guess I should be the one to give the first impression of myself."

    hi "Right, but it's no problem."

    mu "Let's go then."

    return

label a1c2o1:
    hi "Oh, yeah. Is there a library in the school? Lately I've gotten into reading a lot so I'd like to check it out."

    "Misha gives the kind of frown that makes it clear she doesn't consider reading a healthy hobby, but then picks up her smile again."

    mi "There is~! It's in the second floor, we can show it to you sometime!"

    hi "Thanks."

    "I return to my food while the girls talk between themselves."

    return

label a1c2o2:
    "Shizune intrigues me, and I kind of want to ask something about her."

    "But I can't really ask about something that personal, can I?"

    "Hmm…"

    "I can't come up with anything else to ask so I just focus on my food while the girls talk between themselves."

    return

label a1c2o3:
    hi "I can't think of anything, really."

    show misha sign_smile
    with charachange

    mi "Ooh! That means we've been good guides, doesn't it, doesn't it~?"

    "…"

    hi "Eeh… if you say so."

    show misha hips_grin
    with charachange

    show shizu behind_smile
    with charachange

    "Misha positively beams, and so does Shizune after a quick translation."

    "I shake my head at their somewhat exaggerated enthusiasm, and shift my focus on the food."

    return
