# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a2_rin:
    label .a_wider_field_of_vision:
        scene bg school_scienceroom
        with locationchange

        pause 1.0

        play music music_normal fadein 6.0

        "It's already half past eight, but this morning's class has not yet begun. We were supposed to have physics but the teacher is nowhere to be seen."

        "Had I known this beforehand, I would have slept in too."

        play sound sfx_doorslam
        with vpunch

        "Suddenly the classroom door slams open and Mutou grunts his morning greeting to us from the doorway."

        show muto normal at center
        with charaenter

        mu "Good morning, everyone!"

        "Mutou looks like he has not slept at all."

        "The stubble, his messier-than-normal hair, and the stained dress shirt create a less than favorable impression."

        "I guess he had fun last night at the festival too."

        show muto irritated
        with charachange

        mu "Excuse my being late, I ran into unexpected problems. I'm usually not one for festivals like this, but I hope you all had a good time."

        mu "After all, these sorts of events are important for you all, since they give you a short reprieve from schoolwork."

        show muto normal
        with charachange

        "The class replies with various degrees of enthusiasm, and Mutou proceeds to take roll and get started."

        mu "Right, then. Today's subject is photon particle physics…"

        hide muto
        with shorttimeskip

        "Before long, I have descended into a comfortable coma-like state along with the rest of the class, letting Mutou's rambling speeches pass through one ear and exit the other without leaving a trace."

        show muto normal at center
        with charaenter

        mu "Now, who could tell us the solution to this problem?"

        "He's written a rather easy equation on the blackboard. Desperately, he tries to get the class to participate."

        show muto irritated
        with charachange

        mu "Nobody? Come on, guys. Nakai, how about you?"

        "Unfairly singled out and cornered, I give him an answer. It causes his shaggy features to twist into a genial smile that would scare little children senseless."

        show muto smile
        with charachange

        mu "Precisely! Good work, Nakai!"

        "I'm both disturbed and honored by the fact that he can remember my name only one week after I transferred here."

        "From what I've seen, Mutou has serious trouble remembering the names of anybody else in the class, and most of them have been here since the first year."

        "The room settles into a dreary mood, students and teacher alike trying to get back on track after the festival."

        "I figure last week must've been frantic for everyone."

        play sound sfx_normalbell

        stop music fadeout 2.0

        "Not a minute too soon, the lunch bells ring."

        scene bg school_hallway3
        with locationchange

        play music music_running

        mystery "MAKE WAY! IMPORTANT BUSINESS!"

        "I turn my head just in time to see other people scatter out of the way as someone charges from the far end of the corridor towards the stairwell."

        "It's too late to realize that I'm standing in the middle of the corridor, directly in the way of the oncoming human projectile."

        "I try to skip back towards the doorway. Unfortunately, the person running towards me dodges in the same direction."

        "In the following fraction of a second several things come to mind in sequence, yet almost simultaneously."

        "First, I recognize that the girl who is on a collision course with me is Emi."

        "Second, I realize that it feels somehow very natural to be tackled by Emi once again. I could feel almost comfortable if not for the reflexive panic and terror."

        "Third, Emi seems to be carrying a foot-tall stack of papers while running in the hallway."

        play sound sfx_pillow
        with vpunch

        "She crashes into me, but at least the impact was a grazing one on my arm this time."

        show emi sad_depressed at offscreenbottom
        with None

        show emi at center
        with charamovefaster

        emi "Owiiie… Why does this always happen to me?"

        hi "Gee, I wonder. Could it possibly have anything to do with you running through the corridor like you were on fire?"

        show emi sad_shy
        with charachange

        "She whimpers regretfully, looking like a hurt puppy. The sight makes me regret my snappish comment the very instant it emerges from my lips."

        show emi sad_pout
        with charachange

        emi "But… I was in a hurry."

        hi "I can tell."

        emi "Sorry."

        hi "Don't worry about it."

        show emi sad_shy
        with charachange

        "Emi wails weakly one last time and rubs her forehead as if to expel the ache while her gaze sweeps over the hallway floor."

        "As she notices her neat stack of papers spread all over the floor in one big mess, she lets out a horrified yelp."

        show emi basic_shock
        with charachange

        emi "Aah! The printouts! Oh no oh no, what am I going to do? Teacher will give me hell if they get dirty."

        hi "They're probably fine. Let's gather them back up; it won't be a problem."

        "We quickly round up the papers, and Emi tries to sort the scattered pile in her hands back into the orderly stack it was."

        show emi basic_grin
        with charachange

        emi "Where are you going?"

        hi "Nowhere in particular, I guess. Didn't want to be left alone with Mutou in the classroom. I think he has a hangover."

        show emi excited_happy
        with charachange

        emi "Have you eaten lunch?"

        hi "Not yet, but I'm not feeling very hungry anyway."

        show emi basic_confused
        with charachange

        "She looks at me incredulously, as if doubting my sanity for letting such a thing out of my mouth."

        show emi excited_proud
        with charachange

        emi "You should go to the roof! I promised Rin I would eat lunch with her. I bet she'd like company."

        "Uh-oh. My lunches with Rin have been remarkably unsuccessful."

        "I know where this conversation is going and it's hard to not get drawn along, so I have little choice but to play ball."

        hi "OK, I'll go pick up some bread or something first."

        show emi basic_closedgrin
        with charachange

        "Emi smiles brightly before I say anything further."

        show emi basic_grin
        with charachange

        emi "No no, I'll go and deliver these super-quick, and then go buy lunch for us. And Rin, too, of course. What kind of bread do you like?"

        hi "It's fine, you really don't need to…"

        show emi excited_proud
        with charachange

        emi "Don't worry, it's all right. Consider it an apology. I'll be back before you know it!"

        hi "That's what I'm worried about. Don't get into another accident."

        "Emi starts walking down the hall, but since she's still talking to me, she isn't watching where she's going."

        show emi basic_closedhappy
        with charachange

        emi "I won't!"

        hide emi
        with charaexit

        stop music fadeout 4.5

        "Famous last words. She's already jogging down the stairs as she shouts that not-so-reassuring promise back to me."

        $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
        play ambient sfx_rooftop fadein 2.0

        scene bg school_staircase1
        with locationchange

        "Sighing quietly, I start plodding along in her wake. But instead of taking the stairs down, I climb upwards."

        "The stairwell up to the roof is unlit and just as creepy as it was before."

        play sound sfx_dooropen

        "The door squeaks weakly in protest as I push it open."

        play sound sfx_door_creak
        $ renpy.music.set_volume(1.0, 0.5, channel="ambient")

        scene bg school_roof
        with Fade(0.5, 0.0, 2.0, color="#FFF")

        "Rin is there too, like Emi said, lying on her back at the other end of the pebble-covered rooftop for some reason."

        "Predicting something unnecessarily strange again, I walk to her as slowly as possible."

        scene ev rin_roof_boredom
        with locationchange

        rin "Helloooo."

        "She sounds very drowsy as she says that, stretching the end of the word with a slurred voice. Despite that, her eyes are wide open."

        show hisao rin_roof
        with charaenter

        "I look down at her, my shadow overlapping her face."

        hi "What are you doing?"

        show ev rin_roof_doubt
        with charachangeev

        "Rin raises an eyebrow."

        show ev rin_roof_nonchalant
        with charachangeev

        rin "I thought you had a heart problem, not an eye problem."

        "She answers, challenging the rationale of my perfectly valid question without even tilting her head to look at me."

        "Rin's smartass comments are infuriating. The worst thing is that I'm not sure if she's doing it on purpose or not."

        hi "All right, then. Let me rephrase:"

        hi "Why are you lying on your back on the rooftop?"

        show ev rin_roof_boredom
        with charachangeev

        "She gives a lazy shrug and sniffs dismissively."

        rin "I'm trying to experience. People probably don't do this enough."

        hi "What exactly are you trying to experience here? I can't really tell, but there's probably a reason people don't do… whatever."

        "She's playing dodgeball with me again, answering my attempt at small talk with riddles I don't want to puzzle out."

        "But I don't want to ignore her, either."

        show ev rin_roof_nonchalant
        with charachangeev

        rin "Yeah, but the reason is that everyone is too busy with their lives to pay attention to the really important things."

        hi "Like watching the sky?"

        show ev rin_roof_surprised
        with charachangeev

        "She tears her gaze away from the sky and finally looks straight at me. The penetrating deepness of her eyes once she focuses them on something is startling."

        rin "You know, if you were a girl I would be able to see your panties."

        hi "If I was a girl, I wouldn't come this close to anyone who tried to sneak a peek at my panties. I have that much common sense."

        show ev rin_roof_boredom
        with charachangeev

        rin "I wouldn't either, but sometimes it can't be avoided. Like now, for example."

        show ev rin_roof_nonchalant
        with charachangeev

        rin "To tell you the truth, I don't even really want to peek at your panties though."

        rin "Underpants are the soul of a girl. You shouldn't peek at someone else's soul. Even if you are not a girl."

        hi "As a guy, I guess I can understand that. To us, they're some sort of half-mythical object that we can't quite comprehend."

        show ev rin_roof_surprised
        with charachangeev

        rin "Yeah, that's exactly how I think about them too. What a coincidence."

        hi "It really is."

        hi "So did you have world history in the morning class?"

        show ev rin_roof_doubt
        with charachangeev

        rin "I skipped class."

        hi "To do this?"

        show ev rin_roof_boredom
        with charachangeev

        rin "Well, I'm not actually doing what it looks like I am doing, or at least I think that what I am doing doesn't look like what I look like, but from your perspective…"

        extend " probably…"

        rin "Yeah, I skipped class to do this."

        hi "I guess whatever your reason is, it's as good as any."

        hide hisao
        with charaexit

        play sound sfx_rustling

        scene bg school_roof
        with locationchange

        "Giving in to the tired feeling in my legs, I sit down on the roof next to Rin."

        "The pebbles are not the most comfortable bed in the world, but if she can stand it, then I should be able to as well."

        rin "What are you waiting for?"

        hi "Hmm?"

        rin "Try it."

        stop music fadeout 2.0
        $ renpy.music.set_volume(0.4, 3.0, channel="ambient")

        "I bend my neck backwards to take a look where she is looking."

        scene bg misc_sky:
            xalign 0.0
            warp acdc_warp 40.0 xalign 1.0
        with locationchange

        "The silvery blue sky, dotted by herds of cloud-sheep, fills my field of vision entirely."

        "While it's pretty, the view is nothing special even though the weather is fair."

        "I give a shrug, trying my best to imitate the nonchalant manner which Rin seems to have evolved to perfection, and lie down on my back."

        "The stones poke at my back through my thin shirt whenever I shift my weight even a little, forcing me to keep as still as possible."

        "I try to ignore the discomfort and myself, instead concentrating on the vastness over us."

        "Far above, the summer clouds drift soundlessly across the dome of the sky."

        "Neither of us has anything more to say, thus silence covers the rooftop."

        "The subdued noises of students on their lunch break, cicadas in the trees and traffic buzzing past the school are humming pleasantly somewhere in the background."

        hi "Listen, I had a great time yesterday."

        rin "Did you?"

        hi "Well, to be honest, no. But it was all right. It was probably the longest time I've ever sat in one place without doing anything, which is kinda impressive."

        "I try to make it sound as convincing as possible."

        rin "Is that impressive?"

        hi "I think it is. I'm usually too restless to do anything like that."

        rin "I think I had a good time too."

        "A cloud passes above us, casting its shadow on the school."

        "A chill surges through me from the sudden change of sunlight to shade."

        "I realize that summer is not in its full bloom quite yet."

        "The only measure of time passing is the slow pace of the clouds moving towards the town."

        "Stray beams of golden sunlight leak through the gaps, blinding me for a moment whenever they hit me directly in the eyes."

        "The blue of the sky looks so unreachable."

        "This reminds me of the time I spent in the hospital, where I was bored out of my mind on a daily basis."

        "Somehow, it didn't matter after a while. I learned to appreciate other things besides watching TV and gossiping with people I didn't even like."

        "A comprehensive sensation of calmness spreads from my sight to my other senses, finally hitting my brain."

        "An airplane zooms by, leaving two thin contrails in its wake like a pair of chalk lines drawn from one end of the sky to the other."

        "I wonder where it is heading."

        "The low din of its engines carries all the way down to my ears, although it's barely audible over the racket from the quad."

        stop ambient fadeout 8.0
        $ renpy.music.set_volume(1.0, 10.0, channel="ambient")

        rin "It's nice."

        hi "It's nice, but I don't understand why this is more important than going to class."

        rin "Isn't it good to do something you like?"

        rin "Every once in a while?"

        hi "Of course, but—"

        stop sound

        emi "What are you doing?"

        "Emi has snuck up on us without either noticing and is only a step away from me, holding several packages wrapped in plastic film in her arms."

        show bg at right
        with charamovefaster

        show emi excited_happy_close:
            center
            ypos 1.2
            easein 0.5 center
        with charaenter

        show emi at center

        "She leans forwards and peeks over me, overshadowing my face almost exactly the same way I overshadowed Rin before."

        "I wonder how weird this looks, the two of us lying on our backs on the rooftop."

        hi "That's what I asked, too."

        rin "I would be more concerned about what you are doing. If I were you, I wouldn't come that close to people who could see your panties."

        play sound sfx_pillow

        show emi sad_angry_close
        with vpunch

        play music music_comedy fadein 0.5

        emi "Rin!"

        show emi sad_angry_close:
            easeout 0.5 ypos 1.2 alpha 0.0
        with None

        scene bg school_roof
        with locationchange

        show emi basic_hes:
            center
            ypos 1.1
            easein 0.5 center
        with charaenter

        show emi at center

        "Emi's voice is scandalized, but she quickly takes a step backward, pressing her hands against the front of her skirt so abruptly that the parcels of bread she was carrying fall."

        "I quickly avert my eyes, and glance angrily at Rin. She pretends not to see me."

        show emi basic_shock
        with charachange

        emi "Hisao isn't like that, right?"

        hi "Right."

        play sound sfx_rustling

        show emi basic_shock:
            parallel:
                ease 0.5 ypos 1.17
            parallel:
                "emi basic_annoyed" with Dissolve(0.5)
            ease 0.5 ypos 1.0
        with Pause(1.0)

        show emi basic_annoyed at center

        "Emi scowls at Rin and crouches down to pick up the packages."

        play ambient sfx_rooftop fadein 8.0

        show emi basic_grin_close
        with characlose

        show emi:
            ypos 1.12
        with charamove

        "She wipes the dust off them, and skips lithely around me to Rin's other side where she sets herself down."

        emi "Anyway, here's your bread. Sorry it took a while."

        hi "That's all right. Thanks for treating me."

        "I pull myself up into a sitting position and gratefully accept the bread Emi is offering."

        "All three of us ravenously dig into the simple meal. The bread is surprisingly decent and readily fills my stomach."

        show rin basic_awayabsent:
            yanchor 1.0 ypos 1.2 xanchor 0.5 xpos 1.0 alpha 0.0
            ease 1.0 ypos 1.07 xpos 0.9 alpha 1.0
        with None

        show emi:
            xpos 0.3
        show bg at bgleft
        with charamovefast

        show rin:
            center
            ypos 1.07 xpos 0.9

        "I follow from the corner of my eye the skill with which Rin handles her bread between her feet."

        show emi excited_proud_close
        with charachange

        emi "I haven't seen you on the track in a few days."

        show rin basic_absent_close
        with charachange

        hi "Oh. Right, I… figured it was too heavy a routine for me to start with."

        show rin basic_awayabsent_close
        show emi basic_hes_close
        with charachange

        emi "So you've been doing something else?"

        show rin basic_absent_close
        with charachange

        hi "I've been considering my options."

        show emi basic_annoyed_close
        with charachange

        "She frowns but doesn't pursue the issue further, for which I'm thankful."

        "Emi seems pretty headstrong and I wouldn't really want to get pestered by her about this on a daily basis. I have enough burdens to bear with Shizune and Misha already."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        play sound sfx_warningbell
        show rin basic_awayabsent_close
        show emi basic_shock_close
        with charachange

        "We barely finish the lunch before the bells ring, calling us back to our classrooms."

        stop ambient fadeout 0.5
        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        scene bg school_scienceroom
        with locationskip

        show misha sign_smile at center
        with charaenter

        mi "Hicchan!"

        "Misha waves at me as soon as I enter, and starts talking before I even make my way across the classroom."

        show misha hips_smile
        with charachange

        mi "How was your festival? Did you have fun?"

        hi "Umm… still somewhat undecided on that. I'd say 'probably.'"

        hi "Why?"

        show misha hips_grin
        with charachange

        mi "Wahaha~, just asking, just asking!"

        "Her eyes glint in a way that tell me she's not just asking. I can't even start to guess her motives, though."

        hide misha
        with charaexit

        "As the well-timed entrance of the English teacher prevents us from talking further, Misha falls back to plan B."

        show misha perky_smile_close at offscreenleft
        with None

        show misha:
            xpos 0.1 xanchor 0.5
        show bg at left
        with charamove

        call screen written_note(_("{color=#FF2AAA}I was there all day with Shicchan! We had a lot of fun!{/color}"))

        call screen written_note(_("Weren't you supposed to be doing work?"))

        show misha hips_grin_close
        with charachange

        call screen written_note(_("{color=#FF2AAA}Don't worry! Everything went really well.{/color}"))

        "I don't reply to that, and she leaves me alone after Shizune demands her attention."

        stop music fadeout 12.0

        show misha:
            ease 1.0 offscreenleft alpha 0.0
        with Pause(1.0)

        hide misha

        show bg:
            ease 30.0 zoom 1.1

        "My own attention, on the other hand, is directed out the windows."

        "Now that I look at it from here, through the window and the foliage just outside, the sky seems smaller."

        "I catch only small glimpses of blue; everything else is a clutter of noise right in the middle of my field of vision."

        "What 'experience' did Rin want out of staring at the sky? Surely she's done it before. Everyone has."

        "It's no use trying to guess her mind, but if I don't do that, then I have no excuse for not concentrating on the teacher's words."

        "I look at the scribbles appearing on the blackboard, trying to figure out their meaning with little success."

        "English really is not my favorite subject. We have a strong mutual dislike for each other."

        stop music fadeout 2.0

        if _in_replay:
            return

    label .studies_in_grayscale:
        scene bg school_hallway3
        with shorttimeskip

        play music music_normal fadein 3.0
        play sound sfx_normalbell

        "Thick, hot afternoon light invades the corridor, making the air feel heavy and lazy."

        "My body feels weighed down by it as I drag it two doors down the hallway to the art classroom."

        "Maybe this is part of the reason why I didn't join any clubs before: afternoons just aren't suited for activity."

        scene ev rin_artclass1
        with locationchange

        "I knock on the door of the art room and open it. A girl who was possibly doing something important with the scroll of paper she's carrying turns to reckon me, and smiles in a sweet if a bit confused manner."

        scene ev rin_artclass2
        with charachangeev

        "Student" "Hello…?"

        hi "This is the art club, right?"

        "Student" "Yep. You interested in joining?"

        hi "Yeah. In fact, I might already have done so, but we'll see."

        scene ev rin_artclass3
        with charachangeev

        "I give her a weak smile, and her own widens a notch, making me feel less nervous."

        "Student" "Great! Have a seat, then. We'll start when the teacher gets here."

        scene ev rin_artclass4
        with charachangeev

        "Without even scouting the room for a good spot, I walk quickly to the back of the room and settle myself on a free seat, apart from everyone else."

        "A few other members are lounging in their seats, waiting for the teacher. Rin sits alone in a window seat, looking outside. She's the only person here that I know, although a guy I've never really gotten along with from my own class is here, too."

        "Nobody else comes to greet me - maybe introductions are left for later? - so I just settle for silent observation as well."

        "One boy has sunglasses on; an odd sight indoors, were we not at Yamaku. I'll bet he's the blind student Rin was talking about."

        stop music fadeout 2.0
        play sound sfx_footsteps_hard fadein 0.2

        scene bg school_classroomart at left
        with locationchange

        "The wait proves to be extremely short."

        stop sound
        play music music_happiness fadein 2.0

        show nomiya smile at center
        with charaenter

        "Nomiya walks over to stand behind his desk in three long strides, then gives a smile and a flamboyant greeting."

        show nomiya veryhappy
        with charachange

        no "Good afternoon, everyone!"

        show nomiya talk
        with charachange

        no "First things first: Hisao there is a new member, so everyone get along with him."

        "He winks at me unsettlingly."

        "All eight members of the club, including myself, answer his greeting with considerably less enthusiasm. Still, people finally straighten up in their seats and begin to pay attention."

        show nomiya smile
        with charachange

        no "I think some of you still have projects to work on, so please continue with those if you like."

        show nomiya talk
        with charachange

        no "As for the rest, I was thinking that today, we could do some rough studies."

        show nomiya veryhappy
        with charachange

        no "How does that sound?"

        "Nobody answers except with some unintelligible murmurs, which Nomiya apparently interprets as unanimous approval."

        show nomiya talk
        with charachange

        no "All right, then! Everyone not working on other projects, choose a partner and draw a sketch of one another."

        no "You should be able to complete this today, but if not, we can continue it next time, or even do it again if you find it interesting."

        show nomiya veryhappy
        with charachange

        no "Remember to pay attention to lighting and shadow, and give it your best!"

        "Pairing up? I feel pretty awkward about it, hardly knowing anyone here. I wish someone would ask me to be their partner."

        hide nomiya
        with charaexit

        "People stand up and move their chairs closer together, but nobody comes to me."

        "Pretty soon, everyone else has paired off. Friends team up with each other, but I'm left alone."

        "Well, there is Rin."

        show bg at right
        with charamove

        "She's sitting in the furthest corner of the classroom, still staring out the window and seemingly uninterested in taking part in the exercise."

        "Since she's the only other one without a partner, I walk to her seat."

        "I can't see her face because her hair is covering most of it and she's looking away from me."

        hi "Rin?"

        "I call out to her. No response."

        hi "Hey, want to partner up? You're the only one I know here."

        show rin basic_absent at center
        with charaenter

        "She seems to finally acknowledge my presence, head turning like a robot as she looks to see who is addressing her."

        "…"

        "Rin doesn't answer, and I don't want to repeat the question, either. I'm sure she heard it the first time."

        "…"

        "Why doesn't she say anything? It can't be such an awful fate to be paired up with me, can it?"

        "She doesn't look at my face, and instead stares directly at my chest and stomach."

        "…"

        show rin basic_deadpan
        with charachange

        rin "Oh, okay. Why not?"

        "…"

        hi "Okay. Good. Great. I'll get the stuff for us."

        hide rin
        with charaexit

        show bg at left
        with charamove

        "Looking at the equipment Nomiya has prepared for today's meeting confuses me. Instead of graphite or pencils, we are apparently supposed to do ink sketches."

        "I've never done anything like that before."

        "The teacher, however, seems confident in my abilities to adapt to this medium."

        show nomiya veryhappy at center
        with charaenter

        no "Simple!"

        show nomiya smile
        with charachange

        no "First you do the outlines in ink. You let them dry, and then you shade with the diluted ink. This is called India ink, it works like watercolors."

        show nomiya talk
        with charachange

        no "If you're uncomfortable with it, use a pen instead of a brush for the outlines."

        hi "Got it."

        hide nomiya
        with charaexit

        "I pick up paper, water cups, one pen for me, one brush for Rin and ink for both of us, then return to Rin."

        show bg at right
        with charamove

        show rin basic_absent_close:
            center
            ypos 1.1
        with charaenter

        "Grabbing a vacated chair from nearby, I seat myself directly opposite her."

        show rin negative_spaciness_close
        with charachange

        stop music fadeout 1.0

        rin "Do you want me to do it with my foot or my mouth?"

        hi "What did you say?"

        play music music_another fadein 2.0

        show rin relaxed_surprised_close
        with charachange

        "She tilts her head, her brows forming questioning arches, as if she doesn't understand that I didn't understand the question."

        show rin basic_deadpan_close
        with charachange

        rin "I don't mind drawing either way. You'll look better if I do it with my foot, though."

        hi "With your foot, then, if it's all the same to you."

        show rin basic_deadpannormal_close at center
        with charamovechangefaster

        "Nodding in answer, Rin gets up from her seat and kicks off her sandals."

        show rin basic_awayabsent_close:
            center
            ypos 1.17
        with charamovechangefaster

        "In two fluid motions, she picks up the paper sheet and drops it on the floor, then snatches the brush between her toes before sitting on the floor in a weird half-crosslegged position."

        "Although I've seen her do everything with her feet already, from eating to painting, this display of dexterity is so prodigious that I just stare at her, stunned."

        show rin negative_annoyed_close
        with charachange

        "Rin contemplates her blank paper intently. The sharp tip of her brush hovers over the paper in anticipation."

        show rin basic_deadpancontemplation_close
        with charachange

        "When she raises her head to see if I'm ready, I quickly turn my face away."

        show rin basic_deadpan_close
        with charachange

        rin "I'll go first. Make a pose."

        hi "What kind of a pose?"

        show rin basic_lucid_close
        with charachange

        rin "It doesn't matter. That's the point. You have to make the sketch of the impression you get, not decide beforehand."

        "I end up just sitting in my chair, my hands hanging limply between my knees."

        show rin basic_deadpanupset_close
        with charachange

        "I look at her, and she looks at me for a moment before beginning."

        "Rin's stare is piercing, but impassive, as if she were trying to absorb a part of me into her own self. I feel like I'm physically shrinking under the pressure of her gaze."

        "I get the feeling that for the first time since we met, Rin is actually looking at me, instead of in my general direction."

        show rin negative_annoyed_close
        with charachange

        "She sketches with confident, bold sweeps of the delicate brush, not caring about the potentially destructive consequences of an accidentally misplaced stroke."

        show rin basic_absent_close at center
        with charamovechangefaster

        "After she's happy with the outlines, she stands up to pose for me, stretching her back and legs."

        show rin basic_awayabsent_close
        with charachange

        "This time, she doesn't look at me. Instead, Rin lets her gaze wander around the room. I'm relieved; it's easier to stare at someone when they aren't staring back at you."

        "Even so, I find it hard to get the sketch going."

        "I'm not especially artistically talented, so I'm scared my portrait will turn into something disfigured, especially when compared to my partner's skill."

        "I don't want to embarrass myself too badly on the first try."

        "Rin is not helping the process, either."

        show rin negative_annoyed_close
        with charachange

        "She doesn't stand still for even ten seconds; tilting her head from side to side to judge her drawing, biting at her lower lip, looking unsatisfied, and constantly shuffling around like she was on hot coals."

        show rin basic_awayabsent_close:
            center
            ypos 1.17
        with charamovechangefaster

        "I finally manage to make some headway on my sketch, and with my outlines done, we both start inking in the shadow and light."

        show rin:
            tworight
            ypos 1.17
        show bg at center
        with charamove

        show nomiya smile behind rin at twoleft
        with charaenter

        "Nomiya passes by, and remarks on the beginnings of our sketches."

        show nomiya veryhappy
        with charachange

        no "Very good! Standing figure is easier for a beginner to get a grasp of."

        hi "But I didn't choose the pose…"

        hide nomiya
        with charaexit

        "I look at him and then at Rin in confusion, but he's already moving onto the next pair, and Rin seems unresponsive."

        show rin:
            center
            ypos 1.17
        show bg at right
        with charamove

        "Just like when she was painting the mural, Rin has become so engrossed with her work that it seems she has shut me, the classroom and the entire world itself out from her own little sphere of existence."

        "Every now and then, she leans backwards, seemingly to get some perspective. Sometimes she bends forward, leaning down until her nose almost touches the paper."

        "This rocking back and forth looks silly."

        "Suddenly, Rin proves she hasn't completely drifted off into a world of her own, and speaks."

        show rin negative_spaciness_close
        with charachange

        rin "Are you having fun already?"

        "She doesn't raise her eyes from the drawing, which is a good thing. The breaking of the silence sends a jolt of surprise through me, as if I'd been electrocuted."

        hi "I… don't know, yet. It's hard to say."

        show rin basic_awayabsent_close
        with charachange

        "I can't hear how she replies to my answer because it seems she is suddenly having a private, whispered conversation with her sketch."

        "I don't understand how she can draw so well when she has the attention span of a butterfly."

        "As it seems she lost her interest, I go back to work on my drawing as well."

        "I try to add texture to Rin's hair, to somehow grasp the way the golden afternoon sun lights her bright red tousle aflame and transfer it to my paper in shades of black and gray."

        "Somehow, this pen and the bottle of ink seem like such lousy, inadequate tools for the task."

        "Minutes pass, but the sketch doesn't magically look any more like Rin than it did before. Her voice wakes me up from my despair."

        show rin basic_deadpannormal_close
        with charachange

        rin "What about now?"

        hi "Excuse me?"

        show rin basic_deadpan_close
        with charachange

        rin "Are you having fun already?"

        hi "Why do you keep asking that?"

        show rin basic_deadpancontemplation_close
        with charachange

        rin "Because it's a club, right? Clubs are meant to be fun. You joined to have fun. Are you having fun?"

        hi "Is it important that I'm having fun?"

        show rin basic_deadpanupset_close
        with charachange

        rin "…Yes."

        hi "…Okay, I'm having fun."

        show rin basic_lucid_close
        with charachange

        rin "Good."

        "I wonder if I said that just to please her, or if I really meant it. I can't really decide which it was."

        "I don't hate this, though. I can honestly say that much. It's good enough for now."

        stop music fadeout 2.0

        scene bg school_classroomart at right
        with shorttimeskip

        "As the allotted time to finish the studies quickly ticks away, I desperately try to improve my awful sketch, but it doesn't seem to get any better."

        "I want to start again from scratch, but what would be the point? There's no time for that, either."

        play music music_daily fadein 2.0

        no "Okay everyone, that's it for today! Please turn in the drawings on my desk, and I'll see you all next Monday!"

        show ovl rinbyhisao:
            center
            ypos 1.5 alpha 0.0
            easein 1.0 center alpha 1.0
        with Pause(1.0)

        show ovl at center

        "I glance at my portrait. It doesn't exactly look like Rin. I guess you could say it portrays her, but that might be a bit generous."

        "The nose and jaw look hideous, and the shading is terrible. Granted, it's my first attempt at drawing with ink, but it's still pretty bad."

        rin "That's not bad."

        show rin basic_deadpanamused_close behind ovl at center

        show ovl rinbyhisao:
            easeout 1.0 ypos 1.5 alpha 0.0
        with Pause(1.0)

        hide ovl

        "She sneaked up behind me while I was lost in thought."

        hi "Damn it. I was hoping I could smuggle the portrait to the teacher without you seeing it."

        show rin basic_surprised_close
        with charachange

        rin "Why?"

        hi "I'm not really happy with it. I wish I could draw better."

        show rin basic_deadpannormal_close
        with charachange

        rin "You just need some practice. Could you take my drawing to the teacher too?"

        "Curious myself about how the sketch turned out, I peek at the picture. From the way Rin was drawing, it looked like she was really into it."

        show ovl hisaobyrin:
            center
            ypos 1.5 alpha 0.0
            easein 1.0 center alpha 1.0
        with Pause(1.0)

        show ovl at center

        "It's excellent. Somehow the seemingly arbitrary strokes come together to form an image of my face, from the shape of my chin, to the messy hair, to the somewhat gloomy expression."

        menu:
            with menueffect
            "Her sketch blows my mind."

            "You're amazing!":
                $ rin_amazing = True

                call a2rc1o1

            "I wish I was as good as you.":
                $ rin_amazing = False

                call a2rc1o2

        show ovl hisaobyrin:
            yalign 0.0
            easein 20.0 zoom 1.1

        "I take a closer look at her work. It's still glistening with slowly drying ink."

        hi "You know, I look kind of grim here."

        rin "You do look kind of grim. I mean, I agree; but it's also true otherwise, too. Like this you, not the you I made."

        hi "I do?"

        rin "I think so at least."

        "Her simple statement makes me suddenly feel incredibly self-conscious. I feel like I need a mirror right now, to confirm or debunk Rin. It's a nasty feeling."

        "Maybe it's just her. I hope it's just her, and that I don't look like that sketch to everyone."

        "It's a good sketch, but somehow I get a really oppressive feeling from it."

        show rin basic_absent_close

        show ovl hisaobyrin:
            easeout 1.0 ypos 1.5 alpha 0.0
        with Pause(1.0)

        hide ovl

        hi "I see. Anyway, it looks really good. You really are amazing."

        show rin basic_deadpandelight_close
        with charachange

        rin "Thanks. I'm glad I could draw you. You are an interesting person."

        hi "You're an interesting person too, but that didn't help me much."

        "My self-deprecation has no limits today, but Rin ignores it all. I knew that I could never compare, but to see the difference with my own eyes is quite humbling."

        show rin basic_awayabsent_close
        with charachange

        rin "See, I tried to make you look like you think a lot, since you did a lot of thinking."

        show rin basic_deadpanamused_close
        with charachange

        rin "And yeah, I might have overdone the fed-up-with-life expression, but cynics are like that, right?"

        "I want to retort something snappy, but Nomiya gives me no time to think, ushering us to the door."

        show rin at tworight
        show bg at center
        with charamove

        show nomiya talk behind rin at twoleft
        with charaenter

        no "Hurry up, you two!"

        "While we've been chatting the rest of the club has taken their leave."

        hide rin
        with charaexit

        "I quickly pick up our drawings and take them to the teacher's desk before hurrying after Rin, who has already left the classroom."

        stop music fadeout 4.0

        if _in_replay:
            return

    label .interstitial:
        scene bg school_hallway3
        with locationchange

        "She is not in the hallway, to my surprise. I wonder where she managed to run off to in just a few seconds. Would've been nice to talk more."

        "Well, not that I had much to say, except maybe get back at her for calling me a cynic."

        "It's surprisingly late. I already got used to school ending at the same time every day, so I can feel the extra hours in my head. And my gut."

        "My growling stomach reminds me that I am absolutely ravenous. I'm so hungry that I'd dare to try anything the cafeteria staff has deemed edible."

        scene bg school_cafeteria
        with locationskip

        $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
        play ambient sfx_crowd_indoors fadein 1.0

        "Even when I see today's delicacy, fried mystery lumps, my steely resolve doesn't fade. I stuff the dinner down without tasting it at all, which is probably for the best."

        "I don't have much homework to do, but what little I have won't get done by itself, so I stroll toward the dormitories."

        stop ambient fadeout 0.5
        scene bg school_dormhallway
        with locationskip

        $ renpy.music.set_volume(0.0, 2.0, channel="ambient")
        play sound sfx_doorknock2

        "Preparing for the post-homework lull, I knock on Kenji's door."

        "He responds from the other side, although I can't make out what he said. I try the door, but it's locked."

        show kenji neutral:
            center
            xpos 0.2
            easein 1.0 xpos 0.3
        with charaenter

        "After several seconds, the locks click open and he opens the door."

        show kenji:
            center
            xpos 0.3

        hi "Hi. Hey, could I borrow a book? The library was already closed after I got away from my club meeting."

        show kenji tsun
        with charachange

        "He is squinting even more than usual and his eyebrows are twitching nervously."

        play music music_kenji fadein 2.0

        ke "Club? That's dangerous, man. Indoctrination, groupthink, brainwashing, you name it."

        ke "High school clubs sow the seeds of conspiracy. Do you know how many secret societies have grown from high school clubs?"

        ke "Watch your back and don't get too deep in. You might not come back."

        hi "Okay, Kenji. So, how about that book?"

        show kenji neutral
        with charachange

        ke "Er, sure, but return them and don't spoil any of my books. No drinks, no food stains, no bodily fluids, capisce?"

        hi "Sure. Thanks."

        show kenji:
            ease 1.0 xpos 0.2 alpha 0.0
        with Pause(1.0)

        "Instead of letting me in, he retreats from the door, closing it again."

        show kenji:
            ease 1.0 xpos 0.3 alpha 1.0
        with Pause(1.0)

        "After a few seconds he returns with a stack of three thick books and hands them over to me."

        "Opening the topmost one, a familiar emblem stamped on the copyright page greets me."

        hi "Er, your books? These are from the school library."

        show kenji happy
        with charachange

        ke "They are now mine."

        hi "You stole these?"

        show kenji tsun
        with charachange

        ke "What are you talking about, man? I've been liberating these from the oppressive feminist movement that controls the library."

        hi "Please say 'oppressive feminist movement' doesn't mean that poor librarian girl, Yuuko. She couldn't even oppress a wet towel."

        show kenji:
            ease 1.0 xpos 0.2 alpha 0.0
        with Pause(1.0)

        hide kenji

        stop music fadeout 3.0

        "Kenji turns away, mumbling something I can't make out, and closes the door behind him."

        scene bg school_dormbathroom
        with locationchange

        play ambient sfx_shower fadein 1.0

        "Before going to my own room, I enter the bathroom. While washing my hands, my eyes catch my reflection from the mirror above the sink."

        scene ev hisao_mirror:
            truecenter
            zoom 1.2
            ease 20.0 zoom 1.0
        with locationchange

        "I try to look for the grimness Rin saw in me, but it's just the usual me inside the mirror that stares back."

        "I attempt to tell myself that this is what I've always looked like, but I realize I don't remember what I looked like half a year ago."

        stop ambient fadeout 6.0

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    call timeskip

    label .self_study:
        scene black
        with dissolve

        scene bg school_dormhisao
        with openeye

        "I wake up all sweaty, as if I had run a half-marathon in my sleep."

        play music music_pearly fadein 5.0

        "Odd; I don't recall sleeping badly. It sends a little pang of worry through me; I wouldn't want to have my heart acting up without being able to notice it."

        "Still, apart from this odd exhaustion right after waking up, I'm feeling just fine."

        "My mouth is like sandpaper and I have nothing to drink, so I have to go all the way to the bathroom to take my meds. On impulse, I decide to take a shower while I'm at it."

        scene bg school_dormbathroom
        show steam
        with locationskip

        play ambient sfx_shower fadein 1.0

        "While I'm in the shower, I make up my mind that this counts as morning exercise, if I properly compensate with a nice half-hour walk after school."

        "Obviously, I wouldn't want to risk possible complications by going running now. Besides, Emi will never know, and I think she's giving up on me, in any case."

        "Walking could be nice, anyway, just to get to know the area."

        "There's a big forest in the hills behind the school, or I could go down to the convenience store."

        hide steam
        with charaexit
        stop ambient fadeout 1.0

        "While still dabbing the moisture off my skin, I set out to find my uniform."

        "I quickly button up my shirt and pull on my pants before going outside."

        scene bg school_courtyard
        with locationskip

        "Normally during this time of the year, I'd be eagerly awaiting summer vacation. Having only been at school for a little over a week, I don't really have that kind of feeling."

        "I'm still savoring the school life and considering the sharp and awkward turn my life has taken. I haven't had the time to become preoccupied with getting free of it."

        "Besides, once vacations hit, it'll be a nice surprise for me if I'm not expecting it. Especially with the end of term exams looming ahead."

        "At least I don't have any catching up to do with my studies. My diligence has finally paid off."

        "I push myself past the boys gathered in the doorway and flop into my seat."

        stop music fadeout 2.0

        scene bg school_scienceroom
        with locationskip

        "From the corner of my eye I can see Shizune and Misha pause their unavoidably animated conversation and turn almost simultaneously in my direction."

        "They clearly want something from me; I can tell from the way Shizune smiles. It's too obnoxiously bright to be sincere and too calculated to be spontaneous."

        show shizu behind_smile at tworight
        show misha perky_smile at twoleft
        with charaenter

        play music music_normal fadein 2.0

        mi "Good morning~!"

        "Her greeting is made of one hundred percent cheer and bursting energy."

        hi "Mornin'."

        "I fail to put either of those into my response."

        show misha perky_confused
        with charachange

        mi "You don't look very energetic."

        hi "No wonder. I don't feel very energetic either. I think I didn't sleep well, but I'm not sure."

        show misha hips_grin_close
        with vpunch

        "She slaps me in the back and grins."

        show misha hips_smile_close
        with charachange

        mi "Cheer up a bit! It's a great day~!"

        show shizu basic_normal2
        with charachange

        "I catch Shizune's eyes. She has a strange, focused expression on her face, but she furrows her brow a little at direct eye contact and looks away."

        show shizu adjust_happy
        with charachange

        "For a moment, I think that Shizune caught a glimpse of my worries, somehow, and is pondering how to respond. But then she quickly straightens her glasses, and with them, her expression."

        show shizu basic_happy
        with charachange

        shi "…"

        show misha sign_smile_close
        with charachange

        mi "Anyway, we were wondering if you're still interested in that student council position, because we're going to make an offer that you can't decline~"

        hi "Wait, what? I wasn't really interested in the first place. You're putting words in my mouth."

        show shizu adjust_smug
        with charachange

        shi "…"

        mi "Not as such. But, wouldn't it be nice to hang out with us every day while also being useful to your school?"

        hi "Well, to tell you the truth, I… I kinda joined a club. So it'd actually be sort of hard for me to join the council too."

        hi "Even if I wanted to. Which I don't, as I said."

        show shizu behind_blank
        with charachange

        shi "…"

        show misha cross_smile_close
        with charachange

        mi "Is that so? Which club is it, Hicchan~?"

        hi "The art club."

        show shizu cross_angry
        with charachange

        shi "…"

        "Shizune's eyes glint in a sinister way as she scowls at me. With the way she looks, I'll be expecting the art club to lose its funding before lunch break, or the art teacher to mysteriously disappear from the face of the Earth."

        hide shizu
        hide misha
        with charaexit

        "Before she manages to comment, the teacher finally enters the classroom, getting Shizune and Misha off my back, and sending everyone rummaging in their bags for books and pens."

        "I did join the art club, but the first meeting didn't really boost my confidence. I'm not really sure what I'm doing it for."

        "I wish I could draw like Rin, but I don't know what I would do if I could. To what end would I use such a skill? I don't really know."

        $ renpy.music.set_volume(0.5,  1.0, channel="music")

        show ev hisaobird_0:
            center
            ypos 1.5 alpha 0.0
            easein 0.5 center alpha 1.0
        with Pause(0.5)

        show ev at center

        "Ignoring the teacher's sleep-inducing voice, I open my notebook to an empty page and press the needle-sharp graphite tip of the pencil onto it."

        "What to draw?"

        "I can't really think of anything good to draw."

        show ev hisaobird_1
        with charachangeev

        "As I hesitate and raise my hand, a meek black mark left on the previously blank paper seems aggravating."

        "I can't even seem to get to the starting line, let alone get started. It's almost a physical feeling of being held back. Annoyingly, it reminds me of my failed attempt at jogging with Emi."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        show ev:
            easeout 0.5 alpha 0.0 ypos 1.5
        show bg:
            yalign 0.0
            ease 20.0 zoom 1.1
        with Pause(0.5)

        hide ev

        "I look out of the window in desperation. Right then, a small bird takes flight from one of the cherry trees that grow everywhere on the school grounds."

        "I can't really see it clearly, and it's not like I could tell one tiny bird from another. But I pick it as my subject anyway."

        $ renpy.music.set_volume(0.5,  1.0, channel="music")

        show ev hisaobird_1:
            center
            ypos 1.5 alpha 0.0
            easein 0.5 center alpha 1.0
        with Pause(0.5)

        show ev hisaobird_2 at center
        with charachangeev

        "Conjuring up the image of a bird in my mind's eye, I turn my gaze back to the notebook and deliberately draw a thick line across the paper to get started."

        "It seems to be mocking me, as I can't follow up right away. Still, it's a start. Getting started is good."

        show ev hisaobird_3
        with charachangeev

        "I slowly sketch the picture on the notebook page, the image in my brain becoming clearer as the drawing takes shape."

        show ev hisaobird_4
        with charachangeev

        "It's really nothing, just that nameless nothing bird on paper, but that's not important."

        show ev hisaobird_5
        with charachangeev

        "My hesitation fades into the background along with the teacher's voice as I continue my struggle. The feathers form a simple pattern in my mind, but on paper it's a mess of too many rough lines despite my best efforts."

        show ev hisaobird_6
        with charachangeev

        "I realize that I don't really know what a bird's wing should look like, even if I try to think about it. I even put the pencil down and close my eyes for a moment, trying to trace the shape of a wing in my mind."

        show ev hisaobird_7
        with charachangeev

        "Being this serious about it all of a sudden makes me a little frustrated."

        show ev hisaobird_8
        with charachangeev

        "Art class in middle school was the 'easy' class in between exhausting subjects like math or Japanese. But there's this other side to art, the one that you see when you don't just fool around."

        show ev hisaobird_9
        with charachangeev

        "It's almost like a completely different thing."

        stop music fadeout 0.5

        mi "Hicchan?"

        show bg behind ev at center
        show shizu behind_blank_close behind ev at closeright
        show misha cross_smile_close behind ev at closeleft

        show ev hisaobird_9:
            center
            easeout 0.5 alpha 0.0 ypos 1.5
        with Pause(0.5)

        hide ev

        "I look up to see two girls staring back at me."

        $ renpy.music.set_volume(1.0,  0.0, channel="music")
        play music music_comedy fadein 1.0

        "Misha and Shizune have carried their chairs to my desk and are now standing by my sides, looking at my drawing."

        hi "How long have you two been there?"

        show misha hips_grin_close
        with charachange

        mi "I think you need more practice."

        show shizu basic_normal_close
        with charachange

        "Shizune draws a few sharp signs in the air between herself and Misha."

        show misha sign_smile_close
        with charachange

        mi "Shicchan agrees."

        "Rin said the exact same thing yesterday, but why did it sound less condescending?"

        hi "You shouldn't judge before I'm finished."

        hi "Besides, don't you know it's bad luck to see an unfinished piece of work?"

        show misha cross_laugh_close
        with charachange

        "Misha cracks in exuberant laughter."

        show misha hips_grin_close
        with charachange

        mi "What? Don't be silly~! There's no way that could be true."

        hi "Whatever."

        show shizu adjust_frown_close
        with charachange

        "Shizune's eyebrows furrow dangerously, and the movements of her hands become abrupt, like the slashing of a knife."

        show shizu behind_frown_close
        with charachange

        shi "…"

        show misha hips_frown_close
        with charachange

        mi "You should learn to take constructive criticism better."

        hi "I would if you'd actually offer some."

        "I know I'm getting too defensive and that Shizune is taking advantage of it, but I can't help it."

        hi "What are you two doing here, anyway?"

        show shizu basic_frown_close
        with charachange

        shi "…"

        "Misha wags her finger admonishingly at my nose."

        show misha sign_smile_close
        with charachange

        mi "Tsk, tsk, Hicchan. Were you not listening to the teacher at all?"

        show shizu behind_blank_close
        with charachange

        shi "…"

        show misha hips_smile_close
        with charachange

        mi "We have a group assignment, now."

        "I nod bleakly, and let them take the lead."

        show misha hips_grin_close
        with charachange

        mi "So, what do you think of the lesson for today?"

        hi "Not much of anything… I didn't listen to a word of it."

        show misha hips_frown_close
        with charachange

        "Misha slaps her forehead and shakes her head theatrically."

        mi "What are we going to do with you, Hicchan?"

        "Luckily, Shizune and Misha together are more effective than three or four normal people, so I can mostly slack on the assignment."

        "I try my best to offer at least some assistance, but I end up being mostly useless."

        stop music fadeout 2.0

        scene bg school_scienceroom
        with shorttimeskip

        play sound sfx_normalbell

        "The teacher keeps us in class five minutes past the lunch bells, but eventually lets us off the hook."

        "I quickly stuff my books into my bag while Shizune and Misha carry their chairs back to their own seats."

        "The failure of a bird-drawing ends up crumpled and stuffed in my pocket as I hurry outside."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .hisaos_smile:
        scene black
        with locationchange

        "After that morning class, and throughout the week, I keep bumping into Rin."

        scene bg school_hallway3
        show crowd
        show rin basic_absent at center
        with delayblinds

        play ambient sfx_crowd_indoors fadein 2.0

        rin "Hello."

        $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

        nvl clear
        nvl show dissolve

        play music music_daily fadein 2.0

        n "{vspace=60}This is somewhat natural, as our classrooms are adjacent. But rather than just cross paths in the hallway like people regularly do, we seem to pause at the sight of each other."

        n "We invariably end up talking a little bit, or just silently hanging out together."

        n "I think I'm getting used to being quiet in Rin's company, as it doesn't feel as awkward, any more. I am, by nature, somewhat introverted like her, so we fit together well."

        n "I think it's actually an anomaly for someone in this school to be so quiet. Most people here seem to love socializing."

        n "{vspace=30}It's something that I've noticed already, even though I haven't been here very long: people here talk a lot, and they talk all the time."

        nvl clear

        n "{vspace=60}It's a rare case when I see someone sitting alone, just spacing out or whatever. Obviously there are people like that here, too; that Hanako girl and myself, just to name two from my own class. But overall, they are a minority."

        n "At any rate, I wouldn't exactly call what Rin and I do 'socializing,' either, but it's something, at least."

        n "These occurrences themselves don't bother me, but the fact that they happen at all does."

        n "I'd hesitate to say that we are drawn together by something, but we certainly act as if we were."

        n "{vspace=60}However, this sense of a budding friendship is completely wrecked every time Rin opens her mouth."

        nvl hide dissolve
        nvl clear

        stop music fadeout 0.5
        stop ambient fadeout 0.5

        show rin basic_deadpannormal_close
        with characlose

        rin "Can I listen to your heartbeat?"

        play music music_rin fadein 0.5
        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        play ambient sfx_crowd_indoors fadein 4.0

        "She says this, or something else about as outrageous, and I have to fend off whatever nonsense her mind has cooked up during the preceding class of a subject that she is not interested in."

        "It seems Rin has taken a shine to my heart condition as some kind of an extension of her interest in the odder disabilities that people here have, and the consequences of said afflictions."

        "As I stand in front of her for a second too long, looking as flummoxed as I am, she concludes it is necessary to further clarify her request."

        show rin basic_deadpan_close
        with charachange

        rin "I know I can, but I mean, will you let me?"

        hi "Why?"

        show rin relaxed_doubt_close
        with charachange

        rin "Do I need a reason? I'm usually pretty bad with reasons."

        hi "Not per se, but if you want to do it, you probably do have a reason."

        show rin basic_deadpanamused_close
        with charachange

        rin "That's kinda clever. You are smarter than you look."

        hi "Also, I'd rather you not. I think these things should be private."

        show rin basic_deadpandelight_close
        with charachange

        rin "Private. I get it."

        hi "I can tell you something though, if it amuses you. I'm pretty sure it will. My heartbeat does sound very weird. Because of the… you know, condition."

        hi "And I hear it. All the time."

        show rin negative_spaciness_close
        with charachange

        rin "So you're paranoid."

        "It's not a question, it's a statement."

        hi "No, I'm not paranoid. The doctors said that abnormal attention to heartbeat is a common symptom of my… condition."

        show rin basic_deadpannormal_close
        with charachange

        rin "So, for you, it's normal to be paranoid."

        "It's not a question either."

        hi "One could also say that me being like this in the first place isn't normal, either, but what the heck."

        hi "Paranoia fits me fine."

        show rin basic_lucid_close
        with charachange

        rin "I don't think it's something that actually can fit anyone or anywhere."

        show rin basic_deadpan_close
        with charachange

        rin "You know, I ate an orange today for breakfast."

        hi "How was it?"

        "I'm vaguely proud of myself, managing to keep up with Rin's sudden change of topic."

        show rin basic_amused_close
        with charachange

        rin "Excellent. I don't remember when I last ate an orange. Because it's annoying to peel one."

        show rin basic_delight_close
        with charachange

        rin "It's on the list of things I want to learn properly."

        hi "How come you ate one, then?"

        show rin basic_deadpanamused_close
        with charachange

        rin "Emi had some, so she peeled one for me."

        hi "Good for you."

        show rin relaxed_nonchalant_close
        with charachange

        stop music fadeout 6.0

        "Rin stretches her back and yawns, and says nothing further."

        "She throws me a glance from the corner of her eye while she watches people pass by, but I couldn't say why."

        "I realize, though, that this is the first time I've talked naturally about my condition with anyone. In a way."

        stop ambient fadeout 4.0

        "A group of boys walk past us to Rin's classroom, but she doesn't pay them any mind. They pay none to her, either. My mind wanders off, spurred by the silence."

        nvl clear
        nvl show dissolve

        $ renpy.music.set_volume(0.5,  0.0, channel="music")
        play music music_pearly fadein 1.0

        n "{vspace=90}Maybe I should've let her listen to my heart. It's not like it matters. Nothing really matters that much, at the end of the day."

        n "I start feeling depressed for no reason, again. It's like a tidal wave out of nowhere rolling over my consciousness, submerging me underwater."

        n "I feel a sigh coming out of my mouth, and I turn away from Rin, pretending to read a poster on the wall. It's an advertisement for the school festival, promoting an event almost a week past."

        n "The difference between me and Rin is that I'll be more likely than not dead before turning thirty, while she can't eat oranges without help."

        n "{vspace=60}I can't decide which one of us is worse off."

        nvl hide dissolve
        nvl clear

        scene black
        with delayblinds

        nvl show dissolve

        n "{vspace=90}I try to grasp the passing of time, but it seems hard. I'm still used to the rhythm of the hospital, where trivialities such as the day of the week or time of day didn't really matter."

        n "Everything was the same, no matter what."

        n "Rediscovering the significance of time is an oddly disorienting experience, and I find myself enjoying the fact that I can categorize events in this fashion."

        show ev watch_black:
            center
            alpha 0.0
            linear 1.0 alpha 1.0

        n "The relevancy of a ticking clock is surprisingly delightful, and I decide to start wearing an analog wristwatch, something I didn't use to do before."

        n "{vspace=30}When I finally ask Rin on Thursday about something that's been bothering me for the entire week, it's already lunch time."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")

        nvl clear
        nvl hide dissolve

        scene bg watchhallway_blur
        show ev watch_worn at truecenter
        with locationchange

        "The time is somewhere between 11:06 and 11:07, as my watch doesn't have a hand to show seconds. It's the old-fashioned kind with a black leather strap and titanium casing."

        "It doesn't look flashy, but a wristwatch doesn't need to."

        show ev:
            easeout 0.5 ypos 1.0 alpha 0.0

        scene bg school_hallway3
        show crowd behind ev
        show rin basic_awayabsent behind ev at center
        show ev watch_worn:
            truecenter
            easeout 0.5 ypos 1.0 alpha 0.0
        with locationchange

        hide ev

        play ambient sfx_crowd_indoors fadein 2.0

        hi "Hey."

        show rin basic_absent
        with charachange

        hi "Remember that sketch you made of me? How you said I looked grim and gloomy or something?"

        hi "I'd like to know what you meant by that."

        show rin negative_spaciness
        with charachange

        "She gives me a weird look and tilts her head a few degrees to the left, but doesn't say anything for a while."

        rin "Well, you see…"

        show rin basic_deadpanupset
        with charachange

        stop ambient fadeout 2.0
        stop music fadeout 2.0

        rin "We've known each other for two weeks and I haven't seen you smile even once."

        "Her striking observation gives me pause."

        nvl clear
        nvl show dissolve

        n "{vspace=90}Have I stopped smiling?"

        n "{vspace=30}I have to take what she says as truth. She has no reason to lie."

        n "Something about the way she puts it annoys me. I frown at Rin, then try to correct my expression to look less depressed."

        n "I haven't been in the cheeriest of moods during the past few months or so, this is true."

        n "Does it show so much that someone like Rin can tell, after so little contact with me?"

        n "Should I try to smile more at Rin? Maybe she could appreciate it, having such a neutral face herself almost all the time."

        n "{vspace=30}Have I really stopped smiling?"

        nvl hide dissolve
        nvl clear

        play ambient sfx_crowd_indoors fadein 2.0

        hi "I see."

        hi "Should I smile more?"

        show rin relaxed_nonchalant
        with charachange

        rin "I don't mind either way. Be as you are; you can't help being Hisao anyway."

        hi "But it bothers you?"

        show rin basic_absent
        with charachange

        rin "I just noticed it, that's all."

        show emi excited_smile at offscreenleft
        with None

        show rin at tworight
        show crowd at bgright
        show bg at bgright
        show emi at twoleft
        with charamove

        play music music_emi fadein 0.2

        "Emi skips along the hallway, jumps to a sharp stop when she reaches us, and lightly pats Rin's shoulder."

        show emi basic_happy
        with charachange

        emi "Ready for lunch?"

        show rin basic_deadpanupset
        with charachange

        rin "Depends on what lunch is today. Remember that stew from March? Never again, that."

        show emi basic_closedgrin
        with charachange

        emi "Let's go anyway. I'm starving!"

        hide emi
        hide rin
        with charaexit

        "As they are about to depart, Emi turns from her friend to me, seemingly as an afterthought, and smiles charmingly."

        show emi sad_grin at center
        with charaenter

        emi "By the way, Hisao…"

        "Her tone is way too sweet and soft to be sincere. I can sense the trap about to be sprung upon me by this miniature health-devil."

        "I know what she's about to say even before she continues, because I've been trying to avoid her all week."

        show emi excited_proud
        with charachange

        emi "I still haven't seen you at the track this entire week."

        hi "Maybe I've been there when you haven't."

        show emi sad_annoyed
        with charachange

        emi "That's impossible. I'm there all the time."

        hi "But you sleep and go to class."

        show emi basic_annoyed
        with charachange

        emi "I do those at the same time as you do."

        hi "Yeah, I know, I know. I just… haven't been able to pick myself up."

        hi "Don't rat me out to the nurse, okay?"

        hi "Running just isn't my thing, and I haven't come up with a good alternative."

        show emi excited_happy
        with charachange

        emi "Why don't you come to the track meet this weekend? Maybe you'll get inspired."

        hi "Track meet?"

        show emi basic_happy
        with charachange

        emi "Yeah! People from a few other schools come here for some friendly track and field action. It's on Sunday afternoon."

        "I can't think of any reason not to go."

        hi "Sure. I'll come and cheer for you. I guess you'll be running?"

        show emi excited_proud
        with charachange

        emi "Of course! You'll get to see me beat them all!"

        show emi basic_grin
        with charachange

        emi "But bye now! If I don't get something to eat, I'll die."

        hi "See you later."

        hide emi
        with charaexit

        stop music fadeout 3.0

        hi "Bye Rin. I promise I'll smile next time."

        "I call after her, as a bit of an afterthought. Afterward, I feel embarrassed about it, and wonder why I said anything at all."

        stop ambient fadeout 1.0

        scene ev hisao_mirror_800
        with shorttimeskip

        "That night, when I'm doubly certain that Kenji won't be barging in the bathroom, I look in the mirror and smile at my reflection."

        "The me in the mirror smiling at the me in the bathroom looks awfully fake."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .things_you_like:
        play music music_happiness fadein 2.0

        scene bg school_library
        with locationchange

        "Having exhausted the books Kenji lent me in just a few nights, I go back to the library, deeming it a safer alternative for getting my reading fix."

        "I return the books he had stolen while I'm at it, to Yuuko's delight. I don't tell her where I got them, though."

        show yuuko happy_down at center
        with charaenter

        yu "Wow, you sure read a lot, don't you?"

        hi "Yeah, I guess I do."

        hi "I mean, I do. Even I think it's weird. I think I might have a reading problem. Maybe I'm a junkie."

        show yuuko panic_up
        with charachange

        yu "No no, I didn't mean it that way. It's not weird at all, and being addicted to reading is a lot better than being addicted to… to something else."

        hi "Yeah, I know. It was a joke."

        "I smile at her reassuringly and drop the books on the counter so Yuuko can check them out. I feel tired, so I sit down in the vacant chair in front of her desk."

        show yuuko neutral_up
        with charachange

        "While Yuuko goes through the modest pile of reading material I found, I let my gaze wander around the library."

        hide yuuko
        with charaexit

        "At the tables, a pair of girls is chattering in hushed tones rather than working on their homework."

        "The short-haired one notices me looking in their direction and waves at me. When I raise my hand back, they glance at each other and giggle in unison."

        "I'm not sure how I should feel about that, so I decide it's a good thing. The one who waved at me has a horrible case of epilepsy."

        "I saw her having an attack a few days ago. It was one of the most disturbing and scary things I've seen in a very long time."

        "Yet, there she is, happily chirping away about whatever, as if she doesn't have a care in the world."

        hi "You know, this school is really something else."

        show yuuko panic_up at center
        with charaenter

        "Yuuko raises her eyes from the books she was going through, slightly startled. She adjusts her glasses and puts on a nervous, confused smile."

        show yuuko smile_down
        with charachange

        yu "What do you mean?"

        hi "I don't really know how to explain it. It's just that everyone's so… active, or …how should I put it?"

        hi "It's not just the festival thing, I think, even though I haven't been here that long, but it's everything."

        hi "People talk more, work harder and just… are… more than in any other school I've seen before."

        "I'm struggling for words, but it feels like I'm speaking honestly."

        menu:
            with menueffect
            hi "This school feels so alive."

            "It's refreshing." if True:
                $ its_refreshing = True

                call a2rc2o1

            "It makes me feel like I'm stuck." if True:
                $ its_refreshing = False

                call a2rc2o2

        show yuuko worried_up
        with charachange

        yu "I don't think that's a bad thing."

        hi "Yeah, me neither."

        "Suddenly I realize that I've just been babbling my thoughts to Yuuko, out of the blue. She's a bit of a jumpy person, so I fear I might've made a bad impression."

        "She's looking at me with what I hope is curiosity rather than horror, so I figure she's all right."

        hi "Sorry for suddenly talking about weird stuff like this. I didn't mean to trouble you."

        show yuuko smile_down
        with charachange

        yu "Oh no, it's not troubling. I'm happy to listen if you feel like talking."

        show yuuko neutral_down
        with charachange

        yu "It makes me feel a little reliable, too."

        "Yuuko smiles sweetly and a little bit ironically at that. I respond with a thankful smile of my own."

        "As she pushes the neat stack of books across the counter, I stand up and gather them in my arms."

        show yuuko closedhappy_up
        with charachange

        yu "Here you are."

        hi "Thank you."

        show yuuko neutral_up
        with charachange

        yu "I guess we'll be meeting each other again. Please come here anytime."

        "Yuuko's kindness is heartwarming."

        hi "You can count on it. See you later."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .target_audience:
        scene bg school_courtyard
        show crowd
        with locationchange
        play ambient sfx_crowd_outdoors fadein 7.0

        "The morning of the track meet greets me with a brilliant sunshine from a crystal blue sky."

        "While I leisurely stroll towards the track, I decide this is a good sign. Of what, I'm not sure; this event isn't as exciting for me as it seems to be for a large portion of the student body."

        "I'm even less interested in watching sports than I am in participating, but cheering for Emi is a good cause."

        "I'm not expecting this to be any sort of amazing and spectacular experience, but it can't hurt. I'd probably be spending the time reading while cooped up in my room, otherwise."

        scene bg school_track
        show crowd
        show rin basic_absent at center
        with locationchange

        "When I approach the bleachers, I spot Rin emerging from the crowd right before she spots me."

        show rin basic_deadpannormal
        with charachange

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

        show rin negative_spaciness
        with charachange

        "Rin shrugs. Seemingly bored with our conversation, she turns on her heel and heads back toward the stands."

        hi "So, are you excited about this?"

        show rin basic_deadpan
        with charachange

        rin "Not really."

        hi "Me neither."

        show rin basic_absent
        with charachange

        rin "Then why did you come?"

        hi "Why did you?"

        "She doesn't reply at all, so I decide not to, either."

        "We enter the bleachers, and Rin nods upwards."

        show rin negative_spaciness
        with charachange

        rin "Up there."

        show rin basic_deadpancontemplation
        with charachange

        "Rin leads the way, and soon we've settled down on an almost-empty bench."

        $ renpy.music.set_volume(0.3, 3.0, channel="ambient")

        show rin at tworight
        show bg at bgright
        show crowd:
            linear 1.0 alpha 0.0
        with charamove

        hide crowd
        with None

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

        rin "This is no good?"

        show meiko happy
        show rin basic_awayabsent
        with charachange

        "The woman laughs at Rin and shakes her head, apparently unable to find a comeback for that. I know the feeling."

        show meiko smile
        with charachange

        emm_ "Well, I suppose you've always been one to go out for one thing and bring back another."

        emm_ "But I'm being rude! I haven't introduced myself."

        emm_ "I'm Meiko Ibarazaki. I'm sure that if you know this girl, you've at least met my daughter, too."

        show meiko happy
        with charachange

        emm "Pleased to meet you."

        "Well, that explains it. She's like a taller, older, more motherly Emi."

        "Apart from her hair being somewhat darker than her daughter's, there's really no mistaking the resemblance."

        show rin basic_absent
        show meiko smile
        with charachange

        hi "Sorry, I'm Hisao. Hisao Nakai. Nice to meet you."

        show rin basic_lucid
        with charachange

        rin "I'm Rin Tezuka."

        show meiko happy
        show rin basic_awayabsent
        with charachange

        "Mrs. Ibarazaki laughs again - she really does resemble her offspring - and then leans back a little on her seat and raises an eyebrow."

        $ renpy.music.set_volume(0.0, 0.5, channel="ambient")

        show meiko serious
        with charachange

        stop music fadeout 1.0

        emm "So, now that we all know each other, how long have you and Rin been dating?"

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

        hi "We're not—"

        show meiko happy
        show rin basic_awayabsent
        with charachange

        emm "I know, but it's funny to watch you squirm."

        show meiko wink
        with charachange

        emm "I'm sorry. Forgive an old woman her amusements."

        "She chuckles again to herself."

        "Old woman?"

        "She sure doesn't look that old to me."

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

        "By the time she rounds the final turn, a few of the other runners have caught up with her."

        "But she puts on a final burst of speed that leaves them at least a half second behind."

        scene ev emitrack_finish
        with locationchange

        stop ambient fadeout 1.0
        play sound sfx_crowd_cheer

        "Mrs. Ibarazaki whoops and shouts, applauding wildly, and generally looking like any other parent cheering on their child."

        "Emi bounds off the track, looking pleased with herself."

        play music music_daily fadein 2.0

        scene bg school_track at bgright
        show meiko happy at twoleft
        show rin basic_deadpandelight at tworight
        with locationchange

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

        "We fall silent as the next event prepares to start."

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

        hi "You seem pretty into this stuff. I'm surprised; I thought you said this wouldn't be exciting."

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
        with locationchange

        "As the starter tells everyone to get set, her head snaps up, and her eyes narrow slightly."

        "Her mouth curls upward in what could be a grin and could be a growl."

        play sound sfx_startpistol
        play ambient sfx_emisprinting

        scene ev emi_run_face_zoomin
        with locationskip

        "When the pistol goes off, it's as if she's been unleashed from a cage, like she was always moving at this blinding speed, but we couldn't see it happening until the starter's pistol dispelled the illusion of motionlessness."

        stop ambient fadeout 1.0
        play sound sfx_crowd_cheer

        "As soon as she crossed the finish line, the fierce look was replaced by her normal grin."

        "The conquering general returning to his farm."

        hi "Amazing."

        hi "She's really amazing. I've never seen someone move that fast."

        scene bg school_track at bgright
        show meiko smile at twoleft
        show rin basic_deadpanamused at tworight
        with locationchange

        emm "Well, don't look at me, I'm far too relaxed to run that fast."

        stop sound fadeout 9.0

        show meiko worry
        show rin basic_awayabsent
        with charachange

        emm "No, I think Emi's prowess all came from her father's side."

        "At the mention of Emi's father, Mrs. Ibarazaki looks wistful, almost sad."

        emm "He got her into running, you know."

        show rin basic_absent
        with charachange

        hi "Ah, really? I didn't know that."

        "I leave it at that, and don't say anything for a little while. I get the feeling this is something personal I shouldn't ask about."

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

        "While waiting for the relay to start, I peer at Rin. She seems uninterested in her surroundings, myself included."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=120}That remark she made before is still stuck in my head."

        n "'Emi's the most Emi when she runs.'"

        n "It does make sense, now that I think about it. After seeing her run now, I can believe that Emi gives her all on the track."

        n "Sports are more than a hobby or even a competition, to her. They're a defining aspect of her life."

        n "What about Rin, then? Does she feel the same way about art? Considering the persistence she displayed before the festival, I could easily believe it."

        n "Did I see Rin at her 'most Rin' when she was painting the mural?"

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl hide dissolve
        nvl clear

        "The relay's about to begin, but I don't see Emi anywhere."

        hi "I thought Emi ran the relay."

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
            truecenter
            ease 20.0 zoom 1.05 topleft
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

        "Emi flies across the finishing line with a great leap, just barely ahead of the next runners, but still in first."

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")

        scene bg school_track
        show rin negative_worried at center
        with locationskip

        show rin basic_absent
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

        stop music fadeout 5.0
        stop sound fadeout 5.0
        play ambient sfx_crowd_outdoors fadein 2.0

        scene bg school_track_on
        show crowd
        show rin basic_awayabsent at center
        with locationskip

        "Emi is surrounded by her teammates, all of them congratulating her on the run."

        "Rin seems to be waiting for Emi to notice that she's arrived."

        "It doesn't seem her style to draw attention to herself. Or to emote beyond shrugging."

        "Being more impatient than Rin, I wave to Emi in her stead. She looks up and grins happily at us."

        show bg at bgright
        show crowd at bgright
        show rin at tworight
        with charamove

        play music music_emi fadein 1.0

        show emi basic_closedhappy_gym at twoleft
        with charaenter

        emi "Hey, you showed up!"

        show rin basic_deadpanupset
        with charachange

        rin "We would have brought you a crown of laurels, but Hisao didn't find one."

        show emi basic_grin_gym
        with charachange

        hi "Neither did you."

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

        hi "Very impressive."

        show emi basic_closedgrin_gym
        with charachange

        "Emi seems pleased with this assessment."

        "I don't mention how much more impressive her performance is given her lack of legs. I figure she knows that already."

        "Besides, it seems like it would take away from her efforts, somehow."

        show emi basic_grin_gym
        show rin basic_awayabsent
        with charachange

        emi "Great to hear! I was worried that I looked a little slow on the relay, but I guess I did fine, huh?"

        show emi basic_closedgrin_gym
        with charachange

        "Emi giggles, and then seems to remember something."

        show emi basic_happy_gym
        with charachange

        emi "Oh, before I forget…"

        emi "Rin and I are going to do something next Sunday as a post-track meet celebration!"

        show emi excited_proud_gym
        with charachange

        emi "You should come along!"

        show emi sad_grin_gym
        with charachange

        emi "Normally we do it the day after, but since today is Sunday, I've got homework and class and all that stuff to take care of."

        show rin basic_absent
        with charachange

        hi "Oh sure, I'd love to."

        show rin basic_awayabsent
        show emi excited_laugh_gym
        with charachange

        emi "Great! It's a promise, then!"

        show rin basic_absent
        with charachange

        hi "Oh, right. Your mom wanted to say she's proud of you."

        hi "She'll call you later tonight."

        show emi basic_happy_gym
        show rin basic_awayabsent
        with charachange

        emi "I thought I saw her in the stands!"

        show emi basic_closedhappy_gym
        with charachange

        emi "I'm glad she made it!"

        "Teammate" "Hey, Emi! You're going to miss the medal ceremony!"

        show emi basic_shock_gym
        with charachange

        emi "Oh yeah, thanks!"

        show emi basic_grin_gym
        with charadistant

        "She turns to Rin and myself."

        emi "You don't have to stick around for this part. It takes forever."

        show emi excited_proud_gym
        with charachange

        emi "Besides, you should get cracking on your homework now if you don't want to be up late, Hisao."

        play sound sfx_emipacing

        show emi at offscreenleft
        with charamovefast

        hide emi

        stop sound fadeout 2.0

        show bg at center
        show crowd at center
        show rin at center
        with charamove

        stop music fadeout 5.0

        "Emi skips back to her teammates, leaving me and Rin by ourselves."

        "Neither of us has the slightest interest in the post-competition ceremonies, so we silently get away and back to the quad."

        $ renpy.music.set_volume(0.3, 2.0, channel="ambient")

        scene bg school_courtyard
        show crowd
        show rin relaxed_nonchalant at center
        with locationskip

        "Rin yawns without even trying to restrain herself and shuffles her feet around restlessly."

        "I feel awkward, but less so than if I was with someone else. Still, I'm left hanging, not knowing what I should say next."

        hi "Emi was great, wasn't she?"

        show rin basic_deadpannormal
        with charachange

        rin "She was great. I am very jealous of her."

        hi "Why?"

        show rin basic_awayabsent
        with charachange

        rin "Like I said, don't you think it's great to be able to really be yourself?"

        "It sounds weird, coming from Rin."

        hi "I don't think you, of all people, should have trouble finding a way to express yourself."

        hi "Don't you have your paintings?"

        show rin basic_absent
        with charachange

        stop ambient fadeout 1.0

        "She turns to look at me. For the first time, I see in her eyes this strange, hollow expression that I think must be unique to her."

        rin "No, you see, the problem is that I'm not really sure who I am."

        stop ambient fadeout 1.0
        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .eternity_in_an_hour:
        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        scene bg school_classroomart at right
        with locationchange

        "Today's art club meeting is currently on hold while everyone waits for Nomiya to show up. I take this time to try and explain my theory about Yamaku to Rin."

        "I've tried to figure out what exactly about the school feels so special to me; that concept I unsuccessfully tried to explain to Yuuko the other day."

        "It's still difficult, but the track meet and the time I've spent observing my fellow students have helped my ideas mature a little."

        show rin basic_absent_close at center
        with charaenter

        hi "Have you noticed that people talk all the time?"

        hi "I can't really explain it, but…"

        "Once again, as I try to explain my observation, I'm struggling for words."

        "The student body is heavily cliqued, and I'm only now beginning to make sense of the intricate grouping and popularity networks. And yet, the feeling of being a part of a group is stronger here than I remember it being in my old schools."

        hi "I'm trying to say that this school isn't like other schools. Or at least, the students aren't, even after discounting the obvious."

        hi "…Do you know what I mean?"

        show rin basic_deadpan_close
        with charachange

        rin "I don't know what you mean."

        hi "Oh, well… whatever, then."

        "I want to pursue the issue, but at that point, Nomiya arrives."

        hide rin
        with charaexit

        show bg at left
        with charamove

        show nomiya smile at center
        with charaenter

        play music music_happiness fadein 2.0

        "The teacher is wiping sweat from his forehead with a handkerchief and breathing rather heavily. He quickly glances over the room, then settles down a bit."

        show nomiya veryhappy
        with charachange

        no "Hello, hello; apologies for being late."

        show nomiya talk
        with charachange

        no "Is everyone present? Good!"

        no "I must confess, I haven't really planned anything for today as I have been extremely busy, lately. But I'm sure we can come up with something entertaining."

        show nomiya frown
        with charachange

        no "Anyone have any suggestions? I was thinking we could have a discussion circle since we haven't had one in a while. I, at least, found the last one magnificently enjoyable."

        "There are some murmurs here and there, but nobody raises their voice in support of or against Nomiya."

        show nomiya talk
        with charachange

        no "We could delve into various movements of art. Or does someone have a good topic in mind?"

        no "Come on, throw it out there. It doesn't matter if it's silly or odd, we can always cook up something interesting!"

        "Nobody seems to be brave enough to make such a suggestion."

        "As the awkward silence refuses to be broken, I lift my hand in the air."

        show nomiya smile
        with charachange

        no "Oho? Our newest friend seems to have something on his mind. Speak up, my boy, speak up!"

        hi "Um, well… I don't know about anyone else, but I've always wondered why art exists in the first place."

        stop music fadeout 2.0

        "My voice trails off. A silence sets in the room, and nobody makes a followup on my meek suggestion."

        "Then, the teacher bursts in laughter."

        show nomiya veryhappy
        with charachange

        no "Hohoho, excellent!"

        no "Very good, very good indeed. Right out of the gate with the big one, huh?"

        no "Fabulous!"

        "Chuckling, he shifts some papers around on his desk for a few moments. When he's done, he appears to have made some sort of decision."

        show nomiya smile
        with charachange

        no "Very well, then. Let us run with this and see where it gets us, shall we?"

        show nomiya talktongue
        with charachange

        no "Oh my, even an old fogey like me gets excited when such delicious enthusiasm is present. Oh my, indeed."

        show nomiya smile
        with charachange

        no "Let me gather my thoughts a moment so I can figure out a good starting point for everyone."

        "For some reason the teacher seems to be almost literally bursting with excitement. He scribbles a few things down on a loose sheet of paper, then cleans his glasses with the handkerchief."

        show nomiya dreamy
        with charachange

        "He strikes a pose, then freezes for an overtly dramatic, artistic pause that spans what must be half a minute."

        "It's so quiet I could hear a pin drop."

        show nomiya talk
        with charachange

        play music music_another fadein 0.5

        no "First, let's come up with a few questions that we want answered, such as 'What is art?' and 'Why does art exist?'"

        show nomiya smile
        with charachange

        no "Anyone have any questions that might be related?"

        "The boy with sunglasses pipes up almost immediately. His voice is soft and quiet, and I have a hard time making out what he says."

        "Sunglasses boy" "What defines an artist?"

        "After him, another question comes up."

        "Student" "If I fill a cardboard box with water and call it art, is it art?"

        show nomiya veryhappy
        with charachange

        "Everyone laughs at that, even the teacher."

        no "Great! Wonderful, all of these!"

        show nomiya talk
        with charachange

        no "Let me start by saying that this is not a clear-cut issue by any means, and as such, I'm not going to give any answers to you. I'm only going to speak from my own perspective."

        no "Scholars have argued about these sorts of questions since time immemorial, and there has never really been a broadly applicable consensus reached."

        show nomiya smile
        with charachange

        no "There are, however, some qualities that most tend to generally agree upon. Hopefully, you all should find these acceptable as well."

        show nomiya dreamy
        with charachange

        no "In short, art defines itself. It simply cannot be contained to a definition from the outside, since the boundaries of art expand and contract from forces within."

        show nomiya serious
        with charachange

        no "Every day, someone somewhere comes up with something completely outrageous that challenges any and all preconceptions."

        show nomiya frown
        with charachange

        no "The core reason for this is that rather than the rational side of the mind, art appeals to the intuition, the instinct, the primal. You would find it very hard to explain why exactly it is that you enjoy some particular style or piece, no?"

        "He doesn't wait for a response before continuing."

        show nomiya veryhappy
        with charachange

        no "This is exactly why."

        show nomiya frown
        with charachange

        no "So, art is this sort of wild, uncontrollable thing that lurks somewhere deep in our subconscious. Now, why does it exist?"

        "Nomiya apparently expects someone to pipe up with a guess, but as nobody dares to interrupt his inspired speech, he continues."

        show nomiya dreamy
        with charachange

        no "It was a trick question! You see, art also validates itself."

        show nomiya talk
        with charachange

        no "Generally speaking, you might say that art exists for no other purpose than itself. It's something that exists merely to leave a mark in history."

        show nomiya serious
        with charachange

        no "It's the defiance of a mortal against the face of darkness, as was once said. Art is truly the proof of our existence. You all should know that human culture and civilization are tightly tied to the existence of art."

        show nomiya frown
        with charachange

        no "Then, what about artists? What drives a man to dedicate his life to a thing so fickle and mysterious that it even defies definition?"

        show nomiya serious
        with charachange

        no "There are as many answers for this as there are artists, but if I had to put it into words… an artist doesn't make art because he can, but because he must."

        "Nomiya takes a pause, and his gaze sweeps over his audience, eyes flaring with passion."

        show nomiya frown
        with charachange

        no "It is obvious that art touches the very soul of each and every human being in one way or another. So, if you were given a chance to connect with your fellow man in such a fundamental way, how could you not?"

        show nomiya talk
        with charachange

        no "There is a poem I'm very much fond of, and I shall recite the most well-known part of it to you now. I feel that, for me personally, of all possible things it captures best the essence of what it means to be an artist."

        stop music fadeout 2.5

        "Nomiya leans against the desk as he clears his throat in preparation."

        "Looking at some distant place, he utters the words in the heavy afternoon air with his soft basso voice."

        show nomiya dreamy
        with charachange

        play music music_one fadein 0.5

        no "To see a world in a grain of sand"

        extend "{vspace=30}And a heaven in a wild flower,"

        no "Hold infinity in the palm of your hand"

        extend "{vspace=30}And eternity in an hour."

        "There is a solemn and unbelievably awkward silence after he finishes reciting the short fragment. Nobody dares speak a word."

        "Nomiya clears his throat again."

        show nomiya talk
        with charachange

        no "To be an artist is to see the world in a grain of sand."

        show nomiya dreamy
        with charachange

        no "You see, dear children, without art, there would not be much to live for in this world. It is a most profound thing."

        "He is clearly touched by this notion. I almost expect to see a lone tear rolling down his rough cheek, but it never comes."

        show rin basic_awayabsent_close:
            offscreenright alpha 0.0
            ease 1.0 xpos 0.9 xanchor 0.5 alpha 1.0
        with None

        show nomiya:
            ease 1.0 twoleft alpha 0.0
        show bg at bgleft
        with charamovefast

        show rin:
            center
            xpos 0.9
        hide nomiya

        "I turn to Rin and whisper to her."

        hi "So how is this a discussion circle?"

        "She shrugs nonchalantly back at me."

        show rin basic_deadpan_close
        with charachange

        rin "The previous ones were the same."

        "To his credit, Nomiya does try to get some debate going, but the club seems to be reluctant to comply."

        "I feel a bit guilty about opening my mouth. Maybe we would've been spared from this."

        stop music fadeout 1.5

        show rin basic_awayabsent_close
        with shorttimeskip

        play music music_normal fadein 2.0

        "As the meeting comes to a close, I realize we haven't once touched any paint or pens today, and I feel somewhat disappointed."

        show nomiya smile at twoleft
        with charaenter

        "Nomiya suddenly appears next to us. He seems to be still fired up from the speech he delivered."

        "His cologne smells musky and saccharine at the same time, giving me an instant headache, even though I'm not sensitive to perfumes. He is looking at Rin like a hungry wolf."

        show nomiya talk
        with charachange

        no "Tezuka, do you remember Mrs. Saionji, who visited us at the festival?"

        show rin basic_deadpannormal_close
        with charachange

        rin "I think so."

        show nomiya veryhappy
        with charachange

        no "I'm going to tell you something amazing."

        show nomiya smile
        with charachange

        no "The thing is, she's a very well-known gallerist around here. It turns out I might be able to get her to consider having some of your work put on display."

        "He ends his sentence with a dramatic gesture. It seems he's expecting Rin to show some sort of joyous, shocked reaction at such grand news, but she just stares at him blankly."

        show nomiya veryhappy
        with charachange

        no "Magnificent, isn't it? This could be a real chance for us to get ahead, girl."

        show rin basic_surprised_close
        with charachange

        rin "But…"

        show nomiya frown
        with charachange

        no "Now now, I know what you're about to say. Yes, it wouldn't be a simple affair, but I think this is an absolutely fantastic opportunity."

        no "Frankly, I wouldn't be surprised at all if we even made it big! This could be the first step! And then, when the word is out, we strike while the iron is hot! Right, Nakai?"

        hi "Er, yeah, it does sound pretty great. If you're into that kind of thing."

        show nomiya veryhappy
        with charachange

        no "See? We should definitely not let this one pass, am I right?"

        show rin negative_confused_close
        with charachange

        rin "I don't… really."

        stop music fadeout 7.0

        "Rin seems to be troubled for some reason. I can't figure out why. What Nomiya is saying does indeed sound like a possibly great thing."

        "She looks pretty down though, and confused. I've never seen her like this."

        show nomiya talk
        with charachange

        no "So, what do you think?"

        "Rin looks up to her teacher's glowing face, then back down at her desk."

        show rin negative_worried_close
        with charachange

        rin "I'll think about it."

        "Nomiya is at last taken slightly aback by Rin's lack of superlative delight. Then he smiles widely at her and gently pats her head."

        show nomiya smile
        with charachange

        no "Good girl."

        hide rin
        hide nomiya
        with charaexit

        "The club meeting is finally over, and as I lazily collect my things and help clean up, I start feeling exhausted, for some reason. There isn't much to do, however, so it's over quickly."

        if _in_replay:
            return

    label .underwater_and_maple:
        scene bg school_staircase2
        show rin negative_spaciness_close at tworight
        with locationskip

        "I catch up to Rin who left the club room just a moment earlier, so we're walking down the stairs to the ground floor while I try to go over Nomiya's passionate speech about art, and Rin seems to be lost in thought."

        "Not an unusual state for her, I've learned, but something about her expression makes me feel uneasy."

        hi "Penny for your thoughts."

        show rin basic_deadpancontemplation_close
        with charachange

        rin "That'd be too cheap."

        hi "You're just overpricing your thoughts."

        show rin basic_lucid_close
        with charachange

        rin "I wouldn't be able to sell them anyway. I'm not sure what I'm thinking yet. That'd be fraud too, like stealing a candy from a baby."

        hi "That's theft, not fraud."

        show rin basic_deadpanupset_close
        with charachange

        rin "I have to think about what I think."

        hi "Is this about what the teacher said? Getting your work put on display and all that?"

        scene bg school_lobby
        with locationchange

        "She doesn't answer, but stops in her tracks as we reach the lobby."

        "We're the only people around, so it's very quiet. Footsteps echo from a few floors up as someone hurries along a hallway."

        show rin negative_annoyed at center
        with charaenter

        rin "I think I'm going to go somewhere elsewhere."

        "I think she really is troubled."

        hi "Want company?"

        hi "I can't promise much help with the thinking, but it's not like I have much else to do, and I'm supposed to do some light exercise."

        show rin basic_absent
        with charachange

        rin "If you like."

        play ambient sfx_parkambience fadein 20.0

        scene bg school_backexit
        with locationskip

        "Rin leads me outside, to the wall behind the dormitories. There is a small back gate there, made from the same wrought iron as the main gate. It leads to the shadowy woodland park behind the school."

        "The gate is rusty, as if it hasn't seen much use. However, it sits open, so we pass through. It's not forbidden for students to leave the grounds, but somehow I feel a little uneasy."

        scene bg school_forest1
        with locationchange

        "A path leads deeper into the forest. Tall zelkova and maple trees rustle in the wind, their canopies creating patches of chill air hanging in the places where the shadows fall."

        "The forest smells strongly of earth. I almost feel cold, even though the midsummer day is as hot as ever."

        "Rin trudges ahead like a sleepwalker, surefooted but with no apparent destination in mind. Her thoughts seem to be somewhere else. I follow a few steps behind, taking more care to watch where my feet land."

        "The path follows the land uphill at a low angle, sometimes making little detours downhill before climbing back upward. The muted brown and gray trunks line the path on both sides, peppered with ferns and other undergrowth."

        scene bg school_forest2
        with locationchange

        "After a little while, I start getting worried. The path is still wide and clear, so there's no chance of getting lost, but it doesn't look like we have any particular destination."

        "There's nothing wrong with a bit of aimless wandering around, but I don't want to go so far that I get too tired to walk back."

        scene bg school_forestclearing
        with locationchange

        "I'm starting to get a little winded and my legs feel heavy. I want to stop and get a chance to catch my breath and rest my legs, but Rin keeps on going."

        hi "Where are we going? Or are we going anywhere at all?"

        show rin basic_deadpan at center
        with charaenter

        rin "Worry Tree."

        hi "I see."

        hi "So what exactly is the Worry Tree?"

        show rin negative_spaciness
        with charachange

        rin "It's just a tree. Like this."

        "She stops in front of a particularly large maple that might or might not be the Worry Tree. Its lush green leaves sway lightly in the breeze blowing through the small clearing we entered."

        hi "I guessed as much."

        show rin basic_deadpanupset
        with charachange

        rin "There are people who believe that you must come here to wallow in misery, if you are miserable, only by 'people' I mean me, and the tree isn't really called anything."

        hi "So… if you're miserable, you talk to a tree about it?"

        show rin basic_deadpan
        with charachange

        rin "No. What? You can't talk to trees. What do you think I am, crazy?"

        hi "No… I didn't mean it like that."

        show rin basic_lucid
        with charachange

        rin "Or maybe you talk to trees? I'm sorry, I didn't mean to say that you are crazy. Even though you probably are if you talk to trees."

        show rin negative_confused
        with charachange

        rin "I wouldn't recommend it in either case. People will think you are a weird person."

        hi "No, I… just forget it."

        "She looks mildly confused, for which I don't blame her at all. She tilts her head a little to the side, expression melting back to her usual one."

        show rin basic_absent
        with charachange

        rin "All right. I'm good at forgetting things."

        hi "So why are we here? Are you miserable then?"

        "I can't read the expression she makes. I hate how bad I am at interpreting Rin's mood."

        show rin negative_worried
        with charachange

        "She doesn't answer right away, as if she herself isn't quite certain of her own mood. The blank stare changes into a more difficult expression as she shuffles her weight around."

        show rin basic_deadpancontemplation
        with charachange

        "Finally, coming to a conclusion, Rin shrugs her shoulders. I've grown to seriously dislike that gesture. It doesn't mean anything."

        show rin basic_deadpanupset
        with charachange

        rin "Maybe. I just feel kind of like I'm sinking underwater. I don't know what I should do."

        show rin negative_confused
        with charachange

        rin "I don't know where I should go, that's all. Maybe it's not a big deal but I thought walking might help. Kind of like, if I go somewhere I would know where I should go. I don't really know if it did."

        show rin negative_worried
        with charachange

        rin "It really would've made sense if walking had helped to decide where to go."

        hi "So you don't want to try to get an exhibition? Or rather, you don't know if you do? Can't decide?"

        "Rin doesn't say anything for a while, arranging her thoughts in silence. The quiet is broken by birdsong from somewhere in the treetops, followed by rustling leaves as the bird takes flight."

        show rin basic_awayabsent
        with charachange

        rin "Maybe. I'm not sure if I can have a thing like that. So far I've only painted for myself."

        show rin basic_absent
        with charachange

        rin "I don't think I could have my things on display the way I am now. This me couldn't do it."

        "Her reason sounds like a weak excuse. I make my trademark frown but she doesn't notice it."

        hi "I don't get it. The teacher certainly thinks you could. I don't think he'd suggest it otherwise. Sounds like he's calling in favors from his friends, too."

        show rin relaxed_nonchalant
        with charachange

        rin "I know. He's really done a lot for me. But this might be too much."

        show rin negative_confused
        with charachange

        rin "Becoming someone who can do it might be pretty hard. Maybe I couldn't do it at all. He can't do it for me and if I let him try, I'd just sink deeper and deeper."

        "Rin stands in front of the large maple and turns away from me. I want to close the few feet of distance between us and… I don't know. My irritation is suddenly gone, and I start feeling sympathetic to her."

        hi "I know exactly how you feel."

        hi "Well, maybe I don't, but still."

        hi "I think I haven't felt like I was actually in control of my own life this whole year. I'm just helplessly going along with the flow."

        hi "Like coming here to this school. I didn't really choose it myself. And I certainly didn't choose this time of my life to learn that I have… this condition."

        "I still can't casually say the word aloud."

        hi "It's like… yeah, it's exactly like being underwater. Like I can't even breathe."

        show rin basic_sad
        with charachange

        "Rin turns to face me again, a sad expression on her face."

        rin "Is that why you look so sad all the time? I don't want to look sad like you. Do I look to you like you look to me?"

        hi "I don't look sad all the time."

        hi "I just… don't know what I should be feeling. What kind of face I should be making."

        show rin basic_upset
        with charachange

        rin "Me neither. Do I look sad now?"

        hi "Not really. You look like you always do, I think."

        show rin negative_sad
        with charachange

        rin "But I'm sinking."

        show rin negative_worried
        with charachange

        rin "I should try to float. Up, like a rubber duck. Quack quack all yellow and creepy."

        "I have to think for a few seconds about which direction I should pursue in this conversation, then I realize that it doesn't matter."

        hi "You think rubber ducks are creepy?"

        show rin basic_surprised
        with charachange

        rin "You don't? I think they look very creepy. Everything that has eyes but isn't alive is very disturbing. Like rubber ducks and reflections in mirrors."

        show rin:
            ease 0.5 ypos 1.2 alpha 0.0
        with Pause(0.5)

        hide rin

        play sound sfx_rustling

        "She plops down on the forest bed, leaning on the maple she named the Worry Tree. After wondering what to do for a minute, I sit down too, three feet apart from her."

        play sound sfx_rustling
        $ renpy.music.set_volume(0.5, 2.0, channel="ambient")

        scene bg worrytree:
            center
            acdc_warp 30.0 top
        with whiteout

        "The forest envelops us in its embrace, and its stillness falls upon the two of us."

        "We sit there without speaking for a long while. I can literally feel the time passing."

        "Patches of sunlight litter the small clearing in a pattern that echoes the maple canopies. One of them falls directly on me, warming me all the way to the bone."

        "I wonder what I could do for myself, and maybe for Rin. For now, I just keep watching her from this distance."

        "Sometimes she cranes her neck all the way back, so much that it looks almost painful, and stares up at the small patch of sky visible past the canopy of the Worry Tree."

        "Sometimes she just stares blankly ahead, as if seeing something just beyond her reach. She keeps whispering to herself but so quietly that I can't hear her, even though I'm sitting right next to her."

        "I only see her lips moving, like she was in the middle of a distant dream."

        "I realize that right now, I no longer feel any of the intense loneliness I feel at night, just before falling asleep."

        "I might be more like Rin than I thought."

        "I can either give up and stay submerged under the weight of all the crap in my life, or try to change myself for the better."

        "Her decision is different, yet the same."

        "And unlike her, I know for sure that I can't stay like this forever."

        menu:
            with menueffect
            "I have to change."

            "I want to be more like Rin.":
                $ be_like_rin = True

                call a2rc3o1
            "I want to be more like Emi.":
                $ be_like_rin = False

                call a2rc3o2

        "It makes me feel a little bit better too, and I lean back against the tree, breathing out deeply as if for the first time in a long time."

        show bg worrytree_ss:
            yalign 1.0
        with shorttimeskip

        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

        "We stay that way in the small clearing until the angle of sun changes and the chilly shadows deepen. No longer warm where we sit, we leave the forest, returning along the same path we took coming in."

        scene bg school_forest2_ss
        show rin negative_spaciness_ss at center
        with locationchange

        "It doesn't seem like Rin has come to a decision."

        hi "I wonder if it was a bad idea for me to come along."

        show rin basic_absent_ss
        with charachange

        rin "It's all right. I don't mind. I'm sure the trees and dirt and rocks won't mind either. Did you mind?"

        hi "No, not at all. I think it helped me too."

        $ renpy.music.set_volume(0.4, 1.0, channel="ambient")
        scene bg school_forest1_ni
        with locationskip

        "While we walk back towards the dormitories, the sky is changing to a deep ultramarine. The first summer stars twinkle softly from between spots in the canopy, barely visible like tiny fireflies."

        "I become very self-conscious about Rin's presence."

        nvl clear
        nvl show dissolve

        stop ambient fadeout 2.0

        n "{vspace=120}I haven't thought much about girls since things fell apart with Iwanako."

        n "This is kind of the same situation as then, but to be honest I don't think it really counts for much. Not with Rin."

        n "And yet… it feels good walking next to her, even if it isn't anything more than this."

        n "At first, I think Rin agitated me quite a bit with her unpredictable behavior. But recently, I feel I haven't had to be on my toes so much."

        n "I've managed to let myself go a little. It makes me feel satisfied, even though ultimately I think it's more thanks to Rin than myself."

        n "She seems to be disinterested in a huge number of things, but something in her makes me try harder than I normally would."

        nvl clear

        n "{vspace=90}It's not that I want to impress her; I think that truly impressing Rin would take near-superhuman effort just because of how she is. Instead, it's because there is this relentless feeling inside of me that I shouldn't let Rin down."

        n "It's really weird. I wonder why I started thinking like that. I don't even know what sort of expectations she has about pretty much anything."

        n "So how could I let her down? Rin has this unassuming air around her, and she doesn't really talk about stuff very often. Even today's confession of her self-doubt caught me a little bit off guard."

        n "I feel like I want to talk more with her."

        n "The realization suddenly dawns on me that Rin is basically the only person I talk to nowadays, apart from whatever I have to endure from Shizune, Misha or Kenji. I feel slightly depressed."

        nvl clear
        nvl hide dissolve

        scene bg school_dormext_full_ni at bgright
        with locationskip

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        play ambient sfx_cicadas fadein 1.0

        "In front of the dormitories, as if summoned by my dark thoughts, we run into Kenji himself."

        show kenji tsun_ni at center
        with charaenter

        "It feels very odd seeing him outside, breathing fresh outdoor air. At least it's already dusk; I partially expect Kenji would disintegrate upon direct exposure to the sun."

        "Kenji himself seems very insecure as well, standing around looking like he's waiting for something, but doesn't know himself what it might be."

        hi "Hey, Kenji. What're you doing?"

        show kenji at twoleft
        show bg at center
        with charamove

        show rin basic_awayabsent_ni at tworight
        with charaenter

        rin "Hello."

        stop ambient fadeout 0.2

        show kenji rage_ni
        with charachange
        with vpunch

        ke "Who're you?"

        play music music_tension

        show rin basic_absent_ni
        with charachange

        hi "It's me, Hisao. Umm… I'm not sure if you know Tezuka from class 3-4?"

        show kenji tsun_ni
        with charachange

        "From his face I can see that not only he doesn't know Rin, he also can't see her from this short distance."

        show kenji happy_ni
        show rin basic_awayabsent_ni
        with charachange

        stop music fadeout 0.5

        ke "Oh, sup dudes?"

        play music music_kenji
        play ambient sfx_cicadas fadein 6.0

        "Kenji sticks his hand enthusiastically forward, almost straight into Rin's stomach."

        show rin negative_spaciness_ni
        with charachange

        "Rin looks at his outstretched hand in confusion until Kenji clears his throat and retracts the hand."

        show kenji neutral_ni
        with charachange

        "There is something almost cool that he manages to do with social awkwardness. It's not like I'm the most suave man on the planet, but I don't think I'll ever be able to even approach Kenji's level."

        "I think I respect Kenji a little bit more."

        show rin basic_absent_ni
        with charachange

        hi "So you're waiting for someone?"

        show kenji tsun_close_ni
        with characlose

        "He leans closer and lowers his voice to an agitated whisper. I see his facial muscles twitching."

        ke "Come on man, you know I can't talk about stuff here in public. They might be listening."

        ke "I'm going to have to go pick up some stuff from somewhere, and I don't want those snooping student council hags to get on my case."

        ke "Also, I don't trust your friend. Nothing personal. Are you sure he's trustworthy?"

        "I briefly consider telling Kenji about Rin's gender, but as it might end up badly for one or both of them, I decide against it."

        hi "Yeah, I'm sure."

        show kenji neutral_ni
        show rin basic_awayabsent_ni
        with charadistant

        "He turns from me to Rin, and I immediately get the feeling that I have to prevent them from talking to each other with whatever means necessary. However, there is little I can do now, apart from physical violence."

        show kenji happy_ni
        with charachange

        ke "In that case, would you be interested in knowing about the worst threat to mankind since they invented vegetarianism?"

        "He sounds like a vacuum cleaner salesman."

        show rin basic_deadpan_ni
        with charachange

        rin "I thought it was Sunday."

        show kenji neutral_ni
        show rin basic_awayabsent_ni
        with charachange

        ke "I see you're not in the know. Yeah man, I'm talking about man-eating cows here. Very few people know what I know, so I'm not surprised."

        show kenji happy_ni
        with charachange

        ke "We can't talk here, but if you'd like a pamphlet, come to my room after curfew on Mondays or Wednesdays."

        "He suddenly reaches to his pocket and draws out a ballpoint pen and what looks like a convenience store receipt."

        "Kenji furiously scribbles on the scrap of paper and then thrusts it towards Rin."

        show kenji neutral_ni
        with charachange

        ke "Here's the password. Memorize it and then eradicate any trace of this document. Eat it, burn it, dissolve in acid, whatever."

        "I take the receipt from Kenji as Rin is unable to do so, and glance at it. It's indeed a receipt, apparently for two rice balls and five boxes of matches. I hope he is not planning to burn anything down."

        "On the other side is written just one word."

        call screen written_note(_("HONEYMUFFIN"))

        show rin basic_absent_ni
        with charachange

        "I show it to Rin too, but she shows no reaction."

        show rin basic_awayabsent_ni
        with charachange

        rin "Thank you."

        show kenji tsun_ni
        with charachange

        ke "Yo, Hisao. You still in that club? The club of dark arts?"

        show rin basic_absent_ni
        with charachange

        hi "Fine art. Anyway yeah, actually just had a meeting today."

        show rin basic_awayabsent_ni
        show kenji neutral_ni
        with charachange

        ke "Still got your wits about you? No shady mind tricks going on? Nothing personal man, but I have to be on top of things."

        show kenji tsun_ni
        with charachange

        ke "Can't get caught with my pants down. Speaking of which, you should really take showers a bit later. Gotta respect that personal space. Nothing personal."

        "Kenji looks around as if he heard something and then straightens his jacket."

        show kenji neutral_ni
        with charachange

        ke "Okay, I gotta scoot now before it gets too late. Later dudes. Good luck."

        hide kenji
        with charaexit

        show bg at bgleft
        show rin basic_deadpanupset_ni at center
        with charamovechangefaster
        stop music fadeout 4.0

        "Kenji takes off rapidly towards the main gate. Rin looks after him, frowning."

        "We watch after Kenji's diminishing figure in silence."

        show rin basic_deadpancontemplation_ni
        with charachange

        rin "What's wrong with him?"

        hi "Technically speaking, I think he's legally blind."

        show rin basic_deadpansurprised_ni
        with charachange

        rin "Oh. I see."

        stop ambient fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .iwanakos_regret:
        scene ev hisao_letter_closed
        with locationchange

        "I can immediately tell from the envelope that it's not about official matters of any sort. Someone actually wrote me an old-fashioned, hand-written paper letter."

        "Who bothers doing something like that in this day and age, anyway? Yet, as unlikely as the prospect of receiving one sounds, there is definitely a letter lying on my desk."

        scene bg school_dormhisao
        with locationchange

        "The classes for the day are over. Still feeling pretty full from the big lunch that I had unexpectedly eaten at the cafeteria, I returned to my dorm, planning on finishing my homework and probably skipping dinner, or at least just eating light."

        "I feel like I need to eat less than I used to. Maybe I don't use that much energy, now that I don't do much beyond reading."

        "However, the letter on my desk has naturally caught my interest."

        scene ev hisao_letter_closed:
            truecenter
            zoom 1.1
            acdc_warp 10.0 zoom 1.0
        with locationchange

        "It's the first piece of mail I've received here at Yamaku, so it'd feel special even if it wasn't something as rare as a handwritten letter."

        "What causes me even more trepidation is the name of the sender, written neatly on the back of the envelope."

        "Iwanako."

        "I have no idea why she would write to me. I haven't been in contact with anyone from my old school since I transferred, and Iwanako is the last person I'd expect to want to write me a letter."

        nvl clear
        nvl show dissolve

        $ renpy.music.set_volume(0.5, 0.0, channel="music")
        play music music_rain fadein 4.0

        n "{vspace=90}The last time I saw Iwanako was terribly awkward; embarrassingly so. She came to my hospital room, peeled me an apple out of courtesy and then we practically sat in silence for half an hour."

        n "She said 'goodbye' and didn't look me in the eye when she closed the door."

        n "It might've been a natural end to the series of visits that were probably pretty painful for both of us."

        n "Every time she visited me in the hospital I wanted to talk to her, but something stopped me every time. Every time that I didn't speak made the next time even harder."

        n "Iwanako always had this aura of fragility around her, as if she'd shatter into pieces at the slightest disturbance. Initially I think it might've been that delicacy that attracted me to her, but after what happened back then, it felt as if she really had shattered."

        nvl clear

        n "{vspace=150}She looked so sad that I didn't want to say anything that might upset her, and I never could figure out the right words to say."

        n "I told her that it wasn't her fault, she nodded and I really think she understood that if it hadn't been that, then sooner or later something else would've made my heart give out."

        n "Yet she looked so hopelessly sad every time she opened that door and entered my room."

        n "So I never managed to say the things I wanted to say. In the end, that might've hurt her even more."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl hide dissolve
        nvl clear

        scene ev hisao_letter_open
        with locationchange

        "Carefully, I open the envelope and draw out the folded letter from within."

        call screen written_note(_("Dear Hisao,\n\nHow are you? I hope you are well and happy at your new school. Everyone here misses you. Almost all of our second-year class got put together in class 3-1 for the final year, so we are pretty comfortable right from the beginning of the year. I'm sure you would've been assigned to this class as well."))

        call screen written_note(_("The mood among the third-years seems to be very anxious about the final exams, even though they are so far away. The teachers are badgering us about it all the time - even old Mr. Tachibana who is, by the way, our homeroom teacher this year. Would you believe it? I was sure that he'd retire after our second year, but here he is, nagging everyone about studying for exams.\n"))

        call screen written_note(_("I think things like that are the main reason why the mood among the third-years is so nervous. I must admit that I'm somehow losing confidence in myself as well, even though I've always fared reasonably well in exams.{vspace=150}"))

        call screen written_note(_("It's so weird to think we are already seniors, isn't it? Time has really flown past. I wonder where it went. The new first-years seem so young and somehow really innocent. I keep wondering if I was like them in my first year. I've been feeling nostalgic like this for the whole first trimester.{vspace=90}"))

        show ev hisao_letter_open_2
        with locationchange

        call screen written_note(_("There are other things I want to say. I'm writing to you because I felt that there are things I should've said after the incident back in winter. I really regret that I wasn't able to say them in person, and I have no excuse for it.{vspace=150}"))

        call screen written_note(_("The truth is, the times when I visited you at the hospital made me worried about you. I am not talking about your health. You seemed to become more distant and disheartened. It was natural after something like that happened, I'm sure, but somehow I got the feeling that you had given up on something back then. Happiness, maybe?{vspace=30}"))

        call screen written_note((_"I wanted to somehow express my feelings, but the right words didn't come to me. I couldn't say anything to comfort you. I am really sorry for not being able to support you when it mattered the most, even though I like you so much. At least now, finally, I can be more honest.{vspace=120}"))

        call screen written_note(_("If I could go back to those quiet days in February and March, I'd tell you to not give up on yourself. That's what I would say. Maybe you wouldn't have drifted so far away if I had just said something. I hope you've managed to get back on your feet on your own.{vspace=120}"))

        call screen written_note(_("Now that the distance between us is also physical, it also feels more final, somehow. I wonder if we will meet again. Perhaps it's for the best if we don't? Still, if you would like to correspond with me, by all means write me back. I'd very much like to hear about your new school and how you are doing. I wish you all the best.\n\nSincerely, Iwanako"))

        "After finishing reading the letter I fold it like it was, and place it on my desk."

        "I don't know what to think of this. I feel empty and confused."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=60}Why now, after all this time?"

        n "Just yesterday I decided that I can't let myself stay like this, that I'd try to get on top of my own life. Reading this letter just reminds me of what could have been."

        n "Of course I wish that I didn't have to be here. I'd want to be in the same class with Iwanako again. Maybe we would talk every day now and go on dates."

        n "{vspace=30}My life didn't go like that."

        n "I didn't really need to be reminded of this. Iwanako needed to write this letter for her own sake and I'm glad for her that she could, but it would've been better if I hadn't read it."

        n "{vspace=30}Of course, she is right. I thought of the same thing yesterday. I had fallen into a pit of depression and now have to try to climb out."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl hide dissolve
        nvl clear

        scene bg school_dormhisao
        with locationchange

        "I rip out a page from my notebook, and after a moment of thinking how to frame my words, write a short reply to Iwanako."

        "I find it difficult to be really honest to her, but at least I try to appear somewhat convincing. I don't write her about Yamaku at all."

        "I doubt she will write me again, but I don't feel at all sad about it. I fold my own letter to her and as I have no envelope, set it next to Iwanako's. I'll mail it to her later."

        "Then I lie back on my bed, looking at the monotone gray ceiling."

        "A bird sings outside of my window and a sudden gust of wind flutters my curtains. The summer afternoon feels still, as if time had stopped for a brief moment."

        "I think about all the things I've lost and will never regain."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .in_her_own_image:
        play music music_night

        scene bg misc_sky:
            xalign 0.0
            warp acdc_warp 60.0 xalign 1.0
        with locationchange

        nvl clear
        nvl show dissolve

        n "Thus the languid days of mid-June pass by."

        n "I mail my letter to Iwanako, and receive no reply."

        n "Having decided to ditch the old me, I start observing my fellow students even closer than I did before, hoping to understand how other people cope with their own issues."

        n "I start seeing things I didn't before, and it makes me wonder if I've been wrong twice."

        n "Superficially, everyone is abnormal yet so strikingly normal that it shocked me at first. I admired the way my new school mates turned my prejudices around just like that, simply by being themselves."

        n "Now that I've gotten used to it, I begin noticing other kinds of tones in the people surrounding me every day."

        n "{vspace=30}There is this soft, numb sadness all around me."

        n "I can see the effort everyone has to make just to get through the day, and how it weighs on their shoulders, like it weighs on mine."

        n "Even the brightest smile is just slightly subdued, every outburst of annoyance just slightly dampened. It's subtle, but it's definitely there."

        nvl clear

        n "I try to think what it means, what I can learn from others. I wonder if deep down, everyone is as lost as I am. Is there even one person in here who has truly found peace? I start to feel doubtful about myself once again."

        n "I can't decide whether these people are happy, unhappy, or if they've just learned to cope and now live in an unfeeling limbo like I did all spring."

        n "I escape from these feelings into the towering piles of books I carry to my room from Yuuko's sanctuary. After realizing that this will just shut me down even more, I start going to the art club's room more often, usually whenever I can."

        n "{vspace=30}Rin too seems to spend more time in there than in her own classroom."

        n "I've often seen her totter towards the door at the very end of our corridor. That wooden door and the room behind it, smelling of paint and paper, seem to mean more to her than the rest of the world combined."

        n "She says she has special permission to use the room, which I don't doubt at all. I don't think Nomiya would deny Rin anything."

        n "He seems to dote on her like an uncle upon a favorite niece."

        nvl clear

        n "{vspace=90}The object of his affection, however, has no favorites. She says she appreciates the teacher a lot for going the extra mile for her sake, but even when she says that, her expression is the same as always."

        n "It's as if she was talking about a particularly unremarkable rock that she saw the other day. I can't really figure out their relationship."

        n "Rin doesn't seem to let anyone close. I don't think even Emi could say she's crossed the gap that seems to separate Rin from the rest of the world."

        n "{vspace=60}I don't understand it. She seems so indifferent, yet so passionate at the same time."

        play sound sfx_normalbell

        n "Somewhere, the school bells ring the last call of the day."

        stop music fadeout 5.0

        nvl hide dissolve
        nvl clear

        scene bg school_classroomart
        with locationchange

        "I realize I've been zoning out for who knows how long. Dazed, I sit up straighter, trying to look as inconspicuous as possible."

        "The pungent smells of linseed oil and turpentine mix in my nostrils as I draw a deep breath. I feel drowsy and lightheaded."

        "It's already this late and a few club members left early, so it's just me, Rin, the teacher, and two other girls who are also about to leave."

        play music music_soothing fadein 4.0

        scene ev rin_painting_base
        with locationchange

        "Rin is sitting to my right, slowly working on a painting while I'm idling the time away. I don't think she realizes I've been watching her this whole time."

        scene ev rin_painting_foot:
            top
            ease 7.0 center
        with locationchange

        "With a nimble move of her delicate ankle, she dips the brush into crimson paint and presses it lightly onto the canvas. A stain spreads around, as if the brush was bleeding."

        "Her progress has slowed down to a crawl. By now I've learned that this is dangerous for her technique, as the paint must not be allowed to dry before she's finished."

        "It occurs to me that I am literally watching paint dry. And yet somehow I'm not feeling bored, despite spacing out just now."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        scene ev rin_painting_base
        with locationchange

        nvl clear
        nvl show dissolve

        n "{vspace=60}Most of the time, the art club is very relaxed and free-form. Apart from times when Nomiya gets really excited about some technique or style he wants to teach us about, everyone is free to pursue their own interests."

        n "Lacking one, I keep floating around without a direction. I try this and that, but nothing really leaves me with a deeper impression, not to mention that I don't seem to have a special knack for anything."

        n "Well, I did get praised for my attempt at watercolors, and I felt pretty good about that, myself, but that's it."

        n "I suppose it's to be expected. I joined the art club mostly on a whim, after all."

        n "I'm thinking that maybe I should quit the club, if it's going to be this pointless. But there's nothing really wrong with pointlessness and I can't exactly say I'm unhappy."

        n "{vspace=30}Unsatisfied maybe, but I've got only myself to blame for that."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl hide dissolve
        nvl clear

        scene bg school_classroomart
        with locationchange

        "As the pair of girls exit the club room with a cheerful 'bye-bye', Nomiya stands up from his desk. His chair scoots back with a loud screech that breaks the harmony of this quiet afternoon."

        "He taps a pile of papers in his hands twice against the tabletop in order to straighten them, then stretches his back."

        show nomiya smile at center
        with charaenter

        no "I have a faculty meeting to attend, so I can't stay. I'll have to do some paperwork later, so if you want to stay we can talk then. Sorry about this."

        "There are two people here, but he's really talking to only one of us. Nomiya spends extra hours of his time mentoring Rin after official club hours are over, and I'll bet he'd like to discuss his plan of getting Rin's art into a gallery a little more."

        scene ev rin_painting_base
        with locationchange

        rin "It's all right. I think I'll probably be here, but it's not a big deal if I'm not. I don't really have much going now."

        "Rin answers without moving her eyes from her work in progress. The tone of her voice is neither the polite kind expected when talking to a teacher, nor her usual monotone."

        no "So I won't need to send a search party if you aren't here?"

        rin "Yes, no thanks, I don't like to party. We can talk later."

        scene bg school_classroomart
        show nomiya veryhappy
        with locationchange

        no "Good girl."

        hide nomiya
        with charaexit

        stop music fadeout 6.0

        "Smiling, the teacher picks up the rest of his papers and makes his way to the door. I glance at the clock above it and then at my watch to double check."

        "They're three minutes apart, but nevertheless the club's meeting time is over now."

        "Rin seems intent on staying here to work on her piece while waiting for the teacher."

        "I can't quite imagine what their one-on-one time would be like."

        "Would they actually discuss anything? Rin is always so subdued in what she says, and when she does say something it's difficult to understand what she's talking about."

        "Maybe Nomiya just talks endlessly like he does at club meetings, letting Rin absorb what she will from his infinite well of art knowledge, like a sunflower turning to face the glowing sun."

        scene ev rin_painting_base
        with locationchange

        hi "Do you mind if I stay? I er… thought maybe I'd give watercolors another try."

        "I blurt out the excuse sort of accidentally, embarrassing myself. Rin doesn't take her eyes off her painting."

        rin "Okay."

        scene bg school_classroomart
        with locationchange

        "I shift around in my chair, then get to fetching a cup of water, brushes, colors and some paper. The sound of my footsteps invades the still afternoon air."

        "Before starting, I try to recall what the teacher told us, an important philosophy of the medium: working with watercolors means more working with water than working with color. I try to keep that in mind, and dip my tiny sable brush into the water cup."

        "I'm mixing yellow and blue, trying to capture the sunlit treetops outside of the window. The sun is low, so the yellows are more pronounced and everything looks darker."

        "I still can't quite connect what I see with what my hand does with the paints, but it's a passable attempt for my level."

        "After a while I start losing my focus and move the paper aside, deciding to watch Rin work for a while, instead."

        "That little while stretches first into a long while, then into a really long while."

        play music music_dreamy fadein 1.0

        scene ev rin_painting_base
        with locationchange

        "Rin paints, her entire being fully concentrated on the brush between her slender toes and the painting coming to life one stroke at a time."

        "She seems determined and yet at the same time relaxed, effortlessly moving the brush around, never hesitating. Colors meet and part, mix and cover each other on the canvas, bending to her quiet will."

        "I don't know anything about composition, structure or any of that stuff, but I really like Rin's paintings. I like how she looks when she paints."

        "As usual, the silence between us compels me to speak rather than merely wait for her to open up. She might end up saying nothing at all."

        hi "Do you mind if we talk?"

        scene ev rin_painting_reply
        with locationchange

        rin "I don't mind."

        hi "I kinda wanted to ask more about why you get so weird about this thing the teacher wants to arrange for you."

        "Rin picks up a tube of paint and squeezes it between her toes on a palette almost as easily as someone with opposable thumbs would. Taking up a brush again, she replies."

        scene ev rin_painting_concerned
        with locationchange

        rin "A lot of things. And some not-things. Unthings. I don't think that's a word."

        hi "Do you want to talk about it?"

        "I try to reach out to her clumsily, ignoring the embarrassing feeling of awkwardness. Rin keeps her focus on the painting, spreading more and more paint on the canvas, her lips forming a perfectly straight line as she concentrates on the job."

        scene ev rin_painting_base
        with locationchange

        rin "Not really."

        scene ev rin_painting_reply
        with locationchange

        rin "Talking is hard. I mean, it's not hard, I'm talking even now. But saying the right things is really hard for me."

        scene ev rin_painting_concerned
        with locationchange

        rin "No matter what, I just can't say the things I want."

        hi "That sounds weird."

        scene ev rin_painting_base
        with locationchange

        rin "It's true. I say all kinds of things that I don't really mean all the time. And sometimes I forget words and then I use the wrong words. I even come up with new words for things that already have some. That's the worst thing."

        rin "I get really nervous and everything comes out a mess and even I don't really understand what I want to say."

        scene ev rin_painting_concerned
        with locationchange

        rin "I think there's something wrong with me that makes it like this. Remember when I said I can only think of four things at the same time?"

        "I nod wordlessly."

        scene ev rin_painting_reply
        with locationchange

        rin "It's not really four. I mean, it is four, but everything else is also there kind of in the background. Like being at an amusement park and a beehive at the same time. But that's not the point."

        rin "I used to do better. Like six or seven things. I think so, at least. I feel like I'm becoming dumber."

        hi "I think everyone has times when they feel like they can't say the right things."

        scene ev rin_painting_base
        with locationchange

        rin "But it's there all the time. Stronger and deeper. Yeah, deeper is a good word. I like that word. Deeper."

        rin "It's that feeling of being underwater. Maybe it's just art."

        scene ev rin_painting_reply
        with locationchange

        rin "The more I paint, the more words I forget. Maybe at some point I will forget how to speak completely."

        rin "It feels like I'm slowly forgetting everything. Do you remember what you thought about things three or four years ago?"

        rin "I don't."

        "A long pause ensues, during which time seems to bend around itself, almost tying itself into a knot. I don't think I've ever heard Rin talk this earnestly and for so long about anything before."

        scene ev rin_painting_concerned
        with locationchange

        rin "It's like I'm fading away from the world."

        scene ev rin_painting_faceconcerned:
            truecenter
            easein 10.0 zoom 1.05
        with locationchange

        "Rin's foot has stopped its work on the canvas and she is staring at her painting, unmoving, as if gazing at some faraway horizon."

        "Sunlight briefly glints in the corner of her onyx eyes. Something floats up into the top layer of Rin's being and she lets out a long breath."

        scene bg school_classroomart
        show rin basic_lucid_close:
            tworight
            ypos 1.1
            0.2
            "rin basic_awayabsent_close" with Dissolve(0.3)
        with locationchange

        stop music fadeout 0.3

        "Then she blinks and it's gone."

        show rin basic_absent_close
        with charachange

        rin "Paintings stay behind. When I look at my old things, I remember what I was thinking back when I made them."

        show rin basic_lucid_close
        with charachange

        rin "They make me feel like I can be with all the past mes when I was a different me."

        show rin basic_awayabsent_close
        with charachange

        rin "I guess they are the proof of my existence."

        "She uses the exact same words Nomiya used when he spoke to us of the nature of art. I didn't think Rin was paying any attention, back then. I wonder if she was listening, or whether she had heard the same passionate speech from Nomiya before."

        "Either way, I feel overwhelmed."

        hi "Boy, are you complicated. I would've taken up writing a diary."

        show rin basic_absent_close
        with charachangealways

        show rin basic_awayabsent_close
        with charachangealways

        "Her eyes quickly flicker to my direction and then back to the painting, but she doesn't pick up the brush any more."

        play music music_rin fadein 0.5

        rin "That's a great idea. Why didn't I ever think of that?"

        hi "Are you being sarcastic?"

        show rin basic_deadpan_close
        with charachange

        rin "What's sarcasm?"

        "I don't call her on the joke, if it is one."

        show rin basic_awayabsent_close
        with charachange

        "Right at that moment, Nomiya returns from his meeting. He waves to us a very melodramatic hello, mildly surprised to see me here along with his pet student. Walking with a boisterous gait to his desk, he drops his papers upon it."

        "He picks up a handkerchief and cleans his glasses with incredibly meticulous care before walking over to us."

        "Before he is within earshot of us, Rin says something to me in a quick, quiet voice."

        stop music fadeout 0.5

        show rin basic_absent_close
        with charachange

        rin "Change is the scariest thing in the world to me."

        show rin basic_upset_close
        with charachange

        rin "And I seriously don't know if I want to change into a person who could do the thing the teacher wants me to do. I don't know if I could even if I wanted to."

        show nomiya talk behind rin at twoleft
        with charaenter

        no "Hello again!"

        call screen doublespeak(hi, _("Hello."), rin, _("Hello."))

        show nomiya smile
        with charachange

        play music music_pearly fadein 5.0

        no "What's going on?"

        "He smiles a bit sheepishly, looking at both of us with uninhibited interest."

        hi "Ah, nothing. We were just talking about that thing with your acquaintance and the gallery. For Rin's works. Sort of."

        show nomiya veryhappy
        with charachange

        no "Oho? Any decisions?"

        "I look at Rin, who is trying to arrange the bothered expression on her face into something else."

        menu:
            with menueffect
            hi "Anyway, I don't think I have much else to say, other than that you should go for it."

            "I think you'd be a big hit." if rin_amazing or _in_replay:
                $ believes_in_rin = True

                call a2rc4o1

            "You'd be wasting your talents otherwise." if not rin_amazing and not _in_replay:
                call a2rc4o2

            "You won't get a chance like this again." if not its_refreshing and not _in_replay:
                $ believes_in_half = True

                call a2rc4o3

            "Because it would be exciting." if its_refreshing or _in_replay:
                call a2rc4o4

            "It isn't like you at all to hesitate like this." if be_like_rin or _in_replay:
                $ believes_in_half = True

                call a2rc4o5

            "You should aim high." if not be_like_rin and not _in_replay:
                $ believes_in_rin = True

                call a2rc4o6

        if believes_in_rin:
            show rin basic_deadpanupset_close
            show nomiya smile
            with charachange

            "Rin looks absentmindedly at me, not saying anything. I can't even tell if my words had any effect on her."

            hi "I just don't get it. Anyone else would be jumping up and down in excitement."

            hi "What's the point of doing your best, being at this art club, if you don't do anything with your talent?"

            hi "I'm telling you, I'm going to be angry with you if you give this up."

            "My voice rises higher. I don't know what makes me say this. It's like I've been taken over by some force out of my control, but I really do feel angry."

            "Images of a letter written on cute stationery flash in my mind, images of the masked faces of my parents, my doctors, images of the time I've wasted. They mix into my feelings about Rin like a torrent of molten iron."

            show rin at tworight
            with charamove

            "I want to continue, but Rin suddenly stands up."

            rin "Fine."

            rin "I'm going."

            hide rin
            with charaexit

            "She trots out of the room without anyone saying anything. I stare after her, still seething, though with the voice of rationality in the back of my head wondering if I made her angry as well."

            show nomiya veryhappy at center
            show bg at bgright
            with charamovechangefaster

            "The teacher lets out an embarrassed, but extraordinarily loud laugh."

            show nomiya frown
            with charachange

            no "You care a lot for her, don't you?"
        elif believes_in_half:
            show rin basic_deadpanupset_close
            show nomiya smile
            with charachange

            rin "I don't think I want to talk about this."

            rin "I'm going."

            show rin at tworight
            with charamove

            hide rin
            with charaexit

            "Rin stands up and trots out of the room without anyone saying anything more."

            show nomiya at center
            show bg at bgright
            with charamove

            hi "I'm sorry. I think I made her upset."

            show nomiya veryhappy
            with charachange

            no "Hahaha, don't worry about it. She'll be fine, I'm sure. I'll talk to her later."
        else:
            show nomiya smile
            with charachange

            no "Now now, my boy. It's a big decision and even though I'd like Tezuka to be more decisive as well, she needs time to mull it over."

            show nomiya frown
            with charachange

            no "Why don't we let her decide. You have good intentions, but in the end it comes down to her own feelings."

            show nomiya veryhappy
            with charachange

            no "Any thoughts on the subject, Tezuka? You've been quiet all afternoon."

            "We both look at Rin, who doesn't return either of our gazes."

            show rin basic_lucid_close
            with charachange

            rin "No. I think I'm going."

            show nomiya talk
            with charachange

            no "You are? What a shame. Promise me you'll give me some kind of an answer in a week or so, all right?"

            show rin basic_deadpanupset_close
            with charachange

            rin "All right."

            show nomiya smile
            with charachange

            no "Good girl."

            show rin at tworight
            with charamove

            hide rin
            with charaexit

            "Rin stands up and trots out of the room without anyone saying anything further."

            show nomiya at center
            show bg at bgright
            with charamove

        "Nomiya looks at me over his circular pink glasses, smiling sympathetically."

        show nomiya talk
        with charachange

        no "You've made friends with her then, Nakai?"

        hi "Uh… well, something like that, I guess. Depends on how you look at it. To be honest, I'm not really sure."

        "It's more like me and Rin just tend to hang around each other irregularly, talking or not about something that more often resembles some twisted mockery of philosophy rather than normal, everyday things that 'friends' chat about."

        show nomiya frown
        with charachange

        no "Well, that's all good, isn't it? You're a new student and we should be promoting integration into the student body and such. I can't remember all the buzzwords they spew at faculty and Yamaku Foundation meetings, but that's how it is."

        show nomiya veryhappy
        with charachange

        no "Tezuka isn't the most social person around these parts, either."

        hi "Yeah, that's definitely true."

        show nomiya smile
        with charachange

        no "So she's talked about my suggestion to you?"

        hi "Oh, no, not really. I think it's been more me pressing her to decide something. Maybe I shouldn't have."

        show nomiya talk
        with charachange

        no "No, I'm sure it's fine. I'm too soft with her, even when I shouldn't. I don't really know how to handle Tezuka, she's so independent and willful."

        show nomiya talktongue
        with charachange

        no "I wonder if this is what every old geezer of an art teacher who got his hands on a young and fiery prodigy felt like."

        show nomiya smile
        with charachange

        "He chuckles ironically to himself a little bit, turning to face Rin's latest work which she left drying on the easel. She departed so abruptly that I wonder if she considers it finally finished."

        show nomiya talk
        with charachange

        no "So, let's see the painting then."

        "He leans in closer, peering at the canvas."

        show nomiya frown_close
        with characlose

        no "It draws you in, doesn't it?"

        show nomiya dreamy
        with charadistant

        "Nomiya stands back straight, his face a dreamy, nostalgic visage. I don't answer him, as he seems to be taking my agreement as a given."

        show nomiya talk
        with charachange

        no "I sometimes stay here after hours just to look at Tezuka's paintings. She's really just prodigious, and at such a young age. I get shivers just thinking of what she could become with a few more years of refinement."

        show nomiya frown
        with charachange

        no "You asked what makes an artist, remember? This is it. They take a piece of the world and reshape it in their own image. Metaphorically, of course."

        show nomiya dreamy
        with charachange

        no "Looking at her makes you wonder what the world looks like through her eyes. It's a wonderful thing, to be young and full of passion, the most extraordinary time of your life. You would do well to remember that, Nakai."

        hi "Yes, sir."

        show nomiya veryhappy
        with charachange

        no "It's so silly."

        show nomiya frown
        with charachange

        no "People always ask artists 'Where do you get your ideas?' as if ideas were something sold at the market for pocket change."

        show nomiya serious
        with charachange

        no "You can't explain inspiration. For people like Tezuka, it's like breathing. It's an instinct."

        no "I've met maybe one or two with the same kind of raw potential. But no amount of potential will amount to anything if one doesn't work to realize it."

        no "It's practice, technique, skill. Draw for an hour every day for a few years and even the most hopeless case becomes a passable artist."

        show nomiya talk
        with charachange

        no "Tezuka is not brilliant because she was born with a natural talent for this kind of thing. She's brilliant because she works harder than anyone, ever since she learned to hold a pen, most likely."

        show nomiya veryhappy
        with charachange

        no "And all of it with her feet, no less. Absolutely phenomenal."

        "Silence finally lands in the clubroom as Nomiya lets himself get drawn back into Rin's painting, gently murmuring acceptance toward the still-wet canvas."

        hi "What kind of things do you paint yourself?"

        show nomiya smile
        with charachange

        "As if waking from a reverie, he looks at me, surprised at my talking to him."

        show nomiya talk
        with charachange

        no "Oh, I don't. Not any more."

        show nomiya smile
        with charachange

        no "I became an art teacher only after my career in that field came to an end. Now I just pass on knowledge to the next generation."

        "The way Nomiya answers is curious, both giving and withholding information. I feel like asking more, but he cuts in before I get the chance."

        show nomiya veryhappy
        with charachange

        no "Now you should run along, my boy. It's almost dinner time, isn't it?"

        hi "Yes, sir. Have a good evening."

        show nomiya smile
        with charachange

        no "You too."

        scene bg school_hallway3
        with locationchange

        stop music fadeout 2.0

        "I quickly collect my stuff and step out into the deserted hallway, leaving the teacher alone with his musings."

        "The weekend will be here soon. It's amazing how fast time flies here."

        "I promised Emi I'd join her for the celebration of her triumph at the track meet last week. That should be plenty of fun."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .umbrella_logic_cake:
        $ renpy.music.set_volume(0.5, 0.0, channel="music")
        play music music_daily fadein 3.0

        scene bg school_courtyard_rn
        with locationchange

        hi "Are you sure you want to go?"

        "The weather that has been wonderful for all of June has finally taken a turn for the worse. The leaden clouds drooping over the town look worrisome and the air feels heavy and still, just like before rain."

        "The forecast says there's a 60%% chance of rain this afternoon. Maybe this will mark the beginning of the rainy season."

        show emi basic_grin_rn at center
        with charaenter

        emi "Of course I'm sure! I've been waiting for this all week!"

        "Emi had planned a picnic at some nearby park, with snacks aplenty bought from the convenience store, but with the weather this gloomy, it seems risky."

        show emi basic_annoyed_rn
        with charachange

        emi "I asked some other people to come too, but they didn't want to go because of the weather. We have to prove them wrong!"

        hi "Wrong how?"

        show emi excited_smile_rn
        with charachange

        emi "You know, like how it always rains when you think it won't, and when you think it will, it doesn't? We'll go no matter what, so it's a win-win situation!"

        show emi basic_closedhappy_rn
        with charachange

        emi "I've been going without sweets for weeks because of practice for the track meet. But now I can splurge on anything I want. Nothing is going to stop me now!"

        hi "I thought you were all about a healthy lifestyle and stuff."

        show emi excited_proud_rn
        with charachange

        emi "Ohoho, Hisao, you understand so little. There's not a single girl on this planet who doesn't love sweets!"

        show emi at twoleft
        show bg at bgleft
        with charamove

        show rin basic_deadpan_rn at tworight
        with charaenter

        rin "I don't like sweets."

        show emi excited_joy_rn
        show rin basic_awayabsent_rn
        with charachange

        emi "She doesn't count. Anyway, is this clear?"

        show rin basic_absent_rn
        with charachange

        hi "Completely. We will go and eat our fill of sweets."

        show emi basic_closedgrin_rn
        show rin basic_awayabsent_rn
        with charachange

        emi "Damn straight we will."

        show emi excited_laugh_rn
        with charachange

        emi "I'm going to have to work it off later but it's so worth it."

        "Emi seems to be extremely determined about this. She is positively exhilarated, brimming with energy as always, but something seems special today."

        "It looks like she can hardly stop herself from jumping up and down on the spot."

        show emi excited_joy_rn
        with charachange

        emi "Come on!"

        hide emi
        hide rin
        with charaexit

        "I grasp the wooden handle of the umbrella I brought and start to follow the two girls, who seem to have no qualms about leaving me behind if I keep daydreaming."

        "My umbrella is really fancy, the old-fashioned kind with a curved handle and a metal spike at the end. It used to belong to my grandfather. It looks like an antique, but it's in really good shape; almost as good as new."

        "It's really big, too. I remember how my grandfather, my grandmother, and I all fit neatly under it when a rainstorm caught us on an afternoon walk years ago, when I was around nine or ten."

        "My grandparents are both gone now, but I still have the umbrella to keep me dry when it rains."

        scene bg school_road_rn
        with locationskip

        "We walk along the road leading down from the school towards the convenience store, the clouds casting their dark shadow down on us. The weather seems to be taking a turn for the worse and I am pretty sure I just felt a raindrop on my head."

        hi "Didn't you guys think of taking umbrellas? It really looks like it'll rain."

        show rin basic_deadpancontemplation_rn at tworight
        show emi basic_grin_rn at twoleft
        with charaenter

        "Rin looks at her limply hanging sleeves and shrugs her shoulders."

        show emi basic_closedgrin_rn
        show rin basic_awayabsent_rn
        with charachange

        emi "I don't have one. Besides, a little rain won't kill us."

        "She pushes her chest out, looking very confident about that."

        show emi basic_happy_rn
        with charachange

        emi "We aren't made of sugar!"

        show rin basic_absent_rn
        with charachange

        hi "I thought that's exactly what girls were made of, especially considering what you're planning to gorge yourself on today."

        show emi sad_annoyed_rn
        with charachange

        "She just sticks out her tongue in reply."

        hide emi
        hide rin
        with charaexit

        "The walk down from the school to the local shopping district is not a long one, but it's not very short, either. It's all downhill so our steps roll easily, but time stretches out nevertheless."

        "The distance is right there, in that gray area where you don't expect the trip to be quickly over with, but you aren't preparing for a long walk, either."

        "Thus, the trip is slightly too long to stay comfortably quiet the whole time, though the girls don't seem to mind."

        "Rin walks calmly ahead, seemingly lost in thought. I'm kind of wary about starting a conversation, since the last time didn't end very well for either of us."

        "I haven't exchanged a single word with her since then."

        "Emi, on the other hand, is way too happy about just walking."

        "She seems to literally jump a little on every step, or skip over cracks, or balance on the edge of the sidewalk. Every now and then she comments on something to which Rin replies in an automatic-sounding, nonsensical way that makes Emi giggle a little."

        $ renpy.music.set_volume(0.1, 0.0, channel="ambient")
        play ambient sfx_rain fadein 5.0

        scene bg suburb_roadcenter_rn
        with locationchange

        "As we reach the bottom of the hill, the first raindrops begin to fall. I feel one hit the top of my head, then two more hit my nose in quick succession."

        play sound sfx_thunder
        stop music

        $ renpy.music.set_volume(0.2, 0.5, channel="ambient")
        $ renpy.music.set_volume(1.0, 4.0, channel="music")
        show rain light
        with dissolve

        "It's not one or two rainclouds any more. The entire sky has turned shadowy gray, billowing rainclouds swirling right on top of us."

        show emi sad_pout_rn behind rain at center
        with charaenter

        emi "Oh, shoot. I guess we aren't going to have a picnic then."

        hi "What now?"

        show emi at twoleft
        show bg at bgleft
        with charamove

        show rin negative_spaciness_rn behind rain at tworight
        with charaenter

        rin "Maybe we could have a rain picnic. A picnic in rain."

        show emi basic_annoyed_rn
        with charachange

        emi "No, we'd all just catch a cold and I don't like getting me or my snacks wet."

        show rin relaxed_nonchalant_rn
        with charachange

        rin "I kind of like it. Not the snacks part though."

        $ renpy.music.set_volume(0.5, 4.0, channel="ambient")

        show emi basic_concentrate_rn
        show rain medium
        with charachange
        play sound sfx_rustling

        "Emi considers our problematic situation for a moment while I open my umbrella and lift it up, trying to hold it so that all three of us get covered."

        show emi basic_happy_rn
        with charachange

        emi "Hey Hisao, have you been to the Shanghai yet?"

        show rin basic_absent_rn
        with charachange

        if wait_for_shizu or _in_replay:
            hi "Yeah, our class president took me there on my first week."
        else:
            hi "It's a café somewhere around here, right? I've heard of it."

        show rin basic_awayabsent_rn
        show emi basic_grin_rn
        with charachange

        emi "It's a nice place. Let's go there and wait out the rain. If it's just a really quick shower, we can still go for the picnic, and if it gets worse, we'll just order cake there instead."

        show rin basic_absent_rn
        with charachange

        hide emi
        with charaexit

        hide rin
        with charaexit

        "Neither Rin nor I have better ideas, so with Emi taking the lead, we start walking briskly along a side street."

        $ renpy.music.set_volume(1.0, 6.0, channel="ambient")

        scene bg suburb_shanghaiext_rn
        show rain normal
        with locationchange

        "The café is only a few blocks away, but even with the umbrella, we can't avoid getting slightly damp. The rain keeps coming down harder and harder."

        "Raindrops leave tiny dots on the black asphalt road, which then combine into bigger patches like pointillist artwork being made in front of our eyes in mere seconds."

        "It's pouring heavily, drumming on the hoods of the cars parked on the sides of the street and already flowing in little creeks along the sidewalks."

        "The yellow light shining through the rainwater streaming down the windows looks very warm and inviting."

        play sound sfx_storebell
        stop ambient fadeout 0.5
        play music music_jazz fadein 2.0

        scene bg suburb_shanghaiint at left
        with locationchange

        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
        play ambient sfx_crowd_indoors fadein 2.0

        "I shake the excess water off the umbrella and head inside with them, following Emi to a vacant table in the furthest corner of the small café."

        $ renpy.music.set_volume(0.7, 2.0, channel="ambient")

        "The place is almost full; apparently other people had the same idea as Emi, and now we are all stranded together here in this cozy little place."

        show bg:
            warp acdc_warp 5.0 right

        "Varnished wooden pillars and paper screens mix with Parisian-style tables and chairs in discordant harmony, a contrast of old and new."

        "Light jazz plays quietly in the background, though it's mostly drowned out by the murmur of the customers."

        if wait_for_shizu or _in_replay:
            "I notice Yuuko is at work here today, but it seems like she's serving a full house all by herself, frantically gliding from one table to another and trying to keep up with everything."

            "I watch her deliver a tray of tea cups and pastries to another table taken by Yamaku students, then take an order from a middle-aged couple sitting across from us before finally turning to serve us."

            hi "Hi, Yuuko."

            show yuukoshang neurotic_up:
                center
                xpos 0.6
                easein 0.5 center
            with charaenter

            show yuukoshang at center

            yu "Umm… ah, welcome to the Shanghai. "

            hi "Looks like you're busy."

            show yuukoshang neurotic_down
            with charachange

            yu "Ahaha, I'm completely over my head here. I wish I had another pair of hands."

            show yuukoshang neutral_down
            with charachange

            yu "What can I get for you today?"
        else:
            "There's only one waitress serving the full house, frantically gliding from one table to another and trying to keep up with everything. To my surprise, I think I recognize her."

            "I watch her deliver a tray of tea cups and pastries to another table taken by Yamaku students, then take an order from a middle-aged couple sitting across from us before finally turning to serve us."

            hi "Yuuko?"

            show yuukoshang neurotic_up:
                center
                xpos 0.6
                easein 0.5 center
            with charaenter

            show yuukoshang at center

            "Now that she's close and facing me I see that it really is her, the part-time librarian of Yamaku in full waitress attire. It's a pretty cute outfit, and she has tied her hair up in buns to match."

            show yuukoshang worried_up
            with charachange

            "It's a completely different image from her mousy, plain style at her other job. Yuuko blinks a few times looking confused, then remembers that she was about to say something."

            show yuukoshang panic_down
            with charachange

            yu "Umm… ah, welcome to the Shanghai."

            hi "So you work here too? I thought you were a university student or something."

            show yuukoshang neurotic_down
            with charachange

            yu "Ehh, yes, that too. It's a part-time job as you can see, ehehe. It's Sunday, so there aren't any lectures."

            show yuukoshang neutral_down
            with charachange

            yu "Good thing, too, since today has been so busy I'm wishing for another pair of hands. Anyway, I'm in a bit of a rush as you can see. What can I get you today?"

        show emi excited_joy:
            left
            xpos -0.1
            easein 0.5 left
        show rin basic_awayabsent:
            right
            xpos 1.05
            easein 0.5 xpos 0.95
        with charaenter

        show emi at left
        show rin:
            right
            xpos 0.95

        stop music fadeout 1.0
        $ renpy.music.set_volume(0.4, 2.0, channel="ambient")

        "Emi doesn't hesitate even for a second. Her eyes glitter like those of a kid in a candy store."

        play music music_comedy fadein 1.0
        show emi excited_amused
        with charachange

        emi "Tea for everyone! And cake for me!"

        show yuukoshang smile_up
        with charachange

        "Yuuko tries to stay as formal and professional-looking as possible, smiling cheerily at my ravenous companion."

        show yuukoshang smile_down
        with charachange

        yu "Ahh… yes, today we have a choice of strawberry shortcake, raspberry layer cake, or lemon meringue pie."

        show emi basic_happy
        with charachange

        emi "Strawberry… no, lemon! No, actually I'll take both!"

        "She looks at me in challenge."

        hi "Err… I'll take just the pie."

        show rin basic_deadpan
        with charachange

        rin "Nothing."

        show emi basic_annoyed
        with charachange

        "Emi makes a face at Rin as though she had bitten into a lemon. She's clearly unhappy with her for not joining in."

        emi "Oh come on, Rin. That's not polite at all."

        show rin relaxed_boredom
        with charachange

        rin "Nothing, thank you."

        show emi basic_confused
        with charachange

        emi "No, no, you silly! I meant that you should order something too."

        show rin negative_spaciness
        with charachange

        rin "I'll take a straw then. My feet are all wet."

        show yuukoshang worried_up
        with charachange

        yu "Sorry?"

        show rin basic_awayabsent
        with charachange

        rin "The drinking kind of straw. One, please."

        show yuukoshang worried_down
        with charachange

        "Yuuko is obviously uncertain of what to think about this. She fiddles with her pen and stationery for a moment, looking like she's about to cry, before deciding that we've finished ordering."

        show yuukoshang neurotic_up
        with charachange

        yu "Thank you very much!"

        show yuukoshang neurotic_down:
            center
            ypos 1.25
        with Dissolvemove(0.2)

        pause 0.3

        show yuukoshang neurotic_down at center
        with charamove

        hide yuukoshang
        with charaexit

        show emi basic_grin at twoleft
        show rin at tworight
        with charamovechangefaster

        $ renpy.music.set_volume(0.7, 2.0, channel="ambient")

        "She bows down a little bit too deeply and scampers to safety behind the counter."

        "After that ordeal is over with, I have a chance to relax a bit and take a better look at the surroundings."

        "Almost every table is occupied by people happy to be out of the rain, thankfully sipping their tea while waiting to dry off."

        "Fragments of grumbling about the lousy weather or discussions over recent homework carry from nearby tables to my ears. Each one overlaps the other, but all are covered by the sound of falling rain."

        show emi at left
        show rin:
            right
            xpos 0.95
        with charamove

        show yuukoshang smile_up at center
        with charaenter

        $ renpy.music.set_volume(0.4, 2.0, channel="ambient")

        "After a while Yuuko returns to our table, carrying a tray with a huge teapot, three cups, a slice of cake and two slices of pie."

        show yuukoshang neurotic_up at centertremble
        with charachange

        pause 0.5

        show yuukoshang smile_down:
            center
            ypos 1.25
        with Dissolvemove(0.2)
        play sound sfx_pillow

        pause 0.3

        show yuukoshang smile_down at center
        with charamove

        hide yuukoshang
        with charaexit

        show emi basic_grin at twoleft
        show rin basic_awayabsent at tworight
        with charamovechangefaster

        $ renpy.music.set_volume(0.7, 2.0, channel="ambient")

        "She slaps the tray onto our tiny table with a clatter, almost sending the teapot toppling over into Rin's lap. We barely recover before she bows again and leaves, hurrying off to serve the other customers."

        "Emi has been eyeing her strawberry cake very hungrily all this time, but somehow she managed to contain herself until Yuuko was out of sight."

        show emi excited_smile
        with charachange

        "She digs in with gusto, while I content myself with pouring tea for everyone and placing the straw in Rin's cup."

        show rin basic_deadpansurprised
        with charachange

        "Rin looks at the way the tea swirls round and round in her white china cup, her eyes half closed, almost like she is being hypnotized."

        show shangpai:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0
        with Pause(1.0)

        show shangpai at truecenter

        "I pick up my fork and eye the food in front of me. The pie I got looks perfectly done, a thick layer of meringue atop creamy lemon custard."

        "After having the first bite, I pause, savoring the combination of tangy citrus and smooth, sugary meringue. It's quite good, though a bit too sweet for me."

        show emi excited_joy
        show rin basic_deadpannormal
        with None

        show shangpai:
            easeout 1.0 ypos 0.7 alpha 0.0
        with Pause(1.0)

        hide shangpai

        emi "Iff ver’ good."

        "She's talking through a mouthful of cake, already halfway through her slice even though it's not exactly small."

        show emi basic_grin
        with charachange

        emi "I want to taste some of that."

        play sound sfx_slide2

        show emi excited_happy_close
        show rin basic_absent
        with characlose

        show emi basic_closedgrin
        show rin basic_awayabsent
        with charachange

        "Before I get to respond, she strikes out at my delicious pie, takes a piece with her fork, and escapes with it."

        show emi basic_closedhappy
        with charachange

        emi "This is pretty good too."

        hi "What are you doing? You have a slice of your own!"

        show emi excited_proud
        with charachange

        emi "Yeah, but if I started on that before finishing the cake, it'd be rude, don't you think?"

        "Her insolence is outrageous, but the gentleman in me allows for no retaliation."

        show emi basic_grin
        with charachange

        "I glare angrily at her, and she replies by sticking out her tongue impishly. Emi is even more hyper than usual today, but I don't mind. It's good for her to let off some steam."

        "I take another sip of the tea in my cup. It's good and hot, even though I don't usually care much for tea, and the atmosphere in the café is very relaxing."

        "I don't mind spending the rest of the afternoon here, not even after Emi orders her second piece of strawberry cake and Rin spends most of the time staring fixedly at the rain streaming down from the heavens."

        show rain normal behind bg

        "Even Yuuko rolls her eyes at the third piece of cake disappearing into Emi's bottomless stomach just as quickly as the previous two."

        $ renpy.music.set_volume(1.0, 2.0, channel="ambient")
        play ambient sfx_rain fadein 1.0

        scene bg suburb_shanghaiext_rn
        show rain normal
        with shorttimeskip

        "Despite the passing of time, it's still raining outside when we exit the Shanghai, though it seems to be letting up a little."

        hi "Too bad it had to rain on your parade."

        show rin basic_awayabsent_rn behind rain at center
        with charaenter

        rin "Weren't we supposed to have a picnic?"

        show rin at tworight
        show bg at bgright
        with charamove

        show emi basic_closedgrin_rn behind rain at twoleft
        with charaenter

        "Emi doesn't look too distraught over this turn of events."

        emi "Nah it's fine! We had a good time, didn't we? I feel really pumped up."

        show emi basic_grin_rn
        with charachange

        emi "It isn't even raining that hard any more. I kinda want to hike back to school to get rid of this energy and work off some of that cake."

        "She stretches her arms out, and arches her back like a cat. After rolling her shoulders around twice, she smiles brightly."

        show emi sad_grin_rn
        with charachange

        emi "Man, I can't really run with these legs, though, especially uphill. I wish I'd brought my other ones."

        "This notion sounds odd, spoken so casually. But I guess for Emi, changing legs is sort of like someone else changing shoes."

        show emi excited_proud_rn
        with charachange

        emi "Maybe if I walk really fast, that'll be kinda like running. I think I'll do that."

        show rin basic_absent_rn
        with charachange

        hi "I won't be able to keep up with that going uphill, though; I really am in bad shape. Plus, you'll get wet without an umbrella."

        show emi basic_grin_rn
        show rin basic_awayabsent_rn
        with charachange

        emi "It's hardly even a drizzle, now. A few drops won't hurt. I think I'm gonna go to the track after I change my legs, too."

        "Emi skips away from the protection of my umbrella and goes on ahead at a brisk pace. Suddenly, she seems to remember something as she stops and spins around."

        show emi excited_smile_rn
        with charachange

        emi "See you tomorrow!"

        show emi excited_proud_rn
        with charachange

        emi "Come eat lunch with us on the roof! I'll bring enough for three."

        show emi:
            ease 1.0 offscreenleft alpha 0.0
        with None

        show rin basic_absent_rn at center
        show bg at center
        with charamovechangefaster

        hide emi

        stop music fadeout 5.0

        "Rin and I are left to watch her wave at us and skip off again. Soon she disappears around a street corner. I'll never understand why Emi is perpetually in such a hurry to get somewhere."

        hi "So, would you like me to walk you back to school so that at least one of you won't get wet?"

        show rin basic_deadpan_rn
        with charachange

        rin "If you are happy with it."

        "It seems neither of us wants to keep alive the strained atmosphere from the argument a few days ago in the art room, which makes me feel relieved. I don't want to bear grudges and I'm happy that Rin feels the same way."

        "Thus it is decided that we are content with each other's company for now, and we start walking in the same direction as Emi, albeit at a considerably calmer pace."

        scene ev rin_rain_away_close:
            center
            acdc_warp 20.0 top
        show rain normal
        with whiteout
        $ renpy.music.set_volume(0.7, 4.0, channel="ambient")

        "I get a bit closer to Rin, even though the umbrella is already big enough to shelter us both. I can feel her nearby warmth providing a contrast to the chill of this rainy weather."

        "Raindrops hitting the umbrella make a distinctive sound, playing the staccato melody of rainfall for nobody in particular."

        "I realize I haven't been outside in the rain in what feels like forever. I inhale, taking in the scent of rain, feeling the weather with all my senses."

        "The world melts into a blur inside the rain."

        "The colors of the sky have deepened from gray to dark blue, with hues of red added to the mix from the sunlight reflecting off the clouds. The low-hanging sky looks pretty, as if I could reach out my hand and touch it."

        $ renpy.music.set_volume(0.5, 4.0, channel="ambient")

        rin "Have I told you how much I like rain? It's like painting. It makes me feel connected."

        "Almost echoing my thoughts, Rin lets out one of her own. It slips out of her mouth, circling around us gently."

        rin "Everything looks so soft, like the outlines of things just disappear. I like that."

        rin "It's like the rain is hugging me."

        "Her voice sounds different from usual; more gentle, now, and soft. I wonder if it's only because of the rain, or because of the mood the rain brought upon the quiet artist girl."

        show ev rin_rain_away_close behind rain at top
        show ovl rin_rain_hisaotowards_close behind rain at right
        with charachangealways

        "I feel that mood in myself too, enhanced by her words."

        hi "Yeah. I like rainy weather too. It's nice every once in a while."

        hi "I wonder what is it about the rain."

        show ev rin_rain_towards_close at top
        hide ovl
        with charachangeev

        rin "Everything."

        show ev rin_rain_towards:
            truecenter
            zoom 1.05
            ease 5.0 zoom 1.0
        with locationchange

        $ renpy.music.set_volume(0.35, 6.0, channel="ambient")

        "A silence follows the statement, as it allows for no continuation. I decide to push the direction of the conversation a little."

        hi "But you know, if you like the feeling of being connected, what's the problem with showing your paintings to others?"

        hi "Don't you want to be connected to other people?"

        show ev rin_rain_away
        show ovl rin_rain_hisaotowards behind rain at right
        with charachangeev

        rin "It's not the same thing. You're comparing apples and squids."

        "I brought up the subject Rin wants to avoid, and it shuts her down again. The question stays hanging between us for the rest of the trip back to school, and I can't help wondering what on Earth I could have said to truly reach Rin."

        "Does she feel that she's lacking an identity?"

        "She has a strong personality, but if pressed to elaborate, I'm not sure I could describe it accurately. She feels like a person who is in constant conflict with herself. I never know what to expect when I talk to her."

        "I wonder how she herself experiences that disconnect."

        "If Rin is asking herself every day 'Who am I?' and obsessively paints images to define herself day after day, what does she think of that way of living?"

        hide ovl
        with dissolve

        "The irony is, that's the exact same question I've been asking myself for the past four or five months. For me, it was miserable. I can only assume that it's the natural state of being for this girl."

        scene bg school_dormext_full_rn
        show rain normal
        show rin basic_awayabsent_close_rn behind rain at center
        with shorttimeskip

        $ renpy.music.set_volume(0.7, 1.0, channel="ambient")

        "When we stop in front of the dormitories Rin turns to face me, as if sensing my thoughts from afar. Her gaze travels emptily past my left shoulder into the shapeless rainfall."

        "Her dark eyes seem to suck the low ambient light into themselves, like a reverse mirror."

        "That empty gaze lets nothing out. If I want to understand what's going on behind those eyes, I have to work it out myself."

        "Rin opens her mouth, then closes it without saying anything. The silence lasts for a few more moments before she takes a step towards the dorm building door."

        show rin basic_absent_rn
        with charadistant

        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

        rin "See you tomorrow."

        stop ambient fadeout 0.5

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .six_meters_closer:
        scene bg school_dormhisao
        with dissolve

        "The next morning, like every second Monday morning until he says otherwise, I have an appointment with the nurse."

        "They allow me to skip part of my first class in the morning, and I don't feel any shame in skipping the rest, either."

        "Rather than being thankful I get to miss world history, I instead feel dread when I think about these appointments."

        scene bg school_dormbathroom
        show steam
        with locationchange

        play ambient sfx_shower fadein 0.5

        "I wake up at the normal time anyway and wash myself in the bathroom I share with Kenji, tidying my sleep-disheveled hair."

        "I quickly get dressed and put my laundry in the basket."

        stop ambient fadeout 0.5
        scene bg school_dormhisao
        with locationchange

        "I pack up for the school day. I have all my homework done, like usual, so I have a bit of free time now."

        "There's no point in going to the morning class for 20 minutes before I'd have to get to the nurse's office, so I lie down on my bed and read a book until it's time to go."

        scene black
        with dissolve

        scene bg school_nurseoffice
        with locationskip

        play sound sfx_doorknock2

        "The door to the nurse's office is open, which is unusual. I enter while knocking to announce my arrival. Looking up from his computer screen, he motions me to take a seat with a friendly hello."

        "Steam wafts up from a piping hot cup of coffee on his desk. It's probably not his first today."

        play music music_nurse fadein 0.5
        $ renpy.music.set_volume(1.0, 4.0, channel="ambient")

        show nurse neutral at center
        with charaenter

        nk "How are you feeling on this wonderful morning, Hisao?"

        hi "I'm all right, I think. It was cold yesterday because of the rain so I woke up feeling a bit groggy."

        show nurse fabulous
        with charachange

        nk "You too, huh? Quite a few kids got caught without an umbrella, so we've been spending time handing out masks and curing sniffles. Hmm… all right, today it's tests day. Give me your arm."

        show nurse neutral_close
        with characlose

        "I extend my left arm towards him, keeping my face expressionless. The nurse ties a rubber tourniquet around my bicep with a practiced movement and briskly goes about his business."

        "I don't think anybody really likes getting stuck with needles, but at least I got over my distaste for them. I had to. Now, I barely even twitch at the moment of truth."

        "Once that's done, a blood pressure check follows, then there are checklists and questionnaires to go through. The nurse nods and scribbles in my answers to the questions as I give them."

        show nurse grin_close
        with charachange

        nk "All right. Let's have a listen, now."

        show nurse neutral_close
        with charachange
        play sound sfx_rustling

        "I unbutton my shirt and put it neatly on the back of the chair I was using while he puts on his stethoscope."

        "I know by heart the order of places where he's going to listen to my lungs and heartbeat. I adjust my breathing to be even and deep without even being asked. It's become routine now, for both of us."

        "It's funny, this is pretty much the only time in one's life when you really concentrate on breathing and nothing else. It has always amused me."

        "The nurse lifts the cold steel stethoscope from my chest and places it a few inches lower, listening again. The contact of the metal makes me flinch on reflex, even though I was expecting it."

        show nurse concern_close
        with charachange

        "He furrows his brow, but I can't tell if it's because he's unhappy or if he's trying to pick something specific out among the complex multitude of irregularities in my heartbeat."

        hi "Is there something wrong?"

        nk "Please don't talk."

        "I shut up and become more anxious. The nurse is nice, but I can't help disliking these mandatory checkups. I wonder if I'm going to end up hating all medical appointments from now on because of these."

        show nurse concern
        with charadistant

        "He finally lifts the circular metal plate from my chest, allowing me to talk again."

        show nurse grin
        with charachange

        nk "Everything seems to be fine. Are you feeling all right yourself?"

        hi "I suppose. I was out yesterday when it was raining, and yeah, I really felt a bit under the weather in the morning. Maybe I caught a cold."

        show nurse fabulous
        with charachange

        nk "Were you with Emi? She came down with a cold, too. My people told her to stay in bed for a day or two."

        hi "Really? I mean, I was with her but I didn't know she got sick."

        "I guess it was a dumb thing after all, for her to go out in the rain like that."

        show nurse neutral
        with charachange

        nk "Yeah. Well, let's put that aside. Everything seems to check out for you, but remember to be careful."

        hi "Of course. I really don't want to go back to the hospital."

        "He catches something - maybe repressed terror, I don't know - in my voice and glances up from some papers he was looking at."

        show nurse fabulous
        with charachange

        nk "Hey, don't worry. At this stage, it would take a huge crash in your condition to get you rehospitalized."

        "It doesn't really reassure me, but grumbling about it to him won't make any difference. I quietly take my leave."

        stop music fadeout 7.0

        scene bg school_nursehall
        with locationchange

        "Walking along the corridor from the auxiliary building to the main school building, I encounter a young female nurse coming the other way. She smiles at me when we pass by each other."

        scene bg school_lobby
        with locationchange

        $ renpy.music.set_volume(0.1, 0.0, channel="ambient")
        play ambient sfx_crowd_indoors fadein 0.5

        "The lobby is empty of people. No surprise, since classes are still going on. I hear muffled sounds of discussion coming from behind the first floor classroom doors."

        "I glance at my watch. I'd have to rush to get to my classroom in time, and I don't feel like going to class anyway, so I decide to climb up to the roof and have an extra-long lunch break."

        "Emi promised she'd bring something for me today but if she's sick, that's probably not going to happen. I'm not feeling hungry anyway, so it's all the same."

        play ambient sfx_rooftop fadein 0.5
        $ renpy.music.set_volume(0.3, 0.5, channel="ambient")

        scene bg school_staircase1
        with locationchange

        "The climb up the steep stairwell to the roof is oddly liberating, almost like losing weight. I feel satisfaction that it doesn't wind me as badly as it did the first time I came up here."

        "I push open the squeaky door at the top and step into sunlight."

        play sound sfx_door_creak
        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")
        scene bg school_roof
        with Fade(0.5, 0.1, 2.0, color="#FFF")

        "The chain link fence allows for a grand view over the treetops, all the way to the gray silhouettes of downtown, further away."

        scene bg misc_sky:
            left
            linear 40.0 right
        with locationchange

        "The dreary weather of yesterday is just a memory now. The silvery blue sky seems to be a mere arm's reach away."

        "I forget for a moment that I'm in a bad mood. The warmth of the sun soaks into my bones, making me drowsy and lazy instead."

        scene bg school_roof
        with shorttimeskip
        play sound sfx_normalbell

        "The bells ring for lunch break, startling me back into reality."

        "Soon afterwards, the quad below me bursts into life. Students pour out of the doors down on the ground floor, intent on enjoying lunch at the quad and the lush gardens in this perfect weather."

        "When I hear the door to the stairwell being pushed open, I don't bother turning to see who it is."

        "The intruder starts coming towards me with uneven footsteps. The little riverstones the roof is covered with rattle and crunch underfoot."

        $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

        scene bg misc_sky
        with locationchange

        "The footsteps stop a few feet behind me, followed by a silence. I look upwards, into the glowing eye of the sun, absorbing its warmth with my whole body."

        rin "What are you doing?"

        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

        scene bg school_roof
        show rin basic_absent
        with locationchange

        "I turn around out of courtesy at her first words, to behold the slim, awkward figure of Rin Tezuka. She looks very much like herself today, too. Her hair is maybe a tad messier than usual, as if she just got out of bed."

        "She stands with her weight shifted onto one foot, looking at me with mild curiosity, as if I were something in a store's display window."

        hi "I don't know. Just spacing out, I guess."

        hi "What about you?"

        show rin basic_deadpan
        with charachange

        rin "Emi promised food. We usually eat here."

        hi "I'm afraid you're going to be disappointed. I heard Emi came down with a cold."

        show rin relaxed_nonchalant
        with charachange

        rin "Oh. I guess that makes sense. She wasn't in class."

        hi "It's not that common to get a cold in June though. You don't think she went running at the track afterwards like she said? The rain just kept going."

        show rin basic_deadpanupset
        with charachange

        rin "Probably."

        hi "In the rain?"

        rin "In the rain."

        "That sounds like a bit too much for just keeping up with training regime. Emi is a hard-headed one, though, so I can see her running in the downpour just because she 'had to.'"

        hi "Well, that's obviously overdoing it. Probably why she came down with that cold, too."

        hi "But I guess it's kinda cool."

        show rin relaxed_boredom
        with charachange

        rin "Speaking of that, I'm not feeling well either. I…"

        stop ambient

        show rin relaxed_sleepy
        with vpunch

        rin "ACHOO!"

        play music music_another fadein 4.0

        "Rin sneezes pretty hard, failing to stop it in time. She cranes her head down to wipe her nose on her shoulder, so deciding that would be too unladylike I pull out my handkerchief and hold it to her nose."

        show rin relaxed_sleepy_close
        with characlose

        hi "Here. Bless you."

        show rin relaxed_doubt_close
        with charachange

        rin "Danks."

        "She clears her nose and I dab the handkerchief gently on it, wiping it clean."

        "Her nose is really cute. Oddly enough it's probably the girliest part of Rin's face. I think I'm blushing a little, but Rin doesn't notice."

        show rin basic_lucid_close
        with charachange

        rin "Thanks - I think I might be coming up or down with something, too. Like I was saying."

        hi "Hope not."

        show rin basic_awayabsent_close
        with charachange

        "Rin doesn't seem to be to bothered about eating, so despite the lack of Emi-provided lunch, we stay up on the rooftop. She comes over and stands next to me, right up against the fence, looking into the same abstract distance as I am."

        "Nobody else seems to be coming around to intrude upon this calmness, either. It's quiet and peaceful."

        stop music fadeout 2.0
        play ambient sfx_rooftop fadein 3.0

        scene bg school_roof
        with shorttimeskip

        "What does one do on a lunch break if not eat?"

        "It turns out that, between the two of us, we don't really know. Fortunately, passing time is an activity that manages itself just fine."

        "Even though there's no conversation to fill the silence between the passing seconds, no pointless activities like cloud-gazing to spend upon the minutes between now and then, time marches on relentlessly."

        "I keep checking the time on my watch, then decide it's a dumb thing to do. Instead, I try to hold out for as long as possible before I check it again. Maybe I can hold out for six or seven minutes."

        show rin basic_awayabsent_close at center
        with charaenter

        "Rin remains silent, idly looking up at the cerulean expanse above us."

        "I wonder why, more often than not, we don't speak much. She said that she doesn't like speaking because of her perceived difficulties with expressing herself properly."

        "As for me, I think I just got sucked into the habit at the hospital, where I spent such a long stretch of time never really talking to anyone."

        "Most of the time I feel comfortable about this quiet mood. And even when I get the feeling that I have to break the silence, it's always so difficult to come up with something to talk about when it's with Rin."

        "She and I are on such different wavelengths that nothing seems to be on common ground."

        hi "What is it that you like about the sky so much?"

        show rin basic_deadpannormal_close
        with charachange

        "She turns to me, her eyes dark and serious."

        show rin basic_deadpan_close
        with charachange

        rin "Sky is the only thing that is perfect."

        show rin basic_awayabsent_close
        with charachange

        rin "I know it. You could say I'm an expert of sky if you wanted. And I am even if you didn't want to. A sky expert."

        rin "It's always different, but it's always perfect also when it's different."

        $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

        scene bg misc_sky:
            xalign 0.0
            warp acdc_warp 8.0 xalign 1.0
        with locationchange

        "I follow her gaze up into the boundless blue expanse, thinking of her words."

        hi "Have you ever wanted to be something different?"

        rin "It wouldn't be so bad to be the sky."

        hi "No, I mean, someone else, someone different. To go to a normal school like everyone else, not have to worry about stuff…"

        rin "What stuff?"

        "I try to find the right words for a moment, but can't manage to form a sentence that I'd be comfortable with actually using."

        hi "Man, I don't really want to say it aloud."

        rin "Try. I'm not so good at mind reading."

        stop ambient fadeout 0.5
        scene bg school_roof
        show rin basic_awayabsent_close at center
        with locationchange

        hi "Don't you ever want to not be disabled?"

        "She thinks about this and then shakes her head, frowning."

        show rin negative_annoyed_close
        with charachange

        rin "That's a hard question. I don't know what to say."

        hi "It's okay if you don't say anything."

        hi "For some reason, I'm just so unsatisfied with who I am right now that I'm constantly thinking stuff like that. It's pretty hard to admit, but there it is."

        "Honestly, I feel relieved about finally saying it aloud to someone, even if it's just Rin."

        show rin negative_confused_close
        with charachange

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        play music music_serene fadein 8.0

        rin "I think I want to be different, sometimes. I've thought about changing myself lately, but it's a bit scary, like walking backwards with your eyes closed."

        show rin negative_worried_close
        with charachange

        rin "The difficult part is to know where your toes are not pointing. I mean, directions."

        show rin basic_sad_close
        with charachange

        rin "Even if I don't do anything, I would never stay the same."

        show rin negative_spaciness_close
        with charachange

        rin "It's like my old paintings. They are different than what I paint now, because I'm different, but they are still my paintings so there's something same. That's really strange."

        show rin basic_lucid_close
        with charachange

        rin "I am different every day, but I'm still me every day. Who am I then?"

        hi "Is that a riddle?"

        show rin basic_deadpanupset_close
        with charachange

        rin "If you want it to be. I don't know the right answer though, so you have to come up with it yourself."

        hi "Well, it's the sky, isn't it? Going by your definition just now."

        show rin basic_surprised_close
        with charachange

        "I actually manage to surprise her by that. Maybe she had already forgotten about it."

        show rin basic_deadpansurprised_close
        with charachange

        rin "That's right! But I was thinking about myself when I said that. Very strange."

        show rin basic_lucid_close
        with charachange

        rin "Could it be that I actually am the sky?"

        hi "I don't think that's possible. Your logic's a bit off somewhere."

        show rin basic_awayabsent_close
        with charachange

        "She looks down and shuts up and I can see she's quickly going over the deduction mentally, seemingly unhappy with the result she finally arrives at."

        show rin basic_deadpanupset_close
        with charachange

        rin "Yeah, maybe I'm not the sky. Would make sense, I have a hard time knowing what kind of a person I am."

        hi "You're not the only one."

        show rin negative_spaciness_close
        with charachange

        rin "It's like my mind is in some other place than the rest of me."

        hi "Underwater."

        show rin basic_awayabsent_close
        with charachange

        rin "Yeah. I wonder how it got there."

        "I have no answer, so a brief silence falls between us for a moment. I shift my gaze back to the sky above us."

        $ renpy.music.set_volume(0.5, 2.0, channel="music")

        scene bg misc_sky
        with locationchange

        nvl clear
        nvl show dissolve

        n "{vspace=60}The last time I really paid much attention to the sky was… I guess it must've been at the hospital. I could only see a thin strip of sky from the window of my room. If I walked up to the windows and pressed my face against the cold glass, the strip became bigger, but not by much."

        n "That sky made me feel sad and lonely, a reminder of the world on the other side. I wonder if there's another world beyond the sky we see from up here on the school's roof, as well."

        n "I can't stop comparing life at Yamaku to my hospitalization, but I really should. I'm not there any more."

        n "The narrow sky from the window of my hospital room, the faces of the doctors, the faces of my parents. The off-white walls everywhere. Iwanako's letter, echoing the words she never said. They're things of the past now."

        n "I wish I could forget everything up until now and that time would stop completely. There would be only me, Rin, and the sky, an eternal lunch break on this rooftop. Perfect, unchanging, and forever."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")

        nvl clear
        nvl hide dissolve

        hi "I'm not sure if I like or hate this school."

        rin "I could have gone to a normal school if I wanted, but I chose to come here."

        scene bg school_roof
        show rin relaxed_nonchalant_close at center
        with locationchange

        hi "Why?"

        show rin relaxed_doubt_close
        with charachange

        rin "I just decided I would. Kind of like melon or plum jelly."

        hi "Do you think it was a good idea?"

        hi "I mean, there are a lot of good things about this school, but I think there are a few bad things also."

        show rin basic_lucid_close
        with charachange

        rin "I know."

        show rin basic_awayabsent_close
        with charachange

        rin "I kind of collect people, because they are interesting. People here really are amazing. Most of them. But not all."

        show rin negative_angry_close
        with charachange

        rin "Some people can't take it. They hurt too much. It gets really bad sometimes, you know. They hurt."

        show rin basic_deadpanupset_close
        with charachange

        rin "I wonder if you're like that too? I hope not. I don't like things like that."

        hi "Hey, I'm not your case study. And I'm not going to give up and die or anything."

        hi "Anyway, I meant more that this place is too distant from the real world."

        show rin basic_surprised_close
        with charachange

        rin "What's the real world?"

        hi "Everything out there. Real people, with normal everyday lives that fit together like a puzzle."

        show rin relaxed_surprised_close
        with charachange

        rin "You don't think we aren't like that? Real people?"

        hi "Maybe we aren't. Well, no, we are. I just meant that it feels more like we're the leftover pieces."

        show rin negative_annoyed_close
        with charachange

        "Rin thinks for a while, her almond-shaped eyes narrowing as she bites her lip a little bit, like a child."

        show rin basic_deadpansurprised_close
        with charachange

        rin "Is it hard to be disabled?"

        "Her question earns a dry chuckle from me."

        hi "You tell me. You've been in this business a lot longer than I have."

        show rin negative_annoyed_close
        with charachange

        "She thinks about that for another while."

        show rin basic_deadpancontemplation_close
        with charachange

        rin "I don't really feel that disabled. I mean I do pretty much everything differently, but it's not that hard. I can always practice."

        show rin basic_deadpandelight_close
        with charachange

        rin "I've started to practice food things this year. I think I'd want to learn to cook in a real kitchen someday."

        hi "That's admirable, but I don't think it's just a state of mind."

        show rin basic_lucid_close
        with charachange

        rin "Maybe not to you."

        "I have no good counter to that, so I concede by falling silent. The situation is making me more and more confused."

        "I know what I want, but don't know how to reach it. Rin seems to believe she can simply will herself into the shape she thinks she needs to be, but can't decide whether she wants to be a bird or a butterfly."

        show rin basic_awayabsent_close
        with charachange

        rin "I think, in the end I'm not really that happy with who I am either, but that doesn't mean I regret being who I am."

        show rin relaxed_nonchalant_close
        with charachange

        stop music fadeout 0.5

        rin "That's the thing that's wrong with you, Hisao."

        play sound sfx_rustling

        scene bg school_roof_blurred
        show rin basic_lucid_superclose at center
        with characlose

        "I've only started to process that rather blunt statement before Rin suddenly hugs me."

        hi "What are you doing?"

        "I've never been hugged by a girl with no arms before. To be honest, it doesn't really, physically feel like a hug. The awkward way she presses her body against mine and the lack of embracing arms makes it feel like she fell on top of me."

        "But the warmth of a real hug is still there, and that's how I recognize it for what it is."

        show rin basic_deadpannormal_superclose
        with charachange

        play music music_comfort fadein 9.0

        rin "I'm hugging you, Hisao."

        hi "I know that, but…"

        show rin relaxed_doubt_superclose
        with charachange

        rin "Is it wrong? I thought this is what you're supposed to do."

        show rin relaxed_sleepy_superclose
        with charachange

        rin "I'm not really used to this kind of thing. The first time Emi hugged me I got surprised and kicked her in the stomach. I can kick pretty hard so she hasn't been hugging me an awful lot after that."

        hi "It's not wrong. Just, no, it's just me… things are a bit hard for me, for the time being. I can't seem to react properly to anything."

        show rin relaxed_surprised_superclose
        with charachange

        rin "Really? So it is hard being disabled after all?"

        "I guess she has me cornered there. I don't have the energy to start arguing against it, but I feel like I have to get something out."

        hi "Well, I… no, it's not hard. I think it's just me overthinking things."

        hi "I really wish I didn't feel so sorry for myself all the time."

        "I wonder if I always was this fragile or if I became this way after my incident. Nothing had ever truly shaken my world like that before, so there's no telling."

        show rin basic_lucid_superclose
        with charachange

        "Rin presses her cheek against me tightly. I can feel the warmth of her body close against me."

        "Her body temperature feels really high, as if she had absorbed the sunlight into herself and was now sharing it with me. Or perhaps it's a natural state for her."

        "It's the most comforting thing I've felt in a long, long time."

        show rin basic_deadpan_superclose
        with charachange

        rin "Wow, your heartbeat really does sound really weird. It's like a drunken percussion orchestra."

        hi "Please don't say stuff like that. I get very uncomfortable."

        "I laugh at her comment anyway, in an attempt to ease the tension. It sounds a little bit too forced."

        hi "Man, I'm sorry I'm such a mess."

        show rin basic_deadpannormal_superclose
        with charachange

        rin "It's okay. It's the best part of you."

        hi "Hearing that doesn't make me happy."

        scene bg school_roof
        show rin basic_deadpannormal_close at center
        with charadistant

        "She breaks off the hug and settles down. An awkward silence falls upon us like a blanket; me feeling embarrassed about myself and Rin trying to arrange her expression to something she likes."

        $ renpy.music.set_volume(0.5, 2.0, channel="music")

        scene bg misc_sky
        with locationchange

        "One last time, I glance upwards."

        hi "This rooftop is really great. It's like I'm just a little bit closer to the sky."

        rin "I know a better place, but we can't go there on lunch break. I can take you there sometime if you want."

        play sound sfx_warningbell

        "The bells ring for the beginning of the afternoon classes and Rin stands up to make her way downstairs. I don't hurry after her, deciding to stay up here for just a little while longer."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")

        scene bg school_roof
        show rin basic_awayabsent at center
        with locationchange

        hi "Thanks for the hug."

        show rin basic_lucid
        with charachange

        rin "Thanks for not kicking me."

        hide rin
        with charaexit

        "After Rin leaves I finally let tears roll down my cheeks and cry for my condition for the first and only time in my life."

        "Then I cast away that hollow person lying on the hospital bed, forever."

        stop music fadeout 2.0
        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .indecision:
        scene bg school_scienceroom
        with locationchange

        "Two days later, I'm feeling less miserable. I even go for a long, brisk, healthy walk like the nurse recommended, something which I had avoided and dodged with all sorts of excuses earlier."

        "I feel more active in class as well, delighting our science/homeroom teacher, Mr. Mutou, with correct and promptly delivered answers."

        "The break right now between the two morning classes is too short for any sort of meaningful activity, but too long to just spend it sitting in the classroom and doing nothing."

        play ambient sfx_crowd_indoors fadein 0.5

        scene bg school_hallway3
        show crowd
        with locationchange

        "Going out into the hallway isn't much better, but flexing my stiffened muscles is a better use of time than letting them get even stiffer by staying seated."

        "The door of the neighboring classroom door opens and the students of 3-4 emerge to further fill up the already semi-crowded hallway. It seems their teacher kept them in for a few extra minutes."

        "Emi is among them. She notices me noticing her, which almost makes me look away on reflex."

        play music music_emi fadein 0.5

        show emi basic_closedgrin at center
        with charaenter

        "I don't, however, and Emi smiles at me as she happily skips towards me past the other students."

        "Emi looks pretty energetic, showing no sign of illness whatsoever. It seems she recovered from the cold."

        show emi basic_happy
        with charachange

        emi "Hey! Good morning!"

        hi "Nice to see you back on your feet. Feeling better now?"

        "She looks fine to me, but I still feel compelled to ask."

        show emi excited_laugh
        with charachange

        emi "Thanks! And yeah, I do. It was just a cold, nothing serious."

        "Emi laughs confidently, as if to emphasize her condition. I wonder for a moment what would count as serious in Emi's book."

        "She seems to be eager to put the topic aside, though."

        show emi excited_happy
        with charachange

        hi "Where are you going?"

        show emi basic_closedgrin
        with charachange

        emi "Off to Rin's room to see if she's awake yet."

        hi "Oh? She skipped the morning class?"

        show emi sad_grin
        with charachange

        "A sheepish smile emerges on Emi's face and she gets slightly flustered."

        emi "Err… not exactly. It seems that she caught the cold that I had."

        hi "Sorry to hear that. Well, she was out in the rain on Sunday with us, after all. I saw her on Monday and she was feeling a bit under the weather back then too."

        show emi basic_grin
        with charachange

        emi "Yeah. Anyway, I'll ask the nurse for some cold medication to give her if she doesn't get better soon."

        stop music fadeout 3.0

        hide emi
        with charaexit

        "She leaves for the girls' dorm. I want to go with her to wish Rin well. I want to tell her that I'm better now too, but it doesn't feel appropriate."

        "An unspecified feeling diverts my thoughts away. Somehow I just can't summon the resolve to go in there. Is this what Iwanako went through when she tried to tell me what she felt?"

        stop ambient fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .signal_interference:
        scene bg school_girlsdormhall
        with locationchange

        "Even though I'm feeling more energetic, I'm still hesitant about going over there to talk to Rin."

        "It's not until two days later, on Friday, that I finally gather enough courage to enter the girls' dorm. I ask the first person I meet inside for directions to Rin's room."

        play sound sfx_doorknock2

        "I knock on Rin's unmarked door and wait."

        $ renpy.music.set_volume(0.5, 0.0, channel="sound")
        play sound sfx_rustling
        $ renpy.music.set_volume(1.0, 10.0, channel="sound")

        "After a few seconds of silence I hear something rustling inside the room. I start wondering if maybe I should've brought something for her, like a can of warm coffee or some oranges. I could have peeled them for her. Well, too late now."

        "The door opens soundlessly - it was already unlocked - and I find myself staring at Rin, who stares back at me."

        "She looks like she just got out of bed, with her hair all messed up."

        show rinpan basic_deadpanamused:
            right
            xpos 1.05
            easein 0.5 right
        with charaenter

        show rinpan at right

        "…and barely any clothes on."

        "…"

        show rinpan basic_amused
        with charachange

        rin "Hellooooo."

        play music music_rin fadein 0.5

        "There is a strange, stupid-looking smile on Rin's face. I'm not exactly sure why."

        "Rin smiles so rarely that it seems to be out of place every time. Especially so now, given her partially undressed state. Said state makes me feel extremely conflicted about whether or not this was a good idea."

        "Her cheeks are flushed rose-red, contrasting with the milky-pale complexion of a person who doesn't get enough sunlight. Her forehead looks sweaty, as though she might have a fever."

        hi "Um, hi."

        show rinpan basic_absent
        with charachange

        "Now what? I didn't plan anything further than this, and Rin is staring at me with those expectant eyes of hers again."

        "Something about this situation gives me very strange vibes. Her eyes are even more vacant than usual and she seems to have a hard time focusing them on anything."

        "The lack of clothing is disturbing, but since she herself doesn't seem to be bothered, why should I be?"

        "I keep telling myself that."

        hi "Err, I thought I'd pay you a visit since you haven't been at the art club… and I wanted to talk with you and wish you well."

        "Rin doesn't show any sign of recognizing what I just said, making me wonder if she actually understood my words, or if she even heard them."

        "Maybe it's the fever making her groggy; she might've actually been asleep before I came over."

        show rinpan basic_deadpan
        with charachange

        rin "Okay."

        show rinpan basic_deadpan:
            easeout 0.5 alpha 0.0 xpos 1.05
        with Pause(0.5)

        hide rinpan

        "She turns on her heel and withdraws from the door, walking back inside the small room. From the doorway I can see her walk to her bed and half fall down, half sit down on the messy pile of bedsheets."

        "The open doorway seems to be more of an obstacle in my mind than the closed door was, but since Rin doesn't say anything else, I step through it, and into her room."

        scene bg school_dormrin
        with locationchange

        "Rin is on her bed leaning against the wall, leaving the only chair in the room for me."

        "She keeps quiet even after I sit down, so maybe she meant to invite me in but just forgot to say so aloud? An implied invitation, as it were."

        show rinpan basic_deadpanamused at twoleft
        with charaenter

        rin "Very exciting. Nobody has visited me before."

        "The breaking of the silence draws my attention from the room to its inhabitant, who currently seems to be in the middle of a very profound thought process."

        show rinpan basic_awayabsent
        with charachange

        rin "Actually that was not true. About visiting. But Emi doesn't count even if she visits."

        show rinpan basic_deadpan
        with charachange

        rin "She always pampers me too much. I think she's having too much fun."

        show rinpan basic_absent
        with charachange

        rin "I think I've forgot how to put a bra on by myself."

        "She looks groggily down at her chest."

        show rinpan basic_surprised
        with charachange

        rin "Which is probably why I don't have one on, now that I think about it."

        "I haven't failed to notice that Rin doesn't have her shirt buttoned up either, but I try to keep my eyes strictly locked on hers."

        "It's rather evident that she's not a very body-conscious person. My own body, however, is quite conscious of hers right now."

        show rinpan relaxed_sleepy
        with charachange

        rin "She came to wake me up at half past seven today!"

        show rinpan relaxed_doubt
        with charachange

        rin "Can you imagine that?"

        "She pauses for a while and glances up at my dumbfounded face."

        show rinpan basic_lucid
        with charachange

        rin "On second thought, you probably can. It's not like that reverse rainbow fish I tried to imagine earlier. That was hard."

        hi "Well yes, that seems like a pretty normal time to wake up if you want to go to class in the morning."

        "I'm trying to sound as reasonable as possible to counteract Rin's unreasonable annoyance."

        show rinpan basic_deadpanupset
        with charachange

        rin "Told her to sod off."

        show rinpan relaxed_nonchalant
        with charachange

        rin "She gave me these meds and told me to take them."

        "I follow her eyes to the night table and then to the pill bottle sitting on top of it."

        show pills:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0
        with Pause(1.0)

        show pills at truecenter

        "I pick it up and turn it around to look at the label so I can see what kind of medication Emi brought."

        "Active ingredient… codeine?"

        show pills:
            easeout 1.0 ypos 0.7 alpha 0.0
        with Pause(1.0)

        hide pills

        hi "You took all of these?"

        show rinpan relaxed_surprised
        with charachange

        rin "No. Yes. I've been eating some since there's so many of them. Seem to make this thing not so bad."

        show rinpan relaxed_sleepy
        with charachange

        rin "Actually… I think I'm feeling just fine."

        "Her head lolls round and round, making it look like she is either trying to stretch her neck muscles or possibly pass out."

        "She took several of these pills? Can that be safe? At least it's bound to have some side effects… which I'm afraid I am witnessing right now."

        show rinpan basic_deadpanupset
        with charachange

        rin "I am feeling just fine… I am fine… just someone take this buzzing away from my head. I can't think straight."

        "The annoyed expression returns to Rin's face."

        show rinpan basic_upset
        with charachange

        rin "It's like many of those insect things… or one really big insect thing."

        show rinpan basic_awayabsent
        with charachange

        rin "With lots of wings. Very much color and everything."

        show rinpan basic_absent
        with charachange

        rin "What's the word for those?"

        show rinpan basic_deadpanamused
        with charachange

        rin "Oh, never mind. I remembered. It's butterflies."

        "She smiles slightly at her last observation. The small pause in her monologue is not long enough for me to dare saying something that could potentially, but not likely, salvage this discussion."

        show rinpan basic_amused
        with charachange

        rin "I love butterflies. They are the best animal."

        show rinpan basic_awayabsent
        with charachange

        rin "Did you see any on your way here?"

        show rinpan basic_deadpansurprised
        with charachange

        rin "Hisao."

        "She utters my name as an afterthought, possibly to make clear that she is now addressing me instead of just speaking her mind to whoever might be listening."

        "This odd situation has left me speechless more or less since the moment Rin first opened her mouth. Now that she herself doesn't seem to have anything else to add, silence fills the small room."

        "It makes me glance around again in an attempt to find something to talk about."

        "Rin's room is about as small as mine. The big window, which takes up most of the wall furthest from the door, opens to the east just like mine."

        "It looks very normal, which strikes me as strange. I expected something more… different."

        "About a dozen paintings - most of them in Rin's signature abstract style - and a few art posters are taking up almost all of the available wall space, but that's about the only real difference between her room and mine."

        "The room is not exactly ascetic, but it doesn't look like what I'd expected from a girl's room, either."

        "A faint smell of art… of paint and paper is floating in the air. It's the same smell the art room has."

        "Rin isn't too concerned about being tidy, it seems; everything she owns seems to be arranged in various piles around her room."

        hi "Your room looks nice."

        "It's an empty sentence one uses to fill empty spaces in conversations, but my wits are failing me pretty hard right now."

        show rinpan relaxed_nonchalant
        with charachange

        rin "Yeah. Would you like me to show you the places?"

        "She looks down at her half-open shirt quizzically, making me inadvertently follow her gaze to her chest."

        show rinpan relaxed_sleepy
        with charachange

        rin "Oh… I guess I already did."

        "I can't deny that, no matter how hard I tried to act properly."

        show rinpan basic_absent
        with charachange

        rin "It is very nice that you came to see me."

        show rinpan basic_deadpancontemplation
        with charachange

        rin "It makes me feel very… what's that word… you know, the one about things and stuff."

        show rinpan basic_lucid
        with charachange

        rin "Anyway, you came."

        "Rin's rambling makes me remember that I actually came here for a reason."

        hi "Hey, about what we talked on Monday. On the rooftop, remember?"

        stop music fadeout 4.0

        show rinpan relaxed_surprised
        with charachange

        rin "Hmmm?"

        "Rin doesn't seem to be exactly attentive right now, not that she ever is. I plow ahead and get it off my chest anyway."

        hi "I just wanted to tell you that I'm going to be better from now on, I guess."

        hi "I hate being pathetic, so I decided that I'm not going to be, any more."

        hi "I guess… that's all."

        show rinpan relaxed_sleepy
        with charachange

        rin "Okay. Isn't that good?"

        "The blurry words flow out of her lips slowly and uncontrollably."

        show rinpan relaxed_nonchalant
        with charachange

        rin "I'm happy for you I think. That's what I think."

        show rinpan basic_deadpannormal
        with charachange

        rin "You shouldn't look so sad all the time. I mean, looking sad is fine if you are not sad, but you look sad like you actually sad."

        show rinpan basic_deadpan
        with charachange

        rin "That's no good."

        show rinpan basic_awayabsent
        with charachange

        play music music_rin fadein 0.5

        rin "Are you going on some training camp where they make men out of boys? Or mountaintop meditation?"

        hi "No, I don't think so."

        show rinpan basic_absent
        with charachange

        rin "Oh. I guess that's fine too."

        "The sentences come out of her mouth, and probably her brain, one at a time with a small pause between each, making her gibberish hard to understand."

        show rinpan relaxed_doubt
        with charachange

        rin "I just think it seemed like a good idea. Maybe it's not."

        "Rin finishes with one more line, getting to say the last word over herself, an impressive display of what I can only describe as mental shadowboxing."

        hi "While I'm embarrassing myself, might as well tell you that I'm sorry that I said some stupid things to you last week."

        hi "It's your own business to decide what you're going to do."

        show rinpan basic_absent
        with charachange

        "She seems to not register my words first, but then understanding lights in her eyes and she waves her head around in a way that could be interpreted as anything."

        show rinpan basic_deadpancontemplation
        with charachange

        rin "It's OK."

        show rinpan basic_lucid
        with charachange

        rin "I probably said stupid things too."

        rin "It's just sometimes a bit hard to keep my thoughts the way I like them."

        show rinpan relaxed_nonchalant
        with charachange

        rin "They are not very straight, at least most of the time."

        rin "Not that I want to have them straight… I just wish they were at least in some shape."

        rin "Round is fine too. But I need more definition."

        show rinpan relaxed_boredom
        with charachange

        rin "My thoughts are very messy."

        show rinpan relaxed_sleepy
        with charachange

        rin "Messy."

        show rinpan:
            ease 1.0 ypos 1.1 alpha 0.0
        with Pause(1.0)

        play sound sfx_pillow

        scene ev rin_high_frown
        with locationchange

        "She repeats the word melancholically, then flops lying down on her bed and nuzzles her head against her pillow, shutting her eyes."

        rin "Enough. Tired. You should go. I'm going to sleep again."

        scene ev rin_high_oneeye
        with locationchange

        "She opens one of her eyes to look at me."

        rin "Was it you who likes to look at sleeping girls? Or someone else?"

        rin "Maybe there were many of those."

        scene ev rin_high_frown
        with locationchange

        rin "I can't remember."

        rin "You can stay if you want."

        hi "No no, I'll leave. I have to… do homework anyway."

        stop music fadeout 2.0

        scene bg school_dormrin
        with locationchange

        "I stand up from the chair and take a step towards the door."

        rin "Wait."

        "Her request stops me in my tracks, not that I intended to scoot off right away."

        scene ev rin_high_grin
        with locationchange

        "I look over my shoulder at the girl lying on her bed, again with the strangest kind of smile on her features."

        "She should smile more often."

        rin "I can walk you to the door."

        scene ev rin_high_grinwide
        with locationchange

        rin "It's the least a gentleman can do."

        scene ev rin_high_smile
        with locationchange

        "Rin giggles like a little kid, making me beyond absolutely certain that she took far too much of her cold medication today."

        rin "I have always wanted to say that."

        scene bg school_dormrin
        with locationchange

        show rinpan basic_deadpandelight:
            twoleft ypos 1.1 alpha 0.0
            ease 1.0 twoleft alpha 1.0
        with Pause(1.0)

        show rinpan at twoleft

        "Slowly and with difficulty, Rin first rises to a sitting position again, then she stands up with even more difficulty and more slowly still."

        "As if guided by some masculine automation, my eyes instantly lower to the curve of her thighs and the striped panties, at which point my manners force me to lift my gaze back to Rin's eye level."

        "It's getting almost too hard to do that."

        "Rin is standing, although barely. It looks like she has trouble keeping her usually decent balance; again, probably a side effect of the medicine."

        show rinpan basic_deadpandelight_close at center
        with charamovechangefaster

        "She takes an unsteady step towards me, then another smaller one as she notices that it's not a good idea to try to take big steps."

        "I feel my muscles tense as I prepare to catch Rin if she falls down."

        play music music_twinkle fadein 3.0

        scene ev rin_kiss:
            top
            zoom 4.0
            easein 0.4 zoom 1.05
            easein 5.0 zoom 1.0
        with flash

        "She manages to take two more steps before she falls against me. To my surprise, neither her downwards momentum nor our slight height difference are able to stop Rin from pressing her heart-shaped lips squarely against mine."

        "As our lips part after a confusing moment of nothing but the taste of… Rin, I look down at her, trying to find some explanation for this bewildering event."

        $ renpy.music.set_volume(0.7, 2.0, channel="music")

        scene bg school_dormrin
        show rinpan basic_deadpandelight_close at center
        with locationchange

        "The euphoric smile of a madman broadens on Rin's lips again and—"

        show rinpan relaxed_sleepy_close
        with charachange

        rin "I wonder if I will remember this tomorrow."

        "I am absolutely stumped on how to respond."

        show rinpan relaxed_sleepy at twoleft
        with charamovechangefaster

        "Rin takes a step backwards, separating her body from mine, and making me only now realize that they were even connected in the first place."

        show rinpan:
            ease 1.0 ypos 1.1 alpha 0.0
        with Pause(1.0)

        hide rinpan

        play sound sfx_pillow

        "The second step is actually a fall backwards, luckily straight onto her bed."

        "The soft thud Rin's thin body makes against the mattress breaks the silence."

        scene ev rin_high_open
        with locationchange

        "I move quickly over to her to see if she hurt herself, only to be met with the peaceful face of dreaming."

        "Rin sleeps."

        "She is lying diagonally across the bed, somehow managing to have simultaneously fallen asleep while standing up, and fallen down in a way that she didn't injure herself."

        "Fool's luck."

        scene ev rin_high_sleep
        with locationchange

        "I tuck Rin in, covering her with the sheets as well as I can."

        "She feels very light, even though I am not that strong."

        show ev rin_high_sleep:
            right
            ease 10.0 zoom 1.1

        "I stand up to look at her, the oval-shaped face, the dark eyelashes shut against the feverish cheeks, the slender body covered with the pale sheets."

        "Rin sleeps."

        "A conflict - no. Conflicts, plural, churn inside of me. I think about calling a nurse to keep an eye on her, but decide against it. After taking one more glance at her peaceful face, I decide that she'll be fine."

        "I do pocket the remaining pills, though."

        stop music fadeout 5.0

        scene bg school_girlsdormhall
        with locationchange

        "I exit the room, and close the door soundlessly behind me."

        "I exhale deeply, only now realizing I had held my breath for the better part of a minute. Taking a moment to relax, I try to calm down my heart, racing like a jackrabbit."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .dandelions:
        scene black
        with dissolve

        play music music_pearly fadein 1.0

        scene bg school_dormhisao
        with openeye

        "I had trouble getting to sleep that night, so the next morning finds me exceptionally groggy. I briefly consider skipping class but remind myself that I was supposed to be a stronger person now."

        scene bg school_courtyard
        with locationskip

        "I get up like a good boy and put on my uniform, then make my way to the main school building without eating breakfast."

        scene bg school_scienceroom
        with locationskip

        "I sit in my seat in classroom 3-3, waving a greeting to Misha and Shizune like I do every morning, and let the day wash over me."

        with shorttimeskip

        "The afternoon classes are always longer than those in the morning. This is true regardless of whether I count it by the minute or by the number of doodles drawn in my notebooks."

        "Today I'm especially distracted, as I keep thinking about Rin."

        $ renpy.music.set_volume(0.5, 0.5, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=150}Did I manage to properly tell her that I want to get better? Did she understand a word of what I was saying?"

        n "I think about the kiss we shared and what it means. She was so out of her mind, maybe it means nothing. But we've been getting closer lately. What does that mean?"

        n "{vspace=150}I think about Rin more and more nowadays. I wonder if she thinks about me."

        $ renpy.music.set_volume(1.0, 4.0, channel="music")
        play sound sfx_normalbell
        nvl clear
        nvl hide dissolve

        "The ringing of bells makes me flinch, and then realize that I haven't been paying attention during the latter half of class at all."

        "I look at the assortment of sketches traveling up and down the margins of my notebook, the only thing I got done in the last hour."

        "Feeling vaguely disappointed in myself, I pack up and get to the hallway."

        stop sound fadeout 0.5
        $ renpy.music.set_volume(0.0, 1.0, channel="music")
        scene bg school_hallway3
        show rin basic_absent at center
        with locationchange

        "Rin is standing right outside the door, her presence stopping me in my tracks as soon as I spot her."

        "Her posture is relaxed as always, but I suddenly feel like I just ate a crowbar. I'm having a hard time meeting her gaze."

        "She doesn't seem to have any trouble looking at me, but those dark eyes are making me feel flustered for no reason."

        "It's hard to look straight at her so I turn my face away a little."

        "I don't know what one should say in this kind of situation."

        "Then again, I rarely know what to say to Rin in any given situation."

        $ renpy.music.set_volume(1.0, 8.0, channel="music")

        hi "Err… hi."

        show rin basic_deadpan
        with charachange

        rin "Hello."

        "I try to get rid of the awkwardness in my voice and invoke a more natural way of speaking. I suddenly worry about where I should put my hands; it feels like they're in the way somehow."

        hi "How are you feeling? You were pretty out of it yesterday."

        show rin basic_awayabsent
        with charachange

        rin "I'm okay. What do you mean yesterday?"

        hi "You don't remember?"

        show rin relaxed_disgust
        with charachange

        "She tilts her head to the side like a bird, looking somewhat confused."

        rin "Remember what? I have a pretty bad memory."

        hi "About yesterday."

        show rin relaxed_surprised
        with charachange

        rin "What about yesterday?"

        hi "I came to see you and…"

        show rin relaxed_nonchalant
        with charachange

        rin "I don't remember that kind of thing happening."

        "She really doesn't remember? I don't know if this is a good thing or a bad thing, but I feel disheartened all the same."

        show rin basic_lucid
        with charachange

        rin "I remember that I promised to show you one place, though. Did that happen for real?"

        show rin basic_awayabsent
        with charachange

        rin "Maybe I just think that I remember that and I really don't."

        hi "No, that was real too."

        show rin basic_absent
        with charachange

        rin "Okay. Do you want to go?"

        hi "Now?"

        show rin basic_deadpannormal
        with charachange

        rin "Yeah."

        hi "Well, sure, why not. Is it far?"

        show rin basic_deadpan
        with charachange

        rin "It's not."

        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
        $ renpy.music.set_volume(0.8, 0.5, channel="music")
        play ambient sfx_parkambience fadein 0.5

        scene bg school_courtyard
        with locationskip

        "Together, we walk downstairs and then outside. The usual summer day, whirring cicadas and all, greets us. It's immensely hot, and without the air conditioning the classrooms offer, I start sweating immediately."

        scene bg school_gardens
        with locationchange

        "We start along the tree-lined pathway that leads towards the dorms."

        "The cherry trees offer shade, with the sunlight blinking through the holes in the canopy. The light creates a chaotic pattern of shadows dappled with bright places where the beams hit the pavement."

        "Rin's eyes are wandering in every direction but mine. I get the feeling that it's intentional."

        $ renpy.music.set_volume(0.7, 0.5, channel="ambient")
        $ renpy.music.set_volume(0.6, 0.5, channel="music")

        scene bg school_forest1
        with locationskip

        "She leads me to the back gate once again, taking us through it and into the forest beyond. As before, the dropping temperature and the drastically reduced levels of light make it feel like the forest is swallowing us into its cavernous belly."

        scene bg school_forest2
        with locationchange

        "We head uphill along the same path as last time, snaking around trees and boulders, over roots and rocks, past wild undergrowth. Birds sing somewhere in the woods, soloists for the humming background music of the treetops."

        scene bg school_forestclearing
        with locationchange

        "We go past the small clearing with the big maple that is now called the Worry Tree. The climb steepens, then becomes easier again."

        scene bg school_forest2
        with locationchange

        "I have to stop a few times to catch my breath, then hurry after Rin who doesn't stop to wait for me."

        "Soon, I'm out of breath again."

        $ renpy.music.set_volume(1.0, 0.5, channel="ambient")
        $ renpy.music.set_volume(0.4, 0.5, channel="music")

        scene bg school_hilltop_border
        with locationchange

        "Suddenly the trees end, and we emerge from the forest. The boundary of the woods is sharp and abrupt, as though a line had been drawn to mark it."

        "The hill continues to climb up a little further ahead, but from here to the top it's a rocky meadow, patches of grass and small bushes that look like they are growing straight from the rock."

        $ renpy.music.set_volume(1.5, 0.5, channel="ambient")
        stop music fadeout 2.0
        $ renpy.music.set_volume(1.0, 10.0, channel="music")

        scene bg school_hilltop_spring:
            xalign 0.0
            warp acdc_warp 15.0 xalign 1.0
        with locationchange

        "We soon reach the highest point, with the forest behind us and the view to every direction opening in front of our eyes."

        "The city lies far below and away, lazily reveling in the quiet afternoon mood."

        "You can see pretty far from here, and the vista is beautiful. I wonder how high up we are."

        "I breathe the fresh air and feel my heart rate slowly going back down. I think I might've overdone it a bit; a higher pulse is dangerous for me. I'm feeling fine right now, though."

        "The wind picks up, ruffling my hair and causing the trees below us to sway. It makes the grass undulate in waves as the breeze sweeps across the hilltop."

        "Sun shines from the open skies upon us, a few clouds passing by to shadow it. What was painful heat before is now gentle warmth."

        "I take a good look around. The hilltop is pretty in the way nature often is, unplanned harmony found in the natural arrangement of things."

        "The most striking feature is the abundance of small yellow flowers. They're literally everywhere in this small meadow. I can't help commenting on it."

        hi "Wow. A lot of flowers."

        show bg at right
        show rin basic_absent at center
        with charaenter

        rin "Yeah. Do you know this kind? They will fly away."

        hi "Yeah. Dandelions."

        show rin basic_awayabsent
        with charachange

        rin "There are not many of them at the school, because they cut the grass so often. Nobody cuts grass up here."

        "The fragile-looking flowers will soon turn white and fluffy like cotton, and the wind will carry their seeds away."

        $ renpy.music.set_volume(1.0, 0.5, channel="ambient")

        scene ev dandelion:
            truecenter
            ease 20.0 zoom 1.1
        with locationchange

        "I crouch down to look at one tiny yellow flower, silently basking in the sunlight. There's not a hint of white yet, so it's still waiting for its time to be fulfilled."

        "I brush my fingers against the delicate yellow petals, feel the soft texture in my fingertips. It feels nostalgic somehow. I hear Rin approaching from behind and stand back up to face her."

        stop ambient fadeout 3.0

        scene bg school_hilltop_spring at left
        show rin basic_sad at center
        with locationchange

        "She has a weird look on her face."

        hi "Something on your mind?"

        show rin basic_upset
        with charachange

        rin "I don't know. It's just…"

        play music music_rin fadein 0.5

        rinbabble "You just look so sad all the time and become upset so easily and it makes me confused and I really don't remember much about yesterday except that you came to my room and that's why it might be because of me so if it's because of me I think that I know why, it's because people don't really like talking to me and you might be the same and that would be sad I know that people and I'm talking about others than Emi too always say that I'm strange and that I talk strange things so I thought I'd try not to say strange things but that just makes me think more and new and strange and colorful that was not a good word but maybe you understand anyway and odd things so if I want to say something I don't really know how and then the words are not the same as the thoughts because something goes wrong on the way out but it's not like the thoughts are really the thing I should be saying it's more like the idea of the thought or the feeling of the idea or the idea of the feeling but it's not really any of those either because there is no word for it unless I invent a new one which is not really useful so I've been thinking if doing things is better than saying so maybe because yesterday I took those pills and I was feeling a little strange I might have done something that I shouldn't besides I don't even know if it would be any better if I just could say the thought there is no telepathy that's real telepathy isn't there I think it'd be terrible and useful at the same time but right now I wouldn't mind because misunderstanding is so easy but understanding is not and I thought—"

        stop music
        play sound sfx_pillow
        with vpunch

        "I grasp her shoulder and squeeze hard to make her stop. I don't have the capacity to take all that in at once."

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")

        show rin basic_surprised
        with charachange

        "Rin shuts up instantly."

        hi "Take a breath."

        hi "I'm not upset. Why would I be? I'm just a little confused, but it's all right."

        "I wonder if I was making a face she doesn't like again. I guess I've been thinking about yesterday all the time. Maybe I looked weird. I wish I had a mirror with me at all times."

        hi "No need to get it all said at once. I'll listen, even if you talk slower."

        show rin basic_deadpanupset
        with charachange

        rin "It just came out. Sorry. I'm okay now. I just wanted to say something. I didn't mean that much."

        play music music_innocence fadein 10.0

        show rin negative_worried
        with charachange

        rin "It's weird, isn't it?"

        "She looks at me with a surprisingly timid expression, one that I haven't seen before. I can't help but laugh a little."

        hi "Yeah. It's weird."

        hi "You are a pretty weird person but there's nothing wrong with that."

        hi "Thanks for being worried about me, but I'm going to get better. I told you that yesterday, but I guess you don't remember that either."

        show rin relaxed_nonchalant
        with charachange

        rin "I don't. I wonder what else I forgot. Hopefully nothing important like my own name. That'd be terrible."

        hi "Well, you kissed me."

        show rin relaxed_surprised
        with charachange

        rin "I did?"

        hi "Yeah, you did. On the lips."

        "I try to sound as matter-of-fact as I can, but I worry that I might be blushing again."

        show rin relaxed_doubt
        with charachange

        rin "Did you kick me?"

        hi "No! Why would I do that?"

        show rin basic_deadpancontemplation
        with charachange

        rin "Then it's all good, right? It's okay, right? I didn't forget my name."

        hi "Yeah, it's okay."

        "I wish I was more suave so that I could come up with a better follow-up to that, but nothing comes to mind. It's a good thing that Rin has more to say. It makes me feel relieved somehow."

        show rin negative_confused
        with charachange

        rin "I think I should say sorry. I'm really bad with people."

        show rin negative_spaciness
        with charachange

        rin "Some things are hard to understand - like jellyfish. Do you understand jellyfish?"

        hi "I… I guess not."

        show rin negative_sad
        with charachange

        rin "People are like jellyfish to me. I don't understand."

        "Now it's her turn to make a face I don't really like seeing."

        show rin basic_sad
        with charachange

        menu:
            with menueffect
            rin "I've never really had friends."

            "What about me?" if True:
                $ what_about_emi = False

                call a2rc5o1
            "What about Emi?" if True:
                $ what_about_emi = True

                call a2rc5o2

        show rin basic_deadpanamused
        with charachange

        rin "It's really nice of you to say that."

        show rin basic_awayabsent
        with charachange

        rin "I have always been able to tell everything to pencils and paints and paper. They are my best friends."

        show rin basic_lucid
        with charachange

        rin "It is harder with people. I have to use words, that is hard for me."

        hi "Yeah I know, you told me. About how you forget."

        show rin basic_absent
        with charachange

        "Rin nods at me wordlessly and I dare to attempt showing her a little, encouraging smile. I hope I do it properly. She doesn't reply in any way."

        "I feel really glad. The distance Rin puts between herself and everything else has made me feel really uneasy ever since I met her. If we become real friends, I'm sure I could understand her more."

        "I'm sure that this way, we can close the gap of understanding between us."

        show rin basic_awayabsent
        with charachange

        "My thoughts don't transmit to Rin. She seems lost deep in thought, wandering amidst the sea of yellow flowers covering the grassy hilltop. It's just as well."

        $ renpy.music.set_volume(0.4, 2.0, channel="music")
        play ambient sfx_parkambience fadein 7.0

        scene bg school_hilltop_spring_ss at left
        with shorttimeskip

        "Time passes, the breeze making the taller grass sway gently in time with the wind. Rin hums a little song to herself so quietly that I can't tell what it is, if it's even anything at all."

        "A stronger gust sweeps over the hilltop, and the sound of the trees in the wind buries the song away."

        "I check my watch, more out of habit more than anything else. It's 4:30 right now, on this Saturday afternoon."

        show rin basic_awayabsent_ss at center
        with charaenter

        "Rin looks into the distant horizon with that odd, blank stare of hers, as if she were looking at nothing at all. Her pupils are dark and quiet like a pair of deep, still ponds."

        $ renpy.music.set_volume(0.7, 6.0, channel="music")

        if believes_in_rin or _in_replay:
            hi "I think I'm going to quit the art club. I realized it when we had that argument last week."

            hi "It was a good thing I tried it, but it's just not my thing, you know? I had more fun getting to know you than actually doing the art stuff in there."

            hi "But I want to stay as your friend. Would that be all right?"

            show rin basic_deadpan_ss
            with charachange

            rin "Sure. It was getting pretty creepy anyway with you staring at me all the time."

            "Her comment makes me fluster immediately, but I manage a reply."

            hi "Sorry about that."

            show rin basic_deadpandelight_ss
            with charachange

            rin "It's okay, I'm used to it. You're not the first person who likes to see me paint."

            show rin basic_absent_ss
            with charachange

            rin "Are you going to do some other thing?"

            hi "I don't know. Probably not."

        show rin relaxed_doubt_ss
        with charachange

        rin "You are going to become better, right?"

        hi "Sure."

        show rin relaxed_nonchalant_ss
        with charachange

        rin "Me too, you know. I'm going to talk to that friend of the teacher and ask her to put my stuff in her place and work hard to get all that done."

        show rin basic_lucid_ss
        with charachange

        rin "I decided that just now, you know. But I think I knew it all along."

        show rin basic_deadpannormal_ss
        with charachange

        rin "I've had this feeling for a long time now, that I am going to change. Even if I hate it and don't want it, even if I wanted to, I would change."

        show rin basic_deadpanupset_ss
        with charachange

        rin "Like I am not enough the way I am. I think this could be a good way to do it because it's like a straight line."

        show rin basic_deadpancontemplation_ss
        with charachange

        rin "Like I've learned all the things in my life so far just for this. It's just art, and it's the only thing I really know. I know what I'm going to do, so it's good. I'm not afraid at all."

        show rin basic_deadpansurprised_ss
        with charachange

        rin "I feel like I always do. Is that weird?"

        hi "No. Not at all."

        stop ambient fadeout 2.0
        $ renpy.music.set_volume(1.4, 4.0, channel="music")

        scene black
        with shuteye

        "I close my eyes, and give in to the irresistible sensation that has been growing inside me all week long."

        "I float up, towards the surface of my own life."

        "The pressure of being underwater slowly diminishes, the weightless sensation becomes stronger."

        "I break the surface of the water, lifting my head into the sunlight and inhale deeply, breathing in fresh air as if for the first time in a long, long while."

        scene bg school_hilltop_spring_ss at left
        show rin basic_deadpandelight_close_ss at center
        with openeye

        "My lungs fill with oxygen, and I open my eyes to see Rin's peaceful, determined face."

        stop music fadeout 10.0
        $ renpy.music.set_volume(1.0, 2.0, channel="music")

        scene bg school_hilltop_border_ss
        with shorttimeskip

        "We walk down the slope carefully and slowly to avoid falling down, Rin in the lead and me a few steps behind."

        "Rin surely can do this. Even if she can't, she's going to pull through."

        "I'm sure that I can keep my head above water too, from now on."

        "The sun sets behind our backs, setting the world ablaze in its orange glow."

        "I keep watching the back of the red-headed girl descending the path a few steps ahead of me."

        "If it's only this much… this distance between us is definitely within my reach."

        if _in_replay:
            return

    return

