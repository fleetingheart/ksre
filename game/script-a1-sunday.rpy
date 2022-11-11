# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a1_sunday:
    if not force_route:
        $ force_route = FR_KENJI

    call timeskip

    label .dont_panic:
        scene black

        scene bg school_dormhisao
        with openeye

        play music music_daily fadein 4.0

        "The next day, I wake up feeling a little lightheaded. It's almost noon already."

        $ renpy.music.set_volume(1.0, 0.0, "ambient")

        "Sleeping late is fine, since it's a Sunday and there are no classes."

        "Not just a Sunday, though, but the festival as well."

        "From my window I can already see some people at the soba booth slinging noodles onto plates for people with a craving for low-quality food."

        "I throw back a handful of my morning meds and ponder how to spend the day."

        "There will be a few exams in the coming week, but I don't consider those as ominous as others, so I'm not as worried about them as I probably should be."

        "With no urgent obligations regarding education, I should be free to spend the day at the festival as I like."

        scene bg school_dormhallway
        with locationchange

        "Finishing my morning routine, I exit into the hallway, intending to go out and find something to eat."

        "Passing by his door, I decide to see what Kenji's up to today out of impulse."

        "I'm curious if he has any plans, since everyone is doing something."

        "Then again, I can picture him having built a soundproof shelter in his room."

        "Or possibly something like a fort, complete with 'No Girls Allowed' sign."

        "… and with the 'Girls' crossed out and 'body' crudely scrawled underneath it."

        stop music fadeout 2.0

        play sound sfx_doorknock2

        "Knocking on his door which is luckily devoid of any kind of sign, I hear again the unsettling clicking of at least ten locks being pulled back. The door opens up a crack."

        show kenji neutral:
            xpos 0.0 xanchor 0.3
            easein 0.5 xanchor 0.2
        with Dissolve(0.5)

        show kenji:
            xpos 0.0 xanchor 0.2

        ke "Who is it?"

        hi "You're supposed to ask that before you open the door."

        show kenji at center
        show bg at bgright
        with charamove

        play music music_kenji fadein 1.0

        ke "Oh, it's you. Damn, it's early."

        hi "It's not really that early."

        show kenji happy
        with charachange

        ke "What is it, man?"

        hi "Nothing, was just gonna ask what you're gonna do today."

        hi "Half the school is out there already."

        show kenji rage
        with charachange

        ke "Out where? Why?"

        hi "What?"

        ke "What what? Is today special? Why are they there? Who are?"

        show kenji tsun
        with charachange

        ke "I can hear them. It's loud… don't tell me… Has the invasion begun?"

        "He suddenly looks more alarmed."

        show kenji neutral
        with charachange

        ke "What day is it, man?"

        hi "Yeah I guess you can't see the big wooden booths outside, and people selling stuff…"

        ke "What the hell are you talking about? I have my curtains closed at all times to thwart the snipers."

        hi "Uhh, it's the festival. You know that… right?"

        show kenji tsun
        with charachange

        ke "Oh shit, that's today? Ah, damn. Ah… damn. Dammit."

        ke "I can't believe I forgot, I don't have my fort finished yet. This is bad."

        ke "This is going to be a very bad day… It's good you told me this, man. This is going to be a bad day."

        hi "Why?"

        show kenji neutral
        with charachange

        ke "Oh man, they're going to be everywhere. The people. Outside my window. Socializing!"

        "Kenji rubs his temples nervously, suddenly looking very ill."

        show kenji tsun
        with charachange

        ke "It's going to be loud as hell. Damn, and I was going to go out today, but now it's ruined, everything is ruined."

        ke "This is awful. This sucks. This sucks!"

        ke "What the hell, this really sucks. I can't go anywhere now. There's nowhere to run."

        "Kenji seems nervous. You could even say he's majorly freaking out."

        show kenji neutral
        with charachange

        ke "I can't believe this. So that's what today was."

        ke "Damn, and I couldn't even prepare for it."

        show kenji tsun
        with charachange

        ke "I couldn't even brace myself and now it's here and I can't do anything. You should have told me this earlier, dude. I mean, at least, I know, but… I could have known earlier! Imagine what I could have accomplished…"

        hi "Sorry. I thought you knew."

        hi "So I guess you're not going to do anything today?"

        hi "The weather is even good. Yesterday was really windy, so I thought today would be cold. It's not, though, so there's no reason to just stay inside. Yeah, you should check the festival out."

        "Kenji groans and covers his face with his hands."

        ke "Agh, no, no! I can't do it. They'll eat me alive out there, I know it."

        "That has to be a joke, but he said it with such a straight face. Relatively straight."

        show kenji happy
        with charachange

        ke "What are you going to do? We should hang out in here, you can help me build my fort. We might still make it if we work together."

        if _in_replay:
            return

    if force_route == FR_EMI:
        label .is_carnival:
            scene bg school_dormhallway at bgright
            show kenji happy at center

            hi "I wonder… I'm kinda hungry, but I made this deal that I try to take better care of myself. Be healthier, you know."

            hi "Dunno if I should steer clear of the takoyaki, or head straight in."

            show kenji tsun
            with charachange

            ke "Deal? Sounds ominous. So what are you getting in return?"

            hi "Nothing, I guess? It's not that kind of a deal."

            hi "You know Emi, from our year? We kinda agreed to watch each other's backs and…"

            show kenji rage
            with charachange

            ke "Aieeeeeeee!"

            "The shrill scream and the expression of abject terror in Kenji's face chill my blood. It's as if I told a Catholic priest I sold my soul to the devil."

            ke "Her! You sold your soul to the devil, and didn't get anything in return?"

            ke "What the hell is wrong with you, man?"

            ke "Do you know who you are dealing with?"

            ke "She's a public health danger. Do you know how many people she sends to the hospital monthly with her carefully placed flying tackles?"

            show kenji tsun
            with charachange

            ke "She's one of them! A key player in the vast conspiracy that aims for the complete submission of everything that is manly."

            ke "I can't believe what I'm hearing. I trusted in your judgment, man. I thought we were brothers."

            ke "You have to call it off before it's too late."

            ke "This festival too; it's just one of their ploys."

            call stranger_union

            show bg at bgright

            "It's kinda unsettling, and now I start to feel doubtful, myself."

            "Should I bother going?"

            "I've got a book I've been meaning to read."

            "Something about an underground postal system that may or may not exist."

            "It's short, too. I could have it finished in a day."

            "But would that be a good way to spend my time?"

            "Well, yeah. It definitely would be."

            "But I suppose that it would probably be a better idea to head outside."

            "See the festival."

            "Try to integrate with all the other sideshow acts."

            "Honestly, I should at least make an attempt to keep up the somewhat friendly personality I've had the past week."

            "Maybe get something to eat, my stomach suggests."

            "It's almost lunchtime… I could at least grab something from one of the stalls outside."

            play music music_soothing fadein 1.0
            play ambient sfx_crowd_outdoors fadein 1.0

            scene bg school_courtyard
            show crowd
            with locationskip

            "I'm soon outside, surrounded by various students and people who may or may not be their parents."

            "Every so often I catch a glimpse of someone who clearly just came up from town for the promise of a festival."

            "They're easy to spot."

            "The ones who can't stop staring, and behind their eyes you can tell they're thinking 'Now, what's wrong with {b}this{/b} one?'"

            "I almost want to yell at them."

            "But at the same time, can I deny that I've been doing the same thing all week?"

            "A wave of something like disgust sweeps over me; guilt for my own narrow-mindedness."

            "…"

            $ renpy.music.set_volume(0.6, 2.0, "ambient")

            scene bg school_stalls1
            with locationchange

            "I push the thoughts aside, concentrating on the pangs of hunger that burn my guts like a wildfire."

            "The scent of something fried leads me to the promised land, where I can get some lunch."

            stop music fadeout 0.6

            "I'm just getting my order when a loud voice interrupts me."

            show emi basic_annoyed:
                tworight
                easein 0.5 center
            with charaenter

            show emi at center

            emi "Hey, what the hell are you doing?"

            play music music_comedy fadein 0.5

            hi "Having break— er, lunch."

            show emi sad_annoyed
            with charachange

            emi "Breakfast?"

            show emi sad_angry
            with charachange

            emi "You mean you just got up?"

            hi "Er…"

            "Suddenly sleeping all morning feels like a crime."

            hi "No, I meant lunch… honest."

            "She's not buying it."

            hi "Brunch?"

            show emi basic_annoyed_close
            with characlose

            emi "That's not a healthy breakfast at all!"

            "She snatches my food out of my hand and glares at me."

            "What the hell is this girl doing?"

            hi "Hey, that's my breakfast!"

            show emi sad_annoyed_close
            with charachange

            emi "What happened to it being your lunch?"

            hi "That's my… whatever, it's my food!"

            "Emi places her hands on her hips and begins lecturing me."

            show emi basic_annoyed_close
            with charachange

            emi "Did you really forget your dietary plan already?"

            emi "You need to be more conscious of your health, Hisao!"

            show emi sad_angry_close
            with charachange

            emi "What about your heart?"

            hi "My heart's fine the way it is! Mostly."

            "All I get in response is a roll of the eyes."

            show emi basic_annoyed_close
            with charachange

            emi "I doubt that."

            show emi basic_closedgrin_close
            with charachange

            emi "You wouldn't be here if that was the case, would you?"

            "The girl's got a point, of course."

            "But I'm not about to concede it."

            hi "It's not that bad of a heart!"

            hi "Certainly it can handle a little grease now and again!"

            "Yeah, sure. And it handled a little running just fine, too."

            show emi basic_annoyed_close
            with charachange

            "Emi seems unconvinced."

            "Not surprising, as I haven't even managed to convince myself."

            emi "Maybe, but not if you're sleeping the day away all the time!"

            "A devious look suddenly crosses her face."

            show emi basic_grin_close
            with charachange

            emi "Of course, if you'd been following a routine from the beginning you wouldn't be in this situation…"

            stop music fadeout 6.0

            hi "Hey, I've had a pretty eventful week, you know!"

            hi "For example, I almost died! And there was a lot of meeting people, and then I was on a roof for a while…"

            show emi sad_annoyed_close
            with charachange

            emi "Which is no excuse for slacking off, you know."

            emi "A little near death experience is no excuse for skipping basic exercise."

            show emi basic_closedgrin_close
            with charachange

            emi "Like running in the mornings."

            "She nods, as if something important has just been decided."

            show emi basic_happy_close
            with charachange

            play music music_emi fadein 0.5

            emi "So it's settled, then!"

            show emi excited_proud_close
            with charachange

            emi "You've seen the error of your ways and are willing to adhere to my routine, right?"

            emi "I'll see you bright and early in the morning?"

            show emi excited_happy_close
            with charachange

            emi "We'll be running buddies?"

            hi "You know, you'd already convinced me yesterday that this was a good idea."

            hi "You don't need to convince me again."

            "Not that I did a good job of being convinced."

            "She's right about eating healthy, after all. And here I am ordering up something grossly unhealthy."

            "But delicious!"

            "There are more important things than deliciousness, aren't there?"

            "Like staying alive?"

            "If Emi weren't here browbeating me for my poor decisions, I'd probably…"

            "Hey, wait a second."

            "A sudden question springs to mind."

            hi "Hey, why the hell have you taken such an interest in my well-being?"

            show emi basic_closedgrin_close
            with charachange

            "Emi shrugs and grins at me."

            show emi basic_grin_close
            with charachange

            emi "You're the new guy."

            emi "I figure you don't have any friends yet, right?"

            show emi sad_grin_close
            with charachange

            emi "Besides, I've caused you trouble all week, right?"

            emi "I owe you for not getting angry."

            show emi basic_happy_close
            with charachange

            emi "And I told the nurse I would, anyway."

            "Uh… huh. Crazy little running girl wants to make me healthy."

            "Well, I suppose there are worse fates."

            hi "Okay, that sounds… fine."

            hi "Thanks for your concern."

            hi "Tomorrow morning, then?"

            stop music fadeout 1.0

            hide emi
            with charaexit

            "I figure that ends the conversation, so I turn to leave."

            emi "Not so fast!"

            play music music_running
            with vpunch

            "I feel a hand on my collar and in a second I've been yanked backwards."

            hi "Hey, no need to be so rough!"

            hi "What do you want now?"

            show emi sad_shy_close at center
            with charaenter

            "Emi looks almost wounded by my annoyed question."

            emi "Thought you could use the company."

            show emi basic_annoyed_close
            with charachange

            "Her eyes narrow."

            emi "Besides, you were just going to try sneaking some more of that fried crap, weren't you?"

            "Well, I wasn't going to, but now that she mentions it that would have been a really good idea."

            hi "I was not!"

            show emi sad_annoyed_close
            with charachange

            "Another glare."

            hi "Okay, maybe I was going to get a little…"

            "The glare continues."

            hi "Okay, a lot."

            "Jesus, I'm a danger to myself and others, aren't I?"

            "I get done agreeing that I need to be healthier, and then immediately start considering the next unhealthy habit that comes my way."

            show emi basic_closedgrin_close
            with charachange

            emi "I knew it! You can't be trusted."

            show emi basic_grin_close
            with charachange

            emi "Now I definitely have to stick with you."

            "This whole situation feels silly."

            "I can only imagine what passersby think of the sight of me being lectured by a tiny girl half my size."

            "Maybe I should just give up for now."

            hi "Fine, do what you like."

            "I sigh."

            "Might as well make the best of this."

            hi "What do you want to do?"

            show emi basic_confused_close
            with charachange

            "Emi thinks for a minute."

            emi "Well, I promised Rin I'd stop by her mural…"

            show emi basic_grin_close
            with charachange

            emi "So let's do that!"

            "I confess I'm slightly curious as to how her mural turned out myself, so again I consider there are worse fates."

            $ renpy.music.set_volume(1.0, 2.0, "ambient")

            scene bg school_courtyard
            show crowd
            with locationchange

            "I give a nod of assent and find myself almost dragged bodily through the crowd as Emi races to our destination."

            stop music fadeout 6.0
            stop ambient fadeout 2.0

            scene bg school_dormext_full at bgright
            with locationchange

            "By the time we reach the dorms, I can feel my heart pounding."

            "My heart shouldn't be pounding after just that."

            "I take a few deep breaths, willing myself to calm down."

            "I'm one of the most normal looking people in the school, but I still have to be here."

            "Sometimes I almost wish I'd lost a hand or something."

            "At least then it'd be obvious that I belong."

            "But instead I don't even look sick."

            "Even now, trying to catch my breath, I just look out of shape."

            "Emi looks back and notices my state of distress."

            show emi basic_hes:
                xpos 0.4 yanchor 0.5
                easein 0.5 center
            with charaenter

            show emi at center

            emi "You're not going to die on me, are you?"

            show emi basic_shock
            with charachange

            emi "Please don't!"

            show emi sad_depressed
            with charachange

            emi "It'll be all my fault, and I don't want to deal with that kind of guilt."

            emi "Besides, after the last time I really don't think I need to see that again, especially because the nurse will totally say it's all my fault."

            play music music_soothing fadein 8.0

            hi "N… nah, I'm fine."

            hi "Guess I need to start running after all."

            show emi basic_closedgrin
            with charachange

            emi "And you wanted to keep eating your greasy… whatever it was."

            show emi excited_proud
            with charachange

            emi "See? It's a good thing I found you, right?"

            "Yes it was."

            hi "Maybe."

            show emi basic_grin
            with charachange

            "Of course I don't add that I wouldn't be in this state if she hadn't dragged me across the festival grounds."

            "Further conversation is interrupted by the sudden appearance of Rin."

            show rin basic_absent:
                xpos 1.0 xanchor 0.5
                easein 1.0 xanchor 1.0
            with Dissolve(1.0)

            show rin:
                xpos 1.0 xanchor 1.0

            rin "Oh, it's you."

            show rin at tworight
            show emi at twoleft
            show bg at center
            with charamove

            show rin basic_awayabsent
            with charachange

            rin "Hello Emi."

            show emi basic_closedhappy
            with charachange

            emi "Hey Rin! I brought Hisao along because he was going to give himself a heart attack!"

            show rin basic_absent
            with charachange

            hi "I was not!"

            "My objection goes unnoticed."

            show emi basic_grin
            with charachange

            emi "We stopped by to see how the mural turned out!"

            "Rin nods slowly."

            show rin basic_awayabsent
            with charachange

            rin "Well, it's right there."

            show rin basic_deadpan
            with charachange

            rin "You can see it pretty clearly."

            "I find myself wondering how long Rin's been standing here in front of the mural."

            "Has anyone even stopped by to look at it?"

            "Are we the first ones?"

            "Obviously we're not the first to see it, of course."

            "I mean, it's pretty big."

            "You'd be hard-pressed not to see it."

            "At the same time, I don't think anyone's actually talked to Rin about it."

            "Anyone but us, that is."

            "I feel compelled to say something."

            hi "It looks pretty good."

            show rin negative_spaciness
            with charachange

            rin "I'm still not happy with how it turned out."

            rin "But I guess it'll do."

            "She seems almost resigned to it."

            "I'm not sure what she expected as a result, but I guess she didn't quite get there."

            scene bg mural:
                xalign 1.0
                warp acdc_warp 100.0 xalign 0.0
            with Dissolve(2.0)

            "We stand in front of the mural, taking it all in."

            "I try my best to concentrate on the composition of the thing."

            "It's actually fairly interesting."

            "The colors swoop and blend together, dragging me along with them."

            "There's a dreamlike quality to the whole thing that makes me almost feel sleepy."

            "I try hunting out some of the colors Emi and I grabbed for her."

            "Try as I might, I can't see any Prussian Blue."

            "Oh well."

            "I'm sure it's in there somewhere."

            scene bg school_dormext_full
            show rin basic_awayabsent at tworight
            show emi basic_closedgrin at twoleft
            with Dissolve(2.0)

            "My feet start to hurt, but Rin doesn't seem inclined to move on."

            "Emi speaks up."

            show emi basic_confused
            with charachange

            emi "Hey Rin, have you eaten?"

            show rin basic_deadpan
            with charachange

            rin "Of course. You can't survive otherwise."

            show emi basic_hes
            with charachange

            emi "What about in the past five hours?"

            show rin relaxed_nonchalant
            with charachange

            rin "Maybe. But I'm hungry again, so maybe that means I'm wrong."

            show emi basic_closedgrin
            with charachange

            "Emi grins and claps her hands together."

            show emi basic_grin
            with charachange

            emi "Good! Come get some food with us!"

            "Rin nods in assent."

            show rin basic_deadpannormal
            with charachange

            rin "Okay, but we should hurry before they notice I'm gone."

            "Somehow I don't think they'd care."

            "Whoever they are."

            stop music fadeout 3.0
            $ renpy.music.set_volume(0.6,0.0, "ambient")
            play ambient sfx_crowd_outdoors fadein 1.0

            scene bg school_stalls1:
                xalign 0.0 yalign 0.5
                warp acdc_warp 8.0 xalign 1.0
            with locationskip

            "As we head back to the food stalls, I cast a longing eye over the fried food."

            "No, I'd better not."

            "I'm pretty sure Emi wouldn't let me, anyway."

            stop ambient fadeout 1.0

            scene bg school_gardens
            show emi basic_closedgrin at twoleft
            show rin basic_awayabsent at tworight
            with locationchange

            play music music_ease fadein 9.0

            "We find a nice spot on the grass and sit down to eat our purchases."

            "Well, my purchases, anyway. Somehow I've wound up paying for all the food."

            "Surprisingly, my (unfried) food is pretty good."

            "Silence falls as Emi and I eat and Rin stares at… something or other, occasionally eating a bite or two of her food."

            "I finish my meal first, and lay back on the grass."

            "Emi glances up from her food."

            show emi basic_confused
            with charachange

            emi "Tired, Hisao?"

            hi "A little, I guess."

            show emi basic_annoyed
            with charachange

            emi "Well, don't oversleep or anything tomorrow morning."

            show emi excited_proud
            with charachange

            emi "We start our morning runs, remember?"

            "Actually, they'd slipped my mind."

            "I was actually just enjoying myself."

            "Wandering around the festival with these two has actually been fun."

            hi "Yeah, I'll set an alarm."

            show emi basic_annoyed
            with charachange

            emi "You'd better be there!"

            show emi basic_closedgrin
            with charachange

            emi "I'll get angry if you aren't!"

            hi "God forbid."

            show rin basic_lucid
            with charachange

            rin "I don't think God comes into it."

            show rin basic_deadpan
            with charachange

            rin "Unless there's some kind of freak accident and your alarm clock shorts out."

            show rin basic_deadpannormal
            with charachange

            rin "That might be a random act of God."

            show emi basic_grin
            with charachange

            emi "Well don't cause any random acts of God, then."

            "A plan forms itself in my mind."

            "It's a plan that makes me feel kind of guilty, but I throw it into execution anyway."

            "Dammit, I've earned a little fried food."

            "And anyway, I'm going to start running tomorrow, right?"

            "So the actual routine all starts then, not now."

            "Ergo, the dietary portion starts tomorrow too, ergo I can have something unhealthy today."

            "A sort of final farewell to all the stuff I used to eat with wild abandon before the hospital."

            hi "Actually, I suppose I should head back to my room."

            hi "I had some homework to do, and if I'm going to run in the morning I should make it an early night…"

            show emi basic_annoyed
            with charachange

            "Those narrowed eyes again."

            show emi sad_annoyed
            with charachange

            emi "You sure you're not just going to sneak off and buy some of that fried stuff over there?"

            hi "Nah, I'm too full to bother now."

            "I pat my stomach for emphasis."

            hi "Besides, you two have cleaned me out anyway."

            show emi basic_closedhappy
            with charachange

            "Emi giggles. It's a surprisingly pleasant sound."

            "Another pang of guilt."

            "She's got to know that I'm lying to her, doesn't she?"

            "Or is she just that trusting?"

            "I feel kind of like a monster."

            show emi excited_proud
            with charachange

            emi "All part of my master plan, Hisao."

            show emi basic_closedgrin
            with charachange

            emi "Well, I guess I'll see you tomorrow morning then."

            show emi basic_grin
            with charachange

            emi "Thanks for the food! And for keeping us company!"

            "And here I thought she was doing me a favor."

            show rin relaxed_surprised
            with charachange

            "Rin nods in agreement."

            rin "I won't say 'See you tomorrow' because that would be like predicting the future, and I'm pretty sure I can't do that."

            hi "…"

            hi "Okay."

            hi "Bye, you two."

            "I feel oddly glad that I decided to leave my room today."

            "Not a bad way to start my second week here, I suppose."

            stop music fadeout 9.0
            play ambient sfx_crowd_outdoors fadein 1.0

            scene bg school_stalls1
            with locationchange

            "Once I'm sure I'm out of Emi's line of sight, I make a beeline for the food stands and buy some cake."

            "At least it's not fried, right?"

            "That's slightly better than what I was planning to do."

            "I still feel a little bad about lying to Emi, though."

            "She really does seem concerned about my health."

            "I'll make it up to her somehow."

            "Better head back to my room."

            "Hey, I {b}do{/b} have work to do."

            stop ambient fadeout 1.0

            scene bg school_dormhisao
            with locationskip

            "My book waits for me, and I flop on to my bed and read through the fireworks display."

            $ renpy.music.set_volume(0.1,0.0, "ambient")
            play ambient sfx_cicadas fadein 2.0

            scene bg school_dormhisao_ni
            with Dissolve(2.0)

            "Eventually all the walking around (or more accurately, running around) catches up with me."

            "I really am out of shape."

            "Emi dragging me out in the morning to run might just be a good thing after all."

            "It's something to look forward to."

            stop ambient fadeout 2.0

            if _in_replay:
                return

    if force_route == FR_RIN:
        label .clouds_in_my_head:
            scene bg school_dormhallway at bgright
            show kenji happy at center

            hi "Well, I joined the art club so I guess I'll go with them."

            show kenji rage
            with charachange

            ke "You did what?"

            hi "I joined the art club."

            show kenji tsun
            with charachange

            ke "Man, that was a bad move. Really bad. You don't know what kind of girls there are in the art club. Troubled, angsty cuties who tear your heart out and eat it raw."

            "Well, I know one art club member, and I don't really see Rin suddenly becoming a psychotic murderer."

            hi "That seems unlikely."

            ke "Don't say that. Don't fool yourself. You have no idea what you are dealing with here, man. They are the worst kind."

            show kenji neutral
            with charachange

            ke "They drag you in with all this fancy-pantsy shit and when you least expect it, BAM!"

            hi "Bam what?"

            "Kenji seems slightly fazed at my skepticism, but not any less loony."

            show kenji tsun
            with charachange

            ke "It doesn't matter."

            ke "Tread carefully man, tread carefully."

            call stranger_union

            play ambient sfx_crowd_outdoors fadein 0.3
            play music music_soothing fadein 0.5

            scene bg school_dormext_full
            show crowd
            with locationskip

            "The happy hubbub of the crowd greets me as I push myself through the main door and step outside."

            "The school grounds were transformed into festival grounds over yesterday and this morning."

            "Colorful stands line at the main walkways from the main entrance to the school building."

            "Some people are still carrying stuff to and fro, but behind most counters are relaxed students who look like they are good to go."

            "Most of the other students have been up early to finish the preparations."

            "A feeling of guilt passes through me, but it soon goes away."

            "I'm just a lowly transfer student, after all."

            "Some visitors are already strolling around the grounds."

            "There are some young families with the perturbed parents trying to keep up with their overenthusiastic offspring…"

            "…a few students of our own accompanied by their parents…"

            "…and a lot of old and young people who are here for no reason I can imagine."

            play sound sfx_warningbell

            "The carillon bursts into life and the principal's squeaky voice announces the opening of the festival over the PA system."

            "Everyone applauds politely if a bit unenthusiastically."

            "A school festival… we didn't really have festivals at my old high school. It feels kind of old-fashioned, especially considering the school I came from, but it's still somewhat exciting."

            "A day off feels sweet after the first week of hard work, despite me lying on the hospital bed for four months prior to this."

            "I recall even wishing that I could go to math lessons during my stint at the hospital."

            "I can't remember the program for the festival, even though Mutou went through it during class just the other day."

            "I step off the dorm steps, intending to take a tour around the grounds to see all the stuff the others have set up, but I only make it down to the bottom of the stairs."

            stop ambient fadeout 1.0

            hide crowd
            show rin relaxed_boredom at tworight
            with charaenter

            "A few people are studying Rin's mural on the wall, while the artist herself is lounging on the sidelines, leaning against the wall and looking extremely bored and mildly under the weather."

            hi "Good morning."

            show rin relaxed_surprised
            with charachange

            rin "Hello."

            hi "How's it going?"

            show rin relaxed_nonchalant
            with charachange

            rin "Nowhere."

            rin "I'm stuck."

            hi "What do you mean stuck?"

            rin "I mean I can't walk stuck. I think my legs are out of order because of yesterday."

            hi "Does it hurt?"

            show rin relaxed_sleepy
            with charachange

            rin "It's hard to say. Maybe."

            "The strain of working on the mural was greater than she let me know. I thought it was just a bit of tired muscles or something. I mean to ask something further, but Rin swiftly moves on to another topic."

            show rin basic_awayabsent
            with charachange

            rin "Teacher's friends came by."

            show rin basic_absent
            with charachange

            rin "Then they headed into town for lunch and asked me to go. It was a good thing my legs hurt so much."

            hi "But you're stuck sitting there? That's not good."

            show rin basic_lucid
            with charachange

            rin "I'll just wait till I can walk again. It should be either sooner or later, if you think about it for a while."

            rin "Teacher was happy that I finished the mural."

            hi "He should be."

            show rin basic_awayabsent
            with charachange

            stop music fadeout 5.0

            rin "But I wonder if it's finished after all."

            hi "Oh?"

            show rin basic_deadpanupset
            with charachange

            rin "I thought yesterday that I had done everything, but now I'm not sure any more. I should paint more details. Maybe. Probably. It's very hard to decide."

            "Finished or not, the mural looks great in broad daylight."

            play music music_another fadein 2.0

            scene bg mural:
                xalign 0.05
            with Dissolve(2.0)

            "Various human body parts, repeated over and over in a wildly mutating, mostly disfigured variety are the main element."

            "They are rough-looking, as if thoughtlessly placed and rudimentarily painted, but a great deal of thought and care has gone into each and every one of them."

            show bg mural:
                xalign 0.25
            with charamove

            hi "Does this one have a frog growing out of his head?"

            rin "It's a goldfish."

            show bg mural:
                xalign 0.45
            with charamove

            hi "What's that?"

            rin "It's nothing."

            show bg mural:
                warp acdc_warp 25.0 xalign 0.6

            "Anyway…"

            "The wall is so wide I have to turn my neck from side to side to see the entire painting."

            "It's hard to consider it as a single piece. The elements don't seem to fit together, but I guess they do create some kind of a whole."

            "Abstract as it is, I have no idea what it's supposed to be portraying, but it looks nice. That's enough for me."

            "I settle myself next to Rin, leaning against the wall like she does."

            "The happy noises of the festival are becoming louder as more and more folks enter the grounds."

            "The dorms are far from the main attractions in the main building and the stands around the courtyard, so most visitors have not found their way here yet."

            show rin negative_spaciness_close at offscreenright
            with None

            show rin at tworight
            show bg mural:
                xalign 0.6
            with charamovecustom(3.0)

            "A somewhat bored expression settles on Rin's face, making her look detached from everything that's going around her."

            "She is being awfully quiet. I wonder if she's in pain."

            hi "So what did the art people say about your mural?"

            show rin basic_deadpannormal_close
            with charachangealways

            "My question wakes Rin from her daydreaming. She lazily turns her face towards me."

            show rin basic_deadpan_close
            with charachange

            rin "I'm not sure."

            show rin basic_awayabsent_close
            with charachange

            rin "I think they liked it? Maybe they did."

            hi "What about you? Are you happy with the mural? 'Cause I kind of participated, it'd be terrible if you were unhappy."

            "Rin tilts her head, biting her lower lip."

            show rin negative_sad_close
            with charachange

            rin "I think it came out decently. It's not bad but it's not good either. It just… is. I guess I'm all right at being empty-minded."

            hi "Can I ask something else? What does the painting really portray? I thought about it yesterday, when you said that it doesn't portray anything."

            hi "But that's a logical fallacy, isn't it? You can't make something out of nothing, not even art."

            show rin negative_annoyed_close
            with charachange

            "Rin frowns and turns her head back towards the clouds."

            rin "I don't know. I am not really good at explaining things. It's just a mural; there is nothing special to it. I said it already."

            "She sounds annoyed at my inquiries."

            rin "I didn't know what I'd paint, so I decided to paint just a mural."

            rin "It's a mural that portrays a mural."

            show rin basic_deadpancontemplation_close
            with charachange

            rin "No, wait. I just thought up a better way to say it: It portrays itself."

            show rin basic_deadpannormal_close
            with charachange

            rin "So… its muralness is at the maximum, at least as far as I can do, so if you think it has some meaning, I think that's the same as this one has."

            "That makes no sense."

            "Meaning… I feel the corners of my mouth turning upwards into a smile that's just a tiny bit bothered."

            stop music fadeout 5.0

            scene mural all
            with flash

            "I have never understood art in the deepest meaning of the word."

            "I get the basics, how art is supposed to be only a means for exchanging ideas and thoughts."

            scene bg mural:
                xalign 1.0
                warp acdc_warp 40.0 xalign 0.6
            with flash

            "However, I never learned how I should interpret a piece of art, to somehow divine what the artist intends to say through it."

            "I know it's not any special skill, but somehow, my brain never can connect art with anything else than what I see. All I see is a mural."

            "I can admire the technical skill, after all even I know the difference between bad art and mediocre art; mediocre art and good art."

            "But that's as far as I can go, so don't ask me about meanings, Rin."

            "Her reply sure made me reluctant to ask her about it any further either."

            hi "So what are you doing when you get on your feet?"

            play music music_happiness fadein 4.0

            scene bg mural:
                xalign 0.6
            show rin negative_spaciness_close at tworight
            with flash

            rin "Nothing."

            hi "Nothing? But there's the festival, don't you want to go have some fun?"

            show rin basic_absent_close
            with charachange

            rin "I'm fine like this."

            hi "You don't like socializing much, do you?"

            "I think I'm arguing more for her than for myself at this point. It's not that I'm particularly thrilled about the festival, either; just a bit curious to see what it's like, and that's about it."

            "Her answer is unsurprising."

            show rin basic_awayabsent_close
            with charachange

            rin "No, I don't."

            hi "I guess… me neither, in the end."

            show rin basic_deadpan_close
            with charachange

            rin "You should go if you want to."

            hi "I know, but I can keep you company. I'm not used to all this just yet, so it's okay to take it easy."

            hi "I can leave though, if you want to be alone."

            show rin basic_deadpannormal_close
            with charachange

            rin "I like it if you are here."

            "We circle around each other with words, but eventually end up somewhere. Her saying that makes me feel oddly happy, so I stay."

            "Her presence is something I like too. The odd, warm aura of serenity that she seems to emanate makes it comfortable to be silent. I really like that."

            "We watch people walk by, the two of us silent, everyone else chattering happily among themselves."

            "Students are leading their families to the dorms to show their rooms. They pass us and the mural, maybe glance at it once or twice."

            "I pay less attention to them, and more to my companion, trying to figure my way past her cryptic, unreadable wall of a face."

            show rin basic_awayabsent_close
            with charachangealways

            show rin basic_absent_close
            with charachangealways

            show rin basic_awayabsent_close
            with charachangealways

            "Rin's eyes flicker restlessly from one person to another as they walk by."

            "Is she waiting for people to stop at the mural, maybe secretly hoping someone would comment on it?"

            "I don't think anyone would assume she was the artist. We're just sitting here like a pair of hobos, after all, and she doesn't even have hands."

            "I wonder if it's even in Rin's style to fish for compliments. She seems so aloof."

            "More people walk by, some of them pointing their fingers at the mural, exchanging words that I can't make out. Someone drops a snow cone on his shoe. Too bad for him."

            hi "Everyone seems to like it."

            "I suggest it tentatively, throwing a topic in the stale summer air separating us."

            "Rin doesn't answer right away, but by now I am mostly used to her occasional slowness when she must talk. It's like she takes great care picking her words, which is really unbelievable when you consider the jumble that comes out of her mouth."

            show rin basic_lucid_close
            with charachange

            rin "I wanted to make it so that you can just look at it without thinking. Then I realized that it doesn't make any sense. So it became something like a mix of this and that."

            show rin negative_spaciness_close
            with charachange

            rin "From far away, it looks like someone vomited a herd of butterflies on the wall. Which is exactly what that obnoxious president person didn't want. Is that word that?"

            hi "What word?"

            show rin basic_deadpannormal_close
            with charachange

            rin "That. What is the word for more than one butterfly?"

            hi "Butterflies?"

            show rin basic_deadpanupset_close
            with charachange

            rin "No, like a herd, or a school, or a heap."

            hi "Oh. I don't know. A flock maybe?"

            rin "Maybe people like butterfly vomit."

            show rin negative_confused_close
            with charachange

            "Rin looks at the mural, looking surprisingly unhappy."

            rin "The middle could be better."

            show rin negative_annoyed_close
            with charachange

            rin "Usually I like in-betweens, but this was a pain in my butt. Not literally of course… then again I did get that too. I guess it was literally after all."

            hi "Don't be so critical of yourself."

            show rin basic_deadpannormal_close
            with charachange

            "She looks at me funnily, but shuts up."

            scene bg school_dormext_full at bgright
            with locationchange

            "At about this point I start thinking if I should really leave and do something more constructive with my Sunday."

            "This is the pinnacle of social failure. A whole free day, a festival right outside my doorstep, and what do I do?"

            "Sit here with Rin; two bystanders with nothing to do except to think what a pity it is to be just a bystander."

            "Even realizing how pitiful it is, I don't do anything. I don't stand up and take off for a day of fun."

            stop music fadeout 5.0

            play sound sfx_rustling

            centered "*shuffle shuffle*"

            "…"

            centered "*fidget*"

            play sound sfx_rustling

            centered "*shuffle*"

            "…"

            scene bg mural:
                xalign 0.6
            show rin negative_annoyed_close at tworight
            with locationchange

            "Rin is shuffling about restlessly, constantly swinging one leg over the other knee and then back again."

            "She has a very irritated look on her face."

            hi "Is something wrong?"

            show rin basic_deadpanupset_close
            with charachange

            rin "Yes. No. Yes."

            scene bg school_dormext_full at bgright
            show rin basic_deadpanupset:
                tworight
                yanchor 0.8
                easein 0.5 tworight
            with locationchange

            show rin at tworight

            "She suddenly hops up on her feet. It's surprising, I thought she was still rendered immobile but apparently that's not the case."

            show rin negative_confused
            with charachange

            rin "I have to go find Emi or someone, I need some help with something."

            hi "I can help you."

            show rin relaxed_nonchalant
            with charachange

            rin "No, it's okay. One of us has to stay here in case something happens."

            hi "Don't be ridiculous. Nothing even remotely interesting has happened since I came here except that one guy who dropped a snow cone on his foot. Let me help you, since I'm bored."

            hi "So what is it?"

            show rin negative_annoyed
            with charachange

            "Rin's lips flatten tightly against each other into an almost perfectly horizontal line."

            show rin basic_lucid
            with charachange

            "She closes her eyes and draws in a deep breath."

            "When she opens her eyelids the frighteningly stern look in her dark eyes takes me aback."

            play music music_rin fadein 0.5

            show rin negative_angry
            with charachange

            rin "Hisao, you might not want to hear this or maybe you do, I don't know, but it doesn't matter and even if it did you are not leaving me any choice."

            rin "I'm having my period and I need some help regarding that. However, I don't feel that our relationship is yet on the level where I could allow you to pull my underwear down in the girls' toilet even if you offer to."

            rin "That's why you should stay here while I go and look for Emi."

            "As blood rushes to my cheeks like the rising tide my brains try to desperately search for an answer, but the only thing I can think of is how that was the most coherent thing I have heard coming out of Rin's mouth during these four days I've known her."

            hi "Yes."

            hide rin
            with charaexit

            stop music fadeout 4.0

            "Not wanting to meet Rin's eyes, I turn my face aside, pretending I'm looking at someone's parents."

            "From the corner of my eye I see Rin turning on her heel and walking off without further ado."

            "I feel like going to hide under some rock."

            "I wonder how long Rin will be gone… or if she will return at all."

            scene bg mural:
                xalign 0.6
            with shorttimeskip

            play music music_dreamy fadein 3.0

            "She does return eventually, appearing seemingly out of nowhere and sitting back to where she was, next to my place."

            show rin basic_deadpannormal_close:
                xpos 0.8 xanchor 0.5
                easein 1.0 tworight
            with Dissolve(1.0)

            show rin at tworight

            rin "I'm back."

            "She says it flatly, like my blunder never happened. I'd prefer to forget the whole matter as well, so I keep quiet."

            scene bg mural_ss:
                xalign 0.6
            show rin basic_deadpannormal_close_ss at tworight
            show rin_shadow basic behind rin:
                tworight
                yanchor 0.85
                easein 3.0 xpos 0.8 yanchor 0.9
            with Dissolve(3.0)

            "Time passes in standstill, the sun gleams from high above the main building. It hits me directly in the eyes, but I just squint instead of moving."

            "In a bit it becomes painful to keep my eyes open just a little, and my temples start aching."

            hi "My head hurts. I think this day gave me a headache, can you believe it?"

            show rin basic_deadpan_close_ss
            with charachange

            rin "Are you hungry?"

            hi "How is that related to headache?"

            show rin basic_deadpansurprised_close_ss
            with charachange

            rin "It's not. I ask because I am."

            "…"

            "Her oblivious seriousness melts my irritation with its ridiculousness, and I find the corners of my mouth turning slightly upwards again."

            hi "You know what? So am I."

            hi "I'll go get some food for us. What do you want? My treat."

            show rin basic_lucid_close_ss
            with charachange

            rin "Doesn't matter."

            show rin basic_deadpannormal_close_ss
            with shorttimeskip

            "Returning with the food, I give one portion to Rin, taking the other for myself and we dig in without a word."

            show rin negative_spaciness_close_ss
            show rin_shadow negative:
                xpos 0.8 xanchor 0.6 ypos 1.0 yanchor 0.9
            with charachange

            "Rin looks upwards, fork hanging out the corner of her mouth."

            rin "What are clouds? I always thought they were thoughts of the sky or something like that. Because you can't touch them."

            hi "You thought like that when you were a kid?"

            rin "No, last week."

            rin "Maybe because sometimes my thoughts feel like clouds. Fluffy and white and slow."

            rin "Like the sky was in my mind. Like my mind was the sky."

            hi "The sky of your mind?"

            rin "Close your eyes and think of sky. You won't be able to think of anything else until you stop."

            scene black
            with shuteye

            "I try it. It works. Magic?"

            scene bg mural_ss:
                xalign 0.6
            show rin basic_deadpannormal_close_ss at tworight
            show rin_shadow basic behind rin:
                xpos 0.8 xanchor 0.5 ypos 1.0 yanchor 0.9
            with openeye

            "Opening my eyes, I see Rin studying me with her eyes. It feels uncomfortable because she doesn't say anything. I turn away."

            scene bg misc_sky_ss:
                xalign 0.0
                warp acdc_warp 20.0 xalign 1.0
            with locationchange

            hi "Clouds are water. Evaporated water."

            hi "You know they say that almost all of the water in the world will at some point of its existence be a part of a cloud."

            hi "Every drop of tears and blood and sweat that comes out of you, it'll be a cloud. All the water inside your body too, it goes up there some time after you die. It might take a while though."

            rin "Your explanation is better than any of mine."

            hi "Because it's true."

            rin "That must be it."

            "I carry on eating the food before it gets cold."

            "The wall offers a bit of blessed shade as the sun revolves around the dome of the sky."

            "But the afternoon is already slowly making way for the evening so our lunch becomes more of a dinner. Or whatever the word is for an irregular meal like this."

            "Despite what I decide to call it, it certainly hits the spot. I haven't eaten a bit since forever."

            "…"

            "My appetite filled, I let out a satisfied sigh. Rin hasn't eaten all of hers but seems to be done with her food as well."

            "I lean back, taking in the atmosphere. The crowd has thinned already, but the activities are still going. Everyone seems to be enjoying themselves."

            "And why not? It's warm, the kind of perfect summer day when it's hot but not too hot for comfort."

            "The sun will set soon. Time really has flown by."

            scene bg mural_ss:
                xalign 0.6
            show rin basic_deadpannormal_close_ss at tworight
            show rin_shadow basic behind rin:
                xpos 0.8 xanchor 0.5 ypos 1.0 yanchor 0.9
            with locationchange

            hi "We've been sitting here for six hours."

            show rin basic_deadpansurprised_close_ss
            with charachange

            rin "Yes we have."

            show rin basic_deadpancontemplation_close_ss
            with charachange

            rin "Do you want to do something else now?"

            hi "No, not really."

            show rin basic_deadpannormal_close_ss
            with charachange

            rin "Me neither."

            show rin basic_lucid_close_ss
            with charachange

            "She adjusts her position and leans against the wall, and I follow her lead, relaxing my own body."

            "For minutes on end, we sit there without saying a word."

            "I'm trying to feel Rin's mood from her demeanor, the tension of her muscles, the tiny expressions fleeting on her face. It's no use. She's unreadable as always."

            $ renpy.music.set_volume(0.5, 0.0, "ambient")
            play music sfx_crowd_outdoors channel 6 fadein 1.0

            scene bg school_dormext_full_ss
            show crowd_ss
            with locationchange

            "The crowd swells to and fro, people happily chattering with each other. Very few people pay real attention to the mural, and even less to us."

            "I fiddle with a few odd pebbles absentmindedly."

            "The act of doing something just for the sake of doing something, the pinnacle of idleness."

            "Inch by inch, the sun creeps lower and lower towards the treeline, changing the color of the sky close to the horizon from golden yellow to orange and red as the moment of sunset draws near."

            "I feel like my stomach is filled with lead after eating so heavily, but the brick wall feels surprisingly comfortable against my back."

            "I try to fight against the drowsy feeling that is overwhelming me, to no avail."

            scene black
            with shuteye

            stop music fadeout 4.0
            $ renpy.music.stop(channel=6, fadeout=2.0)

            pause 4.0

            $ renpy.music.set_volume(1.0, 0.2, "ambient")
            play ambient sfx_fireworks fadein 1.0

            scene bg misc_sky_ni
            with openeye

            "I wake up with a start."

            "A low boom reverberates through the school grounds. Afterimages of bright sparks flash through my vision like stars."

            "Something rises towards the skies from the direction of the sports field."

            "A tail of fire trails behind it until a burst of red and yellow flame lights the sky high above the school with another loud boom."

            show fireworks
            with dissolve

            "Fireworks."

            "The sudden flash of light against the canvas of the night sky awakens me to realize that it's actually dark already."

            "How long did I sleep? I feel groggy and can't feel my right arm."

            "As I attempt to flex it, I realize why."

            play music music_twinkle fadein 1.0

            show rin basic_lucid_close_ni:
                xpos 1.0 ypos 1.1 xanchor 0.5 yanchor 1.0
                easein 1.0 xpos 0.9
            with Dissolve(1.0)

            show rin:
                xpos 0.9 ypos 1.1 xanchor 0.5 yanchor 1.0

            "Rin is leaning heavily against my shoulder, almost falling on my lap."

            "She is fast asleep, not even fazed by the fireworks."

            "Her mouth is slightly open and her eyes are peacefully closed. A sleeping, child-like face of the innocent."

            "I shake Rin gently with my free arm, trying to wake her up or failing that, move her so that my other arm is liberated from its pinch."

            "Rin's face twitches and her eyelids shut tighter, as if to resist against waking up."

            show rin basic_deadpanupset_close_ni
            with charachange

            "She gradually opens her eyes but keeps them half-closed, letting the light from the fireworks sneak just past her eyelashes so that her green irises mirror the bright flashes of the explosions, then looks up at me and frowns."

            show rin basic_deadpan_close_ni
            with charachange

            rin "Just a while longer, okay?"

            "Rin's voice is drowsy and slow, leaving her almost unintelligibly muttered words hanging lazily in the air."

            "It seems she is not entirely aware of the situation."

            show rin basic_lucid_close_ni
            with charachange

            "Rin's head drops back on my shoulder as she leans against me with all her weight."

            "She snuggles against my side, trying to make herself comfortable but making me feel very uncomfortable at the same time."

            "I become intensely, almost painfully aware of Rin's warm body and the deep, peaceful movement of her chest against my arm, her breathing soon returning to the even rhythm."

            "I can't help admiring her gift for sleeping, or the ease of mind of hers to use someone she has known for less than a week as a pillow."

            "The rockets rise up to the sky one at a time, breaking into flowers of red, green and gold, accompanied by the oohs and aahs of the audience."

            "I try to push Rin's disconcerting proximity out of my mind, for what can I do about it? I just hope her short while really is that."

            "One by one, the glittery bursts are born and die in a blink of an eye, coloring the dark night sky into a constantly changing abstract painting."

            "I listen to the low booms of the explosions and Rin's quiet breathing, trying to clear my own head of the post-awakening disorientation."

            "Thankfully, just a while longer really proves to be just a while, as Rin stirs from her slumber and wakes up again before the fireworks are over."

            show rin relaxed_sleepy_close_ni
            with charachange

            rin "I fell asleep."

            show rin basic_awayabsent_close_ni
            with charachangealways

            show rin basic_lucid_close_ni
            with charachangealways

            show rin basic_awayabsent_close_ni
            with charachangealways

            "She finally opens her eyes completely and blinks a few times."

            hi "You fell asleep on top of me. Twice."

            show rin basic_absent_close_ni
            with charachange

            rin "You didn't like it?"

            hi "Err…, well…"

            show rin basic_absent_close_ni:
                ease 1.0 ypos 1.0

            "Despite the inconclusive stammering, Rin sits upright, drawing herself away from me."

            hi "Well, you are heavy."

            "It's a lie, she weighs next to nothing, but I have to get a jab back at her, even if it's under the belt. My mock protest fails to draw any reaction as Rin's attention is drawn upwards, to the flashes of the fireworks."

            show rin negative_spaciness_close_ni:
                xpos 0.9 xanchor 0.5 xpos 1.0 yanchor 1.0
            with charachange

            "She seems hypnotized by the colorful play of the explosions."

            "A slight tingling sensation goes up and down in my arm as blood starts to circulate again. It's unpleasant but it helps me to get rid of this dizzy feeling."

            "More and more rockets rise up to the sky, the bright colors of their explosions reflecting from the clouds."

            "Both of us stare at the fireworks fixedly through the canopy of the trees, enthralled by the show."

            "We would get a vastly better view of the sky if we moved even a couple of yards, but neither of us bothers to even suggest it."

            show rin negative_worried_close_ni
            with charachange

            rin "I really do like fireworks, even though looking at them makes me feel kinda sad, I think. It's like they want you to look at them so bad so they are loud and bright, but when someone looks, they are already gone."

            show rin negative_sad_close_ni
            with charachange

            rin "It's like they were not even real."

            "…"

            hi "They are real, I can tell you that."

            hi "All of this is… real, you know?"

            hi "If you think about it, nothing really lasts for long. Even something like my life or yours is just a blink of an eye in the history of everything, like one of those rockets. Poof, and we're gone."

            hi "But we're here, aren't we?"

            "Yeah, this is reality. Rin, sitting next to me, the loud bangs of the fireworks, the vast, unlimited sky. These things are definitely real, even though they won't stay here forever."

            "I feel warm inside, and I wonder if it's because Rin is so close to me or just the feeling of being alive."

            show rin negative_spaciness_close_ni
            with charachange

            rin "I don't really know what I should say next."

            hi "It's all right… maybe I'm just talking to myself."

            hi "But you know, fireworks are pretty… but in the end isn't it somehow silly to spend so much money on a fraction of a second worth of pretty sparkles?"

            show rin relaxed_doubt_close_ni at tworight
            with charamovechangefaster

            "Rin rips her gaze off the still ongoing spectacle and leans backwards, looking at me with a repulsed face."

            rin "Wow, I never expected you to be such a cynic."

            hi "Cynic is a pretty harsh word. Rather than that, I think of myself as a realist."

            show rin relaxed_surprised_close_ni at tworight
            with charachange

            rin "Isn't a realist just the word for what a cynic calls himself?"

            stop ambient fadeout 1.0
            hide fireworks
            with dissolve

            "The final rocket goes out with a bang of silver and blue, leaving the grounds eerily silent for a moment until the crowd starts moving towards the main gate like a cattle herd."

            "Wisps of gray smoke drift towards the dorms from the sports field. The pungent, sulfurous smell of gunpowder it carries along feels like it sticks to my hair and clothes."

            hi "Was that it?"

            show rin negative_spaciness_close_ni
            with charachange

            rin "I think so."

            scene bg school_dormext_full_ni
            with locationchange

            "I stand up and stretch my sore back. Sleeping against a brick wall wasn't such a good idea after all."

            show rin negative_spaciness_ni:
                tworight
                yanchor 0.8
                easein 1.0 tworight
            with Dissolve(1.0)

            show rin basic_absent_ni at tworight
            with charachange

            "Rin stands up as well and turns to face me, with an expectant gaze on her tired features."

            "Although she seems to have trouble focusing her eyes, she is looking straight at me, something I feel has not occurred too often in the past week."

            hi "Umm…so…"

            "I suddenly realize we have been almost on a date here, as if by accident. Even if we did nothing."

            "But it wasn't… so why blood is rushing to my cheeks and my speech stammering?"

            "I don't know what I should say, especially since it seems Rin is waiting for me to say something, but luckily she solves my problem for me."

            show rin basic_deadpannormal_ni
            with charachange

            rin "Good night, Hisao."

            hide rin
            with charaexit

            "She gives me one more lingering look, measuring me from tip to toe, turns around on her heel and skips off, disappearing into the crowd."

            stop music fadeout 7.0

            "…"

            hi "Okay… Good night."

            "I'm left standing there, giving my response to the cooling night air."

            "Sigh."

            "The festival turned out to be nothing like I expected."

            "I ended up spending all day in one spot with Rin, even though neither of us agreed on nor suggested that we do anything."

            "I just didn't have anything better to do and evidently, neither did she."

            "Rin's warmth lingers for a while longer in my body before disappearing into the falling night."

            if _in_replay:
                return

    if force_route == FR_LILLY:
        label .promise_of_time:
            call stranger_lilly_and_hanako

            call stranger_union

            call lilly_and_hanako_union

            stop music fadeout 4.0

            "…Right. I know what I'll do. Even if it's just one person, I'll make the festival more enjoyable for her."

            "As I place the bowl on the counter, I call out to Lilly."

            show lilly basic_smile at center
            with charaenter

            li "Ah, Hisao. You brought it back?"

            hi "Yeah, here."

            hide lilly
            with charaexit

            "I slide it into her hands, and she takes it over to someone who is apparently on cleaning duty. Considering that I didn't see them here before, it's probably a penalty for their tardiness."

            hi "Hey, Lilly?"

            show lilly basic_smileclosed
            with charaenter

            "She perks up and returns to the counter as she hears my voice again, realizing that I'm still here."

            hi "Want to go see some more of the festival?"

            play music music_another fadein 0.5

            show lilly basic_pout
            with charachange

            "She puffs her cheeks disapprovingly. It looks kind of cute, and in complete contradiction to her usually reserved nature."

            "It takes a few seconds for me to get what she's taking issue with. Whoops."

            hi "Ah… um, I didn't mean to…"

            show lilly basic_giggle
            with charachange

            "Lilly giggles at me, exposing her teasing for what it is."

            li "You're still not used to the school, are you?"

            "She got me."

            show lilly basic_reminisce
            with charachange

            li "Still… I kind of need to stay with our stall. It's taken until just now to even get everything unpacked."

            "I guess her reluctance shouldn't overly surprise me, considering how much work she's put into this."

            hi "Everything seems to be running fine now, though. Besides, you've got extra help on hand, anyway."

            show lilly basic_surprised
            with charachange

            "A boy in the middle of cooking some soba noodles turns towards us, grinning."

            "Student" "Go on Lils, you've earned yourself a break. We can hold down the fort, for now."

            show lilly basic_displeased
            with charachange

            li "If you say it's okay, then I suppose so…"

            show lilly basic_reminisce
            with charachange

            li "But, if you need any help—"

            "Student" "Then we'll call you. Go on, we'll be fine."

            hide lilly
            with charaexit

            "Lilly finally gives up her resistance as he waves a spatula at her. She feels her way around the back of the stall, and picks up her cane on the way."

            "I guess the first thing we should do is look for Hanako. Lilly seems kind of worried about her, and I doubt she'd be the kind of person to enjoy milling about in crowds like this, all alone."

            hi "So, I guess we should search for Hanako. Where to, first?"

            show lilly cane_reminisce
            with charaenter

            li "Hmm…"

            "The both of us go quiet for a moment to think."

            hi "Maybe she's in her dorm room?"

            li "I doubt it. She doesn't keep too many things in there, so she'd have nothing to do."

            show lilly cane_satisfied
            with charachange

            li "…Ah! The library?"

            "As good a place as any to search for an avid reader, I suppose."

            hi "The library it is. We'll check there first, then."

            $ renpy.music.set_volume(0.2, 1.0, channel="ambient")

            scene bg school_lobby
            with locationskip

            "Aside from the muffled sounds of the crowd seeping in from outside, the inside of the school seems almost deserted."

            "In order to make sure everyone had enough room, I guess all the events were organized to be held outside, on school grounds. They're definitely quite large, by any other school's standards."

            show lilly cane_smileclosed at center
            with charaenter

            li "It's nice and quiet in here, isn't it?"

            hi "Yeah. Much nicer than the hustle and bustle outside."

            stop ambient fadeout 3.0

            scene bg school_staircase2
            with locationchange

            "We take our time and slowly walk through the first floor of the school, eventually reaching the stairs to the second floor."

            scene bg school_hallway2
            show lilly cane_smileclosed at center
            with locationchange

            "I can't help but notice how Lilly anticipates every door and obstacle, her cane remaining still and her hand skating along the hallway railings."

            hi "You really know the school well, don't you?"

            show lilly cane_smile
            with charaenter

            "She smiles and nods straight ahead."

            li "I've been here for a few years now, so I know where everything is."

            show lilly cane_sad
            with charachange

            li "The dorms still trip me up though, sometimes. I haven't been there as long, and they're not as well laid-out as the main building."

            li "If I'm remembering right, they used to be unused buildings before being renovated and used as dormitories."

            "That explains why the male and female dorms looked different from the outside, and why their rooms seem kind of unusual for sleeping quarters."

            "I'd assumed she'd been living in the dormitories since she began attending the school, but now I'm reminded of what she said yesterday."

            hi "That's right, you mentioned that before."

            hi "I'd assumed that most of the students here lived in the dormitories once they enrolled. A lot of them seem to, in any case."

            show lilly cane_reminisce
            with charachange

            "Lilly's expression becomes somewhat harder to read, my questioning evidently touching on a delicate point."

            li "Well… How should I say…"

            show lilly cane_weaksmile
            with charachange

            li "Everyone… has their reasons."

            "Something tells me that one of those with 'reasons' is Hanako, hence her tiptoeing around the answer. My own predicament is yet another such case."

            "I guess it's a choice everyone here would have to make for themselves… or, in my instance, have made for them."

            hi "It can't be helped, I suppose. At least Yamaku itself seems like a nice place."

            show lilly cane_smile
            with charachange

            li "It's good to hear you say that. I'd thought you were coming to dislike it."

            hi "What about you, though?"

            show lilly cane_surprised
            with charachange

            "My reversal of Lilly's statement takes her by surprise."

            li "I've been here for a while, so…"

            hi "It's not that. You just seemed pretty depressed about Akira."

            show lilly cane_smileclosed
            with charachange

            li "Hmm~"

            hi "What's with that look?"

            show lilly cane_smile
            with charachange

            li "Akira's taken. Sorry, Hisao."

            "Lilly never sees how fast my palm meets my face at her sly accusation."

            hi "Hey, I was worried about you. That's no way to respond to concern."

            show lilly cane_cheerful
            with charachange

            "While she gives an amused grin, we round the corner of the hallway and enter the library."

            scene ev hana_library_read_std
            with locationskip

            "As we do so, it isn't hard to spot Hanako, considering that the room is completely devoid of anyone else."

            scene bg school_library
            with locationchange

            "Given that there are no staff around, I guess there's no need to heed the usual library rules. I call out to her."

            hi "Hey, Hanako."

            show lilly cane_surprised
            with charaenter

            li "Hanako is here?"

            "As she hears our voices, Hanako's head flicks up from behind a book, probably the same one she'd been reading on Friday."

            show lilly at twoleft
            show bg at bgleft
            with charamove

            show lilly cane_smile
            show hanako basic_normal at tworight
            with charaenter

            ha "Hisao… Lilly?"

            hi "Just thought we'd drop by. Lilly just managed to escape from the noodle stall, with a little help."

            show lilly cane_pout
            with charachange

            li "That wasn't really an escape…"

            show hanako emb_downsmile
            show lilly cane_surprised
            with charachange

            "Hanako gives a small giggle, briefly surprising both of us."

            show hanako basic_bashful
            with charachange

            ha "I just thought that… Lilly might not be enjoying the festival."

            hi "Well, now we can enjoy it together, right?"

            show lilly cane_smileclosed
            with charachange

            "The two nod happily before we set out of the library and towards the festivities."

            stop music fadeout 2.0

            scene bg school_stalls1_ni
            with shorttimeskip

            $ renpy.music.set_volume(0.5,0.0, "ambient")

            play ambient sfx_cicadas fadein 0.3

            "I hand over some change to the girl behind the counter, and take the two styrofoam cups of tea. I try to accentuate my bow a bit to cover for the fact that she's quite obviously deaf."

            "Come to think of it, I probably should have asked for help instead of leaving those two in the gardens while I bought drinks."

            "Trying to juggle the two cups of hot tea (for them) and a can of coffee (for myself, out of a vending machine) isn't exactly easy."

            "With some careful maneuvering, though, I manage to keep everything stable and upright as I walk over to the bench where Lilly and Hanako are sitting and chatting."

            scene bg school_gardens2_ni
            show lilly basic_smileclosed_ni at twoleft
            show hanako basic_distant_ni at tworight
            with locationchange

            "It's actually quite a nice place. Lit only by moonlight, it's tucked away some distance from the main events."

            "Compared to how hot it had been during the day, this spot is also pleasantly cool by now."

            "Not that it matters all that much. Most of the visitors have moved to areas that are either closer to the fireworks, or higher on the hill in order to view the display apparently planned."

            show lilly basic_smile_ni
            with charachange

            li "Welcome back, Hisao."

            show hanako basic_normal_ni
            with charachange

            "Her ears are good. I'm not exactly close and even Hanako hadn't noticed me."

            hi "Here you go. Sorry it's instant, but that's all they had left by now."

            "Hanako gingerly takes a cup from my right hand, and I gently place the other into Lilly's outstretched hands."

            show hanako basic_smile_ni
            show lilly basic_smileclosed_ni
            with charachange

            li "Did you enjoy the festival then, Hisao?"

            hi "Yeah, it was pretty fun."

            "An honest answer. Much of the food may have been somewhat subpar, but it was a lot of fun in the end, especially with Hanako and Lilly."

            "In fact, I think those two may have enjoyed themselves even more than I did. With both Lilly and me around, much of Hanako's withdrawn nature around others died down enough for her to enjoy herself."

            stop ambient fadeout 1.0

            $ renpy.music.set_volume(1.0,0.0, "ambient")

            play ambient sfx_fireworks
            play music music_twinkle fadein 12.0

            scene bg misc_sky_ni
            show fireworks
            with dissolve

            "As we sit drinking, the whistle of the first firework rings out before it explodes into a vibrant shower of blue against the night sky, heralding the beginning of the end for the festival."

            "Enthusiastic shouts can be heard from the crowds scattered around the school grounds celebrating them."

            "For minutes on end, Hanako and I watch the fireworks overhead as Lilly blissfully listens to them with her eyes shut."

            "Red, green, yellow, star-shaped, circular and patterned, and all manner of shapes and colors fill the air, one after the other, and dance across the sky."

            "No place near where I lived put on such lavish displays. Festivals like this were a thing of the past in such a metropolitan area."

            "To be seeing such a sight with these two… it's probably the happiest I've been in a long while."

            scene bg school_gardens2_ni
            show lilly basic_weaksmile_ni at twoleft
            show hanako basic_distant_ni at tworight
            show fireshine
            with charachange

            li "So… that's it. The festival's finally ending."

            hi "Yeah."

            "She gives a delicate, wistful sigh."

            show lilly basic_concerned_ni
            with charachange

            li "As much as I might complain about all the stuff we have to do, it's still sad that we'll have graduated before the next Yamaku festival."

            show lilly basic_concerned_close_ni
            with characlose

            "I walk forwards and stand beside Lilly, gently resting a hand on her shoulder."

            hi "Don't worry. We still have Tanabata later in the year, right?"

            show lilly basic_smile_close_ni
            with charachange

            li "You're right. It would be nice to go there when it comes."

            "Minutes of silence pass, with only the blasts of the fireworks to be heard."

            "Seeing these two reminds me of those words of advice Lilly had given me as we walked into town together."

            "'Cherish the opportunity to make new friends', huh?"

            hi "Hey, Lilly?"

            show lilly basic_smileclosed_close_ni
            with charachange

            "She turns her head slightly to show that she's listening, Hanako's gaze still firmly fixed on the technicolor fireworks bursting overhead."

            hi "You mind if I join you two for tea every now and again?"

            "The smile on her face is more than enough to see her answer."

            show lilly behind_cheerful_close_ni
            with charachange

            li "It would be a pleasure, Hisao."

            stop music fadeout 2.0
            stop ambient fadeout 2.0

            if _in_replay:
                return

    if force_route == FR_HANAKO:
        label .nc5xb3:
            call stranger_lilly_and_hanako

            call stranger_union

            call lilly_and_hanako_union

            scene bg school_stalls2
            show lilly basic_reminisce at center
            with charaenter

            "Lilly doesn’t look impressed at all, and I can't really blame her."

            "On top of her issues with her stall, she still seems to be worried about Hanako."

            "I can't really help her with the former, so I guess the only way I can help is by trying to take her mind off our shy mutual friend."

            "Placing the bowl back on the counter, I call out to Lilly."

            hi "Hey, Lilly, don't worry about Hanako. I'll go find her and hang out with her, okay?"

            show lilly basic_weaksmile
            with charachange

            "I can see Lilly's relief plainly written across her face."

            li "Thanks Hisao. And if you see anyone from my class, can you tell them to come back here please?"

            hi "Will do. Have a good one. And make sure you take a break, okay?"

            show lilly basic_smile
            with charachange

            li "I will if I can. See you later, Hisao."

            stop music fadeout 10.0
            $ renpy.music.set_volume(1.0,1.0, "ambient")

            scene bg school_courtyard
            show crowd
            with locationchange

            "I leave Lilly in the stall and head out in search of Hanako."

            "In a way, I feel bad for leaving her with the crowds, but even though she was clearly under pressure, I can't help but think that she is enjoying herself."

            stop ambient fadeout 0.5

            scene bg school_hallway2
            show crowd
            with locationskip

            play ambient sfx_crowd_indoors fadein 0.5

            "The halls are packed with swaying crowds meandering throughout the festival."

            "If there's one thing I know about Hanako, it's that she's not going to be anywhere near this."

            "And with the students showing their friends and family their dorms, I doubt she'll be there either."

            "Following blind intuition, I move against the grain of the crowd."

            "Thankfully, this crowd seems to be slightly less festive than your usual festival crowd; I assume this is out of consideration for the student body."

            stop ambient fadeout 5.0

            "As I force my way through the masses, it doesn't take long for them to thin down into nothingness."

            hide crowd
            with Dissolve(2.0)

            "This is not surprising, since I am standing before the library."

            "Even the most eager of students don't bother to show anyone this section of the school."

            play music music_happiness fadein 2.0
            scene bg school_library
            with locationchange

            "As I enter the library, the noise of the festival fades into a dull background noise, and soon I am in the reading area at the rear of the room."

            "Behind one of the partitioned desks I see the top of a head, with straight, dark hair catching my eye."

            hi "Hey, Hanako. I had a feeling I'd find you here…"

            show hanako def_shock:
                xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.9
                easein 0.5 center
            with charaenter

            show hanako at center

            "The head jumps a little in shock before slowly peeping over the partition."

            ha "H-Hisao?"

            hi "Hey. Lilly's pretty busy, so she sent me to find you."

            show hanako basic_normal
            with charachange

            ha "O-oh. Do you want to sit down?"

            hi "Actually, I am feeling a little hungry. Would you like to get something to eat from one of the stands?"

            show hanako defarms_worry
            with charachange

            ha "Um… I… I brought some food so…"

            "I shouldn't be surprised, but it was worth a try. Expecting her to go outside today was a long shot."

            hi "How about we eat in the tea room? I passed by it on the way here, and no one was around."

            hi "We can make some food there, and it'll be a little more comfortable. What do you say?"

            show hanako cover_distant
            with charachange

            ha "S-sure. Let's go."

            show hanako basic_distant
            with charachange

            "Hanako closes her book and puts it away with deliberate, practiced movements."

            hi "Good to go?"

            show hanako basic_normal
            with charachange

            ha "Y…yeah."

            stop music fadeout 2.0

            scene bg school_hallway2
            with locationchange

            "We walk side-by-side from the library to the tea room."

            "As expected, there is barely a soul around."

            "If it weren't for the murmurs through the walls, you wouldn't tell that there was a huge festival going on outside."

            show hanako emb_downtimid at tworight
            with charaenter

            "Hanako carries her bag in both hands and focuses on just the floor ahead of her."

            show hanako emb_downsmile
            with charachangealways

            show hanako emb_downtimid
            with charachangealways

            "Every now and again, she seems to break her pace a little and steps in slightly shorter paces."

            "The first time it happened, I gave it no mind, but I soon notice that she does it on a regular basis."

            hi "Are you all right?"

            show hanako defarms_worry
            with charachange

            "She stops dead in her tracks."

            ha "W-what?"

            hi "I dunno… it looked like you were tripping or something…"

            play music music_another fadein 0.5

            show hanako emb_blushing
            with charachange

            "A pink blush rises into her cheeks as her gaze returns to the floor."

            show hanako emb_downtimid
            with charachange

            ha "It… it's nothing."

            hi "You know, when you say 'nothing' like that, people are inspired to ask further questions."

            "For a second I don't think she is going to answer."

            "Prepared to leave it be, I almost set off walking again, when…"

            show hanako emb_emb
            with charachange

            ha "It's a… a game."

            hi "Game?"

            show hanako emb_downsmile
            with charachange

            ha "Do you… see the floor here?"

            "What a bizarre question. The floor looks just like any other floor; covered in those tiles made up from squares of linoleum."

            "Nothing noteworthy."

            hi "Well, yes. What about it?"

            show hanako emb_downtimid
            with charachange

            ha "Sometimes… when there's no one around… I only step on the darker ones…"

            "Hanako's voice trails off as her explanation continues, until I can barely hear her voice over the roaring silence of the empty hall."

            hi "Darker ones?"

            "Shuffling her feet, Hanako points the toe of her shoe at a tile that is barely a shade darker than the others."

            show hanako emb_downsmile
            with charachange

            ha "L-like these ones."

            hi "Oh, right, so these ones are no good?"

            "I point out a nearby tile."

            show hanako emb_emb
            with charachange

            ha "Y-yeah. Something… something like that."

            hi "Oh, I see. Do you play this game a lot?"

            show hanako emb_downsad
            with charachange

            "Hanako shakes her head."

            hi "Just when the halls are empty?"

            show hanako emb_emb
            with charachange

            "She nods."

            hi "Well then, no point in stopping, I'm beginning to get really hungry."

            show hanako emb_smile
            with charachange

            "She nods again, this time with a little more enthusiasm."

            hi "Well then, let's go."

            hide hanako
            with charaexit

            stop music fadeout 5.0

            "We set off down the hall, and this time I notice that Hanako is paying a little less attention to the floor."

            "I wonder; just how lonely does someone have to be to come up with a game like that?"

            "But, before I realize what I'm doing, I find myself trying to aim each step so it lands on the correct tiles."

            play music music_dreamy fadein 2.0

            scene bg school_miyagi
            with locationchange

            "The noise of the festival is slightly louder inside the tea room, but the breeze coming through the open window makes it worth it."

            "Without thinking, I walk to the windowsill and inhale deeply. I sometimes forget how clean the air is here compared to back home."

            show hanako basic_bashful at center
            with charaenter

            ha "Do… would you like some tea?"

            hi "That would be great, thanks."

            hide hanako
            with charaexit

            "It occurs to me that this is the first time I've been alone with Hanako without her trying to be somewhere else."

            "Turning from the window, I watch as she makes a simple pot of tea and arranges some sandwiches onto a plate."

            "I've seen her do this before a number of times, but this time she seems slightly different."

            "It's like she's…{w} calm."

            "Eventually she places the small tray on the table and pours two cups of tea."

            "The fresh scent of brewed tea mingles with the breeze, and for a second I feel like I'm the only one in the world."

            hi "I think I know why you like this room now."

            show hanako defarms_worry at center
            with charaenter

            ha "Um… I don't know what you mean."

            hi "Well, there are quite a few people out there, but in here it's like another world."

            hi "You can pretend that there's no one around for miles."

            show hanako emb_downtimid
            with charachange

            ha "Y-you're right."

            ha "It's like the world has forgotten this room."

            show hanako emb_emb
            with charachange

            ha "And b-because of that, you can forget about the outside."

            "That would be appealing in some cases."

            "As far as I can tell, conventional bullying doesn't exist in this school."

            "But then again, I haven't seen a single person talk to Hanako besides Lilly."

            "If you're ignored by the world, a place where you can forget its existence would hold a special appeal."

            hi "That's a good point. It's like this room gives you some kind of complete freedom."

            show hanako emb_smile
            with charachange

            ha "Y-yeah."

            show hanako basic_bashful
            with charachange

            ha "Say… do you play chess?"

            hi "Chess? I've played it a bit, I guess."

            hi "I take it you've played before?"

            show hanako basic_distant
            with charachange

            ha "A little…"

            hide hanako
            with charaexit

            "Without saying anything more, Hanako moves to one of the cupboards and digs out a small chess set."

            ha "Do… do you want…"

            hi "Sure, why not?"

            "I cut her off, but she doesn't seem to mind it."

            scene bg school_miyagi
            show hanako basic_normal_close at center
            with shorttimeskip

            "We arrange the pieces, and before long we are sending pawns charging to their inevitable fates."

            "I take my time and intently examine each move and its consequences, nostalgia for the game taking second place to the matters at hand."

            "For a time the game is a lengthy battle of attrition, but I spot an opening and tear a line in her defense."

            show hanako basic_worry_close
            with charachange

            "A few moves later, her king is cornered by several of my pieces."

            hi "Checkmate."

            hi "You're not bad at this, are you?"

            "An honest appraisal. Her technique is pretty good, but several times I was able to exploit her lack of prediction."

            "I pick up a piece and examine it. It looks relatively new, yet worn for its age."

            show hanako basic_smile_close
            with charachange

            ha "I… I guess not."

            hi "Does Lilly play?"

            show hanako def_worry_close
            with charachange

            "The absence of Hanako's answer causes me to think about my question."

            ha "A… A bit…"

            ha "T-this is the first time I've played against someone… other than her, or…"

            show hanako emb_downsad_close
            with charachange

            "Or…?"

            "She cuts herself off abruptly, leaving the answer hanging in the air. Someone she knew before coming to Yamaku, maybe."

            hi "Well then, I'm honored to have played against you."

            show hanako emb_smile_close
            with charachange

            ha "Um… can we play again?"

            "She asks as if she were asking me to cut off my own hands. The spirit of competition's gotten into her?"

            hi "Sure. Though don't expect me to go easy on you this time…"

            "Not that I was before, mind. She seems to appreciate the competitive tone."

            show hanako emb_downsmile_close
            with charachange

            ha "S… same here…"

            stop music fadeout 2.0

            if _in_replay:
                return

        label .movement:
            scene bg school_miyagi
            show hanako emb_downsmile_close at center
            with None

            play sound sfx_doorknock2

            show hanako emb_timid_close
            with charachange

            "As we are setting up the pieces, there is a noise at the door."

            play sound sfx_dooropen

            show bg at bgright
            show hanako at tworight
            with charamove

            show lilly basic_smileclosed at twoleft
            with charaenter

            li "Good afternoon."

            play music music_lilly fadein 4.0

            show hanako emb_emb_close
            with charachange

            ha "Lilly…"

            hi "Oh, hey there Lilly. Are you finished?"

            show lilly basic_smile
            with charachange

            li "You both are here? Wonderful. At any rate, our teacher managed to round up some extra help, so I was able to leave. Have you been here since you left?"

            hi "Pretty much, we've just been playing a bit of chess."

            show hanako emb_smile_close
            with charachange

            ha "W-would you like a cup of tea?"

            show lilly basic_weaksmile
            with charachange

            li "Actually, I think it may be a good idea to go outside for a little while…"

            show hanako def_worry_close
            with charachange

            "The instant drop in Hanako's face shows her objection to this plan, even though she says nothing."

            "I feel strangely compelled to voice what is plainly in view on her face, but Lilly can't see."

            hi "I… I kinda think that we should just stay here…"

            show lilly basic_surprised
            with charachange

            li "Really? It's so crowded here that I was thinking we should leave the school and head for the local teahouse."

            show hanako emb_blushtimid_close
            with charachange

            ha "You mean the S-Shanghai?"

            show lilly basic_smileclosed
            with charachange

            li "Of course; with everyone at the festival it should be practically empty."

            hi "Teahouse?"

            show lilly basic_weaksmile
            with charachange

            li "Oh, that's right, you probably don't know of it."

            show lilly basic_smile
            with charachange

            li "There is a teahouse not far from here, which we go to every so often."

            hi "Sounds like a plan. Hanako, what do you think?"

            show hanako defarms_shock_close
            with charachangealways

            show hanako def_worry_close
            with charachangealways

            "Hanako jumps a little at being forced into the conversation, but at least she seems less distraught than before."

            show hanako cover_bashful_close
            with charachange

            ha "If… if it's the Shanghai, I think it'll be nice."

            show lilly basic_planned
            with charachange

            li "Well then, it's settled. Let's be on our way."

            show hanako basic_bashful
            with charadistant

            "Hanako and I rise from the table and our preempted chess game."

            "Before I can do anything, Hanako has poured the pieces into a small container and placed the board away."

            hi "Looks like we're ready now. Please, lead on."

            stop music fadeout 8.0

            scene bg school_hallway3
            with locationchange

            show hanako emb_smile:
                xpos 0.58 xanchor 0.5
            show lilly basic_smileclosed:
                xpos 0.42 xanchor 0.5
            with charaenter

            "Hanako moves to Lilly's side and we venture onto the school's corridors."

            $ renpy.music.set_volume(0.2, 0.0, channel="ambient")

            play ambient sfx_crowd_outdoors fadein 1.0

            scene bg school_gate_ss
            with locationskip

            "The pair leads me through a series of unfamiliar doors, and we emerge on the side of the building opposite of the festival grounds."

            "Insulated by the heavy stone of the building, the noise from the crowd has faded to a murmur."

            hi "Strange; I thought that most people would be beginning to leave by now…"

            show hanako emb_downtimid_ss:
                xpos 0.58 xanchor 0.5
            show lilly basic_smile_ss:
                xpos 0.42 xanchor 0.5
            with charaenter

            li "They're probably here to view the fireworks."

            hi "Fireworks?"

            show lilly basic_weaksmile_ss
            with charachange

            li "Yes, apparently the school puts on quite a show. A lot of people come from town just to watch them."

            "Lilly's decision to leave the school grounds seems to make sense now. Hanako would probably have a hard time with the whole town descending onto the school. Or ascending, as the case may be."

            stop ambient fadeout 7.0
            play music music_tranquil fadein 3.0

            scene bg school_road_ss
            with locationchange

            "For the second time since arriving at Yamaku I find myself walking down this road with Lilly."

            "Only now that I can barely hear the incessant noise of the festival do I realize how loud it was. I can hear my ears ringing slightly in the still evening air as they recover from the day's assault on them."

            show hanako emb_emb_ss:
                xpos 0.58 xanchor 0.5
            show lilly basic_smileclosed_ss:
                xpos 0.42 xanchor 0.5
            with charaenter

            "Hanako clings to Lilly, but still manages to guide her along the road. That, and avoiding the occasional gaze from curious pedestrians, appears to completely sap her constitution."

            "She rarely raises her focus from the ground in front of her, nor does she utter a word."

            "Lilly, on the other hand, maintains her prim and proper persona just as she does in school. It's obvious she purposely puts effort into her appearance, rather than hiding it as Hanako does."

            "It's striking how different they are in their way of holding themselves outside of Yamaku's grounds. That said, it's obvious in both their cases that they do visibly change."

            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")

            nvl clear

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl show dissolve

            n "{vspace=90}Inside Yamaku, everyone is 'special,' which negates the 'special-ness' of it."

            n "But once we venture outside the school gates, we are returned to the status of 'outsider' and generic labels."

            n "Especially when we are still in school uniform. It's like hanging a sign around your neck challenging people to figure out what is wrong with you."

            n "I'm surprised that so many of the students keep it on. Then again, with canes and wheelchairs common among the students, I guess it's not really that much of a giveaway."

            n "{vspace=30}Or maybe I'm the only one that sees this as a stigma? Maybe you get used to it after a time, like any other school uniform."

            nvl hide dissolve

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl clear

            scene bg suburb_shanghaiext_ss
            with locationskip

            "The teahouse seems fairly standard from the outside; just an ordinary building with typical signs decorating the entrance."

            "It looks like the type of place you'd walk by without a thought, just another generic café in a sea of thousands."

            "If Hanako hadn't steered Lilly into the entrance I would have continued on down the road without ever knowing that it existed."

            play sound sfx_storebell

            scene bg suburb_shanghaiint:
                xalign 1.0
                warp acdc_warp 5.0 xalign 0.0
            with locationchange

            stop music fadeout 6.0

            "Inside the teahouse it takes on a more traditional feel. Everything seems to have been made from the same lump of timber, from the counter and benches to the high-backed booths around the walls."

            "But the most striking feature of the room is the lack of life. I think I can faintly hear something bubbling away in the background, but otherwise the room is silent."

            "Without any direction, we simply wait near the entrance, politely obeying the 'Please wait to be seated' sign."

            hi "Er, is this place closed or something?"

            stop music
            play sound sfx_impact2

            show yuukoshang panic_up:
                center
                ypos 1.5
                easein 0.3 center
            show bg at right
            with vpunch

            show yuukoshang at center

            "The sound of a chair falling over echoes throughout the empty room, and a head shoots up from inside a booth."

            play music music_comedy fadein 0.5

            show yuukoshang neurotic_up
            with charachange

            yu "I wasn't asleep and welcome to the Shanghai!"

            "Yuuko, dressed in a pastel apron and clutching a menu, rushes to greet us. Her misaligned glasses and ruffled hair cast suspicion on her previous statement."

            "But whether she was asleep or not isn't the first question that leaps to my mind."

            hi "You work here now? What happened to the library?"

            show yuukoshang smile_down
            with charachange

            yu "What? Lilly? Hisao?"

            show yuukoshang neurotic_up
            with charachange

            yu "Welcome to the Shanghai!"

            show yuukoshang noglasses_up:
                ypos 1.25
            with Dissolvemove(0.2)

            play sound sfx_dropglasses

            pause 0.3

            show yuukoshang at center
            with charamove

            "Yuuko, still waking up, jerks into a violent bow, dislodging her glasses in the process."

            yu "Uweh!? My glasses…"

            "As I pick up her spectacles off the floor, Lilly offers an explanation."

            show yuukoshang at tworight
            show bg at center
            with charamove

            show lilly basic_weaksmile at twoleft
            with charaenter

            li "Yuuko works here part-time as well as at the library. It's one of the reasons we like to come here."

            show yuukoshang neurotic_up
            with charachange

            "Yuuko takes her glasses from my hands, shakily putting them back on."

            yu "Yes… that's right… thanks…"

            show yuukoshang neutral_down
            with charachange

            yu "Shall I show you to your table?"

            show yuukoshang worried_up
            with charachange

            yu "There's no-one else here so you can choose your table and order whatever you like, but there may be a delay as I will have to make it myself…"

            show lilly basic_smile
            with charaenter

            li "It's all right, Yuuko. Just a pot of black tea and a plate of sandwiches will be fine."

            show yuukoshang happy_down
            with charachange

            yu "Right! I'll get right onto that!"

            hide yuukoshang
            with charaexit

            show lilly at center
            show bg at bgright
            with charamove

            "Yuuko hurries off to the back of the café, leaving us still standing at the entrance."

            "She pushes the swinging half-doors open before realizing that she hasn't seated us."

            yu "I'm sorry! I'm sorry! Please, sit wherever you'd like! I'll be right back!"

            stop music fadeout 3.0

            hide lilly
            with charaexit

            show bg at bgleft
            with charamove

            "Following her advice, I lead Lilly to the nearest booth as Hanako follows."

            show lilly basic_smileclosed:
                twoleft
                ease 1.0 ypos 1.2
            show hanako basic_normal:
                tworight
                ease 1.0 ypos 1.17
            with Dissolve(1.0)

            show lilly:
                twoleft
                ypos 1.2
            show hanako:
                tworight
                ypos 1.17

            "As I begin to sit next to Lilly, I realize how appropriate this place is for Hanako."

            "The high-backed booths totally separate you from the rest of the room, and it doesn't look like it gets all that many customers."

            "All of the furnishings, from the cushions on the benches to the condiment holders, look dated but aren't overly worn."

            "I wonder if Lilly deliberately selects places like this to take Hanako? She seems like the type that would go to lengths to cater to Hanako's unique predicament."

            play music music_another fadein 4.0

            show lilly basic_weaksmile
            with charachange

            li "So, Hisao, I didn't know you played chess…"

            hi "Well, not very well, but I do know how to play."

            show lilly basic_smile
            with charachange

            li "I suppose the obvious question would now be… who won?"

            "Lilly's innocent smile makes me hesitate. I don't really want to look like I'm lording my victory over Hanako."

            show hanako cover_bashful
            with charachange

            ha "H-Hisao did."

            hi "Yes… but, uh, not by much…"

            "Damn. Saying that out loud makes me feel like I've done something terrible."

            show lilly basic_giggle
            with charachange

            li "Well done, Hisao. You've accomplished something I've only ever failed at."

            hi "Er, thanks. I haven't played in ages, so it felt good to play again."

            show hanako basic_smile
            with charachange

            ha "Y… yes… It did."

            "Hanako fidgets with her hair a little and looks away as she replies, but a small smile emerges."

            "It's a little more extreme of a reaction than I expected, but still kind of cute in that Hanako way."

            show hanako defarms_shock:
                ease 0.5 xpos 0.8
            show lilly basic_surprised:
                ease 0.5 xpos 0.2
            with charachange

            show lilly:
                twoleft
                xpos 0.2 ypos 1.2
            show hanako:
                tworight
                xpos 0.8 ypos 1.17

            show yuukoshang worried_up at center
            with charaenter

            "It throws me a little off guard, and only Yuuko's cataclysmic re-entry shocks me back into conversation."

            hi "Are you all right there, Yuuko? Do you need a hand?"

            show yuukoshang neurotic_up
            show hanako def_worry
            with charachange

            yu "I'm fine I'm fine I'm fine. I have to do this properly, it's my job."

            show yuukoshang worried_up
            with charachange

            "Concentration plays across her face while she stares at the tray in her hands, as if simply looking at its contents will hold them in place."

            show yuukoshang at centertremble
            with charachange

            "Sadly, this doesn't prove all that effective; the cups and saucers slowly dance around, occasionally clattering as they collide with one another."

            show yuukoshang:
                ypos 1.1
            with ease

            show yuukoshang at center
            with ease

            "Taking great care, Yuuko sets the tray down on the table with only the subtlest of crashes."

            show yuukoshang happy_down
            with charachange

            yu "There, see!"

            hi "Er, well done?"

            show lilly basic_weaksmile
            with charachange

            li "Thank you, Yuuko."

            show yuukoshang neutral_down:
                ypos 1.2
            with Dissolvemove(0.2)

            pause 0.2

            show yuukoshang at center
            with ease

            "Yuuko's head rockets downwards in her distinctive bow before answering."

            show yuukoshang closedhappy_down
            with charachange

            yu "You're very welcome."

            show lilly basic_smile
            with charachange

            li "Would you like to join us? There's something else I'd like to discuss about that recent order, if I may…"

            "Ah, that's right. Lilly and Yuuko were discussing a pile of books when I first met Hanako."

            "Something about Lilly helping with the Braille…"

            show yuukoshang neurotic_up
            with charachange

            yu "Ah… yes. We didn't get the chance to go through them, did we?"

            show yuukoshang:
                ypos 1.17
            with charamove

            "Yuuko hastily sits down next to Hanako."

            "Apparently her dedication to this job only goes as far as her concentration; once it is broken, she suddenly loses it."

            show yuukoshang smile_down
            with charachange

            yu "I'll be in the library tomorrow afternoon if you'd like to try again…"

            show lilly basic_cheerful
            with charachange

            li "That sounds perfect, I'll meet you there after classes."

            show hanako emb_timid
            with charachange

            ha "Um… L-Lilly…"

            show lilly basic_oops
            with charachange

            li "Oh dear, that's right. Tomorrow is Monday, how could I have forgotten?"

            "I'm starting to feel a little left out of the loop here. Then again that's to be expected; I have been here for barely a week, so it's impossible to know everyone's schedule."

            show lilly basic_weaksmile
            with charachange

            li "Well, perhaps we could come to some other arrangement."

            show lilly basic_smile
            with charachange

            li "Yuuko, will you be in the library later in the week?"

            show yuukoshang worried_up
            with charachange

            yu "Hmm, maybe, but this is already overdue…"

            show hanako emb_downsad
            with charachange

            ha "A-and there are some… things I n-need…"

            show lilly basic_listen
            with charachange

            li "This might be a problem…"

            "Lilly ponders for a second before discovering the answer."

            show lilly basic_planned
            with charachange

            li "I wonder, might we be able to enlist the help of another, if need be…?"

            hi "Um, to do what? You lost me quite some time ago…"

            "Being volunteered for something without even having the slightest idea what is going on isn't really my thing."

            "And here I thought I had finally escaped the clutches of the Student Council and their repeated attempts to recruit me."

            show lilly basic_smileclosed
            with charachange

            li "Oh, of course. The other day I was helping Yuuko sort the new Braille books in the library."

            show lilly basic_weaksmile
            with charachange

            li "But Hanako and I usually go shopping on Monday afternoons; it's quieter on that day than on weekends."

            li "Last week we couldn't go because I was busy with the festival. I managed to slip away later in the week, but Hanako couldn't make it."

            hi "Well, since I can't read Braille, I'm assuming you'd like me to go shopping with Hanako?"

            show lilly basic_smile
            show hanako emb_timid
            with charachange

            li "Correct. You were a great help to me the other day."

            hi "I think I can handle that. Hanako, what do you think?"

            show hanako basic_smile
            with charachange

            ha "I-if you wouldn't mind…"

            hi "Of course not. I'm still not familiar with all the stores in the area, so it sounds like a good idea."

            show hanako basic_bashful
            with charachange

            ha "O-okay."

            show lilly basic_smileclosed
            with charachange

            li "Now that we have that arranged, shall we have some tea?"

            "It's now that I realize our tea has been sitting idly by all this time, getting no hotter."

            show yuukoshang panic_up
            with charachange

            yu "It's my fault! Let me pour that for you…"

            "Yuuko reaches out with shaking hands, but I intercept her; she looks in no state to be handling hot liquids."

            hi "It's all right, I've got it. Since you've already made the tea and sandwiches, you've fulfilled your waitress duties, right?"

            show yuukoshang neurotic_up
            with charachange

            yu "I… I guess."

            "Yuuko relaxes a little, but still watches eagerly as I share out the assortment."

            stop music fadeout 1.0
            play ambient sfx_fireworks

            show fireshine
            show hanako defarms_shock
            show yuukoshang panic_up
            show lilly basic_surprised
            with Fade(0.1, 0.0, 0.5, color="#fff")

            "As I am about to bite into the sandwich, a low, loud rumble can be heard, along with a flash of light from outside."

            show lilly basic_weaksmile
            show yuukoshang smile_down
            show hanako emb_timid
            with charachange

            li "Ah, I take it the show has started."

            hide fireshine
            show bg misc_sky_ni as front
            show fireworks
            with locationchange

            "Only now looking outside, I realize that dusk has come and gone, leaving us in the peak of twilight."

            "Sparking tracers arc upwards ready to explode in the floral shapes of fireworks."

            hide fireworks
            hide front
            show fireshine
            show yuukoshang happy_down
            with locationchange

            yu "Let's go watch!"

            show yuukoshang panic_up
            with charachange

            yu "Oh… sorry Lilly…"

            show lilly basic_ara
            with charachange

            show hanako_fw behind bg:
                zoom 1.05 truecenter
                ease 22.0 zoom 1.0
            show ev hanako_shanghaiwindow behind hanako_fw:
                zoom 1.05 truecenter
                ease 22.0 zoom 1.0

            li "Please, don't miss the show on my account. From what I've heard, this isn't a bad location to watch them from."

            play music music_serene fadein 4.0

            hide fireshine
            hide bg
            hide hanako
            hide lilly
            hide yuukoshang
            with locationskip

            "With the exception of Lilly, we rush to the window of the small teahouse to watch the show."

            "The strobe of colored lights plays across Hanako and Yuuko's smiling faces, and for a second I forget to look out the window."

            "In this totally new world, there are a few things that don't change."

            "I think that's why the school makes such a fuss over this festival. It's a chance to show the similarities between everyone."

            stop ambient fadeout 3.0

            hide hanako_fw
            with Dissolve(1.0)

            "The show is over all too quickly; fireworks are expensive, even for the most well-funded schools."

            scene bg suburb_shanghaiint at bgright
            with locationchange

            "Before we return to our tea and sandwiches, Hanako turns to me."

            show hanako emb_downsmile_close at center
            with charaenter

            ha "Um, t-thanks for today."

            show hanako emb_smile_close
            with charachange

            ha "…and tomorrow."

            hi "That's okay; I don't think that I could have faced those crowds either."

            hi "On days like this it's more relaxing to spend some time away from everyone, don't you think?"

            show hanako basic_normal_close
            with charachange

            ha "Y-yeah."

            hi "Anyway, we've been delaying this tea for far too long now, let's get back."

            show hanako basic_bashful_close
            with charachange

            ha "S-sure."

            stop music fadeout 6.0

            hide hanako
            with charaexit

            show bg at bgleft
            with charamove

            show lilly basic_smileclosed:
                yanchor 1.0 xanchor 0.5 ypos 1.2 xpos 0.2
            show yuukoshang neutral_down:
                yanchor 1.0 xanchor 0.5 ypos 1.17 xpos 0.5
            with locationchange

            show hanako basic_smile:
                yanchor 1.0 xanchor 0.5 ypos 1.0 xpos 0.8
                easein 1.0 ypos 1.17
            with charaenter

            show hanako:
                yanchor 1.0 xanchor 0.5 ypos 1.17 xpos 0.8

            "We return to the booth and our light meal."

            show lilly basic_smile
            with charachange

            li "That sounded impressive. Bigger than last year's at least."

            show yuukoshang happy_down
            with charachange

            yu "Yeah it was great! I've never seen them put on such a show."

            yu "It gets better every year!"

            show lilly basic_weaksmile
            with charachange

            li "I'm afraid, however, that during that time, the tea has gone cold."

            show yuukoshang panic_up at center
            with Dissolvemove(0.2)

            play music music_ease fadein 0.5

            yu "Oh no! Let me make some more! This is my fault!"

            hi "Calm down, Yuuko, it's nobody's fault."

            "I take a sip from my cup, just to prove the point."

            hi "This tea isn't too bad cool, anyway. It's like an iced tea."

            show yuukoshang worried_up
            with charachange

            yu "Really?"

            hi "Yes, really. If you add a bit of sugar it's kinda nice."

            show yuukoshang neurotic_up
            with charachange

            yu "Are you sure?"

            hi "I'm positive. Now why don't you sit down and we'll finish this together?"

            show yuukoshang smile_down
            with charachange

            yu "O-okay."

            show yuukoshang:
                ypos 1.17
            with charamove

            "Yuuko doesn't seem convinced, but sits down regardless."

            "She carefully measures out about five teaspoons of sugar and adds them to her tea."

            hi "Er, I said a bit of sugar…"

            show yuukoshang neutral_down
            with charachange

            yu "I know but I like my tea sweet anyway."

            "Curiously I peer into her cup. As expected, hardly any of the sugar dissolves in the cold liquid."

            "She stirs it twice before upturning the cup and drinking the contents, sugar and all, in a single mouthful."

            show yuukoshang happy_down
            with charachange

            yu "You're right! That's not bad at all!"

            hi "Er, good…"

            "I look back to Lilly and Hanako, both of whom have finished their meal as I witnessed Yuuko's personality in action."

            "Not wanting to hold anyone up, I use her tactic and finish the remainder of my tea in a single swill."

            hi "Well then, it seems we're all finished."

            show lilly basic_smile
            with charachange

            li "Should we head back now or do we want seconds?"

            show yuukoshang neurotic_up
            with charachange

            "Yuuko's expression shows that this is quite clearly not a good idea."

            hi "I think that it would be best if we got back soon."

            hi "We do have to get back before curfew, after all."

            show lilly basic_smileclosed
            with charachange

            li "Oh, that is a good point."

            show lilly basic_smile
            with charachange

            li "I'll meet you tomorrow, Yuuko."

            show yuukoshang neutral_down
            with charachange

            yu "I'll be looking forward to it, Lilly. Goodbye, everyone."

            stop music fadeout 9.0

            $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
            play ambient sfx_cicadas fadein 0.5

            scene bg suburb_shanghaiext_ni
            with locationchange

            "We make our way out of the small teahouse and into the dark of the night."

            $ renpy.music.set_volume(0.4, 1.0, channel="ambient")
            scene bg suburb_roadcenter_ni
            with locationchange

            "Lilly and Hanako once again take point, but under the cover of darkness Hanako seems slightly less stressed than she did on the trip here."

            "We move against the occasional group of people emptying the school grounds, but Hanako seems to lead us along a few minor roads, avoiding the bulk of the crowd."

            $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

            scene bg school_dormext_full_ni
            with locationskip

            "Outside the dorms, the school seems strangely quiet when compared to the noise of the day."

            hi "Well then, thank you both for today. I think I learned a lot."

            show hanako emb_timid_ni:
                xpos 0.59 xanchor 0.5
            show lilly basic_weaksmile_ni:
                xpos 0.41 xanchor 0.5
            with charaenter

            li "You're most welcome, but I'm afraid that I really must be going. Today's been a long day."

            "That's right; Lilly spent all of today on her feet, and I can imagine that walking outside of the school would be pretty tiring for her."

            "I feel a pang of guilt as I remember that I was probably the only one in the school that got up around ten this morning."

            hi "Sure thing."

            hi "Well, I'll see you both tomorrow. Good night."

            show lilly basic_cheerful_ni
            with charachange

            li "Good night, Hisao."

            show hanako basic_smile_ni
            with charachange

            ha "N… night."

            hide hanako
            hide lilly
            with charaexit

            "The girls return to their dorm, and I to mine."

            "Actually, now that I consider it, today tired me out as well."

            stop ambient fadeout 2.0

            scene black
            with dissolve

            if _in_replay:
                return

    if force_route == FR_SHIZU:
        label .throwing_balls:
            scene bg school_dormhallway at bgright
            show kenji happy at center

            hi "I'm going to have to hang out with the Student Council, since I lost a bet."

            "I realize that we didn't agree on when and where. I'll just wait for them rather than risk us missing each other in the chaos outside. They must be busy running around and organizing things, anyway."

            "It's funny. I would've assumed the price for losing to Shizune in her stupid game to be a lot more severe. This is just a pretense for spending time with her. In that case, I guess she just wants me to have fun."

            "Even though she can't just come out and make her intentions clear, they may be good intentions after all, and I think I'm starting to like her more."

            hi "I could skip going, but it'd be a waste. And I want to go, too. I mean, you know, today does seem pretty exciting. If anything, it'll be interesting."

            show kenji tsun
            with charachange

            stop music fadeout 1.0

            ke "The Student Council? What? That's still around?"

            ke "Isn't it like, two dudes?"

            hi "They're both girls."

            play music music_tension

            show kenji rage
            with charachange

            ke "Really? Are they cute? Damn, no, wait… are they cute?"

            ke "No! It doesn't matter! I heard the Student Council president is insane… that whoever it is never talks and only gives orders through flunkies."

            show kenji tsun
            with charachange

            ke "Shit, they're the same in every school… Sounds like a cold-hearted bitch. Bitches everywhere."

            ke "If it's two girls, they outnumber you two-against-one. That is a dangerous situation, dude. Who knows what can happen."

            ke "Damn, the Student Council is just two women, but they hold so much power."

            ke "They must be stopped."

            ke "I can see them, plotting ways to push their feminist agenda. I can't trust an administration like that."

            ke "This is not cool. Not cool!"

            show kenji rage
            with charachange

            ke "Damn. Shit! Damn!"

            call stranger_union

            show bg at bgright

            "I ponder what I'd like to do with Shizune and Misha. Deciding it's best to be extra prepared, I duck back into my room to stock my wallet with money."

            scene bg school_dormhisao
            with locationchange

            "I wonder if they have that game where you try to catch goldfish on a paper net."

            "It seems way easier than they make it look. Then again, if I were to catch a goldfish, I'd have no real reason to keep it."

            "What am I going to do with a fish in my tiny room? Cook it?"

            "I could give it to Shizune, or Misha, but that might be overstepping my bounds."

            "It's a real problem. Both of them are cute, but I don't think I have any chance with either of them. Regardless, I mull over the thought of doing it. I imagine how they might react if I were to give them a gift tonight, like a fish or a doll."

            "Misha would probably laugh like she always does. Shizune might slap it out of my hand."

            "Maybe it isn't such a good idea after all."

            "Okay, I think I'm set."

            with shorttimeskip

            "A good while later, I decide that this could be another psych out test devised by Shizune. Even if it isn't, it's starting to get kind of late."

            "I resolve to just go out and search for them, even though I don't know where I could look. They might be really hard to find today."

            scene bg school_dormhallway
            show shizu behind_blank_close at center
            with locationchange

            "As soon as I step outside, I almost bump into Shizune."

            hi "Hi, Shizune. Where's Misha?"

            show shizu behind_frustrated_close
            with locationchange

            "I try to sign it as best as I can, but really I'm just making stuff up. I've got to ask Misha to teach me some of this."

            mi "Here!"

            play music music_comedy

            show misha hips_grin behind shizu:
                center
                ease 1.0 twoleft
            show shizu:
                ease 1.0 tworight
            with Dissolve(0.7)

            "Misha pops up from behind Shizune, grinning widely."

            show misha at twoleft
            show shizu at tworight

            mi "We just came to make sure you're coming along with us to the festival."

            show shizu basic_angry_close
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "Don't renege on your promise~!"

            hi "Promise? I don't think I promised anything."

            show shizu cross_angry_close
            with charachange

            shi "…"

            show misha hips_frown
            with charachange

            mi "Stop trying to get out of it!"

            show misha perky_sad
            with charachange

            mi "C'mon, Hicchan, it'll be fun! You need this, anyway, or you'll become a no-good person!"

            show misha perky_smile
            with charachange

            mi "You don't want to become one of those people who just stays in their dorm room all day, being paranoid, do you?"

            "I find myself staring over her shoulder at the door to Kenji's room right across from mine."

            "I hope he didn't hear that, but I think Misha wants the opposite."

            hi "No, of course not. I was just playing around a little, and was right about to leave anyway. You two didn't have to come here."

            show misha cross_laugh
            with charachange

            mi "Really? Ahahaha! Shicchan was worried you would try to get out of it somehow!"

            show misha hips_grin
            with charachange

            mi "We need you, Hicchan~!"

            hi "Huh?"

            "I think my heart just skipped a beat."

            show misha perky_smile
            with charachange

            mi "I don't have the aim to knock the dolls off their pedestals in that one game… and Shicchan refuses to throw things."

            hi "Oh."

            "Shizune stares at me, immediately noticing my disappointment. She uncrosses her arms and adjusts her glasses."

            show shizu adjust_happy_close
            with charachange

            shi "…"

            mi "What did you think we meant? I refuse to throw anything."

            show misha perky_confused
            with charachange

            mi "Why, Shicchan? That is weird…"

            show misha perky_smile
            with charachange

            mi "Well, anyway, Hicchan, you've thrown a ball before, right~, right~? So! You have to come with us!"

            "I'm amazed by their logic. I don't know if they're joking or if they're not."

            hi "Heh, I'd feel offended if I didn't know you guys were joking."

            hi "You're joking, right?"

            show shizu behind_frown_close
            with charachange

            shi "…"

            mi "It is what it is, Hicchan~! It is what it is what it is what it is what it is!"

            hi "Well that's reassuring."

            show shizu basic_normal2_close
            with charachange

            shi "…"

            show misha hips_smile_close at closeleft
            with characlose

            mi "Come on, let's go! The deaf band is setting up outside your window."

            "Misha grabs me by the hand and tries to pull me out the door, but it's clear that she isn't trying at all."

            show shizu adjust_blush_close behind misha
            with charachange

            stop music fadeout 3.0

            "Shizune looks at the both of us, blushing slightly and fiddling with her glasses impatiently."

            "I'm not used to this kind of casual contact, but I have nothing against it. How could I object?"

            play ambient sfx_crowd_outdoors fadein 1.0

            scene bg school_courtyard
            show crowd
            with locationskip

            play music music_running

            "It's still light outside, but the sun is getting ready to set behind the trees."

            "It looks like half the school is out here, and I can even see some faculty members standing off to the side, helping themselves to some punch."

            "They are about to empty the entire bowl, to the dismay of the girl working the stall."

            "There are some fortunetellers chatting idly with their friends, while others have already gotten started slinging horoscopes at anyone who walks in range."

            "I think that kind of tactic is a little too aggressive, but it shows that they're into it. It's refreshing to see, but I don't know if I'll be able to get used to it."

            show shizu basic_normal2 at tworight
            show misha perky_smile at twoleft
            with charaenter

            shi "…"

            show misha sign_smile
            with charachange

            mi "Well, we should get something to eat. Hungry, Hicchan?"

            "Come to think of it, I haven't eaten all day."

            hi "I don't really want to eat fried noodles."

            show misha hips_grin
            with charachange

            mi "That's okay, there are other fried foods!"

            hi "Are there any foods that aren't fried?"

            show shizu adjust_smug
            with charachange

            shi "…"

            mi "Candy. Junk food is the essence of celebrations!"

            show misha cross_laugh
            with charachange

            mi "Wahahahaha!"

            show shizu behind_smile
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "Come on, I - I mean, Shicchan - will treat you to one thing~!"

            mi "One?"

            show shizu adjust_smug
            with charachange

            shi "…!"

            show misha sign_smile
            with charachange

            mi "Just one~! Only so you can build up energy for your throwing arm!"

            show misha perky_smile
            with charachange

            mi "Ah, but it doesn't look like all the booths are done setting up yet, so you might not be able to get what you want."

            "I take a look around, surprised by the number of stalls. It's unbelievable, this festival seems larger than the ones you might see in actual towns."

            "Despite what Misha said, it seems like half the school is already celebrating."

            "The air is humming with the excited chattering of at least half the student body."

            "I can smell food cooking, and it's only making me hungrier by the second."

            show shizu behind_frustrated
            with charachange

            shi "…"

            show misha perky_confused
            with charachange

            mi "Come on, Hicchan, the food is already disappearing fast! If you want takoyaki, we need to move now!"

            show misha hips_grin
            with charachange

            mi "I could go for some takoyaki~! Come on, let's eat that!"

            hi "All right, I haven't had takoyaki in forever. I'm game."

            hide shizu
            with charaexit

            hide misha
            with charaexit

            "Shizune takes off before Misha can even sign it back to her, briskly walking towards the takoyaki stand as Misha and I try to catch up."

            scene bg school_stalls1
            with locationchange

            "Misha laughs as she skips towards Shizune, who asks for three orders of takoyaki by holding up three fingers."

            "I never noticed it before, but for someone who is so obsessed with high class tea, it's a little weird that Shizune is also so into fast food."

            "I take the plate of takoyaki she hands me and wonder if I should dig in. It looks extremely hot."

            "I can see the smoke coming off of it and the oil bubbling on the surface."

            show misha hips_smile:
                xpos 0.2 xanchor 0.5
                ease 1.0 twoleft
            show shizu behind_blank:
                xpos 0.8 xanchor 0.5
                ease 1.0 tworight
            with Dissolve(1.0)

            show misha at twoleft
            show shizu at tworight

            "Shizune and Misha both look at me, as if waiting for me to eat before they can begin."

            "I can't back down, so I spear one on the tiny plastic fork jauntily sticking up from the corner of the plate."

            show misha hips_grin
            show shizu basic_normal
            with charachange

            stop music fadeout 12.0

            "However, before I can even put it in my mouth, Shizune and Misha begin eating eagerly, Shizune taking quick but delicate bites out of the takoyaki while Misha eats with relish like a small child."

            "I guess at the end of the day, both of them are just kids like any other student here."

            "This is kind of nice. I don't think I've had a chance like this in a long time to just hang out with other people and enjoy their company."

            "Even before coming here, I'd been going through a very busy year. So busy that I hadn't realized what I have been missing until now."

            "Here, I feel at peace."

            "This is a soothing atmosphere. I didn't know these kinds of festivals still existed."

            show misha perky_confused
            with charachange

            mi "Eh? Hicchan, you aren't going to eat your food?"

            hi "No, I'm going to eat it."

            show shizu adjust_smug
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "I hope you aren't chickening out because it's too hot."

            hi "That's not it."

            "Even their teasing is beginning to become endearing."

            $ renpy.music.set_volume(0.6, 2.0, "ambient")

            scene bg school_stalls1_ss
            with shorttimeskip

            play music music_tranquil fadein 1.0

            "I eat quickly before my food can get cold, thinking that the dimly lit paper lanterns glowing warmly against the sunset make for a beautiful sight."

            show shizu behind_smile_close_ss at center
            with charaenter

            "Before I can finish my last bite of takoyaki, Shizune steps in front of me, standing perfectly straight with her arms rigidly behind her back."

            "I can see she's trying her best to look as serious as possible, but even she can't hide her good mood, as there is a slight smile on her face."

            show bg at bgright
            show shizu at closeright
            with charamove

            show misha cross_laugh_ss at twoleft
            with charaenter

            mi "Ahahaha~! Come on, Hicchan, let's go play some games!"

            hi "Are they even done setting up?"

            show shizu adjust_happy_close_ss
            with charachange

            shi "…"

            show misha cross_grin_ss
            with charachange

            mi "No, but it doesn't matter, it doesn't matter~! Come on, Hicchan, before it gets too crowded!"

            show misha hips_grin_close_ss at closeleft
            with characlose

            "Misha puts her hand on my shoulder and laughs very loudly."

            show misha perky_smile_close_ss
            with characlose

            mi "Come on! Come on! The prizes look really great this year, really really~! Wouldn't you like to win some prizes for two cute girls like us?"

            "Misha flashes her best 'cute' look, which is admittedly pretty cute. I look at Shizune, expecting her to do the same, but she just looks at me like I'm insane."

            show shizu cross_wut_close_ss
            with charachange

            shi "…"

            show misha hips_grin_close_ss
            with characlose

            mi "Misha, stop doing that!"

            show misha perky_confused_close_ss
            with charachange

            mi "Wait… I'm Misha…"

            show shizu basic_normal2_close_ss
            with charachange

            shi "…"

            show misha sign_smile_close_ss
            with charachange

            mi "Hicchan, hurry up, you've been holding that piece of takoyaki for like a thousand years!"

            show misha cross_laugh_close_ss
            with charachange

            mi "Hahahahaha!"

            show misha cross_smile_close_ss
            with charachange

            hi "I like to savor everything that I eat. Even this."

            show shizu basic_sparkle_close_ss
            with charachangealways

            show shizu adjust_smug_close_ss
            with charachangealways

            "Without warning, Shizune picks the takoyaki from my hand and plops it into her mouth with a smile."

            "It happens so fast that there was no way I could have stopped her."

            show misha cross_laugh_close_ss
            show shizu behind_smile_close_ss
            with charachange

            "Before I can even fully process what just happened, Misha bursts into laughter, and Shizune smiles at me, probably the closest I've ever seen her come to laughing."

            show shizu adjust_happy_close_ss
            with charachange

            shi "…!"

            mi "Well, that takes care of that~! Wahaha! Hahahaha!"

            stop music fadeout 6.0

            "Shizune grabs my right hand, and Misha grabs my left."

            show shizu behind_smile_close_ss
            with charachange

            shi "…"

            show misha hips_grin_close_ss
            with charachange

            mi "You're coming with us! There's a lot to do tonight, you should try harder to enjoy it!"

            show misha cross_laugh_close_ss
            with charachange

            mi "Hahahaha~!"

            $ renpy.music.set_volume(1.0,2.0, "ambient")

            scene bg school_courtyard_ss
            show crowd_ss
            with shorttimeskip

            play music music_ease fadein 6.0

            "Running through an already sizable crowd of people, we play game after game, from ring toss, to whack-a-mole, to games I've never even heard of."

            "We rarely win, but it's fun nonetheless."

            hi "Hey, do they have that goldfish scooping game here?"

            show shizu behind_smile_ss at tworight
            show misha hips_smile_ss at twoleft
            with charaenter

            shi "…"

            mi "Of course! I didn't know you liked that game, Hicchan!"

            hi "Well, I've always wanted to try it. It doesn't seem too hard."

            show misha hips_grin_ss
            with charachange

            mi "Are you sure about that, Hicchan~?"

            show misha cross_laugh_ss
            with charachange

            mi "Wahahaha~! Okay, okay! We'll see! It should be around here somewhere!"

            show shizu basic_normal_ss
            with charachange

            shi "…"

            show misha perky_smile_ss
            with charachange

            mi "But, where are you going to keep your fish? Do you have a bowl for it?"

            hi "Well, no…"

            show misha hips_grin_ss
            with charachange

            mi "Maybe he'll eat it!"

            show shizu adjust_smug_ss
            with charachange

            shi "…"

            show misha cross_laugh_ss
            with charachange

            mi "Hahahahahaha! Ahahahahahaha!!"

            show misha cross_grin_ss
            with charachange

            mi "All right, Hicchan, if we win any fish, we'll give them to you!"

            hi "Oh, really? Another game? Fine, then."

            show shizu basic_happy_ss
            with charachange

            "Shizune pushes me excitedly towards the booth, trying to hide the enthusiasm in her eyes."

            scene bg school_stalls2_ss at bgright
            with locationchange

            "Fortunately, the two of them fail to catch a single fish, but I don't do any better."

            show bg at bgleft
            with charamove

            $ renpy.music.set_volume(0.6, 2.0, "ambient")

            "I can't help but laugh as immediately afterwards, they start tugging me towards a particularly large, colorful stall that I helped build."

            "I remember this one; it had been a real pain in the ass to make."

            "The booth runner, an average-looking guy with dyed brown hair, snaps to attention when he sees us walking over. I notice two things:"

            "First, it's one of those games where you throw a ball at a pyramid of opaque bottles and try to knock over as many as possible."

            "Four balls for 50 yen, that's pretty good."

            "Second, there are instructions on how to play in braille. I almost want to say something, and look to see if Shizune and Misha see it as well."

            "Either they don't, or they don't find it strange at all."

            "Booth Operator" "Hey! It's good to see you, Hakamichi! Thank you so much for your help with this booth. Having fun?"

            "Shizune glances towards Misha, who signs everything to her in a flash, then beams at the operator."

            show shizu behind_smile_ss:
                xpos 0.8 xanchor 0.5
                ease 1.0 tworight
            show misha perky_smile_ss:
                xpos 0.2 xanchor 0.5
                ease 1.0 twoleft
            with Dissolve(1.0)

            show shizu at tworight
            show misha at twoleft

            shi "…"

            show misha hips_grin_ss
            with charachange

            mi "Haha~! It was nothing, nothing at all, really~! Yeah, this is great, I think the best festival we've put together yet!"

            show misha perky_smile_ss
            with charachange

            mi "Shiraki, we'd like to play this, that's okay, right?"

            show misha hips_grin_ss
            with charachange

            mi "Of course~, it would be really great if you would just give your cute, hard working Student Council representatives a prize, for all the hours we put in to make all of this possible!"

            "Shiraki" "Hahaha, haha… No."

            "If anything, Shiraki has balls."

            hi "Hey, I built this stall, it was a backbreaking job, too. I wasted two hours of my life, I think I deserve at least a free round."

            show misha hips_frown_ss
            with charachange

            mi "And me!"

            show shizu basic_angry_ss
            with charachange

            shi "…"

            mi "Me too!"

            show misha perky_confused_ss
            with charachange

            mi "Ah…"

            "After some hesitation, he eventually gives in, and hands us each four balls with a shrug."

            show misha hips_grin_ss
            show shizu behind_blank_ss
            with charachange

            "Barely a second later, Shizune and Misha dump theirs in front of me."

            hi "What gives?"

            hi "Don't tell me that after making such a big deal out of it, you two aren't going to even play?"

            hi "Not after the way we ganged up on Shiraki."

            "Shiraki" "Yeah…"

            show shizu basic_frown_ss
            with charachange

            shi "…"

            show misha sign_smile_ss
            with charachange

            mi "You stay out of this, please~!"

            show shizu adjust_happy_ss
            with charachange

            "Shizune turns to me and begins waving her hand dismissively. Misha appears torn between translating for her and consoling the booth operator."

            show shizu adjust_smug_ss
            with charachange

            shi "…!"

            show misha hips_grin_ss
            with charachange

            mi "Ahahaha! Hicchan, where's your sense of chivalry? Besides, I - Shicchan, have a policy against throwing balls!"

            show misha hips_smile_ss
            with charachange

            mi "Ah, sorry, Hicchan. I don't know if my aim is that good, either. You must be pretty good at these things, though, right, right? It shouldn't be a problem for you!"

            stop music fadeout 3.0

            "This looks simple enough. The bottles aren't even that far away, the only challenge is that these are wiffle balls."

            play sound sfx_impact

            "I throw one at the bottles hard, and it bounces off unceremoniously."

            show shizu behind_blank_ss
            show misha perky_confused_ss
            with charachange

            hi "What the hell?"

            "Shiraki" "Ah, yeah, it's not as easy as it looks. There's water inside the bottles. Trade secret."

            show misha hips_frown_ss
            with charachange

            mi "That's not very fair!"

            hi "This must be why it's four balls for 50 yen. How devious."

            show shizu basic_angry_ss
            with charachange

            shi "…"

            show misha hips_smile_ss
            with charachange

            mi "Come on, Hicchan, you can knock them down! You have eleven more chances! Go!"

            hi "Maybe you should do it."

            hi "Shizune? Do you want to try?"

            show shizu behind_blank_ss
            with charachange

            "Shizune emphatically shakes her head from side to side."

            "I laugh, this is actually pretty fun."

            play sound sfx_impact
            play music music_soothing fadein 3.0

            "Winding up, I throw another ball at the pyramid of bottles and manage to get them to budge just slightly."

            show shizu basic_normal_ss
            show misha perky_smile_ss
            with charachange

            "Both Shizune and Misha are casting longing glances towards a doll shaped like a cat."

            "All-in-all, they really aren't that different."

            "Sometimes I wonder if Shizune would sound like Misha if she could talk."

            "No, they're not that alike."

            play sound sfx_impact

            "I throw another ball, realizing that it's actually quite simple. If I can hit two bottles in the bottom row at the same time, it's an easy win."

            "Already, a small crowd is beginning to gather, so the pressure is really on me. Nine more shots."

            play sound sfx_dropstuff

            "Winding up like a baseball pitcher, I throw as hard as I can and the bottles come tumbling down."

            show shizu behind_blank_ss
            show misha cross_laugh_ss
            with charachange

            show stuffedcat:
                yalign 0.5 xanchor 0.5 xpos 0.6
                easein 1.0 xpos 0.5
            with Dissolve(1.0)

            "Triumphantly, I claim my girlish cat doll prize and Misha laughs uproariously as if it was her who won it."

            "Shizune stares at me with her usual blank expression. It's clear she wants the doll too."

            show stuffedcat:
                easeout 1.0 xpos 0.4 alpha 0.0

            pause 1.0

            hide stuffedcat

            show shizu basic_normal2_ss
            with charachange

            shi "…"

            show misha hips_grin_ss
            with charachange

            mi "Hicchan, congratulations~! What are you going to do with that doll?"

            "There is no right answer. I have to tread carefully."

            hi "I… do not know."

            mi "Wellllll~ I'll take it, if you don't want it…"

            show shizu adjust_smug_ss
            with charachange

            shi "…"

            show misha cross_grin_ss
            with charachange

            mi "Unless you want to keep it for yourself, Hicchan. I didn't know you liked dolls. How delicate."

            hi "I don't. I have no use for this."

            show misha cross_smile_ss
            with charachange

            mi "Can I have it, then?"

            show shizu behind_blank_ss
            with charachange

            shi "…"

            "Their eyes are drilling into my soul."

            "This is a decision I don't want to make. I turn back to the booth."

            hi "Hey, you have more than one of this doll?"

            "Shiraki" "Actually, yeah, just one more."

            hi "Okay, set everything up again, I want to try for that one as well."

            "I still have eight tries."

            play sound sfx_pillow

            "As soon as the game is set up again, I throw as hard as I can again, but miss."

            show misha hips_grin_ss
            with charachange

            mi "Hahaha! Trying to win another one? Taking the easy way out, Hicchan?"

            hi "If it's that easy, you could try it."

            mi "No thanks~!"

            show misha perky_smile_ss
            with charachange

            mi "Say, Hicchan, can you at least put the doll down while you throw the balls?"

            hi "No."

            show shizu adjust_smug_ss
            with charachange

            shi "…"

            mi "There's only one more left, you had better get it! If you fail, I'll kill you~!"

            show shizu behind_smile_ss
            with charachange

            shi "…"

            mi "What a clever way to duck out of giving me the doll, though! And by me, I mean me~!"

            show shizu adjust_happy_ss
            with charachange

            shi "!"

            show misha cross_laugh_ss
            with charachange

            mi "Ahahahaha~! Just kidding!"

            "I can see Misha didn't mean any harm from it, and Shizune seems to enjoy her joke, smiling at it, but she looks a little depressed afterwards."

            "I decide to hand her the doll, at least while I'm trying to win the other one. It's kind of hard to aim holding a giant cat."

            show shizu behind_smile_ss
            show misha perky_smile_ss
            with charachange

            shi "…"

            mi "Thank you, Hicchan. Shicchan seems happy, Hicchan~! But, you're going to win one for me, too, right?"

            hi "That is what I'm trying to do, isn't it?"

            stop music fadeout 5.0

            show shizu:
                easeout 1.0 xpos 0.8 alpha 0.0
            show misha:
                easeout 1.0 xpos 0.2 alpha 0.0

            pause 1.0

            hide shizu
            hide misha

            play sound sfx_pillow

            "I throw again, but my aim is way off this time."

            "My arm feels kind of heavy as well, as if blood isn't flowing to it properly."

            "I scold myself mentally, thinking that it's pathetic I could get tired from something like that."

            "Then I realize maybe it's because of my heart. If it is, then I don't know what to think."

            play sound sfx_impact

            "It's depressing that even something as small as this is enough to make me realize my own mortality."

            "I guess there won't ever be a time when I'll be able to forget about it."

            "Even today, when I thought I would be able to just enjoy myself, on this beautiful night and in this beautiful place, I can't escape the reason why I'm here."

            "I've never felt so at peace in my life, in this place which is like nowhere else I've ever been."

            play sound sfx_pillow
            play music music_sadness fadein 2.0

            "It's hard now to keep from thinking the unthinkable:"

            "That I may just have been sent here to die."

            "These past few days have been some of the best of my life. The first time in a long time that I've ever felt truly alive."

            "But in the end, I'm someone who finds himself reminded every time he climbs too many stairs or throws a ball too hard that he could die at any second."

            play sound sfx_pillow

            "I'll always be limited by this."

            "I feel depressed by that, and angry as well. In the end, I care about my life, and I enjoy it, and now it's more transient than ever before."

            "I wonder what it is that will finally do me in. It could be anything, if I'm this weak and pathetic: a bad fall, a punch to the chest, a stray baseball."

            "I've now lost my will to keep playing this game, but I keep playing anyway."

            stop music
            $ renpy.music.set_volume(0.0,0.0, "ambient")
            play sound sfx_heartfast

            show heartattack alpha
            with Dissolve (0.1)

            hide heartattack alpha
            with Dissolve (0.7)

            "Suddenly, I feel a split-second sensation of pain in my chest. It comes and goes instantaneously, but it's enough to make me stumble just a bit."

            $ renpy.music.set_volume(0.4,10.0, "ambient")

            show shizu adjust_blush_close_ss:
                xpos 0.8 xanchor 0.5
                ease 0.5 tworight
            show misha perky_confused_close_ss:
                xpos 0.2 xanchor 0.5
                ease 0.5 twoleft
            with Dissolve(0.5)

            show shizu at tworight
            show misha at twoleft

            "Shizune jumps back, startled. She comes closer, staring at me with concern. Misha puts her hand on my shoulder."

            play music music_pearly

            mi "Hey, Hicchan, are you okay?"

            hi "Yeah, I'm fine. I don't really feel too good right now. I think I'm sick. I don't think I can go on."

            show misha hips_frown_close_ss
            with charachange

            "Misha frowns."

            mi "Don't strain yourself. If you're that sick, you'll just make yourself sicker."

            show shizu basic_normal2_close_ss
            with charachange

            shi "…"

            show misha hips_smile_close_ss
            with charachange

            mi "Look, the festival is just getting started, and we've been playing games for a while. We can take a little break if you're tired."

            show misha sign_smile_close_ss
            with charachange

            mi "Good idea, Shicchan, I'm feeling a little tired too! I think we're all a little worn out, running all over the school, Hicchan!"

            "I nod. They don't seem to notice anything unusual. That's good."

            scene bg school_courtyard_ni
            show crowd_ni
            with shorttimeskip

            $ renpy.music.set_volume(1.0,2.0, "ambient")

            "We walk through the sea of people, with Misha cheerfully pointing out the faces of everyone she knows. Shizune holds the stuffed cat in her arms, cradling it absentmindedly. It seems like they're having fun."

            "Suddenly, I feel a pang of guilt."

            "Because of my poor health, we all had to stop."

            show shizu behind_smile_ni at tworight
            show misha perky_smile_ni at twoleft
            with charaenter

            shi "…"

            mi "Hicchan, we're both feeling kinda hungry. How about you?"

            hi "I'm not as hungry as I could be, but I do want something to eat."

            show misha hips_smile_ni
            with charachange

            mi "That's good enough, Hicchan~! So, what should we get to eat?"

            hi "It doesn't really matter to me."

            show shizu adjust_happy_ni
            with charachange

            shi "…"

            show misha hips_grin_ni
            with charachange

            mi "Ah! How about sandwiches, then? And we'll need something to drink, too! Misha'll get everything!"

            show misha perky_confused_ni
            with charachange

            mi "What?"

            show shizu behind_smile_ni
            with charachange

            "Shizune looks at me and smiles, and I realize she might be trying to cheer me up with a joke. I laugh."

            show shizu adjust_happy_ni
            with charachange

            shi "…"

            show misha perky_smile_ni
            with charachange

            mi "Hicchan, it's getting kind of crowded, so we might not be able to eat here. It's getting kind of loud, too."

            show misha sign_smile_ni
            with charachange

            mi "Maybe we should go eat up on the roof."

            hi "That's fine with me. It might be a nice view, and there could be a little breeze."

            show misha hips_grin_ni
            with charachange

            mi "Okay then! I guess I should get the food and drinks now… So I'll see you two then~!"

            hide misha
            with charaexit

            stop music fadeout 6.0

            "Misha gives a clumsy wave and then runs off."

            "Before, I didn't notice how the paper lanterns look illuminating the dark night, but now that I'm able to see it, it's really an amazing sight."

            "Fireflies float overhead, their soft glow making it look as if it's snowing lights in the night sky."

            "This type of thing would be impossible to see in the city."

            show shizu cross_angry_close_ni at center
            with Dissolvemove(0.5)

            "Shizune tugs at my sleeve impatiently and crosses her arms, frowning as if to show displeasure at me for getting distracted."

            show shizu basic_angry_close_ni at center
            with charachange

            shi "…"

            hi "You know I don't know how to read sign language."

            show shizu behind_frown_close_ni
            with charachange

            shi "…"

            "Come to think of it, isn't it kind of stupid of me to have said that to a deaf person? She wouldn't have heard it."

            show shizu behind_blank_close_ni
            with charachange

            "I shrug, hoping to show her that I don't understand. Shizune shakes her head and dismisses it with a wave of her hand."

            "Maybe I should get around to asking Misha for some lessons on sign language."

            $ renpy.music.set_volume(0.3, 1.0, "ambient")

            scene bg school_roof_ni
            with locationskip

            "Climbing up onto the roof, I find myself in awe again at the sheer size of this school. The grounds are so expansive I can't believe I hadn't realized it before."

            "As I walk across the roof, trailing behind Shizune, I can't help but be taken in by the stars shining in the sky."

            show shizu behind_smile_close_ni at center
            with charaenter

            "Shizune and I sit down on a bench. She seems like she's in a good mood as she smiles softly while the breeze blows through her hair."

            "We look down at the festival, which looks like a sea of glowing amber lanterns and waving paper fans teeming with people, some of them festively dressed in yukata."

            "In fact, most of the girls seem to be wearing yukata. I wonder why Shizune and Misha didn't dress up today."

            "The two of them would look nice in yukata. I briefly think about what types they would wear."

            "Shizune would likely go with something traditional. However, Misha is a bit harder to place."

            "Misha arrives, panting as she runs to us, trying to keep the food in her arms from falling."

            "Setting everything on the ground, she lets herself drop backwards."

            show shizu at tworight
            show bg at bgright
            with charamove

            show misha hips_grin_ni behind shizu at twoleft
            with charaenter

            mi "Ahahahahahahahahaha~! That took awhile! Come on, you two didn't tell me what you wanted, so I got some rice punch, some sandwiches, and some candy, too! A little bit of everything!"

            hi "That's great. Let's dig in."

            "Misha takes a bite out of a small, triangular sandwich."

            show misha hips_smile_ni
            with charachange

            mi "So, Hicchan, what do you think of the festival? It's nice, isn't it?"

            hi "Yeah."

            show shizu adjust_happy_close_ni
            with charachange

            shi "…"

            mi "The stars are nice tonight. This couldn't have been a more perfect day."

            play music music_serene fadein 5.0
            $ renpy.music.set_volume(0.1, 2.0, "ambient")

            scene bg misc_sky_ni:
                xalign 0.0
                warp acdc_warp 30.0 xalign 1.0
            with locationchange

            "The sound of people talking below us is like faint music alongside the chirping of crickets in the distance."

            "I take a sip from the can of punch and look over at Misha, who looks as if she's sleeping comfortably with her back stretched out and a half-full can of apple juice balanced on her stomach."

            "Shizune sits with her legs drawn close to her, rocking back and forth slowly like an impatient child as she stares up at the sky."

            "The two of them are so cute. I look around and can see many students holding hands with their girlfriends or their boyfriends."

            "Not too far from us on this roof, there are couples gazing up at the stars or down at the lights of the festival, holding each other's hand."

            "A part of me wants that."

            "Looking at Shizune and Misha, I wonder if maybe I should ask one of them out some day. I wonder if it would be worth the risk."

            "The golden hands moving across the face of the delicate watch on Shizune's wrist catch my eye, and I see that it's getting kind of late. But the festivities are still going strong."

            "Shizune is still holding the stuffed cat I won by the paw. She notices me looking at it."

            shi "…?"

            "Offhandedly, she offers it to me. I smile, wanting to ask her what I would do with it, but she wouldn't be able to understand me."

            "I shake my head and try my best to tell her to keep it, hoping she'll understand."

            "As I look out towards the school, I can see before me so many people, all of which are happy and cheerful."

            "Watching them makes me feel content."

            "This really was something. Today was worth it."

            "But I still can't shake the feelings of guilt and melancholy from earlier, they keep hanging onto me, and I can't let them go."

            "Shizune signs something to me, and I can't understand her. No matter what I say, she won't be able to hear me."

            hi "I can't understand you, Shizune."

            hi "Well, whatever. I wonder if we both consider ourselves at fault for this. Anyway, I'm sorry for not being able to understand."

            hi "You know, I'm almost, almost glad that you tried to coerce me into coming here. If I attempt to date you, though, I might have to think more about that side of you."

            hi "No, actually… I'm glad. Today was nice."

            hi "You would be cuter if you smiled more, you have a nice smile."

            stop music fadeout 5.0

            show shizu behind_frustrated_close_ni at center
            show bg at right
            with charaenter

            "Frustrated, she stands up, arms behind her back, looking authoritative and confident against the backdrop of stars."

            stop ambient fadeout 2.0

            show shizu out_serious_close_ni
            with charachange

            "Suddenly, Shizune throws her arms out towards the open sky, seeming to hold it between her hands."

            "It's as if she's telling me to look at everything in front of me:"

            show shizu epictransition at epictransform
            show cityscape zoom behind shizu
            show hill enter behind shizu

            "The school, bathed with the festival's glow and lit up with the colorful yukata, the roof illuminated by fireflies, the sky so vast that it imposes the feeling of awe onto you."

            "What does she want? It slowly dawns on me with time. This beautiful scene before me is proof that there are things wonderful enough that spoiling them with a bad mood would be unforgivable."

            "And I can feel the weight of Shizune's personality pressing the point further."

            hi "Thanks, I guess."

            hide shizu
            show hill pairtouch
            with charachange

            "I look away, but then Shizune grabs me by the shoulder, her watch brushing against my cheek."

            "With her left hand, she points up at the sky."

            play ambient sfx_fireworks fadein 1.0

            show fireworks behind hill
            show fw_screen behind fireworks
            with Dissolve(5.0)

            "With faint pops, fireworks begin to go off in the sky, each one spreading a shower of bright colors that slowly fade into the dark."

            "I can't even recall the last time I saw fireworks at all, much less a display this large. Not to mention it seems that they're being launched from the school; it's almost impossible to believe."

            "The lights in the sky mingle with a second salvo from the town below, and they seem timed to complement each other like two parts of a duet."

            "They continue for maybe fifteen more minutes, and then stop."

            "Shizune realizes her hand is still on my shoulder and withdraws it carefully, looking a little uncomfortable."

            stop ambient fadeout 5.0
            hide fireworks
            hide fw_screen
            show hill pairnotouch
            with Dissolve(5.0)

            "Regaining her composure, she grins, with her hands on her hips and her chest thrust out in front of her."

            "It's in these moments that she seems most like a regular teenage girl. Energetic, happy, and carefree."

            "I eat thoughtfully with Shizune, the two of us looking out at the gradually thinning crowds below in silence."

            "She sits leaning forward slightly, her chin resting softly on her hands and a contented look on her face with just a hint of wistfulness."

            "All the while still gently holding on to the stuffed cat's paw."

            "I start feeling tired and I tell her that I'll see her and Misha tomorrow, without even realizing that she can't hear me, and then start walking back to the dorms."

            "I feel warm and alive, even in this chilly night air."

            stop music fadeout 4.0

            "The image of Shizune standing forcefully before the stars themselves, denying my self-pity, does not leave my mind easily."

            "If… if it only takes a moment for there to be love, I think I may be falling in love with her."

            "Just a little bit."

            if _in_replay:
                return

    if force_route == FR_KENJI:
        label .the_deep_end:
            scene bg school_dormhallway at bgright
            show kenji happy at center

            stop music fadeout 2.0

            "What am I going to do? I don't have any plans. In hindsight, that's really stupid."

            "Maybe I should've asked a girl out? Then again, all things considered, I don't think I could've done anything like that. It's only my first week."

            "A week that I have wasted being awkward around almost everyone, stumbling all over myself trying to get the hang of this place."

            "Thinking about it, what have I accomplished?"

            "Who would I have even asked?"

            "Damn, it seems that Kenji is my only realistic option for a date today."

            "This is the most depressing thing that has happened to me since I had a heart attack because a girl confessed her love to me."

            "It can't be helped."

            play music music_kenji fadein 0.5

            hi "I don't know really. I don't have anything I guess, but a fort seems a bit excessive."

            hi "You sure you don't want to go outside? It's not like visitors won't come to the dorms today."

            show kenji tsun
            with charachange

            "He looks thunderstruck by this revelation."

            ke "Damn, you may have a point. This place is not safe today."

            ke "We must find somewhere to hide in."

            "He falls silent for a moment, thinking."

            show kenji neutral
            with charachange

            ke "The roof."

            hi "What about it?"

            show kenji happy
            with charachange

            ke "We are going to hide out on the roof for today."

            ke "It's the perfect place, nobody ever goes up there."

            show kenji neutral
            with charachange

            ke "Meet me there in one hour. I have to prepare."

            stop music fadeout 1.0

            show kenji neutral:
                easeout 0.5 xpos 0.4

            hide kenji
            with charaexit

            play sound sfx_doorslam
            with vpunch

            "He slams the door shut and the locks click closed."

            "Damn, what the hell is wrong with Kenji?"

            "And to think I'm now going along with his craziness. It really makes me depressed."

            "I feel like a failure."

            play ambient sfx_crowd_outdoors fadein 0.3

            scene bg school_courtyard
            show crowd
            with locationskip

            "Once I step outside, the din of the crowd greets me."

            "The whole school is bustling with activity."

            "There are stalls everywhere, and the crowd swarming between them is considerable."

            "I didn't expect the festival would attract so many visitors."

            "I have to admit that the people in charge of decorating the place put a lot of effort into it, and it really shows."

            "People seem to be enjoying themselves, and the atmosphere is colorful, bright, and happy."

            play music music_rain fadein 1.0

            "That is, if I weren't suddenly in such a foul mood."

            "At the moment, it's more annoying than anything else."

            "Well, it can't be helped. I decide to stick with my original plan and eat, then I guess I have to at least see what Kenji is up to on the roof."

            "…"

            scene bg school_stalls2:
                xalign 0.0
                warp acdc_warp 8.0 xalign 1.0
            with locationchange

            "I do a slow circle around the grounds to kill some time, looking at the stalls, but not feeling like playing any of the games any more."

            "The garish colors grind my eyes and I feel more and more ill by the minute."

            "I can't even decide what I want to eat, and the large selection combined with the masses of energetic festival visitors isn't helping."

            scene bg school_stalls1 at bgright
            with locationchange

            "I just head towards the nearest stall that seems to offer something halfway edible and get in line."

            "It turns out to be noodles."

            "It also turns out to be not very good."

            "Well, at least it's nourishment. It's not like I demand anything else, at this point."

            scene bg misc_sky:
                xalign 0.0
                warp acdc_warp 25.0 xalign 1.0
            with locationchange

            "As I stir my disagreeable noodles, I idly wonder what the others are doing right now."

            "Shizune and Misha are definitely somewhere organizing things."

            "I'd better steer clear of them. I guess they wouldn't forgive me so easily for leaving them alone with this thing."

            "I expect Emi to be buzzing all over the place, being depressingly cheerful."

            "There's no chance to find her, but no chance to avoid her either, so it doesn't matter."

            "Lilly would probably be helping her class with that festival event, and entirely too busy for another's company."

            "Hanako wouldn't want to talk to anyone anyway, either keeping to herself or helping Lilly."

            "Rin should be tending to her mural and is probably being unhelpful to any hypothetical interested parties."

            "Going there for some peace and quiet seems like the nicest option of the above, but then again, I can't see having art forced on me raising my mood either, so I'll pass."

            scene bg school_stalls1 at bgright
            with locationchange

            "While I was lost in thought, my food seems to have disappeared, and so has my hunger."

            "I guess I just blocked out the experience of eating, which should be a good thing."

            "Satiated but unsatisfied, I turn to walk towards the main school building. An hour has almost passed already."

            play ambient sfx_crowd_indoors fadein 0.3

            scene bg school_lobby
            show crowd
            with locationskip

            "The crowd is even thicker in here than it was outside."

            scene bg school_hallway3
            show crowd
            with locationchange

            "The hallways are almost unbearable, and I don't even dare to think what's it like inside the classrooms."

            stop ambient fadeout 1.0

            scene bg school_staircase1
            with locationchange

            "I head up the stairs to my destination."

            "The roof."

            "Thankfully, the door at the top isn't locked, but now there's a handwritten sign on it."

            call screen written_note(_("{size=55}{b}OFF LIMITS{/b}{/size}"), quiet=True)

            "Don't mind if I don't."

            scene bg school_roof at bgright
            with locationchange

            "The festival noise is surprisingly muted up here, and the rooftop looks deserted, as expected."

            "Near a place where the cyclone fence has collapsed, there is a pile of blankets that seems oddly out of place."

            stop music fadeout 3.0

            "Wait."

            play sound sfx_rustling

            "Did that pile just move a little?"

            "That would be strange, as there is no wind at all."

            "I carefully stick my hand out and give it an experimental prod."

            play sound sfx_impact
            show kenji rage_close:
                alpha 0.0 xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.7
                easein 0.2 yanchor 1.0 alpha 1.0
            with vpunch

            call screen doublespeak(ke, _("Hello."), hi, _("AHHHHHHHHHHHHH!"))

            play music music_comedy fadein 2.0

            show kenji rage at center
            with charadistant

            "Startled, I jump back."

            ke "Who is it?"

            hi "God damn it, Kenji. It's me."

            show kenji tsun
            with charachange

            ke "Oh damn, you scared me, man."

            hi "So what are we doing up here?"

            show kenji neutral
            with charachange

            ke "We're having a picnic."

            hi "What?"

            show kenji happy
            with charachange

            ke "Yeah. I have blankets, pretzels and whiskey. This is the ultimate setup, man."

            hi "Whiskey?"

            hi "Aren't you a bit too young to drink alcohol?"

            show kenji tsun
            with charachange

            ke "I'm 20, y'know."

            hi "…you're not."

            show kenji neutral
            with charachange

            ke "I am and so are you."

            hi "What? That's absurd."

            show kenji tsun
            with charachange

            ke "Hey, at least YOU get something out of it, all I get is this bottle of whiskey…"

            "He's rambling incoherently, but I decide to play along."

            hi "So why do you have a bottle of whiskey?"

            show kenji happy
            with charachange

            ke "My mom couldn't come visit for the festival, so she sent me some expensive Single Malt instead."

            hi "A likely story."

            ke "Want some?"

            hi "…"

            "It's not like I have anything to lose. This day can't possibly get worse."

            hi "…why not."

            hide kenji
            with charaexit

            show bg at center
            with charamove_accel

            show kenji happy_close at offscreenleft
            with None

            show kenji at twoleft
            show bg at bgleft
            with charamove_decel

            "We sit down on the pile of blankets Kenji apparently dragged up here."

            "He produces an almost full bottle of whiskey and passes it to me."

            hi "You didn't even bring glasses?"

            show kenji tsun_close
            with charachange

            ke "No, this is not some romantic princess picnic. What the hell, man?"

            show kenji neutral_close
            with charachange

            ke "This is a manly picnic."

            ke "No glasses."

            ke "No napkins."

            ke "Whiskey only. The beverage of true men."

            hi "Whatever."

            show kenji happy_close
            with charachange

            ke "And pretzels."

            "I take a closer look at the bottle."

            "12 year old single malt whiskey, as he said."

            "Shrugging my shoulders, I take a swig. It burns my throat like acid, but the taste isn't unpleasant."

            "I feel it going straight into my head, and the aftertaste lingers in the back of my mouth, craving for another swig."

            show kenji neutral_close
            with charachange

            ke "We should outline our counteroffensive and trashtalk women here, where they can't hear us."

            show kenji tsun_close
            with charachange

            ke "Damn, I forgot to bring my graphs."

            "I decide to play a drinking game with myself. Every time Kenji mentions 'female conspiracy', I'll take a swig."

            stop music fadeout 2.0

            scene black
            with delayblinds

            centered "Four or five hours, or possibly several days later:\n{w}(I lost track)"

            play music music_kenji fadein 0.5

            scene ev kenji_rooftop
            with delayblinds

            ke "You shouldn't feel bad, man! Ease the fuck up! Seriously, seriously!"

            hi "I am relaxed, god damn it!"

            ke "I'm telling it as I see it!"

            scene ev kenji_rooftop_kenji
            with flash

            ke "Think about it. When did housing and land start becoming more and more expensive? When women began entering the work force, because it created two-income nuclear families."

            ke "Yeah I forgot my graphs, but, and you'll just have to take my word for it, women are connected to the decay of all society."

            show ev kenji_rooftop_large:
                crop (691, 602, 1920, 1080)
                ease 1.0 crop (2458, 416, 1920, 1080)

            hi "I see. That is kind of hard to believe."

            "Even if I say that, somehow, everything Kenji says seems to make more sense now."

            "It all fits together but I don't know if it's because he can explain things more clearly when drunk, or because I understand everything better when drunk."

            show ev kenji_rooftop_large:
                ease 1.0 crop (691, 602, 1920, 1080)

            ke "No man, think. Think! Think of the deeper implications!"

            ke "People could afford to start saying 'Oh well, since two members of the family are now earning money as opposed to one, they can surely afford something like rising costs of ownership.'"

            show ev kenji_rooftop_large:
                ease 1.0 crop (2458, 416, 1920, 1080)

            hi "I see your point. But land in Japan has always been expensive."

            show ev kenji_rooftop_large:
                ease 1.0 crop (691, 602, 1920, 1080)

            ke "…And the price of land generally goes up when a country starts undergoing industrialization. …But no! It's because of women! Correlation equals causation, you know."

            show ev kenji_rooftop_large:
                ease 1.0 crop (2458, 416, 1920, 1080)

            hi "I thought correlation didn't equal causation. Well, whatever, maybe you're right."

            show ev kenji_rooftop_large:
                ease 1.0 crop (691, 602, 1920, 1080)

            ke "I am always right. Yeah, I bet women created industrialization, too, to cover their tracks."

            ke "How diabolical."

            ke "So yeah, everyone can go fuck themselves!"

            scene bg school_roof_ni
            show kenji rage_ni:
                xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.9
                easein 1.0 center
            with locationchange

            show kenji at center

            "He stands up, impressing me because I'm fairly sure I couldn't even if I wanted. He yells extremely loudly as if he's lost the concept of volume. I wince and almost want to cover my ears."

            stop music fadeout 2.0

            ke "Aaagh, how nice it would have been if I could have been down there… But no. You see, thinking like that is a trap, you think you're missing out on something, but at the end of that road is nothing but despair…"

            show kenji tsun_ni
            with charachange

            play music music_sadness fadein 1.5

            "Kenji snatches back the bottle and leans back his head, attempting to pour the alcohol into his mouth, but just ends up drenching himself in it."

            show kenji rage_ni
            with charachange

            ke "Dammit! See, my aim is terrible, and the bad thing about drinking is that it only gets worse the longer you go!"

            show kenji tsun_ni
            with charachange

            ke "Today is the day of despair."

            "His voice immediately drops to almost a whisper, but he starts talking much faster than before, slightly slurring his words from the whiskey."

            "As he talks, he waves the bottle around, spilling some of it here and there."

            ke "Yeah, you know what was the most shocking event of my life?"

            "I have a hazy recollection of him telling about the second most shocking event in his life, which was a bird pooping on his head."

            "I don't have particularly great expectations of this, but I nod at him to continue anyway."

            show kenji neutral_ni
            with charachange

            ke "You wouldn't think it, but I had a girlfriend here once, I think it was last year."

            ke "Yeah, I just blew your mind, huh? See, I have never told that to anyone."

            "It's true, the thought does blow my mind. Suddenly, I want the bottle. I take it from Kenji and knock back as much as I can."

            show kenji tsun_ni
            with charachange

            ke "I was more innocent back then, and I thought she was sane, unlike most women. But then one day, we engaged in… sexual intercourse."

            ke "It was pretty okay, but then immediately following the event that is the point of all such things, something strange and scary happened."

            show kenji at tworight
            show bg at bgleft
            with charamove

            "He throws himself up against the fence, leaning on it, his eyes narrowed."

            ke "I started feeling incredibly tired and sleepy! That isn't normal, man! What the fuck?"

            ke "I mean, normally, that would be a high-tension, adrenaline-pumping moment of anyone's life, but my energy levels were dropping like a brick!"

            ke "Something sinister was in the works, I could feel it."

            ke "That is when I knew… that women are dangerous, sapping the life force of all men through the one commodity that is almost solely theirs to control!"

            ke "Sickening."

            show kenji neutral_ni
            with charachange

            ke "Yeah, you're better off, dude…"

            "Kenji was right, this really is the day of despair. I drink more to avoid having to process what he just said."

            ke "Now I am the last sane man in an insane world… when other people realize it, there will be a war, a great war between men and the forces of feminism."

            ke "But the problem is that not all men would fight on my side… shit sucks. I could set the bar kinda low, any men are fine. But not the dudes raised by their mom or their sister, that's for sure."

            show kenji tsun_ni
            with charachange

            ke "And nobody into dickgirl porn."

            hi "Ha… That situation seems unlikely to me, like it wouldn't happen, like… like it's not very likely to happen."

            "The alcohol must be working."

            "Regardless, I still feel depressed that I'm up here today."

            "I wasn't really looking forward to the festival with the same excitement as the rest of the school, but still."

            "It would have been nice to have gone with someone. From up here, it certainly sounded like everyone's having fun. Maybe I am missing out."

            "It's just that there was no one I could have gone with."

            "Or maybe there was. So many opportunities, looking back on it now, and I must have squandered so many of them."

            ke "Damn, this is true despair… The worst part is that sometimes I feel like I have no choices in my life, you know?"

            ke "Like I never have a chance to make a decision, shit just happens."

            ke "Like it was all preprogrammed. Like fate… or something. Like there is no way I can have a say in what I do."

            stop music fadeout 0.2

            show kenji rage_ni
            with vpunch

            ke "Quick, ask me a question!"

            hi "Uh…"

            ke "Now!"

            hi "I can't really…"

            show kenji tsun_ni
            with charachange

            ke "See? This is just another example of it! Damn! Shit! Damn! Do you see? Now, when I'm trying to go against my destiny and take charge of my life, the opportunity isn't even there."

            ke "Damn, man, you have failed me. Failed me for the last time. Jerk."

            show kenji:
                easeout 0.7 ypos 0.9 yanchor 0.5

            pause 0.8

            show kenji:
                easeout 0.7 rotate 90 ypos 1.0 yanchor 0.3

            pause 0.7

            play sound sfx_impact
            with vpunch

            hide kenji

            "He slides to his knees and then falls over onto his side, lying on the gravel of the roof."

            hi "Hey, are you okay?"

            ke "No, I'm not okay, can't you see I'm in despair?"

            "He's speaking in a sarcastic tone."

            show kenji neutral_ni:
                xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.0
                easein 0.5 ypos 1.0 yanchor 0.7

            pause 0.5

            "Suddenly, Kenji sits up, clumsily pats himself clean, and puts his hand out towards me to reach for the bottle. I put it in his hand."

            show kenji tsun_ni:
                xpos 0.7 xanchor 0.5 ypos 1.0 yanchor 0.7
            with charachange

            ke "What the hell? Damn, you killed almost the entire bottle. See, it's like I have no options in life…"

            ke "Is this how it's going to be for the rest of time?"

            hi "Well, I'm pretty sure it's not going to be like that for the rest of time."

            "Whatever he's talking about. My head is spinning. I get up and lean against the fence, hoping it'll help me focus a little."

            show kenji at center
            show bg at center
            with charamove

            ke "Yeah, I know. We have to fight the power with all we got. It's the only way to live."

            play music music_one fadein 6.0

            show kenji neutral_ni
            with charachange

            ke "You're an all right guy."

            show kenji happy_ni
            with charachange

            ke "This brotherly bond is what keeps me going in these dark times."

            show kenji neutral_ni
            with charachange

            ke "We should go trolling women."

            hi "Rolling women? What?"

            show kenji neutral_close_ni
            with characlose

            ke "Trolling women. Trolling for women. But we have to do it now, before I lose this alcohol-related courage."

            "He's gesturing wildly. Madly, even."

            show bg:
                yalign 0.75
            show kenji neutral_ni:
                xpos 0.3
            with Dissolvemove(0.5)

            "I take a step backward."

            show kenji neutral_close_ni at center
            with Dissolvemove(0.5)

            "He takes a step forward."

            show kenji happy_close_ni at center
            with charachange

            ke "What's the matter with you? Not in the mood for love?"

            hi "To be frank… no."

            show bg:
                xalign 1.0
            show kenji happy_ni:
                xpos 0.3
            with Dissolvemove(0.5)

            "I take another step backward."

            show kenji happy_close_ni at center
            with Dissolvemove(0.5)

            "He takes another step forward."

            "He leans in extremely, uncomfortably close."

            hi "What the hell, stop leaning in like that, it bothers me."

            ke "Leaning in like what? Hey, you shouldn't lean against the fence like that, it's kind of unsafe."

            "I try to move away from Kenji, but my balance isn't so good."

            "Reeling from the dizziness, I grab at one of the fenceposts, but then feel it give way as soon as I put my weight on it."

            "…This isn't good. Though my alcohol-addled brain doesn't seem to be quite capable of registering why."

            show black behind bg

            show n_vignette:
                xalign 0.5 yalign 0.5 zoom 4.0
                linear 0.2 zoom 1.2

            pause 0.2

            show n_vignette:
                zoom 1.2
                linear 8.0 zoom 0.001
            show kenji happy_close_ni:
                xalign 0.5 yalign 0.5
                linear 8.0 zoom 0.001
            show bg school_roof_ni_crop:
                xalign 0.5 yalign 0.5
                linear 8.0 zoom 0.001

            "Kenji's face seems to be becoming smaller though, which is a bit of a relief."

            "Much smaller, in fact. And rapidly so."

            show nightsky rotation

            "There seems to be a bit of wind now. Somehow it makes me feel almost weightless."

            "I feel dazed, like my mind has gone blank."

            hi "I am… falling…?"

            "I can see the night sky as I turn over in the air. The bottle floats out of my fingertips and disappears into thin air as I fall."

            "I realize that this is the fitting end to a truly, truly bad day."

            stop music fadeout 0.1
            play sound sfx_crunchydeath

            if _in_replay:
                return

    return

