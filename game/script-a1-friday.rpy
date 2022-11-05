# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a1_friday:
    call timeskip

    if promised:
        label .exercise:
            scene black

            play sound sfx_alarmclock

            scene bg school_dormhisao
            with openeye

            "My morning alarm goes off, and I flail about uselessly for a while until I remember that I'd decided to give morning runs another shot."

            "I don't know if this was my greatest idea, but I'm determined to keep going."

            "This is about my health, after all."

            "Sure, things haven't been great lately for me, but that hasn't made existence so intolerable that I'm not going to try everything I can to stay healthy."

            "Besides, it's all about asserting some kind of control over this thing, right?"

            "If I can manage that, well, I can manage anything."

            "At least that's what I keep telling myself."

            scene bg school_track
            with locationskip

            play ambient sfx_emirunning fadein 0.3

            "Once again, it would appear that I'm not alone in my run."

            "Emi has apparently been here for some time."

            "It looks like she's already worked up a good sweat."

            "Just when the hell does she come down here, anyway?"

            stop ambient fadeout 0.3

            show emi basic_grin_gym at center
            with charaenter

            play music music_emi fadein 0.5

            emi "Oh, it's you!"

            show emi basic_closedgrin_gym
            with charachange

            emi "I'm surprised to see you again!"

            hi "Why's that?"

            show emi basic_grin_gym
            with charachange

            emi "Well, not many people actually manage to come back for a second try."

            show emi basic_annoyed_gym
            with charachange

            "She frowns, seemingly annoyed by a passing thought."

            emi "Like the rest of the track team, for instance."

            emi "Still, it was only supposed to be on a volunteer basis, so it's not that big of a shock."

            emi "And I guess it's pretty early in the morning…"

            "A shrug, and suddenly it appears that she's forgotten what she was talking about."

            show emi basic_happy_gym
            with charachange

            "The frown disappears entirely, and she seems to snap back to her previous train of thought."

            emi "So! Come on, then!"

            hi "What?"

            show emi excited_proud_gym
            with charachange

            emi "You're here to run again, right?"

            hi "Well, yes."

            show emi basic_closedhappy_gym
            with charachange

            emi "So come on!"

            scene bg school_track_on
            with locationchange

            "I find myself suddenly grabbed and yanked onto the track."

            play ambient sfx_emijogging fadein 0.3

            scene bg school_track_running
            with locationchange

            "Things seem to be set on mirroring yesterday's run."

            "That is, I seem to be struggling, while Emi moves with an effortlessness that I find enviable."

            "It's incredibly bothersome, to be so easily worn out."

            "I know I should be patient, work toward things gradually, but…"

            "It's difficult to stay positive about this."

            "We round the track and start on our second lap."

            play ambient sfx_emirunning

            "Emi seems to have grown impatient keeping pace with me, and begins to pull away."

            "This is where I gave out yesterday."

            menu:
                "Will I be able to do more?"
                with menueffect

                "Go for it.":
                    $ go_for_it = True
                    $ favor_emi = True

                    call a1c9o1
                "Take it easy.":
                    $ go_for_it = False

                    call a1c9o2

            if _in_replay:
                return

    if not promised or not go_for_it:
        label .invisible_hat:
            if not promised or _in_replay:
                scene black

                scene bg school_dormhisao
                with openeye

                pause 0.2

                scene bg school_dormbathroom
                with locationskip

                "I wake up and take a hot shower."

            scene bg school_dormhisao
            with locationskip

            "Back in my room, the first thing I see is the familiar row of medication bottles lined up on top of my dresser, and it makes me depressed, as usual."

            "It's annoying. I thought I was okay. I thought I had made my peace with this thing, gotten over it."

            "But what I really did… I allowed myself to forget that I have a problem. Being here really reminds me of the reality, and trying to fight against it just hurts."

            "Reflecting on it is only going to do so much. I've done this before, for months. It seems like it's time to get over it."

            "If I allow myself to forget that my life is definitely not going to be as long as those of others, I won't get anywhere."

            "My life may be different from others. But it is a life in progress."

            "That is how I'll rationalize it."

            "I down the usual handful of pills, trying to push the sudden dreary feeling out of my head. Then I prepare to head out to class early, as usual."

            scene bg school_dormhallway
            with locationchange

            "As I step into the hallway, I notice Kenji coming around the hallway corner, stealthily making his way over to his own room with a large bag. As he sneaks past me soundlessly like a ninja hiding in plain sight, I call out to him."

            hi "Hey."

            show kenji neutral at center
            with charaenter

            play music music_kenji fadein 0.5

            "He jumps at the sound of my voice."

            ke "Oh, hey, man. I didn't notice you there. I'm really tired."

            "I think it's more like he didn't see me, but that's not the issue."

            hi "Where have you been this early? Shopping?"

            show kenji tsun
            with charachange

            ke "Nah, I wasn't shopping. Sometimes I have to visit… the math teacher. Yeah, I figured it would be a good idea to find out when the next exam is, since he tells you in advance if you want."

            hi "So then, what's in the bag?"

            show kenji neutral
            with charachange

            ke "I thought I'd go shopping while I was outside. I need supplies to continue the fight against the vast feminist conspiracy."

            hi "Uh, okay."

            hi "I thought you didn't go outside."

            show kenji happy
            with charachange

            ke "I wear a hat now."

            "I decide to not point out that he is not wearing a hat."

            "An awkward silence settles between us and then Kenji breaks it by pushing his door open slowly, releasing a creaking sound into the air that only makes the moment seem more awkward. He sets the bag down inside his room and then closes the door."

            hi "I'm surprised you went out of your way to find out a test date. Trying to take advantage of an opportunity to study is pretty diligent."

            show kenji tsun
            with charachange

            ke "I never study."

            hi "Oh…"

            show kenji neutral
            with charachange

            ke "I just wanted to know when the next test day was. I'm still going to take it, duh. I need to know so I know what day I can't afford to skip class. He usually sends out updates on that crap by phone, so I had to step out and check up on it."

            hi "And why do you have to go out, when you can get it on your phone?"

            show kenji tsun
            with charachange

            ke "I don't carry a phone."

            hi "What do you mean you don't carry a phone? You mean you just leave it at home?"

            show kenji neutral
            with charachange

            ke "Nah, I don't use phones. I don't have a phone. Phones. I have no phone."

            hi "Why don't you have a phone? How can you not have a phone? No phone at all? No phone?"

            show kenji tsun
            with charachange

            ke "I just don't like phones. Actually, I'm kind of scared of them. I don't know why. I think it's some kind of repressed trauma."

            ke "But, basically, when I hear a phone, I get nervous. It's my darkest secret."

            show kenji neutral
            with charachange

            ke "I have two theories on it: either I have some fear of receiving some undefined, ominous, life-altering doom call, or I was beaten with a phone in the past. Beaten so badly I can't remember it."

            hi "Beaten in the head."

            show kenji tsun
            with charachange

            ke "Well, where else could I get beaten with a phone that would make me unable to remember it? The ass?"

            "Unexpectedly logical. I feel very depressed now. Sensing this conversation is more or less over, Kenji opens his door again and prepares to head inside."

            show kenji neutral
            with charachange

            ke "Yeah, I'm going to sleep, dude. Have a good one."

            hi "Class is going to start in like twenty minutes."

            show kenji tsun
            with charachange

            ke "I already did something today. Too tired to go to school."

            show kenji happy_close
            with characlose

            ke "Hey, you need some lip balm? I accidentally bought two because I thought the store had started selling individual double A batteries."

            hi "Thanks but no thanks."

            if not side_lilly and wait_for_shizu or _in_replay:
                show kenji tsun_close
                with charachange

                ke "Whatever, man."

                stop music fadeout 2.0

                hide kenji
                with charaexit

                "He swiftly enters his lair, finally letting me go to the class."

            if _in_replay:
                return

    if (not promised or not go_for_it) and wait_for_shizu:
        label .home_field_advantage:
            scene bg school_dormhallway
            if side_lilly:
                show kenji happy_close at center

            stop music fadeout 0.3

            play sound sfx_doorslam

            if side_lilly:
                show kenji tsun_close
            with vpunch

            "The door down the hall opens with a crack as it swings forward from being pushed opened too strongly and crashing against the wall. The sound is followed by a peal of bubbly laughter, and I instantly know who it is."

            play music music_comedy fadein 0.3

            show misha perky_smile behind kenji at center
            show shizu basic_normal2 behind kenji at center
            with zoomin

            if side_lilly:
                show kenji:
                    0.25
                    easeout 0.5 alpha 0.0 offscreenleft
                with None

            show shizu at tworight
            show misha at twoleft
            with charamovefaster

            if side_lilly:
                hide kenji

            play sound sfx_impact2

            "At the noise, Kenji disappears into his room like a ninja, slamming the door shut just as Shizune and Misha walk over, the former taking small, efficient steps towards me while the latter more or less bounces off the walls."

            show misha hips_smile_close
            with characlose

            "I try to do the same as Kenji, but it's too late. Misha puts her foot between my door to prevent me closing it, so I have no other choice but to let them in."

            scene bg school_dormhisao
            with locationskip

            show shizu behind_smile at center
            with charaenter

            shi "…"

            show shizu at tworight
            with charamove

            show misha hips_grin at twoleft
            with charaenter

            mi "Hi, Hicchan~! Hi~ hi~!"

            hi "Hi."

            hi "What are you two doing here?"

            "I wonder if the pause between those two sentences was politely long enough."

            show shizu basic_normal
            with charachange

            shi "…"

            show misha hips_frown
            with charachange

            mi "Hicchan, that's rude~! We came to pick you up!"

            show misha hips_smile
            with charachange

            mi "Did you think we thought you were going to escape and came to make sure you didn't? Surely not, Hicchan~!"

            hi "Hey, I didn't say that that's what you were here for."

            "But now I know it's exactly what they are here for."

            show misha sign_smile
            with charachange

            mi "It's time for student council work, yes it is~!"

            show misha hips_grin
            with charachange

            mi "Aren't you happy, Hicchan, to be able to help the whole~ school~! You are like, a hero~! The future generations will tell stories of this day!"

            "Interesting. I didn't think joining the Student Council would be a heroic deed worthy of Hercules."

            hi "Well… I guess I did promise so…"

            show shizu adjust_happy
            with charachange

            stop music fadeout 7.0

            "I've neglected Shizune, and only now do I notice her in the corner of my vision, peering around my room over my shoulder, her analytical eyes darting from object to object…"

            "This is kinda intrusive, the feeling of being exposed crawls in my balls. Luckily I don't have dirty laundry on the floor or anything like that."

            show shizu behind_smile
            with charachange

            shi "…"

            show misha perky_confused
            with charachange

            mi "Hm~? What is it, Shicchan?"

            show misha hips_smile
            with charachange

            mi "Yeah, this is Hicchan's room~! We haven't seen it before, I didn't even realize!"

            show misha hips_grin
            with charachange

            mi "It's kinda plain, but Hicchan hasn't had time to decorate it yet, isn't that so~?"

            show misha sign_smile
            with charachange

            mi "What are those?"

            "She points at my collection of medications on the night table."

            menu:
                with menueffect

                "I don't really want to talk about it with these two."

                "Try to dodge the subject." if True:
                    $ kick_shizu = False
                    $ force_route = FR_SHIZU

                    call a1c10o1

                "Kick them out of my room." if True:
                    $ kick_shizu = True
                    $ get_kenji = True

                    call a1c10o2

            if _in_replay:
                return

    if not force_route and (not promised or not go_for_it):
        label .no_recovery:
            scene bg school_scienceroom
            with locationskip

            "For a change, I'm not among the first ones to come to morning class."

            "Instead, almost everyone else seems to be here already. I recognize most of my class by their faces by now, though the names escape me still."

            if wait_for_shizu and not kick_shizu or _in_replay:
                call class_goes_lazily
            else:
                call mas_doesnt_bother

            if _in_replay:
                return

    if promised and go_for_it:
        label .slow_recovery:
            scene bg school_hallway3
            with shorttimeskip

            "The halls are quiet as the courtyard was, naturally so since everyone is in class. I knock lightly at the door of 3-3 and push open the door when Mutou calls from the other side."

            scene bg school_scienceroom
            with locationchange

            hi "Sorry I'm late."

            "Fifteen pairs of eyes turn to me."

            show muto irritated at center
            with charaenter

            mu "Good morning, Nakai."

            "Mutou seems to be somewhat confounded by my coming in late, as if I interrupted his flow or something."

            "Judging from the rambling lectures his classes tend to be, that might be the case."

            "I pass him the note the nurse gave me. Mutou takes it with a nod and reads it quickly."

            show muto normal
            with charachange

            "He lifts his eyebrows and gives me a kind of a stern look but doesn't say anything, just nods solemnly again."

            "I shrug and he gestures at me to run along so I naturally do."

            hide muto
            with charaexit

            "Only two pairs of eyes remain keenly following me as I walk to my seat."

            "I'm not surprised in the least when I feel Misha's fingernail prickle through my shirt about fifteen seconds after seating myself."

            show misha perky_smile_close at offscreenleft
            with None

            show bg at bgright
            show misha:
                xalign -0.3
            with charamove

            play music music_another fadein 2.0

            mi "Psst! Where were you?"

            hi "None of your business."

            "I know this is probably the worst answer I can give as it only serves to pique their curiosity, but I have no energy to come up with elaborate cover stories right now."

            show misha perky_confused_close
            with charachange

            show bg at center
            show misha at offscreenleft
            with charamove

            "However, Misha backs off. She's unexpectedly fast to give up today."

            "…"

            "In a minute, she's back at poking me with her finger."

            show bg at bgright
            show misha hips_grin_close:
                xalign -0.3
            with charamove

            mi "Come on, tell us! Shicchan is very interested too!"

            "It was just my wishful thinking. She just talked about it with Shizune, probably devising ways to get me to spill the beans."

            hi "No."

            show misha perky_sad_close
            with charachange

            show bg at center
            show misha at offscreenleft
            with charamove

            "She retreats to negotiate again."

            show bg at bgright
            show misha sign_smile_close:
                xalign -0.3
            with charamove

            menu:
                with menueffect

                mi "As a member of the Student Council, it's your duty to tell us why you are skipping class! Especially if it's something fun fun fun~!"

                "Yeah, I sure was having fun fun fun at the nurse's office…" if True:
                    $ get_kenji = True

                    call a1c11o1
                    call mas_doesnt_bother

                "I don't want to talk about it, okay?" if True:
                    call a1c11o2

            if _in_replay:
                return

    if force_route == FR_SHIZU:
        label .no_free_lunch:
            scene bg school_council
            with locationchange

            show misha perky_smile at twoleft
            show shizu behind_smile at tworight
            with charaenter

            "Once inside the office, I look around and see that it's deserted."

            hi "I guess this means there isn't a lot of work left, huh? Since there's no one here, and all."

            show misha sign_smile
            with charachange

            mi "It's always like this, Hicchan~!"

            "This confirms what I have thought before but have never actually been able to confirm definitively: Shizune and Misha are the Student Council. The whole Student Council."

            hi "Damn. So it's true. The Student Council is really only you two."

            play music music_ease fadein 4.0

            show misha hips_grin
            show shizu cross_wut
            with charachange

            "Shizune looks as if she's stuck wondering whether to be ashamed or explode with anger, and Misha is equally divided between laughing and trying to stop her."

            show shizu behind_frustrated
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "Well, then, Hicchan, you'll be happy to know that since it's just us three, we have a lot to do! A lot~! A lot~ lot~ lot~…"

            hi "That does not make me happy."

            show shizu adjust_happy
            with charachange

            "But it seems to make Shizune very happy."

            show misha cross_laugh
            with charachange

            mi "Wahaha~!"

            show misha hips_grin
            with charachange

            mi "Just kidding!"

            if promised and go_for_it or _in_replay:
                scene bg school_council
                with shorttimeskip

                "The work turns out to be sorting and double-checking the considerable amount of paperwork necessary for an event such as the school festival to get done."

                "Bureaucracy is a mindboggling thing."

                play sound sfx_normalbell

                "But we manage to finish it just when the lunch bells ring."

                show misha hips_grin at twoleft
                show shizu adjust_happy at tworight
                with charaenter

                mi "Okay~, now that we are done, we can relax a little! But not too much, we have lots more to do in the afternoon~!"

            $ renpy.music.play(music_ease, fadein=4.0, if_changed=True)

            show shizu behind_smile
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "It's actually not that much work, Hicchan~. So~, we can afford to enjoy a little lunch first."

            show misha cross_laugh
            with charachange

            mi "Hahaha~!"

            "The two of them produce a small array of plastic containers seemingly out of thin air."

            show misha hips_grin
            with charachange

            mi "Hm~ hm~… It's chicken cutlet with tomatoes and soybean sprouts~! Doesn't it sound delicious, Hicchan?"

            mi "It was just made this morning, and it's still warm, so eat eat eat~!"

            "I take one of the containers and open it. It looks nice, and certainly smells good. The fact that I'm really hungry adds to that even more."

            hi "Wow, this looks great. Where did you get this?"

            show shizu basic_normal
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "That isn't important, Hicchan!"

            show misha sign_smile
            with charachange

            mi "There was supposed to be a stall selling lunchboxes, but the girl who was to run it suddenly said she couldn't do it. Shicchan said, 'What a waste, it was a lot of work to trick Hicchan into making this~'—"

            hi "Hey, what the hell…"

            show misha hips_grin
            with charachange

            mi "…So~! Shicchan wanted to see if she could do it, but then decided not to, right, Shicchan~?"

            show shizu basic_angry
            with charachange

            "Shizune sulks angrily, shooting Misha a displeased look. I don't think I was supposed to hear that story."

            hi "This is your test food?"

            show shizu behind_frown
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "I'm eating it too, Hicchan~!"

            show misha hips_grin
            with charachange

            mi "And Shicchan is, too~!"

            "That doesn't answer the question!"

            "Nevertheless, I split a pair of chopsticks Shizune offers me, pick up a piece of cutlet, and pop it into my mouth."

            hi "It's surprisingly good. I didn't expect Shizune to be such a good cook."

            show shizu basic_frown
            with charachange

            "Shizune puts her chopsticks down to sign curtly towards Misha, who gulps down her cutlet with noticeable difficulty in order to speak for her."

            show misha sign_smile
            with charachange

            mi "Hicchan~! Don't talk with food in your mouth~!"

            hi "It's not like I enjoy doing it. Anyway, how motherly to show that kind of concern…"

            show shizu behind_frown
            with charachange

            shi "…"

            show misha hips_frown
            with charachange

            mi "You can't even eat right, Hicchan~! That's all it is~!"

            show misha perky_sad
            with charachange

            "It's a stalemate. I can't eat in order to talk to Shizune, who can't eat in order to chastise me for eating the wrong way. Misha, caught in between, is in the same situation, and looks the most disheartened by how this is going."

            show shizu behind_blank
            show misha perky_smile
            with charachange

            "Either way, our food is getting colder by the second, and it wasn't piping hot to start with. Wherever this was going, it dies down pretty fast once we all realize that, and we eat."

            play sound sfx_warningbell

            "After a while the bell rings, but Misha makes no attempt to tell Shizune, so I'm sure they're planning to skip classes and spend the rest of the day in here again."

            show shizu adjust_smug
            with charachange

            shi "…"

            show misha sign_smile
            with charachange

            mi "Hicchan, do you have any plans for the festival?"

            hi "No, not really. After all, I've only been here a week, what could I set up in that time?"

            show misha cross_laugh
            with charachange

            mi "Wahaha~! Hicchan, you helped us out so much, don't sell yourself short!"

            hi "Okay."

            show shizu basic_angry
            with charachange

            shi "…"

            show misha hips_frown
            with charachange

            mi "We're serious~!"

            hi "Okay!"

            "The two of them seem to get indignant over the strangest things."

            show shizu adjust_happy
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "You're going though, right, Hicchan? You should at least see what we've ac—complished…? Everyone should be able to look at what they have done so they can fully understand their work, that's my belief~! You're no exception!"

            show misha perky_smile
            with charachange

            mi "Hicchan, you should definitely go~! If you don't have anything planned, then maybe we can even go together~!"

            show shizu adjust_blush
            with charachange

            hi "Do you need a hand? If there's anything you need help with, I'm fine with sticking around."

            "I feel much more at ease than I did earlier; my previous concerns and fears long gone. I'd forgotten about this morning's trouble entirely until now, having fun with Shizune like this."

            "Having fun with Shizune… It seems like an unfamiliar concept to think of, but, looking back on it, I've really enjoyed the moments I've spent with Shizune and Misha these past few days, in spite of everything else."

            "If we might be going together, then maybe I can afford to stick around a little longer. And I guess it beats class."

            show shizu behind_blank
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "Really, Hicchan? Okay~! We can consider this you repaying us for the free lunch~!"

            show misha cross_laugh
            with charachange

            mi "Great, this is great, really~ really~ great~! Shicchan was hoping to bring this up again later anyway! Ahahaha~! Wahahahahaha~!"

            "That's not a free lunch at all. Normally I would be angry, or at least slightly unsettled, but my mood has improved from earlier on, so I'll let it slide."

            "Helping them out turns out to consist mostly of stamping forms and making what seems like ten thousand copies apiece of fifty different budget reports."

            "It's not hard, but very boring, and according to Misha, the simplest of the tasks they deal with."

            "I feel myself getting more and more tired, and with that, less eager to return to class. This is especially bad because the more time I spend out of class, the harder it seems to just get up and go back."

            "These two, they're a terrible influence. Terrible role models. Not that it bothers me all that much, and I'm sure no one looks up to them, but it's the principle of the thing…"

            show shizu adjust_happy
            with charachange

            shi "…"

            show misha hips_grin
            with charachange

            mi "Done~!"

            hi "Ah, that was fast. I'll be finished before this period's over, I think."

            show misha sign_smile
            with charachange

            mi "No, no, Hicchan, everything is done. So, you're done, too~!"

            hi "That doesn't make any sense, are you telling me this is all arbitrary and you've been keeping me here for the hell of it?"

            show misha hips_grin
            with charachange

            mi "No~…"

            show shizu basic_normal
            with charachange

            shi "…"

            show misha perky_smile
            with charachange

            mi "But we have kept you long enough~! You should go back to class, Hicchan~! You can still make it for most of this period!"

            hi "What about you?"

            show shizu behind_blank
            with charachange

            shi "…"

            show misha hips_smile
            with charachange

            mi "Of course we're coming too, of course; we'll be right behind you!"

            stop music fadeout 6.0

            scene bg school_hallway3
            with locationchange

            "Reassured, I start heading back to class, but the period is almost halfway over, so I start thinking it would be pointless halfway there and pass the difference between this class and the next drinking juice in the hallway."

            "I keep an eye on the door to the student council room, but it doesn't open. What's taking them so long? Are they busy wrapping up my share of the work? Well, it shouldn't take so long, unless there's more, and they just wanted me to leave."

            "The more I think about it, the likelier it seems."

            "Shizune is… well, not an idiot, but clearly, she's unable to just come out with things."

            "Maybe it's because she can't talk, so it's harder for her. She has Misha, but all in all, as easy as they make it look, there's still a difference between casual speech and sign language."

            play sound sfx_normalbell

            "I contemplate going back there to check on them, but the bell rings, and I have to go to class."

            scene bg school_scienceroom
            with locationchange

            "They join me a few minutes later, and the thoughts I had in my mind before slip away in the routine of school life."

            with shorttimeskip

            "By the time I remember, school is over for the day and I'm too tired to do anything but go home, do my homework, and then go to sleep."

            scene black
            with Dissolve(3.0)

            if _in_replay:
                return

    if not force_route:
        label .foot_and_mouth:
            scene bg school_hallway3
            show crowd

            play ambient sfx_crowd_indoors fadein 0.3

            if promised and go_for_it and not _in_replay:
                "Normally, I'd join the flow and grab a lunch myself, but today is different."

                "Today, I've been invited to lunch on the roof."

                "An odd location, but that's where I was told to go."

                "Fortunately, I manage to find shelter from the storm in the lee of the classroom door."

                stop ambient fadeout 1.0

                hide crowd
                with Dissolve(2.0)

                "Eventually the torrent subsides and I step tentatively out into the hallway."

                "Only to be met by Emi, who comes flouncing down the hallway like a cannonball."

                play music music_emi fadein 0.3

                show emi basic_happy at center
                with charaenter

                emi "Hey! Hi Hisao! Great timing!"

                show emi excited_proud
                with charachange

                emi "I have super extra lunch today, as promised! Let's go upstairs!"
            else:
                play music music_emi fadein 0.3

                show emi basic_happy at center
                with charaenter

                emi "Hisao!"

                show emi excited_proud
                with charachange

                emi "I'm going to make you a one-time-only, super extra special lunch offer!"

                show emi excited_laugh
                with charachange

                emi "Emi's home made lunch boxes, and the privilege of enjoying them in private with two bombshell beauties!"

                "Her overly flirtatious sales pitch echoes in the hallway, a remarkable feat since it's full of people."

                show emi basic_closedgrin
                with charachange

                "Emi strikes a very confident-looking pose as though as an attempt to one-up her own ridiculousness, puffing her very modest chest and making the V for victory sign with her hand."

                hi "Sounds delicious. To what do I owe this honor of being invited?"

                show emi excited_proud
                with charachange

                emi "You stood there looking really lost and sad so I thought you could use some company."

                "That is probably the most depressing reason imaginable."

                show emi basic_closedgrin
                with charachange

                emi "So how about it? You're probably really lonely and would eat that awful cafeteria food all alone, otherwise."

                hi "Eeeh…"

                show emi excited_proud
                with charachange

                emi "I'm kidding, I'm kidding!"

                hi "Sure, I'll have your lunch offer. With pleasure."

                show emi basic_happy
                with charachange

                emi "Let's go to the roof!"

                hi "The roof?"

                hi "Why the roof?"

                show emi basic_closedgrin
                with charachange

                emi "Because that's where we eat lunch!"

                emi "And if I don't get up there, then she'll probably wander off and then I just know she'll go hungry because she never packs a lunch for herself!"

                hi "Who will?"

                show emi basic_closedhappy
                with charachange

                emi "Come with me!"

                "Without answering my question or waiting for a response, she grabs me by the arm and drags me through the hallways."

                "I attempt to make conversation on the way."

                hi "Why do you have an extra lunch?"

                show emi sad_grin
                with charachange

                "Emi smiles guiltily."

                emi "Actually, it's yesterday's lunch."

                emi "I slipped in a run at lunch and forgot to eat it."

                "Huh."

                if wait_for_shizu and kick_shizu or _in_replay:
                    "Her expression is so funny that I almost laugh out loud."

                    "Emi giggles, to herself or to something or other, or maybe for no reason at all. I like the sound of it."

                    "Emi's sunny, energetic disposition alleviates the constricting feeling in the back of my head from the fight with Shizune and Misha."

                    "I let that issue slide out of my mind, and smile for the first time today."

            stop music fadeout 2.0
            stop ambient fadeout 1.0

            scene bg school_staircase1
            with locationchange

            "The stairway to the roof is a little dilapidated, but it's clearly been used recently."

            "At the top of the stairs is a door, complete with missing padlock."

            "I wonder who the intrepid individual was that removed the lock?"

            $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
            play ambient sfx_rooftop fadein 2.0

            scene bg school_roof at bgright
            show emi basic_closedgrin at center
            with Fade(0.5, 0.3, 1.0, color="#FFF")

            "Emi shoves the door open and steps beaming into the sunlight."

            show rin silhouette at offscreenright
            with None

            show bg at center
            show emi at left
            show rin at tworight
            with ease

            show emi basic_shock
            with vpunch

            "Suddenly, a tall dark stranger appears out of nowhere, standing imposingly in front of us. Emi flinches back, almost falling back down the stairs."

            call screen doublespeak(emi, _("Eeek!"), rin_, _("Hello."))

            show emi basic_hes
            with charachange

            show emi at twoleft
            with charamove

            emi "Yipes! You scared me, Rin!"

            "Wait, isn't she…"

            show rin relaxed_surprised
            with charachange

            play music music_rin fadein 2.0

            rin "Hello."

            "Noticing that Rin is speaking to me, Emi looks curiously at me."

            show emi basic_confused
            with charachange

            emi "You two know each other?"

            "I look confusedly at Emi."

            hi "She's that friend of yours?"

            show rin relaxed_nonchalant
            with charachange

            "Rin has turned her gaze towards the clouds drifting above the school."

            rin "I didn't know you knew this person, Emi."

            stop music fadeout 2.0

            "…"

            "The awkward silence lasts only for a few seconds until Emi lets out a tiny giggle, shrugging the coincidence off."

            show emi basic_closedgrin
            with charachange

            emi "I invited Hisao for lunch. If you know him, that's just better."

            show rin basic_deadpan
            with charachange

            rin "Oh. Does this mean I don't get food? Or did you invite him for lunch without the lunch?"

            show emi basic_grin
            with charachange

            emi "Erm, neither, I have food for three."

            show rin basic_deadpanamused
            with charachange

            rin "Nice thinking."

            hide rin
            hide emi
            with charaexit

            "They walk to the other end of the roof while I stay at the clock tower for a while, taking in the atmosphere."

            play music music_soothing fadein 0.5

            "There is nobody else but us here. I guess the roof is not as popular as it is in other schools."

            "A few rundown benches and tables are scattered around the edges, perhaps in an attempt to make the rooftop look less desolate."

            "The small pebbles covering the roof rattle beneath our feet."

            "I peek through the chain link fence to take a look at the school grounds and beyond."

            "Students are strolling in pairs and groups around the quadrangle and at the cafeteria."

            "A few delivery trucks are driving past the school towards the convenience store nearby."

            "Somewhere a watchdog barks at a passer-by."

            "Somehow, when I look towards the town center the small town feel strikes me very strongly, almost palpably."

            "The hectic lifestyle of big metropolises seems so far away and foreign here; nobody has to run to catch a bus like their life depended on it or get their senses overloaded by the neon lights and traffic jams."

            "I feel surprisingly optimistic about this new life of mine, looking at my new hometown, even if it's going to be mine for only one short year."

            "Finding out about my illness and having to move away from home all came so suddenly I haven't had time to think how I feel about it."

            "When I step out of the shadow of the clock tower to the open I feel warmth touching my back."

            "The sun shines from a perfectly clear cerulean sky."

            "A cool breeze sweeping over the rooftop makes me shiver, but only briefly."

            "The wind carries the scent of trees and flowers, not smog and car exhaust like it used to, just a few weeks ago."

            "Emi settles on a bench with Rin in tow and produces one big and two small lunch boxes from her bag."

            show rin basic_deadpannormal at tworight
            show emi basic_happy at twoleft
            with charaenter

            emi "Come on, Hisao! What are you waiting for?"

            "She is beckoning me to join them, making room on the already small bench."

            show emi at offscreenleft
            show rin at offscreenleft
            show bg at bgleft
            with charamovefaster

            show emi basic_happy_close at closeleft
            show rin basic_deadpannormal_close at closeright
            show bg at center
            with charamove

            "I seat myself on the corner of the bench to take as little space as possible. It's pretty cramped, but somehow all three of us fit on it."

            hi "Impressive view."

            show emi basic_closedhappy_close
            with charachange

            "Emi suppresses a giggle and places a lunchbox in front of Rin, and hands another lunchbox to me."

            show emi excited_proud_close
            with charachange

            emi "Here you go! Lunch, as promised!"

            "Homemade, no less. I'm impressed."

            hi "Wow. This looks really good."

            show emi excited_amused_close
            with charachange

            emi "Thanks! I make 'em myself when I can."

            "Conversation dies off as I set about the business of feeding myself."

            show rin basic_awayabsent_close
            with charachange

            "Taking a few bites, I glance up and notice Rin deftly opening the lunch box and popping a forkful of food into her mouth using only her feet."

            "Even though I've seen it before, I can't help but be impressed at her dexterity."

            "It's also a reminder of the sort of place I am in right now."

            "Will I ever get used to sights such as this?"

            "I can't decide if getting used to such a thing would be a good thing or a bad thing either."

            "Does getting used to this place mean that I'm giving up on being a normal person?"

            "Or does it just mean that I'm becoming more understanding about those around me?"

            "I'm distracted from my thoughts by the sight of Emi tearing into her lunch as if it had insulted her ancestors."

            show rin basic_absent_close
            with charachange

            hi "You seem pretty hungry."

            show emi basic_grin_close
            with charachange

            "Emi looks up, mouth half full, and swallows before nodding."

            emi "My morning run always works up an appetite."

            show emi basic_closedhappy_close
            with charachange

            emi "Which is great, because then I burn through lunch pretty quickly."

            show emi excited_proud_close
            with charachange

            emi "Helps me keep my girlish figure."

            show rin basic_deadpan_close
            with charachange

            rin "What would happen if you'd lose it? Would you become a man?"

            "I very nearly choke on my lunch trying not to laugh."

            show emi basic_annoyed_close
            with charachange

            emi "It's a figure of speech."

            show rin basic_deadpandelight_close
            with charachange

            rin "Does your figure have to run in the mornings too?"

            hi "Do you always talk like this?"

            show rin relaxed_surprised_close
            show emi basic_confused_close
            with charachange

            call screen doublespeak(emi, _("Talk like what?"), rin, _("Like what?"))

            "I think that answers my question."

            hi "Er, never mind."

            hi "So, uh…"

            "I struggle to think of small talk and settle on the obvious question."

            hi "How'd you two meet?"

            show rin basic_awayabsent_close
            with charachange

            "Rin seems content to let Emi answer this question."

            show emi basic_grin_close
            with charachange

            emi "Someone in the housing department thought that we'd complement each other well, so we were assigned rooms next to one another."

            hi "Complement each other?"

            show rin basic_deadpannormal_close
            with charachange

            rin "Like shoes and a suit."

            hi "Huh?"

            show emi basic_closedgrin_close
            with charachange

            "Emi giggles at my confusion."

            emi "Put us together and we've got all our limbs, get it?"

            hi "Ah."

            show emi basic_happy_close
            with charachange

            emi "So I started helping Rin get ready in the mornings, and that was that!"

            show emi basic_grin_close
            with charachange

            emi "I mean, you can't help someone get dressed every morning and not get along."

            hi "I see."

            "Rin chooses this moment to interject."

            show rin basic_deadpan_close
            with charachange

            rin "I have trouble with shirts."

            hi "Right, that seems… fairly obvious."

            show rin basic_surprised_close
            with charachange

            rin "Really?"

            hi "Kind of…?"

            "This isn't helping, but at least Emi seems to find the whole thing funny."

            "That, combined with the fact that Rin is genuinely curious, makes me feel slightly better and yet, confused."

            hi "I mean, you've got no arms."

            hi "So uh, putting on a shirt seems like one of those things that would be… difficult."

            "You know what? I'm going to just stop talking now."

            "It'll save me a lot of trouble in the long run."

            "Rin nods in what I suspect is meant to be a sage manner."

            show rin basic_lucid_close
            with charachange

            rin "I see."

            show rin basic_absent_close
            with charachange

            "The conversation dies as I turn my attention back to my lunch."

            "It's really quite good."

            "Emi finishes her lunch first and makes a contented noise."

            show emi excited_laugh_close
            with charachange

            emi "Ah, that was good."

            "As she busies herself with cleaning up her lunch, Rin speaks up."

            show rin basic_deadpan_close
            with charachange

            rin "I'm thirsty."

            show emi basic_shock_close
            with charachange

            emi "Oh! I almost forgot about that! Sorry!"

            show emi basic_closedgrin_close
            with charachange

            "With a flourish, she reaches into her bag and removes a trio of juiceboxes."

            "She tosses me one that appears to be cranberry juice, one to Rin that appears to be some kind of strawberry milk (complete with pink color scheme), and keeps an (equally pink) box of some kind of fruit punch for herself."

            show rin basic_awayabsent_close
            with charachange

            "Rin dexterously stabs her straw through the top of her box and begins to drink."

            "I'm once again impressed by how flexible she is, but this time I keep my comment to myself."

            "Somehow I don't think either Emi or Rin are the sorts of people to think twice about the way they work around their particular disabilities."

            "Rin especially so."

            "Indeed, she gives off the impression of being entirely unaware that she's missing any limbs at all."

            "Whether or not that's a conscious decision is another matter."

            "I'm honestly not sure."

            show emi basic_grin_close
            with charachange

            emi "So Hisao, how do you like it up here?"

            show rin basic_absent_close
            with charachange

            hi "Hmm?"

            hi "It's quite nice, actually. I like high places, for the view."

            hi "Thanks for inviting me up here."

            hi "And for the lunch, too."

            show emi excited_amused_close
            with charachange

            "Emi grins a thousand-watt grin, pleased by my response I suppose."

            emi "No problem!"

            show emi excited_proud_close
            with charachange

            emi "Feel free to eat with us next time too, okay?"

            emi "I won't make you a lunch, but you can bring your own up here."

            hi "No lunch service? I don't know…"

            show emi basic_annoyed_close
            with charachange

            "Emi looks mock offended."

            emi "Trying to take advantage of my good nature?"

            emi "The nerve!"

            show emi basic_closedgrin_close
            with charachange

            "She giggles."

            show emi sad_depressed_close
            with charachange

            emi "Well, if that's your answer, I guess Rin and I will just keep eating lunch all alone…"

            "I am suddenly assaulted by the most heart-rending puppy-dog eyes I've ever seen as Emi pouts."

            hi "Kidding! I was kidding!"

            hi "I'd love to eat lunch up here again."

            hi "Good location, and the company's okay too."

            show emi basic_grin_close
            with charachange

            "Emi frowns a bit at my declaration of 'okay' but seems happy enough that I've accepted her invitation."

            "I guess this makes us friends now."

            "Or at least acquaintances."

            play sound sfx_warningbell

            "The lunch bell rings, signaling a return downstairs."

            show emi basic_hes_close
            with charachange

            emi "Rin, you didn't finish your lunch again!"

            show rin basic_deadpan_close
            with charachange

            rin "I wasn't that hungry."

            show emi basic_annoyed_close
            with charachange

            emi "If you don't eat more, you're going to fade away!"

            show rin relaxed_boredom_close
            with charachange

            "Rin shrugs, as if this is an acceptable risk."

            stop music fadeout 4.0

            hi "Come on, we'd better get going."

            stop ambient fadeout 2.0

            scene bg school_staircase1
            with locationchange

            "The three of us head down the stairs together."

            scene bg school_scienceroom
            with shorttimeskip

            "The afternoon class passes. Once again, I find myself without a plan for something to do after school, so I head to the library to return a couple of the books I finished reading."

            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")

            scene bg school_library
            with locationskip

            "Walking inside, I see that there are about as many students here as there were on Tuesday, all the more evident from the almost total silence enveloping the room."

            play sound sfx_impact2
            with vpunch

            show yuuko panic_up at offscreenbottom
            with None

            show yuuko at center
            with charamovefaster

            play music music_happiness fadein 2.0

            "As I drop the books I'd borrowed into the returns slot in the counter, Yuuko suddenly pops up from behind it, quite startled from the banging they make as they hit the trolley next to her."

            hi "Ah, sorry Yuuko. Didn't mean to startle you."

            show yuuko worried_up
            with charachange

            yu "No, no. That's fine. It happens… a lot. I'm used to it by now."

            show yuuko neurotic_up
            with charachange

            yu "Um, can I help you?"

            hi "It's okay, I think I know where everything is. Thanks anyway."

            hide yuuko
            with charaexit

            "I suppose I'll grab another book or two while I'm here. There's not much else to do, and after reading so much during my stay in the hospital, it's become a hard habit to break."

            stop music fadeout 5.0

            "I wander down to the fiction section towards the back of the library, scanning the bookshelves for anything that catches my eye."

            "As I do, I look over to the corner where Hanako had been the last time I was here, not really expecting anything to come of it."

            scene ev hana_library_read_std
            with locationskip

            "…surprisingly, though, she's there, absorbed completely in a fairly thick book. I decide against intruding on her like last time and get back to finding reading material."

            scene bg school_library_ss
            with shorttimeskip

            play music music_tranquil fadein 6.0

            "After an indiscernible amount of time spent perusing the aisles, I finally decide on a couple of books to get and slide them off the shelf."

            "With a minimum of fuss, I quickly walk over to the counter, check out my books and pop them into my bag as I walk out."

            scene bg school_courtyard_ss
            with locationskip

            "By the time I leave the main building, sunset isn't too far away. A small trickle of students remain, but the majority have left; presumably to their homes and dorms."

            if promised and go_for_it or _in_replay:
                scene bg school_dormhisao_ss
                with locationskip

                "Feeling utterly drained, I head to my room to read the books I borrowed. There's been enough action and excitement for one day already."

                "The first is 'Alice's Adventures in Wonderland'. I know the story, of course, but I've never actually read the original book."

                "It's just as trippy as I remember the story to be, with the wacky characters and nonsense plot."

                "I start thinking of myself as some kind of an Alice too, haplessly tumbling down the rabbit hole into this Cripple Wonderland."

                "…Okay, that's a rather strong expression. Still, the isolated location and the overt way the school accommodates to absolutely everything is unsettling. It is like another world."

                "I wonder why I can't shake the feeling of being an outsider like Alice, despite most everyone being so hospitable and friendly with me."

                "Turning another page, my mind starts drifting further away from the book. It's quiet, I can hear my heartbeat thumping against the fabric of my shirt."

                "For some reason, it makes me feel really bad like it has since that time in the forest with Iwanako. Like I was locked in a cage with something nasty and scary."

                stop music fadeout 5.0

                scene bg school_dormhisao_ni
                with Dissolve(3.0)

                "I put the book down for a while and stare at the ceiling, taking my time to shake off the feeling."

                "200 pages later, I fall asleep."

                scene black
                with shuteye

            if _in_replay:
                return

    if not force_route and not (promised and go_for_it):
        label .mind_your_step:
            scene bg school_courtyard_ss

            $ renpy.music.play(music_tranquil, fadein=3.0, if_changed=True)

            "I guess I need to buy some supplies. I can't live off cafeteria food and eating out for my entire stay here."

            scene bg school_gate_ss
            with locationchange

            "As I leave for the gate, I make a few loud stretches to try and stave off the tiredness that's accumulated over the week."

            scene bg school_road_ss
            show lilly back_smileclosed_ss at center
            show lillyprop back_cane_ss at center
            with locationchange

            "After passing through and rounding the corner, though, I see a solitary figure walking downhill towards the small town below. The color of her hair and tapping of her cane are unmistakable."

            show lilly cane_surprised_ss
            hide lillyprop
            with charachange

            "I quickly walk up to her, which seems to catch her attention without a word needing to be said."

            hi "Hi, Lilly."

            show lilly cane_weaksmile_ss
            with charachange

            "She takes a moment to place the voice, slightly adjusting her head to face a bit more towards the source of my voice as she does."

            show lilly cane_smile_ss
            with charachange

            li "…Hisao?"

            hi "Yep, that's me."

            "She seems to have a good memory for voices. The fact that she actually remembered is a pleasant surprise."

            li "Good evening. What brings you here?"

            show lilly cane_weaksmile_ss
            with charachange

            "Once again, she gives a small polite bow. And, once again, I reply in kind before realizing that I needn't do so."

            hi "Just going into town. You?"

            show lilly cane_ara_ss
            with charachange

            li "My my, what a coincidence."

            hi "Doing the same thing, eh?"

            show lilly cane_smile_ss
            with charachange

            li "Mm. I usually go shopping on Fridays."

            show lilly cane_surprised_ss
            with charachange

            "She pauses for a moment, suddenly looking a little lost."

            li "That said, Hanako usually comes into town with me…"

            "Ah. Not lost, but worried. The two do seem to keep pretty close tabs on one another. It's kind of surprising that Hanako would just forget Lilly like that."

            hi "I noticed her reading in the library. She probably just got caught up in a book."

            show lilly cane_weaksmile_ss
            with charachange

            "She lets out a small sigh of relief."

            li "Thank you. She has a habit of doing that."

            hi "Avid reader?"

            show lilly cane_smile_ss
            with charachange

            li "Right. She doesn't like being around crowds of people, so reading away from everyone lets her relax a bit."

            "Although she probably didn't intend it, I can't help but grimace as I recall my first meeting with her."

            show lilly cane_smileclosed_ss
            with charachange

            "Hardly wanting to bring it up, I remain silent as we quietly continue to walk down the quiet road."

            "Tack, tack. Tack, tack."

            "With the road bereft of cars and the students of Yamaku increasingly far behind us, the quiet rustling of the leaves and the measured tapping of Lilly's cane against the sidewalk are all that can be heard."

            "It's kind of nice, especially compared to the hustle and bustle of where I used to live."

            "Before I know it, I've relaxed so much that a loud yawn escapes before I can control it."

            show lilly cane_giggle_ss
            with charachange

            li "Tired?"

            hi "Yeah, been running ragged these past few days."

            "That's an understatement, to be sure. Transferring into a different school would be bad enough, but nothing like this…"

            show lilly cane_smile_ss
            with charachange

            li "Well, hopefully everything should settle down for you. The festival's got everyone in a spin right now, and you've been plopped right in the middle of things."

            "For a moment I hesitate, but given her apparent tolerance for frankness I decide to give my full thoughts."

            hi "I guess. Yamaku's kind of different though. I mean, the formality surrounding everything, the isolation around it… not to mention the most obvious difference."

            hi "It's kind of a whole different mindset. I suppose I'll get used to it though, in time."

            show lilly cane_smileclosed_ss
            with charachange

            "She gives a matter-of-fact nod, apparently pleased with my answer. It feels almost as if she's included me in the flock of students she's shepherding, along with class 3-2 and Hanako."

            "Well, not that I mind. It's nice to get the thoughts off my chest in any case."

            show lilly cane_smile_ss
            with charachange

            li "Looking on the bright side, one could see it as a chance for a new beginning. You should cherish the ability to make new friends."

            "That's optimistic. Nonetheless, it's good to have a positive attitude about such things, I suppose."

            hi "I guess that's a good take on it."

            scene bg suburb_roadcenter_ss
            show lilly cane_reminisce_ss at center
            with shorttimeskip

            stop music fadeout 6.0

            "Walking on down the road, she seems to become somewhat unsettled. Before I can ask what's on her mind, she seems to collect herself and speaks up about something else."

            show lilly cane_weaksmile_ss
            with charachange

            li "So, where in town were you going?"

            "That's actually a pretty good question. I'd come in to buy food, but the layout of the place is still totally foreign to me."

            "I had intended to just wander around and see what I could find, but with sunset already approaching and nightfall not too far away, that doesn't seem very wise."

            "I'm going to have to ask her for directions. Again."

            hi "I was just going to get some food… but now that you mention it, I don't really know the way."

            show lilly cane_planned_ss
            with charachange

            li "Well now, this is quite lucky. I was just about to go to the convenience store myself."

            hi "Looks like I'll be in your care again, then. Thanks."

            "Together we walk to the store, my paces carefully slowed to remain beside her. Compared to my usual walking pace, hers is quite a bit slower. Not that it's without reason."

            scene bg suburb_konbiniext_ss
            with shorttimeskip

            play music music_daily fadein 2.0

            "After what couldn't be more than several minutes, I catch sight of our objective. This town really is pretty small."

            scene bg suburb_konbiniint
            with locationchange

            "Without further ado, we make our way inside with a greeting from the counter."

            show lilly cane_weaksmile at center
            with charaenter

            li "Mind if I tag along with you? Usually Hanako would help me, but seeing as she's not here…"

            "It takes a moment before I realize what she means."

            "Considering she wouldn't be able to read any of the labels, shopping without any help would be a big pain for her."

            "That said, I can't shake the feeling that she'd had this idea since I said I was coming here."

            hi "Sure. It'd be my pleasure."

            "I grab two well-used red baskets from the small stack beside the entrance, handing one to Lilly."

            show lilly cane_weaksmile:
                ypos 1.0 yanchor 0.0
            with charamove

            show lilly basic_smileclosed
            with charachange

            show lilly at center
            with charamove

            "She lays it on the ground, putting her schoolbag in, retracting her cane and sliding it through the basket's handles before picking it back up in her right hand."

            "Wait, if she doesn't use her cane…"

            show lilly basic_smileclosed_close at twoleft
            with charamovechangefaster

            "Before I can complete the thought, she comes beside me and pinches the cuff of my uniform in her slender fingers."

            show lilly basic_concerned_close at twoleft
            with characlose

            li "Is this all right?"

            hi "Ah, sure."

            show lilly basic_smileclosed_close
            with characlose

            "I have no reason not to accept. I can think of worse things than shopping with a pretty girl holding onto me, even if it is out of necessity."

            "We navigate our way through the store, with not one of the occasional passing customers seeming to bat an eyelid."

            "Considering how close Yamaku is, I guess seeing students from there must be entirely normal for the local residents."

            "As we reach each aisle, I quickly check with Lilly and find out what she needs. I grab it along with what I'm looking for, and put our items into their respective baskets."

            "I guess this is the same routine she and Hanako follow every Friday."

            hi "Right, all that's left is the bread and that should be my shopping done. Do you need anything else, Lilly?"

            show lilly basic_smile_close
            with characlose

            li "No, this should be everything."

            hi "Off we go, then."

            show lilly basic_smileclosed_close
            with characlose

            "With a quick side trip to the bakery section, we make our way to the registers."

            "The line, thankfully, is almost nonexistent. It's not long before we've both paid for our food and are out the door."

            scene bg misc_sky_ni:
                xalign 0.0
                warp acdc_warp 15.0 xalign 1.0
            with locationchange

            "As Lilly retrieves her cane and extends it to full length, I waste a minute looking upwards at the night sky while holding both our bags."

            "For a moment I try to make clouds with my breath, but the summer's heat doesn't seem to cooperate."

            "Eventually she rights herself, taking a quick stretch before taking her bag and leaving me to my two."

            scene bg suburb_konbiniext_ni
            show lilly cane_listen_ni at center
            with locationchange

            hi "You tired as well?"

            show lilly cane_sleepy_ni
            with charachange

            li "The festival preparations have been complete chaos. Shizune breathing down my neck doesn't exactly help things, either."

            hi "Hey, she's only trying to get everything organized. Better now than later, right?"

            show lilly cane_weaksmile_ni
            with charachange

            li "I suppose. I'm going to enjoy relaxing in town tomorrow, that's for certain."

            "I guess the festival preparations must be taking their toll on both of them."

            scene bg suburb_roadcenter_ni at bgright
            with locationchange

            "We walk out into the quiet street, talking between ourselves as we carry our bags of food and supplies from the store."

            "…Wait, what's that?"

            "I notice a very distinctive figure making its way towards us, silhouetted by the streetlamps."

            "For a second I think it's another male student from my class, but as he, or should I say she, gets closer I recognize her quickly."

            show rin relaxed_nonchalant_ni at offscreenright
            with None

            show bg at center
            show rin at right
            with charamove

            stop music fadeout 8.0

            hi "Rin? What're you doing out here so late?"

            show lilly cane_surprised_ni at center
            with charaenter

            li "Rin?"

            "Lilly perks her head, looking like she's trying to focus on listening more keenly. It suddenly comes to me that I should probably interpret the scene for her."

            hi "It's Rin… Tezuka, I think was her last name, from our school."

            show lilly cane_weaksmile_ni
            with charachange

            "She stiffens at the name and gives a complicated-looking expression, something like a forced fusion of a composed smile and a painful cringe."

            li "Ah. I understand."

            "I guess Lilly knows Rin too."

            show rin basic_awayabsent_ni
            with charachange

            show bg at bgleft
            show rin at tworight
            show lilly at twoleft
            with charamove

            "Rin turns to look at us, looking terribly out of it. I'm not entirely sure if she recognizes either of us or at least she doesn't acknowledge it if she does."

            "She looks like a zombie. Or a statue. A statue of a zombie."

            "But slowly, some symptoms of understanding seem to light in her dark eyes: this is something she must react to."

            show rin basic_lucid_ni
            with charachangealways

            show rin basic_awayabsent_ni
            with charachangealways

            "Rin blinks once. Very thoroughly."

            show rin basic_absent_ni
            with charachange

            rin "Hello."

            "…"

            "There is an awkward pause, everyone waiting for someone else to say something."

            hi "What are you doing here this late?"

            "…"

            rin "I…"

            show rin basic_deadpan_ni
            with charachange

            rin "I was wondering about that myself too. Just now."

            play music music_rin fadein 0.5

            show rin basic_deadpannormal_ni
            with charachange

            rin "Some people asked that just before. I assume they were wondering the same."

            rin "I didn't know. They didn't know either. I asked. That's why I'm wondering."

            rin "So that was pretty much it. It's a murder mystery without a murder."

            "…"

            show rin negative_spaciness_ni
            with charachange

            rin "They were going that way."

            show rin basic_absent_ni
            with charachange

            "She turns facing to her right in order to demonstrate the direction the other people went to as if that was important, then rotates back like a mechanical puppet in one of those overly complicated clockworks."

            "For a person who gives an impression of being the quiet type, Rin really does use a lot of words to say things that don't need a lot to be said."

            "Unsure if she's finished, I say nothing. Neither does Lilly, who seems equally robbed of words for the time being."

            "I think that both of us are in fact just scared that any response might provoke her to continue."

            "Our stupefied lack of reaction doesn't faze Rin at all. She keeps looking at us expectantly, a calm hint of expression on her blank face."

            "She seems to be that kind of person. Always so relaxed."

            "As if bull elephant-grade sedatives were flowing in her veins in the place of blood."

            show lilly cane_concerned_ni
            with charachange

            li "Do you have amnesia? I don't recall you having anything of the sort, though…"

            hi "No, I don't think it's that."

            hi "The other passersby were probably just worried, though. You do look really lost, the way you're standing in the middle of the street."

            show rin basic_deadpan_ni
            with charachange

            rin "Oh, I see."

            show rin relaxed_nonchalant_ni
            with charachange

            rin "Maybe I should've taken some other kind of pose in that case."

            "I ponder for a while whether I should chase this angle further, or give up for the sake of my own sanity."

            "I decide on the latter."

            "It seems that most of the time, it's better to not read too deeply into what Rin is babbling about."

            "Talking with Rin is like playing chess with a supercomputer who does seemingly completely random moves as if to mock everything you know about chess. It's like that, except with human interaction."

            "And even if I win, it feels like losing."

            "Damn, it's just like Kenji said. Even when I win, I lose. Is this the power of the girls of Yamaku?"

            "…"

            "I push the thought aside as too dangerous to consider further. It's probably just Kenji's anti-female propaganda getting to me during a moment of weakness."

            hi "Yeah, maybe taking another pose might have worked."

            hi "So anyway, you have no idea what you're doing here?"

            show rin negative_annoyed_ni
            with charachange

            "She frowns, looking extremely displeased at either my question, its consequences, or the answer she's about to give."

            rin "I do have. Some idea. I can't really tell what kind of an idea."

            show lilly cane_smile_ni
            with charachange

            li "That sounds like progress, at least."

            "Lilly sounds as if she's spotted an opening for some kind of discernibly normal conversation. I can't say I share her optimism."

            rin "Yes, there is some. Definitely. The rest will come later."

            show rin basic_deadpanupset_ni
            show lilly cane_weaksmile_ni
            with charachange

            rin "I'm sure of it. I always have… reasons."

            "The ensuing silence kills Lilly's hopes all too visibly. That didn't last long."

            "Rin's, as far as I can tell unbased, assurances aside… what should be done?"

            "We could just leave her to her own devices, whatever those are… but it's late and I don't think we'll be getting any thanks if Rin is found standing here in the middle of the night."

            "Which she probably will, unless she manages to remember what she was doing here in the first place."

            "As for me trying to guess what might've been going on in her mind when she decided to embark on this adventure, the chances seem to be on par with winning the lottery."

            "Several times in a row."

            "Lilly is oddly quiet too. I'd appreciate some support from the sidelines here, especially if she's more familiar with Rin than I am."

            "But it can't be helped. It seems her familiarity with Rin is exactly why she's staying subdued."

            hi "So, I assume you were going somewhere, not coming back to the school… any idea where?"

            show rin relaxed_surprised_ni
            show lilly cane_surprised_ni
            with charachange

            "Her eyes widen in shock and she jolts back in a somewhat artificial way, making it seem like an act rehearsed for situations like this."

            rin "Are you a mind reader? Is that your disability? How unique!"

            hi "No… What? Why would you think that?"

            show rin relaxed_disgust_ni
            show lilly cane_listen_ni
            with charachange

            rin "You knew what I was doing."

            show lilly cane_displeased_ni
            with charachange

            hi "Eh, it was just an educated guess. We walked this same street in the other direction just before, to get to the store."

            hi "If you were going to school, we would've met you on the way."

            show rin basic_deadpanupset_ni
            with charachange

            rin "Oh."

            "She looks a little disappointed."

            "Like Kenji, Rin appears quick to jump to completely irrational conclusions."

            "Maybe it's something in the water here. I make a mental note to stock up on soft drinks."

            hi "You know, that is the second time this week that someone asked if I was a mind reader."

            hi "Do I really give off that impression?"

            show rin basic_deadpannormal_ni
            with charachange

            "Rin shrugs her shoulders, which is all the answer I get."

            hi "You know—{w=0.3}{nw}"

            show lilly cane_smile_ni
            with charachange

            li "Maybe you should come with us back to the school?"

            "Lilly interjects just as I am about to further debunk my alleged mind-reading capabilities. She sounds rather concerned, the paper-thin smile on her face badly disguising that fact."

            "Maybe she came to the same conclusion as I did. For everyone's sake, I decide to let the mind-reading topic drop, as it's entirely inane anyway."

            hi "Yeah, Lilly's right. If you can't remember, there's no point staying here."

            show rin basic_awayabsent_ni
            with charachange

            "Rin considers this rather simple deduction for a moment, then nods."

            show rin basic_absent_ni
            with charachange

            stop music fadeout 2.0

            rin "Okay."

            scene bg school_road_ni
            with shorttimeskip

            $ renpy.music.set_volume(0.1, 0.0, channel="ambient")
            play ambient sfx_cicadas
            play music music_dreamy fadein 2.0

            "We start towards the school again, having wasted way more time than necessary with this episode."

            show rin basic_awayabsent_ni at tworight
            show lilly cane_smileclosed_ni at twoleft
            with charaenter

            "Rin walks along the edge of the sidewalk in her arrhythmic way, looking like a mix of sleepwalker and rope dancer, while Lilly keeps one hand on my shoulder, tapping at the ground with her cane."

            "Tap step step tap tap step step step."

            "Apart from that and a few fragmented beginnings of conversation, it's quiet. A quiet quite apart from the relaxing one into town, at that."

            hi "So how's the mural going?"

            show rin basic_deadpan_ni
            with charachange

            rin "We are going to get bad luck. Never talk about works in progress."

            show lilly cane_weaksmile_ni
            with charachange

            li "I'm sure it'll be wonderful."

            show rin basic_deadpannormal_ni
            with charachange

            rin "Bad luck."

            "Tap step tap step. She doesn't care to talk about it. Lilly's politeness feels out of place, for the first time. Step step step."

            "The hill Yamaku rests on top of is surprisingly steep, going uphill. We slow the pace, but I still feel my pulse rising and breathing getting heavier."

            "Almost there, I can see the gates already."

            "More than that, though, I notice that Lilly's hand slightly tightens on my shoulder. Interpreting it as a gesture that she wants to ask something, I speak up."

            hi "Anything wrong, Lilly?"

            "I resist the urge to say 'Aside from our traveling companion?' But only just."

            "For a moment she seems to debate whether she should even bring it up, but goes for it anyway."

            show lilly cane_concerned_ni
            with charachange

            li "Is everything… all right?"

            hi "All right? How do you mean?"

            "The fact I can't interpret her incredibly vague question puts her off, for a second."

            li "It's just… you seem unusually tired, I guess."

            "Now that she brings it up, I notice that my breathing is strangely heavy. The uphill walk has really done a job on me."

            menu:
                with menueffect
                "Lilly noticed it all too quickly…"

                "Sorry, I'm not in very good condition.":
                    $ no_much_talking = False

                    call a1c13o1

                "I don't really want to talk about it.":
                    $ no_much_talking = True
                    $ get_kenji = True

                    call a1c13o2

            if _in_replay:
                return

    return