label a2rc1o1:
    hi "Wow, you're amazing."

    rin "It's not that amazing."

    rin "But thanks."

    return

label a2rc1o2:
    hi "Wow, I wish I was that good. I kind of embarrass myself."

    rin "Wouldn't you have to be me to be as good as me? I don't think you'd want to be me."

    hi "No, I guess not. Maybe just some sort of approximation then."

    return

label a2rc2o1:
    hi "Sure, there were some people like this in my old school, too, but not as many. And it feels more intense, somehow."

    hi "I think, if I had to pin it down to one thing, that the students here really appreciate going to school."

    return

label a2rc2o2:
    hi "I feel like I need to start moving in some direction, too. That's how this school makes me feel."

    return

label a2rc3o1:
    $ renpy.music.set_volume(0.5, 0.5, channel="ambient")

    "Rin could probably do it. Even though she seems to doubt herself, I have no doubts about her strength."

    "She could do it, even if she can't."

    return

label a2rc3o2:
    $ renpy.music.set_volume(0.5, 0.5, channel="ambient")

    "Emi probably has done it. She's so happy and energetic, a runner girl without legs."

    "If anyone has 'beaten' a disability, it must be her."

    return

label a2rc4o1:
    hi "I think you'd be super popular. I mean, your paintings are really amazing."

    hi "And you paint with your feet; that's really cool, too. I bet people will be amazed."

    show rin basic_deadpanupset_close
    with charachange

    rin "It's not a big deal. I would paint with hands if I had any."

    hi "Oh… sorry. I'm sorry, I didn't mean it like that."

    show rin negative_confused_close
    with charachange

    "Rin turns away, looking at her painting wistfully. I want to take back what I said if it was what made her make that face."

    rin "I get it."

    return

