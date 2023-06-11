# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a1_wednesday:
    call timeskip

    label .lunch_evolution_theory:
        play music music_happiness fadein 2.0

        scene bg school_scienceroom
        with locationchange

        "I feel very tired this morning, probably because yesterday itself was a very tiring day. On top of that, I woke up far earlier than necessary."

        "After saying hi to Shizune and Misha, I start doing the work as instructed from the board. It already looks like today is going to be heavy."

        "I don't have a problem with that now, though. Shizune and Misha might jump on me trying to get an answer about whether or not I've decided to join the Student Council, even if it's just one day."

        "I wouldn't put it past them to try, and I don't have an answer for them if they do. So, this situation is convenient for me."

        "About ten minutes into class, Hanako walks in and takes a seat, but no one looks at her. The teacher doesn't even comment on her lateness."

        "He does, however, stop us to say that we're going to break into groups again."

        show shizu behind_smile at tworight
        show misha perky_smile at twoleft
        with charaenter

        "I turn my head and see that Shizune and Misha are looking at me. Shizune gives me a smile that is equal parts cute and menacing. This is a smile that says 'We have you now. There is no escape.'"

        show misha hips_grin
        with charachange

        mi "Hicchan~, it looks like we're together again! Yay yay~!"

        show misha hips_grin_close
        show shizu behind_smile_close
        with characlose

        "Misha leans sideways while Shizune pushes her desk closer to mine. There really is no escape now unless I were to jump through the window."

        "Jumping out the window isn't the best option, sadly."

        show shizu adjust_smug_close
        with charachange

        shi "…"

        show misha hips_smile_close
        with charachange

        mi "What's wrong, Hicchan?"

        show shizu adjust_happy_close
        with charachange

        shi "…"

        show misha perky_smile_close
        with charachange

        mi "Oh… Hicchan, have you been thinking about what you said yesterday? You said that you would think about joining the Student Council, didn't you?"

        show misha hips_grin_close
        with charachange

        mi "It's okay, Hicchan. We were talking about it after you left, and it would be rude to expect you to already have an answer for us this early, right? Right~!"

        show misha cross_laugh_close
        with charachange

        mi "Hahahahahaha~!"

        "I'm so happy you two are able to have a laugh at my expense, and even more pleased to know that you both know how crazy the two of you can be."

        show shizu basic_normal2_close
        show misha perky_smile_close
        with charachange

        "Now that that's over, Shizune snaps back into serious mode and smacks today's assignment with the back of her hand in an overly dramatic and important way."

        "When I actually look at the stuff, it's mostly just reading. In fact, there are only two problems."

        "I almost want to say something about how her rush to get started seems a bit much, considering the small amount of work. In fact, Shizune probably knows how little there is, and simply doesn't care."

        "Yeah, it seems like the workload doesn't matter to her as much as the fact that there is work; the actual amount is unimportant. She approaches everything with the same level of ambition."

        show hanako emb_downtimid at offscreenright
        with None

        show hanako at right
        show shizu:
            xalign 0.4
        show misha:
            xalign -0.3
        show bg at bgleft
        with charamove

        stop music fadeout 7.0

        "While I'm reading, I let my eyes wander around the room and catch Hanako trying her hand at solving the problems. It looks like she's working alone."

        "I can't remember seeing her working with other people before."

        "Thinking back to how shy she is, it's understandable."

        hi "Hey, that girl over there…"

        show misha perky_confused_close
        with charachange

        mi "Huh? Who, Hicchan?"

        hi "Her. Hanako. Over there. Does she always work alone?"

        mi "I think so, Hicchan. Do you feel sorry for her because she's alone?"

        hi "I was just thinking that maybe she could work with us, or something."

        show misha perky_sad_close
        with charachange

        mi "Hmmmm… No, I don't think that would be a good idea, Hicchan."

        hi "Why not?"

        mi "Shicchan wouldn't get along with her."

        hi "Why?"

        show misha perky_confused_close
        with charachange

        "Misha shuffles around the question, letting out a laugh that sounds very strange; it's nervous, but still has that lilting up-and-down quality present in everything she says."

        mi "Just because, Hicchan."

        "By now, Shizune has noticed our conversation, and it makes me realize again how Misha has been signing everything she has been saying this whole time."

        show shizu basic_frown_close
        with charachange

        shi "…"

        show misha perky_sad_close
        with charachange

        mi "What, Shicchan? The friend of my enemy is my enemy? That sounds so harsh, I'm not going to say that."

        hi "You said it anyway."

        show misha hips_grin_close
        with charachange

        mi "I know, Hicchan, it's fine if you overhear~!"

        "I wonder if this is Misha's way of keeping things fair, since without her, I wouldn't be able to understand a thing Shizune is saying, and vice versa."

        "Is that also why she signs all the time, so there is never a conversation Shizune will be left out of?"

        show shizu basic_normal_close
        with charachange

        shi "…"

        show misha perky_smile_close
        with charachange

        mi "Anyway, we should start on the problems now, Hicchan."

        scene bg school_scienceroom
        with shorttimeskip

        play music music_daily fadein 1.0

        "We finish with time to spare, and I decide to ask if there are any alternatives to the cafeteria, as frankly, the food so far has been subpar."

        "This sends Shizune and Misha arguing among themselves about their favorite restaurants. All of them are downtown, so I don't think we have time to go all the way there. And what about the bill?"

        "Are they arguing just for the fun of it?"

        "Maybe. They seem so distracted by it that they don't even notice the start of the actual lunch break."

        "I look over my shoulder towards the back of the classroom."

        show hanako emb_downtimid at tworight
        with charaenter

        "She seems to be studying her notes from the previous class."

        "It's an odd sight; everyone else in the class is busying themselves with the lunch break."

        "Socializing, gossiping, rearranging desks, the ones with actual boxed lunches mixed in and chattering like everyone else, only interrupted by short bouts of eating."

        "But, when I watch Hanako, it feels that I'm the only one who can see her. Almost as if she was invisible; sort of hiding in plain sight."

        "Is she being bullied? Is she isolating herself from the rest of the class on her own accord?"

        show hanako emb_timid
        with charachangealways

        show hanako emb_downtimid
        with charachangealways

        "I see her look over her shoulder towards the classroom's rear door."

        "Come to think of it, she hasn't turned a page since I've started watching her."

        "I guess she's waiting for someone."

        menu:
            set choices
            with menueffect

            "What to do…"

            "Read my book.":
                call a1c6o1

            "Go talk with Hanako." if attraction_hanako > 1 or _in_replay:
                $ talk_with_hanako = True

                call a1c6o2

            "Wait for Shizune and Misha to come to a decision." if attraction_sc > 1 or _in_replay:
                $ wait_for_shizu = True

                call a1c6o3

    if not talk_with_hanako:
        label .short_sharp_shock:
            scene bg school_hallway3
            with locationchange

            play ambient sfx_emisprinting fadein 3.0

            "Just around the corner of the hallway something hits me in the chest with the force of a runaway train."

            call separate_of_sss_and_mc

            "I feel a hand on my shoulder at the same time the girl's eyes widen in horror and whatever she was saying gets interrupted by a very horrified—{w=.9}{nw}"

            show emi basic_hes_gym
            with charachange

            emi_ "Eep!"

            show misha hips_frown behind emi at offscreenleft
            show shizu cross_rage behind emi at offscreenleft
            with None

            show bg at center
            show emi at right
            show shizu:
                xalign 0.4
            show misha at left
            with charamove

            "I don't have time to look behind me because Shizune is already shoving me aside and stomping over to the girl, signing furiously at her."

            show misha hips_grin
            with charachange

            mi "Miss Ibarazaki, I saw that. Running in the halls is strictly forbidden."

            "Misha translates, right on Shizune's tail, but her voice is girlishly playful, not full of the divine fury Shizune's arm movements would seem to call for."

            show emi basic_closedsweat_gym
            with charachange

            emi_ "Er, sorry, I was just going to get some stuff, and I was in a kind of a hurry."

            show shizu adjust_angry
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "You've been told this a thousand times before. Your reckless behavior endangers other students, and even worse, it's explicitly against the school regulations."

            show emi sad_depressed_gym
            with charachange

            "The girl blushes and starts to fidget nervously like a little child caught misbehaving."

            "It's so cute I find myself smiling."

            emi_ "I know that! I— I, um, I was just…"

            show shizu cross_angry
            with charachange

            shi "…"

            show misha cross_smile
            with charachange

            mi "Make sure that this will not happen again… although I'm sure telling you this is futile, and only causes me further headache when you choose to ignore the regulations."

            show misha cross_grin
            with charachange

            mi "Got that, Emi?"

            show emi sad_annoyed_gym
            with charachange

            "The small girl sticks her tongue out in response."

            show emi basic_hes_gym
            with charachange

            emi "Aaah!"

            emi "I gotta go!"

            emi "Teacher'll have my head! I promised to help with printouts, but I went running instead! Sorry, but I've gotta change and everything!"

            play sound sfx_emisprinting
            stop music fadeout 1.0

            show emi at offscreenleft
            with charamovefaster

            hide emi

            stop sound fadeout 1.5

            "Before Misha or Shizune or I can say anything, she's already bolted from where she was a second ago, almost halfway towards the stairwell."

            show shizu at tworight
            show misha at twoleft
            show bg at bgright
            with charamove

            play music music_normal fadein 3.0

            "Shizune looks like she's about to go nuclear on the spot, so I smile at her in a vain attempt to calm her down."

            show shizu basic_frown
            with charachange

            shi "…"

            show misha perky_smile
            with charachange

            mi "Are you okay, Hicchan? That Ibarazaki girl is always like that, causing trouble to others."

            hi "You know, I'm pretty certain Shizune wouldn't call me 'Hicchan.'"

            show misha hips_grin
            with charachange

            mi "Never mind, never mind!"

            "…"

            hi "Yeah, anyway, I'm okay. Just got the wind knocked out of me."

            show shizu basic_normal
            with charachange

            shi "…"

            show misha cross_grin
            with charachange

            mi "That's great, Hicchan!"

            "I wouldn't call that great, but I let it slide this one time."

            if wait_for_shizu or _in_replay:
                $ renpy.music.play(music_normal, fadein=3.0, if_changed=True)

                show shizu adjust_happy
                with charachange

                shi "…"

                show misha perky_smile
                with charachange

                mi "So, let's hurry, Hicchan~! To have lunch!"

                show misha hips_grin
                with charachange

                mi "We promise it'll be great!"

                hi "I'll take your word for it. What kind of a place is it?"

                hi "A restaurant, or something?"

                show shizu behind_smile
                with charachange

                shi "…"

                show misha perky_smile
                with charachange

                mi "It's a teahouse, Hicchan~!"

                "A teahouse… that sounds kind of fancy."

                show shizu adjust_smug
                with charachange

                shi "…"

                show misha hips_grin
                with charachange

                mi "Why are you looking at your wallet, Hicchan? It's okay, if you don't have any money we'll cover for you~!"

                hi "That's really nice of you. Thanks."

                show misha hips_smile
                with charachange

                mi "It's okay, Hicchan! After all, we're friends, right, Hicchan?"

                "It's only been three days. Are we really friends that quickly?"

                "Heh. But, hearing that makes me happy."

                show shizu behind_blank
                with charachange

                shi "…"

                show misha sign_smile
                with charachange

                mi "Ah, it's only for today, though, and only if you accept right now! Do you want to go, Hicchan?"

                "I start wondering if this is some kind of trap. Is this Misha's suggestion or Shizune's? This is important. I'm still a little apprehensive about the possible motives of a girl whose favorite pastime is the game of world domination."

                "No, I'm just being paranoid. Actually, they have grown on me already, and I do have to go to town sometime. So why not now, with them?"

                "I've never actually been to a teahouse before. All my expectations are from what I've seen about them on TV. But those are period dramas, and these are modern times. It might just be a regular café, and they're just calling it a teahouse."

                "Either way, I'm curious about that, too, so there's another reason for me to join them."

                hi "Sure."

                show misha hips_grin
                show shizu behind_smile
                with charachange

                mi "That's great, Hicchan~! That's great, that's great! Yay~!"

                "Misha hops up and down briefly to show how happy she is, which causes a few heads to turn towards us. Shizune opts for a polite, tiny clap that lasts for all of two seconds before she goes back to looking stoic as usual."

                show shizu behind_blank
                with charachange

                hi "Would it kill you to be a little happier, Shizune?"

                show shizu basic_normal2
                with charachange

                shi "…"

                show misha cross_laugh
                with charachange

                mi "Oh? I wasn't aware that Hicchan was a king. Hahahaha~!"

                show shizu adjust_smug
                with charachange

                "Shizune pushes her glasses up as Misha delivers her message totally without sarcasm. I guess it would sting more if she could say it with the intent Shizune meant behind it, so for once I'm happy to have Misha as a barrier between us."

                hi "I'm not telling you to jump for joy just because I'm having lunch with you. I'm not that arrogant."

                show shizu adjust_happy
                show misha cross_grin
                with charachange

                stop music fadeout 2.0

                "She seems to accept this, and we head for town with Shizune leading the way."
            else:
                show shizu basic_normal2
                with charachange

                shi "…"

                show misha perky_smile
                with charachange

                mi "We have to run now, there is an important student council meeting regarding the festival. And we finally decided where to eat~!"

                show shizu behind_blank
                with charachange

                shi "…"

                show misha hips_smile
                with charachange

                mi "Too bad you can't join, but this lunch meeting is only for council members."

                show misha hips_grin
                with charachange

                mi "We can take you there some other time! Oh, but that'd be like a date, wouldn't it?"

                show misha hips_laugh
                with charachange

                mi "Wahaha~!"

                hide misha
                hide shizu
                with dissolve

                stop music fadeout 4.0

                "The girls leave for downstairs."

                "I didn't manage to get far from the third floor hallway before all this commotion struck, literally. I should get going as well."

                scene bg school_scienceroom
                with shorttimeskip

                "The lunch and the afternoon class pass uneventfully."

                "I read most of the book I had started yesterday, and eat some of the mostly inedible offerings of the cafeteria."

                "The class is tiresome."

            if _in_replay:
                return
    else:
        label .meet_cute:
            scene bg school_hallway3
            with locationchange

            "So we leave, all three together."

            show hanako emb_downtimid at center
            show lilly cane_smile at twoleft
            with charaenter

            "Lilly walks beside the wall, letting her cane gently tap against it every now and then. Hanako comes along right beside her, so close that she is practically half-hugging her as they go."

            "Although it must make her walking that much harder, Lilly takes it in stride."

            show hanako defarms_shock
            with charachange

            "As we turn around the corner of the hallway, something hits me in the chest with the force of a steam train. Hanako shrieks a little and my vision briefly goes black."

            call separate_of_sss_and_mc

            show lilly cane_listen behind emi at offscreenleft
            show hanako defarms_worry behind emi at offscreenright
            with None

            show lilly at left
            show hanako at right
            with charamovefaster

            li "Hisao, what happened?"

            "She's not quite up to speed for obvious reasons, but she sounds very worried. More than what the situation deserves, really."

            hi "Someone just bumped into me, nothing serious. Just winded."

            show emi excited_sad_gym
            with charachange

            emi_ "Er, sorry, it's my fault. I was just going to get some stuff, and I was in a kind of a hurry."

            show lilly cane_weaksmile
            show hanako def_worry
            with charachange

            li "That 'someone' here is Emi, isn't it?"

            show emi basic_hes_gym
            with charachange

            "The little girl coughs quietly and shuffles her plastic or metallic feet, looking down at them before saying anything."

            show emi basic_closedgrin_gym
            with charachange

            emi "Hi, Lilly. Hanako."

            "I guess the girls know each other."

            show lilly cane_sad
            show hanako def_worry
            with charachange

            li "Do please try to be more careful. You might be sturdy enough to endure these sorts of accidents, but there are people who aren't."

            show emi sad_depressed_gym
            with charachange

            "The girl blushes and starts to fidget nervously like a little child caught misbehaving."

            "It's so cute I find myself smiling."

            emi "I know that! I— I, um, I was just…"

            show emi basic_hes_gym
            show lilly cane_surprised
            show hanako defarms_shock
            with charachange

            emi "Aaah! I gotta go!"

            emi "Teacher'll have my head, I promised to help with printouts but I went running instead! Sorry, but I've gotta change and everything!"

            play sound sfx_emisprinting
            stop music fadeout 1.0

            show emi at offscreenleft
            with charamovefaster

            hide emi

            stop sound fadeout 1.5

            "Before any of us can say a thing, Emi has already bolted away, leaving the hallway eerily quiet."

            hi "Does that kind of thing happen often around here?"

            show lilly cane_concerned
            show hanako def_worry
            with charachange

            show lilly at twoleft
            show hanako at tworight
            show bg at center
            with charamove

            li "There are more rules in Yamaku than usual for running in corridors."

            show lilly cane_listen
            with charachange

            li "…but that rarely stops Emi, it seems."

            show lilly cane_weaksmile
            with charachange

            "She shakes her head weakly and offers a slight, composed smile."

            li "I don't think there's anything we can do to stop her, I'm afraid. Shall we be off, then?"

            hide lilly
            hide hanako
            with charaexit

            "Lilly heads off along the hallway, and Hanako hurries after her."

            "The route to the room the two use for tea is fairly simple to retrace, being still fresh in my mind from yesterday."

            if _in_replay:
                return

    if wait_for_shizu:
        label .detour_ahead:
            scene bg suburb_roadcenter
            with locationskip

            play music music_tranquil fadein 3.0

            "Watching her walk in front of me, I notice that she walks very quickly, taking long, heavy, determined strides."

            "Maybe if we were traveling through a snowstorm it would make sense to walk like that, but it's a perfectly clear day. Anyway, it's making me feel exhausted just watching her."

            scene bg suburb_shanghaiext
            with locationchange

            "We arrive at the teahouse in what Misha says is 'record time,' likely because of Shizune's blazing pace. I feel a little let down seeing that it's not a huge feudal-era building with mats on the floor and women in kimonos pouring the tea."

            "It actually is more like a café, as I thought. Not that it's a bad thing. It looks very nice."

            play sound sfx_storebell

            scene bg suburb_shanghaiint
            with locationchange

            "As soon as I walk through the doors, someone zooms in front of us, as if they had been lying in wait the entire time."

            show yuukoshang closedhappy_down at center
            with charaenter

            yu "Welcome! Thank you for patronizing this establishment!"

            "The top half of her body drops forward in a bow that looks like an axe chopping through wood."

            "I'm surprised to see it's none other than Yuuko, the librarian."

            hi "Hey, I didn't know you worked here."

            show yuukoshang smile_down
            with charachange

            yu "Oh… Yes, I do. I'm a waitress… I've been working here for one year, six months, and two weeks now… Thank you for choosing to come here, is there anything I can do for you?"

            show yuukoshang at twoleft
            show bg at bgleft
            with charamove

            show shizu behind_smile:
                xalign 1.03
            show misha hips_grin at tworight
            with charaenter

            mi "Hi, Yuu-chan~!"

            show yuukoshang neutral_down
            with charachange

            yu "Hello."

            hi "Misha, you both know her too?"

            show misha perky_smile
            with charachange

            mi "Of course, Hicchan~! Yuu-chan works in the library, after all~! I don't go there often myself, but Shicchan knows her! And~!, we both come here a lot, so it's like we see her all the time!"

            show yuukoshang neurotic_up
            with charachange

            yu "Um… Yes… Should I get you your usuals? And… if there is anything you would want, please feel free to tell me at any time."

            hi "You don't have to be so formal, we all know each other."

            "It's also pretty empty today, so she can afford to take it easy."

            "I was hoping she would stop looking so nervous, but my words have the opposite effect."

            show yuukoshang panic_up
            with charachange

            yu "No… I'm a waitress, this is my job, I have to… do it properly."

            show shizu adjust_happy
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "Okay, okay~! That works for Shicchan! Yuu-chan, please get Shicchan what she usually gets, and I'll have some green tea with milk and honey."

            hi "No pressure."

            show yuukoshang neurotic_up
            with charachange

            yu "Um, yes… but… this is my job, and… there is always pressure. I'm sorry, I'm arguing with a customer… Sorry! Sorry, sorry!"

            "Yuuko takes another hundred-mile-per-hour bow. I decide to give up and join Shizune and Misha at a table."

            scene bg suburb_shanghaiint at bgleft
            with shorttimeskip

            "As soon as I sit down, Yuuko comes by looking even more upset than before."

            show yuukoshang panic_up at center
            with charaenter

            yu "I'm sorry! I'm really, really sorry, I forgot to take your order… I'm… not attentive to customers, that's not right… I'm sorry… If there is anything I can do to make up for it, please tell me…"

            scene ev shizu_shanghai
            with charachangeev

            shi "…"

            mi "It's okay, Yuu-chan, Hicchan didn't order anything, so it's not your fault, don't be upset."

            "It's true. I guess I should order now, but I don't really know what this place serves, and there doesn't seem to be a menu."

            hi "Yeah, she's right. I'll have some coffee, and… a sandwich, if you have one. Whichever sandwich you think is the best tasting one here, because Shizune is paying for my meal."

            scene ev shizu_shanghai_borednormal
            with charachangeev

            "Shizune frowns and gives me alternating looks of surprise, indignation, and bemusement, unable to decide between the three."

            shi "…"

            scene ev shizu_shanghai_boredlaugh
            with charachangeev

            mi "Hicchan, just how much money do you have in your wallet? It can't be that little, right?, right? We should split the cost three ways, to make it fair~! Yeah, I won't accept anything else~!"

            "Misha turns to Yuuko."

            show ev shizu_shanghai_borednormal
            with charachangeev

            mi "Yuu-chan, Shicchan says she wants three of whatever is the most expensive item on the menu~."

            hi "No!"

            show ev shizu_shanghai_boredlaugh
            with charachangeev

            mi "Hahaha~! Just kidding, Hicchan…"

            scene bg suburb_shanghaiint
            show yuukoshang neurotic_up at center
            with dissolve

            yu "Um… okay, I think that the turkey sandwich is the most delicious sandwich… And it comes with free soup… A good employee would try to recommend the item that there is the most of, though… or the most expensive item…"

            show yuukoshang worried_up
            with dissolve

            yu "Am I bad at my job?"

            hi "No! That sounds good, I'll have that. And some coffee."

            show yuukoshang smile_down
            with dissolve

            yu "Okay."

            hide yuukoshang
            with charaexit

            scene bg suburb_shanghaiint
            show yuukoshang neutral_down at center
            with shorttimeskip

            "She comes back a few minutes later with our drinks and my sandwich. Shizune seems to be fine with just her tea, while Misha also ordered a parfait. I don't know why, because I can't imagine many other things that would go worse with tea."

            "Oh well. I take a bite out of my sandwich. It's very good."

            scene ev shizu_shanghai
            with locationchange

            shi "…"

            mi "Hicchan, have you thought about joining the Student Council?"

            stop music fadeout 3.0

            hi "Huh?"

            show ev shizu_shanghai_borednormal
            with charachangeev

            shi "…"

            mi "Don't talk with your mouth full, Hicchan…"

            scene bg suburb_shanghaiint at bgleft
            with dissolve

            "I wash my food down with a sip of coffee, which is also surprisingly good. But now's not the time to remark on how this place has good food."

            hi "You said you understood it was too early to expect me to make a decision this quickly! That was like three hours ago!"

            play music music_comedy fadein 0.5

            show shizu adjust_smug_close at offscreenleft
            show misha hips_grin_close at offscreenright
            with None

            show shizu at center
            show bg at bgright
            with charamove

            shi "…"

            show bg at center
            show shizu at twoleft
            show misha at tworight
            with charamove

            mi "A man should be decisive, Hicchan!"

            show shizu behind_blank_close
            with charachange

            shi "…"

            show misha perky_smile_close
            with charachange

            mi "You really should join the Student Council, Hicchan. Come on, it'll be fun!"

            hi "People always say 'come on, it'll be fun' about things that are never, ever fun."

            show shizu behind_frown_close
            with charachange

            shi "…"

            show misha cross_grin_close
            with charachange

            mi "Don't you believe me, Hicchan?"

            "Is it Shizune saying that or Misha? What a cute expression; but the effect is somewhat jarring, like she has split personalities."

            hi "Uh…"

            show shizu basic_normal_close
            with charachange

            shi "…"

            show misha hips_frown_close
            with charachange

            mi "Hicchan, that's depressing. We just want to spend time with you…"

            show shizu behind_smile_close
            with charachange

            shi "…"

            show misha hips_grin_close
            with charachange

            mi "That's right, Shicchan! Yeah, that's a good point too!"

            show shizu adjust_smug_close
            with charachange

            shi "…"

            mi "Yup, this is beneficial to everyone, it solves all our problems~."

            show shizu behind_frown_close
            with charachange

            shi "…"

            show misha perky_sad_close
            with charachange

            mi "Yeah, I also thought Hicchan would appreciate it… That makes me sad."

            "Suddenly I feel really left out."

            hi "It's rude to talk about someone without letting them in the conversation."

            show shizu adjust_happy_close
            with charachange

            "Shizune adjusts her glasses, laughing to herself."

            shi "…"

            mi "Aw, but it's true, Hicchan~! And you would be helping us out, membership has been really low this year."

            hi "How low?"

            show misha sign_confused_close
            with charachange

            mi "Ah, that's a secret, Hicchan."

            hi "No, I want to know how low it was. How low is 'low'?"

            mi "Ahaha…"

            hi "Five?"

            show shizu behind_blank_close
            with charachange

            shi "…"

            hi "Lower?"

            show misha perky_sad_close
            with charachange

            mi "Well…"

            hi "Zero?"

            show shizu basic_normal_close
            with charachange

            shi "…"

            show misha hips_grin_close
            with charachange

            mi "Wahaha~! Hicchan, that isn't important. What matters is that the number is low, and that is why we would appreciate you giving us a hand, especially with the festival coming up so soon, and it looking to be a busy year ahead in general."

            hi "So you're not going to answer my question?"

            show shizu adjust_smug_close
            with charachange

            shi "…"

            mi "No~."

            "I sigh and straighten up in my chair, trying to look as defiant as possible, because this seems like a big issue and I do not want to let it go that easily. I feel silly, like a blowfish."

            hi "Fine, at least tell me this: How many people are in the Student Council? Total?"

            show shizu behind_blank_close
            with charachange

            shi "…"

            show misha perky_smile_close
            with charachange

            mi "Um, well, Hicchan, we're definitely undermanned, but we have enough members to get the job done. Yup, yup~!"

            hi "It's not just the two of you, is it?"

            show misha cross_laugh_close
            with charachange

            mi "Hahaha~! Hicchan, that's funny~!"

            show shizu basic_normal2_close
            with charachange

            shi "…"

            show misha cross_smile_close
            with charachange

            mi "But~! It's definitely not just us."

            hi "Are you sure? Are you absolutely sure?"

            show misha cross_grin_close
            with charachange

            mi "Yup~!"

            "I stare at them both, trying to see if they will slip up and confirm my worst fears."

            show misha perky_sad_close
            with charachange

            "Misha frowns, looking uncomfortable, but that is probably because I'm staring at her."

            show shizu basic_happy_close
            with charachange

            "Shizune, on the other hand, returns my gaze with one of her own. Maybe she is challenging me, peering at me over the rims of her glasses like that. So teasing; and surprisingly immature, like a little girl beckoning someone to play with her."

            show shizu basic_normal_close
            with charachange

            shi "…"

            show misha perky_smile_close
            with charachange

            mi "Hicchan, your two cute student council representatives have been trying to make you feel welcome and are even treating you to lunch. You should show your gratitude by joining the council so you can at least help them out."

            mi "Yeah, it would be great if you could just file some papers for us, and… the festival is coming up, and we have to build some stalls for the games and food, just a few, so if you were there, it would be a lot easier for us…"

            show misha perky_sad_close
            with charachange

            mi "Please, Hicchan?"

            "What an interesting good cop-bad cop routine."

            "I'll give it a shot. Why not?"

            "Just a shot."

            hi "Okay, I'll give it a trial run. It doesn't mean I'm joining, or anything definite, just that I'll help out a little, and then I'll see. And this makes us even for lunch, I'm not doing this because I want to."

            show misha perky_smile_close
            show shizu basic_frown_close
            with charachange

            "I finish off the last of my sandwich, and this makes Misha notice for the first time in a while that she has a parfait. She starts digging in, much to Shizune's chagrin, because I can tell from the way she plays with her fingers that she had a lot to say."

            stop music fadeout 12.0

            show shizu behind_blank_close
            with charachange

            "Every time I look at Shizune, she looks back with such focus and intensity. This time is no exception. Her face is expressionless; maybe she is thinking. Eventually, it gives way to a smile."

            show shizu adjust_happy_close
            with charachange

            shi "…"

            "She signs something, and obviously, I can't understand it at all. She has to know that. Then, she does it again, a childish playfulness showing through in the speed and energy of her gestures."

            show shizu adjust_smug_close
            with charachange

            shi "…"

            show shizu adjust_happy_close
            with charachange

            hi "Misha, what did she say?"

            show misha perky_confused_close
            with charachange

            mi "…?"

            "Misha looks up from her parfait, torn between wanting to help out and going back to eating."

            hi "What does this mean?"

            "I try my best to make the same movements with my hands that Shizune did. I come to realize quickly that this isn't very easy. Imagine doing this all day, as your only means of communication."

            show misha perky_smile_close
            with charachange

            mi "Hmm~… Sorry, Hicchan, I can't tell you."

            hi "Why not? Is it an insult?"

            show misha hips_grin_close
            with charachange

            mi "No, Hicchan, I can't tell you because~!, it means something nice."

            "Something nice, huh? Well, they've gone back to their tea and food, so I guess this conversation is over for now."

            hide misha
            hide shizu
            with charaexit

            "I don't really understand. But this makes me wish that I could. Maybe I could even try learning sign language. This school might have courses for it."

            "Would I really do that? I think about it as I finish the rest of my coffee. I wonder why I'd even be motivated to think about it."

            "I'm enjoying myself so much that I don't even notice that we were supposed to be back in class ten minutes ago."

            "Even if I were to start heading back to school right now, it would take at least… thirty minutes? Maybe. I can't risk running fast with my condition, so it would take at least that long to get there."

            "Well, ten minutes late already as I am, it wouldn't matter even if I could teleport."

            show shizu behind_blank_close at twoleft
            show misha perky_confused_close at tworight
            with charaenter

            mi "Something wrong, Hicchan?"

            hi "I just realized lunch break ended ten minutes ago. It's only my third day, and I'm already going to miss a class."

            play music music_running fadein 4.0

            show shizu adjust_smug_close
            with charachange

            shi "…"

            show misha hips_grin_close
            with charachange

            mi " Yup~! You are already late."

            hi "Hey, that's not funny, so are you! And, aren't you two in the Student Council? You're setting a bad example."

            show misha perky_sad_close
            with charachange

            mi "Hicchan is so moral…"

            show shizu basic_normal_close
            with charachange

            shi "…"

            show misha sign_smile_close
            with charachange

            mi "But~! Hicchan is right, he is late for class, and~ it looks like you're cutting too, Hicchan, because you're not making an effort to go."

            mi "As your student council representatives, we're going to have to do something about this and make sure you're punished for it~!"

            hi "But you two dragged me out here, this is all your fault. Take responsibility!"

            show shizu behind_frown_close
            with charachange

            shi "…"

            show misha hips_smile_close
            with charachange

            mi "Hicchan, we were just taking a prospective student council member out to try and recruit him. It's business, business~! But~! You're not a member of the council, so there's no excuse!"

            hi "Yes, there is. That prospective student council member is clearly me."

            show shizu basic_happy_close
            with charachange

            shi "…"

            show misha hips_grin_close
            with charachange

            mi "Yes~! Are you going to join the Student Council, Hicchan?"

            "Shizune raises her teacup haughtily and wags her outstretched pinky finger up and down."

            show shizu behind_blank_close
            with charachange

            shi "…"

            show misha perky_smile_close
            with charachange

            mi "Hicchan, if only you were a member of the Student Council… But~! You can still join now, Hicchan! If you join now, you won't be in any trouble at all, and we'll be able to take many more nice excursions like this all the time! It'll be fun~!"

            "I start to think that, maybe, this was all an elaborate set-up leading up to this moment. Maybe Shizune lured me out here, banking on the possibility that I'd lose track of time and be forced into this situation."

            "Diabolical. …Well, considering what I know of her, I should have been more on my guard. But to admit that I got myself into this, even slightly, would be unforgivable."

            "I try to read Shizune's intentions in her eyes, but she just returns my stare blankly. Innocently. She takes a sip of tea, like she is mocking me."

            show shizu basic_normal_close
            with charachange

            shi "…"

            show misha sign_smile_close
            with charachange

            mi "By the way, Hicchan, I didn't plan this at all, things just happened to work out this way~!"

            "I was almost about to drop my theory as paranoia, but this puts a new spin on things. I almost fall over in awe. So it really was an elaborate set up, from the very beginning, all just to burn me and force me to join the Student Council."

            show shizu adjust_smug_close
            with charachange

            shi "…"

            show misha cross_laugh_close
            with charachange

            mi "Ahahahaha~! You look so nervous, Hicchan~! Did you really think we were tricking you this whole time?"

            hi "You're not?"

            show misha perky_sad_close
            with charachange

            mi "Hicchan, you really thought…?"

            show shizu behind_frown_close
            with charachange

            "Misha frowns, looking heartbroken. Shizune quickly frowns as well, following her lead. How synchronized. Two of a perfect pair. They must be twins."

            shi "…"

            mi "Shicchan says she's flattered, Hicchan, but doing that kind of thing would be a grossly inappropriate abuse of power, and imposing on your free will~! And~! It would be blackmail, too! Shicchan would never do anything like that, never!"

            "I think about asking Misha, 'Are you sure?' but resist the urge to."

            show shizu basic_normal_close
            with charachange

            shi "…"

            show misha perky_smile_close
            with charachange

            mi "Anyway, Hicchan, what Shicchan said is true. Since you're with us, and we're doing student council work, it's okay if we miss a class or two."

            show shizu basic_normal_close
            with charachange

            shi "…"

            show misha perky_confused_close
            with charachange

            mi "Not that this is a good excuse to do so…"

            shi "…"

            show shizu behind_blank_close
            with charachange

            mi "…Or one that should be used more than three times a month…"

            show shizu basic_normal_close
            with charachange

            shi "…"

            mi "Or something that can or should be abused…"

            show shizu adjust_happy_close
            with charachange

            shi "…"

            show misha hips_grin_close
            with charachange

            mi "So~! We must definitely, definitely return to class! Eventually~!"

            show misha cross_laugh_close
            with charachange

            mi "Wahaha~!"

            "Shizune waves Yuuko over and points to her empty teacup, indicating that she wants another one, as Misha scrambles to finish her parfait so she can order something else. Maybe I should as well."

            "I am still hungry, and the portions here are a little on the small side. Most importantly, Shizune is paying for everything. With that in mind, I ask Yuuko for another sandwich."

            scene bg suburb_shanghaiext
            with locationchange

            stop music fadeout 5.0

            "By the time we leave the tea shop I've missed not just one class, but two."

            scene bg suburb_roadcenter
            with locationchange

            "Shizune and Misha seem content to let the whole day pass by, stalling for even more time by suggesting a tour of the town that turns out to cover a two block radius from where we start."

            scene bg school_scienceroom
            with shorttimeskip

            "Eventually, we do go back to school, and the rest of the day is business as usual. When classes are over, Shizune and Misha pack their bags and leave the room before me. Come to think of it, this is the first time they've left me alone."

            "It's strange, I almost miss them. The room empties quickly, and I'm the last one out the door."

            scene bg school_lobby
            with locationchange

            "When I try leaving the lobby, however, an arm lowers itself in front of me like a toll bridge gate, stopping me in my tracks."

            show shizu behind_blank at center
            with charaenter

            shi "…"

            hi "Oh, hi Shizune."

            show black
            with hands_in

            "A pair of hands from behind cover my eyes, followed by a sharp burst of laughter."

            mi "Hi, Hicchan~! Guess who!"

            "Misha asks the question completely without sarcasm, meaning she doesn't think that I instantly knew it was her for many obvious reasons."

            hi "I wonder who it could be? Well, it's definitely not Misha…"

            mi "Hahaha~! It is!"

            hide black
            with hands_out

            play music music_shizune fadein 1.0

            show misha hips_grin_close at offscreenleft
            with None

            show bg at bgright
            show shizu at tworight
            show misha at twoleft
            with charamove

            "Misha swings around to stand in front of me, beside Shizune."

            show shizu basic_normal2
            with charachange

            shi "…"

            show misha cross_smile_close
            with charachange

            mi "Hicchan, are you busy right now?"

            hi "Busy going to my room, yeah. See you two tomorrow!"

            show misha at offscreenleft
            show shizu at twoleft
            show bg at bgleft
            with ease

            show shizu at offscreenright
            show bg at center
            with easeout

            show shizu behind_blank_close at tworight
            show misha perky_smile at twoleft
            show bg at bgright
            with easein

            "I try to make a break for it, but Shizune is too agile to get past. As someone who used to play soccer, this is embarrassing. Not to mention that this behavior is drawing some odd looks. I should just quit while I'm ahead."

            show shizu adjust_happy_close
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "Hicchan, could you please go upstairs and get a few things for us from the art room?"

            hi "Why me?"

            show misha cross_laugh
            with charachange

            mi "Hahaha~! Shicchan thinks that if the art teacher sees us, he will say hi, and she doesn't like him!"

            hi "Ignore him."

            show shizu behind_blank_close
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "She tried, but even though Shicchan is deaf, he'll try to say 'hi~!' anyway!"

            hi "Run away?"

            show shizu cross_angry_close
            with charachange

            shi "…"

            show misha perky_smile
            with charachange

            mi "I never run!"

            "A tone of finality so strong that I can pick it up even through Misha. I can see there is no use pursuing this further with Shizune."

            hi "Misha, why can't you get them?"

            show misha sign_smile
            with charachange

            mi "Stairs make me dizzy, Hicchan!"

            show shizu basic_normal_close
            with charachange

            hi "…"

            "Shizune nods, as if to confirm it."

            show misha perky_sad
            with charachange

            mi "Please, Hicchan? We need these things to build stalls for the festival, and you said you would help out a little, right?, right?"

            "I really shouldn't, but I guess just this once would be all right."

            hi "Okay."

            show shizu adjust_happy
            with charadistant

            shi "…"

            show misha hips_grin
            with charachange

            mi "That's great, Hicchan! Thank you~!"

            show misha perky_smile
            with charachange

            mi "This is what we need!"

            "She holds out a piece of paper for me to take."

            "I'm sure this list was made by Shizune. It's handwritten, but each letter is perfectly formed and uniform, as if it were typed. Not just that, but it's exhaustively detailed, complete with numbers, bullet points, and even little checkboxes."

            "What it boils down to is that she wants paint, paintbrushes, posterboard, and an easel. Just different types and specific numbers of each. I wonder how I'm going to carry all of this stuff down the stairs without breaking my neck."

            stop music fadeout 4.0

            if _in_replay:
                return
    elif talk_with_hanako:
        label .sip_p1:
            play music music_dreamy fadein 2.0

            scene bg school_miyagi
            with locationchange

            "Lilly and Hanako quickly go about the business of making lunch."

            "Before I can even open my small bag of food, Lilly's busying herself with her thermos and teabags as Hanako is setting out both their lunchboxes."

            show lilly basic_smile at center
            with charaenter

            hi "So, is this what you meant by coming here almost every day?"

            show lilly basic_smileclosed
            with charachange

            li "Yes, Hanako and I usually have lunch here. It suits both of us, so we ended up using this room regularly."

            "After seeing Hanako's reactions to me over the past couple of days, I can understand why that is a boon. That, and Lilly being able to get some quiet away from her class as well."

            "I take my seat last, after Lilly's poured the tea for us and sits down."

            scene bg tearoom_everyone_noon
            show tearoom_hisaoe lsmile
            show tearoom_lillye smileclosed
            show tearoom_hanae sad
            with fade

            "The more time I spend with these two girls, the more I think they're a perfect foil to Misha and Shizune."

            "Even without a voice, Shizune is direct and brash, and Misha seems to get along with everyone. On the other hand, Lilly is soft-spoken and relaxed while Hanako seems to be the shyest girl I've ever met."

            li "So, how are you faring in Yamaku, Hisao? You seemed a bit flustered before."

            show tearoom_hisaoe sigh
            with charachangeev

            hi "Apart from getting lost every now and again, and being crash-tackled outside my classroom? Fine I guess…"

            show tearoom_lillye smileclosed
            show tearoom_hanae shy
            with charachangeev

            ha "You… you looked pretty hurt before. Are you really… okay?"

            "For a brief moment, I consider telling Hanako and Lilly about my condition but then, I hold it back."

            "I can't tell why, but for some reason I feel uncomfortable talking about it to these relative strangers, even if they have been pretty friendly."

            show tearoom_hisaoe hrelief
            with charachangeev

            hi "Yeah, it's nothing. I was just a bit startled."

            show tearoom_lillye thinking
            show tearoom_hanae sad
            show tearoom_hisaoe lthink
            with charachangeev

            "Judging from the two girls' expressions, I don't think that they're buying it. But, in what I assume is their way of respecting my privacy, they don't press the matter."

            "I guess that is one of the unwritten rules around here; 'don't ask.' Even if people's conditions are obvious, like Hanako's, there's still bound to be a story involved."

            "Everyone has things that they don't feel comfortable speaking about, and I think everyone here recognizes that."

            show tearoom_hisaoe lsmile
            with charachangeev

            hi "So, uh… how long have you been in this school? You both seem to know your way around pretty well."

            show tearoom_lillye smileclosed
            with charachangeev

            li "Hmm… well, I've been here since the start of high school, but only moved into the dormitories a year ago."

            li "Hanako joined at the start of high school as well, and moved to the dormitories when she did, if memory serves me right."

            show tearoom_hanae shy
            with charachangeev

            ha "That's right. Since… high school."

            hi "So you've known each other since then?"

            show tearoom_lillye ara
            with charachangeev

            li "Since I moved, yes. Hanako lives next door to me, so it's only natural, right?"

            ha "R-right."

            show tearoom_hisaoe calm
            with charachangeev

            hi "Yeah, of course."

            "Living next to someone is probably reason enough to befriend them, though I'm guessing that Lilly's blindness played a part in it as well."

            "I can't imagine Hanako easily making friends with someone who has to deliberately avoid looking at her scars."

            "With the immediate conversation dried up, we start to eat our lunch."

            scene bg tearoom_everyone_noon
            show tearoom_hisaoe lsmile
            show tearoom_lillye weaksmile
            show tearoom_hanae sad
            with shorttimeskip

            play sound sfx_warningbell

            "It isn't long before the bells are signaling the end of the break. Like me, the girls pack up their lunches as efficiently as they set them out."

            show tearoom_lillye smileclosed
            with charachangeev

            li "I guess I'd better be off. Are you going to go with Hisao, Hanako?"

            show tearoom_hanae shy
            show tearoom_hisaoe hthink
            with charachangeev

            "Hanako looks up at me, and for a second I can see that she is considering skipping class, maybe just to avoid walking to the classroom with me."

            show tearoom_hanae sad
            with charachangeev

            ha "Y-yes."

            "I don't know what to think of it. Hanako really is delicate to the point of breaking if looked at in the wrong way. It makes me a bit nervous too, but I push the feeling aside, trying to be as natural as I can."

            show tearoom_hisaoe hsmile
            with charachangeev

            hi "We should hurry then. Class has already started by the sound of it."

            "Lilly gives a nod of farewell as she bends down to take her cane, Hanako and I filing out before her."

            scene bg school_hallway3
            with locationchange

            "We walk quickly down the empty halls to our respective classes."

            "As we reach the door to Lilly's 3-2 classroom, she turns towards me."

            show lilly cane_smileclosed at twoleft
            show hanako emb_timid at tworight
            with charaenter

            li "Hisao, thank you for sharing lunch with us today."

            hi "My pleasure, Lilly."

            hide lilly
            with charaexit

            stop music fadeout 8.0

            show hanako at center
            show bg at bgleft
            with charamove

            "And with that, we part ways; Lilly entering her classroom and leaving Hanako and me to make off to our own. She's still looking like she wants to run away."

            hi "So, do you really want to go back to class now?"

            show hanako basic_worry
            with charachange

            ha "Y-yes."

            hi "Okay then."

            "I feel like I should say something more to her, but it's hard to come up with anything that would be appropriate and safe enough."

            "And Lilly was right; the more time we spend out here, the more explaining we have to do."

            play sound sfx_dooropen

            "I open the rear door to the class, and walk in."

            scene bg school_scienceroom
            show muto irritated at center
            with locationchange

            "The teacher looks up at me, and opens his mouth to say something."

            show muto normal
            with charachange

            "However, as Hanako follows me in and closes the door, he simply nods to us and continues his lecture."

            "This is the third time that Hanako has had her truancy practically ignored. There's definitely something going on here."

            hide muto
            with charaexit

            "We make our way to our seats, and I notice that Misha and Shizune are both missing as well."

            "I wonder if it is some form of informal agreement with the staff, or if it's a 'perk' afforded to the unique students of this school?"

            "Trying to make as little disturbance as I can, I extract the relevant textbooks from my bag and start catching up."

            "The class goes on quietly."

            if _in_replay:
                return

    if not wait_for_shizu:
        label .it_builds_character:
            scene bg school_scienceroom

            "The teacher seems like an okay person despite the weird first impression I got, and the material is relatively interesting."

            "However, the way he teaches is really bizarre. It's as if he expects that everyone is a natural genius."

            scene bg school_scienceroom
            with shorttimeskip

            play sound sfx_normalbell

            play music music_tranquil fadein 3.0

            "When the final bell sounds, I realize that there is still a lot of time left in the day, and I'm left wondering what to do."

            "It's odd, at the hospital I had 24 hours a day of free time, but here filling the considerably shorter hours feels difficult."

            "Everyone else leaves, and I'm left alone with the teacher."

            "Mutou is examining the assignment sheets we were working on earlier, marking them with a red ballpen."

            "Raising his eyes from his papers briefly, he notices me and furrows his brow."

            show muto normal at center
            with charaenter

            mu "What is it, Nakai?"

            "I jump at him addressing me, but I guess it's natural to spark some conversation since there is nobody else around."

            hi "Umm… nothing. Thinking about what I'd do after school."

            "The teacher slowly puts the cap on the pen he is holding and arranges his papers into a stack, clacking it against the desk twice."

            "He seems very methodical and for a brief moment I'm reminded of Shizune, but the teacher is more unhurried and relaxed, much more routined."

            mu "You have no plans?"

            hi "No. I considered joining a club, but don't know what kind of club would interest me."

            mu "Go observe a meeting of someone else's club. Might pique your interest."

            hi "I guess…"

            hi "I just…"

            "But I don't know how to continue from there."

            show muto irritated
            with charachange

            "Mutou looks at me in a way that makes me quickly want to take the words back to avoid a conversation."

            "But I can't, so I have to forge ahead."

            hi "I just don't know how to deal with people. I mean, the other students."

            hi "I'm talking to people and everything, so it's not that I'd be isolated or anything."

            hi "I just don't know what to think about… the disabilities. It's like… it feels that I'm being impolite if I pay attention to them, and it's weird to ignore them."

            hi "Damned if I do, damned if I don't."

            "The teacher scratches his cheek absentmindedly, looking very unresponsive."

            show muto normal
            with charachange

            mu "These things are only an issue if you make them one."

            mu "You can talk normally with someone, even if they are blind or something."

            show muto smile
            with charachange

            mu "Try to look behind the superficial. There's not a single student here who isn't just a normal kid behind whatever they might seem at first glance."

            "He says the same thing as Yuuko did."

            "I know they're right, but it's hard. How can you not consider for example Shizune's deafness, when the only way to communicate with her is to talk through Misha?"

            "Or Hanako… it's not like you can ignore her face."

            hi "But…"

            play sound sfx_doorslam
            stop music fadeout 0.3

            show muto irritated
            with vpunch

            "I'm interrupted by the door of the classroom suddenly slamming open."

            show misha hips_grin at offscreenright
            with None

            show muto at twoleft
            show bg at bgleft
            show misha at tworight
            with charamove

            play music music_comedy fadein 0.5

            mi "Teacher~!"

            "Misha crashes in, hand straight in an enthusiastic greeting, her voice loud and lively enough to wake the dead from their graves."

            "She starts towards the teacher's desk with her bouncing step, hands energetically swinging with the rhythm."

            "Mutou, visibly dismayed at the interruption and Misha in general, slumps in his chair."

            mu "Mikado."

            "Misha stops in her tracks and looks around cluelessly, as if she's sensing from his tone that something's wrong but has no idea what."

            show misha perky_confused
            with charachange

            mi "Yes~?"

            mu "We have talked about volume control before."

            show misha perky_smile
            with charachange

            mi "Yes~!"

            "But she doesn't lower her voice at all, and the teacher just rubs his eyes."

            mu "So, what is it?"

            show misha perky_sad
            with charachange

            mi "I… we need help! We are running out of supplies for the festival stands!"

            show misha sign_sad
            with charachange

            mi "This is a distress!"

            "She waves a pink slip of paper she's holding around."

            mu "So… go get more supplies from the art room. What's the problem with that?"

            show misha perky_sad
            with charachange

            mi "Plywood! Plywood is always the problem! Last time we wanted more there was only a little, but that time we just took it all and went with that."

            mi "Now there's like none left there, so do you know where there is some?"

            mu "I don't understand. How would I know?"

            show misha perky_confused
            with charachange

            mi "Shicchan… I mean the president thought that a teacher would know if there is plywood. Was she wrong?"

            "Mutou looks like he is in great pain, frowning with his entire essence, and Misha doesn't get it at all."

            "Looking at the two of them communicate is terrible, like looking at a man being tortured by drilling his skull open while blasting pop music at full volume at the same time."

            mu "I'm afraid I have no idea if there is any plywood in the school, let alone where it would be if there was any."

            show misha perky_sad
            with charachange

            mi "Awww… what should I do?"

            mu "Perhaps try to find Mr. Nomiya? I'm quite sure he would know where to find everything you need."

            mu "You'd have to pry them from his cold, dead hands, but that's a different matter."

            mi "Aaaah! I don't have time! We are so busy!"

            "She holds her head with both of her hands, looking as despairing as it's possible for a person like her. Without even noticing, she crumples the note she's holding against her hair."

            mi "I shouldn't even be fetching these things, there is so much to do and we are falling behind the schedule!"

            show muto smile
            with charachange

            stop music fadeout 2.0

            "Mutou looks at her gravely and then, suddenly smiles. Smiling doesn't really fit his face. I think it'd be better if he didn't."

            mu "I wonder if you could get some temporary help?"

            show muto normal
            with charachange

            "He switches to staring at me focusedly, with a hard expression, as if trying to say 'go make some friends.'"

            "…"

            hi "Eehhh… I guess I can give you a hand."

            play music music_running fadein 0.5

            show misha hips_grin
            with charachange

            mi "You can? Thanks, Hicchan, you are really nice!"

            show misha sign_confused
            with charachange

            "She pauses, does a double take and then points at me with her finger, yelping 'Ah!' and looking very puzzled."

            mi "Come to think of it, what's Hicchan doing here? Class is over, you should be having fun~!"

            mu "We just had a little chat."

            show misha perky_sad
            with charachange

            mi "Oh no! It's not detention is it? Are you in trouble, Hicchan?"

            hi "No, I'm not."

            mi "Is Hicchan in trouble, teacher?"

            mu "No, he's not."

            "Mutou sighs deeply and I feel that I have to help Misha to get her off the teacher's back."

            hi "So what do you need?"

            show misha hips_smile
            with charachange

            mi "Here's a list. I can try to find the plywood from somewhere if there's none in the art room."

            "She offers me the note she's holding. I take it, hesitating a bit."

            hi "I said I'd help you, but this has no implications on whether I'm joining the council or not."

            show misha perky_sad
            with charachange

            mi "Awww…."

            show misha hips_grin
            with charachange

            mi "Still, thanks, Hicchan. Try to be quick, we are in a stall-building streak now, we must hurry hurry hurry!"

            show misha at offscreenright
            with charamovefaster

            hide misha

            "She bounces out of the classroom, leaving me and the teacher looking at each other with something that feels like a silent agreement."

            show muto at center
            show bg at center
            with charamove

            mu "Well, there you have it, Nakai. You have something to do now."

            "Please don't sound so smug."

            "Looking at the list with a number of items ranging from paint to plywood, all written with small, neat handwriting that is undoubtedly Shizune's, I heave a sigh."

            hi "I'll be going then."

            stop music fadeout 4.0

            "Waving the long list limply at the teacher, I exit to the hallway."

            if _in_replay:
                return

    label .a_private_lunch:
        scene bg school_hallway3
        with locationchange

        "The classrooms closest to ours are designated belonging to classes 3-1 and 3-2 on the right side, and 3-4 on the left side, each door looking exactly the same."

        "Further down the corridor still with identical doors, are rooms that I didn't think were used for classes."

        "I guess the art room is not a classroom as such."

        "I carefully push open the furthest door, and peek in."

        scene bg school_classroomart at bgleft
        with locationchange

        "It's a classroom, but it seems rather badly kept or not in use. Am I in the right place?"

        "Desks and chairs are all around the room, a thin layer of dust settled on them. There are some easels in the corner so at least this looks like the right place."

        "The room is flushed in sunlight from the big windows, shadows creeping all over the desks."

        "Specks of dust are dancing in the stagnant air, making the beams of light almost visible."

        "Jokingly, I call into the empty room."

        hi "Anybody ho—{w=.5}{nw}"

        "Something catches my eye and I stop mid-sentence."

        scene ev rin_eating_zoomout
        with flash

        play music music_rin fadein 0.5

        "Sitting on a desk is a short-haired girl; curiously wearing a boy's uniform, with a fork between her toes, a morsel of food stuck firmly on the end."

        "This odd way of dining seems to be caused by her apparent lack of hands, but her presence here is what takes me aback even more."

        "How did I miss her before? She's sitting in a corner very still, but I still somehow took her as a part of the furnishing or a statue at first glance."

        "I'm not being too observant today, as a whole."

        "The girl seems to be frozen in place, staring at me with her huge eyes like a rabbit in headlights."

        "She's staring at me, her mouth wide open, ready to accept the fork."

        "I'm staring at her, my mouth wide open, suddenly remembering I didn't finish my sentence and trying to think if I should."

        "This weird stalemate keeps us both stunned into silence, punctuated only by the wall clock ticking rhythmically."

        rin_ "Hello."

        "The girl stuffs the forkful in her mouth, and is now staring at me expectantly while chewing. This is a bit awkward."

        hi "Umm… hello. I was told to pick up some supplies from here. For some festival stalls I think. I didn't think there would be someone here."

        rin_ "There isn't. That's why I came here, too."

        "She picks up another forkful."

        hi "Doesn't that mean you're here, then?"

        scene bg school_classroomart at bgleft
        show rin relaxed_surprised at center
        with locationchange

        "She raises her eyebrows as if she was suspecting my observation was false."

        rin_ "You are pretty observant. I guess it does. But who are you?"

        "This girl is pretty straightforward, isn't she?"

        hi "I'm Nakai, Hisao Nakai. I just transferred in on Monday."

        show rin basic_absent
        with charachange

        rin_ "I'm Rin. Tezuka Rin. Rin Tezuka."

        show rin basic_deadpandelight
        with charachange

        rin "I won't shake hands with you, but at least we know who we are now."

        rin "That's very nice."

        "Her deadpan manner of talking makes it hard to determine whether she's joking about shaking hands or not."

        "It kinda bothers me, joking about these matters doesn't feel appropriate at all."

        show rin relaxed_nonchalant
        with charachange

        "While I'm trying to figure what's appropriate and whether this girl is, she seems to have lost interest in me and is now gazing yearningly back at her food."

        show rin basic_deadpan
        with charachange

        rin "Can I continue my lunch? If you don't mind me, I won't mind you."

        rin "If you need to get your stuff, the supplies are at the back."

        hi "Go right ahead. But… lunch? School's already over for the day."

        show rin basic_awayabsent
        with charachange

        rin "What word would you use then? There is no word for a meal you eat after lunch but before dinner, right? It bothers me very much too, but I don't really know what I should say."

        hi "I don't think you are supposed to eat a meal between lunch and dinner to begin with."

        show rin negative_spaciness
        with charachange

        rin "But I'm hungry now and my delicious boxed lunch would go to waste otherwise."

        show rin basic_delight
        with charachange

        rin "I have curry. It's very delicious."

        "With much decisiveness, Rin once again picks up the fork between her toes and with at least as much impoliteness, she points it straight at me."

        scene ev rin_eating
        with locationchange

        rin "So, Nakai, what brings you to this place?"

        hi "Like I said, I was told to look for these things."

        stop music fadeout 5.0

        rin "No, the school. From outside you look fine. Is your problem inside?"

        "I come to a full stop, opening my mouth but not getting a word out."

        hi "I…"

        rin "I can guess. I am good at guessing. Better than most people."

        "Rin cuts me off before I can answer her question, or skirt around it somehow. I don't know which I would've done."

        "I froze in front of this issue again. I haven't even told anyone here about my condition, or maybe it's only because it hasn't really come up."

        "I do get the feeling that not making issues of this is a part of the social code here, as the teacher said."

        "I wonder if the people here could relate? Probably not any better than any normal person could."

        "I can't relate to Shizune's circumstances, or Lilly's, either."

        scene bg school_classroomart at bgleft
        show rin basic_absent at center
        with locationchange

        "Naturally, while I go through this in my head, Rin keeps considering what my condition could be, with an overtly contemplative look on her face."

        "She puts her fork between her lips and leans back, looking at the ceiling as if the answer was written up there."

        "A beam of light illuminates her face from the window side, creating a mask of dark shadow on the other side."

        show rin basic_lucid
        with locationchange

        rin "I don't think it's anything in your head, and something in your guts would be boringly ordinary, like this lunch of mine. And less delicious."

        show rin basic_deadpandelight
        with charachange

        rin "The problem must be in your pants!"

        play music music_rin fadein 0.5

        "This messed-up Sherlock Holmes kind of statement and the sheer lack of tact it was delivered with catches me completely off guard."

        "I think I might've reeled back even physically as Rin's eyes widen in revelation and astonishment."

        show rin relaxed_surprised
        with charachange

        rin "So I was right! There's something wrong with your tackle, isn't there?"

        "Still partially in shock but recognizing the need to reply something, I spit out the first thing that I can think of."

        hi "No! Nothing like that. I have a heart problem. Arrhythmia."

        "…"

        "I said it. More like blurted it out, but I said it."

        show rin negative_spaciness
        with charachange

        "The girl in front of me purses her lips together and glowers at me, looking very disappointed."

        rin "How boring. Trouble in the pants would have been much more scandalous."

        "What's with this reaction?"

        hi "I'm sorry to let you down."

        show rin basic_awayabsent
        with charachange

        rin "I forgive you. Just, I collect people and a person with, you know, that kind of problem would've been really great."

        hi "Collect people?"

        show rin basic_absent
        with charachange

        rin "People with different problems."

        hi "Huh, so you just… like, go around asking people what's wrong with them?"

        show rin basic_deadpannormal
        with charachange

        rin "Pretty much."

        hi "I see."

        "…"

        stop music fadeout 8.0

        hide rin
        with charaexit

        "With little left to say, Rin resumes her lunch and the conversation dies away, but I keep thinking about what was said."

        "It's the first time I told anyone else about my condition. All the other people have either known about it already, or heard about it from someone else."

        "Or didn't need to know about it, like every other student here, so far."

        "Should I have told it as a natural part of introductions? Is it expected of me?"

        "'Hi, I'm Hisao. I have a very serious heart condition.'"

        "Is that how I'm supposed to go around introducing myself from now on?"

        "As if our disabilities would define us. What a disgusting thought."

        "Or maybe this Tezuka girl just has an unnatural interest in such things."

        play music music_dreamy fadein 8.0

        show bg at bgright
        with charamove

        show rin basic_awayabsent at right
        with charaenter

        "As I walk to the back of the room to pick up the items on Misha's list, a chance opens to study Rin from the corner of my eye."

        "Her hair is a burnt auburn, almost orange, and cropped short. Long hair would probably be impossible with no arms."

        "The boy's uniform and the lack of arms make her look very thin, almost scrawny."

        "She is not particularly pretty except for her murky green eyes which flicker restlessly from below her short bangs, even when she eats."

        "The distance and the shadows make it seem like they don't reflect sunlight at all, but instead absorb all of it within them like deep wells."

        "She moves her feet almost as deftly as a normal person would use their arms."

        "However, I can see how this sight could discomfort people, especially while eating. It makes me feel a bit uncomfortable at least."

        "I hesitate to think about the word 'unnatural' but it's too late now, isn't it?"

        "I keep searching the cabins and shelves for Misha's things, but after enough time passes the silence grows too uncomfortable, so I try to force some conversation out of this strange girl."

        hi "So, do you always eat alone and this late? Or do you get the occasional visitor?"

        show rin basic_absent
        with charachange

        show rin at center
        show bg at bgleft
        with charamove

        rin "Visitors… maybe you are my first occasional visitor. But I don't always eat alone either."

        rin "Sometimes I eat with a certain person on the roof, if she's not horsing around."

        hi "Horsing?"

        show rin basic_deadpan
        with charachange

        rin "She likes to do sports."

        hi "Oh."

        "And that's all I can think of to say."

        "Both of us fall silent again as Rin forks the last bits of her meal to her mouth."

        "I look down at my haul and double check it with Misha's list. It seems I have everything except plywood."

        hi "Umm… so, I think I have all the things now."

        show rin basic_deadpannormal
        with charachange

        rin "That's very nice for you. Don't feel obliged to stay. I was about to take a nap anyway."

        rin "You need to do whatever you are going to do with that stuff anyway, right?"

        show rin relaxed_surprised
        with charachange

        rin "Or perhaps you like to watch girls sleeping?"

        hi "Ehh…"

        "I'm not sure what to make of this, but Rin looks serious."

        hi "Even if I did, I think I have to be going."

        hi "I… I'll catch you around, Tezuka."

        show rin basic_absent
        with charachange

        rin "You can call me Rin."

        show rin basic_awayabsent
        with charachange

        rin "I feel that our relationship is at this point good enough to warrant this much."

        "I was already turning to make my exit, but she draws me back in."

        hi "Fine, then I'm Hisao."

        show rin basic_deadpannormal
        with charachange

        rin "Then you are."

        "…"

        "Rin looks at me hard in the eyes but that intimidating feeling you get when someone stares at you isn't there."

        "It's like she's actually not looking at me at all."

        "She blinks a couple of times, and I can't figure out why a pause like this just popped between us out of nowhere."

        show rin basic_deadpandelight
        with charachange

        rin "See you later, Hisao."

        "There is something like a tiny smile there in her face, maybe."

        scene bg school_hallway3
        with locationchange

        play sound sfx_doorclose

        "I quietly back out of the room. As I shut the door in front of my face, I whisper to myself."

        hi "What an intriguing person…"

        "From inside, I hear a muffled, sing-song voice:"

        rin "I heard tha~t!"

        stop music

        if _in_replay:
            return

    label .waylay:
        scene bg school_hallway3

        show shizu behind_blank behind misha at center
        show misha hips_grin_close at center
        with hpunch

        mi "What did she hear?"

        play music music_comedy

        "I jump at the sudden appearance of Misha, who I had not heard approaching despite the completely empty hallway."

        "Somehow she had gotten to jumping distance of me without making a sound. Creepy. It briefly reminds me of Kenji's nutty theory about a global feminist conspiracy, but I push that thought aside."

        show misha at twoleft
        show shizu at tworight
        with charamove

        "Shizune, standing slightly behind Misha, looks aloof as she couldn't have heard the remark that drew Misha's attention, but Misha is visibly excited."

        show misha perky_confused_close
        with charachange

        mi "No wait, more importantly, who is in there? There's no club meetings today."

        "She tries to curiously peek past me, even though the door prevents her from seeing anyway."

        hi "What are you doing here?"

        mi "You took so long that we had to come check what's wrong. That's no good, Hicchan~."

        show misha hips_frown_close
        with charachange

        "She wags her finger at me scoldingly."

        mi "I found plywood, but everything else is still missing because you are tardy."

        hi "Oh, sorry. Err… I got the things here, was just going to bring them."

        show misha cross_frown_close
        with charachange

        mi "I think you were up to some mischief, Hicchan~! Who was in there with you, I wonder…"

        "Misha signs something quickly to Shizune, pointing at her own ear a couple of times."

        show shizu basic_angry
        with charachange

        show shizu at right
        with charamove

        play sound sfx_dooropen

        "Shizune immediately pushes her way past me and opens the door into the classroom I just left."

        "I can only imagine the shock she is experiencing."

        "With Shizune's diligence and attitude, the insolence of daring to deface school property by sleeping on top of it must be too much to bear."

        show shizu basic_frown
        with charachange

        "And indeed, she stares at Rin, frozen in place apart from the slight but noticeable trembling of her shoulders, from suppressed rage I'm sure."

        "Instead of blowing up, Shizune just takes a few deep breaths, adjusts her glasses and slams the door shut, turning to sign furiously at Misha."

        play sound sfx_doorslam

        show shizu cross_angry
        with vpunch

        "Maybe she did blow up but I can't understand it."

        show shizu behind_frown
        with charachange

        "She shoots a very loaded stare at me too, as if it was somehow my fault that Rin is sleeping on one of the tables."

        "I hope she's not getting any funny ideas about the reason of my tardiness."

        rin "Hello."

        "Rin's voice comes from the other side of the door and it takes a few eyeblinks to realize she might have trouble opening it."

        play sound sfx_dooropen

        "I open the door to find Rin directly behind it, looking at us with a half-interested, half-sleepy face."

        show rin relaxed_sleepy at offscreenright
        with None

        show shizu basic_frown:
            xpos 0.55 xanchor 0.5
        show rin at right
        with charamove

        rin "Hello."

        show shizu basic_frown
        with charachange

        shi "…"

        show misha cross_frown
        with charadistant

        mi "Miss Tezuka, what do you think you were doing? You absolutely are not permitted to use school property for such… err, disgraceful? activity!"

        show rin negative_confused
        with charachange

        rin "It sure is suddenly very crowded in here. I didn't know I was this popular."

        "It's hard to say whether she's happy or unhappy about this turn of events."

        "At any rate she ignores Shizune/Misha's scolding so they have no choice but to drop the issue."

        show shizu behind_frown
        with charachange

        "Shizune taps Misha's shoulder, points at Rin and makes some quick signs."

        shi "…"

        show misha sign_smile
        with charachange

        mi "Popularity aside, please don't do that any more."

        show shizu basic_angry
        with charachange

        shi "…"

        show misha hips_grin
        with charachange

        mi "Anyway, how is your project going? Will it be done for the festival?"

        show rin basic_awayabsent
        with charachange

        "Rin looks at them blankly, apparently at ease under the pressure Shizune's cold stare is putting on her."

        rin "I keep wondering about that myself too."

        show shizu behind_frustrated
        with charachange

        shi "…"

        mi "And…?"

        show rin relaxed_boredom
        with charachange

        rin "Will think about it harder."

        "As Misha signs her reply to Shizune her face turns into an unsatisfied frown."

        show shizu basic_frown
        with charachange

        shi "…"

        show misha hips_frown
        with charachange

        mi "Miss Tezuka, please try to take this seriously. It'll be a disaster if the wall looks like someone threw up their lunch onto it."

        show rin basic_absent
        with charachange

        "Rin nods assertively."

        rin "Will think more seriously."

        show misha cross_grin
        with charachange

        "Misha actually giggles at that, but Shizune doesn't, not even after translation."

        hide shizu
        hide misha
        with charaexit

        "She just shakes her head, takes the materials from me and takes off with Misha in tow."

        show rin basic_deadpanupset
        with charachange

        "Rin frowns thoughtfully as she looks after the retreating student council duo."

        rin "How rude."

        rin "It's true though, I must finish my project before the weekend. There will be dire consequences if I don't."

        rin "The end of the world as we know it.{w} Like weekends usually are, but more dire."

        rin "Much more dire."

        show rin relaxed_nonchalant
        with charachange

        rin "Maybe I'll postpone my nap. To unforeseen future."

        show rin at offscreenright
        with charamovefaster

        hide rin

        stop music fadeout 6.0

        "I am about to ask what project she has and what are these apocalyptic consequences, but she walks back into the art classroom."

        rin "Since you have nothing to do, would you give me a hand?"

        scene bg school_classroomart
        show rin basic_absent at center
        with locationchange

        rin "This paint can doesn't fit into my bag but I need it."

        "She kicks lightly at a huge can of paint that's lying on the floor next to the table she was sitting and sleeping on."

        "It lets out a dull clang."

        "Being the gentleman I am, I naturally pick it up."

        "Heavy."

        hi "Yeah, sure. Where do you need to take it?"

        show rin basic_awayabsent
        with charachange

        rin "Away."

        hide rin
        with charaexit

        "And with that, she takes off to the hallway, me and the paint can following since there's little choice for either of us."

        scene bg school_hallway3
        with locationchange

        "The hallway is quiet and empty now with Shizune and Misha gone, so we too leave towards the stairwell at the other end."

        scene bg school_staircase2
        with locationchange

        "Every ten or fifteen or twenty steps I have to change the can from one hand to another because the thin handle cuts into my palm. At least it keeps my arms from tiring too fast."

        "Rin strolls on beside me with an uneven pace that I have trouble matching, or maybe I am walking weird because of the extra weight."

        "It seems one of us is constantly walking too slow or too fast, and I can't figure out which."

        scene bg school_lobby at bgright
        with locationchange

        "Two flights of stairs below, trouble appears in the form of the head nurse and his fox-like grin."

        show nurse grin at center
        with charaenter

        play music music_nurse fadein 0.5

        nk "Ah, Mr. Nakai, what a happy coincidence! Tezuka too, of course."

        show nurse at twoleft
        show bg at center
        with charamove

        show rin basic_awayabsent at tworight
        with charaenter

        "He nods courteously to Rin who does not acknowledge him back, then turns to me because obviously it's me who he had some business with."

        show nurse concern
        with charachange

        nk "There is something I forgot to mention on Monday."

        "I nod and wait impassively because I can't even begin to guess what he forgot. The feeling of the handle delving deeper into my skin doesn't make me feel enthusiastic about this interruption, either."

        nk "It's about your medications. Since you haven't been that long on your current medications there might be some unexpected side effects, which might require adjusting dosages or even changing to another kind of medication."

        show nurse neutral
        with charachange

        nk "So we will do a few tests regularly, but what I'd want is for you to keep an eye on everything in your condition that feels off, if you get what I mean."

        nk "Nausea, headache, anything. And come see me if something happens."

        show rin basic_absent
        with charachange

        hi "All right."

        show nurse fabulous
        show rin basic_awayabsent
        with charachange

        nk "So how are you? Everything fine?"

        "I give up and drop the can to the floor before answering him. Apparently this takes longer than my biceps can handle."

        "I'm about to say something generic as an answer, but then I realize how often I've done that lately."

        "Other people have asked me that too. Teachers and students here. My parents, visitors, nurses, doctors at the hospital."

        "Everyone seems to be concerned about that. It's natural for a hospital, not so much for a school.{w} Except this school."

        "This is a small school, and both the student base and the faculty seem to be very tightly knit."

        "At least that's the feeling I'm getting."

        "And this is not the kind of school that gets transfer students too often."

        show rin basic_absent
        with charachange

        "The thought sends shivers up my spine, but I give a generic answer, anyway."

        "…"

        show nurse grin
        show rin basic_awayabsent
        with charachange

        nk "That's great. Also, one other thing."

        show nurse fabulous
        with charachange

        nk "My sources tell me that you've been at neither the school track nor even the pool, so I'd like to know if you have taken up exercising as I asked."

        "Of course I haven't, but his way of inquiring gives me the feeling that I should've been running my ass off on the track since the very first day."

        show rin basic_absent
        with charachange

        hi "You have people spying on me?"

        show nurse grin
        show rin basic_awayabsent
        with charachange

        nk "Not as such. I just happen to know a few people. But that's not the issue here, so don't try to slip out of it."

        show rin basic_absent
        with charachange

        hi "Well, I was actually just doing some improvised weight lifting, as an exercise."

        "I pick up and lift the can up and down a few times like some sad imitation of a bodybuilder, even though it's weighing down on my arms painfully."

        show nurse neutral
        show rin basic_awayabsent
        with charachange

        "The stupid grin disappears from his face for a second, then comes back like it was never gone."

        show nurse grin
        with charachange

        nk "Tezuka, would you give us a second?"

        stop music fadeout 1.0

        show bg at bgright
        show rin at offscreenright
        show nurse at center
        with charamovefaster

        show nurse neutral_close
        with charadistant

        hide rin

        "The nurse grabs me by the shoulder without waiting for Rin's permission which he didn't need in the first place and drags me aside."

        show nurse concern_close
        with charachange

        nk "When I told you to exercise I wasn't joking."

        nk "I understand that you are still on your first week and all, but please don't ignore the importance of this."

        nk "The reason I'm coming down this hard on you is that habits are not easy to form."

        nk "The more you slip and postpone, the harder it'll be. It's the same with everything, like dieting."

        menu:
            set choices
            with menueffect

            nk "Can you promise me to be more serious about this from now on?"

            "Yes.":
                $ promised = True

                call a1c7o1

            "Maybe.":
                $ promised = False

                call a1c7o2

        "He studies me for a moment and then shrugs, smiling again."

        play music music_nurse fadein 0.5

        show nurse neutral_close
        with charachange

        nk "Okay. That's more like it."

        nk "If you go to the school track tomorrow morning, you'll meet my 'spy,' who probably has no qualms offering consultation to you if you want to jog a bit."

        hi "Consultation?"

        show nurse fabulous_close
        with charachange

        nk "See you around."

        stop music fadeout 2.0

        hide nurse
        with charaexit

        show bg at bgleft
        show rin basic_awayabsent:
            xpos 0.8 xanchor 0.5 alpha 0.0
            ease 1.0 center alpha 1.0
        with charamove

        "He leaves with a wave of his hand and no answer, and I walk to Rin who has been waiting, idly leaning against the hallway wall and staring at the pale lighting fixtures in the ceiling."

        "Even when I approach, she doesn't move her eyes off them."

        rin "Are you getting medications for your heart thingy?"

        hi "Were you listening?"

        "It comes out more accusatory than I intended, accidentally lashing out on her."

        "But even so, I don't really want to start talking about it. I just met her, I don't know her. It's not her business."

        "The nurse seems to be happily ignorant about confidentiality too, talking about that kind of thing in public."

        "But it's not Rin's fault, is it?"

        "I look up at her, suddenly feeling a bit guilty, but Rin is just staring past my shoulder quizzically, her head tilted like a bird's."

        "Sigh."

        "I don't know why this is so hard for me. It feels like there is some inexplicable lock that prevents me from being more upfront about this."

        hi "…yeah. They're for my heart."

        show rin basic_absent at center
        with charachange

        rin "Will they make you better?"

        hi "…no, not really."

        hi "They just make me a little less worse."

        "Rin keeps looking at me for a while longer, and she neither says anything further, nor displays any kind of emotion I could discern."

        "I'm thankful that she doesn't. I think I'm still not quite used to all this."

        "At the hospital it was easy, but I still haven't sorted my feelings about having to live a 'normal' life with this disability."

        if _in_replay:
            return

    label .the_other_green:
        play music music_soothing fadein 4.0

        scene bg school_courtyard
        with locationchange

        "We leave the main building, and Rin leads us onwards towards the dorm."

        scene bg school_dormext_start
        with locationchange

        "We stop at the small patch of greenery in front of the dorm building."

        "The dorm is built on a slightly elevated ground, with a wall and a few trees that everyone has to circle around every time they come or go. It's probably the only inconvenient design in the school."

        "The entire wall, made of the same kind of bricks as the building itself, has been covered with some sort of a painting."

        "Most of it is still mere sketches, quick lines drawn with black and white against the gray plastering that covers almost the entire length of the wall, but some places look a bit more finished."

        "There are human faces and legs and hands, I can't quite say what the painting as a whole might portray."

        "Stacks of what seem to be paint cans are arranged in piles on the ground, beside the wall."

        show rin basic_awayabsent at tworight
        with charaenter

        rin "See, the left side is hardly off the ground yet."

        show rin basic_deadpannormal
        with charachange

        rin "It's because I couldn't get in the mood yesterday so I gave up and went to meditate instead. Then it was suddenly morning."

        show rin negative_spaciness
        with charachange

        rin "I have to work on it, but the guys from art class are helping with the negative spaces and base surfaces whenever, which is a problem."

        rin "It's easier to paint big areas if there are a lot of people, with hands."

        show rin basic_deadpan
        with charachange

        rin "The reach is better, and it's faster too."

        "She goes on a tangent of a tangent, waving a little with her arm, or whatever of it there actually is, to demonstrate even though I got the point already."

        "The white cotton of her sleeve flaps around, and it makes me think it could look sadder than it does."

        "But it makes me feel out of place, like almost every tangible reminder of the student base's… special properties has in the past few days."

        "This girl doesn't notice my dreary feelings of course, or the fact that she lost me a while ago already… and just keeps on blabbering."

        rin "…so that's why I'm trying to figure out if there is something I need to figure out and then figure that out before it's too late and all hope is lost."

        hi "Why would the hope be lost?"

        show rin basic_awayabsent
        with charachange

        rin "Because paint has to be painted and then it has to dry and then it has to be painted over with another kind of paint."

        show rin basic_absent
        with charachange

        rin "It takes time."

        "She finally stops, apparently thinking she made some kind of a statement that makes sense."

        "I think it's best to start from the top."

        hi "So, this is your project? You did… this?"

        show rin basic_deadpan
        with charachange

        rin "Yes. Yes."

        hi "All of it?"

        rin "Yes."

        hi "Nice. But…"

        "I stumble with my words, suddenly feeling like I've walked straight into the mine field of political incorrectness."

        show rin basic_deadpanamused
        with charachange

        rin "It's ok, you can say it. I probably won't get mad."

        "I blush really hard. I don't really know what would be the right thing to say, if any. It feels that I'm way more sensitive than Rin is, though."

        "This is really awkward."

        show rin basic_deadpansurprised
        with charachange

        rin "Don't you want to ask?"

        hi "…How do you paint without hands?"

        show rin basic_amused
        with charachange

        rin "See, I'm an easy person to talk to, right? With my feet."

        hi "I almost guessed that already, but isn't that hard to do?"

        show rin basic_delight
        with charachange

        rin "You're good at guessing. Anyway, I don't think it is. But maybe I'm used to it by now."

        "I can't get my mind around the fact that she could be an artist, but seeing how adept she was using her feet to eat I figure painting might not be a problem either."

        "Neither of us has anything more to add to the subject."

        show rin basic_awayabsent
        with charachange

        rin "The afternoon light works pretty well. I was afraid it would look too flat but it's not like that after all."

        show rin basic_absent
        with charachange

        rin "I think it's actually pretty interesting. I wanted to see what it looks like in dim light. Do you think it's flat?"

        hi "Eeeh well, paintings tend to be flat."

        show rin basic_deadpan
        with charachange

        rin "Not like that flat. You know, flat. Like some people are, no substance, no meat where there should be some."

        rin "I know a few girls who—{w=.5}{nw}"

        hi "Okay I get it. But I couldn't really tell, I'm not that good with art. I can't name many artists or artistic terms."

        hi "So I don't really have anything to say."

        show rin relaxed_nonchalant
        with charachange

        "Rin shrugs her shoulders at that, saying 'suit yourself' without saying it and looks up at the sky as if trying to look for something up there."

        rin "I didn't think I'd get any actual work done but if you give me a hand with the paints I could do a little before it's too dark."

        show rin basic_awayabsent
        with charachange

        rin "I wanted to get a halogen lamp like the ones they have at the sports track but there aren't any."

        "Rin sure is quick to recruit my help, as was Shizune. It really makes me feel that the festival is such a big project that every pair of hands is needed."

        hi "Why not? I'm not really sure if I can be of any help, though."

        show rin basic_absent
        with charachange

        rin "It's just mixing some paints, you can do that. Probably. Do you have motor control problems, like you know, those people who have some?"

        show rin basic_deadpan
        with charachange

        rin "Cerebral palsy, maybe?"

        hi "Not that I know of."

        show rin basic_deadpanamused
        with charachange

        rin "I get it. Heart thingy has nothing to do with that."

        "She gives me a sly look for no reason."

        hi "No, it doesn't."

        show rin basic_amused
        with charachange

        rin "Let's do it then."

        hide rin
        with charaexit

        stop music fadeout 7.0

        "So she sits on an empty wooden box and very naturally picks up a wide brush between the toes of her bare right foot."

        "I open a few of the cans and pour some of the contents into shallow bowls for mixing."

        "The thick paints flow lazily from the can to the bowl, like syrup."

        "I mix them, creating funny, hypnotic looking swirl patterns that melt quickly into each other to form a new monotone hue."

        "Rin sets to work, every now and then asking me for a hand with something or the other."

        "…"

        "Finding different brushes is easy enough, but mixing the paints to be the exact tone this girl is apparently seeing in her head is a frustrating ordeal."

        "She wants precision down to the last milliliter before she is satisfied, but her instructions are obscure at best."

        play music music_another fadein 1.0

        scene bg mural_start
        show rin basic_deadpan_close at tworight
        with locationchange

        rin "Add half a splash of green."

        show rin negative_spaciness_close
        with charachange

        "I crouch down to pick up the can of bright green."

        show rin basic_deadpan_close
        with charachange

        rin "The other green. This green."

        show rin negative_spaciness_close
        with charachange

        "I carefully pour some of the other green paint into the mixing bowl."

        show rin basic_deadpan_close
        with charachange

        rin "No, that's almost a whole splash. More white."

        rin "Is green a good color to add?"

        hi "No idea. You're the artist here."

        show rin basic_deadpanamused_close
        with charachange

        "A hint of smile appears in the corners of her mouth."

        rin "Do you lack an opinion?"

        hi "No, it's just that I have no idea."

        show rin basic_deadpandelight_close
        with charachange

        rin "It's OK, because I just got an idea. Add more white."

        "With this exclamation I pour a minuscule amount of white into the bowl and mix it. It looks slightly… whiter."

        show rin basic_deadpanupset_close
        with charachange

        rin "That's not good. It has to be like… like the color when you wake up and you {b}know{/b} that you saw the meaning of life in your dream but can't remember it."

        rin "Maybe it's yellow…"

        show rin negative_spaciness_close
        with charachange

        "…"

        "Despite the impossibility of mixing a color like the change of seasons or any other nonsense that's being imposed on me, I find myself enjoying it more than I thought I would."

        stop music fadeout 7.0

        scene bg school_dormext_start_ss
        with shorttimeskip

        "Seeing a painting being born on the plastered wall feels like magic."

        "I spend the moments I have between mixing paints crouching down on the paving and just looking at her work."

        "It feels slightly intrusive at first, like breaking some imaginary intimacy, but Rin doesn't seem to mind the least bit. Maybe it's just in my head."

        "Her entire presence emits a completely different air as she patiently works the details, adding layers of paint on top of other layers of paint, steadily moving her foot across the wall to add new shapes."

        "When I manage to produce a passable mixture of paint, the rare smile on her face is oddly rewarding."

        "Apart from the few words when discussing paint mixes, neither of us says a word for the longest time."

        "And even those short discussions soon evolve into a shorthand, both of us developing and using weird impromptu code words for various paints and hues."

        "As if there was some need to conserve words and breath and sound."

        $ renpy.music.set_volume(0.1, 0.0, channel="ambient")
        play ambient sfx_cicadas fadein 4.0

        scene bg school_dormext_half_ni
        with Dissolve(4.0)

        "We stay there late into the evening until it becomes too dark to paint properly."

        stop ambient fadeout 3.0

        scene black
        with Dissolve(3.0)

        if _in_replay:
            return

    return