label class_goes_lazily:
    scene bg school_scienceroom
    with shorttimeskip

    play music music_normal fadein 3.0

    "The class goes on lazily. I think I'm starting to get into the rhythm of the school."

    "I have even stopped worrying about taking notes and being overtly attentive. The first days, I was pretty high-strung in class."

    "Mutou finishes his lecture about electricity early, but continues without a pause about the festival."

    show muto normal at center
    with charaenter

    mu "So, as you know, the festival is on the day after tomorrow. I hope everyone's projects are going to be successful this year."

    show muto smile
    with charachange

    mu "Have a good time, but also come Sunday, please keep the meaning of this festival in your minds…"

    mi "Games and fried food!"

    "Everyone bursts out in laughter, and so do I."

    show muto irritated
    with charachange

    mu "Yes, thank you Mikado."

    show muto normal
    with charachange

    mu "But what I meant was more the—{w=.5}{nw}"

    play sound sfx_normalbell

    "The remainder of his sentence is buried beneath the ring of the lunch bells, and everyone starts packing their things."

    "Mutou deliberates for a moment, but since almost nobody seems to pay attention any more, he gives up and sits down."

    stop music fadeout 2.0

    scene bg school_hallway3
    show crowd
    with locationchange

    play ambient sfx_crowd_indoors fadein 0.3

    "It's crowded in the hallway… or as crowded as hallways in this school probably get. Most of the students seem to be heading down for the cafeteria."

    return