label a2rc4o2:
    hi "You'd be letting your talent go to waste if you don't."

    show rin basic_surprised_close
    with charachange

    rin "Go where?"

    hi "To waste. I think it'd be a waste for other people to not see these things."

    "I try to press her a little bit, to extract some sort of decisiveness out of her, but Nomiya decides to intervene."

    show nomiya smile
    show rin basic_awayabsent_close
    with charachange

    no "Oh, it's not that bad."

    show nomiya talk
    with charachange

    no "I agree that it's important to strike when the iron is hot, but Tezuka is still just eighteen. She'll have time and her abilities will mature."

    show nomiya veryhappy
    with charachange

    no "That said, there are many advantages for trying to make a break at a young age, if at all possible."

    show rin basic_absent_close
    with charachange

    hi "Yeah, but…"

    return

label a2rc4o3:
    hi "I mean, the teacher is probably right. You're not going to get a chance like this again."

    hi "People don't get many chances in life, and you shouldn't waste any of them even if you have doubts."

    show rin basic_absent_close
    with charachange

    "Rin stares at me unresponsively. It's like my words don't have any meaning to her at all."

    return

label a2rc4o4:
    hi "Don't you think it would be exciting? I'd be wild about something like this."

    show nomiya talk
    with charachange

    no "Hahaha, so would I. But this is about things like your career and future, rather than a youthful adventure. Although there's nothing wrong with enjoying oneself."

    "Nomiya gently reprimands my excitement, but I'm not going to let it go."

    hi "Seriously, everyday life is so dull, you always do the same things every day, in the same way. This would be something else."

    return