label separate_of_sss_and_mc:
    stop ambient
    play sound sfx_impact
    with vpunch

    scene black
    with Dissolve(0.2)

    hi "Ouch…"

    play music music_emi fadein 2.0

    show ev emi_knockeddown_facepullout
    with openeye

    "Opening my eyes, I see a pair of saucer-like green eyes looking up at me."

    show ev emi_knockeddown_largepullout
    with flash

    "They belong to the perpetrator, a short girl who bumped into me and has now fallen down onto the hallway floor."

    "She wears a PE uniform and a very worried frown. The former strikes me as a rather strange thing to have on during a lunch break."

    "…More striking than that, though, is that she doesn't have legs."

    show ev emi_knockeddown_legs
    with flash

    "Or she does, but they are not flesh and bone. Her pale and very much flesh-and-bone thighs end in shins and feet made of some black metallic or plastic-like material."

    "They look disturbingly artificial and unnatural. It almost makes me forget that my chest is hurting."

    show ev emi_knockeddown at center
    with flash

    "The girl winces a little, rubs her nose and jumps up."

    scene bg school_hallway3 at bgleft
    with locationchange

    show emi sad_depressed_gym at offscreenbottom
    with None

    show emi at center
    with charamovefaster

    emi_ "Aw man… Hey, are you all right? I'm sorry about that, really!"

    emi_ "I wasn't looking where I was going, and you just came out of nowhere. Sorry… Sorry!"

    "She's looking really apologetic, in the hurt puppy way of looking apologetic."

    "I quickly forget about being angry or anything, since hurt puppies are my weak spot."

    stop music fadeout 2.0

    hi "It's okay. Don't worry about it… ouch…"

    play sound sfx_heartfast
    show heartattack alpha
    with Dissolve (0.1)

    hide heartattack alpha
    with Dissolve (0.7)

    "I say that, but there's a stinging pain growing in my chest, and I know that this is about the biggest possible danger for my condition."

    "Don't overexert yourself, don't forget your medication and most of all, don't get hit in the chest."

    play sound sfx_heartslow
    show heartattack alpha
    with Dissolve (0.1)

    hide heartattack alpha
    with Dissolve (0.7)

    "I try to rub my solar plexus to chase the pain away, holding my breath in an attempt to hear my heartbeat."

    play sound sfx_heartslow
    show heartattack alpha
    with Dissolve (0.1)

    hide heartattack alpha
    with Dissolve (0.7)

    pause 1.0

    play sound sfx_heartslow
    show heartattack alpha
    with Dissolve (0.1)

    hide heartattack alpha
    with Dissolve (0.7)

    pause 1.0

    play sound sfx_heartslow
    show heartattack alpha
    with Dissolve (0.1)

    hide heartattack alpha
    with Dissolve (0.7)

    pause 1.0

    "It seems normal…"

    show emi basic_shock_gym
    with charachange

    emi_ "Hey, should I get a nurse?"

    play music music_emi fadein 0.2

    "The worried, high-pitched voice of the girl snaps me out of it."

    "I stare at her for a few seconds dumbfounded, until I realize that I probably looked worse off than I really was, doubled over myself and looking all tense."

    "Damn, I'm overly worried about my heart."

    hi "Err… no need, I'm fine."

    "Managing to say something in response, I pull myself upright, feeling my sore ribs one last time, and take a deep breath."

    "She just knocked the wind out of me. Big time. But it's nothing more than that."

    show emi basic_hes_gym
    with charachange

    emi_ "You sure you're okay? I hit you pretty hard."

    hi "It's okay. I said I was fine, and nothing's broken. No harm done."

    show emi basic_happy_gym
    with charachange

    emi_ "That's good! I was—"

    return