label mas_doesnt_bother:
    scene bg school_scienceroom
    with shorttimeskip

    stop music fadeout 2.0

    "Misha, and by proxy, Shizune, doesn't bother me for the entire morning."

    play sound sfx_normalbell

    "When the bell rings, I don't even look at the two of them as I walk out of the class."

    scene bg school_hallway3
    show crowd
    with locationchange

    play ambient sfx_crowd_indoors fadein 0.3

    "It's crowded in the hallway… or as crowded as hallways in this school probably get. Most of the students seem to be heading down for the cafeteria."

    return

label a1c9o1:
    "What am I doing here?"

    "Am I really just going to fold and let Emi pull ahead?"

    scene bg school_track_running
    with locationchange

    "I speed up."

    "The second lap's done quickly, and without even considering it I keep going."

    "Emi looks back over her shoulder at me and grins."

    show emi excited_proud_gym at twoleft
    with charaenter

    emi "Still going?"

    hi "Wouldn't *pant* want you *pant* to think I'm outta shape *pant*"

    show emi excited_laugh_gym
    with charachange

    show emi at offscreenleft
    with charamovefaster

    hide emi

    play ambient sfx_emipacing

    "Emi laughs - without breaking her stride, no less - and speeds up even more."

    "Well, if this is the way we're going to play things…"

    "I increase my own pace as well."

    "I can feel my lungs burning, and my legs are starting to question just what the hell I think I'm doing."

    "Lactic acid screams in my muscles, but I close my ears."

    "I can't let myself fall behind, because that would be a loss."

    "The rational voice in my head inquires mildly just when we started playing a game."

    "I'd answer it, but I'm having a lot of trouble thinking at present."

    "She's so {b}fast{/b}."

    "How the hell does she keep it—{w=.5}{nw}"

    stop music fadeout 0.2

    play sound sfx_heartfast
    show heartattack alpha
    with Dissolve (0.1)

    hide heartattack alpha
    with Dissolve (0.2)

    "It's like a string pulling at my chest, a choking feeling of narrowness and pain."

    "Before I can think of anything else than 'Oh shit,' the track disappears from under my feet."

    scene bg school_track_on:
        xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
        linear 0.1 rotate -6 zoom 1.2
    with vpunch

    "I stumble, one hand shooting down to clutch at my chest, the other hitting the track to keep me from falling on my face."

    stop ambient fadeout 0.2

    "Emi whirls around and her eyes widen."

    emi "Hisao!"

    play ambient sfx_emisprinting

    "She yells at me, sprinting from the other side of the track."

    show emi basic_shock_gym:
        offscreenright
        rotate -6 zoom 1.2
    with None

    show emi:
        xalign 0.5 yalign 0.7
    with charamovefaster

    stop ambient fadeout 0.1

    emi "What's wrong?"

    hi "Nngh—Nothing, just…"

    play sound sfx_heartfast
    show heartattack alpha
    with Dissolve (0.1)

    hide heartattack alpha
    with Dissolve (0.2)

    "Keep your breathing steady."

    "Calm down. Don't panic."

    play sound sfx_heartfast
    show heartattack alpha
    with Dissolve (0.1)

    hide heartattack alpha
    with Dissolve (0.2)

    "Don't panic."

    show emi basic_hes_gym:
        linear 0.2 rotate -12 zoom 1.5

    emi "Do you need me to get the nurse?"

    scene black
    with shuteyefast

    "I close my eyes, shutting out the outside world."

    play sound sfx_heartfast
    show heartattack
    with Dissolve (0.1)

    hide heartattack
    with Dissolve (0.3)

    pause 1.0

    play sound sfx_heartslow
    show heartattack
    with Dissolve (0.1)

    hide heartattack
    with Dissolve (0.7)

    "My heart struggles to regain its rhythm."

    "Slowly, the pain in my chest begins to subside."

    "Soon it's gone like nothing happened."

    "It was… nothing? No, something happened there."

    play music music_rain fadein 2.0

    scene bg school_track_on
    show emi basic_hes_gym_close at center
    with openeye

    "I open my eyes again and glance at a very worried Emi."

    hi "I think I'm fine."

    "My voice sounds weird even to myself, oddly even and matter-of-fact. It makes Emi frown."

    show emi sad_annoyed_gym_close
    with charachange

    emi "I don't think you are."

    "She seems to come to a decision, and nods to herself."

    show emi basic_annoyed_gym_close
    with charachange

    emi "Right. You're coming with me."

    emi "You've got to see the nurse."

    with vpunch

    "Emi grabs my arm and drags me up. I feel a bit wobbly, but I refuse the shoulder Emi offers for support."

    "Honestly, I'm a little ashamed by my own weakness."

    "I'd really rather not have Emi concerned about me, but it seems to be too late."

    "Heck, I'd really rather not have anyone concerned about my condition, though at this point, it seems to be too late for that as well."

    "I'd like to be able to deal with the whole thing on my own, without being a bother to anyone else."

    "While I'm wishing for things, I'd rather not have this condition in the first place."

    stop music fadeout 1.0

    scene bg school_nurseoffice at bgleft
    with locationskip

    show emi basic_shock_gym at offscreenright
    with None

    show emi at tworight
    with charamovefaster

    emi "Nurse!"

    "Emi crashes into his office without knocking, but it doesn't alarm the nurse in the least."

    play music music_nurse fadein 0.5

    show nurse grin at twoleft
    with charaenter

    nk "Good morning, sunshine. What's up?"

    "Sunshine? Anyway, he calmly sips from his coffee mug but lays it down after following Emi's gaze to me looming in the doorway."

    show nurse fabulous
    with charachange

    nk "Hisao? What brings you here?"

    show emi excited_sad_gym
    with charachange

    emi "We were running and he stumbled over and started grabbing at his chest and I thought I'd come get you and make him wait there but he said he was okay but then I thought you should see him anyway and—{w=1.5}{nw}"

    show nurse concern
    with charachange

    nk "Easy there, Emi. Calm down."

    show nurse neutral
    with charachange

    nk "Hisao, what happened?"

    hi "I don't know. We were running, and then my chest started hurting like that time before, but it went away after a few seconds."

    hi "It was just a flutter or something."

    show nurse concern
    with charachange

    "The nurse frowns, as if to say that 'just a flutter' is some kind of oxymoron."

    nk "I didn't mean quite this when I suggested to get some exercise. You've got to be more careful, Hisao."

    hi "I was being careful, I just…"

    "Come to think of it, 'I just got into a race with a member of the track team' doesn't seem as well reasoned as I thought it would."

    nk "You just what?"

    hi "Er… that is…"

    hi "I was racing Emi."

    nk "Emi, is this true?"

    show emi basic_hes_gym
    with charachange

    "Emi fidgets, looking adorably contrite."

    emi "Um, well…"

    show emi basic_closedsweat_gym
    with charachange

    "Finally she can't seem to bring herself to say it aloud, and merely nods."

    "The nurse sighs and rubs at his forehead with one hand tiredly."

    nk "Emi, you've got to be more sensitive to the limits of others!"

    nk "I don't know if he told you, but Hisao has a bad heart, and getting him to race you was incredibly irresponsible."

    hi "Er, actually I started it."

    "The nurse is stunned by my statement."

    nk "You WHAT?"

    hi "We were just running, and Emi started to pull away, and so I uh, sped up to catch her."

    "The nurse stares at the ceiling, mutters a prayer for patience to some god or another, and looks back down at the both of us."

    nk "So you're {b}both{/b} stupid."

    nk "That's a comfort, I guess."

    nk "Now come on, Hisao. I've got to make sure your heart's not going to explode or something."

    show bg at left
    show nurse at center
    show emi:
        ease 1.0 offscreenright alpha 0.0
    with charamove

    hide emi

    "I dutifully obey and follow him to the adjacent room where we ascertain that I am, in fact, not going to keel over and die."

    nk "So how does it feel?"

    hi "I don't know. Nothing much. Tired, but it might be just from the exercise."

    nk "You should stay here for a few hours and rest, and we'll see how you feel after that."

    "I am not going to object, so I lie down on the infirmary bed."

    stop music fadeout 2.0

    scene bg school_nurseoffice at left
    with shorttimeskip

    "A thoroughly miserable Emi comes in after getting an earful from the nurse in the other room."

    "I couldn't hear what he said through the closed door, but I'm sure it wasn't pleasantries."

    show emi sad_depressed_gym at center
    with charaenter

    play music music_dreamy fadein 0.5

    emi "Look, I'm really, really sorry."

    emi "I should've been more careful."

    hi "Hey, you didn't know. It's not your fault."

    "She looks awfully down and sorry, and my reassurances don't do anything much to cheer her up."

    emi "I want to make it up to you."

    "Again with that decisive nod."

    show emi sad_shy_gym
    with charachange

    emi "So you have to come to lunch with me."

    emi "I'll bring it for you, okay? Something really really good!"

    "I start with a 'You don't have to…' but then shut up and just nod at her when I see her face."

    show emi excited_proud_gym
    with charachange

    emi "Good!"

    show emi basic_grin_gym
    with charachange

    emi "We meet on the roof."

    hi "We?"

    show emi basic_closedgrin_gym
    with charachange

    emi "Yep! The weather's nice now, so the roof's a great spot for lunch, you know."

    hi "I see."

    show emi sad_shy_gym
    with charachange

    emi "You'll come, right?"

    emi "You wouldn't deny me the chance to make it up to you?"

    hi "Of course not."

    show emi excited_joy_gym
    with charachange

    emi "Great! See you there!"

    hide emi
    with charaexit

    with shorttimeskip

    "I stay afloat somewhere between asleep and awake, feeling completely drained."

    "Not only my body, but all of me is limp and paralyzed, apart from my senses."

    "I swallow with difficulty and then try to lie as still as I can, which in this state is not a very hard thing to do."

    "The nurse is shuffling around on the other side of the curtains he drew to give me privacy. I can see his shadow shifting about in the sunlight."

    "He has opened the window of his office. It's windy outside."

    "The clean white curtains flutter in the breeze in a heavy, lazy motion, like waves. Light sifts through them slowly, half absorbing into the fabric."

    stop music fadeout 5.0

    scene darkgrey
    with shuteye

    "I close my eyes. The breeze on my face feels like the soft fabric of the curtains."

    "I listen to the sound of my heartbeat for a moment, trying to shut out the sound of the nurse tapping away on his computer, and my own heavy breathing."

    "It's steady."

    "Damn it, not even a week and I end up like this again. I really screwed up this time. Should've known better than to play the half-baked sports star in front of a real one."

    "And why did I try to act brave, like that heart flutter was no big deal, even when it was obvious that it was?"

    "It was just a reflex, to push it away, to keep it inside."

    "I didn't want it to happen."

    "I didn't want Emi to see it."

    "Aaah…"

    "Stupidstupidstupid."

    "I have to be more careful, or I will end up in the hospital again, or worse."

    "…"

    "That's my final thought before I give in to the tiredness."

    scene black
    with Dissolve(1.0)

    pause 2.0

    scene bg school_nurseoffice at left
    with openeye

    play music music_daily fadein 6.0

    "I fell asleep. For how long? What time is it?"

    "I'm feeling a little lightheaded and I keep blinking compulsively."

    show bg at center
    with charamove

    "Pushing the curtain aside, I squint my eyes against the unfiltered light pouring in from the window. The texture of the canvas feels nothing like the wind did before."

    "The nurse looks up from his work, sitting exactly where he was before."

    show nurse fabulous at center
    with charaenter

    nk "How are you feeling?"

    "I can't really tell, so I don't answer anything. I'm feeling kinda groggy from falling asleep at such a weird time, hopefully I don't look too weird."

    hi "What time is it?"

    "Me croaking the question to gain some orientation. The nurse looking at his wristwatch before answering."

    "Things seem to happen in slow motion."

    show nurse neutral
    with charachange

    nk "Quarter past ten."

    "I try to think for a moment what that means but I'm not really sure."

    show nurse concern
    with charachange

    nk "You didn't answer my question, Hisao."

    hi "Oh. Fine."

    show nurse neutral
    with charachange

    nk "Climb down from that bed then, and let’s see how you are doing. Don’t…"

    $ renpy.music.set_volume(0.5, 0.2, channel="music")

    show bg school_nurseoffice as dizzy_bg behind nurse:
        xalign 0.5 yalign 0.5 rotate 0 zoom 1.0 alpha 0.0
        ease 0.4 rotate 6 zoom 1.05 alpha 0.5
    show nurse neutral as dizzy_fg:
        xalign 0.5 yalign 0.5 rotate 0 zoom 1.0 alpha 0.0
        ease 0.4 rotate -4 zoom 1.05 alpha 0.5
    with Pause(0.4)

    show bg school_nurseoffice as dizzy_bg behind nurse:
        ease 1.0 rotate 0 zoom 1.0 alpha 0.0
    show nurse neutral as dizzy_fg:
        ease 1.0 rotate 0 zoom 1.0 alpha 0.0

    "I try to do exactly that, only to sway dizzily when I move too fast. The nurse moves to support me by an arm and sighs."

    show nurse concern
    hide dizzy_bg
    hide dizzy_fg
    with charachange

    nk "…stand up too quickly, is what I was going to say. Just sit there, I’ll check your pressure to make sure."

    $ renpy.music.set_volume(1.0, 2.0, channel="music")

    "My good intentions sure lasted for a long time. I shut up, embarrassed with myself, while the nurse gets busy with an old-fashioned contraption and my arm. After a couple of minutes, he puts it away, looking neither pleased nor unhappy."

    show nurse neutral
    with charachange

    nk "You’re all right. Head stopped spinning?"

    hi "Yeah."

    nk "Good. And how are the contents doing?"

    show nurse concern
    with charachange

    nk "You didn’t show very good judgment out there, Hisao."

    "I swallow the retort I was going to make. It’s what I was thinking myself, but hearing it stated by somebody else makes me want to protest."

    "What he’s saying is not pleasant to hear. Doesn’t make him any less right."

    hi "No, sir."

    show nurse neutral
    with charachange

    "He nods, still looking as neutral as he was before."

    "It would be easy to be angry at him if he said 'Told you so' or something, but he doesn’t."

    nk "I can try and help you to keep your health, but ultimately the last call lies with you. Hopefully this little episode will be something that’ll remind you of that."

    show nurse fabulous
    with charachange

    nk "Here, a note for your teacher. To avoid an interrogation."

    "I take the slip of paper he's offering and then make my leave as I can't think of anything else to say, nor even really want to."

    show nurse neutral
    with charachange

    nk "Stay out of trouble, you hear me? I don't think it was anything but a scare, but next time could be different."

    "I hear you."

    scene bg school_nursehall
    with locationchange

    stop music fadeout 4.0

    "There is some way to get to the school building straight from the auxiliary building, but I'm not keen to find out and possibly get lost, so I go out from the exit that I know works."

    scene bg school_courtyard
    with locationchange

    "I stop at the stairs of the auxiliary building, deliberating for a moment between going to the dorms to get my books and stuff and going straight away to the class."

    "The sun stings my eyes, so I head towards the dorms."

    return

