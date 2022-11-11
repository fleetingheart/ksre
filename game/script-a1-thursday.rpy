# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a1_thursday:
    call timeskip

    label .the_running_girl:
        scene black

        play sound sfx_alarmclock
        stop ambient

        scene bg school_dormhisao
        with openeye

        play music music_dreamy fadein 2.0

        "The sound of an alarm pulls me out of a fitful slumber and into the unpleasant state of wakefulness."

        "I linger under the blanket for a few minutes, gathering energy to rise up while making excuses as for why I already haven't."

        "Honestly, I wouldn't mind staying here for all day. School is surprisingly exhausting after a long pause, and the culture shock still has not faded, I think."

        "Still, despite getting an impression that skipping class is easy here, I don't think they are going to let me get away that easily."

        "And the nurse is bound to keep breathing down my neck with the talk of exercising as well."

        "So eventually I do rise up, swallow the morning medications and put on my old soccer clothing."

        "Thanks to my condition, I was exempted from taking part in gym classes at Yamaku, so I didn't get issued with a gym outfit."

        "I'd order some to cover such a contingency, but wearing my old soccer clothes is kind of nostalgic."

        "I can't use them for that any more, so maybe they can get a new life this way. A bit like me."

        if promised or _in_replay:
            "After all, if I'm going to start taking care of myself, I can't afford to slack around. I'll start from the basics."

            "Basics which include keeping the rest of my body in shape along with what little I can do to strengthen my heart."

            "Maybe then I can go back to something approaching a normal life; or at least something where I'm less likely to fall over dead at any minute."
        else:
            "Seems a bit stupid to me, really."

            "But I suppose this way at least I can tell the nurse honestly that I'm doing something about my health."

            "Not that I was ever much of a runner to begin with."

            "Can't hurt to try, I guess."

        stop music fadeout 2.0

        scene bg school_track
        with locationskip

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        play ambient sfx_emijogging fadein 0.1

        "I'm surprised to discover that I'm not the only one present at the track."

        "Not just that, but it's a face I've seen before."

        "The prosthetic-legged girl who bowled me over in the hallway yesterday is running on the track lithely, like a half-mechanical gazelle."

        "What was her name again? It was a short one, but I can't remember."

        "She seems to be running laps at a somewhat easy lope, her prosthetic legs clacking rhythmically on the hard track surface."

        "I wonder what reason she has for running this early in the morning. Maybe it's something akin to mine, and the nurse is oppressing the poor girl to jog just like he is oppressing me."

        "I certainly wouldn't be here if it weren't for my health, and his prompting me to do so."

        "And even with things being like they are, it's only because I wanted to get it out of the way early."

        "The fact that I would be less likely to encounter someone who would witness my pitiful attempts to get in shape was merely a happy accident."

        "I'd leave, but it seems that my former assailant noticed me on her last lap."

        "She waves at me cheerfully and jogs over."

        show emi basic_grin_gym:
            xpos 0.7 xanchor 0.5
            easein 1.0 center
        with charaenter

        stop ambient

        emi_ "Good morning! Your name is Hisao, right?"

        play music music_emi fadein 2.0

        "She grins, seemingly pleased that she'd remembered my name."

        show emi basic_closedgrin_gym at center
        with charachange

        emi_ "You may not remember me."

        show emi basic_grin_gym
        with charachange

        emi_ "Emi? I knocked you over in the hall yesterday."

        if not talk_with_hanako and not _in_replay:
            show emi excited_circle_gym
            with charachange

            emi "'Miss Ibarazaki?'"

            "She imitates Misha 'imitating' Shizune, failing to get the same kind of subdued lilt into her high-pitched voice."

        hi "How could I forget such a er, blunt introduction?"

        show emi sad_shy_gym
        with charachange

        "Emi has the decency to look vaguely apologetic for a moment before giggling."

        show emi sad_grin_gym
        with charachange

        emi "Yeah, sorry about that. Again."

        hi "Hmm, well, so long as you don't make a habit of it, I suppose I'll be fine."

        show emi basic_happy_gym
        with charachange

        emi "Great!"

        "I'm not sure she realized I was joking."

        hi "So the 'spy-consultant' the nurse was talking about… is that actually you?"

        show emi basic_closedgrin_gym
        with charachange

        emi "That's right!"

        hi "Oh."

        hi "I was expecting someone from the nursing staff, to be honest."

        show emi basic_confused_gym
        with charachange

        emi "What, are you saying I don't look like I could be a spy?"

        hi "No, this is more like a relief. I was afraid he would have someone to watch my every move."

        hi "Unless you are here to do exactly that."

        show emi excited_laugh_gym
        with charachange

        emi "No, I'm here for my own reasons, the nurse just asked me if I had seen 'a messy-haired transfer student who looks like he's kinda lost' around the track."

        hi "So why are you down here?"

        "Emi strikes a dramatic pose."

        show emi basic_happy_gym
        with charachange

        emi "Training!"

        hi "For what?"

        show emi basic_closedhappy_gym
        with charachange

        emi "Track!"

        hi "Ah, I see. You're on the track team, then?"

        "Emi nods enthusiastically."

        show emi excited_proud_gym
        with charachange

        emi "Yep! I'm one of the better runners, too!"

        "And modest about it, too."

        show emi basic_grin_gym
        with charachange

        emi "Hey, you should join up!"

        emi "It's good exercise, you know."

        "I think that much activity is probably out of the question for me."

        hi "Nah, I'm not even sure that I really like running all that much."

        hi "Plus I'm just not into organized sports, you know?"

        "It's true. I never even really got that much into soccer."

        "I mean I'd run around with my friends and all, but that was really the only reason I ever played."

        "It wasn't for the glory to be found on the field, that's for sure."

        "Emi seems to understand my meaning."

        show emi basic_confused_gym
        with charachange

        emi "I see, I see. Not that into the whole organization thing."

        show emi excited_proud_gym
        with charachange

        emi "But now that you're here, I guess we're going to run together, huh?"

        hi "What? Er, sure, I guess."

        "Emi seems pleased."

        show emi excited_joy_gym
        with charachange

        emi "Are you going to warm up?"

        hi "Real men don't warm up."

        show emi basic_annoyed_gym
        with charachange

        emi "Oh no, you always should warm up! Bad Hisao!"

        show emi excited_proud_gym_close
        with characlose

        "She scolds me enthusiastically, but then smiles and leans closer."

        emi "I hate warming up too."

        show emi excited_laugh_gym_close
        with charachange

        "She laughs suddenly."

        emi "Heck, and I don't even have to stretch my legs!"

        play sound sfx_gymbounce

        show emi gymbounce
        with charadistant

        "As if to confirm her statement she bounces up and down a couple of times, giving a passing impression of standing on a pair of springs. Her legblades seem to be quite elastic."

        emi "Let's go!"

        stop music fadeout 1.0

        play ambient sfx_emijogging fadein 0.3

        scene bg school_track_running
        with locationchange

        "So we both take off around the track, and I can immediately see that she wasn't lying about being good at running."

        "Emi moves fluidly, throwing herself into the run with a sort of wild abandon."

        "I find myself concentrating more on running properly."

        if promised or _in_replay:
            "Hands spread, right?"

            "And something about hitting on the balls of your feet, rather than the heels…"

            "I try to match my stride to Emi's, but it's pretty difficult."

            "Apparently I'm not very good at it."

            "Maybe Emi could help me with that sometime."
        else:
            "Frankly, I don't remember if there's any particular form for running, but I can't help but feel like I'm doing it wrong, somehow."

            "I feel awkward in comparison to Emi, who never seems to break stride."

            "…"

            "I don't think I want to do this any more."

        "I'm really not feeling up to more than a couple of laps today, and slow to a walk pretty quickly."

        scene bg school_track_on
        with Dissolve(4.0)

        "Emi keeps running, and doesn't seem to notice I've stopped until she passes me a second time."

        stop ambient

        "She quickly skids to a halt, breathing steadily in contrast to my own somewhat gasping demeanor."

        play music music_emi fadein 2.0

        show emi basic_confused_gym at offscreenleft
        with None

        show emi at center
        with charamovefaster

        emi "Finished already?"

        "I hang my head ruefully."

        hi "Heh, yeah."

        hi "I'm not in very good shape right now."

        show emi basic_grin_gym
        with charachange

        "Emi nods, and then grins at me again."

        "She seems to do a lot of smiling."

        emi "Well, the important thing is you started, right?"

        show emi excited_amused_gym
        with charachange

        emi "Next time, you just have to try to hold out longer, and then longer, and longer, and eventually you'll be great!"

        hi "I'll keep that in mind."

        hi "But I think right now I'm going to go get ready for class."

        hi "Shouldn't you?"

        "Emi shrugs unconcernedly."

        show emi basic_grin_gym
        with charachange

        emi "Nah, I've got plenty of time."

        "I notice that she's not wearing a watch."

        hi "Are you sure?"

        "Another careless shrug."

        emi "Not really… but I've got to finish my routine!"

        show emi basic_closedgrin_gym
        with charachange

        emi "See you later, Hisao!"

        hi "Er, yeah. See ya."

        stop music fadeout 5.0
        play ambient sfx_emisprinting

        show emi at offscreenleft
        with charamovefaster

        hide emi

        stop ambient fadeout 2.0

        if promised or _in_replay:
            "I'm not sure whether this morning's experiment was a success or a failure, but I'll admit that I do feel slightly good about getting out there this morning."

            "And like Emi said, I just need to keep at it in order to get better, right?"

            "Practice makes perfect, or something like that."

            "It's nice at least to feel like I've taken some semblance of control over my own health."

            "I'll have to try to keep this up."
        else:
            "Apart from feeling more tired than before, I don't think I accomplished anything today."

            "I'm so out of shape it's embarrassing."

            "The whole thing might have been a waste of time. I'll find some other way."

        scene black
        with Dissolve(0.5)

        if _in_replay:
            return

    label .soap:
        scene bg school_dormext_half
        with Dissolve(0.5)

        "I head back to the dorms to wash and change into my uniform, trying to resist the urge to take a really long and hot shower."

        "I'm tired from all the running, so I just want to unwind, but I don't want to break my slowly building routine of getting to school before the morning rush."

        scene bg school_dormbathroom
        show steam
        show steam2
        with shorttimeskip

        "After taking a long shower anyway, I dry myself off and get out of the stall to put on my clothes."

        show kenji silhouette_naked behind steam at center
        with charaenter

        "Out of nowhere, a shadow appears within the mist, looming and radiating malicious intent. It bursts through the fog."

        play music music_kenji fadein 0.3

        show steam behind kenji
        show steam2 behind kenji
        show kenji neutral_naked
        with charachange

        ke "Sup?"

        hi "What are you doing here? What the hell, you scared me! What's your problem?!"

        show kenji tsun_naked
        with charachange

        ke "I should be asking you that. I've been looking for you all over the place, man."

        hi "What do you mean 'all over the place'?"

        "I want to ask if he's been looking for me like that, stark naked, but hold my tongue back."

        "I finally realize I'm still naked too and quickly hold up my shirt in front of me, but Kenji doesn't seem to notice a thing."

        "His glasses are fogged up. But then, why doesn't he wipe them off? Is his vision so bad it's like he's perpetually seeing through fog?"

        ke "You know, your room, and… Yeah, that's it. Hey, I mean, I still had to get up, though. Whatever. It's not important. Can I borrow some money?"

        show kenji neutral_naked
        with charachange

        "He puts on an innocent face and looks away, trying very hard to look very casual. It doesn't work; he's as transparent as his windowpane-sized glasses."

        "Talking neutrally like this, wearing nothing, feels awkward."

        "Actually, somehow it's even more awkward to be naked in front of someone when they can't see me being naked. To say nothing of the fact that he's naked as well."

        "I try to brush the feeling off, with little success."

        hi "Money? Sure."

        show kenji happy_naked
        hide steam
        with charachange

        ke "Awesome."

        hi "Wait, why do you need it?"

        show kenji tsun_naked
        with charachange

        ke "Ehhhh…"

        show kenji neutral_naked
        with charachange

        ke "Can't you just give it to me because I had the good will not to run through your pockets while you were in the shower? I could have, but I exercised restraint. And in the end, isn't it the thought that counts? Come on, be a pal."

        "This makes no sense. If it's the thought that counts, I should withhold payment, since his thoughts were so clearly impure and his intentions are probably even more sinister since he can't tell me what they are. I say as much to him."

        show kenji tsun_naked
        with charachange

        ke "I'm offended man, but if that is your game, then fine, I guess I have no choice. I want to order a pizza, and I already have most of the cost of the pizza. I need your help for the rest."

        hi "I get some of that pizza too, right?"

        ke "No."

        hi "Are you serious?"

        show kenji neutral_naked
        with charachange

        ke "Yeah. I would give you some, but you have class, you don't have time to eat a pizza."

        hi "What about you?!"

        ke "I'm not going to class, I have to wait for the pizza and pay the guy. And then eat it. It's not easy. You have to obtain the pizza stealthily. If you don't, everyone will see you. And the pizza. And they will ask for a slice."

        show kenji tsun_naked
        with charachange

        ke "It's a hard world out there. Everyone wants a piece. Then you're left pizzaless in an unforgiving world. It's happened before, that's how I know."

        ke "Every day, I plan my vengeance, so that when the people who wronged me order a pizza, I will be there. Ever vigilant!"

        "Kenji strikes a dramatic pose, completely without irony."

        show kenji neutral_naked
        with charachange

        ke "But yeah, I only need like 400 yen. Please! You're my only hope! I can't go outside and buy my own pizza, it's too far!"

        ke "I try not to go out unless it's absolutely necessary. Let me tell you what happened the last time I went out without carefully planning it out in advance."

        ke "I was outside. I can't remember what I was doing. Something. Standing? Maybe wondering how I got there."

        show kenji tsun_naked
        with charachange

        ke "And then, out of nowhere, it happened."

        ke "Like a flash of lightning, splitting the sky, like how you split a sandwich into two equal pieces to make it more manageable to hold and eat, a bird crapped on my head."

        ke "It was the second most shocking moment of my life."

        hi "What was the first?"

        "He ignores me and keeps going. I want to grab him and shake him. Is he just trying to keep momentum? I'll go with that, even if it's more likely he just didn't hear me."

        ke "It was like in the openings to some kind of anime show, you know how there is always a part where the main dude is fighting his rival, and they fly at each other and clash swords and there's like, big dramatic colored auras and zoom?"

        show kenji neutral_naked
        with charachange

        ke "It was like that, but with poo."

        hi "Okay."

        show kenji happy_naked
        with charachange

        ke "So yeah, I need some money. Please? Don't leave me hanging, man. I only need like 1000 yen."

        hi "I thought it was 400."

        ke "Okay."

        hi "What?"

        ke "I'll pay you back, I swear."

        hi "You better, that's what it means to borrow stuff."

        show kenji neutral_naked
        with charachange

        ke "I don't know when I'll be able to pay you back."

        hi "You have one week."

        show kenji tsun_naked
        with charachange

        ke "Aaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhggggggggggghhhhhhhh……"

        "Kenji winces and makes a noise like a dying cow, a particularly disturbing fact given that his baton is conducting freely."

        ke "You're not supposed to be so tight assed about money between brothers in arms, man. Men have it bad enough as it is. Did you know that male porn stars only make about half of what female porn stars make?"

        hi "That doesn't mean anything unless you're a porn star."

        ke "So maybe I am a porn star, on the side, struggling to make ends meet as I fight the feminist agenda, and you can't even spot me your crumbs, you bastard. Nobody understands. Nobody."

        "Wouldn't feminists be against pornography in the first place?"

        hi "This feminist agenda stuff again?"

        ke "This stuff is important. I can see that you don't give a shit, but this is serious, here. Feminists… are a dangerous enemy, make no mistake. You take them lightly, and you'll wake up in the morning with a knife in your back, bam! Out of nowhere!"

        hi "How do you wake up in the morning if someone stabbed you in your sleep?"

        show kenji happy_naked
        with charachange

        ke "Women are terrible at stabbing things."

        hi "I thought you just said don't take them lightly."

        show kenji neutral_naked
        with charachange

        ke "Well, I mean don't take them lightly for the big things. Individually they're not a threat, but if there was some kind of war, like a big war, with men on one side, and the feminist forces on the other side, it would be pretty ugly."

        show kenji tsun_naked
        with charachange

        ke "And that day will come, when the feminists come out of their central top secret worldwide feminist headquarters, and say 'It's on now, motherfuckers!'"

        hi "You're being ridiculous, there's no big worldwide feminist headquarters building, where would they even hide that? I mean, it'd have to be massive, you couldn't hide that on Earth, someone would notice a big fortress with women only in it."

        show kenji happy_naked
        with charachange

        ke "Who said it was on Earth?"

        "I turn away from Kenji and start practicing frowning faces in a mirror so that I can figure out what kind of frown will best express my emotions. He can't see me from this distance anyway."

        "Which, unfortunately, means that he just keeps on ranting without any regard to sense or sensibility."

        show kenji tsun_naked
        with charachange

        ke "Yeah, there is a war going on. A war not many know about, but it's a great one that will one day boil over, and encompass all of the known world. Then, we will have to pick sides. We will have to make a stand. In fact, it's happening right now."

        ke "Imagine it, the bloody battlefield. A vicious conflict without end."

        ke "I almost gave up, when I thought this cause was silly… When I grew tired of the bleakness of our fight… When I mistook the time the power went out for a feminist raid and thought the end was near…"

        ke "But then I realized that if I gave up, it would all be over, and I was like, 'whoa' and knew I had to get serious. Because I am the last sane man in an insane world. It's about duty."

        hi "Must be a pretty crappy movement if it all hinges on one naked guy, ranting in a bathroom at another naked guy."

        show kenji neutral_naked
        with charachange

        ke "So can I have the money?"

        "He's blocking the way out, it's getting cold because I'm still naked, and I want to go to class, so I agree to spot him the money."

        show kenji happy_naked
        with charachange

        ke "Awesome. Thanks, dude. We should go bowling later on."

        hi "Bowling?"

        ke "Yeah, it's the ultimate sport. There are almost no women bowlers either, making it also the manliest sport."

        ke "Should I wear my pink bowling shirt with matching shoes or the pastel green with flower accents?"

        hi "There are bowling clothes?"

        show kenji neutral_naked
        with charachange

        ke "Maybe."

        hi "Anyway, you had better pay me back."

        ke "I can pay you back in stuff, right?"

        "I don't have the time to ask him to elaborate on what that means."

        hi "I don't know. I have to get to class, you're kind of in the way."

        show kenji tsun_naked
        with charachange

        ke "Oh. Sorry. Yeah, I don't want to hold you up, and I have some stuff to do myself. The time has come."

        hi "The time for what?"

        show kenji happy_naked
        with charachange

        ke "I just like saying that."

        ke "Okay, now the time has really come."

        hi "For what?"

        show kenji tsun_naked
        with charachange

        ke "I have to use the bathroom. Get out of it."

        hi "I was just going to! And what does that mean? It's a big bathroom."

        ke "So? I have to be alone or I can't go. The pressure…"

        hi "Okay. What if someone else comes in?"

        ke "…"

        ke "I'll think of something."

        "I give him my practiced frown and it looks kind of silly reflected in his glasses. He either doesn't notice or doesn't see, anyway, so I get dressed and run back to my room, feeling as though an eternity has passed since I woke up."

        stop music fadeout 2.0

        scene bg school_dormhisao
        with locationskip

        "That is time I will never get back. I'll get him for this somehow."

        "But right now, I have to get to class."

        if _in_replay:
            return

    label .cold_war:
        scene bg school_scienceroom
        with locationskip

        play music music_normal fadein 2.0

        "I'm the first person in class today, although I think I'm a little too early. Then again, sitting alone here for twenty minutes sure beats having to suffer that time with Kenji."

        "The combination of fatigue, frustration and boredom starts making me feel very tired."

        "I black out for a second, waking up when my head hits the surface of my desk. Rubbing my forehead, I realize this is as good a reason as any to stay up for now and stop coming to class so early later."

        "Eventually, I hear a tapping noise outside in the hallway, and Lilly's tall figure appears in the doorway. She's not in this class, so she must have some other business. Maybe she's looking for Hanako."

        "Lilly stops at the door, looking hesitant as if she was a vampire who can't come in unless invited. I consider doing so because she looks rather lonesome standing there."

        "She steps in on her own accord though, after straightening her skirt and shirt collar as if it was of importance to look prim when entering our classroom."

        show lilly cane_concerned at offscreenleft
        with None

        show lilly at left
        with charamove

        li "Excuse me."

        "She calls into the quiet classroom with a probing, delicate voice. I realize the silence might unnerve her because of her blindness so I break it."

        hi "Good morning, Lilly."

        show lilly cane_surprised
        with charachange

        show lilly at center
        show bg at bgright
        with charamove

        li "Hisao? Good morning. I didn't hear you come in."

        "I wonder if she thinks it's suspicious I didn't say anything to her before. It's likely. If I were to tell too big a lie now, it would sink me."

        hi "Well, I was already here, just asleep until now."

        show lilly cane_listen
        with charachange

        li "Oh. Have you seen Hanako today, by any chance?"

        hi "No, she seems to come in only just before the bells ring… or after that. Do you want me to tell her something for you?"

        show lilly cane_weaksmile
        with charachange

        li "No, it's fine. It's strange, but I think we're the only two people in the school right now. I didn't hear anyone else on my way here."

        hi "I shouldn't have gotten up so early today, I guess."

        show lilly cane_smile
        with charachange

        li "You're chastising yourself for doing something that other people should? Punctuality is a good thing. I think so, anyway."

        show lilly cane_concerned
        with charachange

        li "It's a very busy morning today. The festival is coming up soon, and today is the deadline for event registration, budget reports, and any other official paperwork."

        show lilly cane_weaksmile
        with charachange

        li "It could be that everyone is trying to complete the necessary forms at the last minute. Maybe that is why it's so quiet today."

        play sound sfx_doorslam

        show lilly cane_surprised
        with vpunch

        mi "Hi~ hi~!"

        show misha hips_grin behind shizu at offscreenright
        show shizu behind_blank at offscreenright
        with None

        show lilly at left
        show misha at center
        show shizu at right
        show bg at bgleft
        with charamove

        "Misha pops into the room with Shizune as if on cue, shouting with a loudness that makes Lilly visibly flinch."

        show misha hips_smile
        with charachange

        mi "Hi, Hicchan~!"

        hi "Hi."

        show shizu behind_smile
        with charachange

        shi "…"

        show misha hips_grin
        with charachange

        mi "Look, it's the class representative~! Hello~!"

        show lilly cane_smile
        with charachange

        "Lilly smiles, probably amused by Misha's - or Shizune's - use of the word 'look.'"

        show lilly cane_smile
        with charachange

        li "Good morning."

        show shizu adjust_smug
        with charachange

        shi "…"

        show misha cross_smile
        with charachange

        mi "Of course, you're not the representative of this class, right, right~?"

        show lilly cane_weaksmile
        with charachange

        li "I'm not."

        "Lilly seems a little more guarded in her answers to Shizune than she was with me the other day. I guess they really don't get along at all."

        "Then I realize that Lilly might actually not know Shizune is present and she's trying to detect whether or not she is, to know who she is talking to."

        "For all she knows, she's talking to Misha, but knowing that she and Shizune are practically inseparable, she might expect Shizune being the one that actually 'talks.'"

        "Damn, how complicated. I decide to help Lilly out, for my own peace of mind more than anything else."

        hi "You're here early, Shizune."

        show shizu basic_angry
        with charachange

        shi "…"

        show misha hips_frown
        with charachange

        mi "You were here even earlier than us!"

        "Misha puffs out her cheeks angrily. Why is she getting angry? Does she feel emotions on Shizune's behalf, too?"

        "It's not that weird, though, that Shizune didn't like my little comment. It's true, I was here earlier than them, so me saying something like that could definitely be misinterpreted as anything."

        "Especially to Shizune, who doesn't have the benefit of hearing tone to gauge intent."

        "Before I can start weighing whether or not I should apologize, Shizune has already moved on."

        show shizu adjust_smug
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "Class rep~! It's a good thing you're here~! We have to talk."

        show shizu behind_frown
        with charachange

        shi "…"

        show misha hips_grin
        with charachange

        mi "The festival is coming up in three days, right? Every other class has already handed in their projected budget reports for their events! Even the first-years! Except you~!"

        show misha cross_laugh
        with charachange

        mi "Wahaha~!"

        show lilly cane_surprised
        with charachange

        li "There is still time to hand it in, isn't there?"

        stop music fadeout 2.0

        show shizu cross_angry
        with charachange

        shi "…"

        show misha cross_frown
        with charachange

        mi "Today! The deadline is today! You're certainly taking your time, aren't you? If I had it my way, I'd have had all of the necessary paperwork days ago, but someone~! had to say 'the deadline, please extend it~!'"

        show lilly cane_displeased
        with charachange

        li "Yes, that was me. Planning something on this scale is not a small task, and a week is too small a time frame to expect a whole class to work out such a complex issue completely."

        show shizu adjust_angry
        with charachange

        shi "…"

        show misha hips_frown
        with charachange

        mi "Do you want to know what's harder than distributing the funds for one class' event? Handling the same matter for every class in the school and then some~! The one who does that is me!"

        "Misha puts her hands on her hips and stands up straight. Wow, she is really getting into the role. Lilly doesn't look like she's very amused, though."

        hi "Hey, Shizune, aren't you being a little too hard on her? There's still a whole day left."

        show lilly cane_weaksmile
        with charachange

        li "Please, Hisao. It's all right."

        "Lilly seems happy I'm taking her side, but a bit conflicted that I might not think she can take care of herself."

        show lilly cane_listen
        with charachange

        li "If this is about the budget, then I'm disappointed you think I have forgotten about it. I understand how important it is."

        show shizu behind_frustrated
        with charachange

        shi "…"

        show misha hips_grin
        with charachange

        mi "Then~! Can I have it, please?"

        hi "Shizune, she might not have it on her at this exact second."

        show lilly cane_displeased
        with charachange

        li "It's not here right now. I asked two students to take care of it for me. Students from my class."

        "She emphasizes the last sentence much to my surprise. She knows about Shizune and Misha's efforts to rope me into the Student Council?"

        "I guess word must've gotten around, so now she's using me as ammo against Shizune. This just gets better and better…"

        show shizu cross_angry
        with charachange

        shi "…"

        show misha hips_frown
        with charachange

        mi "It was your responsibility~! A budget report isn't something you should just be delegating away; as class rep, it's your job to be on top of things! This kind of disregard for proper procedure is really just terrible~!"

        show lilly cane_listen
        with charachange

        li "They completed it, being capable of doing so, but the students have been sick recently, so they could not come to school and give it back to me. If you want, I will apologize on their behalf for getting sick."

        show misha hips_grin
        with charachange

        mi "Okay~!"

        "Although Misha misses Lilly's little jab entirely, Shizune doesn't, and she seems torn between being offended by Lilly's daring and jumping for joy at the prospect of a challenge."

        show shizu behind_frown
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "Lilly, don't they live here at the school? That's a five minute walk, you know~."

        mi "What could they possibly have that prevents them from taking five minutes out of their busy lives… to drop off something that will affect the enjoyment of their entire class?"

        show shizu adjust_angry
        with charachange

        "Lilly opens her mouth to say something, but Shizune closes the gap between them and starts signing furiously, waving her hands around like an orchestra conductor."

        "Misha tries her best to convey the same passion, but can't seem to lose her normal cheerful tone. The result is interesting and somewhat surreal."

        shi "…"

        show misha cross_frown
        with charachange

        mi "And what's with that attitude~? I said that it's not something you should be delegating away; are you the class representative or aren't you?"

        show misha hips_frown
        with charachange

        mi "Tell me the names of those two students, they should have your job if you can't even handle something this simple yourself."

        show lilly cane_displeased
        with charachange

        li "One form isn't the full extent of what I am supposed to take care of."

        "Lilly's tone is growing slightly impatient, but she is doing a good job of not letting Shizune see how unsettled she is becoming. She's playing her cards close to her chest."

        "Shizune, on the other hand, wraps her fingers cheerfully along the edge of her glasses, knowing Lilly can neither hear nor see how excited she is."

        show shizu adjust_smug
        with charachange

        shi "…"

        show misha hips_grin
        with charachange

        mi "Of course, you do so much, class rep~! It must be so difficult being you~!"

        show lilly cane_listen
        with charachange

        "Lilly tightens her lips at Misha's words, clearly understanding the intent behind them even though Misha delivers them without even a hint of the sarcasm which they were meant to have."

        "Shizune and Lilly don't like each other, that much is clear, but this seems a little much. It seems like Lilly has had enough and is ready to push back."

        play music music_tension

        scene black
        with Dissolve(0.2)

        show showdown_lilly_slice:
            xpos 1.0
        show showdown_shizu_slice:
            xanchor 1.0 yalign 1.0

        play sound sfx_draw
        show showdown_lilly_slice:
            easein 0.2 xalign 0.0 yalign 0.0

        pause 0.2

        play sound sfx_draw
        show showdown_shizu_slice:
            easein 0.2 xalign 1.0 yalign 1.0

        pause 0.2

        play sound sfx_thunder
        scene ev showdown
        with Fade(0.2, 0.0, 3.0, color="#FFF")

        play sound sfx_slide2
        show ev showdown_large:
            size (1920, 1080) crop (0, 0, 5760, 3240)
            easeout 0.2 crop (672, 240, 1920, 1080)

        li "I was actually just discussing the budget report before you came by. You must be very talented to have finished all your student council duties so quickly that you can track me down to make sure I don't forget my own."

        play sound sfx_slide
        show ev showdown_large:
            ease 0.2 crop (3360, 384, 1920, 1080)

        mi "Are you accusing me of slacking off? It seems like you're confusing me with yourself~!"

        play sound sfx_slide2
        show ev showdown_large:
            ease 0.2 crop (672, 240, 1920, 1080)

        li "I don't think so. That would be a very difficult thing for me to do; comparing myself to you."

        play sound sfx_slide2
        show ev showdown_large:
            ease 0.2 crop (3360, 384, 1920, 1080)

        mi "You're right, the difference between us is like heaven and hell."

        play sound sfx_slide
        show ev showdown_large:
            ease 0.2 crop (672, 240, 1920, 1080)

        li "And it's not hard to guess which one you might represent."

        play sound sfx_thunder
        scene ev showdown
        with Fade(0.2, 0.0, 1.5, color="#FFF")

        "The air between them ripples with the heat of their enmity. Well, not really. They can't disguise it any more, though. Even Misha looks like she's beginning to understand the real nature of this conversation."

        stop music fadeout 5.0

        scene bg school_scienceroom
        show lilly cane_listen at left
        show misha perky_confused at center
        show shizu basic_angry at right
        with flash

        shi "…"

        show misha sign_confused
        with charachange

        mi "Hicchan~! Don't you slack off either~!"

        hi "What are you talking about?"

        show shizu basic_frown
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "Aren't you taking part in the festival, Hicchan? You are, aren't you? Then~! I hope you're going to do a lot more to make sure it goes smoothly than this person~!"

        menu:
            set choices
            with menueffect

            "I don't understand why Shizune is suddenly getting mad at me."

            "Don't drag me into this! I've done my part!":
                $ side_lilly = False

                call a1c8o1

            "Hey, come on. Cut me and Lilly some slack…":
                $ side_lilly = True

                call a1c8o2

        if side_lilly or _in_replay:
            "I turn my back at them."

            if talk_with_hanako or _in_replay:
                hide shizu
                hide misha
                with charaexit

                show lilly at center
                show bg at bgright
                with charamove

                hi "Lilly, class is going to be starting soon, so we can talk more later. I'll tell Hanako you were looking for her."

                "I can feel Shizune freezing. Maybe this is the first time she has ever been ignored in such a blunt manner."

                show lilly cane_smile
                with charachange

                li "Thank you, Hisao. I'll leave now, then."

                "She gives me the sweetest smile I've seen all week, and turns on her heels to make her exit."

                hide lilly
                with charaexit

                "As soon as Lilly walks out the door, I suddenly start feeling reluctant about turning to face Shizune."

                "I can feel her eyes burning into my back, and can't bring myself to look at her. She must be furious. I keep expecting Misha to say something to alleviate the tension, but it really is wanting too much."

                "In the end, I go back to my seat and listen to the sound of Shizune's footsteps as she marches out of the room. She doesn't return until a few minutes before class."
            else:
                hide shizu
                hide misha
                hide lilly
                with charaexit

                "I get back to my seat and shut my ears from the finale of the argument between Lilly and Shizune."

                "Eventually, Lilly leaves our classroom and Shizune and Misha seat themselves, without talking to me."

                "I can feel Shizune's eyes burning into my back. She is probably angry at me, but I'm just as angry with her."

                "I don't get why she had to drag me into the argument."

        if _in_replay:
            return

    if not side_lilly:
        label .proof_of_competency:
            scene bg school_scienceroom at bgleft
            with shorttimeskip

            play music music_daily fadein 0.5

            "Hanako doesn't come to the morning class at all, leaving her seat looking empty and lonely in the back of the classroom."

            "I have to tell her that Lilly was looking for her if I see her later."

            "After the events of this morning, class is pretty boring in comparison. I turn the pages of my textbook lazily."

            "We've been covering the same amount of pages each day, so reading ahead is more or less giving myself a preview of what tomorrow's lesson will be about."

            "The clock at the front of the room sounds unbearably loud. The teacher hasn't said anything in over seven minutes, instead opting to cover the board in rows and rows of equations taken directly from the book."

            "The rhythmic clashing of chalk on blackboard seems to synchronize perfectly with the ticking of the clock."

            show misha cross_smile_close at offscreenleft
            with None

            show misha:
                xpos 0.1 xanchor 0.5
            show bg at center
            with charamove

            "I start to copy down the equations just to pass the time, not noticing Misha's head poking over my shoulder until she is almost on top of me."

            hi "What are you doing?"

            "I try to strike a balance between being quiet enough to not draw attention to myself but loud enough to draw hers."

            show misha cross_grin_close
            with charachange

            show misha at twoleft
            show bg at bgright
            with charamove

            mi "What are you doing, Hicchan~?"

            "Panic shoots through me as Misha starts talking at her normal volume, and I sputter out a hasty reply, still keeping my voice down despite the fact that she just blew any hope of being discreet I may have had."

            hi "I'm copying down that stuff, what are you doing? Why so loud?"

            show misha perky_confused_close
            with charachange

            mi "Aw~, really? But it's all in the book… That's why no one else is copying it down~!"

            hi "I know, why are you so loud?"

            show misha hips_grin_close
            with charachange

            mi "Why are you so quiet, Hicchan? It's hard to hear you."

            "I look around to see if anyone is noticing our conversation and it's pretty obvious that everyone has, even the teacher."

            show shizu behind_smile at offscreenright
            with None

            show shizu at tworight
            with charamove

            "Shizune smiles coyly and I start to wonder if Misha is doing this because she told her to."

            "Is it because of what happened between her and Lilly earlier?"

            "This is what I get for trying to be reasonable? For trying to take the middle path? Shizune is way too prideful, although by now I should know to expect that kind of behavior from her."

            hi "Why are you doing this?"

            show misha perky_confused_close
            with charachange

            mi "Huh?"

            "Misha is totally oblivious to the awkward stare the teacher is giving both of us, while trying to balance her textbook on one finger. For a brief second it looks as if things could get ugly, but the teacher simply looks away, as if it's not worth the trouble."

            "I guess this is a good thing, and I slump back in my seat in relief."

            scene bg school_scienceroom at bgright
            with shorttimeskip

            "The rest of day passes by uneventfully, and this time I'm able to appreciate that it does."

            play sound sfx_normalbell

            "When the bell rings, I'm not in a hurry, so I stay for a while, reviewing what we covered in class today. I prefer to leave last anyway, so I don't have to deal with crowding in the hallways."

            "I notice Shizune and Misha have also stayed behind, talking to someone from another class."

            "Shizune's signing so fast that her hands make noises like swords cutting through the air."

            "Misha is trying desperately to keep up, but it's clear she can barely manage to even understand her."

            "I put my head down. Whatever they're discussing, it looks like serious business. Probably way over my head. Not just that, but Shizune also seems angry, although it could just be her normal severity making it appear so."

            "Shizune signs to the point where her wrists crackle, and Misha struggles to spit it out in word form."

            "Sometimes she trips over herself like she's dealing with tongue twisters. And then on top of that, she has to sign back anything the other girl says."

            "Seems like a rough job."

            "Misha looks tired, like she's about to faint."

            "Luckily for her, their business is soon finished and the girls sit down on their seats again."

            show shizu behind_blank at tworight
            show misha perky_sad at twoleft
            with charaenter

            mi "Uwaaah! I'm so tired!"

            "She's hanging her head limply on her desk, looking exhausted."

            hi "Festival preparations must be tough for you."

            "Indeed, the people in this school seem to be taking the festival very seriously. Whenever I see people idling around before and after classes they're always talking about their plans for it."

            "It's kind of neat to see everyone being so enthusiastic about it."

            "I'm probably the only one who doesn't have something to do."

            show shizu basic_normal
            show misha perky_confused
            with charachange

            "Shizune starts signing at me and Misha perks up, looking at her hands with slightly unfocused eyes."

            show shizu behind_frown
            with charachange

            shi "…"

            "She signs with harsh, heavy, dramatic strokes."

            "Misha translates her signing into speech for me."

            "She does it so well it's almost like Shizune is actually speaking, transmitting her thoughts directly through Misha."

            show misha cross_frown
            with charachange

            mi "Well, we're in the Student Council, you know, so we're pretty busy."

            hi "Sarcasm?"

            show misha perky_confused
            with charachange

            mi "Huh?"

            "The tone of Shizune's actions make me think she is 'speaking' with disdain, but Misha interprets it normally, replacing whatever intent may have been there with her own chipper twist on things. It's still disorienting, I don't think I'll ever get used to it."

            hi "Never mind."

            hi "How could I forget, with you two trying to get me to join at least twice a day?"

            show misha cross_laugh
            with charachange

            mi "Hahaha~! But, Hicchan, some could say the work is too much."

            show shizu basic_normal2
            with charachangealways

            show misha perky_sad
            with charachangealways

            mi "It'd be nice if students were to show a little more support for their leadership, some appreciation to the ones who are working so hard to make it all possible."

            show shizu behind_frown
            with charachangealways

            show misha perky_smile
            with charachangealways

            mi "Maybe, for example, a little help. That's asking too much, is it? Yep~! Help would be appreciated~! From students like you~!"

            show shizu adjust_angry
            with charachangealways

            show misha hips_frown
            with charachangealways

            mi "If students would show their dedication and school spirit, and offer some help, well, I don't exactly need it…"

            show shizu behind_smile
            with charachangealways

            show misha hips_smile
            with charachangealways

            mi "But I wouldn't necessarily refuse it… So~! it would be nice if someone would…"

            stop music fadeout 2.0

            show shizu adjust_blush
            show misha perky_confused
            with charachange

            mi "Oh? Hello~!"

            show hanako emb_timid at offscreenright
            with None

            show shizu at offscreenleft
            show misha:
                xpos -0.45 xanchor 0.5
            show hanako:
                xpos 0.93 xanchor 0.5
            show bg at bgleft
            with charamove

            play music music_pearly fadein 1.0

            "I look over my shoulder and see Hanako peering timidly into the classroom, most of her body hidden behind the door."

            show misha perky_smile:
                xpos 0.15 xanchor 0.5
            with charamove

            mi "Hey! Playing delinquent again?"

            show hanako emb_blushtimid
            with charachange

            "Hanako blushes hard at Misha's straightforward jab, even if it was only in jest."

            show shizu basic_angry:
                xpos 0.35 xanchor 0.5
            with charamove

            shi "…"

            show hanako emb_downsad
            with charachange

            show hanako:
                xpos 0.97 xanchor 0.5
            with charamove

            "Shizune stares at her probingly, causing Hanako to look down and start backing away to the point where only her fingers can be seen wrapped nervously around the edge of the door."

            "Maybe she is showing her dislike of Hanako by association of her dislike of Lilly."

            "It appears so, and Hanako probably knows it as well."

            "They seem to have momentarily forgotten about trying to get me to stay for the rest of the day."

            hi "What is it, Hanako?"

            show hanako emb_timid
            with charachange

            ha "H… has Lilly been here?"

            mi "Sorry, Satou is not here. She, eh, came by in the morning though."

            show hanako emb_downtimid
            with charachange

            "Hanako keeps looking uneasily at Shizune, who stares back at her with her usual studying gaze. What is she trying to do?"

            "Of course Shizune isn't going to look away, and she is intimidating enough as it is, so I can only imagine how terrified Hanako would be."

            "It is a little funny though, watching Hanako's reaction to Shizune's normal behavior. This is what happens when two people of two different extremes meet, it seems."

            show hanako emb_timid
            with charachange

            ha "Do… do you know where she is?"

            show shizu behind_frown
            with charachange

            shi "…"

            show misha hips_frown
            with charachange

            mi "If she has any sense in her head, she's in her classroom, working on their festival project. But who knows where that woman is loitering at."

            if not wait_for_shizu or not _in_replay:
                show misha hips_grin
                with charachange

                mi "She might be slacking off somewhere, just like Hicchan~! Wahaha~!"

                "Damn, what is it with Shizune and her need to point out stuff like this?"

            if _in_replay:
                return

    if not side_lilly and wait_for_shizu:
        label .event_horizon:
            scene bg school_scienceroom at bgleft
            show shizu behind_frown:
                xpos 0.35 xanchor 0.5
            show misha hips_frown:
                xpos 0.15 xanchor 0.5
            show hanako emb_timid:
                xpos 0.97 xanchor 0.5

            mi "She might be slacking off somewhere~! What a useless woman~!"

            show hanako emb_downtimid
            with charachange

            show hanako at offscreenright
            with charamove

            hide hanako

            "Hanako nods quickly and retreats with haste, obviously to avoid any further contact with Shizune. Unfortunately, this turns their attention fully back to me."

            stop music fadeout 2.0

            show shizu at tworight
            show misha at twoleft
            show bg at bgright
            with charamove

            show misha hips_grin
            show shizu behind_smile
            with charachange

            mi "But Hicchan is not useless, right? Right? He said so himself~! Wahaha~!"

            "I can see where this is going, and I do not want any part of it, not after that experience yesterday."

            hi "Well, good luck with your preparations…"

            "I start packing my bag, ready to make a break for the exit."

            "Unfortunately I'm all the way on the other side of the room."

            "The short distance to the doorway seems like a vast No Man's Land to me now."

            show misha perky_smile
            show shizu behind_blank
            with charachange

            play music music_shizune fadein 4.0

            show bg at bgleft
            show shizu at center
            show misha:
                xalign -0.15
            with charamove

            show bg at center
            show shizu at tworight
            show misha at twoleft
            with charamove

            "Shizune and Misha both start maneuvering slowly in front of me, cutting off my route of escape in an unsettlingly cautious way that makes me think of ship-to-ship combat."

            show misha hips_grin
            with charachange

            mi "I think Shicchan is saying that you should help us, Hicchan~!"

            hi "Gee, I wouldn't know, she's so subtle."

            show misha perky_confused
            with charachange

            mi "But~! that's the intent, so, please? I can't keep up, we have to actually build stalls for the festival, almost all of them all by ourselves, can you believe that?"

            show misha perky_sad
            with charachange

            mi "Hammering boards together, over and over again, for hours, it's really hard!"

            mi "I'm so used to it I was doing swinging motions in class, and I didn't even know it!"

            "She bangs her desk a few times, imitating hammer blows."

            mi "It's so repetitive, I can't stand it! And yesterday, I actually hammered all the boards on top of each other…"

            mi "It was just a stack of boards all nailed together, and then I had to take it apart and do it all over again, and I got yelled at and laughed at~!"

            hi "Uh…"

            show misha perky_smile
            with charachange

            mi "So…"

            show misha hips_grin_close
            with characlose

            "She clamps a hand down on my shoulder and grins, quickly running her tongue across her teeth mischievously."

            mi "Do you have any plans for today, Hicchan?"

            mi "I wonder if you do~."

            hi "Sure I have plans…"

            show misha perky_confused_close
            with characlose

            mi "Really~?"

            mi "You're going to help us, right?"

            "I notice her hands are moving constantly."

            "She's signing everything we both say so that Shizune can understand."

            "Shizune is being somewhat quiet today. Is she still angry? Well, probably at least a bit. I can see it in her eyes. But, this could also just be another way of trying to guilt me into lending her a hand."

            "I have to find a way out of this."

            hi "Hey, I should go now, to the library. You know, homework…"

            hi "I should get going, shouldn't I? I have to be diligent, because I'm a new student, and all, so I have to make a good first impression, right? Yeah…"

            hi "See you later, then!"

            show misha behind shizu at offscreenleft
            show shizu at twoleft
            show bg at bgleft
            with ease

            show shizu basic_normal2 at offscreenright
            show bg at center
            with easeout

            show shizu cross_angry_close at tworight
            show bg at bgright
            with easein

            "I turn to bolt for the door, but Shizune is blocking my path, her arms crossed over her chest and a stern expression on her face."

            show shizu basic_angry_close
            with charachange

            "She wags a finger tauntingly and begins signing to Misha with the manner of a squad leader giving directions to his fellow soldiers."

            show shizu basic_angry
            with charadistant

            show misha perky_smile at twoleft
            with charamove

            mi "It didn't seem like you were in any rush to get to the library, Hicchan~!"

            show misha hips_grin
            with charachange

            mi "That's right, Shicchan~, it does seem like he was probably going to slack off for the rest of the day."

            show misha hips_laugh
            with charachange

            mi "Hahaha~! Wahaha~! You're surrounded~!"

            show shizu behind_frown
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "Let's go to the student council room~!"

            "She lets out a chuckle, and then breaks into laughter."

            show misha cross_laugh
            with charachange

            mi "I'm sorry, Hicchan, I feel bad, but this works out for everyone, right?"

            show shizu basic_normal2
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "That's right, Shicchan! Yes~, that's a good point too."

            show shizu behind_blank
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "Yes, this is beneficial to everyone, it solves all our problems."

            show shizu basic_frown
            with charachange

            shi "…"

            show misha hips_frown
            with charachange

            mi "Yeah yeah~!, I also thought he'd be more appreciative of our efforts."

            show misha hips_frown_close
            show shizu basic_frown_close
            with characlose

            "They pull themselves closer, as if they are about to pounce."

            hi "Hey guys, two-on-one isn't very fair, is it?"

            show shizu behind_blank_close
            with charachange

            shi "…"

            "She keeps looking forward, impassive, then gives a sinister smile."

            show shizu basic_sparkle_close
            show misha hips_grin_close
            with charachange

            mi "Come on, we have a lot of work to do! Let's go to the student council room~!"

            hi "Gee, I don't know…"

            show misha cross_laugh_close
            with charachange

            "Misha laughs."

            show misha hips_grin_close
            with charachange

            mi "Deja vu~?"

            "She chortles, before letting out another laugh."

            show misha cross_laugh_close
            with charachange

            mi "Hahaha, you know, my horoscope said it'd be a good day for me today."

            show misha perky_smile_close
            with charachange

            mi "And now that you're going to help—{w=.5}{nw}"

            show shizu adjust_smug_close
            with charachange

            "Shizune signs quickly to her."

            show misha hips_grin_close
            with charachange

            mi "Right~!, I mean, now that you've decided to help us, completely of your own free will, I'll be able to take it easy! Lucky~, huh?"

            "I open my mouth to say something but then realize there's no point."

            "I refocus on trying to think of a way out of this. No, their actions are clearly deliberate, there's no sense in attempting to reason with them."

            "You can't reason with madmen. I frown, and they don't even notice my discontent, further proving my suspicions."

            "They seem pretty relaxed now. I guess they think they've already won, so they're letting their guard down."

            stop music fadeout 2.5

            "That's kind of arrogant."

            "They pass forward in front of me as they move through the doorway,"

            hide shizu
            hide misha
            with charaexit

            "And I stealthily walk backwards back into the classroom as they step into the hallway, turning towards the stairwell."

            "I let out a sigh of relief and quickly pack the rest of my stuff so I can make my escape."

            play sound sfx_doorslam

            "The classroom door slams shut."

            play music music_running fadein 0.5

            show shizu cross_angry at offscreenright
            show misha cross_frown at offscreenleft
            with None

            show shizu at tworight
            show misha at twoleft
            with ease

            shi "…"

            mi "That wasn't very nice, there. Hahaha, you really got us good, though. Didn't he, Shicchan?"

            show shizu behind_frown
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "Right, right… …Hahaha!"

            show misha cross_frown
            with charachange

            mi "What was that about? I thought you said you'd help us!"

            mi "And then you bailed on us! And you thought you would get away with it, didn't you?"

            show misha cross_laugh
            with charachange

            "The indignant expression vanishes and she begins to laugh hysterically, calming down only after an aggravated look from Shizune."

            show misha cross_grin
            with charachange

            mi "Oh, ah… Yeah~, you thought you could get away with it! But, a criminal always returns to the scene of the crime!"

            "I didn't even manage to leave the classroom in the first place. No, wait, I didn't even agree to help in the first place."

            show misha perky_smile
            with charachange

            mi "Not very bright, are you, criminal? Thinking you can just shirk your duties like that… How low, Hicchan~!"

            hi "I'm a criminal? What did I do? What's the charge? What am I guilty of?"

            show misha hips_grin
            with charachange

            mi "That's for the courts to decide, criminal! I don't think we have to tell you that!"

            show misha perky_smile
            with charachange

            mi "Besides, you're the criminal here, you know what you did!"

            hi "Have you ever read 'The Trial,' by Kafka?"

            show misha hips_grin
            with charachange

            mi "No, what's that, Hicchan~? What does that have to do with this?"

            hi "I read it a few months ago. It's about these people who run a kangaroo court on a guy who just wants to live his life. They refuse to leave him alone, and he can't fight the power."

            show shizu basic_frown
            with charachange

            shi "…"

            show shizu behind_frown
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "Hicchan, what does that have to do with anything?"

            show misha sign_confused
            with charachange

            mi "Hey~!, what does that mean?"

            "She turns back to me after signing back and forth for a lengthy amount of time."

            show misha hips_frown
            with charachange

            mi "You know, we're both a little disappointed in you. You've let us down, Hisao."

            show shizu basic_frown
            with charachange

            shi "…"

            mi "Dropped the ball."

            show shizu behind_frown
            with charachange

            shi "…"

            mi "Left us hanging. And out in the cold~."

            show shizu cross_angry
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "Is that any way to treat a person? To run away from your responsibilities, to abandon your comrades?"

            show misha hips_frown
            with charachange

            mi "We think you owe it to us to honor your commitment."

            hi "What? But I didn't commit to anything~!"

            "My breathing catches in my throat and I momentarily start choking."

            show shizu basic_frown
            with charachange

            shi "…"

            show misha cross_smile
            with charachange

            mi "That's not true, Hicchan! You said you are not useless, you definitely said it, yes, definitely, definitely definitely~!"

            show misha hips_grin
            with charachange

            mi "We are calling you on those words now~! You better prepare to show you are not a useless guy!"

            mi "Your honor will be soiled forever if you try to get out of this~!"

            mi "So for the rest of the day, we are going to hang out together, just the three of us, and work hard!"

            show shizu behind_frown
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "You can't fool us!"

            mi "You should be happy, you're doing your school a great service. Ask not what your school can do for you…"

            mi "But what you can do for your school!"

            show misha cross_laugh
            with charachange

            mi "Hahaha!"

            mi "Hahahahahahaha!"

            "How depressing."

            show misha cross_grin
            with charachange

            mi "Cheer up, cheer up, Hicchan!"

            "She slaps me hard across the back with enough strength to knock the air out of my lungs. I gasp to breathe."

            mi "Besides, aren't you happy you get to spend the day with two cute girls?"

            show misha hips_laugh
            with charachange

            mi "Hahahaha!"

            "I guess they are right. I did blurt those words out."

            stop music fadeout 3.0

            "Accepting my fate, I follow them to the student council room…"

            scene bg school_council_ss
            with shorttimeskip

            play sound sfx_hammer
            play music music_tranquil fadein 3.0

            "…And hammer the final nail into the stall. It took all of the afternoon, and dinner time is nearly over. But it is done now."

            show shizu basic_normal_ss at center
            with charaenter

            "Shizune pulls out a roll of measuring tape and a small level, and inspects it thoroughly."

            show shizu behind_smile_ss
            with charachange

            "She smiles, looking pleased, then motions for Misha to come over."

            show shizu adjust_happy_ss
            with charachange

            shi "…"

            show shizu at tworight
            show bg at bgright
            with charamove

            show misha perky_smile_ss behind shizu at twoleft
            with charaenter

            mi "She says you did a very good job. In fact, you might actually have a gift for this."

            show misha hips_smile_ss
            with charachange

            mi "Wow, I'm impressed, too. And that was fast, have you done this before?"

            hi "No. Never."

            hi "Never before."

            hi "And I never will again."

            show shizu behind_smile_ss
            with charachange

            shi "…"

            mi "Well, our quota for the day is six stalls. In a few minutes, me and Shicchan should finish this one."

            show misha hips_grin_ss
            with charachange

            mi "That means~… four more to go!"

            show misha sign_smile_ss
            with charachange

            mi "We're making good time, she says~!"

            show misha hips_grin_ss
            with charachange

            mi "Isn't this great fun?"

            hi "What?"

            "I could think of a million things I'd rather do, but I suppose everyone has to do their share for the festival, even me."

            hi "You're both lucky that I'm helping you two out, if I really didn't want to, I could have gotten out of it easily."

            show shizu basic_normal2_ss
            with charachange

            shi "…"

            show misha perky_smile_ss
            with charachange

            mi "Really, Hicchan?"

            show shizu adjust_smug_ss
            with charachange

            shi "…"

            show misha cross_laugh_ss
            with charachange

            mi "Wahaha~! Shicchan thinks you are just running your mouth! Japanese people have no flight or fight reflex, Hicchan~!"

            "Shizune tents her fingers deviously."

            show shizu basic_happy_ss
            with charachange

            shi "…"

            show misha hips_grin_ss
            with charachange

            mi "Definitely~! Definitely, definitely~! If you really wanted to escape, you would have taken immediate action~! That is how you know someone is serious; when they have no doubts, no regrets!"

            show shizu basic_normal_ss
            with charachange

            shi "…"

            show misha sign_smile_ss
            with charachange

            mi "Maybe it was a bad idea to tell you that, since now Hicchan knows what to do next time~."

            "But, just the fact that she is all right with telling me this shows me that she doubts I'll be able to act on it."

            "That only makes me want to do it more, and I almost want the opportunity to do so to arise again. But if that happens, she might get me again somehow."

            show shizu behind_smile_ss
            with charachange

            shi "…"

            show misha perky_smile_ss
            with charachange

            mi "Shicchan says she is happy now."

            stop music fadeout 1.5

            scene bg school_council_ni
            with shorttimeskip

            play music music_dreamy fadein 0.5

            "Much, much later in the evening, we are looking at six completed stalls."

            "With the pride of a job well done, we sit back and admire the fruits of our labor, not sharing a word between us. Just admiring."

            "I realize I'm feeling quite thirsty."

            hi "Hey, isn't there a vending machine out in the hall? They're on all day, right?"

            show misha hips_smile at center
            with charaenter

            mi "Yeah, the drinks are very cheap, too. We usually get something from there on days like this."

            "I dig around in my pocket, and find a single hundred yen coin."

            hi "Is this enough? I'm feeling kind of thirsty."

            show misha hips_grin
            with charachange

            mi "A hundred yen? You can get any drink in the machine with that."

            hi "That's good, that's very good, then."

            show misha at twoleft
            show bg at bgleft
            with charamove

            show shizu adjust_happy at tworight
            with charaenter

            shi "…"

            show misha sign_smile
            with charachange

            mi "Ah, wait a second."

            show misha hips_grin
            with charachange

            mi "Hm? What is it, Shicchan? Do you want him to get you a drink too? Hahaha!"

            show shizu behind_smile
            with charachange

            shi "…"

            show misha perky_smile
            with charachange

            mi "Hicchan, you've really helped us out, so today I - I mean Shicchan, will treat you."

            show misha perky_confused
            with charachange

            mi "Hey, what about me?"

            show shizu adjust_smug
            with charachange

            shi "…"

            show misha perky_smile
            with charachange

            mi "What would you like? I'm feeling thirsty myself?"

            show misha perky_confused
            with charachange

            mi "So am I!"

            hi "Hm, I don't know. Anything's fine. I guess the melon soda."

            show shizu behind_smile
            with charachange

            shi "…"

            show misha perky_sad
            with charachange

            mi "Hey, wait, Shicchan! I also want a drink!"

            hide shizu
            with charaexit

            show misha at center
            show bg at center
            with charamove

            mi "Aw…!"

            show misha perky_confused
            with charachange

            mi "You know, it's times like this that I think she is just teasing me."

            hi "That's probably it. I'm sure she'll get you something, right?"

            mi "Yeah, she usually does. But… you never know…"

            hi "Heh."

            show misha at twoleft
            show bg at bgleft
            with charamove

            show shizu basic_normal2 behind misha at tworight
            with charaenter

            "Shizune comes back with two melon sodas and a can of fruit juice."

            "She hands me one of the sodas, and the other to Misha."

            show misha hips_grin
            with charachange

            mi "Thanks, Shicchan~! I had total faith that you'd get me one, I knew I could count on you! Wahahaha!"

            show misha perky_confused
            with charachange

            mi "But how did you know this was what I wanted? I usually get something else."

            show shizu behind_smile
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "What? You knew I'd want to try it? And that I like these kinds of childish things? Hahahaha!"

            show misha hips_laugh
            with charachange

            mi "Hahahaha!"

            "I gesture my thanks to Shizune, who smiles and nods."

            show shizu adjust_happy
            with charachange

            shi "…"

            stop music fadeout 4.0

            show misha sign_smile
            with charachange

            mi "Hey, Hicchan…"

            hi "Yes?"

            show shizu behind_smile
            with charachange

            shi "…"

            show misha perky_smile
            with charachange

            mi "We've been spending a lot of time together. Already, in such a short time, we've done so much."

            mi "We should both stop beating around the bush. What I'm trying to say is,"

            "It sounds a lot like she's going to ask me out, but that can't be it. Nevertheless, my heart is beating like a jackhammer. Damn, this reminds me of another similar scene earlier this year."

            "I try to say something, but my brains can't decide whether to stop her or to tell her to continue."

            "I feel myself blushing all the way to the ears."

            show shizu adjust_smug
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "What I'm trying to say is…"

            show misha hips_grin
            with charachange

            play music music_ease

            mi "Would you like to join the Student Council?"

            hi "Ah, what a disappointment."

            show misha cross_laugh
            show shizu adjust_blush
            with charachange

            mi "Hahaha! Hahahaha! Hahahahaha! Wahaha! Hahahaha!"

            mi "Did you think she wanted to ask you out, Hicchan?"

            mi "Hahahaha! Hahaha! Hahaha! Hahahaha!"

            mi "Hahahahahahahaha!"

            "I feel very embarrassed right now, I can feel myself getting even redder in the face."

            "Shizune also tries to hide a blush after Misha translates, and then puts a few sheets of paper in front of me."

            show shizu behind_frustrated
            with charachange

            shi "…"

            show misha cross_grin
            with charachange

            mi "So, how about it? All the paperwork is right here."

            show misha cross_smile
            with charachange

            mi "And you are sitting down, anyway. You look very at home here. Drinks and everything~!"

            show shizu basic_normal
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "What do you say?"

            "She quiets down a little and asks again a little more solemnly."

            show misha cross_smile
            with charachange

            mi "Hicchan, what do you say?"

            show misha sign_smile
            with charachange

            mi "You don't exactly hate this, right?"

            "I'm more than a little surprised by this sudden change of tone. I don't really know how to react to it."

            "For one thing, she isn't shouting uproariously with no regard for tact."

            "Before, I'm sure she knew already that I was going to say no."

            "This time, she seems actually serious."

            show misha perky_smile
            with charachange

            mi "I think maybe you should join. Not just because we could use your help, but, well, you're hanging out with us anyway."

            mi "I think Shicchan would like it if you would join as well. It's not like you hate us or anything, right?"

            show misha perky_sad
            with charachange

            mi "It wouldn't hurt if you joined. And I'd appreciate it if you would."

            "She seems to be having a hard time getting her words out, which is strange for someone talkative like Misha."

            "For some reason, I'm almost troubled by it."

            show shizu behind_blank
            with charachange

            "My eyes drift over to Shizune, who stares back at me tentatively, absentmindedly cleaning her fingernails."

            show misha perky_smile
            with charachange

            mi "If you don't want to join, I promise we won't ask again, but if you did, we would be really happy."

            "Both Shizune and Misha seem to be unable to look me in the eye."

            "I can't lie, the thought of being around two such cute girls is something that I couldn't possibly pass up."

            "I'm not looking forward to this kind of work every day, but there should be less after the festival."

            "At least, I hope so."

            hi "All right. I guess it can't hurt, so, why not?"

            show shizu adjust_happy
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "Wonderful. Wonderful! Ahahaha~!"

            "Shizune tents her fingers in satisfaction."

            show shizu basic_happy
            with charachange

            shi "…"

            show misha perky_smile
            with charachange

            mi "She'll fill everything out, Hicchan. Congratulations, you are officially a member of the Student Council now!"

            hi "Great. I'm not looking forward to a lot of work."

            hi "To be honest, I've never done any student council activities before."

            hi "But maybe it'll be a positive experience?"

            "Misha starts to clap, laughing exuberantly as she does."

            show misha hips_laugh
            with charachange

            mi "Congratulations, Hicchan!"

            show shizu adjust_smug
            with charachange

            shi "…"

            mi "Congratulations!"

            show shizu behind_smile
            with charachange

            shi "…"

            mi "Congratulations!"

            show shizu adjust_happy
            with charachange

            shi "…"

            mi "Congratulations!"

            hi "I get the message."

            "I can't help but smile, finding such a display childishly cute."

            show misha hips_grin
            with charachange

            mi "The Student Council is always busy, you know! But for today, we're done. See you tomorrow, Hicchan!"

            show misha hips_smile
            with charachange

            mi "We still have work left, so we'll be counting on you!"

            stop music fadeout 4.0

            scene bg school_hallway3
            with locationchange

            "I leave the room, feeling totally wiped out. The grounds are totally deserted, and the school looks pretty ominous this late. The council office is the only window with lights on any more."

            "Is this what the Student Council will be like? My body might not be able to take it."

            if _in_replay:
                return

    if side_lilly:
        label .above_and_beyond:
            scene bg school_scienceroom at bgleft
            with shorttimeskip

            play music music_tranquil fadein 3.0

            "Hanako doesn't come to the morning class at all, leaving her seat looking empty and lonely in the back of the classroom."

            "I have to tell her that Lilly was looking for her if I see her later."

            "After the events of this morning, class is pretty boring in comparison. I turn the pages of my textbook lazily."

            "I have a bit of catching up to do, despite trying to keep up with my studies at the hospital, but I'm not feeling that enthusiastic about it."

            "The clock at the front of the room sounds unbearably loud. The teacher hasn't said anything in over seven minutes, instead opting to cover the board in rows and rows of equations taken directly from the book."

            "The rhythmic clashing of chalk on blackboard seems to synchronize perfectly with the ticking of the clock."

            "I start to copy down the equations just to pass the time, even though they are right there in the text book."

            scene bg school_scienceroom at bgright
            with shorttimeskip

            play sound sfx_normalbell

            "When the bell rings, I'm not in a hurry because I have nothing to do, so I stay for a while, reviewing what we covered in class today. I prefer to leave last anyway, so I don't have to deal with crowding in the hallways."

            "I notice Shizune and Misha have also stayed behind, talking to someone from another class."

            "Shizune's signing so fast that her hands make noises like swords cutting through the air."

            "Maybe there is pent up anger in there."

            "Misha is trying desperately to keep up, but it's clear she can barely manage to even understand her."

            "I put my head down. Whatever they're discussing, it looks like serious business."

            "Shizune signs to the point where her wrists crackle, and Misha struggles to spit it out in word form."

            "Sometimes she trips over herself like she's dealing with tongue twisters. And then on top of that, she has to sign back anything the other girl says."

            "Seems like a rough job."

            "Misha looks tired, like she's about to faint."

            "Luckily for her, their business is soon finished and the girls sit down on their seats again."

            show shizu behind_blank at tworight
            show misha perky_sad at twoleft
            with charaenter

            mi "Uwaaah! I'm so tired!"

            "She's hanging her head limply on her desk, looking exhausted."

            "I'll use the opportunity to reconcile with Shizune a bit, without getting roped into the student council thing again, though I suspect that door is now closed for me."

            hi "Festival preparations must be tough for you."

            "Indeed, the people in this school seem to be taking the festival very seriously. Whenever I see people idling around before and after classes they're always talking about their plans for it."

            "It's kind of neat to see everyone being so enthusiastic about it."

            "I'm probably the only one who doesn't have something to do."

            show shizu basic_angry
            with charachange

            "Shizune scoffs at me first, as if trying to decide whether to ignore or sneer at me, but in the end she starts signing without doing either."

            show misha perky_confused
            with charachange

            "Misha perks up, looking at her hands with slightly unfocused eyes."

            show shizu behind_frown
            with charachange

            shi "…"

            "She signs with harsh, heavy, dramatic strokes."

            "Misha translates her signing into speech for me."

            "She does it so well it's almost like Shizune is actually speaking, transmitting her thoughts directly through Misha."

            "She must've practiced it vigorously."

            show misha cross_frown
            with charachange

            mi "Well of course, we're in the Student Council, you know, so we're pretty busy."

            show shizu basic_frown
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "It's an important duty of ours, to ensure the success of the festival with all our strength."

            show shizu behind_frown
            with charachange

            shi "…"

            show misha hips_frown
            with charachange

            mi "We would shame ourselves in front of the past student council generations if the festival were to fail."

            show shizu adjust_angry
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "That's why there must be no flaws, no… errr I think that was 'incumbrances,' no nothing that might make the festival short of perfect."

            "Shizune's passionate speech and Misha's enacting are really oddly fitting of them."

            stop music fadeout 2.0

            show shizu adjust_blush
            show misha perky_confused
            with charachange

            mi "Oh? Hello~!"

            show hanako emb_timid at offscreenright
            with None

            show shizu at offscreenleft
            show misha:
                xpos -0.45 xanchor 0.5
            show bg at bgleft
            show hanako:
                xpos 0.93 xanchor 0.5
            with charamove

            play music music_pearly fadein 1.0

            "I look over my shoulder and see Hanako peering timidly into the classroom, most of her body hidden behind the door."

            show misha perky_smile:
                xpos 0.15 xanchor 0.5
            with charamove

            mi "Hey! Playing delinquent again?"

            show hanako emb_blushtimid
            with charachange

            "Hanako blushes hard at Misha's straightforward jab, even if it was only in jest."

            show shizu basic_angry:
                xpos 0.35 xanchor 0.5
            with charamove

            shi "…"

            show hanako emb_downsad
            with charachange

            show hanako:
                xpos 0.97 xanchor 0.5
            with charamove

            "Shizune stares at her probingly, causing Hanako to look down and start backing away to the point where only her fingers can be seen wrapped nervously around the edge of the door."

            "Maybe she is showing her dislike of Hanako by association of her dislike of Lilly."

            "It appears so, and Hanako probably knows it as well."

            hi "What is it, Hanako?"

            show hanako emb_timid
            with charachange

            ha "H… has Lilly been here?"

            mi "Sorry, haven't seen Satou. She, eh, came by in the morning though."

            show hanako emb_downtimid
            with charachange

            "Hanako keeps looking uneasily at Shizune, who stares back at her with her usual studying gaze. What is she trying to do?"

            "Of course Shizune isn't going to look away, and she is intimidating enough as it is, so I can only imagine how terrified Hanako would be."

            "It is a little uncomfortable, watching Hanako's reaction to Shizune's normal behavior. This is what happens when two people of two different extremes meet, it seems."

            show hanako emb_timid
            with charachange

            ha "Do… do you know where she is?"

            show shizu behind_frown
            with charachange

            shi "…"

            show misha hips_frown
            with charachange

            mi "If she has any sense in her head, she's in her classroom, working on their festival project. But who knows where that woman is loitering at."

            if _in_replay:
                return

    if side_lilly and talk_with_hanako:
        label .paint_by_numbers:
            stop music fadeout 6.0

            scene bg school_scienceroom at bgleft
            show hanako emb_timid:
                xpos 0.97 xanchor 0.5
            show shizu behind_frown:
                xpos 0.35 xanchor 0.5
            show misha hips_frown:
                xpos 0.15 xanchor 0.5

            show bg at right
            show hanako at right
            show shizu at offscreenleft
            show misha at offscreenleft
            with charamove

            hide misha
            hide shizu

            hi "You need to find her? She was looking for you in the morning but I guess you have missed each other."

            "She waits a little without answering the simple question, looking awfully like she's not sure if it's proper to answer such a question."

            show hanako emb_blushtimid
            with charachange

            ha "Y…yeah."

            hi "I can come with you."

            hi "If it's okay."

            show hanako emb_downtimid
            with charachangealways

            show hanako emb_blushtimid
            with charachangealways

            "Hanako nods fractionally, still on guard, her shoulders stiff like wood. I get the feeling that she might be more comfortable by herself after all, but it's too late to back off now."

            "She has this really troubled expression she seems to wear almost constantly, one that makes me constantly be on guard myself. I wonder why."

            "I kind of understand why she always seems to be so wary… or maybe more like, why there could be a person like her."

            "But I still have no idea how I should act around such a person."

            hi "It's dinnertime soon. Were you planning to eat with Lilly?"

            show hanako emb_downtimid
            with charachangealways

            show hanako emb_blushtimid
            with charachangealways

            "She nods slightly."

            "So she must have been trying to get in the cafeteria."

            "Well, there's something of a dinner crowd, just like the cafeteria is crowded during lunch."

            "It's not as bad because dinnertime is longer than lunch hour, but I can understand why Hanako could be discouraged from going in."

            "I pick up my bag and we take our leave. Hanako skips a little to meet my initial pace, so I slow down to match her speed."

            scene bg school_hallway3
            with locationchange

            "It doesn't take long for us to be walking at a comfortable pace down the hallway."

            show hanako def_worry at right
            with charaenter

            "It almost feels like we're going for a stroll together; something that I can't say I've really done before with a girl."

            "Hanako doesn't seem to be thinking the same thing though. Even though we are walking at the same pace, she never comes within arm's reach of me."

            "I guess she's still a little uncomfortable around me. Given how shy she is, there doesn't seem to be much helping it, at least for now."

            scene bg school_cafeteria
            with locationchange

            play music music_night fadein 3.0

            "By the time we arrive at the cafeteria, there is not much of a crowd there, but Lilly is nowhere to be seen."

            show hanako emb_downsad at center
            with charaenter

            "Hanako's head sinks even lower than usual."

            hi "Have you looked somewhere else already?"

            show hanako basic_worry
            with charachange

            ha "J-just at the library… I was reading…"

            "So she does spend the classes she skips at the library."

            hi "Ah, so not exactly a thorough search then. Well, if I had to guess, she'd be in her own class like Shizune said, right?"

            show hanako cover_worry
            with charachange

            ha "R-right."

            show hanako basic_normal
            with charachange

            "With the slightest of nods, Hanako agrees with my reasoning."

            "God, she's being so awkward."

            "It's like I need double layered silk gloves with padding to even begin interacting with her."

            "Some small talk might help her become a bit more used to me. It isn't hard to tell that the silence between us is hovering on the edge of both our minds."

            hi "So you and Lilly usually hang out together after class, right?"

            show hanako emb_downtimid
            with charachange

            ha "Y-yes."

            "I'm not quite sure what I expected from her answer, nor why I even asked the question. That much was rather obvious, after all."

            "She doesn't seem like the type to cultivate a social circle, either, so I suspect that Lilly may well be her only friend."

            hi "Must be a pain being in different classes, I'm guessing."

            "She gives a sharp, almost reflexive nod. Compared to Lilly's careful thought about her actions and speech, Hanako hastens to make her answers as prompt and short as possible."

            show hanako emb_downsmile
            with charachange

            ha "Lilly… comes by the classroom, though. Even when she's busy…"

            "She gives a small smile as she says it, evidently appreciating the fact that Lilly goes out of her way to help her."

            "It's pretty cute, really. There isn't any need to say more, both of us content that the discussion's reached an end."

            scene bg school_staircase2
            with locationchange

            "As we ascend the stairs back to the lobby we are met by a group of students heading downstairs like a school of fish moving from one feeding area to another."

            show hanako cover_worry_close at offscreenleft
            with None

            show hanako:
                xpos 0.0 xanchor 0.4
            with charamovefaster

            "They seem to be keeping mostly to themselves, but before I can notice her doing so, Hanako has moved around behind me."

            hi "Hey, are you all right?"

            show hanako basic_worry_close
            with charachange

            ha "J-just keep going…"

            show hanako at offscreenleft
            with charamovefaster

            hide hanako

            "The students pass us without as much as a second glance, and Hanako takes up position to my side again as we enter the building, her momentary reprieve from her anxiety all but snatched away."

            scene bg school_lobby
            show hanako basic_normal at center
            with locationchange

            "Even as we climb towards the third floor, she doesn't seem to relax."

            "It isn't as if I've never known a shy person before, or even shy girls, but Hanako seems to be pretty far beyond what I'd call normal in her fear of other people."

            "If it weren't for Lilly acting as a mediator, I doubt Hanako would have even been able to walk beside me like this. She seems to completely shut down in the presence of others."

            "The rest of the walk up to Lilly's classroom continues in strained silence, while I rue her inability to socialize at all."

            scene bg school_hallway3
            with locationskip

            stop music fadeout 4.0
            $ renpy.music.set_volume(0.1, 0.0, channel="ambient")
            play ambient sfx_crowd_indoors fadein 2.0

            "After we make our way up the stairs, the noise coming from Lilly's classroom is audible from halfway down the hallway. I wasn't expecting such a din at all."

            hi "Well, I guess we found her…"

            "This wasn't hard. Did Hanako come here first then come to me for backup, I wonder?"

            "Well, if that's true, then at least she's starting to trust me a little. That can only be a good thing."

            "Eventually, the two of us reach the door to class 3-2. With Hanako less than subtly positioning herself behind me, I open the door."

            play sound sfx_dooropen
            $ renpy.music.set_volume(1.0, 1.0, channel="ambient")
            play music music_another fadein 1.0

            scene bg school_room32 at bgright
            with locationchange

            "Inside is a hive of activity, seemingly every student in the class talking at once as they work hurriedly on their separate tasks."

            "Going by the paint cans, decorations and banners being made, it must be for the upcoming school festival."

            "I guess my first priority should be finding Lilly…"

            "…{w} There."

            "Finding her among the din is surprisingly easy, not the least because of her looks."

            "With a couple of students gathered around her as she stands at the front of the class, she seems to be in charge of the preparations, or at least busy organizing them."

            "Carefully negotiating a path through the various students hunched over the floor for lack of desk space, I raise a hand entirely out of habit as we finally reach Lilly."

            hi "Hi, Lilly."

            show lilly basic_surprised at center
            with charaenter

            "She perks her head up as she breaks off talking to a noticeably smaller girl who must be her classmate, trying to listen as best she can."

            li "Sorry, who…"

            hi "Ah, sorry. Hisao. I have Hanako too."

            show lilly basic_smile
            with charachange

            show lilly at twoleft
            show bg at center
            with charamove

            show hanako basic_normal at tworight
            with charaenter

            ha "H-hi."

            "She's pretty skittish. Considering the number of people around, it isn't too hard to work out why."

            "Lilly takes a moment's pause to assess the situation before turning to the other student once again."

            show lilly basic_smileclosed
            with charachange

            li "For the moment, just ask Moriya for his advice. Kenji's busy with painting one of the banners already."

            "A quick nod and she bounces off, fingers carefully sliding along the wall's face for orientation."

            $ renpy.music.set_volume(0.1, 1.0)

            "Wait… Kenji? That Kenji?"

            "I quickly turn about, leaning to the side to see past Hanako."

            "Sure enough, in a corner of the room, Kenji's hunched over a sheet of cloth as he paints it. His eyes remain only inches from the brush, reminding me of how close he had to be to make out my face when I met him."

            $ renpy.music.set_volume(1.0, 1.0)

            show lilly basic_smile
            with charachange

            li "Sorry about that. Our class doesn't have many students with even partial eyesight, so they're in high demand."

            "That's right, class 3-2 was specially for students with poor vision. Preparing for the festival must be pretty arduous for them."

            hi "Need a hand? I could give you help if you need some. Maybe Hanako could too."

            "A chance to set her mind on something would do her good, but I doubt she has the courage to ask outright. She quickly nods in affirmation afterwards, so I'm confident I made the right move."

            "Lilly gives a noticeable sigh of relief."

            show lilly basic_weaksmile
            with charachange

            li "Ah, that's good. This might actually get finished before everyone goes off to dinner, now."

            show lilly basic_listen
            with charachange

            li "Would you be able to help the person painting the main banner? It's a big task for him to do, but nobody else can help."

            hi "Kenji? Sure."

            show lilly basic_surprised
            with charachange

            "She seems surprised that I know him. I can't really blame her."

            li "I take it you've met?"

            hi "Our rooms in the dorm are right next to each other. Hard to miss each other, really."

            show lilly basic_ara
            with charachange

            li "Well, it's good to see you're getting friends so fast."

            "Friend… I wonder if that's the right word to use for him."

            "Hanako's silence during the proceedings reminds me of the reason I put her up to helping in the first place."

            hi "We'll go help him then. He knows what needs doing, right?"

            show lilly basic_smileclosed
            with charachange

            li "That's right. Just ask if you have any problems."

            hide lilly
            hide hanako
            with charaexit

            $ renpy.music.set_volume(0.5, 2.0, channel="ambient")

            "Chorusing in assent, Hanako and I begin another trek across the classroom."

            "Kenji sits crouched on the floor, his gaze fixed on the white calico in front of him."

            show kenji tsun:
                xalign 0.5 ypos 1.0 yanchor 0.45
            with charaenter

            hi "Hey Kenji."

            "…No answer. He continues dragging his paint-soaked brush along the large half-painted kanji that's sketched on the sheet in pencil."

            hi "Kenji?"

            show kenji at center
            with charamovefastest

            ke "Huh? What? Who is it?"

            "If this is the way he treats class members, it's no small wonder he's working on this alone."

            hi "It's me. Hisao. From the—{w=.5}{nw}"

            ke "Right, right, I know that, man. What're you doing here, though?"

            "His dismissive attitude annoys me."

            "He must be the type to really get focused on his work, hating to be disturbed by anyone until he's done, I suppose."

            show kenji at twoleft
            show bg at bgleft
            with charamove

            show hanako cover_distant at tworight
            with charaenter

            "While we talk, the sound of Hanako's footsteps as she walks out from behind me reminds me that she's here."

            hi "I was just going to help with the banner. Hanako and I, that is."

            show hanako cover_worry
            with charachange

            ha "H… Hello…"

            show kenji happy
            with charachange

            ke "Oh. Er, hey. I guess that's okay."

            "As soon as Hanako enters the equation, his demeanor takes a complete about-face. His sudden faux-hospitality is slightly unsettling."

            "Oh, right. Women. On second thoughts, this may not have been a great idea after all."

            stop music fadeout 2.0

            scene bg school_room32 at bgleft
            show kenji neutral_close at left
            show hanako basic_distant_close at right
            with locationskip

            "Hanako and I grudgingly set ourselves down on the opposite side of the cloth banner to Kenji, noting the several small paint tins on the ground around it."

            "Class 3-2… noodle stall?"

            hi "You guys selling noodles at the festival on Sunday?"

            show kenji happy_close
            with charachange

            ke "Yeah, some stalls outside. Or something."

            "'Or something?' His noncommittal nature sparks a fair amount of suspicion on my behalf. The task at hand comes first, though."

            hi "So how do you want to split this? We do borders while you do the text? Or do you want to switch and do the borders?"

            show kenji tsun_close
            with charachange

            ke "Text is mine. You do borders."

            "He has surprisingly strong feelings on the topic."

            show hanako basic_distant_close
            with charachange

            "As I reach over to grab a brush, I notice Hanako's already debating between colors to use."

            show hanako basic_normal_close
            with charachangealways

            show hanako basic_distant_close
            with charachangealways

            show hanako basic_normal_close
            with charachangealways

            "By the time I've put brush to cloth, she's already started on a delicate pattern. Looks like my idea of taking her mind off everyone around her worked."

            "With a dark blue stroke, the three of us silently get to work."

            "Not before Kenji takes advantage of Hanako's working to lean towards me and whisper conspiratorially, though."

            show bg at center
            show kenji at center
            show hanako at offscreenright
            with charamove

            hide hanako

            show kenji neutral_close
            with charachange

            play music music_kenji fadein 0.5

            ke "Okay man, why're you here?"

            hi "Hanako just wanted some help to find Lilly, that's all."

            show kenji tsun_close
            with charachange

            "He apparently disapproves of my motivations."

            ke "I get it. It looks like I misjudged you."

            show kenji happy_close
            with charachange

            ke "You're infiltrating them, aren't you? Going deep undercover?"

            "I should have guessed. Letting the truth slip by him would probably be better than outright lying or annoying him, in any case."

            hi "Is that why you're here?"

            ke "Obviously. It sucks, but there's no better way to get intel than going in yourself."

            show kenji tsun_close
            with charachange

            ke "We gotta stick together, man. This is a harsh school, a harsh world."

            hi "Yes, very harsh."

            "He misses my true meaning as he leans back, satisfied I'm sympathetic to his cause. I'd better get down to work."

            stop music fadeout 2.0
            stop ambient fadeout 2.0

            scene bg school_room32
            show kenji neutral_close at left
            show hanako basic_normal_close at right
            with shorttimeskip

            ha "Finished."

            hi "Looks like I am too. Good job."

            "The two of us connect up the lines of our patterns, mine being as close a copy as I could manage of hers."

            scene bg school_room32
            with locationskip

            "With a grunt, I lever myself up from the floor and look around."

            play music music_dreamy fadein 4.0

            "Aside from Hanako and myself, there's only Kenji left finishing off a sign as well as Lilly and a couple of students talking among themselves in the classroom."

            "Looking at my watch, it's no surprise. It's getting pretty late."

            hi "Need a hand?"

            show hanako basic_normal at offscreenbottom
            with None

            show hanako at center
            with charamovefaster

            "I offer a hand to Hanako, which she uses to get herself up."

            "As she does, I can't help but glance at her wrist; if her scars extend even to there, just how much of her body was burned?"

            show hanako emb_downtimid
            with charachange

            "I feel a pang of guilt about it however as she quickly covers her wrist with her other hand."

            hi "Looks good, doesn't it?"

            show hanako emb_timid
            with charachange

            "She looks surprised for a moment before noticing that I mean the banner."

            show hanako basic_bashful
            with charachange

            ha "It does… I guess."

            "Her smile shows that she feels a slight sense of pride in the result, just as I do."

            hide hanako
            with charaexit

            "With the floor significantly neater for the decorations being placed on desks and shelves, it's much easier to get to Lilly as we cross the room."

            hi "We've finished the banner. I guess that's all that needs to be done?"

            show hanako basic_smile at tworight
            show lilly basic_smileclosed at twoleft
            with charaenter

            "Lilly gives an appreciative nod."

            show lilly basic_smile
            with charachange

            li "Thank you Hisao, Hanako. If there's any way I can thank you…?"

            hi "It's fine. Beats sitting in my room studying, at any rate."

            show hanako basic_normal
            with charachange

            ha "I don't mind either."

            "She nods, before suddenly remembering one last person."

            show lilly basic_surprised
            with charachange

            li "Oh, is Kenji still here?"

            "Just as I open my mouth, Kenji gives the answer from the other side of the room."

            ke "Yeah, just finished."

            "He carefully slides his sign onto an empty section of shelf to dry, before quickly walking past us and out the door."

            show hanako at center
            show lilly at left
            show bg at bgleft
            with charamove

            show kenji neutral:
                xalign 1.15
            with charaenter

            ke "Seeya man."

            hi "Bye."

            hide kenji
            with charaexit

            show hanako at tworight
            show lilly at twoleft
            show bg at center
            with charamove

            "The remaining two students say their goodbyes to Lilly before taking their cue to leave as well, leaving only the three of us."

            hi "Well, I guess that's everyone."

            show lilly basic_displeased
            with charachange

            li "I hope we don't have to do anything like that again."

            hi "Working past schooltime?"

            show lilly basic_concerned
            with charachange

            li "Indeed. The class's plans this year were ambitious. Maybe too ambitious."

            show hanako emb_smile
            with charachange

            ha "The stalls look nice, though."

            hi "She's right, it shows that a lot of work's gone into them."

            show lilly basic_ara
            with charachange

            li "My my, I'm sure a lot of us would be glad to hear that. At least now there's not much work to do until the festival itself."

            show hanako basic_smile
            with charachange

            ha "Umm… It's getting pretty late. Should we go?"

            show lilly basic_smileclosed
            with charachange

            li "That's probably a good idea. Are you going back to the dorms as well, Hisao?"

            hi "Yeah, I guess I'll tag along."

            scene bg school_gardens2_ni
            with locationskip

            "The nighttime lighting really makes the gardens look quite different. Compared to the usual look of lush greenery, things are much more calm."

            "Being that it's so late, the lack of students around probably helps. The odd one or two can be seen scurrying to and from the dorms trying to eke the most out of their approaching curfews, but no more."

            "All that can be heard is our footsteps, in addition to Lilly's cane regularly gently tapping the ground in front of her."

            "It's nice to finally be able to relax a bit after the mad rush during school."

            "Without even noticing it, I let out a small yawn."

            show lilly cane_smile_ni at twoleft
            show hanako basic_normal_ni at tworight
            with charaenter

            li "Tired?"

            hi "Yeah. Still getting used to the flow of things, I guess."

            hi "The… uh… thing… with Shizune took me kind of off guard, though."

            "I grit my teeth a little at the candid mention of their rather public spat. That said, I do want to sort out what in the world was behind it."

            show lilly cane_displeased_ni
            with charachange

            li "Ah… about that…"

            li "I'm sorry about it being so public. Shizune and I… go back some ways."

            "Her voice seems slightly irritated as she remembers Shizune, obviously unwilling to discuss it any further."

            show hanako basic_distant_ni
            with charaenter

            "I glance to Hanako for her views on this, but her expression is, unsurprisingly, evasive and difficult to read."

            "Either way I guess her apologizing for it is something, even if my curiosity goes unanswered."

            show lilly cane_weaksmile_ni
            with charachange

            li "I'll be glad once the festival is over, in any case."

            "The change of topic's welcome, clearing the thickening air quickly."

            hi "I can imagine. My old school's festivals were a lot more low-key than this."

            show lilly cane_smileclosed_ni
            with charachange

            li "Yamaku stresses the idea of a school community, so the staff likes to make our festivals and such special occasions."

            hi "And yet the students are the ones who do the work. What an unfair world."

            show lilly cane_giggle_ni
            show hanako emb_emb_ni
            with charachange

            "Hanako and Lilly both chuckle in agreement, savoring the fact that none of the staff are around to hear our grumbling."

            show lilly cane_smile_ni
            show hanako basic_smile_ni
            with charachange

            li "I suppose coming from a strict all-girls school helped me a bit with Yamaku. Compared to there, Yamaku is much more relaxed."

            "That'd go a way towards explaining her well-bred speech and behavior, in any case."

            scene bg school_dormext_half_ni
            show lilly cane_smile_ni at twoleft
            show hanako basic_smile_ni at tworight
            with locationskip

            "As we come up to the dormitories, it eventually comes time to leave for our respective rooms."

            hi "See you Lilly, Hanako."

            "The two both give polite nods before setting off to the women's dorms, just next to the guys'."

            stop music fadeout 4.0

            hide lilly
            hide hanako
            with charaexit

            "As is to be expected of such an arrangement, there's a staff member casually patrolling around outside to prevent any nighttime shenanigans."

            "Walking past him, I quickly stretch my arms and rub my neck, both quite sore after having worked on the floor for so long, before walking to my room."

            "It feels good to actually have direction, though. After so long in the hospital, the everyday facts of studying, homework and teachers seem almost a blessing."

            "I guess if things continue like this, my time at Yamaku might turn out okay."

            if _in_replay:
                return

    if side_lilly and not talk_with_hanako or not side_lilly and not wait_for_shizu:
        label .things_you_can_do:
            scene bg school_scienceroom at bgleft
            show hanako emb_timid:
                xpos 0.97 xanchor 0.5
            show shizu behind_frown:
                xpos 0.35 xanchor 0.5
            show misha hips_frown:
                xpos 0.15 xanchor 0.5

            show hanako at offscreenright
            with charamovefaster

            hide hanako

            "Hanako nods quickly and retreats with haste."

            stop music fadeout 2.0

            show misha hips_grin
            with charachange

            mi "What were we talking about? Oh yeah, we are really working hard to make the festival happen."

            "And driving other people insane along the way."

            hi "Well, good luck with that."

            "I stand up to leave, making my exit before either of them manages to berate me any more for slacking off."

            scene bg school_hallway3
            with locationchange

            "The halls are somewhat quiet, as expected. Everyone must be in club meetings or at festival preparations. Or both."

            "Shizune's words about being a slacker echo in my head."

            "I feel a bit guilty about not contributing, but I seem to lack the resolve to do something concrete about the matter."

            "For the festival, it's too late already unless I count helping Shizune and Misha which I naturally don't. And clubs… I don't know."

            "Maybe I'm not a club type of a person."

            play music music_soothing fadein 4.0

            scene bg school_dormext_half
            with locationskip

            "Halfway through the way from the school building to the dorms I spot a figure in front of the dorms."

            "It's Rin."

            "It looks like she is working on her mural today too."

            "I walk over to her, but she doesn't seem to notice me approaching."

            scene bg mural_unfinished
            show rin basic_awayabsent_close at tworight
            with locationchange

            "She's sitting on an upturned box, looking intently at the wall she is painting with a brush held between her toes."

            "The mural has progressed considerably since yesterday but it's still only half-done as far as I can tell."

            "More colors have appeared and the twisted human-like figures have spread and increased in number."

            "I have to say, the style is quite eye-catching and very unique. Not that I would be knowledgeable about art by any measurable scale, but it's very nice-looking, nevertheless."

            "I clear my throat to get her attention, but not startle her so that her concentration won't break."

            rin "Wait."

            "She doesn't even turn to check who it is."

            "I'll wait."

            stop music fadeout 6.0

            "…"

            "…"

            "…"

            "…"

            with shorttimeskip

            "…"

            "Fifteen minutes later I decide that her concentration is indeed unbroken, and also that I have waited long enough to warrant poking her gently on the shoulder to remind her of my presence."

            "Rin turns her head mechanically to my direction, ending up staring at my crotch level."

            show rin basic_deadpan_close
            with charachange

            rin "Oh, it's Hisao."

            play music music_rin fadein 0.3

            "She can tell? I would feel a lot less uncomfortable if she would look at my face."

            hi "An astute observation. Hard at work, I see."

            "The conversation starts as if I hadn't been here for a quarter of an hour already, but it's not a concern. At least it starts."

            hi "Looking good."

            "It does, the layers of paint hiding other layers of paint, mixing and shaping the human figures really create an impressive look. But Rin looks miffed."

            show rin basic_deadpanupset_close
            with charachange

            rin "You shouldn't comment on works in progress. Seven years of bad luck."

            hi "Sounds terrible. I guess I'll take it back then."

            "Still, it looks good. I wonder if I get fourteen years of bad luck for thinking that."

            show rin basic_awayabsent_close
            with charachange

            "Rin turns back to look at her painting and pokes it with a big toe."

            show rin relaxed_nonchalant_close
            with charachange

            rin "Could you mix some of this color? I am running out of it."

            "She looks down at a half-empty bowl with the remains of the same pinkish paint in it."

            "I didn't really intend to stay and help her with this project though… I guess I didn't intend to do anything much."

            show rin basic_absent_close
            with charachange

            "I look at Rin, she looks emptily back at me."

            hi "Just this once."

            show rin basic_awayabsent_close
            with charachange

            "Rin picks up another brush and drenches it in another tone of pale red. There are dozens of similar bowls all around her working area. From the looks of this scene she could have been sitting there for hours."

            "I wonder if she has. That would mean she'd have been skipping school though, which I of course wouldn't put beyond someone like Rin."

            "I pour a little bit of white and red into the bowl, trying to match the color with the one already on the wall."

            "I can't seem to get it right."

            "It's really inconvenient of her to not mix enough in the first place. Getting it to be exactly the same tone will be impossible, but at least I can try to get as close as I can."

            hi "Speaking of hard work, isn't that a huge workload for you too? It's such a big painting and all."

            show rin basic_deadpan_close
            with charachange

            rin "Oh, I’m not old and bitter enough yet to think like that."

            hi "I guess you aren't."

            show rin basic_deadpannormal_close
            with charachange

            rin "You guessed right."

            show rin basic_deadpancontemplation_close
            with charachange

            rin "Legs hurt though. They feel like slugs. Slugs made of sea slugs."

            hi "Because of the position?"

            rin "Yeah, I like doing it in a horizontal position more, if you know what I'm talking about."

            rin "But it can't be helped. Can't ask the wall to lay down."

            show rin negative_spaciness_close
            with charachange

            "Saying that, she stretches herself a little, bending her legs and back far more than a human should flex. It's astonishing how effortlessly she manages her body around."

            show rin negative_annoyed_close
            with charachangealways

            show rin negative_spaciness_close
            with charachangealways

            "There is a small flinch in her otherwise blank expression - a hint of pain maybe - as she stretches out her calves."

            "Rin must have stamina and dexterity far above a normal person to be able to live like she does, but she's wearing out working on this."

            hi "Why push yourself so much? Take a break or something at least. Continue tomorrow if it's bad."

            show rin basic_deadpannormal_close
            with charachange

            "This gives her a pause."

            "A long one too, feeling like a mental yawn."

            "…"

            show rin basic_deadpan_close
            with charachange

            rin "I don't think so, Hisao."

            rin "I'm not pushing myself."

            hi "Sure looks like you are."

            show rin basic_deadpannormal_close
            with charachange

            rin "No. It's not about pushing or pulling or anything related to that kind of thing."

            show rin basic_awayabsent_close
            with charachange

            rin "There is this boy."

            hi "A boy?"

            show rin basic_absent_close
            with charachange

            rin "Yes."

            hi "Where?"

            show rin basic_deadpannormal_close
            with charachange

            rin "At the art club."

            hi "Err… and?"

            show rin basic_deadpan_close
            with charachange

            rin "He is blind."

            hi "Oh. How can you paint if you are blind?"

            show rin basic_awayabsent_close
            with charachange

            rin "No idea."

            hi "So why is he there?"

            show rin basic_absent_close
            with charachange

            rin "That's the point. He is there."

            "She really should speak more than one word at a time to make this feel more like a discussion and less like an interrogation."

            show rin basic_awayabsent_close
            with charachange

            rin "He can't really do anything that you'd call art, right? But he comes there anyway. And paints."

            show rin basic_deadpannormal_close
            with charachange

            rin "Why?"

            hi "I don't know. Why?"

            show rin basic_deadpan_close
            with charachange

            rin "I don't know. That's why I asked."

            hi "So?"

            show rin basic_deadpannormal_close
            with charachange

            rin "He doesn't paint often but I think his paintings are very interesting."

            hi "I'm sure they are."

            show rin basic_lucid_close
            with charachange

            rin "I once tried that. Painting with eyes closed."

            show rin basic_deadpannormal_close
            with charachange

            rin "Wasn't too interesting. And cleaning up the floor took ages. Didn't try again."

            show rin basic_deadpandelight_close
            with charachange

            rin "But he is becoming better at sculpting."

            hi "I see."

            "Maybe she was trying to make a point with this. Maybe she forgot she had one."

            hi "Seems like the art club is full of interesting people."

            show rin basic_deadpan_close
            with charachange

            rin "Not really."

            "Pretty blunt statement, and she totally missed the sarcasm."

            hi "No?"

            show rin basic_awayabsent_close
            with charachange

            rin "Just like I said. They are not very interesting. I usually don't have much interest in people who are not interesting."

            show rin basic_absent_close
            with charachange

            rin "Maybe you have."

            hi "Maybe."

            "…"

            show rin basic_awayabsent_close
            with charachange

            rin "But that boy is interesting."

            show rin basic_lucid_close
            with charachange

            rin "Maybe I am like that boy, or maybe you are. Maybe everyone is."

            rin "Doing things you can't do, just because you can."

            "That's pretty deep I think, and tell that to her."

            hi "You're a deep one."

            show rin basic_deadpannormal_close
            with charachange

            rin "Nah. I'm a really shallow and thoughtless person. People say that to me all the time."

            show rin basic_deadpanamused_close
            with charachange

            rin "Did you know I can only think of four things at the same time?"

            hi "No, but now I do."

            show rin basic_lucid_close
            with charachange

            rin "Right now I'm thinking of the second floor's girls' toilet, ice-cream-flavored ice cream, the middle toe, and a haircut."

            show rin basic_awayabsent_close
            with charachange

            rin "I'm going to need a haircut."

            show rin negative_spaciness_close
            with Dissolve(0.1)

            show rin basic_delight_close
            with Dissolve(0.1)

            show rin negative_spaciness_close
            with Dissolve(0.05)

            show rin basic_delight_close
            with Dissolve(0.05)

            show rin negative_spaciness_close
            with Dissolve(0.05)

            show rin basic_delight_close
            with Dissolve(0.05)

            show rin negative_spaciness_close
            with Dissolve(0.1)

            show rin basic_delight_close
            with Dissolve(0.2)

            "She shakes her head around vigorously, letting her short and messy hair ruffle wildly around. I can see that doing it is something she likes to do."

            show rin basic_awayabsent_close
            with charachange

            "We fall silent as Rin treads around absentmindedly, poking some brushes around. The thought about the art club sticks in my head for a while longer."

            "I'm feeling like I'm treading on very unknown territory with art. The way these meetings with Rin go, it's as though I'm starting a smoking habit or something. I should probably stop talking with her."

            "It’s not like I dislike her, despite the confusion her being herself causes, and I don't dislike art either. I’ve even drawn for fun sometimes. I just don’t have a real creative drive, or any technical skill."

            "So usually, if I were to draw something, I get white paper syndrome and just freeze completely."

            "That, or I manage to draw something disfigured and promptly get frustrated at my inability to put the picture in my head down on the paper, then call it quits without really even trying to make an effort."

            "Rin clearly doesn't have this problem… but she frustrates me in another way. Being with her is like looking into a mirror that doesn't reflect anything."

            "It makes one question the sanity of the act."

            show rin basic_absent_close
            with charachange

            "Rin sits down on her box, swaying from side to side, apparently comfortable with the uncomfortable silence. She is staring at me again, or maybe over my shoulder. I can’t quite figure out where her eyes are focused."

            "I'm thinking of leaving so she can carry on working undistracted and that I can do whatever I'm going to do alone. It's not like I have anything that must be done today…"

            hi "Oh, shoot."

            show rin basic_deadpan_close
            with charachange

            rin "Who?"

            hi "Nobody, I just forgot to tell Hanako that Lilly was looking for her."

            hi "Do you know her? From my class?"

            show rin basic_deadpanamused_close
            with charachange

            rin "Oh, her. The Mystery Toilet Girl."

            show rin basic_amused_close
            with charachange

            rin "That person is funny. I saw her going to the toilet five times during one recess three weeks ago. I'm sure it's the world record."

            show rin basic_deadpandelight_close
            with charachange

            rin "It was very mysterious."

            hi "That's why you call her Mystery Toilet Girl?"

            show rin basic_absent_close
            with charachange

            rin "What other reason could there possibly be? Well, if there is, it's an eternal mystery. I didn't follow her in there."

            "…"

            show rin basic_awayabsent_close
            with charachange

            rin "Maybe it was the week before that? Could have been."

            "…"

            rin "Looking at her makes me hungry."

            hi "Don't say that."

            hi "At least, not around her."

            show rin basic_deadpannormal_close
            with charachange

            "Rin turns to look at me blankly, as if she's not sure why I reproved her."

            "But she doesn't acknowledge understanding any more than before, so I give up at this point."

            hi "So do you want to go eat dinner then?"

            show rin basic_awayabsent_close
            with charachange

            rin "No. Not yet."

            "Rin has turned her hungry gaze back to the wall, looking slightly more energetic, or at least slightly less lethargic than she did before."

            "It's as if the wall is an opponent she has to vanquish, something she must overcome before she can indulge in dinner."

            "This is the feeling I get. A weird sense of empathy overcomes me and makes me smile a little to myself."

            "For all her oddity, Rin is pretty cool after all."

            hi "I'll be going anyway."

            hi "Have fun."

            stop music fadeout 3.0

            "Rin has already grasped a brush and is dipping it into fresh paint, so of course she can't hear me any more or doesn't answer anything even if she does."

            if _in_replay:
                return

    scene bg school_dormhisao_ni
    with locationskip

    if promised:
        "Adhering to the nurse's nagging voice in the back of my head, I set my alarm clock to wake me up early enough to go jogging again."

        "I made a promise and I'm going to keep it. Besides, Emi is bound to rat on me if I don't show up."

        "But it's not all that bad."
    else:
        "I'm feeling tired so I set my alarm clock to wake me up as late as I can afford, while still making it to the first class."

        "The nurse's voice is almost nagging in the back of my head about morning jogs. I make a resolution to make up for it by going for a walk after school tomorrow."

        "Emi won't care either way, I bet."

    scene black
    with shuteye

    return

