# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a2_emi:
    label .morning_run:
        scene black
        with dissolve

        $ renpy.music.set_volume(1.0,0.0, "ambient")
        play sound sfx_alarmclock

        "My alarm's beeping shatters the early morning quiet, and I find myself wondering where to find the motivation to rise."

        scene bg school_dormhisao
        with openeye

        "Class is still quite far off, but I agreed to run with Emi in the mornings."

        "Really, I'm not that interested in running as a hobby, or even as a possible life-lengthening exercise."

        "However, I feel obligated to follow through on my promise to Emi yesterday, which is why I find myself throwing on some running shorts and a light tee-shirt."

        scene bg school_courtyard
        with locationskip

        "The cool morning air caresses my face as the morning sunshine causes the dew on the grass to sparkle, nearly blinding me at first."

        "As I make my way down to the track, an ugly thought strikes me."

        "What if this is some sort of joke that Emi's playing on me?"

        "Would that surprise me, really?"

        "Hell, I'd probably do it to the new guy, too."

        "At the very least, I'm sure Emi and Rin made a bet on whether or not I'd actually show up."

        scene bg school_track
        with locationchange

        "I feel a sense of trepidation as the track comes into view."

        show emi basic_annoyed_gym at center
        with charaenter

        play music music_emi fadein 1.0

        emi "You're late!"

        "It would seem that Emi is already there. What a relief."

        hi "Not according to my watch. We both are early, in fact."

        show emi basic_closedhappy_gym
        with charachange

        emi "Damn. You've got me there."

        "Emi is sitting on the bleachers, decked out in her running gear, waiting somewhat patiently for me."

        hi "I'm glad you're actually here. I was afraid that this was a joke or something."

        show emi basic_grin_gym
        with charachange

        emi "Nah, I'd never make someone get up early for nothing."

        show emi excited_proud_gym
        with charachange

        emi "Plus, Rin owes me 500 yen now. She didn't think you'd actually show up."

        "I knew it!"

        "Nice to know Emi was on my side, at least."

        show emi gymbounce_once
        with Dissolve(0.1)

        "Emi hops off of the bleachers and begins stretching out."

        play sound sfx_gymbounce

        show emi gymbounce
        with Dissolve(0.05)

        "She's remarkably lithe, almost like a dancer."

        "I set out to stretch as well, but then realize that I don't exactly remember how to stretch properly."

        "It's been ages since I stretched for anything, if you don't count my one stint at running last week."

        "And even then, I don't think I actually stretched beforehand."

        "The specter of my long hospital stay rises up again."

        "I can't say I was all that active before the hospital stay, though, so maybe I'm just being morose."

        show emi basic_closedgrin_gym
        with charachange

        "Emi giggles as she watches me stretch out."

        show emi basic_grin_gym
        with charachange

        emi "No no no Hisao, you've got to hold it for longer than that!"

        hi "I'm trying! It kinda hurts a little."

        show emi excited_proud_gym
        with charachange

        emi "Ha! That's because you're out of shape. You've got to get some flexibility in you, like this."

        show emi at offscreenbottom
        with charamovefaster

        "To demonstrate, Emi reaches down and puts her head through her legs."

        "God bless you, Emi."

        hi "I see. Is that the sort of thing I should strive for?"

        show emi basic_closedgrin_gym at center
        with charamovefaster

        emi "Of course! Flexibility is important for any runner. You'll be able to go faster the more you stretch out."

        "That makes no sense to me, but Emi seems to believe it's true."

        "With Emi's help, I manage to stretch myself out properly."

        show emi basic_grin_gym
        with charachange

        "I can't help but notice that when she thinks about how to explain things to me, her mouth scrunches up in concentration."

        "It's adorable."

        show emi excited_proud_gym
        with charachange

        emi "Not bad, Hisao. Come on, we'd better start running."

        show emi excited_happy_gym
        with charachange

        emi "We'll start off with just a mile, okay?"

        show emi basic_happy_gym
        with charachange

        emi "That's four laps around the track, got it?"

        hi "That sounds fine to me."

        show emi:
            easeout 0.5 xpos 0.4 alpha 0.0

        stop music fadeout 2.0

        "This shouldn't be too hard, right?"

        scene bg school_track_on
        with locationchange

        "A hazy memory of running a mile for gym class surfaces in my mind."

        "Yeah, it wasn't that bad."

        play music music_running fadein 0.5

        scene bg school_track_running
        with Dissolve(2.0)

        $ renpy.music.set_volume(0.5, 0.5, channel="ambient")

        play ambient sfx_emijogging fadein 1.0

        "Emi sets a pretty good pace, and I fall in behind her."

        $ renpy.music.set_volume(1.0, 0.5, channel="ambient")

        show emi basic_grin_gym at offscreenleft
        with None

        show emi at left
        with charamovefaster

        emi "Try to keep up, okay Hisao?"

        hi "Roger."

        $ renpy.music.set_volume(0.5, 0.5, channel="ambient")

        show emi at offscreenleft
        with charamovefaster

        hide emi

        "We round the first curve without incident, though I can already feel my heart rate increasing slightly."

        "By the second curve, I've started to breathe through my mouth."

        "Emi doesn't even seem to be breaking a sweat."

        "As if to punctuate her superiority, she turns around and starts running backwards."

        $ renpy.music.set_volume(1.0, 0.5, channel="ambient")

        show emi basic_closedgrin_gym at center
        with charaenter

        emi "Are you doing okay, Hisao?"

        hi "Never… better."

        show emi excited_proud_gym
        with charachange

        emi "Oh really? Maybe I should speed up then, hmm?"

        hi "Oh… no, …wouldn't want you…"

        hi "…to… overex…ert yourself."

        "My heavy panting and wheezing makes the statement less convincing than I had hoped. Emi simply smiles and turns around again."

        show emi excited_proud_gym at left
        with charamove

        emi "You're the boss, Hisao. We'll stay at this pace."

        $ renpy.music.set_volume(0.5, 0.5, channel="ambient")

        show emi at offscreenleft
        with charamovefaster

        hide emi

        "I get the feeling that I'm being mocked."

        "If I weren't in such terrible shape, I'd probably feel offended."

        "By the third lap, my breath is coming in ragged gasps."

        "I'm also awash in my own sweat. Gross."

        "We round the curve to start our fourth lap, and Emi looks back at me with a grin."

        $ renpy.music.set_volume(1.0, 0.5, channel="ambient")

        show emi basic_closedgrin_gym at offscreenleft
        with None

        show emi at left
        with charamovefaster

        emi "Here we go!"

        play ambient sfx_emisprinting

        show emi at offscreenleft
        with charamovefaster

        hide emi

        $ renpy.music.set_volume(0.3, 0.5, channel="ambient")

        "She takes off at blinding speed while I stubbornly stick to my slower pace."

        "By the time I get to the first turn, she's already rounding the second."

        "As I struggle across the back stretch, Emi continues running and catches up to me."

        play ambient sfx_emijogging

        $ renpy.music.set_volume(1.0, 0.5, channel="ambient")

        show emi excited_proud_gym at offscreenright
        with None

        show emi at center
        with charamovefaster

        emi "Come on, Hisao! You can do it!"

        $ renpy.music.set_volume(0.5, 0.5, channel="ambient")

        show emi at offscreenleft
        with charamovefaster

        hide emi

        "I'd answer her, but I'm too focused on getting air into my lungs and ignoring the burning in my leg muscles."

        "Part of me wants to say something like 'Maybe {b}you{/b} can, but I'm about to die here.'"

        "But again, I doubt I can actually form words right now."

        "Emi keeps pace with me as I round the second turn and cross the finish line."

        stop ambient fadeout 1.5

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")

        stop music fadeout 5.0

        show bg school_track_on
        show emi basic_happy_gym at center
        with locationchange

        "Her sprint seems to have gotten her sweating."

        "It's actually caused her shirt to turn slightly translucent. It seems she wears a black sports bra."

        "I feel a vague stab of guilt for being the sort of guy who stares at a girl's chest, but my legs and chest are burning so badly I can't bring myself to care that much."

        show emi excited_proud_gym
        with charachange

        emi "Not bad for a first effort, Hisao."

        play music music_happiness fadein 0.5

        hi "Ki— …kind of you… to say… so."

        "Emi seems to be, if not out of breath, at least breathing a little more heavily than she was before we started running."

        "It must have been the sprint that did it."

        show emi basic_grin_gym
        with charachange

        emi "Hey, I've got to get a few sprints in. You should walk around the track to cool down."

        emi "Then we can stretch out, and we'll be all done, okay?"

        hi "Sounds great."

        "My legs are on fire, and my breathing is still heavy, but surprisingly my heart seems to be taking the strain well."

        "Another triumph of medical science, I suppose."

        show emi basic_closedhappy_gym
        with charachange

        emi "You should put your hands behind your head. It makes it easier to catch your breath."

        $ renpy.music.set_volume(0.3, 1.0, channel="ambient")

        play ambient sfx_emipacing

        show emi at offscreenleft
        with charamovefaster

        hide emi

        "Surprisingly, she's right. I begin to stroll around the track, happy to feel my breath coming back to me."

        $ renpy.music.set_volume(1.0, 0.5, channel="ambient")

        show emi blur at offscreenright
        with None

        show emi at offscreenleft
        with move

        $ renpy.music.set_volume(0.3, 0.5, channel="ambient")

        hide emi

        "There's a blur as Emi sprints by me."

        "Watching her run is absolutely fascinating."

        "It's not just because she's on prosthetics, though that is interesting."

        show ev emi_run_face:
            zoom 1.0 xalign 0.5 yalign 0.5
            ease 10.0 zoom 1.055
        with dissolve

        "The really interesting thing is the way her face changes."

        "I can only catch glimpses of it as she runs by, but her eyes seem to come alive with a sort of fierce joy."

        "It's as if there's nothing else in the world but her and the track."

        stop ambient fadeout 0.5

        $ renpy.music.set_volume(1.0, 0.5, channel="ambient")

        scene bg school_track_on
        with locationchange

        "By the time I've gotten to the final stretch, Emi seems to have finished her sprinting."

        "She's breathing heavily now, but she's wearing a satisfied grin on her face. She waves to me cheerily as I near her."

        show emi basic_grin_gym at center
        with charaenter

        emi "Feeling better, right?"

        hi "Actually, yeah."

        show emi sad_grin_gym
        with charachange

        emi "D'you want to take another lap around with me? I've got to cool down too, you know."

        "Part of me would rather sit down, and not move, but something tells me that would be a bad idea."

        "Besides, if I sit down, there may be no getting back up again."

        hi "Sure, why not?"

        "Emi's got her hands behind her head now as well, which makes her seem very relaxed."

        "The positioning of her arms also pulls her shirt upwards ever-so-slightly so that I can see a small strip of her belly."

        "I do my best to act the gentleman and not look, but the contrast of her skin against her red running shorts is rather arresting."

        show emi basic_grin_gym
        with charachange

        emi "So how do you feel, Hisao?"

        hi "Surprisingly good, actually. I'm sore and tired, but… surprisingly good."

        "As soon as I say it, I realize that it's true."

        "Sure, part of me wants to lay down and die, but I feel like I've accomplished something."

        "It's almost like a glow throughout my body that persists despite the soreness."

        show emi excited_proud_gym
        with charachange

        emi "Yeah, that's the runner's high."

        hi "Runner's high?"

        show emi basic_hes_gym
        with charachange

        emi "Yeah, it has something to do with… adrenaline?"

        "Emi thinks for a moment as we walk, trying to remember."

        show emi basic_closedgrin_gym
        with charachange

        "Then she shrugs and grins at me."

        show emi basic_grin_gym
        with charachange

        emi "I don't actually remember. It's a good feeling though, isn't it?"

        show emi basic_happy_gym
        with charachange

        stop music fadeout 0.5
        play sound sfx_heartstop

        emi "Better than sex, right?"

        "I open my mouth to respond shortly before processing what she's just said."

        hi "…"

        "Emi watches my face for a few moments before bursting into laughter."

        play music music_comedy fadein 1.0

        show emi excited_laugh_gym
        with charachange

        emi "Sorry, sorry! I couldn't resist! You're just too easy!"

        hi "Why did I agree to run with you again?"

        "Emi just laughs harder. She takes a hold of my forearm and tilts it, allowing her to get a better view of my watch. Her face changes the moment she sees the time."

        show emi basic_shock_gym
        with charachange

        emi "Oh no! We'd better get a move on, Hisao!"

        show emi basic_closedsweat_gym
        with charachange

        emi "Class is in an hour, and I need to shower!"

        hi "I should probably do that as well…"

        show emi basic_hes_gym
        with charachange

        emi "I need to see the nurse, too… maybe he'll write me a note for being late!"

        hi "Why do you need to see the nurse?"

        show emi basic_closedgrin_gym
        with charachange

        "Emi points to her prosthetics, as if that would explain everything."

        show emi basic_grin_gym
        with charachange

        emi "It's important to check for irritation."

        emi "You know, from sweat or friction, or anything."

        show emi excited_amused_gym
        with charachange

        emi "Normally I only go after practice, but if we're going to be doing these morning runs then I guess I'll see him twice a day."

        "Wait, so Emi has only started doing these runs since I showed up?"

        hi "If it's more convenient for you to run with me at a later time…"

        show emi sad_grin_gym
        with charachange

        emi "Don't be silly! I've been meaning to start running in the morning for a while now."

        emi "But if I didn't have a partner to run with, I'd be less likely to keep up a routine."

        show emi basic_grin_gym
        with charachange

        emi "It's always harder to blow off a commitment if you're going to let someone else down, you know?"

        show emi basic_closedgrin_gym
        with charachange

        emi "So you'll be my running partner for the mornings!"

        show emi excited_proud_gym
        with charachange

        emi "We both need the exercise, so it all works out, don't you think?"

        hi "Yeah, perfect."

        "Did it have to be me, though?"

        "Well, I guess I can't complain too much. Emi's pretty fun to hang out with."

        "And she's right. I do need the exercise. Doctor's orders, even."

        show emi basic_happy_gym
        with charachange

        "Emi waves a quick goodbye to me."

        emi "Right, I'm off! Come have lunch with us, okay?"

        hi "What?"

        show emi basic_closedhappy_gym
        with charachange

        emi "Lunch! You know, the meal? In the middle of the day? Come have it with us!"

        hi "Where?"

        show emi basic_grin_gym
        with charachange

        emi "The rooftop. Rin likes it up there."

        hi "When?"

        show emi basic_annoyed_gym
        with charachange

        emi "Lunchtime, when else? That was a silly question."

        hi "Yeah, but I sort of felt the need to ask all three for completeness' sake."

        show emi excited_laugh_gym
        with charachange

        "Emi laughs and grins. I don't think I've ever seen a girl smile so much before."

        show emi excited_happy_gym
        with charachange

        emi "Not bad, Hisao. See ya!"

        play ambient sfx_emisprinting

        show emi at offscreenleft
        with charamovefaster

        hide emi

        stop ambient fadeout 2.0
        stop music fadeout 8.0

        "With that, she takes off like a shot for the school building."

        "I guess she's going to see the nurse first."

        scene bg school_dormbathroom
        with locationskip

        "I hurry back to my room and hop in the shower, only to find that the water takes a while to heat up."

        play ambient sfx_shower
        with vpunch

        "The shock of the cold water nearly kills me."

        show steam
        with Dissolve(2.0)

        "I manage to warm the water a bit and spend some quality time feeling my muscles loosen."

        "My heart, surprisingly, feels the least bothered by the run."

        "I suppose that's a good thing, even if it does make me feel like a bit of a wuss."

        "I mean at least I'd have an excuse beyond 'I am out of shape' if my heart were bothering me."

        "Guess I'll have to keep this running thing up, otherwise I'm sure Emi won't let me hear the end of it."

        "It's only after I get out and dry myself off that I realize that I've only ten minutes left to put my clothes on and get to class."

        "Crap."

        if _in_replay:
            return

    label .clouds_time_travel_and_thou:
        scene bg school_dormbathroom
        show steam

        stop ambient fadeout 1.0

        scene bg school_scienceroom
        with shorttimeskip

        play sound sfx_normalbell

        "The hands on the clock finally set me free from the tedium of yet another fun-filled class."

        "Getting up from my seat proves to be more of a problem than I anticipated."

        "My legs are killing me from the morning's run."

        "Maybe doing these with Emi isn't such a hot idea after all."

        "Still, the run's given me a hell of an appetite."

        play ambient sfx_crowd_indoors fadein 1.0

        scene bg school_hallway3
        show crowd
        with locationchange

        "I'm halfway down the hallway to the cafeteria when I remember that I've got my lunch with me."

        "My parents saw fit to provide me with some prepackaged stuff when I moved in, and a good thing too."

        "The hallway is packed with students headed for the cafeteria."

        "Going back is like swimming upstream - but I've got an appointment to keep on the rooftop."

        stop ambient fadeout 4.0

        scene bg school_staircase1
        with locationchange

        "It takes me a moment to find the staircase leading up to the rooftop, but I'm willing to bet that Emi and Rin aren't up there by now anyway."

        "In fact, I think I saw Emi among the bodies in the hallway headed for the cafeteria."

        play sound sfx_door_creak
        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
        play ambient sfx_rooftop fadein 0.5

        scene bg school_roof at bgright
        with locationchange

        "I step out of the door to the roof and take a deep breath."

        "The fresh air blowing against my face and body almost makes my legs hurt less."

        show rin basic_awayabsent at center
        with charaenter

        rin "Maybe if I'm upside down…"

        $ renpy.music.set_volume(1.0, 0.0, channel="music")
        play music music_rin fadein 1.0

        "Part of me wants to be surprised that Rin's already up here."

        hi "What's that going to accomplish?"

        show rin basic_deadpan
        with charachange

        rin "Things in the clouds."

        hi "Couldn't you just… look at them right-side up?"

        show rin basic_deadpanupset
        with charachange

        "Rin rolls her eyes in something approaching exasperation."

        rin "Then I wouldn't get a new perspective."

        hi "Is upside down really a new perspective?"

        show rin basic_delight
        with charachange

        "Ah ha! That caught her off guard. Rin looks pensive."

        rin "You may have a point. Maybe sideways."

        show rin at offscreenbottom
        with charamove

        hide rin

        "As Rin lays down on the bench to look at the sky, I give up."

        play sound sfx_impact2
        with vpunch

        show emi basic_closedgrin at center
        with charaenter

        "Fortunately Emi chooses that moment to burst through the door carrying two bags."

        "She nearly takes the door off the hinges."

        show emi basic_hes
        with charachange

        emi "Sorry it took me so long! There were a ton of people in line."

        show emi basic_grin
        with charachange

        show emi at twoleft
        show bg at center
        with charamove

        "She drops the first bag in front of Rin and takes a seat on the bench next to her."

        hi "You buy Rin's lunch for her?"

        show emi basic_closedgrin
        with charachange

        emi "Sometimes, yeah. I'd have Rin buy my lunch for me in return, but I'm not sure how she'd carry it."

        show rin basic_deadpan:
            tworight
            yanchor 0.0

        show rin at tworight
        with charamovefaster

        rin "Plus I'd never buy her lunch."

        "If Rin's offended by Emi's comment, she doesn't show it. Emi sniffs."

        show emi basic_annoyed
        with charachange

        emi "How ungrateful of you."

        "I'm not sure whether the two are joking with one another or if I'm witnessing the beginnings of a cat fight."

        show emi basic_closedgrin
        show rin basic_amused
        with charachange

        "The two girls stare at one another for a few tense moments before breaking into smiles."

        show rin basic_awayabsent
        with charachange

        rin "Hey Emi, do you think being upside down is a new perspective on things?"

        "Didn't I already have this conversation?"

        show emi basic_hes
        with charachange

        "Emi looks thoughtful, apparently giving the question some thought."

        "After a deep and profound pause, she speaks."

        show emi basic_closedsweat
        with charachange

        emi "I have no idea."

        "Well, at least she's as lost as I am."

        stop music fadeout 4.0

        show emi excited_happy
        with charachange

        emi "Hey Hisao, you're coming to the track meet, right?"

        "The question comes out of the blue and catches me off guard."

        hi "Um… I don't know yet?"

        show rin basic_absent
        show emi sad_annoyed
        with charachange

        emi "Honestly, Hisao, after I went through all the trouble of letting you run with me in the morning, you won't even show up at my track meet?"

        show rin basic_awayabsent
        with charachange

        "Wasn't she the one that asked me to run with her?"

        "Actually, she didn't even give me a choice in the matter."

        hi "Wait, no, I didn't say that…"

        play music music_ease fadein 3.0

        show emi basic_closedgrin
        show rin basic_absent
        with charachange

        "She beams at me as if I'd just agreed to give her a million dollars."

        show emi basic_closedhappy
        with charachange

        emi "So you will come after all! That's great!"

        "I didn't say that either!"

        show rin basic_deadpan
        with charachange

        rin "I'll be going too, so I'll make sure he comes, Emi."

        show emi basic_grin
        show rin basic_absent
        with charachange

        emi "Good idea, Rin! Maybe we can get some food or something after the meet's over?"

        "I feel like I've just been conned, but not by these two."

        "More like by some outside force, pushing me irrevocably toward my destiny."

        "…Or maybe I shouldn't read books that feature conspiracy theories so heavily. Otherwise I might wind up sounding like Kenji."

        "Still, I suppose that I've got to show up now."

        "I don't think that I could stand against both of them being disappointed."

        "I'd never hear the end of it."

        hi "When is it again?"

        show emi basic_annoyed
        with charachange

        emi "Next week, silly! I just told you a few days ago."

        hi "No you didn't."

        show emi sad_shy
        with charachange

        emi "I forgot? Well, you won't forget to come though, will you?"

        hi "Of course I won't! I'll even make a note on a calendar or something!"

        show rin basic_lucid
        with charachange

        "Rin nods sagely."

        show rin basic_deadpancontemplation
        with charachange

        rin "That's probably a good idea, you know. Unless time changes its course."

        show emi basic_confused
        with charachange

        emi "It can do that?"

        show rin relaxed_nonchalant
        with charachange

        "Rin gives a noncommittal shrug."

        show rin negative_spaciness
        with charachange

        rin "It hasn't yet, but you never know…"

        show emi basic_closedgrin
        with charachange

        "This time it's Emi who gives a shrug."

        show emi basic_closedhappy
        with charachange

        emi "I suppose it can't be helped if it happens."

        show rin basic_deadpannormal
        with charachange

        rin "Not unless you're a time traveler or something."

        hi "You don't actually think that could happen, do you?"

        show emi basic_confused
        with charachange

        emi "I don't think we do… do we?"

        show rin relaxed_nonchalant
        with charachange

        "Rin shrugs again. That seems to be her default response to everything."

        show rin basic_deadpandelight
        with charachange

        rin "I suppose not. But I reserve the right to change my opinion at a moment's notice."

        "For Rin, this statement makes a disturbing amount of sense."

        "The fact that I realize this now frightens me a bit."

        "I wonder if Emi gets this feeling all the time."

        show emi basic_closedgrin
        with charachange

        "If she does she's not showing it, though. Emi merely nods."

        show emi basic_grin
        with charachange

        emi "As expected."

        show rin basic_deadpanupset
        with charachange

        rin "What's that supposed to mean?"

        show emi sad_grin
        with charachange

        "This time, it's Emi who shrugs."

        "It's like she's using Rin's own weapons against her."

        show emi excited_proud
        with charachange

        emi "Your response is the sort of thing I'd expect from you, that's all."

        show rin negative_worried
        with charachange

        rin "Am I really that predictable?"

        show emi basic_closedgrin
        with charachange

        "Emi's smile seems to border on gloating."

        emi "Nah, it's just that your unpredictability is pretty predictable."

        show rin relaxed_nonchalant
        with charachange

        rin "Well that's all right then."

        play sound sfx_warningbell

        "I don't get the chance to see whether Rin's being serious or not, as the bell rings."

        "I didn't notice the lunch period slipping by at all."

        "Hanging out with these two was far too interesting."

        show emi basic_shock
        with vpunch

        "Emi jumps up, a look of panic on her face."

        emi "Oh no! I needed to stop by my room to pick up my notebook for the next class!"

        show rin basic_deadpandelight
        with charachange

        rin "Don't you wish you had a time machine now?"

        "Rin seems rather smug as she delivers this line; like she'd just won an argument."

        "Emi ignores Rin's comment."

        show emi basic_hes
        with charachange

        emi "Sorry Hisao, but could you make sure our garbage gets thrown away?"

        show emi basic_closedsweat
        with charachange

        emi "I usually clean up myself, but I've got to run!"

        hi "Sure, no problem."

        show emi at offscreenleft
        with charamovefaster

        hide emi

        "Emi darts away with an urgency I'm starting to expect from her."

        hide rin
        with charaexit

        "I don't bother asking Rin why she couldn't help. She already seems to be preoccupied with something else entirely as she wanders off."

        "She's probably used to Emi taking care of cleanup, and for some reason I doubt Emi's ever raised the issue with her."

        "Cleaning up from lunch doesn't take long, so I have plenty of time to toss our garbage and get to class."

        stop ambient fadeout 1.0

        scene bg school_scienceroom
        with locationskip

        "Misha greets me with a wave and a devious grin as I walk through the door."

        show misha cross_grin at center
        with charaenter

        mi "Didn't see you in the cafeteria, Hicchan."

        hi "Yeah, I decided it was too crowded there."

        show misha hips_grin
        with charachange

        "Misha's grin gets even wider."

        mi "Oh really? Are you sure you weren't participating in an illicit ren—dez—vous?"

        hi "W… what? What are you talking about?"

        show misha sign_smile
        with charachange

        mi "You were on the roof, right? With both Rin and Emi, no less! You Casanova, you!"

        hi "We… we just had lunch, that's all!"

        show misha cross_laugh
        with charachange

        "Misha bursts into laughter, drawing the attention of several of my classmates."

        mi "Wahahaha! You're so adorable when you blush like that, Hicchan!"

        show misha cross_grin
        with charachange

        "She gives me a conspiratorial wink."

        show misha cross_smile
        with charachange

        mi "Don't worry, your secret's safe with me."

        hi "There's no secret!"

        show misha perky_confused
        with charachange

        mi "Oh?"

        "Misha seems disappointed and then brightens up again."

        show misha hips_grin
        with charachange

        mi "Time will tell~!"

        "I don't know what the hell she's talking about, but blessedly our teacher comes in, and the class starts."

        stop music fadeout 2.0

        if _in_replay:
            return

    label .questions_that_need_answering:
        scene bg school_scienceroom
        with shorttimeskip

        play sound sfx_normalbell

        "Another day of class has finally dragged itself to a close."

        "Unexpectedly, I managed to stay awake for the whole day."

        "I'm pretty sure that counts as a miracle."

        "My legs seem unwilling to stand up for a moment."

        "I guess the run took a lot out of me."

        scene bg school_hallway3
        with locationchange

        "I head down the hallway and make my way to my room."

        scene bg school_dormhisao
        with locationskip

        "I sit down and half-heartedly chip away at my homework for a while, feeling like a vulture picking at a particularly unsavory carcass."

        "It knows this is what it eats, but it's not sure that it shouldn't be ordering takeout instead."

        "I don't think I can take this, but it's important to get my work done."

        hi "Now let's see… what was I supposed to be looking over again?"

        "I know it's a losing battle, but I fight it anyway."

        "Halfway through my math homework, I put my pencil down."

        "This isn't working. I need a distraction."

        "Unfortunately, my options for distractions are rather slim."

        "I'm not in the mood to read, right now."

        "Kenji is, unusually, out of his room at the moment."

        "If I go to the student council room, I'll just end up doing work for those two."

        "And heaven only knows where everyone else is, except for…"

        "Well, I suppose that's an option."

        "I grab my shoes and head for the track. Emi's probably down there."

        play music music_tranquil fadein 3.0

        scene bg school_track_ss
        with locationskip

        "Track practice is just ending as I arrive at the track."

        "The sun's beginning to dip low in the sky."

        "Has it really gotten that late already?"

        show emi basic_grin_gym_ss at center
        with charaenter

        emi "What are you doing down here, Hisao?"

        show emi excited_proud_gym_ss
        with charachange

        emi "Come to spy on me, have you?"

        "I give a shrug. To be honest, I'm not sure why I'm down here."

        hi "I didn't have anything better to do."

        "I figure that's about right."

        "At the moment, Emi's the only person I can think of who I could visit."

        show emi basic_annoyed_gym_ss
        with charachange

        emi "So I'm your last resort, am I?"

        show emi sad_angry_gym_ss
        with charachange

        emi "Nobody cool around, so I'll just go see Emi, is that what you thought?"

        "She actually looks angry."

        "A chance for some teasing of my own presents itself."

        hi "Actually, yeah, I guess you are."

        show emi sad_annoyed_gym_ss
        with charachange

        "Emi pouts, widening her eyes to give the maximum amount of puppy-dog resemblance."

        hi "Kidding! I was kidding!"

        show emi basic_closedgrin_gym_ss
        with charachange

        emi "So you are down here to stalk me!"

        "Wait, what?"

        hi "That's not what I meant!"

        hi "Why would I stalk you anyway? It's not like you require stalking."

        hi "If you're not asleep or in class, you're down here, right?"

        "Emi laughs at this comment."

        show emi basic_happy_gym_ss
        with charachange

        emi "Well, you're not all wrong, I suppose - but you forgot about eating. I do that too, you know."

        "I nod, conceding the point."

        show emi sad_grin_gym_ss
        with charachange

        emi "Plus I hang out with Rin sometimes too… so really I might take some effort to stalk."

        hi "What do you two do together anyway? You don't seem to have a lot in common."

        show emi basic_closedgrin_gym_ss
        with charachange

        "She puts her hands on her hips and assumes a superior air."

        show emi basic_grin_gym_ss
        with charachange

        emi "That's what you think. I've got all sorts of hidden hobbies, you know."

        hi "Oh really? Like what?"

        show emi sad_grin_gym_ss
        with charachange

        "Emi puts her head to one side, as if she's trying to remember what it is she does in her free time."

        show emi basic_closedgrin_gym_ss
        with charachange

        emi "Well, Rin and I go out shopping sometimes."

        "I guess that makes sense. Emi's a girl, after all. But Rin?"

        hi "Rin comes with you?"

        show emi basic_grin_gym_ss
        with charachange

        emi "We usually swing by the art supply store."

        emi "Plus she likes this music store that sells all kinds of weird sounding stuff."

        show emi basic_closedhappy_gym_ss
        with charachange

        emi "She says it helps focus her."

        "That makes a little more sense."

        hi "I see. Any other hidden hobbies?"

        show emi excited_proud_gym_ss
        with charachange

        "Emi wags a finger at me."

        emi "Now now, why would I go and reveal all my dark secrets to you? We hardly know one another!"

        "Somehow I think that's all that Emi has in the way of hobbies."

        "Still, I don't think my question's been answered."

        hi "Even if you do have a few hobbies, I still don't see why you hang out with Rin so much."

        hi "I mean, she's kind of weird, isn't she?"

        "This comment causes Emi to laugh loudly."

        show emi basic_closedhappy_gym_ss
        with charachange

        emi "Ha! That's the understatement of the year!"

        hi "So why? I mean, you're a lot better at conversation and stuff, so I figure you'd hang out with a lot of people, but I think I've only ever seen you with Rin."

        show emi sad_annoyed_gym_ss
        with charachange

        "Emi seems unusually defensive."

        emi "Hey, I hang out with plenty of people that aren't Rin! You just don't see me doing it because I'm not in your classes."

        hi "Okay, but that still doesn't explain why you hang out with Rin."

        "I'm not even sure why I want to know this."

        "I guess it is because lunch was so strange."

        show emi basic_confused_gym_ss
        with charachange

        "Emi shrugs, looking for a moment very Rin-ish."

        stop music fadeout 4.0

        emi "It's because we have similar outlooks."

        "If you were to ask me the least likely answer to my question, that would be it."

        hi "What do you mean?"

        emi "It's like…"

        play music music_emi fadein 1.0

        show emi basic_grin_gym_ss
        with charachange

        emi "Okay, Rin paints and stuff, right?"

        hi "Yes…"

        "I'm not sure where this is going."

        show emi basic_closedgrin_gym_ss
        with charachange

        emi "Well, I run."

        hi "And?"

        show emi basic_happy_gym_ss
        with charachange

        emi "And… that's why we're similar."

        hi "…"

        hi "You lost me."

        show emi basic_annoyed_gym_ss
        with charachange

        "Emi frowns, as if trying to figure out her answer."

        emi "Well, maybe it's that we do things for the same reasons."

        hi "Huh?"

        show emi sad_grin_gym_ss
        with charachange

        emi "You know, we follow our passions."

        hi "So you're passionate about running and Rin's passionate about art, is that it?"

        emi "Well, sort of. Let me think…"

        show emi basic_closedgrin_gym_ss
        with charachange

        emi "Well, Rin explained it to me once, but I don't know how much of it I followed."

        "Not surprising. I think any explanation from Rin would probably confuse anyone."

        show emi basic_grin_gym_ss
        with charachange

        emi "She says we both chase after an extreme."

        emi "Like, she's always trying to find a new way to show a particular feeling or something."

        show emi sad_grin_gym_ss
        with charachange

        emi "And I run because of the feeling I get from it."

        emi "And since we don't allow ourselves to be slowed down by anything, we make a connection based on that."

        hi "What do you mean 'slowed down by anything?'"

        show emi basic_confused_gym_ss
        with charachange

        "Emi looks surprised and points to her legs."

        emi "You know, because I'm a runner. And Rin's a painter even without arms."

        emi "So we respect each other's determination."

        show emi basic_closedhappy_gym_ss
        with charachange

        emi "And that's why we hang out."

        show emi sad_grin_gym_ss
        with charachange

        emi "I think."

        "Well, I'm not sure that made any sense to me… but from Emi's sheepish expression, she's not sure about it either."

        emi "Honestly, it's not something I think about much."

        emi "We just get along - I think that's really all that matters."

        "I suppose she's got a point there."

        "Another question strikes me, and since I've got nothing better to do, I ask it."

        hi "So what got you so into running, anyway?"

        show emi basic_closedgrin_gym_ss
        with charachange

        emi "Oh, I've been running since I was really little!"

        show emi basic_grin_gym_ss
        with charachange

        emi "My dad was a runner, and so as soon as I could walk, he started teaching me how to run."

        show emi sad_grin_gym_ss
        with charachange

        emi "It was our father/daughter thing, you know?"

        show emi sad_depressed_gym_ss
        with charachange

        stop music fadeout 10.0

        emi "Our own mutual hobby."

        "A shadow crosses her face, and I'm shocked to see her looking… sad."

        "Did something happen between them?"

        show emi basic_shock_gym_ss
        with charachange

        emi "Man, I don't have a lot of time left."

        show emi basic_closedsweat_gym_ss
        with charachange

        emi "Sorry, but I've got to get a few more laps in before I go see the nurse!"

        play ambient sfx_emipacing

        show emi at offscreenleft
        with charamovefaster

        hide emi

        $ renpy.music.set_volume(0.3, 1.0, channel="ambient")

        "She races off around the track, hair streaming in the wind."

        "It seems to me she's going a lot faster than she was this morning."

        "As she rounds the track, I catch a glimpse of her face."

        scene ev emi_run_face_ss:
            zoom 1.05
            ease 10.0 zoom 1.0
        with locationchange

        "It's much the same as it was this morning, but her eyes seem to have taken on a harder edge."

        "I guess she's right."

        "I don't really know much about her."

        scene bg school_track_ss
        with locationchange

        "I watch her run for a little while and then stand up to head back to my room."

        emi "Hey!"

        "She spots me leaving and waves to catch my attention."

        emi "Don't forget! Same time tomorrow morning, got it?"

        hi "Got it."

        stop ambient fadeout 2.0

        "I head back to my room."

        "Homework beckons."

        if _in_replay:
            return

    label .second_times_the_worst:
        scene bg school_track_ss

        scene bg school_dormhisao_ni
        with shorttimeskip

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")

        "I can't sleep."

        "My body's tired, but my mind is kept awake, staring at the ceiling in the hollow darkness of my room."

        "I grasp desperately for a thread of thought, hoping that I can run my brain into the ground."

        "All I can think of is how I can't think of anything."

        "This is not productive at all."

        "I wonder if this is a side effect of my medication, though it seems odd for it to take so long to show up."

        "Then again, maybe I'm just not as used to my new surroundings as I'd like to think."

        "I don't know, but for whatever reason, I'm awake and I shouldn't be."

        "This is ridiculous."

        play sound sfx_switch

        scene bg school_dormhisao
        with Dissolve(0.2)

        "Ignoring my body's stiffness, I get out of bed and look at my clock."

        "Four in the morning. Last time I checked it was only one, so maybe I slept a little."

        "I don't know."

        "I throw on some clothes and head out of my room."

        "A walk might do me some good."

        scene bg school_courtyard_ni
        with locationskip

        "I'm surprised at how chill the air is compared to the relative warmth of the day."

        "I can almost see my breath as I wander the campus, waiting for the sun to come up or for me to fall asleep."

        "At this point, either option works for me."

        scene bg school_track_ni at left
        with locationchange

        "I find myself at the track - where for the first time, Emi's not out running."

        "I suppose that makes sense; it's too early, even for her."

        "The bleacher seats are cold, but at this point I welcome the sensation."

        show bg school_track as overlay:
            left
            alpha 0.0
            linear 15.0 alpha 0.5

        "The sun is starting to show its face over the horizon, and I know with an awful certainty that I'll get no more sleep tonight."

        "The sun's steadily strengthening rays start to warm me up, and I watch the dew on the ground begin to steam slightly."

        "My mind calms down, a little."

        stop music fadeout 2.0

        scene black
        with shuteye

        pause 3.0

        play sound sfx_rustling

        "Someone's shaking me."

        emi "Hey, wake up!"

        hi "Huh? Where? Wha?"

        scene bg school_track
        show emi basic_shock_gym_close at center
        with openeyefast

        "I guess I fell asleep after all."

        show emi basic_annoyed_gym_close
        with charachange

        emi "What are you doing out here? You're going to catch a cold or something!"

        play music music_dreamy fadein 4.0

        "I rub my eyes and am confronted by Emi, who bends over me with a worried expression."

        "I'm still a little groggy, so my response comes out in a mumble."

        hi "Couldn't sleep. Watched the sun come up."

        show emi basic_confused_gym_close
        with charachange

        emi "Sounds like something Rin would say."

        "I shrug, feeling the stiffness that comes with sleeping on a bench for a few hours."

        hi "Is it? I wouldn't know."

        show emi basic_grin_gym_close
        with charachange

        "Emi grins a little at my (somewhat cranky) response."

        show emi basic_closedgrin_gym_close
        with charachange

        emi "So, couldn't sleep, eh? Obviously we need to run you harder today!"

        "Even though I've only known her for about a week, this seems a very Emi-ish response to the problem."

        hi "Hey, my body was plenty exhausted after yesterday!"

        hi "My mind was just racing, that's all."

        show emi basic_confused_gym_close
        with charachange

        emi "I don't see the difference. If you run hard enough, your brain will get tired too."

        "I'm seriously questioning the wisdom of doing this first thing in the morning."

        "I don't know if my grades will be able to handle me tiring my brain out like that."

        show emi basic_closedgrin_gym_close
        with charachange

        with vpunch

        show emi basic_closedgrin_gym
        with charadistant

        "Emi pulls me up from the bleachers with surprising strength for someone her size."

        emi "Now come on, Hisao! We've got work to do!"

        "I don't actually know if I'm up to this today, to be honest."

        "I mean I obviously didn't get much sleep… and what sleep I got was on the bleachers!"

        hi "I don't know… should I really be running?"

        show emi basic_annoyed_gym
        with charachange

        "Emi glares at me."

        "Good heavens."

        show emi sad_annoyed_gym
        with charachange

        emi "What are you talking about? Of course you should be running!"

        emi "How else do you expect to work out the kinks?"

        show emi basic_annoyed_gym
        with charachange

        emi "You've been sleeping on the bleachers, for heaven's sake!"

        emi "The best way to get that soreness out is to run around a little."

        emi "Now stop hiding in the bleachers and get down here!"

        "There's no arguing that. I'm pretty sure she'd kill me if I didn't do as she said."

        "I get to my feet and hop down to the track."

        scene bg school_track_on
        with locationchange

        "The sun is warming things up rather nicely, I think."

        "Emi and I begin to stretch out, and I find myself once again hard pressed not to stare."

        "If this is how I have to wake up every day, I might be able to get used to this."

        show emi basic_annoyed_gym at center
        with charaenter

        emi "You know Hisao, it's not polite to stare."

        hi "I wasn't staring! I swear!"

        "Emi raises an eyebrow and considers me for a minute, as if evaluating my response."

        "There's a brief moment where I'm afraid for my life."

        show emi basic_closedhappy_gym
        with charachange

        "But then she smiles and laughs, shaking her head slowly."

        show emi basic_grin_gym
        with charachange

        emi "Honestly, you didn't have to deny it so strenuously."

        stop music fadeout 5.0

        "In response, I clap my hands together and go for a change of subject."

        hi "So! That's enough stretching, right?"

        show emi sad_grin_gym
        with charachange

        "Emi gives a casual shrug."

        emi "Do you feel stretched? That's really how you tell."

        "Well, I do feel up to the run, if that's what she means."

        hi "Yeah, I feel ready to go."

        show emi basic_grin_gym
        with charachange

        emi "Same as yesterday, okay?"

        emi "We'll just run for a mile at a steady pace."

        show emi basic_closedhappy_gym
        with charachange

        emi "Don't worry about going really fast, just worry about keeping the pace, got it?"

        hi "You're the boss."

        play music music_running fadein 0.5

        show emi basic_grin_gym
        with charachange

        play ambient sfx_emijogging

        show emi at offscreenleft
        with charamovefaster

        hide emi

        $ renpy.music.set_volume(0.5, 2.0, channel="ambient")

        "Emi grins again, and we take off around the track."

        scene bg school_track_running
        with Dissolve(2.0)

        "…"

        "…"

        "I think I'm going to die."

        "We're not even done with the first lap, and my legs are on fire."

        "My breath is coming in ragged gasps."

        "I can feel sweat pouring down my brow, and we've only just now rounded the second turn."

        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

        show emi basic_closedgrin_gym at offscreenleft
        with None

        show emi at left
        with charamovefaster

        emi "Come on, Hisao! You've got three more laps to go!"

        $ renpy.music.set_volume(0.5, 0.5, channel="ambient")

        show emi at offscreenleft
        with charamovefaster

        hide emi

        "I can't do this…"

        "I can't do this."

        "I can't do this!"

        "I think I might hurl."

        "Somehow we're on the second lap. Emi's not even sweating."

        "How can she do this so effortlessly?"

        "For some reason I'm still moving."

        "She's like a machine."

        "Third lap. What happened to the second?"

        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

        show emi excited_proud_gym at offscreenleft
        with None

        show emi at left
        with charamovefaster

        emi "Almost there, Hisao!"

        $ renpy.music.set_volume(0.5, 0.5, channel="ambient")

        show emi at offscreenleft
        with charamovefaster

        hide emi

        "Liar! We've got another two!"

        "Nothing to be done."

        hi "I… ca… can't… do… this."

        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

        show emi basic_annoyed_gym at offscreenleft
        with None

        show emi at center
        with charamovefaster

        "Emi whirls around and begins running backwards."

        "Her face is a mask of anger that surprises me."

        show emi sad_angry_gym
        with charachange

        emi "Never say that!"

        emi "If you say that, you'll have already lost."

        show emi at left
        with charamove

        emi "Keep moving! If you're alive, you can keep moving, dammit!"

        $ renpy.music.set_volume(0.5, 0.5, channel="ambient")

        show emi at offscreenleft
        with charamovefaster

        hide emi

        "Whoa, language. We're on the fourth lap now."

        "She really seems to want me to keep going."

        "Legs move. Move. Move. They feel so sluggish."

        "I'm in mud, or molasses, or tar."

        "I can't go on."

        "I'll go on."

        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

        show emi basic_grin_gym at offscreenleft
        with None

        show emi at left
        with charamovefaster

        emi "Final stretch, Hisao! Give it all you've got!"

        $ renpy.music.set_volume(0.5, 0.5, channel="ambient")

        show emi at offscreenleft
        with charamovefaster

        hide emi

        "I pump my legs as fast as they'll go."

        "They keep refusing to obey my commands."

        "Somehow, I keep moving."

        "Somehow, I finish."

        stop ambient fadeout 0.5

        show emi excited_happy_gym at center
        with charaenter

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")

        emi "That's it, Hisao! I knew you had it in you!"

        "The anger Emi showed a lap ago is gone, replaced with pride."

        "She's positively radiant, like she just won the gold medal or something."

        scene bg school_track_on
        show emi excited_happy_gym at center
        with vpunch

        "I stagger to a stop and fall to my hands and knees, gasping for air."

        "My heart is pounding far harder than it has in a long time."

        stop music fadeout 1.0

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.2)

        "I don't think it's done this since…"

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.2)

        "Oh God."

        scene black
        with shuteyefast

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.2)

        "Please slow down, heart."

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.5)

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.2)

        "Just slow down. Stop racing."

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.5)

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.2)

        "I cough, and for some reason, feel a grin crossing my face."

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.5)

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.2)

        "So this is how I die, huh?"

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.5)

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.2)

        "Trying to stay healthy?"

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.5)

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.2)

        "How ironic."

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.5)

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.5)

        play sound sfx_heartfast
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.2)

        "I'm all ready to give up right there."

        play sound sfx_heartslow
        show heartattack
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.8)

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.8)

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack
        with Dissolve (0.2)

        "But then, I feel my heart slow down."

        "Two hands grab under my arms and tug upwards."

        scene bg school_track_on
        show emi basic_confused_gym_close at center
        with openeye

        "I look up and see Emi standing over me, with a mixture of delight and worry."

        emi "On your feet!"

        show emi sad_grin_gym_close
        with charachange

        emi "Come on, you'll never catch your breath that way."

        "Somehow, I manage to stand. I try to raise my arms above my head, but they feel like lead."

        "I start to walk around the track while Emi keeps close to me, like she's afraid I'll fall over or something."

        "She may not be far off."

        "I feel terrible, and say so."

        show emi basic_closedhappy_gym_close
        with charachange

        "Emi laughs."

        show emi basic_happy_gym_close
        with charachange

        emi "But you finished, didn't you?"

        show emi basic_grin_gym_close
        with charachange

        emi "You said you couldn't, but you did."

        emi "Isn't that worth it?"

        "I'm not sure, and I don't really have the breath to say so."

        "But that small grin I felt on my face earlier hasn't left."

        "So what if my heart's weak?"

        "I still survived this morning."

        "Maybe I'll survive tomorrow, too."

        scene bg school_track
        with shorttimeskip

        $ renpy.music.set_volume(0.3, 0.0, channel="ambient")

        play ambient sfx_emisprinting

        "As soon as it becomes apparent that I'm not going to suddenly keel over, Emi takes off on her sprints."

        "I don't know how the hell she can manage to sprint after running a mile, but I guess she's in much better shape than me."

        "Once again, as I walk around the track, I can't help watching Emi sprint."

        scene ev emi_run_face:
            zoom 1.0 xalign 0.5 yalign 0.5
            ease 10.0 zoom 1.055
        with locationchange

        "It's weird, but she's like a different person when she's pushing herself."

        "Last time I noticed her eyes, but this time it's her mouth that catches my attention."

        "She's not wearing her normal grin."

        "She's still smiling, but there's a tightness to it."

        "It's almost grim, like she's fighting a losing battle but doesn't care."

        "She seems to be running harder, like she did yesterday."

        "Sweat has started to pour down her face, but she keeps going."

        "Her mouth finally opens as she can no longer get enough air through her nose."

        "As she passes me once more, legs pumping, arms swinging in time, and her lips slightly parted…"

        "She looks beautiful."

        stop ambient fadeout 2.0

        scene bg school_track
        with shorttimeskip

        play music music_normal fadein 3.0
        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")

        "After we've both taken some laps around the track to cool down, Emi changes back to her usual self."

        "The transformation I saw in her is gone."

        show emi basic_happy_gym at center
        with charaenter

        emi "Not bad today, Hisao."

        "There's almost admiration in her voice."

        hi "What do you mean? I would have stopped if you hadn't yelled at me."

        show emi sad_shyblush_gym
        with charachange

        "Emi colors a little, seemingly embarrassed about her outburst."

        emi "Sorry about that, I just… can't stand to see people give up."

        emi "Especially about something like this."

        show emi sad_grin_gym
        with charachange

        emi "Saying 'I can't go on' is silly when you're obviously going on while you're saying it."

        emi "That's what this is all about."

        hi "What, saying silly things?"

        show emi basic_annoyed_gym
        with charachange

        "Emi sticks her tongue out at me."

        emi "Idiot. I mean showing that you're alive."

        "Showing I'm alive, huh? I didn't know it had to be so painful."

        "But it does feel pretty good, despite that."

        show emi excited_proud_gym
        with charachange

        emi "Besides, this is one of the hardest days."

        hi "What do you mean?"

        show emi basic_grin_gym
        with charachange

        emi "Whenever you start a workout, it's difficult the first day, really hard the second day, and then the third day is easier."

        emi "You'll still get days that are really hard, but they'll pop up less and less."

        hi "So this will eventually get really easy, huh?"

        show emi basic_closedhappy_gym
        with charachange

        emi "Yeah, of course."

        show emi basic_closedgrin_gym
        with charachange

        emi "But then you have to increase the difficulty, or you'll never get ahead."

        emi "You'll just get complacent, and you'll lose the sense of accomplishment."

        hi "So I'll have to run more than just four laps, huh?"

        show emi excited_proud_gym
        with charachange

        emi "Yep! But not for a while - you'll have to be careful, you know."

        "A thought strikes Emi, and her face lights up."

        show emi basic_closedhappy_gym
        with charachange

        emi "Got it!"

        hi "Got what?"

        show emi basic_happy_gym
        with charachange

        emi "You can come with me to see the nurse! That way you won't fall over dead or anything!"

        "How charming."

        hi "Um… when?"

        show emi basic_grin_gym
        with charachange

        emi "Right now, of course! You'll need a shower and everything, right? We don't have much time, then!"

        "Grabbing my hand, she's off, pulling me along with her."

        stop music fadeout 2.0

        if _in_replay:
            return

    label .an_apple_a_day:
        scene bg school_nurseoffice
        show nurse neutral at center
        with shorttimeskip

        nk "My goodness, but you're in a hurry today, aren't you, Emi?"

        play music music_nurse fadein 2.0

        "I have no idea how we got to the nurse's office so fast, but here we are."

        show nurse at twoleft
        show bg at bgleft
        with charamove

        show emi basic_grin_gym at tworight
        with charaenter

        "The nurse grins at Emi and seems to completely ignore me."

        show nurse grin
        with charachange

        nk "You've got plenty of time to take a shower and get to class, you know."

        show nurse concern
        with charachange

        nk "There's no need to run through the hallways like that. I could hear you coming a mile away!"

        "Somehow, it doesn't seem like he's actually scolding Emi at all."

        "It's like this is a sort of routine between the two of them."

        "Emi does a passable imitation of remorse."

        show emi excited_sad_gym
        with charachange

        emi "I'm sorry! I won't ever do it again!"

        show nurse grin
        show emi basic_closedhappy_gym
        with charachange

        "The nurse and Emi both laugh at some private joke."

        show emi basic_grin_gym
        show nurse neutral
        with charachange

        "Suddenly, it seems that he notices me."

        show nurse fabulous
        with charachange

        nk "Ah, hello Hisao."

        show nurse neutral
        with charachange

        nk "What brings you here?"

        hi "Well, I've been—{w=.3}{nw}"

        show emi basic_closedgrin_gym
        with charachange

        emi "Hisao's officially joined me on my morning runs."

        "I start to explain, but Emi cuts me off."

        show emi basic_happy_gym
        with charachange

        emi "I thought he might need to visit you so that he doesn't die or anything."

        show nurse fabulous
        with charachange

        "The nurse raises his eyebrows in mock horror."

        nk "Yes, that would certainly put me out of a job fast, wouldn't it?"

        show nurse neutral
        show emi basic_grin_gym
        with charachange

        nk "Well then Hisao, let's have a look at you."

        nk "Lift up your shirt, would you?"

        "I'm suddenly very conscious of the fact that Emi's in the room with me and blush in spite of myself."

        "The nurse seems to sense my discomfort, but it only seems to amuse him."

        show nurse grin
        with charachange

        nk "A bit shy, are we?"

        "He makes an apologetic bow to Emi."

        nk "Sorry Emi, I tried to get you a free show, but it doesn't seem to have worked."

        show emi basic_annoyed_gym
        with charachange

        "Emi stiffens slightly and fires a look of annoyance at him."

        emi "You're an asshole."

        show emi excited_proud_gym
        with charachange

        "Emi bows to me apologetically."

        emi "I'll wait outside, okay Hisao?"

        hide emi
        with charaexit

        show nurse at center
        show bg at center
        with charamove

        "I begin to stammer that it's not really a big deal, she doesn't have to leave, but she's already out the door, and the nurse is laughing as he watches her go."

        show nurse fabulous
        with charachange

        nk "Still got it! Ha!"

        hi "I don't follow."

        show nurse grin
        with charachange

        "He laughs again, like he's in on some joke that's over my head."

        nk "I can still get her flustered. It's a competition of sorts we've had going on for a while now."

        "That sounds incredibly sinister to me, and it seems as if the nurse realizes that too."

        show nurse concern
        with charachange

        nk "Er. That sounded a lot worse than it actually is, come to think of it."

        hi "I wasn't going to say anything…"

        nk "No no, you're right. I should fill you in so that you don't get the wrong idea."

        show nurse neutral
        with charachange

        nk "I'm actually relatively new here, you see. I got hired on the same year Emi started going here."

        nk "Before that, I worked with Emi during her initial rehab following her accident."

        "Hold on, what?"

        show nurse concern
        with charachange

        nk "We had to amputate her legs after a really nasty car wreck. It nearly killed her, and succeeded—"

        "He shuts up abruptly. I blink at receiving this unexpected piece of news."

        nk "Well, that's not my place to say. Anyway, we've known each other for quite a while."

        nk "So we have a slightly more familiar relationship than is strictly professional."

        "He seems embarrassed, like he's done something stupid."

        "I guess he's really worried about that. I wave a hand to let him know it's not a big deal."

        hi "Don't worry, sir. I promise I'm going to be discreet."

        "I had been wondering about what caused Emi to lose her legs, and that was one of the scenarios I thought of."

        "There were only so many ways that could have happened, but actually hearing about the facts… it's still a little shocking."

        show nurse neutral
        with charachange

        nk "Well, thanks. You're a good kid, Hisao."

        nk "I can see why Emi became friends with you."

        show nurse fabulous
        with charachange

        nk "She's quite indomitable, you know."

        hi "What do you mean?"

        nk "You didn't see her learning to walk. She'd go for so much longer than the others in the hospital. She refused to quit."

        nk "Normally it takes years to get to a point where you can even think about running again. Emi did it all in about a year."

        "He almost seems proud of her, like a father who watches his daughter win a competition or something."

        show nurse neutral
        with charachange

        nk "Hell, she'd probably have done it faster if not for the fact that we wouldn't let her."

        hi "Wouldn't let her? Why not?"

        show nurse concern
        with charachange

        stop music fadeout 4.0

        nk "Because she'd go for so long that her legs would start bleeding where they met her prosthetics."

        nk "It's a real concern - it's why she comes by every day after she runs."

        nk "To say nothing of the risk of infection if her legs get cut up and her prosthetics are dirty."

        show nurse neutral
        with charachange

        nk "But enough about that."

        show nurse fabulous
        with charachange

        play music music_nurse fadein 2.0

        nk "If we don't get you on your way soon, Emi will think we're up to something."

        "As he says this, he gives a wink and begins checking my heartbeat."

        "The stethoscope is way too cold."

        "He really should have heated it up or something before he used it."

        "After a few moments he leans back, satisfied."

        show nurse neutral
        with charachange

        nk "Well, you sound pretty good to me, Hisao. You didn't have any chest pains while you were running, did you?"

        hi "No, not really. I had some trouble catching my breath, though - and my heart was racing by the end, too."

        show nurse concern
        with charachange

        "The nurse frowns as I say this, but then shrugs."

        show nurse neutral
        with charachange

        nk "It's probably just because you're out of shape… but if you don't improve, then you should let me know, okay?"

        nk "Don't push yourself too much - and of course if you have any chest pains, come to me immediately, right?"

        "I put my shirt back on, and the nurse leans out of the doorway to call in Emi."

        show nurse at twoleft
        show bg at bgleft
        with charamove

        show emi basic_annoyed_gym at tworight
        with charaenter

        emi "What took you so long? Now I'm going to be late!"

        stop music fadeout 2.0

        show nurse fabulous
        with charachange

        "The nurse gives me a significant look."

        show nurse grin
        with charachange

        nk "I was just seducing Hisao, that's all."

        play music music_comedy fadein 0.5

        show emi sad_annoyed_gym
        with charachange

        emi "What!? Come on, what have I told you about seducing my friends?"

        "I'd expected Emi to be shocked by this, but instead she seems merely annoyed, scolding the nurse as if he were a child stealing cookies."

        "Meanwhile, I try hard not to blush at the nurse's innuendo."

        show nurse fabulous
        with charachange

        nk "I'll try not to do it again, though I fear young Hisao may be lost to the female gender forever!"

        stop music fadeout 0.5

        hi "Not freaking likely."

        pause 3.0

        play music music_comedy fadein 0.5

        show nurse grin
        show emi excited_laugh_gym
        with charachange

        "I didn't mean to say that out loud, but both the nurse and Emi regard me for a moment before bursting into laughter again."

        show emi basic_happy_gym
        with charachange

        emi "Told you he was funny, didn't I?"

        "Huh. I guess Emi does talk to the nurse about a lot of stuff."

        show nurse fabulous
        show emi basic_grin_gym
        with charachange

        nk "Well Hisao, you should probably get moving. You still need a shower before class starts, don't you?"

        "Crap! He's got a point, and it looks like I've only got a half hour!"

        hi "Thanks for your time. I'll see you later, Emi!"

        scene bg school_nursehall
        with locationchange

        stop music fadeout 5.0

        "I dash out of the room as the nurse begins to remove Emi's prosthetics."

        "As I head down the hallway, I can just barely hear his voice drifting after me."

        nk "Emi, you've got to be more careful…"

        scene bg school_dormhisao
        with locationskip

        "I make it back to my room and shower in record time. It occurs to me that I've already been up for four hours, and class hasn't even started yet."

        "This is going to be a really, really long day."

        "I hope I don't fall asleep in class."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .track_meeting:
        scene black

        show bg school_dormhisao
        with openeye

        play music music_pearly fadein 5.0

        "The morning sunlight streaming through my window wakes me up instead of my alarm, and I realize that it must be Sunday."

        "Emi has kindly deigned to give me weekends off from our morning runs."

        "I don't actually know if I woke up at all yesterday, or if I just slept through the entire day."

        "My legs groan in protest as I lever myself out of bed."

        "All this running has really taken it out of me."

        "Still, I can't deny that Emi wasn't lying to me."

        "It has gotten a little easier."

        "I'd been worried that the runs would start to wear on my nerves, but thus far I haven't minded them that much."

        "Well, it's only been a week."

        "I suppose there's plenty of time for me to start dreading the sound of my alarm in the morning."

        "Not that I could ever skip out now."

        "As Emi said, it's harder to stop a routine when there's another person."

        "And frankly, I don't think I'm equipped to deal with a disappointed Emi."

        "She'd probably give me those puppy-dog eyes and I'd feel terrible about myself."

        "Which reminds me… wasn't I supposed to be somewhere today?"

        $ renpy.music.set_volume(0.3,2.0,channel="music")

        scene bg school_track_fb
        show emi basic_closedhappy_gym_fb at center
        show noiseoverlay
        with flashback

        emi "Hey, you're coming to my track meet on Sunday, right?"

        show emi basic_grin_gym_fb
        with charachange

        emi "What am I talking about, of course you are."

        show emi sad_grin_gym_fb
        with charachange

        emi "Right?"

        "Those puppy-dog eyes again."

        hi "Of course I'm going!"

        hi "I owe you, right?"

        show emi excited_proud_gym_fb
        with charachange

        emi "Exactly! So don't forget, okay?"

        $ renpy.music.set_volume(1.0,2.0,channel="music")

        scene bg school_dormhisao
        with flashback

        "Crap, Emi's track meet!"

        "I'd better get a move on if I don't want to miss her running, since she's the only reason I'm even considering going."

        "Otherwise, it would defeat the whole purpose of going."

        scene bg school_courtyard
        show crowd
        with shorttimeskip

        play ambient sfx_crowd_outdoors fadein 3.0

        "And so, I soon find myself quite suddenly surrounded by a crowd of people, all turning out to see our track team compete with another school like this one."

        $ renpy.music.set_volume(0.5, 1.0, channel="ambient")
        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear

        nvl show dissolve

        n "{vspace=30}I'll admit it, it's almost comforting to know we're not the only school like this."

        n "After you see that there can be {b}two{/b} schools with a bunch of… defective kids, well."

        n "…You stop feeling so defective."

        n "You also stop feeling unique, which in most cases would be a bad thing, but in this case it sure as hell isn't."

        n "That's part of Yamaku's appeal, I guess."

        n "Learn that you're not unique - hell, learn there's a lot of others who would kill to be saddled with your problem instead of whatever they're dealing with."

        n "Some of the kids here aren't here because they're missing a leg or they have a heart condition."

        n "Some of them might be here because they're as good as dead in two, maybe three years if they're lucky."

        n "And that's only if they get the right sort of care."

        n "It's a bitter sort of comfort to be able to say 'Well, at least I've got a chance of being alive through college,' but there it is."

        $ renpy.music.set_volume(1.0, 2.0, channel="ambient")
        $ renpy.music.set_volume(1.0, 2.0, channel="music")

        nvl clear

        nvl hide dissolve

        stop music fadeout 3.0

        "I'm brought out of my rather morbid musings by the appearance of Rin near the entrance to the bleachers."

        show rin basic_deadpannormal at center
        with charaenter

        rin "You came."

        hi "Of course. I said I would, didn't I?"

        show rin basic_deadpanamused
        with charachange

        rin "That doesn't necessarily imply that you had to follow through."

        show rin basic_awayabsent
        with charachange

        rin "Lots of people say things and don't mean them."

        hi "Well, I don't."

        play music music_soothing fadein 0.5

        show rin relaxed_boredom
        with charachange

        "Rin shrugs. Seemingly bored with our conversation, she turns on her heel and heads back toward the stands."

        rin "I owe Emi money now."

        hi "Why's that?"

        show rin basic_absent
        with charachange

        rin "I didn't think you'd show up."

        rin "Emi did."

        show rin basic_awayabsent
        with charachange

        rin "So I owe her 500 yen."

        hi "You two bet an awful lot, don't you?"

        "Another shrug from my armless companion."

        show rin basic_deadpan
        with charachange

        rin "I don't think so."

        scene bg school_track
        show crowd
        show rin basic_deadpan at center
        with locationchange

        "We enter the bleachers, and Rin nods upwards."

        show rin negative_spaciness
        with charaenter

        rin "Up there."

        show rin basic_deadpancontemplation
        with charachange

        rin "I came out to see if you'd come."

        "For the bet, I presume."

        "Rin leads the way, and soon we've settled down on an almost-empty bench."

        $ renpy.music.set_volume(0.3, 3.0, channel="ambient")

        show crowd:
            linear 1.0 alpha 0.0
        with None

        show rin at tworight
        show bg at bgright
        with charamove

        hide crowd
        show meiko smile at twoleft
        with charaenter

        "There's an older woman sitting next to Rin - someone's mother, I assume."

        "She's got rather long hair done up in a braid. On seeing Rin, she gives her an oddly familiar-seeming grin."

        show meiko happy
        with charachange

        emm_ "Well, this is surprising."

        show meiko wink
        with charachange

        emm_ "I thought you went to get a snack, not a boy."

        hi "Huh?"

        show rin basic_surprised
        with charachange

        rin "A snack?"

        show rin relaxed_nonchalant
        with charachange

        rin "I wondered why I was down there."

        show meiko happy
        show rin basic_awayabsent
        with charachange

        "The woman laughs, again in a way that seems familiar."

        "Where have I seen her before?"

        show meiko smile
        with charachange

        emm_ "Well, I suppose you've always been one to go out for one thing and bring back another."

        emm_ "But I'm being rude! I haven't introduced myself."

        emm_ "I'm Meiko Ibarazaki, Emi's mother."

        show meiko happy
        with charachange

        emm "Pleased to meet you."

        "Well, that explains it."

        "She's like a taller, older and better endowed Emi."

        "Apart from her hair being a darker shade than Emi's, there's really no mistaking the resemblance."

        show rin basic_absent
        show meiko smile
        with charachange

        hi "Sorry, I'm Hisao. Hisao Nakai."

        hi "And really, you don't have to apologize for not introducing yourself, Mrs. Ibarazaki."

        hi "That's really Rin's job in this situation, isn't it?"

        show meiko happy
        show rin basic_awayabsent
        with charachange

        "Another laugh from Emi's mother."

        emm "I take it you've not known Rin for that long, then."

        show meiko smile
        with charachange

        emm "It's best not to expect her to remember something like that."

        show meiko wink
        with charachange

        emm "She's got other things to think about, I assume."

        show rin basic_deadpannormal
        with charachange

        "Rin nods, seeming pleased by this assessment."

        show rin basic_deadpan
        with charachange

        rin "She's right."

        show rin basic_lucid
        with charachange

        rin "I was thinking about sunsets."

        show meiko happy
        show rin basic_awayabsent
        with charachange

        emm "You see? It's really up to us to make introductions and the like."

        "For lack of any better response, I nod."

        "Mrs. Ibarazaki leans back a little on her seat and raises an eyebrow."

        $ renpy.music.set_volume(0.0, 0.5, channel="ambient")

        show meiko serious
        with charachange

        stop music fadeout 0.8

        emm "So, how long have you and Rin been dating?"

        "My response consists of silence as my brain suddenly lurches into gear. But just before I can begin to utter a hastily babbled explanation, Emi's mother bursts into laughter again."

        play music music_soothing fadein 0.5
        $ renpy.music.set_volume(0.3, 0.5, channel="ambient")

        show meiko happy
        with charachange

        emm "Ha! You're a blusher, aren't you?"

        "I don't know if there's any way to keep my dignity in this situation, so I settle for a mumbled response."

        show meiko smile
        show rin basic_absent
        with charachange

        hi "Maybe."

        show rin basic_awayabsent
        with charachange

        emm "So this must be a new romance then, mustn't it?"

        show rin basic_absent
        with charachange

        hi "Wait, that's not the question that—"

        show meiko happy
        show rin basic_awayabsent
        with charachange

        "Another laugh."

        show meiko smile
        with charachange

        emm "I know, but it's funny to watch you squirm."

        show meiko wink
        with charachange

        emm "I'm sorry. Forgive an old woman her amusements."

        "Old woman?"

        "She sure doesn't look that old to me."

        "Clearly Emi gets her youthful features from her mother."

        show rin basic_absent
        with charachange

        hi "I suppose I can let it go."

        show meiko happy
        show rin basic_awayabsent
        with charachange

        emm "How kind of you."

        stop music fadeout 6.0

        show rin basic_deadpan
        with charachange

        rin "It's starting."

        stop ambient fadeout 2.0

        scene ev emitrack_blocks:
            xalign 1.0
            easein 12.0 xalign 0.0
        with locationskip

        "I direct my attention to the track, where they're preparing for the first sprint."

        "It looks like the 400 meter dash."

        "My eyes scan the runners, before finding Emi."

        scene ev emitrack_blocks_close
        with flash

        "She's smiling, with an almost cocky look on her face."

        show insert startpistol at offscreenright
        with None

        show insert at right
        with charamovefaster

        "The starter raises his pistol."

        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")

        play sound sfx_startpistol
        play ambient sfx_emisprinting

        scene ev emitrack_running:
            xalign 1.0
            easein 1.0 xalign 0.0
        with silentflash

        "Emi explodes off the block, disappearing from the starting line in a blur."

        "It's amazing. Even as the other sprinters converge on the lanes closest to the inside line, Emi surges to the front of the pack."

        "By the time she rounds the final turn, some of the other runners have caught up with her."

        "Their efforts come to naught though, since a final burst of speed from Emi leaves them at least a half second behind."

        scene ev emitrack_finishtop:
            xalign 0.5 yalign 0.0 zoom 4.0
            0.2
            linear 0.3 zoom 1.05
            easein 8.0 zoom 1.0
        with flash

        stop ambient fadeout 1.0
        play sound sfx_crowd_cheer

        "Mrs. Ibarazaki whoops and shouts, applauding wildly, and generally looking like any other parent cheering on their child."

        "Emi bounds off the track, looking pleased with herself."

        scene bg school_track at bgright
        show meiko happy at twoleft
        show rin basic_deadpandelight at tworight
        with locationchange

        play music music_daily fadein 2.0

        "I cheer right along with the rest of them."

        "The announcer (sounding suspiciously like Misha) gleefully gives the results."

        show meiko smile
        show rin basic_awayabsent
        with charachange

        emm "I think she's gotten faster since the last time."

        show rin basic_absent
        with charachange

        hi "That was incredible."

        show meiko happy
        show rin basic_awayabsent
        with charachange

        "Mrs. Ibarazaki grins proudly."

        emm "Emi's a heck of a runner."

        show meiko smile
        with charachange

        "We fall silent as the next event is being prepared."

        "I'm surprised to see Emi striding out onto the track again."

        show rin basic_absent
        with charachange

        hi "Wait, didn't she just run?"

        "Emi's mother nods."

        show rin basic_awayabsent
        with charachange

        emm "Yes, but she runs multiple events for the team. Especially the sprints."

        show meiko happy
        with charachange

        emm "It's a lot of running, but Emi can handle it."

        "From the looks of things, she's right."

        "Emi doesn't appear to be tired, as if she hadn't run the previous event at all."

        "If not for the sweat visible on her shirt, you'd never know."

        show rin basic_absent
        with charachange

        hi "Which event is this?"

        show meiko smile
        show rin basic_awayabsent
        with charachange

        emm "It's the 200 meter dash."

        emm "She'll do this one, the 100-meter, and the relay."

        show rin basic_absent
        with charachange

        hi "I see."

        show rin negative_spaciness
        with charachange

        play sound sfx_startpistol
        play ambient sfx_emisprinting

        "Once again the pistol sounds, and once again Emi flies off the block."

        "A thumping sound draws my attention away from the race."

        "It's Rin's foot."

        "She seems completely absorbed in the race."

        show meiko happy
        with charachange

        stop ambient fadeout 1.0
        play sound sfx_crowd_cheer

        "Emi's mother cheers again, and I assume that the race is over."

        "Sprints don't seem to me like they'd take very long to complete."

        hi "Your foot."

        show rin relaxed_surprised
        show meiko smile
        with charachange

        rin "Hmm?"

        hi "Your foot was bouncing on the bleachers."

        show rin basic_deadpan
        with charachange

        rin "Oh."

        hi "You seem pretty into this stuff. I'm surprised."

        show rin basic_deadpansurprised
        with charachange

        "Rin looks at me quizzically."

        rin "Why wouldn't I be?"

        hi "No reason, I just thought stuff like sports wouldn't interest you."

        show rin relaxed_nonchalant
        with charachange

        rin "Hmm, I suppose you're right."

        rin "It's not that interesting."

        show rin basic_deadpannormal
        with charachange

        rin "But I'm watching Emi, not the sport."

        hi "I don't follow."

        show rin basic_lucid
        with charachange

        rin "Emi's the most Emi when she runs."

        rin "You don't get to see Emi at her Emiest very often."

        show rin basic_deadpanamused
        with charachange

        rin "But here, you can. See?"

        "She directs my attention toward the track again, where the 100-meter dash is about to start."

        stop music fadeout 6.0
        stop sound fadeout 2.0

        scene ev emitrack_blocks_close
        with locationskip

        "I watch Emi closely."

        "As she gets onto the starter blocks, her whole body seems to relax, but it's a false relaxation."

        "I can see that she's actually like a coiled spring."

        scene ev emitrack_blocks_close_grin
        with charachangeev

        "As the starter tells everyone to get set, her head snaps up, and her eyes narrow slightly."

        "Her mouth curls upward in what could be a grin and could be a growl."

        play sound sfx_startpistol
        play ambient sfx_emisprinting

        scene ev emi_run_face:
            zoom 1.0 xalign 0.5 yalign 0.5
            ease 10.0 zoom 1.055
        with locationskip

        "When the pistol goes off, it's as if she's been unleashed from a cage, like she was always moving at this blinding speed, but we couldn't see it happening until the starter's pistol dispelled the illusion of motionlessness."

        "It's all over in a few seconds, but in those few seconds I feel like I just witnessed something very personal for Emi."

        stop ambient fadeout 1.0
        play sound sfx_crowd_cheer

        "As soon as she crossed the finish line, the fierce look was replaced by her normal grin."

        "The conquering general returning to his farm."

        hi "Amazing."

        hi "She's really amazing. I've never seen anyone move that fast."

        scene bg school_track at bgright
        show meiko smile at twoleft
        show rin basic_deadpanamused at tworight
        with locationchange

        emm "Well, don't look at me, I'm far too relaxed to run that fast."

        show meiko worry
        show rin basic_awayabsent
        with charachange

        emm "No, I think Emi's prowess all came from her father's side."

        "At the mention of Emi's father, Mrs. Ibarazaki looks wistful, almost sad."

        emm "He got her into running, you know."

        show rin basic_absent
        with charachange

        hi "Yeah, she told me."

        "I'm uncertain as to whether or not it would be rude of me to ask after Emi's father."

        "But after that look on her face a few days ago, I feel compelled to ask."

        hi "Where is her father now, if I might ask?"

        "Emi's mother hesitates, clearly not willing to answer the question but at the same time not wishing to appear rude."

        show meiko serious
        show rin basic_awayabsent
        with charachange

        emm "He… isn't around any more."

        hi "I'm sorry, I didn't mean to bring up bad memories."

        show rin basic_absent
        with charachange

        hi "Emi just seemed a little sad when she mentioned him earlier."

        show meiko worry
        show rin basic_awayabsent
        with charachange

        emm "That's not surprising, considering."

        hi "Hmm?"

        emm "They were very close."

        show rin basic_absent
        with charachange

        hi "I see."

        play sound sfx_cellphone

        "A beeping noise suddenly emanates from Mrs. Ibarazaki's pocket. Reaching into it, she pulls out a cell phone and looks at it."

        show meiko serious
        show rin basic_awayabsent
        with charachange

        emm "…Honestly, text messages?"

        emm "What is he, sixteen?"

        hi "Hmm?"

        show meiko smile
        with charachange

        emm "Oh, nothing."

        show meiko wink
        with charachange

        emm "I've got to go meet up with a friend of mine."

        show meiko happy
        with charachange

        emm "Will you tell Emi I'm very proud of her and that I'll call her later tonight?"

        show rin basic_absent
        with charachange

        hi "Of course."

        hide meiko
        with charaexit

        show rin at center
        show bg at center
        with charamove

        show rin basic_awayabsent
        with shorttimeskip

        play music music_tranquil fadein 2.0

        "I'll admit that I zone out for a while."

        "I almost don't notice that the relay's about to begin. But when I look, I can't find Emi."

        hi "I thought that Emi would be running the relay."

        show rin basic_deadpan
        with charachange

        rin "She runs anchor."

        show rin basic_deadpannormal
        with charachange

        rin "So she won't be running for a while yet."

        hi "Ah."

        show rin basic_deadpandelight
        with charachange

        rin "Did you see it?"

        hi "Huh?"

        rin "Emi at her Emiest."

        hi "Maybe."

        show rin basic_deadpanupset
        with charachange

        rin "Hmm. Maybe this time."

        play sound sfx_startpistol

        "The race begins, and I cheer Emi's teammates along as they pass the baton."

        play ambient sfx_emisprinting

        scene ev emitrack_running:
            zoom 1.0 truecenter
            ease 20.0 zoom 1.05 xalign 0.0 yalign 0.0
        with locationskip

        "Finally, I see Emi sprinting onto the track to take the final handoff."

        "Once again I'm taken aback by how graceful she looks when she runs."

        "It really is beautiful."

        "The look of determination and fearlessness on her face only adds to the picture."

        "Emi at her Emiest, I suppose."

        stop ambient fadeout 1.0
        play sound sfx_crowd_cheer

        show ev emitrack_finish
        with locationskip

        "But then, as she crosses the finish line, I see her stumble slightly."

        "It's only barely, but it's a definite stumble."

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")

        scene bg school_track
        show rin negative_worried at center
        with locationskip

        "Rin inhales sharply, and actually looks concerned for a second."

        rin "Aw, Emi…"

        hi "Did she hurt herself, do you think?"

        show rin basic_surprised
        with charachange

        rin "You noticed it too?"

        show rin negative_confused
        with charachange

        rin "It must be bad."

        show rin negative_annoyed
        with charachange

        "She frowns, as if deciding on the next course of action."

        "Eventually that proves to be too tiresome, and she shrugs again."

        show rin basic_deadpanupset
        with charachange

        rin "Well, let's go down."

        rin "Gotta crown the victor."

        show rin basic_deadpanamused
        with charachange

        rin "See if you can find a laurel branch."

        hi "That's not going to be easy."

        show rin basic_deadpannormal
        with charachange

        "Rin shrugs."

        show rin basic_deadpan
        with charachange

        rin "At least we tried."

        "Well, we didn't really try all that hard."

        "Or at all. But hey, whatever."

        stop music fadeout 5.0
        stop sound fadeout 5.0
        play ambient sfx_crowd_outdoors fadein 2.0

        scene bg school_track_on
        show crowd
        show rin basic_awayabsent at center
        with locationskip

        "Emi is surrounded by her teammates, all of them congratulating her on the run."

        "Rin seems to be waiting for Emi to notice that she's arrived."

        "Oh yeah, I guess she can't exactly wave Emi over."

        "Then again, I'm not sure that Rin would do such a thing even if she had arms."

        "It doesn't seem her style to draw attention to herself. Or to emote beyond shrugging."

        "Either way, I'm not willing to wait, so I wave to Emi, who looks up and grins happily at me - er, us."

        show bg at bgright
        show crowd at bgright
        show rin at tworight
        with charamove

        play music music_emi fadein 1.0

        show emi basic_closedhappy_gym at twoleft
        with charaenter

        emi "Hey, you showed up!"

        show emi excited_proud_gym
        with charachange

        emi "Guess Rin owes me money, huh?"

        show rin basic_deadpanupset
        with charachange

        rin "We would have brought you a crown of laurels, but Hisao didn't find one."

        show emi basic_grin_gym
        with charachange

        hi "Hey, neither did you."

        show rin basic_deadpan
        with charachange

        rin "It wasn't my job to look."

        hi "When did we assign jobs?"

        show rin basic_deadpannormal
        with charachange

        rin "When I said 'See if you can find a laurel branch.'"

        show rin basic_deadpandelight
        with charachange

        rin "Try to keep up."

        "I shrug. Guess Rin's rubbing off on me."

        hi "Seems it's my fault after all, Emi."

        show emi basic_closedhappy_gym
        show rin basic_awayabsent
        with charachange

        "Emi laughs at Rin and me."

        show emi basic_happy_gym
        with charachange

        emi "It's okay, I'm sure you'll make it up to me somehow."

        show rin basic_absent
        with charachange

        hi "Uh, sure."

        show rin basic_awayabsent
        show emi excited_amused_gym
        with charachange

        emi "Good! So, how'd I look?"

        show rin basic_absent
        with charachange

        "I stop myself from blurting out 'beautiful' or 'amazing' and settle for the substantially safer 'very impressive.'"

        show emi basic_closedgrin_gym
        with charachange

        "Emi seems pleased with this assessment."

        "I don't mention how much more impressive her performance is given her lack of legs. I figure she knows that already."

        "Besides, it seems like it would take away from her efforts, somehow."

        show emi basic_grin_gym
        show rin basic_awayabsent
        with charachange

        emi "Great to hear! I was worried that I looked a little slow on the relay, but I guess I did fine, huh?"

        show rin basic_absent
        with charachange

        hi "Actually, I noticed—{w=.4}{nw}"

        play sound sfx_impact

        show rin basic_deadpanupset
        with vpunch

        "Rin kicks me and keeps me from finishing my sentence."

        show emi basic_confused_gym
        with charachange

        emi "What was that all about?"

        show rin basic_deadpancontemplation
        with charachange

        rin "He noticed it. At the end."

        show emi basic_annoyed_gym
        with charachange

        emi "Hmm, that's no good."

        show emi sad_grin_gym
        with charachange

        emi "Guess the nurse will look at it for me later."

        show emi sad_grit_gym
        with Dissolve(0.2)

        show emi sad_grin_gym
        with charachangealways

        "There's a carelessness in her voice, as if it isn't a big deal, but I suddenly notice a slight twitch on her face."

        "Like she's trying to hide the fact that she's in pain."

        "It's then that I notice her breathing is a little shallow, too."

        "I guess she really is hurt."

        "She must notice my concern, because she skips up to me and gives me a friendly pat on the shoulder."

        show emi basic_closedgrin_gym_close
        show rin basic_deadpannormal
        with characlose

        emi "Hey, you look a little worried!"

        show emi basic_grin_gym_close
        with charachange

        emi "I'm fine, really!"

        emi "Just sore from all the running, is all."

        show emi excited_proud_gym_close
        with charachange

        emi "And come on, a little pain isn't going to stop me."

        hi "Oh no?"

        show emi basic_closedgrin_gym_close
        with charachange

        "Emi grins, and for a moment she looks like she did during her sprint, fierce and unconquerable."

        "Or to put it another way, really beautiful."

        show emi basic_grin_gym_close
        with charachange

        emi "Hasn't yet."

        hi "Well then. I guess I shouldn't worry, huh?"

        show emi basic_closedhappy_gym_close
        with charachange

        emi "Damn right! I'm Emi Ibarazaki, fastest thing on no legs! I don't stop for anything!"

        hi "Impressive."

        show emi basic_closedgrin_gym_close
        with charachange

        "Emi giggles, and then seems to remember something."

        show emi basic_grin_gym_close
        with charachange

        emi "Oh, before I forget…"

        emi "Rin and I are going to do something next Sunday as a post-track meet celebration!"

        show emi excited_proud_gym_close
        with charachange

        emi "You should come along!"

        show emi sad_grin_gym_close
        with charachange

        emi "Normally we do it the day after, but since the track meet was on a Sunday, I've got homework and class and all that stuff to take care of."

        show emi basic_closedgrin_gym_close
        with charachange

        emi "Plus our morning run, of course."

        hi "Right, of course."

        hi "Oh, right. Your mom wanted to say she's proud of you."

        hi "She'll call you later tonight."

        show emi basic_happy_gym_close
        with charachange

        emi "I thought I saw her in the stands!"

        show emi basic_closedhappy_gym_close
        with charachange

        emi "I'm glad she made it!"

        show emi sad_grin_gym_close
        with charachange

        emi "Used to be my dad who showed up to my meets, but Mom's done a pretty good job of taking over."

        show emi sad_shy_gym_close:
            function partial(tremble_general, 1.0, 0.3, 1.0, 0.5, 1.0)
        with Dissolve(0.1)

        "She shivers slightly, and I realize that she's still all sweaty."

        "A breeze has started to blow, too."

        "I'm not cold at all, and I've got my jacket with me, so without a word I throw it around her shoulders."

        play sound sfx_rustling

        show emi basic_shock_gym_close at twoleft
        with vpunch

        pause 0.5

        show emi basic_grin_gym_close
        with charachange

        "Emi jumps slightly and then grins at me."

        show emi basic_closedhappy_gym_close
        with charachange

        emi "Hey, thanks!"

        show emi sad_grin_gym_close
        with charachange

        emi "It's getting a little cold, I guess."

        hi "Yeah, looked like it."

        "Just as I begin to wonder whether or not giving Emi my jacket could be taken the wrong way, a boy in a track uniform approaches."

        "Teammate" "Hey, Emi! You're going to miss the medal ceremony!"

        show emi basic_closedgrin_gym_close
        with charachange

        emi "Oh yeah, thanks!"

        show emi basic_grin_gym
        show rin basic_awayabsent
        with charadistant

        "She turns to Rin and myself."

        emi "You don't have to stick around for this part. It takes forever."

        show emi basic_closedgrin_gym
        with charachange

        emi "Besides, you should get cracking on your homework now if you don't want to be up late, Hisao."

        show emi excited_proud_gym
        with charachange

        emi "Morning run tomorrow! Don't forget!"

        show rin basic_absent
        with charachange

        hi "How could I?"

        show emi basic_closedhappy_gym
        show rin basic_awayabsent
        with charachange

        emi "Good point. I mean, it's spending time with {b}me{/b}, after all."

        play sound sfx_emirunning

        show emi at offscreenleft
        with charamovefaster

        hide emi

        stop sound fadeout 3.0

        show bg at center
        show crowd at center
        show rin at center
        with charamove

        "With this, she waves quickly and dashes off to receive her medals, or whatever they pass off as a medal these days."

        scene bg school_courtyard
        show crowd
        show rin relaxed_nonchalant at center
        with locationskip

        stop music fadeout 7.0

        "Rin and I head away from the track, Rin remaining deep in whatever thoughts she has for most of the walk back to her dorm."

        "As I see her off, she speaks up."

        show rin basic_deadpan
        with charachange

        rin "You're probably not getting that coat back, I think."

        hi "I'm sure I'll get it back eventually."

        show rin basic_deadpannormal
        with charachange

        rin "Interesting. Take it as it comes, huh?"

        show rin basic_deadpandelight
        with charachange

        rin "Very Emi-ish."

        hide rin
        with charaexit

        "With this odd statement, she turns and heads into the building."

        "Honestly, was it that big a deal?"

        "Emi was cold and, unless I'm mistaken, in pain."

        "Giving her a solution to at least one of those problems seems like an obvious reaction."

        "Though I guess there is a chance I could lose my jacket if Emi never remembers to return it."

        "I guess Rin has a point."

        "Still, I can't bring myself to muster much worry over the whole thing."

        "After all, it's been getting warmer lately."

        "I don't need a jacket."

        "Odd. I think I used to be a little more responsible with my stuff."

        "'Emi-ish,' huh?"

        "Maybe that's not really a bad thing."

        stop ambient fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .down_that_medicine_now:
        scene bg school_nurseoffice
        show nurse concern at center
        with locationchange

        nk "You haven't been forgetting to take your medicine, have you?"

        play music music_nurse fadein 0.5

        nk "I'm catching a little murmur."

        nk "You should take it easy for a few days."

        "The nurse's words hurt me far more than the exhaustion of the morning run ever could."

        "Take it easy for a few days?"

        "I knew I should have kept quiet."

        "I keep my eyes on the floor, feeling like a complete idiot."

        "Of course I hadn't been remembering to take my medicine."

        "I've been rushing out of my room to get to the track before Emi."

        "After the track meet a few days ago, I felt… inspired."

        "So I've been running warm-up laps in the morning before Emi shows up."

        "But then today while she and I were running, I felt a little pain in my chest."

        "It was only slight, and it was only for a second, so I mentioned it to the nurse."

        hi "Honestly, it wasn't that bad."

        hi "I mean I kept running and finished just fine, so really it couldn't have been that bad…"

        "Why do I feel like I'm making excuses to the nurse?"

        "Moreover, why do I feel a need to justify continuing to run despite the pain?"

        "Really, it comes down to my being unwilling to concern Emi, who seemed concerned anyway."

        "I'm not sure how she was able to tell there was anything wrong, but she claims I stumbled a little."

        "She's the one who insisted I tell the nurse, so now I feel bad for worrying her at all."

        "The nurse is shaking his head ruefully while Emi paces outside the room."

        nk "Hisao, I know it's difficult for you get into a new routine, but if you don't want to find yourself in a lot of trouble you're going to have to try harder."

        nk "You can't afford to forget your pills, and you can't push yourself too hard."

        hi "But if I don't push myself, how will I improve?"

        "I don't know where that came from."

        "The nurse seems to have an idea."

        show nurse fabulous
        with charachange

        nk "Now where have I heard that before?"

        show nurse grin
        with charachange

        "He laughs and pats me on the shoulder."

        nk "Ha! She's rubbing off on you, I guess."

        show nurse concern
        with charachange

        "His expression changes again, and he's back in serious mode."

        nk "Look, I'm not saying you shouldn't push yourself."

        nk "But that doesn't mean you shouldn't be taking your medication, and it doesn't mean you shouldn't stop if your chest starts to bother you."

        nk "I'd prefer not to have any fatalities while I'm on staff here."

        show nurse neutral
        with charachange

        nk "A bit of a lofty goal, to be sure, but I'm always up for a challenge."

        "I hate to admit it, but I think he's right."

        "I've got to remember to take my medication."

        hi "You're right. I'm sorry to worry you."

        show nurse fabulous
        with charachange

        nk "Who's worried? You're a smart kid, right?"

        show nurse neutral
        with charachange

        nk "I know you can be responsible, Hisao. A situation like yours, you've got to learn to be responsible fast."

        hi "I know, I know."

        "His expression suddenly becomes devious."

        show nurse fabulous
        with charachange

        nk "I suppose you've started to enjoy your runs with Emi then, eh?"

        hi "Yeah, they've really been helping me."

        hi "I mean, until today I was feeling a lot more healthy."

        hi "Plus it's really impressive to see Emi run. Did you see her at the track meet?"

        hi "She was incredible!"

        show nurse grin
        with charachange

        "The nurse nods, grinning all the while."

        nk "That she was, Hisao. I watched her first couple of races before I had some business to take care of, but she told me all about it."

        show nurse fabulous
        with charachange

        nk "Kind of you to loan her your jacket, by the way."

        hi "Huh? Oh yeah, it wasn't that big of a deal."

        "I had honestly forgotten all about that. I still haven't gotten it back."

        show nurse neutral
        with charachange

        "The nurse gets a smile that makes me feel like he's just made a joke."

        nk "Not to you, but Emi certainly appreciated it."

        nk "And I know she appreciates your running with her in the mornings."

        "This one catches me off guard a little. Sure, she mentioned that it's easier to keep to a schedule with an extra person, but I didn't think that I was doing her a favor at all."

        hi "I thought she was doing me the favor of helping me follow the doctor's orders."

        nk "She tries harder when you're around."

        nk "If there's someone else running with her, she's going to push herself more."

        nk "And she tries even harder when you're around because, well, it's you."

        hi "What the heck does that mean?"

        show nurse grin
        with charachange

        nk "Oh ho, you'd love to know, wouldn't you?"

        "He laughs in the style of evil megalomaniacs."

        show nurse neutral
        with charachange

        nk "No seriously, it's because you're her friend."

        nk "If Rin ran with her, I'm sure she'd do the same."

        nk "Well, probably."

        nk "But that's not the point."

        nk "The point is, you're helping her, even if you don't know you are."

        show nurse fabulous
        with charachange

        nk "And she's grateful for that, even if she never says it."

        hi "What do you mean 'even if she never says it?'"

        show nurse neutral
        with charachange

        nk "Emi doesn't talk a lot, but she and I have known each other long enough that I can read her most of the time."

        "I'll admit it. I have no idea what he's talking about."

        "Emi always seems pretty talkative to me."

        hi "I see."

        "The nurse suddenly realizes that he's been rambling and stops talking, looking a little embarrassed."

        show nurse fabulous
        with charachange

        nk "Anyway, you don't have to stop your morning exercise."

        show nurse neutral
        with charachange

        nk "Just walk the track instead of running for a few days. Let things calm down."

        show nurse concern
        with charachange

        nk "And take your damned medicine!"

        scene bg school_nursehall
        with locationchange

        stop music fadeout 0.3
        play sound sfx_impact

        show emi basic_confused_gym_close at center
        with vpunch

        "I laugh as I exit the office, bumping straight into Emi."

        show emi basic_confused_gym
        with charadistant

        hi "Whoops, sorry about that."

        show emi basic_hes_gym
        with charachange

        emi "Are you okay? What did the nurse say?"

        emi "Do you need to go to a hospital?"

        show emi basic_shock_gym
        with charachange

        emi "Omigosh, it was my fault, wasn't it?"

        show emi basic_closedsweat_gym
        with charachange

        emi "I've been pushing you too hard, haven't I?"

        show emi excited_sad_gym
        with charachange

        emi "I'm a horrible person!"

        "The words pour forth like a torrent. She's really agitated."

        "I didn't expect her to be this concerned about me, to be honest."

        "Gotta calm her down… but how the hell do I do that?"

        "I do the only thing I can think of."

        show emi basic_shock_gym_close
        with characlose

        play music music_serene fadein 6.0

        "I give her a hug. Emi tenses up slightly, so I pat her head in what I hope is a reassuring manner."

        hi "Hey, settle down!"

        hi "I'm fine, okay? No worries."

        show emi basic_hes_gym_close
        with charachange

        "I can feel Emi's body relax as I continue to assure her I'm fine."

        "Her arms wrap around me, as if she's trying to confirm that I'm not about to fall over dead."

        "I catch a whiff of her hair. It smells like sweat, or how adrenaline should smell. It's the scent of activity."

        "And a hint of strawberries. From her shampoo, I suspect."

        hi "I just need to remember to take my medicine, that's all."

        hi "Don't worry about it. It's not your fault."

        show emi sad_depressed_gym_close
        with charachange

        emi "You're sure?"

        "Her voice is muffled, mostly because at the moment her face is pressed into my chest."

        hi "Yeah, I'm sure. I just need to take it a little easy for the next few days."

        "It suddenly occurs to me how close the two of us are."

        "It also occurs to me how nice being this close feels."

        "I can feel Emi's heartbeat calming down, and I have to resist the urge to rest my chin on the top of her head."

        show emi sad_grin_gym_close
        with charachange

        emi "Thank goodness."

        emi "You really had me worried there, Hisao."

        stop music fadeout 1.5

        show nurse concern behind emi:
            center
            xpos 0.0 xanchor 0.3
            easein 0.5 xanchor 0.2
        with Dissolve(0.5)

        show nurse:
            center
            xpos 0.0 xanchor 0.2

        nk "Emi, you going to come in here any time soon?"

        show nurse grin
        with charachange

        nk "…Oh, I'm sorry. Was I interrupting?"

        show emi basic_shock_gym
        with vpunch

        "The two of us spring apart as if the other just caught on fire."

        show emi basic_hes_gym
        with charachange

        "Emi brushes her hair back nervously and laughs."

        play music music_emi fadein 1.0

        emi "'Course not!"

        show emi sad_shy_gym
        show nurse fabulous
        with charachange

        emi "I'll uh… see you later, okay?"

        show emi basic_closedgrin_gym
        with charachange

        emi "Oh, and Hisao?"

        hi "Hmm?"

        show emi basic_annoyed_gym_close
        with characlose

        with hpunch

        emi "Take your damn medicine!"

        "This last phrase is punctuated by a punch to the shoulder."

        hi "Yeah, yeah, I'll remember."

        hi "See you later."

        show nurse grin
        with charachange

        "The nurse smiles again like he's in on some joke I don't know about and waves to me as I head for my room, feeling a burning in my cheeks."

        stop music fadeout 8.0

        scene bg school_dormhisao
        with locationskip

        "I need a shower."

        "A cold one, if the thoughts running through my head now are any indication."

        "She was really soft."

        "My pills are waiting for me when I make it to my room."

        "I swallow them without a second thought."

        "I don't know why I didn't think of waiting until after the runs to take them. For some reason I figured it was when I woke up or not at all."

        "But no, they only need to be taken every twenty-four hours. The exact time of day doesn't factor into it."

        "My thoughts drift back to the hug in the hallway."

        "It's weird, you'd expect someone to smell foul after a run, but for some reason, Emi smelled… right. That tinge of sweat just seemed to fit her."

        "I really need that shower."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .piracy_on_the_high_seas:
        scene bg school_roof
        with locationchange

        nvl clear

        nvl show dissolve

        $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
        play ambient sfx_rooftop fadein 1.0

        n "{vspace=60}Strange that it feels so natural for me to go up to the roof these days."

        n "I never would have done such a thing at my old school."

        n "In those days I liked to eat alone… no, that's not quite true. Though I liked to sit alone, I also liked to watch people."

        n "I always figured that was the sort of person I was, but it appears I was wrong."

        n "Then again, I also thought I was the sort of person who had a normal heart, so there you have it."

        n "I don't know myself that well."

        n "Now I'm on the roof so that I can have lunch with a couple of people."

        n "And they are both girls, which is even stranger."

        n "Oddly enough, I feel closer to Emi and Rin than I felt to anyone at my old school."

        n "Somehow I get the feeling they'd at least visit me if I wound up in the hospital."

        $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

        nvl hide dissolve

        nvl clear

        "I focus on the view from the roof, banishing such thoughts from my head."

        "There's a light breeze blowing, and the sun is shining high in the sky."

        "The sky itself is a deep blue, with hardly a cloud in it. It's gotten pleasantly warm, and as I sit down to wait for my friends, I close my eyes and enjoy the feeling of the sun seeping into my skin."

        $ renpy.music.set_volume(0.1, 2.0, channel="ambient")

        scene black
        with shuteye

        pause 4.0

        "Voices intrude upon the edge of hearing."

        emi "—seems to have fallen asleep on us, Rin."

        rin "Maybe he's faking, to lull us into a false sense of security."

        emi "Why would he do that?"

        rin "No idea."

        emi "Still, you make a good point."

        emi "We should kick him or something to make sure he's really asleep."

        stop music fadeout 1.0

        hi "Huh? What?"

        $ renpy.music.set_volume(0.5, 5.0, channel="ambient")

        scene bg school_roof
        show rin basic_absent at tworight
        show emi excited_happy_close at twoleft
        with openeye

        play music music_ease fadein 3.0

        "Emi looms over me like only a short girl can, peering at me intently."

        show emi basic_closedgrin_close
        with charachange

        emi "Oh, you're awake. I guess we don't have to kick you then."

        show rin basic_deadpan
        with charachange

        rin "Was it part of your master plan?"

        hi "What are you talking about?"

        show emi basic_grin_close
        with charachange

        "Emi shrugs, her twin tails bouncing with the motion."

        show emi basic_closedhappy_close
        with charachange

        emi "I'm not sure either."

        show emi sad_grin_close
        with charachange

        emi "You must be pretty tired to fall asleep out here."

        show emi basic_closedgrin_close
        with charachange

        emi "Although it's pretty comfortable, I suppose."

        show emi:
            yanchor 0.9
        with ease
        with vpunch

        "She plops down next to me and begins to eat."

        show rin basic_absent
        with charachange

        show rin:
            yanchor 0.77
        with charamove

        "Rin sits opposite from the two of us, a move which only makes me more aware of the girl sitting next to me."

        "If I didn't know any better, I'd swear Rin did it on purpose."

        "I concentrate on my food, trying to tune out the majority of the conversation that Rin and Emi are having."

        "Despite my best efforts, however, I still find myself glancing over at Emi whenever she speaks."

        show emi basic_grin_close
        with charachange

        "I notice how she purses her lips when she's thinking about something, squinting slightly as if that would improve her thinking ability."

        show rin basic_deadpan
        with charachange

        show emi basic_closedhappy_close at leftrock
        with charachange

        "Rin says something that makes Emi laugh, and I notice, perhaps for the first time, how she laughs with her whole body, rocking back and forth, head thrown back, almost like she's about to fall over."

        "I probably look like a creep."

        show emi basic_confused_close
        with charachange

        "It's about this time that I realize Emi's looking at me. Her voice raised slightly, so she's probably just asked me a question."

        hi "Huh? Sorry, I kinda zoned out for a moment there."

        show rin basic_deadpannormal
        show emi basic_annoyed_close
        with charachange

        "Emi rolls her eyes, while a slight quirk of the eyebrow is the only sign that Rin's even paying attention."

        emi "I said, did you get a career survey in your class too?"

        show emi basic_grin_close
        with charachange

        emi "You know, one of those 'What do you want to do after high school?' things?"

        hi "I don't… think so. Maybe we'll get one tomorrow."

        show emi excited_happy_close
        with charachange

        emi "What are you going to put down?"

        "That's a really good question."

        "I guess I always figured I'd go to college after high school, but I've no idea what I'd do once I got there."

        "And with the heart attack and all, I'd really been concentrating on each day as it came rather than making long-term plans."

        "I suppose I can safely start planning ahead, again."

        "I've always liked having at least a vague plan for my future, so it'll be nice to come up with one again."

        "Of course, that doesn't change the fact that right now I've got absolutely…"

        hi "…No clue."

        hi "I always kind of assumed I'd figure it out in college. That or just become a salaryman. That's pretty popular."

        "But do I really want to? That's a tough question."

        "I guess I don't really want to do anything."

        show emi basic_closedhappy_close
        with charachange

        emi "You don't sound very excited about that one, do you?"

        show emi at leftrock

        "She laughs as she says this, and I'm caught up in her laugh again."

        "It's so… girlish. High and giggly, like a… well, pardon the cliché - like a babbling brook."

        "It bubbles out of her, starting in her belly and working its way up her throat."

        "I can't help but laugh myself - it's infectious."

        hi "Yeah, I guess I'm pretty unhappy with the salaryman idea."

        hi "But to be honest, I haven't given much thought to the future recently."

        hi "I suppose that, these days, I've been more concerned with living one day at a time."

        show emi basic_grin_close
        with charachange

        "Emi considers this for a moment and grins."

        emi "That's a pretty good idea, Hisao!"

        show emi excited_proud_close
        with charachange

        emi "I just wrote down, 'Pirate.'"

        "I'm momentarily stunned, then I start laughing."

        "I stop myself and manage to gasp out a question."

        hi "You're… you're not actually serious, are you?"

        show emi sad_annoyed_close
        with charachange

        "Emi looks mock offended."

        emi "Well I've got the legs for it already, so I just kind of figured…"

        show rin basic_amused
        with charachange

        "Even Rin seems amused by this."

        show emi basic_annoyed_close
        with charachange

        emi "Just you wait, I'll be the terror of the high seas!"

        emi "I'll show you all!"

        show emi basic_closedhappy_close
        with charachange

        emi "I've even been working on my pirate voice!"

        show emi at offscreenleft
        with ease

        show emi basic_annoyed behind rin at left
        with ease

        "She suddenly springs up and begins swaggering up and down the rooftop shouting orders."

        show emi at center
        with ease

        emi "Yarr, me hearties, give 'em a broadside with the long guns!"

        show emi at twoleft
        with ease

        emi "We'll wear their guts for garters!"

        show rin basic_deadpanamused
        with charachange

        rin "Do you even know what that means?"

        show emi basic_confused
        with charachange

        "Rin's unexpected interruption stops Emi in her tracks."

        show emi sad_shy
        with charachange

        emi "Not really."

        show emi basic_closedgrin
        with charachange

        emi "But it's all in the delivery!"

        play sound sfx_warningbell

        show emi basic_hes
        show rin basic_awayabsent
        with charachange

        "The ringing of the bell prevents her from demonstrating her point further."

        show emi at offscreenleft
        with charamovefaster

        hide emi

        "Emi dashes off immediately, leaving Rin and myself alone on the roof."

        show rin:
            xpos 0.5
        show bg at bgleft
        with charamove

        show rin basic_deadpancontemplation
        with charachange

        "Rin stares at me intently for a few moments."

        hi "Is there… something wrong?"

        show rin basic_lucid
        with charachange

        "Rin considers this question closely for a moment."

        "After a lengthy pause, she shakes her head."

        show rin basic_deadpannormal
        with charachange

        rin "Nope."

        hi "Oh, um…"

        extend " why the staring, then?"

        show rin basic_awayabsent
        with charachange

        "Rin shakes her head again."

        rin "Nope, I don't get it."

        hi "Get what?"

        show rin basic_deadpan
        with charachange

        rin "The staring thing. You two seem to, but I don't."

        "Great. She saw me staring. Now she probably thinks I'm a pervert or something."

        "Actually, probably not. This is Rin we're talking about, after all."

        "Still, I feel the need to defend myself."

        hi "I wasn't staring, I was just tired."

        show rin basic_deadpancontemplation
        with charachange

        "Rin actually snorts at this, but she doesn't say anything."

        hi "No, really! I was just… distracted, is all."

        show rin basic_lucid
        with charachange

        rin "Mmm."

        stop music fadeout 4.0

        "Eager to end this conversation, I head back down to class."

        stop ambient fadeout 2.0

        scene bg school_scienceroom
        show misha cross_grin at twoleft
        show shizu behind_blank at tworight
        with locationskip

        "I'm greeted by the twin specters of Shizune and Misha, looking like they mean business."

        "Well, Shizune looks like she means business, anyway."

        "Misha just looks like she's about to start laughing at any minute."

        play music music_shizune fadein 3.0

        show misha perky_smile
        with charachange

        mi "Up on the roof again, Hicchan?"

        show misha hips_frown
        with charachange

        mi "You know that's dangerous, don't you~?"

        show shizu basic_angry
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "That's right~!"

        show misha hips_smile
        with charachange

        mi "The school cannot be held responsible for any injury that comes from being up there, you know!"

        show misha cross_frown
        with charachange

        mi "Furthermore, we could report you for breaking the rules~!"

        show misha cross_frown_close
        with characlose

        "Misha leans in and whispers conspiratorially."

        show misha sign_smile_close
        show shizu behind_smile
        with charachange

        mi "But we won't, Hicchan!"

        show misha hips_grin_close
        with charachange

        mi "You three are too cute together~!"

        show misha cross_laugh
        with charadistant

        "She straightens up again, laughing at my sudden blush."

        mi "Wahahaha~!"

        show misha cross_grin
        with charachange

        mi "You're too easy to tease, Hicchan~!"

        hi "Hey, come on."

        hi "I'm still new here, sort of."

        hi "Isn't it mean to pick on the newcomer like this?"

        show misha hips_grin
        with charachange

        mi "Nope~!"

        show misha sign_smile
        with charachange

        mi "It's to help you get acclimated to your new surroundings!"

        hi "Ah, I see."

        hi "Well…do you have to be so overzealous about it?"

        show misha hips_grin
        with charachange

        mi "Yep!"

        show misha hips_smile
        with charachange

        mi "Ah! That aside, Hicchan, we were looking for you this morning, but you weren't in your room!"

        hi "Of course I wasn't. I was out for my morning exercise, or here in class, bright and early."

        hi "Unlike you."

        show shizu basic_angry
        show misha hips_frown
        with charachange

        "Shizune looks peeved, and a beat later, so does Misha. Or she tries to, at any rate."

        mi "That was because of student council business! You should be grateful that we work so hard for you~!"

        hi "Oh, I am, I am. So what did you need me for?"

        "Not another attempt to rope me in to do their dirty work, I hope."

        show misha sign_smile
        with charachange

        mi "We had to give you something~ but since you weren't around, we dropped it off in your room!"

        hi "Something? Like what?"

        show misha hips_grin
        with charachange

        mi "Oh, you'll find out when you get back, Hicchan~! Wahahaha~!"

        hide misha
        hide shizu
        with charaexit

        "Mutou entering the room ends our conversation, and we all head to our seats."

        stop music fadeout 10.0

        "It's only after I've settled down at my desk and the teacher's started talking about something or other that something odd strikes me."

        "What did Rin mean, 'You two seem to?'"

        "Was Emi staring at something too?"

        "For a brief moment, I consider the possibility that Emi was staring at me the way I was staring at her."

        "Of course, that's ridiculous."

        "Still, I can't deny that I wouldn't mind if it were true…"

        "But it's best not to think of that. No need to get my hopes up."

        "Come to think of it, when did I start having hopes like that anyway?"

        "I shake my head in an attempt to clear it, and focus on the lesson."

        scene bg school_dormhallway
        with shorttimeskip

        "After class, I make my way to my room. Mutou really piled on the homework today."

        play sound sfx_impact2

        show kenji tsun at left
        with vpunch

        "Before I can open my door, however, I am suddenly intercepted by Kenji, who has just exploded out of his own room in a flurry of papers."

        ke "Hey, we need to talk."

        play music music_kenji fadein 1.0

        ke "These rooftop shenanigans of yours, man."

        ke "They've gotta stop."

        hi "What?"

        ke "Your running around on the rooftop with the limbless wonders!"

        ke "They're women, man! You'll get yourself killed running around like that!"

        hi "I don't follow."

        show kenji neutral
        with charachange

        "Kenji sighs and adjusts his glasses, before what could be understood as an attempt at explaining himself patiently."

        ke "Look, we're friends so I'm telling you this for your own good."

        ke "But if I were going to kill someone, I'd do it by throwing them off the roof and making it look like an accident."

        show kenji tsun
        with charachange

        ke "And if I've thought of it, you can be sure they've thought of it too."

        ke "They're crafty - almost as crafty as I am."

        hi "I see."

        show kenji happy
        with charachange

        ke "Good!"

        ke "I'm glad we had this chat."

        show kenji neutral
        with charachange

        ke "Loan me 500 yen."

        hi "…I'm sorry?"

        show kenji tsun
        with charachange

        ke "I need to get a drink, man!"

        ke "I've been inside all day and the tap water's been compromised, as I'm sure you know."

        ke "So I need to stock up on something canned, got it? But to do that, I need 500 yen."

        show kenji neutral
        with charachange

        ke "And since I've just saved your life with my timely advice, you can at least spare me 500 yen."

        "You know, if it'll make him go away, 500 yen is a bargain."

        stop music fadeout 6.0

        show kenji happy
        with charachange

        show kenji:
            easeout 0.5 xanchor 0.2 alpha 0.0

        "I hand the money over to Kenji, who nods in thanks and dashes off down the hallway, but not before he locks his door."

        "What an exhausting person. I'd better go, in case he changes his mind."

        scene bg school_dormhisao
        with locationchange

        "Hm?"

        "As I close the door, my heel taps against something lying on the floor."

        "It's a brightly-colored rectangle of paper. Ah, this must be the 'something' Misha mentioned before."

        "Probably a student council leaflet she slid under the door."

        "However, when I pick it up, I find that I couldn't have been more wrong."

        "Someone actually wrote me an old-fashioned, hand-written paper letter."

        "Who bothers doing something like that in this day and age, anyway? Yet, as unlikely as the prospect of receiving one sounds, this is definitely a letter I have in my hands."

        "I was planning on finishing my homework, getting some dinner, and going to bed in order to be ready for tomorrow morning's run."

        "However, the letter has naturally caught my interest. I sit at my desk to examine it properly."

        scene ev hisao_letter_closed:
            xalign 0.5 yalign 0.5 zoom 1.1
            acdc_warp 10.0 zoom 1.0
        with locationchange

        play music music_rain fadein 5.0

        "It's the first piece of mail I've received here at Yamaku, so it'd feel special even if it wasn't something as rare as a handwritten letter."

        "What causes me even more trepidation is the name of the sender, written neatly on the back of the envelope."

        "'Iwanako.'"

        "I have no idea why she would write to me. I haven't been in contact with anyone from my old school since I transferred, and Iwanako is the last person I'd expect to want to write me a letter."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=150}The last time I saw Iwanako was terribly awkward; embarrassingly so. She came to my hospital room, peeled me an apple out of courtesy and then we practically sat in silence for half an hour."

        n "She said 'goodbye' and didn't look me in the eye when she closed the door."

        n "It might've been a natural end to the series of visits that were probably pretty painful for both of us."

        n "Every time she visited me in the hospital I wanted to talk to her, but something stopped me every time."

        n "Every time that I didn't speak made the next time even harder."

        nvl clear

        n "{vspace=120}She looked so guilty that I didn't want to say anything that might upset her, and I never could figure out the right words to say."

        n "I think Iwanako blamed herself for my heart attack. That's ridiculous, of course, but knowing it and believing it are two very different things."

        n "I told her that it wasn't her fault, she nodded and I really think she understood that if it hadn't been that, then sooner or later something else would've made my heart give out."

        n "Yet she looked so hopelessly sad every time she opened that door and entered my room."

        n "So I never managed to say the things I wanted to say. In the end, that might've hurt her even more."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")

        nvl hide dissolve
        nvl clear

        scene ev hisao_letter_open
        with locationchange

        "Carefully, I open the envelope and draw out the folded letter from within."

        call screen written_note(_("Dear Hisao,\n\nHow are you? I hope you are well and happy at your new school. Everyone here misses you. Almost all of our second-year class got put together in class 3-1 for the final year, so we are pretty comfortable right from the beginning of the year. I'm sure you would've been assigned to this class as well."))

        call screen written_note(_("The mood among the third-years seems to be very anxious about the final exams, even though they are so far away. The teachers are badgering us about it all the time - even old Mr. Tachibana who is, by the way, our homeroom teacher this year. Would you believe it? I was sure that he'd retire after our second year, but here he is, nagging everyone about studying for exams.{vspace=30}"))

        call screen written_note(_("I think things like that are the main reason why the mood among the third-years is so nervous. I must admit that I'm somehow losing confidence in myself as well, even though I've always fared reasonably well in exams.{vspace=150}"))

        call screen written_note(_("It's so weird to think we are already seniors, isn't it? Time has really flown past. I wonder where it went. The new first-years seem so young and somehow really innocent. I keep wondering if I was like them in my first year. I've been feeling nostalgic like this for the whole first trimester.{vspace=90}"))

        call screen written_note(_("There are other things I want to say. I'm writing to you because I felt that there are things I should've said after the incident back in winter. I really regret that I wasn't able to say them in person, and I have no excuse for it…{vspace=150}"))

        "Yeah, I think I have had quite enough of this."

        scene bg school_dormhisao
        with locationchange

        "I crumple up the sheet of paper and toss it across the room. My aim is off, so the letter rolls under my nightstand instead of going into my wastebasket."

        "That was an apology for abandoning me. Except I don't know that I really need it any more, at this point."

        "The hospital seems like a lifetime ago, and here, now, I've got other things on my mind."

        stop music fadeout 8.0

        "Emi, for starters."

        "It wasn't great to be abandoned during my stay, but it's not something I'm worried about any more."

        "In fact, I hadn't even thought about the hospital in what feels like forever until this letter came in. It's almost annoying to have received it."

        "I've got exams to study for, myself. I have no time for the past."

        "Now, about that homework…"

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .famous_last_words:
        scene black

        hi "So what's the plan for today anyway?"

        play music music_daily fadein 1.0

        scene bg school_girlsdormhall
        with dissolve

        "I'm waiting patiently in the hallway of the girls' dormitory just outside of Emi and Rin's rooms."

        "Emi is apparently helping Rin with getting dressed."

        "I suppose that makes perfect sense, as I've no idea how Rin would get dressed otherwise."

        emi "Picnic!"

        hi "Picnic?"

        emi "That's what I said!"

        hi "Sounds pretty exciting."

        emi "I know, right?"

        "Rin chooses this moment to make an observation."

        rin "The sky seems threatening today."

        "Actually, I noticed that, too, on my way over. Despite the sunshine of the early morning, the afternoon seems to have taken a turn for the gloomy."

        "There's a heaviness to the air as well that usually heralds a rainstorm."

        "I wonder if I should have brought my umbrella…"

        hi "She's got a point."

        hi "Emi, you sure that you still want to risk getting caught in the rain?"

        "I don't even know why I bothered asking."

        show emi basic_shock:
            tworight
            xpos 0.9
            easein 0.5 tworight
        with charaenter

        show emi at tworight

        "Emi pops out of Rin's room into the hallway looking shocked that I'd even suggest canceling our plans."

        emi "Of course!"

        show emi basic_annoyed
        with charachange

        emi "What, the threat of rain's supposed to stop me?"

        "I can't help but grin at her belligerent response. It's almost like she's daring the rain to come."

        "If Mother Nature were walking down the street, I think Emi would probably start a fight with her."

        "Or at the least challenge her to a race."

        "In fact, Emi seems almost aggressively cheerful today."

        show rin basic_absent:
            tworight
            xpos 0.7 alpha 0.0
            ease 1.0 tworight alpha 1.0
        with None
        show emi at twoleft
        show bg at bgleft
        with charamove

        show rin at tworight

        "Rin wanders out into the hallway, looking her usual self."

        hi "Well then, are we all ready to go?"

        show emi basic_closedhappy
        with charachange

        emi "I'm ready!"

        show rin basic_deadpannormal
        with charachange

        "Rin nods and says a single word."

        show rin basic_deadpan
        with charachange

        rin "Basket."

        hi "Beg pardon?"

        show rin basic_deadpannormal
        with charachange

        rin "The basket. In Emi's room. You should carry it."

        show emi basic_hes
        with charachange

        "Emi claps a hand to her mouth, embarrassed."

        show emi basic_closedsweat
        with charachange

        emi "Omigosh! I almost forgot all about it! Nice save, Rin!"

        show emi at offscreenleft
        with ease

        pause 0.3

        show emi basic_closedgrin at twoleft
        with ease

        "Emi darts into her room and emerges with what looks like a very well-stocked picnic basket."

        with vpunch

        "As she hands it over to me, I note that it feels heavy enough to be one, too. Good Lord, how much food did she pack?"

        "…More to the point, where'd she get the money for all of this?"

        hi "So, are we set to head out?"

        show emi basic_grin
        with charachange

        emi "Yep!"

        show rin basic_awayabsent
        with charachange

        "Rin gives another nod, and we head out of the dormitory."

        scene bg school_courtyard_rn
        with locationskip

        "I can't help but frown when I notice how gray the sky's gotten in the ten minutes I was inside."

        "Still, Emi does not seem concerned by such petty concerns as the color of the sky. She's positively skipping as we walk."

        "Which reminds me…"

        hi "Where are we going?"

        "This brings Emi up short and she shoots me an embarrassed look."

        show emi sad_shy_rn at center
        with charaenter

        emi "You know, I hadn't really thought of that."

        emi "What do you think, Hisao?"

        "Well, there's the spot where we ate during the festival, but it might be nice to leave the campus for a while. However, I'm not sure if there's any good places to do that in town."

        "Just as I'm about to open my mouth, Rin unexpectedly interjects with a suggestion."

        show emi at twoleft
        show bg at bgleft
        with charamove

        show rin basic_deadpan_rn at tworight
        with charaenter

        rin "There's a park in town near the art shop."

        show emi basic_closedhappy_rn
        with charachange

        emi "Great idea, Rin! I totally forgot all about that place!"

        "Crisis averted."

        hi "Do you know how to get there, Rin?"

        show rin basic_deadpannormal_rn
        with charachange

        "Rin shrugs."

        show rin basic_awayabsent_rn
        with charachange

        rin "It's pretty likely."

        show emi excited_amused_rn
        with charachange

        emi "Good enough for me!"

        "I would prefer knowing for sure… but, what the hell."

        hi "Lead on, Rin."

        scene bg school_gate_rn
        with locationchange

        "The three of us quickly make our way off campus and take the road down into town."

        scene bg school_road_rn
        with locationchange

        "This basket's a bit heavy. I hope that the park is close by."

        scene bg suburb_roadcenter_rn
        with locationchange

        "We pass the art supply store, Rin slowing her pace slightly as we go by."

        "Emi notices Rin's change of pace and stops."

        show emi basic_grin_rn at twoleft
        show rin relaxed_nonchalant_rn at tworight
        with charaenter

        emi "You wanna go in, Rin?"

        show rin basic_awayabsent_rn
        with charachange

        "Rin shrugs."

        show rin basic_deadpan_rn
        with charachange

        rin "Nothing I need."

        show emi excited_proud_rn
        with charachange

        emi "Are you suuure?"

        show rin basic_delight_rn
        with charachange

        show rin basic_deadpandelight_rn
        with charachange

        "There's the slightest flutter of a smile on Rin's face, quickly replaced with her usual expression."

        show rin basic_deadpan_rn
        with charachange

        rin "Life's uncertain, but on this at least I am pretty sure."

        show rin basic_deadpanamused_rn
        with charachange

        rin "Nice of you to offer."

        show emi basic_closedhappy_rn
        with charachange

        emi "Well it's not like I'm the one carrying the basket."

        show emi basic_grin_rn
        with charachange

        emi "But I'll bet Hisao wouldn't have minded anyway, right?"

        hi "Oh, of course not. This is hardly a heavy load."

        "I flex for emphasis."

        show emi excited_laugh_rn
        with charachange

        "Emi stifles a snort of laughter by pointing to the park at which we've suddenly arrived."

        $ renpy.music.set_volume(0.02, 0.0, channel="ambient")
        play ambient sfx_rain fadein 15.0

        scene bg suburb_park_rn at bgright
        with locationchange

        emi "Oh, I remember this place!"

        show emi basic_closedhappy_rn at center
        with charachange

        emi "I ran into you here that one time, didn't I, Rin?"

        show emi at twoleft
        show bg at center
        with charamove

        show rin basic_deadpannormal_rn at tworight
        with charaenter

        "Rin's eyebrow raises slightly."

        show rin basic_deadpan_rn
        with charachange

        rin "Maybe."

        show rin relaxed_boredom_rn
        with charachange

        rin "I'm unwilling to say for certain one way or the other."

        show rin relaxed_nonchalant_rn
        with charachange

        rin "Memory's a tricky thing, you know."

        "Well I'll be. We made it in one piece after all."

        "The sun's still nowhere to be seen, but neither Emi nor Rin seem to mind."

        scene ev picnic_normal:
            yalign 1.0
            easein 8.0 yalign 0.0
        with whiteout

        "We find a spot to sit on the grass and I set the basket down gratefully."

        "There's a surprising amount of food prepared. Maybe we were supposed to be joined by some of Emi's teammates or something?"

        emi "I'm starving! Dig in!"

        "She attacks the food as if she's had nothing to eat for years."

        stop music fadeout 2.0

        play sound sfx_thunder

        show ev picnic_rain:
            yalign 0.0
        with charachangeev

        $ renpy.music.set_volume(0.2, 0.5, channel="ambient")

        show rain light
        with dissolve

        "I'm just reaching for the food myself when I feel the first drop of rain land on the back of my hand."

        hi "Uh oh."

        hi "Looks like the weather's not going to cooperate with us after all."

        scene bg suburb_park_rn behind rain
        show emi sad_grit_rn behind rain:
            twoleft
            ypos 1.15
        show rin basic_absent_rn behind rain:
            tworight
            ypos 1.2
        show rain light
        with flash

        "Emi glares at the sky as if that alone will hold back the rain."

        "I very nearly believe she can do it. It's one heck of a glare."

        show emi basic_annoyed_rn
        with charachange

        emi "It had better cooperate."

        show emi sad_angry_rn
        with charachange

        emi "You hear me sky? You stop that raining right this instant!"

        "The sky doesn't seem inclined to listen to her, despite the commanding tone she's taken with it."

        $ renpy.music.set_volume(0.5, 4.0, channel="ambient")

        show rain medium
        with dissolve

        "Instead, the rain seems to increase. Rin wrinkles her nose in distaste at this turn of events."

        show rin basic_deadpan_rn
        with charachange

        rin "Regrettable."

        show emi basic_confused_rn
        with charachange

        emi "What do you mean?"

        show rin basic_deadpannormal_rn
        with charachange

        "Rin shrugs."

        show rin relaxed_nonchalant_rn
        with charachange

        rin "I could paint this if I weren't out here. Shame to miss it, is all."

        "She doesn't seem angry or annoyed about it, just a little disappointed."

        show emi basic_closedhappy_rn
        with charachange

        "Emi laughs in response to Rin's comment."

        show emi basic_grin_rn
        with charachange

        emi "Guess we should have stopped in that art supply store after all, huh?"

        $ renpy.music.set_volume(1.0, 6.0, channel="ambient")

        show rain normal
        with dissolve

        "The rain increases a little more, offended that we haven't fled yet."

        "Despite the warm temperatures we've been enjoying, the rain is rather cold. I wish I'd brought my umbrella."

        hi "Hey, we should probably head inside to keep dry."

        show emi basic_confused_rn
        show rin basic_absent_rn
        with charachange

        emi "We're already pretty wet, Hisao."

        hi "Yeah, but we can dry off this way and maybe wait out the storm. You don't want to catch a cold or anything, do you?"

        show emi basic_annoyed_rn
        with charachange

        "Emi considers this for a moment. I can tell that part of her wants to stay out in the rain just to spite the weather."

        "Unfortunately for her, the weather hardly cares about what we do."

        show emi basic_closedgrin_rn
        with charachange

        emi "I suppose you're right."

        show emi sad_grin_rn
        with charachange

        emi "Where could we go?"

        "I don't have an answer for her. The area's still pretty new to me."

        "Though I guess I'm slowly getting used to the school itself, the surrounding town remains a mystery."

        "All I know is the art supply store, and that's only because we've just passed it."

        show emi basic_closedgrin_rn
        with charachange

        "Fortunately, Emi soon snaps her fingers in triumph."

        show emi basic_happy_rn
        with charachange

        emi "That's it! There's a tea shop nearby!"

        emi "We could have some tea and dry out, no problem!"

        "That doesn't sound like a bad idea."

        hi "Great! You know where it is?"

        show emi basic_grin_rn
        with charachange

        "Emi nods, looking fairly confident."

        show emi basic_closedgrin_rn
        with charachange

        emi "Sure do!"

        show emi basic_hes_rn
        with charachange

        emi "I think."

        show emi excited_laugh_rn
        with charachange

        emi "But it'll be an adventure either way, right?"

        hi "Adventure, huh? Well, I suppose we could use a little adventure."

        "I think as long as we get out of the rain I'll be happy."

        show emi basic_grin_rn at twoleft
        show rin at tworight
        with Dissolvemove(1.0)

        "The picnic basket is a little lighter now, at least."

        hi "Lead on!"

        scene bg suburb_roadcenter_rn behind rain
        show rain medium
        with locationchange

        "Rin and I follow Emi as she weaves through the streets with something approaching confidence."

        show emi basic_confused_rn behind rain at center
        with charaenter

        emi "Now, a left here…"

        show emi excited_joy_rn
        with charachange

        emi "There! The Shanghai!"

        "Emi beams triumphantly as she points to the tea shop."

        scene bg suburb_shanghaiext_rn
        show rain medium
        with locationchange

        if wait_for_shizu or _in_replay:
            "Come to think of it, I have been here before. It seems fairly crowded inside; entirely the fault of the sudden rain, I'm sure."

            play sound sfx_storebell
            stop ambient fadeout 0.5
            play music music_jazz fadein 2.0

            scene bg suburb_shanghaiint
            with locationchange

            $ renpy.music.set_volume(0.7, 0.0, channel="ambient")
            play ambient sfx_crowd_indoors fadein 2.0

            pause 1.0

            show yuukoshang neutral_down at center
            with charaenter

            yu "Welcome! Can I—"

            show yuukoshang happy_down
            with charachange

            yu "Oh, it's you."

            "Yuuko seems to know Emi."

            show yuukoshang at tworight
            show bg at bgright
            with charamove

            show emi basic_closedhappy at twoleft
            with charaenter

            "Emi grins brightly, pleased to be remembered."

            show emi basic_grin
            with charachange

            emi "Hey Yuuko! Got room to seat us?"

            show yuukoshang neutral_down
            with charachange
        else:
            "It seems fairly crowded inside; a symptom of the sudden rain, I'm sure."

            play sound sfx_storebell
            stop ambient fadeout 0.5
            play music music_jazz fadein 2.0

            scene bg suburb_shanghaiint
            with locationchange

            $ renpy.music.set_volume(0.7, 0.0, channel="ambient")
            play ambient sfx_crowd_indoors fadein 2.0

            pause 1.0

            show yuukoshang neutral_down at center
            with charaenter

            yu "Welcome! Can I—"

            "I'm surprised to find out that our waitress is none other than Yuuko."

            "She sure looks the part in her uniform. It's hard to believe this is the same librarian from our school."

            "Does she work two jobs? I guess that must be it."

            show yuukoshang happy_down
            with charachange

            yu "Oh, it's you."

            "Yuuko seems to know Emi."

            show yuukoshang at tworight
            show bg at bgright
            with charamove

            show emi basic_closedhappy at twoleft
            with charaenter

            "Emi grins brightly, pleased to be remembered."

            show emi basic_grin
            with charachange

            emi "Hey Yuuko!"

            hi "Hi, Yuuko. I didn't know you worked here too."

            show yuukoshang worried_down
            with charachange

            yu "Do I know you?"

            show yuukoshang worried_up
            with charachange

            yu "You seem awfully familiar, but I don't think I've ever seen you in here."

            hi "Er, we met at your other job. At the Yamaku library. Remember?"

            show yuukoshang happy_up
            with charachange

            "Her eyes widen in memory."

            show yuukoshang closedhappy_down
            with charachange

            yu "Yeah, that's it! Nice to see you again…"

            show yuukoshang panic_down
            with charachange

            yu "Oh no, this is bad!"

            show yuukoshang panic_up
            with charachange

            yu "I should have remembered a customer's face! I'm sorry… I'm terribly sorry!"

            "Yuuko goes from realization to panic in a split second, performing a series of high-speed bows. I narrowly avoid getting headbutted in the process."

            hi "Whoa, hey, calm down!"

            hi "Listen, I wasn't a customer when we first met, in fact I hadn't ever been to the Shanghai, so it's all right."

            "Not the best display of logic, but it seems to relax her a little."

            show yuukoshang worried_down
            with charachange

            yu "Do you really think so?"

            hi "Uh, yeah, I'm sure. Positive. Isn't that right, girls?"

            show emi basic_closedgrin
            with charachange

            "Emi has been watching this little drama unfold with considerable amusement."

            show emi excited_proud
            with charachange

            emi "Yep, it sure is!"

            show yuukoshang neutral_up
            with charachange

            yu "Well, okay…"

            show emi basic_happy
            with charachange

            emi "So Yuuko, got room to seat us?"

            show yuukoshang neutral_down
            with charachange

        $ renpy.music.set_volume(0.3, 3.0, channel="ambient")

        "Yuuko nods and leads us to a corner booth, providing us with some small towels before taking our order."

        show yuukoshang happy_down
        with charachange

        yu "What will you have?"

        show emi basic_closedhappy
        with charachange

        emi "Cake! And some tea too, I guess."

        show yuukoshang neutral_down
        with charachange

        yu "What kind of cake?"

        show emi excited_proud
        with charachange

        emi "Surprise me!"

        show yuukoshang worried_up
        with charachange

        "Yuuko looks uncomfortable at the thought of surprising anyone, but she gives a nod and turns to Rin."

        show rin basic_absent at offscreenright
        with None

        show yuukoshang neutral_down:
            xpos 0.55
        show emi basic_grin at left
        show rin at right
        show bg at center
        with charamovechangefaster

        yu "And for you?"

        show rin negative_spaciness
        with charachange

        rin "I'll take a straw. My feet are all wet."

        show yuukoshang worried_up
        with charachange

        yu "Sorry?"

        show rin basic_awayabsent
        with charachange

        rin "The drinking kind of straw. One, please."

        show yuukoshang worried_down
        with charachange

        "Yuuko is obviously uncertain of what to think about this. She fiddles with her pen and stationery for a moment, looking like she's about to cry, before turning in my direction."

        show yuukoshang neutral_down
        with charachange

        yu "And you, sir?"

        hi "Just tea, I think."

        "Emi would probably yell at me if I ordered cake."

        show emi sad_depressed
        with charachange

        emi "Aw, come on Hisao! Don't let me be the only one with food, I'll feel like a pig!"

        hi "Just trying to eat healthy."

        hi "Your orders, after all."

        show emi basic_closedgrin
        with charachange

        emi "Well… today is your day off! You can be healthy tomorrow!"

        hi "Well then, I suppose I will have some cake after all."

        show yuukoshang neurotic_up
        with charachange

        "Yuuko seems slightly irritated that I'm changing my mind."

        yu "What kind?"

        "I glance at Emi and grin."

        hi "Surprise me."

        show yuukoshang smile_down
        with charachange

        "Yuuko sighs and nods."

        yu "Very well. Your order will be out soon."

        show emi basic_grin
        show yuukoshang neutral_down
        show rin basic_awayabsent
        with shorttimeskip

        "Despite the crowd, our order does indeed arrive quickly."

        show emi excited_joy
        with charachange

        emi "Thanks, Yuuko!"

        "Yuuko nods in appreciation."

        stop music fadeout 4.0

        show yuukoshang happy_down
        with charachange

        yu "This is a different guy than usual, isn't it?"

        "What? Different guy?"

        show emi basic_hes
        with charachange

        "Emi must notice my confusion, because she seems a little embarrassed."

        emi "W-what? Oh, yeah, I guess he is."

        show emi sad_grin
        with charachange

        emi "This is my friend Hisao."

        hi "We've met."

        show yuukoshang smile_down
        with charachange

        yu "Huh. Small world."

        show yuukoshang neutral_down
        with charachange

        yu "Well, let me know if you need anything."

        hide yuukoshang
        with charaexit

        show emi at twoleft
        show rin at tworight
        with charamove

        "With that, Yuuko takes off like a shot to wait on some other tables, leaving me to ponder her comment."

        "Different guy, huh? I guess it makes sense, right? Emi's pretty popular, or so I've been told."

        "It's probably that kid from the track team."

        "This is stupid. I can just ask Emi."

        show rin basic_absent
        with charachange

        play music music_comedy fadein 0.5

        hi "So who's this other guy, huh? You got a secret lover or something?"

        show emi basic_closedhappy
        show rin basic_awayabsent
        with charachange

        "Emi laughs again, only I get the feeling it's from nervousness as much as anything else."

        show emi basic_grin
        with charachange

        emi "It's just the track team captain. He likes coming down here after practice sometimes."

        show emi basic_closedgrin
        with charachange

        emi "So if we have anything to discuss I tag along."

        "Hmm, sounds mighty suspicious to me…"

        show rin basic_absent
        with charachange

        hi "Oh, I see."

        "I could let the matter drop, but I can't resist at least getting another dig in."

        hi "So it {b}is{/b} a secret lover!"

        hi "I knew it!"

        show rin basic_deadpanamused
        with charachange

        "Rin watches our play, seeming mildly amused before muttering something that I don't quite catch."

        rin "… y'anyway"

        show emi basic_confused
        with charachange

        call screen doublespeak(emi, _("What?"), hi, _("Huh?"))

        show rin basic_surprised
        with charachange

        "Rin jerks back from wherever her mind wandered off to."

        rin "Huh?"

        hi "What did you just say?"

        show rin basic_deadpan
        with charachange

        rin "Huh."

        hi "No, before that."

        show rin relaxed_nonchalant
        with charachange

        rin "No idea."

        hi "Oh. Well."

        hi "Okay."

        show emi basic_grin
        show rin basic_deadpannormal
        with charachange

        "I let the matter drop, but I can't help notice that Emi seems relieved that Rin interrupted the conversation."

        "Maybe I went a little too far…"

        "Conversation dies down for a moment as Emi and I busy ourselves with cake."

        "Mine is strawberry, and surprisingly good."

        play sound sfx_slide2

        show emi excited_happy_close
        with characlose

        show emi basic_closedgrin
        with charadistant

        "Emi seems to think so too, as she suddenly reaches over with her fork and steals a bit."

        hi "Thief!"

        show emi excited_proud
        with charadistant

        emi "Pirate. There's a difference."

        hi "We're not on water!"

        show emi basic_closedgrin
        with charadistant

        emi "Well, no. But there's a lot of water outside, so it still works, right?"

        show emi sad_grin
        with charadistant

        emi "Besides, you can have some of mine. I think it's cranberry or something."

        show emi sad_depressed
        with charadistant

        emi "I should have asked for the strawberry. I like strawberries."

        hi "Feel free to help yourself to mine, if you really must."

        "For some reason, I feel compelled to add:"

        hi "Seeing as how you've already done it once, and all."

        show emi basic_closedgrin
        with charadistant

        "Emi sticks her tongue out at me, but that doesn't stop her from appropriating my cake. I try some of hers, as well."

        "It's raspberry, and pretty good."

        show rin relaxed_boredom
        with charachange

        rin "The rain's let up."

        "It would appear that Rin is correct."

        "Good timing, too. I've finished my food, and it looks like Emi has as well."

        hi "Well, we'd better pay and get a move on before it starts raining again."

        stop ambient fadeout 1.0

        scene bg suburb_shanghaiext_rn
        with locationchange

        "It takes a few minutes to get Yuuko's attention, but we pay and get out pretty quickly."

        show emi basic_grin_rn at center
        with charaenter

        emi "So, do you want to return to the park?"

        "My jaw nearly drops."

        hi "Are you kidding? It's probably going to rain again!"

        "In fact, I think I just felt some raindrops."

        show emi sad_grin_rn
        with charachange

        emi "Hmm… you may be right."

        show emi basic_closedgrin_rn
        with charachange

        emi "Well okay, I'll let you off the hook this time, but you owe me a picnic now. Got it?"

        "I don't know if she's addressing me, Rin, or the both of us."

        hi "Fine, fine."

        show emi excited_proud_rn
        with charachange

        emi "Now hurry up! I wanted to get some laps in at the track, and it would be nice to do it without the rain."

        hi "I thought this was your day off!"

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        stop music fadeout 6.0

        show emi sad_depressed_rn
        with charachange

        emi "Well…"

        "Emi suddenly seems reluctant to explain herself."

        show emi sad_grin_rn
        with charachange

        emi "I need the practice."

        show emi basic_grin_rn
        with charachange

        emi "And I need to burn off that cake, anyway."

        "Why do I get the feeling that she's leaving something out?"

        hi "Are you sure? It wasn't that much cake…"

        show emi basic_closedgrin_rn
        with charachange

        emi "No, it wasn't that much cake for {b}you{/b}. I ate most of it."

        "She's got a point there."

        menu:
            with menueffect
            "Still, I feel like I should at least offer to run with her…"

            "Offer to run with Emi.":
                $ run_with_emi = True

                call a2ec1o1

            "Keep quiet.":
                $ run_with_emi = False

                call a2ec1o2

        stop music fadeout 12.0

        scene bg school_dormext_full_rn
        with locationskip

        play ambient sfx_rain fadein 2.0
        show rain normal
        with Dissolve(2.0)

        "As we approach the girls' dormitory, it starts to rain again."

        show emi sad_annoyed_rn behind rain at center
        with charaenter

        "Emi's expression sours slightly."

        emi "Aw, man…"

        emi "Stupid rain."

        hi "Hey, it'll let up soon enough. You can go running then, right?"

        show emi basic_grin_rn
        with charachange

        "Emi snorts, seemingly amused."

        show emi excited_proud_rn
        with charachange

        emi "Like I'm not going to run in the rain."

        hi "Well you shouldn't! You could catch a cold!"

        show emi basic_grin_rn
        with charachange

        "Emi waves her hand airily."

        emi "Ridiculous! I don't get colds."

        show emi basic_closedgrin_rn
        with charachange

        emi "My immune system is far too strong for something like that."

        "I can't help but laugh."

        hi "Well, I'll see you tomorrow then, okay?"

        show emi basic_happy_rn
        with charachange

        emi "Yeah!"

        show emi basic_grin_rn
        with charachange

        emi "Thanks for coming! Oh, and for carrying the picnic basket!"

        show emi excited_amused_rn
        with charachange

        emi "I'll bring it for lunch tomorrow. We can have our picnic on the roof!"

        hi "Sounds good to me. See you then!"

        hide emi
        with charaexit

        "Emi grabs the basket from me and shoots through the door."

        "Rin gives me a sort of half-nod and ambles inside as well."

        "Damn, it's wet out here."

        "I need to get back to my room and into some dry clothes."

        stop ambient fadeout 2.0

        scene bg school_dormhallway
        with locationskip

        "I'm soon in front of my door, but I am intercepted by the sudden appearance of Kenji, who appears to be carrying a stack of books."

        show kenji neutral at center
        with charaenter

        ke "Hey man, give me a hand, would you?"

        hi "Huh?"

        play music music_kenji fadein 0.5

        with vpunch

        "The books are unceremoniously dumped into my arms as Kenji fumbles with his room key."

        show kenji happy
        with charachange

        ke "Thanks, you're a lifesaver."

        ke "If you weren't around I'd have to keep my door unlocked, and that's just begging for trouble."

        show kenji tsun
        with charachange

        ke "The perfect opportunity to set up an ambush, or maybe just plant a bomb if they don't want to get their hands too dirty."

        ke "Probably don't."

        ke "Afraid they'll break a nail or something if they have to stab me."

        ke "Women."

        "My mind thinks about digesting the verbal torrent that's just been unleashed, but elects to remain comfortably in the dark."

        hi "Uh… huh."

        show kenji happy
        with charachange

        ke "Anyway, where have you been, man?"

        show kenji neutral
        with charachange

        ke "I could have used some help carrying these back from the library!"

        ke "I knocked on your door, but you weren't there."

        hi "Oh, sorry."

        "Not really. You appear to think I'm some kind of pack mule."

        hi "I was out with Emi and Rin."

        show kenji rage
        with charachange

        "Kenji staggers back in shock."

        "It looks like I just shot his dog, if he had a dog."

        ke "The limbless ladies again?"

        show kenji tsun
        with charachange

        ke "What'd you do this time?"

        hi "Well, we wound up at the Shanghai—"

        "I'm prevented from continuing by a sudden exclamation of despair."

        show kenji rage
        with vpunch

        ke "The Shanghai?"

        ke "Why the Shanghai?"

        ke "No no no no, man, you can't just go to the damn Shanghai!"

        ke "It's the most dangerous place in the city!"

        ke "A veritable stronghold of their best agents!"

        ke "I know! I've met them!"

        ke "They'll stop at nothing to lull you into a false sense of security, and then BAM!"

        play sound sfx_impact2
        with vpunch

        "He hits his door for emphasis."

        ke "Wallet's gone. Bus pass? Gone. Identity? Fuckin' {b}gone{/b}, man!"

        show kenji tsun
        with charachange

        ke "Promise me you won't go there again!"

        "He seems so vehemently opposed to the idea of the Shanghai that I'm willing to lie a little in order to get to my room."

        hi "Sure, I won't go there again."

        "Or at least, I won't ever tell you I've gone there again."

        "This seems to mollify my bespectacled companion."

        show kenji neutral
        with charachange

        ke "Good, good."

        show kenji happy
        with charachange

        ke "Sorry to come on so strong, but I know the danger there too well to let you just wander into the lion's den again."

        ke "You got out of there alive once, but twice is pushing it."

        hi "Yeah, well I need to get changed and uh, do homework. So… I'll see you later."

        show kenji tsun
        with charachange

        ke "Huh?"

        show kenji neutral
        with charachange

        ke "Oh, sure. Whatever."

        "I suddenly remember that I'm still holding his books."

        hi "You'd better take these."

        "I catch a glimpse of one of titles, something about cryptography."

        "What a weirdo."

        stop music fadeout 6.0

        show kenji neutral:
            easeout 0.5 xpos 0.3 alpha 0.0

        "Kenji grabs his precious cargo from me and disappears through his doorway."

        $ renpy.music.set_volume(0.1, 0.0, channel="ambient")
        play ambient sfx_rain fadein 1.0

        scene bg school_dormhisao
        with locationchange

        "I open my own door and walk in, grateful to get out of my soaking wet clothes."

        "The rain outside picks up, and I find myself hoping that Emi's not out running in this weather. She seemed so adamant about doing the run alone, I can't help but wonder if her leg's still bothering her."

        "I try to remember whether or not I've seen her limping at all today, but I can't. Guess I was too caught up in enjoying the day, even if it did rain on us."

        "And as I think back over the events of today, I keep finding myself focusing on my running partner."

        "Her complete refusal to allow the rain to spoil her plans was incredibly cute."

        "But there was something else there, too."

        "Sort of an unflappable attitude when it comes to enjoying the day as it comes."

        "I really like that quality."

        "Maybe I need to do a little of that myself."

        stop ambient fadeout 2.0
        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .tracking_absences:
        scene black

        play sound sfx_alarmclock

        pause 2.0

        scene bg school_dormhisao
        with openeye

        "The sound of my alarm brings me out of a dream involving pirates and some other stuff I can't really remember."

        scene bg school_track
        with locationskip

        play music music_pearly

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")

        "I'm a little bleary-eyed, and it feels like it takes me longer than usual to get dressed and down to the track."

        "A glance at my watch reveals that I was right, and I am in fact running a little late."

        "The thing is…"

        "There's no Emi."

        "That's odd. She should be here."

        "She definitely should be here."

        "I mean, I was {b}late{/b}."

        "I guess I wasn't the only one who had trouble getting up this morning."

        "The thought crosses my mind that it never quite stopped raining yesterday. Did she go running anyway?"

        if run_with_emi or _in_replay:
            "It seems likely. Emi's a lot of things, but cautious isn't one of them. She probably figured the rain wouldn't stop, and that's why she was so adamant about running alone."

            "Still, I would have gladly run with her, even if it was in the rain."

            "Heck, if anything I would have been able to convince her to come in once it got really bad. That would be why she didn't want me along, of course."
        else:
            "I should have offered to run with her."

            "Then I could have talked her out of the idea, or at the least known that she was okay. What if she got struck by lightning or something?"

            "I'd never forgive myself."

            "…"

            "Okay, that's probably a little stupid."

            "Emi's a resourceful girl. I doubt even she'd stay out in a thunderstorm."

            "I trust her judgment on that matter, at least."

        "Even so, I can't help wanting to know where she is."

        "…Well, nothing for it. I'd better stretch and run, and hope that Emi shows up with a grin and an excuse."

        scene bg school_track_running
        with shorttimeskip

        scene bg school_track_on
        with Dissolve(3.0)

        "On my cool down lap, I am forced to admit that Emi isn't showing up."

        "Furthermore, I have no idea where she is. Anxiety gnaws at me while at the same time I wonder just why I'm so worried over her."

        "The run helped to take my mind off it for a little while, but now that I'm finished I'm back to worrying."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear

        nvl show dissolve

        n "{vspace=60}It was weird not having her here."

        n "Downright unnerving."

        n "It suddenly dawns on me that I've been running to hang out with Emi as much as I've been running to stay healthy - probably more to be with Emi, now that I think of it."

        n "It's one of those things that are completely obvious yet somehow, I never realized it."

        n "She really is someone I enjoy being with."

        n "As revelations go, it's hardly world-shaking."

        n "All the same, I find myself feeling slightly shocked."

        n "When did this happen?"

        n "Well, no time to think about this - though I want to ponder this new development, I have a greater desire to find out what's happened to Emi."

        n "I'll ask the nurse when I stop in to see him."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")
        stop music fadeout 2.0

        nvl clear

        nvl hide dissolve

        scene bg school_nurseoffice
        show nurse neutral at center
        with shorttimeskip

        nk "Well, you seem to be in good shape, Hisao."

        hi "That's good to hear."

        "I replace my shirt and stand to leave, as usual."

        "Except instead of leaving, I ask a question."

        hi "Hey, where's Emi? She didn't show up this morning."

        hi "Is she okay?"

        show nurse concern
        with charachange

        "While I try valiantly to conceal the anxiety in my voice, the nurse's expression suggests that I've failed miserably."

        nk "You mean she didn't tell you?"

        nk "She's sick in bed."

        hi "What? Sick?"

        show nurse neutral
        with charachange

        "The nurse shrugs."

        nk "Yeah, she came to my office early this morning with a fever."

        nk "To be honest I'm surprised she made it here."

        show nurse concern
        with charachange

        nk "She was burning up when she arrived."

        nk "I believe she'd planned to let you know, but she asked me to tell you - oh shoot!"

        stop music fadeout 2.0

        show nurse neutral
        with charachange

        "The nurse gives me a sheepish smile that seems at least partially sincere."

        nk "I told her I'd stop by the track to let you know in case she forgot to. Sorry about that."

        play music music_nurse fadein 1.0

        show nurse fabulous
        with charachange

        nk "But we don't need to tell Emi I forgot, right?"

        "I return the nurse's smile with a devious one of my own."

        hi "Oh, of course not."

        hi "This is fine blackmail material."

        hi "I'll save it for whenever I need a favor from you."

        show nurse grin
        with charachange

        "The nurse laughs."

        nk "Well, I guess I deserve that."

        nk "But you know, I've got tons of blackmail on you that you're not even aware of."

        show nurse fabulous
        with charachange

        nk "So don't push your luck, okay?"

        "My expression earns another laugh from the nurse."

        show nurse grin
        with charachange

        nk "I'm just kidding, Hisao."

        show nurse concern
        with charachange

        nk "But seriously - don't tell Emi I forgot, okay?"

        hi "Your secret is safe with me."

        show nurse neutral
        with charachange

        nk "Oh good. Now go on, get out of here."

        hi "Wait, I've got one more question."

        show nurse fabulous
        with charachange

        nk "Shoot."

        hi "Is she going to be okay?"

        show nurse grin
        with charachange

        nk "Oh yeah, definitely."

        show nurse neutral
        with charachange

        nk "Her fever was high, but it was already starting to go down by the time she came by my office."

        nk "I'll probably check up on her again at lunch to be sure, but I expect she'll be up and about by the evening no matter what I tell her."

        hi "Hmm, maybe I should visit her after class."

        "It takes me a second to realize I've spoken aloud."

        show nurse fabulous
        with charachange

        "The nurse raises an eyebrow and gives me a searching glance for a moment."

        nk "Hmm…"

        show nurse neutral
        with charachange

        nk "Well, it might not be a bad idea."

        nk "You could let me know if she'd taken a turn for the worse, I guess."

        show nurse concern
        with charachange

        nk "But no funny business, you got it? I know what meds you're on, after all."

        "I think that's a threat against my life, but I'm not sure."

        stop music fadeout 7.0

        scene bg school_nursehall
        with locationchange

        "Either way, I assure the nurse that my intentions are chaste and exit the office."

        "Interesting that the nurse sees me as some sort of potential suitor to Emi."

        "Even more interesting is how pleased that makes me feel."

        "I need a shower."

        scene bg school_scienceroom
        with shorttimeskip

        play sound sfx_normalbell

        "The lunch bell rings, and I find myself disinclined to make my way up to the roof."

        "After all, I'm betting Rin knows where Emi is, and if that's the case then I doubt she'd bother going up there."

        "More to the point, I doubt we'd have any sort of scintillating conversation if she did. Chances are she'd prefer to be alone up there anyway, so I don't accidentally ruin her train of thought or something."

        "Unfortunately, I don't really feel like heading to the cafeteria either."

        "Guess I'll go to the library instead."

        "I need a new book to read anyway, having finished my other one yesterday before bed. Maybe I can find more by the same author."

        scene bg school_library
        with locationskip

        play music music_happiness fadein 2.0

        "I love libraries."

        "They smell like dust and paper and ink."

        "All these stories and facts and opinions crowded together in one place makes the air come alive with potential."

        "I'm not sure how to navigate Yamaku's library yet, having mostly stuck to books I brought with me, so I search for the librarian to ask for help."

        "…"

        "Hmm. I suppose she's not arou—{w=0.5}{nw}"

        show yuuko smile_down:
            center
            xpos 0.4
            easein 0.5 center
        with charaenter

        show yuuko at center

        yu "…can't believe it."

        "Yuuko, looking rather distracted, suddenly emerges from one of the aisles."

        hi "Er, excuse me."

        show yuuko neutral_down
        with charachange

        yu "Oh, can I help you?"

        hi "Actually, I was looking for a book…"

        show yuuko panic_up
        with charachange

        yu "So am I!"

        show yuuko smile_down
        with charachange

        yu "'Advanced Cryptography.' We just got it in, and now it's gone missing."

        show yuuko worried_up
        with charachange

        yu "I really, really wanted to read that one!"

        hi "Cryptography?"

        show yuuko neurotic_up
        with charachange

        yu "Yeah, my… er, that is…"

        yu "This guy I knew. Know. Um."

        yu "Not sure how to describe it…"

        hi "Skip to the end."

        show yuuko smile_down
        with charachange

        yu "He got me interested in cryptography only now the book's gone, and I think it's been stolen!"

        hi "Sounds pretty terrible."

        show yuuko worried_up
        with charachange

        yu "Yeah, especially because now I have to search the whole library for it!"

        yu "Even though it's probably not even here!"

        hi "You seem… busy."

        show yuuko neurotic_up
        with charachange

        yu "A little."

        show yuuko neurotic_up:
            easeout 0.5 xpos 0.6 alpha 0.0

        "She dashes off down another aisle, and I resign myself to finding my own damn book."

        "Hmm, plenty of choices."

        stop music fadeout 2.0

        scene bg school_library
        with shorttimeskip

        "Oh come on, how did I get lost?"

        "These aren't even printed books! They're all in Braille."

        "I guess that makes sense in a school like this, but honestly, it's a little annoying."

        li "I'm sorry, is someone there?"

        "A lilting voice drifts out from behind one of the cubicles set up for research."

        show lilly basic_displeased at center
        with charaenter

        "As I approach, I see that Lilly's been reading a book while I've been stomping about the aisles."

        hi "Oh no, I should be apologizing. I didn't mean to make so much noise."

        show lilly basic_ara
        with charachange

        li "My, is that you Hisao?"

        show lilly basic_smile
        with charachange

        li "I've not heard from you in quite some time."

        show lilly basic_pout
        with charachange

        li "I was beginning to think you'd forgotten all about me."

        hi "Er, sorry."

        play music music_lilly fadein 4.0

        show lilly basic_giggle
        with charachange

        "Lilly laughs in that refined manner of hers and shakes her head."

        show lilly basic_smile
        with charachange

        li "I'm only teasing you, Hisao."

        li "From what I hear, you've been busy."

        show lilly basic_cheerful
        with charachange

        li "Morning runs with Emi Ibarazaki {b}and{/b} lunch on the rooftop, if I'm not mistaken."

        hi "Heh, yeah."

        hi "Guess word gets around pretty quickly."

        show lilly basic_weaksmile
        with charachange

        li "That and I can't coax poor Hanako on the roof any more."

        show lilly basic_displeased
        with charachange

        li "You three are always up there, claiming the spot for yourselves."

        "She chides me gently, though it's pretty clear she's just teasing me again."

        "Still, I feel an odd need to apologize."

        hi "Sorry, we could eat lunch somewhere else if it's a real problem—"

        show lilly basic_ara
        with charachange

        li "Oh no, I wouldn't worry about it."

        show lilly basic_smile
        with charachange

        li "Hanako and I have other things to do at lunch, too."

        li "Such as read in the library, as you can see."

        hi "Oh, Hanako's here too? I didn't see her."

        show lilly basic_smileclosed
        with charachange

        "Lilly smiles, a bit enigmatically."

        li "Oh, she's around somewhere."

        show lilly basic_smile
        with charachange

        li "But I'm surprised, Hisao. You're in here, instead of up there."

        li "What brings you to the library?"

        hi "Well, Emi's ill, so there's no lunch on the rooftop to keep me occupied…"

        show lilly basic_giggle
        with charachange

        "Lilly raises an eyebrow at my statement before giving another chuckle."

        li "My, poor Rin must feel left out."

        hi "It's not like that!"

        show lilly basic_weaksmile
        with charachange

        li "Ah, but I'm sure it isn't. Emi tends to be the life of whatever group she's in."

        show lilly basic_sad
        with charachange

        li "It's a shame to hear she's fallen ill. Will she be okay?"

        "Somehow I get the feeling that Lilly's just inquiring out of politeness, but I respond anyway."

        hi "The nurse thinks so. I'm going to swing by and see how she's doing after school myself."

        show lilly basic_smileclosed
        with charachange

        "Another raised eyebrow."

        li "My, what a noble gentleman you are, Hisao."

        hi "It's nothing, really. Just checking up on my friend, after all."

        show lilly basic_planned
        with charachange

        li "Ah, so it's just friends, is it? How disappointing."

        "I blush, glad that Lilly can't see it."

        show lilly basic_giggle
        with charachange

        "But somehow she knows that I've been flustered by her comment anyway, and laughs."

        li "I'm sorry, Hisao. I'm teasing you again."

        show lilly basic_smile
        with charachange

        li "Please do tell Emi that I hope she feels better, won't you?"

        "A glance at my watch reveals that I'm very nearly out of time to find my book."

        hi "Of course."

        hi "Hey, I've got to find a book before lunch is over, so I'd better get moving."

        hi "See you later."

        "That was probably not the best phrase to use."

        "Lilly, however, takes my gaffe in stride."

        show lilly basic_weaksmile
        with charachange

        stop music fadeout 3.0

        li "Until we meet again, Hisao."

        scene bg school_hallway2
        with shorttimeskip

        "I never do find the book I was looking for, but I walk out with something else instead."

        "My stomach growls slightly, letting me know that I should have had something for lunch."

        "Oh well."

        "I'll grab something before I visit Emi later."

        if _in_replay:
            return

    label .dropping_by:
        scene bg school_hallway2

        scene bg school_scienceroom
        with shorttimeskip

        play music music_normal fadein 3.0

        "It seems as if time has decided to slow down for the express purpose of annoying the hell out of me."

        "Class feels like it drags on for ages."

        "I suspect that my being consumed with worry probably has something to do with it."

        play sound sfx_normalbell

        "Blessedly the bell rings and I dash out of class, drawing a few raised eyebrows, I'm sure."

        scene bg school_hallway3
        with locationchange

        "I have spent the majority of the day fretting as unobtrusively as I could."

        "Even though the nurse thinks that Emi is perfectly okay, I want to see for myself."

        stop music fadeout 14.0

        scene bg school_girlsdormhall
        with locationskip

        "It doesn't take long to get to the girls' dormitory and make my way to Emi's room."

        "Standing outside her door, I suddenly pause. What if she's resting?"

        "I'd hate to wake her up, especially if she's still feeling ill."

        "Then again, if she sleeps all day then it could throw off her sleeping schedule."

        "But rest is important if you're ill, isn't it?"

        "I can't decide what to do, so I settle for standing outside the door looking like an idiot."

        "Then I hear Emi's voice from behind the door."

        emi "Thanks for your concern, but I really am okay."

        "Is she talking to me?"

        emi "I'll see you at practice tomorrow!"

        "Guess not."

        "Still, clearly she's not asleep, so I can knock without worry."

        "So why this clenched feeling in my gut? I wasn't nervous about dropping by the other day, so why today?"

        "Granted, I still haven't really had time to figure out this newfound interest in Emi's well-being."

        "I don't have a lot of experience in the matter, of course, but certainly this seems to go beyond feelings of mere friendship."

        "But could I take that step? Could I even bring myself to risk what I have right now?"

        "I mean it's enough to be friends with her, isn't it?"

        "Either way, shouldn't I just open the door and see how she's doing? That's why I came here… right?"

        stop music fadeout 1.5

        "What if she's not dressed yet?"

        play ambient sfx_heartslow

        with Fade (0.05, 0.0, 0.3, color="#ffc0cb")

        "The image that flashes through my mind causes my heart to skip a beat, literally."

        stop ambient fadeout 3.0

        "I should probably not ever think those thoughts again. Not if I want to avoid a heart attack."

        "I suddenly realize I'm still standing in the hallway looking like an idiot."

        play sound sfx_doorknock2

        "Emi still seems to be in the middle of a conversation, but I knock anyway. Hopefully she won't mind the interruption."

        emi "You worry too mu— Come in! The door's unlocked."

        "So it is. I open the door and step in, which is about where my thought process comes to a grinding halt."

        play music music_serene fadein 4.0

        scene ev emi_sleepy_face:
            center
            zoom 1.05
            ease 15.0 zoom 1.0
        with whiteout

        "Emi is sitting up in bed, her hair tousled from a day spent asleep. I think this is the first time I've seen her without those familiar beads in her hair."

        "Her gym shirt and bloomers, obviously hastily pulled on before I came in, are creased and folded from less than proper storage."

        scene ev emi_sleepy_legs:
            xalign 0.0
            warp acdc_warp 8.0 xalign 1.0
        with flash

        "Her legs lay bare on the sheets."

        "I've never seen Emi without prosthetics before. Yet here she is, slender legs terminating in stumps just below her knees."

        "But as odd as the sight is, I find myself more captivated by everything north of the waist."

        scene ev emi_sleepy:
            center
            zoom 1.05
            ease 15.0 zoom 1.0
        with flash

        "It seems that Emi had finished her conversation with whoever was on the phone with her, and is now watching my reaction closely out of her one open eye as she wipes sleep from the other."

        "Her expression, far from being embarrassed, is rather one of a surprisingly wide yawn. One perhaps appropriate from such a small mouth."

        "A grin that for a brief moment seems almost flirtatious tugs at the corner of her mouth as she takes the sight of me in."

        "I can do nothing but remain in a state fluctuating between fear, confusion, and not a little bit of lust."

        "Emi hastily sweeps her hair out of her eyes, fixing it back into place before addressing me."

        scene bg school_dormemi
        show emi sad_grin_gym at center
        with locationchange

        emi "You seem a bit caught off guard, Hisao."

        "A wave of laughter erupts from her, and I find myself grinning and rubbing the back of my head ruefully."

        hi "Sorry, I've just…"

        "Never seen someone so disheveled look so attractive."

        "Never seen you without your legs on."

        "Never seen you look so…"

        hi "Um, sorry."

        show emi basic_closedgrin_gym
        with charachange

        "Emi giggles again and moves to sit up a little straighter."

        "I'm caught up in the movements of her shirt, very nearly losing myself."

        show emi basic_grin_gym
        with charachange

        emi "I was wondering what your reaction would be."

        show emi basic_closedhappy_gym
        with charachange

        emi "The nurse called and told me you were going to drop by, you see."

        show emi basic_grin_gym
        with charachange

        emi "And I know you haven't seen me… well, you know."

        show emi sad_grin_gym
        with charachange

        emi "Without legs."

        "I respond in a tone of casual surprise."

        hi "Oh, you don't have them on? I didn't notice."

        "This is almost the truth. I very nearly didn't."

        "I'm not trying to be suave or anything, mind you. Somehow I think Emi would get offended by that."

        stop music fadeout 0.5
        play sound sfx_pillow
        show emi basic_annoyed_gym
        with vpunch

        "Instead, she sticks her tongue out at me and chucks a pillow at my head."

        emi "Ass."

        "I deftly catch the pillow and take careful aim before throwing."

        play music music_running

        show emi basic_annoyed_gym:
            center
            parallel:
                ease 0.5 xpos 0.7
            parallel:
                "emi basic_closedhappy_gym" with Dissolve(0.5)

        "Emi laughs and rolls to one side, dodging my shot, the shifting of her shirt distracting me enough so that the next thrown pillow hits me right between the eyes."

        play sound sfx_pillow

        hi "Oof!" with hpunch

        "I retaliate, of course."

        "And once I've retaliated twice, well, a war was bound to break out sooner or later."

        "And really, when Emi appears to have far better aim than me, well…"

        "It was just a matter of time before I'd have to resort to a suicidal charge."

        show bg school_dormemi:
            ease 0.5 bgleft
        with None
        show emi basic_closedhappy_gym_close:
            ease 0.5 center
        with characlose

        show emi at center

        hi "Gotcha!"

        show emi basic_hes_gym_close
        with charachange

        emi "Eep!"

        play sound sfx_pillow

        show comic vfx1
        show emi basic_closedsweat_gym_close
        with vpunch

        pause 0.5

        play sound sfx_pillow

        show comic vfx2
        with hpunch

        pause 0.5

        play sound sfx_pillow

        show comic vfx3
        with vpunch

        pause 0.5

        show comic vfx3:
            truecenter
            easeout 0.5 yanchor 0.3 alpha 0.0

        pause 0.5

        stop music fadeout 3.0

        scene black
        with dissolve

        "And once the charge was accomplished, well, of course I'd have to wrestle the pillows away from her."

        "And with that kind of struggle, of course we'd wind up in this sort of position."

        play music music_twinkle fadein 2.0

        scene ev emi_bed_full:
            xalign 0.5 yalign 1.0
            easein 15.0 yalign 0.0
        with Dissolve(1.0)

        pause 3.0

        "And so I find myself staring down at her from my position atop her."

        "She's grinning, eyes sparkling with amusement, maybe a little sweaty now from our tussle."

        "Her chest is heaving up and down, sucking in air."

        "The small bit of my brain that is not currently enraptured by the sight and the smell of her observes that she must still be ill, because her stamina's not what it should be."

        "We stay that way for a while."

        "I'm not sure how long, because everything seems to go fuzzy. Everything that isn't her, anyway."

        "Her eyes meet mine, and deep inside them I almost catch a glimpse of… what, fear? Longing?"

        "Hope?"

        hi "Emi…?"

        stop music fadeout 0.5

        show ev emi_bed_unsure at center
        with vpunch

        "A cough suddenly convulses her, and I'm almost stumbling in my haste to get off, to apologize for everything."

        play music music_emi fadein 3.0

        hi "Sorry, I shouldn't have…"

        show ev emi_bed_happy
        with charachangeev

        emi "It's fine, it's fine."

        "She gives me a reassuring pat on the shoulder."

        show ev emi_bed_normal
        with charachangeev

        emi "So… what brings you here?"

        "She's still breathing hard, and that causes her voice to shake slightly."

        hi "Well, before I was so rudely assaulted by pillows, I came to see how you were doing."

        play sound sfx_pillow

        show comic vfx4 at truecenter
        show ev emi_bed_frown
        with vpunch

        pause 0.5

        show comic:
            easeout 0.5 yanchor 0.3 alpha 0.0

        pause 0.5

        hide comic

        "This earns me another shove, and I very nearly fall off her bed."

        show ev emi_bed_normal
        with charachangeev

        "Emi's eyes sparkle again, and I wonder how I never noticed how attractive they are before."

        show ev emi_bed_smile
        with charachangeev

        emi "Consumed with worry, were you?"

        "Her tone is mocking, haughty. Teasing."

        "She throws her arm across her forehead dramatically, grin still apparent from underneath."

        show ev emi_bed_unsure
        with charachangeev

        emi "Couldn't bear the thought of me laying deathly ill?"

        "As we both recover from our brief wrestling match, Emi appears to fall back on teasing me."

        hi "Well, I wouldn't say consumed with worry, but after you didn't show up this morning like a total wuss…"

        show ev emi_bed_frown
        with charachangeev

        "Emi pouts, crossing her arms petulantly and sticking her lower lip out."

        emi "It's not my fault."

        emi "Nurse wouldn't allow it."

        hi "Sure he wouldn't. I completely believe you."

        "Emi sticks her tongue out again."

        emi "You're such a jerk, Hisao."

        hi "So how was your day then, eh? Did you enjoy slacking off?"

        show ev emi_bed_normal
        with charachangeev

        emi "Not really, the phone woke me up pretty early on."

        hi "The phone?"

        emi "Yeah, the captain of the team called to make sure I was doing okay."

        emi "Also to let me know it was okay to skip practice."

        "Good, at least she wasn't alone all day. Someone checked up on her."

        "Although I can't help but think that it should have been me."

        hi "Oh, that's good."

        hi "He really keeps an eye on you, huh?"

        show ev emi_bed_smile
        with charachangeev

        "Emi shrugs."

        emi "It's his job."

        emi "Part of being the captain means you know where your team members are when they're not in school."

        emi "Still, I guess it was nice of him to call, huh?"

        hi "Yep. Sure was."

        "Emi yawns and shimmies down into a more comfortable position."

        show ev emi_bed_normal
        with charachangeev

        emi "So how was your day?"

        hi "Kind of uneventful, you know?"

        hi "I went ahead and ran by myself, and talked with the nurse about how you were doing…"

        stop music fadeout 2.0

        scene bg school_dormemi_ni
        with shorttimeskip

        "I meander through the day's events, none of which are particularly engrossing."

        "That's when I'm distracted by an arm finding its way across my waist."

        "It seems that Emi fell asleep while I was talking so I draw her blanket to cover us."

        play music music_comfort fadein 9.0

        scene ev emi_sleep_unsure
        with locationchange

        "She's rolled over on to her side, and now one leg is thrown over my legs, effectively trapping me."

        hi "Hey."

        "It seems a shame to wake her, but I have things to do."

        play sound sfx_rustling

        "I gently shake her, but in response she only tightens her arm's grip on me and sighs a little."

        "My resistance to this position crumbles rather quickly."

        "The feeling of her body breathing steadily is both calming and incredibly stimulating at the same time."

        "My breathing cannot decide if it wants to relax or speed up."

        "Relaxation wins, and I find myself putting an arm around Emi."

        scene ev emi_sleep_normal
        with charachangeev

        hi "I think I'm in love."

        "The words slip out and hang in the air unnoticed."

        "At least I hope they've gone unnoticed."

        scene ev emi_sleep_weep
        with charachangeev

        "Emi whimpers weakly through her dream, and her grip suddenly tightens again."

        "For the first time since I've known her, I see tears running down Emi's face."

        "It feels like my heart is about to break."

        "I instinctively tighten my own grip and stroke her hair in what I hope is a soothing manner."

        "Words of comfort, meaningless in this situation, spring to mind."

        "Maybe I should wake her. Are you supposed to wake people having nightmares?"

        "I can't for the life of me remember."

        "The decision is taken from me as Emi suddenly jerks awake with a cry."

        scene ev emi_sleep_cry
        with charachangeev

        emi "Dad!"

        "This is… more than I think I want to hear without her knowing. I quickly sit upright and gently shake her shoulder to stir her."

        scene bg school_dormemi_ni
        with locationchange

        hi "Hey, you okay?"

        "What a silly question."

        show emi basic_shock_gym_close_ni at tworight
        with charaenter

        emi "Huh? What?"

        show emi basic_hes_gym_close_ni
        with charachange

        emi "Hisao?"

        "She shakes her head as if to clear it and quickly wipes her eyes."

        hi "You had a nightmare. I think."

        show emi sad_shy_gym_close_ni
        with charachange

        "Emi shudders again and glances up at me a little cautiously, as if unsure whether or not she's actually up."

        emi "Y-yeah, I guess so."

        hi "You wanna talk about it?"

        emi "Hmm?"

        "A speedy internal debate seems to be going on in her head, which resolves itself with a shrug."

        show emi basic_hes_gym_close_ni
        with charachange

        emi "Nah, I don't really remember much of it."

        "I'm pretty sure she's lying to me, but somehow I don't think I should press the issue."

        show emi sad_shyblush_gym_close_ni
        with charachange

        "Emi shudders again and turns toward me, looking a little sheepish."

        emi "Sorry for falling asleep on you like that."

        "I keep my voice as soothing as I can."

        hi "Hey, don't worry about it. You've been ill."

        emi "Yeah, I guess that cold medicine's just made me a little drowsy."

        hi "I guess so."

        "Emi does not strike me as the sort of person who'd fall asleep at the drop of a hat."

        "Rin, maybe. But Emi's far too energetic."

        show emi basic_grin_gym_close_ni
        with charachange

        "Emi gives a half-smile at my response, and then just like that she's back to her old self."

        show emi basic_closedgrin_gym_close_ni
        with charachange

        emi "Well, prepare yourself for tomorrow morning Hisao!"

        show emi excited_proud_gym_close_ni
        with charachange

        emi "We'll have to go twice as hard to make up for today!"

        hi "But I went running this morning!"

        show emi basic_annoyed_gym_close_ni
        with charachange

        emi "No excuse!"

        hi "Oh fine, I'll be ready for you!"

        show emi basic_grin_gym_close_ni
        with charachange

        "Emi nods, satisfied."

        emi "Good."

        "I take this as my cue to exit."

        hi "Well, I'd better get going. Especially if I want to get enough sleep for tomorrow."

        show emi basic_grin_gym_ni
        with vpunch

        "I hop off the bed and head for the door."

        show emi sad_shy_gym_ni
        with charachange

        emi "Hey, Hisao…"

        hi "Hmm?"

        "I pivot neatly on my heel and face Emi."

        show emi basic_hes_gym_ni
        with charachange

        "She opens her mouth to say something, and then in another first, I see her falter slightly."

        "She closes her mouth and opens it again."

        show emi sad_grin_gym_ni
        with charachange

        emi "…Thanks."

        emi "For dropping by, I mean."

        emi "You're kind of the first visitor I've ever had who wasn't Rin."

        "Now that's surprising. I would figure that Emi'd have people dropping by all the time."

        "She's certainly popular enough, or so I thought. Always talking to people in the hallways."

        show emi sad_shy_gym_ni
        with charachange

        "Emi hesitates again."

        emi "And thanks for staying around after I… well."

        show emi sad_depressed_gym_ni
        with charachange

        "A look of pain flits across her face."

        emi "You know."

        show emi sad_grin_gym_ni
        with charachange

        emi "It helped."

        show emi basic_closedgrin_gym_ni
        with charachange

        "She brightens back up and waves cheerily at me."

        emi "See you tomorrow!"

        hi "Yeah, see you later."

        "I'm just about to exit the door when something makes me turn around again."

        hi "Hey, Emi."

        show emi basic_grin_gym_ni
        with charachange

        emi "Hmm?"

        hi "Anytime you need to talk, let me know, okay?"

        show emi sad_shy_gym_ni
        with charachange

        "Emi seems taken aback by this offer."

        show emi basic_closedgrin_gym_ni
        with charachange

        "Her grin gets even wider."

        emi "Sure thing, Hisao."

        show emi basic_grin_gym_ni
        with charachange

        emi "See you in the morning!"

        scene bg school_girlsdormhall_ni
        with locationchange

        "I exit Emi's room with my head in a whirl."

        "Should I have even left?"

        "Was she really okay?"

        "I want to turn around and march back down the hallway, open the door and tell her…"

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear

        nvl show dissolve

        n "{vspace=60}Tell her I love her, tell her I think she's beautiful, tell her that I'll be there when she needs me."

        n "I want to stay with her, to hold her close as she falls back to sleep."

        n "How many nights has she woken up like that?"

        n "Only to find that nobody's there."

        n "I want to be that person she can be with when that happens."

        n "It's a silly thought, I know."

        n "We don't know each other that well, do we?"

        n "The whole idea, while exhilarating, also makes me feel worry."

        n "Worry, perhaps, that I'd overstep my bounds."

        n "And now to add to my troubles, it seems as if Emi herself already has an interest in someone else."

        nvl clear

        n "{vspace=180}This track captain of hers who seems so interested in her well-being."

        n "True, I've only seen the two of them together a few times, but that doesn't change the fact that they seem better suited to one another."

        n "There's really nothing to be done about that."

        n "I need to take my mind off of this whole situation."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")

        nvl clear

        nvl hide dissolve

        "I've got homework to do."

        "Maybe that will distract me."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .the_first_morning_after:
        scene black

        scene bg school_dormhisao
        with openeye

        "A night of restlessness has left me feeling fairly groggy this morning."

        play music music_drama fadein 8.0

        "The events of the previous day keep intruding upon my mind."

        "The memory of how Emi felt against me."

        "The memory of our wrestling match."

        "And most bothersome, the memory of her nightmare."

        "She was in so much pain."

        "I can't stop wondering what it must be like for her to wake up with nobody there."

        scene bg school_dormbathroom
        show steam
        with locationskip

        play ambient sfx_shower fadein 1.0

        "The shower shocks me awake with hot water. Awake, but still worried."

        $ renpy.music.set_volume(0.5, 1.0, channel="ambient")
        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl show dissolve

        nvl clear

        n "{vspace=30}What will happen today?"

        n "Will things just go back to normal?"

        n "End of the episode, back to the status quo?"

        n "There was a connection yesterday. Something that nearly pushed us past the boundaries of normal friendship."

        n "Would that have been so bad?"

        n "My mind goes back to the look in Emi's eyes after our pillowfight. It almost seemed like she was daring me to go on."

        n "Almost."

        n "But I can't know for sure."

        n "Anyway, the track captain's probably first in her affections."

        n "But even as I say that, my mind is already snorting derisively. I'm just looking for an excuse. A reason for everything to go wrong."

        n "A reason to not try."

        nvl clear

        n "{vspace=120}It's not as if I've even seen the two of them together outside of track practice."

        n "And clearly he's never visited. Emi said as much herself. If they were close, surely he'd visit."

        n "I'm such a wuss."

        n "I ought to just go for it anyway, damn the consequences."

        n "That's what Emi would do, I think. Hell, I {b}know{/b} that's what she'd do."

        n "Which is partially why I'm convinced there's no interest on her end. She hasn't acted either."

        n "Maybe because of this track captain. It's possible she's got a bit of an unrequited crush thing going on."

        nvl clear

        n "{vspace=180}But who would be able to clarify their relationship?"

        n "It sure as hell can't be Emi. She'd probably just laugh and ask why I wanted to know… and I'm not ready to answer that yet."

        n "Rin… Rin would probably just give me some cryptic answer or something. And then with my luck, she'd just ask Emi, who would ask me why I wanted to know, and I've already covered that problem."

        n "I wonder…"

        nvl clear

        n "{vspace=150}Could I get away with asking the nurse? He seems pretty protective of Emi. I'm sure he'd know if something was up…"

        n "And he owes me for not letting Emi know he forgot to tell me about her being ill, so he'll keep quiet."

        n "What if he asks me why I want to know, though?"

        n "I can shake him off. Just say I'm curious as a friend. He'll buy that, won't he?"

        n "Of course!"

        n "That's settled, then."

        n "After the run, I'll talk to him while Emi's waiting outside the office."

        stop ambient fadeout 2.0

        nvl clear

        nvl hide dissolve

        scene bg school_track
        with locationskip

        nvl show dissolve

        n "{vspace=120}There's no sign of Emi when I arrive at the track. Is she still too ill?"

        n "I decide to give her ten minutes."

        n "I'm a little early, and she was ill yesterday, so if she takes a while to show up it shouldn't be surprising."

        n "Still, I'd hate to just waste my time, so I occupy myself by stretching and pacing back and forth anxiously."

        n "What if I went too far yesterday?"

        n "What if she doesn't come because she's embarrassed?"

        n "What if…"

        $ renpy.music.set_volume(1.0, 2.0, channel="music")
        $ renpy.music.set_volume(1.0, 2.0, channel="ambient")

        nvl clear

        stop music fadeout 2.0

        nvl hide dissolve

        show emi basic_closedgrin_gym at center
        with charaenter

        emi "You're early again, Hisao!"

        show emi excited_proud_gym
        with charachange

        emi "I'm impressed!"

        "Just like that, I feel some of the tension leaving my body."

        "Emi seems to be bright and cheerful as usual, with no sign that she even was ill the other day, much less had a less-than-restful sleep."

        "Still, I have to ask."

        hi "Sleep well last night?"

        play music music_serene

        "It's just a throwaway question. Small talk."

        "The sort of thing people ask someone they bump into in the café while getting their morning coffee."

        "But not for us. At least, not for me."

        "I don't know if Emi realizes that I'm actually concerned about how well she slept last night, but the question does give her pause."

        show emi basic_grin_gym
        with charachange

        "After a short moment of what seems like her genuinely pondering this, she nods."

        show emi basic_closedhappy_gym
        with charachange

        emi "Yep! Sure did!"

        "Was it because of me?"

        "Did I actually help?"

        "Or are you just saying that to get me to stop asking questions?"

        hi "Good to hear."

        show emi basic_closedgrin_gym
        with charachange

        "Emi grins and begins warming up."

        show emi basic_grin_gym
        with charachange

        emi "So, ready to begin?"

        hi "Pfft, am I ready? Of course I'm ready! I was born ready!"

        show emi basic_closedhappy_gym
        with charachange

        "Emi laughs at my bravado, and we take off running."

        scene bg school_track_running
        with shorttimeskip

        "I keep a steady pace the whole time, breathing steadily."

        scene bg school_track_on
        with Dissolve(2.0)

        "I still feel dead at the end, but at least I don't gasp like a fish out of water now."

        show emi basic_happy_gym:
            center
            xpos 0.6
            easein 0.5 center
        with charaenter

        show emi at center

        "Emi is positively beaming after the run today."

        emi "Nice job, Hisao! You're improving!"

        show emi basic_closedgrin_gym
        with charachange

        emi "You'll be half as fast as me in no time!"

        "This last line is delivered with a teasing grin that I've grown all too used to."

        hi "Oh, how exciting."

        play ambient sfx_emisprinting

        $ renpy.music.set_volume(0.3,1.0,channel="ambient")

        show emi at offscreenleft
        with charamovefaster

        hide emi

        "Emi begins to run her sprints while I take a cool-down lap."

        "She's really pushing herself today."

        stop ambient fadeout 1.0

        scene bg school_track
        with shorttimeskip

        $ renpy.music.set_volume(1.0,0.0,channel="ambient")

        "By the time I'm done with my lap, she's laying across one of the bleachers, looking exhausted."

        hi "Goodness, not pushing it a little too much today, are you?"

        hi "You did just have a cold, you'll recall."

        show emi basic_annoyed_gym at center
        with charaenter

        "Emi gives an annoyed snort and sits up."

        emi "Bah! I'm just trying to make up for lost time, that's all."

        show emi excited_happy_gym
        with charachange

        emi "I went twice as hard today, you know."

        show emi excited_laugh_gym
        with charachange

        emi "A good run always gets the kinks out, you know."

        show emi basic_closedgrin_gym
        with charachange

        emi "Clears the mind, too."

        hi "Oh?"

        show emi excited_happy_gym
        with charachange

        "Emi nods vigorously."

        show emi excited_amused_gym
        with charachange

        emi "Yep! It's a great outlet for that sort of thing."

        "She does not explain further, and I don't ask."

        "I suspect I know the real reason she went so hard today."

        "Being sick had nothing to do with it. Something's bothering her."

        "Maybe the nightmare. Maybe something else."

        "But it's not my place to pry."

        "She'd tell me if she wanted me to know."

        hi "I'm sure that comes in handy."

        show emi basic_grin_gym
        with charachange

        emi "You have no idea."

        "The sincerity in her voice confirms my suspicion."

        "The only problem is…"

        "Even though I know she'd tell me if she wanted me to know, I still want to know."

        hi "Something on your mind, then?"

        "Emi doesn't seem surprised by my question."

        show emi basic_closedgrin_gym
        with charachange

        "Instead, she shrugs."

        show emi sad_grin_gym
        with charachange

        emi "Nah, it's nothing worth getting worried about."

        "She seems as if she's trying to convince herself as much as she's convincing me."

        "I open my mouth to ask if yesterday is responsible for her current state of mind, but think better of it."

        "Too much risk of her taking the question the wrong way."

        "Besides, I'm not even sure myself what to think about yesterday."

        "Really I can only get about as far as how it felt to have Emi sleeping next to me before my brain shuts down."

        "Having her before me now, covered in sweat and looking wryly at me, she's making it difficult to think."

        hi "Yeah, I hear you."

        show emi basic_hes_gym
        with charachange

        emi "We'd better hurry to see the nurse. We're running short on time."

        hi "Aren't we always?"

        show emi basic_grin_gym
        with charachange

        "Emi laughs at this, a dry chuckle that seems most un-Emi-like."

        show emi sad_grin_gym
        with charachange

        emi "Too true."

        "For a brief moment, she looks old, worn down by some old hurt."

        "But just like yesterday I can almost see her shouldering the burden and straightening up slightly."

        "And then she's back to being Emi again."

        show emi excited_proud_gym
        with charachange

        emi "Come on then Hisao. Race ya!"

        play ambient sfx_emisprinting

        show emi at offscreenleft
        with charamovefaster

        hide emi

        stop ambient fadeout 2.0

        "With a sudden smile, she darts off."

        hi "Hey! No fair!"

        "I take off after her, knowing I won't catch her but not caring."

        "Even if there's no chance of catching her, I'll still run after her."

        stop music fadeout 2.0

        scene bg school_nursehall
        show emi basic_grin_gym at center
        with locationskip

        "Emi's waiting for me at the door as I arrive."

        show emi basic_closedhappy_gym
        with charachange

        emi "Well well, look who's finally shown up!"

        hi "Yeah, yeah."

        hi "Enjoy your victory while you can."

        show emi basic_closedgrin_gym
        with charachange

        "Emi grins as the nurse pokes his head out of the door."

        show nurse neutral:
            xpos 0.0 xanchor 0.5
            easein 0.5 xpos 0.1
        with charaenter

        show nurse:
            xpos 0.1 xanchor 0.5

        nk "Well, there you are."

        nk "Come on in, Hisao."

        play music music_nurse fadein 1.0

        scene bg school_nurseoffice
        show nurse neutral at center
        with locationchange

        "In what has become a familiar routine by now, he checks my blood pressure and my heart rate."

        show nurse fabulous
        with charachange

        nk "A bit fast today, isn't it?"

        hi "Yeah, I kind of raced Emi here."

        show nurse grin
        with charachange

        "The nurse laughs."

        nk "That's never a good idea!"

        show nurse neutral_close
        with characlose

        "He leans in to whisper to me in a conspiratory manner."

        show nurse fabulous_close
        with characlose

        nk "I don't know if you've heard… but Emi's a bit of a track star."

        show nurse fabulous
        with vpunch

        "I reel back in mock surprise."

        hi "Really? She never mentioned it before!"

        show nurse grin
        with charachange

        "The two of us share a laugh."

        show nurse neutral
        with charachange

        nk "Did she do okay today?"

        nk "Cold seemed to bother her?"

        hi "Why don't you ask her?"

        show nurse concern
        with charachange

        "He rolls his eyes in exasperation."

        nk "Of course I'm going to ask her too, but she'll tell me that she didn't have any problems, regardless of whether or not she did."

        show nurse fabulous
        with charachange

        nk "So I'm asking you, because you're her friend and would probably tell me if she had trouble today."

        "When he puts it that way, it makes a lot more sense."

        hi "She seemed pretty good today, if a little more tired than usual."

        hi "She was already feeling better when I dropped by yesterday, so I'm not that surprised."

        show nurse neutral
        with charachange

        "The nurse nods, though I notice he tenses slightly when I mention yesterday's visit."

        nk "Well, that's good to hear."

        nk "I figured it was just a 24-hour thing. Emi tends to recover quickly from colds and the like."

        hi "Hey, speaking of Emi…"

        hi "Are she and the track captain…? Well, you know."

        show nurse fabulous
        with charachange

        "A look of suspicion crosses his face."

        nk "Why do you ask?"

        hi "Well, it's just that they seem kind of close, and I was just curious, you know?"

        hi "And I'd never ask her, because that would be kind of embarrassing."

        "So far, so good. Now to really sell it."

        hi "Besides, I think they'd make a cute couple."

        show nurse grin
        with charachange

        "The nurse laughs."

        nk "Well, I don't suppose you're the first to think that."

        nk "But I think I can say with some certainty that the two of them will never do anything like that."

        hi "Certainty?"

        show nurse neutral
        with charachange

        nk "Yep."

        show nurse fabulous
        with charachange

        nk "Not that I could tell you, of course. Confidentiality and all that."

        hi "Yeah right, you just like holding a secret over my head."

        show nurse grin
        with charachange

        nk "That too."

        show nurse neutral
        with charachange

        nk "Right. Get out of here. I'm a busy man, you know."

        stop music fadeout 2.0

        scene bg school_nursehall
        show emi basic_grin_gym at center
        with locationchange

        "I roll my eyes at his last statement and head out the door, motioning to Emi to go in."

        show emi basic_grin_gym:
            center
            easeout 0.5 xpos 0.4 alpha 0.0

        pause 0.5

        hide emi

        "The whole time, I'm trying to keep from doing a celebratory dance."

        play music music_running

        centered "The two of them will never do anything like that."

        "That's precisely the sort of thing I wanted to hear."

        "I'm half-tempted to make some sort of a move on Emi right now, but I think the nurse would probably disapprove."

        "Besides, I still don't know exactly how Emi feels about me."

        "I mean it's obvious that she cares about me as a friend, but something more than that? I can't be certain."

        "Even so, I can't help but feel hopeful. I just need to figure out a good time to tell Emi exactly how I feel."

        "That puzzle should keep me occupied for the rest of the day, at least."

        stop music fadeout 6.0

        if _in_replay:
            return

    label .the_real_beginning:
        scene bg school_nursehall

        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
        play ambient sfx_rooftop fadein 1.0

        scene bg school_roof
        with shorttimeskip

        "The rooftop is completely deserted."

        "Normally I could count on Rin to be up here before me, but she's strangely absent."

        "I wonder if she decided to accompany Emi to the cafeteria for once. That seems pretty unlikely, but it's all I can think of right now."

        "Part of me wants to go look for Rin, but a far larger part of me is too pleased with the way the sun feels on my skin to care."

        "I pick idly at my lunch while I wait for Emi and Rin to show up."

        "It does not take long for me to hear the sounds of someone coming up the stairs."

        $ renpy.music.set_volume(0.5, 0.0, channel="sound")
        play sound sfx_door_creak

        "I wait until the door begins to open before talking."

        hi "Took you long enough."

        hi "Keeping me waiting for you, honestly."

        hi "The two of you are…"

        hi "Huh?"

        "Well that's odd."

        show emi basic_confused at center
        with charaenter

        "The only person standing in the doorway is Emi, who looks mildly confused."

        emi "What do you mean, 'huh?'"

        show emi basic_grin
        with charachange

        emi "It's me! You know, Emi! We run in the mornings."

        "She grins, and I feel my heart jump slightly in my chest at the sight."

        hi "Yes, I knew that. I'm just confused…"

        hi "…Where's Rin?"

        show emi sad_depressed
        with charachange

        "Emi's grin is replaced by a rather guilty-looking expression."

        emi "Yeah, about that…"

        emi "I kind of… sort of…"

        show emi sad_shy
        with charachange

        emi "Gavehermycold."

        play music music_another fadein 0.5
        $ renpy.music.set_volume(1.0, 0.0, channel="sound")

        hi "Oh dear."

        hi "Am I at risk too?"

        "It would make sense, after all. Emi and I were in close contact the other day…"

        "So what did she and Rin do that got her ill?"

        "…"

        "Steady on, old lad. Don't go down that road."

        "Rin's just probably got a worse immune system than me."

        show emi basic_shock
        with charachange

        "Emi seems shocked by my comment, like she hadn't considered that before."

        emi "I hope not!"

        show emi excited_sad
        with charachange

        emi "I'll feel terrible if you get ill because of me, Hisao!"

        hi "Oh man, I think I feel a fever coming on…"

        show emi sad_annoyed
        with charachange

        "Emi looks horrified, and then quickly shifts into a more angry expression."

        emi "Hisao!"

        emi "You stop getting sick this instant!"

        show emi basic_annoyed
        with charachange

        emi "I won't have it!"

        show emi basic_annoyed_close
        with vpunch

        "Impulsively she seizes me by the collar."

        emi "Are you listening to me, Hisao's immune system?"

        show emi sad_angry_close
        with charachange

        emi "Get your ass in gear!"

        "I give a smart salute."

        hi "Duly noted, ma'am."

        show emi basic_grin
        with charadistant

        "Emi steps back and nods, satisfied."

        show emi basic_closedgrin
        with charachange

        emi "Good."

        show emi basic_happy
        with charachange

        emi "You are not allowed to miss any of our morning runs, after all."

        hi "But you missed a morning run!"

        show emi sad_annoyed
        with charachange

        "Emi crosses her arms and looks at me haughtily."

        emi "Yes, but that's a special case. It was me, and not you."

        hi "That's not an explanation at all."

        show emi basic_confused
        with charachange

        "Emi looks flabbergasted."

        emi "You're kidding, right?"

        show emi basic_annoyed
        with charachange

        emi "That explanation makes perfect sense!"

        hi "No it doesn't! It's a blatant double standard!"

        show emi sad_annoyed
        with charachange

        emi "I don't see what that has to do with anything."

        hi "Oh, fine."

        show emi basic_closedgrin
        with charachange

        "Emi seems pleased by her victory."

        hi "Anyway, is Rin going to be okay? She's not terribly ill, right?"

        show emi basic_grin
        with charachange

        "Emi shakes her head."

        emi "Nope! She'll be fine."

        show emi excited_proud
        with charachange

        emi "I got her some cold medicine that should help her."

        show emi basic_hes
        with charachange

        emi "Although I probably should have made sure she didn't try to take them all at once…"

        show emi basic_grin
        with charachange

        emi "She's done it before, you know."

        "Somehow, I don't find this all that surprising."

        "I doubt Rin is one to pay attention to maximum dosages and such."

        hi "You should probably check in on her later, then. Just to make sure."

        show emi sad_grin
        with charachange

        "Emi shrugs."

        emi "I'll stop by after practice. She'll be fine until then."

        "I nod, figuring that line of conversation is over."

        "The only problem is, I don't know what else to talk about."

        hi "So…"

        hi "You got any more track meets coming up?"

        nvl clear

        nvl show dissolve

        n "{vspace=240}This is a terribly roundabout way of trying to see if she's free on the weekend."

        n "If she's free, then maybe I can ask her on a date or something."

        n "Well, assuming I can get myself to actually form the words."

        nvl clear

        nvl hide dissolve

        show emi basic_grin
        with charachange

        "Emi shakes her head."

        show emi basic_closedgrin
        with charachange

        emi "Nah, not for another couple weeks, I think. The season's winding down."

        "Oh yeah. I came in right in the middle of things, didn't I?"

        "Does that mean exams are coming up soon? I should probably look into that."

        hi "What do you do on weekends if there's not a meet?"

        show emi excited_proud
        with charachange

        "An eyebrow goes up, and Emi gets a teasing look on her face."

        emi "You're awfully inquisitive today, aren't you?"

        "I shrug and hope it looks casual."

        hi "Just making conversation."

        hi "I don't know what it's like to be a track star, after all."

        show emi basic_closedgrin
        with charachange

        emi "Pfft, flattery."

        "She waves a hand idly."

        show emi basic_grin
        with charachange

        emi "I'm not actually that good, you know."

        show emi basic_closedhappy
        with charachange

        emi "You just so happened to see me on a good day, is all."

        hi "You liar."

        show emi sad_grin
        with charachange

        stop music fadeout 6.0

        emi "Heh, yeah."

        emi "But humility is the sign of a good athlete."

        show emi sad_depressed
        with charachange

        emi "At least that's what my dad used to say."

        "She shrugs and tries unsuccessfully to hide the rather troubled expression her face has taken on."

        hi "Hey, what's up? You seem bothered by something."

        "Emi starts to deny it, then sighs in defeat."

        "I wonder if she's too tired from being sick to get herself to deny it like usual."

        "Or if she actually just trusts me enough at this point to open up."

        show emi sad_shy
        with charachange

        play music music_comfort fadein 9.0

        emi "Well, you remember last night?"

        "Do I ever. I settle for nodding, however."

        show emi sad_depressed
        with charachange

        emi "That's not the first time that's happened to me."

        emi "Actually, I get them kind of…"

        "She pauses, as if it's suddenly occurred to her what she's doing."

        "It's almost like she's breaking some sort of personal rule, here."

        "But she starts up again, choosing her words carefully."

        emi "Well, not often, but…"

        show emi sad_shy
        with charachange

        emi "On occasion."

        emi "It's just been one of those weeks where that's what happens."

        show emi sad_depressed
        with charachange

        "A sigh escapes her, and she looks terribly frustrated."

        show emi sad_shy_close
        with characlose

        "I reach over and give her a hug, which unlike last time doesn't seem to shock her."

        "Instead, she seems to relax as my arms wrap around her."

        "We stay that way for a while."

        hi "Hey, you know I was serious last night."

        hi "You really can talk to me if stuff like this is bothering you. It's always difficult to do this sort of thing solo, you know?"

        show emi sad_grin_close
        with charachange

        "Emi smiles and breaks the embrace, but stays leaning on my shoulder."

        emi "Thanks, Hisao."

        show emi basic_grin_close
        with charachange

        emi "I'll be fine, I think."

        "I can already see her reassembling herself, getting ready to bottle it all up again."

        "Guess that topic's closed, now."

        hi "So hey, given any more thought to that career survey?"

        show emi basic_closedgrin_close
        with charachange

        emi "Can't say I have."

        show emi basic_grin_close
        with charachange

        emi "I don't tend to plan very far ahead, you know."

        emi "Although I suppose I could at least start looking into college, huh?"

        "I shrug."

        hi "I suppose, unless you were serious about that pirate thing."

        hi "Last I checked, pirates didn't have much need for universities."

        hi "Unless there's like, a pirate university out there somewhere."

        show emi basic_closedgrin_close
        with charachange

        "Emi giggles and starts to look a little like her old self, but there's a new element to her expression."

        "Impish. That's how I'd describe it."

        "Emi looks impish, looking up at me with her head nestled into my shoulder."

        show emi sad_grin_close
        with charachange

        emi "Would you come with me if I ran off to be a pirate?"

        hi "Of course I would!"

        hi "Who in their right mind would pass up the opportunity to be pirates with you?"

        show emi basic_grin_close
        with charachange

        emi "Well, when you put it that way, I'm not sure."

        show emi basic_closedgrin_close
        with charachange

        "She giggles again."

        "I notice that my heart seems to have sped up. It's probably due to Emi's proximity to me."

        "That hint of strawberries, again."

        "I can't help but grin as I gaze down at her."

        "She's happy again."

        show emi sad_shy_close
        with charachange

        emi "Hey, Hisao."

        hi "Hmm?"

        show emi sad_grin_close
        with charachange

        emi "If you're going to kiss me, you should probably do it soon. I think the lunch bell is about to ring."

        stop music fadeout 1.0

        "My thoughts grind to a sudden halt."

        "I'm pretty sure my mouth is hanging open in shock."

        "All I can manage is a strangled 'Huh?'"

        show emi basic_closedgrin_close
        with charachange

        "This amuses Emi even more."

        show emi excited_proud_close
        with charachange

        emi "You were thinking about it, weren't you?"

        "She sits up, bringing her face level with mine."

        show emi basic_grin_close
        with charachange

        emi "I'd probably enjoy it, you know?"

        show emi sad_grin_close
        with charachange

        emi "You're a really…"

        show emi sad_shy_close
        with charachange

        emi "…Well."

        "She briefly composes herself, looking like she's about to say something important."

        show emi sad_grin_close
        with charachange

        emi "If you hadn't figured it out by now, I think I've developed a bit of a crush on you."

        show emi basic_grin_close
        with charachange

        emi "You're going to have to do something about that."

        "This time her grin short circuits several important thought processes."

        "At some point I turned toward her, and at another point her arms moved to around my neck."

        "At yet another, my arms wrapped around her waist."

        "I'll be damned if I could tell precisely when that happened."

        "Because at the moment, there's only a voice in the back of my head yelling at me to kiss her."

        "I look into Emi's eyes."

        "There it is."

        "The thing I saw yesterday on the bed. It's there again."

        "It suddenly strikes me that she's worried that I'll reject her."

        stop ambient fadeout 1.5

        "What a silly worry for her to have."

        play music music_romance fadein 0.5

        scene white
        show ev emi_firstkiss:
            truecenter
            zoom 4.0 rotate 20
            0.7
            linear 0.3 zoom 1.1 rotate 0
            easein 12.0 zoom 1.0
        with GenericWhiteout(0.5, 0.2, 2.0)

        pause 5.0

        nvl clear
        nvl show dissolve

        n "{vspace=120}Her lips taste faintly of strawberries."

        n "She leans into the kiss, and her arms tighten around the back of my head, making sure that I don't pull away."

        n "Not that there was any danger of that."

        n "There's a churning feeling in my gut."

        n "The world falls away."

        n "There's just me, and her, and this bench."

        n "My arms tighten, drawing her waist closer, entranced by the feel of her."

        n "I inhale her scent, my mind trying desperately to memorize everything about how she tastes, how she smells, how she feels."

        play sound sfx_warningbell
        play ambient sfx_rooftop fadein 4.0

        nvl clear

        nvl hide dissolve

        scene bg school_roof
        show bg school_roof_blurred as overlay:
            center
            linear 6.0 alpha 0.0
        show emi sad_shyblush_close at center
        with silentflash

        "The ringing of the bell snaps us both back to reality, and we break the kiss."

        "Emi's cheeks are slightly flushed, and she seems to be catching her breath. In her defense, so am I."

        "We stand there for a few moments, trying to wrap our heads around what we've just done."

        "Emi is the first to break the silence."

        show emi sad_grin_close
        hide overlay
        with charachange

        emi "So…"

        show emi basic_closedgrin_close
        with charachange

        emi "…Wanna grab dinner after I'm done with practice?"

        hi "What a coincidence."

        hi "I was about to ask you the same thing."

        "Well, actually I suppose it was going to be some kind of proper date on the weekend or something. But the thought was there, I think."

        with vpunch

        "Emi gives me a playful shove."

        show emi basic_happy_close
        with charachange

        emi "Yeah right."

        show emi basic_closedhappy_close
        with charachange

        emi "You were still in shock from how incredibly awesome I am at kissing."

        "We begin to head down the stairs back to our respective classrooms."

        stop ambient fadeout 2.0

        scene bg school_hallway3
        show emi sad_grin at center
        with locationskip

        hi "Hey, I didn't see you talking immediately afterwards either."

        show emi basic_closedgrin
        with charachange

        emi "That I didn't."

        show emi basic_closedhappy
        with charachange

        emi "See you after practice, Hisao."

        show emi basic_closedgrin_close
        with charachange

        show emi:
            easeout 0.5 xpos 0.6 alpha 0.0

        "She leans in quickly and gives me a quick kiss in the middle of the hallway, sending me into another brief state of mental freefall."

        scene bg school_scienceroom
        with locationchange

        "As I head into my classroom, a giggling Misha greets me."

        show misha hips_grin at center
        with charaenter

        mi "Why Hicchan, you romantic, you~!"

        mi "Did you confess on the rooftop? Did you~?"

        hi "Er, actually I think it was the other way around."

        show misha cross_laugh
        with charachange

        "This sends Misha into a fresh fit of laughter."

        show misha hips_grin
        with charachange

        mi "Young love is so unpredictable, isn't it~?"

        "This being Misha, I suppose I should have expected her to tease me over this."

        hi "I guess…"

        show misha:
            easeout 0.5 xpos 0.4 alpha 0.0

        "Before I can really respond, Mutou's entered the room and Misha skips off to her seat, giggling all the while."

        "I suspect that I'll get a lot of that sort of conversation now, especially seeing as how Emi kissed me right in the middle of the hall."

        "But somehow, I don't care about that."

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        stop music fadeout 5.0

        "For the first time since arriving here, my heart feels light."

        if _in_replay:
            return

    return

label a2ec1o1:
    hi "Hey, I'll run with you."

    hi "I might as well, right?"

    show emi basic_annoyed_rn
    with charachange

    "Emi shakes her head emphatically."

    emi "No you won't, Hisao. Rest is critical for you, remember?"

    emi "I won't allow you to push yourself too hard."

    "I guess she's better at giving advice than taking it."

    hi "Whatever you say, Emi."

    "I think it's probably best not to press the issue."

    return

label a2ec1o2:
    "Come to think of it, she looks like she'd rather be alone right now."

    "I decide to keep my offer to myself."

    return