label a1c9o2:
    stop music fadeout 10.0

    "I let Emi go with her own pace, and she doesn't show mercy, pulling half a lap ahead of me in an instant."

    "I don't blame her."

    "I mean, it's not as if I'm really putting up any sort of real fight out here, is it?"

    "Instead, I'm just running at a steady pace, which is what I should be doing, right?"

    "There's no need to go pushing my limits at this stage of the game."

    "God, is this even worth it?"

    scene bg school_track_on
    with locationchange

    "As we finish the second lap, I break off again."

    "Emi keeps going, and it almost seems to me that she's disappointed."

    "Well, that's stupid."

    "I don't have anything to prove to her - come to think of it, I've got nothing to prove to myself, either."

    "I'm just fine the way I am."

    "And what I'm not is a runner."

    "This was probably a bad idea."

    "Maybe there's something else I can do instead of this."

    "Getting up this early sucks, anyway. There's got to be some other way to keep healthy."

    "Walking, maybe. Nice afternoon walks."

    "Yeah, that sounds good. Running isn't for me."

    stop ambient fadeout 2.0

    scene bg school_track
    with locationchange

    "I wave to Emi and head back to my room."

    "I'll think of something else later."

    return

label a1c10o1:
    hi "It's nothing."

    show shizu basic_normal2
    with charachange

    "I quickly step in front of them, trying to hide the stuff behind my back. Shizune takes a step back, looking suspicious, but it's an expression not without concern."

    "I hope if I avoid it, she'll understand that I don't want her to keep prodding me about it."

    show shizu behind_blank
    with charachange

    shi "…"

    show misha perky_confused
    with charachange

    mi "Really? What are you hiding, Hicchan~?"

    hi "Nothing."

    show shizu basic_normal
    with charachange

    shi "…"

    show misha sign_confused
    with charachange

    mi "Is that so~?"

    "I realize I can't really squirm my way out of this. They are nosy by nature and hiding it is just going to pique their curiosity more."

    hi "Yeah okay, it is {b}something{/b}, but I don't really want to talk about it, okay? Not… yet."

    hi "Can we just put this aside for now?"

    show misha perky_smile
    with charachange

    "As Misha translates, Shizune stares at me hard with her eyes focused and analytical as ever, peering at me curiously over the rims of her glasses."

    "Her fingers press against each other thoughtfully, as if she's weighing the value of pursuing this further than necessary against the insult of disrespecting my wish."

    "Her expression finally melts into a slight smile and she signs something to Misha."

    play music music_dreamy fadein 2.0

    show shizu adjust_happy
    with charachange

    shi "…"

    show misha hips_smile
    with charachange

    mi "Okay~! Then, we'll wait, and become better and better friends, and one day when you feel like it, you can tell us about it~!"

    "Both of them smile widely at me, and I feel shocked and a little stupid about being like this."

    "They are not stupid, and probably can at least halfway guess what's going on with me. And…"

    "Such simple, kind words. I feel relieved that they don't think any worse of me even if I'm like this. Even if I'm not like the rest here. Even if I can't be at ease about it."

    "Seems that behind the obnoxious, mischievous acts, both of these girls are really kind and good people. That's what I think."

    hi "Thanks."

    hi "So, you want me to help you out today, right? Since I'm one of you now?"

    show misha hips_grin
    with charachange

    mi "Yup~!"

    hi "After class?"

    show misha sign_smile
    with charachange

    mi "No no no~! Now!"

    hi "Now? But what about class? You are going to skip again?"

    show shizu adjust_smug
    with charachange

    shi "…"

    show misha cross_laugh
    with charachange

    mi "Hahaha~! It's for the common good, so we sacrifice our math lessons, and maybe the social studies too~!"

    hi "Well, I guess I'm fine with it."

    show shizu behind_smile
    with charachange

    shi "…"

    show misha sign_smile
    with charachange

    mi "Awesome, Hicchan~! You said it, okay? Remember: 'I'm fine with helping out~,' that's what you said, right~?"

    hi "Yeah."

    "That tone… I suddenly regret saying it."

    show shizu basic_normal2
    with charachange

    shi "…"

    show misha hips_grin
    with charachange

    mi "Okay~! Are you ready to go then? We can go to the office together~!"

    hi "No. You're probably going to make me carry all your stuff for you or something."

    show shizu adjust_happy
    with charachange

    shi "…"

    show misha perky_smile
    with charachange

    mi "Don't be silly, Hicchan."

    show misha hips_smile
    with charachange

    mi "We've never walked to school together, Hicchan~."

    "I almost want to ask why we would, but then it dawns on me. The both of them consider me their friend, like Misha said before. And they want to become better friends with me, even."

    "It's weird, I've never really thought about them that way. Or any of the people I've met so far this week. Is it really so easy?"

    "Just like that…"

    hi "Okay, let's go, then."

    show shizu behind_smile
    with charachange

    "Shizune grins craftily and puts her hands behind her back."

    show misha hips_grin
    with charachange

    mi "Hahaha~! That's great, Hicchan~! Okay, okay, but first~! You had a really great idea, Shicchan liked it a lot… So~! it's time for a game!"

    hi "Oh no."

    show misha hips_smile
    with charachange

    mi "Shicchan is holding a 1000-yen note in one hand, Hicchan~! If you guess which one, you can have it! If you don't…"

    show misha hips_grin
    with charachange

    mi "You're carrying all our books to school~! Right, Shicchan~? Right~!"

    "She and Shizune exchange nods."

    show misha sign_smile
    with charachange

    mi "Okay, Hicchan~! Get ready~!"

    stop music fadeout 7.0

    scene bg school_courtyard
    with shorttimeskip

    "Carrying three bags instead of one, I think about the day that's ahead of me. Of us."

    "I can see students walking back and forth through the courtyard, probably in preparation of their own projects."

    "The festival is practically here. That means there are only two possible reasons that my help is required."

    "Either there is only a small amount of work left, and they just want a helping hand to wrap up the mundane final checks they are obligated to do."

    "Or there is a ton of work left, and Shizune is putting on a calm face as a torrent of built-up procrastinated work threatens to kill us all."

    return

