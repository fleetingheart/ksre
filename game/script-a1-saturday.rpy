# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a1_saturday:
    call timeskip

    if got_kenji() or not go_through_shizu():
        label .support:
            scene black

            scene bg school_scienceroom
            with Dissolve(2.0)

            play music music_normal fadein 3.0

            "The students roll into class for the Saturday morning session, each and every one of them sporting the tired eyes of people who have worked through the night."

            "With only a day left to prepare, I suppose it's not so surprising. Thankfully, we only have to suffer through classes until the lunch break, and then our time is our own."

            show muto irritated at center
            with charaenter

            "Mutou lurches into class in a tired stagger. I suppose students aren't the only people here that enjoy their late Friday nights."

            "Without saying a word, he scrawls some page and question numbers on the board and slumps down at his desk."

            "It's completely atypical behavior for him, but it appears that no one in the class is going to call him out on it."

            play sound sfx_paperruffling

            hide muto
            with charaexit

            stop sound fadeout 6.0

            "Wordlessly, the students shuffle their textbooks into position and get to work. Not wanting to break the trend, I do the same."

            "Fatigue has made the class antisocial; not a peep is heard among the ruffling papers."

            "That can partly be attributed to the two empty seats beside me. For some reason Misha and Shizune aren't present; probably doing council work for the festival."

            "It's very quiet without Misha present."

            "I wonder if she was born as rowdy as she is, or if she is 'making up' for Shizune's lack of voice."

            show muto normal at center
            with charaenter

            stop music fadeout 2.0

            mu "Nakai, can I speak to you for a moment?"

            "I'm so engrossed in thinking about Misha that I don't even notice Mutou approaching my desk."

            hi "Sure… what's this about?"

            mu "It's probably better if we speak outside the classroom…"

            play sound sfx_dooropen

            hide muto
            with charaexit

            "Something about this doesn't sound too good, but I stand up and follow him out into the hallway."

            play sound sfx_doorclose

            scene bg school_hallway3
            show muto normal at center
            with locationchange

            "Mutou stands in the hallway, scratching his head as he works out what he is trying to say. Not knowing what's going on, I wait silently."

            if get_tired() and not _in_replay:
                mu "I heard from the school's head nurse that you had an incident the other day."

                "Ah. So it's about that."

                hi "Well, kind of, but it's not anything to be worried about."

                show muto irritated
                with charachange

                mu "Yes, yes it is. Anything that can endanger your health is something to be worried about."

                mu "We try our best here to prepare you for life here. Part of that involves knowing your limits, and how to work around them."

                mu "It would be remiss of me if I didn't speak up about this."

                hi "All right, I get it. I'm sorry."

                "Mutou closes his eyes in frustration, and I realize that this probably wasn't the best thing to say."

                mu "Something tells me that you're not sorry. Pretend as much as you want, but this isn't a normal school."

                mu "A lot of people have put in a lot of time, effort, and money to make sure that you, and every other student here, can have the same level of education as your peers."

                mu "For you to abuse that by throwing out advice, especially medical advice, is plain selfish."

                "I'm not quite sure if this is actually how he feels, or if it is some act that he's practiced many times to guilt-trip students into doing the 'right' thing. Either way, it's working."

                hi "I understand. This is all new to me, and I apologize. I know my limits now, and I'll be sticking to them."

                show muto smile
                with charachange

                "Mutou appears to lighten up a little, satisfied that his message has been received."
            else:
                mu "So, tell me, how are things?"

                hi "Things?"

                "I expected Mutou to be a little vague, but this is pushing the limits."

                show muto irritated
                with charachange

                mu "You know. Things. You've had a week to settle in now, so how are things?"

                hi "Er, fine I guess."

                show muto normal
                with charachange

                mu "I see. And how is your… condition?"

                "The pause before 'condition' seemed a little unnecessary."

                hi "Haven't had any problems so far."

                show muto smile
                with charachange

                "A brief shimmer of relief passes across Mutou's face."

                mu "Good, that's good. The school nurse was a little concerned that you might have been pushing yourself a bit too hard."

                mu "He asked me to keep an eye on you when he couldn't."

                hi "That makes sense…"

                show muto normal
                with charachange

                mu "I'd ask that you don't blow us off so freely. As much as we try to give you the level of education that you would get at a normal school, you have to realize that you have limits."

                mu "Our goal is to make sure that you know where those limits are, and how to maximize your potential within them. Do you follow me?"

                hi "I guess. I mean, I don't plan on doing anything stupid."

                show muto smile
                with charachange

                mu "Well, that's a start, I guess."

            show muto normal
            with charachange

            play music music_normal fadein 3.0

            mu "So then, onto my next question; how are you finding your studies? I understand you were laid up for a while. We're not too far ahead, are we?"

            hi "I don't really think so. I tried to keep up when I was in the hospital, so it hasn't been too hard."

            show muto irritated
            with charachange

            "Mutou taps his chin and raises an eyebrow as he absorbs this information."

            mu "Is that so… I suppose there are still students out there who realize the importance of learning…"

            "I wouldn't go that far, I was only trying to keep myself occupied in my little life-support prison."

            hi "Well, yeah. You've got to keep up with these things, right?"

            show muto smile
            with charachange

            mu "That's exactly it. One wrong move in this world and you're left behind, right?"

            hi "Er, right. Wouldn't want that to happen."

            show muto normal
            with charachange

            mu "No, no you wouldn't. Every week there's a new scientific discovery. Most of them mean nothing to the layperson, but any one of them could be the key to the Next Big Thing."

            hi "I'll keep that in mind…"

            "It's obvious that Mutou's Serious Talk is over, and he's gone back to his standard, slightly scatterbrained approach to life."

            "I think, in hindsight, that I prefer him this way. He's slightly more predictable in his unpredictability."

            show muto smile
            with charachange

            mu "Well then, I think that's all I really had to say. Let's get back inside, shall we?"

            "My relief at that suggestion is insurmountable."

            hi "Sure. You're the boss, right?"

            show muto normal
            with charachange

            "Mutou pauses for a moment."

            mu "I don't think any of my students have ever said that to me before."

            "For an instant I consider replying to this, but something deep within me tells me to shut my mouth and get back into the classroom."

            play sound sfx_dooropen

            scene bg school_scienceroom
            with locationchange

            stop music fadeout 5.0

            "A few of the students jump at the sound of the door, rapidly trying to pretend that they are working on the questions on the board."

            play sound sfx_doorclose

            "Some don't even bother, their heads slumped on the desk as they nap. Thankfully, it would appear that Mutou does not even notice them."

            "He returns to his desk and retrieves a scientific journal from one of the drawers. I guess I got to him there."

            "The class returns to the near-silence that Mutou and I left it in before our chat."

            "Mixed feelings of tiredness and anticipation buzz around the room. Everyone here is either waiting for a chance to rest or the chance to get their last-minute preparations underway."

            play sound sfx_normalbell
            play music music_daily fadein 8.0

            "The clock on the wall slowly ticks the remaining class time away, until finally the bells cry out, ending the torment."

            show muto normal at center
            with charaenter

            mu "Before you all leave, I expect the answers for those problems by Monday."

            hide muto
            with charaexit

            "The class sighs as one, instantly regretting slacking off, but still acutely aware of the more pressing issues at hand."

            "The classroom empties in a blink as everyone rushes to their last-minute festival preparations."

            "I stay behind and try to quickly finish the questions so I don't have to bother with it over the rest of the weekend, with the festival and all tomorrow."

            show hanako emb_downtimid at offscreenright
            with None

            show bg at bgleft
            show hanako at right
            with charamovefaster

            "Apart from me, Hanako is the only one left, obviously waiting for Lilly."

            "It's weird that Lilly comes all the way to our classroom to pick her up. I expect that moving around is at least nominally harder for her than it is for Hanako."

            "But it's none of my business, and I naturally don't ask about it from Hanako."

            "Despite the relative proximity of our seats, neither tries to strike up a conversation about that or anything else either, so an oppressive silence falls upon the classroom."

            "Time passes in silence. It's probably just fifteen minutes or so but it feels longer. I turn pages of my notebook. Hanako turns pages of the novel she's reading."

            "My pencil lead splinters against the paper just when I was about to finish a paragraph."

            "The sounds of my irritated sigh and subsequent fumbling around for a sharpener feel like they're breaking the mood in the classroom."

            "Hanako keeps her eyes firmly away from my direction."

            "Before long, Lilly's tall figure appears in the doorway."

            show lilly basic_smileclosed at offscreenleft
            with None

            show bg at center
            show hanako at offscreenright
            show lilly at left
            with charamove

            li "Hanako?"

            show lilly at twoleft
            show bg at bgright
            show hanako emb_downsmile at center
            with charamove

            "Her name is all it takes to make Hanako jump up from her desk and run to Lilly."

            hide lilly
            show hanako emb_downsad
            with charaexit

            show hanako at tworight
            with charamove

            hide hanako
            with charaexit

            "They talk quietly for a moment, but it isn't long before Lilly leaves down the hall and Hanako idles back into the classroom, taking her seat once again."

            show hanako emb_downsad at offscreenright
            with None

            show bg at bgleft
            show hanako at right
            with charamove

            "I watch Hanako out of the corner of my eye out of sheer curiosity at the idea that the two would be separated."

            "For a couple of minutes, she does nothing but sit with her chin in her hand, staring at the desk dejectedly."

            show hanako emb_downtimid
            with charachange

            "The boredom evidently becomes too much for her though, her slender frame reaching into her bag and pulling out a small book."

            "Come to think of it, that isn't the one I saw her reading at the library. She must be quite a fast reader to get through them at this rate."

            if got_kenji() or _in_replay:
                hide hanako
                with charaexit

                stop music fadeout 4.0

                "After about ten minutes of restlessly shuffling in her seat and trying to read, Hanako closes her book and leaves too."

                "As should I, since the assignment is all but finished and there is nothing else to do in the classroom."

                scene bg school_dormhisao
                with locationskip

                "Not really feeling energetic, I just go straight to my room and read for the rest of the day."

                scene black
                with Dissolve(3.0)

                $ force_route = FR_KENJI

            if _in_replay:
                return

    if force_route:
        return

    python:
        if go_through_lilly() and not get_tired():
            force_route = FR_LILLY
        elif go_through_shizu():
            if get_tired() and not are_student_council:
                force_route = FR_EMI
            else:
                force_route = FR_SHIZU
        elif get_tired():
            force_route = FR_EMI
        else:
            force_route = FR_RIN

    if force_route in (FR_EMI, FR_RIN):
        label .an_asethetics:
            scene bg school_scienceroom at bgleft
            show hanako emb_downtimid at right
            with None

            hide hanako
            with charaexit

            stop music fadeout 4.0

            "After about ten minutes of restlessly shuffling in her seat and trying to read, Hanako closes her book and leaves too."

            "As should I, since the assignment is all but finished and there is nothing else to do in the classroom."

            "Not that I have anything to do anywhere else either."

            play music music_tranquil fadein 3.0

            scene bg school_hallway3
            show crowd
            with locationchange

            play ambient sfx_crowd_indoors fadein 0.3

            "The school is a beehive of activity but nobody pays me any heed."

            "I saunter past classrooms filled with students frantically doing this and that, buzzing around like little worker bees."

            "You wouldn't guess the school day is over."

            stop ambient fadeout 0.3

            scene bg school_courtyard
            show crowd
            with locationskip

            play ambient sfx_crowd_outdoors fadein 0.2

            "It's a bit quieter outside, but not by much."

            "People zip by, left and right, hurrying as quickly as they can; busy and energetic."

            "I feel the opposite. The midday sun seems to be draining all the spirit out of my body, making it feel limp all over."

            "Warm, soft air flows inside my shirt, feeling like a cushion."

            "I yawn lazily, thinking about what I'd do."

            "I'll drop off my books at the dorms first, and then… something I haven't decided yet."

            "Maybe Kenji is in his room."

            stop ambient fadeout 2.0

            scene bg school_dormext_half
            with locationchange

            "On the way to dorms, I spot Emi coming my way, running despite not having those weird running prosthetics on. I wave at her and she skids to a stop."

            show emi basic_closedgrin at offscreenright
            with None

            show emi at center
            with charamovefaster

            emi "Yo, Hisao!"

            "Spatters of white and green paint adorn her nose and chin respectively, but her smile is wide, as it seems it always is."

            show emi excited_happy_close
            with charachange

            "She leans closer to me, amplifying the feeling she is examining me."

            emi "Whatchadoin'?"

            hi "Nothing, really. I don't have anything to do for the festival and everyone else seems to be doing something important."

            show emi excited_laugh_close
            with charachange

            emi "That's perfect! Then you can help me and Rin!"

            hi "With the festival preparations? Eeeh, I'm not sure if I would be of much help."

            show emi excited_proud_close
            with charachange

            emi "That's fine! I'm not much help either!"

            "Emi grabs my wrist and starts dragging me back inside the school quite forcefully."

            scene bg school_lobby
            show crowd
            with locationskip

            play ambient sfx_crowd_indoors fadein 0.3

            "Even her walking speed is more like jogging, making me stumble over myself simply trying to keep up."

            scene bg school_staircase2
            with locationchange

            "The stairs slow Emi down a little bit. Maybe it's hard to climb with her legs, or maybe she's finally run out of breath."

            stop music fadeout 7.0

            scene bg school_hallway3
            show crowd
            with locationchange

            "We go all the way back to the third floor and to the seniors' hallway, ending up where I left five minutes ago. I could just as well have stayed here waiting for Emi, had I known."

            hi "So are you… is Rin working on that mural, still?"

            show emi basic_closedgrin at center
            with charaenter

            emi "That's right! She needs all kinds of paints and brushes and stuff, so I went to get them from the art classroom."

            hi "And you need me to help with that."

            show emi basic_grin
            with charachange

            emi "Well… Rin told me you had already helped her so I thought you wouldn't mind."

            hi "I see."

            stop ambient fadeout 1.0

            scene bg school_classroomart at bgright
            with locationchange

            play music music_another fadein 0.5

            "So thanks to Emi's flaky logic, here I am again, collecting stuff from the art classroom for other people. "

            "The room is empty apart from ourselves and the lonely specks of dust floating in the air. Emi skips straight away to the back wall, digging out a tiny, crumpled piece of paper from her pocket."

            "While she tries to make sense of the scrawled handwriting, I take a closer look at the materials lying around here."

            "Dozens of paint cans and bottles are arranged on the shelves in a most unorganized fashion."

            "Some look like they have been left there for several decades; relics of previous art club generations."

            "Next to the heavy stacks of neatly piled drawing paper are boxes full of different-sized brushes and unsorted crayons."

            "The smells of paint, turpentine and fresh paper float in the stale air, mixing in my nostrils to form that unmistakable scent of art."

            show emi basic_closedgrin at offscreenright
            with None

            show bg at bgleft
            show emi at right
            with charamove

            "Emi studies her notes, comparing them to markings on the various paint cans, and passes them to me as she finds the correct matches."

            show emi basic_grin
            with charachange

            "She stretches her neck to look on the topmost shelf, but it's not quite enough."

            show emi basic_annoyed
            with charachange

            "Her eye level stays below the shelf no matter what she does. Emi gives up and just looks up to the shelf longingly, like a child at a toy store, huffing in annoyance."

            show emi annoyedbounce

            "After a moment of building anger, she starts jumping up and down, apparently trying to speed-read the labels during the fraction of a second she can see them, and catch what she can."

            show emi basic_closedsweat at center
            with charachange

            "It's no surprise that she fails miserably, and almost manages to bring the entire shelf crashing down."

            "Now I see why me lending a hand here would be useful."

            hi "Come on, let me do that. You can't jump high enough, and I don't want you to hurt yourself trying."

            hi "Also, I'm like twice your height."

            show emi sad_angry
            with charachange

            emi "You are not!"

            "She turns around, flaring scorn, flushed cheeks and all."

            hi "Just kidding, just kidding. Anyway, I'll look up there, okay?"

            show emi basic_annoyed
            with charachange

            "She glares at me one more time, but can't come up with a retort. With a grudging 'hmph,' turns her back to me."

            hide emi
            with charaexit

            "So I begin scrounging around the top shelf for paint while below, Emi crouches to scavenge what she can from the cupboards."

            "I shake my head a little, after double-checking to ensure she can't see me do so."

            "Emi having a complex about her height was a surprise; I wouldn't have joked about it otherwise."

            "She seems easygoing, but I guess everyone has their weak spots."

            show emi basic_grin at center
            with shorttimeskip

            "Only after we have almost all the items collected and spread out on a desk like a treasure hunter's spoils do I realize that it wasn't necessarily the height jab that got her riled up."

            "She might not like to be told that she can't do something. Like jump."

            "But Emi herself seems to have forgotten all about it already. Quick to anger, quick to forgive… is she that type of person?"

            "At least she doesn't seem to have taken anything to heart, as she chatters away happily while we pick up the rest of the items and then make our way back to Rin."

            scene bg school_courtyard
            show crowd
            with locationskip

            play ambient sfx_crowd_outdoors fadein 0.2

            "I chivalrously carry the bulk of the materials as we make our way towards the dormitories."

            show emi basic_annoyed at center
            with charaenter

            emi "Rin is really stressed about getting her painting done. It's her own fault though; she should've started earlier."

            hi "Is she going to make it?"

            show emi basic_closedgrin
            with charachange

            emi "No idea. It looks good to me, but with Rin, you never know what's going on."

            show emi basic_annoyed
            with charachange

            emi "I found her this morning lying in front of the dorm in fetal position. She hadn't slept all night. I can't believe that the night nurses hadn't found her."

            show emi basic_grin
            with charachange

            emi "And now she's painting again like crazy."

            hi "Yeah, I've… noticed that she comes off as kinda… unhinged. So to speak."

            show emi basic_closedhappy
            with charachange

            "Emi giggles at that, as well as at my likely too-obvious awkwardness."

            show emi basic_happy
            with charachange

            emi "I don't mind it. She's just a little weird sometimes."

            "On that I can agree with her. Unlike me, Emi seems to be cool with Rin's… whatever it is that feels so off about her."

            "Still, they don't feel close like Misha and Shizune do. With them working as a single entity sometimes, it's hard to say where one ends and the other begins."

            "Even though they're so different, just like Emi and Rin are."

            "And Rin is the most different of them all, different from anyone else I've met."

            hi "Yeah, I guess she's a very… unique person."

            "I return to that word again, as if it encompasses Rin's personality by itself, but really it's just a substitute for a lengthy description of her oddities."

            show emi basic_closedhappy
            with charachange

            "Emi giggles as I grasp about for a properly descriptive word."

            show emi basic_grin
            with charachange

            emi "She's just weird."

            show emi excited_proud
            with charachange

            emi "You know, earlier, she just spent half an hour sitting on her box."

            emi "And stared at her toes."

            show emi basic_closedhappy
            with charachange

            "She giggles again in a way that makes me think she doesn't know what's funny about it, it just is."

            stop music fadeout 3.0

            show emi basic_grin
            with charachange

            emi "All that time."

            stop ambient fadeout 2.0

            scene bg school_dormext_half
            with locationskip

            play music music_happiness fadein 2.0

            "The working area is a mess, but the mural itself has taken over even more of the wall since I last saw it."

            "The disfigured human figures have been mostly colored in tones of red, pink, and orange; weird, imaginary… things populating the spaces between."

            "It looks… nice. I can't think of any word that would describe the work concisely and comprehensively so I settle myself on a nondescript 'nice.'"

            "But honestly, it seems that the area around the wall becomes untidier at the same rate as the mural progresses."

            "The ground is littered with dozens of paint cans, various art supplies and empty soda bottles."

            show rin negative_spaciness at center
            with charaenter

            "Rin herself is in the center of this chaos, standing there looking very cozy as if she was a natural part of the scene."

            "Her pant legs have been rolled up to her knees, exposing her thin legs which sport a drying spectrum of war paintings, similar to those on Emi's face."

            show emi basic_grin at offscreenleft
            with None

            show bg at bgright
            show rin at tworight
            show emi at twoleft
            with charamove

            "Emi sprints to Rin ahead of me and gleefully jumps in front of her."

            show emi basic_closedhappy
            with charachange

            emi "I'm back!"

            show rin basic_awayabsent
            with charachange

            rin "That was fast. Did you run in the corridors again?"

            show emi excited_proud
            with charachange

            emi "Hisao helped me."

            show emi basic_grin
            with charachange

            "Emi points victoriously at me."

            show rin basic_absent
            with charachange

            "Rin turns around following Emi's finger with her eyes, looking at my general direction."

            show rin basic_deadpannormal
            with charachange

            "She nods absentmindedly at me. She looks like she hasn't slept since last night: a vacant, glazed stare that's focused slightly off me, and movements like in a slow-motion movie."

            rin "Hello, Hisao. Thank you for the help."

            hi "Don't mention it."

            show rin basic_deadpan
            with charachange

            rin "I just did."

            hi "Never mind."

            hi "Looks like you've made progress. Looking good, as far as I can tell."

            show rin basic_deadpannormal
            with charachange

            rin "But now you get more bad luck."

            hi "I know, but I'm willing to take the risk."

            show rin basic_deadpandelight
            with charachange

            rin "That's a very nice thing to say. For me, of course. Not for you."

            show rin basic_awayabsent
            with charachange

            rin "This is why artists are always unlucky. They have to constantly look at their unfinished paintings."

            rin "So artists can't find romance, their favorite TV shows are canceled, or they die young because of an unspecified disease. It's a deep and mysterious law of the universe."

            show rin basic_lucid
            with charachange

            rin "Unless they are blind."

            "She considers this for a while, looking like she's going to fall asleep."

            show rin basic_absent
            with charachange

            rin "There is a boy."

            show rin basic_deadpannormal
            with charachange

            rin "At the art club, you see. Blind boy. So he doesn't. See."

            if side_lilly and not talk_with_hanako or not side_lilly and not wait_for_shizu:
                hi "You already told me."

                show emi basic_hes
                with charachange

                "I glance sideways at Emi and she glances back in a way that tells she has heard this one before too."

                "Neither of us says anything to Rin, though, so she continues her monotone soliloquy like an unfunny stand-up comedian."

            show rin basic_awayabsent
            with charachange

            rin "He should become an artist. No bad luck, guaranteed."

            rin "Don't you think that would be a good idea?"

            show rin basic_lucid
            with charachange

            hi "That only blind people should become artists? No, not as such."

            "…"

            show rin basic_deadpan
            with charachange

            rin "You might have a point."

            show rin negative_spaciness
            with charachange

            "Abandoning this train of thought, she turns again to consider her work and starts humming a tune that I think I recognize, but can't remember the name of."

            show emi basic_closedgrin
            with charachange

            "Emi arranges the supplies we brought and moves a few paint cans around, trying to bring some organization to the scene."

            show rin basic_awayabsent
            with charachange

            rin "Emi, I need the Prussian blue paint."

            show emi basic_confused
            with charachange

            emi "Which one's Prussian blue…"

            "She is staring helplessly at seven or eight cans, each with a different tone of blue."

            show rin basic_deadpan
            with charachange

            rin "It's the one with Prussian blue paint in it."

            show emi basic_annoyed
            with charachange

            emi "Geez, Rin! You're not helping at all!"

            "I look around as well, even though I don't know what Prussian blue looks like, either. I wonder what blue has to do with Prussia."

            "…Or what Prussia even is. The name sounds vaguely familiar, but I can't place it."

            "While none of the blues looks more Prussian than the others, the small print on the labels is legible enough to determine that none say anything about the contents being Prussian."

            hi "There is no Prussian blue here."

            if _in_replay:
                return

    if force_route == FR_RIN:
        label .creative_pain:
            scene bg school_dormext_half at bgright
            show rin basic_deadpan at tworight
            show emi basic_annoyed at twoleft

            "Emi heaves a sigh."

            show emi basic_closedsweat
            with charachange

            emi "I guess I have to go back and get some."

            show emi basic_grin
            with charachange

            emi "I promised to help with our class project, though, so I'll be back a bit later. Can you manage without it for a few hours?"

            show rin basic_deadpannormal
            with charachange

            "Rin nods, and so Emi leaves."

            stop music fadeout 2.0

            hide emi
            with charaexit

            show rin at center
            show bg at center
            with charamove

            "I stay because I like watching Rin paint, and because I have nothing better to do."

            "I sit on a box and pick up today's book from my bag. It's a story about three guys drinking beer for two weeks straight and doing little else."

            play music music_pearly fadein 2.0

            hide rin
            with charaexit

            "Rin moves from the spot that was in need of the blue and starts slowly working on another."

            "Her foot works the brush steadily against the plastered wall. Layers of paint on top of layers of paint. The mural slowly gains more form."

            "I turn the pages at a leisurely pace. In this chapter they are drinking beer at the protagonist's friend's place. In the previous ones it was the protagonist's own apartment."

            "It's not a page-turner kind of book, a slice of someone's imaginary life that makes me wonder why it had to be written."

            "Why indeed. The reason for doing something creative… it's something incomprehensible."

            "Like why Rin does paintings. It feels like she and Emi are the same, going squarely against their fates as if it's just out of spite."

            "Rin even said something like that. 'Do something you can't just because you can.'"

            "Is that what she meant? Is that her reason? It might be Emi's, she comes off as quite a headstrong person."

            "Rin doesn't give off that kind of an air. Thinking about it, she doesn't give off any kind of air, or maybe a different kind every time I talk with her."

            "Why did she say what she said? Why does she, or anyone at all paint, or draw, or sculpt, or write?"

            "I've never had much of a creative impulse so I don't think I can really understand it."

            "It makes me feel hollow inside."

            "What a grim thought. I can't really decide whether it's true or not, either."

            "Am I content being this way? I can't deny I'm feeling a little bit envious of Rin, but I can't really consider it a flaw of any kind."

            "I'm myself and she is herself."

            "Still, I do need to find something. Something that could… make me feel a little less lost about myself, instead of just drowning myself in these books as I did in the hospital."

            "I can't help but feel disoriented; the new school, lifestyle and people around me contribute heavily to this sensation."

            "I'm trying my best to fit into existing social circles, and most of the people I've met have been really nice."

            "It still feels like I'm an outsider, though; like I don't belong."

            stop music fadeout 2.0

            "I shake the feeling off, realizing that I'm spacing out. I have neither turned a page of the book, nor done anything for Rin."

            "She is trying to pour some paint from a big can using only her feet, having not bothered to ask me. Or maybe she did, and I didn't hear it."

            "Either way, it looks very unstable."

            scene bg mural_part
            show rin basic_awayabsent_close at tworight
            with locationchange

            play music music_soothing fadein 0.5

            "I quickly jump to help her, as it looks like she's about to spill the entire contents of the can all over the pavement."

            "I take the can from her feet and pour some in the bowl."

            show rin basic_absent_close
            with charachange

            "She doesn't say anything, and neither do I. I catch a glimpse of her eyes, looking silently at me from under her unkempt bangs."

            "It's an unreadable expression, a perfect poker face, mixed with a hint of something like a mild surprise."

            "I wonder what she is thinking. Maybe she is wondering about what I'm thinking. Maybe nothing."

            hi "A penny for your thoughts."

            show rin basic_deadpan_close
            with charachange

            rin "Do you have any pennies with you?"

            hi "I don't think I do."

            show rin basic_deadpancontemplation_close
            with charachange

            rin "Then I don't think I will tell. I'm not thinking anything either, so you're in luck. Except now I just did."

            "She frowns, looking very unsatisfied."

            rin "It's hard to not think about anything. But it's important."

            "I'm about to ask why it's important when some old guy walks up to us, looking like he has some business with Rin."

            scene bg school_dormext_half at bgright
            show nomiya smile at center
            with locationchange

            no_ "Good afternoon. How's it going?"

            show nomiya at twoleft
            show bg at center
            with charamove

            show rin basic_awayabsent at tworight
            with charaenter

            rin "I can make it."

            "Rin doesn't take her eyes off the wall and responds so naturally that I can only assume they know each other."

            "I haven't seen the man before, so I naturally wonder who he might be. Maybe a teacher?"

            "His hair has faded to a silvery gray, so much so that it looks artificially dyed. I hope that's not the case."

            "Small round glasses hang on the bridge of his nose, but it appears he's constantly looking over the lenses, rather than through them."

            "He's studying the mural intently over said glasses."

            show nomiya talk
            with charachange

            no_ "Good, good."

            no_ "What bold composition you have here!"

            "He moves to inspect the mural closer, talking to himself about it in a way that makes it obvious he wants us to hear it too."

            show nomiya veryhappy
            with charachange

            no_ "Very good, very good indeed…"

            "I don't really know what to make of it but Rin doesn't seem to care much. She's looking around her working space, the various bowls of different tones scattered all over."

            show rin basic_deadpan
            with charachange

            rin "Hisao."

            hi "Hmm?"

            show rin basic_deadpannormal
            with charachange

            rin "A little more of this."

            hi "Give me a second."

            "I pour a 50-50 mix of two paints into the bowl to create more of the same pale pink tone Rin was using to fill up the shape of a man's face."

            "Rin watches me doing so, which makes me feel nervous somehow. Her face is so unassuming that it feels she's just waiting for me to do something wrong."

            "The man turns to reckon me as well, looking surprised as if he noticed my presence only just now."

            "…Maybe he did."

            show nomiya talk
            with charachange

            no_ "Why, hello there. Who might you be?"

            hi "Ah, I'm a transfer student to class 3-3. Hisao Nakai. Nice to meet you."

            show nomiya frown
            with charachange

            no_ "Mutou's class, eh? Well, I won't hold that against you!"

            play sound sfx_birdstakeoff

            show nomiya veryhappy
            with vpunch

            "He laughs very loudly. Obnoxiously loudly. A few small birds take flight from a nearby tree."

            show nomiya talk
            with charachange

            no_ "I'm Shinichi Nomiya, the art teacher."

            "So this is the art teacher. In retrospect, should have guessed that much. He even looks like one, as far as first impressions go."

            show nomiya smile
            with charachange

            no "How did you come to end up assisting my protégée?"

            menu:
                set choices
                with menueffect

                "I wish I knew…"

                "I just kinda stuck with her, I think.":
                    $ force_route = FR_KENJI

                    call a1c14o1

                "I'm interested in the art club.":
                    call a1c14o2

            if _in_replay:
                return

    if force_route == FR_EMI:
        label .proper_exercise:
            scene bg school_dormext_half at bgright
            show rin basic_deadpan at tworight
            show emi basic_annoyed at twoleft

            stop music fadeout 6.0

            show emi basic_closedgrin
            with charachange

            emi "We need to go get more, then."

            "I open my mouth to say that actually, we're not both needed for such a simple task like finding another pot of Prussian Blue, but Emi's already grabbed my arm and started dragging me off."

            hide emi
            with charaexit

            "I wave to Rin, who doesn't seem to have noticed that the two of us are even leaving."

            play ambient sfx_crowd_outdoors fadein 0.5

            scene bg school_courtyard
            show crowd
            with locationskip

            "Well, she'll notice when she goes for her Prussian Blue and finds out it's still not there."

            scene bg school_lobby
            show crowd
            with locationskip

            play ambient sfx_crowd_indoors fadein 0.5

            "Maybe."

            scene bg school_staircase2
            with locationskip

            "…"

            scene bg school_hallway3
            show crowd
            with locationskip

            "Probably not, actually."

            stop ambient fadeout 2.0

            scene bg school_classroomart
            with locationskip

            "While I'm busy thinking of how weird Rin is, Emi's been dragging me back to the art classroom."

            "I feel myself starting to run out of breath."

            hi "What's the rush?"

            show emi basic_confused at center
            with charaenter

            emi "Huh?"

            "Emi's giving me an appraising look, as if she's trying to figure something out."

            hi "It's just that you seem to be in a hurry."

            hi "I'm not sure I can keep up."

            "Comprehension dawns on her face."

            play music music_emi fadein 0.3

            show emi excited_proud
            with charachange

            emi "You're not out of breath, are you?"

            "There's almost an accusing playfulness to her tone."

            "I'm tempted to deny it, but then I realize that I've been breathing heavy since we stopped."

            "Guess it's kind of obvious."

            hi "A little. Not everybody can be in shape, you know."

            hi "Takes all kinds, right?"

            show emi basic_annoyed
            with charachange

            "Emi frowns. It's not a particularly good frown."

            hi "Er, that is…"

            hi "I should… get in shape?"

            "Not that I hadn't already decided to try for that."

            "After that flutter on the track I figure there's a real need to get in some sort of running habit."

            "I was, after all, feeling pretty good until I had my false alarm."

            "Well, actually I wasn't. But it was… fun?"

            "Meanwhile, my comment seems to have helped Emi come to some sort of a decision."

            show emi basic_closedgrin
            with charachange

            emi "Well, that's it, then."

            stop music fadeout 1.0

            show emi basic_annoyed
            with charachange

            "She gives me a serious look."

            emi "You're joining me."

            "…"

            hi "I beg your pardon?"

            show emi basic_grin
            with charachange

            emi "In the mornings."

            emi "You and I are now running partners."

            show emi basic_closedhappy
            with charachange

            emi "I've got a routine all planned out. In fact…"

            play sound sfx_paper

            "She produces a crumpled sheet of paper."

            show emi excited_amused
            with charachange

            emi "I've got it right here with me."

            play music music_running

            "I take the sheet of paper and give it a once-over."

            "Times, dates, and laps, all laid out."

            "A slow increase from just a few laps a day to…"

            "My God, does she expect to have me running marathons?"

            "And where did she find the time to get this all together?"

            "And how long has she been planning this, anyway?"

            hi "You've been planning this?"

            show emi sad_shy
            with charachange

            emi "A little."

            show emi sad_grin
            with charachange

            emi "But it's really the nurse's idea!"

            show emi basic_closedgrin
            with charachange

            emi "He told me to keep an eye on you to make sure you exercised like he told you to!"

            "A vast conspiracy?"

            "Maybe Kenji's on to something here…"

            hi "This seems a bit much for just 'keeping an eye on me.'"

            show emi sad_grin
            with charachange

            emi "Well, to be honest I've been trying to find a running partner in the mornings for a while now."

            "My God, Kenji! If you could only see the scheme unfolding!"

            hi "What do you need a partner for, anyway?"

            show emi basic_annoyed
            with charachange

            emi "It's easier to keep up a workout if you're not the only one doing it."

            emi "Isn't that obvious?"

            emi "You're less likely to quit if someone else is counting on you to be there, right?"

            hi "I see. And this won't only keep you running, but it'll make sure that I keep running as well."

            hi "Meaning that I'll be obeying the nurse…"

            show emi excited_proud
            with charachange

            emi "…and I'll be keeping an eye on you just like he asked!"

            show emi basic_closedgrin
            with charachange

            emi "You caught on quick, Hisao."

            hi "And if I refuse?"

            "I have no intention of refusing, of course."

            "But I've got to at least put up a token resistance to such a masterfully executed plan."

            show emi basic_grin
            with charachange

            emi "Well, if you refused I'd have to pout."

            emi "And you'd have to live with being the guy who made Emi Ibarazaki pout."

            show emi basic_closedgrin
            with charachange

            emi "You don't want that on your conscience, do you?"

            show emi sad_depressed
            with charachange

            "As if to demonstrate, Emi begins pouting."

            "It is the most adorable, heart-wrenching thing I've ever seen."

            hi "Okay! I'll do it!"

            hi "Just… don't do that!"

            hi "I feel like I just hit a puppy!"

            show emi basic_closedgrin
            with charachange

            emi "So it's settled, right?"

            emi "You're going to be my running partner?"

            emi "Follow the workout?"

            emi "And the dietary plan?"

            hi "Dietary plan?"

            show emi basic_grin
            with charachange

            emi "Yeah, the dietary plan!"

            show emi excited_proud
            with charachange

            emi "You've got to eat healthy if you're going to get in shape, you know!"

            "I examine the workout routine closely."

            hi "I don't see a dietary plan on here."

            show emi basic_shock
            with charachange

            emi "Oh right! I forgot to give that to you!"

            play sound sfx_paper

            show emi excited_amused
            with charachange

            "Another crumpled sheet of paper is produced and handed over."

            "It's somewhat less detailed."

            show emi excited_happy
            with charachange

            emi "I had the nurse help me come up with it."

            "The amount of dedication that the nurse has to keeping me in good health is pretty overwhelming."

            "I don't know many school nurses who would get one of their students to spy on me, much less help come up with a dietary plan."

            "Then again, I guess I'm not in a normal school."

            "And maybe that's not such a bad thing."

            "Then again, this dietary plan seems to cut out just about everything that'll be offered at the festival tomorrow."

            "Hmm."

            hi "So when does our running start?"

            show emi basic_grin
            with charachange

            emi "After the festival."

            hi "Right after? What if I've had something to eat there? I could get a stomach ache, you know."

            show emi basic_annoyed
            with charachange

            emi "I meant the day after the festival."

            hi "I knew that."

            "Wasn't there something we were supposed to be doing?"

            hi "Oh! I guess we should get that paint for Rin, huh?"

            show emi basic_shock
            with charachange

            emi "Oh no! It slipped my mind!"

            stop music fadeout 8.0

            scene bg school_dormext_half_ss
            with shorttimeskip

            "By the time we get the paint and get back to the mural, Rin's already wandered off."

            "Oh well."

            "Emi and I both decide to part ways there, leaving the paint on the ground."

            "Rin'll find it. Whenever she comes back, anyway."

            scene bg school_dormhisao
            with locationskip

            "Festival's tomorrow. I'm actually a little excited for it."

            "At the same time, the week's left me feeling pretty tired, so I read a little and then go to bed."

            scene black
            with Dissolve(3.0)

            if _in_replay:
                return

    if force_route == FR_LILLY:
        label .sip_p2:
            scene bg school_scienceroom at bgleft
            show hanako emb_downtimid at right

            "But why would Lilly leave her to her own devices? It seems to be quite out of the ordinary, going by Hanako's reaction."

            "…"

            "…Ah, that's right. I think Lilly mentioned something about going into town today before Rin bumped into us."

            "The thought of that walk makes me look outside."

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            scene bg misc_sky:
                xalign 0.0
                warp acdc_warp 15.0 xalign 1.0
            with locationchange

            "The bright sun and occasional people wandering around and enjoying the afternoon make me yearn to get out of school, or at least do something other than sit here."

            "Giving in to one of my worst vices, procrastination, I decide that history is a subject best studied on a Sunday. Or a Monday. Or on any day other than this one."

            "I give a grunt as I lever myself out of my seat, briefly debating with myself whether or not to hang out with Kenji."

            "He doesn't strike me as the 'enjoying the nice weather outside with others' kind of person, really. I guess I'll catch up with him later."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            scene bg school_scienceroom at bgleft
            with Dissolve(1.5)

            "Changing tacks, I briefly entertain the idea of talking with Hanako, but by the time I look at her seat, it's vacant. She must've left for the library."

            menu:
                set choices
                with menueffect

                "There's got to be something to do that can kill the time…"

                "Go for a walk into town.":
                    "Following Hanako to the library seems a bit intrusive. There was a reason she left the classroom, after all."

                    "And that aside, I do want to catch up with Lilly. At the very least, I'd like to thank her for looking out for me despite her other, obviously taxing, duties."

                    "I guess I'll walk around town. With any luck, I should be able to find Lilly. The exercise'll do me some good, as well."

                    play music music_tranquil fadein 3.0

                    scene bg school_courtyard
                    with locationskip

                    "Walking through the school courtyard to the gate, I give a small nod to a couple of passing classmates, the gesture being returned in kind."

                    "Even from here, the shouts of the sports club members can be heard. From the sheer volume of the din, the track must be packed right now."

                    "I remember what Lilly said yesterday about being dropped right into the middle of a busy time for the school."

                    "While I'm trying to get my bearings and catch up on study that I've missed, everyone else is doing normal school activities. The feeling of being a foreigner still hasn't dissipated. At least, not yet."

                    "Well, I guess not everything's bad."

                    "This is a private school, and that much is easily noticed when walking around outside. Not only are the school grounds huge, but the buildings themselves are immaculate and quite divorced from the dime-a-dozen concrete blocks of public schools."

                    "There's also the fact that there's a much stronger feeling of community here, or at least a friendlier atmosphere. At my old school, it was generally accepted that people would keep to their little clique and be done with it."

                    scene bg school_gate
                    with locationchange

                    "Eventually I reach the gate, and begin to walk down the road and into town."

                    scene bg suburb_roadcenter
                    with shorttimeskip

                    "Well, that was fairly productive."

                    "Having seen a fair portion of town, even including the houses perched on the hills around the outskirts, I decide to take a walk around the park before heading back."

                    "Living in the city all my life, the total lack of smartly-dressed businessmen and fashionably-dressed girls strikes me as incredibly unusual."

                    "All that's to be seen are the odd elderly person shuffling along the sidewalk and assorted busily chatting pairs of middle-aged women outside of small storefronts."

                    stop music fadeout 8.0

                    "Walking along the road to the park quickly distracts me from them, though, making me realize that I perhaps pushed myself further than I should have done to see as much as I could."

                    "As my breath begins to wheeze and my chest tightens more and more, I give up on the prospect of soldiering on."

                    play ambient sfx_parkambience fadein 1.0

                    scene bg suburb_park
                    with locationskip

                    "After a quick glance around the park as I enter, I take a seat on a wobbly old bench that I notice near a couple of vending machines."

                    "For minutes on end I sit with my head bent over, forcing myself to take deep breaths. I feel more like an old man than a teenager who should be in the prime of his life."

                    "The stay in hospital, the surgery and the medications must be taking their toll on me. Dammit."

                    "Eventually, my breathing returns to normal and the muscles in my chest loosen, not without a fair measure of relief. I guess this means the end of my little sojourn though, in any case."

                    stop ambient fadeout 1.0

                    scene bg suburb_shanghaiext
                    with locationchange

                    "There's a café on the far corner, so I'll stop by to quench my thirst before heading back."

                    play sound sfx_storebell

                    scene bg suburb_shanghaiint at bgright
                    with locationchange

                    play music music_dreamy fadein 2.0

                    "A little bell above the door signals my arrival to an empty counter."

                    "For a few moments I stand there waiting, my eyes every now and again drifting from one end of the counter to the other searching for a service bell."

                    show yuukoshang neutral_down at center
                    with charaenter

                    "Eventually a door some ways behind the counter opens, the person emerging from it taking me by complete surprise."

                    hi "Yu… Yuuko?"

                    hi "Hi, I had no idea you worked here."

                    "I really have no idea how to address her either, given that she is technically school staff as well as, apparently, a waitress."

                    show yuukoshang neurotic_up
                    with charachange

                    yu "Ah, yes, um…"

                    "She quickly paces up to the counter, before flinging her upper half downwards in an overacted bow."

                    show yuukoshang closedhappy_down
                    with charachange

                    yu "Welcome to the Shanghai! May I take your order?"

                    "Straight down to business, I see."

                    hi "I don't know… well, some coffee, please?"

                    show yuukoshang neutral_down
                    with charachange

                    yu "Yes, certainly. I'll make it right away and bring it to you when it's done."

                    hi "Uh, thanks."

                    "Yuuko's formality takes me aback. She seems to take her job very seriously."

                    hide yuukoshang
                    with charaexit

                    "Obeying her instructions, I turn around and quickly glance around for a free table. Considering the café seems to be empty, this is a simple task to accomplish."

                    show bg at bgleft
                    with charamove

                    "As I walk towards a table adjacent to the window, I notice a flash of yellow around one of the table dividers."

                    show lilly basic_smileclosed at twoleft
                    show akira basic_lost at tworight
                    with charaenter

                    "Sure enough, no more than a glance is needed to ascertain that it's a certain Satou at the table. That said, I don't recognize the suited figure across the table from her."

                    "Blonde, fair-skinned and only a little shorter, he… she? I think she, must be a relative."

                    "Since the two are all but silent as the suited figure takes a swig from a cup of coffee, I decide to greet Lilly. Some part of my coming here was in order to meet her, after all."

                    hi "Hi, Lilly."

                    show lilly basic_smile
                    with charachange

                    li "…Hisao?"

                    hi "Yeah. Nice to see you again."

                    show akira basic_smile
                    with charachange

                    "The suited girl looks up, noting my uniform with a relaxed smile."

                    aki_ "Know each other?"

                    hi "I… guess."

                    "It's as good an approximation of our relationship as I can think of."

                    show lilly basic_smileclosed
                    with charachange

                    li "Hmm… care to take a seat?"

                    "She says this to the air beside me, but the message is clear enough and I take a seat beside her."

                    show lilly basic_weaksmile
                    with charachange

                    li "I suppose some introductions might be in order."

                    show lilly basic_smile
                    with charachange

                    li "Hisao, this is Akira Satou, my older sister. Akira, this is Hisao Nakai, another Yamaku student."

                    "Looks like my guess was correct. The newly-introduced Akira gives a nod, which I return."

                    "What I don't return however, is the almost analytical gaze with which she looks me over."

                    show lilly at left
                    show akira at right
                    with charamove

                    show yuukoshang neutral_down at center
                    with charaenter

                    "As she does so, Yuuko walks up to the table and carefully places the coffee on the table before bowing and taking her leave."

                    hide yuukoshang
                    with charaexit

                    show lilly at twoleft
                    show akira at tworight
                    with charamove

                    "Gently bringing my hand to the side of the cup, I realize that it's already at just the right temperature to drink. After taking a sip, the flavor turns out to be just as good as the temperature."

                    "Yuuko seems a lot better at this than being a librarian."

                    "I take a good, long drink before relaxing into the seat."

                    "It takes mere seconds for Akira's examination to come to an end. Apparently becoming quickly bored with the activity, she turns to her sister."

                    show akira basic_boo
                    with charachange

                    aki "So, how's school recently?"

                    "It seems Akira is entirely unconcerned with someone she doesn't know at all listening to everything they say."

                    "Not that I mind. Leaving them to their chatting, I sit back and continue drinking the pleasantly aromatic coffee."

                    show lilly basic_smileclosed
                    show akira basic_smile
                    with shorttimeskip

                    aki "Sounds like it's pretty busy for ya, then."

                    show lilly basic_smile
                    with charachange

                    li "At least I'm not cooking your meals after school any more."

                    "As they talk, I slowly realize that I'm entirely unable to gauge Lilly's emotions through her eyes; as I would for any other person."

                    "It becomes slightly unsettling as I subconsciously focus on that fact."

                    show akira basic_lost
                    with charachange

                    aki "Whoa, so cold. Weren't ya just cooking for yourself anyway? I only ever got leftovers."

                    show lilly basic_displeased
                    with charachange

                    li "That's not the point… are you managing to feed yourself, at least?"

                    show akira basic_resigned
                    with charachange

                    aki "I can cook without blowing myself up, you know."

                    show akira basic_annoyed
                    with charachange

                    aki "Mostly."

                    show lilly basic_listen
                    with charachange

                    li "That's…"

                    show akira basic_laugh
                    with charachange

                    aki "Hahaha! It's fine, it's fine. I needed to learn sometime anyway."

                    show lilly at left
                    show akira at right
                    with charamove

                    show yuukoshang neurotic_up at center
                    with charaenter

                    yu "Ah, Lilly?"

                    show lilly basic_smile
                    show akira basic_boo
                    with charachange

                    "Everyone present is momentarily distracted by Yuuko, who places a cup of tea on the table for Lilly."

                    hide yuukoshang
                    with charaexit

                    show lilly at twoleft
                    show akira at tworight
                    with charamove

                    "Taking the moment to glance at her watch, Akira levers herself off her seat and gives me a quick nod."

                    show akira basic_smile
                    with charachange

                    aki "Well, I'd better be off. It was nice talking to ya, Lilly."

                    show lilly basic_oops
                    with charachange

                    li "Akira, do you have to…?"

                    "Lilly looks genuinely mournful at her sister suddenly leaving. It does seem like she might have the wrong idea."

                    show akira basic_resigned
                    with charachange

                    aki "Sorry, I need to get back to work. They'll be on my neck again if I don't make it back quickly."

                    "So informal… Akira's trim and tidy appearance would give anyone the wrong impression of her."

                    show lilly basic_concerned
                    with charachange

                    li "Bye, Akira…"

                    show akira basic_smile
                    with charachange

                    aki "C'mon, don't look so down. I'll be around again soon. Seeyas."

                    hide akira
                    with charaexit

                    "With that, she waltzes out of the Shanghai with her hand held high."

                    "Lilly still looks pretty depressed, so I try to make some small talk in an effort to take her mind off it."

                    show lilly at center
                    show bg at center
                    with charamove

                    hi "She seems nice."

                    show lilly basic_displeased
                    with charachange

                    li "We used to live together, but now that I live at school we hardly ever see each other."

                    "Despite Lilly having been quite affable, I still don't really know much about her. In hindsight, it's surprising just how much she's extracted from me, really."

                    hi "You used to live together? Was it somewhere around here?"

                    li "It was pretty far south, so the trip into Yamaku was fairly long."

                    show lilly basic_reminisce
                    with charachange

                    li "With her working hours getting longer and Yamaku being so far away, there was little choice in the end but to move into the dormitories."

                    "Well, that explains the chatter about cooking. Evidently regaining her composure, she livens back up… at least, in part."

                    show lilly basic_weaksmile
                    with charachange

                    li "I take it you're better rested, now?"

                    hi "Sorry?"

                    show lilly basic_smileclosed
                    with charachange

                    li "You sound less exhausted than you did when you first came in."

                    "To be able to pick out my breathing like that… she must have pretty good ears."

                    hi "Yeah. Ended up walking all over town, despite only planning on taking a short walk down here."

                    "Reminded of my thirst from the walk, I lean forward to take a sip."

                    play sound sfx_teacup

                    "Without further ado, Lilly starts on her cup of strong-smelling tea."

                    "I guess I'd better get going back to Yamaku. There's only so long I can stall studying for, and I want to get a good night's sleep before the festival."

                    stop music fadeout 4.0

                    "Standing from my seat, I take the coffee-stained cup from the table."

                    show lilly basic_surprised
                    with charachange

                    li "You're leaving?"

                    hi "Yeah. You going to head back as well? It's getting kind of late."

                    "For a moment she pauses, before lifting her face over her teacup as if she was looking at me."

                    play music music_lilly fadein 3.0

                    show lilly basic_smile
                    with charachange

                    li "Yuuko, could we have one more coffee please?"

                    yu "Okay, I'll bring it right away!"

                    hi "That's… not subtle."

                    show lilly basic_giggle
                    with charachange

                    "She gives a short giggle at my frank assessment of her maneuver. It's surprisingly childish and carefree, given her otherwise collected appearance."

                    "In the end, though, I have little reason to refuse. To be honest I can hardly say no, all things considered."

                    "Giving a manufactured sigh, I take a seat opposite her."

                    hi "Wanting company, then?"

                    show lilly basic_cheerful
                    with charachange

                    li "Hmm… I'd say that it's more that I was wondering…"

                    "I see she's in questioning mode, again. She does seem to be unusually interested in me, or at least curious."

                    show lilly basic_smile
                    with charachange

                    li "Do you have any siblings?"

                    "Not exactly an unexpected tangent."

                    hi "No, only child. To be honest, the idea of having someone that close makes me a bit envious."

                    show lilly basic_smileclosed
                    with charachange

                    li "Interesting…"

                    "I raise an eyebrow, which of course goes unseen. The short silence communicates the question well enough."

                    show lilly basic_smile
                    with charachange

                    li "It's just that others have said the same thing before."

                    li "It's a difficult subject to try and think about objectively, given that I've always had someone like that."

                    "I can mostly understand what Lilly means, given that it would be hard to place oneself outside of a situation they've been in all their life."

                    "She and her sister must have a pretty close relationship."

                    "Taking pains to interrupt us as little as possible, Yuuko dutifully comes over and places a cup on the table."

                    "Lilly thanks her as I sit back, taking in this vexing girl in front of me."

                    "Despite always seeming to be on her guard and in control of herself when talking to others, she has an almost childlike curiosity about other people."

                    "That said, those rare moments she seems to slightly lower her guard are the most insightful into how she thinks."

                    "Reaching forward for my drink, I realize something I probably should've noticed earlier."

                    "…I think I'm starting to become kind of curious about her."

                    stop music fadeout 2.0

                    scene bg school_gate_ni
                    with shorttimeskip

                    play ambient sfx_cicadas fadein 0.5

                    "Despite making a good pace, it's already nightfall by the time I reach the large iron gates in front of the school."

                    "While it's nice to have plenty of time to wander around by virtue of living right next to the school, I can't help but get the feeling that very few students actually take the opportunity."

                    scene bg school_courtyard_ni
                    with locationchange

                    "Compared to the number of students I see milling around on-campus during free time, it's startlingly rare to see anyone around town."

                    "Given the large number of accommodations and facilities that the school offers, many of them might simply not see any point in venturing outside, let alone people such as Hanako and Kenji."

                    "It makes me wonder if students like Shizune, Misha, and Lilly are the exception for this school, rather than the norm."

                    stop ambient fadeout 1.0
                    scene bg school_dormhallway
                    with locationskip

                    "As I wander back to my dorm room, I continue to compare my old school with Yamaku. As I do so, I begin to be surprised that I managed to get even this used to everything that's happened to me."

                    scene black
                    with Dissolve(3.0)

                "Go to the library.":
                    $ force_route = FR_HANAKO

            if _in_replay:
                return

    if force_route == FR_SHIZU:
        label .shanghaied:
            scene black
            with dissolve

            play sound sfx_doorknock

            scene bg school_dormhisao
            with openeye

            "At five minutes past eight, an unbelievably loud banging jolts me awake. It's coming from outside my door."

            scene bg school_dormhallway
            show shizu behind_blank at tworight
            show misha hips_smile at twoleft
            with locationchange

            play music music_comedy fadein 0.3

            "Quickly, I open the door to see Shizune and Misha standing side-by-side before me. Both of them look a little worn out, although it's more noticeable on Misha."

            hi "Which one of you knocked?"

            "I ask, echoing the question that must be on the mind of everyone in the entire building."

            show misha hips_grin
            with charachange

            mi "Ahahaha, that's not important, Hicchan!"

            "She quickly dismisses it without even batting an eye."

            show misha hips_smile
            with charachange

            mi "Oh? You're still in your pajamas, Hicchan? So you don't wake up at eight?"

            "I notice her hair is wet. Her curls are barely holding their shape."

            hi "No, I thought I'd sleep a bit later since it's the weekend and all, and I've been seriously sleep-deprived this week."

            "I wonder if she missed the poison in my words."

            show shizu basic_normal2
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "Then it's a good thing we came to wake you up!"

            show shizu adjust_happy
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "Anyway, Hicchan, I guess you would like to know why we're here, wouldn't you?"

            "It's not hard to guess, but I wish she wouldn't say the words she is going to say next."

            show misha perky_smile
            with charachange

            mi "Would you like to skip class and go somewhere nice with us?"

            hi "Come again?"

            show misha hips_smile
            with charachange

            mi "Would you like to skip class to do something fun?"

            "I was certain they'd force me to help them again with some slave work."

            hi "Seriously?"

            show misha hips_grin
            with charachange

            "Misha grins and nods enthusiastically."

            "I like this new approach they're taking although I'm somewhat surprised that they would suggest skipping class, even if we have only half a day since it's Saturday."

            hi "Aren't you two worried about constantly missing class?"

            show shizu behind_smile
            with charachange

            shi "…"

            show misha perky_smile
            with charachange

            mi "Well, it doesn't seem to be a problem! Hicchan, this school is pretty much at a standstill whenever this time rolls around."

            show misha hips_smile
            with charachange

            mi "It's a Saturday, too~. Don't you want to do something fun?"

            "I'm amazed by how little they seem to care."

            show shizu adjust_smug
            with charachange

            shi "…"

            show misha perky_smile
            with charachange

            mi "Not that we're pressuring you to give us your company, but we thought you might like to hang out!"

            show shizu behind_blank
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "So… would you like to join us? Come on, you'll have a lot more fun than just sitting here with your head on your desk~!"

            "I guess I won't be missing anything important; nor will I be missed."

            hi "All right, then, I don't think I'd be missing much. What do you have in mind?"

            "My eyes narrow with suspicion as a thought crosses into my mind."

            hi "Wait… this isn't just some trick to get me to do some more student council stuff, right?"

            show shizu basic_angry
            with charachange

            shi "…"

            show misha perky_confused
            with charachange

            mi "No, of course not!"

            show misha hips_frown
            with charachange

            mi "And that's a really mean thing to just assume like that, Hicchan."

            show shizu behind_frown
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "…And besides, you're in the Student Council now, remember?"

            show misha hips_grin
            with charachange

            mi "If we wanted you to do something for us, we wouldn't have to trick you~!"

            show misha hips_laugh
            with charachange

            mi "Hahaha!"

            show misha hips_smile
            with charachange

            "This is a kind of coercion that is new to me. Only two pretty girls could pull it off."

            stop music fadeout 3.0

            "I allow myself to relax a bit. Maybe I'm being too paranoid; it seems like they may really just want to hang out."

            "Nevertheless…"

            hi "No tricks?"

            play music music_shizune fadein 4.0

            show shizu basic_angry
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "No tricks! Stop being so paranoid!"

            hi "Well, if you say so."

            "Suddenly, I realize I still am wearing pajamas."

            hi "I wonder if you'd let me dress up first?"

            show shizu adjust_smug
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "Eh? Why, Hicchan? You look just fine!"

            hi "I'd still prefer wearing something else."

            play sound sfx_doorclose

            scene bg school_dormhisao
            with locationchange

            "I close the door before she gets a chance to reply and quickly pull on my uniform."

            play sound sfx_dooropen

            scene bg school_dormhallway
            show misha perky_smile at twoleft
            show shizu basic_normal at tworight
            with locationchange

            "Stepping back into the hallway, I see Shizune and Misha are engaged in an animated discussion."

            "I wonder if people discussing in sign ever accidentally poke each other in the eyes."

            show shizu behind_frown_close
            with characlose

            "While I'm contemplating this, Shizune taps me on the shoulder impatiently."

            shi "…"

            show misha hips_smile
            with charachange

            mi "So, we're planning on slipping into town! Remember that tea shop we were at on Wednesday?"

            hi "Tea shop?"

            show shizu behind_frustrated_close
            with characlose

            shi "…"

            show misha perky_confused
            with charachange

            mi "You don't remember?"

            hi "Oh, you mean that café."

            show misha hips_smile
            with charachange

            mi "Tea shop! It's called the Shanghai. China is the birthplace of tea, you know. Come on, Hicchan! I'll even treat you today!"

            show misha hips_grin
            with charachange

            mi "Ah… not me, not me, I mean Shicchan! Ahaha~!"

            hi "I don't know…"

            show misha sign_smile
            with charachange

            mi "It's nice, it's really relaxing! It's like… half café, half restaurant, half sophisticated, half… library…"

            "What?"

            hi "That's a lot of halves."

            "But Misha doesn't seem to notice that."

            show misha hips_smile
            with charachange

            mi "So~! Come on, it's not often that we have this much free time!"

            show shizu adjust_smug_close
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "If you're busy, though, you don't have to! It's not like your presence is absolutely, absolutely required!"

            show misha cross_laugh
            with charachange

            mi "Hahahaha!"

            show misha cross_grin
            with charachange

            "I've never seen more weakly disguised reverse psychology in my life. I feel kind of tired today, and my teachers in my classes might want to know where I am. Maybe."

            "On the other hand, I haven't really been into town at all since I've gotten here, so this is a good reason to head there."

            "Also, I could use something to eat. If it's Shizune's treat, even better; I'm totally broke."

            hi "All right, let's go. Lead the way."

            show misha hips_smile
            show shizu behind_smile_close
            with charachange

            mi "Great~!"

            stop music fadeout 2.0

            scene bg suburb_shanghaiint
            with shorttimeskip

            "We make it to the tea shop with a fifteen-minute walk. It seems that we are the only customers around."

            play music music_another fadein 2.0

            show shizu behind_blank at tworight
            show misha perky_smile at twoleft
            with charaenter

            hi "Is it always this quiet in the morning?"

            "By that, I mean is it always this empty."

            show shizu basic_normal
            with charachange

            shi "…"

            show misha perky_confused
            with charachange

            mi "No, this is kind of weird. Hey, this isn't a bad thing though, right?"

            hi "You're right."

            scene ev shizu_shanghai
            with locationchange

            "We take our seats at a large, square wooden table, and it hits me that I don't know what this place serves. I just went with what Yuuko recommended the last time."

            hi "Hey, is there a menu or something?"

            scene ev shizu_shanghai_normallaugh
            with charachangeev

            mi "Nope!"

            "That was a strange amount of zest."

            scene ev shizu_shanghai_smirklaugh
            with charachangeev

            shi "…"

            scene ev shizu_shanghai_smirknormal
            with charachangeev

            mi "So, Hicchan, have you decided what you're going to order?"

            scene bg suburb_shanghaiint:
                xalign 0.0
                warp acdc_warp 8.0 xalign 1.0
            with locationchange

            "I look around the store and can't see anything resembling a menu."

            "I don't understand, what's up with this place? What gives?"

            "Is this some kind of secret shop? Can you normally only enter here with a secret handshake? Some kind of wink and a nod?"

            "Do you need someone to vouch for you? A blood oath? Dammit, it was nothing like this last time."

            scene ev shizu_shanghai
            with locationchange

            hi "I don't know, the last time I think I just got coffee? What do they serve here?"

            scene ev shizu_shanghai_smirknormal
            with charachangeev

            shi "…"

            scene ev shizu_shanghai_smirklaugh
            with charachangeev

            mi "Tea!"

            hi "Ah, well, that's…"

            hi "Not just tea, right? Not only tea? There's other stuff too, right?"

            scene ev shizu_shanghai_normallaugh
            with charachangeev

            shi "…"

            scene ev shizu_shanghai
            with charachangeev

            mi "Clearly~!"

            hi "Clearly? Like what? There are no menus here. Where are the menus?"

            "They're playing another joke on me. There is no way out of this; all I can do is brace myself for the inevitable, oncoming burn."

            "I almost want to walk out of the store, but I'm already sitting down."

            "It would be improper to leave now; the unspoken rules of polite social conduct block my exit like a wall of fire."

            "I decide to play it safe. I'll order what they order, if it's acceptably manly enough."

            hi "Why don't you two order before me? Ladies first."

            scene ev shizu_shanghai_smirknormal
            with charachangeev

            shi "…"

            mi "Well played, Hicchan, but~ we already ordered!"

            hi "How is that possible? When? How? From who?"

            mi "We're regulars, we come here so often that we don't have to do that any more!"

            scene ev shizu_shanghai
            with charachangeev

            shi "…"

            mi "Well, I guess you've had enough. We're sitting on the menus, of course~!"

            scene ev shizu_shanghai_normallaugh
            with charachangeev

            mi "Hahaha!"

            "I look around at the other tables. There are no menus on any of them. That means they must just keep them in a big stack near the door or something. What a thing to sit on, and what speed to grab them so quickly."

            hi "Well, whatever. Can I have one, then?"

            scene ev shizu_shanghai_smirklaugh
            with charachangeev

            shi "…"

            scene ev shizu_shanghai_smirknormal
            with charachangeev

            mi "You can take one if you want, but you're not the kind of person who would do something that la—sci—vious?, isn't that right?"

            "I tell them that I'd just like some coffee and put my head down on the cool tabletop."

            scene ev shizu_shanghai_borednormal
            with charachangeev

            shi "…"

            scene ev shizu_shanghai_boredlaugh
            with charachangeev

            mi "Coffee? This is a very high class establishment, and you're going to order coffee?"

            "I can tell they're messing with me again."

            hi "In that case, I'll have whatever you're having."

            scene ev shizu_shanghai_smirklaugh
            with charachangeev

            shi "…"

            scene ev shizu_shanghai_smirknormal
            with charachangeev

            mi "Hicchan, Shicchan is drinking a special tea that is only grown in remote areas of India."

            mi "The tea is still handmade by a tribe of tea makers who have passed the methods down in their families for generations."

            mi "They must wade through alligator-infested waters to obtain the leaves once a year. On each trip, some do not make it back alive."

            "I can't drink that, I would feel too guilty."

            hi "Then I'll have what you're having."

            scene ev shizu_shanghai_smirklaugh
            with charachangeev

            mi "I don't know what I'm drinking."

            "How?"

            hi "Fine, then I want the tea that people died for."

            hi "No, never mind. I'll have coffee."

            hi "If this is a very high class establishment, then they should have very high class coffee, right? … No one died for it, right?"

            scene ev shizu_shanghai
            with charachangeev

            "The perfect answer, there is no way they can stand against it. Shizune shrugs, as if to say 'well played.'"

            "They still didn't answer my second question."

            scene bg suburb_shanghaiint
            with locationchange

            show yuukoshang neutral_down at center
            with charaenter

            "Misha calls for Yuuko, who brings over our drinks and a single incredibly tiny yellow cake with a little black plastic fork stuck in it for each of us."

            hide yuukoshang
            with charaexit

            "I eat my cake in one bite, amazed at how it's probably the least filling thing I've ever eaten."

            show shizu behind_blank:
                xpos 0.2 xanchor 0.5
                easein 1.0 twoleft
            show misha perky_smile_close:
                xpos 0.8 xanchor 0.5
                easein 1.0 tworight
            with Dissolve(1.0)

            show shizu at twoleft
            show misha at tworight

            stop music fadeout 3.0

            mi "Hicchan, do you have any plans for tomorrow?"

            "Misha takes a gulp of her tea, something sounding suspiciously high class even though it looks like ordinary tea."

            "She drinks with incredible recklessness considering how hot it is. The exact opposite of Shizune or Lilly."

            "Plans? That sounds ominous."

            play music music_running fadein 8.0

            hi "Plans? Yes."

            hi "Yes, I am incredibly busy tomorrow. In fact, I have so much to do that I will not have any free time at all."

            hi "That's right… none whatsoever. And everything I have to do is extremely important. Very, very important."

            show misha hips_grin_close
            with charachange

            "Misha giggles, clearly not buying it, and then signs it all back to Shizune, who nods slowly and deliberately while looking very unamused."

            show shizu basic_normal_close
            with characlose

            "Suddenly, she leans forward, staring analytically at my face like a human lie detector, waiting for the smallest tell to give me away."

            "After at least a minute of this, she sits back down in her seat and takes a sip of tea."

            show shizu behind_blank
            with charadistant

            shi "…"

            show misha perky_smile_close
            with charachange

            mi "Okay, Hicchan, if you're that busy. We don't have anything to do tomorrow, so we thought maybe you would want to hang out with us at the festival!"

            show misha sign_smile_close
            with charachange

            mi "You're new here, anyway, right? Right? So~ we thought we would show you around and have some fun together, but if you're that busy, we understand!"

            show shizu adjust_happy
            with charachange

            shi "…"

            mi "Oh well, oh well!"

            show misha cross_grin_close
            show shizu basic_normal2
            with charachange

            "The both of them shrug together in perfect sync, as if they've rehearsed it."

            show misha cross_laugh_close
            with charachange

            mi "Ahahahahaha~!"

            show misha cross_grin_close
            with charachange

            mi "Hicchan, you're so paranoid."

            show shizu adjust_smug
            with charachange

            shi "…"

            show misha cross_smile_close
            with charachange

            mi "…And you'll never beat me anyway, so why bother getting so worked up about it?"

            show misha cross_laugh_close
            with charachange

            mi "Haha! Wow, Shicchan~!"

            hi "Beat you? What are you talking about?"

            "Is she talking about the coercion? I never realized that was just a game to her. I thought I was the only one who saw it as competition."

            show shizu basic_happy
            with charachange

            shi "…"

            show misha hips_grin_close
            with charachange

            mi "You know~! …Eh? Do you, Hicchan? Because I don't."

            show shizu adjust_smug
            with charachange

            shi "…"

            show misha hips_smile_close
            with charachange

            mi "You can't outwit me! —Ah, well, Hicchan, not me…"

            show shizu basic_sparkle
            with charachange

            shi "…"

            show misha perky_confused_close
            with charachange

            mi "What? What are you talking about, Shicchan…"

            "I can see Shizune smiling craftily, daring me to enter this battle of wills and wits with her."

            "When he is pushed to the edges of despair, a man has no choice but to sink, or grasp at the fleeting wisps of hope, fight with all his power against the inevitabilities of his fate and struggle against the impossible."

            "For even if he fails, at least fail knowing that he dared greatly…"

            "…Or something like that."

            hi "Well, we'll see about that. Don't underestimate me."

            show shizu behind_blank
            with charachange

            shi "…"

            show misha perky_smile_close
            with charachange

            mi "Don't you have to follow through to make good on that, Hicchan?"

            hi "Ah, well, I could get lucky. Don't count out that possibility."

            show shizu adjust_smug
            with charachange

            shi "…"

            show misha cross_grin_close
            with charachange

            mi "You won't~."

            hi "I will! Wait—"

            show shizu basic_happy
            with charachange

            shi "…"

            show misha cross_smile_close
            with charachange

            mi "Let's make a wager on it, then!"

            hi "I don't care about competition."

            "That's a blatant lie."

            hi "Wait, what exactly do you mean?"

            show misha cross_laugh_close
            with charachange

            mi "That's okay if you don't know, neither do I! Wahahaha!"

            show shizu basic_normal2
            with charachange

            shi "…"

            show misha perky_smile_close
            with charachange

            mi "So it's settled, then! All right, all right!"

            hi "What? Didn't you hear what I just said?"

            show shizu adjust_happy
            with charachange

            shi "…"

            show misha sign_smile_close
            with charachange

            mi "Now all that's left is the stakes! What the winner wins, or, more interestingly, what the loser loses!"

            hi "Hey!"

            "This is a very dangerous game I'm playing. Shizune herself is a very dangerous girl, if she can only think in terms of winning and losing."

            "If she views every time that I talk with her as some kind of battle of wills, I don't think I could take it."

            "That kind of thing drives people insane. She's too Machiavellian; before this I'd assumed she was just kind of stoic."

            "But nevertheless, I'm interested. In hindsight, I realize that I just challenged her to what is essentially a duel without any rules that won't end until one of us… what?"

            "I guess that's it. That's so vague. What are the conditions for winning or losing? The first person to feel stupid loses?"

            hi "I don't know, I've never had to think of anything like this before."

            show misha hips_smile_close
            with charachange

            mi "Never?"

            hi "Never."

            show misha perky_confused_close
            with charachange

            mi "So you have never gambled, Hicchan?"

            hi "I'm surprised you two have."

            show shizu behind_blank
            with charachange

            shi "…"

            show misha hips_grin_close
            with charachange

            mi "Oh, come on… It's just for fun, anyway! Between friends~!"

            show misha sign_smile_close
            with charachange

            mi "It's about causing humiliation, suffering, and absolute despair! Isn't that the point?"

            "Shizune puts a finger to her temple thoughtfully."

            show shizu adjust_happy
            with charachange

            shi "…!"

            show misha hips_smile_close
            with charachange

            mi "Hm… Ah, how about this, Hicchan: If you lose, you have to go to school one day without any pants on."

            hi "Are you insane?"

            "Although in comparison to what I was afraid she would say, it's pretty mild."

            hi "Can't we just bet money, like normal people?"

            show shizu basic_sparkle
            with charachange

            shi "…"

            show misha hips_grin_close
            with charachange

            mi "It's not like you could match my wager if we did~! Now, it's your turn! …But nothing perverted! Understand?"

            show misha hips_laugh_close
            with charachange

            mi "Hahaha!"

            hi "I think I need more time."

            "This is going to have me constantly on edge for weeks."

            show misha hips_grin_close
            with charachange

            mi "Okay~! Come on, you should both hurry up, your drinks are getting cold!"

            show shizu basic_happy
            with charachange

            "I quickly down the rest of my coffee as Shizune does the same, staring at me with a fierce look of competition in her eyes."

            "It seems like a waste for her to be gulping down something that someone may have died for her to enjoy."

            show misha sign_smile_close
            with charachange

            mi "Hicchan, are you sure you don't want to hang out tomorrow? A lot of people are looking forward to it; you don't want to miss out."

            "I mumble unintelligibly at her."

            show misha perky_confused_close
            with charachange

            mi "I don't really understand…"

            "It's time to think. Shizune's drink is smaller, but I can consume mine faster."

            "If Shizune finishes her drink first, she might skip out on paying, leaving me to pick up the tab, even though she said the drinks were on her."

            "Because I have no money on me, I would be humiliated, and therefore this could be considered a loss."

            "If I finish first, the laws of chivalry would make me look like a jerk, as I would need to run out of this teahouse, leaving her to pay for everything. That could also be considered a loss. She would use that."

            "In the event of a draw, she may attempt to run out the door, and I'll probably do the same. This might lead to a collision at the door, which would be humiliating, but not overly so. …And Misha would be left to pick up the tab."

            "This is really childish. I'm a little disappointed in Shizune, and myself."

            show misha perky_smile_close
            with charachange

            mi "Well, Hicchan, it'd be really nice if we could all celebrate how well we put everything together for the festival by taking a look at our handiwork…"

            "Misha seems oblivious to the fact that an epic battle of wills is raging in front of her. I nod slowly and down the last of my coffee."

            hi "Well, I am finished enjoying my drink. I guess it's time for me to leave. And I am going to leave now. Calmly."

            show shizu adjust_happy
            with charachange

            shi "…"

            show misha perky_confused_close
            with charachange

            mi "You too, Shicchan?"

            mi "Why are you two acting so weird?"

            scene bg suburb_shanghaiext
            with locationchange

            "I quickly walk out the door and Shizune follows. Misha is going to have to foot the bill."

            scene bg suburb_roadcenter
            with locationchange

            "Sorry, Misha."

            show shizu behind_smile at center
            with charaenter

            "Catching up to me, Shizune quickly pushes her glasses up and presses a note into my hand."

            call screen written_note(_("If you lose, you have to come hang out with us tomorrow."))

            hi "So you think you can win today? That's kind of cocky, Shizune."

            "I forgot for a second that she can't hear me. I nod."

            "Right now, she seems much cuter than she usually is, smiling softly with a hint of confidence coming through."

            "Shizune looks energetic and carefree, although it could just be the caffeine."

            show shizu adjust_happy
            with charachange

            "She winks, and extends her hand for a handshake. I wonder if there's a buzzer in there and she plans to shock me, but that doesn't seem like something she would do, so I accept."

            "With a squeeze, she pushes another note into my hand. I momentarily think that it's a buzzer and wonder if the shock could kill me."

            hide shizu
            with charaexit

            "Shizune smirks and then runs off."

            call screen written_note(_("You probably don't know how to get back to school from here.\n\nThere will be work waiting for you when you do. See you then~"))

            "I crush the note in my fist dramatically, but no one is there to see it, and that makes me sad."

            "I wonder if it's too late to go back to the shop and ask Misha for directions."

            "But then again, I gave her a hard time for not knowing the way here, so I can't allow her to score off me for not knowing the way back."

            "And if I ask her, Shizune could see it as a victory. No, it's not necessary."

            stop music fadeout 3.0

            "The school is on top of a damn hill, how hard could it be to find?"

            "I may be slightly directionally challenged, but I'm sure that even I can do this."

            scene bg school_courtyard
            with shorttimeskip

            play music music_happiness

            "About an hour and a half later, I walk the long paved path leading from the gates to the main building."

            scene bg school_lobby
            show shizu behind_blank at tworight
            show misha hips_grin at twoleft
            with locationchange

            mi "Hahaa! Just the person we were waiting for. So you made it here eventually, Hicchan, good! Now it's time for work work work~!"

            "Misha and Shizune had laid an ambush for me in the main lobby of the ground floor and I walked straight into it. I should have just circled around the school like I had originally planned, but I thought that I was overreacting and being silly."

            "Misha is waving a thick stack of printouts in my general direction, taunting me."

            show misha perky_smile
            with charachange

            mi "We sort of need your help~!"

            hi "Sort of?"

            show misha hips_grin
            with charachange

            mi "We need your help~!"

            show shizu cross_angry
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "You will help us!"

            "Misha speaks with her usual playful, carefree manner, but even so I can hear Shizune's unnervingly hard severity behind it."

            hi "That sounds like an order."

            mi "Really? Is it?"

            show shizu behind_frown
            with charachange

            shi "…"

            show misha perky_confused
            with charachange

            mi "Eh? It is?"

            show misha hips_laugh
            with charachange

            mi "Ah, sorry, Hicchan, I guess it is! Hahahaha!"

            "She doesn't sound very sorry at all."

            show misha hips_grin
            with charachange

            mi "I thought we had almost everything done by now, but it turns out we have all these signs to attach to backing boards."

            show shizu adjust_angry
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "More hands make light work!"

            show misha hips_laugh
            with charachange

            mi "And everybody wins! Hahahahaha!"

            show shizu basic_angry
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "This is your duty, after all, as a member of the Student Council. Which you are a part of."

            mi "As a member."

            mi "Of the Student Council."

            show misha hips_laugh
            with charachange

            mi "Ahahaha~!"

            show shizu behind_blank
            with charachange

            shi "…"

            show misha perky_smile
            with charachange

            mi "It's a simple task, so getting it out of the way now would be good. It's not that much work. A small thing, really!"

            show shizu basic_normal2
            with charachange

            shi "…"

            mi "And we'd really appreciate your help!"

            mi "Really, really appreciate it!"

            show misha hips_grin
            with charachange

            mi "Besides, it's time to pay back for us treating you so nicely!"

            hi "So the tea shop was a trap after all! You two-timing scoundrels!"

            show shizu behind_blank
            with charachange

            shi "…"

            show misha cross_smile
            with charachange

            mi "Don't say that, it was completely unrelated. We wanted to celebrate you joining the council!"

            "But why did she bring that up, then?"

            hi "But—{w=0.3}{nw}"

            show shizu cross_rage
            with charachange

            shi "…!"

            show misha hips_grin
            with characlose

            mi "No buts! You're coming with us!"

            show misha hips_grin at offscreenleft
            show shizu cross_rage at offscreenright
            with ease

            show misha cross_smile_close at closeleft
            show shizu cross_angry_close at closeright
            with ease

            "I don't even get to finish my sentence as they grab me by the arms and try to pull me towards their office."

            show misha cross_laugh_close
            with charachange

            "Misha laughs giddily as she and Shizune exchange sly looks behind my back."

            show shizu basic_angry_close
            with charachange

            shi "…!"

            mi "Ah, I don't think you have a choice in this, Hicchan! Hahahaha!"

            show misha hips_grin at twoleft
            show shizu basic_angry at tworight
            with charadistant

            mi "There are two of us, so don't even try to get away, now! Don't take us lightly!"

            show shizu behind_frown
            with charachange

            shi "…!"

            mi "Hicchan, it's your duty to help us, anyway! As a member of the Student Council!"

            hi "All right, all right! How could I forget?"

            hi "But, seriously, aren't there other people who can help you?"

            show misha perky_confused
            with charachange

            mi "Like who, Hicchan?"

            mi "You were fine with helping us yesterday…"

            hi "Yesterday is not today!"

            hi "And anyone who isn't me!"

            hi "Why don't you have anyone else in the council?"

            show shizu cross_wut
            with charachange

            shi "…!"

            show misha cross_laugh
            with charachange

            mi "That's what we'd like to know! …Aha… Ahahahahaha!"

            "Misha's laughter explodes through the hall. She doesn't notice the grimace on my face at all. That's right, it's just the two of them, isn't it?"

            hi "Oh, right. Okay, I'll help you."

            show misha hips_grin
            with charachange

            "Misha runs her tongue over her teeth, looking quite pleased."

            mi "That's my Hicchan! I knew we could trust you~!"

            show shizu behind_smile
            with charachange

            shi "…!"

            mi "So predictable~."

            stop music fadeout 2.0

            scene bg school_council
            with locationskip

            "When we get to the student council room, my jaw drops. The number of signs, backing boards, and signposts is insane."

            "They're stacked all over the place like building materials at a construction site, something I let Shizune and Misha know right off the bat."

            hi "There are so many signposts here you could probably build a second wall around the school with them!"

            play music music_ease fadein 4.0

            show shizu behind_blank at tworight
            show misha perky_smile at twoleft
            with charaenter

            mi "Hahaha~! Really? Well, there are a lot of them, so maybe…"

            show shizu basic_angry
            with charachange

            shi "…!"

            show misha perky_confused
            with charachange

            mi "Eh? No?"

            mi "How do you know that, Shicchan?"

            show shizu behind_frown
            with charachange

            shi "…!"

            mi "Really?"

            hi "Don't tell me she's actually considered it?!"

            show misha hips_grin
            show shizu adjust_smug
            with charachange

            "Shizune hesitates, then pushes her glasses up a bit as Misha lets out a very uneasy sounding laugh."

            "So she has considered it."

            show shizu basic_normal2
            with charachange

            shi "…!"

            mi "Ahaha! That's… irrelevant, Hicchan! Can you get on with making the signs, please?"

            hi "All right, all right."

            hi "I feel sort of lied to, though. I thought you said it wouldn't be that much work?"

            show shizu behind_blank
            with charachange

            shi "…!"

            show misha hips_smile
            with charachange

            mi "Ah, well, Shicchan meant it wouldn't be that much work for us."

            show shizu basic_normal
            with charachange

            shi "…!"

            mi "Someone has to supervise you while you do this, you know, to make sure you're doing it right. And those people will be us."

            hi "So what are you two going to do?"

            show misha cross_laugh
            show shizu basic_happy
            with charachange

            mi "Watch you! Hahahaha~!"

            show shizu adjust_happy
            with charachange

            shi "…!"

            show misha perky_smile
            with charachange

            mi "No, that was just a joke, Hicchan. We'll help out too, of course. The Student Council is really supposed to have a lot more people."

            show misha perky_sad
            with charachange

            mi "This is just a bad year. Fewer people than usual, even though we already didn't have many the year before."

            mi "And then there's just a lot more work than before, too."

            show shizu behind_smile
            with charachange

            shi "…!"

            show misha perky_smile
            with charachange

            mi "Besides, Shicchan likes working with you. And so do I!"

            mi "We've accomplished a lot more than we normally could, you know."

            stop music fadeout 7.0

            "I can accept that. Lately, they've been looking a little fatigued every time I see them."

            "Student council work is apparently a 24-hour-a-day thing, and from what I've seen and heard, there are just the two of them. Well, I guess I make it three."

            "They must work almost nonstop. I wonder how much time they spend working in this room, when I don't see them."

            "And I've even glimpsed Misha taking naps sometimes without Shizune at her side. By herself, Shizune has to be working 60-hour weeks doing her student council duties, on top of regular classes."

            scene bg school_council_ss
            with shorttimeskip

            play music music_tranquil fadein 3.0

            "Two hours pass, and I reach for a tack only to find the box is empty. Shizune grabs it before I can even say anything."

            show shizu adjust_happy_ss at tworight
            show misha perky_smile_ss at twoleft
            with charaenter

            "She smiles, tossing it expertly into a trash can along with another empty box of tacks."

            show shizu behind_smile_ss
            with charachange

            shi "…!"

            show misha hips_grin_ss
            with charachange

            mi "So you're out too, Hicchan? Don't worry, Shicchan says she'll get some more."

            show misha hips_laugh_ss
            with charachange

            mi "Hahahaha!"

            show misha hips_grin_ss
            with charachange

            mi "We went through a box too, but me and Shicchan decided to wait until you needed a new box as well before getting a new one."

            "Something about that strikes me as odd."

            hi "Wait, we both ran out of tacks just now? Wow, what a weird coincidence, huh?"

            show misha perky_smile_ss
            with charachange

            mi "Ah, well, actually, Hicchan, we ran out twenty minutes ago, and there was only one spare box of tacks, the ones we gave to you."

            mi "And you were flying through those pretty quickly, so~! we thought that we should wait until we both had no more tacks before getting more!"

            show misha sign_smile_ss
            with charachange

            mi "Then, Shicchan could go get fresh boxes of tacks for all of us at the same time. You know, for efficiency~!"

            show shizu basic_normal2_ss
            with charachange

            "Shizune nods, preparing to step out the door."

            hi "Wait a second, so what did you two do for the past 20 minutes?"

            show shizu adjust_happy_ss
            with charachange

            shi "…!"

            show misha hips_grin_ss
            with charachange

            mi "Ahaha~! Nothing, of course! What could we do? We had no tacks, Hicchan!"

            show shizu behind_smile_ss
            show misha cross_grin_ss
            with charachange

            "Shizune and Misha exchange knowing glances before they give me a perfectly synchronized and incredibly exaggerated simultaneous shrug."

            hi "I see. So you decided to take a break. Clever."

            show shizu adjust_smug_ss
            with charachange

            shi "…!"

            show misha hips_grin_ss
            with charachange

            mi "Oh, we know it was clever."

            hi "Whose idea was it?"

            show misha hips_smile_ss
            show shizu adjust_happy_ss
            with charachange

            mi "The both of us, of course, of course!"

            show misha cross_laugh_ss
            with charachange

            mi "Ahahaha~! Well, Hicchan, it was all Shicchan's idea."

            show shizu behind_smile_ss
            with charachange

            hide shizu
            with charaexit

            stop music fadeout 3.0

            "I turn immediately to Shizune, who gives me a curt wave and a surprisingly cheery smile before quickly vanishing out the door."

            show misha cross_grin_ss
            with charachange

            show misha at center
            show bg at bgright
            with charamove

            "Well then why didn't you just say you wanted to take a break!?"

            "I used to think that Shizune and Misha were polar opposites. Misha always seems so energetic and playful, like any other girl. Shizune, on the other hand, always seemed distant. Aggressively manipulative and vaguely scary, but distant."

            "There were times when I thought that she had no sense of humor. As cute as she was, I'd almost never seen her smile. Not to mention all the other things."

            "The analytical stare, the permanently stoic expression, and even her penmanship; so mechanically precise that everything she writes looks typed."

            "But Shizune and Misha really aren't as different as I'd thought."

            hi "I'm a little surprised."

            play music music_shizune fadein 5.0

            show misha perky_confused_ss
            with charachange

            mi "Why?"

            hi "Shizune. I didn't know that she liked to joke around like that."

            "What I mean to say is, I didn't know that she could act so girlish. It was actually pretty cute."

            show misha perky_smile_ss
            with charachange

            mi "You would be surprised, Hicchan."

            hi "Well, I didn't know you and her were so close, either, the first time I saw you."

            "I've always been curious as to how these two met."

            hi "Do you two go far back or something?"

            hi "Childhood friends?"

            hi "Next-door neighbors?"

            show misha perky_sad_ss
            with charachange

            mi "Haha… Sorry, Hicchan, it's not anything like that, even if it would be cuter that way."

            show misha perky_smile_ss
            with charachange

            mi "When I came to this school, they just placed me next to Shicchan, and she looked like a very serious person."

            show misha sign_smile_ss
            with charachange

            mi "And I thought, 'I'm going to be spending the rest of the year next to this person, maybe!'"

            mi "'So it would be nice if we could be friends! But~, I wonder if she'll like me.'"

            show misha hips_grin_ss
            with charachange

            mi "And I learned that she was deaf. You know, Hicchan, the first time I just thought she was ignoring me~!"

            show misha hips_smile_ss
            with charachange

            mi "But, luckily, I knew a little sign language, and we became friends."

            "I want to know where Misha learned how to sign, but I guess that's something for another time."

            show misha perky_smile_ss
            with charachange

            mi "Now, I guess we're always together. It's nice, I've always wanted someone to listen to me, and I think Shicchan likes having someone to talk to! So, everybody wins."

            hi "Heh. That's nice."

            show misha hips_grin_ss
            with charachange

            mi "That's it? You look disappointed, Hicchan, what were you expecting?"

            show misha hips_laugh_ss
            with charachange

            mi "Ahahahahaha!"

            show misha hips_grin_ss
            with charachange

            mi "You know, Hicchan, I don't think that me and Shicchan thanked you properly."

            hi "For what?"

            show misha perky_smile_ss
            with charachange

            mi "Joining the Student Council. You've been a real help to us, Hicchan! I think I will get a lot more sleep now~!"

            hi "Well, I'm glad I could help, if it helps a young woman sleep at night."

            show misha hips_smile_ss
            with charachange

            mi "That's an interesting thing to say, Hicchan."

            mi "Shicchan really appreciates you helping us out too."

            show misha at twoleft
            show bg at center
            with charamove

            show shizu behind_frustrated_ss at tworight
            with charaenter

            "At that moment, Shizune steps back into the room, looking slightly annoyed and sipping offhandedly from a juicebox."

            show shizu adjust_happy_ss
            with charachange

            shi "…"

            play sound sfx_dropstuff

            "She throws two boxes of tacks on the floor with a wry smile."

            show shizu basic_normal2_ss
            with charachange

            shi "…!"

            show misha sign_smile_ss
            with charachange

            mi "Ah, Shicchan."

            play sound sfx_crunchydeath

            show shizu behind_frown_ss
            show misha sign_confused_ss
            with charachange

            "Misha opens her mouth to speak, but then quickly closes it as Shizune suddenly crumples her juicebox with a crunch like the sound of breaking bones."

            show shizu basic_angry_ss
            with charachange

            shi "…!"

            show shizu adjust_angry_ss
            with charachange

            shi "…"

            show shizu behind_frown_ss
            with charachange

            shi "…!"

            "I can tell that each harsh, quaking hand gesture is most likely an epithet."

            hi "What's she saying?"

            show misha perky_confused_ss
            with charachange

            mi "It was just very hard to get these…"

            show shizu basic_angry_ss
            with charachange

            shi "…!"

            show misha sign_confused_ss
            with charachange

            mi "I guess that is an understatement, Shicchan…"

            "Shizune calms down a bit, straightening her glasses and lightly brushing her bangs back with one finger."

            show shizu adjust_happy_ss
            with charachange

            shi "…"

            show misha perky_smile_ss
            with charachange

            mi "It really wasn't a big deal in retrospect? That's forward thinking of you!"

            show misha hips_smile_ss
            with charachange

            mi "All right then, I guess the two of us should get back to work, Hicchan!"

            stop music fadeout 4.0

            hi "Sure, why not."

            scene bg school_council_ni
            with shorttimeskip

            "By the time we're done with the signs, it's already getting dark out."

            "I hadn't expected something like this to take so long. But then again, if it were that easy, I doubt Shizune and Misha would have asked for my help."

            play music music_dreamy fadein 2.0

            show shizu basic_normal at tworight
            show misha perky_smile at twoleft
            with charaenter

            "Shizune falls into a nearby chair, cracking her knuckles systematically and letting out a muted yawn."

            show shizu behind_blank
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "That's all for today, I guess! That's a good thing, Shicchan, I'm very tired, too."

            hi "That took longer than expected."

            show shizu behind_frustrated
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "You agree? Hahaha, we didn't expect it to take so long either! Not as planned!"

            show misha perky_sad
            with charachange

            mi "Aww, I'm so hungry. I just realized I haven't eaten all day."

            "Now that I think about it, I have eaten nothing since I woke up this morning, but right now I'm almost too tired to think about food."

            hi "I think they already stopped serving dinner."

            show misha perky_confused
            with charachange

            mi "This can't be happening! Hicchan, can you think of any way we could… obtain food?"

            hi "Obtain food?"

            "I don't like her tone of voice."

            show shizu adjust_happy
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "Why not order out? Oh, that's right, I guess I could do that."

            hi "Order out? From where?"

            mi "From town, of course!"

            hi "I didn't know they deliver to the school. Well, what are you going to get?"

            show misha hips_smile
            with charachange

            mi "Maybe some Chinese food!"

            hi "As long as you're going to, can I get in on it too? I'm also pretty hungry."

            show misha hips_laugh
            with charachange

            mi "Ahahaha~! Hicchan, you should have just said so in the first place!"

            show shizu basic_normal2
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "What's that? It's your treat? That's great! That's great!"

            show shizu behind_blank
            with charachange

            shi "…"

            show misha cross_laugh
            with charachange

            mi "Wahaha, that's true, if it wasn't for you, we wouldn't be here so late, Shicchan!"

            show misha cross_grin
            with charachange

            "Misha quickly grabs a menu from a drawer behind her and begins to enter the number slowly and carefully, as if she's used to messing it up."

            mi "What do you want, Hicchan?"

            hi "Well, I guess I'll just have some dumplings."

            show shizu behind_smile
            with charachange

            "I raise my hand in a gesture of thanks to Shizune, who responds with a very faint, split-second smile."

            show misha cross_laugh
            with charachange

            mi "Ahahahahaha~!! Hicchan, Shicchan is paying for everything tonight, it's all on her, so you can afford to splurge a little!"

            hi "Some shrimp fried rice too, then."

            show misha cross_grin
            with charachange

            mi "All right, all right! And you, Shicchan?"

            show shizu basic_normal2
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "A Chinese omelette? Okay, then."

            hi "Hey, Misha, does that really mean 'omelette'? Can I see that again?"

            show misha hips_grin
            with charachange

            mi "Sure! Haha! Like this, like this…"

            show misha sign_smile
            with charachangealways

            show misha perky_smile
            with charachangealways

            show misha hips_grin
            with charachangealways

            mi "And this is for what you ordered: Dumplings!"

            show misha perky_smile
            with charachangealways

            show misha sign_smile
            with charachangealways

            show misha hips_smile
            with charachangealways

            mi "Shrimp fried rice!"

            show misha hips_grin
            with charachange

            mi "I'm going to get soup and a stir-fry, you say that like this…"

            show misha sign_smile
            with charachangealways

            show misha perky_smile
            with charachangealways

            mi "And here's how much it all costs: 3685 yen!"

            show misha:
                "misha cross_laugh" with charachange

            extend " Wahahahaha~!"

            hi "Well, I don't know in how many situations I'll need to remember such an exact number…"

            mi "Ahahahaha! Okay~! I'm going to order now, unless anyone wants something else. No objections? All right all right, then!"

            scene bg school_council_ni
            show shizu behind_frustrated at tworight
            show misha hips_smile at twoleft
            with shorttimeskip

            "Shizune impatiently twirls a pair of chopsticks between her fingers as we wait for the food to arrive."

            hi "Hey, where did you get those?"

            show misha hips_grin
            with charachange

            mi "This isn't the first time we've ordered out, Hicchan, and they always give us a ton of chopsticks, for some reason, even when we tell them we're only two people."

            hi "And you two have accumulated a lot of them from a lot of long nights eating takeout in the office?"

            show misha cross_laugh
            with charachange

            mi "That's exactly it! Hahahahahaha!"

            show shizu basic_angry
            with charachange

            shi "…"

            show misha perky_confused
            with charachange

            mi "I'm overstating it?"

            show shizu behind_blank
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "Haha! That's right, Shicchan! Hey, Hicchan, did you know that once we've collected a hundred pairs of chopsticks from ordering out, we'll be able to take over the universe?"

            hi "I used to think that too, when I was little."

            show misha perky_smile
            with charachange

            mi "Hicchan, are you good at breaking them down the middle? I can never do it right, so I found the little pile of chopsticks Shicchan had saved up and practiced on at least twenty of them."

            show misha hips_grin
            with charachange

            mi "She was really mad about that!"

            show shizu adjust_blush
            with charachange

            shi "…!"

            "I let out a laugh as Shizune turns bright red with indignation. I didn't know she had such a childish side."

            stop music fadeout 5.0

            scene bg school_council_ni
            with shorttimeskip

            "When the food arrives, I dig in heartily, drinking one of the tiny cans of soda Shizune bought for us from one of the vending machines in the hall."

            "Thanking them both for the food, I head back to the dorms, ready to turn in for the night."

            scene bg school_dormhallway
            with locationskip

            "The dorms are eerily quiet except for the sounds of portable TVs and radios murmuring unintelligibly behind thin walls."

            $ renpy.music.set_volume(0.1,0.0, "ambient")
            play ambient sfx_cicadas fadein 4.0

            scene bg school_dormhisao_ni
            with locationchange

            "It's quiet here at night, and very peaceful. I can hear the crickets chirping outside my window, and see actual stars when I look up."

            "Tired, I try to fall asleep as quickly as I can, only feeling slightly robbed of my Saturday."

            stop ambient fadeout 2.0

            scene black
            with shuteye

            if _in_replay:
                return

    if force_route == FR_HANAKO:
        label .quiet:
            scene bg school_scienceroom at bgleft

            "The library seems as good a place as any to go. Hanako looked as if she was taken pretty off-guard by Lilly leaving, so she might want someone to talk to."

            "Slinging my bag over my shoulder, I make my way out of the classroom."

            stop music fadeout 4.0

            scene bg school_hallway2
            with locationchange

            "I walk down the hallway to the library, past a multitude of closed doors."

            "Through each one the sound of furious rehearsal can be heard. Rock music blares out of one door, almost as loud as a concert."

            "I guess that's one of the advantages of a private school; there are actually enough rooms to go around at a time like this."

            "And, when I think about it, the grounds and buildings of the school are kept in pretty good condition. That can't be too cheap."

            "I've heard that this place has some pretty serious benefactors."

            scene bg school_library
            with locationchange

            play music music_happiness fadein 1.0

            "The walls of the library only partially insulate the noise of the festival preparations, but they're the only sounds to be heard."

            "Not a soul stirs here, with everyone apparently enjoying the weather outside or working on festival events."

            "Yuuko isn't here either. Maybe she doesn't work on Saturdays."

            "I quietly walk through the library, now fairly familiar with its layout. I head to the back, where Hanako's private little corner is."

            "I run my hand along the spines of the books on the way through, feeling the individual texture of each as I glance across the titles."

            "I used to do this all the time at the library at the hospital. Some things never change, I guess."

            "Like the smell of a library. No matter how much care you take, the paper in books is always going to degrade with time."

            "Probably, no matter which library you go into, anywhere in the world, it must have that same, musty smell."

            "I find something that looks light enough to read without any major thought involved then look for Hanako in the reading area."

            scene ev hana_library_read_std
            with locationchange

            "Once again, she is sitting on a beanbag with her back to a bookshelf. Reading the same book she'd had in the classroom, she's slowly making her way through the pages."

            play sound sfx_pillow

            show ev hana_library_std
            with charachangeev

            "Unlike last time I saw her here, I quietly take a seat in a beanbag. The noise is enough to catch her attention, but not startle her."

            "This delicate routine that must be followed each and every time I try to talk to her almost feels like hunting game."

            hi "Is that the same book as before?"

            ha "Y-yes… I'm almost finished…"

            hi "Cool."

            "I wonder if I should…"

            hi "Do you mind if I borrow it when you're finished?"

            "My mouth is faster than my mind, it seems."

            ha "S-sure… you m-may not like it but…"

            hi "I'm sure it can't be that bad. After all, you've stuck with it, haven't you?"

            ha "I-I guess."

            scene bg school_library
            with locationchange

            "I settle into my beanbag and set about reading my own book that had been buried in my bag."

            "It's a light novel about pirates. To be honest I'm barely skimming over the words, having chosen the book merely because it belongs to a different genre than I usually read."

            "Finding it hard to muster enough enthusiasm to finish the book, and noting that I've inadvertently distracted Hanako quite a bit, I decide to try and make conversation."

            hi "So, I see Lilly left without you?"

            show hanako emb_downtimid at center
            with charaenter

            show hanako basic_worry
            with charachange

            "She nods before taking her eyes off her book. She must have been really into it after all."

            ha "Lilly said she had to go and… meet someone…"

            hi "Oh?"

            show hanako basic_normal
            with charachange

            ha "A-Akira. Her sister…"

            hi "Sister? I haven't heard her talk about her family…"

            show hanako cover_distant
            with charachange

            ha "She… she and Akira used to live together."

            hi "I thought all the students lived in the dorms?"

            show hanako cover_worry
            with charachange

            ha "T-they… I mean we… don't have to."

            hi "But it's easier, right? I mean, there's food here and you're close to school… I don't think I've ever been to class on time so often in my life."

            show hanako cover_smile
            with charachange

            "Her badly hidden smile proves quite rewarding."

            "In the back of my mind I know I have a bit of homework to catch up on, but it's quite comfortable in here. No one can find me and force me into working for their pet project, either."

            "Though now that I'm thinking about the festival, another question comes up…"

            hi "Hey, Hanako, what are you doing for the festival?"

            stop music fadeout 0.2

            show hanako def_shock
            with charachange

            "For a split second I think that Hanako is about to throw her book in the air from shock."

            ha "S-sorry…?"

            hi "I was just asking what you're doing for the festival tomorrow. Anything planned?"

            show hanako def_worry
            with charachange

            ha "I… I don't know."

            "Hanako answers in the way that people do when they don't want you to ask any more questions. I take it large crowds and loud music aren't really her 'thing.'"

            hi "Oh, okay."

            "Change the subject, change the subject…"

            play music music_happiness fadein 4.0

            hi "So, what's Lilly's sister like?"

            show hanako basic_normal
            with charachange

            ha "She… she's nice. She's pretty like Lilly, but she dresses… business-like…"

            hi "Business-like?"

            show hanako basic_distant
            with charachange

            ha "She… she's always wearing a suit…"

            hi "Ah, I see. And that makes her less pretty somehow?"

            show hanako emb_emb
            with charachange

            "Hanako gives an embarrassed shake of her head."

            ha "N-no… just… different."

            "I'll admit it, this has got me intrigued. To hear Hanako talk about someone other than Lilly is a first, and to be complimentary about it too…"

            "But as I try to picture this mystery sister, all I can think of is Lilly in a suit. And I can't imagine that not being attractive. Not at all."

            hi "Well, one day you'll have to introduce me to her."

            show hanako basic_bashful
            with charachange

            ha "O-okay."

            "Our brief conversation ends as abruptly as it started, and we both return to our novels."

            stop music fadeout 4.0

            scene bg school_library_ss
            with shorttimeskip

            "The passage of time is marked only by the gradual movement of the patch of light cast through the window."

            "Slowly, the noises from the various rehearsals in the building fade out and die as students start to get hungry and tired."

            "Just thinking about that makes my stomach start to turn knots around itself. I think it's time to head back."

            hi "Do you think Lilly would be back by now? I think I might head back to my dorm. I'm pretty tired from this week."

            "And not a word of that is a lie. Moving to a new school as it ramps up for a major event has been taxing, to say the least."

            "I can feel myself nodding off as I read my book."

            show hanako basic_smile_ss at center
            with charaenter

            ha "O-okay. I… I might stay here a little longer."

            "Looking at Hanako's book, I can see that she is only a few pages away from completing it."

            "For a moment I consider hanging around until she finishes, but once again my stomach turns, emitting a gurgling sound."

            hi "Sure thing. Well I'm going to head off before it gets dark. I'll see you around, okay?"

            show hanako basic_bashful_ss
            with charachange

            ha "O-okay. See you, Hisao."

            hi "Later."

            show hanako defarms_worry_ss
            with charachange

            ha "H-Hisao?"

            hi "Hmm?"

            show hanako emb_smile_ss
            with charachange

            ha "T-thank you. F-for hanging out with me."

            play music music_dreamy fadein 2.0

            "I can see how hard it was for her to get that simple sentence out of her mouth. It leaves me hanging for a moment."

            "So. There is someone in this school who is even lonelier than me. Maybe lonely is a wrong word, I haven't been lacking company for this first week, but I've still managed to feel somewhat alone and detached."

            "Maybe lonely is a wrong word for Hanako too, she has Lilly after all, doesn't she?"

            "I realize I've been standing there far too long without answering, and pull off a flawless, not too exaggerated smile."

            hi "You're welcome."

            hi "Good night, Hanako."

            show hanako emb_downsmile_ss
            with charachange

            ha "N-night."

            scene bg school_hallway2
            with locationchange

            "I leave her to finish her book and head back to the dorms and the promise of food…"

            stop music fadeout 3.0

            scene black
            with Dissolve(3.0)

            if _in_replay:
                return

    return