label a1c8o1:
    hi "Why am I being dragged into this, again? I've done more than enough, I think."

    hi "If you're angry with Lilly, that has nothing to do with me."

    show lilly cane_reminisce
    with charachange

    li "Now, wait just a second… are you implying the president is more right in scolding me than yourself?"

    "Ah damn, I think I could've worded that better."

    hi "No, I don't know about that but… I mean…"

    show shizu behind_frown
    with charachange

    shi "…"

    show misha perky_confused
    with charachange

    mi "What are you saying, Hicchan?"

    hi "It's just that I hardly think it's fair you can say that, seeing that I've helped you guys."

    "The mood has changed. This is like a showdown between two gunfighters now. Well, it was like that before too, but this time Shizune's focus is on me."

    "And so is Lilly's, though she keeps quiet. I'm afraid I inadvertently pissed her off."

    show shizu cross_angry
    with charachange

    shi "…"

    show misha hips_frown
    with charachange

    mi "Are you saying I'm wrong?"

    "What a dangerous situation."

    hi "It's too early to argue with you. …Yes, I think it's unfair of you to get on my case."

    show shizu behind_frustrated
    with charachange

    shi "…"

    show misha hips_smile
    with charachange

    mi "Hicchan, you want too much~! But~! You have a point. Okay, okay okay~! You're not lazy, Hicchan."

    show misha hips_laugh
    with charachange

    mi "Hahaha~!"

    "Shizune pushes her glasses up with her thumb, almost approvingly."

    show shizu adjust_happy
    with charachange

    shi "…"

    show misha perky_smile
    with charachange

    mi "That's good! If you're not useless, you shouldn't let anyone say you are~! But the next time I say it, it'll really be because you are disappointing me like Miss Class Rep here, so don't let this go to your head!"

    show lilly cane_displeased
    with charachange

    "Lilly takes the jab silently, a venomous visage frozen on her face."

    show misha hips_smile
    with charachange

    mi "Class rep~! Shicchan says: 'Don't forget that report, please~!'"

    li "I won't."

    show lilly cane_listen
    with charachange

    li "Would that be all?"

    show misha hips_grin
    with charachange

    mi "Yup~!"

    li "Then, good day to you all."

    "Her voice would cut the air of the classroom into half, if it was more tangible."

    hide lilly
    with charaexit

    "Lilly leaves the room, understandably in a bad mood but still managing to be as poised and calm as usual."

    show misha at twoleft
    show shizu at tworight
    show bg at bgleft
    with charamove

    hi "Shizune, you really did go a little too far today."

    show misha perky_smile
    with charachange

    mi "It's true, Shicchan, just a little~."

    "If I had been expecting Shizune to grudgingly admit I have a point there as well, I think I was expecting too much. She doesn't respond."

    show shizu basic_normal2
    with charachange

    shi "…"

    show misha cross_laugh
    with charachange

    mi "Hahaha~! Shicchan thinks you should mind your own business."

    show misha hips_smile
    with charachange

    mi "Hicchan, we have a few last minute things to take care of before class~! We might be late, so~! Can you please cover for us?"

    hi "Yeah."

    show misha cross_grin
    with charachange

    mi "Perfect~! Yay~! Okay~! Thanks, Hicchan!"

    hide misha
    hide shizu
    with charaexit

    "They walk outside even though there are only ten minutes left before the bell will ring, signaling the start of class."

    return

label a1c8o2:
    hi "Hey, I'm the new guy, remember?"

    hi "It's not like I could've done much, even if I wanted."

    show lilly cane_displeased
    with charachange

    li "That's right, you shouldn't expect a transfer student to jump right into it on his first week."

    "Lilly taking my side feels oddly comforting so I decide to back her up too."

    hi "Yeah you're being unreasonable with us both."

    show shizu behind_frustrated
    with charachange

    shi "…"

    show misha hips_frown
    with charachange

    mi "Excuses, excuses. Miss Class Rep has had plenty of time to deal with her report."

    mi "And we repeatedly offered you a position to help with the student council work, but you refused to commit yourself to making the festival a success."

    hi "Yeah, but as I said back then, I'm not sure if…"

    "I don't have time for this right now; no matter what I do, it will mean being drawn into a confrontation with Shizune, and that is what she wants."

    hi "Whatever. Forget it."

    return