label a1c10o2:
    play music music_rain fadein 4.0

    "Even so, they have really crossed the line this time. Nosy annoyances."

    hi "It's nothing."

    show misha perky_smile
    with charachange

    mi "Really~, Hicchan? It doesn't look like it's nothing to me."

    show shizu adjust_smug
    with charachange

    shi "…"

    show misha hips_smile
    with charachange

    mi "What a long line of bottles, right~? Right~! What are all of those, Hicchan?"

    hi "Just a few things."

    show shizu basic_normal2
    with charachange

    shi "…"

    show misha perky_confused
    with charachange

    mi "That looks like a lot more than 'just a few things'…"

    "I can't fault either of them for being this way. Misha's just talking for Shizune, and Shizune is just curious by nature. Still, I wish the two of them would stop digging and take the hint. But Misha wouldn't pick up on it, and Shizune can't."

    "Because of that, they keep pressing on."

    hi "It's really none of your business."

    hi "Shouldn't you be leaving? A man's room is private, you know."

    "Shizune seems to take that as a challenge."

    show shizu behind_frown
    with charachange

    shi "…"

    show misha hips_frown
    with charachange

    mi "What does that mean, Hicchan? When someone sees something interesting, their first instinct is to ask what it is, that's obvious. What's wrong with that?"

    hi "Because, like I said, there's nothing to see."

    show misha perky_confused
    with charachange

    mi "Hicchan, I think Shicchan is just concerned."

    hi "What I have in my room isn't any of your business, that's all."

    show misha sign_confused
    with charachange

    mi "But…"

    hi "Damn it! Sometimes, I wish you two would just stop playing around so much. It's not funny all the time. You know that, right?"

    "I say it way more strongly than I meant to, almost yelling straight at Misha's face. She flinches and freezes in mid-sign, and even Shizune reacts to it even though she didn't hear me."

    stop music fadeout 6.0

    "I guess my angry face said all that needs to be said to her."

    show misha perky_sad
    show shizu behind_blank
    with charachange

    "After Misha slowly finishes the translation, the girls look at each other regretfully."

    show shizu behind_sad
    with charachange

    shi "…"

    mi "Okay, Hicchan, we'll leave you alone."

    "It's the first time I've heard Misha speak without that familiar lilting up-and-down quality in her voice. It feels so strange to hear, and I want to apologize, but they have already turned to leave."

    "As the silence settles in, I regret what I said more and more."

    hide shizu
    hide misha
    with charaexit

    "The girls leave quietly, and after a while of standing in my room I dress up and follow after them."

    return

