# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a3_hanako:
    label .invitation:
        scene bg school_miyagi_ss
        show hanako basic_distant_close_ss at center
        with locationchange

        "The tint of the room slowly changes from the shine of the afternoon to the orange of dusk. A clock lazily ticks away the seconds, counting in the background, on the verge of hearing."

        "But no matter how long I wait, the outcome cannot be changed."

        "The diminutive playing piece makes a small click against the board."

        show hanako basic_normal_close_ss
        with charachange

        "Like a wound spring, Hanako makes her move only moments after mine."

        "It's embarrassing. In comparison to my five-minute moves, she seems to know exactly what she wants to do."

        show hanako basic_smile_close_ss
        with charachange

        play music music_tranquil fadein 3.0

        ha "Mate."

        hi "Again… What does that make this? 3-2?"

        show hanako cover_bashful_close_ss
        with charachange

        ha "S-stalemates don't count."

        hi "Damn. You're getting better at this every day."

        "That, or she's been holding back. I'd never have thought it when I first met her, but she really has a knack for this game."

        "Chess seems to have become a popular pastime for the two of us; hiding away in the tea room, playing a game or two after classes."

        "From here, the students outside can just barely be heard milling about. The everyday noises from below remind me a little of my life before Yamaku, though I'm by now well aware that it's a life I'll never get back to."

        hi "Fancy another game?"

        show hanako basic_worry_close_ss
        with charachange

        ha "I… I have to finish my homework…"

        hi "Oh. Well, I'll see you tomorrow then."

        show hanako basic_distant_close_ss
        with charachange

        ha "But… what about this…"

        "Hanako points to the tea set surrounding the mostly-empty chess board."

        hi "Don't worry about that, I've got it."

        show hanako basic_normal_close_ss
        with charachange

        ha "Oh… okay…"

        show hanako basic_bashful_close_ss
        with charachange

        ha "S-see you."

        hi "Later."

        hide hanako
        with charaexit

        "Hanako departs as I start cleaning up the area."

        "The occasional whistles and cheers from the sporting clubs outside become less frequent, eventually approaching silence."

        "A part of me still wants to be in some kind of team. Since I played soccer and other sports before my accident, I guess it's only normal to feel nostalgic about what I can't do any more."

        "But I have other reasons than that for my coming here so often, and I don't feel so bad about losing that part of myself because of them. Lilly is a good friend by now, but it's the small exchanges I have with Hanako that feel especially dear."

        "The small victories I feel every day as I see more of what she's like under her self-imposed shell. That's why I come here most of all."

        "As I'm putting away cups and saucers, I hear talking outside the door. Pausing for a moment to listen, I can make out that it's Hanako and Lilly, and decide to go outside to investigate."

        scene bg school_hallway2
        show lilly basic_weaksmile at twoleft
        show hanako emb_downtimid at tworight
        with locationchange

        li "Are you quite sure?"

        ha "I… I'm sure…"

        show hanako emb_timid
        with charachange

        ha "Ah, Hisao."

        "Hanako turns to see me with a look of mild surprise as she notices my approach. Lilly must've caught her just as she was about to leave."

        show lilly basic_smile
        with charachange

        li "Oh my, Hisao is here as well?"

        hi "'Afternoon, Lilly. What's up?"

        show lilly basic_smileclosed
        with charachange

        li "I was hoping, now that I've finished with my class representative duties for the day, that I might have the two of you accompany me for tea at the Shanghai. It would be nice to enjoy ourselves outside of the school, for a change."

        hi "I'd be up for it. I think Hanako had work to do, though…?"

        show hanako basic_smile
        with charachange

        ha "I-it's… not all that much…"

        show lilly behind_cheerful
        with charachange

        li "Wonderful. It seems that we're decided, then."

        stop music fadeout 2.0

        scene bg suburb_shanghaiint:
            xalign 1.0
            warp acdc_warp 3.0 xalign 0.0
        with shorttimeskip

        $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
        play ambient sfx_crowd_indoors fadein 2.0

        "I cast my eyes across the café as the three of us step in. As usual, there are only a handful of people around at most, and the noise level is a quiet background hum."

        scene bg suburb_shanghaiint at left
        show hanako emb_emb:
            xpos 0.4 xanchor 0.5
        show lilly cane_smileclosed at twoleft
        with charaenter

        play music music_dreamy fadein 6.0

        "The hold Lilly has on Hanako's arm remains just as it has been for the entire slow walk down the hill to the local town, though it's hard to say for which reason - for Lilly's guidance, or for Hanako's reassurance."

        show lilly basic_smile
        with charachange

        "For a moment, Lilly removes her arm from Hanako's to retract her cane as Yuuko quickly skitters over to where we stand, but soon replaces it right back where it had been."

        show yuukoshang closedhappy_up at tworight
        with charaenter

        yu "Welcome to the Shanghai! May I take your order?"

        show yuukoshang neutral_up:
            tworight
            ypos 1.25
        with charamovechangefastest

        show yuukoshang neutral_down at tworight
        with charamovechangefaster

        "She gives a deep bow, her well-delivered and professional introduction putting her in a good mood. It's a nice change from the norm for Yuuko."

        show lilly basic_smileclosed
        with charachange

        li "Just tea, please. Hanako, Hisao?"

        hi "I'll have a slice of pie and a coffee."

        show hanako basic_smile
        with charachange

        ha "Just… t-tea… please."

        show yuukoshang smile_up
        with charachange

        yu "Coming right up. Please take any seat you wish, and I'll be back shortly."

        hide yuukoshang
        with charaexit

        "Yuuko gives a smile and a nod before shuffling to the counter, and we make our way to some empty seats by the window in quick measure."

        hide hanako
        hide lilly
        with charaexit

        show bg at right
        with charamove

        show lilly basic_sleepy_close:
            twoleft
            easein 1.0 ypos 1.1
        show hanako basic_smile_close:
            tworight
            easein 1.0 ypos 1.09
        with charaenter

        "We slip into our seats, the girls on one side with Lilly's cane propped up beside them and I on the other. I realize that Hanako's not doing something that she so often does."

        show lilly:
            twoleft
            ypos 1.1
        show hanako:
            tworight
            ypos 1.09

        "Rather than keeping her eyes pinned to the ground and hiding behind her blind escort, busily trying to convince herself that the world around them doesn't exist, she's merely keeping her eyes low and helping Lilly around."

        hi "Are you you okay, Lilly? You look tired."

        show lilly basic_weaksmile_close
        with charachange

        "She lowers her head a little, looking somewhat embarrassed that she let it show."

        li "Class representative work can be very tiring, considering that it often means dealing with the Student Council."

        show lilly basic_sleepy_close
        with charachange

        li "Very tiring indeed."

        show hanako basic_normal_close
        with charachange

        ha "How… do the other representatives go?"

        show lilly basic_reminisce_close
        with charachange

        li "Better than I, but not by much. Shizune is a harsh taskmaster no matter whom she deals with."

        hi "It doesn't sound like you particularly relish the job. Why do you do it in the first place, if it's that bad?"

        show lilly basic_displeased_close
        with charachange

        li "Being a class representative is enjoyable, and I can deal with the responsibility well enough. It's just that the people involved are sometimes…"

        "She trails off, cutting her words at a rather opportune spot. It's hard to imagine Lilly cursing, but I imagine that if anyone could make her do so, it would be Shizune."

        show hanako cover_worry_close
        with charachange

        "Hanako looks to be withering a bit in the light of such conflict, but before I can steer the topic away a little, she stands up."

        show hanako basic_worry_close at tworight
        with charamovechangefaster

        show lilly basic_surprised_close
        with charachange

        li "Hanako?"

        show hanako defarms_strain_close
        with charachange

        ha "I'll… be back in a bit."

        hide hanako
        with charaexit

        "With that, she leaves for the restrooms. I suppose that's one way to deal with the situation, if that was indeed her motivation."

        show bg at center
        show lilly basic_concerned_close at center
        with charamovechangefaster

        "Lilly, however, looks a little wounded."

        hi "Don't worry about it. I don't think it was you."

        show lilly basic_oops_close
        with charachange

        li "But…"

        hi "I think she's been getting stronger recently. You've seen it yourself… right…?"

        "That went a bit awry. Fortunately Lilly doesn't look offended, and by now I really shouldn't be quite so scared of stepping on that landmine around her."

        show lilly basic_sleepy_close
        with charachange

        li "Possibly. Sometimes… I find it hard to tell, though."

        "Silence reigns for a moment before two teacups, a pie, and a mug of steaming coffee appear in front of us."

        show bg at right
        show lilly at twoleft
        with charamove

        show yuukoshang closedhappy_down at tworight
        with charaenter

        "I notice that Yuuko takes special care to place the teacup against the tip of Lilly's fingers, letting her know where it is."

        show yuukoshang closedhappy_up
        with charachange

        yu "Here you go."

        hi "Thanks, Yuuko."

        show lilly basic_weaksmile_close
        with charachange

        li "Thank you."

        hide yuukoshang
        with charaexit

        "With a quick and silent bow, the bespectacled waitress takes her leave."

        show bg at center
        show lilly at center
        with charamove

        li "Ah, that's right. I was meaning to ask you something, and now would be the right time to do so."

        hi "I'm all ears."

        show lilly basic_smileclosed_close
        with charachange

        li "Hanako's birthday is coming up, and I was hoping that you might accompany me for present shopping in the city this weekend."

        "Hanako's birthday is soon? I suppose it would be a nice chance to cheer her up a bit. Like Yuuko, she always seems to be teetering on the edge of either panic or depression, and I've never seen her enjoy herself much outside of our chess games."

        "All that aside, learning the layout of the city better with a friend keeping me company sounds like a good way to spend a weekend."

        hi "Sure, I'd be happy to. Have you got any plans for what to do for her birthday? A party or anything?"

        show lilly basic_weaksmile_close
        with charachange

        li "Hanako being Hanako, perhaps a low-key affair would be—"

        show lilly basic_listen_close
        with charachange

        "Lilly suddenly cuts herself short, leaving me to wonder why as she brings her teacup to her lips and begins to sip."

        "After a few seconds, I notice Hanako walking up to us over her shoulder. Lilly's hearing must be very good indeed if it was the sound of the restroom door opening that tipped her off."

        show bg at bgleft
        show lilly at twoleft
        with charamove

        show hanako basic_normal_close:
            tworight
            easein 1.0 ypos 1.09
        with charaenter

        "Hanako takes her seat once again, and wastes no time in drinking her tea. Soon the three of us are quietly eating and drinking as the sun sets."

        "It's a nice way to spend the remainder of the day's light, and it makes me appreciate the quiet and serene surroundings of Yamaku. I think I'm really beginning to like life here, as isolated as it may be."

        stop ambient fadeout 2.0

        scene bg suburb_shanghaiint at bgleft
        show lilly basic_smileclosed_close:
            twoleft
            ypos 1.1
        show hanako basic_smile_close:
            tworight
            ypos 1.09
        with shorttimeskip

        "I finish off the last of my coffee and rest the mug on the table while the girls talk between themselves. The coffee here's a little bitter for my tastes, but still quite good. Better than what I can make for myself, in any case."

        "The girls' discussion is mainly focused on their respective reading preferences, which does give me a little curiosity about a related topic."

        hi "Hey Hanako, I was just wondering… aside from chess and reading, do you have any hobbies or things you like doing?"

        show hanako emb_timid_close
        with charachange

        "She's completely stopped in her tracks, looking quite surprised that anyone would be interested in asking such a question about her. It takes her a little time to formulate a response."

        show hanako emb_downsmile_close
        with charachange

        ha "Um… I guess… I like singing a l-little. I'm okay with c-computers as well, but I… don't use them all that much."

        "Singing's not exactly something I expected to hear. It's hard to imagine her singing voice, given how soft-spoken she is."

        show lilly basic_smile_close
        with charachange

        "Lilly, on the other hand, simply nods. She must already know all this, since she's been friends with Hanako for one year or so by now."

        show hanako cover_bashful_close
        with charachange

        ha "W-what about… y-y…"

        hi "Me?"

        show hanako basic_bashful_close
        with charachange

        "She hesitates before quickly flicking her head up and down. It's only logical that she'd want me to talk about my hobbies after she's told me hers."

        hi "There's chess, obviously, but also… hmm…"

        hi "There was soccer as well, though I can't really do that any more. Reading, which I picked up in hospital… um…"

        show hanako basic_normal_close
        show lilly basic_sleepy_close
        with charachange

        "This is surprisingly hard. Lilly and Hanako look a little put off by the direction this is taking, and the more I think about it, the more I am too."

        show lilly basic_weaksmile_close
        with charachange

        li "It sounds as if you've picked up quite a few things since your accident."

        "Lilly's candor is coated with probably the most positive spin one could put on what I said. Hanako, however, is silent."

        "If a situation becomes difficult, her reaction always seems to be withdrawing into silence, in order to prevent things getting worse. That, or physically retreating."

        $ renpy.music.set_volume(0.2, 0.0, channel="sound")
        play sound sfx_phone

        show lilly basic_surprised_close
        show hanako cover_worry_close
        with charachange

        "A soft ringing gives us pause. As Lilly reaches into her pocket, it becomes obvious that the sound's coming from her phone."

        show lilly basic_weaksmile_close
        with charachange

        li "Sorry…"

        show hanako basic_normal_close
        with charachange

        ha "I-it's okay…"

        show lilly:
            ease 1.0 ypos 1.0 alpha 0.0
        with Pause(1.0)

        hide lilly

        "Lilly gives a quick nod before shuffling out of her seat and taking the call a little distance away, to avoid disturbing the both of us."

        hi "Must be nice to be popular."

        show hanako cover_bashful_close
        with charachange

        "Hanako smiles, but doesn't take up the hook for further discussion."

        $ renpy.music.set_volume(0.5, 2.0, channel="music")

        scene black
        with shuteye

        "I end up just sitting back and closing my eyes, relaxing as best I can."

        hi "It's nice and peaceful here. I wonder what it'd be like to have grown up somewhere like this, rather than in the city."

        ha "Y-you come from the city?"

        "Looks like I've found something she wants to talk about."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")

        scene bg suburb_shanghaiint at center
        show hanako basic_smile_close:
            center
            ypos 1.09
        with openeye

        hi "Yeah. You could say I was a city kid through and through."

        show hanako basic_worry_close
        with charachange

        ha "I-it sounds like a lot changed…"

        hi "It did. I'm still not quite sure what to make of it all, though. It's a bit of a culture shock, in more ways than one."

        hi "You must've gone through something like this when you first arrived at Yamaku, right? I'd imagine most new students would."

        show hanako basic_distant_close
        with charachange

        ha "N-not really…"

        "Hanako gazes a little to the side, looking unwilling to go on. I tilt my head inquisitively, but a couple of seconds pass with no further answer."

        show bg at bgright
        show hanako:
            tworight
            ypos 1.09
        with charamove

        show lilly back_pout at twoleft
        with charaenter

        stop music fadeout 8.0

        li "But can't we deal with that on Monday? The fallout has hardly settled from the last…"

        show lilly back_listen
        with charachange

        li "I understand. I'll try to talk her down. You know what she's like when she gets locked onto an idea."

        li "Yes, thank you. I'll talk to you later, then. Goodbye."

        show lilly basic_displeased
        with charachange

        "Lilly's conversation ends with the snap of her phone closing. She returns to our table, but doesn't take her seat."

        hi "Need to go?"

        show lilly basic_concerned
        with charachange

        li "Unfortunately. Class representative work calls once again."

        show hanako cover_worry_close
        with charachange

        ha "I-I can come with you."

        show lilly basic_weaksmile
        with charachange

        li "It's all right, Hanako. I'll just be going straight to the Student Council. There's no need to spoil a fine evening on my account."

        show lilly basic_smile
        with charachange

        li "Besides, if you were to accompany me on my way back to the school, who would keep our poor Hisao company?"

        show hanako basic_normal_close
        with charachange

        ha "Okay…"

        show lilly basic_weaksmile
        with charachange

        li "I can join you for tea again later tonight, if you'd like. I may well need it."

        show lilly cane_weaksmile
        with charachange

        "We agree on that plan, and Lilly says her farewells to the both of us, taking her cane after Hanako passes it to her."

        hide lilly
        with charaexit

        "Despite my offer to pay for Lilly's share, she insists on giving us her portion of the bill, and gives her regards to Yuuko as she takes her leave."

        play music music_dreamy fadein 4.0

        show bg at center
        show hanako:
            center
            ypos 1.09
        with charamove

        "And then… we're alone. It may be all well and good to leave Hanako and me alone to have some time together, but all it typically means is the two of us sitting near each other in silence for a while."

        "I wonder what I must look like to Hanako. I never thought of myself as a scary person, but to have someone my own age acting this way around me makes me intensely self-aware, as if it's my fault that she's so troubled."

        "She might get more used to people if she were to stop being so cloistered in Yamaku, but then again… when even people much older than her react so strongly after a single glance at her face, she may well feel the same way I do now."

        "It's a real catch-22. If she stays in Yamaku, she won't get used to socializing, but if she leaves, any efforts she might try would get thrown back at her by the people who can't deal with her scarring."

        hi "Want to order something else to keep us going? We haven't had much of a dinner, after all."

        show hanako basic_smile_close
        with charachange

        "Hanako brightens and nods vigorously, glad that I brought up the topic for her. I catch Yuuko's gaze, and she dutifully comes over to take our orders."

        show bg at bgright
        show hanako:
            tworight
            ypos 1.09
        with charamove

        show yuukoshang neutral_down at twoleft
        with charaenter

        yu "Would you like something else?"

        hi "I'll just have a sandwich special and a hot chocolate. Bit late for coffee by now. Hanako?"

        show hanako cover_bashful_close
        with charachange

        ha "I-I'll… have the same…"

        hide yuukoshang
        with charaexit

        "With a nod and a bow, Yuuko turns on the ball of her foot and returns behind the counter, where she busies herself fishing out bread and condiments and working the machine to make our drinks."

        show yuukoshang smile_up at twoleft
        show hanako basic_bashful_close
        with charaenter

        "Not a word is said between us until Yuuko comes back. She smiles and gives us our food and drinks, before moving to a customer who's called for her attention."

        hide yuukoshang
        with charaexit

        show bg at center
        show hanako:
            center
            ypos 1.09
        with charamovefaster

        "I give up on the prospect of having much of a conversation with my companion and decide to just enjoy the meal, small as it may be."

        "It tastes nice, as does most of the food here. After having a few mouthfuls, I notice something's missing. Namely, the sound of Hanako eating."

        show hanako basic_distant_close
        with charachange

        "Looking back to her, I see Hanako fidgeting a little behind her untouched sandwich."

        hi "Not hungry?"

        show hanako cover_worry_close
        with charachange

        "She shakes her head from side to side. Even as she does, the patch of hair she keeps over the right side of her face still does its job in hiding it almost entirely."

        ha "I-it's not that."

        hi "Aw. I was all ready to have your share, too."

        show hanako basic_worry_close
        with charachange

        ha "You looked… t-troubled. I-is something… w-wrong?"

        "I'm startled by her thinking that I'm the one who looks troubled, but on second thought, she's probably right. My face may have given away my emotions without me noticing, and she's hardly a dim person; quite the opposite."

        hi "We're friends, right?"

        show hanako emb_downsad_close
        with charachange

        ha "Friends…"

        "From the tone of her voice and shrinking posture, it looks as though I've hit yet another landmine."

        "This is another reason why interacting with her is difficult; the self-imposed psychological barriers she puts up between herself and others, including me and, most likely, even Lilly. It's a shame that—"

        show hanako basic_bashful_close
        with charachange

        ha "I-I think th-that we are…"

        "I'm a little taken off guard by Hanako's straightforward answer, all the more so since I was about to give up on getting any reply at all."

        hi "I see…"

        show hanako basic_worry_close
        with charachange

        ha "A-am I wrong? S-sorry, I-I…"

        hi "No, it's just… hearing confirmation of that from you is reassuring."

        hi "To pick up on what you said earlier: since coming to Yamaku, I've been a bit uneasy about how I should relate with others."

        "I find myself chuckling a little. It's surprising how much of a relief that was. I can feel my face smiling as I pick up my cup of hot chocolate and bring it to my lips."

        hi "Ouch! That's hot…"

        show hanako emb_downsmile_close
        with charachange

        ha "Th-that's why…"

        show hanako emb_smile_close
        with charachange

        ha "That's why I haven't eaten yet. I-I was waiting… for my drink to cool down first."

        hi "I guess I'll wait, then."

        "The both of us share a little chuckle. The situation isn't really that funny, but for some reason… it feels like laughing is the most natural thing to do right now."

        "I guess we were both a bit wound up about each other. I was so busy thinking Hanako was the one with something wrong, it took her to remind me that I was uneasy as well."

        "But be that as it may… it still feels a little nice. A little nice to have someone thinking about me like that, in her own way."

        $ renpy.music.set_volume(1.0, 0.0, channel="sound")
        stop music fadeout 8.0

        scene bg school_dormext_full_ni
        with shorttimeskip

        "Following a long, quiet trudge up the hill and into the school grounds, the two of us find ourselves between the two dormitories."

        "Regular night patrols pass between the male and female dormitory buildings, both for security and to quickly raise the alarm for any medical issues that may arise. The guard currently on duty notices us and gives a quick nod as he continues on his way."

        show hanako emb_downtimid_ni at center
        with charaenter

        "A loud yawn escapes from Hanako's mouth before she has a chance to cover it. I have little doubt she's fairly tired by now."

        hi "I'd better be off to my room, then. See you tomorrow, Hanako."

        show hanako emb_smile_ni
        with charachange

        ha "G-good night…"

        hide hanako
        with charaexit

        "We separate and begin to walk our separate ways, before I stop and look back."

        show hanako basic_smile_ni
        with charaenter

        "Hanako stands there, waving to me as she smiles. I smile and wave back to her, and after a few seconds, she turns and walks up the stairs to her dormitory building, disappearing through the door."

        hide hanako
        with charaexit

        "These little moments we share between us feel like a small treasure. One thing is sure; I want to protect that small, delicate smile she so fleetingly wears around so few people."

        "I wonder about these feelings I have when Hanako's around, and when I'm able to do things for her… whether they may be the seed for something beyond what we share now."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .shady_encounter:
        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        play music music_happiness fadein 2.0

        scene bg school_track
        with locationchange

        "The summertime sun is something to be savored, but when combined with the clean country air, it's all the better."

        "The track and field club members are horsing around on the field ahead; some are playing with a soccer ball, others are talking, and a few laugh as two of them mock-fight with each other."

        "None of them pay me any heed as I sit alone on the grass, underneath the shade of a particularly large tree. It's a nice and peaceful moment after a dreary day of schoolwork."

        play ambient sfx_footsteps_soft fadein 4.0

        "I played soccer pretty often before my heart attack, so I had thought it would be really nostalgic to watch them. What I'm feeling now, though, is quite distinct from that emotion."

        stop ambient fadeout 0.3

        show miki smile:
            center
            easein 1.0 ypos 1.12
        with charaenter

        "I hear footsteps approaching from behind me, and I turn to my side to see one of my classmates taking a seat beside me. I'm taken off guard, as the two of us haven't talked much before, and I didn't think anyone would notice me here."

        show miki grinclosed:
            center
            ypos 1.12
        with charachange

        mk "'Sup."

        hi "Hi. Miura, wasn't it?"

        show miki wink
        with charachange

        mk "Just call me Miki. Surnames are too stuffy."

        hi "Likewise, then."

        show miki smile
        with charachange

        "We both look back out to the field were the guys are playing. It looks like they're getting ready to have a second game, with people spreading out to their positions and the ball being carried to the center of the field."

        "Sure enough, the whistle is blown to begin the match and they get right back into it."

        hi "Not going to play?"

        show miki grinclosed
        with charachange

        mk "Nah, just gonna rest for a bit."

        show miki wink
        with charachange

        mk "What about you? You kinda looked like you wanted to play when you were watching us before."

        "So someone did notice me after all."

        hi "It's kind of a long story."

        show miki grin
        with charachange

        "Her face says that I've piqued her interest."

        hi "I'm in Yamaku because I've got a heart condition. I can't really play soccer any more."

        show miki smile
        with charachange

        mk "Wanted to be a soccer player, did you?"

        hi "No, I only really did it for fun. My friends played it, so I played it as well."

        hi "Any of those guys playing around could have been me before my accident. But I don't feel like I have any real wish to go back to that, either. It's a little hard to explain."

        "I'm still decently physically built from the days when I played, even if my strength's largely left me by now, and I got on well with the other club members."

        "When I think about it, I should feel pretty bad watching people play when I can't any more. Yet I don't. Maybe it's a good thing; a sign that I've gotten over it and that I'm ready to become a new person."

        hi "Sorry, I'm kinda rambling."

        show miki grinclosed
        with charachange

        mk "It's cool. I'm actually glad to hear that."

        show miki smile
        with charachange

        mk "It sounds like you really have your stuff together. Some of the people that come to Yamaku are pretty messed up at first."

        hi "So you're a member of the track and field club, then?"

        show miki grin
        with charachange

        mk "Yup. Been in it since I first arrived."

        hi "Don't suppose you're friends with Emi? Short, fast runner, no legs? I don't think there are all that many female track and field members."

        show miki grinclosed
        with charachange

        mk "Haha, Emi. Everyone knows about her, don't they."

        show miki smile
        with charachange

        mk "But nah, I tend to get on better with guys, so me and Emi don't really talk much. Anyway, what about you?"

        hi "Ah, well, I'm not really in any clubs. Real clubs, anyway."

        show miki wink
        with charachange

        mk "You've been hanging around with Hanako and that blonde Amazon though, right?"

        "Blonde Amazon… I suppose Lilly has the height to fit that description, if nothing else. I nod in response, without making too fine a point of things."

        show miki grinclosed
        with charachange

        mk "Then don't worry about it. As long as you've got some friends, you don't need to join a club."

        "A loud whistling from the field attracts our attention. One of the players is on the ground, clutching his leg, and the others stop play to jog up to him, leaving Miki grimacing."

        show miki serious
        with charachange

        mk "Ouch, that looks painful. That guy really has bad luck."

        "As she continues to look out onto the field, I can't help being reminded of her own injuries. Her left arm, ending in a stump rather than a hand, has been bandaged up for the entire time I've been in Yamaku, and her injury doesn't seem that new."

        "She turns to talk to me again and catches me looking. Both of us sit in awkward silence as she takes her bandaged arm and holds it in her lap with other remaining hand."

        hi "S-sorry. I guess I'm still a bit…"

        show miki smile
        with charachange

        mk "It's fine. Really."

        "Her tone is light, but neither of us says anything afterwards. Every disabled student here has their own way of dealing with their problems, and some finding their conditions troublesome is only natural. I'm included among them, after all."

        "The injured guy from the soccer game manages to get onto his feet with some help, and ends up hobbling off the field with one arm over the shoulder of another for support. Probably just pulled a muscle if he can still manage to walk."

        "The whistle blows again, and the game continues once more with one less man on the field."

        show miki whistle
        with charachange

        mk "Hanging out with Hanako and that blonde girl… you keep some pretty strange company."

        hi "How so?"

        show miki serious
        with charachange

        mk "It's just that Hanako's kind of… I don't know."

        hi "Shy?"

        mk "No, it's not really that. It's just… she's got some issues, I think. I can't really put it in a nice way."

        show miki wink
        with charachange

        mk "Not that I don't think she's a nice person, though. She's perfectly nice."

        show miki serious
        with charachange

        mk "Just… hard to deal with."

        "It sounds like Miki, or at least some other people in the class, have tried to get closer to Hanako in the past. And that it didn't go well."

        "I think her judgment is rather harsh, given that everyone, not just those in Yamaku, have their own issues. Then again, I haven't known Hanako for that long, so it wouldn't surprise me if there was some stuff I didn't know about."

        hi "I'll just take it as it comes. She's a nice person, and I think that should be all that matters."

        "Miki's eyes narrow a little, and her smile spreads."

        show miki grin
        with charachange

        mk "You really like her, don't you?"

        menu:
            with menueffect
            "Miki certainly doesn't mince words."

            "Admit it." if True:
                $ like_hanako = True

                call a3hc1o1
            "Deny it." if True:
                $ like_hanako = False

                call a3hc1o2

        "Miki gives off a different vibe from the other girls. Talking to her feels more like talking to a guy than a woman. Her saying she prefers male company doesn't help to dispel that notion, either."

        "Glancing at my watch shows that lunch break is ending in only a few minutes. Time to start heading back to class."

        hi "Lunch is about to end. Want to head back?"

        show miki smile
        with charachange

        mk "Yeah, we'd better."

        show miki at center
        with charamove

        "I pick myself up off the grass and dust myself off, offering a hand to Miki to help her up as well. She takes it and easily pulls herself up, showing the muscles moving in her toned bare arms in the process."

        hi "Come to think of it, why aren't you wearing the normal girls' blouse?"

        show miki whistle
        with charachange

        mk "Eh, it's too hot and constricting. The boys' uniform is better, anyway."

        "She throws her arms around a bit to emphasize her point, which has the side effect of showing off one particular part of her body that would be especially constricted by the blouse."

        scene bg school_gardens
        with locationchange

        "The two of us start the walk back to the main building through the gardens, talking as we go."

        show miki smile at center
        with charaenter

        mk "It sounds like you're settling in well. That's a relief. It was pretty surprising to get a transfer student at this point in the year, considering the exams are coming up."

        hi "Don't remind me…"

        show miki grinclosed
        with charachange

        mk "Haha, don't worry about them. Just cram it and you'll be fine."

        hi "That doesn't sound like good advice."

        show miki grin
        with charachange

        "She claps my shoulder a couple of times as she grins. I don't think she takes school very seriously."

        show miki wink
        with charachange

        mk "You seem like a smart guy, and Mutou's taken to you well already. You're like a hand in a glove."

        hi "Now to work out whether that's a good thing or a bad thing."

        hi "I still don't know what to make of this school. I've been here a few weeks already, but I still feel dazed at times."

        show miki smile
        with charachange

        mk "You'll get used to it, just give it some time. It's only a high school, just like any other."

        "She makes it sound so simple, but I've never thought about it that way. To me, Yamaku symbolized a marked shift in my life. I was no longer normal; I was 'different,' and was to be educated with other 'different' people."

        "And yet, I'm walking back to class and talking casually with a classmate during lunch, after watching some others play a soccer game - all perfectly normal. Maybe she has a point."

        "Maybe I should just look at Hanako in the same way. Everyone has their own issues; this is hardly something unique to Yamaku. After all, it's only a high school, just like any other."

        "As we continue to talk, I find myself smiling. Miki and I are very different people in almost every way, but it feels good to have gotten to know another classmate a bit better."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .antiques_and_pie:
        play music music_daily fadein 2.0
        $ renpy.music.set_volume(0.4, 0.0, channel="ambient")
        play ambient sfx_parkambience fadein 2.0

        scene bg misc_sky
        with locationchange

        "A light breeze blows the scent of early summer around my head while I wait for Lilly."

        "Small white clouds litter the sky, breaking up the monotony of the blue."

        li "Hisao? Are you here?"

        "Lilly's voice lilts on the breeze as if they were one and the same thing."

        "I stop gazing into the sky to examine Lilly."

        $ renpy.music.set_volume(0.8, 1.0, channel="ambient")

        scene bg school_gate
        show lilly cane_surprised_cas at center
        with locationchange

        "With a peach off-the-shoulder sweater and tan ankle-length skirt, in addition to tan sandals, she's quite a nice sight."

        hi "Yeah, I'm over here, Lilly. Near the gate."

        hi "Were you able to sneak away from Hanako?"

        show lilly cane_weaksmile_cas
        with charachange

        li "Yes. It's not uncommon for me to go out during weekends, so I don't think she noticed anything suspicious."

        show lilly cane_sleepy_cas
        with charachange

        li "That, and… she has someone she sees."

        "Lilly purses her lips, as if she maybe shouldn't have continued. I find it a little hard to believe."

        hi "Hanako's seeing someone? Really?"

        show lilly cane_weaksmile_cas
        with charachange

        li "No, it's just… she sees a therapist every so often on weekends."

        hi "Oh. Well. That does make a lot of sense."

        show lilly cane_reminisce_cas
        with charachange

        "Lilly rubs her arm uncomfortably, and after one look at her troubled expression, I quickly move to change the topic away from Hanako."

        hi "Huh…"

        show lilly cane_surprised_cas
        with charachange

        li "Yes?"

        hi "I was just wondering… you can get around the city on your own?"

        show lilly cane_listen_cas
        with charachange

        "Lilly sighs at my consternation surrounding the topic of her blindness. I'm my own worst enemy, sometimes."

        li "I can, yes. It's easier when I'm out with a friend or my sister, though."

        "I wonder how Lilly gets along with her sister. Being an only child, it's hard to imagine what having a sibling would be like, so it makes me a little envious of her."

        hi "Right. Well then, the bus arrives in a few minutes, so we should probably get a move on."

        show lilly cane_weaksmile_cas
        with charachange

        li "Indeed; it's a long wait if we miss this one."

        stop music fadeout 6.0
        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

        scene bg school_road
        with locationchange

        "With that, we set off for the bus stop on the hill. It's only a small distance from the school gate, so it's very convenient."

        hi "It's a nice view from here. Coming from the city, I never really got to see scenery like this, let alone on a daily basis."

        show lilly cane_smile_cas at center
        with charaenter

        li "This area is nice for me as well. It's tranquil, and away from the noises and smells of the city."

        show lilly back_listen_cas
        show lillyprop back_cane at center
        with charachange

        "Lilly's head perks up in a trademark gesture of hers, signifying that she's caught a sound."

        show lilly back_smile_cas
        with charachange

        li "Oh, here comes the bus…"

        "I look down the road to see the bus trundling up the hill. Her hearing's quite a useful tool."

        "The bus only takes a short while to reach the bus stop, forcing its way up the road, and within a minute we are on our way to the city."

        stop ambient fadeout 2.0

        scene bg city_street1
        with shorttimeskip

        play music music_ease fadein 2.0
        $ renpy.music.set_volume(0.4, 0.0, channel="ambient")
        play ambient sfx_traffic fadein 2.0

        "Walking around the city, I feel a distinct nostalgia. The smells, the traffic, the tall buildings everywhere… It's a lot like my native city, save for the raised walkways."

        "It feels a little weird; walking around a city as casually as I would in a park, but with cars rushing around underneath me."

        "As I'm busily pondering the engineering marvel that is the raised walkway, I get a surprise."

        show lilly cane_smileclosed_cas_close:
            center
            xpos 0.4
            easein 1.0 center
        with charaenter

        "It takes a moment for me to realize that Lilly has wrapped her arm around mine, extending her cane in front of her with her other hand."

        show lilly at center

        "For a moment I'm startled, but I manage to keep enough of a lid on it for Lilly not to notice. While it's not the first time that Lilly's relied on me for guidance, she'd only held onto my sleeve's cuff before."

        "It's logical that it would be easier for her to navigate a crowded and complex area such as the city while securely linked, but I'm far from being as used to this kind of contact as Lilly is."

        "Finally realizing the growing silence between us as Lilly waits for me to get moving, I quickly kick my brain into gear."

        hi "You know, it was quite a surprise that Hanako likes to sing. Have you ever heard her do that before?"

        show lilly cane_smile_cas_close
        with charachange

        li "I have indeed. We've been to karaoke sessions several times, along with my sister. I can't say I take to the activity much, but the other two like it."

        "Maybe Hanako doing karaoke is more fitting than I initially thought. Just her and those she knows, all alone in a little room."

        "It would give her a rare chance to let her guard down, with nobody else there to judge her."

        hi "Maybe it would be nice to bring her into town for a karaoke birthday party, if she likes doing it."

        show lilly cane_sleepy_cas_close
        with charachange

        li "Hmm. I'm not sure she would deal very well with the excitement."

        "I move to protest, but her face shows that she's mulling the proposal over some more. It takes quite some time for her to come to a conclusion."

        show lilly cane_weaksmile_cas_close
        with charachange

        li "Then again, the best thing we can do for Hanako at this point is to try to create some pleasant birthday memories. Continually treating her as if she's abnormal won't help."

        hi "I think you're right; if she has something to remember apart from loss, then maybe she'll come around."

        "If we bought her something nice that she could see every day then maybe she'd be able to take her mind off her past and remember that she has friends."

        "And in any case, I think Hanako can handle something like this. In the time I've spent beside her, I've learned that she isn't quite as frightfully fragile as I first thought she was."

        hi "So, shall we be off? I'm not really sure about the layout of this area."

        show lilly cane_smileclosed_cas_close
        with charachange

        stop music fadeout 6.0

        li "Very well. I might like to suggest having something to eat, first."

        hi "I haven't either, so that sounds like a good plan."

        show lilly cane_cheerful_cas_close
        with charachange

        li "Make sure you choose a nice place, Hisao."

        "She gives a teasing smile, one that makes me smile reflexively in response even if she can't see that."

        hi "I'll make very sure I do, don't worry about that."

        stop ambient fadeout 1.0
        play music music_another fadein 4.0
        scene bg city_karaokeint
        with locationskip

        "Once inside, I order two slices of pie and accompanying cups of tea and take them back to our table."

        show lilly basic_smileclosed_cas_close:
            center
            ypos 1.1
        with charaenter

        "I'd pegged this café as the type to appeal to Lilly; small and quiet, but well-kept and somewhat upscale. Going by the dainty smile she wears, I… don't really know if I chose right."

        "It's very, very rare to not see her smiling, after all."

        "Nevertheless, I take a seat near her at one of the corner tables and lay down our small meals."

        show lilly basic_planned_cas_close
        with charachange

        "Lilly gingerly brings her head over the slice of pie placed in front of her, delicately taking in the aroma."

        show lilly basic_cheerful_cas_close
        with charachange

        li "Lemon pie, is it? Thank you, Hisao."

        hi "No problem. The tea's just next to it, so be careful not to knock it over."

        show lilly basic_weaksmile_cas_close
        with charachange

        "She nods appreciatively, but judging from the slightly weak smile she has, the warning wasn't really necessary. I suppose the sound must have tipped her off to its position."

        "We both tuck into our food without further ado, both of us remaining largely silent as we do so. Lilly isn't the type to appreciate discussion while eating, and I can't say I like it either."

        "Eventually we finish both our meals, and the last of our teacups follows in short order. Lilly's the first to break the silence."

        show lilly basic_smile_cas_close
        with charachange

        li "That was very nice. I must say you've chosen quite well, Hisao."

        hi "This is the first time I've really had much of a look around the city, so all I could really do is choose somewhere that looked nice."

        hi "Uh… damn. Sorry."

        "I feel really bad for inadvertently bringing up the subject of sight around Lilly, but she doesn't appear to mind much. Quite the opposite; she almost looks amused by my awkward attempt at an apology."

        show lilly basic_smileclosed_cas_close
        with charachange

        li "You are thoughtful, Hisao, but sometimes I fear that it gets the better of you. There is no need to change your speech on my account."

        "Lilly truly is pretty comfortable in dealing with her condition. I still hasten to change the subject, as I can't really say that I share her confidence in the matter."

        hi "Have you lived here for very long? It seems like you have this place pretty much sorted out."

        show lilly basic_planned_cas_close
        with charachange

        "She quickly waves her hand in front of her face to dismiss the notion."

        show lilly basic_smile_cas_close
        with charachange

        li "It's nothing like that. I've attended Yamaku since the start of high school, but I didn't walk around the city very much because Akira, my sister, picked me up and dropped me off."

        hi "Oh, right. You mentioned not living in the dormitories until recently."

        "It's quite a surprise. I'd just assumed she'd been living here since entering Yamaku at the least, which would give her a few years here."

        show lilly basic_smileclosed_cas_close
        with charachange

        li "I've lived with my family for most of my life, then I was just together with my sister. With my family having moved to Inverness long before, and Akira working longer hours, I ended up having to move."

        hi "Inverness? Isn't that somewhere in Scotland?"

        show lilly basic_surprised_cas_close
        with charachange

        li "Oh, did I not tell you? My family currently lives in Scotland, the birthplace of my mother. My father's side is mainly Japanese, though."

        "Huh. The question of what gave Lilly her looks did cross my mind every now and again, but I'd never thought to ask. That answers that, then."

        hi "To be honest, I'd never have guessed. Considering you have no accent, I'm guessing you were born here?"

        show lilly basic_giggle_cas_close
        with charachange

        li "Full marks. I am thankful for my heritage though, as without it I'd likely have not been taught English so early in my life."

        show lilly basic_smile_cas_close
        with charachange

        li "And what of you, Hisao?"

        hi "What about me?"

        "She gives a moment's thought. She probably should have thought of what to ask me before switching the topic."

        show lilly basic_weaksmile_cas_close
        with charachange

        li "I'll go with… what are your plans for the future?"

        hi "To be honest, I haven't thought much about that recently."

        hi "After my accident and subsequent months in hospital, enjoying my life here with you and Hanako has been enough for me."

        "In fact, I don't think I've thought at all about a 'future' for some time now. It seems almost futile."

        show lilly basic_sleepy_cas_close
        with charachange

        li "This is your last year of school. After this, you will have to fend for yourself one way or the other."

        hi "It's not like I don't know that, I just haven't put much thought into it since then…"

        show lilly basic_weaksmile_cas_close
        with charachange

        "She opens her mouth to continue, but gives a small sigh instead. She seems to have realized that she really doesn't know enough about my situation to go too deeply into this."

        li "Well, we all have our own pace. I just hope you'll take any chance you see."

        hi "…I understand. I'll think about it."

        stop music fadeout 2.0

        $ renpy.music.set_volume(0.4, 0.0, channel="ambient")
        play ambient sfx_traffic fadein 2.0

        scene bg city_street2
        show lilly cane_smileclosed_cas_close at center
        with shorttimeskip

        "As we walk back out into the city, Lilly takes hold of my arm once again."

        show lilly cane_smile_cas_close
        with charachange

        li "So, did you get any good ideas for a present?"

        hi "To be honest, no. I've never been very good at picking them."

        show lilly cane_weaksmile_cas_close
        with charachange

        li "As absurd as it sounds, perhaps we should just… look around?"

        "Hearing Lilly utter those words throws me for a moment."

        hi "Er… right. How do we do that?"

        show lilly cane_cheerful_cas_close
        with charachange

        li "That's just the reaction I was expecting. It's simple; you can go window shopping, and just tell me what is around."

        show lilly cane_smileclosed_cas_close
        with charachange

        li "If something interesting comes up, then we might get an idea."

        hi "Right… I'm still not so sure of this, but I'll take your word for it."

        show lilly cane_smile_cas_close
        with charachange

        li "I think we'll manage. Hanako, my sister, and I manage to do it well enough."

        $ renpy.music.set_volume(0.2, 1.0, channel="ambient")

        scene bg city_street3
        with locationskip

        "With Lilly's simplistic and rather optimistic statement, we set off into the shopping district of the city and I start describing everything I see to Lilly."

        "It's hard to think of Hanako going window shopping. She doesn't feel like the type to place much stock in fashion, nor have I noticed her reading magazines or the like. In fact, all I think I've really seen her do as a hobby is read books."

        hi "There's a housewares shop just ahead. Looks like it's mostly crockery though."

        show lilly cane_sleepy_cas_close at center
        with charaenter

        li "I can't think that she'd have much of a need for that, and what type of message would that send to her?"

        hi "Um… 'cook more food?' That's not such a bad idea, maybe…"

        show lilly cane_weaksmile_cas_close
        with charachange

        li "Sometimes it's best to leave these things alone, Hisao."

        "Once again, I get the feeling that Hanako's exploits in the kitchen aren't always successful. Lilly must have had to help her with that sometimes."

        hi "Let's see, next along is a bookshop… that seems like a good one, she's always reading."

        show lilly cane_concerned_cas_close
        with charachange

        li "Yes, but there are a few problems with books. I'm not quite sure what she has and hasn't read."

        hi "What about a gift card then?"

        show lilly cane_listen_cas_close
        with charachange

        li "There's nothing as impersonal as giving someone a gift card. It's like saying 'I don't know enough about you to work out what you'd like.'"

        hi "I always thought of it as making sure they got what they wanted."

        show lilly cane_displeased_cas_close
        with charachange

        li "Giving people gifts is supposed to show them the level of affection you have for them. If you can't decide on a simple gift for them, then how much could you think of them?"

        hi "Right, right, no gift cards."

        "Lilly seems overly passionate about this, but I can see her point. If you're going to get something for someone, then you should put at least some thought into it."

        "If I want to get something for Hanako that reminds her of us every day, then what good is a gift card?"

        hi "In that case, what did you get Hanako last year?"

        show lilly cane_smile_cas_close
        with charachange

        li "A porcelain doll. I thought that if she had someone to talk to, it might help her ease her pain."

        show lilly cane_weaksmile_cas_close
        with charachange

        li "A doll isn't ever going to criticize her, after all."

        hi "So should I be looking for a doll shop?"

        show lilly cane_smileclosed_cas_close
        with charachange

        li "If you could be so kind to keep a lookout for one, I would be grateful."

        hi "Sounds good to me, though I wish you'd mentioned it earlier."

        show lilly cane_cheerful_cas_close
        with charachange

        li "But if I did that, then you wouldn’t have started thinking for yourself, would you?"

        "Once again Lilly has a point. My brain is currently analyzing every store we pass for gift options. If Lilly had mentioned a doll shop to begin with I wouldn't have thought of anything else."

        $ renpy.music.set_volume(0.4, 1.0, channel="ambient")

        scene bg city_street4
        with locationskip

        "We wander through the city's streets, but seem unable to find anything that resembles a doll shop, or anything that I could consider a fitting present."

        "The simple act of searching is starting to clear my head. The events of last week are starting to fade away, and I'm looking forward to giving Hanako her gift…"

        "…if I can find one, that is."

        hi "This is hopeless. I thought we'd be able to find something in the city for sure. And I'm sure we've walked down this street at least once before."

        show lilly cane_oops_cas_close at center
        with charaenter

        li "That almost sounds like you're giving up, Hisao."

        hi "I'm not, but it's a lot harder than I thought."

        show lilly cane_smileclosed_cas_close
        with charachange

        li "Try not to be so restricted in your thinking. Maybe we should actually go into some shops and have a look around?"

        hi "That might work. I've never really been any good at window shopping."

        $ renpy.music.set_volume(0.2, 1.0, channel="ambient")

        scene bg city_street3 at right
        with locationskip

        "Lilly and I circle around the city's streets once more, this time popping into stores that catch our attention. In the end, though, nothing comes up as especially appropriate."

        "Hanako's tastes are often quite hard to pin down at the best of times, thanks to her intensely private nature, and those tastes we do know are hard to accommodate."

        show lilly cane_sleepy_cas_close at center
        with charaenter

        li "May we take a break for a minute? I'm a bit exhausted."

        show lilly cane_sleepy_cas_close:
            ypos 1.05
        with charamove

        show lilly:
            ease 1.0 xpos 0.8 alpha 0.0
        with None

        show bg at left
        with charamovefaster

        "I agree and leave Lilly to rest against a railing while I go to get a couple of drinks from a nearby vending machine."

        "After walking up to the vending machine and grabbing myself some lemonade, I find myself at a bit of a loss. Not really knowing Lilly's tastes, I decide to take a guess and grab something that seems a little girly, but not too weird; strawberry-flavored milk."

        show bg at right
        show lilly cane_weaksmile_cas_close:
            center
            ypos 1.05 alpha 1.0
        with charamovechangefaster

        show lilly:
            center
            ypos 1.05

        hi "Back."

        "I walk up to her and place the carton into her outstretched hands, making sure she has a grip on it before letting go."

        show lilly cane_smile_cas_close
        with charachange

        "She feels out its contours before opening it and taking a very tentative sip, her approving smile afterwards telling me I made the right choice. We both rest and have a quiet drink for a few minutes."

        $ renpy.music.set_volume(0.2, 0.0, channel="sound")
        play sound sfx_phone

        show lilly cane_surprised_cas_close
        with charachange

        "A familiar soft ringing begins to sound from Lilly's side. She quickly apologizes as her hand goes into her pocket, pulling out her mobile phone."

        show lilly cane_weaksmile_cas_close
        with charachange

        li "Do you mind if I take this?"

        hi "It's fine, don't worry."

        show lilly back_listen_cas_close
        show lillyprop back_cane_close:
            center
            ypos 1.05
        with charachange

        "She nods to me in thanks before turning away and flipping the phone open, bringing it to the side of her face as she picks up the call. "

        show lilly back_smile_cas_close
        with charachange

        "Going by the tone of Lilly's voice, the person on the other end is no doubt some friend or another. I tune out of their conversation pretty quickly, as the snippets that Lilly says make it sound like little more than gossip."

        "Without much else to do, I find myself watching Lilly. She really is a pretty girl, which would hardly hurt her popularity in school. It's interesting just how much Hanako and Lilly contrast with each other, in both personality and appearance."

        show lilly back_smileclosed_cas_close
        with charachange

        "For a few minutes I just lean back and drink, watching her. Before long, Lilly says her goodbyes to the person she's talking to and hangs up, placing her phone back in her pocket and leaning back against the railing as before."

        hide lillyprop
        show lilly cane_weaksmile_cas_close
        with charachange

        li "Sorry, just a friend from class."

        $ renpy.music.set_volume(1.0, 0.0, channel="sound")
        play sound sfx_can_clatter

        "I take one final swig from my can before throwing it into the bin. Lilly gives me her carton to throw away soon after, finishing it off relatively quickly."

        $ renpy.music.set_volume(0.1, 2.0, channel="ambient")

        hi "You seem to have a lot of friends."

        show lilly cane_smile_cas_close
        with charachange

        li "Oh?"

        "Lilly waits for me to continue, her interest piqued."

        hi "I was just thinking that you and Hanako contrast really heavily. It's hard to imagine Hanako doing a lot of the things you do, or knowing the people you know."

        show lilly cane_giggle_cas_close
        with charachange

        li "You seem to think about Hanako quite a bit."

        hi "I don't know. It's just… she's mysterious, I guess. I kinda want to know more about her, which isn't that easy."

        show lilly cane_weaksmile_cas_close
        with charachange

        li "It almost sounds like you're doubting your relationship to her."

        hi "I don't think it's that. I just want to do more for her, being her friend and all. I don't even really know how she sees me."

        show lilly cane_smile_cas_close
        with charachange

        "This statement seems to interest Lilly quite a bit. I wonder if Hanako's said anything about me to Lilly during their conversations."

        show lilly cane_smileclosed_cas_close at center
        with charamovechangefaster

        "I'm about to ask what's on her mind as she picks herself up from the railing."

        show lilly cane_cheerful_cas_close
        with charachange

        li "Shall we be off, then?"

        "Her voice and expression show that she's playing games with me. Lilly knows damn well that she's leaving me hanging."

        "With a sigh, I pick myself up off the railing as well and have a brief look around. We have stuff to do, so I'll just try and get back to her about this later."

        "Tucked in between a newsstand and a convenience store is a small shop. The sign above the door reads 'Othello's Antiques' in decorative English script."

        "It would be easy to miss if we were walking along the street, but since we're stationary and I'm purposefully looking around, it's just noticeable."

        $ renpy.music.set_volume(0.3, 6.0, channel="ambient")

        hi "Say, Lilly… that doll you got Hanako; was it new?"

        show lilly cane_smile_cas_close
        with charachange

        li "Well, yes, but I'm not quite sure I know what you mean."

        hi "I think I've found our shop. It's across the road."

        show lilly cane_surprised_cas_close
        with charachange

        li "Oh? What is it? Some kind of toy shop?"

        hi "It's an antique shop. I think it's probably going to be our best bet."

        show lilly cane_satisfied_cas_close
        with charachange

        li "Really? I didn't know we even had one of those near here."

        hi "Neither did I, I missed it the first time we went by here. It's pretty well hidden."

        show lilly cane_smileclosed_cas_close
        with charachange

        li "Well then, it can't hurt to check."

        "Inspired by this new find, we quickly dust ourselves off and head towards the store, Lilly's hand finding its way to my elbow for guidance."

        stop ambient fadeout 0.5

        $ renpy.music.set_volume(1.0, 0.0, channel="sound")
        play sound sfx_storebell
        play music music_soothing fadein 0.5
        $ renpy.music.set_volume(1.0, 4.0, channel="ambient")

        scene bg city_othello at right
        with locationchange

        "The store has a strange, musky scent to it. The layout is more like a garage than a store; things are strewn around the floor without any immediate semblance of order."

        show shopkeep neutral at center
        with charaenter

        "The shopkeeper gives us an almost bored look though his particularly small eyes. His face looks weary and tired, and his dress style is distinctly anachronistic. He gives us a polite nod of welcome before going back to his book."

        hide shopkeep
        with charaexit

        "Lilly holds tightly onto my arm, and I find myself having to split my efforts between making sure we don't miss a potential gift for Hanako and making sure Lilly doesn't inadvertently bump into anything."

        show bg at center
        with charamove

        "The task is quite difficult given the haphazard way the store is laid out, and the many things poking out of the shelves they're on or sitting on pieces of furniture, but eventually we safely arrive at an old desk covered in dolls and teddy bears."

        hi "I think this is the right place. There's pretty much every kind of doll you could imagine here."

        show lilly cane_smileclosed_cas_close at center
        with charaenter

        li "That should make the choice much simpler. Could you please pick one for me, Hisao?"

        "I had a feeling that it would come to this. I picture Hanako in my mind, and try to imagine which of the dolls before me would suit her the best."

        "My eyes wander across the collection; each one is as exquisite as the one before it. The sheer number of styles is boggling, but eventually one catches my eye."

        hi "Here, what about this one?"

        "I pick up a small porcelain doll that looks to be at least somewhat affordable. Dressed in a Victorian era green dress with a little brown hat sitting atop its blonde hair, it looks a little like Lilly."

        show lilly cane_listen_cas_close
        with charachange

        "I gently pass it to her, who delicately feels her way around the object while wearing a look of slight concentration."

        show lilly cane_smile_cas_close
        with charachange

        li "It certainly feels beautiful. Do you think it would suit Hanako, in your opinion?"

        hi "I think it would; it could look good in her room."

        show lilly cane_smileclosed_cas_close
        with charachange

        li "In that case, I'll trust your judgment. Will you be getting her something as well, or shall this be a shared gift?"

        hi "Hmm, I'm not sure. I think I should get her something myself, but I don't think getting her another doll is such a great idea. Maybe…"

        "I let my voice trail off as I look around the shop. Resting on a writing table not far from us is a decorative box that catches my eye."

        hi "Wait here, I think I've found something…"

        show lilly cane_ara_cas_close
        with charachange

        li "My my, that was fast."

        "I gingerly walk through a collection of crystal glassware and pick up the box. The wooden sides are covered in carvings depicting ancient battles around a castle."

        "The top, however, looks far too familiar. Alternating squares of white- and black-varnished wood are arranged on the lid."

        sk "That's a really nice item. It's a chess set from overseas."

        show bg at bgleft
        show lilly cane_smileclosed_cas_close at twoleft
        with charamovechangefaster

        show shopkeep neutral at tworight
        with charaenter

        "The store owner's sudden appearance startles me a little; I didn't see him approaching at all."

        "I suppose he's trying to help us because we don't really look like we know what we're looking for. …Or on the other hand, maybe he wants to keep an eye on us because he suspects we might shoplift instead."

        hi "I'm… looking for a present for a friend."

        show shopkeep happy
        with charachange

        sk "I see. In that case, this chess set would make a fine choice."

        "Realization floods into my mind. This is a pretty good-looking set, but this is an antique shop. They're not well known for their bargain prices."

        hi "How old is this?"

        show shopkeep neutral
        with charachange

        sk "This is a reproduction. My best estimate is that it's about five years old."

        hi "I see. How much?"

        show shopkeep thinking
        with charachange

        "He thinks a little before telling me, which is slightly disconcerting."

        show shopkeep neutral
        with charachange

        sk "I'll let you take this now for 7000 yen."

        "I balk a little; I wasn't expecting to spend that much, but this does seem perfect. Then again, maybe that's a testament to how well he worked out how much he could make me pay."

        hi "Couldn't make it 5000?"

        show shopkeep thinking
        with charachange

        sk "5500, no lower."

        hi "I'm sold. Oh, we'd also like to get that doll…"

        show shopkeep neutral
        with charachange

        "The store owner looks over my shoulder, focusing on Lilly and the doll in her hands. His eyes narrow, and he visibly takes a moment to switch mental gears."

        "In the process, his smile drops slightly."

        sk "Ah…"

        "I guess that means that not everything in his store is a reproduction."

        show shopkeep thinking
        with charachange

        sk "Are you quite sure that you want that doll, miss?"

        show lilly cane_smile_cas_close
        with charachange

        li "I trust my friend's judgment."

        show shopkeep surprised
        with charachange

        sk "I see… oh, no offense…"

        show lilly cane_smileclosed_cas_close
        with charachange

        li "None taken. If you could please wrap it for me, it would be appreciated."

        show shopkeep neutral
        with charachange

        sk "Yes, of course, but it is 20,000 yen…"

        "Lilly reaches into her purse and presents four crisp-looking 5,000 yen notes."

        show lilly cane_cheerful_cas_close
        with charachange

        li "Here you are, 20,000 yen."

        show shopkeep thinking
        with charachange

        "The storekeep dutifully takes them and the doll, and proceeds to the counter. I take Lilly's arm to guide her there."

        hi "Are you sure about this?"

        show lilly cane_smileclosed_cas_close
        with charachange

        li "It's okay; I… have the funds I need. As I said, I trust your judgment."

        "I feel a little guilty on two fronts; firstly because Lilly has just spent a lot of money on my recommendation, and secondly because I have a feeling the value of my gift isn't high enough."

        "Nevertheless, Lilly does seem to get somewhat awkward whenever the mention of money comes about…"

        show shopkeep neutral
        with charachange

        "I hand the shopkeeper my present and the money for it in turn. He puts the cash into the register before busying himself with wrapping the doll and repeating the process on the chessboard."

        "Eventually, he finishes the giftwrapping and hands us both our presents."

        show shopkeep happy
        with charachange

        sk "Please be careful on your way back, and do come again."

        hi "Thanks."

        show lilly cane_smile_cas_close
        with charachange

        li "Indeed, thank you very much."

        "The store owner bows deeply to us as we leave."

        stop music fadeout 6.0
        $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
        play ambient sfx_traffic fadein 1.0

        scene bg city_street3
        with locationchange

        show lilly cane_weaksmile_cas_close at center
        with charaenter

        li "Well, it did take us all day, but we found something in the end."

        hi "That we did."

        "Now that the presents are wrapped, I'm feeling a little impatient to give them to Hanako. It's a common reaction to buying gifts; wanting to see the reaction of the receiver as they discover what it is."

        "And part of me wants to return to Hanako, just to confirm her condition with my own eyes."

        hi "So should we head back?"

        show lilly cane_smile_cas_close
        with charachange

        li "Let's. We've done a lot of walking today, so I shan't mind taking a rest back at the dormitories."

        "Lilly's right. Now that the need to find a shop is over, my legs are feeling quite tired."

        hi "Well then, back to the school for us. I'm looking forward to resting for a bit, too."

        "Lilly holds out her arm, and I link mine with hers. Together, we make our way back to the bus stop."

        stop ambient fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .falling:
        play music music_pearly fadein 5.0

        scene bg school_scienceroom at right
        with locationchange

        "Mutou reads equations and formulas to us one by one, in his usual, unenthusiastic monotone, directly from the book."

        "It's possible that he might be excited about what he teaches us; sometimes he can display an awkward spark of passion for it, as if he's starting to get into the material."

        "Most days, however, are like this one. What we're covering is fairly simple, so I find it increasingly difficult to keep my concentration on him. It's not too long until my legs begin aching again, which only makes it even harder."

        "I'm almost starting to regret walking around the city yesterday with Lilly."

        "Since leaving the hospital, I've done very little physical exertion. Walking to and from the local corner store hardly counts. Despite Emi's attempts when I first arrived in Yamaku, I've largely given up on the idea of ever returning to my old level of fitness."

        "I have little doubt that's why walking around town for so many hours has made me quite so sore. It's depressing, and it reminds me of one more thing I can't do since I had my heart attack. It makes me feel pathetic."

        show muto normal at twoleft
        with charaenter

        mu "Now… Ikezawa?"

        show hanako defarms_shock at tworight
        with vpunch

        "It's odd for Mutou to ask Hanako a question, but not unheard of. She quickly jumps to her feet, a little startled, and immediately pins her eyes onto him."

        "She knows that Mutou calling on her is rare, so all eyes in the classroom are going to be on her. This way, she doesn't run the risk of making eye contact with anyone else."

        show hanako def_worry
        with charachange

        ha "Y-yes?"

        mu "In this particular example of a redox reaction, the combustion of methane reaction actually produces one more product than is listed. That product is…?"

        show hanako emb_downtimid
        with charachange

        "Even though it's a softball question, she timidly waits a bit before answering, biting down slightly on her lower lip as if to keep her concentration."

        show hanako emb_timid
        with charachange

        ha "Um… h-heat?"

        show muto smile
        with charachange

        mu "Well done. This is an exothermic reaction, with the reaction giving more heat than is put into it."

        show hanako:
            ease 1.0 ypos 1.1 alpha 0.0
        with Pause(1.0)

        hide hanako

        "Receiving a nod from Mutou, Hanako takes her seat once again and gives a relieved sigh."

        "A shaky start, but it's something."

        "It'll be nice to take her out for her birthday, somewhere different from the usual isolation of her room and the tea room. With the progress she's made until now, I don't think she'll have much of a problem going to the city."

        show bg at center
        show muto at center
        with charamove

        mu "Right then. For the remainder of this class I'd like you to work in groups of three or four on the problems in chapter 12. I'll be here if you need me."

        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
        play ambient sfx_crowd_indoors fadein 8.0

        show muto:
            ease 1.0 ypos 1.1 alpha 0.0
        with Pause(1.0)

        hide muto

        "Mutou sits down behind his desk, pulls some loose sheets out of a folder and starts on some kind of paperwork of his own. I thought teachers were supposed to do that kind of thing after class, not during it."

        show shizu behind_blank_close:
            tworight xpos 0.8 alpha 0.0
            ease 1.0 tworight alpha 1.0
        show misha hips_smile_close:
            twoleft xpos 0.2 alpha 0.0
            ease 1.0 twoleft alpha 1.0
        with Pause(1.0)

        show shizu at tworight
        show misha at twoleft

        "Regardless, I look to my right to pick out someone to form a group with. Given the two smiling faces hovering near mine, I don't think I'm going to get much say in the matter."

        hi "I suppose we have a group, then."

        show misha hips_grin_close
        with charachange

        mi "Hicchan~! You want to work together? Okay, okay~! That's great! It's really been a while~!"

        show shizu:
            ypos 1.09
        show misha hips_smile_close:
            ypos 1.09
        with charamovechangefaster

        "The class begins the process of noisily shuffling the desks around, with Shizune doing the same as she puts hers in front of mine. She's a little lucky to not be able to hear the din of the classroom, which is loud enough to cause some discomfort."

        "Truth be told, working with Shizune and Misha is probably a good outcome - Shizune and I are pretty good at this subject, and Misha… has really nice handwriting."

        show hanako silhouette behind shizu at center
        with charaenter

        "As I look to Misha, I notice a tall figure behind her. The shadow catches Misha's attention as well and she turns to face the dark-haired observer."

        show shizu:
            xpos 0.8
        show misha perky_smile_close:
            xpos 0.2
        show hanako basic_worry
        with charamovechangefaster

        mi "Good afternoon, Hanako~!"

        show hanako emb_timid
        with charachange

        ha "Um… hello…"

        "Shizune finally notices Hanako, after looking up and following the gazes of Misha and I. In quick measure, she taps Misha on the shoulder to get her attention before signing away."

        show shizu adjust_happy_close
        with charachange

        shi "…"

        show misha sign_smile_close
        with charachange

        mi "Shicchan says, if you're looking for a group, you can join ours~!"

        show hanako emb_downsmile
        with charachange

        "Hanako looks down and blushes a little at the offer. Out of all the people in the class, Hanako's most familiar with the three of us, so it's reasonable that she'd come to us first."

        "Then again, her actually coming up to a group with the intention of joining them is something she apparently very rarely did before."

        hide hanako
        with charaexit

        show shizu behind_smile_close:
            tworight
            ypos 1.09
        show misha hips_smile_close:
            twoleft
            ypos 1.09
        with charamovechangefaster

        "She leaves briefly to drag her desk over, and Shizune and Misha wheel back to me as soon as her back is turned."

        show shizu adjust_happy_close
        with charachange

        shi "…"

        show misha perky_smile_close
        with charachange

        mi "I guess we get to play again, Hicchan~! You hardly ever play with us any more…"

        hi "I wonder why? You two always seem to have some ulterior motive."

        show shizu basic_frown_close
        with charachange

        shi "…"

        show misha hips_frown_close
        with charachange

        mi "That hurt, Hicchan… I'd almost think you were insulting me~!"

        show misha hips_grin_close
        with charachange

        mi "But~! It's Hicchan, so I know that you're joking!"

        hi "Such a great sense of humor about it; it'd be awful if someone were to take advantage of your good nature. Like making you help them with their work."

        show shizu adjust_smug_close
        with charachange

        shi "…"

        show misha cross_laugh_close
        with charachange

        mi "Wahaha~!"

        "Shizune seems excited for a second, a little surprised that I'm willing to challenge her, but when she sees Hanako coming back, she backs off with a smile. I guess the mind games are over early today."

        show hanako emb_downtimid_close behind shizu:
            center alpha 0.0
            ease 1.0 ypos 1.09 alpha 1.0
        with None

        show shizu behind_blank_close:
            xpos 0.85
        show misha perky_smile_close:
            xpos 0.15
        with charamovechangefaster

        show hanako:
            center
            ypos 1.09

        "Hanako gently sets down her desk in front of Misha's. Her eyes are locked downwards, and I'm left wondering why until I look around the class."

        "Most are busy setting up their own groups, but a few are casting curious glances at her. At this range, it's hard to tell whether that is where their interest in her ends, or if they are talking about her as well."

        "It's strange. No one bats an eyelid when Hanako runs out of class to avoid group work, but now that she's making an effort they're staring at her as if she's done something wrong."

        "We all move to sort ourselves out, spreading our textbooks and worksheets around the larger surface created by the four joined desks. It isn't long before the class as a whole gets down to work."

        show misha sign_smile_close
        with charachange

        mi "Hi, Hanako~! It's nice to finally work with you~."

        show hanako basic_distant_close
        with charachange

        ha "Y-yeah."

        show shizu adjust_smug_close
        with charachange

        shi "…"

        show misha hips_grin_close
        with charachange

        mi "Are you the reason Hicchan has been avoiding us, lately~? Shicchan says it's a little rude, but if Hicchan wanted to spend time with a cute girl, it's understandable~!"

        show hanako cover_worry_close
        with charachange

        ha "I-I don't t-think it's like that…"

        "Hanako starts to fidget, unused to this kind of attention."

        "I think that an ordinary person would drop the conversation by now, but Misha is like the antithesis of Hanako. Part of that includes being blind to ordinary social cues, while Hanako is overly sensitive to them."

        "Because of that, Misha barrels ahead with the questions, too quickly for me to get a chance to interject and guide the discussion somewhere more comfortable."

        stop music fadeout 7.0

        show misha hips_smile_close
        with charachange

        mi "Really~? So~! He wasn't hanging out with you yesterday?"

        show hanako emb_downsad_close
        with charachange

        ha "N… no…"

        "I can feel my cover being blown already. Lilly didn't want Hanako to know that we were out buying presents for her, let alone planning out her birthday party. It wouldn't be good for her to find out."

        hi "Yeah I was… doing something else. You know how it is…"

        show shizu behind_blank_close
        with charachange

        shi "…"

        show misha sign_smile_close
        with charachange

        mi "Really~? I wonder what was so important, for Hicchan to blow us off like that~! If it wasn't to spend time with Hanako, then what could it be~? It's really interesting…"

        "Now this is starting to feel like an interrogation. I'm surprised at how Misha is able to exert such a feeling of pressure without actually intending to."

        show hanako defarms_strain_close
        with charachange

        ha "W… were you with L-Lilly?"

        $ renpy.music.set_volume(0.3, 0.0, channel="ambient")

        "Out of nowhere, Hanako manages to stumble on the answer. She may be dreadfully quiet and shy, but she's very intuitive."

        hi "W-what makes you say that?"

        show hanako emb_sad_close
        with charachange

        ha "Y-yesterday Lilly said something s-similar."

        show shizu basic_happy_close:
            xpos 0.8
        with charachangealways

        shi "…"

        show misha hips_smile_close
        with charachange

        mi "Suspicious~! Hicchan~! I demand that you explain yourself!"

        hi "Hey, shouldn't we be doing the assignment?"

        show misha cross_smile_close
        with charachange

        mi "But~! It's so mysterious… Even Hanako wants to know~!"

        "I turn to look at Hanako. It's true; from the expression on her face, it's obvious that she wants to know as well, and I think we're past the point where I could weasel out of having to provide an explanation."

        "I apologize to Lilly in my mind. She really did want to keep it a secret, but now it doesn't seem possible any more."

        "I feel a rush of conflicting emotions, so jumbled that I can't readily identify them, but they crash around in my head as I try to calm down and speak."

        hi "All right, I'll tell you. I went into town with Lilly, but it wasn't what you think."

        hi "Lilly and I were… uh… for Hanako's birthday… we were…"

        "The cat is out of the bag. But it looks like Hanako is taking it a little better than I thought she would."

        show misha perky_confused_close
        show shizu adjust_blush_close:
            xpos 0.85
        show hanako emb_downtimid_close
        with charachangealways

        "A brief silence passes around our little group as Shizune and Misha look at each other sheepishly. I can tell that they didn't expect their game to turn out like this."

        "Misha looks up to Hanako in order to apologize, then pauses. Hanako is staring at the middle of her desk and barely moving, a maudlin expression on her face. I guess I was wrong about her taking it well."

        show misha perky_sad_close
        with charachange

        mi "Hanako? I'm sorry…"

        "There's a few seconds' pause, but Hanako lifts and shakes her head."

        show hanako emb_timid_close
        with charachange

        ha "I-it's… okay…"

        "Her expression looks odd, like she's very tired. That doesn't seem natural, but it's nothing alarming. Nobody really wants to continue with the current conversation, so we open our textbooks and begin our group work."

        play music music_rain fadein 12.0
        $ renpy.music.set_volume(0.5, 5.0, channel="ambient")

        show shizu basic_normal2_close:
            xpos 0.8
        with charachangealways

        "This is pretty dull. While the equations we're supposed to work out as a group will take a while, most of it is going to be boringly mechanical."

        "It also doesn't help that while that didn't go as bad as it could have, it has left an awkward atmosphere around us. Still, we manage."

        "Shizune's face betrays that she has about the same expectations of our work as I do, and the two of us begin to write our group's results."

        show misha perky_confused_close
        with charachange

        "Misha, on the other hand, is scrunching up her lips and very visibly trying to make heads or tails of what we're doing. Hanako is looking on quietly, absorbing what we write and what I say. She usually has this same expression when the teacher speaks."

        "It's a shame her attendance is so unreliable. With the way she takes in information, I think she'd do quite well in class, if she actually followed the lessons regularly. I wonder if this might be why Shizune seems so hard on her."

        show misha perky_smile_close
        with charachange

        mi "Hey, Hanako, do you understand this~?"

        "Misha looks to Hanako, but I suspect her hope is more to find a comrade in ignorance rather than genuine help."

        show hanako emb_downtimid_close
        with charachange

        ha "I-I… um… n-not really… I g-guess…"

        "I'm surprised by how tense she is in answering, but she settles back down. She breathes out, and the way her upper body and head lower reminds me of a deflating balloon."

        hi "You okay? I could go over this bit if you want."

        "Hanako shakes her head slightly, but then again, I don't think she needs the extra explanation despite what she said. Misha quickly interjects, entirely oblivious, and I end up slowly going through how we ended up at one of our results, step by step."

        "Times like this remind me that this kind of work may not be mechanical for everyone, but rather feels that way to me due to my grasp of the subject. It's a satisfying feeling."

        "As Misha brings her balled fist onto an open hand in realization, I discover another nice feeling. My explanation got through to her, and she manages to work out the next equation by herself with a minimum of guidance."

        "Throughout all of this, Hanako is unusually unresponsive."

        "She's normally very quiet, but one can still see her eyes roving periodically over the landscape of the classroom in front of her, or anxiously moving her hands in some way, or shifting her shoulders periodically."

        "Right now, these small movements that I've gotten used to seeing are all missing. Someone not moving at all is definitely weird. Even Misha can tell there's something wrong."

        show misha perky_confused_close
        with charachange

        mi "Hanako? Are you sure you're okay?"

        ha "Y-yes…"

        hi "Are you sure?"

        show hanako emb_downsad_close
        with charachange

        ha "I'm fine."

        "A little more strongly, this time, but she turns away as she says it. It only makes me doubt her answer, yet at the same time, I can tell she doesn't want to talk about it further."

        "Having already had one very awkward conversation today that I'm still not fully over, I don't want to pursue the matter too much either."

        "We settle back into our routine, debating over our answers whenever a doubt comes up, but as time goes on I notice that Hanako isn't talking at all. It's frustrating; she had made so much progress."

        "It makes me a little angry at Shizune and Misha for undoing the surprise Lilly had wanted to keep secret so much. I know I'm at fault, too. Maybe I could have kept it under wraps somehow."

        show shizu behind_frustrated_close:
            xpos 0.85
        with charachangealways

        "Shizune has noticed Hanako's silence as well, and is also getting antsy. I can see it on her face. It's strange that even though she's deaf, Shizune has perceived Hanako's unusual quietness sooner than Misha."

        show shizu adjust_frown_close
        with charachange

        shi "…"

        show misha sign_smile_close
        with charachange

        mi "Hanako, you're being too quiet~. You have to contribute, too~! Someday, we might work on a bigger project, like one that's so big it's worth celebrating afterwards, like with ice cream, or cake. If you act like this, we won't take you along~!"

        "I can tell that they're trying to tease her to bring her out of her shell, but I don't think that that kind of approach will work on Hanako. It will just make her feel worse."

        hi "Guys, don't tease her like that."

        show shizu behind_smile_close
        with charachange

        shi "…"

        show misha hips_smile_close
        with charachange

        mi "Hicchan, it's all in good fun~! Shicchan says she teases everyone, anyway."

        show misha perky_smile_close
        show shizu behind_blank_close
        with charachange

        "They do back off, though, with Misha moving away from the issue by asking me a question again. On seeing how difficult the problem she is working on is, I don't know whether it was a skillful dodge, or mere coincidence."

        "It takes way more of our time than necessary, because Shizune keeps disagreeing with me while I'm trying to explain it to Misha, and Misha is quick to believe her over me. So quick, in fact, that she forgets to translate what Shizune is saying."

        hi "Hey, the clock is kind of ticking down. We should speed up a little."

        stop music fadeout 4.0

        show misha perky_confused_close
        with charachange

        mi "Hicchan~! You sound a little like Shicchan, there…"

        hi "Just because I looked at my watch? Jeez, is that really all it takes? Time management, and suddenly I'm the Student Council president?"

        stop ambient fadeout 4.0

        scene evbg hanako_breakdown:
            truecenter
            1.0
            zoom 1.05
            easein 8.0 zoom 1.0
        show evfg hanako_breakdown_down:
            truecenter
            1.0
            zoom 1.1
            easein 8.0 zoom 1.0
        with silentwhiteout

        play music music_tragic fadein 8.0

        "I look at Hanako's desk to see how she's doing, and freeze. Our papers are covered in equations, but Hanako's only halfway there. It seems like she hasn't written anything in the past twenty minutes."

        "When I realize that, I want to kick myself for how dumb I've been."

        "I should have known that someone as fragile as Hanako wasn't just going to brush off what happened so easily, but I've been too eager to move on from an awkward situation to notice."

        "She has been slowly shutting down for the last half hour, and I had no clue. Her pen is still in her hand, but she doesn't slowly spin it around like she usually does. There isn't a single idle movement from Hanako."

        scene evbg hanako_breakdown:
            truecenter
        show evfg hanako_breakdown_up:
            truecenter
        with charachangeev

        "Only the fact that she tries to inch away once she feels Shizune, Misha and me looking at her tells me that she is even still conscious. We look away, and at least in my case, it's partly out of shame that it's gotten to this point."

        "Though on the outside she has shut down almost completely, I know that it's a different story on the inside."

        "What kinds of things could she be thinking about as she tries harder and harder to shrink into herself, as if by willing it she could somehow disappear?"

        "Everyone is looking at her, now, stealing quick glances inbetween putting the finishing touches on their work."

        "Misha attempts to ask her what's wrong, but that only makes the problem worse. If she weren't frozen to her seat, she would probably run out of the room right now."

        show evfg hanako_breakdown_closed
        with charachangeev

        "Misha's questions are loud enough to be heard throughout the entire classroom, and for a second I'm ready to snap at her, because I can only imagine how much worse it's making Hanako feel."

        "Of course, if I were to do that, it would only make the situation worse."

        "I'd believed that Hanako had gotten stronger, and she has, but it wasn't enough, and I was too eager to believe it. Now, she's terrified, alone in the middle of the classroom, and there's nothing I can do without drawing more attention to her."

        "It's infuriating. Misha's worried, and even Shizune is biting her lip."

        "None of us know how to deal with this situation, so I decide to call Mutou. His judgment would probably be better than ours."

        "I look up and manage to catch his eye, silently motioning for him to come over. I want to make as little a fuss about this as possible, since if there's anything that would make this worse, it's more attention being focused on her."

        "I know that Hanako can see everyone staring at our group. Specifically, at her. Because they know that if there's a problem, it has to be her."

        "Everyone knows her, and it's the first thing anyone's mind would leap to. Her reputation for being a truant has marked her as an unusual person, even in unusual Yamaku."

        "Who knows how many times they have stared at her before. Maybe it's because she's seen the class staring at her so much that she fears their gazes like she does, cowering from them."

        "The time it takes Mutou to walk over must be like an eternity to Hanako, and she looks as if she is about to fall over."

        scene bg school_scienceroom
        show shizu behind_blank_close:
            tworight
            xpos 0.85 ypos 1.09
        show misha perky_sad_close:
            twoleft
            xpos 0.15 ypos 1.09
        show hanako emb_downtimid_close:
            center
            ypos 1.09
        show muto irritated behind shizu at tworight
        with dissolve

        "Mutou quietly begins to ask us what's wrong, before catching himself as he sees Hanako."

        show misha perky_sad_close
        with charachange

        mi "Did… did we upset her…?"

        show muto normal
        with charachange

        mu "Don't worry."

        "Mutou bends down after calming Misha and looks intently at Hanako's face."

        show muto smile
        with charachange

        mu "Hi, Ikezawa. Can I help you at all?"

        "His voice is hushed and gentle. Everyone's acting so differently around Hanako now that the whole class has noticed something's wrong with her."

        show muto smile_close
        with characlose

        "Hanako doesn't respond, so Mutou gently rests a hand on her shoulder."

        show hanako emb_downsad_close:
            function partial(tremble_general, 1.0, 0.5, 1.09, 0.5, 1.0)
        with charachangealways

        "She starts shaking at his touch, but won't even look up. Hanako continues to stare into the equations on her desk, vision so unfocused that I doubt she even sees them."

        "She is worse than before. I remember that not even an hour ago, she was able to talk to him almost normally."

        show muto irritated
        show hanako:
            center
            ypos 1.09
        with charadistant

        "Mutou grimaces a bit as he stands again, and now that his expression's changed, I can see he wasn't exactly unaffected by what happened either."

        show muto normal
        with charachange

        "He takes a breath to settle himself before speaking in a very quiet voice. I'm a little impressed at how quickly he takes control of the situation."

        mu "Is that it? Nothing's wrong, then?"

        play ambient sfx_crowd_indoors fadein 8.0

        "Mutou seems to say that to no one in particular. However, his words sound convincing enough that most of the people who were looking over at Hanako now turn away, getting back to their work."

        "He gives a quick glance to his left and right. Several people at the desks around us are still staring curiously, but other than that, we seem to have escaped attracting too much attention."

        show muto smile
        with charachange

        "Mutou notices me doing the same as him and smiles a little, in his usual stilted way."

        mu "I think, for Ikezawa's sake, that it would be good to quickly take her somewhere away from others."

        mu "Nakai, Hakamichi; could you please take Ikezawa out of the classroom? I'll keep everyone settled, so please don't worry about anything but her, okay?"

        show misha sign_confused_close
        show shizu behind_blank_close
        with charachange

        "He looks at Misha to tell her to interpret his words for Shizune, but she's already finishing her translation by the time he does so. It's remarkable how little thought she needs to sign, as she still looks quite dazed otherwise."

        show muto:
            ease 1.0 alpha 0.0
        show shizu behind hanako:
            ease 1.0 tworight xpos 0.85 ypos 1.0
        with None

        show misha perky_confused_close
        with charamovechangefaster

        hide muto
        show shizu:
            tworight
            xpos 0.85

        "Nodding, Shizune and I stand and move to either side of Hanako. Mutou steps back to allow us some room, and talks to the table behind us as some people there have begun to mutter between themselves about what's going on."

        show hanako emb_downsad_close at center
        with charamove

        "We look at each other before lowering ourselves in unison, taking one arm around each of our shoulders and lifting."

        show misha:
            ease 1.0 xpos -0.1 alpha 0.0
        with None

        show hanako:
            twoleft
            xpos 0.35
        show shizu at tworight
        show bg at bgleft
        with charamovefaster

        hide misha

        "The two of us begin to walk, at a slow pace to make sure we don't inadvertently hurt her. As much as we try to make this look normal, I'm quite sure there would be many more gazes on us if not for Mutou's distraction."

        "Eventually, thankfully, we reach the door and go through."

        stop ambient fadeout 0.5

        scene bg school_hallway3
        with locationchange

        "Nobody's outside, so we walk down the hallway. It doesn't seem like it's making her more at ease than she was in the classroom. Finally, I ask if she wants to just sit down."

        show shizu adjust_happy_close at tworight
        show hanako emb_downsad_close:
            twoleft
            xpos 0.35
        with charaenter

        "For a while, we simply stay in place and wait for her to say something. Shizune tentatively rubs Hanako's shoulder a little, but there's no response."

        show shizu behind_smile_close
        with charachange

        "Eventually, she shakes her head a little when Shizune tries again. Both of us are looking at her, so we pick up on it immediately."

        show shizu adjust_happy_close
        show hanako emb_sad_close
        with charachange

        "Shizune's hand again comes to rest on Hanako's shoulder as she awakens, her face lifting to two very worried and anxious people looking at her."

        "She looks at us silently for a while. I'm initially worried she might freak out or do something extreme, but those fears prove unwarranted as her expression slowly changes from an almost lifeless blank state to a more normal withdrawn shyness."

        show hanako emb_downtimid_close
        with charachange

        "She wordlessly lowers her head, her eyes evasively moving to the side. She looks embarrassed, almost ashamed."

        "I want to say something, anything, to help. I can't, though. I don't really know what just happened, or even what caused it. I feel helpless, and ashamed of myself for not being of any use."

        show shizu basic_normal2_close
        with charachange

        "Shizune sighs before looking at me. Even without words, I think I can tell what she's asking."

        hi "I'll take Hanako to the nurse. Is that okay by you?"

        "I try to communicate my intentions through hand gestures, but I don't feel like I manage to get through to her very well."

        show shizu behind_frustrated_close
        with charachange

        "Shizune makes a dreary face in response to my gesticulations, confirming my impression."

        show shizu adjust_frown_close
        with charachange

        "She stabs her finger in the air decisively, first at me, then at Hanako, and then towards the stairs. She waits for me to nod before pointing at herself, then pointing at the door to the classroom."

        "I get the feeling Shizune is much better at this than I am."

        show shizu behind_blank_close
        with charachange

        "I nod at her, since her plan is after all the same as mine. Shizune gets ready to make her exit, but she only leaves after looking at Hanako for quite some time."

        hide shizu
        with charaexit

        hi "Are you okay with me taking you to the nurse's office?"

        stop music fadeout 4.0

        "Hanako doesn't say anything or nod, but she stands up in place by herself, and when I begin to walk, she obediently follows. I've read about people being catatonic before, but I think this time I'm seeing it for myself."

        "She looks extremely tired. After everything that's happened, it's not a surprise."

        stop music fadeout 1.0
        scene bg school_nurseoffice
        with locationskip

        "After Hanako silently takes off her shoes and lies on the bed in the infirmary, the nurse and I take our leave."

        play music music_hanako fadein 0.3

        "He shuts the curtain behind us. We both take a seat, and I quietly and thoroughly go through everything that happened, in quite some detail."

        "I want to understand what happened, and the nurse has as good a chance as anyone of knowing."

        show nurse concern at center
        with charaenter

        "He nods throughout my explanation, his face looking troubled as I finish."

        nk "It must have been very troubling for you to have seen all this."

        hi "I'd be lying if I said it wasn't. I get that she fainted, but I don't really understand anything about why it happened or why she's acting like this."

        "He nods, but his face is clouded."

        hi "You don't know either?"

        nk "Well… yes and no. It's complicated."

        nk "I assume you've heard about the concept of patient confidentiality at some point?"

        nk "This is a bit of a minefield in that respect. I'm going to put this pretty bluntly; this is a matter for Ikezawa, me, and her therapist."

        "I move to protest, but think better of it. I want to deny what he says, but if I think this through rationally, what he says makes perfect sense."

        hi "I understand."

        show nurse neutral
        with charachange

        nk "Good, good. I wish I could help you more, but I think what Ikezawa needs right now isn't somebody prying into her past or her emotions. She just needs somebody to be there for her."

        nk "She needs a friend."

        show nurse fabulous
        with charachange

        nk "For what it's worth, I think you've done well in bringing her here. Sounds like you and your friends dealt with the situation well, too."

        show nurse grin
        with charachange

        nk "I'd give you a lollipop or a sticker as a reward, but you might be a little too old for either."

        "He gives a cocky grin, obviously trying his best to lighten the atmosphere. I'm not really in a laughing mood, but he does manage to get a smile out of me."

        hi "Thanks. Um, do you mind if I stay here with Hanako?"

        show nurse neutral
        with charachange

        nk "I appreciate the thought, but I think it would be better to let her rest for now."

        nk "She'll be let back to her dormitory room this evening, so you could visit her then."

        "I agree with him before standing. It feels like all I can ever do around the nurse is humbly agree to what he says, but it was the same with the doctors in the hospital, too."

        stop music fadeout 3.0

        scene bg school_nursehall
        with locationchange

        "The walk back to the classroom is a long one, my mind feeling heavy under the weight of so many things happening so suddenly."

        scene bg school_scienceroom
        with locationskip

        play music music_dreamy fadein 2.0
        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
        play ambient sfx_crowd_indoors fadein 2.0

        "Even as I reenter the classroom, I'm thinking about Hanako."

        "My stomach feels like it's turning into knots while I think about how to deal with her. I still don't know what I'm going to say when I see her again."

        "Thankfully, the class doesn't pay me much heed. There are a couple of questioning glances, but overall not many people seem to be very aware of what happened."

        "Mutou raises his eyebrows to get my attention when I pass by his desk."

        show muto normal at center
        with charaenter

        mu "Nakai… I take it Ikezawa is in the infirmary now?"

        hi "Yeah. I took her there, and the nurse said I should let her rest."

        "Mutou nods, assuring me that I made the right call. He scratches his chin for a second before rising from his desk."

        show muto smile
        with charachange

        mu "Everyone, I want you to continue with the exercise. Nakai, I'll see you in the hallway, please."

        "His speech is hushed, but overall he doesn't seem to be acting too differently from how he usually does. Being a teacher, maybe it's to be expected."

        stop ambient fadeout 1.0
        scene bg school_hallway3
        with locationchange

        "As we go out into the hallway, I notice him taking a quick glance left and right to check if there are any students milling around."

        "The hallway is nearly soundless, but I can't think of anything except waiting for Mutou to speak."

        show muto smile at center
        with charaenter

        mu "Nakai, what do you think the purpose of this school is?"

        hi "Umm… to cater to the needs of disabled students?"

        show muto normal
        with charachange

        "Mutou scratches his head as he shakes it."

        mu "No. If we wanted to do that we would have built a whole new school from scratch. One floor. Talking whiteboards. That kind of thing."

        mu "Look around, Nakai. This school is about giving you all a future that you would have been denied in regular education."

        hi "Huh?"

        mu "Think of it this way. If we wanted you to graduate and go straight into a hospital, do you think we'd put in this much effort?"

        "The bluntness of Mutou's statement temporarily stuns me, causing me to forget about the immediate situation."

        hi "No…"

        mu "That's right. We want you all to leave here as useful members of society."

        hi "I'm… not quite sure I'm following you…"

        show muto smile
        with charachange

        mu "I have high hopes for you, Nakai. You are possibly the first student I've had that gets my lectures."

        "That isn't something that a teacher should be admitting so freely."

        mu "You could easily take your studies of science well into university. Have you ever considered that?"

        hi "I can't say I have."

        mu "Well, what have you considered? For your future, that is…"

        hi "I… can't say that I've put much thought into my future."

        "For a moment I'm distinctly reminded of Lilly questioning me about the same subject."

        "It's only been a little over five months since I was gasping for air on the ground. It's too soon to be thinking about the future, and besides, Hanako's problems seem much bigger to me right now."

        show muto irritated
        with charachange

        "Mutou gives a disapproving sigh before continuing."

        show muto normal
        with charachange

        mu "Think of this place as an opportunity. Here you have boundless facilities, good teachers, plus the added bonus of the nurse and his staff."

        mu "You should be doing nothing but thinking of the future."

        hi "Er… right."

        "As I raise my head to meet his gaze, a thought occurs to me; it's almost like Mutou totally side-stepped the issue at hand."

        hi "Excuse me, but why do none of the staff seem to care when Hanako skips class?"

        hi "I've seen you watch her walk out of class more than once. Shouldn't you at least say something?"

        show muto smile
        with charachange

        mu "Well, Nakai, it's not really that simple. Every student here has special needs; if it weren't for that then we wouldn't have a school here."

        mu "For example, I wouldn't keep you in class if you were having trouble breathing, would I?"

        hi "But that's not…"

        "Mutou cuts me off before I can even think about finishing my sentence."

        show muto normal
        with charachange

        mu "Ikezawa's case is very much like that. But instead of CPR or a pacemaker, what she needs is time and space."

        mu "The faculty was made aware of this from the day she arrived here, thus whenever she feels the need to leave classes, we let her do so."

        show muto smile
        with charachange

        mu "And even though she isn't a star pupil, she seems to pass all of her exams, so it hasn't affected her ability to study. Isn't that enough?"

        "I open my mouth to protest, but I can't find a fault in his argument. While her condition does at first seem to be wholly physiological, its worst effects have been on her psyche."

        "It still puts me off, though. Isn't he just passing on the responsibility for her problem? Surely she can't go like this for her entire life."

        show muto normal
        with charachange

        mu "I understand that you might not be used to this kind of thing yet. It's been a big change for you. That said, it's less than a year until graduation now."

        mu "Maybe you won't have to get used to this school. If you keep your head down, I'm sure you'll do well enough in your exams."

        "I numbly nod, more to simply acknowledge that I'm listening than out of agreement. I felt like I was getting used to this school, but it feels like it's just been thrown back in my face."

        hi "But… what about Hanako?"

        mu "I believe… well, I hope, that she will perform well enough to do what she wants to do."

        mu "What that is, I don't know. Not all students leave school with an idea of what they want to do, unfortunately."

        "He takes care to emphasize the last word, as if it wasn't quite clear enough already, and gives me a moment to mull his words over."

        show muto smile
        with charachange

        mu "Today's been a troublesome day for you, and I doubt you'd be able to concentrate much anyway after all that's happened, so I'll allow you to take the rest of the day off."

        mu "Your grades have been good in this class so far, which makes me think you won't have any trouble catching up on what we've been doing."

        "He gives a small smile along with his praise, as if to make up for the seriousness of his lecturing before now."

        mu "Go collect your things, and I'll see you tomorrow."

        hi "Right. Thank you."

        stop music fadeout 5.0

        hide muto
        with charaexit

        "Mutou's round-about speech has left my thoughts scattered. I'm still not any closer to working out what I can do to help Hanako, if anything, and my mind is all the more confused after what Mutou's said."

        "I'm also still bothered by the fact that Hanako was helped at least as much by Shizune, her enemy-by-proxy, as by myself, but I don't know whether that is just male bravado or a genuine concern."

        scene bg school_scienceroom
        with locationchange

        "While I collect Hanako's and my things from the class, I continue to try and sort out my feelings."

        "I want to say that I understand her, and that I'm there for her… but while I might have been able to say that just yesterday, I can't say it now."

        "I wish I could."

        if _in_replay:
            return

    label .treading_softly:
        scene bg school_dormhisao_ss
        with shorttimeskip

        play music music_night fadein 1.0

        "I lay on my bed, trying to collect my thoughts."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=60}After Hanako's panic attack, I've found myself fundamentally reassessing the relationship we share, and what I know about her."

        n "I had a hard enough time dealing with four months in the hospital. One look at her scars tells me that she was in one for a lot longer than I was."

        n "Be that as it may, I know next to nothing about her past. She has told me about the house fire, but only in the most basic way."

        n "And what of her family? I still haven't asked Lilly about them; there hasn't been a good opportunity to bring it up."

        n "I don't know where she grew up, or what her old school was like. Nor of her past friends, her wishes and ambitions. Not even her tastes in music, food and movies… all the little things that I knew about all of my old friends."

        n "{vspace=60}Just what have I been doing, for all this time I've been with her and Lilly?"

        $ renpy.music.set_volume(1.0, 1.0, channel="music")
        $ renpy.music.set_volume(0.1, 0.0, channel="sound")
        play sound sfx_normalbell

        nvl clear
        nvl hide dissolve

        "In the distance, I hear the bells signaling the end of classes. With any luck, Lilly will soon realize that neither Hanako nor I are around, and return to the dormitories."

        $ renpy.music.set_volume(0.5, 0.0, channel="sound")
        stop music fadeout 0.5
        play sound sfx_phone

        "My mobile phone starts to ring, cutting my thinking short. It quite startles me, as I've rarely been called since coming to Yamaku."

        scene bg school_dormhisao_blurred_ss
        show phone mobile:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0
        with locationchange

        pause 0.5

        hi "Hello, Hisao Nakai speaking…"

        li "Oh, Hisao, I'm glad I found you. You weren't at any of our usual places, so I thought this would be the fastest way to contact you."

        "I probably should have guessed it would be Lilly, as she's one of the few people I've given my number to. Even through the phone, her voice sounds slightly on edge."

        hi "I… Hanako and I left class early. She had some kind of panic attack…"

        "The line goes silent. If it weren't for the background static, I would have thought Lilly had hung up on me."

        li "I understand. Could you come by my room? I'd like to talk with you."

        hi "Sure. I'd… I'd appreciate the chance to have a bit of a talk, actually."

        li "Good… good. I… also have some bad news. I think we should discuss this in person."

        "It's hard to grasp the seriousness of the situation from Lilly's tone. She sounds so calm most of the time, but that could be a good or a bad thing, depending on how you look at it."

        hi "Okay, I'll be right there."

        show phone:
            easeout 1.0 ypos 0.7 alpha 0.0
        with None

        scene bg school_dormhisao_ss
        show phone mobile:
            truecenter
            easeout 1.0 ypos 0.7 alpha 0.0
        with locationchange

        pause 0.5

        hide phone

        "I collect Hanako's school things from my desk and head straight for Lilly's room."

        scene bg school_girlsdormhall
        with locationskip

        $ renpy.music.set_volume(1.0, 0.0, channel="sound")
        play sound sfx_doorknock2

        "I rap my knuckles on her door, and she soon calls me in."

        play music music_drama fadein 4.0

        scene bg school_dormlilly
        show lilly basic_sleepy:
            center
            ypos 1.17
        with locationchange

        "Lilly sits at the table inside her room, looking a little worse for wear; I guess that's because of the bad news."

        "Following her gesture of invitation, I sit across from her and lay Hanako's things on the table."

        show lilly basic_weaksmile
        with charachange

        li "Well, there's no point in either of us waiting. Would you mind going first, Hisao? What happened today?"

        "My memory of the incident is already beginning to fade, but I explain it as best I can to Lilly."

        "Inviting Hanako to work with the group, Shizune and Misha's questioning, our foray to town getting discovered, and the subsequent panic attack."

        "I add Shizune's reaction almost as an afterthought, but Lilly seems to take some kind of comfort in hearing about it."

        "I guess rivals don't become rivals for no reason. There must be some history there, but now isn't the time to explore it."

        show lilly basic_concerned
        with charachange

        li "I see. She had said her therapist sessions were helping, but I had my doubts. It's quite a shame."

        show lilly basic_reminisce
        with charachange

        li "Her birthday has caused problems before, but I had hoped that she would have improved with you around, and the more intensive therapy."

        show lilly basic_oops
        with charachange

        li "Where is Hanako now?"

        hi "Last time I saw her she was in the infirmary. I guess she's gone back to her room by now."

        show lilly basic_sleepy
        with charachange

        li "She wasn't in the library or the tea room when I checked, so I can only assume that too."

        hi "You said you also had some bad news… what's the matter? Does it concern Hanako?"

        "Lilly shifts her position; the body's way of saying she's searching for the right words."

        show lilly basic_concerned
        with charachange

        li "My aunt has fallen gravely ill. I'm afraid I'm going to be heading back to Scotland to visit her, and to spend some time with my family."

        hi "What? Is she all right? When do you leave?"

        show lilly basic_reminisce
        with charachange

        li "I'm not altogether sure of exactly how she's faring at the moment, though last I heard she was stable. I'll be leaving Saturday; it's the earliest flight that I could get."

        "'Stable.' That's code for 'needs to stay in the hospital.' I've been 'stable' long enough to know that, and to know that it doesn't necessarily mean someone is in good condition, but merely treading water."

        "On the upside, 'stable' is much better than 'critical condition.' At least she's not on the brink of death."

        hi "Stable… that's a relief."

        show lilly basic_sad
        with charachange

        li "Yes, but this means that I won't be here for Hanako's birthday."

        show lilly basic_concerned
        with charachange

        li "I wanted to tell you now so we could think of something before we told Hanako, but after today's events, I'm not even sure if there's going to be an issue if we simply cancel the party."

        hi "I… don't think that is such a good idea. Hanako already knows that we were planning a party now; to go back on that seems like the wrong thing to do."

        hi "Also, we should do something for your going away, right?"

        show lilly basic_weaksmile
        with charachange

        li "You make it sound as if I won't be coming back. If all goes well, I should only be away for a week, though possibly two."

        hi "That's one relief, at least."

        show lilly basic_oops
        with charachange

        li "With that in mind, what do you suggest then?"

        hi "Given the circumstances, I don't think karaoke is really appropriate. You're not going away for the greatest of reasons, so having too much fun would feel wrong."

        hi "What did you do for her birthday last year?"

        show lilly basic_reminisce
        with charachange

        li "Last year… I literally couldn't get her out of her room. She'd locked the door."

        li "All I could do was leave food outside for her, making sure that she was at least eating well."

        "This is perhaps the most depressed I've ever seen and heard Lilly act. I feel sorry for her, given how defeated she must feel to be unable to help her closest friend."

        hi "Perhaps it would be better to throw the party before you leave, then?"

        show lilly basic_weaksmile
        with charachange

        li "That does sound like it would be the easiest option."

        hi "I think we should at least tell Hanako, both about your trip and her party. I have her things from class as well."

        show lilly basic_smile at center
        with charamovechangefaster

        li "That's a good point. Should we go and visit her now?"

        hi "I… I think that would be a good idea."

        "Part of me is dying to see Hanako. The last time I saw her she looked like death walking, and these last few hours have torn me apart just thinking about that."

        stop music fadeout 4.0

        scene bg school_girlsdormhall
        with locationchange

        "We quietly get up and file out of Lilly's room. Hanako's room is next door in the same hallway."

        play sound sfx_doorknock2

        "Knocking lightly gets us no response, but the door proves to be unlocked. Lilly pauses for a moment as the handle unexpectedly moves under her hand, before opening the door."

        play music music_moonlight fadein 0.5

        scene bg school_dormhanako_ni:
            xalign 0.0
            warp acdc_warp 8.0 xalign 1.0
        with locationchange

        "Hanako's room is startlingly bare and monotone. There are no decorations on the plain white walls, a plain dark blue blanket, and only a few books, papers, and purely utilitarian items on the shelves."

        "Even her bedsheets are monochrome. The entire room feels as subdued as Hanako's character."

        scene ev hanako_cry_closed
        with whiteout

        "Hanako herself is laying curled up on her bed. She may not be crying now, but her eyes are closed tightly to stop herself, and the tracks left by her tears still sit on her reddened cheeks."

        "I quietly walk in and set her bag down on her desk, afraid of startling her too much."

        li "Hello, Hanako. Hisao told me about what happened today… are you all right?"

        show ev hanako_cry_away
        with charachangeev

        "Hanako's eyes open, though only a little."

        ha "I… I'm okay…"

        show ev hanako_cry_open
        with charachangeev

        "She tilts her head slightly to look at me, noticing my grimacing before I can hide it."

        ha "S-sorry… f-for making you w-worry."

        show ev hanako_cry_closed
        with charachangeev

        ha "R-really… I'm f-fine now…"

        "She really doesn't look nor sound okay, though at least she seems more calm than she was before. She still looks as if the slightest breath could emotionally break her."

        hi "I said it before, right? You don't need to be sorry for this."

        li "Hisao's right. We… I… shouldn't have hidden something like a birthday celebration from you."

        "I see Hanako shiver at the word. Lilly picks up on the silence that follows, and crouches down to Hanako's level."

        li "I'm the one who should be sorry, Hanako."

        show ev hanako_cry_away
        with charachangeev

        "Hanako's eyes open to peer at Lilly. She looks at Lilly for some time, taking in her face with those dark, analytical eyes of hers."

        play sound sfx_rustling

        scene bg school_dormhanako_ni
        show hanako emb_downsad_ni:
            center
            ypos 1.3
            easein 1.0 ypos 1.15
        with locationchange

        "Lilly must have made the right impression on her, as Hanako recovers enough to prop herself up on the bed and shift to sitting on its side. Hanako worries about many things, but troubling others is foremost among them."

        show bg at bgright
        show hanako:
            xpos 0.6
            ypos 1.15
        with charamove

        show lilly basic_weaksmile_ni:
            twoleft
            xpos 0.4
            ease 1.0 ypos 1.17
        with Dissolve(1.0)

        show lilly:
            twoleft
            xpos 0.4 ypos 1.17

        "Hearing Hanako's shuffling, Lilly moves forward and feels out the side of the bed, eventually taking a seat beside her and taking Hanako's left hand in both of hers."

        "The feeling of me being out of place when the two are together has lessened in the time that we've known each other, but it's still occasionally very much there. This is one of those times, I think."

        hi "Lilly, if you want me to go…"

        show hanako emb_sad_ni
        with charachange

        ha "I don't… want that…"

        show lilly basic_surprised_ni
        with charachange

        "Lilly and I are both surprised at Hanako mustering her courage. A half-mumbled 'Okay' is all I can give her in reply, and I take her desk chair to sit in."

        show lilly basic_concerned_ni
        with charachange

        li "Hanako, I'm afraid I have some bad news."

        "So Lilly's going to break the news now. With Hanako having affirmed our relationship so clearly, perhaps Lilly thought the timing was good, or at least, as good as it will ever be."

        show lilly basic_sad_ni
        with charachange

        li "My aunt has fallen ill, so I need to return to my family for a time."

        show hanako cover_worry_ni
        with charachange

        "Concern replaces Hanako's remorseful expression."

        ha "Your… family… You mean in Scotland, right?"

        show lilly basic_reminisce_ni
        with charachange

        li "That's right. Akira and I will be leaving Saturday."

        show hanako defarms_strain_ni
        with charachange

        ha "S-so you're going away?"

        show lilly basic_weaksmile_ni
        with charachange

        li "I won't be gone for long. Probably only a week or two. I'll be back before you know it, and Hisao will be here, right?"

        hi "That's right, I'm not going anywhere."

        show hanako basic_worry_ni
        with charachange

        "Hanako seems to take only minor comfort in this, but she does manage to summon some resolve from somewhere inside her."

        ha "I-is your aunt going to be all right?"

        show lilly basic_reminisce_ni
        with charachange

        li "I'm not sure."

        "Silence falls. It's depressing that the thing to truly bring Hanako out of her rut is another's misfortune."

        "I decide to bring up the other matter that brought us here, to distract at least in part from the dismal feeling permeating the room."

        hi "Anyway, we were thinking that it would be a good idea to have a going-away party for Lilly, and it could double as… yeah…"

        "I cut myself off before mentioning her birthday, as that seems to be a trigger for such fierce emotions within her."

        "Lilly gives Hanako's hand a gentle squeeze."

        show lilly basic_weaksmile_ni
        with charachange

        li "Is it all right by you, Hanako? It won't be anything lavish or overdone, just something small in my room."

        show hanako def_worry_ni
        with charachange

        ha "S-so just in the school? Just us?"

        show lilly basic_smileclosed_ni
        with charachange

        li "That's right, just the three of us. If you like, I could ask Akira to come as well."

        show hanako basic_normal_ni
        with charachange

        ha "O…kay. Y-you're only going for a week?"

        show lilly basic_smile_ni
        with charachange

        li "One week or two, yes. I promise you it won't be any longer."

        show hanako cover_distant_ni
        with charachange

        ha "O-okay…"

        "Most people would be upset at hearing about a friend's family member falling ill and happy at having a party, but with Hanako it seems that both events are on the same level."

        hi "All right then. You look like you need a rest, Hanako, so it might be best if we all went back to our rooms for now."

        show lilly basic_weaksmile_ni
        with charachange

        li "You know that if you ever want anything, you can always talk to me or Hisao, right?"

        "Lilly's voice is pensive, an unusual edge for someone as confident in herself as she."

        show hanako basic_bashful_ni
        with charachange

        ha "I… understand. Thank you, Lilly, Hisao."

        show lilly basic_smileclosed_ni:
            twoleft
            xpos 0.4
        with charamovechangefaster

        li "Well then, good night, Hanako."

        show hanako basic_normal_ni
        with charachange

        ha "'Night…"

        stop music fadeout 4.0

        scene bg school_girlsdormhall
        with locationchange

        "I let out a long breath after the door closes behind us. It feels a little like I've been deep underwater, and only now have been able to come up for air."

        show lilly basic_concerned at center
        with charaenter

        "Lilly doesn't seem to be doing well either. She looks pale and drawn."

        hi "Are you all right?"

        li "I'm just a little tired. It's been… hectic recently."

        hi "Have you slept at all? 'A little tired' sounds like an understatement, given how you look."

        show lilly basic_sleepy
        with charachange

        li "I think I managed to get a couple hours of sleep before class. I'll be okay."

        "I feel bad about pressing Lilly right now. I think both of us are pretty tired from everything that's happened as well."

        hi "I think you should get some rest. It's been a big day, and staying up isn't good for your complexion."

        show lilly basic_weaksmile
        with charachange

        li "Thank you for your concern, Hisao. Good night, then."

        hi "Okay. 'Night, Lilly."

        hide lilly
        with charaexit

        "I leave Lilly in the hallway as she opens the door to her room, and begin to make my way to my own."

        scene ev hanako_cry_closed_fb
        show noiseoverlay
        with flash

        "As I walk down the quiet hallway, I can't get that image of Hanako out of my mind. Huddled and pitiable, lying helpless with tears on her cheeks. I began to think that she was just a normal, if extremely shy, person, but her problems run much deeper."

        "Trying to take our relationship further than what we share now, when she's so fragile and vulnerable, wouldn't be right. I don't need to be more than her friend in order to protect her, to try and stop anything like this ever happening again."

        "The possibility of my feelings for her going beyond that… that doesn't matter any more. Hanako is precious to me, and that's why I can't take advantage of her."

        "But even so… there's still that sting I feel when I think that way."

        scene bg school_girlsdormhall
        with flash

        "For now, I need to sleep. Tomorrow, hopefully, will be a better day."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .reaching_out:
        scene bg school_scienceroom
        with locationchange

        "Hanako is more noticeable in her absence than when she is in the room."

        "I feel her empty desk calling out for me. I find myself peering over my shoulder endlessly, hoping that I'm hallucinating and that Hanako will magically appear."

        "She makes sure she's as small a presence as possible when she attends class, and although she had been getting better recently, that fact never changed."

        "Nobody ever pays her any heed in class, and now that she's not here, they don't notice her absence. It's as if she just never existed."

        "Lilly did say that her skipping class wasn't an unusual thing before I met her, but it's still very off-putting."

        play sound sfx_normalbell

        "The bells heralding the end of school make me jump in my seat. It's only now that I notice Misha is prodding me in the side with her mechanical pencil to get my attention."

        show shizu behind_blank:
            center xpos 0.4 alpha 0.0
            ease 1.0 center alpha 1.0
        show misha sign_smile_close:
            center xpos 0.1 alpha 0.0
            ease 1.0 xpos 0.2 alpha 1.0
        with None

        show bg at bgright
        with charamovefaster

        show shizu at center
        show misha:
            center
            xpos 0.2

        play music music_normal fadein 3.0

        mi "Hello… is anybody in there~?"

        hi "Hey, stop that."

        show misha hips_grin_close
        with charachange

        mi "Ah! There we are! Welcome back to Earth, Hicchan~!"

        hi "What are you talking about?"

        show misha hips_smile_close
        with charachange

        mi "You keep on dazing off into space; I was beginning to think that you might be trying to contact alien life."

        "I really didn't get much sleep last night, so I don't doubt Misha's words. I'm not sure whether it was due to my medicines' side effects, Hanako's panic attack yesterday, my worrying about her in general, or all three."

        "I yawn tiredly before resting my chin in my palm, having been reminded of how badly I slept."

        show misha perky_confused_close
        with charachange

        mi "Hey, are you really all right? Yesterday kinda rattled me as well…"

        hi "Yeah… yeah, I guess. I wanted to speak to Hanako again, though."

        show misha perky_smile_close
        with charachange

        mi "Did you see her last night?"

        hi "Yeah, Lilly and I talked to her."

        hi "Um, this may sound a bit weird, but can you tell Shizune 'thank you?' From both me… and Lilly."

        "I know Lilly technically didn't thank Shizune, but I could tell by her reaction last night that she wanted to. At least, that's how it works out in my head."

        show shizu adjust_blush
        with charachangealways

        show shizu cross_angry
        with charachangealways

        shi "…"

        show misha sign_confused_close
        with charachange

        mi "Er… I think what Shicchan is trying to say is 'you're welcome.'"

        "The furious signing and Shizune's reddened cheeks tell me that what she said was entirely different. Her blatantly flustered expression is amusing enough to make me chuckle."

        show misha perky_confused_close
        with charachange

        mi "What's so funny, Hicchan~? Was it something we said?"

        hi "No, no, that's not it. I was simply thinking about how cute Shizune can be at times."

        show misha cross_laugh_close
        with charachange

        mi "Wahahaha~! You're right~! Shicchan is really cute when she tries not to be!"

        "I notice that Misha decides not to sign her response to Shizune. Maybe Shizune's rage is enough of a counter to any quantity of 'cute.'"

        show shizu adjust_frown
        with charachange

        "Nevertheless, Shizune quickly calms down and signs something else to Misha."

        show shizu behind_smile
        with charachange

        shi "…"

        show misha perky_smile_close
        with charachange

        mi "Oh~? Okay… Hicchan, Shicchan wants you to come and have dinner with us."

        hi "Dinner, eh?"

        "Turning away from them a bit, lest I be swayed by their pleading smiles, I begin to mull it over."

        "The invitation certainly is tempting. A takeaway dinner with two cute girls is not a bad thing, after all. The thought of Hanako locked up in her room, though, keeps dancing on the edge of my mind."

        hi "Sorry, I'll have to pass."

        show misha perky_sad_close
        with charachange

        mi "Awww…"

        show shizu behind_frown
        with charachange

        "Misha doesn't sign my response, but Shizune picks up on it easily enough and grimaces in disappointment."

        show shizu basic_normal2
        with charachange

        "She moves her arms, assumedly beginning some form of either protest or coercion, but stops herself and taps Misha's shoulder twice. Once Misha gives Shizune her attention, the only statement Shizune has on the matter is a shrug."

        show misha perky_confused_close
        with charachange

        mi "Oh well. It's your choice, Hicchan."

        hi "I promise I'll join you two another time, if that helps."

        show misha perky_smile_close
        show shizu behind_blank
        with charachange

        "Misha perks up at this, but Shizune doesn't share her reaction. With a flick of the head to signal for Misha to follow her away, Shizune simply raises her hand to silently wave me goodbye."

        hide misha
        hide shizu
        with charaexit

        stop music fadeout 3.0

        "As the two make their way out the door, I return the gesture until they're out of sight."

        "I didn't think they would be so disappointed, and it makes me feel a little bad for ditching them. Still, I have things to do."

        scene bg school_girlsdormhall at right
        with shorttimeskip

        "The girls' dormitory is especially rowdy today, with a number of girls loudly playing games and watching the television in the common room on the first floor. I can hear their voices even now, standing in front of Hanako's door."

        "It's an odd contrast to the emptiness of the floor she's on. The voices from below make the emptiness feel all the more lonely."

        "I had hopes Hanako would be in class today, especially after the talk Lilly and I had with her last night, but I feel like I shouldn't hold it against her. It was a pretty awful episode, and to have experienced it firsthand must be all the worse."

        scene bg school_dormhanako_ni
        show hanagown worry_close:
            center
            xpos 0.39
        show expression Solid("#00000022")
        show hanako_door_base at right
        show hanako_door_door at left
        with locationchange

        play sound sfx_doorknock2

        "Not knowing what state she's in, I take a small breath before giving a few sharp knocks on her brown door."

        "All I can do is stand and wait, doing my best not to feel anxious."

        "As the seconds wear on, I begin to think she might be asleep and didn't hear me knocking. The door handle rattles a little before I can raise my hand to knock again, though."

        play sound sfx_dooropen

        show hanako_door_door:
            xpos -0.05
        with charamove

        "The door opens a sliver, an eye appearing in the gap only just large enough for it to peer through. I'm sure this girl would install a peephole in her dormitory door, if only such a thing was allowed."

        "I just stand and smile at her. I don't think words would really help here, after all."

        "The act is returned in kind, with Hanako wordlessly looking at me. The gap's not wide enough to see her expression, and I can only guess what she's thinking."

        "Time passes as we look at each other, the only sound being the disembodied gaiety from the ground floor."

        hide hanagown
        with charaexit

        "I'm not sure how long it takes, but eventually the eye moves away. I keep wondering whether she'll let me in or shut me out until the door slowly begins to creak open."

        play sound sfx_door_creak

        show hanako_door_door:
            easeout 1.0 xpos -0.2
        show hanako_door_base:
            easeout 1.0 xpos 1.1
        show bg school_dormhanako_ni:
            center
            easeout 1.0 xpos 0.55

        scene bg school_dormhanako
        show hanagown normal at center
        with silentwhiteout

        play music music_comfort

        "Now that I have a full view of her and her bedroom behind, the first thing I notice is that Hanako's hair is quite damp. She's recently showered, which is made even more obvious by the scent of shampoo wafting towards me."

        "The look on her face seems one of curiosity, as if she's not really sure what to make of me. Even so, I'm not really all that sure of what she's thinking."

        "It feels as if she's gone away for a long time, and having now returned, neither of us knows what to say to the other."

        show hanagown distant
        with charachange

        "Hanako realizes she's staring, looking away awkwardly before turning to the side and gazing at her feet. I decide to take it as an invitation and step past her into the room, closing the door behind me as I do so."

        "I can see her hands fiddling in the folds of the oversized gown that hangs from her shoulders. I try to concentrate on what I want to say, but the scent from her addles my senses."

        "To my surprise, it's not me, but Hanako that breaks the silence."

        show hanagown normal
        with charachange

        ha "Why…"

        hi "Because… uh…"

        "…Why did I come here?"

        "I was worried about Hanako, so I came to her room. She let me in, as I had hoped, and then… what? What did I mean to do? What did I mean to say?"

        "Why didn't I think this through before coming here…"

        "I want to make up for what I feel I caused, at least partly. I want to try and remove the distance I feel between us since then, and to see her happy. How can I do that when I don't know the first thing about her?"

        "I wonder… I wonder if this is how Iwanako felt when she saw me lying in that sterile, pastel blue hospital bed."

        hi "I uh… I… um…"

        "A deep sigh steadies my nerves a little and ends my stammering. I don't think I've ever felt this nervous around someone before. When I'm like this, I don't think I can lie. Even if I could bring myself to, Hanako would see through it right away."

        hi "I don't know. I just… wanted to see you, I guess."

        show hanagown smile
        with charachange

        "Her fingers stop moving, giving me a little surprise. Looking up to her face, she gives a sweet smile and a nod. That was a satisfactory answer for her?"

        ha "Um… since you're here…"

        show hanagown distant_blush
        with charachange

        ha "I'd like to… play a game of chess with you…"

        "I almost hang my head in disbelief that all she wants to do, after I've been winding myself up so much, is play a game. Looking at her face though, a tentative smile perched upon it, I realize that this is more than that."

        "She could have not bothered answering the door. She could have shut it as soon as she saw my face. She could have asked me to leave."

        "She could have rejected me at many points, but she didn't. Now, with this calm face, she wants me to play the same game that we played when we first really spent time alone together."

        "A feeling of relief washes over me."

        "Everything will be all right. Hanako has let me into her world. As long as we can be together like this, I think everything will be all right."

        hi "It would be my pleasure."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .one_more_year:
        scene bg school_girlsdormhall
        with locationchange

        "The day of Hanako's birthday party is finally here."

        "To be honest, I'm looking forward to seeing Hanako and Lilly in their pajamas again. Hanako's gown has grown on me as looking rather cute, though a bit conservative, and Lilly's shorts and thin silken top are a lovely combination."

        "But the event is stained a little with the memory of Hanako's reaction to it."

        "I still don't really understand what happened, only being able to vaguely guess at the possible reasons for it, but I don't think finding the answer will be as straightforward as asking her."

        play sound sfx_doorknock2

        "With that in mind, I knock on the door next to Hanako's."

        li "Is that you, Hisao?"

        hi "Yeah, it's me."

        "I can hear the pitter-patter of footsteps coming to the door, followed by the sound of the lock snapping open. I don't think I've ever seen Lilly's door locked before, and it makes me a little suspicious."

        "Once the door opens, the sight is… a little underwhelming for a birthday party."

        play music music_ease fadein 1.0

        scene ev lilly_bedroom
        with locationchange

        "Hanako returns to her seat at the table with a quick smile and a nod, leaving me to close and, assuming they wanted it to be kept that way, lock the door."

        "As I do so, I realize that the scene before me is that of an evening tea party, just like any other between the two. Somehow, I don't think I should be surprised."

        scene ev lilly_bedroom_large:
            xpos -1900 ypos -150
        with charachangeev

        "To my relief, Hanako looks relatively calm. The break from class has probably done her good, and given her time to wind down a bit."

        scene bg school_dormlilly
        show lilly basic_smileclosed_paj:
            twoleft
            ypos 1.2
        show hanagown distant:
            tworight
            ypos 1.17
        with locationchange

        "I take a seat between the two at the low table in the center of Lilly's room, the brightly-colored teapot steaming away between us."

        "A tall brown bag close by Lilly's side catches my attention. I covertly try to glance inside it a couple of times, but can't get a good look from here."

        "Looking to Hanako, it seems like she's as curious about it as I am."

        hi "Hey, Lilly?"

        "Lilly finishes off the teacup raised to her lips before setting it down and giving me her attention."

        show lilly basic_smile_paj
        with charachange

        li "Yes?"

        hi "I was just wondering about that brown bag…"

        "She pauses for a moment, then gives a slightly cheeky smile."

        show lilly basic_cheerful_paj
        with charachange

        li "That would be Akira's present. Unfortunately, she said she was working and can't join us."

        "Lilly leans over and feels out the item inside before raising her arm."

        "I raise an eyebrow as two items, not one, rise from the bag. The glass necks are grasped by Lilly on either side of her middle finger. So this is why she had her door locked."

        show wine:
            offscreenright
            yalign 0.5
            easein 1.0 right yalign 0.5
        with Dissolve(1.0)

        show wine:
            right
            yalign 0.5

        ha "Wine…"

        "There are two small thuds as the bottles are brought to rest on the table; one red, one white. I want to believe that it's fake, non-alcoholic wine, but if it was, there wouldn't be any need to be this circumspect."

        hi "Alcohol? Seriously? Are you sure this is a good idea?"

        show lilly basic_smileclosed_paj
        with charachange

        "Lilly smiles politely and giggles. I'm not really convinced that she is."

        li "These would be the present from my sister. I know it's a bit questionable, but a little shouldn't hurt."

        "If Lilly took serious issue with it, I don't think she'd have agreed quite so easily. That aside, I had Akira squared as the serious and responsible type, maybe like an older Lilly, but it looks like I was wrong. We aren't even legally able to drink yet."

        hi "Well, in that case, I won't complain. They don't look bad, either."

        "I'm no connoisseur, but at least the bottles look nice. Apart from a surreptitious glass of wine or two given from my father at family dinners, I haven't really had enough to know what's what."

        show hanagown smile

        show wine:
            easeout 1.0 right yalign 0.5 alpha 0.0
        with Pause(1.0)

        hide wine

        "That, and I can't really say that I'm a total straight edge. Going by Hanako's expression, she's thinking the same, and it's her birthday anyway."

        show lilly basic_smile_paj
        with charachange

        li "Shall I open one?"

        hi "Sure. I'll get some—{w=0.3}{nw}"

        $ renpy.music.set_volume(0.5, 0.5, channel="music")
        $ renpy.music.set_volume(1.0, 0.0, channel="sound")
        play sound sfx_doorknock2

        show lilly basic_displeased_paj
        show hanagown worry
        with vpunch

        "My heart skips as I hear three sharp bangs coming from Lilly's door. Hanako's head flicks around, and Lilly's eyes close as she listens intently. None of us want to be busted for this."

        show lilly basic_oops_paj
        with charachange

        li "Who is it?"

        mystery "Lemme in, I'm cold!"

        show lilly basic_weaksmile_paj
        with charachange

        $ renpy.music.set_volume(1.0, 6.0, channel="music")

        "Lilly lets out a resigned sigh before motioning for Hanako to open the door."

        show hanagown:
            ease 1.0 tworight alpha 0.0
        with Pause(1.0)

        hide hanagown

        "She obediently gets up and fusses with her gown before moving, apparently still not quite sure of who it is, but trusting enough in Lilly to do as she requests."

        "I can just see a blonde, dark-suited figure become visible over Hanako's shoulder as she opens the door."

        mystery "Happy birthday, Hanako."

        ha "Th-thank you… Akira…"

        "Hanako gives a small bow while twiddling her fingers in front of her. So, this is Lilly's elusive sister."

        show bg at bgleft
        show lilly:
            left
            ypos 1.2
        with charamove

        show hanagown normal:
            center alpha 0.0
            ease 1.0 ypos 1.17 alpha 1.0
        show akira basic_smile:
            right alpha 0.0
            ease 1.0 right xpos 0.95 alpha 1.0
        with Pause(1.0)

        show hanagown:
            center
            ypos 1.17
        show akira:
            right
            xpos 0.95

        "Akira follows Hanako to the table after shutting the door behind her, giving me plenty of time to have a good look at her."

        "She looks to be about the same height as Hanako, and has short blonde hair that's quite roughly cut. That, in addition to her rather modest breasts, masculine suit and deep voice, gives her quite an androgynous effect."

        show akira basic_ending:
            right
            xpos 0.95 ypos 1.18
        with charamovechangefaster

        "Without further ado, she plops herself down on the side of the table across from me."

        show lilly basic_smile_paj
        with charachange

        li "It's nice to have your company after all, Akira. Did work let you off?"

        show akira basic_boo
        with charachange

        aki "Yep. I have to go back there in a bit, but I managed to get enough of a break to drive down."

        show akira basic_smile
        with charachange

        aki "So… this would be Hisao, then?"

        "A confident smile gets thrown in my direction, so I nod politely in return. Considering she just jumped straight to using my first name, she's much more informal than her appearance would suggest."

        "Wait, if she already knows who I am, that must mean that Lilly's talked about me with her. I wonder what she said."

        show lilly basic_smileclosed_paj
        with charachange

        li "Sorry for not introducing you, Hisao. This is Akira Satou, my elder sister."

        hi "I see. Nice to meet you."

        show akira basic_ending
        show hanagown worry
        with Dissolve(0.1)

        show hanagown:
            ease 0.1 ypos 1.15
            ease 0.1 ypos 1.17

        "The person in question loudly claps her hands together, making Hanako jump a little bit."

        show akira basic_lost
        with charachange

        "Akira notices this, and looks uneasy for a fraction of a second before getting back into her stride."

        show akira basic_smile
        with charachange

        "Only now do I realize that Akira hasn't paid Hanako's scars any undue attention. Hanako also seems to be comfortable, if not exactly relaxed, around Akira."

        show akira basic_laugh
        with charachange

        aki "Well then, I assume the presents got through? No point in waiting, considering Hisao and the birthday girl look like they're pretty eager."

        show lilly basic_cheerful_paj
        with charachange

        "Lilly giggles as I awkwardly turn away, a little embarrassed by the fact that I couldn't hide my interest. Hanako's eyes are telling me that she wants to try the wine together with me, though, so I settle for a look of badly feigned indifference."

        show lilly basic_smile_paj
        show akira basic_smile
        show hanagown distant
        with charachange

        "Akira manages to uncork the first bottle with small effort, and Hanako goes to get some glasses before I get to pour the four of them full of white wine."

        "I heard somewhere that white wine has less alcohol than red wine, so I think it would be the best to start with."

        hi "Here's to Hanako, and to Lilly's trip."

        show lilly basic_giggle_paj
        show akira basic_laugh
        with charachange

        call screen doublespeak(li, _("Cheers!"), aki, _("Cheers!"))

        show hanagown smile
        with charachange

        ha "C-cheers…"

        show lilly basic_smileclosed_paj
        show akira basic_smile
        with charachange

        "After the traditional raising of the glasses we all take sips of the pale yellow liquid. It's nothing like the stuff I've had with my parents, with the fruitiness of the flavor almost entirely hiding the taste of alcohol."

        "Maybe this is what proper wine is supposed to taste like. Then again, it's possible that Akira just chose a wine which would be suited to our tastes, since none of us are used to alcohol yet."

        "Or at least, I hope none of us are."

        hi "This isn't too bad. I was expecting something… harsher."

        show akira basic_ending
        with charachange

        aki "If you hadn't liked it, I have a few other varieties you could have chosen from."

        hi "You sound like you know your stuff when it comes to wines."

        show akira basic_smile
        with charachange

        aki "Only a bit; I'm more of a beer kind of person."

        show akira basic_laugh
        with charachange

        aki "I have the drinking side down pat, though."

        "As if to prove her point, she refills her glass before bringing it to her lips and flicking her head back."

        stop music fadeout 6.0

        show akira basic_smile
        show hanagown normal
        with charachange

        "Hanako and I silently watch as the whole glassful disappears down Akira's throat. I can't decide whether to be impressed or put off, but I certainly don't have any urge to imitate the act."

        show lilly basic_displeased_paj
        with charachange

        "Lilly grimaces slightly at her sister's boast. I note that she is sipping from her glass as she does so, though."

        show lilly basic_weaksmile_paj
        with charachange

        li "Anyway, now that Akira's gift has been opened and sampled, shall we move onto ours?"

        show hanagown worry
        with charachange

        ha "G-gifts?"

        play music music_twinkle fadein 6.0

        show lilly basic_smile_paj
        with charachange

        li "That's right, we got you presents. It's your birthday, after all."

        show lilly basic_smileclosed_paj
        with charachange

        li "This is from me."

        "Lilly pulls out the carefully-wrapped doll from under the table and passes it to Hanako."

        "Hanako handles the present as if it was glassware, carefully turning it over to remove the tape that binds the wrapping. Eventually the paper falls from the doll, revealing the emerald green of the doll's dress."

        show hanagown normal_blush
        with charachange

        ha "It's… beautiful."

        "I'm not sure what reaction I was expecting from Hanako. The near-total lack of dolls in her room made me think that she didn't care about them, but the look in her eyes now is something different."

        "She turns the doll around with the same delicacy she afforded the wrapping, as if she was expecting it to fall apart in her hands."

        show lilly basic_weaksmile_paj
        with charachange

        li "I'm glad that you like it. Hisao picked it out, to be honest."

        "Hanako suddenly remembers that she is not alone in the room, and shifts her focus from the doll."

        show hanagown smile
        with charachange

        ha "Y-yes, I like it. Th-thank you, Lilly and H-Hisao."

        hi "Actually, I got you something else…"

        "I reach into my bag and remove the wrapped chess set."

        hi "Here. Happy birthday."

        show hanagown normal
        with charachange

        "Hanako carefully sits Lilly's doll next to her and opens my present with the same care that she showed Lilly's."

        "Before long, the checkered squares of the chessboard are visible, and Hanako gently runs her fingers across the carved surfaces."

        show hanagown normal_blush
        with charachange

        ha "Oh!"

        "Almost by accident she triggers the catch to the lid, startling herself in the process. She opens it and retrieves one of the gray pieces."

        "She seems as absorbed in the chess pieces as she was in the doll before."

        hi "They're coral. Natural coral, undyed. Or so I'm told."

        show hanagown smile
        with charachange

        ha "Thank you, Hisao…"

        hi "No problem. It's your birthday, after all."

        show hanagown distant
        with charachange

        ha "That's right… my birthday…"

        "Once again Hanako's reaction seems a little off, but she carefully closes the board lid."

        show akira basic_lost
        with charachange

        "I notice Akira's smile beginning to look very strained. I wonder if she knows anything about what happened in class, given that she seems to be treading on eggshells around Hanako."

        hi "I'll have to play you again sometime."

        show hanagown smile
        with charachange

        ha "I'll… make sure I'll play you first…"

        show ev hanako_presents2:
            truecenter
            zoom 1.1
            warp acdc_warp 10.0 zoom 1.0
        with whiteout

        "She takes the doll she received from Lilly and holds it to her chest together with the small chessboard, putting the piece on top."

        "The act seems to settle her down somewhat, and we just sit in silence for a while."

        "I think it's one of the few times I've seen her genuinely happy, cradling the friendship of two people to her chest as tightly as she can."

        show akira basic_boo
        show lilly basic_smile_paj

        hide ev
        with locationchange

        ha "Thank you, Lilly. Thank you, Hisao."

        show hanagown worry_blush
        with charachange

        "In the process of thanking us, Hanako drops the chess piece and fumbles a bit in her rush to retrieve it."

        show hanagown distant
        with charachange

        "Once she finds it, Hanako puts the chess set down and nervously gulps at her wine. It's as if the real world suddenly rushed back into her consciousness, and her fastest escape from it was in a glass."

        hi "Hey, easy there, you shouldn't drink it that fast…"

        show lilly basic_weaksmile_paj
        with charachange

        li "It is a party, Hisao…"

        "Despite saying this, there is a slightly concerned edge to her voice. Eventually acquiescing, Lilly proceeds to follow Hanako's lead, though not as eagerly."

        "She looks to be taking small sips from her glass and letting the wine settle on her tongue before swallowing. I decide that this is probably the best approach and do the same myself."

        hi "Since this is kind of a going-away party for you as well, I hope you enjoy your trip at least a little, Lilly. Hopefully your aunt will be okay."

        show hanagown worry
        with charachange

        ha "I-I hope your aunt is okay too, Lilly…"

        show lilly basic_surprised_paj
        with charachange

        "Lilly and I are slightly taken aback by Hanako's fervor to wish Lilly well, despite her own familial situation. I'm a little impressed."

        show lilly basic_weaksmile_paj
        with charachange

        li "My my, thank you both. I'll be sure to convey your thoughts to my family when I meet them."

        show akira basic_smile
        with charachange

        aki "It'll all be fine in the end, Lilly. Don't worry about it."

        "Since the room's mood has become noticeably more sullen, I decide to try and move things along."

        hi "Well then, shall we start on the cake?"

        show hanagown normal
        show lilly basic_smileclosed_paj
        show akira basic_ending
        with charachange

        "My tentative suggestion has the intended effect, everyone lightening up considerably."

        show hanagown normal_blush
        with charachange

        ha "Y-yes, please…"

        show lilly basic_surprised_paj
        with charachange

        li "Cake? I didn't know there was any cake…"

        hi "I picked one up before I came, along with some snacks."

        show lilly basic_giggle_paj
        with charachange

        li "Well done, Hisao. At least one of us remembered to bring one."

        "Everyone seems to welcome the distraction, so I retrieve the cake from my bag and start cutting it up."

        "Mixing wine and chocolate cake isn't something that I thought would work well, but none of us seem to mind. Conversation is temporarily suspended as we start to eat."

        "I was initially wary of this idea; after Hanako's panic attack I expected the worst from tonight, but I think Lilly's idea of giving her good memories of her birthday is working. That, and also having it shared with her going-away party."

        "From Hanako's reaction to her gifts, I can tell she was really appreciative."

        show lilly basic_smileclosed_paj
        show akira basic_smile
        show hanagown drunknormal
        with shorttimeskip

        "Hanako tries to pour herself another glass of wine, but ends up spilling some on the table. She's had a couple by now, so considering that she's never had alcohol before, it's no wonder if she's feeling a bit light-headed."

        show hanagown drunksad
        with charachange

        ha "S-sorry Lilly… I didn't mean to make a mess… I…"

        hi "Don't worry, I've got it…"

        show ev lilly_hanako_hug:
            xalign 0.5 yalign 1.0
            easein 12.0 yanchor 0.0 ypos -0.15
        with whiteout

        "Lilly reaches sideways and gently takes the fussing Hanako in her arms, giving me pause."

        li "It's okay, Hanako. I'm just happy you're here."

        "Hanako gives only a faint nod in response. It's fitting, I suppose, that Lilly would be the one to support her like this. I have no idea what Hanako would be like if she hadn't."

        "Seeing the two like this makes me appreciate the fact that I'm privy to such an intimate moment. Even Akira can't help but smile at the sight."

        "I never would have thought I'd manage to find new friends so quickly, and I'm all the more thankful that of all people, these two are the two I befriended."

        stop music fadeout 3.0

        show lilly basic_cheerful_paj:
            xpos 0.02
            ease 1.0 xpos 0.0
        show hanagown drunksmile:
            xpos 0.48
            ease 1.0 xpos 0.5

        hide ev
        with locationchange

        "They slowly break off from one another, Hanako regaining herself somewhat while I quickly get myself back on task."

        show lilly:
            xpos 0.0
        show hanagown:
            xpos 0.5

        "I find a towel among Lilly's tea set and start mopping up the spillage. By the time I finish, however, Hanako and Lilly have managed to uncork the other bottle and have topped off their glasses."

        show akira basic_ending
        with charachange

        aki "Looks like you're enjoying the wine, then. Just don't go too crazy with it after this, mind."

        "We all dutifully nod and agree, but her reminder feels a bit silly given that she's the one supplying underage people with alcohol."

        play music music_comedy fadein 0.5

        show lilly basic_cheerfulblush_paj
        show hanagown drunkgiggle
        show akira basic_boo
        with shorttimeskip

        "The second glass of wine goes down a lot quicker than the first, and before any of us notice, the second bottle is empty. While Akira is helping us finish them off, Hanako looks to be almost equaling her in the amount she's had."

        "My head feels a little light, but I think I've managed to gauge my own tolerance surprisingly well. Hanako smiles lazily, toying with her doll's hair. I think it's a pretty safe bet that she… hasn't moderated herself as well as I."

        "I don't think it was Hanako's intention to get this drunk, but it seems that the alcohol hit her all at once. She has a very light frame, something which wouldn't help her handle her booze well, either."

        "Lilly cradles her glass, running a finger around the rim. Her cheeks are rosy, but she's managing to avoid looking woefully drunk. Akira is, as I somewhat expected, largely unaffected."

        "Her smile might be a little wider than before, though. Maybe."

        show hanagown drunkgiggle:
            ease 0.1 ypos 1.15
            ease 0.1 ypos 1.17
        with None

        show hanagown drunkpout
        with charachange

        show hanagown:
            center
            ypos 1.17

        "Hanako suddenly hiccups and accidentally knocks over the doll."

        show hanagown drunksad
        with charachange

        ha "I… think I should maybe go to bed. T-thank you, Hisao, thanks Lilly and Aaaakiraaaa."

        "She slurs Akira's name pretty hard, barely avoiding breaking out into a giggle midway through. She's completely plastered, and I can't decide whether I should feel a little bad or not for being amused at the state she's in."

        "It really is bizarre to see her acting so carefree. A shame that it's only with the help of alcohol."

        show akira basic_ending:
            right
            xpos 0.95 ypos 1.0
        with charamovechangefaster

        aki "Here, let me give you a hand."

        "Akira begins to get up to help Hanako out, but she's stopped when Lilly gives a sharp cough."

        show lilly basic_planned_paj
        with charachange

        li "Hisao, would you please?"

        show akira basic_lost
        with charachange

        "Akira looks a little surprised, and I have to admit that I am as well. I don't mind the request at all, let alone when it's said with such a smile… it just comes rather unexpectedly."

        hi "S-sure. No problem."

        show hanagown drunkgiggle_close at center
        show akira basic_smile
        with charamovechangefaster

        stop music fadeout 4.0

        "I pick up the chess set and help Hanako stand up. I do feel somewhat responsible for her considering that, other than Akira, I'm probably the most sober person in the room. She nurses the doll in one hand and offers me the other."

        show hanagown drunkgiggle_close:
            parallel:
                ease 0.5 xpos 0.45
                ease 1.5 xpos 0.55
                ease 0.5 center
            parallel:
                1.5
                "hanagown drunkgiggle_close_ni" with Dissolve(1.0)
        show bg school_dormlilly:
            ease 1.0 xpos 0.45
        show akira basic_smile:
            ease 1.0 xpos 1.0 alpha 0.0
        show lilly basic_planned_paj:
            ease 1.0 xpos 0.05 alpha 0.0
        with None

        show bg school_girlsdormhall:
            center
            xpos 0.6
            ease 2.5 xpos 0.4
        with Dissolve(1.0)

        hide akira
        hide lilly

        pause 0.5

        show bg school_dormhanako_ni:
            center
            xpos 0.45
            ease 1.0 center
        with Dissolve(1.0)

        show bg at center

        "We stumble out of the door, into the hallway, and into Hanako's room, Hanako bumping into me a number of times on the way."

        play sound sfx_switch

        scene bg school_dormhanako
        show hanagown drunkgiggle_close at center
        with Dissolve(0.2)

        "Inside the room, I flick on the light as Hanako turns her attention towards a shelf on her dresser. An elegant doll is sitting on it, staring into the bare room."

        show hanagown drunksmile_close
        with charachange

        ha "There you go… you'll be safe in here…"

        show ev hanako_dolls
        with locationchange

        "Hanako gingerly places the doll next to the other one and straightens its dress."

        "They sit in silence, hair and clothes perfectly arranged. Just like the teapot in Lilly's room, they serve as a distinct contrast to the dull whites and grays that permeate her bedroom."

        show hanagown:
            ease 0.25 ypos 1.05
            ease 1.0 ypos 1.0
        hide ev
        show hanagown drunkdistant:
            ease 0.25 ypos 1.05
            ease 1.0 ypos 1.0
        with charadistant

        "Satisfied that her dolls, her only two real possessions, are safe, Hanako takes a step back and stands up, staggering severely. I step forward to catch her if need be, but she regains her balance without my help."

        "For a while, both of us stand in silence as Hanako looks downwards toward the cupboard."

        show hanagown:
            ease 1.0 xpos 0.48
            ease 1.0 xpos 0.5
            repeat

        pause 0.5

        "After a minute or two she begins to sway a little from side to side. It's very off-putting."

        hi "Are you… going to be all right?"

        show hanagown drunksmile at center
        with charamovechangefaster

        "Hanako raises her head, and turns around to me as if she's only just remembered that I'm also in the room."

        show hanagown drunksmile_close:
            ease 1.0 ypos 1.05
        with vpunch

        stop music fadeout 0.3
        play sound sfx_pillow

        "What's unexpected is that she takes two steps towards me and wraps her arms around my body, her head coming to rest against my chest."

        play music music_heart fadein 0.5

        "I can feel my heart beating as all of my senses feel like they're coming alive again after their deadening through the previous drinking."

        "The smell of wine on her breath, the feeling of her fingers through my clothing, the scent of her hair underneath my chin…"

        "My hands remain out in front of me, not daring to touch her. The temptation is there to hug her, to embrace her, to tell her everything will be fine… but this feels wrong. Really, really wrong."

        hi "Hanako…"

        show hanagown drunknormal_close:
            center
            ypos 1.05
        with charachangealways

        ha "But I want to staaaay with you and Lillyyyy."

        "Hanako's slurring reminds me a bit of Misha. She probably wouldn't be pleased to hear that."

        hi "You know I can't. You're a girl and I'm a guy, after all, and Lilly needs to sleep."

        show hanagown drunkpout_close
        with charachange

        "She gives a disappointed groan. It's so strange for her to act so forward."

        hi "Don't worry, I'll see you again tomorrow, okay?"

        "I decide to rest a hand on her head to reassure her, deciding that this is as far as I'll allow myself to go in terms of physical contact with her while she's in this state."

        "Hanako's head nuzzles against my chest. It makes me feel all the more uneasy with the situation, and as her arms tighten around my back, I quickly decide to bail out."

        "I rest my hands on her shoulders and give a firm but gentle push. Her grip tightens a little as I do so, but she eventually breaks off."

        show hanagown drunkworry_close
        with charachange

        ha "I don't want you to go…"

        hi "Hanako, please. Akira and Lilly are going to start thinking weird stuff if I take too long here."

        "It's perfectly true, too. I really don't want to take any chances, and I feel very uncomfortable right now."

        "I shouldn't try to read anything into the way she's acting right now. I read that aside from alcohol lowering inhibitions, people can react to getting drunk in many different ways that don't necessarily reflect reality."

        "And even without that, there are plenty of ways to interpret what she's saying. As long as she's safe, I'm going to try and get out of her room as soon as possible."

        show hanagown drunkworry_close:
            ease 0.1 ypos 1.03
            ease 0.1 ypos 1.05
        with Pause(0.2)

        show hanagown:
            center
            ypos 1.05

        "Hanako hiccups again, looking a right mess as she stands and looks downcast in the center of the room."

        "Her personality changed as she drank more and more, and now, all alone in her room with me, her previous brightness seems to have left her. Was she just acting upbeat to make sure we didn't worry?"

        "Even if she was… what could I possibly do for her, since I do exactly the same thing in regards to my own condition?"

        show hanagown:
            ease 1.0 ypos 1.1 alpha 0.0
        with Pause(1.0)

        hide hanagown

        "Distancing myself from my thoughts, I eventually manage to corral Hanako towards her bed, though her attempts to tame the wild sheets on it end up accomplishing little."

        hi "Sorry about tonight, Hanako. I know you probably won't remember any of this, but… happy birthday. I'm sorry I couldn't do more for you."

        "She looks up at me for a moment. I have no idea if what I said actually got through to her, but any chance to ask is lost as her eyes peacefully close."

        play sound sfx_switch

        scene bg school_dormhanako_ni
        with Dissolve(0.2)

        "I sigh in relief before quietly backing away from her and leaving the room, flicking the light switch off as I go."

        stop music fadeout 4.0

        scene bg school_girlsdormhall
        with locationchange

        "I hesitate a little before opening the door to Lilly's room again, quickly rehearsing what I should say if I get questioned about Hanako. After a few seconds, I still can't come up with anything."

        scene bg school_dormlilly
        show lilly basic_smileclosed_paj:
            twoleft
            ypos 1.2
        show akira basic_smile:
            tworight
            ypos 1.18
        with locationchange

        "I open the door and make sure to close it behind me, lest any passing students catch a glimpse of the wine, before turning my attention to the two girls at the low table."

        "Akira's casually smiling, as is Lilly. I welcome the change from the mood in Hanako's room."

        show lilly basic_smile_paj
        with charachange

        li "Is that you, Hisao?"

        hi "Yeah. I got Hanako to her bed; she's sleeping now."

        show lilly basic_weaksmile_paj
        with charachange

        li "That's good. I have to admit I hadn't thought that she'd drink quite so much."

        show akira basic_lost
        with charachange

        aki "Hey, it's fine. She's all safe and tucked up in bed now. With the way she is…"

        "She awkwardly trails off, though Lilly and I would hardly protest. For someone so anxious and fearful, drinking would give an easy out from those constant feelings."

        play music music_night fadein 4.0

        "I wish I could do more for her. I feel useless."

        "Looking at Lilly, I think back to what I asked myself in town. My relationship with her is that of a friend, and has only ever felt that way, but now I think I know why."

        "Lilly's been there for both Hanako and me since I first met her, but she's like that for everyone, trying to do her best to make them feel better."

        "With that in mind, then what's the bond between me and Hanako?"

        "After rescuing our relationship following the panic attack I inadvertently triggered during class, I feel like we're back to being friends, but she's on my mind more and more."

        "I can't say I view any other girl in quite the same way, but maybe it's just a normal reaction to someone acting like this."

        hi "Say, Akira?"

        show akira basic_boo
        with charachangealways

        show akira basic_smile
        with charachangealways

        "She yawns before looking at me. It is getting pretty late."

        hi "You know about what happened with Hanako, don't you?"

        show akira basic_resigned
        with charachange

        aki "Yeah. Lilly told me."

        show akira basic_boo
        with charachange

        aki "I negotiated pretty hard for a break so I could come down and help make her birthday a bit brighter. We get along pretty well."

        "It's surprising to hear that from someone as extroverted as her, but if Hanako came to know her through Lilly, maybe she had time to get used to Akira."

        show akira basic_smile at tworight
        with charamovechangefaster

        aki "And on that note, I'd better get going. I'm already going to be a bit late as it is."

        show lilly basic_oops_paj
        with charachange

        li "But it's already so late…"

        show akira basic_boo
        with charachange

        aki "Sorry. We got a bunch of work dropped on us, so overtime it is."

        show akira:
            ease 1.0 xpos 0.8 alpha 0.0
        with Pause(1.0)

        "She levers herself up with a grunt and heads past me towards the door. Just before she leaves, she turns back towards us."

        show akira basic_lost:
            ease 1.0 tworight ypos 1.18 alpha 1.0
        with Pause(1.0)

        show akira:
            tworight
            ypos 1.18

        aki "You haven't forgotten about the time for the flight and all the rest?"

        show lilly basic_smileclosed_paj
        with charachange

        li "Don't worry, I have everything ready. It's just a matter of packing when it gets closer to the time to leave."

        show akira basic_ending
        with charachange

        aki "'Atta girl. I'll see you guys later, then."

        show akira:
            ease 1.0 xpos 0.8 alpha 0.0
        with Pause(1.0)

        hide akira

        "And with that, she disappears through the door with her hand held high in farewell."

        show lilly:
            center
            ypos 1.2
        show bg at bgright
        with charamove

        hi "Your sister is… something, all right."

        show lilly basic_giggle_paj
        with charachange

        "I probably should have thought that comment through before saying it. Regardless, Lilly seems quite amused at my appraisal."

        hi "You okay after all that drinking? Not wasted and just hiding it well?"

        show lilly basic_smileclosed_paj
        with charachange

        li "I assure you, I am quite all right. I can moderate myself. You seem quite self-possessed as well, if I do say so myself."

        hi "Yeah, well, I guess your moderation applies to me as well."

        "With a little hesitation, I take a seat at the table in front of Lilly. I want to address this directly, if for no other reason than to settle my own thoughts."

        hi "I've been meaning to ask this, but it took me a while to make up my mind…"

        hi "Do you have any idea about what triggered that panic attack? I gathered it was something to do with her birthday, but I don't know anything more."

        hi "Even Akira was being really careful around her, so I assume she knows as well."

        show lilly basic_reminisce_paj
        with charachange

        "Lilly's smile drops, the gaiety of the birthday party now well and truly over."

        li "To be honest, I'm not sure of all of the details myself."

        li "Hanako told you that she was in a house fire. She told me as much, after we met and spent a lot of time together."

        show lilly basic_concerned_paj
        with charachange

        li "Other than that… she quite simply never told me."

        hi "She never told you…"

        show lilly basic_sad_paj
        with charachange

        li "Assuming the worst, what does she have to look back upon? A life of isolation and possibly even the death of her family? Maybe even going as far as blaming her existence for their deaths?"

        "Even thinking about what little I know of Hanako's past is bleak. To have lived through all that, and to live on with those memories, must be infinitely worse."

        "Lilly looks similarly depressed, but I can see her rebuild at least some of her composure before my eyes."

        "I get the feeling that both of us are talking more frankly than we might otherwise do thanks to the wine, but it feels like just talking this out is a good thing anyway."

        hi "I feel kind of helpless about it. When it's put like that, what can I possibly do for her?"

        show lilly basic_sleepy_paj
        with charachange

        li "I'm not wholly sure I should tell you this, but Hanako told me that you visited her the day after we both went to check on her."

        show lilly basic_weaksmile_paj
        with charachange

        li "I must admit that I did not predict she would take such a step so quickly after what happened, nor did I expect you to. I think it was a nice gesture on your part."

        hi "It wasn't much, really."

        hi "It's just… at times like this, I sometimes think it would be better if we never had to leave Yamaku, or at least this town. Things are so much easier without others around."

        "I didn't expect Lilly to look quite so troubled at what I say, and for a while she looks lost in thought."

        show lilly basic_oops_paj
        with charachange

        "She moves to speak, but stops herself as soon as she does, and rethinks. It's a bit off-putting."

        show lilly basic_reminisce_paj
        with charachange

        li "I think…"

        show lilly basic_smile_paj
        with charachange

        li "Tell me, do you have anything planned for Friday evening?"

        hi "Friday evening? No…"

        hi "Isn't your flight to Scotland the next day? I don't think it would be a good idea to tire yourself out before you even get there."

        show lilly basic_weaksmile_paj
        with charachange

        li "I'll be all right, you needn't worry about me. I'd do this tomorrow evening, but I imagine Hanako will be feeling rather off for a while."

        "The thought of how she's going to be tomorrow makes me grimace. Maybe we should count our blessings that she didn't end up simply throwing up from drinking so much while having such a low tolerance."

        hi "Well, I'm going to be able to attend whatever you are planning. What is it?"

        show lilly basic_smileclosed_paj
        with charachange

        li "Nothing unusual, I assure you. Just a little excursion."

        show lilly basic_cheerful_paj
        with charachange

        li "And you'd better be off, Hisao. I can't imagine it's long at all until curfew is here."

        "Oh damn, curfew. I'd completely forgotten."

        "I look at the clock next to Lilly's bed, but it seems to be some oddity without written numerals. Which I suppose makes sense, given Lilly's condition."

        "Not wanting to risk a haughty security patrol giving me a scolding, I get up and decide to go to my dorm as she says."

        hi "Well then. I guess I'll see you and Hanako tomorrow, assuming the both of you manage to get up in the morning."

        show lilly basic_smileclosed_paj
        with charachange

        li "Thank you for your concern, Hisao. Until then."

        scene bg school_girlsdormhall
        with locationchange

        "With that, I make my way out of her door and into the hallway."

        "I hope her idea will be a good one."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .one_piece_of_paper:
        scene black
        with dissolve

        play sound sfx_doorknock

        "The hammering of a fist against the door feels like a nail being pounded into my head."

        "Once, twice, three times, I let out a long, annoyed breath and bear it while pressing my eyelids shut, fervently hoping for whoever it is to just go away."

        "I feel pretty damn awful. My face feels like it's cast out of lead, my arms feel heavy, and I feel very queasy. It's been like this since I woke up half an hour ago, and I can't summon the energy to pick myself up out of bed."

        "So… this is what they call a hangover."

        "I wonder if perhaps this is the best treatment for teenagers who desperately want to try drinking as a way to feel like an adult. Considering how unpleasant this is, it's not something I want to repeat."

        play sound sfx_doorknock

        "A series of thumps rings out again, reverberating around the small room. I wish they'd just give up already; I have no intention of getting out of bed for them."

        "Seconds pass, turning to minutes. Since no more knocks are coming from the door, whoever it was must have left. Thank goodness."

        play music music_dreamy fadein 2.0

        scene bg school_dormhisao
        with openeye

        "Looking to my clock, the time when I really should think about getting dressed and ready for class is approaching. I don't think I can manage it, though."

        "I hate cutting class, but I don't think I'm going to be able to get much done at this rate. I can tell I look like a mess without needing to look in the mirror to confirm it, too."

        scene bg school_hallway3
        with shorttimeskip

        "The morning rush is giving me enough time to stand outside the classroom for a little while without looking too suspicious. I hope that Mutou doesn't ask any awkward questions about my not attending school yesterday."

        "I was sick, that much is true, it's just the reasons for it that I have to hide."

        "Confident I can get by with a tactical omission of certain truths, I stride into the classroom doing my best to appear normal."

        scene bg school_scienceroom
        with locationchange

        "The instant I open the door and take a single step in, I can feel a dozen eyes looking at me. There is no way I'm imagining this; they're not even making any attempt to hide it."

        show hanako emb_emb:
            tworight
            ypos 1.15
        with charaenter

        show hanako emb_downtimid
        with charachange

        "My eyes take a quick sweep around the classroom, and I spot Hanako. We make eye contact momentarily, before she looks down and stares very hard at her desk."

        "Did she spill the beans? Mutou may be okay as far as teachers go, but underage drinking on campus is not exactly something that would be taken lightly."

        "I look to him with some trepidation."

        show muto normal at twoleft
        with charaenter

        mu "Feeling better today?"

        hi "Yeah. Thank you."

        "He motions for me to take my seat, my legs feeling like sticks as they carry me there. This is going to be a long day."

        scene bg school_scienceroom at bgleft
        with shorttimeskip

        stop music fadeout 2.0
        play sound sfx_normalbell

        "As soon as the lunchbell rings, I'm on my way to Hanako's desk to ask her what's going on."

        hi "Hanako… did you tell…?"

        show hanako emb_emb:
            center
            ypos 1.15
        with charaenter

        "She looks up at me and shakes her head. That's a big relief."

        show hanako emb_downtimid
        with charachange

        ha "It's just…"

        hi "Just…?"

        mi "Well hello there, Hicchan. It's nice to see you again today~!"

        show bg at bgright
        show hanako:
            right
            ypos 1.15
        with charamovefaster

        show shizu basic_sparkle at center
        show misha perky_smile at twoleft
        with charaenter

        play music music_happiness fadein 2.0

        "I grimace and turn towards the unmistakable voice coming from behind me. That was way too upbeat a tone of voice to feel comfortable, even from Misha."

        "Misha's happy smile is nothing out of the usual. Shizune's, though, is a very bad sign. The one she wears has become notched into my brain as her 'I have got you seven ways from Sunday' smile."

        hi "Hi Shizune, Misha. You uh… you look happy to see me."

        show shizu adjust_smug
        with charachange

        shi "…?"

        show misha hips_grin
        with charachange

        mi "Not feeling well yesterday, Hicchan~?"

        hi "No, no I wasn't. But I'm feeling better now, at least."

        show shizu behind_smile
        with charachange

        shi "…"

        show misha cross_smile
        with charachange

        mi "That's good to know, Hicchan."

        "Why do I get the feeling that Shizune is leading me into a trap?"

        hi "You sound like you're not being completely serious."

        show shizu adjust_happy
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "Oh no, Hicchan, we're genuinely pleased that you're all better now~."

        show shizu basic_happy
        with charachange

        shi "…"

        "Shizune is positively overflowing with happiness. There's only one reason why she would be like this. Oh no."

        show misha perky_smile
        with charachange

        mi "In fact, we were quite worried about you. After all…"

        show misha sign_smile
        with charachange

        mi "You, Hanako and Lilly were all absent from class on the same day."

        "Yep, she's got us. So thoroughly that all I can do is sigh in defeat."

        hi "I guess you have your own theories about this. Could you just kinda… not tell anyone?"

        show misha cross_smile
        with charachange

        mi "It's a bit late for that, Hicchan~."

        "I suppose she's right, considering the looks I got as I entered class. Still, things only seem to be at the level of vague suspicion rather than outright accusations, so we'll probably be fine."

        show hanako emb_downsad
        with charachange

        "Hanako's face sinks a little further. Such attention is troublesome enough for me, let alone for her. Going by Shizune and Misha's reactions, I think they notice this as well."

        show shizu basic_angry
        with charachange

        shi "…"

        show misha hips_frown
        with charachange

        mi "The only reason why we're giving you such a hard time is that you ignored us yesterday morning~!"

        "Yesterday morning? It takes a while to recollect what happened then, given the haze induced by the generally awful state I was in at the time."

        hi "Oh, right, the knocking. That was you two?"

        show shizu behind_frown
        with charachange

        shi "…"

        show misha cross_frown
        with charachange

        mi "It was, and you left us there for ages after we'd taken all the effort of coming to your dormitory early in the morning."

        hi "Sorry, I was having a… problem with nausea? A problem with nausea."

        "They're not buying it. I can't blame them."

        show shizu behind_frustrated
        with charachange

        "Shizune's head drops in resignation before she reaches into her pocket."

        "Something white and yellow can be seen sticking out a little, and as she pulls it out, it turns out to be an envelope with very bright decorations on it."

        show letter_insert:
            truecenter
            ypos 0.7
            easein 1.0 truecenter
        with Dissolve(1.0)

        show letter_insert at truecenter

        "Since she points it towards me, I duly take it."

        mi "This is what we were trying so hard to give you, Hicchan! You don't check your…"

        stop music fadeout 5.0

        "I tune out the sound of Misha's voice as my eyes register what's written on the envelope."

        stop music fadeout 0.3

        hi "Iwanako…"

        "I stare at the envelope for a moment, before suddenly remembering that there are people around me."

        show misha cross_smile
        show shizu behind_blank
        show hanako emb_timid

        show letter_insert:
            easeout 1.0 ypos 0.7 alpha 0.0
        with Pause(1.0)

        hide letter_insert

        "There's a very strange, somewhat invasive feeling about their expressions. I kind of want to be alone right now."

        show hanako emb_sad
        with charachange

        ha "Iwanako…?"

        hi "It's nothing. Thank you for bringing me this, you two."

        show misha hips_grin
        with charachange

        mi "I should think so, after what we went through to get it to you~."

        show misha hips_frown
        with charachange

        "I step back and say my goodbyes. Misha theatrically pouts even as I go out the door, but Shizune and Hanako remain very visibly curious about my reaction. I hope they won't interrogate me on this later."

        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
        play ambient sfx_parkambience fadein 2.0

        scene bg school_gardens2
        with locationskip

        play music music_serene fadein 2.0

        "The smell of the gardens is, as always, a very pleasant sensation. Some of the most visible signs of how well-funded this school is, aside from its sheer size, are the expanse and condition of the grounds."

        "A good number of students can be seen eating lunch, chatting, and playing on the bright green lawns. Even some of the staff is enjoying the summer here, keeping watch over the students and idly walking along the long concrete paths."

        "I'd never seen a sight like this in my home city. On excursions, maybe, but certainly never in the school or anywhere near where I lived."

        "Even the bench I sit on to read is warmer thanks to the summertime sun, reminding me of why I haven't worn the school blazer even once yet."

        show letter_open_insert:
            truecenter
            ypos 0.7
            easein 1.0 truecenter
        with Dissolve(1.0)

        show letter_open_insert at truecenter

        "Considering this, the sunflowers and splashes of vibrant yellow coloring adorning the paper are quite appropriate for the time. If only the words written on it were as well."

        "Here I was, thinking I'd managed to get over her, when this troublesome thing shows up."

        "Her handwriting looks vaguely familiar at best, and only now that I see it again I remember that she used to write in pink pen a lot. She was always very girly, for lack of a better term."

        "But she was also quite fragile. I never knew if I liked this aspect of her or not, though with the arrival of this letter, that question seems to have become largely moot."

        "The letter begins with not much more than an update on the state of things going on in her life. My old class had a good start to the school year, many are anxious about the exams that will be coming up in the future, etcetera."

        play sound sfx_paper

        hide letter_open_insert
        show letter_open_insert_2 at truecenter
        with charachangealways

        "But it ends on a very personal, if brief, note. It feels a bit like she wrote most of the letter just to try and soften the blow from the ending."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        call screen written_note(_("I wanted to somehow express my feelings, but the right words didn't come to me. I couldn't say anything to comfort you. I am really sorry for not being able to support you when it mattered the most, even though I like you so much. At least now, finally, I can be more honest.{vspace=120}"))

        call screen written_note(_("If I could go back to those quiet days in February and March, I'd tell you to not give up on yourself. That's what I would say. Maybe you wouldn't have drifted so far away if I had just said something. I hope you've managed to get back on your feet on your own.{vspace=120}"))

        call screen written_note(_("Now that the distance between us is also physical, it also feels more final, somehow. I wonder if we will meet again. Perhaps it's for the best if we don't? Still, if you would like to correspond with me, by all means write me back. I'd very much like to hear about your new school and how you are doing. I wish you all the best.\n\nSincerely, Iwanako"))

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        "And so, that's that. Our relationship is over. Nice, neat, and tidy, with no ambiguity."

        "I hadn't held on to any illusions that it could ever begin anew. The last time she visited me, neither of us said a thing, except for the one word she said as she left for the last time. 'Goodbye.'"

        "Be that as it may… this feels more final. The capstone on an experiment that both of us tried, and failed at."

        show letter_open_insert_2:
            easeout 1.0 ypos 0.7 alpha 0.0
        with Pause(1.0)

        hide letter_open_insert_2

        "A loud shout draws my eyes away from the letter. It's just some students horsing around, with one of the teachers standing nearby coming over to talk to them."

        mystery "Are you okay?"

        show yuuko neutral_down at center
        with charaenter

        "A tentative voice comes from my side. For a moment I assume it to be Hanako, but it's actually Yuuko."

        hi "Oh, hello Yuuko. I thought you'd be in the library."

        show yuuko closedhappy_up
        with charachange

        "She gives a cheerful smile, one quite fitting the atmosphere, and flourishes the empty wrapper of a roll in her hand. She must have someone else covering for her while she grabbed something to eat."

        "It reminds me that I haven't had anything to eat yet. I don't feel hungry though, and skipping one lunch won't hurt."

        show yuuko smile_up
        with charachange

        yu "Mind if I sit here?"

        hi "Sure, go ahead."

        show yuuko neutral_down:
            center
            ypos 1.15
        with charamovechangefaster

        "I quickly slide the letter back into its envelope, slipping it inside my bag propped against the side of the bench as Yuuko takes a seat. She drops the wrapper into a bin beside us."

        "Without much else to do, I lean back and take what enjoyment I can from the sun, silently reflecting on the letter."

        "The lush lawns, the clear blue skies… everything looks so different from the way it did back then. Even the school's surroundings, from the hill it's on to the woods around it, are completely opposite to the urban scenery I remember."

        "Maybe this is what it's like to feel homesick. Then again, it's not an outright bad sensation; the feel of the area around Yamaku, while very different, is also nice. I think I could get used to it."

        show yuuko smile_down
        with charachange

        yu "Hey, Hisao?"

        hi "Yeah?"

        show yuuko worried_down
        with charachange

        yu "You didn't answer my question from before. I wasn't going to say anything, but you still look troubled."

        show yuuko panic_up
        with charachange

        yu "If you don't want to say anything though, that's okay, I don't mind at all. Um, s-sorry for asking something strange like that…"

        hi "I don't mind."

        hi "It's just… I got a letter from someone I knew before I came to Yamaku. It made me think about some things."

        hi "I thought I'd managed to get over most of the problems that my accident caused, but now I'm not really so sure. I kinda wish I'd never seen it."

        show yuuko worried_up
        with charachange

        yu "I don't think that's good, Hisao."

        show yuuko neutral_down
        with charachange

        yu "When my boyfriend left me, he did so very suddenly, and never let me know why. At first I was very depressed about it, but I decided to forgive him."

        hi "You forgave him? Couldn't he at least have talked properly with you about it?"

        yu "He was always one of those people that found it difficult to come close to others."

        yu "In the end, I decided that I fell in love with him for a reason. He was a good person, and I think that if I had been in his position, I would probably have found it just as hard to try and talk to him."

        hi "I don't… really see the connection to the letter I got."

        show yuuko worried_up
        with charachange

        yu "I mean that… um, how should I put this…"

        yu "It must have been very hard for that person to send that letter, and if they did, I think they must have thought very hard about exactly what to say."

        "Iwanako managed to write this letter and bring a final close to our relationship; something that I'd never managed to do."

        "Whereas here I am, trying to protect and help Hanako as best I can, especially with Lilly leaving for a while, and I'm not even able to deal with my own problems."

        show yuuko neutral_down
        with charachange

        yu "Does that make sense?"

        "She's taken my nonresponse and furrowed brow as doubt. She really reads faces too much, just like a certain other person."

        hi "Yeah, that makes sense."

        hi "The letter was just kind of a shock, really. I think I'd tried to fool myself into thinking that my life reset when I came into Yamaku, but now I'm suddenly aware that it didn't. I'm at a bit of a loss about how to deal with these feelings."

        show yuuko worried_down
        with charachange

        yu "I think that's something I can't really help you with. Sorry."

        hi "It's fine. I think being able to talk with you helped me get things sorted out a bit better in my head, so thank you anyway."

        show yuuko closedhappy_down
        with charachange

        "She nods and smiles sweetly. Yuuko is a nice girl, so it's a shame she's so highly strung so often."

        play sound sfx_warningbell

        show yuuko panic_up
        with vpunch

        "The school bell ringing out startles us both."

        yu "Ah, I was supposed to be back before the bell!"

        hi "Oops…"

        show yuuko worried_up at center
        with charamovechangefastest

        "She jumps off the bench and almost races off without a second word, but turns on her heel as she remembers she was talking to me just now."

        show yuuko neutral_up
        with charachange

        yu "I'll see you later, Hisao. Cheer up, okay?"

        hi "I'll try to. Thanks, Yuuko."

        stop music fadeout 9.0

        hide yuuko
        with charaexit

        "With a quick bow, Yuuko takes her leave and begins her rush to the library. Her flight catches the curious eyes of a few passing students, who are unenthusiastically trudging back to their classes after their fun."

        "Reluctantly standing from the bench, I dust myself off and join them."

        "Even while I walk through the gardens back to the main building, the thought of the letter in my bag doesn't stray far from my mind."

        stop ambient fadeout 2.0
        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .stripes_and_solids:
        $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
        play ambient sfx_traffic fadein 1.0

        scene bg city_street2_ni
        with locationchange

        "The feeling of walking through the streets is one of very deep nostalgia. While Yamaku may be like the reverse of where I've lived in the past, the city at night is amazingly familiar."

        "My eyes are moving constantly from the bright electronic screens glowing high in the night sky, to the street lamps piercing the darkness with their light, to the businessmen enjoying themselves after work and the busily talking couples on dates."

        "Even if I didn't want to, I can't help soaking in every aspect of the city. I savor its familiarity like a sweet candy sitting on my tongue."

        show akira basic_boo_ni:
            center
            xpos 0.59
        show lilly cane_smileclosed_cas_ni:
            center
            xpos 0.41
        with charaenter

        "Lilly is walking to my left with her cane swaying to and fro, holding onto her sister's arm for guidance while talking to her."

        "Compared to traveling by taxi or bus, being driven by Akira in her rather nice car was a much more enjoyable experience."

        show hanako basic_distant_cas_close_ni:
            offscreenright
            xanchor 0.5 alpha 0.0
            ease 1.0 tworight alpha 1.0
        with None
        show bg at bgleft
        show lilly:
            center
            xpos 0.21
        show akira:
            center
            xpos 0.39
        with charamovefaster

        show hanako at tworight

        "Maybe not for the person on my right, though. While Lilly was used to her sister's driving style, and I quite liked a bit of excitement, Hanako was holding very tightly to the door for most of the trip."

        show hanako basic_smile_cas_close_ni
        with charachange

        ha "E-everything looks so p-pretty at night…"

        show hanako emb_downtimid_cas_close_ni
        with charachange

        "Hanako quickly looks down yet again as she accidentally catches someone's gaze."

        hi "Yeah, it does."

        "My answer isn't very thoughtful, since I'm distracted by so many thoughts that I find it hard to keep up on smalltalk."

        "One of those distractions, aside from the city sights, is how Hanako looks."

        "This is the first time I've seen her in something other than her school uniform or her pajamas. It gave me pause when I first saw her outfit, when we met up at the school gate."

        "Considering how much her head is lowered when people walk near us, I imagine that the hat she wears is more than a fashion statement."

        "While initially I was wary of Lilly's plan to take us out into the city, when night fell it became obvious she had thought about this. Not many people have paid Hanako much heed, since the darkness hides her scarring well."

        hi "So… we're in the city. Any ideas on what to do?"

        show akira basic_smile_ni
        with charachange

        "Akira beams a smile. Something tells me that she's the one who is making this particular decision, even if her sister may have proposed the outing in the first place."

        show akira basic_ending_ni
        with charachange

        aki "You'll see. Just follow us."

        "I nod, and try my best to stifle a grimace. After what happened during Hanako's birthday party, I don't trust Akira's judgment all that much."

        $ renpy.music.set_volume(0.1, 1.0, channel="ambient")
        $ renpy.music.set_volume(0.1, 0.0, channel="music")
        play music music_jazz fadein 14.0

        scene bg city_street3_ni
        with locationchange

        "We keep walking, and I notice that we're passing more and more cafés, restaurants, and other eateries."

        "Every once in a while a drunken man in a suit comes out of a bar, usually being supported by another, but for the most part the customers around this part of the city look young and fashionable."

        "Different kinds of music come and go as we pass by each business. The discord created by the overlaps should be grating, but it reminds me so strongly of the times I spent in the city with my old friends that I don't mind."

        "Hanako and I have started to drift a little apart from Lilly and Akira. That comes to a stop when I hear a soft thud from beside me."

        show hanako defarms_shock_cas_ni at center
        with vpunch

        ha "S-s-sorry…!"

        "By the time she rights herself from her apologetic bow, the middle-aged businessman she bumped into is walking away after mumbling a half-hearted apology."

        show hanako emb_downtimid_cas_ni
        with charachange

        "Hanako looks a little put off by the experience, and as she quickly skips ahead to match my pace, I notice her head hanging low once more. She probably bumped into him because she was looking downwards and not where she was going."

        show hanako emb_timid_cas_close_ni
        with charachange

        "I step to the side a little and put one hand on her far shoulder, drawing her closer."

        ha "Hisao?"

        hi "It's okay. You can walk closer to me if you want."

        show hanako emb_smile_cas_close_ni
        with charachange

        "Hanako hesitates, but eventually nods in assent."

        stop ambient fadeout 1.0
        $ renpy.music.set_volume(0.5, 10.0, channel="music")

        scene bg city_karaokeext_ni
        show crowd_ni
        show akira basic_smile_ni:
            center
            xpos 0.39
        show lilly cane_listen_cas_ni:
            center
            xpos 0.21
        show hanako basic_smile_cas_close_ni at tworight
        with locationskip

        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
        play ambient sfx_crowd_outdoors fadein 2.0

        "After a couple of times when I'd thought we had arrived at Akira's destination, we reach our target. By now we're below the elevated walkways, and past the most garish and brightly-lit places."

        "I'm a bit surprised. The average age of those around us is distinctly older, and the smell of cigarette smoke is pretty thick. The area is far from seedy though, and it's a little amusing to see Lilly's reaction to the smell of the smoke."

        "While it's masked by the low talking of those around us, jazz music can be heard emanating from inside. Looking up at the dimly-lit sign, it becomes obvious why."

        hi "A jazz club. I have to admit, this isn't what I expected."

        show lilly cane_giggle_cas_ni
        with charachange

        "Lilly gives an amused snort and a smile."

        show lilly cane_smileclosed_cas_ni
        with charachange

        li "Somehow I feel like I should have known it, Akira."

        "As we talk outside, I notice more and more odd sideways glances directed our way. People awkwardly catch themselves staring and look away, but that just makes it more obvious."

        "I had noticed this occasionally when we were walking, but it's more pronounced now."

        "I've never experienced anything like that in my life. An average-looking Japanese teenage guy, just a little taller than normal, isn't the type to draw attention without making an effort."

        show akira basic_laugh_ni
        with charachange

        aki "Hey, c'mon. Just because you're teenagers, doesn't mean you can't have a taste. Right?"

        hi "Well… I don't really mind the music, if that's what you mean."

        show hanako cover_bashful_cas_close_ni
        with charachange

        ha "I-I… don't mind it… either…"

        "She's only just managing to force the words out. It contrasts heavily to when we're alone in Yamaku, and it disappoints me a little that she's so highly strung for what's supposed to be a good time out on the town."

        "It's hard to read Hanako's face as she keeps looking downwards. It's little wonder if she doesn't often come out into the city because of this, and it makes me a little thankful that my own scarring is easily hidden."

        "Lilly has a similar way of attracting people's gazes, but the reason for it is clearly different. She hardly looks like a native, and the same can be said for her sister. That much is far more noticeable than her blindness, from a distance."

        "She may not be able to see this for herself, but I have little doubt she can hear the odd whispered phrase from people who think they're out of earshot."

        "Be that as it may, she doesn't seem to show any sign of either annoyance or pleasure at the attention."

        hide akira
        hide lilly
        with charaexit

        "Akira's still as confident as ever, though. Flashing a smile, she strides in with Lilly by her side and the two of us following behind."

        stop ambient fadeout 1.0
        $ renpy.music.set_volume(1.0, 10.0, channel="music")

        scene bg city_clubint:
            center
            xpos 0.6
        show crowd
        with locationchange

        $ renpy.music.set_volume(0.8, 0.0, channel="ambient")
        play ambient sfx_crowd_indoors fadein 1.0

        "I had expected my eyes to need adjusting to the light inside, but it's not much brighter than outside."

        "The music we'd heard is clearer now, mixed in with the sound of glasses moving on the tables and counter, and the husky chatter of the patrons. Looking to my right reveals the music's source, a jazz group playing beyond some tables."

        "The patrons seem to be mostly men, and though there's a handful of women, nobody looks under thirty. Aside from us, of course."

        "It feels a little like we've stepped into the 1920s, and the atmosphere is quite agreeable. I'm not completely comfortable simply because of my age, but were I older, I would probably feel quite at home."

        show hanako basic_smile_cas_close at tworight
        with charaenter

        "Hanako seems a bit more relaxed now, probably due to nobody looking at her. Everybody's talking between themselves, drinking, or watching the band."

        $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

        show akira basic_smile behind crowd:
            center
            easein 1.0 ypos 1.06
        hide crowd
        with Dissolve(1.0)

        show akira:
            center
            ypos 1.06

        "Akira casually takes a seat at the counter without even glancing around. She's probably come here before."

        show lilly basic_smileclosed_cas:
            twoleft
            xpos 0.25
            easein 1.0 ypos 1.1
        with Dissolve(1.0)

        show lilly:
            twoleft
            xpos 0.25 ypos 1.1

        "Lilly retracts her cane, feeling out the bar stool and the edge of the counter before taking a seat beside her sister. The bartender takes a brief break from polishing a glass to watch her, before putting it down and coming over."

        "Bartender" "Good evening, ladies. What'll it be?"

        show akira basic_ending
        with charachange

        aki "Just a scotch, thanks. Lilly?"

        show lilly basic_cheerful_cas
        with charachange

        li "May I have a glass of cham—{w=0.5}{nw}"

        show lilly basic_surprised_cas
        show akira basic_boo
        with vpunch

        "A black-suited elbow hits her side sharply."

        show lilly basic_weaksmile_cas
        with charachange

        li "Orange juice, please."

        "Bartender" "No problem, coming right up."

        "The bartender starts to pour their drinks. A couple of seconds pass before Akira suddenly remembers that Hanako and I are indeed here, and turns around to us."

        show akira basic_smile
        with charachange

        aki "You two want anything, or are you just gonna stand there?"

        "Hanako seems to be getting a bit restless. No matter where we're going to seat ourselves, there's going to be people right next to her, and I don't think she looks convincingly older than twenty, unlike Lilly."

        show bg:
            xpos 0.4
        show akira:
            xpos 0.3
        show lilly:
            xpos 0.05
        show hanako:
            xpos 0.5
        with charamove

        "Looking around, there's a games section to our right. A couple of billiards tables can be seen in the corner, and nobody's using them either."

        "I glance to Hanako, about to ask her if she'd like to play, but she's already looking longingly in the same direction. Maybe it says something that we can get by with so few words nowadays."

        hi "We'll go play pool over there."

        show akira basic_boo
        with charachange

        "Akira leans back to see past me, before shrugging and sitting back up."

        show lilly basic_giggle_cas
        with charachange

        li "It seems you'll have to put up with only me for company. How unfortunate."

        show akira basic_smile
        with charachange

        aki "Have fun, you two."

        $ renpy.music.set_volume(0.8, 1.0, channel="music")
        stop ambient fadeout 14.0

        hide hanako
        with charaexit

        "We turn and set off for the abandoned corner, with Hanako taking the lead."

        "The prospect of a nice, quiet game away from everyone makes her walk noticeably faster. Her eyes stay firmly fixed on her prize."

        scene bg city_clubpool
        with locationchange

        "The table's full-size and well-lit despite the surrounding darkness, thanks to the bright overhead lights. A huge painting of… something… covers the wall."

        "There aren't many people milling about this corner of the club, and I can see Hanako becoming a little less tense as a result."

        show hanako basic_smile_cas at center
        with charaenter

        ha "You… kn-know how to play?"

        hi "I'm no expert, but yeah, I do."

        show hanako basic_bashful_cas
        with charachange

        ha "Then um… eight-ball?"

        hi "Sure."

        hide hanako
        with charaexit

        "Hanako gets the chalk and two cues from a set of hooks against one of the walls, while I fetch the balls from the table's pockets and grab the rack from a shelf underneath."

        "She patiently waits as I get the table set up. After slotting the final ball into the rack and doing some last adjustments, I end up having to fight my perfectionist urges in getting the bottom row of balls exactly perpendicular with the edges."

        "With the balls arranged and ready for play, I step back and take my cue from her outstretched arm. I carry out a quick inspection of the tip before I'm satisfied that it's in good condition."

        hi "So you've played before?"

        show hanako cover_bashful_cas at center
        with charaenter

        ha "Once… or twice. I j-just kind of… know the rules."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        "The air between us feels a little awkward. She's still pretty nervous; understandably, given that we're in public."

        "Eventually the silence becomes too much even for Hanako, and she begins to quietly stammer."

        $ renpy.music.set_volume(0.8, 1.0, channel="music")

        show hanako basic_worry_cas
        with charachange

        ha "Wh-who'll… b-break?"

        "I think for a moment before reaching into my pocket and drawing a coin."

        hi "I'll take heads, you're tails."

        "After a nod of agreement from Hanako, I flick the coin up in the air, catch it, and flip it over onto the back of my left hand."

        hi "Looks like it's you that gets to break."

        scene ev hanako_billiards_break
        with locationchange

        "Hanako nods again, before taking up her position at the end of the table."

        "She's not usually this quiet around me, but I'm not wholly sure if it's because of the tidbit of information about her past that slipped out moments ago."

        scene bg city_clubpool
        with flash

        play sound sfx_billiards_break

        "The cue comes back in a practiced gesture before smacking dead into the center of the cue ball with a thud. The white ball skates across the smooth green expanse before smashing into the carefully-arranged balls at the other end."

        "Balls skitter across the table at high speed. The break was good, with the balls being nicely distributed around the table. My eyes are already flicking from one to another to pick out the easiest candidates to pocket."

        play sound sfx_billiards

        "Hanako retreats from the side and I take my shot."

        show hanako basic_smile_cas at center
        with charaenter

        ha "Well done."

        "It's only after Hanako says this that I realize the ball I was shooting at was sunk."

        "I look at her and notice a small smile on her face. It's nice how playing games seems to loosen her up a little."

        hi "Guess I'm stripes, then."

        show hanako cover_distant_cas
        with charachange

        "I take a step back and let her take the next shot, but she doesn't advance to the table. Rather, she looks down a little and rubs her arm."

        "By now I can identify this as one of her gestures that mean she wants to say something, but isn't sure enough of herself to do it."

        hi "What's up?"

        show hanako cover_bashful_cas
        with charachange

        ha "It's just… you had a… n-nice smile. Do you like… playing this?"

        "I sigh and lean back against the table."

        hi "I like playing, yeah. I think I was smiling because it's really nostalgic, though."

        show hanako def_worry_cas
        with charachange

        "Hanako tilts her head quizzically."

        hi "Me and my friends used to play pool in the game centers near where we lived pretty often, and at night too."

        show hanako basic_worry_cas
        with charachange

        ha "W-wouldn't your parents…"

        hi "My parents both worked, so they didn't mind me not being in the house. I stayed on top of schoolwork pretty easily as well, so there was plenty of time to do other stuff at night."

        show hanako basic_distant_cas
        with charachange

        "Our conversation dies down, with Hanako's timidity getting the better of her. In response, I get off the table and let her take her turn shooting."

        scene ev hanako_billiards_smile
        with locationchange

        "There aren't many solids in easy positions, so Hanako bends down and takes a while to line herself up properly."

        scene ev hanako_billiards_smile_close:
            truecenter
            zoom 1.0
            easein 6.0 zoom 0.8
        with flash

        "Hanako's expression is the same as when we play chess; a relaxed but focused concentration. Athletes sometimes talk about getting into a zone where nothing unnecessary enters their mind, and I wonder if that's something she can do."

        "Her posture is good. Better than mine, to be sure. It's very close to a textbook method of playing, whereas I tend to contort myself into whatever position I feel is most natural for the shot I'm taking."

        scene ev hanako_billiards_serious
        with charachangeev

        "She lines up the cue. The cue comes back, and she does a couple of practice movements to make sure she's lined up correctly."

        "Hanako takes games so seriously. It's the only real hobby I know she has, outside of reading. It feels good to be able to share this kind of experience with her."

        scene bg city_clubpool
        with flash

        play sound sfx_billiards

        "She takes the shot after careful consideration, and the cue ball zooms off towards a ball sitting at a slightly awkward angle near a corner."

        "Hanako's careful preparation pays off as the cue ball hits and sends the ball rolling towards the corner pocket. For a moment it looks like it'll stop just on the lip of the hole, but it eventually tilts just enough to drop in."

        hi "Man, that was a hard shot. If you can pull that off, I don't think I have much hope."

        show hanako emb_emb_cas at center
        with charaenter

        ha "I'm not… th-that good…"

        hi "It's not just the shot though; even when lining it up you looked really serious. You're like this with chess, too."

        show hanako emb_downsmile_cas
        with charachange

        "The praise makes her a little flustered. She sets the cue against the table and stands, turning to me."

        ha "I just… like those kinds of things…"

        "Her fingers are twisting and turning tightly."

        show hanako emb_downtimid_cas
        with charachange

        ha "When I was in the orphanage… I just… k-kept doing the things I liked… before."

        ha "If I p-played games with the others, th-that was enough for the helpers there, so…"

        "I'd never thought about it that way. Staff at an orphanage would naturally want to have everyone socialize at least a little."

        hi "If it's okay for me to ask… what was it like for you at the orphanage?"

        show hanako emb_sad_cas
        with charachange

        ha "W-why do you want to know?"

        "I've touched a nerve, but the fact that she responded at all shows there's at least a chance she'll answer my question. Before, she likely would just have shrunk away from it without a word."

        show hanako emb_blushing_cas
        with charachange

        ha "I'll… tell you, but…"

        hi "But…?"

        show hanako cover_worry_cas
        with charachange

        ha "Could you… t-tell me who I-Iwa… n-nako… is?"

        $ renpy.music.set_volume(0.2, 1.0, channel="music")

        hi "Iwanako…? Oh, the letter."

        "I wonder how long she's been waiting for the right opportunity to ask me this. I'm surprised, but don't hesitate. Sharing information is naturally a matter of give and take."

        $ renpy.music.set_volume(1.0, 8.0, channel="music")
        $ renpy.music.set_volume(0.4, 0.0, channel="ambient")
        play ambient sfx_crowd_indoors fadein 8.0

        hi "She's… someone I used to like."

        show hanako basic_normal_cas
        with charachange

        "Her nervousness subsided, at least for the time it took to ask. Her curiosity is getting the better of her, and I feel a bit uncomfortable to be questioned on this, of all matters."

        "There's no way I could spill out all my feelings about Iwanako here. I don't even know myself what my feelings regarding her are, even after talking to Yuuko earlier, and I want to avoid the subject around Hanako."

        show hanako def_worry_cas
        with charachange

        "Hanako doesn't look overly satisfied with the awkward ending to the discussion, but thinks better of continuing it. She was only just managing to ask me in the first place, without knowing that I wouldn't want to talk about it."

        "I move to finally take my own shot. The lack of talking between us is filled by the chatter of other patrons and the band at the other end of the club."

        hide hanako
        with charaexit

        "Spying a shot that doesn't look too difficult, I try and shoot for it."

        play sound sfx_billiards

        "The cue ball taps the ball, and the trajectory is about right, but I put in too much power. It grazes the corner of the hole and moves off to the side, just skirting the pocket."

        "I grit my teeth a little. I was pretty good at this game, and it's frustrating to have deteriorated so much."

        "I step back and let Hanako take her turn, glancing towards the counter where Lilly and Akira are sitting. They're talking busily between themselves, and seem to be having a good time."

        scene ev hanako_billiards_serious
        with locationchange

        "I turn back to Hanako as she takes her shot. With the same face as before, she lines herself up and sharply pushes the cue."

        scene bg city_clubpool
        with flash

        play sound sfx_billiards

        "Just as before, she sinks the ball she was aiming for. It drops into the side pocket more cleanly than her last, though. It looks as if she's getting a bit more into the groove of the game."

        hi "Nicely done."

        "She hesitates for a moment, and begins to address me without turning her head."

        scene ev hanako_billiards_smile_med
        with locationchange

        ha "The orphanage… was nice. It felt a bit like Yamaku does… and the staff was r-really kind."

        show ev hanako_billiards_distant_med
        with charachangeev

        ha "But as th-the years went on, I realized something. I was d-different."

        "It feels strange to hear her speak so candidly about herself. She's audibly forcing the words out. It reminds me of when she insisted she tell me about the fire."

        "Hanako must feel that she has to tell me of such things, if I'm willing to tell her about my own past."

        "Her grip on the cue tightens as she continues to speak."

        show ev hanako_billiards_timid_med
        with charachangeev

        ha "M-most of the children there were up for adoption, just like I was. But unlike me… they gradually left, o-one by one. By the time I went to Yamaku, I was… among the oldest children there."

        ha "For a while, I h-helped with some of the y-younger children, b-but eventually…"

        scene bg city_clubpool
        with locationchange

        "I lay a hand on her shoulder. She's forcing herself by now."

        hi "It's okay."

        show hanako emb_blushtimid_cas_close at center
        with charaenter

        "She looks mildly surprised for a moment, but then nods before setting down her cue and turning towards me."

        show hanako basic_worry_cas_close
        with charachange

        ha "Do you… really think so?"

        hi "Yeah, I think so. Even while Lilly's away, I'll be around to protect you, right?"

        show hanako basic_normal_cas_close
        with charachange

        "Hanako looks at me for a long time, and I'm taken a bit off guard."

        "Her expression hasn't changed from before, still looking somewhat maudlin, and silences between us aren't unusual. I think it's the fact that she's holding such prolonged eye contact that makes this feel a bit odd."

        "It feels as if she's judging me. It's a very strange, vaguely uncomfortable feeling."

        hi "Hanako…?"

        show hanako cover_smile_cas_close
        with charachange

        ha "I-I understand. Thank you."

        "She smiles and looks away a little, but it feels stilted. Hanako isn't very good at faking emotions, and this is no exception."

        hide hanako
        with charaexit

        "I move to the table and take my turn to try and distract myself, but it doesn't seem to work. Does she think I'm not up to the task of helping her? Is she disappointed in me?"

        "I'm probably overthinking this. While her silences are just an accepted fact of life by now, sometimes I do wish she'd speak more."

        play sound sfx_billiards

        "With a thud, I send the white sphere careening down the table into my target."

        show hanako def_strain_cas at center
        with charachange

        ha "Ah…"

        "Hanako sees what's happening just as I do. The ball hits hard, with the striped ball I'd intended to sink veering off towards the eight ball."

        "Sure enough, as both Hanako and I look on and bite our lips, they connect and the black ball rolls leisurely into a corner pocket."

        show hanako basic_smile_cas
        with charachange

        "All I can do is sigh. It looks like Hanako is smiling again though, so maybe it wasn't for naught."

        hi "That was an awful shot, you win. It seems I'm getting pretty rusty after all this time."

        hide hanako
        with charaexit

        "Hanako bends down and begins to shoot the remaining balls into the closest pockets. I almost ask if we could play another game, but a quick check of my watch confirms that the night is getting pretty late."

        "Lilly and Akira appear to be still drinking at the counter. Seems like we'll have to drag them away."

        ha "Um, Hisao…"

        scene ev hanako_billiards_distant
        with locationchange

        "I turn back to Hanako, who's still looking over the pool table shooting balls. Her voice sounds different from before."

        scene ev hanako_billiards_smile
        with charachangeev

        ha "I'm… here for you as well…"

        stop ambient fadeout 2.0

        hi "Ah…"

        "I suddenly find myself blushing. It's only natural that she'd respond this way, given what I said earlier, but it's still a shock to actually hear it."

        scene ev hanako_billiards_smile_close:
            xalign 0.0 yalign 0.0 zoom 0.8
            acdc_warp 20.0 zoom 1.0
        with charachangeev

        "Just what is my relationship with this girl? I want to protect her, to make her happy… I'm not really sure that it's something like love, but I don't think these are the same kinds of feelings I have for Lilly, either."

        "I feel sorry for her, having gone through so much in her life. Her parents died in a housefire, and she lived in an orphanage for much of her childhood… I can't even imagine that kind of life."

        "But I feel like there's so little I can do for her, especially now that Lilly is going to be leaving the country."

        stop music fadeout 10.0

        $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
        play ambient sfx_traffic fadein 4.0

        scene bg city_karaokeext
        show akira basic_boo_ni:
            center
            xpos 0.39
        show lilly cane_smileclosed_cas_ni:
            center
            xpos 0.21
        show hanako basic_normal_cas_close_ni at tworight
        with locationskip

        "Hanako and I finish tidying up the table and cues, and pick up Lilly and Akira on our way out of the club."

        "It feels like something changed between Hanako and me. I can't quite place what it is, but Hanako is acting differently now. I feel like we're further apart, if anything."

        show akira basic_smile_ni
        with charachange

        aki "So, you enjoy yourselves?"

        show hanako emb_smile_cas_close_ni
        with charachange

        "Hanako and I both nod and agree. The game was good, and we both did learn more about each other, so it's a honest answer."

        show lilly cane_sleepy_cas_ni
        with charachange

        "Lilly appears to be a little distracted."

        hi "Worried about the trip, Lilly?"

        "She pauses before sighing and smiling weakly."

        show lilly cane_weaksmile_cas_ni
        with charachange

        li "A little. It means quite a bit."

        show akira basic_laugh_ni
        show lilly cane_surprised_cas_ni
        with vpunch

        "The comment earns her a clap on the shoulder from her sister. Hanako smiles back, too."

        show hanako basic_smile_cas_close_ni
        with charachange

        ha "You'll be okay, Lilly. I hope you can enjoy your time over there."

        show lilly cane_smile_cas_ni
        with charachange

        li "Thank you, Hanako. I'll try to. It will be nice to be back with my family, after all, no matter for how brief a time it may be."

        "With that, the four of us begin the walk to the carpark where Akira's car is. We continue to talk between ourselves, but it's mostly just smalltalk."

        stop ambient fadeout 2.0
        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .beginning_of_the_end:
        play music music_daily fadein 2.0

        scene bg school_girlsdormhall
        show lilly basic_smile_cas at twoleft
        show hanako basic_normal_cas at tworight
        with locationchange

        hi "Right then. Are you taking the bus, Lilly?"

        show lilly basic_smileclosed_cas
        with charachange

        "Lilly motions to a large suitcase standing beside her."

        show lilly basic_weaksmile_cas
        with charachange

        li "I'll have to take this with me, so I've booked a taxi. It'll meet us at the school gates in about five minutes."

        hi "Ah, I see."

        show lilly basic_sleepy_cas:
            ypos 1.1
        with charamovechangefaster

        "Lilly reaches down and feels out the handle of her suitcase. Its weight causes her some difficulty, so I quickly offer to take it myself."

        show lilly basic_smileclosed_cas at twoleft
        with charamovechangefaster

        li "That is awfully kind of you, Hisao."

        "She has no qualms about accepting, and I end up picking it up. It's not what I'd call light, but it's not exactly heavy, either. I don't think I'll have too much trouble carrying it."

        show lilly basic_weaksmile_cas
        with charachange

        li "Well, thank you then. We should hurry though, if the taxi leaves then it will take quite a while to book a new one. Are you ready, Hanako?"

        show hanako cover_worry_cas
        with charachange

        ha "Y-yeah. Let's go."

        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
        play ambient sfx_parkambience fadein 2.0

        scene bg school_gate at bgright
        with locationskip

        "We rush to the gate as fast as we can, only to find that the taxi has yet to arrive."

        hi "Well, nothing like a bit of exercise in the morning. The nurse told me that I should be doing that."

        show lilly basic_weaksmile_cas at center
        with charaenter

        li "I think he probably had other things in mind, Hisao. And probably with more regularity. Do you intend to be helping people with their luggage every day?"

        hi "I guess not. Looks like we've got a bit to wait anyway. How long should we wait for the taxi before calling them again?"

        show lilly basic_smileclosed_cas
        with charachange

        li "I would say another ten minutes, but they've never let me down before. There's probably just a little traffic."

        hi "Okay then."

        hi "So how long is the flight to Scotland?"

        show lilly basic_smile_cas
        with charachange

        li "About sixteen hours, if I remember correctly. It's a bit hard to tell with the changing time zones."

        show bg at center
        show lilly at twoleft
        with charamove

        show hanako defarms_worry_cas at tworight
        with charaenter

        ha "So long…"

        "It's now that I realize Hanako's been unusually quiet, even for her. She doesn't handle stress well, so she's looking really uptight."

        hi "Yeah, I can't imagine being on a plane for that long."

        "I've only ever flown on a short family holiday up north, so it really is quite hard to fathom. If Hanako's spent so much of her childhood at an orphanage, she's probably traveled very little, let alone flown."

        show lilly basic_weaksmile_cas
        with charachange

        li "It's not too bad. I'll spend most of it either asleep or catching up on my English. I hardly use that here so I need to refamiliarize myself with it a little."

        show hanako cover_worry_cas
        with charachange

        ha "W-will your accent… be a problem?"

        show lilly basic_smile_cas
        with charachange

        li "I wouldn’t worry about that too much. It may be an issue initially, but I should be fine once I get used to it."

        show hanako basic_worry_cas:
            ypos 1.14
        show lilly basic_smileclosed_cas:
            ypos 1.17
        with charamovechangefaster

        "We all move to sit down on the small bench beside the school gate in silence."

        "Strangely enough, even though I know that Lilly is going away, I can't think of anything to say to her. Lilly is a reliable person, so it might be because she isn't the one that I'm thinking of most."

        show hanako emb_downsad_cas
        with charachange

        "Lilly might not be able to see it, but Hanako's chewing her fingernails nervously. I move to talk to her, but can hear an engine straining up the hill before I get the chance."

        hi "Ah, I think the taxi is on its way…"

        show lilly basic_cheerful_cas
        with charachange

        li "Well spotted Hisao, I only just heard it as well."

        "A small wave of pride washes over me. To have noticed something at the same time as Lilly must mean that I've become more aware of my surroundings."

        "Anyway, we won't have to call the taxi company, nor worry about missing Lilly's plane."

        show hanako basic_worry_cas at tworight
        show lilly basic_smileclosed_cas at twoleft
        with charamovechangefaster

        "Once the taxi stops where we're standing, the driver rolls down a window and leans over. After confirming that, yes, Lilly is the same Lilly Satou that booked the trip, we sort out her luggage."

        hide lilly
        with charaexit

        "The driver opens the trunk of the taxi and takes Lilly's suitcase, with Lilly climbing into the back seat as he loads it into the trunk and slams it shut."

        "After getting back into his seat and shutting the doors, he waits for us to say our farewells."

        show hanako emb_downtimid_cas
        with charachange

        ha "Have a safe trip, Lilly."

        hi "Take care of yourself."

        "Hanako looks understandably downcast, and that much is obvious even in her voice."

        li "Of course I will. I'll be back before long, don't worry. There will still be another person here for you too, won't there, Hisao?"

        hi "Yeah, of course."

        show hanako emb_blushtimid_cas_close
        with characlose

        "I turn and smile to Hanako, putting my hand on her shoulder."

        show hanako emb_downtimid_cas_close
        with charachange

        "She only manages to keep eye contact with me for a couple of seconds, her cheeks red all the while, before turning back to Lilly."

        hi "See you, Lilly."

        show hanako basic_worry_cas_close
        with charachange

        ha "Good bye!"

        stop music fadeout 6.0

        "Lilly gives her farewells to the both of us with a fair measure of reluctance. Without further ado, the driver starts the engine once more and they begin the journey down the hill, and towards the airport."

        "The two of us stand at the gates for a long time even after they've disappeared from sight, not really knowing what to do."

        show bg at bgleft
        show hanako at center
        with charamove

        hi "So, what do you want to do?"

        show hanako def_worry_cas_close
        with charachange

        ha "I… don't know."

        menu:
            with menueffect

            "Do you want to go into the city?":
                $ go_to_the_city = True

                call a3hc2o1
            "How about we call it a day?":
                $ go_to_the_city = False

                call a3hc2o2

        if _in_replay:
            return

    return