label a1c6o1:
    stop music fadeout 6.0

    "I do what I always do when I don't know what to do."

    "Like now."

    "I've already started on one of the books I borrowed yesterday, and took it with me to school to fill the empty moments between classes."

    hide hanako
    with charaexit

    "I find the page that I creased a corner of to mark the spot I left yesterday night, and pick up from there."

    "Misha and Shizune are still arguing heatedly, probably about restaurants still."

    "If I joined them, I'd just get caught up in that, or worse, get grilled about joining the Student Council."

    "Misha isn't speaking aloud since there is nobody who'd need to hear what they are talking about."

    "But why does she tend to sign things even when Shizune doesn't need to understand what's being said, or even more strangely, when Shizune is not around at all? What an odd conflict of habits."

    "I find it hard to focus on the book, and besides, the lunch break beckons me to leave the dullness of the classroom. I do so, heading down for the cafeteria."

    "Misha and Shizune, having come to a conclusion of one kind or another, follow in my wake though still talking in their animated fashion."

    stop music fadeout 2.0

    return

label a1c6o2:
    "I still feel bad for making her run away yesterday, so I'd better say something."

    show hanako at center
    show bg at bgleft
    with charamove

    hi "Um, hey there, Hanako."

    show hanako def_shock
    with vpunch

    ha "H… Hisao?"

    "Well, at least she remembers my name."

    hi "Hey… I just wanted to apologize for yesterday."

    hi "I didn't mean to startle you or anything."

    hi "I'm just new here and thought I should get to know my classmates."

    show hanako basic_bashful
    with charachange

    "As Hanako looks up at me, I notice her scarring once more."

    "It's a little bewildering that you can barely notice it from across the room, but it's so noticeable from close up."

    show hanako cover_bashful
    with charachange

    ha "T… that's okay."

    ha "It… it was my fault."

    hi "Nah, that wasn't anyone's 'fault,' it just kind of happened."

    hi "So, are you waiting for someone? I saw you looking at the door before…"

    show hanako basic_normal
    with charachange

    ha "Y-yes… Lilly."

    hi "Oh, you mean Lilly the blind girl?"

    "Hanako only nods in response, and I can't help but wonder if defining people through their disabilities is a faux pas of the worst kind or just normal here."

    "I guess that explains why Lilly took off after her yesterday."

    hi "She seems like a nice girl. Are you two friends?"

    show hanako basic_bashful
    with charachange

    ha "Y-yes."

    show hanako basic_distant
    with charachange

    "As if hoping for Lilly to appear, she checks over her shoulder again."

    stop music fadeout 6.0

    "I think I'm making her nervous again."

    hi "I hope I'm not disturbing you right now…"

    show hanako basic_bashful
    with charachange

    ha "N-no, that's not it."

    ha "It's just easier if Lilly doesn't come here…"

    hi "Oh, because it's hard to get around the classroom?"

    show hanako basic_distant
    with charachange

    ha "Not… really."

    "Hanako's gaze drifts past my shoulder and towards Shizune."

    hi "Shizune?"

    "Hanako nods again."

    hi "What about her? Don't they get along?"

    "Hanako shakes her head. Clearly this is something she doesn't want to talk about."

    "It does make a strange sort of sense, Shizune and Lilly not getting along so well."

    "Communication between the two would be all but impossible. It's hard enough talking to Shizune through Misha, even when you can see whose hands are 'talking.'"

    "Hanako is so focused on Shizune that I am the first to notice Lilly at the door."

    hi "Oh, she's here now."

    show hanako defarms_shock
    with charachange

    "Hanako spins around to confirm this. Upon seeing Lilly, she moves quickly to the door."

    show hanako at tworight
    show bg at center
    with charamove

    show lilly cane_weaksmile at twoleft
    with charaenter

    play music music_lilly fadein 3.0

    show hanako emb_smile
    with charachange

    ha "Lilly…"

    show lilly cane_smile
    with charachange

    li "Ah, Hanako. Good morning. Is the president here?"

    show hanako emb_downtimid
    with charachange

    ha "Y-yes."

    show hanako basic_distant
    with charachange

    "Hanako glances over her shoulder at Shizune again, as if to confirm she can't hear them even though that's impossible."

    show lilly cane_sad
    with charachange

    li "I suppose we'd best be off, then."

    "Lilly's sigh and tone of what seems like frustration makes me raise an eyebrow. I guess there's some kind of enmity between the two."

    "It's intriguing, but that's not really something I'd ask about. I'm sure if they wanted me to know, then they would tell me."

    "It's only my third day here; I should be trying to make friends, not finding out why people are enemies."

    "Still, it's a little funny to find out that this school has little feuds, just like my old high school."

    "Even if people are more tolerant of others, they're still going to get on each other's nerves."

    hi "Hey Lilly. How are things? I'm sorry I made you run off yesterday…"

    show lilly cane_surprised
    with charachange

    li "Oh my, is that Hisao? I didn't realize you were here…"

    "It seems that Lilly is a little embarrassed about being so frank in front of me."

    show hanako emb_sad
    with charachange

    ha "S-sorry Lilly. I thought you realized…"

    show lilly cane_weaksmile
    with charachange

    li "No, it's all right, Hanako."

    li "Hisao, please don't worry about yesterday. It was just a misunderstanding."

    hi "If… you say so. I'm still working this place out."

    show lilly cane_smile
    with charachange

    li "Well then, I think you'll find most people here a lot more forgiving than elsewhere."

    li "If you are feeling a little confused, please don't be afraid to ask questions."

    hi "Sure, I'll remember that."

    show hanako emb_timid
    with charachange

    ha "Um… Lilly…"

    show lilly cane_weaksmile
    with charachange

    "Lilly gives a small nod of acknowledgment."

    li "I'm sorry Hisao, but we must be off."

    "Hanako really doesn't look all that comfortable here right now, and Lilly still seems a little embarrassed."

    "I wonder if my apologies really made any impact."

    hi "Mind if I accompany you two?"

    show lilly cane_smile
    with charachange

    "I know I'm kinda pushing it, but… Lilly hmms quietly, still smiling."

    show lilly cane_weaksmile
    with charachange

    li "I'm sure that we could accommodate you, can't we, Hanako?"

    show hanako emb_downsad
    with charachangealways

    show hanako basic_worry
    with charachangealways

    "She looks at Lilly, then at me, and then she freezes, wide-eyed."

    ha "S… sure."

    show lilly cane_cheerful
    with charachange

    li "Well then, shall we go?"

    "I'm sure Lilly wouldn't do this so easily if she saw how scared Hanako looks, but it can't be helped now."

    "Declining after the deal is sealed would only cause confusion and problems."

    stop music fadeout 1.0

    return