label a1c11o1:
    stop music fadeout 4.0

    "God damn it. She just doesn't know when to stop."

    hi "Yeah fine. Whatever. I'll tell you. I was having a great time."

    hi "I had a heart attack first thing in the morning and then hung out with the head nurse for a few hours for kicks."

    hi "Best morning of my life, I gotta tell you."

    "I'm trying to imitate her ridiculous lilting speech while keeping my voice so low that nobody else hears me. The words come spitting out of my mouth."

    show misha perky_confused_close
    with charachange

    mi "Hicchan, you had a what? Seriously?"

    hi "Just drop it. You heard me."

    show misha perky_sad_close
    with charachange

    mi "But Hicchan, this is important!"

    hi "No, really. Leave me alone. We're in the middle of the class, too."

    show misha sign_sad_close
    with charachange

    mi "But Hicchan!"

    "Misha sounds concerned, or maybe panicky. I wonder if she realizes herself that it wasn't the best of ideas to be so damn intrusive."

    "…"

    "I let her simmer in her own juices for a while before replying. It won't translate to Shizune but I don't care."

    hi "Piss off, Misha."

    hi "And tell Shizune to do so too."

    "As the words leave my mouth, I immediately regret saying them, but it's not like I can take them back any more."

    show misha perky_sad_close
    with charachange

    show bg at center
    show misha at offscreenleft
    with charamove

    hide misha

    "To my partial surprise, Misha actually shuts up though I don't bother checking if she passes the message to Shizune. Doesn't matter either way."

    "Mutou ends his class in some generic talk about the festival two days from now."

    return