label a2rc4o5:
    hi "This isn't like you. You told me that people should do things they can't, just because they can."

    hi "And now you're being all wishy-washy yourself about something this important."

    return

label a2rc4o6:
    hi "I really think you should aim higher. You should take the chance."

    hi "Even if you crash and burn, at least you tried. It'd be worth it just for that."

    "Nomiya sucks in his breath then lets it out after a pause, as if he wants to add something, but he manages to restrain himself. Rin finally replies to me."

    show rin basic_surprised_close
    with charachange

    rin "You don't think I'm good enough like this?"

    hi "No. I think that you're selling yourself short if you think like that. It's cowardly."

    return

label a2rc5o1:
    hi "Nah. I'm your friend, for one."

    hi "I mean, think about it. We already talk a lot to each other, and we've even gotten upset at each other and then forgiven the other for it."

    hi "That's what they call friendship."

    return

label a2rc5o2:
    hi "What about Emi?"

    show rin basic_surprised
    with charachange

    "She pauses for a while, as if having to consider the possibility came unexpected to her."

    show rin basic_awayabsent
    with charachange

    rin "Emi… takes care of me. I don't really know why."

    show rin negative_annoyed
    with charachange

    rin "But I can't really talk to her, not in that way. It's like her head is made of soap foam and marshmallows. Or maybe it's just me. I like her though."

    hi "She's really nice, isn't she?"

    show rin basic_absent
    with charachange

    rin "Yeah."

    hi "I want to be your friend too."

    hi "I'll listen to you if you want to talk. If you don't, then I can just sit quietly next to you."

    hi "And I want to tell you about what I think too. It goes both ways."

    hi "We should definitely be friends."

    return