label a3hc1o1:
    hi "To be completely honest… yeah, I do. I'd appreciate it if you didn't tell anyone."

    show miki wink
    with charachange

    mk "Hey, whoa, you can trust me. No problems there."

    show miki grinclosed
    with charachange

    mk "To be honest, I think it's kind of cute. If you want to go for it, don't let me stop you."

    hi "Thanks."

    "She may say that, but she was just talking about Hanako having 'issues.' Still, I want to hold myself to the words I said. Hanako's problems don't matter; I'll deal with anything that comes up, because I want to help her."

    "If there's even the smallest possibility that I can pull Hanako out of her depression and seclusion, then I should work towards that, no matter what. If she needs a prince, then I will be that prince."

    "As I think about the possibility of a relationship, I can see Miki grinning at me while watching my face. I'm no doubt blushing, and looking away from her only makes her laugh."

    return

label a3hc1o2:
    hi "I don't think so. We're just friends."

    show miki serious
    with charachange

    mk "Aw. I thought I'd discovered something nice for a moment there. I understand; girls and guys don't need to be boyfriends and girlfriends, after all."

    "What she says is true, even if I do have feelings for Hanako. Right now we are good friends, and I don't want to mess that up, but I also want to be more than that for her. It's hard."

    return

label a3hc2o1:
    scene bg school_gate at bgleft
    show hanako def_worry_cas_close at center

    $ renpy.music.set_volume(0.5, 0.0, channel="ambient")

    "The bus stop, standing by the school gates like a mute sentinel, puts a strange idea in my mind."

    hi "Do you want to head into town and look for a bookshop or something? We have the rest of the day free."

    "It's a long shot, as Hanako doesn't like going into the city. I count the fact that we managed to get her out there even when it was so dark as a small miracle, but I genuinely want to spend more time with her."

    "Anyway, she's likely to just refuse and go back to…"

    show hanako basic_smile_cas_close
    with charachange

    ha "Okay."

    hi "Really?"

    show hanako basic_bashful_cas_close
    with charachange

    ha "R-really. Let's go."

    "I can't work out why Hanako has decided to agree with me, but I'm not about to ask her to change her mind."

    stop ambient fadeout 2.0

    scene bg city_street2
    show crowd
    with shorttimeskip

    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    play ambient sfx_crowd_outdoors fadein 2.0

    "Stepping off the bus, I immediately notice that a lot of people are around us. In hindsight, it should have been obvious; of course lots of people will be downtown on a Saturday afternoon."

    show hanako emb_downtimid_cas_close at center
    with charaenter

    "Hanako retreats close to my side, and I can feel her hand clutching my arm tightly. Her body is held against mine and her head is bowed so low that her hat hides most of her scarring."

    hi "So uh, where shall we go? A bookshop?"

    "Hanako's present and my other general living expenses have pretty much drained my budget, but I should be able to afford a few books. They're something I try to reserve a few funds for anyway."

    "For a second I think Hanako didn't hear me, but then I look to my side and notice her nodding almost imperceptibly."

    show hanako emb_smile_cas_close
    with charachange

    ha "O-okay. D-do you know of one?"

    hi "Actually, I do. We passed a few when Lilly and I were looking for your presents…"

    show hanako emb_downsad_cas_close
    with charachange

    "Hanako's expression clouds a fraction. I've got to remember to stop bringing up her birthday."

    show hanako emb_timid_cas_close
    with charachange

    ha "You both… spent a lot of time?"

    "Or maybe I misjudged the situation."

    hi "We wanted to make sure we got the right present, after all."

    show hanako emb_smile_cas_close
    with charachange

    "Hanako smiles and blushes a bit. It's a small treasure when she does."

    hi "Anyway, there should be a bookshop just up ahead, do you want to check it out?"

    show hanako basic_bashful_cas_close
    with charachange

    ha "S-sure."

    scene bg city_street1
    show crowd
    with locationchange

    "The crowds start to build as we head towards the bookshop along the raised walkways. Hanako latches her other arm onto me as well, making our progress a little slower."

    "As we walk, the sound of the traffic makes me think of a possible distraction for her."

    hi "I was wondering, Hanako… have you thought yet about when you're going to learn to drive?"

    show hanako cover_worry_cas_close at center
    with charaenter

    ha "D-driving?"

    hi "Yeah. You're kind of lucky, in a way; there aren't a whole lot of students in Yamaku that are allowed to drive."

    "It's not the best topic of conversation, but I want to try and distract Hanako from the situation. She's really highly strung right now."

    "Then again, all I've really done is make her feel awkward, since she's probably never thought about it. I wish I hadn't said anything."

    stop ambient fadeout 0.5

    scene bg city_street3 at left
    with locationchange

    $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
    play ambient sfx_traffic fadein 1.0

    "Before long we are before one of the bookshops Lilly and I passed by during our search."

    hi "What kind of self-respecting bookshop closes on Saturdays?"

    show hanako def_worry_cas_close at center
    with charaenter

    ha "Bookshops… don't make much money any more, because of the Internet. Maybe they just had to close over weekends?"

    "She seems pretty knowledgeable about technology. I guess it's a pursuit that would lend itself well to someone who enjoys solitude."

    hi "Huh, I guess that makes sense… it's easier to find books online. Anyway, it looks like this idea is shot. Anything else you'd like to do?"

    show hanako emb_smile_cas_close
    with charachange

    ha "I-if it's not… not a bother… could you show me where you bought my present?"

    hi "Sure, not a problem. It's not far from here."

    hide hanako
    with charaexit

    show bg at right
    with charamove

    "I head off in the direction of the store, only half-sure of its exact location. I don't want a repeat of the last time; spending half the day walking around aimlessly."

    hi "Here we are, Othello's Antiques."

    show hanako basic_normal_cas_close at center
    with charaenter

    ha "I-it's small."

    hi "Well, yes. It took Lilly and me some time to find it."

    show hanako basic_distant_cas_close
    with charachange

    ha "Can we go in?"

    hi "I don't see why not; it's open."

    stop ambient fadeout 0.5
    play sound sfx_storebell
    play music music_soothing fadein 0.5

    scene bg city_othello
    with locationchange

    "Hanako pushes through the door and enters before me. Once again, the store is empty save for the store owner."

    show shopkeep neutral at center
    with charaenter

    "His face drops a little when he sees me."

    sk "Oh, you're not here for a return are you? Wait, that's not the girl you had with you last time…"

    hi "Er, no, we're not here to return anything. We were just in town and wanted to have another look in here."

    show shopkeep thinking
    with charachange

    "The store owner considers this for quite a long time. I guess he's not used to high school students coming to his shop on a regular basis."

    show shopkeep happy
    with charachange

    sk "Might this be the friend you bought gifts for?"

    hi "That's right. They were presents for her."

    show shopkeep at twoleft
    show bg at bgleft
    with charamove

    show hanako defarms_strain_cas_close at tworight
    with charaenter

    "The store owner turns to Hanako, who freezes on the spot like a deer caught in the headlights."

    show shopkeep surprised
    with charachange

    "He moves to address her, but stops before doing so, looking a little taken aback."

    show shopkeep thinking
    with charachange

    "He catches himself staring and looks to the side, addressing us indirectly. His expression is awkward and tense, as is his entire body."

    "I want to be mad at him, but I know full well that I had the same instinctive reaction when I first saw her. First surprise, then curiosity, then an awkward look away as I dealt with what I'd seen."

    show hanako emb_downsad_cas_close
    with charachange

    "Hanako looks less panicked than before… but I think the feeling she's giving off now is worse. It's not anger, nor annoyance. If anything, it's one of apology."

    show shopkeep neutral
    with charachange

    sk "You're lucky there, young lady. To have friends that care about you as much as they do."

    show hanako emb_downtimid_cas_close
    with charachange

    ha "Th-thank you…"

    "If I hadn't spent so much time with Hanako I wouldn't even have realized that she said anything. Then again, the store owner's mumble was hardly clear either, thanks in part to being directed away from us."

    hide hanako
    with charaexit

    show shopkeep:
        ease 1.0 xpos 0.6 alpha 0.0
    with None

    show bg at left
    with charamovefaster

    hide shopkeep

    "Hanako strikes out into the store, gazing in wonder at the various items on display. She finds the doll section, and spends lingering minutes studying each and every one."

    "It's a side of Hanako I've only barely been introduced to. I was astonished when Lilly said she liked dolls, and even more so to find her 'collection' sitting on her dresser."

    show hanako basic_normal_cas_close at center
    with charaenter

    "She looks a little better now that she's distracted and out of the store owner's sight, but I'm still quite put off by the whole experience."

    "I might have my own problems, but I've never had strangers react to me like that, as if I was something completely alien to them."

    show hanako basic_smile_cas_close
    with charachange

    ha "This is a nice shop."

    hi "Yeah, it's not what I expected. Do you want to buy something?"

    show hanako cover_worry_cas_close
    with charachange

    ha "I-I didn't bring any money."

    hi "Well, we can always come again."

    "Now that I know where to find it, that is."

    show hanako cover_bashful_cas_close
    with charachange

    ha "W-we can?"

    hi "Of course. We can come here as often as you'd like."

    show hanako basic_bashful_cas_close
    with charachange

    ha "Th-thank you."

    hi "You don't need to thank me; I almost forgot where this place was."

    "I don't really think either of us completely believes in what we're saying, but rather, we're just repeating what we think we should say."

    show hanako emb_smile_cas_close
    with charachange

    ha "C-can we go back to the school now?"

    hi "Sure thing. Let's go."

    stop music fadeout 5.0
    play ambient sfx_traffic fadein 2.0

    scene bg city_street3 at right
    with locationchange

    "As we leave for the bus stop, I see the store owner peek through the curtain at the back of the shop."

    "I'm not really sure what that glance he gives to her says. It feels a bit weird, and the fact that Hanako didn't see it is both a relief and a bit frustrating."

    stop ambient fadeout 2.0

    scene bg school_dormext_full
    with shorttimeskip

    "Hanako and I stop walking once we reach the concrete area between the dormitory buildings. There was barely a word said between us on the way back from the city."

    show hanako basic_bashful_cas at center
    with charaenter

    ha "Well then, goodbye."

    hi "Do you want to have some tea or something? How about a game?"

    show hanako emb_emb_cas
    with charachange

    "Hanako shakes her head embarrassedly."

    ha "I… I'm tired. Maybe later? I've got homework…"

    "She sounds a little depressed. Hanako obviously does want to do more, but I suppose she would have a bit of schoolwork to catch up on; she's missed a few days of lessons."

    hi "Ah, homework. Thanks for reminding me; I've got a stack to do as well. I guess I'll see you tomorrow."

    show hanako basic_smile_cas
    with charachange

    ha "See you, Hisao."

    hide hanako
    with charaexit

    "Before I can say goodbye, Hanako has turned and begun walking towards the entrance to the female dormitory building."

    "I look at the door she disappears through for a bit, before going off towards my own dorms."

    "Today was a tiring day."

    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")

    return

