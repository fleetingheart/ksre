# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a4_emi:
    if have_a_minute and talk_to_her_mom:
        label .a_swing_and_a_miss:
            scene black

            pause 2.0

            play sound sfx_alarmclock

            pause 3.0

            scene bg school_dormhisao
            with openeye

            play music music_dreamy fadein 4.0

            "The sound of my alarm is an unwelcome intrusion on a sleep that's been a battle to obtain. I doubt I've been truly asleep for more than an hour or two."

            "Too much on my mind. Did I make the right choice, leaving the house yesterday? Did I manage to get Emi to realize how unreasonable she's been?"

            "Am I ever going to manage to get her to stop being unreasonable? Emi's mom gave me a new perspective the other day, but I'm still not sure that it's the right perspective."

            "She was hurt when I left yesterday, too."

            "I know that part of any conversation is going to have to include an apology about that. Right thing to do or not, I hurt her."

            "I hurry down to the track, eager to talk to Emi. I think I know what to say. Apologize for leaving first, and go ahead from there."

            scene bg school_track
            with locationskip

            "Unless, of course, Emi doesn't show up."

            "Which from the looks of things seems like it's the case. It's been about fifteen minutes since I got here, and there's no sign of her."

            "She's never late, not unless she's sick, which is unlikely. She probably just doesn't want to see me right now."

            scene bg school_track_on
            with locationchange

            scene bg school_track_running
            with locationchange

            "To take my mind off what that implies, I begin my warm-up routine and take off around the track."

            "It clears my mind wonderfully; for the half-hour I'm running, I don't think about anything but the run."

            scene bg school_track_on
            with locationchange

            stop music fadeout 4.0

            "However, once I've finished, and Emi still hasn't shown up…"

            "I get a little worried. With any luck, the nurse will know where she is; if nothing else, I can see what he thinks I should do next."

            scene bg school_nurseoffice
            show nurse grin at center
            with locationskip

            play music music_nurse fadein 0.5

            nk "So, last night didn't go too well, I take it."

            hi "Huh? You already know?"

            nk "I have my ways, and it's not as if I'd miss the distinct absence of your running partner this morning, now would I?"

            hi "No, I suppose not."

            show nurse neutral
            with persistent.charachange

            nk "So, what happened?"

            hi "Don't you know already?"

            show nurse fabulous
            with persistent.charachange

            nk "Maybe, but I could be bluffing. Perhaps I'd prefer to get your side of the story before I give any advice."

            "I quickly fill the nurse in on the events of last night, and he takes it all in without changing expression once."

            "Nothing about the whole event seems to surprise him, although he does seem surprised when I say that I didn't follow Emi."

            show nurse grin
            with persistent.charachange

            nk "Chose to talk to her mom instead, huh? Smart move, though I guess it didn't work out too well for you in the end."

            hi "Well, I'm not sure. Emi seemed apologetic when I left, or at least she seemed that way until she put up her defenses again."

            "The nurse sighs and spreads his hands in a conciliatory gesture."

            show nurse fabulous
            with persistent.charachange

            nk "Frankly, I'm surprised she let them down at all. Emi's had a lot of practice on that score. You probably won't get anything else out of her."

            hi "I don't believe you."

            nk "Is that so? You think she'll tell you the whole tale?"

            "I'd swear I just saw the nurse's eyes glitter a little. His expression is the same, but he leans forward ever so slightly."

            hi "I think she'll open up if I ask her without being an idiot about it, yeah."

            "The nurse gives his enigmatic smile in response and shrugs widely. I think he's enjoying his role a little too much."

            show nurse grin
            with persistent.charachange

            nk "That's the real trick, isn't it? Are you sure you know the right way to approach the subject? I can guarantee that Emi's going to try her hardest to pretend last night didn't happen."

            show nurse neutral
            with persistent.charachange

            nk "It will be painfully awkward for the both of you, but it'll also be a lot safer than trying to ask her for the whole story again. It could go worse, this time."

            nk "Are you ready for something like that?"

            "It sounds like a challenge, like he doesn't believe for a minute that I'd be so bold. I actually feel a little insulted by his lack of confidence in me."

            hi "Of course I'm ready for that! I love her!"

            show nurse fabulous
            with persistent.charachange

            "My outburst gets a raised eyebrow in response."

            nk "Well then."

            show nurse neutral
            with persistent.charachange

            nk "Good luck. Let me know how it all turns out."

            "Although he delivers his parting shot with the same smirk as usual, I actually think that the nurse wants me to succeed."

            stop music fadeout 3.0

            scene bg school_nursehall
            with locationchange

            "I resist the urge to charge directly to Emi's room to prove the nurse wrong. I've gone in half-cocked before, and the results were less than stellar."

            "If I'm going to do this, I need to figure out exactly what I'm going to say, and how I'm going to say it. Something to think about in class."

            scene bg school_scienceroom
            with shorttimeskip

            "Sure enough, by the time lunch rolls around, I think I have a good enough idea of what to say. I can do this."

            play sound sfx_normalbell

            scene bg school_staircase1
            with locationskip

            "The bell rings, and I grab my lunch and dash up the stairs, eager to be there first. I'll need to ask Rin to leave, and I'll need to—"

            $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
            play ambient sfx_rooftop fadein 1.0
            play sound sfx_door_creak

            scene bg school_roof
            show emi basic_hes at twoleft
            show rin basic_absent at tworight
            with silentwhiteout

            emi "Hi Hisao! Sorry I wasn't able to run with you this morning! I overslept!"

            "Somehow, both Emi and Rin have managed to get to the roof before me."

            hi "Oh, that's no problem. Last night was kind of… draining, I guess."

            "Emi's expression doesn't alter in the slightest."

            emi "Yeah, sorry about that! But I've had such a weird morning since then!"

            hi "Oh uh, really?"

            show emi basic_happy
            with persistent.charachange

            "Emi proceeds to make small talk for the rest of the time. I can barely get a word in edgewise, and soon find myself interjecting with the sort of back and forth dialogue that seems to have defined our early relationship."

            "I'm not gonna get anywhere on this problem during lunch, obviously. I can respect that; Emi obviously doesn't want to accidentally pull Rin into things, and that's fine."

            "Not that I think Rin would notice, but I can at least respect that sort of rationale."

            "I try a different tactic."

            hi "Hey, Emi. What are you up to after class today? I was thinking we could go somewhere for dinner, or something."

            show emi sad_depressed
            with persistent.charachange

            "Emi looks genuinely remorseful."

            emi "Sorry, Hisao! I promised the track captain that I'd stick around after practice and help some of the other kids with their form! It'll have to be some other time."

            hi "Yeah, sure…"

            scene black
            show bg misc_sky at center
            with locationchange

            nvl clear
            nvl show dissolve

            n "I'm honestly not sure what to do now. Maybe diving into things the day after would be a bad idea anyway."

            n "She might still be angry about it and just not showing it. Besides, if she's got track team responsibilities that's fine, right?"

            show bg misc_sky:
                linear 10.0 alpha 0.0

            n "I tell myself some variation on this theme the next day. Then the next. I wake up, run with Emi (during which she refuses to talk about anything but the run and what she was doing the night before), and then lunch, where we sit and make small talk until the bell rings."

            n "Her new responsibilities effectively keep me from seeing her outside of school. Maybe, just maybe, I'm letting it happen because it's safer this way, just like the nurse said."

            n "Except while it may be safer, I'm feeling more and more wretched. Emi doesn't look good when I see her any more; dark circles lurk under her eyes, she seems more and more distracted, and I can't bring myself to just ask what's wrong, because the timing never seems right."

            n "{vspace=30}I'm absolutely miserable."

            stop ambient fadeout 2.0

            nvl clear
            nvl hide dissolve

            scene black
            with dissolve

            if _in_replay:
                return

        call timeskip

        label .saving_throw:
            scene bg school_staircase1
            with locationchange

            "Another lunch comes. I trudge up the stairs to the rooftop like a condemned man."

            play ambient sfx_rooftop fadein 1.0

            scene bg school_roof at bgleft
            show rin basic_absent at center
            with locationchange

            "Rin is up there, but Emi is not. Immediately I worry that something's happened to her. Maybe the lack of sleep finally made her collapse, or something worse."

            "She seemed pretty tired after our morning run. Maybe she fell asleep and didn't even make it to class."

            hi "Hey, Rin. Where's Emi?"

            show rin basic_deadpancontemplation
            with persistent.charachange

            "In response I get a rather penetrating look from Rin, and something approaching a frown appears on her face."

            rin "Is that information really important?"

            hi "I think so. She's usually here with you, isn't she?"

            show rin basic_awayabsent
            with persistent.charachange

            rin "I don't know. I have no way of being sure."

            hi "I can confirm that she is, in fact, usually here with you when I come up."

            show rin basic_deadpannormal
            with persistent.charachange

            rin "Well she isn't now. Does that worry you?"

            hi "Kind of."

            show rin basic_deadpancontemplation
            with persistent.charachange

            rin "Hm."

            play sound sfx_door_creak

            pause 0.5

            show emi basic_closedhappy:
                xpos 0.1 alpha 0.0
                ease 1.0 twoleft alpha 1.0
            with None

            show bg at center
            show rin at tworight
            with charamovefaster

            show emi at twoleft

            "That seems to end the conversation, and the point becomes moot anyway because Emi bounds through the door with her usual energy."

            show rin basic_deadpan
            with persistent.charachange

            rin "Hisao is kind of worried about you, Emi. I don't think he can decide, or maybe I just don't believe him, but I think I'm going to go somewhere less awkward now."

            hide rin
            with charaexit

            pause 0.5

            show bg at bgright
            show emi basic_confused at center
            with charamovechangefaster

            "I'm so surprised by Rin's being so suddenly forward about, well, anything at all that I merely watch her head through the door."

            show emi basic_shock
            with persistent.charachange

            "Emi is similarly surprised, and colors slightly crimson as she stares openmouthed at me. It occurs to me that I should probably say something, if only to break the awkward silence that has suddenly descended."

            hi "It's because you weren't here yet. I was uh, worried about it."

            show emi basic_confused
            with persistent.charachange

            emi "Why?"

            hi "You're usually here, so I was worried that something had happened to you."

            show emi sad_grin
            with persistent.charachange

            emi "This isn't the first time that I've been late, you know. Did you get worried all the other times, too?"

            hi "Er, not really."

            show emi basic_closedgrin
            with persistent.charachange

            "Emi seems slightly amused by this. I don't know why, but that kind of pisses me off."

            show emi basic_grin
            with persistent.charachange

            emi "So why was this time an exception?"

            "Maybe it's the light, teasing tone of the question, but something in her response pushes me to be honest, though I can't help snapping at her when I say it."

            play music music_innocence fadein 10.0

            hi "Because you've been worrying me since dinner at your house, that's why."

            show emi basic_hes
            with persistent.charachange

            "Well. Now it's out in the open. And Emi's eyes are wide, and she looks like she wants to bolt, but she doesn't."

            show emi sad_shy
            with persistent.charachange

            emi "Ah. Still on that, I see."

            hi "What, you think I'm supposed to just forget about it? You threw me out of your house! We've been going on for almost a week pretending it never happened!"

            show emi sad_annoyed
            with persistent.charachange

            emi "I didn't see you bringing it up either, you know."

            hi "I know, and I'm sorry that was the case. We have to address it, or we'll just keep up this whatever it is we've got right now."

            hi "It's killing me to look at how you look right now, did you know that? Those circles under your eyes and that distracted look in them, and I can't help worrying that I've caused it somehow."

            show emi sad_pout
            with persistent.charachange

            emi "You haven't. Trust me."

            hi "Well I haven't helped, either. I keep pushing you to tell me things you aren't ready to tell me; maybe I was wrong to try getting your mother to help me out, but I've been so worried about you that I didn't know what else to do."

            show emi sad_depressed
            with persistent.charachange

            emi "Well, you don't have to worry about me any more, okay? I think it's pretty clear we're not right for each other, so maybe we should just… stop."

            "Her face is twisted up as she says this, like she doesn't want to say it but forces herself to anyway."

            hi "You don't actually want that, do you? Heck, you can barely bring yourself to say it. Anyway it won't keep me from worrying about you. I care too much about you to just stop on command."

            hi "You don't want to tell me what's wrong? That's fine, but I won't stop trying to help you, even if it's just standing by you."

            show emi sad_angry
            with persistent.charachange

            emi "Stop saying that!"

            "She's shaking now, and as she looks at me I can see she's afraid and frustrated and a million different things all at once. I shake my head slowly and take a few steps toward her."

            hi "You know what your mom told me? She told me that you'd never ask for help, because you know that you're strong enough to get through anything on your own, but that's not the full story, is it?"

            show emi basic_hes
            with vpunch

            "Her eyes go wide, and she takes a step back. I keep going, because I think I've finally figured it out. Something tells me I won't get another shot. I've put it off for far too long as it is."

            hi "There's no harm in having someone help you, unless you're worried about needing help in the first place. You're scared, aren't you? Because of…"

            "I trail off, because I don't know for certain what happened to Emi's father, and I don't want to jump to a conclusion."

            hi "Well, never mind why, but it's okay to be afraid. You've been running from it and from me for so long, even though you know eventually you have to turn around and face your fear, and I'm going to be there to help when you do."

            hi "I won't stop, because I don't think you'd want me to. You can understand that sort of determination, can't you?"

            "I can see that I've gotten through to her, but she quickly falls back to anger to try and push me away again."

            show emi sad_angry
            with persistent.charachange

            emi "Back on your white charger, Hisao? Gotta help the poor cripple face her emotional problems? What do you know about me, and about what I've already had to face?"

            show emi sad_grit
            with persistent.charachange

            emi "You think two months of learning to walk again was fun? But I did it, and after I did that I had to…"

            "For a moment it seems as if she's going to say something else, but she cuts herself off."

            hi "And after all that, you don't think you can get past your fear? Emi, I can't fathom what you've been through, but to come through it and still be the sort of girl that you are, well, it makes me think that you have even more strength than you think."

            hi "So I'm not going to help you because I think you need rescuing. I don't want to be a knight rescuing the damsel in distress, but even knights helped each other out, you know. I want to help you, even though I know you can do it on your own."

            show emi sad_depressed
            with persistent.charachange

            "For a moment it looks like Emi's going to break down completely, but she doesn't. Tears run down her face, but she stares at me steadily."

            emi "Why are you trying so hard to help me?"

            hi "I'd say that it's because I owe you one for helping me out when we first met, but that wouldn't be the truth. The truth is, I just want you to be happy, because I love you."

            stop music fadeout 4.0

            "Had I ever said that before? We've been in a relationship, and it's been pretty obvious that I love her, but did I ever actually speak the words?"

            show emi sad_shyblush
            with persistent.charachange

            emi "What did you say?"

            "I say it again, savoring the feeling of being able to say it at all, being able to say it and mean it. Emi seems stunned."

            hi "I said I love you, Emi. I love you. Just you, and that makes me want to stand by you, no matter what you have to face."

            play music music_serene fadein 0.5

            show emi excited_sad_close
            with vpunch

            "I'm wrapped in a fierce hug then, as Emi begins to sob against my chest."

            emi "I'm sorry! I'm so sorry about everything but I'm so scared, Hisao, I'm so scared of losing you and I love you too but I can't lose you I just… I'm so sorry!"

            show emi sad_shy
            with charadistant

            "I hold her quietly, shushing her until she settles down. She steps back, a little more composed."

            emi "Will you come with me tomorrow? Back to my house? There are some things I need to show you, if I'm going to do this."

            hi "Of course. Maybe this time we can leave together, instead of separately."

            show emi sad_grin
            with persistent.charachange

            "Emi grins, a sudden flash of brightness that seems more genuine than anything I've seen in the past week."

            emi "Yeah, maybe."

            play sound sfx_warningbell

            "The lunch bell rings, and I curse the universe's poor sense of timing."

            hi "Are you free tonight? We can talk more then, right?"

            "Emi shakes her head."

            show emi sad_depressed
            with persistent.charachange

            emi "Sorry Hisao, but I'm still helping the track team. Plus, I don't think it would be good if we talked this over tonight. I'm going to be too tired to think properly, and I want to be able to tell you everything without screwing it up."

            show emi sad_shy
            with persistent.charachange

            emi "You can wait, right?"

            "Even now, there's a bit of fear in her voice. I smile and rest a hand on her shoulder."

            hi "Okay. I'll be waiting."

            show emi excited_amused_close
            with characlose

            "Emi gives me a quick kiss before she heads for the stairwell."

            show emi sad_grin
            with charadistant

            emi "Thanks, Hisao. See you tomorrow morning."

            hi "Wouldn't miss it."

            hide emi
            with charaexit

            $ renpy.music.set_volume(1.0, 2.0, channel="ambient")
            stop ambient fadeout 2.0

            scene bg school_staircase1
            with locationchange

            "I head down the stairs with the feel of her lips on mine, suddenly aware of how much I've missed that sensation. I'll have to remember to thank Rin for getting us to talk to one another."

            "Although it's possible she won't even realize what she's done. Still, if not for her I doubt I'd have ever been able to confront Emi again."

            "I guess I needed more help than I realized. Tomorrow, however, I'll need to stand alone through whatever Emi's trying to work herself up to doing."

            "I'll be up to the task. I hope."

            stop music fadeout 2.0

            scene black
            with dissolve

            if _in_replay:
                return

        call timeskip

    label .whispers_of_the_past:
        scene black

        pause 2.0

        play sound sfx_alarmclock

        pause 3.0

        scene bg school_dormhisao
        with openeye

        "The morning sun is bright through my open window, and the sound of my alarm quickly has me up and about."

        "I slept surprisingly well last night, secure in the knowledge that at least I've got another chance with Emi."

        "If I can just keep myself from doing anything stupid, maybe I'll find out what's been eating her recently."

        "I have a few educated guesses, but nothing concrete. And certainly nothing that I'm going to say to her; I'd much prefer to have her tell me herself."

        if have_a_minute and talk_to_her_mom or _in_replay:
            "Although I can't help remembering the nurse's warning that I might not like what she has to say. Do I really need to know that badly?"

            "What if it's something awful that makes me repulsed by her? Can I really say that I'm prepared to handle whatever she has to say, regardless of what it is?"

            "Emi said she wanted to tell me 'without screwing it up.' What the hell did she mean by that? What's there to screw up?"

            "I suppose there's not much use worrying about it, though. I'll find out today. It occurs to me that I really, really need a run this morning, to clear my head if nothing else."

        scene bg school_track
        show emi basic_grin_gym at center
        with locationskip

        "Emi is waiting for me as promised, looking a little haggard but otherwise bright and cheerful. Much more so than any previous day this week."

        show emi excited_proud_gym
        with persistent.charachange

        emi "Hisao! You're late!"

        "I wave my hand dismissively."

        hi "Nonsense! You're just early."

        play music music_emi fadein 2.0

        show emi basic_closedgrin_gym
        with persistent.charachange

        "Emi grins back, and it feels like we're finally back where we should be with one another."

        "Except now Emi, not just me, wants to take another step forward. Although a part of me worries that she'll back out at the last second."

        show emi basic_grin_gym
        with persistent.charachange

        emi "Hurry up and stretch, Hisao! I don't want to miss the bus!"

        hi "The bus?"

        show emi sad_grin_gym
        with persistent.charachange

        if not have_a_minute or not talk_to_her_mom and not _in_replay:
            emi "Yeah, the bus. I want to show you something, and I don't want to be late."

            hi "Oh, okay."

            "I try not to grin too wide. I'm happy beyond words that Emi wants to hang out after the run at all, but her promise of showing me something has me even more intrigued."

            "Is this what she had to think about? I wonder just what she's planning to do."
        else:
            emi "I said I wanted you to come back to my house, remember? And I promised mom we'd be there in time for lunch, so I wanted to hurry!"

            hi "Early start, huh?"

            show emi basic_closedgrin_gym
            with persistent.charachange

            emi "It's more for my mom's benefit than anything else."

            hi "Ah, well that's okay."

            "I unsuccessfully try to guess what Emi has planned, shortly before realizing that it doesn't matter that much to me."

        show emi basic_concentrate_gym
        with persistent.charachange

        play sound sfx_gymbounce

        show emi gymconcentratebounce

        "I quickly go through my warm up routine while Emi bounces impatiently from one foot to the other. She really does seem to want to get moving as soon as possible."

        scene bg school_track_running
        with shorttimeskip

        "The run is over so quickly I can barely believe that I haven't fallen over dead afterwards. Emi set a blistering pace and I, in my foolishness, kept up with her."

        scene bg school_track_on
        with Dissolve(2.0)

        show emi basic_grin_gym at center
        with charaenter

        "Well, until the last few laps. I had to slow down just in case. But I don't mind, and Emi's waiting patiently for me when I finish. As patiently as she can wait, anyway."

        show emi basic_closedgrin_gym_close
        with vpunch

        emi "Finished? Good! Come on!"

        stop music fadeout 2.0

        scene bg school_nursehall
        with locationskip

        "Grabbing my arm, she practically rushes me down to the nurse's office."

        play music music_nurse fadein 0.5

        show nurse neutral:
            twoleft
            xpos 0.2
            easein 0.5 twoleft
        with charaenter

        show nurse at twoleft

        nk "You seem in a hurry, Emi. Trying to catch the early bus?"

        show emi basic_grin_gym at tworight
        with charaenter

        emi "Yeah, I told mom I'd be back for lunch."

        show nurse grin
        with persistent.charachange

        nk "Well, I'll take care of you first, then."

        show emi basic_confused_gym
        with persistent.charachange

        emi "But Hisao's gotta come with me too!"

        show nurse fabulous
        with persistent.charachange

        "The nurse raises a single eyebrow at this statement and peers at the two of us searchingly."

        nk "Really? Today, huh?"

        show emi sad_grin_gym
        with persistent.charachange

        "Emi's response is a nod, followed by a surprisingly shy grin."

        show nurse grin
        with persistent.charachange

        nk "Well then, we'll make this quick."

        hide nurse
        hide emi
        with charaexit

        "Emi enters the nurse's office, and I patiently wait outside for her to be finished, wondering just why the nurse seemed to be surprised by Emi's declaration."

        "I feel like I'm missing out on some joke or the significance of today. Beyond the fact that it is clearly significant in some way, of course."

        scene bg school_nurseoffice
        with shorttimeskip

        "True to his word, the nurse has Emi out of his office surprisingly quickly, and I take her place after promising to meet up at the front gate. The nurse takes my pulse and listens for a bit."

        show nurse fabulous at center
        with charaenter

        nk "Your heartbeat's faster than usual. Been pushing yourself again, have you?"

        hi "Well, Emi seemed in a rush to get through the run, so…"

        show nurse neutral
        with persistent.charachange

        nk "Hm, I'm not surprised. Today is rather important to her, you know."

        hi "I suspected that could be the case, but I have no idea why that's the case."

        show nurse fabulous
        with persistent.charachange

        nk "She hasn't told you? Interesting."

        hi "So you're not going to tell me either, then."

        show nurse grin
        with persistent.charachange

        nk "No, I'm not. I suspect that Emi has her own plan for explaining today to you, and I don't want to mess with that. You'll find out soon enough, so what's the rush?"

        show nurse neutral
        with persistent.charachange

        nk "Now as for your heart, I would take it easy the rest of the day. No spontaneous races or anything like that, got it?"

        hi "Got it. She won't have her running legs on anyway, right?"

        show nurse grin
        with persistent.charachange

        nk "No, but if you think something like that is going to stop her…"

        hi "Good point."

        show nurse neutral
        with persistent.charachange

        nk "I don't think it'll be much of an issue today of all days, but still."

        "If he's trying to reassure me, he's doing a terrible job. I'm quickly becoming more and more worried about what today could be for, like suddenly finding out Emi's in a cult or something."

        "At the same time, if today is such a big deal and Emi wants me to be with her for it, then maybe she really does want to grow closer to me. Maybe this will be the answer to all the riddles, to the sleepless nights and the sudden mood swings."

        stop music fadeout 1.0

        scene bg school_dormhisao
        with locationskip

        "Either way, I barely remember to thank the nurse before taking off as quickly as I dare for my room, to get a shower and throw on some decent-looking clothes. If today is as important as it seems to be, I should dress appropriately."

        scene bg school_gate
        show emicas grin at center
        with locationskip

        play music music_dreamy fadein 2.0

        "Emi, of course, proves me wrong as soon as I reach the front gate, wearing her usual shirt and shorts. So at least I know it's not a terribly formal affair, whatever it is."

        show emicas smile
        with persistent.charachange

        emi "You're early, Hisao."

        hi "Not as early as you. Eager, are we?"

        show emicas wink_up
        with persistent.charachange

        "Emi cheekily pokes out her tongue."

        show emicas closedsmile
        with persistent.charachange

        "The bus stop isn't very crowded at this hour, which seems to please Emi, and we end up relaxing a little as we wait. We sit in silence for a while, but I can tell that Emi's trying to work herself up to say something."

        "I don't have anything to say myself, so I sit waiting for her to talk. It doesn't take too long."

        show emicas awayfrown
        with persistent.charachange

        emi "So uh, I'm sure you're curious as to why the nurse thought it was so weird for me to be bringing you along today…"

        hi "I was a bit, yes, but if you're not ready to tell me—"

        show emicas blush_close
        with characlose

        "Emi stops my sentence by placing a finger on my lips."

        show emicas frown_close
        with persistent.charachange

        emi "Don't tempt me, Hisao. I want to tell you this, but I'm just uncertain as to how to go about it. I don't want to keep delaying or deferring, I just want to be able to say it."

        hi "So say it."

        show emicas neutral_close
        with persistent.charachange

        emi "You know that it's not going to be that easy for me, Hisao."

        hi "So treat it like running. Warm up to it with something small and easy, and go from there. But don't do it too fast, okay? I'm a patient man, I can wait for you to get to it."

        show emicas awayfrown_close
        with persistent.charachange

        "Emi seems to consider my words, weighing them against what is probably a desire to get it over with. I will admit, as much as I keep telling Emi to take her time, I wouldn't mind her getting it over with either."

        "But somehow I know that Emi probably needs more time than the bus ride will provide to get it all out, whatever it is."

        show emicas frown_close
        with persistent.charachange

        emi "Yeah, maybe you're right. The bus stop probably isn't the best place for this anyway. But just to make sure that I don't go back on my word, I'll at least say this:"

        show emicas awayfrown_close
        with persistent.charachange

        "She takes a deep breath, lets it out, and after a moment says in a low voice,"

        show emicas weaksmile_close
        with persistent.charachange

        stop music fadeout 1.0

        emi "We're going to see my dad today."

        "The words hang in the air, and I can see that Emi's afraid that I'll panic and disappear in response. Which a part of me almost wants to do."

        "But it would be stupid of me to back out, or to suddenly abandon the promise I made to be there for Emi when she needs me."

        "The nurse thought it was so weird of her to bring me along. She doesn't bring anyone along, or at least I'm willing to bet that she hasn't before today."

        "The day seems to take on an even greater significance. What has it taken Emi to even get this far?"

        play music music_dreamy fadein 5.0

        hi "Ah."

        "And why is that the best I can manage as a response?"

        show emicas neutral_close
        with persistent.charachange

        emi "Yeah."

        hi "I uh, I don't know what I should say."

        emi "Nothing, I think. Just promise that you're going to come with me."

        hi "Of course! You know I will."

        show emicas weaksmile_close
        with persistent.charachange

        "Emi smiles wanly, looking a little relieved."

        emi "Good. In that case, we'd better get going."

        "The bus pulls up just a little after she finishes the sentence."

        scene bg city_street4
        with shorttimeskip

        $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
        play ambient sfx_traffic fadein 2.0

        "Vague memories of my first trip out here come to mind as I step off the bus, but unfortunately, they're too vague to be of any use."

        "I will be the first to admit that I don't quite recall how to get to Emi's house, so I let her lead the way."

        $ renpy.music.set_volume(1.0, 8.0, channel="ambient")
        stop ambient fadeout 1.0

        scene bg emi_houseext
        with locationskip

        "She seems content to walk in silence, and I myself have no idea what I could possibly say, so the two of us arrive at her house having said nothing since getting off the bus."

        show meiko smile:
            tworight
            xpos 0.8
            easein 0.5 tworight
        with charaenter

        show meiko at tworight

        "Emi's mother opens the door and doesn't seem surprised to see me standing next to her daughter. I expect that Emi would have phoned ahead to let her mother know of the change in plans."

        show meiko happy
        with persistent.charachange

        emm "Emi, Hisao, you're just in time! Lunch is just about ready."

        show emicas happy at twoleft
        with charaenter

        emi "Great! I was afraid we might be running late."

        hi "As fast as you were going this morning, I doubt there was much of a chance of that."

        show meiko serious
        with persistent.charachange

        emm "I certainly hope she wasn't too much of a bother, Hisao. She tends to get a little paranoid about being on time when food's involved."

        hi "I hadn't noticed."

        show emicas pout_up
        with persistent.charachange

        "This earns me a swat on the arm from Emi, who despite the serious nature of our conversation on the bus and the almost brooding quiet walk has quickly become cheerful again."

        "Probably to keep her mother from worrying about whatever it is Emi plans to tell me later."

        scene bg emi_dining
        with shorttimeskip

        "Mrs. Ibarazaki ushers us in, and in short order we're around the table devouring lunch. I hadn't realized how hungry I was until I got here, but for once I seem to be eating almost as much as Emi."

        show meiko happy at tworight
        show emicas closedsmile at twoleft
        with charaenter

        emm "Goodness, it's a good thing I made so much. The two of you are acting like you haven't eaten in days!"

        hi "I skipped breakfast this morning."

        show emicas grin
        with persistent.charachange

        emi "Me too."

        show meiko smile
        with persistent.charachange

        emm "Had to catch the bus, I assume?"

        show emicas wink_up
        with persistent.charachange

        emi "That and I figured you'd make too much food so it wouldn't matter if I skipped breakfast."

        show meiko wink
        with persistent.charachange

        emm "Well, it's good to know that I'm predictable."

        show emicas grin_up
        with persistent.charachange

        "Emi nods enthusiastically, and conversation falls off again as we very nearly clear the table of anything edible. It is a testament to the sheer amount of food on offer that we don't finish everything."

        show emicas grin
        show meiko smile
        with shorttimeskip

        "I lean back in my chair with a sigh and thank Mrs. Ibarazaki for the food."

        show meiko happy
        with persistent.charachange

        emm "I'm glad you liked it, Hisao. Now, has Emi told you where we're going?"

        hi "Yeah, sort of. Is it far from here?"

        show emicas closedsmile
        with persistent.charachange

        emi "Not really, but we'll drive there to save time. It closes kind of early."

        "I nod in assent and stand up, ready to go."

        hi "Well then, shall we?"

        hide meiko
        with charaexit

        show bg at bgright
        show emicas awayfrown at center
        with charamovechangefaster

        "Mrs. Ibarazaki nods and leaves the room to grab her keys. Emi, I notice, has started to fidget nervously."

        hi "Second thoughts?"

        show emicas weaksmile
        with persistent.charachange

        "Emi smiles tightly at me and shrugs. She's fallen silent again, which probably means that I'm right, and she is starting to regret bringing me along."

        "Not that I blame her; she's done such a good job of shutting me out that I doubt it's easy to suddenly open up. Honestly, I'm worried that she's forcing it."

        "But she said while waiting for the bus that I'm not supposed to give her a chance to back out, and since I promised to go with her anyway, I suppose there's not much of a choice. I can't go back on my promise, and she can't go back on hers."

        "I just hope the both of us are up to it."

        show bg at center
        show emicas at twoleft
        with charamove

        show meiko happy at tworight
        with charaenter

        emm "We're off!"

        "Emi's mother blows through the dining room, collects the two of us, and heads out the door at a brisk pace. Now I know where her daughter gets it from."

        stop music fadeout 4.0

        scene bg city_graveyard
        with shorttimeskip

        "The car pulls up at the cemetery gates, and I feel Emi tense up beside me. I reach over and give her hand a comforting squeeze, which causes her to relax a little."

        "Emi's mother doesn't follow us, explaining that she prefers to visit the grave alone. Emi steps through the gates and looks back, as if to make sure I'm still there. We step into the cemetery."

        "I don't feel comfortable in cemeteries. Gravestones litter the ground, each one serving as a reminder that someone used to be alive and is no longer."

        "How many died young? How many were as old as I am now? When do I wind up with a marker of my own? How much longer do I have left?"

        "The concept of not waking up, not seeing Emi any more, is not a happy one. It frightens me, and I very nearly turn around and exit right then and there."

        "I don't want to go among dead people, I don't want to see their stones and think about who they were or what they could have been if they'd only had more time."

        "Then I look at the girl next to me, and my resolve returns. Emi's striding purposefully down the path, eyes clear, setting a pace that's very nearly a jog. The sooner we get there, I suspect she thinks, the better."

        show emicas weaksmile at center
        with charaenter

        emi "We're here."

        scene ev emi_grave:
            truecenter
            zoom 0.95
            easein 10.0 zoom 1.0
        with whiteout

        $ renpy.music.set_volume(0.4, 0.0, channel="music")
        play music music_friendship fadein 1.0

        "A gravestone, wholly unremarkable in everything except for the name etched upon it. The grass has grown up around the base."

        "Emi's eyes are riveted to the stone."

        scene bg city_graveyard
        show emicas neutral at center
        with locationchange

        $ renpy.music.set_volume(1.0, 20.0, channel="music")

        "After a few moments she turns around, looking surprisingly calm, yet solemn."

        show emicas awayfrown
        with persistent.charachange

        emi "Pink's not actually my favorite color, you know."

        hi "Er, what?"

        show emicas frown
        with persistent.charachange

        emi "I'm warming up to it."

        hi "Ah."

        show emicas neutral
        with persistent.charachange

        emi "People tend to think that pink's my favorite color. I think it's because I like strawberries, and even though those are red they just assume that pink's the right color for strawberries."

        emi "And that it's my favorite color. But it's not. I'm too polite to tell anyone otherwise, of course, and it's not the kind of thing worth getting worried about, but I'll bet even you thought pink was my favorite color."

        show emicas weaksmile_up
        with persistent.charachange

        emi "Blue. That's my favorite color. My mom and dad are the only two who know that, and now you do too."

        hi "Thanks for telling me, I think."

        show emicas closedsmile
        with persistent.charachange

        emi "You're welcome."

        "There's a pause as she considers what to say next, drawing a quick breath."

        show emicas neutral
        with persistent.charachange

        emi "I can't carry a tune to save my life. I can hum, but actually singing a song is something I've never been able to do. I don't mind, because I'm not a fan of karaoke anyway."

        hi "Well that's one potential date idea out the window."

        show emicas frown
        with persistent.charachange

        emi "People all think that I'm a really popular and friendly person, but I only have a few close friends. Probably because I keep everyone in the dark, but I think it's also because I hate the idea of losing a close friend."

        show emicas awayfrown
        with persistent.charachange

        emi "There aren't many people worth the risk."

        show emicas frown
        with persistent.charachange

        emi "I'm terrible at saying goodbye."

        emi "I sometimes think that I only run because it's what I used to do with my father."

        show emicas neutral
        with persistent.charachange

        emi "You're not my first boyfriend. I dated a guy for a long while during my second year at Yamaku, but in the end we broke up, because I didn't want to get closer to him. He couldn't live with that distance between us."

        "Her rate of speaking increases slightly, as if she's rushing towards a finish line."

        show emicas weaksmile
        with persistent.charachange

        emi "I'm actually one year older than you. Everybody thinks I'm younger because I'm short, but I had to skip one school year because of my accident."

        show emicas neutral
        with persistent.charachange

        emi "They initially thought I was paralyzed when they pulled me out of the wreckage. I'd lost my legs already, but they were afraid that I wouldn't even be able to use what was left of them."

        emi "After surgery, it was clear that their initial assessment was mistaken. I couldn't feel my legs because of shock. Short term paralysis due to the other trauma I'd experienced."

        emi "My recovery was one of the fastest they'd ever seen, or so they told me. I never found out if they were serious about that or if they told that to all the patients learning to walk again."

        show emicas awayfrown
        with persistent.charachange

        emi "I…"

        "She pauses, gathering herself for one last effort."

        show emicas sad
        with persistent.charachange

        emi "Eight years ago today, I lost my legs. And I lost my father as well."

        emi "He died on the way to the hospital. I didn't even get to go to the gravesite until two months later, and couldn't attend his funeral."

        hi "I'm so sorry."

        show emicas neutral
        with persistent.charachange

        emi "Don't be. That's what everyone always says, that they're sorry. I hate hearing that. Like anyone could have done anything to change what happened."

        show emicas frown
        with persistent.charachange

        emi "You know the best piece of advice I got? 'These things happen.' I don't even remember who said it, but I guess they didn't have anything better to say."

        show emicas sad
        with persistent.charachange

        emi "But it's true, you know? These things happen, and there's nothing you can do about it. They aren't necessarily planned, and they aren't always bad, and they aren't always good, but they are."

        emi "So I made the decision that I would live without worrying about the future. And to be sure that I never had to say goodbye again, I decided I wouldn't let people get close to me any more."

        emi "After all, they could be taken away at any time. And you know what?"

        "She laughs, a little bitterly."

        show emicas sad_up_close
        with characlose

        "Her eyes start to well up with tears, and I step forward to embrace her but she holds up a hand to stop me."

        emi "M'not finished."

        "A deep breath, and she continues."

        show emicas sad_close
        with characlose

        emi "It worked pretty well! Until I met you and saw that you were trying to adjust to stuff here, so I thought I'd help and then you were so nice and I couldn't help it, I just…"

        scene black
        show ev emi_cry_down at slow_out
        with whiteout

        "The tears are flowing now, and she accepts the embrace this time. The rest of her sentence is mumbled into my chest."

        emi "I tried not to fall for you, but I did. And then I tried to keep you at a distance, like with my first boyfriend, but I couldn't. But I've been so scared, because I don't want to lose you and I might anyway—"

        hi "Hey, I'm still around, right? And maybe I won't be forever, but don't you think it'll be fun while it lasts? Neither of us could survive the day, there could be a bus crash or something, but so long as I know that I've been with you, I don't think it matters."

        "A sudden thought strikes me, and I can't help laughing. My condition had me scared of dying so badly that I immediately seized on the opportunity Emi presented to improve my odds of living longer."

        "But without Emi, would there have been any motivation to keep up with my running? It hits me that Emi is the reason I want to go running every day, so I can spend as much time with her as possible. Emi looks up at me, confused."

        hi "We'll go on living until we stop. And when we stop living we'll be able to know that at least we've had time together, and I wouldn't have it any other way. Because I love you, Emi, and right now that's enough for me."

        scene bg city_graveyard
        show emicas weaksmile_close at center
        with locationchange

        "Emi smiles through her tears, and steps back from me."

        emi "You know, it's funny."

        hi "What is?"

        show emicas closedsmile_close
        with persistent.charachange

        emi "I thought that the best way to live in the moment was to do it alone. But now, I don't think I'd have it any other way either. I'm glad I met you, Hisao."

        hi "Well, these things happen."

        "Emi and I stay by the grave for a while, as Emi pays her respects to her father. When she's ready to go, we exit the graveyard side by side."

        stop music fadeout 15.0

        if _in_replay:
            return

    label .hooray_for_socks:
        scene bg school_gate_ss
        with shorttimeskip

        "Emi's mother drives us back to Yamaku. The trip back is very quiet."

        show emicas neutral_close_ss at center
        with charaenter

        "We wave goodbye as the car drives off, and I glance down at the girl leaning on my arm."

        hi "How are you feeling?"

        show emicas awayfrown_close_ss
        with persistent.charachange

        "Emi shrugs noncommittally."

        show emicas frown_close_ss
        with persistent.charachange

        emi "I'll be fine. Come on, let's go."

        scene bg school_dormext_full_ss
        with locationskip

        "We pause outside the girls' dorm and I turn to face Emi, ready to say goodbye."

        show emicas weaksmile_close_ss at center
        with charaenter

        emi "Why don't you come up for a while?"

        hi "Okay."

        scene bg school_girlsdormhall_ss
        with locationskip

        "The walk up to her room is in silence. I'm not sure why I supposed I'd be turned away at the door."

        "I guess I just assumed she'd want to be alone."

        "Her mom, the nurse, hell, everyone who knew the significance of today seemed to think it best to leave Emi alone."

        "But she took me into the graveyard with her. She told me the whole story of what happened on the day she lost her legs."

        "She wanted me around. The significance of this does not escape me."

        play sound sfx_dooropen

        "Emi opens the door and steps into her room, not even bothering to invite me in, holding the door for me expectantly."

        scene bg school_dormemi_ss at left
        with locationskip

        play sound sfx_doorclose

        "I step in, and the door swings shut behind me."

        show emicas weaksmile_close_ss at center
        with charaenter

        emi "Hey, can I ask you a favor?"

        hi "Sure. Can't guarantee I'll do it, but…"

        show emicas closedsmile_close_ss
        with persistent.charachange

        "Emi giggles and pulls me into a kiss that starts out soft but deepens into something almost desperate."

        show emicas smile_close_ss
        with persistent.charachange

        emi "Stay with me? Please?"

        "Her voice has dropped to a whisper, the question is barely audible over the sound of my own breathing."

        "There's something about the way that she asks that question, the hesitancy in it, the quiet voice, that makes me think she doesn't mean tonight."

        "No, she means exactly what she said. 'Stay with me.' Not 'tonight' or 'forever,' because both of us know there's no such thing as forever."

        "There's no time limit to her request, there's just the request."

        "The favor."

        "Can I do that?"

        "Can I stay with her?"

        hi "Of course."

        play music music_comfort fadein 4.0

        show bg at right
        show emicas closedsmile_close_ss at center
        with charamovechangefaster

        "We embrace again, Emi guiding me towards her bed, stepping backwards with care, until she sits down on the edge."

        hide emicas
        show eminude smile_close_ss at center
        with persistent.charachange

        "She's gotten my shirt off by this point, and I've similarly lifted hers over her head, bra and all. Her shorts come off just as quickly."

        "With practiced ease she removes her legs and pulls me onto the side of the bed with her, my hand coming around her smooth shoulder."

        hide eminude
        with persistent.charachange

        "I cast my gaze over her face, down her neck, following the line to the swell of her breasts before I lower my head, planting kisses across her chest, listening to her breath hitch as her hand slides further and further down my chest."

        "As I work my way back up to her neck, I can feel her hands working at my belt, now fumbling slightly with the buckle, now unbuttoning, now unzipping, until my pants fall to the floor."

        "Her panties are noticeably darkened in the right place, showing that my earlier ministrations have produced some results."

        "I step back quickly and shuck my boxers, and move back in as Emi reaches over into a drawer on her nightstand, removing a small foil package."

        "She tears it open with a quick jerk of her teeth and reaches down to apply the protection, which, as always, causes me to gasp a little."

        "Her expression suddenly changes as she takes the view of me in."

        show eminude evil_close_ss at center
        with charaenter

        emi "Wait a second… Are you still in your socks?"

        "I pause, and look down. Apparently, I am."

        hi "Er, yeah. Does that matter?"

        show eminude frown_close_ss
        with persistent.charachange

        emi "Take 'em off, it's weird if you still have them on."

        hi "You know, you've still got your socks on too."

        show eminude closedsmile_close_ss
        with persistent.charachange

        emi "Yes, but I don't have my legs on. So it doesn't count."

        "Unable to deny her logic and impatient to have the conversation over anyway, I quickly remove the offending items."

        "I'm so eager to get back at Emi that I practically jump on top of her, pushing her down playfully."

        scene evh emi_miss_closed
        with whiteout

        "Emi's giggling and squirming quickly ends, replaced by a happy sigh as I enter her. Breathing deeply as she savors the feeling, she spreads her arms to grab the sheets."

        "Her breath is in my ear as I begin moving, whispering words of encouragement, nipping at my neck, now at my mouth."

        "My hips hit the edge of the mattress, shaking the bed. A part of my brain briefly wonders if I should try to be quieter before succumbing to the waves of pleasure racing up my spine."

        scene evh emi_miss_open
        with charachangeev

        "Emi's stomach tenses as she grows closer to the edge, and as our bodies both begin to glisten with sweat time begins to become hazy."

        "The sound of my own breathing mingles with Emi's panting, and I ready myself for a final surge before surrendering to the rushing wave of climax."

        "Emi's body shudders, and she cries out, her fingers digging into my back as I too lose control of myself."

        "My back arches as I let myself go, feeling my body spasm as I orgasm."

        scene bg school_dormemi_ss at right
        with shorttimeskip

        "I collapse next to Emi, who almost immediately curls against me, smiling."

        "Mentally, I feel grateful that Emi keeps her nails short, otherwise I think she might have drawn blood."

        "I sit up briefly to dispose of the now-used condom and lay back down next to Emi, who's in turn taken care of cleaning herself off."

        "For a while, we lay in silence, savoring the feeling of being next to one another."

        "Emi is the first to speak."

        show eminude smile_close_ss at center
        with charaenter

        emi "Hey, Hisao."

        hi "Hmm?"

        show eminude closedsmile_close_ss
        with persistent.charachange

        emi "Thanks for coming with me today."

        "I smile and plant a kiss on her head."

        show eminude blush_close_ss
        with persistent.charachange

        hi "Of course. My pleasure."

        show eminude closedsmile_close_ss
        with persistent.charachange

        "Emi snuggles closer, and I can feel her breathing begin to slacken as she begins to drift off to sleep."

        "Just as she's about to fall asleep, she wakes up enough to mutter a single sentence."

        emi "I love you, Hisao."

        "Then she's out like a light, leaving me feeling like I'm on top of the world."

        "I draw the slumbering Emi as close as possible, pull the covers over us to keep the chill off, and fall asleep as happy as I've ever been."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .clean_teeth:
        scene black
        with dissolve

        scene bg school_dormemi
        with openeye

        "The morning light seems to reach further into Emi's room than it does into mine."

        "This results in my waking up earlier than I would have if I had gone back to my room last night, as had previously been our routine."

        "I did not realize it until this morning, but this is the first time we've actually spent the night together."

        play music music_twinkle fadein 1.0

        "A small movement from my partner's still-slumbering form causes me to look to the side."

        "Hair splayed across her face, Emi continues to sleep peacefully curled up next to me."

        "It's slightly weird seeing her without her trademark twintails, but it's also a look I could get used to."

        "The small size of the beds here necessitates her curling up, but I'm pretty sure she would have done so anyway."

        "The covers are nearly over her head, and I smile as an errant strand of hair causes her nose to twitch slightly."

        "Unable to help myself, I draw her a little closer, a move which she seems to think is a good idea."

        "Her steady breath raises a trail of goosebumps on my chest, but I don't mind."

        "I am no longer tired, but I do not feel a need to move from my current position."

        "Emi's warm body in repose against mine is far too comfortable to move."

        "I gaze up at the ceiling and consider how it is that we got to this point. We've been close for a while, but not this close."

        "It seems like only yesterday that she ran into me in the hallway and after apologizing decided to take an interest in my well-being."

        "But that grew into something else, which I at least was not expecting."

        "One thing is for certain: having found Emi, I will try as hard as I can not to lose her."

        "My morning musing is interrupted by further movement from Emi."

        "Her eyes flutter open, and she seems briefly confused by my presence in her bed as well as her current state of dress, which is nonexistent."

        scene ev emi_ending_smile
        with whiteout

        "Then she smiles happily and sits up, her face looking down at me."

        emi "Good morning, Hisao."

        hi "Hi. Sleep well?"

        emi "Yeah. Yeah, I did. Exhausting day yesterday, you know?"

        "I think back over yesterday's trip to the graveyard."

        hi "Yeah. Glad to hear you slept well."

        emi "How'd you sleep?"

        hi "Well enough, although you kept hogging the covers…"

        "This earns me a shove and a stuck-out tongue. I chuckle, and Emi giggles a little, and we fall quiet for a while."

        "I soak up the feeling of how right it all seems, waking up with Emi by me, crammed into a bed made for one person."

        "It's something I could get used to."

        emi "Hey, Hisao…"

        hi "Hmm?"

        emi "Thanks for sticking around."

        hi "No problem. Saved me the walk back anyway, right?"

        scene ev emi_ending_serious
        with charachangeev

        "This draws another giggle, but then Emi's expression turns serious again."

        emi "No, really. I kept trying to push you away, because I thought that was the right thing to do, and you stuck around through it all."

        emi "I haven't made any of this easy for you, but you stuck it out anyway."

        emi "So really, I mean it. Thank you."

        scene ev emi_ending_smile
        with charachangeev

        "She punctuates this by giving me a kiss, pulling back and looking at me with an expression of affection."

        "I reach up and ruffle her hair, smiling all the while. I'm stupidly lucky, I think. To have come through everything after my heart attack and to somehow have found this girl is nothing short of a miracle."

        hi "You're very welcome, Emi."

        "I couldn't bear the thought of giving you up."

        hi "I'll even continue to stick around, if you want."

        emi "I'd like that."

        "That settles it, then. I don't know how long my heart will keep working, and I don't even really know what I'll do after this year is over, apart from going to university."

        "As long as Emi's around, I think I'll be okay. I've managed to help her, and she's managed to help me. If we keep doing that, we'll be okay, I think."

        emi "So, Hisao."

        hi "Hmm?"

        scene ev emi_ending_glad
        with charachangeev

        emi "What do you want to do today?"
        

        $ ach("emigood_achieve")

        stop music fadeout 3.0

        if _in_replay:
            return

    return