label stranger_lilly_and_hanako:
    scene bg school_dormhallway at bgright
    show kenji happy at center

    hi "I don't know. I'm pretty hungry so I thought I'd get some food first and then check out the attractions."

    hi "Your class project seemed pretty cool, and I gave a hand with it so I want to see at least that one and chat with Lilly I guess."

    hi "Speaking of that, don't you have any obligation for the project?"

    show kenji rage
    with charachange

    ke "Are you out of your mind?"

    ke "That blind broad is up to no good; I can feel it in my spleen, man. Her presence is like a dark shadow that's in the way of my great vision."

    ke "As expected of blind people."

    hi "What."

    hi "Besides, I thought that you were also…"

    show kenji neutral
    with charachange

    "He holds up his hand to interrupt me."

    ke "Only legally."

    ke "Metaphorically, I can see farther than any man before me has seen."

    "Kenji looks stoically into the metaphorical distance to emphasize his statement, thrusting his chin forward to look manlier. Actually it's just the corridor wall two meters away but it's all the same."

    show kenji tsun
    with charachange

    ke "I can see the future of mankind, and it's a dark one unless the threat of women is stifled."

    ke "They are everywhere."

    return

label stranger_union:
    "He fingers his scarf nervously, faster and faster like he is trying to start a fire, then slowly begins to calm down once the panic attack finishes running its course."

    show kenji neutral
    with charachange

    ke "I'm going to have to find some place to hide in, a safe haven. And then knock the lights out of myself so that I don't have to experience this horrible day."

    ke "I have the perfect thing for that. I must prepare now."

    show kenji tsun
    with charachange

    ke "Don't go to the festival."

    hi "Okay."

    show kenji neutral
    with charachange

    ke "Later, dude."

    stop music fadeout 2.0

    hide kenji
    with charaexit

    "The door slowly closes with a low creak and I don't know how to feel about what Kenji just said."

    return