label a1c6o3:
    hide hanako
    with charaexit

    show misha sign_smile at twoleft
    show shizu adjust_happy at tworight
    with charaenter

    "Misha and Shizune are still arguing about their choice for lunch place, incomprehensible for a pair of high school students who have to take a taxi at least to make it to downtown and back in time."

    hi "Haven't you finished, already?"

    show misha hips_grin
    with charachange

    mi "Oh, sorry Hicchan! Were you waiting for us?"

    show shizu behind_smile
    with charachange

    shi "…"

    show misha hips_smile
    with charachange

    mi "You don't have any plans?"

    hi "Plans?"

    mi "For lunch?"

    hi "Well, I don't, so I thought I could hang with you guys."

    show misha sign_smile
    with charachangealways

    show misha perky_smile
    with charachangealways

    "Misha smiles victoriously at my lack of plans, and excitedly translates my response to Shizune."

    show shizu adjust_smug
    with charachange

    shi "…"

    show misha hips_grin
    with charachange

    stop music fadeout 5.0

    mi "If you don't have anything specific planned out, do you want to eat lunch with me and Shicchan? Ah, we're going to go to town for lunch, though… Don't worry, Hicchan, it's not that far."

    hi "Sure, I'll come with you."

    "And with that, we leave the classroom."

    return

label a1c7o1:
    hi "Yeah, I promise. Definitely."

    return

label a1c7o2:
    hi "Maybe, no… I mean…"

    "He gives me a nasty sort of look when I say that, making me try to take back the word."

    hi "I mean, I don't know… I'm still trying to get used to the school."

    hi "I'll promise to try though."

    nk "You're not being very convincing there, Hisao. Tip number one: medical professionals are not amused if you take their advice lightly."

    "What's up with him? As if a day or two would make that much of a difference."

    "I didn't do anything at the hospital either."

    hi "Yeah, okay. Sorry."

    return
