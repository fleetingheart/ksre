# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a2_hanako:
    label .to_town_to_town:
        scene black

        $ renpy.music.set_volume(0.0, 0.0, channel="ambient")
        play sound sfx_alarmclock

        pause 1.2

        play sound sfx_impact2

        $ ach("act1hanako_achieve")

        "My alarm blares into my ears, only to be swiftly silenced by my fist."

        scene bg school_dormhisao
        with openeye

        "My body switches into auto-mode, carrying my subconscious self out of bed and into my uniform."

        "As always, my bottles of pills sit on my desk patiently, waiting for me to take them and pick out my daily dosage of medicine; seventeen pills a day."

        scene bg school_scienceroom at bgright
        with locationskip

        "Before I know it, I'm opening the door to class 3-3, glad to see that I'm not the only one who seems to be a little hung-over from festival week."

        "Every face in the classroom looks gaunt. With the festival now over, it's as if everyone's life dreams have been achieved."

        "With nothing left to live for, the students have relied on instincts alone to guide them to class."

        "Or maybe I'm just reading too much into it."

        "I slowly make my way to my seat, and it's only then that I realize why the room is so peaceful."

        "The seats beside mine are blissfully empty; the world's loudest interpreter for the deaf has yet to arrive."

        play sound sfx_doorslam
        play music music_running

        show misha hips_grin:
            offscreenright
            easein 0.3 right
        with vpunch

        show misha at right

        "Just as I am about to sit down, the door flies open, revealing a resplendent Misha; drills bobbing from the dramatic entrance and arms stretched towards the sky."

        show misha hips_laugh
        with charachange

        mi "Ya-hooo~! It's all over!"

        "It would appear that not everyone is affected by the post-festival depression."

        "The rest of the class glare at her, obviously thinking the same thing I am."

        show misha sign_confused
        with charachange

        "Misha, still frozen in the doorway with her arms still in the air, nervously looks around."

        "It's obvious that she senses the foul mood, but can't work out exactly what to do."

        show misha at center
        with charamovefastest

        "Suddenly, she jerks forward."

        show misha perky_sad
        with charachange

        mi "Hey!"

        show shizu adjust_happy behind misha at offscreenright
        with None

        show misha at twoleft
        show bg at center
        show shizu at tworight
        with charamovefaster

        "As she stumbles into the classroom, she reveals Shizune, arm still extended from where she shoved Misha."

        show shizu basic_normal
        with charachange

        shi "…"

        hi "Thanks for the entertainment, but shouldn't you two take your seats?"

        show shizu behind_frown
        with charachange

        shi "…"

        "Still slightly embarrassed, Misha takes a few seconds to realize she has to translate."

        show misha sign_smile
        with charachange

        mi "Oh! Yeah! Shicchan says she's not happy with you ditching us last week."

        show misha cross_frown
        with charachange

        mi "We were really busy!"

        hi "Is that so? What about the stuff I already did for you two?"

        show shizu cross_angry
        with charachange

        shi "…"

        show misha hips_grin
        with charachange

        mi "She says that only counts for council members. Since you declined, she doesn’t owe you anything."

        show misha hips_grin_close
        with characlose

        "Misha leans closer, and whispers conspiratorially into my ear."

        mi "Actually, I think she's just a little sore that you didn’t spend the day with her."

        show misha hips_smile_close
        with charachange

        mi "She's really thankful for your work last week though."

        show shizu behind_frustrated
        with charachange

        "Sensing that she is being talked about, Shizune lightly raps her fingers on her desk until Misha turns around to face her."

        show misha sign_smile
        with charadistant

        show shizu basic_angry
        with charachangealways

        show misha hips_grin
        with charachangealways

        show shizu adjust_blush
        with charachangealways

        "I can't understand any of the fast-paced signing that's going on, but from Shizune's slightly embarrassed expression, and Misha's poorly contained laughter, I can guess."

        stop music fadeout 8.0

        "While this exchange is happening, the door opens once again, but this time at a much more reasonable pace."

        show hanako emb_downtimid at offscreenright
        with None

        show bg at bgleft
        show shizu basic_normal:
            xpos 0.42
        show misha hips_smile:
            xpos 0.18
        show hanako at right
        with charamovechangefaster

        "Hanako quietly enters the room, and pulls the door closed behind her."

        show hanako emb_timid
        with charachange

        "Peering out from under her hair, she quickly scans the classroom."

        "Our eyes meet, and she suddenly stiffens. She closes her eyes, takes a deep breath, and then walks over to my desk."

        show hanako cover_distant
        with charachange

        ha "G… good morning Hisao."

        hi "Morning Hanako. You're a little late, aren't you?"

        show hanako basic_normal
        with charachange

        ha "I… was talking to Lilly."

        show hanako basic_worry
        with charachange

        ha "A-about today."

        hi "Ah, so you've got her list then? We can leave straight after classes in that case."

        show hanako emb_smile
        with charachange

        ha "S-sure."

        hi "I'm looking forward to it."

        "Hanako briefly flashes her embarrassed smile at me then hurries off to her seat."

        scene bg school_scienceroom at bgright
        with shorttimeskip

        play music music_normal fadein 3.0

        "During classes, it becomes apparent that it's not only the students that are a little despondent after the festival."

        "Mutou simply gives us a list of exercises from the textbook and then sits behind his desk."

        "I totally forget about the brief lunch period for a moment, such is the banality of the day."

        play sound sfx_normalbell

        "It's mind-numbing, and everyone seems surprised when the bells signal the end of the lessons."

        show shizu basic_normal at tworight
        show misha perky_smile at twoleft
        with charaenter

        "As I am packing up my bags, Shizune and Misha flank and entrap me."

        show misha hips_grin
        with charachange

        mi "Say, Hicchan, it's still not too late to join up. There's a lot of post-festival paperwork for us to complete…"

        hi "Er, sorry Misha, I've… got plans…"

        show hanako cover_distant at offscreenright
        with None

        show bg at center
        show shizu:
            xpos 0.42
        show misha hips_grin:
            xpos 0.18
        show hanako at right
        with charamovefaster

        "As if sensing the cue, Hanako appears behind me, holding a small bag, and trying to avoid eye contact with the outside world."

        show misha cross_laugh
        with charachange

        "Misha's eyes open wide, then she bursts into laughter."

        mi "BWAHAHA! You move fast, don't you Hicchan~? We won't disturb your date any further! Bwahahaha!"

        show shizu behind_blank
        with charachange

        "Behind the roaring Misha, I see Shizune taking far too little interest in the scene. I might be taking this the wrong way, but I think she's deliberately ignoring me."

        show hanako emb_downtimid_close
        with characlose

        "I feel a gentle tug on my shirt, and turn to see Hanako's eyes fixed firmly on the floor."

        show hanako emb_timid_close
        with charachange

        ha "L… let's…"

        hi "Got ya. Shizune, Misha, I'll see you later."

        hi "And I'm still not interested in the council."

        show misha cross_grin
        with charachange

        mi "Spoilsport."

        stop music fadeout 2.0

        hide misha
        hide shizu
        with charaexit

        show bg at bgleft
        show hanako at center
        with charamove

        "Misha and Shizune retreat into the hallway, happily signing to each other."

        hi "Got all your stuff? Let's head off."

        play music music_soothing fadein 4.0

        scene bg school_gate
        with locationskip

        "Floods of students pour out of the school gates and onto the road into town."

        "It's a little weird. It's almost a scene from any other high school, but the illusion fades because of the occasional wheelchair or missing limb."

        "One thing I do notice is that nobody is alone."

        scene bg school_road
        with locationchange

        show hanako emb_downsad_close at center
        with charaenter

        "And, as Hanako and I pass through the gates, I notice that she closes the distance between us."

        "Not enough to be considered 'close', but she certainly isn't at her usual just-a-little-far position."

        "I guess we're not familiar enough for her to get as close as she does with Lilly."

        "However, even though she has moved a little closer to me physically, mentally she seems to have traveled a mile."

        "Her hands clutched around the leather straps of her bag to the point of whitening her knuckles, her head down and her mouth pursed closed."

        "She almost looks like she's being walked to the Principal's office for the first time."

        "I try to stifle a giggle at the thought, but it is futile."

        show hanako emb_timid_close
        with charachange

        ha "W-what's the matter…?"

        "I guess there's no point in hiding it…"

        hi "Sorry. For a second there it looked like you were getting in trouble."

        show hanako defarms_strain_close
        with charachange

        ha "W-w-what do you mean?"

        hi "I think you need to relax a little. We're not going too far, and it's only students around, right?"

        show hanako def_worry_close
        with charachange

        ha "R-right."

        "It bothers me a little to see Hanako so worked up."

        hi "And you do this every week, don't you?"

        show hanako basic_worry_close
        with charachange

        ha "Y-yes. With Lilly."

        "Of course. 'With Lilly.' I wonder, has she ever left the school without her?"

        "It doesn't seem like much at first glance, but Hanako's dependence on Lilly is absurdly heavy."

        "If she can't even handle leaving the school without her, how would she have managed to survive if the two had never met?"

        "Would she have found someone else to latch on to? And what drew her to Lilly?"

        "Was it her lack of eyesight, or was Lilly just kind enough to lend a hand?"

        "I wonder if anyone would have fit the bill."

        hi "Well, I'm here. Besides, we're not going far. It'll be over before you know it."

        show hanako emb_downsmile_close
        with charachange

        "Hanako's knuckles slowly regain their color as she tries to hide a small smile, but the effort of that seems to prevent further conversation."

        "We travel, side by side, down the winding road towards the town. The crowd of students thins as we continue along the sidewalk."

        "Faster students rush ahead, and the less mobile ones fall behind, rarefying the crowd into nothingness."

        scene bg suburb_konbiniext
        with locationskip

        "By the time we reach the convenience store we are practically alone."

        scene bg suburb_konbiniint
        with locationchange

        "Using me as a shield between herself and the attendant, Hanako moves through the narrow aisles, adding an assortment of items to her basket."

        "Bread, milk, tea… thyme?"

        "What kind of convenience store sells herbs?"

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear

        nvl show dissolve

        n "{vspace=60}Then again, nothing about this town seems normal, which may not be such a bad thing in retrospect."

        n "Everything is so different and uncomfortable; dwelling on such matters isn't really an option."

        n "When I think about that, it reminds me of Hanako."

        n "No matter how much you try, you can't escape her scars; they still interrupt my train of thought when I see them."

        n "As much as I don't want to admit it to myself, I think I'm forcing myself to try to ignore them."

        n "Not that I am scar-free myself. The jagged line down my sternum will never completely fade away."

        n "I just have the luxury of being able to hide it easily."

        n "{vspace=30}But, in a way, both of our scars remind me that we're all in this place for a reason."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl hide dissolve
        nvl clear

        "…"

        "Hanako throws one last item into her basket then sheepishly holds it out to me, along with a few bank notes."

        show hanako emb_downtimid_close at center
        with charaenter

        ha "C-c-could you p-please…"

        "It takes me a second to understand what she's trying to say."

        hi "Oh, you want me to pay for this?"

        show hanako emb_downsad_close
        with charachange

        "She nods, but doesn't look up."

        "I guess this task falls to Lilly on the usual occasions."

        hi "Sure. Lemme just grab a couple of things…"

        "Hastily I grab a few essential items for myself and head for the counter with Hanako in close tow."

        "The attendant gives me an indifferent nod as he scans in the items."

        "I suppose just ignoring us is one way to deal with the anomalies of Yamaku; they must get a lot of students here, being the closest store to the school."

        "The staff must all have their own way of dealing with us. Or maybe they don't; maybe it's only me who thinks twice about my unique schoolmates."

        stop music fadeout 2.0

        scene bg suburb_konbiniext_ss
        with locationchange

        "Our transaction complete, Hanako and I head back out onto the street."

        scene bg school_road_ss
        with locationskip

        play music music_tranquil fadein 10.0

        "The road is pretty much abandoned now. The students that were heading out have already left, and nobody has started returning just yet."

        "And, with only the school ahead on the road, there doesn't seem to be anyone else around."

        show hanako def_worry_close_ss at center
        with charaenter

        "The emptiness certainly reflects on Hanako; her arms by her sides each carrying a bag, her head no longer bowed, and back to the upright position…"

        "It's almost as if she were enjoying this walk."

        hi "So, why all these weird things? Mixed Spice? Why would you need that in school?"

        show hanako basic_normal_close_ss
        with charachange

        ha "I… sometimes… like to m-make food."

        hi "Well, yeah, so do I but… spices?"

        hi "That's a little more advanced, don't you think?"

        show hanako emb_blushing_close_ss
        with charachange

        ha "N-not really."

        hi "Well, I think it's cool. You'll have to teach me one day."

        show hanako emb_smile_close_ss
        with charachange

        ha "S-sure."

        "She doesn't seem all that sure, but pushing the point doesn't seem all that wise."

        "At the very least, she seems a great deal happier than she did on the walk down here."

        "That alone makes me a little happier."

        scene bg school_dormext_full_ss
        with shorttimeskip

        show hanako basic_normal_close_ss at center
        with charaenter

        "Outside the girls' dorm, Hanako and I sort out the grocery bags with our respective purchases."

        "In comparison, my things look positively plain."

        hi "I tell you, you're putting me to shame here…"

        show hanako defarms_shock_close_ss
        with charachange

        ha "N-no I'm not… I just…"

        hi "I'm only joking."

        show hanako def_worry_close_ss
        with charachange

        hi "I have a stack of homework that I skipped last week, so I must leave now."

        hi "Will you be all right getting that to your room?"

        show hanako cover_bashful_close_ss
        with charachange

        ha "Y-yeah."

        hi "Sure? Okay then. I'll see you tomorrow."

        show hanako basic_smile_close_ss
        with charachange

        ha "B-bye."

        hide hanako
        with charaexit

        stop music fadeout 7.0

        "We part ways, and I return to my room."

        scene bg school_dormhisao_ss
        with locationskip

        "Piles of papers sit upon my desk, begging to be completed. With the entire ruckus of the last week, I've barely had any time to catch up."

        "I tried to keep up with my studies while I was in the hospital, but some of this stuff I've never seen before, even back in my old school."

        "Totally unprepared, I pop the top on a can of drink, and get to work."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .tea_leaves:
        scene black

        play music music_daily fadein 6.0

        scene bg school_dormhisao
        with locationchange

        "The days are really starting to heat up."

        "This morning, I awoke covered in sweat."

        "By the time the student body starts leaving their dorms for breakfast and morning duties, the sun has taken full effect; oddly, that puts me in high spirits."

        "It's not even eight, yet I feel that this day is going to be one of those pleasant, tranquil, warm ones."

        "If I weren't at a school that considered every absence from class as a sign of a life-threatening situation, I'd consider skipping the whole day and just relaxing in the school gardens."

        "Yes, today will be a genuinely lazy day."

        "For a second, I stop in mid-stretch, and consider the nurse's warning about exercise. Maybe I should have kept up those morning jogs."

        "Running with someone like Emi might have been a little testing, but if I worked at my own pace…"

        "Ah, who am I kidding? I couldn't stick to something like that without some kind of motivation."

        "It's not like I sit around all day. The walk to and from the convenience store counts as exercise, right? Especially the walk back up the hill…"

        "Yeah, it's no big deal. Compared to months lying in a hospital bed I'm getting plenty exercise."

        scene bg school_scienceroom
        with shorttimeskip

        "It seems that I'm not alone in my appreciation of the day."

        "Nearly every member of the class is glancing through the window and into the tantalizing sky."

        "Even the steadfast Shizune seems to lack her usual vigor for schoolwork."

        "Misha, as brazen as ever, has even unbuttoned the top buttons of her shirt and is fanning herself with a note book."

        "I must have been staring, as she's now sticking her tongue out at me."

        "However, she shows no signs of halting her efforts, nor is she trying to hide the fact."

        play sound sfx_normalbell

        "The lunch bells seem to catch everyone by surprise, and the class empties at a much slower pace than usual."

        "The heat seems to be draining the need to rush from everyone."

        stop music fadeout 8.0

        "Well, almost everyone."

        show hanako emb_emb at center
        with charaenter

        ha "H… Hisao?"

        hi "Hey there Hanako, what can I do for you today?"

        "Hanako already has a lunch bag in hand."

        "I don't have to be a detective to work out where this is going."

        show hanako emb_smile
        with charachange

        ha "Um… would you like to have lunch with us again?"

        show hanako basic_bashful
        with charachange

        ha "I… I brought enough for everyone…"

        hi "Awesome. You don't have to be so stiff about it though."

        show hanako basic_normal
        with charachange

        ha "Ah… right."

        hi "I take it we're going to the tea room?"

        show hanako cover_worry
        with charachange

        ha "P… please."

        show hanako basic_normal
        with charachange

        ha "Lilly said she'll meet us in there, so we should… should…"

        hi "Should?"

        show hanako emb_smile
        with charachange

        ha "…should go ahead together…"

        hi "Sounds like a plan. This heat has made me pretty hungry."

        "Hanako breathes a sigh of relief, and I gather my things together."

        scene bg school_miyagi
        with locationskip

        play music music_happiness fadein 1.0

        "As usual, the aura of the tea room is refreshing, feeling isolated from the rest of the world."

        "Then again, the usual din of the school seems to be a bit subdued; most likely from laziness promoted by heat exhaustion."

        "Hanako slowly spreads her food on the table, intently focusing on every little movement, as if she's trying to keep her mind off other thoughts."

        "It's not much, but I can tell from her demeanor that she has prepared everything with utmost care."

        hi "I guess Lilly isn't here yet. Should we start without her?"

        show hanako emb_timid:
            center
            ypos 1.17
        with charaenter

        ha "S-she'll be here soon…"

        show hanako emb_downtimid
        with charachange

        "Hanako struggles with the lid of the container of rice."

        hi "Here, let me help with that…"

        "I take the container from Hanako's hands, and try to force open the lid."

        "Try as I might, it seems wedged shut."

        hi "Let me guess, did you put this in while the rice was still hot?"

        show hanako emb_sad
        with charachange

        ha "Y-yes. I was in a rush…"

        "I put the container on the table between us."

        hi "I thought so. It looks like this is wedged shut. We'll need some hot water to get it open."

        hi "But that could be a pain in here. We'd get water everywhere."

        li "Well, in that case, how about I contribute to today's meal?"

        show lilly basic_cheerful at offscreenleft
        with None

        show hanako emb_smile:
            tworight
            ypos 1.17
        show bg at bgright
        show lilly at twoleft
        with charamovechangefaster

        "At the door, Lilly smiles while holding up a bag stocked with various buns and bread rolls. I can't help but do the same."

        show lilly basic_smileclosed
        with charachange

        li "Since you two had a change of plans because of me, I thought I would bring a little something."

        hi "Thanks, Lilly. Here, let me get that for you…"

        show lilly:
            ypos 1.2
        with charamove

        "With a little guidance, Lilly's bread assortment joins Hanako's rice-less platter. I hastily make some tea to complete the picture."

        hi "Well, I'm looking forward to this."

        show hanako emb_downtimid
        with charachange

        "As I take a bite, I notice Hanako trying her hardest to not look like she is looking at me."

        "It's nothing special, but then again I can't really complain. I'm pretty lazy when it comes to cooking for myself."

        hi "Not bad, I guess this is made with the stuff you bought yesterday?"

        show hanako emb_blushtimid
        with charachange

        ha "Y-yes."

        "Hanako's eyes shout at me, begging for some kind of feedback."

        hi "Well it was clearly worth it. Thanks, Hanako."

        show hanako cover_bashful
        with charachange

        ha "I… I wanted to show you this… after yesterday…"

        hi "It's okay. I was just a little surprised at the stuff you were buying."

        show lilly basic_weaksmile
        with charachange

        li "Hanako's always liked to experiment when it comes to food. I think it's good… most… of the time."

        "While Lilly's smile doesn't waver, the slight change in her tone tells me that things have not gone so well in the past."

        "And it's not like Hanako has many people to sample her cooking…"

        stop music fadeout 7.0

        "Hang on… was Lilly waiting for me to go first? She didn't start eating until after I said it was all right…"

        "Her cheeky grin tells me that this was a deliberate action on her part. I'll have to try and work out how to get one over her in the future, to make up for this."

        hi "Well, it's good, and that's all that counts, right?"

        show hanako basic_smile
        with charachange

        ha "R-right."

        show lilly basic_smileclosed
        with charachange

        "Lilly, satisfied at not being the first to sample Hanako's creation, begins to consume the food in front of her."

        "I find myself staring as I watch her chopsticks gently touch the plate, their tips delicately poking and tracing to quickly ascertain the positions of the food as she dexterously picks it up."

        "One might think she were a child playing with her food if not for the situation, though she does it with such care and thoughtlessness that it's obvious this is simply how she eats this kind of meal."

        "Not wanting to miss out, I start filling up myself."

        show hanako emb_downsmile
        with charachange

        "Hanako takes a different approach, waiting until Lilly and I have our hands clear before quickly snatching up her share."

        show hanako emb_smile
        with shorttimeskip

        play music music_dreamy fadein 4.0

        "Before long the containers are empty, save for the still-shut rice container."

        show lilly basic_smile
        with charachange

        li "Thank you Hanako, that was filling."

        show hanako basic_smile
        with charachange

        ha "N-no… thank you for the bread…"

        hi "Yes, it would have been a disaster if not for that."

        show lilly basic_planned
        with charachange

        li "You're both welcome."

        show lilly basic_weaksmile
        with charachange

        li "But now, I must be getting back. It's far too easy to be late after eating here."

        hi "Yeah, I see what you mean. I think we'll just clean up here and then head off."

        show lilly basic_smileclosed at twoleft
        with charamovechangefaster

        li "Well then, good day."

        hide lilly
        with charaexit

        show hanako:
            center
            ypos 1.17
        show bg at center
        with charamove

        "Lilly leaves, her cane tapping away down the quiet hallway."

        "Hanako and I quickly pack our things and stay seated, waiting for the bell."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        scene bg misc_sky:
            xalign 0.0
            warp acdc_warp 20.0 xalign 1.0
        with locationchange

        "Together, we stare out the window and into the endless azure sky."

        play sound sfx_warningbell

        "If it weren't for the pealing of the bells, I would have sworn that time had stopped."

        "The urge to skip class rises in my gut."

        "I shoot a glance at Hanako, who shows no signs of moving either."

        ha "Not… just yet…"

        $ renpy.music.set_volume(1.0, 3.0, channel="music")

        scene bg school_miyagi
        show hanako basic_smile:
            center
            ypos 1.17
        with shorttimeskipsilent

        "The interval between the warning bells and the end of lunch bells passes in the blink of an eye."

        hi "We really should go… people will freak out and start a search party if we skip…"

        show hanako basic_distant
        with charachange

        "Hanako sighs."

        show hanako basic_normal
        with charachange

        ha "You're right."

        show hanako basic_normal at center
        with charamove

        "Slowly, she rises to her feet, and I follow suit."

        scene bg school_staircase2
        with locationskip

        "Silently, we make our way up the old stairs to the third floor and then to our classroom."

        scene bg school_hallway3
        with locationchange

        play sound sfx_dooropen

        "At the door, I take point and open the door ahead of Hanako, bowing my head down in apology in advance."

        scene bg school_scienceroom at center
        with locationchange

        stop music fadeout 5.0

        hi "I'm sorry we're late, teacher."

        play sound sfx_doorclose

        "I am greeted not by stern words, nor by an angered instruction to take my seat, but simply by the silence created by fifteen or so students trying not to laugh."

        "Mutou, ever tardy, has yet to arrive. However, the fact that Hanako and I have arrived together is blatantly obvious."

        show misha hips_grin at center
        with charaenter

        mi "Pff… pffwa…"

        "Make that about fourteen students trying, and one student failing."

        play music music_comedy

        show misha cross_laugh
        with charachange

        mi "Pft-bwahahaha! The lovers return~!"

        show misha hips_laugh
        with charachange

        mi "WAHAHAHA~!"

        hi "Yeah, thanks. You can calm down now."

        hide misha
        with charaexit

        show hanako emb_downsad_close:
            offscreenright
            ease 1.0 xpos 0.8
        with charaenter

        show bg school_scienceroom at bgleft
        with charamovefaster

        "I step through the door, and realize that Hanako is firmly pressed against my back, hiding herself from the class."

        show hanako:
            ease 1.0 xpos 0.7 alpha 0.0

        pause 1.0

        hide hanako

        "With my steps coming closer to my desk, she eventually breaks from me and stiffly walks to her own. Her efforts to mentally block everyone's presence from her mind are written fairly clearly on her face."

        scene bg school_scienceroom at bgright
        with charamove

        "Quickly checking the door for any signs of the teacher's arrival, I make a trip to Hanako's desk and whisper in her ear."

        hi "Don't worry about Misha, she's always like this. I enjoyed myself today. Don't sweat it, okay?"

        "Hanako nods her head behind her folded arms, but still doesn't show her face."

        play sound sfx_dooropen

        show muto normal:
            tworight alpha 0.0
            ease 1.0 center alpha 1.0
        with None

        show bg at center
        with charamovefaster

        show muto at center

        "I yearn to stay and console her more, but Mutou picks this exact moment to enter the class, halfway through his lecture, as if he started it in the hallway."

        show muto smile
        with charaenter

        mu "…which, of course, is directly proportional to the charge but inversely proportionally to the square of the distance…"

        hide muto
        with charaexit

        play sound sfx_doorclose

        "He's so engrossed in his speech that he doesn't even notice me sneaking back into my seat from Hanako's desk."

        "While Mutou's spiel rambles on, Misha leans over to me."

        show misha perky_smile_close:
            offscreenleft alpha 0.0
            ease 1.0 xanchor 0.5 xpos 0.16 alpha 1.0

        pause 1.0

        show misha:
            center
            xpos 0.16

        mi "The teacher may not have noticed your tardiness, but I did."

        "That much is obvious from the show you just put on."

        show misha hips_grin_close
        with charachange

        mi "I have been instructed to let you off the hook for today, but only on one condition."

        hi "Oh? And what would that be?"

        show misha sign_smile_close
        with charachange

        mi "You have to help us this afternoon~!"

        "I crane my neck to look over Misha's shoulder."

        "Shizune is conveniently not making eye contact with me."

        hi "Fine. Just for today."

        hi "I've already told you I'm not joining the council, remember?"

        show misha hips_grin_close
        with charachange

        mi "Of course! Doing so could be considered… um, considered…"

        show misha perky_confused_close
        with charachange

        "She looks down at her notebook, obviously looking for her place in her script."

        show misha hips_grin_close
        with charachange

        mi "…under duress and hence would be against regulations."

        hi "How very strange of you to be considerate of the regulations now."

        show misha sign_smile_close
        with charachange

        mi "Things should be done by the book!"

        show misha perky_smile_close
        with charachange

        mi "It's just that the book hasn't been written for every situation, so there are times when it can be ignored."

        hi "And yet, you two wonder why no one else wants to be in the Student Council…"

        stop music fadeout 3.0

        show misha hips_frown_close
        with charachange

        pause 0.3

        show misha:
            ease 1.0 offscreenleft alpha 0.0

        pause 1.0

        hide misha

        "After poking her tongue out at me, Misha returns to her workbook, and we battle our way through the latter half of the school day."

        with shorttimeskip

        play sound sfx_normalbell

        show shizu behind_blank_close at offscreenright
        show misha hips_smile_close at offscreenleft
        with None

        show misha at twoleft
        show shizu at tworight
        with charamovechangefastest

        "Before I can even stand up, Misha and Shizune have placed their hands on both my shoulders."

        hi "Hey, I said I'd help out, damn…"

        play music music_shizune fadein 1.0

        show misha hips_grin_close
        with charachange

        mi "This is just insurance, Hisao, insurance~!"

        show hanako emb_timid behind shizu at offscreenright
        with None

        show misha hips_smile_close:
            xpos 0.17
        show shizu:
            xpos 0.5
        show bg at bgleft
        show hanako:
            xanchor 0.5 xpos 0.9
        with charamovechangefaster

        ha "H-Hisao?"

        "Hanako timidly tries to leave the room by circling around us and I suddenly realize that this may be my one chance to escape."

        hi "Oh hey Hanako. What's up?"

        show shizu basic_angry_close
        with charachange

        shi "…"

        show misha hips_frown_close
        with charachange

        mi "Hey, what makes you think you've got time to chat?"

        hi "Oh relax, this won't take long… sorry Hanako, you were saying?"

        show hanako emb_downtimid
        with charachange

        ha "I… I was going to go to the library, and… and I thought…"

        "Hanako's thumbs dance around each other and her eyes flit around the room, looking everywhere but at us."

        show misha sign_smile_close
        with charachange

        mi "Sorry Hanako, but Hisao has to come with us. He's got work to do."

        show shizu behind_smile_close
        with charachange

        shi "…"

        show misha hips_grin_close
        with charachange

        mi "Oh! But you can help too if you'd like."

        show hanako cover_worry
        with charachange

        ha "Um…"

        if _in_replay:
            return

    menu:
        with menueffect
        mi "So, how about it, Hisao?"

        "What do you think, Hanako?":
            $ ask_hanako = True

        "I've done enough work for the council already.":
            $ ask_hanako = False

    if ask_hanako:
        label .office_confessional:
            scene bg school_scienceroom at bgleft
            show hanako cover_worry:
                xanchor 0.5 xpos 0.9
            show shizu behind_smile_close at center
            show misha hips_grin_close:
                xpos 0.17 xanchor 0.5

            hi "What do you say, Hanako? If we all help it shouldn't take long at all."

            show hanako emb_timid
            with charachange

            "Hanako's fidgeting answers my question before she can even form the words."

            show hanako emb_downtimid
            with charachange

            ha "I… I really need to go…"

            "Well, that was to be expected. Looks like it's just me and the council girls again."

            "It's easier to resign myself to another afternoon's work in the small council office."

            hi "I'll catch up with you later, okay?"

            show hanako emb_smile
            with charachange

            ha "O-okay."

            stop music fadeout 3.0

            show misha at twoleft
            show shizu at tworight
            show hanako at offscreenright
            show bg at center
            with charamovefaster

            hide hanako

            show misha hips_smile_close
            with charachange

            mi "Right! Now that the farewells are over, it's work time!"

            scene bg school_hallway3
            with locationchange

            "Misha and Shizune frog-march me to the student council office, never once letting go of my shoulders."

            "I feel a little bad for ditching Hanako like this, but if this is the price of getting Misha off her back, so be it."

            scene bg school_council
            with locationchange

            hi "So then, what are we up to today?"

            show misha sign_smile at center
            with charaenter

            play music music_ease fadein 8.0

            mi "Debrief!"

            hi "Huh? Isn't that supposed to happen after something?"

            show misha hips_grin
            with charachange

            mi "Yup! We have to collate all of the information from the festival so that Shicchan can debrief the teachers."

            show misha at twoleft
            show bg at bgleft
            with charamove

            show shizu adjust_happy at tworight
            with charaenter

            "Shizune drops a large pile of paperwork on the desk in front of me, and smiles succinctly."

            show misha hips_smile
            with charachange

            mi "You need to sort those out into two piles."

            show misha sign_smile
            with charachange

            mi "One for financial stuff, like receipts, one for feedback, one for positive feedback, maybe one for things that look like they could be problems next year, one for problems that probably won't be able to be fixed…"

            hi "That's a few more than two piles…"

            show misha perky_confused
            with charachange

            mi "Huh? Oh, right. Yeah I thought it would be only two piles. My bad."

            hi "Right. While I'm doing this, what will you two be doing?"

            show misha hips_grin
            show shizu adjust_smug
            with charachange

            mi "Well, we missed lunch because we were collecting all of these reports, so we're going to go get some food!"

            "Why didn't you just sort them out while you were collecting them…"

            "Thankfully my self-defense mechanism kicks in and prevents me from opening my mouth and further worsening my situation."

            show misha perky_confused
            with charachange

            mi "Eh?!"

            show misha perky_sad
            with charachange

            mi "How is that fair?"

            show shizu behind_blank
            with charachange

            shi "…"

            "I was fretting over the unfair distribution of work so much that I didn't notice that Shizune had kept on signing."

            "If it weren't for Misha's outburst, I probably wouldn't have noticed at all."

            show shizu adjust_smug
            with charachangealways

            show shizu basic_normal
            with charachangealways

            show shizu behind_blank
            with charachangealways

            "Shizune seems to be delivering a fairly long string of commands to Misha, and none of them look pleasant."

            show misha sign_sad
            with charachangealways

            show misha perky_sad
            with charachangealways

            show misha:
                ypos 1.15
            with charamove

            "Reaching a conclusion, Misha signs briefly back to Shizune, and then sits down at the desk next to me."

            show shizu adjust_happy
            with charachangealways

            hide shizu
            with charaexit

            show misha:
                xalign 0.5
            show bg at center
            with charamove

            "Shizune waves to the both of us before disappearing out the door."

            hi "What was all that about?"

            show misha perky_confused
            with charachange

            mi "Shicchan was worried that you'd get it all wrong unless you were supervised."

            show misha perky_sad
            with charachange

            mi "And since she can't tell you how you are messing things up, she's making me stay. Awww… bummer, I wanted to go with Shicchan!"

            show misha cross_smile
            with charachange

            mi "But she is going to bring us back some food~!"

            show misha cross_grin
            with charachange

            mi "How good is that!"

            "Misha's flippancy is out of this world. From down in the dumps to on top of the world over some calories."

            "It's hard to imagine how anyone could operate at that level."

            hi "Well, it could have been worse."

            hi "So what are we supposed to be doing?"

            show misha sign_smile
            with charachange

            mi "Collation."

            hi "I gathered that."

            show misha hips_smile
            with charachange

            mi "Well, let's just start making piles. We'll work out what the piles mean later."

            hi "Right…"

            show misha perky_smile
            with charachange

            "We start to separate all of the papers into increasingly complex piles."

            "At first it's just simple categories; financial, feedback, incident reports…"

            "Then they split apart into the good and bad reports, and further still, until it starts to look like we've just thrown the papers onto the desk."

            hi "This is hopeless."

            show misha perky_confused
            with charachange

            mi "Huh? Why? We're doing what we were told, right?"

            hi "Yes, but it looks like we're just making a mess."

            show misha hips_grin
            with charachange

            mi "No, I think we got a lot done. Shicchan will be able to work out the rest from here."

            show misha cross_grin
            with charachange

            mi "So I think we can stop about here then."

            "It's almost as if Misha's common sense left the room with Shizune."

            "Still, there's no point in arguing."

            show misha sign_smile
            with charachange

            mi "Anyway…"

            show misha cross_smile
            with charachange

            mi "What's the deal with you and Hanako?"

            hi "Deal?"

            show misha hips_smile
            with charachange

            mi "You were hanging out with her today, weren't you~?"

            show misha hips_grin
            with charachange

            mi "Have there been any fireworks? Any gossip that you're withholding from me~?"

            hi "If I told you about my own circumstances, it wouldn’t be gossip, would it?"

            show misha perky_confused
            with charachange

            mi "I guess not…"

            hi "We're just friends, I guess."

            hi "Why are you so interested? I thought you and Shizune didn't like her…"

            show misha cross_frown
            with charachange

            mi "It's not really like that. You know Shicchan and Lilly don't get along well."

            mi "And since you can't really get Hanako away from Lilly, we don't talk to her much."

            show misha sign_smile
            with charachange

            mi "But that doesn't mean that I can't be concerned for her."

            hi "What is there to be concerned about?"

            show misha perky_sad
            with charachange

            mi "Well, she never hangs out with anyone else, right? It's no good, Hicchan!"

            "If Shizune and Lilly dislike each other because 'their personalities are different' then I hate to think how Misha and Hanako would get along…"

            show misha perky_confused
            with charachange

            mi "I mean, in one way or the other, we're all in the same boat here, right~?"

            hi "Well, I guess."

            show misha sign_smile
            with charachange

            mi "This one time, when she left class halfway through, Shicchan went to the teacher and asked what was going to be done about it."

            show misha sign_confused
            with charachange

            mi "He said that every student here has special needs, and that Shicchan shouldn't worry herself about it."

            show misha perky_confused
            with charachange

            mi "Hanako never does any group work; she just runs off."

            mi "Isn't that enough to be concerned about?"

            hi "I guess you're right. She still hardly says a word when we're talking."

            show misha perky_sad
            with charachange

            mi "Well, that's more than I have been able to do. Shicchan and I both tried when she started, but she got scared and ran off."

            "I consider telling Misha that exactly the same thing happened with me, but she seems caught up in thought."

            "Listening to Misha without Shizune's influence is… interesting."

            show misha cross_frown
            with charachange

            mi "I think she needs to realize that people here don't care what she looks like, and that she can trust us."

            show misha cross_smile
            with charachange

            mi "If she could, I'd feel a lot better about her."

            "I think this is the longest I have watched Misha without seeing her sign."

            "When she's with Shizune, she is constantly waving her hands about, explaining the world to Shizune."

            "That amount of effort probably places a strain even on an agile mind."

            "And let's face it; Misha isn't the world's brightest spark."

            hi "Well, I'll keep an eye on her for you."

            hi "But you should probably apologize for earlier. I don't think Hanako is cut out for that kind of joke."

            show misha perky_confused
            with charachange

            mi "Oh? Oh~!"

            show misha perky_sad
            with charachange

            mi "I didn't even notice. Sorry."

            hi "Don't say it to me, just mention it to her."

            show misha perky_smile
            with charachange

            mi "All right. First thing tomorrow, I'll speak to her."

            hi "Good."

            play sound sfx_doorslam
            with vpunch

            "A cacophony from the door heralds the return of Shizune."

            "I guess she can't really tell how much noise she is making."

            show misha hips_grin
            with charachange

            mi "Oh, Shicchan! You're back!"

            show shizu behind_blank:
                xanchor 0.5 xpos 1.0 alpha 0.0
                ease 1.0 tworight alpha 1.0
            with None

            show misha at twoleft
            show bg at bgleft
            with charamovefaster

            show shizu at tworight

            "Shizune appears, completely laden with goods from the convenience store."

            show shizu basic_normal2
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "There was some surplus left from the festival. Since this is officially festival business, I've splurged a little."

            show misha hips_grin
            with charachange

            mi "Nice idea Shicchan, ten points."

            hi "Is that really allowed?"

            show shizu cross_angry
            with charachange

            shi "…"

            show misha cross_frown
            with charachange

            mi "For someone who refuses to join us, you seem to take an unhealthy interest in the politics of this council."

            show misha cross_grin
            show shizu adjust_smug
            with charachange

            mi "I shall punish your insolence by rationing your portion of the feast."

            hi "Fine, fine, I get it."

            show misha perky_smile
            show shizu adjust_happy:
                ypos 1.15
            with charamovechangefaster

            "Misha slides the multiple stacks of paper to one side to make room for the avalanche of food Shizune is spreading out."

            "As I watch my hard yet misdirected work become wasted, I realize that it's little wonder why these two need help."

            "The convenience store meal isn't overly tasty, but at the very least it's filling."

            show shizu behind_smile
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "Thanks for helping today. Most of the time we just make up the reports for the staff."

            show misha perky_smile
            with charachange

            mi "This year we can at least make up some relevant headings on the debrief."

            hi "Are you sure this isn't a corrupt organization?"

            show misha hips_grin
            with charachange

            mi "Not at all, not at all. We're by the book. It's not our fault if the book isn't specific enough."

            hi "I thought that was the definition of corruption…"

            show misha hips_smile
            with charachange

            mi "You think too much~!"

            hi "You know what? You're probably right."

            hi "Anyway, I must be off…"

            hi "…that is, if I'm allowed to leave."

            show shizu adjust_smug
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "Your work has been deemed sufficient. You may leave."

            hi "Well, thank you."

            hi "You know, if you stressed the 'free meal' side of things over the 'endless workload' side, you'd probably end up with more recruits."

            stop music fadeout 6.0

            show misha sign_smile
            with charachangealways

            show shizu behind_blank
            with charachangealways

            mi "You might just have a point."

            hi "Well, think about it."

            hi "And think about what we talked about… you don't have to tell that to Shizune if you don't want."

            show misha perky_confused
            with charachange

            mi "What? Oh, right. I'll try to see her tomorrow."

            show misha perky_smile
            with charachange

            mi "G'night, Hicchan."

            hi "Night Misha, Shizune."

            scene black
            with dissolve

            if _in_replay:
                return

    if not ask_hanako:
        label .chess_and_slides:
            scene bg school_scienceroom at bgleft
            show hanako cover_worry:
                xanchor 0.5 xpos 0.9
            show shizu behind_smile_close at center
            show misha hips_grin_close:
                xpos 0.17 xanchor 0.5

            hi "Hey, Shizune. I know I said I'd help, but I forgot I'd already made plans. Besides, I helped out more than my fair share last week, didn't I?"

            hi "I promise I'll make it up to you some other time."

            show misha sign_confused_close
            with charachangealways

            show shizu basic_frown_close
            with charachangealways

            show misha perky_smile_close
            with charachangealways

            show shizu behind_blank_close
            with charachangealways

            "Shizune and Misha release their grip on me and have a long, deep, and silent conversation."

            show misha sign_smile_close
            with charachange

            mi "Well, you have a point there. To be honest, we were only going to spend the rest of the budget on cakes."

            show misha cross_laugh_close
            with charachange

            mi "So, if you're not there, it works out better. More cake for us. Wahahaha~!"

            stop music fadeout 6.0

            show shizu at offscreenleft
            with charamovefaster

            show misha at offscreenleft
            with charamovefaster

            hide shizu
            hide misha

            "Shizune about-faces and marches out the door, and Misha skips out after her."

            hi "Well, that was a lot easier than I thought it was going to be. Last week those two were like bloodhounds. Or prison guards."

            hi "Or maybe prison guards bred from bloodhounds…"

            "I can't believe I just thought that, let alone saying it out loud. I think I need to move away from Kenji."

            hi "…Never mind. Anyway, should we go to the library?"

            show hanako basic_smile
            with charachange

            ha "S-sure."

            play ambient sfx_crowd_indoors fadein 0.5

            scene bg school_hallway3
            show crowd
            with locationchange

            "Hanako follows me through the still-crowded halls to the library, using me as a shield."

            stop ambient fadeout 0.5
            play music music_happiness fadein 2.0

            scene bg school_library
            show hanako basic_worry at offscreenright
            show yuuko neutral_down at center
            with locationchange

            show hanako at tworight
            with charamovefaster

            "As soon as we are through the door, Hanako bolts for the counter, where Yuuko is stacking books."

            show hanako emb_emb
            with charachange

            "Before I can catch up, Hanako has whispered something to her."

            show yuuko neurotic_up
            with charachange

            yu "Um, you'd find that in non-fiction, but I don't know where, exactly. If you want I can look it up…"

            show hanako emb_downsad
            with charachange

            ha "N-never mind."

            hi "Hey Yuuko, what's all this about?"

            show yuuko neutral_down
            with charachange

            yu "Oh, Hisao… Hanako was just looking for a book on…"

            show hanako emb_blushing
            with charachange

            ha "N-nothing…"

            hi "A book on nothing? In the non-fiction section?"

            show hanako def_strain
            with charachange

            ha "I… I was just…"

            show yuuko neurotic_up
            with charachange

            "I shoot a glance at Yuuko. She looks like she's about to burst from the pressure of keeping Hanako's request secret."

            hi "Yuuko, what did…"

            show yuuko happy_down
            with charachange

            yu "Chess! She's looking for a chess book!"

            "I make a mental note to never entrust Yuuko with any important information."

            show hanako defarms_shock
            with charachange

            ha "Y-Yuuko…"

            show yuuko panic_up
            with charachange

            yu "I'm sorry Hanako… it just slipped out…"

            hi "Well, it's not a secret any more. Come on, I'll give you a hand. I should really brush up on my skills, too."

            show hanako def_worry
            with charachange

            ha "O… okay."

            hide yuuko
            with charaexit

            show hanako at center
            show bg at bgleft
            with charamove

            "Yuuko disappears behind the counter in shame as Hanako and I wander into the depths of the non-fiction section."

            "I know there is supposed to be a system for categorizing these books, but I don't see how anyone can decipher it without spending half of their life researching it."

            "That's probably why all the librarians I know are neurotic."

            "Towards the end of the aisle, between a book on card tricks and some book on kid's games, stands a single book bearing the title 'Chess Tactics for Champions'."

            show hanako basic_bashful
            with charachange

            "Before I can reach for it, Hanako has the book in her hands, clutching it to her chest."

            hi "Well, I guess that's yours then. Mind if I borrow it when you're finished?"

            show hanako cover_worry
            with charachange

            ha "S-sure. I… I just haven't really played against anyone but L-Lilly before, so I thought…"

            "Damn. It's not like I was trying to beat Hanako deliberately or anything, but she seems to have taken it to heart."

            "Then again, at least this means she wants to play me again. That's a plus, right?"

            hi "Ha, well it's not like I'm a master or anything; I just played a bit before…"

            "It occurs to me that I haven't told Hanako about my condition. I falter for a second, deciding to cover my tracks. That is a conversation for another day."

            hi "…before I came here."

            stop music fadeout 6.0

            show hanako cover_distant
            with charachange

            ha "Are… are you all right?"

            hi "Yeah, I was just remembering something…"

            "When I think about it, I shouldn't be afraid to tell Hanako about my condition and my time in the hospital. Judging by her scars, she probably spent a fair amount of time in a hospital bed."

            "But, for some reason, I can't bring it up. At least not today, and not on short notice."

            "Eager to break off the conversation, I grab a random book from the shelf."

            "It's some book on the world's fastest roller coasters…"

            "…published in 1982. Well, not very up to date, but it should at least be interesting."

            hi "Well, we both got books now, should we go sit down?"

            show hanako cover_bashful
            with charachange

            "Hanako seems to accept my bluff, and we head to the reading nook in the back of the library."

            hide hanako
            with charaexit

            "Neither of us says a word; we simply open our books and start reading."

            "I try to read my book, but it would seem that in 1982 roller coasters weren't nearly as large as the ones built in the decades since."

            "Most of the ones listed are made of wood. Something about that doesn't seem safe to me."

            "If I'm going to ride on something potentially dangerous, I want it to be made out of steel, or some kind of space-age alloy that has big words like 'Titanium' and 'Ruthenium'."

            "I quickly lose interest, and my eyes wander across the reading area to rest on Hanako."

            show ev hana_library_read_std:
                zoom 1.0 truecenter
                easein 20.0 zoom 1.05
            with locationskip

            "Hanako seems absorbed in her book, flicking back and forth through the pages, as if confirming what she just read."

            "I wonder if that's actually effective, or if she's just overloading herself."

            "She unconsciously brushes her hair from her face, temporarily revealing her scar tissue."

            "I'm still not sure about the protocol here. Is it right to ask her about her scars? Or her past? How long was she in the hospital? Does she still visit the doctor?"

            "These all seem like the questions that you'd ask someone who just transferred to your school, translated into the local language."

            "But, to date, no one has directly asked me any of them. Well, except Rin, but I don't think I should use her as a guide to proper social behavior."

            "For the time being, I'll just keep my mouth shut. If someone wants you to know something, then they'll tell you. Trying to force the issue might drive Hanako back into herself."

            scene bg school_library_ss
            show yuuko worried_up_ss at center
            with shorttimeskip

            yu "Um… sorry to interrupt, but I have to close the library now."

            play music music_tranquil fadein 3.0

            hi "Already?"

            "I check my watch. Somehow, as I was lost in thought, nearly two hours have passed."

            show yuuko smile_down_ss
            with charachange

            yu "Do you want to check out those books? I can do it on the way out…"

            show hanako basic_worry_ss:
                center
                xpos 0.9 ypos 1.17 alpha 0.0
                ease 1.0 xpos 0.7 alpha 1.0
            with None

            show bg at bgleft
            show yuuko at twoleft
            with charamovefaster

            show hanako:
                tworight
                ypos 1.17

            ha "P-please."

            hi "I'm done. I'll drop this one back on the way through. It wasn't as interesting as I first thought."

            show hanako emb_timid_ss at tworight
            with charamovechangefaster

            "Hanako marks her place with a slip of paper and stands up. The girls head to the counter and I return my book to what I think is the right shelf."

            show yuuko neurotic_up_ss
            with charachange

            "Yuuko scans Hanako's book with practiced precision, yet still manages to fumble it."

            show yuuko neutral_down_ss
            with charachange

            yu "Oh… there we go. Third time lucky. Since this is a non-fiction book, you can only have it for a week."

            show hanako basic_smile_ss
            with charachange

            ha "T-that's okay."

            scene bg school_hallway2
            with locationchange

            "Yuuko shuts down the library's computer and herds us out the door."

            show yuuko panic_up at twoleft
            show hanako def_worry at tworight
            with charaenter

            yu "Argh! I didn't think it was this late already…!"

            hi "But you're the one that told us you had to close…"

            show yuuko worried_up
            with charachange

            yu "Yes but, I know but, that was before I looked at the time!"

            show yuuko neurotic_up
            with charachange

            yu "I'll see you later."

            show yuuko at offscreenleft
            with charamovefaster

            hide yuuko

            "Yuuko bolts down the hall, her handbag trailing behind her like an awkward streamer."

            show hanako at center
            show bg at bgleft
            with charamovefaster

            hi "I guess all librarians really are neurotic."

            show hanako emb_timid
            with charachange

            ha "Huh?"

            hi "Ah, never mind. I was just thinking that I've never met a librarian that can organize their time, no matter how good they are with their books."

            show hanako basic_smile
            with charachange

            ha "Oh… I k-know what you mean…"

            "Hanako smiles in amusement. It wasn't meant to be a joke, but I must have reminded her of some other librarian… or something…"

            show hanako cover_worry
            with charachange

            ha "I… I have to get back."

            hi "Yeah, me too. I didn't realize it was this late. Thanks for letting me hang out with you."

            show hanako basic_bashful
            with charachange

            ha "N-no problem."

            hi "I'm going to my dormitory room now anyway, so do you mind if I tag along?"

            show hanako emb_blushing
            with charachange

            ha "O-okay."

            hide hanako
            with charaexit

            "Hanako sets off ahead of me, and I need to jog a little to reach her side."

            scene bg school_dormext_full_ss
            with locationchange

            show hanako def_worry_ss at center
            with charaenter

            "We walk through the gardens, eventually arriving in front of the dorm buildings."

            hi "Man, you walk pretty fast. I used to play in a soccer club, and you manage to outpace me."

            stop music fadeout 6.0

            show hanako emb_downsmile_ss
            with charachange

            "I kinda regret saying that. It has less to do with her pace than with the fact that my condition has significantly worsened my fitness."

            "Hanako's reaction is odd. I expected an awkward attempt to downplay her walking speed, but she just blushes while looking at her feet and smiling."

            "Silence hangs in the air between us. That happens often around Hanako, but feels slightly different than usual this time. After a few seconds, I try to break the silence."

            hi "Here you go. See you in class tomorrow?"

            show hanako emb_smile_ss
            with charachange

            ha "S-sure."

            hide hanako
            with charaexit

            "Hanako waves a short goodbye before pushing her way through the dorm's doors. I stand and look at them for a while, before making my way to my own dormitory room."

            scene black
            with dissolve

            if _in_replay:
                return

    call timeskip

    label .rise_and_shine:
        scene bg school_dormhisao
        with locationchange

        "Chirping birds."

        "Normally, this would be a good time to reflect upon the beauty of nature."

        "But it is 6 AM."

        play sound sfx_pillow

        scene black
        with Dissolve(0.2)

        "Covering my head with the pillow, I slam my face into the mattress, hoping that the impact will send me instantly back to sleep."

        "Futile."

        "I toss and turn, but sleep simply won't return to me."

        play music music_daily fadein 10.0

        scene bg school_dormhisao
        with locationchange

        "All right nature, you've won. See? I'm getting up now…"

        "The lack of sleep weighs my mind down, and there's only one remedy for this; a nice, hearty breakfast."

        $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
        play ambient sfx_crowd_indoors fadein 0.5

        scene bg school_cafeteria
        with locationchange

        "It would be nice to be the first person here."

        "To be the first to dig into a piping hot pile of food, to sit wherever I desire…"

        "It would have been nice."

        "But even my exceptionally early start has put me behind the most diligent students."

        "I guess there are quite a few people that have early starts here, for one reason or another."

        "A group of students in sports clothes huddle around one table, eagerly discussing game plans inbetween inhaling great gulps of food."

        "Scattered around the hall are a number of bleary-eyed students, probably suffering from the same ailment as myself - noisy birds."

        "And, of course, there are the people that actually enjoy getting up this early, the ones with their bags stuffed with textbooks and completed homework."

        "It's hard not to despise people like that, even more so when you're tired yourself."

        "Picking out a familiar face from the thin crowd, I head towards the nearest table."

        "Lilly sits alone, delicately feeling her way around a small plate of eggs with her fork."

        "It's almost a shame to interrupt her and her clockwork movements."

        "I wonder, is this how a blind person zones out? Simply moving in pre-determined patterns learned over the years, just like how a sighted person would eat while reading a newspaper."

        hi "Good morning, Lilly. I didn't expect you to be here this early."

        show lilly basic_surprised:
            center
            ypos 1.2
        with charaenter

        li "Oh, Hisao, you startled me. I didn't know you took breakfast this early."

        hi "I don't. This is an exception to the rule. I'd greatly prefer to be late to school than early to breakfast."

        show lilly basic_weaksmile
        with charachange

        "Lilly gives a small sigh at my admitted tardiness as I begin eating my food."

        "It doesn't take long for her to lapse back into her previous mindless nibbling."

        "Each short motion lacks energy. I suppose this is similar to letting your eyes wander while performing any ordinary chore."

        "But after a few repetitions of the find food/eat food cycle, Lilly puts down her fork and dabs her lips with a napkin."

        stop music fadeout 6.0
        stop ambient fadeout 6.0

        show lilly basic_concerned
        with charachange

        li "Hisao, do you mind if I ask you a question?"

        "Damn. All I want is a little food and about four hours of sleep. And nobody says 'can I ask you a question' for a simple question."

        hi "Sure."

        show lilly basic_listen
        with charachange

        li "Do you think of Hanako as a friend?"

        "Huh, this seems like a leading question."

        hi "I… guess so. Why do you ask?"

        show lilly basic_weaksmile
        with charachange

        li "No real reason."

        show lilly basic_displeased
        with charachange

        play music music_serene fadein 8.0

        li "I do have another question though. Why is it that you think of her as a friend?"

        "This is well above my level. What is she expecting from me?"

        hi "I'm not really sure. I guess it's because she's a little different in the way she deals with people…"

        show lilly basic_reminisce
        with charachange

        li "Hmm. Since I've known her, she hasn't really connected with anyone."

        show lilly basic_concerned
        with charachange

        li "She doesn't seem interested in other people, and I think people are a little scared off by her appearance."

        hi "Really? I thought that kind of thing was, well, discouraged here. Discriminating and such."

        show lilly basic_listen
        with charachange

        li "Hmm, if I were to put it one way…"

        "She furrows her brow in thought, a move which makes me slightly anxious as to what she's plucking from her mind."

        show lilly basic_weaksmile
        with charachange

        li "I'd say that you're a little naive."

        "Naive? I'd be insulted if not for the slightly cynical grin on her face."

        hi "I… see."

        show lilly basic_reminisce
        with charachange

        li "While Yamaku has a stronger sense of community compared to other schools, it's far from being free of conflict."

        show lilly basic_displeased
        with charachange

        li "Rules cannot remove human nature, after all, only suppress it."

        "That's something I've noticed, actually."

        "Just little things, like how certain people and cliques avoid each other in the hallways. It's no different than my old school, really."

        "Even Lilly and Shizune could be considered bitter rivals, even though they both seem like fairly accepting people."

        "Well, at least the Misha-tinted Shizune does; who knows what actually goes on with her fingers and behind her glasses."

        hi "I guess you're right. But when I first came here, everything was a bit of a shock."

        hi "I kept on making mistakes, or at least thinking I was making mistakes. Like when we first met, and I said 'I see' to you."

        hi "I didn't know if that was considered rude or anything, so I tried to just put it in the back of my mind. Treating people any differently and that kinda thing."

        hi "So I didn't. I told myself that Hanako and you and everyone else was just normal, and I tried to ignore the obvious."

        hi "I talked to Hanako as if she were any other person, and so we became friends."

        hi "At least, that's how I think it happened."

        hi "But you know, I feel guilty just from saying something like that aloud. As if it took extra effort to think of Hanako, or you, or anyone here as normal people. I don't think that's right."

        show lilly basic_smileclosed
        with charachange

        li "Hisao, I think you are naive, but I also think that you are a good person. It is perhaps one of your better traits."

        hi "I… suppose… I can take that as a compliment…"

        show lilly basic_smile
        with charachange

        li "Tell me, are you free tonight?"

        hi "If you don't count homework, then I'm as free as the breeze."

        show lilly basic_cheerful
        with charachange

        li "In that case, would you care to join myself and Hanako for tea?"

        hi "Er, I don't really have that much money at the moment, so going out isn't really…"

        show lilly basic_smile
        with charachange

        li "Oh, I didn't mean going out. Just here, this evening."

        hi "You can access the classrooms in the evening here?"

        show lilly basic_giggle
        with charachange

        li "No, that's not what I meant. Hanako and I often use my room for tea parties together. Please feel free to drop by after dusk."

        hi "Sure, I see no problem with that. What's your room number?"

        show lilly basic_smileclosed
        with charachange

        li "225; Room 25 on the second floor."

        hi "Okay, sure."

        show lilly basic_weaksmile
        with charachange

        li "Well then, I had best be off. I have class representative duties to attend to, after all."

        show lilly basic_cheerful at center
        with charamovechangefaster

        li "Until this evening, Hisao."

        hi "Yeah, catch you later."

        hide lilly
        with charaexit

        stop music fadeout 8.0

        "Hang on… was I just invited to a girl's room after hours? Is that even allowed?"

        "There is the curfew here, but I've never heard any rules about visitors in the dorm rooms."

        "Even still, this is enough to get my sleep-deprived brain jump-started."

        "Add that to a lukewarm breakfast and you have one hell of a pick-me-up."

        scene bg school_scienceroom
        with locationskip

        "I grudgingly go to class, still a little excited at the prospect of breaking the rules."

        "I feel a little like a kid planning to sneak out of his window at night."

        "Well, maybe that's going a little too far, but when you compare an invitation to a party to six or so hours of lectures, I know which one wins."

        "Misha and Shizune do little to relieve my boredom either. For once, they seem determined to actually complete Mutou's assignments."

        scene bg school_scienceroom_ss
        with shorttimeskip

        play sound sfx_normalbell

        "Nevertheless, the day eventually winds to a close."

        scene bg school_dormhisao_ss
        with locationskip

        "I hurry back to my room to wash up and comb my hair. Thankfully I don't run into Kenji."

        scene bg school_dormext_full_ss
        with locationchange

        "Before long I am leaving the boys' dorm."

        if _in_replay:
            return

    label .mad_hatter:
        scene bg school_girlsdormhall
        with locationskip

        play sound sfx_doorknock2

        "I nervously rap on the door marked 225, checking my watch once again."

        li "Is that you, Hisao? The door is open, you can come in."

        "Lilly's voice lilts through the door and soothes my nerves."

        "This is the first time I've been invited to a girl's room after dark."

        "Even though I know there is no ulterior motive behind this invitation, it doesn't stop my mind running wild with possibilities."

        "One guy. Two girls. In a dorm room. With a tea set."

        "When I put it like that, it sounds a little dodgy."

        "Giving a small sigh to steady myself, I gingerly put my hand on the handle and open the door, craning my head to see inside."

        play sound sfx_dooropen

        scene white
        with dissolve

        pause 0.1

        play music music_one fadein 10.0

        scene ev lilly_bedroom:
            truecenter
            zoom 1.1
            ease 15.0 zoom 1.0
        with Dissolve(4.0)

        "The door opens completely and I catch my first glimpse of Lilly's room."

        "Her furniture looks almost antique, but the bare walls and flat surfaces are barely decorated at all. In the center of the room sits a low table, where I see a small tea set at rest."

        "It seems that everything in this room has its place, possibly excepting the several piles of books stacked up against the wall."

        "My sense of vision isn't the only one to be stimulated; the faint smell of something can be picked up on the air. Nail polish, perfume, makeup… it's hard to describe in any way other than 'girly'."

        "My eyes finish their quick sweep of the room, before returning their position onto the girls."

        scene ev lilly_bedroom_large:
            xpos -312 ypos -840
            warp acdc_warp 5.0 ypos -1680
        with flash

        "Lilly sits next to the small table, wearing very dark blue pajamas. Dark blue pajamas with shorts that show off plenty of her alluring pale legs."

        show ev lilly_bedroom_large:
            ease 1.0 xpos -1900 ypos -580
            warp acdc_warp 12.0 ypos -110

        "Opposite her, Hanako sits adorned in a conservative light pink gown."

        "Her hands are firmly fixed between her legs, her shoulders forward, and her head down, as if trying to hide herself in it."

        "It would be easy for her to do; it looks about two sizes too big for her."

        "Waves of flannel flow from her frame, making her look like a child playing dress-up in her parents' clothes."

        "She looks up to confirm my identity, and the beginnings of a thin smile creep across her face, before vanishing so fast that I can't be sure they ever were there."

        show ev lilly_bedroom_large:
            ease 1.0 xpos -312 ypos -1040

        li "There's no point in you standing in the doorway, Hisao."

        scene bg school_dormlilly
        show lilly basic_smile_paj:
            twoleft
            ypos 1.2
        show hanagown distant:
            tworight
            ypos 1.17
        with locationchange

        play sound sfx_doorclose
        stop music fadeout 10.0

        "I take a step into the room, closing the door behind me."

        show lilly basic_weaksmile_paj
        with charachange

        li "My my, I'm afraid this really is a small room for the three of us. Would you like to take a seat?"

        "I slowly walk to the table and sit down, trying my hardest not to disturb anything along the way."

        "I also can't help but steal a quick glance into Lilly's top as I sit."

        "To be robbed of sight would be a most terrible fate."

        show lilly basic_smileclosed_paj
        with charachange

        li "Well now, how about some tea. Hanako, could you please pour?"

        show hanagown normal_blush
        with charachange

        ha "S… sure. Hi… sao… would…"

        show hanagown distant_blush
        with charachange

        ha "…would you…"

        show hanagown worry_blush
        with charachange

        ha "…would you like…"

        hi "I would love some tea. Do you need a hand?"

        show hanagown normal_blush
        with charachange

        ha "N… no, I'm fine…"

        show hanagown smile
        with charachange

        ha "Thank you…"

        play music music_dreamy fadein 2.0

        show lilly basic_giggle_paj
        with charachange

        "Lilly finds it difficult to resist a smile at her companion's nervousness, something I can't really blame her for."

        show hanagown distant
        with charachange

        hi "Been a tiring day?"

        show hanagown smile
        with charachange

        ha "Y… yeah."

        show lilly basic_smileclosed_paj
        with charachange

        "I relax at my place, opposite of the cabinet."

        "To my left is the blue-clad Lilly and to my right sits the pink Hanako."

        show teaset:
            center
            ypos 0.6
            easein 0.5 center
        with charaenter

        show teaset at center

        "The tea set on the table looks cute as well as practical; painted red with a floral motif."

        "It looks odd when contrasted with Lilly's plain but generally sophisticated-looking furniture, which leads me to think that Hanako might have picked it out."

        "There is a slight 'ting' when Hanako accidentally clips the teapot on a cup as she is pouring."

        show hanagown worry
        show lilly basic_displeased_paj

        show teaset:
            easeout 0.5 ypos 0.6 alpha 0.0

        pause 0.5

        hide teaset

        "She breathes in sharply; she must be really nervous, as it's not the kind of thing anyone would worry about."

        show hanagown worry_blush
        with charachange

        "Hanako quivers at her mistake."

        show lilly basic_weaksmile_paj
        with charachange

        li "It's okay, Hanako. There's no need to be nervous."

        show hanagown normal
        with charachange

        "Hanako seems to find some confidence in Lilly's reassuringly soft-spoken words and deftly pours the next two cups."

        show hanagown normal_blush
        with charachange

        ha "Here you are, Hisao… Lilly."

        "Hanako carefully places a cup and saucer in front of Lilly and myself. I could get used to service like this."

        show lilly basic_smile_paj
        with charachange

        li "Thank you, Hanako."

        hi "Yeah, thanks."

        show hanagown smile
        with charachange

        ha "Y-you're welcome."

        show lilly basic_smileclosed_paj
        with charachange

        "Lilly searches for her cup, and upon finding it, sips delicately."

        "I do the same. This tea tastes somewhat better than the tea we usually have at school."

        hi "This is nice, it's so different from any tea I had before…"

        show lilly basic_ara_paj
        show hanagown normal_blush
        with charachange

        li "Looks like you picked the right one, Hanako."

        show lilly basic_smileclosed_paj
        with charachange

        li "You've done well, even if it was a bold move."

        show hanagown smile
        with charachange

        "Hanako's smile returns, redoubled."

        "Even with her blighted face, her shy smile couldn't be called anything but 'cute'."

        show hanagown distant_blush
        with charachange

        ha "I'm glad you like it…"

        "Hanako, finally beginning to relax, sips from her cup."

        if ask_hanako or _in_replay:
            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "I think back to my chat with Misha the other day."

            n "Is Hanako's behavior something to be concerned about, or is she just shy?"

            n "And then there was Lilly earlier this morning."

            n "The concern from both of them seemed to be genuine, and they know the situation better than I."

            n "But, really, how could I possibly help?"

            n "I'm no plastic surgeon, so I can't really help her appearance. Nor am I a psychologist who can make her more sociable."

            n "So what the hell do Lilly and Misha want me to do?"

            n "It's frustrating. Hanako and I are quickly becoming friends on our own accord, and because of that, it's like everyone wants me to solve all her problems."

            n "And I have no idea how to do that."

            n "No one can cure my heart, nor Lilly's eyes, nor anyone who is here, in this school."

            n "However, I see no harm in becoming better friends with Hanako. Now that she's warming up to me I kind of enjoy hanging out with her."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")
            nvl clear
            nvl hide dissolve
        else:
            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=120}Something about this makes me think about Lilly's question at breakfast."

            n "Why am I friends with Hanako?"

            n "Lilly seems genuinely concerned for Hanako's well being, but it's not like I can do anything to help her."

            n "As far as I can tell, her scars don't hold her back physically, and everyone I've met seems to have overcome their disabilities to some extent."

            n "I don't have any ulterior motives to hang out with Hanako, we just share similar interests."

            n "{vspace=30}Isn't that enough?"

            $ renpy.music.set_volume(1.0, 1.0, channel="music")
            nvl clear
            nvl hide dissolve

        show lilly basic_smile_paj
        with charachange

        li "So, Hisao, are you enjoying yourself?"

        "Lilly's words break me out of my reverie, and I take a second to reconsider where I am."

        "I'm in a room with two girls in their bedclothes. This is something to be enjoyed."

        hi "Yeah, it's relaxing. Almost like I'm not in the school any more. Do you do this often?"

        show lilly basic_weaksmile_paj
        with charachange

        li "Quite often, but not as often as we take tea in the school building."

        "Considering they do that nearly every day, that's not a big surprise."

        "As I move to take another sip from my teacup, I find it sadly empty."

        hi "That was delicious. Thank you Hanako, Lilly."

        show hanagown smile
        with charachange

        ha "You're welcome."

        show lilly basic_smile_paj
        with charachange

        li "Yes, you're most welcome Hisao. It's nice to have a third person here."

        hi "Well, any time you need someone to fill that position, I'm always available. Always."

        "One must be sure to get one's point across in these circumstances."

        stop music fadeout 8.0
        show lilly basic_sleepy_paj
        with charachange

        "Lilly lets loose a yawn, which she unsuccessfully hides with her hand."

        show lilly basic_weaksmile_paj
        with charachange

        li "Pardon me, I think I'm a little tired."

        show hanagown distant
        with charachange

        ha "I think we're all a little tired…"

        show lilly basic_ara_paj
        with charachange

        li "My my, how astute we are tonight, Hanako."

        show lilly basic_weaksmile_paj
        with charachange

        li "We really should head to bed; we all have class tomorrow."

        hi "Yeah… I should go."

        show lilly basic_smile_paj
        with charachange

        li "Thank you for your presence, Hisao."

        show hanagown normal
        with charachange

        ha "Th… thanks. You'll come again?"

        hi "Not even a whole army could stop me."

        show lilly basic_cheerful_paj
        with charachange

        li "I'm impressed by your determination, Hisao."

        hi "Either way, you're right. We'd best get going."

        "I stand up, and make for the door."

        show hanagown at tworight
        with charamovefaster

        "Hanako gingerly stands up behind me."

        "I stop and face her."

        hi "Are you coming with me?"

        play music music_comedy fadein 0.5

        show hanagown normal_blush
        with charachange

        "Hanako instantly blossoms into full blush."

        show hanagown distant_blush
        with charachange

        ha "No… I… not… this room… isn't…"

        hi "It's okay, I was only joking."

        show hanagown smile
        with charachange

        ha "Oh… okay… good night…"

        show lilly basic_smileclosed_paj
        with charachange

        li "Good night, Hanako. Good night, Hisao."

        hi "Night all."

        "And with that, our tea party finishes."

        scene bg school_girlsdormhall
        with locationchange

        "I'm still not sure what it is that Lilly wants me to do for Hanako, but I don't want to let her down."

        "I wait until the door has closed behind us before turning to Hanako."

        show hanagown distant_blush at center
        with charaenter

        hi "Hey, Hanako, you know, you don't have to be nervous around me or anything."

        hi "I mean, we're friends, right?"

        show hanagown normal_blush
        with charachange

        ha "R-right. We're… friends."

        hi "If you ever want to hang out or anything, just let me know. We still need to have that chess rematch, remember?"

        show hanagown distant
        with charachange

        ha "S-sure…"

        show hanagown normal
        with charaenter

        ha "B-but I don't think you'll win…"

        hi "It wouldn't be any fun if it was easy."

        show hanagown smile
        with charachange

        "Hanako seems to give a muted laugh, but she could have just as easily been exhaling."

        ha "G-good night Hisao…"

        show hanagown:
            easeout 0.5 xpos 0.7 alpha 0.0

        pause 0.5

        hide hanako

        stop music fadeout 5.0

        "With that, Hanako quickly retreats into her room, located next to Lilly's."

        "I start to walk back to my dorm, but the simple act of walking seems to drain me of my energy."

        scene bg school_dormhisao
        with locationskip

        "I barely make it to my room before I am hit by a wave of exhaustion."

        play sound sfx_switch

        scene bg school_dormhisao_ni
        with Dissolve(0.2)

        "I kick off my shoes, fall into bed and fall asleep by the time my head hits the pillow."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .small_change:
        scene bg school_dormhallway
        with locationchange

        "I pull my door closed, ready for another day of classes."

        show kenji neutral_close:
            twoleft alpha 0.0
            easein 0.5 center alpha 1.0

        pause 0.5

        show kenji at center

        ke "Sleep well?"

        play music music_kenji fadein 0.5

        "Kenji's sudden arrival makes me jump, and I narrowly avoid butting heads with him."

        "I know he has poor eyesight, but he knows who I am now. Does he still have to stand this close?"

        show kenji neutral
        with charadistant

        hi "Oh. Yeah. Like a baby."

        show kenji tsun
        with charachange

        ke "Damn, why do people say that? Have you ever heard a baby sleep?"

        ke "They scream. All night. Every night. Babies don't sleep well, ever."

        "Well, there goes my restful state. I have to remember to never use figures of speech with Kenji."

        hi "All right, I get your point. It was a figure of speech."

        show kenji neutral
        with charachange

        ke "Yeah, sure, whatever. Where were you last night? I had a favor to ask but you weren't around."

        "For a split second I consider telling Kenji the truth; that I was spending time with Hanako and Lilly."

        "Thankfully, that split second passes as soon as it came."

        hi "I was just out. Checking out the local area and stuff. You know, recon."

        show kenji happy
        with charachange

        ke "Good man, good. I knew you were the type to plan ahead…"

        hi "Anyway, what was this favor you wanted?"

        show kenji neutral
        with charachange

        ke "I was going to get some take-out, but I needed change."

        hi "Wait, what? I gave you money last week and you still haven't paid me back!"

        show kenji tsun
        with charachange

        ke "Tch, and I was starting to think you were cool."

        "Kenji fishes around in his pocket and produces his wallet."

        "As he counts out the 400 yen he owes me, I can clearly see at least two 10,000 yen notes."

        hi "Hey, what the hell? Why are you borrowing money off me when you've got that much cash?"

        "Kenji hisses a little, realizing that he's been had."

        ke "Get off my case, man. It's bad luck to break a big note for anything less than half its value. It's the tycoon's rule."

        ke "Last night's dinner is going to cost me seven years of bad luck. Seven years!"

        show kenji happy
        with charachange

        ke "Don't you think that's enough cause to help someone out? I'd get a shorter sentence if I just stole the stuff."

        "My common sense screams at me to say something to him, but thankfully I restrain myself."

        "Arguing a point like this with Kenji will just lead to further and more complicated discussions."

        hi "Yeah, I guess you're right. Maybe you should plan these things a little better?"

        show kenji neutral
        with charachange

        ke "Yeah man, I know. But I've just got so much stuff to do, it's hard. And you're never around any more so I'm on my own."

        ke "We're supposed to be brothers in brotherhood, remember?"

        hi "Yeah yeah, I get you. Global conspiracy and such. I'll keep my ear to the ground."

        show kenji neutral_close
        with charachange

        "Kenji draws close enough for me to get a clear whiff of his garlic-tainted breath."

        show kenji tsun_close
        with charachange

        ke "You'd better, man. You're already spending less time here. That's the first thing they do."

        ke "They'll try to split us up. Divide and conquer. Sun Tzu said that."

        hi "Roger that. Now, I've got to be going. I've got classes. You coming?"

        show kenji neutral_close
        with charachange

        ke "Nah, I'm tired. I stayed up all night just to make sure nothing was going to happen after splitting that note."

        hi "As rational as ever, I see."

        show kenji tsun_close
        with charachange

        ke "Whatever. Night."

        stop music fadeout 3.0

        show kenji:
            easeout 0.5 twoleft alpha 0.0

        pause 0.5

        hide kenji

        "Kenji scurries back into his room, and I hear him throwing his locks as I walk down the hallway."

        if _in_replay:
            return

    label .absenteeism:
        scene bg school_dormhallway

        scene bg school_scienceroom
        show muto smile at center
        with shorttimeskip

        play music music_daily fadein 4.0

        mu "…that is why some people can't roll their tongue, or why their second toe is longer than their big toe."

        "Mutou beams a half-moon smile at us, obviously proud of his explanation of recessive genes."

        "However, no matter how impressed he is at the science that defines who we are, the classroom seems to be reduced to a stupor."

        "Why is it that a bad explanation can make even the most interesting thing seem worthless?"

        show muto irritated
        with charachange

        "I can see Mutou deflate as he realizes that nothing he's said in the past half hour has sunk in."

        $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
        play ambient sfx_crowd_indoors fadein 4.0

        "Whispered conversations start to break the silence, and like an avalanche, the noise level in the class starts to rise."

        show muto normal
        with charachange

        "Defeated, Mutou identifies some questions from the text book and sets to clearing off the blackboard."

        hide muto
        with charaexit

        "Almost as if expected, Hanako packs up her things and leaves as soon as people start talking and laughing among themselves."

        "The initial shock of seeing someone play so blatantly truant has started to fade, but it doesn't stop me from wondering."

        "Is she leaving because she doesn't want people to speak to her? Or is it just the thought of people around her shattering her peace?"

        play sound sfx_normalbell
        $ renpy.music.set_volume(1.0, 4.0, channel="ambient")

        "Before I can think about the topic any further, the lunch bells ring. I wonder if she was simply taking the opportunity to leave early."

        "The usual clamor of students exchanging books for lunch reverberates around the room, and while Misha is distracted, I grab my lunch and head out the door."

        stop ambient fadeout 1.0

        scene bg school_miyagi
        show lilly basic_smileclosed:
            center
            ypos 1.2
        with locationskip

        "Lilly already sits in the tea room, setting out her lunch alone."

        hi "So, Hanako's not here then?"

        show lilly basic_smile
        with charachange

        li "Oh, Hisao, how are you? I haven't met Hanako since this morning, I'm afraid."

        "That's right, Hanako and Lilly live next to each other."

        "Somehow I think their morning conversations are slightly more grounded than Kenji's ramblings."

        hi "That's strange. She left class early, so I figured that she'd come here."

        show lilly basic_displeased
        with charachange

        li "So she's still leaving class early…"

        hi "Huh? Yeah, I've seen her do it a few times."

        show lilly basic_sad
        with charachange

        stop music fadeout 7.0

        "Lilly drops her head a little, and her tone of voice is notably depressed. It's very reminiscent of someone who is used to hearing bad news."

        li "I was so sure that she'd stop doing that once you two became friends."

        show lilly basic_weaksmile
        with charachange

        li "Everyone has their own pace, I suppose."

        hi "Well, I was wondering about just that today. Why exactly does she leave?"

        show lilly basic_reminisce
        with charachange

        li "I'm not entirely sure myself. I personally think it's because she doesn't want to be put in a situation where she has to answer someone."

        "I have a flashback of my first meeting with her, when I thought she looked like a cornered animal. Maybe I wasn't far from the truth."

        hi "But she seems fine with talking to you, and with me… a bit…"

        show lilly basic_displeased
        with charachange

        li "It's a little more complex than that. I imagine that the first thing most people ask her about is her scars, and what happened."

        li "She rarely talks about it with me, but I can tell that she doesn't like to remember whatever happened back then."

        show lilly basic_reminisce
        with charachange

        li "Leaving class and running away from discussions is her preemptive strike, if you will."

        hi "Huh… so then how does that explain her talking to me?"

        show lilly basic_weaksmile
        with charachange

        li "You said it yourself yesterday at breakfast; you tried to ignore her scars. Once she saw that you weren't going to ask her about that, she opened herself up to you."

        hi "Hrm, I guess you're right. Maybe. I dunno. You know her better than I, so I'll take your word for it."

        play music music_normal fadein 3.0

        show lilly basic_giggle
        with charachange

        li "I wouldn't worry about that. I'm sure you'll come to know her as well as I do soon enough."

        show lilly basic_smileclosed
        with charachange

        li "I welcome the prospect of her having a new friend, and the two of you have such similar interests…"

        hi "Well, I hardly count reading as a team sport. It is good to have company, though."

        show lilly basic_smile
        with charachange

        li "That's my point. Hanako is still an average person at heart. She also wants company at times like that."

        hi "Huh, I see. I think. To be honest, both of you still confuse me a little."

        show lilly basic_smileclosed
        with charachange

        li "That's only natural, Hisao. We've only known each other for a little while; it's unreasonable to expect you to understand us, just as we can't understand you."

        show lilly basic_weaksmile
        with charachange

        li "But that is half the fun of becoming friends, right?"

        hi "Yes, yes it is."

        show lilly basic_giggle
        with charachange

        li "Although… I suppose there is the matter of us being opposite genders. Men and women do seem to confuse each other quite often."

        "She says this with a light giggle, finding amusement at the odd little details of life."

        show lilly basic_cheerful
        with charachange

        li "I hope you don't mind, but I'm going to start eating."

        hi "No, go ahead, I think I'll eat something too. I've got some books I want to drop back at the library before classes start, so I'd better get a move on."

        show lilly basic_smileclosed
        with charachange

        li "You'll probably find Hanako there as well. If you do see her, can you tell her to stop by my room later tonight? I'd like to talk to her."

        hi "You're not coming?"

        show lilly basic_weaksmile
        with charachange

        li "Unfortunately I have a class representatives' meeting later, so I'll be gone as soon as I've finished my lunch."

        hi "Okay then, if I don't see her in the library then I'll tell her in class. I'm sure she'll be back after lunch."

        "We fall silent as we start to eat, and I take a second to reflect on our conversation."

        "I've always thought that Hanako's shyness was simply due to her being self-conscious of her scars."

        "But that is a pretty superficial way of looking at her."

        "Just when I thought I was able to see through the fog of Lilly and Hanako, I realize that I'm more lost than when I started."

        "Lilly quickly finishes her lunch, acutely aware of her meeting. I don't blame her."

        "Shizune is most likely going to be there, and I doubt she wants to give her the satisfaction of another argument."

        show lilly basic_smile
        with charachange

        li "I must be off. Same time tomorrow?"

        hi "Same time, same channel. I'd better head off too; I don't want to risk being late."

        show lilly cane_smileclosed
        with charachange

        show lilly at center
        with charamove

        stop music fadeout 4.0

        "Lilly smiles gently, picks up her cane and walks out into the hall."

        if _in_replay:
            return

    label .equivalent_exchange:
        scene bg school_hallway2
        with locationchange

        "I turn my back on Lilly as we head in opposite directions. For some reason I find myself hoping she doesn't get into another fight with Shizune."

        "As much as I like Lilly, Shizune and Misha have been pretty instrumental in helping me adjust, even if half of our conversations are thinly-veiled recruitment attempts."

        "Then again, I barely know either of them. Maybe they were previously leaders of some kind of secret society, but their love for each other drove them apart…"

        "Man, I need to stop reading cheap fiction. It's rotting my brain. Either that or I've got to move away from Kenji and his bad influence."

        "It's sad that I can't tell the two apart any more."

        scene bg school_library at right
        with locationskip

        play music music_happiness fadein 2.0

        "I slide my books down the return chute and they crash into the cart with a pleasant thud."

        play sound sfx_impact2

        show yuuko panic_up at center
        with vpunch

        "Yuuko, however, doesn't seem as impressed as I."

        yu "H-Hisao! You scared me!"

        hi "Sorry, I thought you would be used to that by now. Or is the literacy level here so low that nobody borrows any books?"

        show yuuko worried_up
        with charachange

        yu "Huh? No I think everyone here can read fine…"

        hi "Yeah… never mind."

        "There are some battles that you can never win. Trying to explain jokes is one of them. My Dad taught me that the hard way."

        hi "Say, Yuuko, have you seen Hanako about? She left class early but she wasn't in her usual hiding place."

        show yuuko closedhappy_down
        with charachange

        yu "I think I saw her sneak in before lunch…"

        show yuuko panic_up
        with charachange

        yu "Oh! But I'm not supposed to tell anyone that!"

        hi "I just told you that I saw her leave, no need to stress out…"

        show yuuko smile_down
        with charachange

        yu "Oh… of course. She's probably in the back."

        hi "Thanks. Get any new books in recently?"

        show yuuko worried_up
        with charachange

        yu "No, sorry. I'll let you know when we do, though."

        hi "Okay."

        "If there's one thing I know about librarians, part-time or otherwise, it's that they appreciate people who take a genuine interest in their work."

        hide yuuko
        with charaexit

        show bg:
            warp acdc_warp 10.0 left

        "I walk the now-familiar path to Hanako's reading nook, picking out a few titles along the way."

        "Sometimes I find it hard to discover a book that will interest me among the shelves. An author's name and a two-word title don't mean much in a sea of similar words."

        "For that reason, I sometimes re-read books that I read in the past. Better to bet on the favorite than a new runner."

        "An unfamiliar title from a familiar author peeks out among the spines of its neighbors, so I remove it from the shelf."

        "At least I'm not going over old material."

        scene ev hana_library_read_std
        with locationskip

        "As expected, Hanako sits on her beanbag, buried deep in a copy of 'Dance Dance Dance.'"

        hi "Hi Hanako. How's it going?"

        "I fight back the urge to ask why she left class early. If Lilly's suspicions were right, then asking her about that could have the opposite effect."

        "Best to leave it for the time being. Sometimes the best way to get an answer from someone is to never ask the question."

        show ev hana_library_smile_std
        with charachangeev

        ha "Hello, H-Hisao. I'm fine."

        "Something seems off, and after a couple of seconds, I realize what it is. Hanako's smiling."

        "She looks as if she's pleased to see me. It's a nice change from the usual, instinctively frightened reaction, and something I hope I can see more of as we get to know each other better."

        hi "Good to hear. How's that book? I've heard it's a trip."

        ha "I-it's good… I think."

        ha "I've only j-just started it, so I d-don't really know."

        hi "Fair enough. Let me know how it goes; I may borrow it once you're done."

        ha "S-sure."

        "There's a good fifteen minutes left in lunch. Not enough to really get into a book, but too much to stand around doing nothing."

        show ev hana_library_read_std
        with charachangeev

        "And Hanako's already returned to her reading, so I doubt I'll get much conversation from her."

        "Oh well, I'd better make myself comfortable."

        play sound sfx_pillow

        "I slouch into a beanbag and crack open my book."

        "The familiar style of the author leaps out at me from the very first line. As the sentences turn into paragraphs, I start to relax a little."

        stop music fadeout 8.0

        "But no matter how I try, I can't seem to get myself into the atmosphere of the book."

        "This is partly due to the lack of time, but the more distracting factor is Hanako."

        show ev hana_library_std
        with charachangeev

        show ev hana_library_read_std
        with charachangeev

        "Every ten or so seconds she peers over the top of her book, but when our eyes meet she quickly ducks behind the covers."

        "I guess she did want to talk about something after all."

        scene bg school_library
        with locationskip

        hi "What's up? You look like a prairie dog on lookout."

        show hanako emb_blushing:
            center
            ypos 1.17
        with charaenter

        ha "N-… it's nothing."

        hi "I've told you before, 'nothing' means 'something' when you say it like that."

        show hanako cover_worry
        with charachange

        "Hanako squirms a little in her beanbag, hoping that by changing her position she'll find the words she's looking for."

        show hanako emb_downsad
        with charachange

        ha "I… I was in an accident."

        hi "Accident? Just now? Are you all right?"

        show hanako emb_sad
        with charachange

        "Hanako shakes her head, her hair flowing around her shoulders in wisps of amethyst on a background of pale and dark flesh."

        show hanako emb_downsad
        with charachange

        ha "N-no. When I was y-younger."

        play music music_hanako

        "Realization crashes into me like a semi."

        ha "When I… when I was…"

        hi "It's all right Hanako, you don't have to tell me anything if you don't want to…"

        "Again she shakes her head."

        show hanako emb_sad
        with charachange

        ha "N-no. I want… I have to tell you."

        scene ev hanako_crayon1:
            truecenter
            linear 20.0 zoom 1.05
        with locationskip

        ha "When I was young… I was in a fire."

        ha "M-my house b-burned down, and I nearly… I nearly didn't make it."

        show ev hanako_crayon2:
            linear 8.0 zoom 1.05
        with charachangeev

        ha "A-after that… I was alone…"

        scene bg school_library
        show hanako emb_downsad_close:
            center
            ypos 1.1
        with locationskip

        "Hanako's eyes glisten in the dim light of the library, and I reach out to grasp her hand."

        hi "It's okay, Hanako. You don't have to keep going."

        show hanako emb_sad_close
        with charachange

        ha "B-but… I have to…"

        hi "Why? What brought this on?"

        show hanako cover_distant_close
        with charachange

        ha "L-Last night Lilly t-told me about your heart…"

        show hanako cover_worry_close
        with charachange

        ha "A-and I… I didn't think it was f-fair."

        hi "Fair?"

        show hanako emb_blushing_close
        with charachange

        ha "T-that I knew about you b-but you didn't know about me…"

        "I squeeze Hanako's hand a little."

        hi "Don't be silly. But yes, I have a heart condition."

        "I lean a little closer to Hanako."

        hi "What I didn't tell Lilly is that I had my first attack when a girl confessed to me."

        "I smile a little to break the tension."

        show hanako cover_worry_close
        with charachange

        ha "R-really?"

        hi "Really. I haven't heard from her for a while though, so I guess it's all over."

        "I know it's all over. There's no other way to interpret what happened the last time I saw her. In some ways, not having heard from her again has helped me move on from that period of my life."

        hi "So now, we both know a little more about each other. But you don't have to talk about things if you don't want to."

        "In fact, I feel a little bad even thinking about that whole incident. I can almost smell the hospital's disinfectant burning the back of my sinuses again."

        "I imagine Hanako is going through the same thing now."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=60}When I was in the hospital I went to the burn ward once, and only once. I was bored, so I went for a walk through all of the wards."

        n "I went through oncology and thought I could take it, but when I got to the burn ward I turned around and went back to my bed."

        n "To think that Hanako would have spent months in a place like that, smelling nothing but corrupted skin, strong disinfectant and sterilized air."

        n "The really bad cases were kept in isolated pods that no foreign objects could enter. That would have meant no reading."

        n "{vspace=30}I would have gone insane if I didn't have my books in the hospital."

        n "And she said she was alone…"

        n "Did her parents die? I'll have to ask Lilly about it. I can imagine myself saying something dumb unintentionally."

        stop music fadeout 2.0

        nvl clear
        nvl hide dissolve

        show hanako emb_timid_close
        with charachange

        ha "T-thank you, Hisao."

        show hanako emb_downtimid_close
        with charachange

        ha "I… I haven't told many people about this."

        hi "To be honest, I haven't told many people about my… circumstances either."

        show hanako cover_smile_close
        with charachange

        ha "T-then I won't tell a-anyone either."

        hi "Deal."

        play sound sfx_warningbell

        "I change my grip on Hanako's hand into a handshake as the warning bells chime through the window."

        hi "Well then, we'd better head back to class then, eh?"

        show hanako basic_bashful_close
        with charachange

        ha "S-sure."
        $ renpy.music.set_volume(1.0, 0.0, channel="music")

        if _in_replay:
            return

    return