label a1c11o2:
    hi "Give up. I'm not going to tell."

    show misha hips_grin_close
    with charachange

    mi "Is that so~?"

    hi "Yeah."

    show misha perky_confused_close
    with charachange

    "She thinks about this for a moment."

    show misha hips_frown_close
    with charachange

    mi "That's stingy, Hicchan~!"

    "I can hear the pout in her voice, disappointed and downcast."

    show bg at center
    show misha at offscreenleft
    with charamove

    "She retreats again for a moment to negotiate with the brainy half of the dynamic duo, before returning."

    show bg at bgright
    show misha:
        xalign -0.3
    with charamove

    mi "I think we should have lunch together and discuss more about this… Shicchan says."

    show misha hips_grin_close
    with charachange

    mi "It's our treat."

    show misha sign_smile_close
    with charachange

    mi "Besides, you need to make up for not being there in the morning and we need help with the work~!"

    "The other students around us are starting to give us looks, probably because Misha is leaning so much over her desk that she's almost bumping heads with me. Her curly hair brushes my neck."

    "It smells like shampoo and very much like whatever she puts in there to make it go like that."

    "I think the girl in front of me is trying to eavesdrop. Hope nobody is getting the wrong idea about this, though I'm not really sure how it would be possible to get any other kind of idea."

    "Luckily Mutou stays oblivious, or deliberately ignores Misha. So far."

    "I can't really win this one, can I?"

    menu:
        with menueffect

        "I promised to eat with Emi too, but I can't be in two places at the same time."

        "I'll go to the lunch with Emi and her friend.":
            call a1c12o1
            call class_goes_lazily

        "I'll go with Shizune, after all I'm in the Student Council now.":
            $ force_route = FR_SHIZU

            call a1c12o2

    return