label lilly_and_hanako_union:
    scene bg school_gardens
    with shorttimeskip

    $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
    play ambient sfx_crowd_outdoors fadein 0.5
    play music music_soothing fadein 0.5

    "After buying a plastic plate of takoyaki from a stall belonging to the class next to ours, I take a seat in the school gardens and watch people pass as I tentatively nibble away at the rather bland-tasting item."

    "I guess I shouldn't complain. It's better than nothing and didn't cost much."

    "As I look out towards the school, watching the people coming and going proves a surprisingly entertaining way of passing the time as I eat."

    $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

    show bg school_courtyard
    show crowd
    with locationchange

    "Little children accompanied by parents or grandparents scamper about in the din from event to event; one hand dragging their company and the other bearing an oversized, colorful snack."

    "I can't help but notice the age range among the people here is skewed towards the elderly, something that I'd also noticed when I was walking around town."

    "This must be one of those towns where the only people left are those that lived here their whole lives and ardently refuse to leave, and those wanting to live out the rest of their days in one of the increasingly few tranquil places."

    "I guess that also goes a way to explaining how conservative Yamaku's school culture seems to be."

    $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

    scene bg school_gardens:
        xalign 0.0
        warp acdc_warp 8.0 xalign 1.0
    with locationchange

    "Not that I mind one bit. I kind of like how calm Yamaku and its surroundings are."

    "The heat, though, is another matter entirely. Sitting in one place for so long has focused my mind on how annoyingly humid it's getting, now that the hottest part of the day is here."

    "I'd better get moving if I—{w=.5}{nw}"

    play sound sfx_warningbell

    "Gah!"

    "The sound of the carillon bells takes me completely by surprise as I stand up, a reaction shared by a few of the people strolling around as well."

    "The PA system crackles to life after the tolling bells end. Its age shows as the principal makes a barely intelligible announcement over it, officially opening the festival that's very much in full swing."

    "It's quite amusing to contrast the pleasant smiles of the older folk against the alternatively pained and bored grimaces of their younger charges. The students, on the other hand, seem to pay it little heed."

    "Nevertheless, as the address finally ends, all are united in polite - if not overly enthusiastic - applause, and then get back to business."

    "Slipping a hand in my pocket to look as relaxed as possible, I casually glance around for something to do."

    "…It's somewhat difficult to see very far with all the people around."

    "I decide to fall back on a tried and trusted rule: go where everyone else seems to be gathering. Right now, that's the school courtyard and surroundings."

    play sound sfx_can_clatter

    "Throwing the used plate into a trash can, I make my way towards the school building."

    $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

    scene bg school_courtyard
    show crowd
    with locationchange

    "Seeing the number of stalls around the perimeter of the school building surprises me. Quite a few of the classes must have opted to have multiple stalls."

    "In deciding which to visit first, I catch sight of a familiar banner with a blue patterned border and red text."

    "Lilly's stall is as good a place to start as any. I'm curious as to how it's going, after all of the work she and her class have been doing for it."

    $ renpy.music.set_volume(0.5, 2.0, channel="ambient")

    scene bg school_stalls2:
        xalign 1.0
        warp acdc_warp 8.0 xalign 0.0
    with locationchange

    "Stepping up to it, I begin to see why the class took so long to organize everything."

    "Easily twice as wide as many of the other stalls and with equipment for cooking strewn everywhere, it's closer to an outdoor restaurant than a festival event."

    "As a student in front of me takes a bowl of noodles and leaves, I walk up to the counter."

    "The girl behind it seems quite exasperated, and asks me to wait a moment before she disappears underneath the counter."

    "Seizing the moment, I take a quick glance around."

    "Steam seems to be rising from everywhere, as pots and pans simmer away. The most blind of the students are unpacking ingredients while being helped by someone who is probably the teacher of 3-2."

    "It doesn't take long to notice Lilly among them, talking with the teacher as she quickly counts out the boxes and packets with her fingers."

    "From her expression and the fact that both she and the teacher seem to be in a state of mild confusion, it appears that there's been some problem in coordination."

    "Before I can stare any longer, the girl behind the counter pops up again, only to look back and ask where the spare change box is."

    "Lilly pauses for a moment, before she and the girl switch places at the counter and the teacher quickly walks off somewhere."

    stop music fadeout 2.0

    show bg school_stalls2 at left
    show lilly basic_smileclosed at center
    with charaenter

    li "Sorry about that, we're having a few problems. What would you like?"

    "It takes me a second to remember what I'd come here for. My eyes quickly dart to the side to read the menu sitting on the counter."

    hi "Oh, uh, I guess some… miso soup?"

    show lilly basic_surprised
    with charachange

    li "Ah, is that Hisao?"

    hi "Yep. Looks like you're pretty busy."

    play music music_ease fadein 6.0

    show lilly basic_weaksmile
    with charachange

    "Her face all but confirms it as she drops her waitress facade."

    li "Somewhere along the line, our order got mixed up. We're trying to fix it now, but it looks like we only have half of what we needed."

    hi "Wouldn't serving smaller portions cover over the problem?"

    show lilly basic_sad
    with charachange

    li "It seems like that's what we'll have to do, though I wish we didn't. The fact that a good half of our class is gone doesn't help, either."

    "I glance behind her to see how many people are actually operating the stall."

    "It couldn't be over about eight."

    hi "I take it that's why your teacher left?"

    show lilly basic_weaksmile
    with charachange

    li "That's right. She's going to try and round up a few more of our classmates to help."

    "Hearing the sound of footsteps behind me, I stealthily glance backwards to see an elderly couple taking a place in the line. I guess I'd better stop loitering around and chatting."

    hi "Here's the money for the soup."

    show lilly basic_smile
    with charachange

    li "Soup… oh, right, coming right up."

    "Lilly turns and calls for a bowl of miso soup as I hand over the money for it."

    show lilly basic_reminisce
    with charachange

    "Taking the coins in her palm, I can't help but notice how efficiently she counts them out with her long, pale fingers. Eventually satisfied that I've handed over correct change, she puts it into a small metal tray."

    show lilly basic_smileclosed
    with charachange

    "It isn't long before the soup is made and carefully handed to her, after which she turns and subsequently passes it to me."

    hi "Thanks. I'll come back to drop off the bowl."

    show lilly basic_smile
    with charachange

    li "Thank you, Hisao. Oh, there is one other thing. Have you seen Hanako?"

    hi "Hanako… no, not today. Why?"

    show lilly basic_sad
    with charachange

    "She gives a small sigh of abject disappointment."

    li "It's okay. I was just wondering what she was doing for the festival."

    show lilly basic_weaksmile
    with charachange

    li "You'll come back when you're done, then?"

    hi "Sure. I'll keep an eye out for Hanako, too."

    li "Thank you, Hisao."

    $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

    scene bg school_courtyard
    show crowd
    with locationchange

    "I walk off from the stall and find a seat, carefully cradling the steaming wooden bowl in both hands."

    "Compared to the dumplings from before, this is quite nice. A little cool compared to what it probably should be, perhaps, but the flavor is enough to cover for that reasonably well."

    "As I drink, I can't help but feel somewhat guilty for not being as involved in the festival as the others."

    "It can't really be helped, considering I was dropped into the school only a week ago, but it still weighs heavily on my mind."

    "That, and the fact that a few students don't really seem to be enjoying the festival as much as the visitors."

    "Eventually I finish my bowl and leave for the stall, to drop it off."

    "Considering that there seems to be no line at all, I take my time walking up."

    $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

    scene bg school_stalls2
    with locationchange

    "It seems the teacher's mission paid off: there are now over a dozen students helping, and much of the unpacking has been done."

    "Despite most of them seeming quite relaxed as they work, Lilly still appears to be somewhat stressed."

    return