label a1c14o1:
    hi "I keep wondering that myself. The lack of anything better to do, probably."

    show nomiya veryhappy
    with charachange

    "He lets out a hearty laugh, then checks his watch."

    show nomiya smile
    with charachange

    no "I really must take my leave now. Tezuka, I'm pleased to see that this little project is going so well."

    show nomiya talk
    with charachange

    no "I just stopped by to remind you to not run off by yourself, tomorrow. I've invited certain people to the festival for you, and I'm sure they'd like to meet you as well."

    show nomiya smile
    with charachange

    no "Also, Monday's club meeting is off, since I'm going out of town. I guess you kids can do something among yourselves, if you want to."

    hide nomiya
    with charaexit

    stop music fadeout 4.0

    show rin at center
    show bg at bgleft
    with charamove

    "He leaves, turning around flamboyantly, then walking off as dramatically as it's possible to walk."

    "What a weird teacher."

    hi "I'll be off, too. See you around, Rin."

    "Holding up a hand, I turn to go up the stairs to the dorms."

    "Maybe, if I can finish reading these books today, the entirety of tomorrow will be free for the festival."

    scene black
    with Dissolve(3.0)

    return

label a1c14o2:
    hi "I guess I'm a little interested in the art club."

    "I blurt it out, partially inadvertently."

    show nomiya talk
    with charachange

    no "What do you mean?"

    hi "Nothing… specific."

    hi "I wonder if I could come by sometime. Even if it's just to observe or something."

    hi "I've been thinking that I should join some club or something, so…"

    "It's in no way a premeditated move, but a vague sense of determination has really been building inside of me for this past week."

    "I want to do something. I want to belong somewhere."

    "It might as well be the art club, my shortcomings notwithstanding."

    "The teacher seems pleased."

    show nomiya veryhappy
    with charachange

    no "Oh? You want to join? Well, we always welcome new people, of course."

    no "Club meetings are normal enough. We study various aspects of the fine arts and try our hands at them, as well."

    show nomiya frown
    with charachange

    no "Or feet."

    "He gives an embarrassed cough, but Rin doesn't seem to mind. I take a small amount of comfort from the fact that I'm not the only one with vocabulary difficulties in this school."

    "Nomiya rebounds from his faux pas by theatrically checking the time from his huge, gleaming pocket watch, and slaps his forehead even more theatrically."

    show nomiya veryhappy
    with charachange

    no "I really must take my leave now, but if you have questions, I'm sure Tezuka can clarify."

    "Somehow, mentioning 'clarify' and Rin in the same sentence doesn't feel right. However, I don't say as much to the teacher, since he seems to be in a hurry."

    show nomiya smile
    with charachange

    no "Tezuka, I'm pleased to see that this little project is going so well."

    show nomiya talk
    with charachange

    no "I just stopped by to remind you to not run off by yourself, tomorrow. I've invited certain people to the festival for you, and I'm sure they'd like to meet you as well."

    show nomiya smile
    with charachange

    no "I hope I'll see you on Monday, then, Nakai."

    stop music fadeout 6.0

    hide nomiya
    with charaexit

    show rin at center
    show bg at bgleft
    with charamove

    "The teacher leaves, and we are left by ourselves again. Rin is still painting as if nothing notable happened. Since nothing in fact did, I am left wondering what on Earth is wrong with me."

    "Art and I haven't worked well together in the past, at least judging from the grades I used to have in middle school."

    "Maybe a club will be different than an obligatory class. Who knows?"

    "I try to come up with something meaningful to ask about it, but to no avail."

    "I'll just go to a club meeting and see how it goes."

    hi "So he invited some people tomorrow just to check out your painting?"

    show rin basic_absent
    with charachange

    rin "He has a lot of art-people friends. They like to talk about art."

    show rin basic_awayabsent
    with charachange

    rin "I think he wants me to talk about art with them."

    hi "Somehow, I get the feeling that you aren't too thrilled about it."

    "Rin shrugs noncommittally, but it still gives an impression of her general displeasure at the idea of having to discuss her painting, or any painting, with other people."

    show rin basic_deadpan
    with charachange

    play music music_rin fadein 5.0

    rin "I don't really like talking about art. It is already a way to talk without talking, so why bother talking about it?"

    hi "I can understand that."

    show rin basic_deadpannormal
    with charachange

    rin "It's like being bored and talking about being bored, because you are bored."

    hi "I'm not following you."

    show rin negative_spaciness
    with charachange

    rin "Have you ever talked about being bored? It's pointless and not very exciting. All you can really say about it is 'I'm so bored.' I once spent a week trying to think of something meaningful to say about boredness."

    rin "It was the most boring week I've ever had."

    hi "But that's pretty fitting, don't you think?"

    show rin basic_deadpan
    with charachange

    "Rin gives me a look, the laconic kind that looks like it doesn't mean anything but it does."

    hi "Anyway… I don't know, I guess I just rarely can come up with anything to say about art."

    hi "I mean, like this one you're doing now. I have no idea what to think about it, except that it looks nice. What is this painting about?"

    show rin basic_deadpannormal
    with charachange

    rin "It's not about anything at all."

    "…"

    show rin basic_deadpandelight
    with charachange

    rin "That's what I'd like to say. So I did."

    show rin basic_deadpannormal
    with charachange

    rin "But that was a small lie. I said it anyway because I would kind of like it to be true."

    rin "Teacher wanted me to do this, but I didn't have any ideas. I tried to have some, but nothing happened."

    show rin negative_spaciness
    with charachange

    rin "So now this is a painting without any ideas."

    hi "But… what are you painting then?"

    show rin basic_absent
    with charachange

    rin "No idea."

    show rin basic_delight
    with charachange

    rin "Come to think of it, I think I'll call this 'No idea.'"

    show rin negative_worried
    with charachange

    rin "Ah, now I started thinking again. This is bad."

    show rin basic_absent
    with Dissolve(0.15)

    show rin negative_worried
    with Dissolve(0.1)

    show rin negative_worried
    with Dissolve(0.05)

    show rin basic_absent
    with Dissolve(0.05)

    show rin negative_worried
    with Dissolve(0.05)

    show rin basic_absent
    with Dissolve(0.05)

    show rin negative_worried
    with Dissolve(0.05)

    show rin basic_absent
    with Dissolve(0.05)

    show rin negative_worried
    with Dissolve(0.1)

    show rin basic_absent
    with Dissolve(0.15)

    show rin negative_worried
    with Dissolve(0.5)

    "She shakes her head vigorously for a while, trying to shake 'thinking' out of her head. That amber-red hair flies wildly around."

    show rin basic_deadpannormal
    with charachange

    rin "This is why I had Emi help me. She makes it easy to not think about anything."

    rin "You know, how she just talks talks talks about nothing for hours. It's like her head is made of bubblegum foam bath jelly."

    show rin basic_deadpandelight
    with charachange

    rin "You are kinda the same, but not really. It's very helpful if you stay here."

    stop music fadeout 5.0

    "I am not sure if that's a compliment or not. It's probably neither; with Rin being the overtly neutral person she is."

    hi "So is there anything specific you'd like me to do to make you not think?"

    show rin basic_deadpan
    with charachange

    rin "Just be."

    hide rin
    with charaexit

    "So without knowing what I should do, I just sit on an empty box to watch her continue with the painting, idly leafing the pages of the beer-drinking book."

    play music music_dreamy fadein 1.0

    scene bg mural_part
    show rin negative_spaciness_close at tworight
    with locationchange

    "Rin has a serene expression on her face, her dark green eyes hiding what she might think behind them. No wait, she's supposedly not thinking anything, right?"

    "She quietly hums to a tune, interrupting every now and then with polite requests for more paint or another kind of brush."

    "Her concentration is admirable, even though she seems to be sleep-deprived and under pressure to finish the job."

    "Inch by inch the painting gains more form, details being added on top of details, colors entwining with each other, filling the empty spaces, growing on top of each other."

    "I find myself thinking about inspiration and motivation to create art again."

    "Where does one get ideas? They don't come out of nowhere, and I don't think there are muses that magically inject some inspiration in your head."

    "Ideas have an origin and a purpose."

    "The more I think about it, the more I'm convinced that Rin is lying about her mural, or at least twisting the truth. Maybe she doesn't even realize it, herself."

    "You can't do anything creative without having an idea of what you are going to create. That would go against the definition."

    "Every stroke must be decided to be drawn. Even if it's made at random, then that, too, is a conscious decision."

    "So her painting, even this one, must be based on having some deliberate goal or idea of what to paint."

    "If Rin's idea is to have no idea, as she said, does that count as having an idea?"

    "A logical paradox? That seems to be Rin's modus operandi for most normal interactions, so it wouldn't surprise me if she hadn't even noticed this herself."

    "I wonder if I should bring it up, but I'm not sure if I want to engage in an argument about logic with this girl."

    "One of us would probably end up short-circuiting fairly quickly, so I discard the thought."

    show rin basic_awayabsent_close
    with charachangealways

    show rin negative_spaciness_close
    with charachangealways

    "Rin is squirming and shuffling restlessly."

    show rin negative_annoyed_close
    with charachangealways

    show rin negative_spaciness_close
    with charachangealways

    "Even her usual blank visage breaks occasionally into pretty difficult looking expressions, the kind that one doesn't just come up with accidentally."

    show rin negative_annoyed_close
    with charachange

    hi "Everything all right?"

    rin "Yes. No."

    rin "My back started hurting again."

    rin "This painting is too big, after all, and it's hard to paint in this position."

    hi "Want to take a break?"

    show rin basic_deadpanupset_close
    with charachange

    rin "After I finish this part."

    show rin negative_annoyed_close
    with charachange

    "Of course, she doesn't take a break, and I don't bring it up again because that would be completely and utterly pointless."

    scene bg school_dormext_half_ss
    with locationchange

    "Rin continues her work and I stay with her: I like to watch her paint, and I'm going to be a member of the same club she's in, now."

    stop music fadeout 4.0
    $ renpy.music.set_volume(0.5,0.0, "ambient")
    play ambient sfx_cicadas fadein 3.0

    scene bg school_dormext_full_ni
    with Dissolve(3.0)

    "When she declares the mural to be finished, it's already so dark that I have no idea how she can tell."

    "There is no celebration, no general sense of a job well done, just a tired and laconic 'I'm done' and then we both go to sleep."

    stop ambient fadeout 3.0

    scene black
    with Dissolve(3.0)

    return