label a1c12o1:
    hi "Sorry, I can't. I promised to have lunch with someone else already."

    show misha perky_confused_close
    with charachange

    mi "Eeeh? Who? Is it a girl~?"

    hi "Yeah…"

    show misha hips_grin_close
    with charachange

    "Her giggle compels me to quickly follow with something so she doesn't get the wrong idea."

    hi "It's nothing like that! It's… a bit complicated."

    show misha perky_smile_close
    with charachange

    "Complicated… yeah, that's what my life is, despite already setting into a daily routine of school life."

    "All things must be put into a new kind of perspective in this second life, reconsidered from the point of view of this new me."

    "The me with a broken heart."

    hi "Also, I don't know if I can come to the council after all."

    hi "Or at least for now. I have something else I need to focus on first."

    "That's right. I have to rethink my priorities. This is something that has swirled around in my head since the nurse gave me that speech. I really can't afford to pretend I don't have this condition."

    "I'm surprised that I can think so analytically, but I'll go with the flow for now."

    hi "I promise I'll explain properly later, but not now, okay? Please tell Shizune I'm sorry for letting her down."

    show misha perky_confused_close
    with charachange

    mi "If you say so, Hicchan."

    "She sounds surprised, and serious, which I don't think I've ever heard Misha to be before."

    show bg at center
    show misha at offscreenleft
    with charamove

    hide misha

    stop music fadeout 3.0

    "Misha luckily understands that I'm serious, a stroke of luck that I could tell what I mean so clearly even she got it. She retreats to translate our discussion to Shizune."

    "Neither of them talk to me after that."

    return

label a1c12o2:
    hi "Fine, I'll come with you, but get off my back for the rest of the class, okay?"

    show misha hips_grin_close
    with charachange

    mi "It's a deal, Hicchan~!"

    stop music fadeout 2.0

    show bg at center
    show misha at offscreenleft
    with charamove

    scene bg school_scienceroom
    with shorttimeskip

    play sound sfx_normalbell

    pause 7.0

    play ambient sfx_crowd_indoors fadein 0.3

    scene bg school_hallway3
    show crowd
    with locationchange

    "On the way to the student council room, I can see students walking back and forth through the halls, probably in preparation of their own projects."

    "The festival is practically here. That means there are only two possible reasons that my help is required."

    "Either there is only a small amount of work left, and they just want a helping hand to wrap up the mundane final checks they are obligated to do."

    "Or there is a ton of work left, and Shizune is putting on a calm face as a torrent of built-up procrastinated work threatens to kill us all."

    stop ambient fadeout 1.0

    return

label a1c13o1:
    $ renpy.music.set_volume(0.1, 1.0, channel="ambient")

    hi "It's all right, I just need to catch my breath. My condition isn't the best, these days."

    show lilly cane_oops_ni
    with charachange

    li "Oh."

    li "Is it something that… is related to you being transferred here? I mean…"

    show lilly cane_concerned_ni
    with charachange

    "She cuts herself off rather abruptly, maybe realizing she was being a bit intrusive. Her instincts are sharp though, and while I don't like the subject it's not like I should lie about it."

    "If it's Lilly, I don't think I mind."

    hi "I'm just a little weak for the time being."

    show lilly cane_oops_ni
    with charachange

    li "Hanako said you look fairly… healthy, so I naturally thought…"

    show lilly cane_sad_ni
    with charachange

    "Lilly doesn't finish her sentence again, letting it trail off with a measure of concern."

    "As she furrows her brow, Lilly's uncomfortable expression spurs me to say at least something to ease her feelings."

    "It's surprising she's this flustered, considering her straightforward attitude with her own blindness. She must know that not all share her own comfort about such things."

    hi "No, it's okay."

    hi "I have a pretty… I guess the best way to put it would be messed-up… heart. Arrhythmia."

    hi "I had a bad heart attack a while ago because of it, and spent most of the spring in a hospital. Ended in Yamaku on doctor's orders."

    "She silently nods her head in acknowledgment."

    "My answer, though, only seems to make Lilly furrow her brow even further. She doesn't seem to quite know how to react, given we don't really know each other that well."

    "I can't really fault her for it, given I have the exact same reaction."

    if talk_with_hanako:
        "To my surprise, in a moment's time her face shows that she comes to some sort of realization."

        show lilly cane_oops_ni
        with charachange

        li "Wait… so the time when Emi and you collided in the hallway…?"

        "I grimace slightly. Her ability to connect the dots quite so fast is unexpected."

        hi "Yeah. I guess I'm a textbook example of why those rules about running in the corridors exist."

        show lilly cane_sad_ni
        with charachange

        "That was a lot more dry than I'd intended. Lilly visibly shies away from continuing the topic."

    "While I do want to assuage her concern, I really don't want to dwell on this either."

    hi "Don't worry about it."

    show lilly cane_weaksmile_ni
    with charachange

    "I try to offer a reassuring smile but then I realize the futility. Without knowing this, Lilly smiles at me reassuringly but doesn't say anything further."

    $ renpy.music.set_volume(0.5, 5.0, channel="ambient")
    stop music fadeout 2.0

    scene bg school_dormext_half_ni
    show rin relaxed_surprised_ni at tworight
    show lilly cane_weaksmile_ni at twoleft
    with shorttimeskip

    "Arriving at the dorms, Rin stops in front of her mural as if lightning struck her. She had been so quiet for almost all of the walk back that I had all but forgotten she was here."

    show rin relaxed_disgust_ni
    with charachange

    rin "It's Friday, isn't it?"

    show lilly cane_smile_ni
    with charachange

    li "Yes… Friday, the eighth of June."

    show rin basic_upset_ni
    with charachange

    play music music_rin fadein 0.5

    rin "This is bad."

    show lilly cane_surprised_ni
    with charachange

    li "Bad? Why?"

    show rin negative_annoyed_ni
    with charachange

    rin "I think I am going to go in a fetal position and throw up. Possibly in reverse order."

    show lilly cane_concerned_ni
    with charachange

    li "Is something wrong?"

    show rin negative_confused_ni
    with charachange

    rin "No. Nothing is wrong. It's Friday and nothing is wrong yet. This mural, it's going to need to be finished by Sunday. So everything's all right."

    show rin negative_worried_ni
    with charachange

    rin "Do you have any drugs? Or a time machine?"

    show rin negative_confused_ni
    with charachange

    rin "This is not good. Not good."

    "So she's behind her schedule. Recalling Shizune's exasperation at Rin's carefree attitude several days ago, I don't know what to think."

    "She has left herself open for a 'told you so' unless she can pull off whatever she needs to pull off by Sunday morning."

    "Rin keeps staring at her mural looking as mortified as she can."

    show rin negative_annoyed_ni
    with charachange

    rin "Leave me. I'm going to need to work for a while."

    "I glance at Lilly, expecting her to share an incredulous look with me as I roll my eyes, but then I realize she's not one to do that kind of thing."

    show rin negative_angry_ni
    with charachange

    rin "Leave me."

    stop music fadeout 2.0

    hide rin
    with charaexit

    show lilly at center
    show bg at bgright
    with charamove

    "We do, of course, not wanting to aggravate her any more than she already is."

    "There is a churning bad feeling in my gut. Rin sure has a knack of making people feel worried about her."

    "She seems like a person who should never be left alone."

    hi "Maybe we should call someone? She sounded like she was going into shock or something."

    show lilly cane_oops_ni
    with charachange

    li "I'm sure she will be just fine. She's just a… eeeh… how to say…"

    "Lilly cocks her head a little, trying to find a polite way of calling Rin crazy without calling her crazy."

    hi "Unique?"

    show lilly cane_weaksmile_ni
    with charachange

    li "Yes, a very unique person."

    hi "I guess you could say that."

    show lilly cane_giggle_ni
    with charachange

    "She giggles at the notion melodiously, nodding in agreement."

    show lilly cane_weaksmile_ni
    with charachange

    li "Sorry about leaving you stranded as you talked to her. I… don't really understand her, so I keep my distance."

    "So my guess was right. Lilly offers a slight, apologetic smile as if she was sorry that her own shortcomings have prevented her from becoming closer to Rin."

    "I'm not one to blame her. At all."

    "Lilly lets slip a long breath, probably a disguised yawn. I imagine she's as exhausted by all this as I am."

    show lilly cane_cheerful_ni
    with charachange

    li "I'd better leave now and give these to Hanako. Thank you for the company, Hisao."

    "She smiles very sweetly at me. It feels different than normal, despite the fact that she seems to be smiling so often."

    "I can't put my finger on what the difference is. It's just different."

    "Relaxed, I'd say, but that's probably just relief over getting rid of Rin. Maybe."

    hi "Yeah… good night. Say hi to Hanako for me."

    show lilly cane_smile_ni
    with charachange

    li "I will. Good night."

    hide lilly
    with charaexit

    stop ambient fadeout 2.7

    scene black
    with Dissolve(3.0)

    return

label a1c13o2:
    $ renpy.music.set_volume(0.1, 1.0, channel="ambient")
    stop music fadeout 5.0

    hi "I… I'm fine."

    hi "There's nothing to worry about, the hill is just surprisingly steep, don't you think?"

    hi "I wonder what they have the school so high up here for anyway, don't we have students in wheelchairs and everything?"

    show lilly cane_sad_ni
    with charachange

    li "Indeed."

    show lilly cane_concerned_ni
    with charachange

    "Lilly's forehead wrinkles in concern, and I don't really want her to have that kind of an expression over me. We barely know each other."

    hi "Yeah, my thoughts exactly. Not that you can find a place like this wherever, I guess, but it makes me wonder what they were thinking."

    "My voice is overly calm, it sounds weird to my own ear and I speak way too fast. I briefly wonder how much Lilly can sense from someone's voice alone."

    li "Mmm…"

    hi "Let's continue. We're almost there anyway."

    hide lilly
    hide rin
    with charaexit

    "For the rest of the way back to the school, we all remain silent."

    stop ambient fadeout 3.0

    scene black
    with Dissolve(3.0)

    return
