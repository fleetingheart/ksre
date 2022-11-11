# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a2_shizune:
    label .message_passing:
        scene bg school_dormhisao
        with locationchange

        pause 1.0

        nvl clear

        nvl show dissolve

        play music music_dreamy fadein 5.0

        n "{vspace=60}The next morning, I recall what a perfect night last night was. So much so that I can't stop thinking about it."

        n "It's probably not the most appropriate time to reminisce, since I have a test first period."

        n "Ah, it's so unfair. How can they do this? They hold a festival that is the culmination of what has to be at least a few weeks' worth of work on a Sunday, and then follow up with exams starting the very next morning?"

        n "It's got to be some kind of sick joke."

        n "I'm not too worried about it, but I wonder if they really couldn't have held off on this for at least another week."

        n "{vspace=60}Well, at least the weather this morning is nice enough that I can study outside before class."

        nvl hide dissolve

        scene bg school_courtyard
        with locationskip

        nvl clear

        nvl show dissolve

        n "{vspace=60}It's a lot more refreshing out here than it would be in the classroom. Not to mention with how quiet it is, I'm starting to think that everyone else will be sleeping in pretty late today."

        n "I put down the notes I'm reviewing for a second and stare out at the school grounds, still littered with festival stalls."

        n "Looking at them now in the daytime, without paper lanterns or crowds of people to draw my attention away from them, I notice something peculiar."

        n "A lot of the stalls that Shizune, Misha, and I visited last night also happen to be ones that we worked on."

        n "{vspace=30}…"

        n "{vspace=30}That's cute. Did Shizune come up with this? It had to be intentional, especially knowing her. Did she hope that I would catch on and see the fruit of our labors?"

        play sound sfx_footsteps_soft fadein 5.0
        stop music fadeout 4.0

        nvl hide dissolve

        show shizu basic_normal at center
        with charaenter

        "I hear footsteps crunching the grass behind me and turn around. I feel slightly paranoid, but all I find is Shizune standing there with an innocuous look on her face."

        play music music_shizune fadein 1.0

        show shizu adjust_happy
        with charachange

        shi "…"

        hi "Good morning."

        "Why do I keep forgetting that she can't hear me?"

        "It's probably because I've gotten so used to Misha translating for both of us that I haven't actually run into many situations where I was forced to acknowledge Shizune's deafness and the problems that could stem from it."

        "I think yesterday was the first."

        "I give her a wave anyway. I can do at least this much, but I'm not even going to pretend for a minute that I could hold up a conversation with her, considering my ignorance of sign language."

        "Would it be rude to just go back to my notes? I don't really know what else I could do."

        hi "Where's Misha?"

        show shizu behind_blank
        with charachange

        shi "…"

        hi "Not just because I can't understand you. You two are always together anyway, so I'm not used to seeing you apart."

        "I know it's silly but for some reason talking to her makes me feel less awkward."

        show shizu basic_normal2
        with charachangealways

        show shizu adjust_happy
        with charachangealways

        show shizu behind_blank
        with charachangealways

        "Surprisingly, she doesn't get mad at all. She starts signing; but it's different than usual. Shizune's hands move more slowly, and the gestures are simpler."

        "I quickly realize that this isn't sign language at all, but she's still attempting to communicate with me."

        hi "So is this the sign language equivalent of breaking it down into layman's terms?"

        show shizu behind_frown
        with charachange

        "I'm terrified that if I attempt to gesticulate back, I'd just look like a total dumbass. The look on Shizune's face tells me that she is starting to think that trying to have any kind of back and forth like this is not exactly the best way to accomplish things."

        "There has to be a better way."

        "Writing on a pad? Well, I do have paper and a pencil. What else, though?"

        "Cell phones? I don't really have much use for mine here, so I barely carry it around, and I don't know if Shizune even has one."

        show shizu adjust_happy
        with charachangealways

        show shizu basic_normal
        with charachangealways

        "She takes the initiative, holding up a finger to ask for a pause before pulling out a pad and pen from her bag and writing a single word on it:"

        call screen written_note(_("Hello."))

        show shizu basic_normal2
        with charachange

        shi "…"

        "I stare blankly at her and receive a similar but somehow more intimidating stare in response. She nudges the pad in my direction forcefully, clearly wanting me to reply."

        call screen written_note(_("Good morning."))

        show shizu behind_smile
        with charachange

        "Shizune beams with a disproportionate amount of happiness. She starts twirling her pen triumphantly as she thinks about where to go from here."

        hi "Oh, come on, it's not like we just invented fire."

        show shizu basic_frown
        with charachange

        "Shizune pushes up her glasses curtly, as if she had heard me, and then starts writing at a furious pace."

        call screen written_note(_("Use the notepad! Write write write write write write write write write write write write write write write write write write write write write!"))

        "I'm confused; am I supposed to take it from her and write 'okay' now?"

        "This is about the furthest thing I could imagine from a smooth, flowing conversation. It makes me envy the ease with which Misha is able to communicate with Shizune."

        show shizu behind_blank
        with charachange

        call screen written_note(_("Are you studying for the test?"))

        "I'm pretty sure I can get away with answering simple yes or no questions like this with nods."

        show shizu adjust_smug
        with charachange

        call screen written_note(_("You are here very early; most people sleep in late after the festival. That means you are abnormal."))

        "…Is that so?"

        call screen written_note(_("You're here too."))

        "Before handing that response back to her, though, I remember what I'd noticed earlier, and add:"

        call screen written_note(_("You're here too.\n\nYesterday was fun. I noticed today that I built a lot of the stalls we went to. Maybe that's why they were so familiar. Was this another game?"))

        show shizu behind_frown
        with charachange

        "She shakes her head from side to side indignantly."

        call screen written_note(_("No tricks."))

        show shizu basic_normal2
        with charachange

        call screen written_note(_("I thought that because you had made those stalls, they were the most important ones. We had to visit them, because everyone should be able to appreciate the fruit of their labors. I wanted you to be able to see and enjoy what you had done."))

        "I'm sort of touched. Still, I have to wonder why she would go so out of her way, and I ask as much in my response."

        show shizu behind_blank
        with charachange

        stop music fadeout 3.0

        call screen written_note(_("Because you were depressed."))

        "I want to say that I was depressed for days, but stop. It's true, I was moping quite a bit, and not being too subtle about it half the time, either, so it's possible that she knew. Was everything she did just to cheer me up, then?"

        hi "Thanks."

        "I mumble it before I can catch myself, but Shizune doesn't seem to care. I write it down instead, and she nods once, as if unused to it."

        "The silence between us grows more vast with each passing second, and there's nothing I can do to break it. Having to write everything down on paper kind of destroys any hope of trying to be casual."

        show shizu adjust_happy
        with charachange

        call screen written_note(_("Good luck on the exam."))

        "Shizune pushes the pad right in front of my eyes, breaking my concentration. Taking the initiative again, as always."

        hide shizu
        with charaexit

        "As she walks into the school building, I can't help feeling a little sad."

        nvl clear

        nvl show dissolve

        n "{vspace=60}That felt like the longest twenty minutes of my life, and all because it's so alien to me to have a face-to-face conversation with someone by passing notes to each other that I can't help coming up blank most of the time."

        n "It makes me want to learn sign language."

        n "That's easier said than done. Although in a school like Yamaku, they might very well have sign language classes. In that case, there would be little reason not to pursue this."

        n "The only person who I can think to ask, at the moment, is Misha."

        n "How badly do I want to know this? There's two options: Wait until after class, or go look for her now."

        n "I guess I'll go now, but I'm not certain where she is. My best bet would be to start searching for her in the girls' dorm, though. After all, if she wasn't with Shizune, that's probably the only place where she would be."

        nvl hide dissolve

        nvl clear

        scene bg school_dormext_full
        with locationchange

        $ renpy.music.set_volume(0.5, 0.0, channel="music")
        play music music_daily fadein 1.0

        nvl show dissolve

        n "{vspace=60}A guy casually prowling around the girls' dorm early in the morning is unacceptable, but asking Misha about sign language classes in front of Shizune would be just unthinkable."

        n "She has to come to school sometime. After all, we're in the same class, so she too has to take this test."

        n "If I wait here, I'll be sure to see her sooner or later."

        n "I just hope she doesn't walk past me while I'm flipping through my notes."

        n "{vspace=60}It turns out to be a pretty long wait. As students file into the school, I wonder if Misha is going to be late."

        n "Eventually I catch sight of her. While she bounces across the grounds, it hits me that I'd have to be blind to miss her with her incredibly distinctive hair."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl clear

        nvl hide dissolve

        show misha hips_grin at center
        with charaenter

        mi "Hi, Hicchan~! Good morning~!"

        hi "'Morning."

        "I don't have a lot of time left before class starts, so I cut directly to the chase."

        hi "Hey, can I ask you a question?"

        show misha perky_smile
        with charachange

        mi "A question? Hm~… Okay, Hicchan~! Sure~ sure~! I have time, but only because I'm late!"

        hi "What does that mean?"

        show misha hips_grin
        with charachange

        mi "Haha~. I should have woken up earlier, but I was so tired~… if I had, I would have to study, but since I didn't, it won't hurt~! What is it, Hicchan?"

        hi "Well, there are sign language classes here, right?"

        show misha hips_smile
        with charachange

        mi "Yup~! They're electives! Why do you want to know, Hicchan?"

        "For some reason that question briefly makes me panic."

        hi "No reason. It sounds interesting, but I guess it's too late to sign up now, right?"

        "I'm not exactly being too subtle here, but Misha never seems to pick up on things like that anyway, so I'm probably being more cautious than is necessary."

        show misha sign_smile
        with charachange

        mi "Hm~? Ah, well, Hicchan, I've heard there are fewer and fewer students taking sign language every year. So! If you want to, I'm sure they will let you in~!"

        show misha hips_grin
        with charachange

        mi "Are you thinking of learning sign language, Hicchan?"

        hi "…Yeah."

        show misha perky_smile
        with charachange

        mi "If you learned sign language, Hicchan, that would make Shicchan really happy~. If you want, we can go to the teachers' office after school. They'll probably let you in."

        hi "That would be great."

        hi "Don't tell Shizune that I want to learn it, though."

        show misha perky_confused
        with charachange

        mi "Why not?"

        hi "So it can be a surprise. Besides, it'll look bad if you tell her this morning, and then I find out in the afternoon that I can't take the classes."

        show misha perky_smile
        with charachange

        mi "Aw~. You're right, Hicchan. Still, this will be hard~… It's such good news…"

        hi "I'm in the Student Council, so I might as well try learning it. Even if it's just the basics, it'd be a step up from nothing. Besides, Shizune and I can't keep relaying everything through you as if you were a phone or something, right?"

        "…"

        pause 2.0

        show misha hips_laugh
        with charachange

        mi "Wahaha~!"

        show misha hips_grin
        with charachange

        mi "You're right, Hicchan~!"

        "…"

        stop music fadeout 4.0
        play sound sfx_warningbell

        "The bell rings to signal the start of first period, cutting our conversation short. I guess I'll just ask a teacher after classes are through."

        "Her reaction was a little strange, but I forget about it as the day goes on."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .talk_to_the_hand:
        scene bg school_scienceroom
        with locationchange

        play sound sfx_normalbell

        "The bell rings and the teacher at the front of the room gestures that classes are over for the day."

        play music music_normal fadein 3.0

        "Although getting into this class was surprisingly easy, it's only been a few days and I'm still not used to the experience. The actual signing is easier to pick up than I expected, but most of my classmates are hard of hearing."

        "On top of that, the teacher favors immersion. I haven't heard her speak since I asked if I could take the class. It's an alien concept, and really unnerving."

        scene bg school_hallway3
        with locationchange

        "The moment I step out of the classroom, I hear a familiar laugh explode through the air a short distance to my left."

        show misha hips_grin at center
        with charaenter

        mi "Hi, Hicchan~!"

        "Misha's not in my sign language class, so this is the first time I've seen her in this context. I still don't know whether her not being in my class is good or bad."

        "It would be more interesting with her in it, but the potential for awkward situations would increase drastically."

        hi "Hi."

        show misha sign_smile
        with charachange

        mi "It's a surprise to see you here, Hicchan! …Ah, that's right! You're taking sign language, aren't you~? Right~!"

        show misha perky_smile
        with charachange

        mi "What do you think of it so far, Hicchan?"

        hi "It's not easy to learn a new language, but I think I'm getting the hang of it. Despite how different it is from other languages, it's still easier than English."

        show misha cross_grin
        with charachange

        mi "Haha~! Really, Hicchan?"

        show misha cross_smile
        with charachange

        mi "Hm~… I agree~!"

        "I was just joking, but she's apparently totally serious."

        "I wonder how Misha can effortlessly translate things to me while simultaneously having a conversation with Shizune in a different language like she does."

        "Until now, I've taken for granted how amazing it is."

        "Someone bumps into my shoulder and apologizes. It's getting kind of crowded here, what with it being the end of the day and all."

        hi "I think we should talk somewhere else instead of the hallway. Let's go to the roof or something."

        show misha sign_smile
        with charachange

        mi "Okay~!"

        "I decide to continue talking on the way. It's surprisingly quiet enough to carry on a conversation while doing so."

        $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
        play ambient sfx_rooftop fadein 1.0

        scene bg school_staircase1
        with locationchange

        stop music fadeout 5.0

        hi "It's still taking me some time to get used to having to look at the teacher constantly. I guess I took all those years of simply listening to the lectures while I doodled for granted. It makes taking notes a lot more difficult, too."

        hi "The introductory class is small, and I'm already behind. I guess I have a lot of stuff to do."

        play sound sfx_door_creak
        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

        scene bg school_roof
        with locationchange

        hi "Yeah, this is much better."

        "I turn around to look back at Misha and see her staring at me with her hands on her hips and her cheeks puffed outwards."

        show misha hips_frown at center
        with charaenter

        play music music_happiness fadein 4.0

        mi "Hicchan, you're behind? That's not good at all!"

        hi "I started the class a week later than everyone else. It's not that bad."

        show misha sign_smile
        with charachange

        mi "Okay, Hicchan, let's review what you learned, then~! I'll tutor you, okay~?"

        "This is the first time I've heard 'I'll tutor you' used outside of dirty movies; I'm not nearly as turned on as I'd have expected."

        hi "I don't know if I need a tutor yet."

        show misha perky_sad
        with charachange

        mi "Aw…"

        "She looks more disappointed than usual. It makes me feel awkward to see her making that kind of face."

        show misha hips_frown
        with charachange

        mi "I want to be a sign language teacher, Hicchan! But~, it would really be great if I could try tutoring someone in it, first. Even if it's for a little while, the experience would be valuable."

        hi "Ah, well, yeah, that's true."

        hi "I didn't know you wanted to be a sign language teacher."

        "It's hard to believe she isn't intentionally trying to make me feel guilty, because she's very good at it."

        "Still, it makes sense. She's very good at sign language already from what I've seen, and certainly has the voice for dealing with the hearing impaired. I never saw her as the teaching type, though."

        show misha hips_grin
        with charachange

        mi "Hahaha~! It's the reason why I wanted to go to this school, Hicchan!"

        show misha sign_smile
        with charachange

        mi "It's also really expensive to attend here, you know. Because I want to be a sign language teacher, I have reduced tuition fees. If it wasn't for that, I don't know if I'd be able to keep going here."

        hi "I see. It's not that I think you would be bad at tutoring, it's just that I don't know if I need it just yet."

        show misha perky_sad
        with charachange

        mi "You're right, Hicchan, you're smart."

        hi "Well, no, that just makes me sound arrogant."

        hi "All right, please tutor me."

        show misha cross_laugh
        with charachange

        mi "Ahahaha~! Really? Okay~! Okay okay okay~! Yay~! Thanks, Hicchan~! I'll do my best!"

        show misha sign_smile
        with charachange

        mi "Let's start right now~!"

        hi "Too soon."

        show misha perky_sad
        with charachange

        "…"

        mi "I miss Shicchan~…"

        hi "Didn't you just see her this morning?"

        show misha sign_smile
        with charachange

        mi "But it's hard to talk to her in class, Hicchan! There's no Student Council today, either~."

        hi "Well, there have been exams all week. I'd be kind of mad if there was still Student Council; I'll be glad when they are over."

        show misha perky_confused
        with charachange

        mi "When it's back, you're not going to skip out, right, Hicchan?"

        hi "Of course. I'm in it, after all."

        hi "Don't worry, I'm not going to just suddenly stop showing up. A promise is a promise."

        "Misha pauses for a second, not looking very convinced."

        show misha sign_smile
        with charachange

        mi "Shicchan takes the Student Council very seriously, Hicchan. Now that you've joined, she works harder than before since she wants to make a good impression."

        show misha hips_frown
        with charachange

        mi "Some other people joined, at first, but they stopped coming soon after. Shicchan tried to get more people interested in the Student Council but wasn't successful."

        show misha perky_sad
        with charachange

        mi "Even when someone would join, they'd stop coming eventually. They'd make excuses and just put it off more and more until they stopped coming altogether."

        show misha sign_smile
        with charachange

        mi "However… I believe that you really mean it, Hicchan."

        "My eyes stay focused on her hands, tilting and moving almost of their own free will, softly signing everything she is saying to herself as she speaks."

        show misha perky_smile
        with charachange

        mi "When you said you would join, she was really happy."

        show misha hips_smile
        with charachange

        mi "Shicchan thinks you're interesting, Hicchan. An uninteresting person won't have the drive needed to join. Even if they do, a person that isn't interesting will quit soon after."

        mi "That's what Shicchan said."

        show misha hips_grin
        with charachange

        mi "So~! It's my duty to make sure you keep going~!"

        hi "Is that why you want to tutor me? You're kind of sneaky."

        show misha cross_laugh
        with charachange

        mi "Really, Hicchan? That's the first time anyone has said that about me~! Wahahaha~!"

        "There's no chance that I would avoid student council work now."

        "Thinking back over the past few days, I've started to realize that the only reason I joined in the first place was because of Shizune; her competitiveness and force of will are alluring."

        "I can't tell Misha that, though."

        show misha sign_smile
        with charachange

        mi "Okay, Hicchan, let's review what you learned in class today~!"

        hi "You don't even know what I learned in class today."

        show misha hips_grin
        with charachange

        mi "Hm~, you're right, Hicchan~! Okay, let's start with the basics, then~! I'll just teach you everything from the beginning~!"

        hi "You're kidding, right?"

        show misha perky_confused
        with charachange

        mi "Huh~?"

        hi "You're serious? That's like, days of lessons, and we're not even learning on the same level…"

        show misha sign_smile
        with charachange

        mi "It's like riding a bike, Hicchan~! You never forget the basics! Wahaha~!"

        show misha sign_confused
        with charachange

        mi "I don't know how to ride a bike, though~…"

        "Oh no."

        show misha hips_grin
        with charachange

        mi "Right, right~. I want to be a teacher one day, so of course I know what I'm doing… Okay~! Okay okay okay~! We're starting~!"

        stop music fadeout 3.0

        show misha perky_confused
        with charachange

        mi "Uh…"

        show misha sign_confused
        with charachange

        mi "…Mmm~…"

        show misha perky_sad
        with charachange

        mi "Ahahaha~…"

        "She looks like she's trying very hard, so this could be bad. Well, learning a language is vastly different from teaching it, and the first step is usually the hardest part. Honestly, I couldn't do any better."

        "Still…"

        show misha sign_confused
        with charachange

        mi "Um… Sign language was formally introduced in the 18th century by a Frenchman named… ah… whose name I can't pronounce, and he started the first public school for the deaf in 1755, but the unwritten history of sign language is said to…"

        show misha sign_sad
        with charachange

        mi "I don't really know where to start. Sorry~… Well~, what better place to start than the history of sign language? Right~? Right~!"

        show misha hips_grin
        with charachange

        mi "No, wait, maybe the alphabet. Okay~, the alphabet it is, then!"

        play music music_another fadein 0.5

        show misha sign_smile
        with charachange

        mi "Okay, Hicchan~! This is pretty basic stuff, although some people think that this is all of signing, and forget there are all kinds of specific gestures and words."

        show misha hips_smile
        with charachange

        mi "Although you can't really get anywhere else without the basics! This is A. Do you see it? Now, you try!"

        hi "I already know this, though."

        "I humor her anyway."

        show misha hips_grin
        with charachange

        mi "Hahaha! Yeah, that's it!"

        show misha sign_smile
        with charachange

        mi "Now, this is B, and this is C."

        "Misha makes one symbol with each hand, without specifying which is which."

        show misha perky_smile
        with charachange

        show misha sign_smile
        with charachange

        show misha hips_grin
        with charachange

        mi "And now D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, VWXY 'n' Z~!"

        "Yeah, this is bad."

        hi "Do you think Shizune wants to do some student council work today anyway? We could go."

        show misha sign_smile
        with charachange

        mi "Of course not, Hicchan~!! Come on, I'll do it again! A, B, C, D, E, F, G, H, I, J, K… Your turn~!"

        hi "So there's really no student council work that needs doing, or anything like that?"

        show misha hips_smile
        with charachange

        mi "What are you talking about, Hicchan? Come on, sign, sign~!"

        hi "Like this?"

        show misha sign_smile
        with charachange

        mi "No, like this!"

        hi "Like…"

        show misha perky_smile
        with charachangealways

        show misha sign_smile
        with charachangealways

        mi "This~!"

        hi "Uh… huh…"

        show misha perky_sad
        with charachange

        mi "I wish Shicchan was here, this would be so much easier with her. Hahaha, that's how sign language is taught most of the time, anyway, with two instructors~! Did you know that, Hicchan?"

        hi "No."

        "I let my brain run through what this would be like if Shizune were here."

        "…"

        show misha hips_frown
        with charachange

        mi "Hicchan~! Are you paying attention?"

        hi "Yeah."

        show misha sign_smile
        with charachange

        mi "Shicchan says that sign language is different from any other, because you have to think about everything before you say it. That means every word has more weight, Hicchan. Every single one is more important than normal."

        show misha cross_smile
        with charachange

        mi "So~, pay attention, please."

        show misha sign_smile
        with charachange

        "She continues her basic rundown of the basics of sign language. Eventually she starts talking about stuff I start to recognize."

        "In the end, I'm impressed. It took a bit of stumbling to get there, but as a teacher, she's pretty good when she's serious."

        stop music fadeout 4.0

        scene bg school_roof_ss
        show misha sign_smile_ss at center
        with shorttimeskip

        "After awhile I start to notice that it's getting late, so I thank Misha, bid her goodbye, and go back to my dorm."

        stop ambient fadeout 1.0

        scene bg school_dormhisao_ss
        with locationskip

        "I learned a lot today."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .chinese_whispers:
        play sound sfx_doorknock

        scene bg school_dormhisao
        with vpunch

        "I'm jolted awake by a thunderous banging sound coming from my door."

        "My first thought is, it could be Shizune. After all, only a deaf person or a jackass would knock that loudly at this hour."

        hi "Who is it?"

        "Of course, if it's Shizune, she wouldn't be able to hear that or answer it."

        "There's no reply, so I'm kind of pleased. I haven't seen Shizune in a while."

        play sound sfx_dooropen

        scene bg school_dormhallway
        show kenji tsun at center
        with locationchange

        play music music_kenji fadein 2.0

        "Opening the door, I find Kenji standing out in the hall, his eyes nervously darting from side to side."

        hi "Oh, it's you."

        show kenji neutral
        with charachange

        ke "Yeah, it's me. What kind of reaction is that?"

        hi "Well, I'd be able to give you a more personalized response if you had answered when I asked who it was."

        show kenji tsun
        with charachange

        "Kenji frowns and pushes up his glasses exactly like Shizune."

        ke "Why are you making that weird face?"

        "I wonder how he's able to see me making a face now, yet wasn't able to the millions of other times I've reacted to something weird he has said or done. I kind of want to pursue this, but am too tired to actually do it."

        hi "Shizune pushes her glasses up just like that. You know, the Student Council president. It's just a little weird."

        show kenji rage
        with charachange

        ke "What the hell? What do you mean there's this girl who does the same thing? You mean she touches her glasses? I do that, that's my thing."

        ke "Who is this bitch? Why are bitches all up in my business, stealing what I do?"

        show kenji tsun
        with charachange

        "His character flips from anger to fear in the blink of an eye."

        ke "Is she trying to replace me? Pod people? No, wait, that's an exact copy. Pod women?"

        ke "It's like my two greatest fears combined."

        show kenji rage
        with charachange

        ke "It is!"

        "I can't believe he has a point…"

        show kenji neutral
        with charachange

        ke "Hey, you going to go into town today?"

        hi "Uh, maybe later."

        show kenji happy
        with charachange

        ke "Okay. Awesome. I have some… stuff I want you to pick up for me at the post office. Some delicate and secret stuff."

        "He speaks in a whisper, as if talking about his mail in even a normal tone of voice will jeopardize it."

        hi "You can have your mail sent directly here, you know."

        show kenji neutral
        with charachange

        ke "No you can't. You can have your mail sent to the school, and then the Student Council picks it up, and then they give it to you. That's not the same as the mail appearing in your hands."

        ke "I don't trust the Student Council. Many dudes don't get their mail here, you know."

        show kenji tsun
        with charachange

        ke "They probably steal it all! They think that just because it's sent to them, they have a license to steal? I can just see them now, elbow deep in mail, fast grabbing all the free swag they can get a hold on. Sickening."

        hi "Where can I find this mailman who can conjure mail out of thin air and into your hands?"

        ke "I don't know, I bet the Student Council killed him to preserve their monopoly on all the students' shit."

        hi "It doesn't work that way."

        hi "Is that what you wanted, though? Fine, I can pick up your mail for you, but eventually I'm going to collect on all these favors. You already owe me some money."

        show kenji neutral
        with charachange

        ke "Thanks for reminding me. I'll pay you back after I get my package."

        ke "Yeah, my bad, I can't really pay you until then. I'm still broke."

        hi "Then I'm basically doing it for money, like a job. Why do you need the package first? Is there money in the package?"

        show kenji happy
        with charachange

        ke "Nah."

        "I am seriously dumbfounded."

        hi "Why can't you get it?"

        show kenji neutral
        with charachange

        ke "Because I am going to remodel my room today into a war room."

        ke "As the days go by, I realize more and more how dangerous feminism is. It really is everywhere, even in places like Iran. You can't tell how far up it goes."

        show kenji tsun
        with charachange

        ke "When the war begins, if we haven't transcended the concept of nations to fight for our genders, it will be chaos."

        ke "No one will know who will take what side, and a war against feminism wouldn't just mean World War III, but the end of all life on Earth as we know it."

        ke "If we lose, all our supple Japanese women will be raped and enslaved by a bunch of sociopathic lesbian supremacists."

        ke "Meanwhile, the handful of men that didn't die in the war will be castrated and forced to repair toilets and build massive monuments commemorating the feminist victory."

        hi "That's crazy. You're crazy. I think you're overthinking this."

        ke "As the days go by, I realize more and more that you are not ballin'."

        hi "We've only talked like four times."

        show kenji neutral
        with charachange

        ke "Oh. Sorry."

        hi "Yeah, whatever, I'll get your package."

        show kenji happy
        with charachange

        ke "Awesome."

        play sound sfx_doorslam

        stop music fadeout 0.5

        scene bg school_dormhisao
        with vpunch

        "I close the door and jump right back into bed."

        play ambient sfx_alarmclock

        "The second my head hits the pillow, a painfully loud ringing assaults my ears, and I realize it's my clock. The alarm going off means that right now is the time I'm supposed to wake up in the first place."

        "On weekdays, at least."

        play sound sfx_impact

        "I pick it up and throw it without looking up. It gets wedged between the bed and the wall, the noise not stopping. In fact, it seems to grow louder."

        stop ambient

        "By the time I'm able to pry it out of there I know I'm not going to be able to go back to sleep. The only thing I can think of doing now is going into town and just getting Kenji's stupid package, but it's too early for that."

        "After showering, I take my medication. I'm actually very hungry today since I went without dinner yesterday, and before that I had just a very light lunch."

        "I eat the pills, chomping on them like a leg of lamb. They are unbelievably bitter and disgusting."

        "Well, good medicine tastes bad, or something like that. I'm still hungry, and there's still a lot of time to kill, so I decide to go into town and find somewhere to have breakfast."

        "I can't remember the last time I ate out. Besides, the weather is nice, so why not?"

        scene bg school_road
        with locationskip

        play music music_soothing fadein 3.0

        "The walk into town is longer than I remember, possibly because it's been a while, and probably because I rarely come here alone. There are barely any cars on the road because it's so early in the morning, making it unusually quiet."

        scene bg suburb_roadcenter
        with locationchange

        "The first thing I do is start looking for a place to eat. Immediately I think of the Shanghai, but I want something more substantial than sandwiches or a cake."

        "Since it's so early, though, I decide to get Kenji's package first."

        "Picking it up at the post office doesn't take very long, but the moment I see it, I'm enraged about what a pain in the ass it will be to carry this thing all the way back to the school."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        show kenjibox:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0

        pause 1.0

        show kenjibox at truecenter

        "The box is huge, you need two hands to hold it. Insultingly, it's not even very heavy."

        "I was thinking of wandering around for a little while, but with this thing in tow, that's going to be a real problem. I guess the Shanghai is my only option now."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        show kenjibox:
            easeout 1.0 ypos 0.7 alpha 0.0

        pause 1.0

        hide kenjibox

        "Everything else is closed, and the ones that aren't all have about the same menu. That fact also makes me want to throw some more business Yuuko's way."

        stop music fadeout 4.0

        scene bg suburb_shanghaiext
        with locationchange

        "Before I can even open the door and enter, someone taps me on the shoulder from behind. I turn around and see Shizune there. Instinctively, I look for Misha, but she doesn't seem to be here."

        show shizu adjust_happy at center
        with charaenter

        ssh "Good morning."

        "Looks like those sign language classes are already starting to pay off. I'm tempted to sign it right back, but then she might think I know a lot more than I actually do."

        "For now, I just give her a wave and open the door. She's probably here for her morning tea and didn't come here just to greet me. It turns out I'm right, as Shizune follows me inside the teahouse."

        play sound sfx_storebell

        scene bg suburb_shanghaiint at bgright
        with locationchange

        "It's a total ghost town in here. It's not exactly peak hours, but every other café I passed had at least a few customers."

        "Actually, the Shanghai has been fairly empty every time I passed by. How does this place stay in business?"

        show yuukoshang happy_down at center
        with charaenter

        yu "Hello! Thank you for choosing to patronize our establishment!"

        show yuukoshang neurotic_down:
            center
            ypos 1.25
        with Dissolvemove(0.2)

        play sound sfx_impact
        with vpunch

        pause 0.3

        show yuukoshang at center
        with charamove

        "Yuuko bows with the force of a falling axe and her head collides with the box in my hands, launching it towards the floor."

        play music music_comedy

        show yuukoshang panic_up
        with charachange

        yu "Oh no, I'm sorry, I'm really sorry, sorry, please forgive me!"

        hi "It's okay, and you don't have to do that 'Hello, thanks for choosing our shop!' thing since we know you."

        show yuukoshang worried_up
        with charachange

        yu "But it's part of my job."

        show yuukoshang worried_down
        with charachange

        yu "You're here early, what can I get you?"

        hi "I just want some coffee for now."

        show shizu behind_blank:
            right alpha 0.0
            ease 1.0 tworight alpha 1.0
        with None

        show yuukoshang worried_down at twoleft
        show bg suburb_shanghaiint at center
        with charamovefaster

        show shizu at tworight

        "I wonder what Shizune wants. Without Misha, there's no real way to tell, or any way to even ask. I haven't learned about that yet. She's here, so I'm pretty sure that means she wants something too."

        hi "Er, I don't really know what Shizune wants. Does she have a usual?"

        hi "Wait, she might want something else, though. Perhaps you should bring us a menu just in case."

        "I look around for one, but can't find anything that looks remotely like a menu."

        show yuukoshang neurotic_up
        with charachange

        yu "Menus… I'll look for one right now."

        hi "Huh?"

        show yuukoshang worried_up
        with charachange

        yu "Um… there are menus. They're just… rare."

        "It's only a restaurant menu, not a collector's edition."

        show shizu basic_normal2
        with charachange

        shi "…"

        hi "Weird."

        show yuukoshang neutral_down
        with charachange

        yu "Is that what Shizune is saying?"

        hi "Nah, she can't hear you. It's just weird for a café to make you have to go out of your way to look for a menu."

        show yuukoshang worried_up
        with charachange

        yu "Weird…?"

        show yuukoshang neurotic_down
        with charachange

        yu "Yes… you're right. It's so illogical. There are so many things… Like, why is it called the Shanghai? This is a Western style teahouse… but, the name is Chinese… and the architecture is old-fashioned, but my uniform is so modern and sophisticated…"

        "She looks like she's about to pass out. If she does she'll probably fall forward and make a mess of everything."

        show yuukoshang panic_up
        with charachange

        yu "I can't work here any more."

        "What a bad place for her circular train of logic to end up."

        hi "No, come on. That kind of stuff is what sets this place apart; there are a lot of cafés around here, you know. I think it's charming, really. Please don't quit. Business is good here, isn't it?"

        show yuukoshang worried_up
        with charachange

        yu "Not really…"

        hi "See, I think this is a good job for you. It suits you, you shouldn't quit."

        "I've never had to defuse this kind of crisis before."

        stop music fadeout 2.0

        "Eventually, I manage to calm her down, and convince her that I'm sure Shizune just wants what she usually orders here."

        hide yuukoshang
        with charaexit

        show shizu at center
        show bg at bgleft
        with charamove

        show shizu:
            ypos 1.15
        with charamove

        "Yuuko walks away to get our drinks, and by then, Shizune has already picked a table."

        play music music_dreamy fadein 4.0

        "There are no other customers, and Yuuko isn't the most talkative person, so it's very quiet."

        "It doesn't really bother me, but I wish that there was some way we could communicate. There are so few moments when we're alone. Shizune and Misha are almost always together, to the point where sometimes it seems like they are one."

        "Now, it's just me and her, and I'm unable to understand her or have her understand me. It's terrible."

        hi "You don't have your little notepad today? I know it's the weekend and all, but it's not like you to be unprepared."

        hi "Well, that's fine. I don't really like using it anyway. Still, it would come in handy now."

        show shizu behind_blank
        with charachange

        shi "…"

        show shizu basic_normal
        with charachange

        shi "… …"

        "Shizune starts signing in short bursts punctuated by her stopping to take a sip of tea. It's strange how she doesn't make the slightest attempt to change how she normally acts."

        "I'm talking to her for the most part because I'm not used to long silences. I briefly wonder if it's the same for her, in a way; however, it seems unlikely. I think it's more that she is the type who doesn't change how she acts for anyone."

        hi "Hey, it seems like Misha joined the Student Council because of you. That makes two of us, you know. I'm only there because you forced me into it."

        hi "Well, not really forced, I guess. If it wasn't for you, I wouldn't have joined."

        "That sounds slightly romantic, and I find myself blushing a little. I feel like such an idiot."

        hi "Although, I still don't know why you joined. It should have been the first thing I asked, in retrospect, but I'm really curious. I'll have to remember to ask Misha sometime."

        show shizu behind_blank
        with charachange

        shi "…"

        hi "It's nice to talk to you, even if you can't understand me. I wonder if it's the same for you."

        hi "That would be really… great."

        show shizu adjust_happy
        with charachange

        shi "…"

        hi "I don't think sign language will ever be as natural for me as Misha makes it look, but it's got to be a step up from using pen and paper, right?"

        show shizu basic_normal2
        with charachange

        shi "…"

        stop music fadeout 4.0

        "We've both been finished with our drinks for a while, and Shizune's eyes fall upon the box sitting in its own chair by my side."

        show shizu adjust_happy
        with charachange

        shi "…"

        hi "I'm just picking it up for someone, it's not mine."

        play music music_running fadein 0.5

        show shizu basic_sparkle
        with charachange

        "Shizune pulls it closer to her, intending to open it, and my heart almost leaps out of my throat. I quickly try to pull it back by wrapping my leg around the leg of the chair."

        hi "What the hell, don't open it. You can't just open other people's mail, that's not legal."

        show shizu basic_frown
        with charachange

        shi "…"

        hi "No!"

        show shizu cross_angry
        with charachange

        shi "…!"

        "Once she gets going, there is almost no stopping her. Eyes filled with excitement, she looks ready to fight me over this stupid package and I realize just how fast this could turn into a game of tug-of-war."

        show shizu behind_frown
        with charachange

        "I am almost out of my seat now and waving my arms like an air traffic controller, before she finally settles down."

        show shizu at center
        with charamove

        "Shizune pouts, not pleased with having her curiosity checked, and gets up to leave."

        "It's about time to, I guess. We've been here a while. I protectively pick up the box before standing up myself."

        show shizu basic_happy
        with charachange

        "Suddenly, she tents her fingers excitedly and pulls out a marker from her pocket, and starts writing on Kenji's box."

        hi "Hey, what are you doing? I said this isn't mine!"

        hi "Hey!"

        "I can't even see her with it blocking my vision."

        hi "Fine, at least let me put it down first."

        "I have to to read whatever she's writing, anyway."

        call screen written_note(_("I'll help you carry it."), custom_background=Frame("vfx/cardboard.jpg", 0, 0, tile=True))

        show shizu adjust_smug
        with charachange

        "It doesn't seem like she's finished, though, and Shizune draws a fierce line afterward to signify that there's a catch."

        call screen written_note(_("I'll help you carry it.\n ___________________\n\nBut, it's a game! The first one to stumble loses, and the loser has to carry it the rest of the way by themselves."), custom_background=Frame("vfx/cardboard.jpg", 0, 0, tile=True))

        hi "That's stupid, there's a fifty percent chance I'll end up carrying it myself anyway."

        "Actually, I feel pretty stupid myself right now. I just forgot she can't hear me. I stop talking and shake my head."

        show shizu behind_blank
        with charachange

        shi "…"

        show shizu cross_angry
        with charachange

        shi "…!"

        show shizu adjust_angry
        with charachange

        shi "…!"

        "I can't understand her at all, but she's coming across very forcefully. It's clear that she thinks this is a great idea."

        "Well, if she drops the box or something, she'll have to carry it. That would make things a lot easier for me, obviously."

        "The odds are 50-50, then… they're probably higher than they would be for any other plan of hers. All right, I'll take it."

        show shizu basic_normal_close
        with characlose

        "Thinking about it, I'm not sure how we should do this. Then Shizune grabs hold of one end of the box and lifts it up, and I take the side that she isn't holding. Is this even right? It's very uncomfortable to walk like this."

        show bg suburb_shanghaiext
        with locationchange

        "We leave the café, and I find myself hoping that the streets are still devoid of people. Yuuko seemed confused as to what we were doing, and I imagine it'll only get worse as more people see us."

        show shizu adjust_happy_close
        with charachangealways

        show shizu basic_normal_close
        with charachangealways

        "Shizune doesn't seem bothered at all while walking with her arm at this unnatural angle; she just grins confidently and periodically makes some kind of weird gesture."

        show bg suburb_roadcenter
        with locationchange

        "There are people staring at us as time passes, and the usual morning crowd begins to fill the streets."

        "I feel silly, but I'm sure that if I give up, Shizune will take it as a sign of surrender. I can't allow that, because I think I'm doing well so far."

        show shizu adjust_happy_close
        with charachangealways

        show shizu basic_normal_close
        with charachangealways

        "Initially, I just write Shizune's little hand signals off as her preemptively gloating, but I catch on quickly that she's actually signaling where she wants to go."

        "It dawns on me that this isn't a competition. It's not much of a challenge, first of all, and second, it's really more of an exercise in teamwork. It's just that Shizune has made a punishment for failing instead of a reward for doing well."

        stop music fadeout 3.0

        show shizu adjust_blush_close
        with charachange

        "Our fingers touch under the box, and Shizune moves her hand away, almost dropping her side of the box in the process."

        "Well, that's game over for her."

        "She doesn't look very happy. Does she think I did it on purpose to make her lose? If she does, she isn't making a big deal out of it. All's fair in love and war."

        show shizu basic_frown
        with charadistant

        "I feel like I should take it from her and carry it myself, but she pushes me away when I try."

        play music music_shizune fadein 1.0

        "She glares at me as if to tell me off, but she can't. With that box in her hands, she is basically gagged."

        show shizu basic_normal2
        with charachangealways

        show shizu basic_normal
        with charachangealways

        "A sad expression flickers across her face for a second, maybe on realizing that and having to acknowledge that there are some limitations she has to deal with after all."

        "However, she is still as prideful as ever, even when it's to her detriment. She wouldn't accept letting me allow her to skip out on the consequences of her bet."

        "Anything is fair during the game, but the results have to be honored to the letter, huh?"

        "Shizune is an interesting type of person."

        show bg school_dormext_full
        with shorttimeskip

        "The march back to the dorms is uneventful. Shizune passes the trip by shifting the box around occasionally like a giant Rubik's cube. It looks like another game she has invented to amuse herself."

        "It can't be good for whatever's inside, but I don't care enough to stop her."

        "Maybe this is how she deals with things, by making everything into a game; it's hard to say for sure, though."

        "It seems futile to try to psychoanalyze Shizune. In the short time we've known each other, I've been surprised on a fair number of occasions."

        show shizu basic_normal2:
            function partial(tremble_general, 1.0, 0.5, 1.0, 0.5, 1.0)

        stop music fadeout 6.0

        "I notice Shizune shivering. The wind is picking up, and the school is pretty high up. It makes sense that she would be cold. If I gave her my jacket, though, would she reject it?"

        play sound sfx_rustling

        show shizu basic_normal2_close at center
        with characlose

        "I take off my jacket and drape it across her shoulders before she has a chance to protest. Her shoulders are slim and delicate, so much so that I want to let my hands linger on them."

        show shizu adjust_blush_close
        with charachangefast

        "Shizune flinches when my fingers brush against her, understandably surprised."

        hi "Sorry."

        show shizu basic_normal_close
        with charachange

        shi "…"

        show shizu adjust_happy_close
        with charachange

        shi "…"

        "Her fingers dance lightly over the surface of the box, and I think of taking it from her, but I doubt she would let me. Shizune makes a quick gesture with her hands as best she can, pausing a bit afterward as if wanting to say more."

        "I'm sure that what she means is 'thank you.' I'm glad that I was able to catch it."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .advanced_game_theory:
        scene bg school_cafeteria
        with locationchange

        nvl clear

        nvl show dissolve

        $ renpy.music.set_volume(0.5, 0.0, channel="music")
        play music music_normal fadein 0.5

        n "{vspace=60}The sign language teacher says I'm pretty good."

        n "I try not to think about it too much, but the truth is I'm poring over it so much lately that it's hard not to keep coming back to it at least a couple times a day. I guess I am picking it up faster than expected, but it's still not enough."

        n "I understand it just fine; understanding it is simple. Well, I have to put my mind to it to read it, but it's easy enough when I do."

        n "The signing itself is doable, I just need a little more practice. However, trying to do both at the same time, even at half the speed Misha does it? It's impossible."

        n "Where I'm at now is good for my level, but in order to reach a point where I'll be able to really converse with Shizune, I'll need more work."

        n "{vspace=30}I'm doing my best to get to that point one step at a time by doing as much studying as I can squeeze in during lunch."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl clear

        nvl hide dissolve

        "I look up from 'Introduction to Japanese Sign Language' to check if Shizune or Misha are around."

        "Of course, since this is taking up my lunch hour, I've had to avoid them for a few days now. What's more, I'll have to continue doing so if I want to keep Shizune from finding out."

        "My back to the corner, scanning the area every ten minutes, I feel like some kind of criminal trying to evade capture."

        "…"

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl show dissolve

        nvl clear

        n "{vspace=60}Every chance she gets, Misha asks me why I want to hide the fact I'm learning sign language from Shizune."

        n "Looking back on it, there really wasn't any reason, but now I think I know."

        n "If I want Shizune to be able to treat me as a true equal, sign language is an important step towards that goal."

        n "If I want to be able to treat Shizune as an equal, then sign language is an important step towards that goal."

        n "Another important step is to make sure she doesn't know, so that when we're able to finally speak on equal terms, I'll be fully ready, able to do it right, not like some dilettante."

        n "Anything less, I think, would be insulting. She would see it the same way."

        n "{vspace=30}So to me, this is the only option. Especially now that I've decided to be so resolute with it."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl clear

        nvl hide dissolve

        "Shizune has a huge aura. It's very easy to see her coming, or even to sense her coming. Mostly because Misha's hair lights up any crowd she's in like a beacon, and you can hear her laughing from a mile away."

        "Although, even if Misha weren't with her, it would be the same. Her directness and efficiency are core parts of her, so it's no surprise that they come across in the way she walks as well."

        "Due to all these factors, I'm able to put away all my things and put on my best casual face long before they see me and head my way."

        show shizu behind_smile at tworight
        show misha perky_smile at twoleft
        with charaenter

        hi "Hi."

        show shizu adjust_smug
        with charachange

        ssh "Student Councilll."

        show misha hips_grin
        with charachange

        mi "Student Council~!"

        "'Student Council' was the first thing I asked to learn; it seemed like it would come in handy."

        hi "Yeah, I've been dodging it for a while now, huh?"

        show misha sign_smile
        show shizu behind_smile
        with charachange

        mi "Yup~!"

        show shizu behind_smile_close at closeright
        show misha perky_smile_close at closeleft
        with characlose

        show shizu behind_smile_close:
            ypos 1.07
        show misha perky_smile_close:
            ypos 1.1
        with charamove

        stop music fadeout 3.0

        "Shizune sits down in front of me to my right, and Misha to my left. It was a mistake putting myself in the corner; now I'm, well, cornered."

        scene bg school_lobby
        with shorttimeskip

        "In the end, I'm dragged off to the student council room, but I don't mind. I was starting to miss them a bit, anyway."

        "In some ways this makes it easier: satisfied with having caught me, Shizune doesn't ask me where I've been all this time."

        "Once I stand before the door, I wonder what could be so important that they're so eager to pull me back in."

        scene bg school_council at bgright
        with locationchange

        hi "Games."

        play music music_another fadein 0.5

        "There are more games out than books. This at last explains why every time I come here there are stacks of books piled on every table and occasionally parts of the floor: they need the room to put all these games somewhere."

        show misha cross_laugh
        with charaenter

        mi "Hahaha~!"

        show misha hips_grin
        with charachange

        mi "It's boring playing against each other so much, Hicchan. So, it's your turn, okay? Okay~! It's settled then~!"

        hi "I didn't even say anything!"

        show shizu basic_normal behind misha:
            right alpha 0.0
            ease 1.0 tworight alpha 1.0

        show misha at twoleft
        show bg at center
        with charamovefaster

        show shizu at tworight
        with None

        show shizu behind_blank
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "Hicchan, this is one of the last days we'll be able to take it easy like this for a while. So~, it's especially important that we make the most of it, don't you think?"

        show misha cross_smile
        with charachange

        mi "Tanabata will be coming up soon, and we'll have to put in a lot of work for that, too."

        show misha hips_grin
        show shizu behind_smile
        with charachange

        mi "So, for now, play with us~!"

        "Come to think of it, it's true. I hadn't even noticed because I've been so wrapped up in wanting to learn sign language. Right on the heels of one festival, a bigger one appears."

        "I wonder if Shizune will try and rope a couple new members in to help with that one as well."

        hi "You're right."

        show misha cross_laugh
        with charachange

        mi "Hahaha~! Yay~! Hicchan agrees~! Let's celebrate!"

        show shizu basic_happy
        with charachange

        ssh "I know, we should play a game."

        show misha sign_smile
        with charachange

        mi "Let's play a game to celebrate, Hicchan~!"

        hi "I don't know, that kind of thing usually ends badly for me."

        show misha perky_sad
        with charachange

        mi "Hicchan is worried about the stakes~."

        "Misha makes a very disappointed face. It's hard to tell if she's mocking me, since her expressions are so exaggerated by default. She's an 'all-out' kind of girl."

        "I turn my head to Shizune. Now, this person, she is definitely mocking me."

        hi "Hey, stop that. But, yes, I'll play with you if you tell me what's at stake first."

        show shizu adjust_smug
        with charachange

        shi "…"

        show misha cross_grin
        with charachange

        mi "How very Japanese, putting the consequences above everything else."

        show misha sign_smile
        with charachange

        mi "Hicchan, have you ever heard of the expression 'missing the forest for the trees?'"

        hi "No."

        "That's a lie. But I have my pride, which is currently feeling wounded."

        hi "Okay, I'll play, but I want to pick the game."

        show shizu adjust_happy
        show misha perky_smile
        with charachange

        "Misha nods."

        hi "Additionally, I pick the punishment if you lose."

        show shizu cross_angry
        with charachange

        "Shizune makes an X with her arms. That either means 'denied' or that she's about to use her special attack."

        hi "Aha, now who's afraid of consequences?"

        show shizu behind_frown
        with charachange

        ssh "How vengeful, still thinking so spitefully about a playful little joke."

        show shizu basic_frown
        with charachange

        ssh "If a … bit you, you would probably bite back."

        "Shizune signs a word that I don't quite catch."

        show misha hips_frown
        with charachange

        mi "Hicchan is so vengeful~, even though it was just a playful little joke. If an armadillo bit you, you would probably bite back!"

        hi "Armadillo?"

        show misha sign_smile
        with charachange

        mi "It's foolish to bite an armadillo back, Hicchan!"

        show shizu behind_blank
        with charachange

        shi "…"

        show misha cross_laugh
        with charachange

        mi "But Hicchan would do it anyway, you see~! Hahaha!"

        hi "I see."

        show shizu adjust_smug
        with charachange

        "Shizune adjusts her glasses with a small flourish of her hand."

        show shizu behind_smile
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "Hicchan, we didn't have anything planned at all if you were to win or lose, you just assumed there would be something like that~."

        hi "I wonder why."

        show misha hips_grin
        with charachange

        mi "Hm~, me too~! But, oh well~! There isn't. Does that change your mind, Hicchan?"

        hi "Well… yes."

        show misha hips_laugh
        with charachange

        "Misha windmills her arm at high speed to show her joy. Weird habit. This is the kind of thing you could only see in the student council room, occupied only by three people."

        "Anywhere else she would end up socking someone in the face."

        show misha hips_grin
        with charachange

        mi "Yay yay~! Let's start right now~!"

        hi "Not just yet."

        show misha hips_smile
        with charachange

        mi "…"

        show shizu behind_blank
        with charachange

        shi "…"

        mi "…"

        shi "…"

        hi "Okay, okay."

        hi "However, we have to all be able to play. That's my condition."

        hi "I don't like games where one person is clearly the ace player right off the bat, or games where only two people can play so one of us has to sit back. It has to be something the three of us can play equally."

        show shizu basic_normal
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "Checkers?"

        "The instant she says it, Misha takes out a bag of checkers and places them on the table."

        hi "Only two people can play that. I told you—"

        show misha hips_grin
        with charachange

        mi "Okay okay~! Hicchan, how about… Monopoly?"

        "A Monopoly box slowly edges towards me, and I take it out of Misha's hands and put it under my chair."

        hi "I don't like games that revolve around luck of the draw; they're too much about chance and not about skill. Also, stop jumping the gun with these games!"

        show misha perky_confused
        with charachange

        mi "Luck is kind of a skill, you know."

        hi "No, no it's not!"

        show shizu adjust_smug
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "It can be if you're consistently lucky~! Right~?"

        hi "Once at that point it's something else entirely."

        show shizu adjust_happy
        show misha hips_grin
        with charachange

        mi "Hm~, hm~ hm~ hm~~. Baccarat? Marbles? Life? Snakes and Ladders? Roulette? Blackjack? Paper football? Trivial Pursuit?"

        "Misha begins to excitedly name a bunch of games as if she were reading from a list."

        "With each suggestion, a new box, board, and pieces appear around her, a bizarre catalogue of games ranging from children's fare to serious, polished-looking gambling instruments that look very out of place in this humble room."

        show misha sign_smile
        with charachange

        mi "Three way chess?"

        hi "Is that even possible?"

        show shizu behind_smile
        with charachange

        ssh "Let's try."

        show misha cross_laugh
        with charachange

        mi "Yes yes~, let's try it, definitely~! Ahahahaha~!"

        show shizu basic_happy
        show misha hips_grin
        with charachange

        "They pull a chessboard from behind them with a flourish like two junior magicians. Well, magic does require some deft sleight of hand, and they've got that in spades."

        "I'm not surprised. Nevertheless, it is still somehow unsettling."

        hi "Stop doing that!"

        stop music fadeout 2.0

        ha "E-excuse me…?"

        show shizu basic_normal
        show misha perky_confused
        with charachange

        "A very timid voice manages to make me look up."

        show hanako emb_downtimid:
            offscreenright alpha 0.0
            ease 1.0 xanchor 0.7 xpos 1.0 alpha 1.0
        with None

        show misha at left
        show shizu at center
        show bg at bgleft
        with charamovefaster

        ha "I l-lost my ID card, and someone told me… I could find out where to get a new one here. If I'm interrupting s-something, I can come back later."

        show hanako emb_timid
        with charachange

        "Hanako's eyes drift across the room, taking in the landscape of piled-up record books, haphazardly scattered chairs, and overturned board games."

        "I guess this isn't exactly the image an organized, tightly run Student Council like ours should be giving off."

        hi "Hello."

        "It's the only thing I can think of to break the ice. Unfortunately, it just seems to startle her further."

        show hanako def_worry
        with charachange

        ha "…"

        show hanako def_strain
        with charachange

        ha "Ah…{w=0.5} my ID card…{w=0.5} I…"

        show misha sign_smile
        with charachange

        mi "You're in our class, aren't you, right? Right~! So~! Don't be so timid, okay? Come on!"

        show shizu behind_smile
        with charachange

        shi "…"

        show misha hips_grin
        with charachange

        mi "Yup, even though we're your seniors, it's not like we'll bite!"

        hi "We're not her seniors, we're in the same class."

        play music music_happiness fadein 3.0

        "Still, I am grateful to them for stepping in."

        show misha hips_smile
        with charachange

        mi "What is it you said you want? An ID card, right~? Right~!"

        show hanako basic_distant
        with charachange

        ha "Yes."

        "Her eyes slide away from Misha. Being shy, it's no wonder she's not the best at keeping eye contact. I follow where she's looking, and notice her gaze stop on the chessboard on the table."

        show hanako basic_normal
        with charachangealways

        show hanako basic_distant
        with charachangealways

        "Hanako's eyes widen, just for a moment. Shizune notices as well."

        show shizu basic_happy
        with charachange

        shi "…"

        show misha perky_smile
        with charachange

        mi "Do you like chess?"

        show hanako defarms_strain
        with charachange

        ha "Eh!?"

        show shizu adjust_smug
        with charachange

        shi "…!"

        show misha hips_smile
        with charachange

        mi "You like chess, don't you~? Yeah, you do, definitely~!"

        show misha hips_grin
        show shizu adjust_happy
        with charachange

        mi "Do~{w=0.2} you~{w=0.2} want~{w=0.2} to~{w=0.2} play~?"

        "Hesitation. She might make a break for it. I refuse to get involved in this; it won't end well."

        show hanako basic_normal
        with charachange

        "To my amazement, Hanako seems to be considering the idea very seriously. She touches the tips of her fingers together pensively, mulling the thought over."

        "That level of consideration is more or less a confirmation."

        show misha sign_smile
        with charachange

        mi "We're having our lunch break, so you'll have to wait anyway. Why not play with us in the meantime~? Come on, it'll be fun, really fun~! You like chess, don't you? I can tell, really really, it's obvious, so~! Please~, will you?"

        show hanako cover_distant
        with charachange

        ha "Okay…"

        show misha cross_laugh
        with charachange

        mi "Wahaha~! Yay~! Success, success, okay okay okay~! That's great~!"

        scene ev shizu_chess_large:
            xanchor 2173 yanchor 2396 xpos 400 ypos 300 zoom 1.0
            easein 10.0 yanchor 2296
        with flash

        "The chessboard is set up."

        "The opening move is important."

        show ev:
            ease 1.0 xpos 400 xanchor 2870 yanchor 650 ypos 300
            acdc_warp 10.0 xanchor 2670

        "However, Shizune doesn't seem to care."

        show ev:
            ease 0.5 xanchor 1600 yanchor 560
            easein 10.0 xanchor 1400 yanchor 560

        "Hanako ponders her moves carefully, sliding pieces forward just a little bit, then pulling them back in uncertainty, second-guessing herself over and over again."

        "She's really into this game; you can't call her a casual player. Definitely an enthusiast."

        "Shizune can't take her lightly; no matter what she does, Hanako has an appropriate response."

        "Yet there's something wrong about the pacing of this game."

        scene ev shizu_chess_base:
            truecenter
            zoom 1.05
            easein 5.0 zoom 1.0
        with flash

        "Shizune moves too quickly. No, not even too quickly, but with illogical speed. It's like she isn't even thinking about what she'll do next. Either Shizune is in the realm of supercomputers, or she isn't taking this game very seriously."

        "Or maybe Hanako just isn't very good."

        scene ev shizu_chess_base
        show sc_shiz normal:
            xalign 1.0 yalign 0.0
        with charachangeev

        "Shizune forces an exchange of pawns."

        scene ev shizu_chess_base3
        with charachangeev

        "Hanako's turns take increasing amounts of time as the game goes on, and it hasn't even been going on that long. Suddenly it all becomes clear: Shizune has a lot more time to think about her next move because Hanako takes forever to move a piece."

        "Despite that, it's an interesting game."

        nvl clear

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl show dissolve

        n "{vspace=60}Black knight to f6."

        n "Bishop to d3."

        n "Since they're both playing seriously, no one is toying with the other. There is no clearly dominant player, at least for now. Maybe this is helped by the fact that they aren't very close to each other, from what I can see."

        n "Shizune is a mysterious opponent to Hanako, and Hanako is an enigma to Shizune. Hanako's furrowed brow shows that she is into the game. She wants to really win, and Shizune always wants to win."

        n "Their lack of familiarity is a little depressing, but it is giving life to the game, and allowing them to see each other as good competition."

        n "Maybe they might even end up being friends over it, or at the very least, rivals in chess. It's an optimistic thought."

        n "Although remembering playing Risk against Shizune, she doesn't want to just crush people for the fun of it."

        nvl clear

        n "{vspace=90}The game continues."

        n "Shizune plays twelve moves in four minutes. What a scary opponent."

        n "But Hanako holds her own, even though her king is being chased around the board a bit."

        n "Pawn to h6."

        n "White knight to e6."

        n "The end is near."

        n "{vspace=60}…"

        stop music fadeout 3.0

        n "The game ends."

        nvl clear

        nvl hide dissolve

        scene bg school_council
        show shizu adjust_happy at center
        show misha perky_smile at left
        show hanako basic_normal at right
        with locationchange

        shi "…"

        show misha sign_smile
        with charachange

        mi "That was a really good game~!"

        $ renpy.music.set_volume(1.0, 0.0, channel="music")
        play music music_ease fadein 5.0

        show hanako cover_bashful
        with charachange

        ha "T-thanks…"

        show shizu behind_smile
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "It was really close~, I thought I would lose. You're very skilled."

        "Magnanimous in victory, and extending a hand to the defeated. Maybe it's because Hanako is taking her defeat so well."

        show shizu basic_normal
        with charachange

        shi "…"

        show misha perky_smile
        with charachange

        mi "This is a fun game, but it took so long. Almost the whole period!"

        mi "Chess is too formulaic, especially at this level. How about some advanced rules~?"

        hi "What?"

        show hanako cover_worry
        with charachange

        ha "Ad… vanced…?"

        show shizu basic_sparkle
        with charachangealways

        show shizu adjust_smug
        with charachangealways

        show shizu basic_happy
        with charachangealways

        shi "… … …"

        show misha hips_smile
        with charachange

        mi "Yeah, yeah~! Like speed chess, or chess with additional pieces, or maybe we can pair up and play tag team chess, with one or two boards, your choice! C'mon c'mon c'mon c'mon it'll be fun, really, really~! Regular chess is so slow, too methodical, it's boring."

        show misha hips_grin
        with charachange

        mi "I want to play chess that rewards quick thinking, and daring! Any one of these, comparing chess to it is like comparing checkers to go, or tic-tac-toe to shogi, right? Right~!"

        show misha cross_laugh
        with charachange

        mi "Wahahaha~! Even laser chess might be more exciting, pick something, pick~!"

        show hanako defarms_strain
        with charachange

        ha "Aaaah…"

        "Like a deer in the headlights. Many emotions spring up in me, watching Hanako's mind reel in front of the chessboard as if she's about to faint. The dominant one is amusement, but I move a little closer in case she might really topple over."

        scene ev shizu_chess_base2:
            truecenter
            zoom 1.05
            easein 5.0 zoom 1.0
        with flash

        "The board is set up again, but this time, it's not even close."

        "Hanako can't even make a move out of fear of her hand colliding with Shizune's. She's all over the board. It's an onslaught. Anywhere Hanako wants to put a piece, Shizune is already there."

        "It's the fastest game I've seen in my life."

        scene bg school_council
        show shizu basic_sparkle at center
        show misha hips_grin at left
        show hanako defarms_strain at right
        with locationchange

        mi "Let's change the rules and play again~! Best out of six, like Kasparov and Deep Blue~!"

        show hanako at offscreenright
        with charamovefaster

        hide hanako

        "Hanako excuses herself and flees from the room."

        show shizu basic_normal
        show misha perky_confused
        with charachange

        mi "Huh? Wait!"

        hide misha
        with charaexit

        mi "Ah, didn't she want to know where she could get a new ID? Excuse me! Hello~? Come back, please! Wait, wait~! Wait~!"

        stop music fadeout 3.0

        "Strangely, the farther Misha goes away, the louder the sound of her voice seems to grow."

        show bg at bgright
        show shizu at tworight
        with charamove

        show misha perky_sad at twoleft
        with charaenter

        mi "I couldn't catch her~…"

        show shizu adjust_happy
        with charachange

        play music music_normal fadein 3.0

        shi "…"

        "Shizune pats her on the shoulder reassuringly."

        hi "There, there."

        show misha hips_smile
        with charachange

        mi "There, there~!"

        hi "You're pretty cheerful for someone who needed a pat on the shoulder."

        show misha cross_laugh
        with charachange

        mi "Ahahaha~!"

        "…"

        show shizu basic_normal2
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "Hicchan, do you hate games where luck is involved?"

        "A question out of nowhere, but it feels like an important one."

        "If it wasn't, why would Shizune be looking at me, watching for my reaction? Even as I glance in her direction, she tries to pretend she isn't doing so, putting on a casual air by spinning a chess piece in her fingers."

        show misha hips_grin
        with charachange

        mi "'I don't like games that revolve around luck of the draw,' right? That was you, Hicchan~."

        hi "Yeah. Revolving around luck isn't the same as just having luck involved, though. I don't hate games just for having an element of luck. Most games have an element of luck to them anyway. It's what keeps them interesting."

        hi "I think a game where you know from the beginning how far you can go is boring. Then it's not a game, isn't it? Just going through motions."

        hi "For a game where you have little to no control, I don't think I could get into something like that."

        show shizu behind_smile
        with charachange

        ssh "I see."

        show shizu adjust_smug
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "That girl isn't very good at chess."

        show shizu basic_normal
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "Chess is a formulaic game. So~! It's a game that isn't suited for her… There was nothing formulaic about her. Someone who plays chess like that, looking only at the next piece, playing so shallowly, can't be called a serious chess player."

        show misha perky_smile
        with charachange

        mi "Anyone who loves chess to the point where their eyes sparkle like that when they see a chessboard would be the kind of person who would study the game."

        mi "If you study it just casually, you can learn to see at least two moves ahead, even against pros."

        show misha hips_frown
        with charachange

        mi "Why would someone who loves the game so much… with that enthusiasm… know so little about it? Even less than someone with just a passing interest in it?"

        "Shizune puts down the piece in her hand. It's a rook."

        show shizu behind_frown
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "Her feelings are real, but her feelings for the game aren't real. Do you understand, Hicchan~?"

        show misha perky_smile
        with charachange

        mi "There is no luck in chess~! It's very important to realize that. Luck in games is good because it gives everyone a chance. Just enough to matter, but not so much that skill is penalized. Chess is boring because it's not a game; to me, it seems like formulas."

        show misha sign_smile
        with charachange

        mi "Hanako isn't the kind of person who would love something like that either~."

        show shizu adjust_angry
        with charachange

        shi "…"

        show misha cross_frown
        with charachange

        mi "If you value something, you fight. Struggle is proof of precs— preciousness? I think so, at least. Or~! You concede immediately~! Since it's so precious that it stops your thinking. The first is a passionate love. The second is a gentle love."

        show shizu basic_normal2
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "I tried to fight her, chasing around her king, and trying to bait her. I didn't succeed though, because she stuck to only what would work."

        mi "The trickiest moments were when she moved the fastest. That means she knew exactly how to deal with those situations."

        show misha sign_smile
        with charachange

        mi "That means someone taught her. Do you understand, Hicchan~?"

        hi "Not really."

        show shizu adjust_happy
        with charachange

        shi "…"

        show misha hips_grin
        with charachange

        mi "If you love chess that much, but you can't give it your all, it's because you love the memories attached to it and not the game; it's too precious to her to see as a tool for true competition."

        show shizu behind_blank
        with charachange

        shi "…"

        show misha perky_smile
        with charachange

        mi "Due to that, you can't become friends over it. Not without words."

        stop music fadeout 5.0

        "Well, your way of making friends isn't the kind of way that works on everyone, Shizune."

        "The look on her face isn't one of sadness, at least as far as I can tell, but her words are very sad."

        hi "Hey, let's play a game."

        hi "While the board is still here."

        play sound sfx_warningbell

        "But the bell rings and cuts me off."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .bread_scissors_paper:
        scene bg school_council
        with locationchange

        nvl clear

        nvl show dissolve

        $ renpy.music.set_volume(0.5, 0.0, channel="music")
        play music music_daily fadein 0.5

        n "{vspace=60}Things have returned to normal. Well, I transferred in at a pretty unusual time, and I can hardly say that I had a normal first few weeks here. I guess it's more like things have calmed down, and reached normality."

        n "I've been here longer than I thought."

        n "It's hard not to think about all the stuff I must have missed in this school before my arrival, or the things that might have happened in my old school since I've been gone."

        n "I wonder where these feelings come from, since I didn't leave much behind."

        n "I have a lot more here that I like. If that wasn't the case, then I wouldn't even bother with something like Student Council, or Shizune and Misha. I would be hard pressed to care about anything, if this school was how I imagined it would be."

        n "So even this feeling of a daily routine makes me glad, in a way."

        n "I dread the amount of work that's going to hit me in Student Council after school, enough to want to consider stepping out on my duties, just this once. Yet it's nice to feel like there is something I can do."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl clear
        nvl hide dissolve

        show shizu basic_normal
        with charaenter

        "Shizune drops a stack of attendance sheets next to me."

        show shizu adjust_happy
        with charachange

        ssh "Thanks again for helping out."

        show shizu at tworight
        show bg at bgright
        with charamove

        show misha hips_grin at twoleft
        with charaenter

        mi "Thanks again, Hicchan~!"

        "Sure is a lot of work, though. I had to skip out on sign language class again, but now I'm at a level where I can understand most of Shizune and Misha's conversations with each other, so I'm not too bothered by it."

        "Shizune still doesn't know that, though. I'm determined to keep things that way until I'm very sure of my skills. Perhaps it's a little childish of me."

        show shizu behind_frown
        with charachange

        ssh "Tanabata is in less than five days, but they're only going to start building the stalls tomorrow."

        show misha sign_smile
        with charachange

        mi "Hicchan, we might have to help out with building stalls again starting tomorrow."

        hi "Why? What was the point of taking them apart then? That took days, didn't it?"

        show misha hips_grin
        with charachange

        mi "Yup! That's right~! Even though Hicchan wasn't there for it~."

        hi "I would have helped out if you asked."

        show shizu basic_normal
        with charachange

        ssh "It wouldn't have made sense to bore you with cleanup duty after you enjoyed the festival so much."

        show misha hips_smile
        with charachange

        mi "It wouldn't have made sense to bore you with making you clean up right after the festival, it would have ruined the fun."

        show shizu behind_smile
        with charachange

        ssh "Besides…"

        show misha hips_grin
        with charachange

        mi "Ahahaha~! Hicchan is lazy anyway, you would have tried to run away again~! Shicchan doesn't like playing foxhound."

        hi "That stings."

        show shizu adjust_smug
        with charachange

        "Shizune covers her mouth with her hand and starts shaking. It takes me a second to realize she's laughing, mostly because she's doing so completely soundlessly."

        "It's a little strange to see, but more or less the same good-spirited kind as Misha's, without being eardrum-piercing."

        show misha sign_smile
        show shizu adjust_happy
        with charachange

        mi "Hm~, that's a good question, though, Hicchan."

        hi "Huh?"

        show misha hips_grin
        with charachange

        mi "Stalls~!"

        show shizu basic_normal2
        with charachange

        ssh "It's a storage issue. The school doesn't have anywhere to store so many stalls, since each one is pretty large. They won't pay for outside storage either, so this is what they decided on. It's inefficient, but cheaper."

        show misha sign_smile
        with charachange

        mi "Because~! the school doesn't have anywhere to store that many stalls, Hicchan."

        show shizu behind_frown
        with charachange

        shi "…"

        show misha perky_confused
        with charachange

        mi "Ah, yeah yeah~, right, they do, but they don't want to pay~! Sorry, Shicchan~…"

        show shizu basic_normal2
        with charachange

        ssh "It's because of the previous generation."

        show shizu behind_frustrated
        with charachange

        ssh "The leadership decided that outside storage costs had risen too much, and the Student Council before us was too weak-willed to tell them that it's stupid to have to build and disassemble sixty stalls twice every year."

        show shizu adjust_angry
        with charachange

        shi "…!"

        show misha cross_grin
        with charachange

        mi "Okay~!!"

        show shizu behind_smile
        with charachange

        shi "…"

        show misha perky_smile
        with charachange

        mi "Hicchan, let's eat something~! It feels like we've been working all day~…"

        hi "We have. Now that I think about it, I am hungry. I would have had lunch, but it was really crowded today for some reason, so I decided it wasn't worth the trouble."

        show misha cross_laugh
        with charachange

        mi "Ahahaha~! It was like that today because they had some especially interesting things for sale on the side."

        hi "Like what? No, don't tell me. I guess it doesn't matter, since I won't be able to eat them anyway."

        show shizu adjust_smug
        show misha hips_grin
        with charachange

        "Shizune looks oddly pleased with herself. I wonder what the context of that could be."

        show shizu behind_smile
        with charachange

        ssh "I prepared ahead of time for this."

        "Beaming with self-satisfaction, she produces a wide assortment of food from her bag. I can immediately see that ninety percent of it or more was taken from the lunch room."

        stop music fadeout 5.0

        "There's a lot, as well. Isn't there a limit on how much a person can buy?"

        "That means these gains are definitely ill-gotten."

        hi "The veal cutlet bread is always sold out in the first minute of lunch. I'm impressed you managed to obtain one."

        hi "Thank you."

        show misha perky_smile
        show shizu basic_sparkle
        with charachange

        "I reach for it quickly, but Shizune immediately makes a grab for it as well."

        play music music_another fadein 0.5

        show shizu basic_happy_close
        with characlose

        "Her hand goes slack for a second when it touches mine, but she immediately pushes forth with redoubled effort, that blazing, competitive spirit flashing dangerously in her eyes. Her fingers pry at mine, searching for an opening."

        "I don't budge an inch, prepared to fight for this bread with my life. I might never have another chance to eat this."

        "I am fully aware that if we continue like this, we could crush the bread, greatly reducing its edibility."

        hi "Misha… Tell her that unless she lets go, the bread is going to be crushed."

        show misha perky_confused
        with charachange

        mi "Hmmmmm? Why can't you do it yourself?"

        "I'm startled she can so nonchalantly let slip that I could communicate with Shizune just fine if I wanted to. I almost consider the possibility it was intentional, but I'm sure she was just distracted trying to tear the wrapper off a juice box straw."

        hi "Isn't it obvious? I can't let go of the bread."

        show misha sign_smile
        with charachange

        mi "I can't tell Shicchan that, then."

        show misha hips_grin
        with charachange

        "She puts her palms up to the sky and shrugs, a wide grin on her face."

        hi "Why not?"

        show misha sign_smile
        with charachange

        mi "Because~! You have a stake in this, so I can't trust you~! If Shicchan wants to reply, she has to let go of the bread, and then you win. Who knows, who knows, maybe that's what you want, Hicchan?"

        show misha cross_smile
        with charachange

        mi "It wouldn't be fair, so I'm going to be neutral! Like Switzerland~!"

        hi "Switzerland?"

        show misha perky_smile
        with charachange

        mi "Do you know about Switzerland?"

        hi "Of course I do… it's neutral, they're neutral."

        show shizu basic_sparkle_close
        with charachange

        "Shizune stares at me cockily, the tip of her tongue sticking out slightly from between her teeth as she continues to tug firmly at the veal cutlet bread between us."

        show shizu adjust_happy
        with charadistant

        "Suddenly, she lets go and holds her hands up, palms facing outwards. The universal gesture of peace."

        show shizu behind_blank
        with charadistant

        ssh "This seems like a poor way to settle this, doesn't it? And we might crush the bread."

        show shizu behind_frown
        with charadistant

        "She glares, and her passive expression quickly plummets into a disapproving grimace."

        show shizu adjust_angry
        with charadistant

        shi "…!"

        show misha hips_frown
        with charachange

        mi "Hicchan! Drop the bread! We are negotiating now!"

        "I drop the bread reluctantly."

        show misha perky_smile
        show shizu behind_blank
        with charachange

        "Misha's hand darts in from the side, her fingers drumming across the table as it makes its way over."

        show misha hips_grin_close
        with characlose

        mi "Ah~! Haha~! Don't mind me, I don't even really like veal. I'll just take this sandwich right here~! And something to drink, too…"

        show misha perky_smile
        with charadistant

        "Picking them up cautiously, she immediately retreats."

        "She has the right idea. I could just pick something else, there are lots of delicious things here. The chicken katsudon bread is also a popular seller, ranking high in taste and demand. But I've already eaten one before."

        show shizu basic_angry
        with charachange

        ssh "You're so immature, Hisao. This wouldn't be a problem if you would pick something else. The chicken katsudon bread is delicious."

        show misha hips_smile
        with charadistant

        mi "You're so immature, Hicchan. Why don't you pick the chicken katsudon bread instead? It's delicious~!"

        hi "But I have already eaten that."

        show shizu behind_frown
        with charachange

        shi "…"

        show misha hips_frown
        with charachange

        mi "Hicchan~! Why are you so obsessed with eating the veal cutlet bread, spe—ci—fi—cal—ly?"

        hi "It's hard to get normally. Rare things are more delicious."

        show shizu basic_frown
        with charachange

        ssh "You are acting like a child."

        show misha cross_frown
        with charachange

        mi "You're acting like a kid, Hicchan."

        hi "Why don't you eat the chicken bread?"

        show shizu adjust_blush
        with charachange

        ssh "That's not important."

        "Turning bright red, she smiles cunningly and continues."

        stop music fadeout 6.0

        show shizu basic_happy
        show misha perky_smile
        with charachange

        ssh "There is no reasoning with you. So it looks like there is only one way to settle this: we are going to play for it."

        show misha sign_smile
        with charachange

        mi "That doesn't matter: we'll play for it instead~!"

        "Somehow, I expected this. It's the logical conclusion."

        "Shizune has been studying for a long time, pretty much continuously up until now. With our finals over, I guess that surplus energy has to go somewhere."

        hi "Play what?"

        show misha behind shizu
        with None

        show shizu behind_blank_close
        with characlose

        ssh "The oldest game known to man, upon which the fate of nations has been known to rest: Rock, Paper, Scissors."

        show misha sign_smile
        with charachange

        mi "We'll play Rock, Paper, Scissors."

        show misha perky_confused
        with charachange

        mi "Really? That sounds so serious, Shicchan…"

        play music music_shizune fadein 1.0

        "There is no humor in her expression, she is dead set on this."

        hi "Okay, okay."

        show shizu adjust_happy_close
        with charachange

        "She draws her hand back, and I mirror her."

        hi "Go!"

        show shizu basic_angry_close
        with charachange

        "We both put out rock. A draw. I had thought I had the perfect plan. Rock is unbeatable. Shizune frowns, deeply upset by this unexpected turn of events. Not as planned?"

        show shizu adjust_angry_close
        with charachange

        ssh "Again!"

        show shizu basic_frown_close
        with charachange

        "Two papers."

        hi "Damn."

        show shizu adjust_angry_close
        with charachange

        ssh "Again!!"

        show shizu basic_frown_close
        with charachange

        "We both throw out two rocks again, but a third hand is among us representing scissors."

        show misha hips_grin
        with charachange

        mi "This looks like fun, can I play?"

        show misha cross_laugh
        with charachange

        mi "Hahahaha~!"

        show shizu behind_frown_close
        with charachange

        ssh "… … …"

        show misha perky_smile
        with charachange

        mi "It's a duel, Shicchan?"

        show shizu adjust_angry_close
        with charachange

        shi "…"

        show misha sign_confused
        with charachange

        mi "Eh~, dueling conduct? Hm~… You're right, you're right~! I really don't know…"

        show shizu cross_angry_close
        with charachange

        shi "…"

        show misha perky_confused
        with charachange

        "The faster she signs, the harder it is to follow. In fact, it looks like even Misha is having trouble keeping up."

        hi "What's she talking about?"

        show shizu adjust_angry_close
        with charachange

        ssh "One more time!"

        show shizu basic_frown_close
        with charachange

        "We tie again. Every time, Shizune demands a rematch, eventually skipping that step altogether and throwing rock, paper, or scissors out with increasingly reckless abandon."

        "Even playing completely randomly, we continue to tie. This is a mathematical longshot."

        stop music fadeout 8.0

        show misha hips_grin
        with charachange

        "Misha hovers above us, watching it all and laughing each time we draw. After sixteen rounds, Shizune pushes her chair away from the table and stands up."

        show shizu behind_blank_close
        with charachange

        shi "…!"

        show misha hips_smile
        with charachange

        mi "Enough of this, Hicchan~! I see what I have been doing wrong, this will all be over in the next round, so brace yourself, okay~? Okay~!"

        show misha sign_smile
        with charachange

        mi "I have studied your thought processes and~ I see how you play. I'm anticipating your next move and will combat it expertly."

        "This is all news to me, as I can't remember what we are doing this over."

        show shizu adjust_happy_close
        with charachange

        "Shizune grins confidently, a look of fearless daring on her face. Her cool eyes flash with pure competitive spirit as she draws her hand back, goading me wordlessly to do the same."

        "Her form is amazing, like a professional bowler or something, just to throw a hand motion."

        show shizu basic_happy_close
        with charachange

        "Two papers."

        play music music_comedy

        show shizu cross_stunned_close
        with charachange

        "Shizune's body immediately goes slack, and she rubs her temples with a look of exasperation on her face as she lets out a sigh so long it sounds like a tire deflating. I realize I've gotten a lot hungrier in the time we've been doing this."

        hi "We can just split it."

        show shizu behind_blank_close
        with charachange

        "I break the bread in half and offer one half of it to Shizune. She takes it."

        show shizu adjust_happy_close
        with charachange

        ssh "Thank you."

        "She looks at the bread in her hand, studying it."

        show shizu basic_normal2_close
        with charachange

        ssh "But this feels hollow, somehow."

        show shizu basic_normal2_close
        with charachange

        "Regardless of how she feels, she still eats it."

        "All of a sudden, I see Misha observing the scene out of the corner of my eye."

        show misha hips_grin
        with charachange

        mi "Hicchan~… That was very romantic, I think."

        hi "Oh, come on."

        show misha cross_laugh
        with charachange

        mi "Wahahahahaha~!"

        show misha hips_smile
        with charachange

        stop music fadeout 5.0

        "She laughs and takes a bite of her second sandwich."

        "We eat in silence for a while, Shizune and I managing to avoid any other contests. And then, we go back to work."

        scene bg school_council_ss
        with shorttimeskip

        play music music_tranquil fadein 3.0

        "As I finish up the day's usual filing, I think to myself that this might be Shizune's way of trying to start this week on a high note."

        "After all, tomorrow is when the real work will begin, and with her hands literally full building stalls, she won't be able to 'talk' very much."

        "It will likely be pretty dull and tiring, like it was the first time around. I'm appreciative of her effort, in that case. It's nice to have days like this, as a way of enjoying yourself before the days ahead. I think that was her idea as well."

        "…I also remember that I still have to get rid of Kenji's package. The damn thing is bulky, and somehow I've never been able to track him down since I picked it up."

        scene bg school_lobby_ss
        with locationchange

        "After Student Council is adjourned for the day, I walk towards the vending machines to look for something to drink, parting from Shizune and Misha. It's a short trip, but after even just a few seconds I start to get the feeling I'm not alone."

        scene black
        with hands_in

        "A pair of hands cover my eyes."

        mi "Guess who~!"

        hi "Shizune?"

        mi "Wahahaha~! It's me, Hicchan~!"

        hi "Yeah, I know."

        scene bg school_lobby_ss
        with hands_out

        pause 0.3

        show misha hips_frown_close_ss:
            center
            xpos 0.3
            easein 1.0 center
        with Dissolve(1.0)

        show misha at center

        mi "Then why did you say it was Shicchan~? It's okay to be wrong sometimes, Hicchan~! You're too proud."

        show misha sign_smile_close_ss
        with charachange

        mi "Anyway~, after Student Council, you don't usually have any plans, right~? So, you're just going to go straight to your dorm?"

        hi "Where else would I go?"

        show misha hips_grin_close_ss
        with charachange

        mi "Okay, that's great~! That's great, Hicchan~! I wanted to talk to you today, so this works out perfectly!"

        "Two high school students, alone after classes in a quiet, empty building. As the sun dyes the sky a romantic amber color, the cute girl says that she wants to talk."

        "What a secretive and appealing situation, my imagination is buzzing. It's likely not going to be anywhere near as exciting as I am making it out to be, but it's fun to play it up that way."

        play sound sfx_can
        show misha perky_confused_close_ss
        with Dissolve(0.2)

        "The popping sound of my canned coffee opening destroys any chance of maintaining such a cheesy mood, sounding louder than I'd have ever thought imaginable, amplified by the context of the situation. I sigh in disappointment and relief."

        hi "So, what is it?"

        show misha perky_smile_close_ss
        with charachange

        mi "Hm? Oh! Actually~… I'm a little behind in some of my classes, and if I don't catch up, it could be a problem~! I can't put it off any longer."

        show misha perky_sad_close_ss
        with charachange

        mi "My teachers say that I have to really start taking things seriously, so I should listen, especially~ because this is the third time."

        mi "Sorry~! I'm sorry, Hicchan."

        hi "Why are you apologizing?"

        show misha sign_sad_close_ss
        with charachange

        mi "I won't be able to help you or Shicchan with Student Council for a few days~. It'll only be for two or three days, really! I'll definitely try and come back as soon as possible! But~…"

        "I can't say I'm happy about this. It's supposed to be getting really busy this week too, isn't it? That's some unfortunate timing. For a second I want to ask if maybe Shizune could pull some strings to get her out of it."

        "But Misha looks so genuinely apologetic about it. It would be pretty dickish of me to say something like that."

        "Besides, if she says it's something that can't be put off any longer, I'm inclined to believe her, considering how surprisingly serious she can be with student council duties."

        hi "Yeah, I see. It's okay. You managed with just Shizune and yourself last year, didn't you? So I'm sure I'll be able to as well. Don't worry about it."

        show misha hips_grin_close_ss
        with charachange

        mi "Really? Thank you, Hicchan~! Really~! Yay yay~! I didn't know Hicchan would take it so well~! I thought you would be worried, with how there's going to be so~ much work, with Tanabata coming up and everything~!"

        "Damn, she knows me oddly well."

        show misha sign_smile_close_ss
        with charachange

        mi "…But~! Hicchan is so composed~! I'm glad~…"

        hi "Haha, yeah. You're sort of right, I was thinking about it, but it's not that big a deal. I'm not going to freak out over that."

        hi "It's going to be a little annoying passing that pad back and forth to talk to Shizune, though."

        show misha hips_frown_close_ss
        with charachange

        mi "Hicchan, just tell Shicchan that you can use sign language too! I don't understand why you won't."

        hi "Not yet. I can understand most things already, but I want to be really sure. Heh, actually, I wouldn't mind. The secrecy is killing me too, and it would be nice to be able to talk to her in a real conversation."

        hi "Don't worry, I'm going to have to tell her eventually. I want to. Actually, I'm trying to think of a good opportunity for it."

        show misha hips_smile_close_ss
        with charachange

        mi "That won't be a problem, Hicchan~!"

        hi "Why not?"

        stop music fadeout 3.0

        show misha sign_smile_close_ss
        with charachange

        mi "Well~, because I… kind of… told Shicchan that you could understand her. She was worried about the same thing, that you wouldn't be able to understand each other~! So~! I was worried, but it worked out fine in the end after all~!"

        show misha sign_confused_close_ss
        with charachange

        mi "Hahaha?"

        "I lose it."

        play music music_running

        hi "AAAAAAAAAAHHH!!"

        hi "Do you know how stupid I look now? I sat there for like half the damn day acting like I couldn't read sign language, and are you seriously telling me that she knew the whole time I could?"

        hi "She was probably thinking, 'this guy is a complete jackass, pretending he can't understand me.' I just made a total ass of myself."

        hi "How could you let me do this?!"

        show misha hips_frown_close_ss
        with charachange

        "Misha frowns, seeming lost for words on realizing that I'm taking this differently than she might have expected. She doesn't speak again until after seeing that I've calmed down."

        show misha hips_smile_close_ss
        with charachange

        mi "…But, Hicchan, I think this is definitely for the best~!"

        "She says without batting an eye, having waited patiently through my panic to say it."

        "The cheerful delivery of her words makes it seem like she sliced out the time between when she dropped the bomb on me and now. It's pretty funny, in a way."

        hi "You have such a one track mind, you know that?"

        show misha hips_grin_close_ss
        with charachange

        mi "Yes~!"

        stop music fadeout 4.0

        "The damage is done. If Misha can believe that things will work out with such unflinching surety, then maybe it's worth giving it a chance."

        "And if things don't work out, I'll run as fast as I possibly can…"

        "To try and make it up to me anyway just in case, she offers to buy me another drink from the vending machine. It's a very small token of apology, but I suppose it's the thought that counts, and her thoughts are sincere."

        "Plus it's a free drink, so I accept."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .interface:
        scene bg school_dormhisao
        with locationchange

        "I throw back my daily fistful of pills with a glass of water."

        "After a solid eight hours of sleep, I don't really know what I was so afraid of last night. As I chew a particularly large tablet in half, I continue to rationalize my worries away."

        $ renpy.music.set_volume(0.5, 0.0, channel="music")
        play music music_dreamy fadein 2.0

        nvl clear

        nvl show dissolve

        n "{vspace=30}Shizune knew I was taking sign language classes all day yesterday, and didn't make a big deal out of it."

        n "She might be mute, but that doesn't mean she can't make her feelings known. No, in fact, it seems like she's all the more direct for it."

        n "She doesn't beat around the bush or hold back, she always makes herself clear unapologetically, so there can be no mistakes."

        n "So, if she wasn't mad then, it's unlikely she would be at all. And on top of that, I didn't do anything wrong, anyway."

        n "But as that fear of mine recedes, the thought of spending a couple days with Shizune without Misha takes its place. I hadn't really thought about it yesterday, but the idea becomes more and more intimidating. It's true I can understand sign language pretty well, but…"

        n "I would definitely hesitate to say I can understand it above a basic level, and if she were to speed up her signing, which she does quite a bit, I don't think I could keep up."

        n "Signing, too, is not my strong suit. Doing both at the same time like Misha can is still a distant dream."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl clear
        nvl hide dissolve

        scene bg school_scienceroom
        show misha hips_grin at twoleft
        show shizu behind_smile at tworight
        with shorttimeskip

        mi "Hicchan~!"

        hi "What?"

        show misha sign_smile
        with charachange

        mi "Don't forget, you said you would help out with building stalls today~! Behind the school after classes are over, okay~?"

        hi "I know, I know."

        show shizu adjust_happy
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "Last time you helped out, Hicchan, we really appreciated it~! This time, it's even more important, so skipping out is unforgivable, okay?"

        "I want to ask why that is, but there isn't any opportunity to. Besides, Misha is behind in her classes, so it seems like a bad idea to distract her now that I know that. I can always ask her at lunch, which is what I end up doing."

        scene bg school_cafeteria
        show misha sign_smile at twoleft
        show shizu behind_blank at tworight
        with shorttimeskip

        mi "Because, Hicchan, a festival that celebrates a town is exactly what it sounds like. It's to celebrate your home and its history."

        show misha hips_grin
        with charachange

        mi "Tanabata is different, it's for wishes and lovers~! That definitely makes it more important, doesn't it? Yeah~, naturally, it would be~."

        hi "Is that really what it's for, though?"

        show shizu basic_frown
        with charachange

        shi "…"

        show misha cross_frown
        with charachange

        mi "Hicchan, you have no sense of fun…"

        "She puffs out her cheeks in displeasure before blowing the air out like a deflating balloon."

        show misha hips_frown
        with charachange

        mi "You have to appreciate things like that, even if it's just an excuse to eat interesting things and dress up in the end~!"

        show misha sign_smile
        with charachange

        mi "I'll be disappointed in you if you don't, okay?"

        stop music fadeout 5.0

        "Before I can say anything, she turns to the side to inhale a croquette."

        scene bg school_gardens2
        with shorttimeskip

        "After classes, I meet Shizune behind the school, where it seems she already set everything up sometime yesterday."

        show shizu adjust_happy at center
        with charaenter

        "She greets me with a short wave, and then with a flourish of the hammer already in her hand, extends her arm towards the stalls behind her, some of them already half completed, others still haphazard piles of board bundled together with string."

        hide shizu
        with charaexit

        show bg school_gardens2_ss as overlay:
            center
            alpha 0.0
            linear 20.0 alpha 1.0

        play ambient sfx_stallbuilding fadein 8.0

        "As time passes, I realize the pills can only do so much. I still get way more tired than should be normal. Luckily, Shizune's back is to me, so I can afford to take a lot of breaks without having to worry about her wondering why."

        "When I stop and think about it, though, I start to feel pretty guilty for taking advantage of her inability to hear that my hammer's stopped banging. It's a terrible thing to be happy about."

        "Her work ethic is admirable. It's obvious that it bores her, and even annoys her, but she doesn't slacken her pace. When she gets tired nailing a stall together with one arm, she switches to the other."

        hi "Shizune—"

        "I feel like an idiot the second I say her name."

        "I can't tell her what I think. There's a hammer in my hand as well, and in the end, I feel like I have to keep up with her."

        "I can't slack off either, especially when it's just the two of us. There's no time to sign, no opportunity. Not even for a compliment for a job well done."

        "Even something as casual as that would require me to put my hammer down, get her attention, and then sign it to her."

        "A simple gesture turned into something so needlessly complex, like a single footstep taken on a road that's longer than first imagined."

        "I've known her long enough to know this, and still forgot it."

        "The air is filled with the rhythmic knocking of nails being driven into wood."

        "It's actually kind of nice after a while. To pass the monotony of the task at hand, I try to match my hammering to Shizune's, then alternate it to try and form a beat. Of course, she doesn't notice."

        "It makes me wonder, does the lack of sound make this work seem more drawn out and boring to her?"

        stop ambient fadeout 3.0

        "Is it strange, being unable to hear the results of her actions even as she feels the vibrations through her fingers? Or, having no concept of sound, does it bother her at all?"

        "Distracted, I don't notice Shizune sneaking up on me until her head pops into view."

        scene bg school_gardens2_ss
        show shizu adjust_happy_ss at center
        with charaenter

        play music music_soothing fadein 5.0

        ssh "Taking a break?"

        his "Yeah, I guess."

        show shizu behind_smile_ss
        with charachange

        ssh "Okay, let's do that."

        show shizu basic_normal_ss
        with charachange

        ssh "You can understand sign language."

        show shizu behind_blank_ss
        with charachange

        ssh "That makes it more convenient for both of us. Even though you hid it from me."

        hi "Hahaha…"

        show shizu basic_normal2_ss
        with charachange

        ssh "Why?"

        his "Why what?"

        show shizu behind_blank_ss
        with charachange

        ssh "Why did you decide to take sign language?"

        "Her eyes don't break off from mine even for a second, if she needs to read my response, her peripheral vision is good enough. Once she has something in her gaze, she doesn't look away."

        "It's strange how piercing her eyes can be, dark as a lake at night."

        his "Because I wanted to. It seemed like it would come in handy. And it did, didn't it?"

        show shizu adjust_happy_ss
        with charachange

        ssh "Yes."

        show shizu basic_normal_ss
        with charachange

        shi "…"

        his "Sorry, I didn't catch any of that."

        his "See? This kind of thing still comes up now and then. I wish Misha was here."

        show shizu behind_blank_ss
        with charachange

        ssh "She has work to make up for, doesn't she? That might be partly my fault. Misha doesn't need supplemental lessons. Her grades aren't the best, but she understands how the decisions she makes affect others. That puts her ahead of many people."

        show shizu basic_angry_ss
        with charachange

        ssh "Especially certain blondes."

        hi "Ah…"

        "She doesn't forget things easily."

        show shizu behind_smile_ss
        with charachange

        ssh "Your sign language is very good. You're learning oddly fast."

        his "I've been taking classes for a while now. And it's kind of easy to pick up after awhile, through immersion, or osmosis, that kind of thing. It's not too bad."

        his "And if I'm really stuck, Misha's there, too."

        show shizu adjust_smug_ss
        with charachange

        shi "…"

        show shizu behind_smile_ss
        with charachange

        shi "…"

        "I guess I spoke too soon. I didn't understand any of that. Time to backpedal."

        his "Well, yeah, it's actually not that easy. It's actually hard as hell. Like trying to pick up broken glass."

        his "But I guess in some ways it's interesting, as well. Like an adventure. Well, no…"

        show shizu basic_normal2_ss
        with charachange

        ssh "Picking up broken glass is not an adventure."

        his "Sure it is. It's just as challenging."

        show shizu behind_blank_ss
        with charachange

        ssh "If you use a dustpan and a broom it's not."

        "I feel frustrated and sad."

        "When I look up, I notice she has a can of soda in her hand."

        hi "Where did you get that?"

        show shizu adjust_happy_ss
        with charachange

        "I forget to sign it, but she understands anyway, following my eyes, and produces another one from behind her back. She tosses it in my direction, and I catch it with both hands."

        show shizu behind_smile_ss
        with charachange

        ssh "I brought an extra one for you."

        play sound sfx_can

        "She pauses to slide her fingernail under the tab of her can and pop it open before setting it aside for a moment."

        show shizu basic_normal_ss
        with charachange

        ssh "If you are going to try and help me so much, then I have to look out for you too. It's only natural."

        show shizu behind_blank_ss
        with charachange

        ssh "If you're going to learn sign language, that is something entirely different. I'm naturally going to be impressed. What separates the two is obligation."

        show shizu adjust_happy_ss
        with charachange

        stop music fadeout 8.0

        ssh "I'm very happy."

        show shizu behind_smile_ss
        with charachange

        "She downs her drink in one go, stretches her arms behind her back and jumps to her feet."

        show shizu adjust_smug_ss
        with charachange

        ssh "OK! Back to work!"

        hide shizu
        with charaexit

        "And like that, it's over. Shizune returns to her work with the same energy as before, the lingering traces of a smile on her face the only evidence that she had taken a break at all."

        show bg school_gardens2_ni as overlay:
            center
            alpha 0.0
            linear 10.0 alpha 1.0

        "As I do the same, I think that Misha was right in saying everything would work out for the best. Everything so far seems to be going in that direction."

        "Misha swings by as it starts to get darker, looking just as tired as I feel, and Shizune decides to stop for today."

        "As we cover the day's work and go our separate ways, I look at how fluidly they talk to each other, and how easily they laugh together as they walk to their dorm."

        "It makes me appreciate Misha's skill at sign language more. I wonder if I'll ever reach that level, or if I even will have the time to."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .spring_into_action:
        play sound sfx_impact

        scene bg school_dormhisao
        with vpunch

        "The first thing I do this morning is trip once again over Kenji's package as I get out of bed, finding myself diving headfirst into the floor before I'm even fully awake."

        show kenjibox:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0

        pause 1.0

        show kenjibox at truecenter

        "I want to smack this thing with the first blunt object I can find, like I'm going for a home run, but I don't even have the energy for that this early in the morning… and it would likely damage whatever's inside. And that would be mean."

        show kenjibox:
            easeout 1.0 ypos 0.7 alpha 0.0

        pause 1.0

        hide kenjibox

        scene bg school_dormhallway
        with locationchange

        "I slide it into the hallway. It sails along the smooth floor with little difficulty and stops with a soft and almost inaudible bump on colliding with Kenji's door. Immediately, a dozen locks unbolt in succession like a mounting symphony."

        play music music_kenji fadein 0.5

        show kenji tsun:
            center
            xpos 0.4
            easein 0.5 center
        with charaenter

        show kenji at center

        ke "Who is it?"

        "He says, as he blindly steps forward into the hallway anyway, somehow stepping over the box in a way that would be uncharacteristically, impressively graceful if it weren't for the fact I know it was wholly accidental."

        hi "It's me, I got your mail. You're standing over it."

        show kenji happy
        with charachange

        ke "I know. Thanks a lot, man."

        hi "…Yeah, whatever."

        hi "So what's in it?"

        show kenji tsun
        with charachange

        "He cringes, instantly turning very defensive and agitated."

        ke "It's nothing."

        hi "Come on, tell me, I'm curious."

        hi "And you know, I almost broke my neck falling over it, and before that I had to carry the stupidly large box around with it blocking my vision, crossing roads with it in front of me… I think you can at least tell me what's inside in return."

        ke "It's secret stuff. I can't tell you, because then it wouldn't be very secret and shit. It's nothing important."

        hi "Well, if it's nothing important, you can tell me."

        ke "If it's nothing important, why do you have to know?"

        hi "Why is that wrong?"

        ke "Why do you have to know?"

        hi "Why can't I know?"

        show kenji neutral
        with charachange

        ke "Why are you answering my questions with questions?"

        hi "Why won't you answer my first question?"

        ke "Why won't you answer my last question?!"

        "I realize our voices are getting higher with each reply. Down the hall, a door pops open and someone sticks his head out quizzically to see what is going on."

        "We must look like such tools, but I bet I'm the only one out of the two of us with enough shame to realize it."

        hi "Fine, you can take it to your grave. I have to get ready for school anyway."

        show kenji tsun
        with charachange

        ke "Damn, no. Why are you so hasty to leave? Stick around a little. You want some coffee? It's been a while. You know, I thought you were dead since you were so slow with the package delivery."

        hi "You're lucky I was willing to do package delivery in the first place, smartass!"

        show kenji neutral
        with charachange

        ke "Whoa, calm down. Man, you are so confrontational. Is it because of the Student Council thing? I hear you hang out with them now."

        hi "You heard it from me. When I told you."

        ke "Really?"

        ke "Yeah, well, whatever, man. The point is they are terrible."

        show kenji tsun
        with charachange

        ke "You're the new guy, so of course you wouldn't know, but around here she's a very divisive figure. Before you came here, she tried to institute a badge policy. It's a long story, so maybe you should sit down."

        "I look around for a chair, but can't find one as we are in a goddamn hallway. I raise a finger and start thinking that maybe I should tell him that, but he's already started talking. Not wanting to waste the arm movement, I look at my watch instead."

        ke "It would have been a real reign of terror, if it had happened."

        hi "Wait, you're judging her based on something that didn't even happen?"

        stop music fadeout 8.0

        ke "Yes. Anyway, her idea was like merit badges, but there would also be demerit badges."

        hi "What would those do?"

        show kenji neutral
        with charachange

        ke "I don't know, it never happened. It seemed bad, though, so when I heard about it I didn't leave my room for a few weeks."

        hi "So you heard there would be massive change and hid in your room, trying to just ride the change out."

        show kenji tsun
        with charachange

        ke "Nah, I decided to do something about it. I found the student council office after a while and marched right in with a list of demands and a bunch of people I grabbed in order to make myself look like I had supporters."

        hi "Wait, so not only did it not happen, but no one even cared?"

        show kenji rage
        with charachange

        play music music_tension

        "Kenji doesn't hear me, having gotten a good momentum going. Wrapped up in the energy of his own ranting, he starts to completely flip out and flail his arms, appearing to wildly throw gang signs."

        ke "I walked up to the desk and said to her, 'Hey you, fascist woman! What is this badge idea? How out of touch can you be, here in your ivory tower, smugly looking down upon us like we're just a bunch of idiots? Who do you think you are?'"

        ke "'Your level of elitism is terrible, you're probably one of those outrageous rich people who have chaffeurs drive them around slums so they can point and laugh…'"

        ke "'…and only drink pricey coffee beans shat out by the last living dinosaur and brewed in a solid gold skull.'"

        ke "'And how could you? Go open up a history book; don't you know that the bourgeoisie are always overthrown in a bloody revolution for shit like this? Stupid! You're an idiot!'"

        ke "'Sure, the revolutionaries usually end up turning everything into an utter clusterfuck later on, but a maniac is the only kind of person who would create a policy like this…'"

        ke "'…it's like something I would create to make people suffer, only real and you want to institutionalize it! Where will this desecration of our rights end? We are people! This is not justice!'"

        show kenji neutral
        with charachange

        ke "That's what I said."

        show kenji rage
        with charachange

        ke "Then I added a cry of 'They can take our things, but they'll never take our freeeeeedoooooom!' to appeal to the masses like in that movie about the life of William Wallace where they took his things but not his freedom, and then killed him."

        stop music fadeout 5.0

        show kenji tsun
        with charachange

        ke "…But she just ignored me and didn't even look up from writing in her little paper shit."

        ke "Maybe I overwhelmed her with my logic, so badly that she just retreated into denial. Maybe she is just an asshole. Either way, she didn't reply, and the future refused to change."

        ke "To top it off, on the way back I realized I had lost my student ID somewhere. This is the story of my life. A constant and seemingly futile struggle. Like trying to climb up a brick wall with sponges for hands."

        hi "Hey, you said nothing changed, but she didn't make everyone wear a bunch of stupid badges. So, it did change."

        play music music_kenji fadein 0.5

        show kenji happy
        with charachange

        ke "Yeah, that's true. Okay, maybe they're not so bad, then."

        "I guess that counts for something, if I can get Kenji to admit that maybe two women may not be so bad after all. I'll take it. Especially if it allows me to slip out of this conversation; I didn't realize how much time had gone by."

        stop music fadeout 2.0

        scene bg school_dormext_full
        with locationchange

        "I try to run through my usual morning routine as quickly as possible. I check my watch again as I leave the dorms and see that I'm already late."

        scene bg school_scienceroom
        with shorttimeskip

        play music music_daily fadein 1.0

        "Fortunately, the rest of the day goes more smoothly, and after classes are over, I head to meet with Shizune again."

        scene bg school_gardens2
        with locationskip

        "Behind the school, I catch her leaning against a completed stand with parts of it still flecked with bits of paper and tape, remnants of signs from the last time it was used. Absentmindedly spinning a nail in her hand, she hasn't noticed me yet."

        "The temptation to sneak up on her is unbearable. Years of watching foreign wildlife documentaries have prepared me for this. I'm downwind, conditions are favorable. However, the more I think about it, the more it seems like a bad idea."

        "If get caught halfway I'll look like an idiot, and if she doesn't know it's me, I could end up with an injury. Either way, I'll also look a little insensitive. So, it would probably be best not to try anything funny… as disappointing as it is."

        show shizu adjust_blush at center
        with charaenter

        "I walk in front of her, startling her a little."

        his "Why so surprised? Did I catch you slacking off?"

        show shizu behind_blank
        with charachange

        ssh "No, I was taking a break."

        his "You don't look like you even broke a sweat. That's some break there, president."

        show shizu behind_frustrated
        with charachange

        "Shizune's eyes dart back and forth momentarily, and I think I've managed to fluster her."

        "There's exasperation on her face, and a little tension as well, but she can't back down; that would be unthinkable for her. Her fingers dance across each other impatiently."

        show shizu basic_normal2
        with charachange

        ssh "You're acting competitive today. Are you trying to get my blood boiling? Do you want to make it a contest? We'll race to see who can construct the most stalls by sundown."

        his "No, no! I'm teasing you. That's okay, it's not a real Student Council if you can't tease the Student Council president a little. You agree, don't you?"

        show shizu behind_frown
        with charachange

        ssh "That isn't in the student council charter, so it isn't true."

        his "There is no charter!"

        "At least, I don't think there is. The only thing they pledge loyalty to are a stack of takeout menus."

        show shizu adjust_smug
        with charachange

        ssh "Anyway, it's good that you're finally here, even if you could have been earlier. Pick up a hammer and we'll resume where we left off."

        hide shizu
        with charaexit

        play ambient sfx_stallbuilding fadein 0.5

        "As we work assembling stalls again, I slowly realize that it's really much less work than I would have expected. In fact, according to Shizune, we should be done by the end of the day with a little luck."

        "The last time I did something like this for them, it took her, Misha, and myself almost four days to do it. It can't be just my imagination."

        stop ambient fadeout 2.0

        his "You know, this doesn't seem like that much work."

        show shizu behind_blank at center
        with charaenter

        ssh "Because it isn't."

        play ambient sfx_parkambience fadein 10.0

        "That answer leaves me wanting a little more. Knowing that it isn't the best, Shizune puts down her hammer to elaborate."

        show shizu basic_happy
        with charachange

        ssh "It would be impossible for two people to do that much work in less than a week. The truth is that I don't dismantle half the stalls, I just store them someplace else. Actually, more like I hide them in plain sight."

        show shizu adjust_smug
        with charachange

        "She waggles a finger mischievously."

        show shizu adjust_happy
        with charachange

        ssh "But that's a secret, and it's not proper to reveal the tricks of the trade."

        his "You're not a magician."

        show shizu behind_smile
        with charachange

        "Winking, she takes out two plastic containers from her bag, then puts them down on a nearby board before raising her hands slightly as if to say 'ta-da!'"

        show shizu adjust_happy
        with charachange

        ssh "I made lunch today for both of us."

        show shizu behind_smile
        with charachange

        ssh "You can have this one. The food shifted in my bag and now some of it is mixed together."

        "She hands me one of the containers. I open it. It looks delicious, if a little simple. She hands me a pair of chopsticks, as if she had just remembered to, and I eat what looks like some grilled beef."

        his "It's very tasty."

        his "You don't like your food touching other food?"

        show shizu basic_normal
        with charachange

        ssh "I do not."

        his "You're very picky."

        show shizu behind_blank
        with charachange

        ssh "Sometimes I mix my food on my own, but not always, and not everything. I don't like it when it's done for me. What is important is the choice."

        show shizu basic_normal
        with charachange

        "She points decisively to emphasize it, and then breaks her chopsticks apart to eat her own meal."

        "As I continue to eat, I notice two things. The first is that almost everything I'm eating besides the rice is fried. Even the vegetables are fried."

        "And there's so much meat. Does she eat this kind of stuff all the time? I wonder how she manages to stay so thin in spite of it."

        "The second thing I notice is that I can't talk to her while eating. Talking with your mouth full is a little rude anyway, but with our hands holding our chopsticks and bowls, communication between us is impossible. Just like yesterday."

        "Even though we're spending time together, even though I took the time to learn sign language, it feels like I'm talking to her less. Despite that, it also feels like I'm understanding her more."

        stop music fadeout 4.0

        show shizu at tworight
        show bg at bgright
        with charamove

        show lilly cane_smileclosed at twoleft
        with charaenter

        "I hear the sound of something tapping against one of the stands and look up to see Lilly standing off to my side, feeling her way around with her cane."

        hi "Hi."

        "I narrowly catch myself before I can say 'didn't see you there.'"

        show lilly cane_surprised
        with charachange

        li "Oh, Hisao, is that you? I thought that I smelled something delicious cooking, and wondered who it might be."

        show shizu behind_frustrated
        with charachange

        ssh "What is she saying?"

        play music music_happiness fadein 6.0

        "It's hard to move my hands in parallel to saying something completely different to Lilly. This has to be why Misha just signs everything all the time. A bit sillier, but it seems like it would simplify things a lot."

        show shizu basic_happy
        with charachange

        "Shizune tents her fingers delightedly at my translation, as if from hearing a joke."

        show shizu adjust_smug
        with charachange

        ssh "All of this food was cooked hours ago, but for someone as slow as yourself, who can't even turn in a piece of paper without being a week late, I guess your perception of time would have to be a little different!"

        hi "That's… not very nice."

        show lilly cane_displeased
        with charachange

        "A frown crosses Lilly's face in response to a reply to something she didn't hear."

        hi "Ah, sorry. I'm just having a late lunch here. The Student Council president cooked everything."

        show lilly cane_reminisce
        with charachange

        li "Is the Student Council president here right now?"

        hi "She's right here."

        show lilly cane_listen
        with charachange

        li "I apologize, I didn't notice. Normally her level of presence is much higher. I was not aware that the Student Council serves lunch outdoors, why wasn't I invited? I think that it is good to have enough free time to be able to do things like this, however."

        show shizu behind_frustrated
        with charachange

        ssh "What is she saying?"

        "…"

        show shizu basic_angry
        with charachange

        ssh "If I were to invite you anywhere, you would just show up late."

        "But Shizune's words are outside of Lilly's perception, a fact that is by the second increasingly maddening to her."

        show shizu behind_frown
        with charachange

        ssh "Translate for me completely, please."

        "What polite phrasing. It's a shame she's essentially asking me to let her fully release the dogs of war. Still, I can't just do nothing. The feeling of being unable to even respond and be understood is so isolating. She would never forgive me."

        "I'll just try to soften her words a little."

        hi "Well, actually, this was all cooked a while ago."

        show lilly cane_weaksmile
        with charachange

        li "Really? That's nice."

        show shizu cross_angry
        with charachange

        ssh "Turn over here, it's very disrespectful to not look at the person you're speaking to. That isn't the way a prim and proper lady should conduct herself."

        hi "Half of what I'm saying is really what Shizune is saying. She doesn't like it when people don't look in her direction when she's trying to make a point. She's, uh, to the right of my voice."

        "Although in this case I can understand why Lilly wouldn't. This is a very awkward situation and it's daunting being the sole conduit for dialogue between the two of them."

        "Truthfully, I had forgotten what happened the last time they butted heads like this. It's clear Shizune remembers, and Lilly is being pretty hostile herself, in her own way."

        show lilly cane_displeased
        with charachange

        li "I'm sorry, such formalities slipped my mind completely. I forgot that the Student Council president is the type of person who would demand such respect and adherence to the rules at all times."

        show lilly cane_listen
        with charachange

        li "I suppose student government requires you to keep a tight ship. Then again, she certainly has time for her own fun as well, so that must not be completely true."

        show shizu adjust_angry
        with charachange

        ssh "Student Council is not a dictatorship, nor a zero-sum game!"

        play sound sfx_snap

        "Shizune points at Lilly with her finger out like the barrel of a gun and snaps her fingers explosively, causing her to flinch and become visibly upset."

        show lilly back_listen
        show lillyprop back_cane at twoleft
        with charachange

        li "Is that so? Then that makes it more impressive that you have been a part of it for so long, playing it as though it were one. I admire the fact that you are so tenacious. To manage it all, you must be so responsible as well."

        show shizu behind_frown
        with charachange

        ssh "Not as much as I would like to be. You can't complain about yourself, though, can you?"

        show shizu cross_rage
        with charachange

        ssh "You're very responsible; actions like requesting a deadline to be extended and then running all the way through to the next deadline? That's the very model of responsibility!"

        hi "Shizune is happy to hear that. But, apparently you're pretty responsible yourself, she says."

        show lilly cane_surprised
        hide lillyprop
        with charachange

        li "Does she really?"

        hi "More or less…"

        "Lilly doesn't seem very happy."

        hi "We're not holding a cookout, we're just taking a little lunch break. We're actually out here building stalls for the festival."

        show shizu behind_frown
        with charachange

        ssh "You wouldn't know, since you never go outside. Did you run out of tea?"

        hi "Are you going into town? Shopping?"

        show lilly back_devious
        show lillyprop back_cane at twoleft
        with charachange

        li "No. As I said before, I was just passing by, in case you did not hear. I would hate to interrupt the Student Council president. You're not doing anything now, but you must both be very busy."

        show lilly cane_listen
        hide lillyprop
        with charachange

        li "In any case, Hisao, I'm sure that the Student Council president will be able to find or make work for the both of you if she needs to."

        show shizu cross_rageclosed
        with charachange

        ssh "I'll devour you!"

        hi "Yeah, very busy."

        "'Devour' is a hard word. I'm pleased that I can read it. This isn't time to celebrate, though, not over that. Instead, it looks like they might stop squabbling. I would drink to that."

        show lilly cane_listen
        with charachange

        li "Have a nice day, Hisao. Goodbye, Student Council president."

        hi "Thanks, you too."

        show shizu basic_frown
        with charachange

        ssh "Stay classy."

        hide lilly
        with charaexit

        show shizu basic_normal2 at center
        show bg at center
        with charamovechangefaster

        stop music fadeout 4.0

        "As soon as Lilly leaves, Shizune dives into the remains of her lunch as quickly as possible, as if each bite she shovels away is a means to forgetting any of this ever happened."

        hide shizu
        with charaexit

        "When she is done, she heads right back to hammering with the same mindset. It's good that she's working off her frustration, but now it doesn't look like she is in any mood to talk any more."

        scene bg school_gardens2_ss
        with shorttimeskip

        play music music_tranquil fadein 3.0

        "About two hours later, she stops, having mowed through the rest of the stalls nonstop in that time."

        "It still feels hard to approach her, and I think about how easily a conversation can die. After it took so long to be able to get her alone and speak to her directly, it almost hurts."

        show shizu basic_normal_ss at center
        with charaenter

        ssh "Your translation was good."

        his "Really?"

        show shizu adjust_happy_ss
        with charachange

        ssh "First class!"

        "She punctuates it with a thumbs up."

        show shizu behind_blank_ss
        with charachange

        ssh "…For your level."

        show shizu basic_normal_ss
        with charachange

        ssh "There aren't many deaf people in the school, and sign language classes have been on the edge of getting cut for a while now. I'm sure you don't have many classmates, am I right?"

        show shizu behind_blank_ss
        with charachange

        ssh "If you're only learning sign language now, your speed is going to be limited. That is why interest in it wanes, because it takes more effort than normal just to communicate. I imagine it's the same with all languages."

        show shizu basic_normal2_ss
        with charachange

        ssh "In such a situation, conversations in sign language are less … than they would inherently be to start with."

        his "I don't understand that word. Less what?"

        show shizu behind_blank_ss
        with charachangealways

        show shizu basic_normal2_ss
        with charachangealways

        ssh "Sp—{w=0.2}on—{w=0.2}ta—{w=0.2}ne—{w=0.2}ou—{w=0.2}s."

        show shizu behind_blank_ss
        with charachange

        ssh "Misha is the only person who can really capture it."

        his "Yeah, that's definitely true."

        show shizu behind_sad_ss
        with charachangealways

        show shizu behind_blank_ss
        with charachangealways

        "Her expression changes for a second, and changes back too quickly to digest, but I get the feeling that this isn't meant to be pursued."

        "What I really want to know about is…"

        his "Why do you and Lilly fight so much?"

        show shizu basic_frown_ss
        with charachange

        "Tensing a little and visibly frowning, Shizune tents her fingers and overlays them repeatedly as if shuffling an invisible deck of cards."

        show shizu behind_frustrated_ss
        with charachange

        ssh "Two fights that you know of aren't worth calling 'so much.' If you had been here last year you could say that."

        his "I heard it was a rough year. Something about how you tried to institute a badge policy."

        show shizu cross_wut_ss
        with charachange

        his "Ha ha, surprised? Well, I want to hear more about that later, definitely, but… you don't like Lilly very much, do you? Don't dodge my question."

        show shizu behind_frustrated_ss
        with charachange

        ssh "I'm not dodging anything."

        show shizu basic_angry_ss
        with charachange

        ssh "She was part of the Student Council until last year. We didn't get along very well. She wanted to keep doing things like the old Student Council did. The old Student Council was just so ineffectual. It was stupid, and insulting."

        show shizu behind_frown_ss
        with charachange

        ssh "I wanted to do more, and we had a fight."

        show shizu basic_frown_ss
        with charachange

        ssh "A lot of fights."

        show shizu adjust_angry_ss
        with charachange

        ssh "She couldn't do anything on time."

        show shizu behind_frustrated_ss
        with charachange

        ssh "Then, she said that what I wanted to do was meaningless, just extra busywork. Does this look like meaningless busywork to you?"

        "Shizune gestures around us."

        show shizu basic_frown_ss
        with charachange

        ssh "What's really meaningless is a Student Council that doesn't do anything. Weak, lazy, and boring. Especially boring!"

        show shizu adjust_angry_ss
        with charachange

        ssh "I couldn't get excited over sitting in a room with nothing to do, that's just a waste of time. Why would I even be there? It didn't get my blood flowing. Arguing with her does that!"

        show shizu behind_blank_ss
        with charachange

        ssh "If she could have been that motivated before, she wouldn't have to put so much dedication into being my enemy. But if she shows that much spirit, it's not a complete loss. At least it's something! It's still exciting."

        his "I see."

        his "And what about the badge thing?"

        show shizu adjust_happy_ss
        with charachange

        stop music fadeout 4.0

        "She laughs, covering her mouth with her hand as if to hide it. Her laughter is the only thing she regularly tries to hide."

        show shizu behind_smile_ss
        with charachange

        ssh "That was just a joke."

        show shizu adjust_happy_ss
        with charachange

        ssh "Having a little fun sometimes is important, too."

        stop ambient fadeout 0.5

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .past_imperfective:
        scene bg school_dormext_full
        with locationchange

        play music music_normal fadein 0.5

        "The next day, I end up having to hunt around a bit at the start of lunch when I find that my usual vending machine near the dormitory buildings is sold out of my usual favorite canned coffee. The detour takes longer than I expected."

        scene bg school_gardens
        with locationchange

        "Things have been so hectic lately that it takes some time for me to register why something smells different as I walk through the school gardens back to the cafeteria. The grass has been freshly mowed."

        "The realization makes me pause and watch for a bit. The odd group of students chatting or playing around on the grass and a couple of teachers conversing on the path ahead make for a very idyllic scene."

        stop music fadeout 2.0

        "Unfortunately, a feeling of imminent dread starts creeping up on me after a while. The feeling that I'm not alone."

        play music music_kenji fadein 0.5

        show kenji neutral at center
        with charaenter

        ke "Hey, Hisao, is that you?"

        hi "Yeah, it's me."

        "I guess I should be happy it's him and not, say, a slasher. Kenji begins talking as if he's having a conversation with someone other than me."

        show kenji happy
        with charachange

        ke "Knew it. That haircut is unmistakable. No normal person would have a haircut like that."

        "Unconsciously, I start touching the back of my head. Once I realize what I'm doing, I feel insulted, yet too surprised to even get indignant about it."

        hi "Yeah… What are you doing here?"

        show kenji neutral
        with charachange

        ke "Measuring the temperature."

        show kenji happy
        with charachange

        ke "Winter will come soon. It will be too cold for women to go out and have their Sex and the City-style power lunches, followed by obstructive human wave formation walks in crowded urban areas."

        ke "When this happens, man will be able to walk the streets unfettered once again, and reclaim what is his heritage."

        show kenji neutral
        with charachange

        ke "In order to prepare for that day, I've been eating nothing but pizzas for the past week, to store energy."

        hi "Okay."

        hi "That's what bears do."

        show kenji happy
        with charachange

        ke "So? There is much we can learn from the bear."

        "Kenji nods, emphatically agreeing with himself."

        show kenji neutral
        with charachange

        ke "Okay, so check this shit out: I was in town today, buying milk. They had a new clerk, some hipster girl with a baseball cap with two hockey sticks on it. I'll call her hipster hockey baseball hat girl."

        ke "I noticed the milk didn't have a price tag, so I told her to get over there and label that milk, for future generations."

        "He was in town today? He must have cut his morning classes. I want to scold him, but his verbal torrent prevents me from getting a word in."

        show kenji tsun
        with charachange

        ke "She told me not to bother her, because she was sick. Sick? Sick!? We live in a society, here. You can't just opt out of human interaction because you're sick. Do you know how much effort it takes me to even get up in the morning?"

        show kenji rage
        with charachange

        ke "I still do, though, and I got up that morning to go down there and buy milk, not to have my vital questions just brushed aside by some hipster doofus college girl who wears a {b}hockey baseball cap{/b} to work. {b}Indoors{/b}."

        show kenji tsun
        with charachange

        ke "Anyway, I was just trying to uphold the integrity of her products. A milk carton without a price tag? When I see something like that, it just leads to questions. Important questions. It's her job to answer them, dammit."

        ke "That's the problem with women, they have no sense of duty."

        show kenji neutral
        with charachange

        ke "I get diarrhea a lot, but you don't see me complaining about it. I soldier on and do what I have to do anyway, because that's what being a man is all about. Even if you have diarrhea, you keep going, for the dream of a better tomorrow."

        hi "You know, frequent diarrhea is bad."

        hi "Maybe you should stop drinking so much milk."

        ke "I can't do that, it's what allows me to maintain my awesome strength. And in this world… a man's strength is the only thing that can't be browbeaten out of him by an increasingly pussywhipped society."

        show kenji happy
        with charachange

        ke "That's why I walk around leaving open jars of olives everywhere. Sometimes just to show that I can."

        hi "Do you refrigerate after opening?"

        show kenji tsun
        with charachange

        ke "What? Man, I don't know, that's not important."

        hi "You have to refrigerate after opening. Even elementary school kids know that."

        show kenji neutral
        with charachange

        ke "They can't get the jar open in the first place, so it doesn't matter."

        hi "Ah, that's true."

        show kenji happy
        with charachange

        ke "I'm a genius."

        "He self-assuredly rubs his chin, which is something I imagined scientists did, until I met Mutou and was tremendously let down."

        show kenji neutral
        with charachange

        ke "Anyway, I can't go to that store again, since it's clearly been compromised by bitches. Unless… I disguise myself. Maybe change to a different pair of glasses."

        hi "Worst disguise ever."

        show kenji tsun
        with charachange

        ke "Pffft, it's been working flawlessly all these years. I don't even need glasses to see. They're for effect. Also, to protect my identity. I'm like Superman."

        hi "Worst disguise ever."

        show kenji happy
        with charachange

        ke "I'm telling you, when people see my school ID, they can't even recognize me."

        hi "Really? Let me see."

        show kenji neutral
        with charachange

        ke "Can't do that. I can't go around showing my ID to everyone. It was made long ago. In a different time. I had hippie hair."

        stop music fadeout 2.0

        "While I'm trying to imagine that, Kenji takes his glasses off."

        scene evbg kenji_glasses:
            truecenter
            zoom 0.82
            acdc_warp 20.0 zoom 0.8
        show evmg kenji_glasses_closed at kenji_mg_out
        show evfg kenji_glasses:
            truecenter
            zoom 1.0
            acdc_warp 20.0 zoom 0.8
        with whiteout

        play music music_friendship

        "He squints as soon as they're off his face, which makes him look even more tired than he already does. He was right; he does look very different. Kind of like he hasn't slept in years. Not different enough for it to be a good disguise, though."

        hi "You need more sleep."

        show evmg kenji_glasses_frown at kenji_mg_out
        with charachangeev

        ke "Nah."

        hi "You look like you need it."

        show evmg kenji_glasses_normal at kenji_mg_out
        with charachangeev

        ke "No way. These are just the eyes of a man who has seen things. A shaman's eyes. Terrible things, that you can't imagine."

        ke "Like when I made a ship in a bottle and my mom sat on it. There was blood and shreds of floral print everywhere. That's what life experience is."

        "Kenji doesn't seem very horrified, even though I think this is actually the first thing he told me about himself that could have been legitimately traumatic."

        "He's also talking about thirty degrees to my left, so I guess his blindness is real. I wave a hand in front of him anyway, to little effect."

        ke "Man, I hope you realize I'm just joking."

        "I laugh, pretending that I did. Somehow, looking him in the eyes is more difficult than usual."

        show evmg kenji_glasses_closed at kenji_mg_out
        with charachangeev

        ke "Want some trivia? People with small eyes wear big glasses."

        hi "I've read that somewhere. It's because it makes your eyes look less beady."

        ke "Really? I didn't know that."

        stop music
        $ renpy.music.set_volume(0.5, 0.0, channel="sound")
        play sound sfx_scratch

        scene bg school_gardens
        show kenji tsun at center
        with locationchange

        $ renpy.music.set_volume(1.0, 2.0, channel="sound")

        "He puts his glasses back on, and I feel oddly relieved for a moment until I remember that I still have to deal with him, glasses or not."

        play music music_kenji fadein 2.0

        ke "Well, anyway… This artist girl wanted to paint my portrait once, I think. I had to talk to her like five times before she started making sense."

        "Must have been Rin, I suppose."

        hi "What'd she look like?"

        show kenji neutral
        with charachange

        ke "I don't know. A woman with sandals."

        "I was hoping he'd say something more specific, like 'she had no arms.' Rin does wear sandals, but I feel like the chance of there being another freespirited female art student wearing sandals besides her is reasonably high."

        show kenji happy
        with charachange

        ke "I was thinking, sure. Someday, after I burn all documentation that I exist, it might be okay to leave a portrait behind, so that people can look at it and remember the savior of mankind. They'll need it to model the statue."

        show kenji neutral
        with charachange

        ke "Then I thought about it some more and had to turn her down. It was tempting, but she wanted it for some school thing. It would be displayed."

        show kenji tsun
        with charachange

        ke "People would ask who I was, only I haven't saved society yet, so it would be pointless. And then if someone recognized me, I'd have to explain myself."

        ke "That's already a chain of events I don't want to deal with. I don't want to get mixed up in some weird situation; shit like that always happens. Sticking out is a surefire way to get put on a list."

        show kenji neutral
        with charachange

        ke "That's why I make such a careful effort to blend in with people in my daily life. Until I can make my move."

        hi "Sure."

        hi "What list?"

        ke "There are many lists."

        show kenji happy
        with charachange

        ke "So what are you doing here, anyway?"

        hi "Nothing. I kind of got here by accident."

        ke "Happens to me all the time. Well, hope that works out for you. I think I'm going to go back to my dorm room. I need to set my TV to record my shows."

        hi "You have TV?"

        ke "Yes, you should come over sometime, we can watch the game. In high definition."

        stop music fadeout 4.0

        hide kenji
        with charaexit

        "Before I can ask him what he's talking about, he's gone. He left like he came: with zero respect towards other people. Kind of amazing."

        "Now that Kenji is gone, I resume looking aimlessly at the school gardens in their summer splendor. It's no use, he ruined them for me."

        scene bg school_cafeteria
        with locationchange

        $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
        play ambient sfx_crowd_indoors fadein 1.0

        "When I get back to the cafeteria, exhausted but alive, I think of eating lunch with Shizune again, but find her sitting at a table with Misha already."

        "If it were anyone else, I would think how they were too far away for me to hear them. This is Shizune and Misha, however."

        "If I wanted to, I could 'eavesdrop' on their conversation easily. What a dirty thing to think about, but it's there. …I don't want to, though."

        "They must have a lot of catching up to do, even if it's only been a few days. I'm inclined to just leave them alone so they can do just that."

        "However, the second they see me, they wave me over."

        show misha hips_grin at twoleft
        show shizu basic_normal at tworight
        with charaenter

        stop ambient fadeout 5.0
        play music music_shizune fadein 1.0

        mi "Hi, Hicchan~!"

        "Hearing her voice again even after such a short time apart is jarring, and I wince."

        "These past few days, I had forgotten that communication with Shizune is almost entirely silent, and concentrating on getting it right, I had tuned out even ambient noise."

        "Well, I'll get used to it again. I'm glad she is back."

        show misha sign_smile
        with charachange

        mi "I'm done making up all my work~! Just in time~, I won't have to miss the festival. Wahaha~."

        show shizu adjust_smug
        with charachange

        ssh "If they really tried to enforce that, I would pull you out on student council business."

        show misha perky_confused
        with charachange

        mi "If they really really tried to enforce that, you would pull me out on student council business~?"

        hi "That's abuse of power."

        show shizu behind_frown
        with charachange

        shi "…"

        show misha hips_frown
        with charachange

        mi "No it isn't, Hicchan~!"

        show misha sign_smile
        with charachange

        mi "Shicchan says that if there were only two Student Council members overseeing the festival, it would be a problem, wouldn't it? Yeah~, definitely! It has to be at least three! It's for the good of everyone, it's perfectly reasonable, it's necessary~!"

        show shizu adjust_happy
        show misha perky_smile
        with charachange

        "Shizune leans across the table a bit as Misha delivers her slightly disturbing, militaristic justifications in a childish, bubbly, up-and-down tone."

        "Shizune looks so happy, though, tenting her fingers and trying to hold back a laugh as Misha pouts more seriously on her behalf."

        hi "If you say so."

        "I'm actually happy right now, that we can talk so easily to each other. All three of us."

        "In the beginning I thought that I might have found myself in a bad situation. I was sure that Shizune would hate getting saddled with being tour guide for the new guy."

        "I didn't want to be that kind of burden, either. It would be awkward even if she weren't deaf and mute, too."

        "Just now, she said that we would all have to be at the festival, the whole Student Council. I don't think that the Student Council has any real jurisdiction over Tanabata. It's only Shizune's way of saying that she wants us to spend it together."

        "It's nice to have friends."

        "It's a simple thought, but one that makes me genuinely happy, that we could slip into being such with so much ease. Despite the roundabout way in which she said it, I'm glad that Shizune thinks it strongly enough to express it at all."

        show shizu basic_normal
        with charachange

        ssh "Why did you wait until we waved you over to come sit with us?"

        "A question out of nowhere. Shizune's eyes are expectant as Misha repeats her message. I feel like teasing her."

        hi "You want me to sit with you that badly?"

        show shizu behind_blank
        with charachange

        ssh "We're in the Student Council. We should sit together as much as possible. It's logic."

        show shizu adjust_happy
        with charachange

        ssh "Anyone would jump at the chance to sit with two cute girls anyway."

        "She pauses, in case I might say something like 'You're not that cute!' and instantly lock myself into an obvious no-win situation. When I don't take the bait, Shizune becomes more energetic and continues."

        show shizu basic_happy
        with charachange

        ssh "You're abnormal."

        "Well, I didn't expect her to end it like that."

        hi "You're too quick to call other people abnormal. So arrogant."

        show shizu adjust_smug
        with charachange

        ssh "You're too quick to call other people arrogant. That makes you arrogant, and arrogance is also abnormal. You're double-abnormal."

        hi "It doesn't work that way. It's a sliding scale."

        show misha hips_grin
        with charachange

        mi "Hahaha~."

        "Leaning on her arm, Misha closes her eyes and lets out a low, slow laugh like a chuckle."

        hi "Don't laugh…"

        show shizu behind_blank
        with charachange

        ssh "Don't laugh in this kind of situation."

        "I notice that Misha signs everything I say to Shizune anyway, even though I'm signing myself. This is redundant, but it's an unconscious action for Misha. On the other hand I can't stop."

        "If I let myself take it easy and sign less just because Misha is back, then what was all this for? I don't want to risk losing familiarity with how to sign either. My hands are pretty slow to speak on my behalf as it is."

        show misha sign_smile
        with charachange

        mi "Hicchan, you and Shicchan talk to each other much more now~! Back and forth, it's really funny too! Like an old married couple, right~ right~?"

        "What a loaded comment, in so many ways. Although, because it's Misha, it can't have been on purpose."

        hi "That's not a compliment."

        "Shizune doesn't react to Misha trying to pair the two of us up. Maybe she didn't see it. Sometimes it does happen, I've noticed. I still wonder if it's really that simple, and why I care so much, but I don't want to think about it too hard."

        "I want to leave. I keep thinking that I'm hogging Misha's time with Shizune, and it could be that Misha cut in just now on purpose, feeling that way too. I doubt that either of them will let me leave, though. In some ways they're too nice."

        hi "Anyway, Shizune, if you really want to know, I didn't want to sit here because I didn't want to intrude."

        hi "I thought that because of Misha being away for supplementary lessons or whatever, you two would have a lot to talk about, and I should just leave you alone to catch up. That's why I thought I would just hang back."

        hi "Don't worry, Misha, I'm not trying to monopolize Shizune."

        show misha cross_laugh
        with charachange

        mi "Wahaha~! Hicchan! It's not like that~."

        show shizu basic_normal
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "You're so considerate, Hicchan! Shicchan is sorry~ and apologizes."

        hi "I don't really think it's worth apologizing over, so, don't worry about it. Hey, don't you both think that since Misha is back, we should go celebrate somehow? I think so."

        show misha cross_frown
        with charachange

        mi "Hicchan~! Usually, having to make up work isn't something to celebrate over."

        show shizu adjust_happy
        with charachange

        ssh "No, it's a good idea."

        hi "The timing is perfect, and Shizune said that the Student Council should have a little fun too sometimes. You've probably heard that too, right, Misha? It should be fine."

        show shizu behind_blank
        with charachange

        shi "…"

        hi "Actually, wait a second. Didn't you have to make up work because you were missing so many classes to begin with? So, skipping out to celebrate would be kind of stupid. Maybe the timing isn't perfect, like I said, but we could go after school."

        show misha sign_smile
        with charachange

        mi "Where should we go?"

        "Misha speaks Shizune's question to her aloud before she even stops to think it over, both of them completely ignoring me."

        hi "Hey, listen to me, two-man shortsighted Student Council team!"

        show shizu adjust_smug
        with charachange

        shi "…"

        show misha hips_grin
        with charachange

        mi "Wahaha~! Hicchan, you're a part of this team, too!"

        hi "Ah, yeah. I guess I am."

        show misha hips_smile
        with charachange

        mi "Yeah yeah~! You are, Hicchan!"

        show shizu behind_smile
        with charachange

        ssh "So forgetful, and troublesome. I feel sorry for the girl who falls in love with you."

        show misha sign_smile
        with charachange

        mi "So~! Where do you think we should go?"

        "I'm laughing in spite of myself, wanting to point out how Misha seems so enthusiastic now, when she was the one who was most apprehensive about it just a few seconds ago. For whatever reason, I can't bring myself to do it. But, this is okay, too."

        stop music fadeout 4.0

        "After a short discussion on where to go, it seems like the only place all three of us know and are willing to travel to is the Shanghai."

        "A teahouse doesn't look like a bad place to celebrate, especially because I'm sure they sell cake there, and cake is the most celebratory food."

        scene bg suburb_shanghaiext
        with shorttimeskip

        "I haven't seen Yuuko in a while, either, and neither have the girls. For all these reasons, plus the fact that it's so close, I end up standing in front of the little tea shop with Shizune and Misha before I know it."

        play sound sfx_storebell

        scene bg suburb_shanghaiint
        with locationchange

        show yuukoshang neutral_down at center
        with charaenter

        yu "Welcome!"

        play music music_dreamy fadein 2.0

        "It's been a while since I heard Yuuko's voice, so I'm surprised all over again by the energy she puts into her greetings. Kind of like an extremely nervous Misha."

        show yuukoshang at tworight
        show bg at bgright
        with charamove

        show misha perky_smile at twoleft
        with charaenter

        mi "Hi~! But~! you don't have to do that all the time if it's just us."

        show yuukoshang worried_up
        with charachange

        yu "Yes I do…"

        show misha sign_confused
        with charachange

        mi "But—"

        show misha cross_laugh
        with charachange

        mi "Okay~! Okay~! If you say so, Yuuko! Hahahahaha~!"

        "I take this moment to glance around the teahouse and notice that it is as empty as ever. It's lunch time; essentially the peak hour for an establishment of this type. And yet, it's as barren as ever. I don't understand. There has to be a reason for this."

        show yuukoshang at center
        show misha hips_smile at left
        show bg at center
        with charamovechangefaster

        show shizu behind_blank_close:
            yalign 1.0 xpos 1.0 xanchor 0.8
        with charaenter

        "Shizune gently taps my arm to get my attention."

        show shizu adjust_happy_close
        with charachange

        ssh "What do you want to get?"

        show yuukoshang neurotic_up
        with charachange

        "Yuuko looks a little agitated after Misha automatically relays the question."

        yu "N-no, I'm supposed to… ask that… Is there anything that I can do for you?"

        show shizu behind_smile_close:
            ypos 1.1
        show misha perky_smile:
            ypos 1.14
        with charamovechangefaster

        hi "Just some coffee for now, I guess. Thanks."

        show yuukoshang neutral_down
        with charachange

        "The dedication Yuuko has towards her waitressing duties is sort of admirable. So is the speed at which she whisks slices of cake and our drinks to our table when we order."

        hide yuukoshang
        with charachange

        show shizu behind_smile_close:
            closeright
            ypos 1.1
        show misha perky_smile:
            twoleft
            ypos 1.14
        with charamove

        "Then again, we're the only customers here. Who knows what it would be like with a full house."

        "Shizune and Misha immediately dig into their cakes with gusto, probably because they can't talk with utensils in their hands."

        "The whole point of sharing a meal with friends like this is being able to talk over it, after all. It makes sense that it would be the same with them."

        "I'm barely halfway through my cake when I hear their forks clinking as they set them down on their empty plates."

        hi "It's not healthy to inhale your food."

        show misha hips_grin
        with charachange

        mi "Hahaha~! Hicchan sounds like an old man~!"

        "I cringe and instantly feel like I've been punched."

        show shizu adjust_happy_close
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "Are you going to wear a yukata tomorrow, Hicchan?"

        hi "No, I don't even have one. Well, even if I did, I'm not the kind of guy who does stuff like that."

        hi "What about you? Are you two going to dress up?"

        show shizu behind_blank_close
        show misha perky_smile
        with charachange

        ssh "Of course."

        hi "What do you mean 'of course?' You didn't dress up last time."

        show shizu basic_normal2_close
        with charachange

        ssh "One time is not a trend! It's a completely different situation anyway. Aside from not being Tanabata, the festival was on school grounds; students should wear their uniform on school grounds."

        "Clearly a joke, but her delivery isn't any different from the usual. That isn't normal, but her sense of humor never was, and I'm used to it."

        "I guess her way of saying outrageous things seriously is a little better than if she were to say serious things outrageously."

        "What's more troubling in any case is that I've started to associate a voice with her signing, and it's clashing with how Misha says out loud everything Shizune signs anyway. I feel disoriented."

        show shizu behind_smile_close
        with charachange

        ssh "I'll dress up this time!"

        show misha sign_smile
        with charachange

        mi "I'll dress up this time~! You'll see, Hicchan!"

        show misha hips_smile
        with charachange

        mi "Not just Shicchan, but me too~!"

        show misha hips_grin
        with charachange

        mi "Maybe~ I'll change my hairstyle, too."

        hi "Don't do that, I can't really imagine you looking differently."

        show shizu adjust_happy_close
        with charachange

        "Shizune wags a finger and smiles."

        show shizu adjust_smug_close
        with charachange

        ssh "Such a quick and firm disapproval. What if I were to change my hairstyle?"

        hi "Maybe you should grow your hair out and make it look like drills."

        show shizu behind_blank_close:
            xpos 1.0 xanchor 0.8
        show misha hips_smile:
            left
            ypos 1.14
        with charamovechangefaster

        show yuukoshang neutral_up behind misha at center
        with charaenter

        "She looks unamused. Luckily, I see Yuuko making her way over, likely to clear our plates or ask if we need anything from her."

        hi "Yuuko, are you doing anything for Tanabata?"

        show yuukoshang panic_up
        with charachange

        yu "Huh?"

        "It's like she was practicing how to most smoothly ask if I needed a refill of coffee while walking over, but she has no idea what to do having been asked a question first. I feel bad."

        show yuukoshang worried_down
        with charachange

        yu "Yes, I'm… working…"

        show misha perky_sad
        with charachange

        mi "Yuuko~, they make you work on holidays? Awwww…"

        show yuukoshang neutral_down
        with charachange

        yu "W-we have the most business on holidays, and sometimes tourists. I don't mind. I have to do my best."

        show shizu adjust_happy_close
        show misha perky_smile
        with charachange

        ssh "I understand completely. So admirable."

        "Shizune nods her head in solidarity, feeling a kind of kinship with Yuuko through their shared determination to be the best, although for her it's a matter of pride whereas Yuuko might just feel that she really, really needs this job and maybe a raise."

        hi "The most business, huh? So, how many people on average during a holiday?"

        show yuukoshang neurotic_up
        with charachange

        yu "Ah, well…"

        show yuukoshang worried_up
        with charachange

        yu "…"

        hide yuukoshang
        with charaexit

        show shizu behind_smile_close:
            closeright
            ypos 1.1
        show misha perky_smile:
            twoleft
            ypos 1.14
        with charamovechangefaster

        "Yuuko walks away and starts cleaning a cup of swizzle sticks. That isn't polite. This is not what a proper waitress would do! Nevertheless, I sort of got my answer anyway. Clearly, business is scarce at best."

        "I start to wonder again how the Shanghai remains open at all. Maybe this eclectic style of teahouse is a trend that was outrageously successful before I got here but isn't any more, and they're just keeping it like this while they retool."

        "Maybe the owner is rich and is involved in some sort of bet with someone else or a crazy scheme to see who can lose the most money. Maybe I just conveniently miss mobs of customers by seconds each visit."

        "Or maybe this place is just a front for arms dealers."

        hi "Since there's no one else here, why don't you sit down with us?"

        "We can talk about economic infeasibility. …But Yuuko doesn't take the bait, shaking her head from side to side emphatically."

        show misha hips_grin
        with charachange

        mi "I've never really celebrated Tanabata before, or dressed up for anything like this~! I'll finally be able to wear my yukata. Yay yay~!"

        hi "What do you mean never? What about last year?"

        show misha sign_smile
        with charachange

        mi "Hm~… last year, Shicchan, me, and the 3-2 class rep ran a stall for the festival! It was a soba stall, I think~? Yeah, it was~! Yup!"

        show shizu adjust_blush_close
        with charachange

        "The blind class rep of 3-2 must be Lilly. I'm surprised they were able to work together on anything, but Misha would likely be the best possible buffer for that kind of thing, with how innocent she is."

        show misha hips_grin
        with charachange

        mi "Shicchan cooked, and Lilly took the orders, and I translated for them~!"

        show misha hips_smile
        with charachange

        mi "Shicchan kept saying, 'It's so inefficient~! Misha~! Why do you have to be the middleman? As in~, why is there a middleman in the first place? Huh~? It would be fine if I did the cooking and you took orders! It doesn't make sense at all!'"

        show misha sign_smile
        with charachange

        mi "But~! I think everyone had fun in the end. Right, Shicchan~?"

        show shizu behind_frustrated_close
        with charachange

        shi "… … …"

        "Shizune adjusts her glasses grudgingly, causing Misha to break into laughter."

        show misha hips_grin
        with charachange

        mi "It was the old Student Council's idea~! That's why~!"

        hi "So, what was the last Student Council like, then?"

        "Shizune finally decides to step in again, or it's more like she can't stop herself."

        show shizu basic_angry_close
        with charachange

        ssh "Terrible."

        "That was blunt. She ends with a chopping motion, as if passing judgment on them. I hope she's going to elaborate a little."

        show shizu adjust_angry_close
        with charachange

        shi "…"

        show misha sign_confused
        with charachange

        mi "At universities and some private schools, student councils can have control over millions of yen to budget and distribute as needed! Wow~! Really? Millions? Ah, right~! And they are much more involved in school activities, too, Hicchan!"

        "From Misha's tone, it seems like this is newer to her than it is to me."

        show misha hips_frown
        with charachange

        mi "This school's Student Council was like a joke in comparison~! Don't give people positions of power if they don't have any power at all! What's the point~?"

        show shizu behind_blank_close
        with charachange

        ssh "So…"

        show misha sign_smile
        with charachange

        mi "…I wanted us to have more and more work~! It was hard to convince the school and the other Student Council members to allow it. Actually~, a lot of the work you've seen us do really is work that I took on, which is what Lilly was talking about."

        show misha hips_grin
        with charachange

        mi "If it wasn't for Shicchan, the Student Council would just file attendance reports day in and day out~!"

        show misha cross_laugh
        with charachange

        mi "Hahaha~! Would you prefer that, Hicchan?"

        show misha sign_smile
        with charachange

        mi "Of course, Hicchan, as soon as the workload started going up, most of the Student Council stopped coming."

        show misha hips_laugh
        with charachange

        mi "Wahahaha~!"

        show shizu basic_normal2_close
        show misha hips_smile
        with charachange

        shi "…"

        "Shizune's fingers fold over each other carefully. It looks like she wants to add something, but she can't bring herself to."

        "Like she said, sign language gives you a little more time to think about what you 'say.' I guess she feels like she can't talk about this."

        show shizu behind_blank_close
        with charachange

        ssh "That was then, and this is now. Let's just have fun tomorrow."

        "That is what she finally settles for."

        hi "Yeah."

        show shizu adjust_happy_close
        with charachange

        shi "…"

        show misha perky_smile
        with charachange

        stop music fadeout 5.0

        mi "Okay~! Then, Student Council is ad—jour—ned? for today~!"

        show misha hips_grin
        with charachange

        mi "It has to be adjourned excitingly, because today was a good day."

        show misha cross_laugh
        with charachange

        mi "Ahahaha~!"

        scene bg school_road_ss
        with shorttimeskip

        "School seems to be over by the time we leave the teahouse, as I can see students coming down from the school as we walk up the road towards it."

        "A couple people wearing our school uniform look at Shizune as she walks by, and I wonder if they recognize her as the Student Council president or if their eyes are just being drawn to Misha's head."

        "It's impossible not to overhear the chatter in the air, and the topic is more often than not plans for Tanabata. I wonder how many of them will be using or going to the stalls that I reassembled."

        "It makes me feel a little pride, an emotion I've never felt doing something for school."

        "Maybe this is how Shizune feels as well. I almost want to ask, but it seems stupid to want to do so."

        scene bg school_courtyard_ss
        with locationskip

        "So I just hold on to the thought as the three of us walk onto campus and then separate; Shizune to the student council room, and Misha and me to our dorms."

        "It isn't until they're gone that I realize I again didn't ask when and where they wanted to meet up tomorrow."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .when_stars_embrace:
        scene bg school_dormhisao
        with openeye

        "Even though it is a holiday, I wake up at the same time as usual, on a day when everyone else is likely sleeping in for another six hours."

        play music music_pearly fadein 3.0

        "I take my morning regimen of pills for the first time in a few days. Admittedly, I'd let my medication slip my mind. Looking at the rows of bottles in front of me, I don't know how I managed to."

        "Seventeen different medications. I feel full enough to skip breakfast after taking all of them."

        "I'm already up, so I might as well take a walk."

        scene bg school_dormext_full
        with locationskip

        "The weather looks nice outside, giving off an idyllic atmosphere I'd often dreamed of."

        "It's always been kind of a romantic notion to me to be able to meander around in the countryside, taking in the fresh air."

        "Now that an opportunity to do just that is here, I can't resist, even though I know it must seem silly."

        scene bg school_courtyard
        with locationchange

        "I stop at the main building in order to buy a drink, and then decide to enter it and maybe hang around on the roof a little bit."

        "The view might be pretty cool at this time, and I'm sure that nobody else will be up there either. And I've never been up there by myself."

        $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
        play ambient sfx_rooftop fadein 1.0

        scene bg school_staircase1
        with locationchange

        "The school is quiet today. Deserted. My footsteps echoing in the staircase to the roof are unnervingly loud."

        "It shouldn't bother me due to how much time I've spent in sign language class in near-total silence, or working so much with Shizune lately, but it still does."

        "It makes the smallest noises that I wouldn't have even noticed before seem boomingly loud. It feels like I'm sneaking around some place I shouldn't be. I wonder why I'm getting that vibe. Maybe the school is haunted or something."

        play sound sfx_door_creak
        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")
        stop music fadeout 3.0

        scene bg school_roof at left
        with locationchange

        "When I open the door to the roof, I see I'm not alone. Misha leans against the fence, looking over the school grounds, not having noticed me at all."

        "Instantly, I know what I have to do: I have to put my hands over her eyes and say 'Guess who?' It's the only option."

        "Halfway, I start thinking of how bad this would look if Shizune suddenly popped in, having left just for a second to get some sandwiches, and saw me sneaking up on Misha like this."

        "I pray silently that such a coincidental misunderstanding doesn't happen."

        show bg at right
        with charamove

        hi "Guess who?"

        mi "Hicchan!"

        "She says, without hesitating for a second, without deviating even slightly from her normal tone. My fun was over before it started."

        play music music_soothing fadein 1.0

        show misha hips_grin_close:
            center
            xpos 0.6
            easein 0.5 center
        with charaenter

        show misha at center

        mi "Hi, Hicchan! Good morning~!"

        show misha sign_confused_close
        with charachange

        "She reflexively tries to move her hands to form a greeting and entangles them in the fencing."

        hi "Good morning. I didn't expect to find you here. What're you doing up so early?"

        show misha perky_smile_close
        with charachange

        mi "I could ask you the same thing, Hicchan! What are you doing up so early? I didn't expect to find you here~!"

        hi "I asked you first."

        show misha hips_grin_close
        with charachange

        mi "Hm~… you're right. Wahaha~!"

        show misha sign_smile_close
        with charachange

        mi "You sound just like Shicchan."

        hi "No, I don't."

        "…I say, in the least convincing manner possible. Luckily, Misha doesn't notice what a bad actor I am."

        hi "Are you looking forward to tonight?"

        show misha hips_smile_close
        with charachange

        mi "Of course, Hicchan~! I don't like celebrations, or maybe not as much as Shicchan does, but Tanabata stands always have interesting things to buy and all kinds of seasonal food. And~! I get to wear a yukata~!"

        "Her choice of words is a little strange. It sounds like she's saying that she doesn't like celebrations, but likes doing everything involved with them. I don't know if it's worth pursuing, though, and it could be that I just misunderstood."

        show misha perky_smile_close
        with charachange

        mi "What about you, Hicchan~?"

        hi "I am, or else I'd just stay home, wouldn't I? That's the logical step."

        show misha hips_grin_close
        with charachange

        mi "Ahaha~! Hicchan, you're not that logical~! So~! That's really surprising! Hm, okay, though. I was just making sure, because you didn't look like you were having a lot of fun last time. Me and Shicchan were a little worried, because of that."

        hi "Hey, I had fun. I guess I ended up appreciating it more than I expected to."

        show misha perky_smile_close
        with charachange

        mi "Really, Hicchan~? Wahahaha~! What part of it? Tell me~!"

        hi "Well, there were fireworks at the end. They were… really nice."

        hi "I think you slept through them."

        show misha hips_smile_close
        with charachange

        mi "Aw~… I always fall asleep early. But~! I won't sleep through them this year! I'll definitely stay awake!"

        hi "I don't think they have fireworks during Tanabata. It's a different mood entirely."

        hi "Maybe you can get Shizune to petition them to have them, though. And to move the fireworks to an earlier time."

        show misha cross_laugh_close
        with charachange

        mi "Hahahahahaha~! Maybe I will~! That's a great idea, Hicchan!"

        hi "Ah, no, no it's not! Don't do that. I wasn't being serious."

        hi "Although… maybe it would annoy Shicc— Shizune."

        show misha hips_grin_close
        with charachange

        mi "Wahaha~. You make it sound like you would like that, Hicchan."

        show misha cross_smile_close
        with charachange

        mi "Hicchan~! Do you like Shicchan?"

        "I can't say yes or no, and, sitting down like I am, I can't even smoothly leave."

        hi "Don't be silly; the one I like is you."

        show misha perky_smile_close
        with charachange

        mi "Ahahaha~! Really, Hicchan? Hm~! No, you're kidding, right? You must like Shicchan more."

        hi "Misha, you jump to conclusions too much."

        show misha sign_smile_close
        with charachange

        mi "But you almost called her Shicchan! So~! I'm right, right~?"

        hi "It's because you call her Shicchan all the time. It got stuck in my head. Osmosing language is common, you know. Besides, it's one little slip-up. And by your logic, you should like her more than me. And… are you making fun of me or something?"

        show misha cross_laugh_close
        with charachange

        mi "Wahaha~!"

        show misha perky_smile_close
        with charachange

        mi "Maybe~."

        show misha hips_smile_close
        with charachange

        mi "I'm hungry. Did you eat breakfast, Hicchan?"

        hi "No. Just medicine."

        show misha sign_confused_close
        with charachange

        mi "Hm…"

        "Misha twirls her finger lazily in the air to keep her hands busy as she thinks."

        show misha hips_grin_close
        with charachange

        mi "We should eat something, then~! Do you think they will be serving breakfast today?"

        "That's really the kind of thing a member of the Student Council should know. I can't say that, though. I'm on the Student Council and don't know."

        hi "It didn't seem like anyone was working in the kitchen when I entered the building, but I don't know for sure."

        show misha perky_smile_close
        with charachange

        mi "Hey, Hicchan, have you ever heard about those vending machines that you can get food from, like burgers, soup, and even pizza? Wouldn't it be great if we had some of those at our school~?"

        hi "I don't know, I always thought those machines were kind of weird."

        show misha hips_smile_close
        with charachange

        mi "Imagine how cool it would be if we had machines like that at our school, Hicchan~! It would almost be like magic, wouldn't it?"

        mi "Hot food coming out of a vending machine, that's so amazing, I could never imagine that. Seeing one of those machines would be like a dream!"

        show misha perky_sad_close
        with charachange

        mi "Hm~… We don't have machines like that in this whole town, though~. It's too early to even go into town~! I won't be able to eat breakfast, Hicchan, that's the most important meal of the day. Everyone says so~! Ah, I want to eat!"

        hi "You're really silly. If it bothers you so much, I'll buy you a soda."

        show misha hips_frown_close
        with charachange

        "Misha puffs out her cheeks and puts on her serious face."

        mi "Hicchan, a soda is not a breakfast. It's like water~."

        hi "It's not like water, it's a liquid. Water isn't food. Liquid can be food."

        "'Now who sounds like Shizune, Misha?' I want to say it. Even her tone reminds me of Shizune's unblinking, matter-of-fact way of stating the ridiculous. If I did say that, though, I would be the one who sounds like Shizune again."

        "It's terrible, her competitiveness is really rubbing off on me."

        hi "Let's look for something to eat, then."

        show misha cross_frown_close
        with charachange

        mi "…"

        show misha cross_laugh_close
        with charachange

        mi "Okay. Ahahahaha~!"

        stop music fadeout 3.0
        stop ambient fadeout 1.0

        scene bg school_lobby
        with locationskip

        "Predictably, our search for food in an empty school building this early in the morning leads only to failure."

        "Misha decides to go off on her own after we both decide to give up for now, vowing to eat breakfast even though by now it's closer to time for brunch."

        scene bg school_dormhisao
        with locationskip

        "I go back to my dorm. The following hours tick by slowly, and I pass the time by catching up on my reading."

        show bg school_dormhisao_ni as overlay:
            center
            alpha 0.0
            linear 6.0 alpha 1.0

        play music music_dreamy fadein 6.0

        "Some of these books I haven't touched since I was in the hospital. Thinking back on it, it wasn't that long ago, even though it definitely feels like it was."

        "A free day, and I can't think of anything to do. I take a short nap, and as I change for the second time today, I realize that I never actually confirmed with Shizune or Misha when and where we would meet up."

        "I guess that eventually they would come looking for me, but I would look pretty stupid if it came to that."

        scene bg school_dormhisao_ni

        "It's already evening, so I should at least make an effort to find them first."

        scene bg school_courtyard_ni
        with locationskip

        "Even though the grounds aren't exactly flooded with people and it should be impossible to miss Misha's pink hair even if they were, I have a lot of difficulty finding them."

        scene bg school_gate_ni
        with locationchange

        "Finally, I run into them at the front gate, which was the first place I had looked."

        show shizuyu basic_happy_ni at center
        with charaenter

        ssh "Hello!"

        "She attempts to punctuate her normal greeting with a grand little sweep at the end."

        show shizuyu at tworight
        show bg at bgright
        with charamove

        show misha sign_smile_yuk_ni at twoleft
        with charaenter

        mi "Hicchan~! How're you?"

        "It's strange seeing them in yukata, though I've been seeing yukata in general all night."

        "Shizune's is simple and tasteful, which seems obvious for her in retrospect. For all her grand flourishes and over-the-top behavior, I think she would rather die than dress the part."

        "What draws my eye is the hairpin she is wearing, a pearl flower that gleams softly in the moonlight."

        "It looks pretty on her, but in a way it also feels out of place. As if it's too elaborate for a high school girl, or maybe just for someone as secretly childish as Shizune."

        "Misha's yukata is about what I expected, so it actually fits a little too well. Paired with her bubblegum pink hair, she looks cute, but anachronistic."

        hi "You two look nice."

        show misha perky_smile_yuk_ni
        with charachange

        mi "Thanks, Hicchan~!"

        show shizuyu cross_angry_ni
        with charachange

        shi "…"

        mi "Hicchan, you're a little late. We were waiting here a while for you, did you forget the time or the place?"

        mi "Oh well~! Let's get going, Hicchan~!"

        show shizuyu cross_happy_ni
        with charachange

        shi "…"

        "Misha dropping this line of discussion saves me what could potentially be a pretty embarrassing thing to own up to; specifically, that I had been looking for them for at least an hour."

        "Seeing Shizune and Misha looking so cheerful, it's hard not to want to fall into the atmosphere and enjoy a nice night out."

        "What bothers me is that I'm having some trouble reading Shizune's signing tonight. I haven't been to sign language class in almost a week, so I'm not surprised. I guess having lost focus for a while, I'm slipping. It certainly wouldn't be the first time."

        hi "Hold on, where are we going? Into town?"

        show shizuyu basic_happy_ni
        with charachange

        ssh "Yes."

        hi "That doesn't make any sense. We haven't even checked out what's on the grounds. Unless you two decided to have fun while I wasn't looking."

        show shizuyu cross_happy_ni
        with charachange

        ssh "We're going to come back; we'll be working our way up."

        show misha sign_smile_yuk_ni
        with charachange

        mi "Hahaha~! Either way, Hicchan, we have to walk into town and then back up if we want to see everything. So~! This way, after we're done, we'll be right by our dorms when we're tired. It works out perfectly~!"

        show shizuyu basic_happy_close_ni at closeright
        with characlose

        stop music fadeout 2.0

        "That is admittedly logical. Shizune doesn't give me much time to argue anyway, grabbing me by the arm and lightly trying to pull me along."

        scene ev shizutanabata:
            truecenter
            zoom 8.0 rotate 45.0
            easein 1.0 zoom 1.1 rotate 0.0
            easein 8.0 zoom 1.0
        with locationskip

        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
        play ambient sfx_crowd_outdoors fadein 2.0
        play music music_ease

        "The streets illuminated only by the light of the moon and low lanterns tinted with tissue paper put me at ease."

        "Now that we're in town, Shizune moves a bit more slowly in order to see the sights."

        "So, I decide to walk more briskly in order to mess with her, but she quickly readjusts her own speed to match, letting out a soundless laugh before quickly signing to Misha with her off hand."

        shi "…"

        mi "What do you want to do first, Hicchan~?"

        hi "How about some games, if there are any?"

        mi "I thought you didn't like games, Hicchan."

        hi "I don't mind."

        "For the second time today, I feel her slim fingers wrapping around mine. It feels like all this time, I've been pulled along by Shizune's will. Occasionally, it's quite tiring, but I think that for the most part, I wouldn't say I hate it."

        "It's just the quality of some people to drag others into their lives, like a storm. That word fits Shizune sometimes, I think. Although I didn't want to tell Misha earlier today, I do like her."

        mi "Hicchan, you're going to win a doll for me too this time, right~?"

        hi "You're still thinking about that? Okay, I will."

        $ renpy.music.set_volume(1.0, 2.0, channel="ambient")

        scene bg suburb_tanabata_ni at bgright
        show nightwash
        with shorttimeskip

        "The time passes by faster than I thought it could as we run around, trying to do as many frivolous things as possible."

        show misha perky_smile_yuk behind nightwash at center
        with charaenter

        mi "Snow cones! Hicchan, do you want one~?"

        "Misha runs towards the stand, not even waiting to hear my answer."

        show misha at twoleft
        show bg at center
        with charamove

        show shizuyu cross_happy_close behind nightwash at closeright
        with charachange

        ssh "They look delicious, I want one too. We'll play rock-paper-scissors to see who can pay for them all."

        hi "Or… we could each pay for our own."

        show misha sign_smile_yuk
        with charachange

        mi "Hicchan~, what flavor do you want?"

        hi "The blue one."

        show shizuyu basic_angry_close
        with charachange

        ssh "Blue is not a flavor."

        hi "I knew that…"

        ssh "Ordering something based on color is childish."

        hi "You're childish. What are you getting? Are you getting strawberry? Ha! That's such a childish flavor, only children eat strawberry."

        show shizuyu cross_angry_close
        with charachange

        ssh "You should get plain, the most mature flavor of all!"

        "I want to know where her personality comes from. I wonder if I would think that way if she hadn't been the first student I ended up having a conversation with on my first day here."

        "It's entirely possible that I'd have missed the parts of her that kept drawing me in."

        "If I didn't know that she couldn't hear me, and that she was so competitive, and so focused with getting me to join the Student Council, and so alternatingly playful and sharp…"

        "Without these constant new facets to keep my interest in her, would I have grown to like her so much?"

        "It's likely that I'm overthinking it."

        hi "Aren't you going to make a wish?"

        show misha perky_confused_yuk
        with charachange

        mi "Shicchan never makes wishes, Hicchan!"

        hi "Oh really? Not even on New Year's? Why's that?"

        show shizuyu basic_happy_close
        with charachange

        shi "…"

        "Shizune tents her fingers and smiles, but won't answer."

        ssh "It's a secret."

        show misha sign_smile_yuk
        with charachange

        mi "I know~!"

        mi "Hicchan, do you want me to tell you?"

        show shizuyu cross_blush_close
        with charachange

        shi "…!"

        hi "Yes."

        show shizuyu basic_angry_close
        with charachange

        "Shizune alternates between as many forceful iterations of 'no' she can think of."

        show misha perky_smile_yuk
        with charachange

        mi "Wahaha~! I'll tell you later, okay?"

        show misha perky_sad_yuk
        with charachange

        stop music fadeout 5.0

        mi "Actually, I feel tired. I think I'm going to go to bed early~."

        show shizuyu cross_blush_close
        with charachange

        ssh "Really?"

        hi "It doesn't feel like it's been that long."

        "Time flies when you're having fun."

        show misha sign_smile_yuk
        with charachange

        mi "But~! it has, Hicchan. Maybe I can visit Yuuko first, then go back? Or~… I don't know~."

        show misha perky_smile_yuk
        with charachange

        mi "Well, it doesn't matter. Have fun without me, okay~?"

        hi "We're going to go back to the school soon anyway, Misha."

        hide misha
        with charaexit

        show shizuyu at center
        show bg at bgleft
        with charamove

        "Misha doesn't want to hear it, and leaves anyway. Shizune starts to wonder why just as soon as I do, but while I keep it in my head, she signs it, seeming to want to discuss the possible reasons."

        scene bg suburb_tanabata_ni at bgleft
        show nightwash
        with shorttimeskip

        "After we're both done seeing all there is to see, I check the time, and find that it is pretty late. My energy is starting to wear off, and it's a miracle that I managed to have even this much, too."

        "Even Shizune is starting to look a bit tired. We make our way back to the grounds."

        stop ambient fadeout 0.5

        scene bg school_courtyard_ni
        with locationskip

        play ambient sfx_cicadas fadein 0.5

        "Shizune seems disappointed when she sees the school building lit up and teeming with students."

        his "Something wrong?"

        show shizuyu basic_aside_ni at center
        with charaenter

        ssh "I wanted to go up to the roof, but now there are too many people. I'm tired, so it might be for the best."

        his "There are probably couples on the roof, since it's that kind of holiday."

        his "Then again, I wouldn't know. Is that how it really is? I'd never really been to any festivals before coming here."

        shi "…"

        his "I'm disappointed, I thought you said you wanted to see what the school was doing last, like saving the best for last. Now you're telling me you don't want to? Not even a little? I thought you would have more energy. I don't feel tired."

        show shizuyu basic_happy_ni
        with charachange

        "This seems to spark her competitive spirit, and Shizune immediately perks up, although it's then that I realize I didn't have anywhere in mind to take her, and I don't feel like going to the main building myself."

        scene bg school_gardens_ni:
            xalign 0.0
            warp acdc_warp 4.0 xalign 1.0
        with locationchange

        "Fortunately, the area behind the school is both deserted and impressive-looking today. I'd never appreciated how sprawling and well kept it was until seeing it at night. It almost seems to go on forever in the moonlight."

        show shizuyu basic_happy_ni at center
        show bg at right
        with charaenter

        ssh "It's very pretty, even though it's just a field."

        "I'd thought earlier that she was too immature to pull off the old-fashioned clothes she is wearing tonight, but right now, she is quite beautiful in them."

        "It makes me think back to that day, the other festival that I went to with her. She had looked the same way then."

        $ renpy.music.set_volume(0.5, 1.0, channel="ambient")
        $ renpy.music.set_volume(0.5, 0.0, channel="music")
        play music music_serene fadein 1.0

        nvl clear

        nvl show dissolve

        n "{vspace=30}I want to tell her that I like her. Decisively, in one go. But even thinking about it is just so awkward."

        n "And the more I like her, the more awkward and afraid I am of telling her how I feel, even now, when I could do so if I wanted without having to go through another person."

        n "Not to mention, what if what happened last time happens again? If it does, I might not get off so easily with a months-long hospital stay. I don't want to even think about it."

        n "I try to shove the thoughts out of my mind any way possible. I try to dismiss them as unlikely fears."

        n "Still…"

        n "The first time I had seen all of my pills, I'd imagined them cascading before me, enough of them to choke me."

        n "I still think about it from time to time. I can't say that it's not a legitimate concern. Times like these are nice enough that I can forget, though."

        nvl clear
        nvl hide dissolve

        $ renpy.music.set_volume(1.0, 1.0, channel="music")
        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

        scene ev shizuconfess_normal
        with flash

        ssh "My favorite thing about this school is that it's on top of a mountain."

        his "Is it because it's that much closer to the sky?"

        ssh "Yes."

        his "I like it too, but more because of the fresh air."

        his "You're so competitive. Too competitive. If a whale bit you, you would bite it back."

        scene ev shizuconfess_smile
        with charachangeev

        shi "…"

        "That makes her laugh, and she winks."

        ssh "Would that be so bad?"

        "Her smile is contagious."

        his "Yes."

        shi "…"

        scene ev shizuconfess_closed
        with charachangeev

        ssh "It's true. I'm terrible, a little."

        scene ev shizuconfess_smile
        with locationchange

        ssh "But if I can make people happy, I'm not entirely terrible, am I? Then, it's okay. I have many examples in my defense."

        "Maybe even this moment is a kind of game to her."

        his "That's right."

        stop music fadeout 2.0

        "This is a romantic moment. I don't know if such a chance might come again, and I feel compelled to say something awkward and stupid. If I think about it too much, I doubt my hands will listen to me."

        his "Do you want to be my girlfriend?"

        scene bg school_gardens_ni at right
        show shizuyu cross_blush_ni
        with locationchange

        shi "…"

        "I hope that I signed it properly."

        "I feel nervous; as if I want to break into a run, yet I'm rooted to this spot. I couldn't hear a thing just minutes ago, now I'm picking up every little ambient noise. I really am nervous, and I wonder if it shows."

        "Before, hours passed like seconds. Now, the seconds pass like eons."

        show shizuyu basic_blush_ni
        with charachange

        "Then I see Shizune's hands moving unsteadily before her, fumbling over each other, stopping halfway through each gesture."

        "It's like she said, sign language gives you an opportunity to think your words through, and she is trying very hard to do that right now."

        "A situation that she doesn't know how to respond to. It must be unthinkable. As stoic as Shizune tries to be, she can't hide her reddening cheeks, and she's very cute and feminine like this. And it puts me at ease to know she is as nervous as I am."

        "The thought is yet another way in which I've found myself competing with her."

        show shizuyu cross_happy_ni
        with charachange

        ssh "Okay."

        play music music_romance fadein 1.0

        show shizuyu basic_happy_close_ni
        with characlose

        "That's a simple reply. But as soon as I think that, Shizune takes a step forward and embraces me."

        stop ambient fadeout 3.0

        nvl clear

        nvl show dissolve

        n "{vspace=270}An unsure and careful embrace, as if I were made of eggshell, and as if she doesn't know how to hug someone. Although to be honest, it's not a subject I'm familiar with either."

        n "Her yukata is cool and silky under my fingers, but I can also feel Shizune's warmth."

        n "In the end, she thought this the best possible gesture to show how she felt."

        stop music fadeout 3.0

        nvl hide dissolve

        if _in_replay:
            return

    return