label a3hc2o2:
    scene bg school_gate at bgleft
    show hanako def_worry_cas_close at center

    $ renpy.music.set_volume(0.5, 0.0, channel="ambient")

    hi "I don't know about you, but I think I'm going to try and take a nap. My head is killing me."

    show hanako basic_distant_cas_close
    with charachange

    "Judging by Hanako's instant relief, I can only assume that I've guessed right. I don't think she wants to be out and about."

    hide hanako
    with charaexit

    "Wordlessly, she turns and heads back through the school gate."

    scene bg school_dormext_full
    with locationskip

    "We walk all the way back to the dorms together, stopping awkwardly at the spot where we need to part."

    show hanako cover_distant_cas at center
    with charaenter

    ha "Well then, g-goodbye."

    hi "Do you want to have some tea or something, later? How about a game?"

    show hanako emb_timid_cas
    with charachange

    "Hanako shakes her head embarrassedly."

    show hanako emb_downtimid_cas
    with charachange

    ha "I… I'm tired. Maybe tomorrow? I've got homework…"

    "I suppose she would have a bit of schoolwork to catch up on; she's missed a few days of lessons, after all."

    hi "Ah, homework. Thanks for reminding me; I've got a stack to do as well. I guess I'll see you tomorrow."

    show hanako emb_downsmile_cas
    with charachange

    ha "See you, Hisao."

    hide hanako
    with charaexit

    "Before I can say goodbye, Hanako has turned and begun walking towards the entrance to the female dormitory building."

    "I look at the door she disappears through for a bit, before going off towards my own dorms."

    "Tomorrow will be a better day."

    stop ambient fadeout 1.0
    $ renpy.music.set_volume(1.0, 2.0, channel="ambient")

    return
