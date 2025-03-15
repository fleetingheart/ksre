# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a3_emi:
    label .eet_ees_scienca:
        scene bg school_scienceroom
        with fade

        nvl clear
        nvl show dissolve

        $ renpy.music.set_volume(0.5, 0.0, channel="music")
        play music music_normal fadein 3.0

        n "{vspace=90}My head's in a spin all through Mutou's class."

        n "I'm going to have dinner."

        n "With Emi."

        n "Who wants to be my girlfriend, no less."

        n "A date…"

        n "And then she kissed me."

        n "That kiss. I keep going back to it, playing it over in my mind again and again."

        n "Everything about that moment felt so right."

        n "{vspace=30}My mind drifts off, lost in thoughts of Emi."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")

        nvl clear
        nvl hide dissolve

        show muto normal at center
        with charaenter

        mu "Nakai? Hello?"

        "It seems like I've drifted a bit too far."

        hi "Huh? What?"

        show muto irritated
        with persistent.charachange

        mu "Egad! You've contracted some kind of amnesia!"

        mu "Someone get the nurse!"

        "The class chuckles at Mutou's antics."

        hi "Sorry, sir."

        show muto normal
        with persistent.charachange

        mu "Hmm, won't happen again and all that, right?"

        hi "Exactly."

        "Mutou brightens considerably."

        show muto smile
        with persistent.charachange

        mu "Well! Lovely to hear!"

        mu "I'd hate to have my star pupil slacking off, after all."

        hide muto
        with charaexit

        "I've been doing well, but I hardly qualify as a star pupil, I think."

        "I'm fairly certain that this class is the sort that everyone does well in. It's just memorizing formulas."

        "True to my word, I manage to pay attention for the rest of the class."

        stop music fadeout 2.0

        show muto normal
        with shorttimeskip

        play sound sfx_normalbell

        mu "Nakai, may I have a word with you?"

        "I wonder if I'm in trouble for earlier."

        hi "Uh, sure."

        hi "Am I in trouble?"

        show muto irritated
        with persistent.charachange

        "Mutou looks genuinely confused for a moment."

        mu "Beg your pardon?"

        "He tilts his head to one side and thinks for a moment."

        show muto smile
        with persistent.charachange

        mu "Oh, that! No, no, you're not in any sort of trouble."

        mu "There's just a question I want to ask you."

        hi "What's that?"

        show muto normal
        with persistent.charachange

        mu "Nothing terrible, I was just wondering what your plans for after graduation are."

        play music music_another fadein 2.0

        mu "Are you going to university?"

        hi "Yeah, I guess. I can't really see a reason not to go."

        mu "Given any thought to what you'll study?"

        hi "Not really, no. I figure I'll come up with something when I get there."

        show muto smile
        with persistent.charachange

        "Mutou laughs."

        mu "Taking things as they come, eh?"

        mu "I'd argue against it, but that's how I did things when I went to university."

        mu "Well, not really."

        mu "I knew I'd go into a science, I just wasn't sure which one."

        mu "Ended up with physics, but could just as well have gone for astronomy or what have you."

        show muto irritated
        with persistent.charachange

        mu "Actually I did go for chemistry first, but there were all sorts of things…"

        "Mutou trails off, and frowns slightly."

        "It takes a minute for him to recover his train of thought, and I wait patiently for him to continue."

        show muto normal
        with persistent.charachange

        mu "So anyway, I did a lot of physics as well, because I had an interest in that, but I wasn't sure if it was for me."

        show muto smile
        with persistent.charachange

        mu "So I went back to chemistry, and here we are. Yes?"

        show muto smile
        with persistent.charachange

        "He smiles at me enthusiastically, as if waiting for me to confirm that yes, here is where we are."

        "Somehow I get the feeling that Mutou had a plan for this conversation, but I'll be damned if I can figure it out."

        hi "I'm sorry, I'm not following you."

        "Mutou frowns and rubs his chin a bit, looking perplexed. He then snaps his fingers as if he's remembered what the point of all this was."

        mu "Right! Yes! You!"

        hi "Me?"

        mu "Yes! You should look into studying one of the sciences!"

        mu "You're fantastic at it."

        mu "Unless you'd rather just go into math."

        show muto irritated
        with persistent.charachange

        "Mutou makes a sour face."

        mu "Not a big fan of straight math. I always liked the experiments more than the proofs."

        hi "You're saying I should study science at university?"

        "Mutou seems thrown off balance by my question."

        show muto normal
        with persistent.charachange

        mu "Well, sort of."

        show muto smile
        with persistent.charachange

        mu "You could also join the science club!"

        mu "Trouble is, there's not actually a science club."

        mu "But there could be!"

        mu "You could even be a charter member!"

        mu "A founding father!"

        mu "Of course, you'd need to find other members."

        show muto normal
        with persistent.charachange

        mu "Well, only if you wanted to."

        mu "We could just start it up with the two of us."

        mu "And um."

        show muto smile
        with persistent.charachange

        mu "I could give you things to read, and we could talk about them."

        mu "Er, and I could help you get ready for university and such as well."

        show muto irritated
        with persistent.charachange

        mu "Wait!"

        "Mutou rummages around in his briefcase and tosses me a book."

        show muto smile
        with persistent.charachange

        mu "Read that."

        mu "If it's interesting, then we can talk about it."

        "'A Brief History of Time?'"

        "I don't know if I actually want to read this, but Mutou seems pretty excited about it."

        hi "What's it about?"

        show muto normal
        with persistent.charachange

        mu "Time. Space. Space-time. Black holes and such."

        mu "And it's not that dense. Just to see if that sort of thing's interesting for you, you understand."

        mu "Hang around after class, and we can either discuss it, or I can show you how to make explosives in the lab."

        show muto smile
        with persistent.charachange

        "He waves a hand at my quizzical expression."

        mu "Joking, sorry."

        mu "Still, I've kept you here long enough for now."

        mu "Think about science as a career path, Nakai. I think you'd enjoy it."

        hi "Uh, okay. I will. Thank you for the book."

        stop music fadeout 14.0

        scene bg school_hallway3
        with locationchange

        "I leave the classroom and look up at the clock; quite a chunk of time to kill until Emi's out of practice."

        "Guess I'll give this book a look; I should probably shower as well."

        "Showering before a date's only proper, right?"

        "I head back to the dorms."

        scene bg school_dormhisao
        with locationskip

        "I wonder where I'm supposed to meet Emi, anyway."

        "She said 'after practice,' but she didn't say where I should find her."

        "I guess I can just swing by the track; that's probably best, anyway."

        "If she needs a shower, I can just wait for her in her room or something."

        "Or in the hallway, I guess; that would be better as well."

        "I take a quick shower, remembering to take my medication once I hop out."

        "Now, for a look at this book."

        stop music

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .definitions:
        scene black

        scene bg school_dormhisao
        with vpunch

        "I wake with a start."

        "Shit! What time is it?"

        "A glance at the clock reveals that I've been asleep for nearly an hour."

        hi "Thank goodness."

        "Emi's practice should be finishing up soon."

        "I throw on some casual clothes and head for the track."

        scene bg school_track
        with locationskip

        "Somehow I get the feeling we won't be doing anything fancy for dinner."

        "Emi doesn't strike me as a very fancy sort of person."

        "Still, I suppose there's a lot I have yet to know about Emi."

        "Despite our newfound closeness, I still feel like I don't know her as well as I should."

        "Ah well, I have lots of time to fix that."

        "To be honest, I'm looking forward to getting to know her more."

        "I'm so caught up in my own thoughts that I hardly register that I'm already at the track."

        "Emi is nowhere to be found."

        "I don't even see any signs of the track team."

        "This could be embarrassing."

        "I turn to head toward the girls' dormitory when I hear a shout."

        emi "Hey, Hisao!"

        play music music_emi fadein 1.0

        show emicas smile at center
        with charaenter

        "I turn around to see Emi making a beeline for me with a gym bag slung over her shoulder."

        "She's changed into some decidedly more casual clothing; a pair of shorts and an olive green top."

        "Her running blades have been replaced by more realistic-looking legs that probably wouldn't fool anyone."

        "Emi doesn't seem to care about that, a fact which makes me smile."

        show emicas happy
        with persistent.charachange

        emi "Hey, you came!"

        show emicas closedsmile
        with persistent.charachange

        emi "I mean I figured you would, but still…"

        show emicas closedsmile_up_close
        with characlose

        "I suddenly find myself wrapped in a rather affectionate hug, and it proves to be impossible for me to keep what must be the world's largest grin off my face."

        hi "Well, of course I came!"

        hi "I'd be crazy not to, right?"

        "Emi ponders for a moment."

        show emicas grin_up_close
        with persistent.charachange

        emi "You know, that's true."

        show emicas wink_up_close
        with persistent.charachange

        emi "I mean I'm pretty amazing, after all."

        "I shrug in response."

        hi "I certainly think so."

        show emicas blush_up_close
        with persistent.charachange

        "It's an offhand remark, which is why I'm surprised to see that it seems to have caught Emi by surprise."

        show emicas smile_up_close
        with persistent.charachange

        "She blushes and smiles warmly at me before planting a kiss on my lips."

        "Now it's my turn to be surprised."

        show emicas grin
        with charadistant

        "Emi steps back, resting her weight on her back heel, looking pleased with herself."

        "My brain fumbles for an appropriate response."

        hi "…"

        hi "I should compliment you more often."

        show emicas happy_up
        with vpunch

        "Emi laughs and gives me a playful shove."

        show emicas closedsmile
        with persistent.charachange

        emi "Jerk."

        show emicas weaksmile_up_close
        with characlose

        "I throw an arm around Emi's shoulders and am pleased when she immediately leans into me as if it were the most natural thing in the world."

        hi "So, where to?"

        show emicas awayfrown_up_close
        with persistent.charachange

        emi "I'm not actually sure."

        show emicas neutral_up_close
        with persistent.charachange

        emi "Where do people go on dates around here, anyway?"

        "That's a damned good question."

        hi "I've got no idea."

        hi "Why don't we just head down to the Aura-Mart and grab something portable?"

        "Emi's face brightens at this idea."

        show emicas happy_up_close
        with persistent.charachange

        emi "A picnic!"

        show emicas wink_up_close
        with persistent.charachange

        emi "I think you're on to something, Hisao."

        scene bg school_gate
        with locationskip

        "Emi snakes her arm around my waist, and we begin to head for the front gate."

        "I'm entirely unsure of what I'm meant to do in this situation, but at least Emi seems to be equally clueless."

        scene bg suburb_roadcenter
        with locationskip

        "Despite the relaxing feeling of being with Emi, I still can't help feeling a little tense."

        "What if I do something wrong?"

        "I'd hate to make an ass out of myself."

        scene bg suburb_konbiniext
        with locationchange

        "The trip to the Aura-Mart is accompanied by Emi's chatter about how practice went."

        "I keep quiet for the most part, merely enjoying the warmth of being around Emi."

        "We get a few odd looks from passersby, but I don't mind."

        "We wind up buying some bread and instant noodles, realizing too late that we cannot actually cook the latter in the park."

        show emicas weaksmile at center
        with charaenter

        emi "Oh well. I'll make it for lunch or something."

        hi "That'll work."

        stop music fadeout 2.0
        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        play ambient sfx_parkambience fadein 2.0

        scene bg suburb_park
        with locationskip

        "The park is located after a brief loss of direction that I blame entirely on Emi."

        "She, of course, blames me."

        show emicas smile:
            center
            easein 1.0 ypos 1.13
        with charaenter

        show emicas

        "We find a spot beneath a tree and sit down. I lean back against the trunk, Emi sits across from me."

        play music music_ease fadein 3.0

        hi "I guess we should have brought a blanket or something to sit on, huh?"

        show emicas smile_up
        with Dissolve(0.2)

        show emicas smile
        with persistent.charachange

        "Emi shrugs."

        show emicas closedsmile
        with persistent.charachange

        emi "I don't mind."

        hi "Neither do I."

        show emicas grin_up
        with persistent.charachange

        "Emi tosses me a package of bread and we dig in."

        "Curry bread. Interesting."

        "I guess I wasn't really paying attention to what I grabbed in the store."

        show emicas wink_up
        with persistent.charachange

        emi "Hey, Hisao. You look like your bread's a little spicy."

        "I shake my head, trying in vain to keep an image of manliness."

        hi "Nah, it's hardly spicy at all."

        show emicas closedsmile_up
        with persistent.charachange

        emi "I see, I see. That must be why your face has gotten so red."

        hi "Yes, exactly. The lack of spice has uh… gotten my blood up."

        hi "Because of the disappointment."

        show emicas happy
        with persistent.charachange

        "Emi laughs and swallows the last of her bread."

        show emicas wink
        with persistent.charachange

        emi "Well, if you can't handle it, I'll be glad to take it off of your hands."

        hi "Hey, just because you wolfed down yours so quickly doesn't mean I'm just going to give you mine."

        show emicas pout
        with persistent.charachange

        "Emi mock-pouts, causing me to nearly choke on my bread with laughter."

        emi "Aw, come on Hisao!"

        show emicas awayfrown
        with persistent.charachange

        emi "Aren't you supposed to be concerned with making sure I've got enough to eat now?"

        emi "We're dating, you know!"

        show emicas pout
        with persistent.charachange

        emi "Though…"

        "Emi looks troubled all of a sudden."

        show emicas frown_up
        with persistent.charachange

        emi "I can't say I feel any different."

        hi "Hmm? What do you mean by that?"

        show emicas awayfrown
        with persistent.charachange

        emi "What makes this a date?"

        emi "It's just what we would have done anyway, really."

        emi "But this should feel different because before when we had lunch we were friends, and now we're a level above friends."

        hi "You sound like Rin."

        show emicas happy
        with persistent.charachange

        "Laughter escapes, and Emi grins."

        show emicas closedsmile_up
        with persistent.charachange

        emi "Well, she might've put the thought into my mind."

        show emicas closedsmile
        with persistent.charachange

        emi "We've talked about that sort of thing before."

        hi "Really? About me?"

        show emicas grin
        with persistent.charachange

        emi "Not really. Just… stuff, really."

        show emicas neutral
        with persistent.charachange

        emi "Rin thinks that the change of a label from 'friend' to 'girlfriend' seems arbitrary most of the time."

        emi "Like there's no difference between the two."

        hi "I can think of at least one, you know."

        hi "You don't tend to kiss your friends quite as much."

        show emicas blush
        with persistent.charachange

        "For the second time today, Emi blushes slightly and giggles."

        show emicas closedsmile
        with persistent.charachange

        emi "I suppose you're right."

        hi "Exactly. I'm always right about things like this."

        show emicas weaksmile_up
        with persistent.charachange

        "Emi rolls her eyes and chuckles."

        emi "Guess you're pretty smart, huh?"

        "I nod in agreement."

        hi "Yep."

        hi "Even Mutou thinks so. He thinks I should go into some scientific study after graduation."

        show emicas neutral
        with persistent.charachange

        "Emi raises an eyebrow."

        emi "Oh really?"

        hi "Yeah, I'm thinking I actually might do just that."

        "Really, the more I consider the idea, the more it appeals to me."

        "I make a mental note to look into it a little more closely."

        hi "So what are you thinking of doing after graduation?"

        hi "Still planning on running?"

        show emicas awayfrown
        with persistent.charachange

        "Emi shrugs, seeming almost a bit hesitant."

        show emicas frown
        with persistent.charachange

        emi "I dunno. If I'm good enough and I can find a team, I guess?"

        hi "You mean you aren't sure?"

        show emicas neutral
        with persistent.charachange

        emi "I haven't… really thought about it, to be honest."

        hi "Really?"

        hi "You probably should, you know. Graduation isn't that far off."

        show emicas awayfrown
        with persistent.charachange

        "Emi fidgets a little nervously."

        emi "Yeah, well… it's far enough, right?"

        show emicas neutral
        with persistent.charachange

        emi "Besides, I've got other things to think about."

        show emicas grin_up_close
        with vpunch

        "There's a mischievous flash behind Emi's eyes, and I suddenly find myself gloriously pinned against the tree."

        show emicas smile_up_close
        with persistent.charachange

        emi "Like making sure this is a real date, right?"

        show emicas closedsmile_up_close
        with persistent.charachange

        emi "I mean if we don't kiss then it's not a date at all, right?"

        hi "I suppose s— mmmph." with vpunch

        "Strawberries and curry. Not the best combination, but I don't think I mind."

        show emicas grin
        with charadistant

        "Emi sits back on my legs and grins again."

        emi "There. Science would approve, right?"

        "I have the oddest mental image of Mutou nodding seriously and making a mark on some checklist."

        "I can't help laughing at the idea."

        show emicas neutral
        with persistent.charachange

        emi "Well I'll admit, this is the first time I've ever witnessed a kiss being met with laughter."

        emi "Should I feel offended?"

        hi "Heh, no, no."

        hi "I'm sure science approves."

        show emicas happy_up
        with persistent.charachange

        "Emi beams at me, and I find it increasingly difficult to keep my brain functioning properly."

        emi "Oh good!"

        "It is at this point I notice that Emi has stolen the remainder of my curry bread while I was otherwise occupied with images of teachers wielding clipboards."

        hi "Hey!"

        show emicas blush
        with persistent.charachange

        "Emi tries to look innocent, but considering she's just crammed the last bits of my bread into her mouth it does not appear to be working."

        emi "Mmph? F'orry, couln't refisft."

        hi "Thief!"

        show emicas neutral
        with persistent.charachange

        "A shrug from my companion is all I get in response."

        hi "You used your feminine wiles on me!"

        "I wasn't that hungry anyway, but I still feel that the point needs to be made."

        show emicas pout
        with persistent.charachange

        "Emi seems confused by the phrase 'feminine wiles,' but the understanding dawns on her features after a moment's thought."

        show emicas angry_up
        with persistent.charachange

        emi "Wasn't anything of the sort!"

        show emicas frown_up
        with persistent.charachange

        emi "You were laughing! Feminine wiles don't involve laughing!"

        "I guess I can't argue with this."

        hi "That doesn't change your thievery."

        show emicas happy
        with persistent.charachange

        "Emi laughs at my injured tone and gives me a playful shove."

        show emicas closedsmile
        with persistent.charachange

        emi "Fine, you can have the instant noodles."

        hi "Are you kidding? That stuff's terrible!"

        hi "If anything, you should definitely eat it as punishment!"

        show emicas wink
        with persistent.charachange

        "Another laugh from the girl sitting on my legs."

        "…Both of which have fallen asleep by now."

        show expression im.Composite((531, 2160), (0, 0), "sprites/emicas/emicas_wink.png") as emicas:
            center
            ypos 1.13 yanchor 0.5
            easeout 0.8 rotate -90
        with None
        show expression im.Composite((531, 2160), (0, 0), "sprites/emicas/emicas_blush.png") as emicas:
            center
            ypos 1.13 yanchor 0.5
            easeout 0.8 rotate -90
        with Dissolve(0.2)
        pause 0.6

        hide emicas
        with vpunch

        "I twitch one leg to try waking it up, which has the unintended effect of unbalancing Emi, who falls to the side with a startled 'Eep!'"

        hi "Whoops! Sorry about that."

        hi "Legs fell asleep on me."

        "Emi remains on the ground, giggling."

        "I stand up a little shakily, feeling the nerves in my legs return to normal."

        "My eyes wander over the scenery before fixing on the figure of Emi, who has yet to get up."

        scene ev emi_parkback:
            xalign 0.5 yalign 0.5 zoom 1.1
            ease 10.0 zoom 1.0
        with locationchange

        "Her hair is splayed out around her head, her arms are spread, and laughter is bubbling up through her mouth."

        "Everything about Emi seems condensed into this one image."

        "Her energy, her spirit, her childish giggling."

        "The urge to lay down on the grass with her rises swiftly from the back of my mind to the forefront of my thoughts, and indeed I am convinced that I would love nothing more than to do just that."

        "Unfortunately the sun has set, and it is probably time for us to get back to the dormitories."

        "While Emi may be happy to stay out here all night, I don't think I have that ability."

        "Besides, homework soon beckons."

        "It wouldn't make sense to start thinking about things like university and then slack off, would it?"

        "I extend a hand to Emi to help her up."

        hi "We should probably get going."

        show ev emi_parkback_frown
        with charachangeev

        "Emi makes a sour face."

        emi "You're right."

        scene bg suburb_park
        with locationchange

        show emicas weaksmile_close:
            center
            ypos 1.2
            easein 0.5 center
        with charaenter

        show emicas at center

        "She grabs my proffered hand, and I pull her to her feet and into a hug."

        "This time I'm the one who kisses her, unable to resist having Emi against me."

        hi "Seems a shame to leave, you know."

        show emicas closedsmile_close
        with persistent.charachange

        emi "Yeah, it does."

        show emicas grin_up_close
        with persistent.charachange

        emi "But if we don't get back to the school soon, we'll probably get into trouble."

        "Emi pokes me in the ribs playfully."

        show emicas wink_up_close
        with persistent.charachange

        emi "And you need to do your homework, I'm sure."

        hi "Sadly, you're absolutely right."

        hide emicas
        with charaexit

        "I throw my arm around her shoulders, and we make the trek back to the school, accompanied by occasional bouts of laughter as our conversation jumps from subject to subject."

        "Everything from running, to school, to the peculiar way that one of the cafeteria workers smells."

        stop ambient fadeout 2.0

        scene bg school_dormext_full
        with locationskip

        "All too soon we find ourselves outside of the girls' dormitory building."

        show emicas closedsmile at center
        with charaenter

        emi "Well, I guess I'll be going, then."

        hi "I guess so, huh?"

        show emicas grin_up
        with persistent.charachange

        "Emi grins at me again with that mischievous look."

        emi "Are you going to be able to survive without me?"

        "I laugh."

        hi "I'm sure I'll manage."

        show emicas pout_up
        with persistent.charachange

        emi "How terrible! Aren't you supposed to say something like 'I'll be counting the seconds you are away?'"

        hi "Nah, I don't think so."

        show emicas closedsmile_close
        with characlose

        show emicas weaksmile
        with charadistant

        "Emi pulls me down into a quick goodbye kiss and steps back, looking unexpectedly shy."

        emi "Thanks for dinner."

        emi "I really had fun."

        show emicas closedsmile
        with persistent.charachange

        emi "Honestly, I did."

        hi "So did I."

        hi "I think we shall have to do it again, sometime."

        show emicas happy
        with persistent.charachange

        "Emi laughs at my deadpan delivery and nods."

        emi "See you bright and early tomorrow morning, right?"

        show emicas wink
        with persistent.charachange

        emi "You've gotta run off that bread, after all."

        hi "Of course. Despite the fact that you ate most of it."

        show emicas smile_up
        with persistent.charachange

        emi "Yes, despite that."

        show emicas grin_up
        with persistent.charachange

        emi "See you later, Hisao!"

        stop music fadeout 3.0

        show emicas:
            ease 1.0 xpos 0.6 alpha 0.0

        pause 1.0

        hide emicas

        "As Emi turns to head inside, I notice something weird."

        "Something so weird that I'm surprised I didn't notice it earlier."

        "She's limping slightly, favoring the left leg."

        play music music_pearly fadein 8.0

        hi "Hey, Emi!"

        show emicas neutral:
            tworight 
            alpha 0.0
            ease 1.0 center alpha 1.0
        with None
        show bg at bgleft
        with charamovefaster

        show emicas at center:
            alpha 1.0

        emi "Hmm?"

        hi "Is your leg okay?"

        show emicas awayfrown
        with persistent.charachange

        "Emi looks confused, or at least fakes confusion."

        show emicas frown
        with persistent.charachange

        emi "What are you talking about?"

        hi "Your right leg. You're limping."

        show emicas blush
        with charachangealways

        show emicas frown
        with charachangealways

        "There's the briefest flash of concern on Emi's face."

        "Either she didn't want me to know, or she didn't think I'd notice - or, I prefer to think, she just didn't realize it."

        show emicas neutral_up
        with persistent.charachange

        emi "Oh, that."

        "She shrugs casually."

        show emicas awayfrown
        with persistent.charachange

        emi "Must've gotten knocked a little out of alignment during the picnic."

        show emicas wink
        with persistent.charachange

        emi "No idea what would have caused that, of course."

        "I think back to being pinned under the tree."

        hi "Ah."

        hi "You should have told me! We could have stopped and fixed it, you know."

        "Emi waves a hand airily."

        show emicas smile_up
        with persistent.charachange

        emi "Nah, it's not that big of a deal."

        show emicas weaksmile_up
        with persistent.charachange

        emi "Don't worry about it, okay Hisao?"

        show emicas closedsmile_up
        with persistent.charachange

        emi "It's fine."

        menu:
            with menueffect
            "Why do I get the feeling that she's convincing herself as well as me?"

            "Press Emi.":
                $ pressed_emi = True

                call a3ec1o1
            "Let it rest.":
                $ pressed_emi = False

                call a3ec1o2

        show emicas smile
        with persistent.charachange

        emi "Now really, I need to get going."

        show emicas wink_up
        with persistent.charachange

        emi "Your attempts to keep me around are doomed to fail!"

        hi "Heh, of course."

        hi "Just prolonging the goodbye, I suppose."

        "Another grin lights up Emi's face."

        show emicas happy_up
        with persistent.charachange

        emi "Goodnight, Hisao."

        hi "Goodnight."

        hide emicas
        with charaexit

        stop music fadeout 5.0

        "As she limps inside, I find myself hoping she's okay despite her assurances that she's fine."

        "I think I can call this a successful first date."

        "Hell, any day that ends with Emi pinning me under a tree to kiss me can't be bad, can it?"

        "I head back to my room, mentally thank the gods that Kenji doesn't ambush me in the hallway, and get started on my homework."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .invisible_rock:
        scene bg school_dormhisao
        with locationchange

        play music music_night fadein 5.0

        "The morning is far too early for my taste."

        "It doesn't help that I had trouble sleeping last night."

        "There were simply too many things to think about. My mind refused to slow down."

        "Instead I replayed the rooftop, the park, and everything else over and over in my mind."

        "There's a small part of my mind that is still paranoid that this has all been some kind of joke."

        "That I'll meet up with Emi at the track, and she'll act like nothing happened yesterday."

        "Pushing these thoughts to the back of my mind, I throw on my running clothes and open the door."

        scene bg school_track
        show emi basic_grin_gym at center
        with locationskip

        "Emi's waiting for me with her usual smile."

        show emi basic_annoyed_gym
        with persistent.charachange

        emi "You're late!"

        show emi basic_closedgrin_gym
        with persistent.charachange

        emi "Or at least, you're not early today."

        show emi excited_hesitant_gym
        with persistent.charachange

        emi "Are you tired or something?"

        "I find myself ruefully rubbing the back of my head."

        hi "Something like that, yeah."

        hi "Lots to think about and all that."

        show emi basic_closedgrin_gym
        with persistent.charachange

        "Emi giggles at my mild understatement."

        show emi basic_grin_gym
        with persistent.charachange

        emi "Yeah, I didn't sleep that well either."

        show emi excited_proud_gym
        with persistent.charachange

        emi "I was actually glad you weren't early, 'cause I wasn't early either."

        "I wonder if the same thing kept us awake."

        "The image of her weeping face passes through my mind."

        hi "What kept you up?"

        show emi sad_shy_gym
        with persistent.charachange

        "Emi's expression falters, but she quickly notices my curiosity and forces a smile."

        show emi sad_grin_gym
        with persistent.charachange

        emi "Nothing important."

        "She's obviously not telling me something."

        "The question is, should I press the issue?"

        "Something's clearly been bothering her for a while."

        "I want to help her, but would it just come off as me being nosy?"

        "She's got to know I care about her, though."

        hi "Are you sure?"

        hi "If something's bothering you, I'm here to help you sort it out."

        show emi basic_closedhappy_gym
        with persistent.charachange

        "Emi laughs then, but it's not her usual laugh. There's an edge to it that seems almost bitter."

        show emi sad_grin_gym
        with persistent.charachange

        emi "Sort it out?"

        emi "I'm not sure it can be sorted out, Hisao."

        "An almost grim smile crosses her lips."

        "It's like a smile of resignation."

        show emi sad_pout_gym
        with persistent.charachange

        emi "I don't think you could help me, anyway."

        "That hurts."

        "I don't want to say that it hurts to her, but it does."

        "Doesn't she realize I want to be there for her when things go wrong?"

        hi "Well, I won't push you on the matter."

        hi "But I'm here for you if you decide later that you'd like to talk about it."

        hi "It might help."

        show emi sad_shy_gym
        with persistent.charachange

        "I can see the debate raging behind Emi's eyes."

        "It seems like she wants to tell me, but she's not sure whether or not she can."

        hi "Hey, forget about it for now, okay?"

        hi "We've got running to do."

        "The mention of running, something that she can handle, brings Emi back to her usual self."

        show emi basic_closedhappy_gym
        with persistent.charachange

        emi "Right!"

        show emi basic_grin_gym
        with persistent.charachange

        emi "Hurry up and stretch out, Hisao!"

        show emi excited_proud_gym
        with persistent.charachange

        emi "We've got to get moving!"

        play ambient sfx_emipacing

        show emi at offscreenleft
        with charamovefaster

        hide emi

        stop ambient fadeout 3.0

        "She takes off like a shot, far quicker than I'm used to."

        scene bg school_track_on
        with locationchange

        scene bg school_track_running
        with Dissolve(2.0)

        "Still, I try to keep pace with her, recklessly testing my limits."

        "It gives me a feeling of freedom, like my heart is no longer important."

        "I find myself wanting to laugh, filled with the feeling of moving beyond what I once called my boundaries."

        "The nurse's warnings to not overdo things echo in my mind, and I disregard them."

        "This feeling I have, this willingness to risk a heart attack for something so trivial as a morning run, feels out of character for me."

        "But is it?"

        "Or rather, should it be?"

        "I've got a weak heart, sure."

        "It'll never be capable of the kind of speed and endurance Emi's capable of."

        "Though I probably wouldn't be able to get that good even if I had a healthy heart."

        stop music fadeout 6.0

        "As we round the final bend, I feel my legs screaming in protest, but for the first time, I ignore them."

        "I accelerate to finish at a sprint, nearly catching up to Emi."

        "That was never going to happen, of course."

        "Still, I feel surprisingly good."

        "Oh sure, my legs feel like they're about to catch fire, and I'm having trouble staying upright."

        "But there's been a shift of some sort today."

        "And it's all thanks to the girl grinning at the finish line, waiting for me."

        scene bg school_track_on
        show emi basic_grin_gym at center
        with locationchange

        play music music_emi fadein 1.0

        hi "That felt a little faster than usual."

        "My comment is met with a grin and a shrug."

        show emi excited_proud_gym
        with persistent.charachange

        emi "Can't have you think I was going to go soft on you, now can I?"

        show emi basic_closedgrin_gym
        with persistent.charachange

        emi "But you managed to handle it just fine."

        hi "Well, I couldn't have done it without you."

        show emi basic_confused_gym_close
        with characlose

        "Still feeling the high from the run and moved by a surge of gratitude, I seize Emi in a hug."

        hi "Thanks."

        hi "Really, I'm not just saying that."

        hi "I'm in your debt."

        show emi basic_hes_gym_close
        with persistent.charachange

        "Emi seems flustered by my words, squirming uncomfortably."

        emi "Don't be silly, Hisao."

        show emi basic_grin_gym_close
        with persistent.charachange

        emi "Someone had to haul you out here, didn't they?"

        show emi basic_closedgrin_gym_close
        with persistent.charachange

        emi "And it's not like you're not doing anything for me, right?"

        show emi basic_grin_gym_close
        with persistent.charachange

        emi "I needed a running partner, remember?"

        show emi basic_shock_gym_close
        with persistent.charachange

        "I shake my head, still pointedly not letting go of Emi, who stops squirming and merely looks up at me with a quickly deepening blush that almost seems out of character."

        hi "No, that's not true."

        hi "You wanted a running partner, but you didn't need one."

        hi "If I hadn't shown up the day after the festival, you would still run, right?"

        hi "But it doesn't work the other way around."

        hi "I only managed to make it out a few times before the festival."

        hi "And without you, I probably wouldn't have made it out at all after that."

        show emi basic_closedgrin_gym_close
        with persistent.charachange

        "Emi smiles at me and prods my chest with one finger."

        show emi excited_proud_gym_close
        with persistent.charachange

        emi "You are pretty lazy, Hisao."

        hi "Hey, I was giving you a compliment!"

        show emi sad_grin_gym_close
        with persistent.charachange

        emi "Well… you're welcome, I guess."

        hi "I'll pay you back somehow."

        show emi basic_hes_gym_close
        with persistent.charachange

        emi "Oh, uh, well…"

        show emi basic_closedgrin_gym_close
        with persistent.charachange

        emi "That's not necessary, you know."

        show emi basic_happyblush_gym_close
        with persistent.charachange

        emi "I mean I kinda like you, Hisao."

        show emi sad_grin_gym_close
        with persistent.charachange

        emi "And being able to run with you in the mornings isn't exactly a bad deal for me either, so…"

        "For someone who gets so much praise, she seems unused to gratitude."

        "I can't think of anything else to say, so we fall silent."

        "I become aware of Emi's breathing, of the dampness of her clothing, and of the scent of her."

        "Coming off of anyone else, it would stink."

        "Coming off of Emi, it fits her in a way nothing else could."

        "Her skin is cool, slick with sweat, and a breeze causes goosebumps to rise."

        show emi excited_amused_gym_close
        with persistent.charachange

        "Almost without thinking about it, I lean down and meet Emi's mouth which has already moved to meet my own."

        "Her lips are soft, and she hums happily as we kiss, sending vibrations from her mouth to mine."

        "There's a startling rightness to everything about this moment. We fit one another perfectly."

        show emi basic_grin_gym_close
        with persistent.charachange

        "The kiss ends, and I finally let my arms drop back to my sides."

        show emi basic_closedgrin_gym_close
        with persistent.charachange

        "Emi is smiling warmly at me and giggles again."

        show emi basic_closedhappy_gym
        with charadistant

        emi "Come on Hisao, we'd better go see the nurse."

        stop music fadeout 1.0

        "Then it happens."

        show emi excited_sad_gym:
            center
            ypos 1.05
        with Dissolvemove(0.25)

        show emi at center
        with charamovecustom(0.25)

        "As she turns to begin walking, she gives out a tiny yelp and stumbles forward."

        hi "Emi!"

        play music music_rain fadein 2.0

        show emi excited_sad_gym_close
        with characlose

        "I leap to steady her and notice with some concern that she's favoring the same leg as last night."

        hi "Your leg…"

        show emi basic_hes_gym
        with charadistant

        "Emi seems panicked and pushes away from me."

        emi "It's fine!"

        "My expression must seem hurt, because she hastens to apologize."

        show emi basic_shock_gym
        with persistent.charachange

        emi "Sorry! Sorry!"

        emi "Didn't mean to push you like that!"

        show emi basic_closedsweat_gym
        with persistent.charachange

        emi "I was just…"

        "She stumbles for something to say."

        show emi sad_depressed_gym
        with persistent.charachange

        emi "It's nothing, really."

        hi "Hey, don't worry about it."

        "She's so flustered, I decide to shrug the whole thing off."

        "But there's a cold feeling in the pit of my stomach now that won't go away."

        "I tried to step in and help her, and she pushed me away."

        "Smiling, I shove those thoughts to the back of my mind and concentrate on Emi."

        hi "I just don't want you getting hurt, that's all."

        show emi sad_pout_gym
        with persistent.charachange

        emi "You don't have to worry about me, honest."

        show emi sad_grin_gym
        with persistent.charachange

        emi "I'm fine!"

        "Yes, you say that, but I don't believe you."

        if pressed_emi or _in_replay:
            "Why won't you tell me what's wrong?"

            "It's like she gets offended by my trying to help."

            "What am I supposed to make of that?"
        else:
            "I keep worrying about you regardless, and not saying anything yesterday just makes me feel guilty about today."

            "I should have at least asked."

            "Would she have reacted the same way last night?"

            "Guess I'll never know now."

        stop music fadeout 2.0

        scene bg school_nursehall
        with locationskip

        "I'm still trying to sort out what happened on the track as we arrive in front of the nurse's office."

        "Emi raises her hand to knock, hesitates and turns to me smiling guiltily."

        show emi sad_grin_gym:
            yalign 1.0 xanchor 0.5 xpos 0.47
            easein 0.5 center
        with charaenter

        show emi at center

        emi "Hey, can you do me a favor?"

        hi "Of course."

        show emi excited_proud_gym
        with persistent.charachange

        emi "Can you tell the nurse that I'll see him later?"

        show emi basic_grin_gym
        with persistent.charachange

        emi "I just remembered that I've got some… stuff to take care of before class."

        show emi sad_grin_gym
        with persistent.charachange

        emi "So I really need to get moving."

        show emi sad_shyblush_gym
        with persistent.charachange

        "I peer at her closely, and she fidgets under my stare."

        "Yeah, she's clearly just avoiding the nurse."

        "That leg of hers…"

        "Well, whatever. I said I'd help, and so I will."

        "But I'll make damn sure she sees the nurse before the day's out."

        hi "Yeah, okay. I'll let him know."

        show emi excited_smile_gym
        with persistent.charachange

        "Emi looks like I've just given her a pony on Christmas."

        show emi excited_joy_gym
        with persistent.charachange

        emi "Thank you so much!"

        show emi excited_amused_gym
        with persistent.charachange

        emi "You're the best, Hisao!"

        show emi excited_amused_gym_close
        with characlose

        "I am rewarded for my complicity in her lie by a kiss that makes it all worth it, or so I tell myself."

        hide emi
        with charaexit

        "As Emi heads out of the building, trying hard not to let her limp show, I knock on the door of the office."

        nk "Ah, Hisao. Come on in."

        play music music_nurse fadein 1.0

        scene bg school_nurseoffice
        show nurse neutral at center
        with locationchange

        nk "I don't see Emi with you."

        show nurse fabulous
        with persistent.charachange

        nk "She's not sick again, is she?"

        "From the tone of his voice, I don't think the nurse is expecting me to say 'Yes, she's ill.'"

        hi "Er, she said that she'd forgotten to do something, and so she had to skip out, but she'll see you later today."

        show nurse concern
        with persistent.charachange

        "The nurse heaves an exasperated sigh."

        nk "Honestly, that girl…"

        hi "Hmm?"

        show nurse neutral
        with persistent.charachange

        nk "She's been avoiding me."

        nk "Yesterday she was in and out of here without even taking off her prosthetics. And now this."

        "Well, at least it's not just me Emi doesn't want worrying."

        "That's a… comfort, I guess."

        "Still, I feel like I should say something about her leg. I said I'd lie for her, but she really needs to see him."

        hi "Now that you mention it, she was limping pretty badly today."

        hi "And last night as well."

        show nurse concern
        with persistent.charachange

        "The nurse's eyes narrow at the words 'last night.'"

        nk "And what exactly were you two doing last night?"

        hi "We were uh, on a date."

        show nurse fabulous
        with persistent.charachange

        "The nurse raises his eyebrows as if surprised."

        nk "Really? Interesting."

        hi "Huh?"

        show nurse neutral
        with persistent.charachange

        nk "Oh, nothing."

        "His gaze turns thoughtful, and then he grins at me."

        show nurse grin
        with persistent.charachange

        nk "You don't think you could use some of that boyfriend charm to get her to come see me today, could you?"

        hi "Of course!"

        hi "I was planning on doing that anyway."

        hi "I think she's really hurt and just pretending she isn't."

        show nurse neutral
        with persistent.charachange

        nk "Hmm, yes. She does that."

        nk "Afraid I'll make her stop running."

        hi "Will you?"

        show nurse concern
        with persistent.charachange

        nk "I don't like to, but if it's bad enough that she's been limping, well…"

        nk "I guess I'll have to see what's wrong for myself before I make that call."

        hi "I see."

        "Emi, not allowed to run? Perish the thought."

        "I don't know if she'd be able to function without running."

        "No wonder she's reluctant to admit anything's wrong."

        hi "Well, I'll make sure she sees you."

        show nurse neutral
        with persistent.charachange

        nk "Good. Oh, and before I forget…"

        show nurse grin
        with persistent.charachange

        "He grins at me again in what feels like a vaguely threatening manner."

        nk "Don't forget that I know what medications you're on."

        show nurse neutral
        with persistent.charachange

        nk "You be careful around Emi, got it?"

        "Wow. He looks serious, too."

        hi "Got it."

        hi "Don't hurt Emi. Wouldn't dream of it."

        show nurse grin
        with persistent.charachange

        nk "Grand!"

        show nurse fabulous
        with persistent.charachange

        nk "I'd hate for you to be late."

        hi "Huh?"

        show nurse grin
        with persistent.charachange

        nk "Late, as in the late Hisao Nakai."

        show nurse concern
        with persistent.charachange

        "He frowns briefly, dissatisfied."

        nk "Sounded better in my head…"

        show nurse neutral
        with persistent.charachange

        nk "Well, at any rate."

        show nurse grin
        with persistent.charachange

        nk "Get out of here before you miss your first class!"

        nk "You've got things to do, I'm sure. Shoo!"

        stop music fadeout 6.0

        "As I leave, I notice the nurse pulling out his phone and dialing a number."

        show nurse concern
        with persistent.charachange

        nk "Meiko, your daughter's being a pain in the ass again…"

        "I'd better head back to my room, or I really will be late."

        "Hey, wasn't he supposed to check my heart rate?"

        if _in_replay:
            return

    label .lunch_and_science:
        scene bg school_scienceroom
        with shorttimeskip

        play sound sfx_normalbell

        "The lunch bell sounds, and I bring myself out of the stupor I slipped into during the morning's classes."

        "My lack of sleep last night, coupled with the increased pace of this morning's run, has left me a little exhausted."

        $ renpy.music.set_volume(0.15, 0.0, channel="ambient")
        play ambient sfx_rooftop fadein 1.0

        scene bg school_staircase1
        with locationskip

        "Despite that, I find myself skipping stairs up to the roof."

        "There's a thrill of excitement now, in addition to the pleasure one gets from eating lunch with one's friends."

        play sound sfx_door_creak
        $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

        scene bg school_roof
        with locationchange

        "True, both Emi and Rin are still my friends, but Emi has become more than that now."

        "Rin is back in her usual spot on the roof, almost as if she'd never been absent."

        scene ev rin_roof_boredom
        show hisao rin_roof
        with locationchange

        hi "Feeling better, I take it?"

        show ev rin_roof_surprised
        with charachangeev

        "A raised eyebrow is my reward for speaking."

        rin "Better than what?"

        play music music_rin fadein 6.0

        hi "Er, better than you felt yesterday."

        show ev rin_roof_nonchalant
        with charachangeev

        "Rin gives my question some serious thought."

        rin "I'm not sure."

        rin "I think I might have felt rather good for some of yesterday, but it's all fuzzy."

        hi "Too much cold medicine?"

        show ev rin_roof_doubt
        with charachangeev

        rin "Well, I was asleep. And that usually is pretty good."

        show ev rin_roof_boredom
        with charachangeev

        rin "But I can't remember what it feels like to be asleep, because I'm not conscious for it."

        rin "It's a real problem."

        show ev rin_roof_nonchalant
        with charachangeev

        rin "Then again, if I knew how good it felt I might not sleep any more."

        rin "But this way I keep trying so I guess that's how I can keep from being overtired."

        hi "An eternal mystery to keep you sleeping at night?"

        show ev rin_roof_boredom
        with charachangeev

        rin "Maybe mystery's the wrong word. Intangibility might be the proper way to describe it."

        hi "I see."

        "No, I don't see at all. I have no idea what she's talking about, but that's okay, since I rarely do."

        show ev rin_roof_doubt
        with charachangeev

        rin "Do you remember what sleeping feels like?"

        rin "Like yesterday, do you remember what you felt like sleeping yesterday?"

        hi "Well, I actually didn't get a lot of sleep yesterday."

        show ev rin_roof_nonchalant
        with charachangeev

        rin "Hmm."

        rin "Maybe that's because you remember subconsciously."

        hi "Actually, I think I was worrying about Emi."

        show ev rin_roof_surprised
        with charachangeev

        rin "Doesn't Emi worry enough about herself?"

        "I hadn't considered that, but it gives me pause."

        hi "True, but would she ask for help if she needed it?"

        show ev rin_roof_doubt
        with charachangeev

        "Rin frowns, and I raise an eyebrow. Will I get a proper answer?"

        rin "Probably not. Is there something she should be asking for help with?"

        hi "Her leg, for starters."

        "This seems to catch Rin's interest."

        show ev rin_roof_disgust
        with charachangeev

        rin "Leg?"

        hi "It's hurt, but she won't see the nurse about it."

        "Rin shakes her head in disapproval."

        show ev rin_roof_doubt
        with charachangeev

        rin "You have to make her."

        show ev rin_roof_nonchalant
        with charachangeev

        rin "Like she makes me go to class. For her own good."

        rin "Otherwise she could lose her legs again, and that's just too weird."

        rin "Losing things twice."

        show ev rin_roof_doubt
        with charachangeev

        rin "Especially if you don't find them again to begin with."

        rin "Unless prosthetics are the same as finding something."

        show ev rin_roof_nonchalant
        with charachangeev

        rin "But that's a different kind of lost, isn't it?"

        hi "I think so."

        show ev rin_roof_boredom
        with charachangeev

        rin "Hmm. I wonder…"

        stop music fadeout 0.5

        show emi rin_roof
        with charaenter

        emi "Wonder what?"

        scene bg school_roof
        show emi basic_grin at center
        with locationchange

        "Emi seems to have snuck up on Rin and me, though Rin doesn't seem especially surprised. Which is itself unsurprising, I suppose."

        show bg at bgleft
        show emi at twoleft
        with charamove

        show rin basic_deadpannormal:
            tworight
            ypos 1.25
            easein 0.5 ypos 1.2
        with charaenter

        show rin

        "Rin manages to sit herself upright quite expertly, throwing her upper body forward and using her momentum to right herself."

        show rin basic_absent
        with persistent.charachange

        hi "Your leg. How's it feel?"

        show emi sad_annoyed
        show rin basic_awayabsent
        with persistent.charachange

        "That earns me a frown and a bit of a glare."

        emi "It's okay, I think."

        show emi sad_shy
        with persistent.charachange

        emi "Not worth worrying about."

        show rin basic_absent
        with persistent.charachange

        hi "Tell that to the nurse."

        hi "He's quite insistent that you visit him, you know."

        show emi sad_pout
        show rin basic_awayabsent
        with persistent.charachange

        "Emi pouts like I've just told her she's been grounded."

        emi "He worries too much."

        show emi basic_grin
        with persistent.charachange

        emi "It's not a big deal, just a little soreness."

        "I try to resist rolling my eyes in exasperation."

        show rin basic_absent
        with persistent.charachange

        hi "If it's nothing, then you should have no problem seeing him, right?"

        show emi basic_annoyed
        show rin basic_awayabsent
        with persistent.charachange

        "Emi narrows her eyes suspiciously."

        emi "Did he put you up to this?"

        show rin basic_absent
        with persistent.charachange

        hi "Well, maybe. A little."

        hi "But that's not the point. I would have reminded you to see him anyway."

        hi "It would be terrible to see you really hurt and not doing anything about it."

        hi "That would make it worse, and I don't really want to see you hurt, you know?"

        hi "Call me crazy, but I kinda would prefer to see you happy and healthy."

        show emi sad_grin
        show rin basic_awayabsent
        with persistent.charachange

        "With each statement, Emi's frown fades a little more, until eventually she's grinning, albeit a little shyly."

        play music music_daily fadein 4.0

        emi "Well, if you're going to put it that way, then I guess I'll have to see him."

        show emi excited_proud
        with persistent.charachange

        emi "Otherwise you'll keep worrying, and then I'll never hear the end of it, right?"

        show rin basic_absent
        with persistent.charachange

        hi "That's right. I'll keep bugging you about it, and that might put a damper on our dates."

        hi "'How's the food, Hisao?' 'Talk to the nurse, Emi.'"

        hi "'How was your day, Hisao?' 'Talk to the nurse, Emi.'"

        hi "'Hisao, I think I'm ready to go all the w—' '{b}Talk to the nurse, Emi.{/b}'"

        hi "See? It doesn't work that well."

        show emi basic_closedhappy
        show rin basic_awayabsent
        with persistent.charachange

        "Emi giggles at my high-pitched rendition of her own voice and gives me an affectionate shove."

        show emi excited_amused
        with vpunch

        emi "My voice isn't that high, jerk."

        show rin basic_deadpan
        show emi excited_circle
        with persistent.charachange

        rin "I thought it was pretty accurate."

        pause 3.0

        "Emi and I stare at Rin for a while before I burst into laughter."

        show emi sad_annoyed
        show rin basic_awayabsent
        with persistent.charachange

        "Emi crosses her arms and huffs, mock-offended."

        show emi sad_angry
        with persistent.charachange

        emi "You're both jerks."

        show rin basic_absent
        with persistent.charachange

        hi "Such vile calumnies from you, young woman."

        hi "I'm stunned that you would call me, of all people, a jerk."

        hi "Honestly, I just… I don't know what to think."

        show emi basic_annoyed
        show rin basic_awayabsent
        with persistent.charachange

        "Emi sticks her tongue out at me."

        emi "You ass."

        show emi basic_grin
        with persistent.charachange

        emi "So Rin, how's the art club these days?"

        show rin basic_surprised
        with persistent.charachange

        "Rin, seemingly as surprised by this sudden change of topic as I am, takes a minute to think before answering."

        show rin basic_lucid
        with persistent.charachange

        rin "I believe it is okay."

        show rin basic_deadpancontemplation
        with persistent.charachange

        rin "Although Nomiya keeps telling me to work harder."

        show rin relaxed_nonchalant
        with persistent.charachange

        rin "But I don't think he understands my methods."

        show emi sad_annoyed
        with persistent.charachange

        emi "He always struck me as slightly creepy."

        show rin basic_lucid
        with persistent.charachange

        "Rin ponders this statement for a while."

        show rin basic_awayabsent
        with persistent.charachange

        rin "I've never really noticed."

        show rin basic_deadpancontemplation
        with persistent.charachange

        rin "But I don't pay much attention to him most days, so maybe that's why."

        hi "How often do you meet?"

        show emi basic_closedgrin
        with persistent.charachange

        emi "Thinking of joining, Hisao?"

        show rin basic_absent
        with persistent.charachange

        hi "What? Nah, I've already decided to join a club."

        show emi excited_happy
        show rin basic_awayabsent
        with persistent.charachange

        emi "Really? Which one?"

        show rin basic_absent
        with persistent.charachange

        hi "Well, it's not really much of a club, to be honest…"

        show emi excited_proud
        show rin basic_awayabsent
        with persistent.charachange

        emi "Oh, you joined the tea club?"

        show rin basic_absent
        with persistent.charachange

        hi "No, I uh… joined the science club… I think."

        show emi basic_confused
        show rin basic_awayabsent
        with persistent.charachange

        "Emi looks highly confused."

        emi "We have a science club?"

        show rin basic_absent
        with persistent.charachange

        hi "Er, not really. It's just me."

        show emi basic_closedhappy
        show rin basic_awayabsent
        with persistent.charachange

        emi "Hisao, that's not a club. That's sitting in your room reading books."

        hi "No, I mean it's just me and Mutou."

        hi "I'm just the only student so far."

        show emi basic_confused
        show rin basic_lucid
        with persistent.charachange

        emi "Mutou? Really?"

        "A thought strikes her."

        show emi basic_happy
        with persistent.charachange

        emi "Oh, is that what you were talking about yesterday? Your meeting with Mutou?"

        hi "Yeah, that was our first meeting, I guess."

        show emi basic_closedgrin
        with persistent.charachange

        "Emi giggles."

        show emi basic_grin
        with persistent.charachange

        emi "Nerd."

        hi "Hey, I can't help being clever."

        show emi excited_proud
        with persistent.charachange

        emi "You know, I could have used your help years ago."

        emi "You should've had your heart attack earlier in life, Hisao."

        "I laugh, and then realize this is probably one of the very rare times I've laughed about my heart attack."

        hi "Hindsight…"

        show emi sad_grin
        with persistent.charachange

        emi "Yeah…"

        play sound sfx_warningbell

        "The ringing of the bell ends our conversation."

        hi "Hmm, guess we'd better go."

        show emi basic_grin
        with persistent.charachange

        emi "Yeah, I guess so."

        show emi excited_amused:
            center
            xpos 0.45
        with charamovechangefaster

        emi "Come on Rin, you too."

        show rin basic_surprised
        with vpunch

        "Rin has apparently begun to doze off, so Emi gives her a sharp bump."

        show rin basic_deadpanupset
        with persistent.charachange

        rin "I almost had it."

        show emi basic_closedgrin
        with persistent.charachange

        emi "Sorry, but you need to go to class."

        show rin relaxed_nonchalant at tworight
        with charamovechangefaster

        rin "I disagree, but maybe if I nap in class I'll get it this time."

        show rin relaxed_boredom
        with persistent.charachange

        rin "Changing location is sometimes helpful for that kind of thing."

        "Neither Emi or I bother asking what 'it' is."

        stop music fadeout 3.0
        stop ambient fadeout 2.0
        scene bg school_hallway3
        with locationskip

        "As we arrive at my classroom, Emi gives me a quick kiss and heads down the hallway, Rin in tow."

        show shizu behind_blank:
            tworight
            xpos 0.8
            easein 0.5 tworight
        show misha perky_smile:
            twoleft
            xpos 0.2
            easein 0.5 twoleft
        with charaenter

        show shizu at tworight
        show misha at twoleft

        "I turn to enter the classroom, to be met by the duo of Shizune and Misha."

        play music music_shizune fadein 1.0

        show shizu adjust_happy
        with persistent.charachange

        shi "…"

        "Misha seems to be fighting a losing battle to keep from breaking into a fit of giggles while she translates Shizune's latest rant."

        show misha hips_grin
        with persistent.charachange

        mi "While we are pleased, nay thrilled, to see how well you've managed to make new friends and forge relationships - and with such a cutie too, Hicchan~…"

        "I think that last part was probably Misha."

        show shizu basic_normal
        with persistent.charachange

        shi "…"

        show misha hips_frown
        with persistent.charachange

        mi "We nevertheless feel compelled to politely remind you that public displays of affection are strictly forbidden - really? That's disappointing, Shicchan - by section eight of the code of conduct laid out in the student handbook."

        show shizu adjust_smug
        with persistent.charachange

        shi "…"

        show misha sign_smile
        with persistent.charachange

        mi "In this case, however, ignorance of the law may be your excuse, as we are feeling lenient…"

        show shizu behind_smile
        with persistent.charachange

        shi "…"

        show misha hips_smile
        with persistent.charachange

        mi "…and the paperwork required to punish the both of you would only add to the already mountainous volume of work which confronts us, the sole members of the Student Council - and besides, you two are adorable together~!"

        show shizu adjust_happy
        with persistent.charachange

        shi "…"

        show misha hips_grin
        with persistent.charachange

        mi "Therefore consider this a formal warning, and please refrain from such displays in the future. At least when Shizune can see you, Hicchan~!"

        "This whole spiel is so patently ridiculous that I can't help but reply in the same pompous manner."

        hi "Well, I for one feel enlightened."

        hi "I apologize profusely for my rash actions and will strive to contain my baser impulses which, I fear, impel me toward such inappropriate displays of public affection."

        hi "It is hardly my wish to burden an already overworked Student Council with such petty matters, and will do my best to make your lives easier in this matter in the future."

        hi "At least, when Shizune's watching."

        "This last line is delivered with a wink to Misha, who finally loses control of her laughter."

        show misha cross_laugh
        with persistent.charachange

        mi "Wahaha~!"

        show misha cross_grin
        with persistent.charachange

        mi "Well said, Hicchan~!"

        "Chuckling a little myself, we enter the classroom."

        stop music fadeout 2.0
        scene bg school_scienceroom
        with shorttimeskip

        "Class is uneventful, and after the final bell rings, I find myself alone with Mutou again."

        show muto smile at center
        with charaenter

        mu "So, it looks like we've all assembled for the second meeting of the Science Club."

        play music music_another fadein 2.0
        show muto normal
        with persistent.charachange

        mu "Or is it the first? What do you think, should we count yesterday as a meeting?"

        hi "Well, we did form the club yesterday, didn't we?"

        hi "That seems like club business, so we can safely call yesterday a meeting."

        show muto smile
        with persistent.charachange

        "Mutou smiles in his usual stilted and awkward way. I wonder if the muscles in his face are just not shaped correctly to let him smile naturally."

        mu "You really do have a knack for this, I think. Logical thought processes, that is."

        hi "I guess so?"

        show muto normal
        with persistent.charachange

        mu "A scientist speaks with authority, Hisao. The answer here is 'Yes, I do.'"

        mu "When the world wants to know how it works, we tell it. Even if all we've got is a decent hypothesis."

        show muto smile
        with persistent.charachange

        mu "But we must sound certain anyway, because we're the authorities on the subject, right?"

        "He chuckles, to go along with his awkward smile at his awkward joke. I'm doing my best not to grimace, but I don't think I'm being too successful."

        show muto normal
        with persistent.charachange

        mu "That's entirely false, of course."

        mu "We know a lot, sure, but nobody's an expert on how the world works, if only because nobody can be sure. With no certainty, there are no experts."

        mu "But we like to pretend, sometimes."

        hi "There's some things we can be certain of, right?"

        mu "Yes… but no."

        mu "We know gravity's there, for example."

        "To illustrate, Mutou picks up a pencil and drops it."

        mu "See? Still there. But it's good to check every once in a while."

        mu "That's why you'll still see researchers mucking about with gravity."

        show muto smile
        with persistent.charachange

        mu "We're pretty sure we know how it works, but there's always a chance that something isn't how we think it is."

        mu "So you check, and check, and check. That's science in a nutshell, Hisao."

        "The whole time I've listened feeling rather spellbound. Mutou seems to really be passionate about this stuff… I think. It's hard to tell, sometimes."

        "How the world works…"

        "How humans work."

        "How the universe works."

        "All these questions to be answered."

        "And, depending on what I go into, maybe I could even figure out a way to fix my heart. That said, I don't think that's a real priority for me."

        "Besides, as we start discussing the book he gave me yesterday, I find myself more and more interested in that than my heart condition."

        show muto normal
        with shorttimeskip

        "Before we even realize it, an hour's gone by."

        mu "Well, let's call this meeting over for now, okay?"

        mu "We'll have another meeting… tomorrow, or uh… the day after."

        "He considers this for a moment."

        mu "Call it the day after. I've got a lot of grading to do."

        hi "Okay. See you then."

        scene bg school_hallway3
        with locationchange

        stop music fadeout 5.0

        "As I exit the classroom, I realize that I don't really have anything to do tonight."

        "Emi and I didn't make plans, so…"

        "I guess I'll go to the library. It beats doing homework in my room, anyway."

        scene black
        with Dissolve(0.5)

        if _in_replay:
            return

    label .up_down_and_up_again:
        play music music_happiness fadein 2.0
        scene bg school_library
        with Dissolve(0.5)

        "The library always seems cooler than the rest of the building."

        "Probably to keep the books from getting damaged by excessive heat and humidity."

        "Books are sturdy objects, but if you want to keep them in good condition it takes a little effort."

        "I've got several books that are so well-worn the pages are barely clinging to the spine."

        "It seems impossible for them to still be usable, but if you handle them with care…"

        "I make my way to the main desk, where I spot Yuuko busying herself with something or another."

        show yuuko neutral_up at center
        with charaenter

        "She smiles at me as I enter and waves."

        show yuuko closedhappy_down
        with persistent.charachange

        yu "Hello, Hisao."

        show yuuko happy_down
        with persistent.charachange

        yu "Good to see you again! What are you looking for this time?"

        hi "Nothing in particular, I guess. I just didn't really feel like going back to my room, is all."

        show yuuko neutral_down
        with persistent.charachange

        "Yuuko nods."

        show yuuko smile_up
        with persistent.charachange

        yu "Well, if you're unoccupied, maybe you could help me look for something?"

        hi "Sure, what do you need?"

        stop music fadeout 5.0

        show yuuko worried_up
        with persistent.charachange

        "Yuuko brings a finger to her lips and looks around furtively."

        "She seems to be looking for eavesdroppers."

        yu "Come closer."

        show yuuko worried_up_close
        with characlose

        "I take a few hesitant steps forward while feeling distinctly unnerved."

        "Yuuko lowers her voice to a confidential whisper."

        show yuuko neutral_up_close
        with persistent.charachange

        yu "I'm on the trail of the Yamaku Cat Burglar."

        play music music_tension fadein 0.5

        hi "The what?"

        show yuuko panic_up_close
        with persistent.charachange

        yu "Shh! The walls have ears, Hisao!"

        yu "Or they might."

        show yuuko worried_down_close
        with persistent.charachange

        yu "But listen! Those missing books, remember them?"

        hi "Er, yeah?"

        show yuuko worried_up_close
        with persistent.charachange

        yu "Well, they weren't missing! They were stolen!"

        yu "I'm convinced of it!"

        hi "I remember you saying something of the sort earlier, but how do you know?"

        "Yuuko leans in closer and, if possible, whispers even lower."

        show yuuko closedhappy_down_close
        with persistent.charachange

        yu "Because I found one of his hiding places!"

        hi "You did what?"

        "Yuuko looks triumphant."

        show yuuko happy_up_close
        with persistent.charachange

        yu "Found one of his stashes! It was under one of the stairwells in the boy's dorm!"

        yu "Three books I'd been looking for, all there!"

        show yuuko closedhappy_up_close
        with persistent.charachange

        yu "I'd suspected a thief before, but this proves it!"

        hi "So did you take back the books?"

        show yuuko panic_up_close
        with persistent.charachange

        "Yuuko looks as if I've just suggested she walk around naked."

        yu "Are you nuts?"

        show yuuko worried_down_close
        with persistent.charachange

        yu "He can't know I'm on to him! He might go to ground and evade capture!"

        hi "Uh… huh. So what do you need my help with, then?"

        "Yuuko casts another glance around the library and leans in closer."

        show yuuko neutral_down_close
        with persistent.charachange

        yu "You've got to spy for me."

        hi "Spy?"

        yu "Yeah, like when you're in the dorms, you know."

        show yuuko closedhappy_down_close
        with persistent.charachange

        yu "Keep an eye out for suspicious activity."

        "What constitutes suspicious, anyway?"

        "I mean Kenji's a pretty suspicious dude, but I'll wager he barely goes to class, much less sneaks into the library to pilfer books."

        "Still, what's the harm in saying yes? At the least it'll get me out of this weird conversation."

        hi "Yeah, I can do that. No problem."

        show yuuko closedhappy_down
        with charadistant

        "Yuuko straightens up and claps excitedly."

        yu "Great!"

        show yuuko worried_down
        with persistent.charachange

        yu "Now, hurry up and talk about something else in case someone comes in!"

        stop music fadeout 2.0

        show yuuko happy_down
        with persistent.charachange

        yu "How's the school treating you?"

        hi "Er, pretty well, actually."

        hi "I've been running in the mornings with—"

        show yuuko closedhappy_up
        with persistent.charachange

        yu "Emi Ibarazaki, right?"

        play music music_comedy fadein 2.0

        hi "Uh, yeah."

        hi "How'd you know?"

        show yuuko smile_down
        with persistent.charachange

        yu "I served you two in the teahouse, remember?"

        show yuuko closedhappy_down
        with persistent.charachange

        yu "I deduced that if you were going to run with anyone, it would probably be her."

        "She looks pleased with herself."

        hi "Impressive."

        hi "Anyway, yes. We've been running in the mornings."

        hi "And uh, we kinda started dating."

        show yuuko closedhappy_up
        with persistent.charachange

        "Yuuko claps her hands together excitedly."

        yu "Really? That's great!"

        yu "I'll bet you two are great together!"

        show yuuko neutral_down
        with persistent.charachange

        yu "I love seeing people find one another like that, you know?"

        yu "I even thought to myself when you walked into the Shanghai that one time, 'I wonder if that kid will wind up with one of those girls.'"

        hi "…Really?"

        "Yuuko doesn't seem to notice my somewhat weirded out tone and nods affirmatively."

        show yuuko closedhappy_down
        with persistent.charachange

        yu "Yup! I could tell that you'd wind up with one of them, you know."

        show yuuko neutral_down
        with persistent.charachange

        yu "I've got an eye for that sort of thing."

        show yuuko worried_down
        with persistent.charachange

        yu "Of course…"

        "Her expression droops slightly."

        yu "I'm not so good at it myself."

        hi "Aw, I'm sure that's not true."

        show yuuko neutral_down
        with persistent.charachange

        yu "Oh, it's true."

        yu "I met this guy once…"

        show yuuko smile_down
        with persistent.charachange

        yu "We got along really great, but it turned out he was younger than me."

        show yuuko neutral_up
        with persistent.charachange

        yu "And that was kinda weird, but not terribly so."

        yu "What was really weird was that he disappeared one day, and I've not seen him since then."

        hi "Huh. That does seem kind of odd."

        show yuuko worried_up
        with persistent.charachange

        yu "Doesn't it?"

        show yuuko neurotic_down
        with persistent.charachange

        yu "I hope it wasn't something I did…"

        "I feel compelled to reassure her."

        hi "I'm sure it wasn't."

        stop music fadeout 4.0

        $ renpy.music.set_volume(0.5, 0.0, channel="sound")
        play sound sfx_phone
        show yuuko panic_up
        with vpunch

        "I intend to try and calm her down further, but the both of us jump in surprise at the ringing suddenly coming from my pocket."

        show yuuko worried_down
        with persistent.charachange

        "Yuuko sighs to steady herself as I pull the phone from my pocket. I feel a little sheepish for indirectly causing the incident."

        scene bg school_library_yuuko_blurred
        show phone mobile:
            xalign 0.5 yanchor 0.5 ypos 0.7 alpha 0.0
            easein 1.0 yalign 0.5 alpha 1.0
        with locationchange

        pause 0.5

        hi "Emi? What's up?"

        emi "Oh thank God I haven't called your phone before so I didn't know if this number would work or whether you would pick up and I can't—"

        $ renpy.music.set_volume(1.0, 0.0, channel="sound")
        play music music_pearly fadein 2.0

        hi "Woah there Emi, slow down."

        hi "What's wrong?"

        "There's a pause on the other side of the line, during which I can hear Emi trying to control her breathing in order to calm down."

        "Something's got her terribly agitated, and it's starting to agitate me."

        emi "Can you just…"

        emi "Can you stop by?"

        emi "Like, now? Or shortly after now?"

        emi "I really, really need to talk to you."

        "There's a tone of pleading in the last sentence that I don't think I've ever heard from her."

        hi "Of course, I'll be right there."

        hi "Hold steady, okay?"

        "In my increasingly agitated state I've apparently started saying things that don't quite make sense."

        emi "Okay. I'll be okay."

        hi "See you soon."

        show phone mobile:
            xalign 0.5 yalign 0.5
            easeout 1.0 ypos 0.7 alpha 0.0

        scene bg school_library
        show yuuko worried_down at center
        show phone mobile:
            xalign 0.5 yalign 0.5
            easeout 1.0 ypos 0.7 alpha 0.0
        with locationchange

        pause 0.5

        hide phone
        with charaexit

        "I press the button to end the call before slipping the phone back into my pocket, apologize to Yuuko for running off, and run off."

        scene bg school_girlsdormhall
        with locationskip

        "Perhaps at some point I would have stopped to think about the time, or how suspicious it looks for a guy to enter the girls' dorm at this hour."

        "Except right now I'm just concerned with getting to Emi and finding out what's wrong and how I can help her."

        play sound sfx_doorknock2

        "I knock on the door and am greeted with a subdued 'Come in.'"

        scene bg school_dormemi at left
        with locationchange

        "Something is very wrong as I stare at the scene before me."

        "Emi's there, yes."

        "But she's in a wheelchair."

        "And her legs are missing. I glance around the room and see them sitting in a corner, looking like they've been thrown there."

        show emiwheel weaksmile at center
        with charaenter

        "Emi responds to my entrance with a lopsided grin that is both pleased to see me and completely, utterly heartbroken."

        emi "Hi, Hisao."

        "It looks like she's been crying, but if she was, she's stopped now."

        "I notice that I'm a little out of breath, having taken the stairs two at a time in order to get here."

        "My heart doesn't seem to mind the strain, though. I file this happy fact away for later consideration."

        "Like when I am not staring somewhat dumbstruck at my girlfriend in a wheelchair."

        "Realizing I've still not responded to her greeting, my brain lurches into gear."

        hi "Emi? What happened?"

        show emiwheel pout
        with persistent.charachange

        emi "Guess I should've listened to you, Hisao."

        show emiwheel sad
        with persistent.charachange

        emi "My leg's got a nasty infection. I'm not allowed to run on it for at least a couple of weeks."

        "She gives a bitter laugh that shouldn't be coming from her."

        show emiwheel frown
        with persistent.charachange

        emi "Heh, I can't even walk on it."

        emi "I could have used a crutch and kept one of my legs, but I didn't see the point."

        show emiwheel awayfrown
        with persistent.charachange

        emi "Why hop? You can't run on one leg."

        show emiwheel pout
        with persistent.charachange

        emi "At least this way I can still, I dunno, roll fast or something."

        hi "Y-yeah, that's good, right?"

        "My awkward attempt to look on the bright side seems appreciated, but not really effective."

        "Emi shrugs again."

        show emiwheel awayfrown
        with persistent.charachange

        emi "It's just… kind of a nuisance."

        show emiwheel frown
        with persistent.charachange

        emi "I mean, we can't even eat up on the roof now. No wheelchair access."

        hi "Yeah, but that's not a big deal, right?"

        hi "I mean we can still eat together, and that's the important thing."

        show emiwheel weaksmile
        with persistent.charachange

        "That lopsided grin again. It hurts to look at."

        emi "I suppose so, yeah."

        show emiwheel frown
        with persistent.charachange

        emi "But like I said, it's a nuisance."

        show emiwheel awayfrown
        with persistent.charachange

        emi "I mean, I haven't really used a wheelchair in…"

        stop music fadeout 10.0

        "She thinks for a minute."

        show emiwheel pout
        with persistent.charachange

        emi "Maybe seven years? Something like that, anyway."

        emi "A long time."

        show emiwheel weaksmile
        with persistent.charachange

        emi "I'm afraid I'm a bit out of practice."

        hi "Well, fortunately it's only temporary, right?"

        "Emi nods."

        show emiwheel neutral
        with persistent.charachange

        emi "Oh yeah, of course."

        emi "It's not like I've lost 'em permanently."

        show emiwheel awayfrown
        with persistent.charachange

        emi "But it's a pain in the ass all the same."

        "I nod sympathetically."

        "There's not much else I can do, after all."

        "What am I gonna do, say 'I told you so?'"

        "Although I {b}did{/b} tell her to get that leg looked at."

        "But by the time I noticed, it was too late anyway."

        hi "Do you need help with anything?"

        hi "Er, that is, can I help with anything?"

        show emiwheel closedsmile
        with persistent.charachange

        "Emi shakes her head and there's a bit of her usual grin back."

        emi "Nah, I can manage fine by myself."

        show emiwheel grin
        with persistent.charachange

        emi "Although if you want to help me over to my bed, it would save me the trouble of rolling over there myself."

        "I blush, in spite of myself."

        "Emi giggles."

        play music music_heart fadein 0.5

        show emiwheel wink
        with persistent.charachange

        emi "You're such a prude, Hisao."

        hi "I'm not a prude! I just wouldn't want to take advantage of a young woman such as yourself."

        hi "It's ungentlemanly."

        hide emiwheel
        with charaexit

        show bg at right
        with charamove

        "I wheel Emi's chair to her bed, and easily scoop her up and deposit her there. She quickly sorts herself out and sits on the side."

        show emi basic_grin:
            center
            easein 0.5 ypos 1.1
        with charaenter

        show emi:
            center
            ypos 1.1

        "She's actually a little heavier than she looks. It would be rude of me to observe this aloud, of course."

        hi "Man, you're kind of heavy."

        play sound sfx_pillow
        show comic vfx2 at truecenter
        show emi excited_amused
        with hpunch

        pause 0.5

        show comic vfx2:
            easeout 0.5 yanchor 0.3 alpha 0.0

        pause 0.5

        "Emi hits me with a pillow."

        show emi basic_closedgrin
        with persistent.charachange

        emi "Ass."

        hi "Just sayin', is all."

        hi "Must be all that running."

        show emi sad_shy
        with persistent.charachange

        "At the mention of running Emi's grin falters slightly."

        show emi sad_pout
        with persistent.charachange

        emi "Heh, well I guess I won't have to worry about that for a bit, huh?"

        show emi sad_grin
        with persistent.charachange

        emi "Maybe I'll lose some weight."

        hi "That's what you do to lose weight, right? Cease physical activity?"

        show emi basic_closedgrin
        with persistent.charachange

        emi "I'm pretty sure that's what the nurse would recommend."

        hi "Speaking of which, are you going to still be showing up in the mornings?"

        hi "I'd hate to run alo—"

        show emi sad_depressed
        with persistent.charachange

        emi "Ah, shit…"

        "Emi's sudden interjection, more a disquieted muttering than anything too profane, causes me to look over in shock."

        "She's leaning forward, trying to cover the fact that she's crying by covering her eyes with a hand."

        "Of course, the subdued sobbing makes it pretty obvious that she's crying."

        hi "Hey, I'm sorry."

        hi "Forget I said anything, okay?"

        show emi sad_depressed_close at center
        with characlose

        "I place a hand gingerly around her and pull her close."

        "I can think of nothing else to say or do. How do you comfort someone who's just lost their legs again?"

        show emi sad_pout_close
        with persistent.charachange

        "Emi wraps me in a hug and stays that way for a while."

        hi "Sorry."

        hi "I'm pretty bad at this whole comforting thing, I guess."

        emi "Don't say that."

        emi "I'm fine, really."

        "Her voice is slightly muffled by my chest. I pat her head reassuringly."

        hi "That's the spirit, right?"

        hi "You'll get through this fine, I know it."

        hi "Besides, I'm here to help you, remember?"

        show emi sad_shy_close
        with persistent.charachange

        "Emi lifts her head and stares at me with tear-stained eyes."

        show emi sad_grin_close
        with persistent.charachange

        emi "Can you? Can you really?"

        "She's grinning lopsidedly, and something sparkles in her gaze."

        "I can't tell if I'm being mocked or not."

        hi "Of course. I mean sure, you're a bit heavy, but -{w=0.5}{nw}"

        play sound sfx_impact

        show emi excited_amused_close
        with vpunch

        extend " mmph!"

        "My witty comment is cut off by the sudden press of Emi's lips on mine. I'm caught off guard, and am rewarded by hitting my head on the wall behind her bed."

        hi "Ow."

        show emi basic_hes
        with charadistant

        "Emi pulls back, trying to look concerned rather than like she's about to laugh."

        emi "Are you okay?"

        show emi excited_proud
        with persistent.charachange

        emi "Sorry!"

        "I rub my head ruefully and grin back at her."

        hi "Caught me off guard, there."

        hi "Is that going to become a habit? Am I going to be lectured by Shizune and Misha more?"

        "At the mention of the duo, Emi giggles."

        show emi basic_closedgrin
        with persistent.charachange

        emi "Honestly, those two…"

        show emi basic_grin
        with persistent.charachange

        emi "If I didn't know why, I'd be utterly confused as to why she hangs around with someone so bossy."

        hi "Which one are we talking about?"

        show emi basic_closedhappy
        with persistent.charachange

        emi "You know exactly which one, Hisao. Misha's hardly bossy."

        hi "So what's the reason, then?"

        show emi basic_confused
        with persistent.charachange

        emi "Huh?"

        hi "The reason why Misha hangs around Shizune."

        show emi basic_closedgrin
        with persistent.charachange

        "Emi waves my question off with a smile."

        emi "No idea."

        hi "I see."

        show emi basic_grin
        with persistent.charachange

        emi "Anyway, you seem to be forgetting the original question, don't you?"

        hi "Oh yeah, I guess I am."

        hi "You wouldn't mind giving a guy a little warning, would you?"

        hi "Otherwise I'm liable to wind up with a concussion."

        "I emphasize the point by rubbing at the back of my head."

        show emi excited_amused
        with persistent.charachange

        "Emi giggles madly."

        emi "You could wear a helmet."

        show emi excited_proud
        with persistent.charachange

        emi "Some kids here do, you know."

        stop music fadeout 1.0

        hi "Or I could just take revenge!"

        play sound sfx_pillow

        show emi excited_circle
        with vpunch

        "I grab a pillow from beside me and whack Emi over the head."

        show expression im.Composite((531, 2160), (0, 0), "sprites/emi/emi_excited_circle.png") as emi:
            center
            yanchor 0.5
            easeout 0.8 ypos 1.25 rotate -90
        with None
        show expression im.Composite((531, 2160), (0, 0), "sprites/emi/emi_excited_sad.png") as emi:
            center
            yanchor 0.5
            easeout 0.8 ypos 1.25 rotate -90
        with Dissolve(0.5)
        pause 0.3

        play sound sfx_impact

        hide emi
        with vpunch

        "Emi topples off the bed and lands on the floor with a thump."

        show emi sad_pout:
            center
            ypos 1.2
            ease 1.0 ypos 1.0
        with Dissolve(1.0)

        "Her arms promptly reappear on the bed, and she manages to pull herself back up."

        "She really has a surprising amount of strength in that little body."

        "Her face is turned downwards and away from mine, making me think I might have accidentally hurt her."

        hi "Emi? You okay?"

        hi "You didn't hit your—{w=0.3}{nw}"

        show emi excited_smile_close
        with vpunch

        "A hand shoots up and grabs my collar. She pulls me in with a sharp tug, her face now barely an inch away from mine as she grins cheekily."

        hi "Emi…?"

        show emi excited_smile_close:
            linear 0.1 ypos 1.7 zoom 2.0

        scene white
        with Dissolve(0.1)

        play sound sfx_impact

        scene black
        with Dissolve(0.75)

        "She gives me a sharp headbutt, our foreheads making quite a loud thud."

        scene bg school_dormemi at right
        show emi basic_closedgrin at center
        with openeye

        "I sit back and rub my now sore head as Emi smirks victoriously."

        show emi basic_grin
        with persistent.charachange

        emi "How's {b}that{/b} for revenge?"

        play music music_running

        hi "No fair!"

        hi "You can't take revenge for revenge!"

        "For someone missing most of her legs, Emi's surprisingly agile."

        show emi basic_grin:
            center
            parallel:
                "emi basic_closedgrin" with Dissolve(0.2)
            parallel:
                easeout 0.5 xpos 0.3 alpha 0.0

        pause 0.5

        hide emi

        "I swipe at her, but she deftly rolls out of the way and lands a hit with her pillow."

        "Of course, the odds are against her. I can stand up, for starters."

        scene black
        with vpunch

        "Oof!"

        show evh emi_grinding_victorytall:
            xalign 0.5 yalign 1.0
            easein 12.0 yalign 0.0
        with Dissolve(1.0)

        pause 6.0

        "Guess I can't, after all. Emi seems to have effectively tripped me up, and is now sitting primly astride me as I lay on my back. I'm not even sure how she managed it."

        emi "I win!"

        "Her eyes twinkle mischievously. I've been thoroughly defeated, and by a girl that's a fraction of my size, at that."

        "Then again, being defeated doesn't seem quite so bad. Emi being positioned over my waist isn't something that I, or my body, can ignore easily."

        scene bg school_dormemi
        with locationchange

        "I open my lips to speak, but Emi's head darts downwards before I can get so much as a word out. I give no resistance as she presses her mouth to mine, not that I'd want to."

        "This is… different, somehow."

        "She pulls back, nips at my lower lip, and reinitiates the embrace. Her tongue darts inside my mouth, exploring. I can feel a warmth spreading through my body as my heart begins to beat faster."

        "My mind starts to go foggy, and I become vaguely aware of my hand traveling up Emi's blouse. Emi gasps as I reach a breast, then there's a giggle, and then—"

        scene evh emi_grinding_victory
        with locationchange

        "I stare up at a grinning Emi."

        emi "Told you. That makes my second win, now."

        hi "What? That doesn't count; you used feminine wiles."

        show evh emi_grinding_wink
        with charachangeev

        emi "'All's fair in love and war,' right?"

        emi "Ha, and you're even blushing! I didn't know you were a blusher, Hisao."

        hi "You were blushing too, you know. Probably because of your prudish ways."

        "Even I've got to admit this is a stupid thing to say to a woman who is currently straddling me and has been, up until a few seconds ago, playing tonsil hockey with me."

        show evh emi_grinding_grin
        with charachangeev

        emi "A prude, am I?"

        emi "Well then, let's see who blushes first, shall we?"

        "I'm not sure whether the tone of her voice terrifies or arouses me, but that question is quickly made rather moot."

        show evh emi_grinding_half_undress
        with charachangeev

        show evh emi_grinding_half_grin
        with charachangeev

        "In a motion of practiced ease, she peels her blouse off and tosses it carelessly aside. Her bra and skirt quickly follow it onto the floor."

        emi "Ha!"

        "I fight the urge to blush. It's a rather hard task."

        hi "Escalation, is it?"

        show evh emi_grinding_off_yawn
        with charachangeev

        "My own shirt follows suit, albeit with some difficulty thanks to my position. Emi mock-yawns."

        emi "You'll have to try harder than th—"

        show evh emi_grinding_off_closesurprise
        with charachangeev
        stop music fadeout 3.0

        emi "Ah…!"

        "My hands gently caress Emi's bare skin, causing her to shiver. It would seem that my hands are acting on their own, again. If our position had let me, I'd probably have finished her undressing for her."

        "I start to say something about how Emi's starting to blush, but both of us are very rapidly reaching the edge of something very barely holding us back. Conversation grinds to a halt, and I feel my arms losing energy."

        play music music_one fadein 0.5

        "Neither of us, however, is prepared for this sudden new sensation."

        show evh emi_grinding_off_closearoused
        with charachangeev

        "An indescribable heat surges through me, coming from both myself and, it seems, Emi as well."

        "With one hand on my chest to steady herself, and another holding mine to make sure that I can't have my way with her body again, she looks quite pleased with herself."

        show evh emi_grinding_off_aroused
        with charachangeev

        "And then, after a moment's hesitation, she moves."

        "And she moves again."

        "And again."

        "As she moves, Emi's breath hitches. My breathing is starting to come faster, and more raggedly as well."

        "Emi's body shivers and shudders against mine, and I can feel her starting to lose her balance. It must be harder for her to keep steady because she's missing her legs."

        show evh emi_grinding_off_closesurprise
        with charachangeev

        "I steady her as best as I can, cupping my hands around her backside. It's firm and taut."

        "Makes sense, considering how much she runs. The potential power in those muscles makes them flex as she responds to my touch."

        "What I fail to take into account is the fact that my attempt to steady Emi kind of slides her forward and, well… It feels amazing."

        show evh emi_grinding_off_arousedclosed
        with charachangeev

        "Her panties slide easily against my trousers, and it doesn't take us long to figure out a rhythm."

        "But Emi refuses to keep to it, going now fast, now slow, now pausing for what feels like an eternity. I'm not sure whether she's doing this to toy with me, or if it's to make her feel better, but I'm well past caring."

        "The heat between us is growing more intense, and I can't hold back a gasp. The noise only seems to drive Emi along."

        "I begin to punctuate her movements with some of my own, which causes her modest breasts to bounce in time with my movements. Her breath begins to come faster as we continue, my own breathing becoming equally quick."

        "With her eyes closed, her lips purse expectantly. I just manage to lift myself up for a few moments. Our mouths seeking one another, her chest sliding against mine as our sweat mingles."

        "As I flop back down, my trousers are soaked with sweat. I would take them off if it didn't mean stopping what we're doing."

        "And I don't want to stop what we're doing, stop this growing pressure, this tickling in the back of my brain."

        "Emi is sliding faster and faster, panting heavily, her voice seemingly unable to convey what she's feeling. Her body, on the other hand, is doing a fine job."

        show evh emi_grinding_off_come
        with charachangeev

        "Suddenly she moves a little more erratically as my own breath hitches in my throat, ending in a final desperate thrust that sends me over the edge into a surging feeling I didn't know existed."

        scene white
        with Dissolve(3.0)

        "My mind blanks, fills with white noise, and I succumb to the feeling of climax. For a few seconds, everything else in the world falls away except for this amazing feeling of Emi and I, together."

        show evh emi_grinding_off_end
        with Dissolve(1.0)

        "And then… it passes. The white noise clears, and I am left staring up into the eyes of the girl atop me."

        "For a few minutes, neither of us speaks. The sound of our breathing fills the room, our chests heaving from the experience."

        "She eventually, reluctantly, shifts off of me and sits against the wall. I join her."

        scene bg school_dormemi at right
        with locationchange

        show eminude smile_close
        with persistent.charachange

        emi "So… did I blush?"

        hi "I didn't notice."

        hi "Did I?"

        show eminude neutral_close
        with persistent.charachange

        "Emi shrugs, still breathing a little heavily."

        show eminude weaksmile_close
        with persistent.charachange

        emi "Didn't notice either."

        hi "Well, maybe we should—"

        play sound sfx_dooropen

        stop music fadeout 0.3

        show rin basic_deadpan behind eminude:
            offscreenright alpha 0.0
            easein 0.5 right alpha 1.0
        show eminude blush_close
        with vpunch

        show rin:
            right alpha 1.0

        rin "I need to use your window."

        "My first instinct is to hide, but then I realize that I'm still utterly exhausted and sitting next to a topless Emi, so there's no running anyway."

        show rin basic_awayabsent
        with charachangealways

        show rin basic_absent
        with charachangealways

        show rin basic_awayabsent
        with charachangealways

        "Rin's eyes pass over Emi, and me, and focus on the window."

        show rin basic_deadpannormal
        with persistent.charachange

        rin "There was a cloud."

        play music music_comedy fadein 0.5

        show eminude neutral_close
        with persistent.charachange

        emi "A cloud?"

        show rin basic_lucid
        with persistent.charachange

        "Rin nods."

        show rin relaxed_nonchalant
        with persistent.charachange

        rin "I was watching it from my window, but it didn't stay in my window."

        show rin negative_spaciness
        with persistent.charachange

        rin "So I need to use your window."

        show eminude closedsmile_close
        with persistent.charachange

        "Emi shifts a little, causing me to cough in order to cover up a giggle of my own."

        emi "How long do you need the window for?"

        emi "We're uh."

        show eminude wink_close
        with persistent.charachange

        emi "Busy."

        "This time I can't contain my laughter."

        show rin negative_annoyed
        with persistent.charachange

        "Rin ignores both Emi and me and peers out the window."

        show rin basic_deadpanupset
        with persistent.charachange

        "Her shoulders slump, and she looks disappointed."

        rin "Hmm."

        rin "It changed into something else."

        rin "Disappointing."

        show eminude grin_close
        with persistent.charachange

        "Emi is having trouble keeping a straight face."

        emi "Sorry to hear that, Rin."

        show eminude pout_close
        with persistent.charachange

        emi "Could we have a little privacy now, please?"

        show rin relaxed_nonchalant
        with persistent.charachange

        pause 0.2

        show rin relaxed_nonchalant:
            easeout 1.0 offscreenright

        pause 1.0

        play sound sfx_doorclose

        hide rin

        "Rin shrugs, as if to say 'Can you?' and hooks her foot around the door, pulling it closed behind her."

        show eminude happy_close
        with persistent.charachange

        "We both dissolve into raucous laughter, unable to deal with Rin's bizarrely timed visit any other way."

        "After our laughter dies down, I look to Emi. We're both a total mess."

        stop music fadeout 5.0

        hi "Well."

        show eminude neutral_close
        with persistent.charachange

        "Emi raises an eyebrow."

        emi "Well?"

        hi "Again?"

        show eminude wink_close
        with persistent.charachange

        "Emi grins and laughs, and then she nods."

        show eminude grin_close
        with persistent.charachange

        emi "We should probably ditch the clothes, this time."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .storage_space:
        play sound sfx_alarmclock

        pause 2.0

        scene bg school_dormhisao
        with openeye

        "The sunlight breaks through my window shortly before my alarm ruins the morning silence."

        play music music_dreamy fadein 6.0

        "I feel sore."

        "The events of the previous evening suddenly intrude upon my consciousness, and I find myself blushing."

        "That was an eventful evening - and it explains perfectly the soreness in my lower back."

        "The walk back, as I recall, had been rather tense."

        "My trousers having been… soiled, I had washed them off in the bathroom before going back to my room."

        "But there was still a fairly obvious-looking stain on the front."

        "Fortunately for me, the only person I ran into on my way back was Kenji."

        "And he didn't notice a thing."

        "Well, apart from my being in the general vicinity."

        "Of course he'd asked how the night went, and whether or not I'd learned anything of importance."

        "I don't even know if I opened my mouth to answer; I was too tired to care."

        "And this morning, I'll admit that I'm feeling pretty worn out."

        "Still, Emi had promised to meet me at the track, and I'd hate to disappoint."

        scene bg school_track
        show emiwheel weaksmile at center
        with locationskip

        "She is indeed waiting for me when I arrive."

        "Doing her best to look cheery, despite the fact that she's sitting in a wheelchair."

        "I wave to her and begin stretching."

        hi "You're early."

        show emiwheel frown
        with persistent.charachange

        "Emi frowns and shakes her head."

        show emiwheel angry
        with persistent.charachange

        emi "Ridiculous."

        emi "{b}You're{/b} late."

        show emiwheel grin
        with persistent.charachange

        emi "Overslept, Hisao?"

        show emiwheel wink
        with persistent.charachange

        emi "All tuckered out?"

        "Well, at least she seems more like her old self."

        "And as expected, she doesn't seem that shy about mentioning our… previous activities."

        hi "Hey, you're lucky I could show up at all."

        hi "All that cardiovascular activity last night, I nearly thought I'd have to see the nurse afterwards."

        show emiwheel wink
        with persistent.charachange

        "Emi laughs out loud, then her face suddenly becomes concerned."

        show emiwheel blush
        with persistent.charachange

        stop music fadeout 8.0

        emi "Hey, that's not uh…"

        emi "I mean, you're not…"

        hi "Go on, spit it out."

        show emiwheel awayfrown
        with persistent.charachange

        emi "It's just that it would be hard to explain if you had an episode while we were…"

        hi "Oh."

        hi "{b}Oh.{/b}"

        "Now that she mentions it, it really is a legitimate concern."

        "I certainly hadn't thought of it last night, of course - other, more pressing concerns had been at hand."

        hi "Well, I don't think anything we, er, {b}do{/b} is going to be any more of a strain than these morning runs, and I handle those fine, so…"

        show emiwheel frown
        with persistent.charachange

        "Emi considers this point."

        show emiwheel evil
        with persistent.charachange

        "A devious light appears in her eyes."

        play music music_emi fadein 2.0

        emi "Say…"

        hi "Hmm?"

        show emiwheel grin
        with persistent.charachange

        "The light vanishes, and Emi grins ruefully at me."

        "I can't help but feel vaguely suspicious."

        show emiwheel happy
        with persistent.charachange

        emi "I seem to have forgotten a pair of gloves."

        hi "What do you need gloves for?"

        show emiwheel smile
        with persistent.charachange

        "Emi indicates the chair upon which she is seated."

        emi "For this, of course!"

        show emiwheel wink
        with persistent.charachange

        emi "Sure, regular moving around is all well and good without 'em, but I want to be able to get a good workout."

        show emiwheel grin
        with persistent.charachange

        emi "And to get that kind of speed, you gotta have gloves if you don't want blisters."

        hi "So what, are you wussing out on me then? Do I have to go it alone?"

        show emiwheel awayfrown
        with persistent.charachange

        "Emi thinks for a minute - or pretends to think."

        show emiwheel closedsmile
        with persistent.charachange

        emi "Hmm… if I remember right, there's a spare pair or two in the track shed."

        "So she does seriously want to do it, then."

        "But in her normal school uniform? I'd have expected her to wear her gym outfit for something like this."

        hi "Wait, what are they doing there?"

        show emiwheel frown
        with persistent.charachange

        "Emi looks askance at me."

        emi "Seriously? You can't think of why a shed full of track supplies at a school for the disabled would have racing gloves?"

        "Well, when she puts it that way, I suppose that makes perfect sense."

        hi "Hey, I'm still getting used to this place. Give me a break, huh?"

        show emiwheel grin
        with persistent.charachange

        emi "I guess I can let it slide this time."

        show emiwheel wink
        with persistent.charachange

        emi "Now come on, I'll need your help."

        "I can't imagine what for, but then again I didn't have a clue why racing gloves would be in the shed, so I'm not willing to press the issue."

        scene bg school_sportsstoreext
        with locationchange

        "Emi navigates her way to the shed easily enough, though I can hear her grumbling under her breath."

        "It's actually kinda cute."

        "I hurry a little to reach the door first. Opening it will be easier for me than for her."

        play sound sfx_door_creak

        show emiwheel neutral:
            center
            xpos 0.4
            easein 0.5 center
        with charaenter

        show emiwheel at center

        "The door opens, and Emi starts to wheel inside, only to come to a sudden halt at the doorway."

        "It seems the doorsill is slightly too high for her to get over by herself."

        show emiwheel awayfrown
        with persistent.charachange

        show emiwheel:
            ease 0.4 xpos 0.45
            easeout 0.2 xpos 0.5
            ease 0.4 xpos 0.45
            easeout 0.2 xpos 0.5
            ease 0.4 xpos 0.45
            easeout 0.2 xpos 0.5
            ease 0.4 xpos 0.45
            easeout 0.2 xpos 0.5

        pause 1.0

        "She makes a few runs at it, unsuccessfully, before crossing her eyes and glaring at the offending object."

        show emiwheel angry at center
        with charaenter

        emi "Stupid wheelchair."

        show emiwheel frown
        with persistent.charachange

        emi "Hisao, can you give me a hand here?"

        hi "Sure, no problem."

        scene bg school_sportsstoreroom
        with locationchange

        "It's a simple enough matter for me to bump Emi over the doorway, jostling her slightly."

        show emiwheel blush_close_ni at center
        with charaenter

        emi "Hey, easy there!"

        hi "Whoops! Sorry."

        "It's at about this time that I fail to notice where I'm going and run Emi's chair into a mat."

        play sound sfx_impact

        show expression Composite((765, 2160), (0, 0), night("sprites/emiwheel/close/emiwheel_blush_close.png")) as emiwheel:
            xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
            easeout 0.5 ypos 1.4 rotate 70
        with vpunch

        hide emiwheel

        "She gives a startled yelp and topples forward out of her chair."

        "There's a moment of silence as I gaze in horror upon what I've done, and Emi glares at me."

        emi "Hisao…"

        hi "Yes?"

        emi "Promise me you'll never work at a hospital."

        hi "Sorry! I didn't mean to!"

        "Emi giggles, and holds up a hand."

        emi "Would you kindly help me back into my chair, Hisao?"

        show emi basic_closedgrin_close_ni:
            center
            ypos 1.2
            easein 0.5 center
        with charaenter

        show emi at center

        "As I bend down to pick up Emi, she grins in triumph and pulls me into a kiss that quickly has us both entirely unconcerned about getting her back into the chair."

        play sound sfx_door_creak

        "In fact, as I move to a more comfortable position, I confess that the chair is pushed out the door, which, startled by the passage, swings shut."

        play sound sfx_rustling

        hide emi
        show eminude smile_close_ni at center
        with persistent.charachange

        "Well, at least we've got privacy now, which is a good thing as my hands work quickly to remove Emi's blouse and skirt."

        "I'm startled to discover that she's forgotten to put her bra on today. Did she plan this?"

        show eminude blush_close_ni
        with persistent.charachange

        "Her arms hook under mine and rest on my shoulders as I kiss my way down Emi's neck, pausing to give special attention to a spot right where the neck meets the shoulder that I'd found last night."

        emi "Y-you've gotten pretty good at th-hee!"

        hi "I do try."

        show eminude frown_close_ni
        with persistent.charachange

        "Emi pushes on my chest, insistently, and I draw back with a puzzled expression."

        emi "I've got a confession, Hisao."

        hi "Oh?"

        "Having pulled back, I decide instead to focus my attention on her breasts."

        show eminude blush_close_ni
        with vpunch

        "As she attempts to speak, her words are interspersed with giggles that I find incredibly cute."

        show eminude wink_close_ni
        with persistent.charachange

        emi "I don't ac-hee hee hee-actually w-woah! Wear gloves."

        "My own reply is rather mumbled onto her chest instead of being addressed to her face."

        hi "Should've known…"

        "Words quickly become irrelevant."

        show eminude closedsmile_close_ni
        with vpunch

        "Emi's movements are almost frantic, as if she's been holding something back since we met this morning, and now she has an outlet."

        "I'm very nearly caught off guard by her aggressiveness, feeling her nearly rip my shirt off, the way she seems to vie to be in the dominant position."

        "For my part, I confess that I'm caught up in her attitude as well, fighting back, rolling and wrestling even as I caress her breasts, even as her fingers dig into my shoulders, and I lose track of where we are."

        show eminude blush_ni
        with vpunch

        "So much so that I roll right off the mat and land on something small and rather hard."

        hi "Ow!"

        show eminude weaksmile_ni
        with persistent.charachange

        "Emi, still flushed and breathing a little heavily, peers at me and bursts into laughter."

        emi "I'm sorry, I'm sorry. Are you all right?"

        hi "Yeah, I think so. Not sure what I landed on, though…"

        "I reach under my back and pull the offending object out, inspecting it closely."

        stop music fadeout 0.2

        "'Personal lubricant. Lemon-flavored.'"

        "Wait, what?"

        play music music_running

        show eminude happy_ni
        with persistent.charachange

        "Emi's eyes shoot upwards and she begins, if possible, to laugh even harder."

        hi "Somehow, I don't think this is… this isn't track-related."

        show eminude closedsmile_ni
        with persistent.charachange

        emi "Oh man, I know whose that is!"

        hi "What?"

        show eminude wink_ni
        with persistent.charachange

        emi "It's the track captain's!"

        "Ah, my old nemesis. Or, kind of."

        hi "How d'you know it's his?"

        show eminude awayfrown_ni
        with persistent.charachange

        "It appears that I've asked a stupid question, or at least Emi thinks so."

        show eminude frown_ni
        with persistent.charachange

        emi "Because he's the one who told me the track shed was a good place for… what did he call them?"

        show eminude pout_ni
        with persistent.charachange

        emi "'Clandestine encounters.'"

        hi "Oh? He invite you to one or something?"

        show eminude happy_ni
        with persistent.charachange

        "Emi bursts into more laughter."

        "I confess the sight of a naked Emi laughing is oddly beautiful."

        "I feel an eagerness to end conversation and get back to what we were doing, despite my rather pointed questioning."

        show eminude closedsmile_ni
        with persistent.charachange

        emi "Hisao, the track captain's gay."

        "Huh."

        hi "Really? And here I initially thought you two were a couple."

        show eminude awayfrown_ni
        with persistent.charachange

        emi "Well… I did have a crush on him when I first joined up, but he wasn't interested."

        show eminude frown_ni
        with persistent.charachange

        emi "Obviously."

        show eminude neutral_ni
        with persistent.charachange

        emi "But we are good friends, I guess."

        show eminude grin_ni
        with persistent.charachange

        emi "I mean he told me about all this, you know."

        hi "I hesitate to ask,"

        "And really, I do. But I ask anyway."

        hi "But what does he need the uh… lube for, anyway?"

        hi "I mean, he doesn't… er…"

        "How the hell does Emi always manage to not blush?"

        show eminude wink_ni
        with persistent.charachange

        emi "Obviously he uses it for, you know."

        show eminude evil_ni
        with persistent.charachange

        emi "Anal."

        "I try to suppress a snicker."

        "I fail."

        show eminude happy_ni
        with persistent.charachange

        "Emi's giggling too."

        hi "And he {b}tells{/b} you about all this?"

        show eminude awayfrown_ni
        with persistent.charachange

        "Emi shrugs."

        show eminude neutral_ni
        with persistent.charachange

        emi "Yeah, of course."

        stop music fadeout 10.0

        show eminude closedsmile_ni
        with persistent.charachange

        emi "He's kinda wild about the whole thing."

        emi "Says it's a feeling that can't be beat."

        hi "Uh… huh."

        "The air in the track shed seems charged with some kind of horrible curiosity."

        hi "That's interesting."

        hi "I suppose I'll have to take his word for it."

        show eminude neutral_ni
        with persistent.charachange

        emi "Well…"

        "Birds outside stop chirping."

        "The wind dies down."

        "Somewhere, a man is drinking a cup of coffee. He freezes with the cup at his lips."

        show eminude neutral_ni
        with persistent.charachange

        emi "We could…"

        extend " maybe…"

        show eminude blush_ni
        with persistent.charachange

        emi "Try it."

        play music music_one fadein 5.0

        "My jaw suddenly and spontaneously unhinges and hits the floor."

        hi "W-what?"

        "Emi is finally blushing, rubbing the back of her head ruefully."

        show eminude pout_ni
        with persistent.charachange

        emi "Well, it's just that we really can't… do what we did last night, you know?"

        emi "It would be a little… it wouldn't be safe, you know?"

        show eminude weaksmile_ni
        with persistent.charachange

        emi "I mean it wasn't exactly a great idea last night."

        show eminude closedsmile_ni
        with persistent.charachange

        emi "So you know, we could try this to see if it uh…"

        hi "Is as good?"

        show eminude weaksmile_ni
        with persistent.charachange

        emi "Well uh, yeah. Basically."

        hi "Huh."

        scene evh emi_shed_base1
        show emi emi_shed_grin
        show hisao emi_shed_neutral
        show evh_l emi_shed_up
        show evh_r emi_shed_down
        with shorttimeskip

        emi "Careful!"

        hi "Are you sure about this?"

        "I'm positioned behind Emi, who is looking back over her shoulder, looking a little flushed."

        "Well obviously once we decided to go ahead with this idea, we had to get back into the mood."

        "That accomplished, we emptied the bottle of lube and…"

        "Here we are."

        show emi emi_shed_hesitant
        with persistent.charachange

        emi "Yes, I'm sure! Come on, before I calm down and think too much about this."

        "Emi's breathing is still coming a little heavily, and her response is almost impatient."

        "Which is to be expected, I suppose. We were both so close, and this is kind of delaying things."

        "I think we've both gone temporarily insane."

        "At least that's going to be my claim from here on out."

        "I try hard not to think about the specifics of what I'm about to get myself into."

        "There's no way this is going to be very clean."

        show evh emi_shed_base2
        show hisao emi_shed_closed
        with charachangeev

        "Taking a breath that is as much for me as it is for her, I enter slowly."

        "There's a lot of resistance, and it's like both our bodies are reluctant to actually go through with it."

        show emi emi_shed_shock
        with hpunch

        "Emi's whole body tenses, and as I'm only partially in by this point, it feels surprisingly good, if a bit odd."

        "Emi, on the other hand, looks uncomfortable."

        "The expression is almost comical."

        show hisao emi_shed_neutral
        with charachangeev

        hi "Should I stop?"

        "Emi's breath hitches in her throat, and it seems to take a few seconds longer than it should to formulate a reply."

        show emi emi_shed_closed
        with charachangeev

        emi "N-no, keep going. It just feels weird."

        "She giggles."

        "I can't blame her. I'm surprised that I even managed to form a sentence."

        show hisao emi_shed_closed
        with charachangeev

        "It's… hot."

        "Feels exceedingly odd."

        "The lube glistens unnaturally."

        "It makes me uncomfortable."

        "I continue to work my way inside her, working slowly and listening carefully to Emi's breathing."

        show evh emi_shed_base3
        show emi emi_shed_hesitant
        with charachangeev

        "I reach my limit and pause. Emi looks back again, biting her lower lip."

        emi "Are you going to try moving, or are we just going to sit here feeling silly?"

        show hisao emi_shed_neutral
        with charachangeev

        hi "No, I just wanted to give you a chance to adjust."

        "This doesn't make any sense."

        "How did we even decide to do this?"

        show emi emi_shed_grin
        with charachangeev

        emi "I don't think there's really any adjusting to this, Hisao."

        show emi emi_shed_hesitant
        with charachangeev

        emi "Try moving. Maybe it'll feel better?"

        "She sounds doubtful, but certainly unwilling to admit defeat now that we've come so far."

        show emi emi_shed_closed
        with charachangeev

        "I begin a slow motion that seems to work well for both myself and Emi, as she closes her eyes in an attempt to concentrate on this new feeling."

        "As I begin to find a rhythm, I begin to feel that familiar falling-away sensation I got yesterday."

        show hisao emi_shed_closed
        with charachangeev

        "I close my eyes and try to lose myself in the feeling, except…"

        "It doesn't seem right."

        "Emi's not making any noise."

        "I learned very quickly yesterday that Emi is somewhat less than quiet when she's enjoying herself."

        show hisao emi_shed_neutral
        with charachangeev

        "As I open my eyes, I see that Emi's trying to get into things, but it just doesn't seem to be working for her."

        "Her eyes are closed, and she's biting her lip, but it seems to be out of toleration rather than enjoyment."

        "A sort of 'well, this was a failure, but hopefully it'll be over soon' look."

        "I'm caught in a bit of a situation here."

        "In truth, I don't want to stop."

        "But at the same time, it doesn't seem to be doing much for Emi - or if it is, it's coming on far slower than I am."

        "I feel bad. I want Emi to enjoy this, too."

        show evh_r emi_shed_up
        show emi emi_shed_shock
        with charachangeev

        "I reach one arm around to tease at Emi's chest, which startles her."

        show hisao emi_shed_sweat
        with charachangeev

        "This in turn causes her to tighten around me considerably, causing a wave of pleasure to blindside me."

        show evh emi_shed_base4
        show hisao emi_shed_neutral
        show emi emi_shed_closed
        show evh_l emi_shed_down
        with charachangeev

        "My gasp seems to amuse Emi, but her grin quickly turns to a gasp as I move my other hand casually down her front and begin to stroke gently at the soft patch of hair between her legs."

        "The motion of my own hips increases as my hand's ministrations to Emi's front bring back the gasps and yelps that I'm used to."

        show hisao emi_shed_sweat
        with charachangeev

        "I concentrate only on the feelings of my hands, one now slick and sliding, the other on skin soft and responsive, goosebumps on her flesh, shivers and sweats, as her own building climax causes her to tighten, until finally I can't possibly—"

        "NoIcan'tpossibly"

        show hisao emi_shed_closed
        with charachangeev

        "OhgodI'msorryEmiI'mgoingto"

        "I give a final thrust, my fingers tense around Emi's nipples, dive between her legs."

        play sound sfx_flash
        with Fade(0.1, 0.0, 0.1, color="#FFF")
        play sound sfx_flash
        with Fade(0.1, 0.0, 0.4, color="#FFF")
        with GenericWhiteout(0.5, 1.0, 4.0)

        "Emi's back spasms and she arches up, a high, girlish cry that echoes off the walls, and I feel the wave of my own climax annihilate all other sensations in my body."

        show evh_l emi_shed_up
        show evh_r emi_shed_down
        with charachangeev

        "Emi's arms give out and she falls forward, rather violently disengaging us and pulling something dear to me in the process."

        play sound sfx_impact

        scene bg school_sportsstoreroom
        with vpunch

        "The sudden switch from pleasure to pain causes me to lose my balance, and I fall forward on top of Emi."

        stop music fadeout 2.0

        emi "Ow!"

        hi "Ow."

        "I quickly roll off Emi and prop myself up, breathing heavily and trying to ignore the pain in my crotch."

        "Emi yelps a little as she rolls over. She grabs a couple of the tissues we'd kept handy earlier, and cleans up before getting her panties back on and awkwardly leaning against a wall."

        "Still breathing heavily, I decide to sit against the wall next to her. The feeling of the cool concrete against my sweating back is a welcome sensation."

        show eminude sad_close_ni at center
        with charaenter

        emi "That {b}hurt{/b} at the end!"

        hi "Yeah, I uh…"

        hi "This was probably not a great idea."

        "Emi squirms in order to try and sit down beside me without too much pain. Judging by her wincing, it doesn't really work."

        show eminude pout_close_ni
        with persistent.charachange

        emi "Yeah, I'm going to have words with the captain."

        show eminude angry_close_ni
        with persistent.charachange

        emi "He was clearly lying."

        play music music_ease

        "The utter and absolute ridiculousness of the situation suddenly hits, and I begin laughing."

        show eminude happy_close_ni
        with persistent.charachange

        "Emi shakes her head and begins laughing with me."

        show eminude grin_close_ni
        with persistent.charachange

        emi "Hey, Hisao."

        hi "Yeah?"

        show eminude pout_close_ni
        with persistent.charachange

        emi "We're never doing this again, right?"

        hi "Yeah, I think my curiosity is satisfied on this one."

        "Emi nods, satisfied."

        show eminude closedsmile_close_ni
        with persistent.charachange

        emi "Good."

        show eminude smile_close_ni
        with persistent.charachange

        emi "I think we should maybe stick to the basics, don't you?"

        show eminude blush_close_ni
        with persistent.charachange

        emi "I mean most of this is new to me anyway."

        hi "What d'you mean, 'most?'"

        show eminude grin_close_ni
        with persistent.charachange

        "Emi grins impishly."

        show eminude closedsmile_close_ni
        with persistent.charachange

        emi "I'll never tell."

        "An unpleasant thought strikes me."

        "Even more unpleasant is the thought of having to ask Emi about it."

        "Still, after what we've just done, it should be a cakewalk."

        hi "Hey, is there a sink?"

        hi "I'd kinda like to, er."

        hi "Wash off a little."

        show eminude blush_close_ni
        with persistent.charachange

        "Emi's jaw drops."

        emi "In the {b}sink{/b}?"

        hi "Well, there's not really anywhere else to do it, is there?"

        hi "And it uh… I want to avoid a smell."

        hi "That the nurse might notice."

        "This is the most awkward conversation I have ever had."

        show eminude closedsmile_close_ni
        with persistent.charachange

        emi "You're right."

        show eminude grin_close_ni
        with persistent.charachange

        emi "Yeah, there's uh… It's on the back wall."

        show eminude smile_close_ni
        with persistent.charachange

        emi "There might be some soap, too."

        hi "Thanks."

        hide eminude
        with charaexit

        "There is in fact a little hand soap, which is better than nothing."

        "No towel, though. Guess I'll just have to drip dry."

        show eminude grin_ni at center
        with charaenter

        emi "All finished?"

        hi "Yeah, that'll do for now. It's not like I'm not going to take a shower after we see the nurse."

        show eminude weaksmile_ni
        with persistent.charachange

        emi "Glad to hear it."

        show eminude wink_ni
        with persistent.charachange

        emi "Now help me find my clothes. You tossed 'em somewhere."

        hi "Hey, you were no better! How am I supposed to explain that hole in my shirt, hmm?"

        show eminude closedsmile_ni
        with persistent.charachange

        emi "Heh, sorry. I got a little excited earlier."

        scene bg school_sportsstoreroom
        with shorttimeskip

        "It takes some time, but finally we're both more or less clothed."

        "There's a frantic moment where neither of us knows where Emi's wheelchair is, but I recall it going through the door and rescue it."

        show emiwheel neutral_close_ni at center
        with charaenter

        emi "Now be more careful going through the door this time, would you?"

        show emiwheel awayfrown_close_ni
        with persistent.charachange

        emi "Bumps are not my friend right now."

        hi "I am so sorry we tried this."

        show emiwheel grin_close_ni
        with persistent.charachange

        "Emi shrugs and grins."

        show emiwheel wink_close_ni
        with persistent.charachange

        emi "Well, it was worth a shot, right?"

        show emiwheel closedsmile_close_ni
        with persistent.charachange

        emi "And anyway, it was good exercise, right?"

        "Can't argue that."

        scene bg school_nursehall
        with shorttimeskip

        "As we make our way up to the nurse's office, I notice that Emi keeps shifting uncomfortably in her seat."

        show emiwheel awayfrown
        with persistent.charachange

        emi "God, this feels weird."

        show emiwheel neutral
        with persistent.charachange

        emi "Good thing I'm in a wheelchair, Hisao."

        hi "Why's that?"

        show emiwheel weaksmile
        with persistent.charachange

        emi "Because, now I don't have to explain to the nurse why I'm walking funny."

        hi "Oh."

        hi "We're never doing this again."

        scene bg school_nurseoffice
        show nurse fabulous at center
        with locationchange

        "The nurse is at least kind enough to not comment on the marks that Emi left on my shoulders."

        "Nor does he say a word about Emi's constant shifting about in her wheelchair."

        "Either he didn't notice, or he didn't want to notice."

        "All the same, I'm going to have to make sure he didn't slip cyanide into my medication for a little while."

        "Just to be safe."

        stop music fadeout 4.0
        scene bg school_dormhisao
        with locationskip

        "I shower for longer than usual, just to be sure I'm clean of our little 'experiment', and then collapse on my bed."

        "Class is in twenty minutes, so I can probably afford a nap."

        scene black
        with shuteye

        if _in_replay:
            return

    label .afterschool_plans:
        scene black
        with dissolve

        pause 5.0

        play sound sfx_doorknock

        "Knock knock."

        "Who's there?"

        play sound sfx_doorknock

        "Knock knock."

        "That's not how the joke goes at all."

        play sound sfx_doorknock

        "Knock knock."

        "I already said who's there!"

        "More importantly, what time is it?"

        "Even more importantly, what day…?"

        scene bg school_dormhisao
        with openeyefast

        "I am suddenly catapulted into wakefulness by both the fact that the knocking still hasn't stopped and the fact that it's noon."

        "On a school day."

        "Now fully awake, I can remember why I was napping."

        "Better not give that excuse to Mutou."

        "'Sorry I wasn't in class, I was experimenting sexually with my girlfriend and it tired me out.'"

        "Yeah, that'll go over well."

        play sound sfx_doorknock

        "I wonder how long this knocking is going to continue."

        "Guess I ought to answer the door."

        play sound sfx_dooropen

        scene bg school_dormhallway
        show kenji tsun at center
        with locationchange

        "I'm strangely unsurprised to see Kenji on the other side."

        "Though it appears that Kenji is surprised to see me."

        ke "What the hell are you doing here, man?"

        play music music_kenji fadein 0.5

        hi "Well, I was sleeping."

        show kenji neutral
        with persistent.charachange

        "Kenji nods in understanding."

        show kenji happy
        with persistent.charachange

        ke "Knocked out. I see."

        show kenji tsun
        with persistent.charachange

        ke "I told you to be careful around that Ibarazaki chick, man."

        ke "This is the sort of thing that happens when you aren't cautious."

        "He makes an attempt to look at the back of my head."

        show kenji neutral
        with persistent.charachange

        ke "Did she hit you with something?"

        ke "Or was it a drug?"

        hi "Stop trying to touch me."

        with flash

        "Kenji produces a flashlight and shines it in my eyes."

        ke "You got a concussion?"

        hi "I wasn't knocked out!"

        show kenji happy
        with persistent.charachange

        ke "Maybe you just don't remember."

        "This conversation isn't going anywhere."

        hi "No, I just had a tiring morning and fell asleep."

        show kenji tsun
        with persistent.charachange

        ke "Whatever, man."

        ke "If you want to be in denial about this, I guess I can't stop you."

        ke "But you gotta watch out for that girl, man. She's not safe."

        hi "What?"

        show kenji rage
        with persistent.charachange

        ke "She's not safe to be around; she's one of their most sinister agents!"

        ke "If you're not careful, there's no telling what could happen!"

        ke "She's brought down stronger men than you, you know!"

        hi "What the hell are you talking about?"

        hi "She's not an agent of anything, and she didn't knock me out, okay?"

        hi "I also highly doubt that she's brought down anyone at all."

        show kenji tsun
        with persistent.charachange

        "Kenji looks almost offended."

        "I have no idea why."

        ke "You don't believe me?"

        ke "That's cold, man. Real cold."

        ke "I'm just trying to look out for you. That's what friends do, you know."

        "We're friends? I had no idea."

        "Then again, I wonder if Kenji knows what being a friend even entails."

        "I feel something like pity for him, standing there before me."

        "Maybe he does think he's looking out for me."

        hi "I know, I know."

        hi "I'm sorry about that. Thanks for the warning."

        "I hold out my hand as a sign of peace."

        show kenji neutral_close
        with characlose

        "Kenji shakes it gingerly, like my hand could possibly be on fire."

        "There's an awkward silence for a few seconds before Kenji remembers that he's still shaking my hand."

        show kenji happy_close
        with persistent.charachange

        ke "Anyway, I need a favor."

        hi "What kind of favor? I'm out of money…"

        ke "No you aren't. You've got money kept in your desk drawer under a black notebook. For emergencies."

        hi "Did you ransack my room?"

        show kenji neutral_close
        with persistent.charachange

        ke "That's not important."

        ke "I don't need money, anyway."

        "He adopts a very serious tone."

        show kenji tsun_close
        with persistent.charachange

        ke "I'm about to undertake a major op."

        ke "It'll blow the whole conspiracy wide open if I'm right."

        ke "But it's dangerous, so I need you to do something for me in case I don't come back."

        hi "Uh, sure man. Anything."

        "What the hell is he planning on doing?"

        "Should I be telling someone about this?"

        show kenji neutral_close
        with persistent.charachange

        ke "If I go missing, wait three days and then mail my journal off to the newspapers."

        ke "It's hidden in my room under a false bottom in one of my desk drawers."

        hi "How do I get into your room? I don't have a key."

        show kenji tsun_close
        with persistent.charachange

        "Kenji looks at me like I'm crazy."

        ke "So pick the lock. You know how to do that, right?"

        ke "It's an important skill to learn at a young age!"

        hi "Uh, yeah, of course I know how."

        hi "I'll be sure to uh, do that for you. If you go missing."

        "I don't think I want to read Kenji's journal."

        "Either way, Kenji seems pretty happy that I've agreed to do this thing for him."

        show kenji happy_close
        with persistent.charachange

        ke "Great, man. Great."

        ke "I'll see you around, I got stuff to do."

        stop music fadeout 5.0

        show kenji happy_close:
            easeout 0.5 xpos 0.7 alpha 0.0

        pause 0.5

        hide kenji

        "And he's gone, dashing down the hallway."

        "He made it seem so final."

        "I hope I don't have to carry out his final wishes."

        scene bg school_dormhisao
        with locationchange

        play sound sfx_doorclose

        "Shaking my head, I close my door and walk back to my bed."

        "Guess I should go to class, if only to catch the last half of the day."

        "But I've come this far without going to class today…"

        "And I did want to read more of that Hawking book Mutou lent me…"

        "I'm sure he'll understand."

        with shorttimeskip

        play sound sfx_hammer

        "Knock knock."

        "This time the noise jerks my attention away from my book."

        "An experience not unlike being woken up."

        hi "Who's there?"

        emi "Me! Aren't you glad?"

        play music music_emi fadein 4.0

        "The voice is muffled through the door, but unmistakably Emi's."

        play sound sfx_dooropen

        scene bg school_dormhallway
        show emiwheel smile at center
        with locationchange

        "I hop up and open the door, smiling broadly."

        hi "Hey! Nice to see you again!"

        show emiwheel grin
        with persistent.charachange

        "Emi grins back, staring up at me from her wheelchair."

        show emiwheel closedsmile
        with persistent.charachange

        emi "Yeah, you would have seen me earlier, but the damned elevator wasn't working."

        show emiwheel pout
        with persistent.charachange

        emi "Had to wait for them to fix it."

        show emiwheel awayfrown
        with persistent.charachange

        emi "You'd think they could keep it in better order, but nooo…"

        "I chuckle a bit at her vexed expression and invite her in."

        scene bg school_dormhisao
        with locationchange

        "She wheels in easily, and with my help she hops onto my bed."

        show emi basic_closedgrin:
            center
            easein 0.5 ypos 1.1
        with charaenter

        show emi:
            center
            ypos 1.1

        emi "There. Much more comfortable than that stupid chair."

        show emi basic_grin
        with persistent.charachange

        "A sigh of contentment hangs in the air, and for a minute we both just stare at one another."

        "It's at that point that I notice the circles under Emi's eyes."

        "They're not that dark, but they definitely weren't there before."

        "Before I can ask about them, Emi fixes me with a mischievous stare."

        show emi excited_happy
        with persistent.charachange

        emi "So, I couldn't help but notice you weren't at lunch today."

        emi "In fact, I don't think I saw you at all."

        show emi excited_proud
        with persistent.charachange

        emi "What happened, hmmm?"

        hi "Fell asleep."

        hi "I actually didn't wake up until lunch, and only then because Kenji woke me up."

        show emi excited_amused
        with persistent.charachange

        emi "What had you so tired, hmm?"

        hi "Strenuous workout this morning. Slightly uncomfortable, too."

        show emi basic_closedhappy
        with persistent.charachange

        "Emi coughs, a half-laughing, half-embarrassed noise."

        show emi basic_happy
        with persistent.charachange

        emi "Remind me not to do that again."

        hi "No problem. It wasn't exactly great for me either, to be honest."

        hi "We'll just avoid that from now on."

        hi "Are you, er, still sore?"

        show emi basic_confused
        with persistent.charachange

        "Emi stares at me in disbelief."

        hi "What? It's a legitimate question!"

        show emi sad_grin
        with persistent.charachange

        emi "Of all the questions I never thought I'd be asked, that's one of them."

        hi "Well, I didn't ever expect to have to ask it, so we're even."

        show emi basic_closedhappy
        with persistent.charachange

        "Emi laughs at this."

        emi "I guess so, huh?"

        stop music fadeout 5.0

        show emi sad_shy
        with persistent.charachange

        emi "Well, since you asked, yes. I'm still a little sore."

        show emi sad_pout
        with persistent.charachange

        emi "We're never doing that again."

        hi "No arguments from here."

        "A yawn escapes her, and I raise an eyebrow."

        hi "Tired?"

        show emi sad_grin
        with persistent.charachange

        "Emi nods sleepily."

        play music music_serene fadein 8.0

        show emi sad_depressed
        with persistent.charachange

        emi "Haven't slept well."

        "Not sleeping well?"

        "I can tell that she didn't mean to tell me this either, because she gives a little start like she's just been caught lying and hastens to add,"

        show emi basic_closedgrin
        with persistent.charachange

        emi "It's not a big deal, though."

        hi "What's the trouble?"

        show emi basic_grin
        with persistent.charachange

        "Emi shrugs and refuses to elaborate."

        hi "Stressed over exams?"

        "Another shrug, but after a pause, Emi nods hesitantly."

        show emi sad_shy
        with persistent.charachange

        emi "Er, yeah, I guess."

        emi "Actually, that's why I stopped by."

        "She begins to look more and more miserable."

        "Not so you'd notice, of course; but her eyes are on her lap, she's fidgeting and her voice is quiet."

        show emi sad_pout
        with persistent.charachange

        emi "We uh, we need to stop hanging out so much."

        hi "Huh? Why?"

        "Emi takes a deep breath, like she's been practicing this."

        show emi sad_shy
        with persistent.charachange

        emi "Because you're too much fun to be around."

        emi "And I can't concentrate when you're near me."

        emi "With exams coming up soon, I just… can't have that distraction."

        show emi sad_depressed
        with persistent.charachange

        emi "Otherwise my grades will be pretty lousy, I'm afraid."

        hi "I could help you study…"

        show emi sad_grin
        with persistent.charachange

        "She smiles at me, clearly unhappy with the situation."

        emi "I'd love it if you could, but we wouldn't actually study, would we?"

        show emi sad_shy
        with persistent.charachange

        emi "I mean even now, I'm trying to have a conversation with you but I kinda just want to, uh…"

        show emi sad_shyblush
        with persistent.charachange

        emi "Not converse."

        hi "Ah."

        hi "Overwhelmed by my rugged manliness. I understand."

        show emi basic_grin
        with persistent.charachange

        "That earns me a grin, at least."

        "Emi shakes her head."

        show emi basic_closedgrin
        with persistent.charachange

        emi "Idiot. You're full of yourself."

        hi "Well, I am pretty irresistible."

        show emi sad_shyblush
        with persistent.charachange

        emi "Er, more or less. I guess."

        show emi sad_grin
        with persistent.charachange

        emi "So that's the situation, Hisao."

        emi "I have too much fun around you, and if I'm going to go into exams prepared, I need to be alone."

        hi "Hey, that's okay."

        "It really seems to have been bothering her."

        "Besides, it's only a couple of weeks. And we'll still see each other in the mornings, and at lunch."

        hi "We can just hang out at school, no problem."

        hi "And after exams, we'll go on a date to celebrate their being over, okay?"

        show emi basic_closedgrin
        with persistent.charachange

        "Emi grins, pleased by this proposal."

        show emi basic_happy
        with persistent.charachange

        emi "Yeah, sure! That sounds great!"

        show emi excited_amused_close at center
        with characlose

        "As if to signal the end of the conversation, she leans in and kisses me."

        "The rest of the night is not spent worrying about exams."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .detached:
        $ renpy.music.set_volume(0.5, 0.0, channel="music")
        play music music_night fadein 4.0

        scene bg school_library_bw
        with locationchange

        nvl clear
        nvl show dissolve

        n "{vspace=60}It's weird how easily Emi and I can keep from seeing one another after class now."

        n "Actually, I'd venture to say that it's vaguely disturbing."

        n "As easily as we'd come together, we seem to have split apart without much trouble."

        n "Well, I guess that's not exactly true."

        n "We'd both been pretty bummed after that last night together."

        n "And we get to see each other every morning for our runs (and just our runs, I might add)."

        n "Lunch, too. I especially enjoy lunchtime with her."

        n "We have plenty of time to talk about everything outside of school, whereas the morning runs have become increasingly businesslike."

        n "I think it's because Emi wants to make up for our foolery in the storage shed."

        n "But no matter how much we joke at lunch, I can't help feeling a little worried about her."

        nvl clear

        n "{vspace=60}She seems distracted more often, and I've caught her fidgeting nervously more than once."

        n "Never figured her to be someone who cared that deeply about exams, but they certainly seem to be taking their toll."

        n "Even though they haven't even started."

        n "This is just the run up, the deep breath before the plunge."

        n "Tomorrow, the real trials begin."

        n "Or the real exams, anyway."

        n "As for me, I actually don't feel that worried about exams at all."

        n "I'm not sure why. I mean, they're pretty important; my scores here will determine my odds of getting into a good university."

        n "Hell, if I'm too cavalier now, it could spell doom for my academic career."

        n "But going into them, I feel confident that I'll come out the other side okay."

        nvl clear

        n "{vspace=180}Mutou thinks I've got the science examination locked up, at any rate."

        n "Or as he says, 'The last thing that should give you trouble is my exam, Hisao. It's way beneath your talents.'"

        n "Then again, it is Mutou who's telling me this."

        n "His praise of me carries the veiled implication that anything less than perfect from me would be a disappointment, which has actually caused me to fret more than I should about the exam."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl clear
        nvl hide dissolve

        scene bg school_library
        with locationchange

        "It's for that reason that I find myself in the library after class, poring over the textbook."

        "Pretty simple things to look over; some formulas of velocity, a few bits about friction…"

        "A walk in the park compared to my dreaded English exam. Never was good with languages…"

        "As I flip through my notes one more time, my mind begins to wander."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=90}After these exams are over, things should get easier."

        n "Soon we'll be graduated."

        n "Then off to college, hopefully."

        n "I remember my abortive attempt to find out what Emi plans to do after high school."

        n "Hmm, she avoided the subject pretty deftly, as I recall."

        n "Heck, it seems that just about every time I push too hard, she dances around the subject."

        n "Or distracts me through… other means."

        n "Like a few days ago at lunch, when Rin wasn't around…"

        n "Heh."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl clear
        nvl hide None

        stop music fadeout 0.2

        show yuuko happy_up at center
        with vpunch

        yu "I've done it!"

        "I'm startled from my reverie by Yuuko's triumphant shout."

        hi "Gah!"

        show yuuko panic_up
        with persistent.charachange

        "Yuuko seems mortified at my sudden starting."

        play music music_happiness fadein 2.0

        yu "Oh my god!"

        show yuuko panic_down
        with persistent.charachange

        yu "I'm so sorry! I just got - and I really wasn't - and it's just that—"

        "As she stutters, I move to quickly calm her down before she gets too agitated."

        hi "Woah, hey."

        "My words seem ineffective."

        "Yuuko continues to work herself into a complete frenzy."

        show yuuko panic_up
        with persistent.charachange

        yu "And it's a library and I shouldn't be—"

        hi "Easy there, just calm down."

        show yuuko cry_down
        with persistent.charachange

        yu "And really I'm setting a bad example, and now I'll get fired because I can't do anything right—"

        hi "YUUKO!" with vpunch

        show yuuko worried_up
        with persistent.charachange

        "Shouting seems to work, though I draw the ire of several other students studying in the library."

        "Yuuko snaps to attention, like a soldier who's just heard the captain bark an order."

        show yuuko neurotic_up
        with persistent.charachange

        yu "Sorry! Sorry!"

        hi "Calm down, it's okay."

        hi "You just startled me a little, and that's only because I was daydreaming instead of studying."

        hi "So really, you got me back on task."

        "This is a complete lie. But it seems to work."

        show yuuko worried_down
        with persistent.charachange

        "Yuuko takes a deep breath and seems to calm down a little."

        "Though she keeps shifting around with a nervous energy that seems awfully familiar."

        hi "So, what's got you so excited anyway?"

        show yuuko neutral_up_close
        with characlose

        yu "The Yamaku Cat Burglar!"

        "To her credit, Yuuko manages to convey her intense excitement in a whisper."

        show yuuko closedhappy_up_close
        with persistent.charachange

        yu "I think I know who it is!"

        show yuuko happy_down_close
        with persistent.charachange

        yu "I got an anonymous tip as to their identity!"

        yu "So I did some spying, and I think the tipster was right!"

        hi "Oh really? And who was this er, burglar?"

        show yuuko worried_down_close
        with persistent.charachange

        "Yuuko shuts her mouth, shaking her head decisively."

        yu "Nope, I can't tell you that."

        hi "Why not?"

        show yuuko worried_up_close
        with persistent.charachange

        yu "It's between me and the burglar."

        yu "I can't risk you warning him that I'm on to his game."

        yu "He could tip his hand early and blow town."

        yu "Then I'm left with no perp."

        "When did Yuuko start talking like a hard-boiled detective?"

        hi "I wouldn't warn them! Why would I care?"

        show yuuko neutral_down
        with charadistant

        yu "If you've got to ask that question, then you don't need to know."

        hi "That doesn't make any sense, but okay."

        hi "Congratulations, I guess?"

        show yuuko closedhappy_down
        with persistent.charachange

        yu "Thanks!"

        show yuuko worried_up
        with persistent.charachange

        yu "Uh, what for?"

        hi "The uh, cat burglar thing?"

        show yuuko smile_down
        with persistent.charachange

        "Yuuko nods and smiles appreciatively."

        yu "So! Studying for exams?"

        hi "Well, that was the plan. I'm not having much luck, though."

        show yuuko worried_down
        with persistent.charachange

        yu "Really? Is it because you can't find a book?"

        show yuuko panic_up
        with persistent.charachange

        yu "I'm really sorry!"

        yu "I've been meaning to clean the shelves up for weeks now, but I keep getting distracted!"

        yu "I'm so sorry!"

        hi "Woah, wait."

        hi "It's not that. I've got my book right here."

        "To illustrate the point and hopefully calm Yuuko down, I show her the textbook in front of me."

        hi "My mind just keeps wandering, is all."

        show yuuko worried_up
        with persistent.charachange

        yu "Is it because of the noise in here?"

        yu "I'm trying to be more strict about the noise levels, but I can't bring myself to yell at people…"

        show yuuko worried_down
        with persistent.charachange

        yu "I mean aren't their lives hard enough without me throwing my authority around?"

        hi "No, it's not the noise level either, I promise."

        hi "I'm just…"

        "Hell, I don't know."

        "Worried about Emi."

        "Worried about us."

        "Worried about what happens after we graduate."

        hi "Emi's been kind of weird, lately."

        show yuuko worried_up
        with persistent.charachange

        yu "What do you mean?"

        hi "Well, you know how we're dating now?"

        hi "I just don't know that we're actually, you know…"

        hi "A couple. Or at least I don't know that we're beyond friends."

        "Though friends normally don't do the sort of things we do."

        "Physically we're a couple."

        "Coupling, at least."

        hi "It's like every time I try to find out more about her, or about what she wants to do with her life, she dodges the question."

        hi "Like the other day, I was talking to her at lunch about some schools I've been looking into."

        hi "And I asked her, 'Have you looked into any schools lately?'"

        hi "She shrugs in response, says no, and when I ask why not, she says that she doesn't think that far ahead."

        hi "I asked why she had that policy, and she…"

        "I suddenly realize what I'm about to start describing, and wisely decide to clam up."

        show yuuko neutral_up
        with persistent.charachange

        yu "She what?"

        hi "Er, she changed the subject."

        hi "Wouldn't talk about it."

        show yuuko neutral_down
        with persistent.charachange

        yu "Maybe it's an uncomfortable subject for her?"

        yu "Or she just doesn't think it needs explaining."

        hi "Yeah, but it's not just that."

        hi "Every time I try to find out what's been bothering her, she changes the subject too."

        hi "It's like she likes being with me, but not getting close to me."

        "Now that I've said it out loud, I feel worse."

        "Yuuko digests this bit of information."

        show yuuko worried_down
        with persistent.charachange

        yu "You know, it seems to me that you're more serious about this than she is."

        "I can almost feel my stomach twist into a knot."

        "She's right."

        "That's exactly what it seems like."

        hi "But is that really what's going on? I mean…"

        show yuuko panic_up
        with persistent.charachange

        yu "Sorry! I'm just talking nonsense!"

        yu "You shouldn't take my advice, you barely know me!"

        show yuuko cry_down
        with persistent.charachange

        yu "I'm just the librarian, and I'm single so you can imagine I can't know what I'm talking about!"

        hi "No, I think…"

        hi "I think you have a point."

        "As much as it hurts to even consider it."

        "Yuuko seems to try desperately to find a way to soften the blow somewhat."

        show yuuko neutral_down
        with persistent.charachange

        yu "Er, look."

        show yuuko smile_down
        with persistent.charachange

        yu "I'm probably wrong, but if you want to be sure of how obviously wrong I am, maybe you should just talk to her?"

        yu "Get some time alone and just ask about it."

        show yuuko closedhappy_down
        with persistent.charachange

        yu "And don't let her change the subject, either!"

        hi "Yeah, maybe I should do that."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=60}Or maybe I should just enjoy what I have."

        n "We have fun hanging out, after all."

        n "And the runs are nice, and the other activities are nice, and talking to her is nice…"

        n "Do I really need to get closer to her? What I've got right now is pretty good."

        n "But that's silly."

        n "I want to get closer to her."

        n "I want to be able to help her out with whatever is bothering her."

        n "But… maybe I should wait until after exams are over."

        n "Maybe she'll brighten up once the stress has passed."

        n "If she does, then I don't need to worry about it any more."

        n "But if she doesn't, well."

        n "I'll cross that bridge when I come to it."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")

        nvl hide dissolve
        nvl clear

        stop music fadeout 5.0

        "I thank Yuuko for her advice and head back to my room."

        scene bg school_hallway2
        with locationchange

        "Maybe I'll be able to concentrate more on my studies in there."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .phantom_pain:
        scene bg school_hallway3
        with locationskip
        play music music_tranquil fadein 3.0

        "I leave the room after finishing my final exam and breathe a sigh of relief."

        "As I'd hoped, the exams weren't so bad. I managed to breeze through just about everything but the English final."

        "And even that was acceptable."

        "I wonder how Emi did."

        "Even more so, how she's doing; she looked terrible at lunch today."

        "I mean, she was pretty happy to be out of her wheelchair, but she was so exhausted."

        "Something's been wearing her down, and I'm starting to really doubt that it was just the exams."

        "Should I confront her about this, though?"

        "My musing is interrupted by a tap on the shoulder."

        show muto smile at center
        with charaenter

        mu "Hey, Hisao."

        menu:
            with menueffect
            mu "Got a minute?"

            "I suppose I can spare a few minutes.":
                $ have_a_minute = True

                call a3ec2o1

            "No, I have other things to worry about." if True:
                $ have_a_minute = False

                call a3ec2o2

        scene bg school_dormhisao
        with locationskip

        "The question keeps spinning in my head even after I made my way back to my room."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=60}What if she gets angry about it?"

        n "Besides, what if it's nothing?"

        n "If I go in and refuse to leave until she tells me what's wrong or something, won't that come off as clingy?"

        n "I don't want to start a fight or anything over something like this."

        n "Maybe I should just drop the matter and see how she is tomorrow before I do anything."

        n "Would it be so bad to just let it go?"

        n "It's not like we don't enjoy each other's company."

        n "But odd as it sounds, I really want to… help her."

        n "I don't even know what with or if there's anything at all she needs help for."

        n "But I want to."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")

        play sound sfx_doorknock

        stop music fadeout 2.0

        nvl clear
        nvl hide dissolve

        "Suddenly, a knock at my door rouses me."

        play sound sfx_dooropen

        scene bg school_dormhallway
        show kenji neutral at center
        with locationchange

        "I open it to see Kenji."

        hi "Oh, it's you."

        play music music_kenji

        show kenji tsun
        with persistent.charachange

        ke "It's me? That's it?"

        ke "If you had any idea what I'd been through, what I'd done, you'd be happier to see me, dude."

        ke "I mean that was some epic, you-may-never-see-me-again shit."

        ke "And here you're just acting like I went down to the store for some milk."

        show kenji happy
        with persistent.charachange

        ke "You're a cold man, Hisao. I really respect that."

        hi "Uh, thanks, I guess."

        show kenji neutral
        with persistent.charachange

        ke "It's smart to play it safe, you know. Don't show any emotion."

        ke "Keep your cards close to your chest."

        ke "Unless it's time to show your cards, or you have bad cards."

        ke "Then you should fold or collect your winnings."

        show kenji happy
        with persistent.charachange

        ke "Do you understand?"

        hi "Yeah, that makes perfect sense."

        hi "I take it the uh, mission went well?"

        show kenji tsun
        with persistent.charachange

        ke "Woah, awfully nosy of you, isn't it?"

        ke "You can't just go saying things like that! Things are at a delicate stage!"

        ke "One wrong move, and BAM! The invasion succeeds!"

        hi "I thought you were going to blow the conspiracy wide open?"

        ke "It's bigger than I thought; I need to update my charts."

        ke "And probably change some of the puppets around."

        show kenji happy
        with persistent.charachange

        ke "You wanna help? I've got some whiskey from… somewhere."

        ke "You can fill me in on everything your investigation has turned up."

        hi "Er, better not. I'm uh… supposed to meet her today."

        hi "Gotta go do that. Can't raise suspicion."

        show kenji neutral
        with persistent.charachange

        "Kenji nods in approval."

        ke "Still keeping it close to the chest, eh? Okay man, I respect that."

        ke "Good luck."

        hi "Er, thanks."

        hide kenji
        with charaexit

        stop music fadeout 4.0

        "I'm just going to pretend, for the sake of my own sanity, that he's wishing me luck in talking to Emi."

        "And if I squint, that whole card analogy he was talking about works here."

        "Time to lay it all on the table."

        "Or see if I can't get Emi to do so, rather."

        "With a sense of something approaching purpose, I head for Emi's room."

        scene bg school_girlsdormhall
        with locationskip

        play sound sfx_doorknock2

        "I hop up the stairs leading to her room and knock on her door."

        emi "W-who's there?"

        play music music_drama fadein 8.0

        "Huh. That's odd. Her voice sounds a little choked."

        hi "Hey, it's me. Thought I'd stop by."

        emi "Hisao?"

        emi "Come on in!"

        "I reach down to open the door, only to find that it's locked."

        "More and more curious."

        hi "Er, your door's locked."

        emi "Oh yeah, sorry. Gimme a minute."

        show emi basic_grin:
            tworight
            xpos 0.8
            easein 0.5 tworight
        with charaenter

        show emi at tworight

        "In a few minutes, Emi opens the door, grinning."

        emi "Sorry, I had to put my legs on. I was napping."

        "Despite her grin, there's something definitely off."

        "Emi's eyes are slightly red, and it looks like she's been crying."

        hi "Hey, no problem."

        hi "Er, are you okay?"

        show emi sad_shy
        with persistent.charachange

        emi "Huh? Yeah, I'm fine!"

        hi "It's just that you look like you've been crying…"

        "Oh yeah, Hisao. You're off to a great start on this one."

        show emi sad_grin
        with persistent.charachange

        emi "What? Nah, I'm fine. I'm just happy to see you."

        scene ev emi_firstkiss
        with flash

        "She punctuates this with a long kiss that continues as the door slams shut behind us."

        "I know what she wants to do now, and I'm also painfully aware of how badly I want to do it too, but…"

        scene bg school_dormemi at left
        show emi excited_amused_close at center
        with locationchange

        "I break the kiss with a wrench of self control that nearly kills me."

        hi "Hey, wait."

        show emi basic_confused_close
        with persistent.charachange

        "Emi's eyes crinkle in confusion."

        emi "Huh? Wait for what?"

        hi "We need to talk."

        show emi sad_grin_close
        with persistent.charachange

        emi "Isn't that supposed to be my line?"

        show emi sad_shy_close
        with persistent.charachange

        emi "And never a good thing to say?"

        "She's got a point."

        "It's usually the lead-in to a breakup."

        "Or the prelude to a fight."

        hi "Maybe it can be a good thing this time."

        hi "Er, that's the hope, anyway."

        show emi sad_shyblush_close
        with persistent.charachange

        emi "Uh… huh."

        show emi basic_grin_close
        with persistent.charachange

        emi "Can we at least get onto the bed? It's my first day back on these things, and I'm still readjusting."

        show emi basic_closedgrin_close
        with persistent.charachange

        emi "Plus the nurse said I should try to be on them less often, since running puts such a strain on them."

        hi "Can't argue with that."

        "It's a trap, we both know it, and we both don't care."

        "Then again, it's awfully hard to get angry while in bed with the object of your affections, so maybe there's that motivation too."

        hide emi
        with charaexit

        show bg at right
        with charamove

        show emi basic_grin_close:
            center
            easein 0.5 ypos 1.1
        with charaenter

        show emi:
            center
            ypos 1.1

        "I set Emi's legs by the bedside and sit down next to her, throwing an arm around her shoulders."

        "In silence, we just enjoy being able to be in this position again for a few minutes."

        "Then, of course, I need to ruin it by opening my mouth."

        hi "Look, I know that… that you've been having kind of a rough time of it lately."

        hi "And I want to help you out."

        hi "I thought it was just exams getting to you, but now I come to your room and you've been crying, and that kills me."

        hi "But I can't do anything if you won't talk to me about it."

        show emi basic_closedgrin_close
        with persistent.charachange

        emi "I told you, I'm fine."

        hi "No, you aren't. It's obvious something's eating at you."

        hi "You can tell me, you know."

        "There's the slightest increase in tension in Emi's voice."

        show emi sad_shy_close
        with persistent.charachange

        emi "Why is my saying I'm fine not good enough?"

        show emi sad_annoyed_close
        with persistent.charachange

        emi "You're concerned, I get that. That's cool."

        emi "But I'm fine, and it's nothing that you need to worry about."

        hi "Not sleeping and spacing out more than Rin doesn't strike me as 'being fine.'"

        hi "I just… I want to help."

        emi "Uh-huh."

        hi "Yeah, I don't like seeing you like this."

        hi "I want you to be happy, you know?"

        show emi basic_annoyed_close
        with persistent.charachange

        "I get the feeling that came out wrong, because Emi fixes me with an icy stare."

        emi "So you want to fix me, Hisao?"

        "She's definitely getting angry now."

        show emi sad_grit_close
        with persistent.charachange

        emi "Wanna swoop in on your white charger and save the day?"

        emi "Stop the nightmares, the phantom limb pains?"

        show emi sad_angry_close
        with persistent.charachange

        emi "Restore what's lost?"

        show emi sad_depressed_close
        with persistent.charachange

        "Her voice catches in her throat, and the tears start to flow."

        emi "Well you {b}can't{/b}."

        show emi sad_pout_close
        with persistent.charachange

        emi "Nobody can."

        emi "Nobody will."

        "I'm so stunned by her sudden verbal assault that I remain quiet."

        "Neither of us says anything for a while."

        "I'm surprised that Emi tightens her grip on me rather than pushing me away."

        "After a deep breath, she starts talking again."

        show emi sad_shy_close
        with persistent.charachange

        emi "Look, I'm sorry."

        show emi sad_depressed_close
        with persistent.charachange

        emi "I just… there's these nightmares."

        emi "About the accident."

        "Ah. The accident. I should've known."

        "It took her legs, after all, but it never comes up, of course."

        show emi sad_pout_close
        with persistent.charachange

        emi "And I usually deal with them fine, because I can run."

        emi "Running clears my head like nothing else."

        emi "I don't have to worry about anything while I'm running."

        emi "I just concentrate on breathing, on the rhythm of things."

        emi "It's easier that way. Life's easier that way."

        show emi sad_shy_close
        with persistent.charachange

        emi "Just keep moving forwards, you know? Nothing else matters, just getting around the next curve."

        emi "And then it's the next curve, and the next, and the next, until I can't go any more, or think any more, or do anything but slow down and walk until I catch my breath again."

        emi "After something like that, nothing else matters."

        show emi basic_annoyed_close
        with persistent.charachange

        emi "But I've been stuck in that goddamned wheelchair for too long. So, no outlet."

        show emi sad_shy_close
        with persistent.charachange

        emi "Today it just kinda boiled over a little."

        hi "You could have talked to me about it, you know."

        hi "You didn't have to go it alone."

        show emi sad_grin_close
        with persistent.charachange

        "Emi smiles sadly, like she's trying to explain to a child that all fire burns."

        emi "Yeah, I did. And I do."

        hi "But why?"

        hi "Why do you have to keep going through this alone?"

        hi "Why can't you just trust me enough to let me help you?"

        "That smile again."

        show emi excited_amused_close
        with persistent.charachange

        show emi sad_grin_close
        with persistent.charachange

        "Emi leans in and kisses me on my cheek, an almost motherly gesture."

        "She leaves her mouth close to my ear, as she confesses this one thing to me."

        show emi sad_shy_close
        with persistent.charachange

        emi "Because, Hisao."

        emi "I've already had everything I knew ripped away from me once."

        show emi sad_depressed_close
        with persistent.charachange

        emi "I don't know what I'd do if it happened again."

        "She pauses, as if uncertain as to whether or not she should continue."

        "I can feel a violent churning in my gut."

        "She continues."

        show emi sad_shy_close
        with persistent.charachange

        emi "So I can't rely on you."

        emi "Or the nurse."

        emi "Or anyone else."

        show emi sad_pout_close
        with persistent.charachange

        emi "Just me."

        emi "That's how it's got to be."

        "Having delivered this short speech, she looks down and covers her mouth with the back of her hand."

        "The conversation is clearly over. I search for something to say, but can't think of anything."

        hi "I…"

        hi "Maybe I should go, for now."

        hi "I've got… stuff."

        "Emi doesn't even look up."

        "She sounds tired, or relieved."

        "I can't tell which."

        emi "Okay, Hisao."

        emi "Go take care of that stuff."

        emi "I'll see you tomorrow."

        hide emi
        with charaexit

        pause 0.2

        show bg at left
        with charamove

        "I get off the bed and head for the door, pausing at the doorway."

        hi "Hey, Emi…"

        show emi sad_shy at tworight
        with charaenter

        emi "Yeah?"

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=60}A thousand things I want to say."

        n "I'm too mixed up to say any of them, though."

        n "After her admitting that she'll never let me close, I feel like {b}my{/b} world's just been ripped out from me."

        n "What happened in that accident?"

        n "I know she lost her legs, but that's never seemed to bother her."

        n "What happened there?"

        n "What scares a girl so badly that she won't accept help, even from someone she loves?"

        n "I don't know."

        n "{vspace=30}But I want to know."

        n "I want to know so badly that being denied that answer feels like a knife in my guts."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl clear
        nvl hide dissolve

        emi "Hisao?"

        emi "You were saying?"

        "I'm still standing in the doorway."

        hi "…Nothing."

        hi "Never mind."

        scene bg school_girlsdormhall
        with locationchange

        play sound sfx_doorclose
        stop music fadeout 6.0

        "And I'm closing the door."

        "And walking down the hallway."

        "Down the stairs."

        scene bg school_dormext_full_ni
        with locationskip

        "Out the door."

        "Into the dark."

        scene bg school_dormhisao_ni
        with locationskip

        play music music_night fadein 1.0

        "Somehow I wander back to my own room. My brains are doing a mile a minute, going nowhere fast."

        nvl clear
        nvl show dissolve

        n "{vspace=60}I can't figure out how to deal with this."

        n "I thought that moving forward was a good thing."

        n "Dwelling less on a past that I can't change. Living in the present and looking at the future."

        n "{vspace=60}After this… thing with Emi, I'm not sure any more."

        n "She was saying the truth. It's simpler to look at the next curve, ignoring the path gone by."

        n "No worry about the opponent left behind. No care for the spectators on the sidelines."

        n "And unfortunately, no time to watch out for lagging teammates either."

        nvl clear
        nvl hide dissolve

        "I throw myself down on the bed, looking at one corner of my ceiling as if the answers I want were written there."

        "No such luck, of course."

        nvl clear
        nvl show dissolve

        n "{vspace=150}She's literally running away from something - but have I not been doing the same thing, trying my best to forget about my hospitalization?"

        n "I am getting better, but my health isn't going to magically fix itself."

        n "{vspace=30}Emi has two legs instead of a heart to deal with, but those aren't going to magically fix themselves either."

        n "{vspace=30}Maybe this is just as fixed as the both of us can get."

        nvl clear
        nvl hide dissolve

        "The room becomes darker and darker, until I can't really tell I'm looking at a corner any more."

        if _in_replay:
            return

    label .debate_expresses_doubt:
        scene bg school_dormhisao
        with shorttimeskip

        "The morning comes too soon, on the heels of a sleepless night."

        "Is this how Emi's been spending her nights?"

        "Staring at the wall, or ceiling. Trying to stop thinking about whatever it is."

        "Her, in my case."

        "That clenched feeling in my gut is still there."

        nvl clear
        nvl show dissolve

        n "{vspace=60}'I can't rely on you.'"

        n "{vspace=30}Words spoken so casually."

        n "Almost like she were teasing me, or chastising me for suggesting that the Earth is flat."

        n "{vspace=30}'That's how it's got to be.'"

        n "{vspace=30}The way it's got to be sucks."

        n "I'm feeling so miserable that I very nearly decide to skip the run."

        n "That would be stupid, though. It's not something I should do just to see her."

        n "Sure, that was the original reason, but it's something more now."

        nvl clear

        n "{vspace=120}I've started to enjoy the running itself."

        n "There are worse ways to get the blood flowing, anyway."

        n "Never thought I'd say it after that first week or so, but—"

        n "{vspace=30}I feel a lot better after a run, like no matter what else I do today, I've at least done that one thing."

        n "It wakes me up, too, and Emi herself said that running always clears her mind. Maybe it'll help clear mine."

        n "{vspace=30}I hope so."

        nvl clear
        nvl hide dissolve

        scene bg school_track
        with locationskip

        "The morning is cool and clear, if a bit humid. Summer's making itself known, it seems."

        "Emi's already stretching out when I arrive, and greets me with a smile and a wave."

        show emi basic_closedgrin_gym at center
        with charaenter

        emi "Hey, Hisao!"

        "The sight of her so chipper is like a kick in the nuts."

        "How can she be so happy after yesterday?"

        show emi excited_amused_gym_close
        with characlose

        "I give a half wave and am surprised to receive a hug."

        show emi sad_shy_gym_close
        with persistent.charachange

        emi "Hey, about last night."

        "Here it comes."

        stop music fadeout 1.0

        show emi basic_grin_gym_close
        with persistent.charachange

        emi "I wanted to say thanks."

        show emi excited_happy_gym_close
        with persistent.charachange

        emi "I actually managed to get some sleep for the first time in a while, and I think it's because of our talk."

        show emi basic_closedgrin_gym_close
        with persistent.charachange

        emi "So, thanks."

        play music music_rain fadein 4.0

        "How could she sleep better after our chat?"

        "She basically told me that she wouldn't get any closer to me."

        "And that let her sleep well?"

        "Excuse me, but what the hell?"

        "Emi either doesn't notice my bafflement or chooses not to notice."

        "No telling with her any more."

        hi "Oh, no problem. Glad it helped."

        "The venom that threatens to drip into my voice is controlled for now, but I think I'd better start running now, before I do anything stupid."

        scene bg school_track_on
        with locationchange

        "Emi seems equally willing to get started, and before long we're darting around the track."

        "I can tell she feels more relaxed."

        scene ev emi_run_face:
            truecenter
            acdc_warp 20.0 zoom 1.1
        with flash

        "Her running has gone back to the more graceful movements I remember from when I first watched her."

        "It's a stark contrast to the almost brutal way she's been hurling herself around the track these past few days."

        "Our talk really does seem to have helped her."

        "A pity it couldn't help me."

        "I get into the rhythm of the running, thinking back to when I couldn't afford thinking about anything else but keeping my breathing steady and legs moving."

        "Guess those days are gone."

        "At least for the first couple of laps."

        scene bg school_track_running
        with Dissolve(2.0)

        "Annoyed at the lack of success I'm having with clearing my head, I increase the pace."

        "Ah, there's the burning sensation in my legs."

        "The breaths coming ragged in my chest, the pounding of my heart. Which I still need to be careful about."

        "But it does seem to have gotten stronger; I can feel it pumping blood through my veins."

        "The sound thrums in my ears, but instead of being panicked as I was that day in the snow, I'm instead filled with elation."

        "Yes, it's working! My heart, that fatal flaw that landed me here, has improved."

        "I'm able to keep going now, and maybe one day I'll be able to stop worrying as much."

        "Right now, it doesn't matter that I have no idea what to do about Emi and me."

        "All that matters is that my arms and legs continue to pump in concert with one another."

        "Nothing else."

        scene bg school_track_on
        with locationchange

        "As I hit the final stretch, I remind myself that running really does help, though not as much as I'd hoped."

        "I do feel better, and as I walk a few laps to cool down, I begin to remember last night in a slightly less emotional manner."

        "Emi wants me to stay distant from her."

        "I can't bring myself to do so."

        "There's got to be a way around this, some kind of middle ground I can reach."

        "Not sure what that middle ground is, though."

        "Damn, I was almost feeling optimistic."

        show emi excited_joy_gym at center
        with charaenter

        emi "Nice run, Hisao! You've really improved!"

        "Nice run. That's all I can hope for now, isn't it?"

        "Congratulations, Hisao. You're pathetic."

        "I gotta change my attitude."

        hi "Well, you know. I am pretty awesome."

        "And yet I just keep saying things that I don't mean."

        "Any second now I'll be as good at hiding my problems as Emi is."

        show emi basic_closedgrin_gym
        with persistent.charachange

        emi "I like to think so."

        "Why does she do this to me? Say something like that with such real affection in her voice that it makes my heart leap?"

        "She doesn't mean it. She can't."

        "I must be doing a worse job than I thought, because Emi peers closely at me."

        show emi basic_confused_gym
        with persistent.charachange

        emi "Hey, you feeling okay?"

        show emi basic_hes_gym
        with persistent.charachange

        emi "Maybe we should get to the nurse, huh?"

        hi "Yeah, I'd hate to keel over on you."

        "Emi looks a little shocked at my bitter tone."

        show emi basic_shock_gym
        with persistent.charachange

        emi "Don't say things like that!"

        show emi sad_shy_gym
        with persistent.charachange

        emi "You've already done it once before, you know."

        "Why does she act so affectionate?"

        "She doesn't really care, I thought she made that clear."

        "But despite all of that I find myself apologizing, even though I shouldn't have to. Even though she's probably just putting on an act."

        hi "Sorry, heh."

        hi "Come on, let's see the nurse."

        "I can't get myself to calm down the whole time."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=120}Every time it feels like I've gotten over what happened last night, Emi does something or says something that shows affection, and I'm back to the beginning."

        n "The image of her ending that conversation haunts me."

        n "It was like the final twist of the knife that left me feeling bereft of any hope that Emi and I could be more than what we are."

        n "And what are we at this point? Little more than friends who happen to fuck."

        n "And really, it's not like I don't enjoy the time I spend with her. Said so the other day myself."

        n "I very nearly didn't even bring anything up with her, was just gonna hop on in there and let it ride, wasn't I?"

        stop music fadeout 2.0

        nvl clear
        nvl hide dissolve

        scene bg school_nursehall
        with shorttimeskip

        "With this running through my head, I find myself in front of the nurse's office, still brooding as he checks out Emi."

        "Emi comes bounding out of the door, gives me a kiss, and darts off to shower, I assume."

        "Meanwhile, the nurse beckons me into his office to give me the ritual once-over."

        $ renpy.music.set_volume(1.0, 0.0, channel="music")
        play music music_nurse fadein 0.5

        scene bg school_nurseoffice
        show nurse neutral at center
        with locationchange

        nk "Any problems today?"

        hi "Nah. I even pushed it a little harder today than I have in the past, and I seemed able to handle it."

        show nurse grin
        with persistent.charachange

        nk "That's uncharacteristically risky coming from you, Hisao."

        nk "You've been hanging out with Emi too much. She's rubbed off on you, and not necessarily in a good way."

        "At the mention of Emi's name, I can't help but frown unhappily in spite of my efforts at control."

        show nurse fabulous
        with persistent.charachange

        nk "Well, now. This is new, don't you think?"

        show nurse neutral
        with persistent.charachange

        nk "Last I checked, your usual response to Emi's name was a grin, not a frown."

        show nurse concern
        with persistent.charachange

        nk "What exactly happened between you two? Because Emi doesn't seem to be in on it, whatever it is."

        show nurse neutral
        with persistent.charachange

        nk "She looked more relaxed than I've seen her in weeks, which is unusual for this time of the year."

        hi "What do you mean by that?"

        show nurse fabulous
        with persistent.charachange

        nk "By what?"

        hi "'For this time of year.' I keep trying to find out what's been bothering her, but she clams up as soon as I broach the subject."

        hi "Then last night, she said—"

        show nurse neutral
        with persistent.charachange

        nk "Let me guess. She won't tell you, because she says she can't trust you?"

        nk "And now you're crushed, because you thought that the two of you were so much more than she seems to think, right?"

        hi "Er, more or less."

        hi "How the heck did you know?"

        show nurse grin
        with persistent.charachange

        nk "Hisao, I'm the nurse. It's my job to know these things."

        show nurse neutral
        with persistent.charachange

        nk "Plus, I've known Emi for long enough to know that she'd try to do something like this; it's just like her."

        "He says this in the sort of half-affectionate, half-frustrated tone that would seem more appropriate if he had a cigarette dangling from his lips."

        "As it is, he seems willing to make do with a pen."

        show nurse fabulous
        with persistent.charachange

        if have_a_minute or _in_replay:
            menu:
                with menueffect
                nk "Look, you mind if I give you some advice?"

                "Sure, why not?":
                    $ got_advice = True

                    call a3ec3o1
                "No, this is my problem." if True:
                    $ got_advice = False

                    call a3ec3o2

        $ renpy.music.set_volume(0.3, 0.0, channel="sound")
        play sound sfx_hammer

        "I open my mouth to respond but a knocking sound at the door interrupts me."

        emi "Hey, you guys still in there?"

        show nurse grin
        with persistent.charachange

        nk "Just a moment, Emi."

        nk "Give us a second to get our pants back on."

        $ renpy.music.set_volume(1.0, 0.0, channel="sound")
        play sound sfx_doorslam

        show emi basic_annoyed_gym:
            center alpha 0.0
            ease 1.0 tworight alpha 1.0
        with None

        show bg at bgleft
        show nurse at twoleft
        with charamovefaster

        show emi at tworight

        "The door bursts open and Emi glares knives at the nurse."

        emi "Asshole."

        show nurse fabulous
        with persistent.charachange

        nk "Didn't mean to get your hopes up."

        hi "Hey, can we… leave me out of this?"

        hi "Anyway, what's up, Emi? Forget something?"

        "I try to take a more cheerful tone with her."

        "No need to upset her. Two can play the 'everything's fine' game."

        show emi sad_grin_gym
        with persistent.charachange

        emi "Actually, I forgot to ask you something."

        hi "Oh? What's that?"

        show emi basic_happy_gym
        with persistent.charachange

        emi "Do you wanna come with me on a trip to my house?"

        show emi basic_closedgrin_gym
        with persistent.charachange

        emi "My mom's making dinner, and I thought you might want to join us."

        show nurse grin
        with persistent.charachange

        nk "Well, of course I accept."

        show emi basic_closedgrin_gym:
            parallel:
                "emi excited_proud_gym" with Dissolve(0.2)
            parallel:
                ease 0.2 xpos 0.6
                ease 0.2 tworight

        pause 0.5

        "Emi punches the nurse in the arm playfully."

        emi "Not you, idiot. You were over last week."

        show emi sad_grin_gym
        with persistent.charachange

        emi "I was talking to Hisao."

        show nurse neutral
        with persistent.charachange

        nk "Oh? How interesting! Meeting the parent!"

        hi "I'd love to go, Emi. Thanks."

        show nurse fabulous
        with persistent.charachange

        "The nurse raises an eyebrow, but says nothing."

        emi "Great! I'll be in my room, swing by after you shower and change into something clean and we'll grab the bus!"

        hi "Sounds good. I'll see you in a bit!"

        stop music fadeout 2.0

        show emi excited_amused_gym_close
        with characlose

        "This time it's me who leans in for a quick kiss before darting off to my room."

        scene bg school_dormhisao
        with locationskip

        "What an interesting development."

        "Maybe we're getting closer after all."

        "Maybe Emi's finally ready to open up a little."

        "Or maybe she's just being polite, and a free meal seems like a good way to apologize for last night."

        "Great. Now I can't decide whether to be excited, nervous, or depressed."

        "I settle for a combination of all three and hop in the shower."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .guess_whos_coming_never_mind:
        $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
        play ambient sfx_businterior fadein 2.0

        scene ev busride
        with locationchange

        nvl clear
        nvl show dissolve

        n "{vspace=90}I don't think I like riding on buses."

        n "Actually, I think I'm pretty comfortable saying that as a fact."

        n "They sway a lot, and they smell funny, and you can feel every bump in the road."

        n "I'm really not looking forward to this."

        n "{vspace=30}Plus Emi's legs keep making a clanking noise that draws the attention of everyone else on the bus."

        n "She's in shorts again, and she's got long socks drawn up on her prosthetics so they don't look so obviously false again."

        n "But that doesn't stop the odd look or two every time her legs bump together with an audible clunk."

        nvl clear

        n "{vspace=90}I shift nervously in my seat, and Emi raises an eyebrow questioningly."

        n "She doesn't seem to mind the stares; either that or she doesn't even notice that people are staring."

        n "I'm sure she's gotten her fill of odd looks before. After a certain amount of time, I doubt she'd notice any more."

        n "{vspace=60}Not that she'd ever tell me if I asked."

        n "Another fact is, I'm not just uncomfortable about the bus."

        n "I can't seem to come to terms with the fact that Emi appears to be trying to bring me closer while at the same time pushing me away."

        nvl clear

        if have_a_minute and got_advice or _in_replay:
            n "{vspace=90}The nurse said she trusts me, even if it doesn't look like it."

            n "But I'm not sure I can trust the nurse."

            n "He's protective of Emi, just like I'm protective of Emi, and I'd be likely to say something to make her look good if someone asked me about her."

            n "{vspace=30}So he might just be doing that."

            n "{vspace=30}Still, there was something about the way he seemed genuinely surprised that Emi invited me along…"

            n "Maybe last night's talk helped more than I think, but I'm still worried."

        stop ambient fadeout 12.0

        nvl clear

        n "{vspace=90}Meeting the parents is a big deal, right?"

        n "Not that I haven't already met Emi's mother, but that was just as an acquaintance."

        n "Now it's going to be as Emi's boyfriend, with everything that implies."

        n "I can feel my heart pounding in my chest, an echo of that snow-covered afternoon that feels like it was so long ago that it might as well be another life entirely."

        n "Except then, I didn't know what was going on; I also didn't have medication to help prevent things spiraling out of control."

        n "I've come a long way in terms of my physical health, and for the second time today I feel like I'll be able to live normally now, or at least as normally as possible."

        n "{vspace=30}Now if only I could manage my relationship as well as I've managed my heart, I'd be in great shape."

        stop ambient fadeout 1.5

        nvl clear
        nvl hide dissolve

        scene bg city_street4
        show emicas smile_close at center
        with shorttimeskip

        $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
        play ambient sfx_traffic fadein 2.0

        emi "Well, we're here."

        play music music_soothing fadein 2.0

        "Emi grabs my hand as soon as we've stepped off the bus. She starts heading down the street almost immediately."

        show emicas wink_up_close
        with persistent.charachange

        emi "Come on, we've got a couple blocks until my place."

        hi "What? Oh, okay."

        scene bg city_alley
        with locationchange

        stop ambient fadeout 12.0

        "I follow Emi down the street, watching her confident stride."

        "She's setting kind of a quick pace for just a walk."

        "I guess she's anxious to get there."

        hi "So does your mom do this sort of thing often?"

        show emicas neutral_close at center
        with charaenter

        emi "Nah, not too frequently. Mom's never been much for playing hostess."

        hi "Oh yeah?"

        show emicas awayfrown_close
        with persistent.charachange

        emi "Yeah, my dad was always the one pushing her to have people over."

        "This sudden and unprompted reference to her father catches me off guard."

        "And from the look on Emi's face, I'm not sure she meant to mention him. I think I've only ever heard her talk about him once."

        "All I remember is that Emi's mom told me that he wasn't around any more."

        hi "Oh? Your mom prefers solitude?"

        show emicas happy_up_close
        with persistent.charachange

        "Emi laughs, either from relief that I didn't ask about her father or from finding my statement actually funny."

        emi "Not at all! She's why I'm such an outgoing person, you know."

        show emicas closedsmile_close
        with persistent.charachange

        emi "She just prefers to be a guest rather than a hostess; it's less stressful that way, or so she says."

        hi "Clearly she's never had to meet her girlfriend's mother for dinner."

        "Emi giggles again and speaks in a teasing tone."

        show emicas wink_close
        with persistent.charachange

        emi "Nervous, Hisao?"

        show emicas smile_close
        with persistent.charachange

        emi "You shouldn't be, you know! It's not that big a deal! Just dinner at my house, that's all!"

        hi "Yeah, but have you ever brought home a boyfriend before?"

        "I confess that part of me dreads hearing the answer to this."

        "I know very little of Emi's past relationships - I don't even know if there were past relationships."

        show emicas awayfrown_close
        with persistent.charachange

        emi "No, I guess I haven't."

        show emicas frown_close
        with persistent.charachange

        emi "Hey, maybe this really is kind of a big deal after all…"

        hi "Oh good, now I feel twice as nervous."

        "Though to tell the truth, I'm pretty happy to hear that I'm the first one."

        "Maybe we've got something special after all."

        stop ambient
        stop music fadeout 10.0

        scene bg emi_houseext
        with locationchange

        play sound sfx_hammer

        "Bolstered by this new thought, I've managed to calm down considerably by the time Emi knocks on her front door."

        show emicas grin_up at center
        with charaenter

        emi "Hey, mom, open up! We're here!"

        show bg at bgleft
        show emicas at twoleft
        with charamove

        show meiko smile at tworight
        with charaenter

        "The door swings open, and Mrs. Ibarazaki stands grinning at her daughter. The grin is still surprisingly similar to Emi's."

        "I'm never going to get used to that."

        show meiko wink
        with persistent.charachange

        emm "You know, people normally wait for a few minutes before they start shouting at the door."

        show emicas pout_up
        with persistent.charachange

        emi "And most mothers say hello to their daughters instead of scolding them right away."

        show meiko happy
        with persistent.charachange

        emm "Ah, of course. Welcome home, dear. I've missed you."

        play music music_another fadein 0.5

        scene bg emi_kitchen
        with locationchange

        "An affectionate hug later we're inside, and it is only then that Emi's mom seems to remember that I'm actually here."

        show meiko smile at center
        with charaenter

        emm "And hello to you too, Hisao. How are you?"

        hi "I'm quite well, thank you. Nice to not have school to worry about for a little bit."

        show meiko happy
        with persistent.charachange

        emm "Ah yes, you've finished up your exams, haven't you? That must be quite a relief for you both."

        hi "It's certainly a weight off of my mind, that's for sure."

        show bg at bgright
        show meiko at tworight
        with charamove

        show emicas happy at twoleft
        with charaenter

        emi "Mine too! I think I slept well for the first time in weeks last night from relief alone."

        "If this news is a surprise to Emi's mother, she doesn't show it. Still, her response betrays a note of interest."

        show meiko smile
        with persistent.charachange

        emm "Is that so? I'm very glad to hear that, Emi. You know I get worried when you get all wound up about… well, exams."

        "Certainly Emi's mother knows something I don't - or rather, she doesn't know that Emi's told me about the nightmares."

        "It's interesting, being able to observe how Mrs. Ibarazaki covers for Emi. That protective instinct to make sure that I don't know any more than Emi's willing to tell me."

        if have_a_minute and got_advice or _in_replay:
            "I suppose Emi's got more in common with quarks than I ever realized."

            "Moves around fast, impossible to understand through direct observation, yet she has an effect on everyone she encounters."

        "I wonder if Mrs. Ibarazaki will figure out that I know about the nightmares, or is she just keeping everything secret from everybody?"

        show emicas weaksmile
        with persistent.charachange

        emi "Yeah, it's not been as bad this year as in the past; Hisao helped me to stay focused."

        "Okay, I know that's not true. She even cut off contact outside of school hours during exam week!"

        "But… she did see me during the day. And she told me more than once that the morning run was the only thing she looked forward to during exams, so maybe it's not that much of a lie."

        "Either way, to hear that being around has helped even a little makes me feel a bit better."

        "Emi's mother raises an eyebrow at this statement. Either she doesn't believe Emi, or she's as surprised as I am."

        show meiko happy
        with persistent.charachange

        emm "Well, then it appears that it's a good thing you two have become so close."

        show meiko smile
        with persistent.charachange

        emm "I'd tell you to take good care of my daughter, Hisao, but it looks like you're already doing that."

        show emicas closedsmile
        with persistent.charachange

        "Emi grins at this and seems to take pride in my having managed to ingratiate myself with her mother so easily."

        hi "Actually, I'd say your daughter's been the one taking care of me. She's gotten me out and running."

        hi "I've probably been more active since meeting her than I ever was, even before…"

        "I'd actually never thought of it that much, nor had I ever appreciated the humor in it."

        "I wasn't too active before the heart attack. Pickup games of soccer don't really count since they weren't that common."

        "So now that I know for sure that I have a weak heart, {b}now{/b} I run every day, pushing my luck with the help of my medication."

        "I chuckle quietly, then realize that I never finished my sentence."

        hi "Well, before I had my heart attack and wound up at school here."

        "It comes out so casually. There was a time that I would have thought twice about talking about what was wrong with me at all."

        "But now? Now it just seems silly to care, especially in the company of Emi and her mother."

        "If Emi can be cavalier about her disability, then so can I."

        "I think back to the track meet, where Emi declared herself the fastest thing on no legs."

        "The fact of her obvious loss has never seemed to bother her, at least not in public."

        "Being stuck in the wheelchair frustrated her, I know. But even that was something she dealt with on her own, despite my efforts to the contrary."

        show meiko happy
        with persistent.charachange

        emm "Emi has a way of bringing out the more active side in people. I've never quite figured out how she does it."

        "Those puppy dog eyes she gets, for starters."

        show meiko smile
        with persistent.charachange

        emm "I'm not surprised that she managed to rope you into an exercise routine."

        emm "If Rin weren't just as stubborn as she is, I'm sure that Emi would have gotten her out and running with you too."

        show emicas happy
        with persistent.charachange

        emi "Oh, that reminds me! Rin says hello."

        scene bg emi_dining
        with locationchange

        "I drift to the outer edges of the conversation again as we move into the dining room to eat."

        "It smells delicious in here, and the spread that Emi's mom has produced is impressive."

        show meiko smile at tworight
        show emicas happy_up at twoleft
        with charaenter

        emi "Woah, you've made enough to feed an army in here!"

        show meiko happy
        with persistent.charachange

        emm "Is it too much? Well, you can always take some leftovers with you when you go."

        hi "That sounds great! I can only handle cafeteria food for so long. Something home-cooked would be a welcome change of pace."

        show emicas smile
        with persistent.charachange

        emi "What he said. Thanks, mom."

        "The food tastes as good as it smells, and there's a lull in the conversation while we all dig in."

        "Emi assaults her plate with the usual amount of gusto, and I will admit that I set a pretty fast pace myself."

        show meiko wink
        with persistent.charachange

        emm "So Hisao, I hear that you and my daughter here have gotten rather close, hmm?"

        "The urge to say something like 'Not really' is so strong that I open my mouth to say it, but then reassert control."

        "We are close, there's no getting around it. I mean Emi's brought me here, hasn't she?"

        "Fortunately, both Emi and her mother seem to take my reaction as a sign that I'm caught off guard rather than considering saying something cruel."

        hi "Heh, I suppose we have. I blame the morning runs, myself."

        show emicas pout_up
        with persistent.charachange

        emi "You make it sound like a bad thing, Hisao."

        show meiko smile
        with persistent.charachange

        emm "Well, I for one found it a relief."

        hi "Why's that?"

        show meiko worry
        with persistent.charachange

        emm "Emi's always been a popular girl, but never made many close friends."

        "This is a bit of news to me. I've always seen Emi chatting with her classmates in the hallways."

        "And certainly the whole track team seems to love her, but it is true that she chooses to isolate herself during lunch with Rin and me."

        "Not exactly the sort of behavior one expects from a popular girl, after all. Then again, I've experienced her unwillingness to get close firsthand, so I can't say I'm that surprised."

        show meiko serious
        with persistent.charachange

        emm "I was beginning to have my doubts."

        show emicas awayfrown_up
        with persistent.charachange

        "Emi rolls her eyes to the ceiling and grumbles something I can't quite make out."

        stop music fadeout 1.0

        hi "Huh?"

        show emicas neutral_up
        with persistent.charachange

        emi "What?"

        hi "What's that you just said?"

        show emicas blush
        with persistent.charachange

        emi "Nothing."

        show meiko happy
        with persistent.charachange

        "Mrs. Ibarazaki chokes on her drink with laughter."

        play music music_comedy fadein 0.5

        emm "You've been hanging out with the nurse too long, Emi."

        emm "I'm going to have to talk to him about corrupting my daughter."

        hi "Somehow I don't think that would be very effective."

        show emicas evil
        with persistent.charachange

        emi "I learned most of it from you anyway. Not the nurse."

        show meiko smile
        with persistent.charachange

        emm "Don't listen to her, Hisao. She's a born liar."

        show emicas awayfrown
        with persistent.charachange

        emi "Hmph. Yeah right."

        hi "Oh, I don't know, Emi. I think your mother has a point."

        show emicas angry_up
        with persistent.charachange

        emi "What? You traitor! You're supposed to take my side in this!"

        hi "Yeah, but you did lie about your leg after the meet—{w=0.3}{nw}"

        with vpunch

        extend " ow!"

        "A kick in the shins from an unmistakably plastic foot cuts me off, but not before Mrs. Ibarazaki's eyebrows shoot upwards."

        show meiko serious
        with persistent.charachange

        emm "What about your leg?"

        show emicas awayfrown
        with persistent.charachange

        emi "It wasn't a big deal, that's all… I just was, er, inawheelchairforabit."

        "The last few mumbled words are quickly deciphered by Emi's mother - I suspect she has experience with this sort of thing - and a worried frown appears on her face."

        show meiko worry
        with persistent.charachange

        emm "So that's why he kept dodging my calls…"

        emm "Oh Emi… I know how much you hate being in a wheelchair."

        emm "No wonder you've been in such a mood lately!"

        show emicas frown
        with persistent.charachange

        hi "Yeah, she's much happier on her feet, so to speak."

        show meiko serious
        show emicas awayfrown
        with persistent.charachange

        emm "Well of course! She spent enough time in a chair just after the accident."

        show emicas frown
        with persistent.charachange

        hi "She didn't get prosthetics immediately?"

        show meiko worry
        show emicas awayfrown
        with persistent.charachange

        emm "No, she had to finish healing up before they'd let her start the sort of therapy you've got to go through to adjust to those things."

        emm "Especially since she wanted to run on them."

        show emicas frown
        with persistent.charachange

        hi "I had no idea."

        show emicas weaksmile_up
        with persistent.charachange

        emi "Yeah, it sucked. Oh, did you see Rin's mural at the festival?"

        "Emi's sudden change of topic makes me realize belatedly that she's been fidgeting the whole time her mother and I have been talking."

        "I should have figured on her being a little skittish when it comes to talking about the accident. Even around her mother."

        show meiko serious
        with persistent.charachange

        emm "No, I didn't make it out to the festival, remember?"

        show meiko happy
        with persistent.charachange

        emm "Although I caught a glimpse of it at your track meet. It seemed pretty weird to me."

        show emicas closedsmile
        with persistent.charachange

        emi "I think that's more or less what she was going for. She talked a lot about it being dreamlike. Or trying to make it dreamlike."

        show meiko smile
        with persistent.charachange

        emm "Rin's art is one of those things I don't think I'll ever understand."

        show emicas wink
        with persistent.charachange

        emi "That's not surprising. I don't think Rin expects to be understood."

        show emicas grin
        with persistent.charachange

        emi "She told me once that art allows people to understand stuff they wouldn't understand otherwise, but all the same she doesn't think it actually works that way."

        "I'm surprised that Emi's talked about this with Rin extensively enough to actually have Rin's opinion, such as it is."

        "Although I expect that Rin could not, if she were so inclined, say the same thing about Emi's."

        "Unless, of course, Emi is purposely keeping me in the dark about everything; which is likely, but unpleasant to think about."

        "I drift down this unpleasant train of thought for a while, losing track of the conversation."

        show meiko serious
        with persistent.charachange

        emm "Hey Emi, I've been meaning to ask…"

        show emicas neutral
        with persistent.charachange

        emi "Huh?"

        show meiko worry
        with persistent.charachange

        emm "Are you going to visit your father this year?"

        stop music fadeout 3.0

        "From the way she says it, you'd think Emi's mother was talking about the weather. From the way Emi reacts, it's clearly not the weather they're talking about."

        show emicas awayfrown
        with persistent.charachange

        "She flinches, a slight jerk of the head backwards as if she's just been slapped in the face."

        show emicas sad
        with persistent.charachange

        emi "Can we talk about this later?"

        "Her voice sounds brittle, strained. It looks as if she's been severely shaken by the question."

        "It seems that Mrs. Ibarazaki misjudged just how close Emi and I are."

        "Some things, it seems, are best not conversed about with me around. Her father is one of these things."

        "The accident that took her legs is probably another one of those things, if her reaction to the earlier conversation between her mother and myself is any indication."

        "It doesn't take Emi's mother long to realize she's screwed up."

        show meiko happy
        with persistent.charachange

        emm "Of course we can, dear. I'm sorry to bring it up, I just wanted to ask so I could make plans—"

        show emicas neutral
        with persistent.charachange

        emi "It's fine. Don't worry about it."

        "Emi fidgets nervously, as if embarrassed by her own reaction. I confess that her reaction is confusing."

        "She only just mentioned her father to me earlier today! Less than a few hours ago, even!"

        "Why does a simple question about when she'll visit her father cause such a strong reaction?"

        "Unless whatever serenity she claimed to have reached by means of our talk the previous evening has suddenly evaporated."

        "Or it didn't help as much as she thought. Or claimed."

        show emicas weaksmile
        with persistent.charachange

        emi "I'll uh, be right back. Gotta visit the little girl's room."

        hide emicas
        with charaexit

        show bg at bgleft
        show meiko smile at center
        with charamovechangefaster

        "Emi gets up suddenly and leaves the table, leaving me and Mrs. Ibarazaki alone."

        "I'm a little conflicted. Should I go after her, or should I stay here?"

        "It's obvious that Emi's departure was not based on the call of nature. Something's bothering her, and I have to know what it is."

        if not have_a_minute and not _in_replay:
            $ talk_to_her_mom = False

            call a3ec4o1

        else:
            menu:
                with menueffect
                "How to go about it?"

                "Go after her.":
                    $ talk_to_her_mom = False

                    call a3ec4o1
                "Talk to her mom.":
                    $ talk_to_her_mom = True

                    call a3ec4o2

        if _in_replay:
            return

    if not have_a_minute or not talk_to_her_mom:
        call timeskip

        label .instant_replay:
            scene black
            with dissolve

            play sound sfx_alarmclock

            pause 2.0

            scene bg school_dormhisao
            with openeye

            "The morning alarm sounds and I roll over, switching it off. My eyes open blearily to stare at the ceiling."

            play music music_night fadein 1.0

            nvl clear
            nvl show dissolve

            n "{vspace=60}What am I going to do? Do I get out of bed, go down to the track, and pretend that nothing happened?"

            n "Will Emi even show up? After last evening's events, I doubt it."

            n "Even supposing that she did, what would I do then? Get over this fight just to dance the same routine the next time something's bothering her?"

            n "I know that I spoke hastily last evening, especially trying to use her father as leverage."

            n "But was anything I said really off the mark? She won't let me in, ever, and she'll be forced to suffer alone."

            n "Nothing I do, nothing I say is going to change that. She won't change, and she's already decided to keep me at arm's length."

            n "{vspace=30}Can I really bring myself to go down there and see her, knowing that I'm never going to get past where I am now?"

            nvl clear
            nvl hide dissolve

            scene black
            with shuteye

            "No, I decide. I really can't. Not today. I roll over and go back to sleep."

            "She probably won't be there anyway."

            scene bg school_cafeteria
            with shorttimeskip

            "A similar mental conversation repeats itself when it comes time to go to lunch, and I eat in the cafeteria, alone."

            "I don't want to see her; the very thought makes me feel ill."

            scene bg school_track_ni
            with shorttimeskip

            "That night, I go for a run; I'm solo for the first time since Emi got sick after the track meet."

            "Skipped seeing the nurse, just in case he asked about Emi."

            "I don't want to talk about her, either."

            scene bg school_hallway3
            with shorttimeskip

            "The next day, I do the same thing. Alarm, off. Stay in bed. Eat alone, run alone."

            "To fill the time that I would usually be spending with Emi, I start reading more."

            "It works surprisingly well, until I find myself ducking into a restroom because I see her walking down the hall in between classes."

            "If she noticed me, she didn't show it, even though I don't suppose she ever shows anything."

            "Certainly not to the girls from her class I see talking cheerfully to her."

            "Or to her fellow track members."

            "Especially not to me."

            "Alarm off. Stay in bed."

            scene bg school_scienceroom
            show muto normal at center
            with shorttimeskip

            "Mutou and I have a lengthy talk about the possibility that string theory is plausible. I don't buy it, myself."

            "More than four dimensions, I can buy. But a bunch of vibrating strings at the subatomic level? That's asking a bit much."

            "Looks like I'm not the only one to think this way, too. Apparently it's not really as strong a theory as it once was."

            "Mutou says that's just because nobody has found the right way of looking at the data yet."

            $ renpy.music.set_volume(0.3, 0.0, channel="ambient")
            play ambient sfx_rooftop

            scene bg school_roof
            with shorttimeskip

            "Eat alone."

            "The rooftop is deserted today. I briefly wonder where Emi and Rin are, but shrug off the question. The important thing is that they aren't here, so I won't have to talk to them."

            "Since I have nobody to talk to, I bring a book with me to read."

            "The weather's nicer, if getting a little hot."

            "Hopefully it will be cooler in the evening; a cool breeze seems to back up my theory."

            stop ambient fadeout 2.0

            scene bg school_track_on_ni
            with shorttimeskip

            "Run alone."

            "It is, in fact, cooler at the track. No sign of Emi, which is exactly the sort of thing I'm going for."

            "I stretch out and start on my usual run, trying hard to ignore the lack of a running partner in front of me."

            "Finding my thoughts drifting damnably to that girlish laugh, incorrigible grin, those wide and friendly eyes, her incredibly toned body—"

            scene bg school_track_running_ni
            with Dissolve(1.0)

            "I increase the pace to clear my head. Chew up the distance between me and the turns, find the speed that makes me think only of my legs and how much they burn."

            "I glance at my watch as I round the final turn, noting that my time's gotten faster."

            show bg school_track_on_ni
            with Dissolve(2.0)

            "My heart seems a little squirrelly tonight, so I give myself a few extra cool-down laps just to be safe."

            "No reason to bring this to the nurse's attention. I'll be fine. A rather Emi-ish thought to have, I'll admit."

            "I have to hope that eventually I'll stop thinking about her so much."

            scene bg school_dormhisao
            with shorttimeskip

            "I finish another book before going to bed that night. I'll have to stop by the library tomorrow."

            play sound sfx_switch

            show bg school_dormhisao_ni
            with Dissolve(0.2)

            pause 0.5

            $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
            stop music fadeout 3.5

            scene black
            with shuteye

            pause 2.0

            play sound sfx_alarmclock
            scene bg school_dormhisao
            with openeye

            "I don't know why I keep the early alarm on any more, but it wakes me up the next morning just the same. I still turn it off and go back to sleep."

            scene bg school_scienceroom
            show misha perky_smile at center
            with shorttimeskip

            play music music_pearly fadein 1.0

            "That afternoon, as I get ready to head to the cafeteria for another solo lunch (I've got a new book about a couple of con men in ancient Persia that I'm pretty excited about reading) I am suddenly cornered by Misha and…"

            "Huh. I guess just Misha."

            show misha hips_smile
            with persistent.charachange

            mi "Off to eat alone again, Hicchan~?"

            show misha sign_smile
            with persistent.charachange

            mi "We've noticed, you know~!"

            hi "We?"

            show misha hips_grin
            with persistent.charachange

            mi "Uh huh! Shicchan and I noticed that you've been spending more time alone!"

            show misha hips_smile
            with persistent.charachange

            mi "She wanted me to find out why, so I told her I'd ask you!"

            hi "I'm surprised she didn't ask me herself."

            show misha perky_smile
            with persistent.charachange

            mi "She would have, but she wanted to get a head start on some paperwork. There's a lot of it since we're coming up on the end of the term, you know~!"

            hi "Why the sudden interest in my well-being, anyway?"

            show misha sign_smile
            with persistent.charachange

            mi "Ah, Shicchan said 'It is the duty of the Student Council to keep track of the emotional health of its students! To allow a cons—constituent to spiral into depression unchecked would be an unforgivable failure in the council's duties!'"

            hi "Well, that's easy, then. I'm not depressed."

            show misha perky_confused
            with persistent.charachange

            mi "But you're eating alone, and nobody's seen you and Emi together at all! Something happened, didn't it, Hicchan~?"

            "Misha's voice takes on a slightly sterner tone, though somehow she keeps the familiar lilt at the end of her sentences."

            menu:
                with menueffect
                "I purse my lips, uncertain about how to respond."

                "Downplay the issue.":
                    $ let_misha_know = False

                    call a3ec5o1
                "Give in and let Misha know.":
                    $ let_misha_know = True

                    call a3ec5o2

            if _in_replay:
                return

    return

label a3ec1o1:
    hi "Are you absolutely sure?"

    hi "You don't want to go ahead and adjust it before heading up the stairs?"

    hi "You could get hurt if you don't, right?"

    show emicas awayfrown_up
    with persistent.charachange

    emi "I said it was fine, Hisao."

    show emicas frown
    with persistent.charachange

    emi "Seriously, don't worry about it."

    show emicas weaksmile
    with persistent.charachange

    emi "I've got some experience in these matters, after all."

    hi "Yeah, I suppose so."

    "Emi grins reassuringly."

    show emicas grin
    with persistent.charachange

    emi "Honestly, Hisao, I appreciate the concern but I really am okay."

    return

label a3ec1o2:
    "Well, she's probably fine."

    "I imagine she'd say something if it was really a problem."

    "Heck, she'd probably get annoyed if I kept bringing it up."

    return

label a3ec2o1:
    hi "Yeah, I've got some time. Nowhere important to be or anything like that."

    show muto normal
    with persistent.charachange

    "Mutou raises an eyebrow as if questioning my statement, then beckons me back into the classroom."

    hide muto
    with charaexit

    scene bg school_scienceroom
    with locationchange

    show muto normal at center
    with charaenter

    mu "I wanted to get some feedback from you, if I could."

    mu "I know that this course wasn't quite up to your level…"

    hi "Don't worry about it. The science club activities more than made up for it."

    show muto smile
    with persistent.charachange

    mu "Hmm, did they?"

    show muto normal
    with persistent.charachange

    mu "Well in fact, that's what I wanted to talk to you about."

    mu "Do you think that was a worthwhile activity? Just for my own reference."

    hi "Well yeah, it was a great way to go further than we did in class. It was definitely worthwhile."

    show muto smile
    with persistent.charachange

    "Mutou seems delighted by my response."

    mu "That's great! Exactly the sort of thing I was hoping for."

    mu "You know, Hisao, I'm glad you came here. It's always good to have a student who really gets into the subject you teach."

    mu "In a way, it makes dealing with the rest of the students more tolerable."

    mu "You're a bright kid, too. You took to this stuff like a duck to water, or some other such simile."

    hi "Er, thanks."

    hi "You were a great help. Especially with that college stuff."

    show muto normal
    with persistent.charachange

    mu "There's one more thing, Hisao."

    mu "A bit of advice, from one scientist to another."

    hi "What's that?"

    mu "What does a scientist do?"

    hi "Observe the world around him."

    show muto smile
    with persistent.charachange

    mu "Exactly. Good."

    show muto normal
    with persistent.charachange

    mu "A simple question, but one that most people can't seem to answer. That's the essence of a scientist, Hisao."

    mu "We observe what's there, and try to figure it out."

    mu "But what if there's something you can't figure out?"

    mu "What's a scientist to do if he can't observe something?"

    mu "How, for example, can we talk about quarks when nobody has ever actually seen one? Or black holes when observing them directly is impossible?"

    hi "Well, scientific equipment's pretty advanced…"

    show muto irritated
    with persistent.charachange

    "Mutou irritably waves away my response."

    mu "No, that's not it at all."

    mu "Those are tools, I'm trying to give you a philosophy."

    show muto normal
    with persistent.charachange

    mu "Think. If you can't observe something directly, then how can you observe it?"

    hi "Uh, guess?"

    mu "How? How would you guess the movement of a quark? What is your guess based on?"

    "Of course."

    "I should have thought of it earlier."

    hi "The things it affects."

    show muto smile
    with persistent.charachange

    "Mutou claps his hands together excitedly and whoops."

    mu "Yes, exactly. Good."

    mu "Remember that, Hisao."

    show muto normal
    with persistent.charachange

    mu "If you can't examine something directly, it's because you're looking at it wrong."

    mu "You have to look at it differently if you want to uncover the truth. And if it eludes you, then look at what it leaves behind."

    mu "That is the essence of being a scientist. We never stop looking for the answer. Never take anything for granted."

    mu "Observe, experiment, and observe some more."

    mu "There's a lot of stuff out there that makes no sense, Hisao. Your job is to get it to make sense."

    mu "If nothing else, I hope you've learned that here."

    hi "I think I can remember that."

    show muto smile
    with persistent.charachange

    "Mutou smiles, satisfied."

    mu "Good. Now go enjoy your time off. You've earned it."

    stop music fadeout 8.0

    scene bg school_hallway3
    with locationchange

    "I leave the room feeling a little confused."

    "What brought that on?"

    "Although…"

    "Am I going about this thing with Emi the wrong way?"

    "If she won't tell me, then can I go about it some other way?"

    return

label a3ec2o2:

    hi "Actually, I've got something I need to do…"

    show muto normal
    with persistent.charachange

    mu "Yeah? Oh well."

    mu "I wanted to get some feedback on the science club from you. But we can do that later, I guess."

    mu "Enjoy your break, you hear?"

    hi "Thanks, I will."

    "I'd really love to chat with Mutou, but I've got other things on my mind."

    "Specifically, what to do about Emi."

    "Can I really just confront her?"

    return

label a3ec3o1:
    "What was it Mutou said yesterday?"

    "If you can't observe the thing, then observe what's around it?"

    "Worth a shot."

    "The nurse knows Emi better than I do, I'll wager."

    hi "Sure, I'm open to suggestions."

    hi "Honestly, I'm kind of lost."

    hi "I've got no idea how to deal with this."

    show nurse grin
    with persistent.charachange

    nk "I never would have guessed."

    "He grins while he says this. I think he's kidding."

    show nurse neutral
    with persistent.charachange

    nk "Look, here's the deal: Emi is… stubborn."

    show nurse grin
    with persistent.charachange

    nk "You should know that by now, and if you don't then you're pretty unobservant, but I'm giving you the benefit of the doubt here."

    hi "I'm so grateful."

    show nurse neutral
    with persistent.charachange

    nk "Anyway, if she's decided that she doesn't want to talk about what happened, then she's not going to talk about what's happened."

    nk "Has she said anything about what's been bothering her? Even a hint?"

    hi "Well, she did say she'd been having nightmares about the accident…"

    show nurse fabulous
    with persistent.charachange

    nk "Really? You're making progress, then. That's good."

    show nurse neutral
    with persistent.charachange

    nk "Well, I guess I can fill you in on this without violating my strict non-interference policy when it comes to Emi making stupid decisions."

    show nurse concern
    with persistent.charachange

    nk "The anniversary of her accident is coming up soon."

    nk "She gets depressed around this time, because it was a pretty traumatic event, considering what she lost."

    hi "That's the other thing. She acted like she lost more than just her legs. What happened?"

    show nurse fabulous
    with persistent.charachange

    nk "Whoa! Nope, not going there. You'll have to ask someone else about that, because that's a whole can of worms I'm not about to open."

    show nurse neutral
    with persistent.charachange

    nk "If Emi wants you to know, she'll tell you in her own time."

    nk "You've just got to be patient, that's all."

    hi "Why are you even helping me with all this?"

    show nurse grin
    with persistent.charachange

    nk "Because you're good for her. She trusts you, even if you don't think she does."

    nk "And you've got the best chance out of anyone at this school right now to help her through this time of year."

    show nurse neutral
    with persistent.charachange

    nk "She won't accept my help, but she might accept yours if you don't screw it up."

    show nurse fabulous
    with persistent.charachange

    nk "So don't screw it up, got it?"

    return

label a3ec3o2:

    "Advice? About what? I don't think there's anything I can actually do about this."

    hi "Not really. I don't think there's anything you can say that'll help."

    show nurse neutral
    with persistent.charachange

    nk "You never know, Hisao."

    hi "No, I think I've got a pretty good idea."

    hi "Emi's just being stubborn about some things, and it's bothering me, but I'll get over it."

    hi "Don't worry about us."

    show nurse concern
    with persistent.charachange

    "The nurse doesn't seem to believe me, but shrugs."

    nk "Have it your way, kiddo."

    return

label a3ec4o1:
    "The only way to find out is to go to the source. And the source is currently pretending that she has to use the toilet."

    scene bg emi_kitchen
    with locationchange

    "I excuse myself politely from the table and head that way, only to catch sight of Emi not in the bathroom, but in the kitchen just next to the living room."

    show emicas sad at center
    with charaenter

    "Emi's left the door open, and as I approach I can see that she's holding on to the table in an attempt to compose herself, an effort that fails as soon as I open my mouth."

    hi "Doesn't look like nature's call was that urgent."

    show emicas angry
    with persistent.charachange

    "Emi jumps and glares at me."

    show emicas angry_up
    with persistent.charachange

    emi "What are you doing here? I didn't come here to be with other people."

    hi "I just wanted to help you. You looked pretty rattled."

    show emicas awayfrown
    with persistent.charachange

    emi "I said it was nothing, didn't I? And besides, I thought we'd established that you can't help me."

    hi "No, we've established that you're stubborn."

    show emicas angry
    with persistent.charachange

    emi "Look who's talking. The guy who followed me."

    hi "This is different! I want to help you with… whatever this is."

    show emicas awayfrown
    with persistent.charachange

    emi "Funny, because {b}I{/b} just want you to leave me alone."

    hi "But why? Why can't you just trust me?"

    show emicas frown
    with persistent.charachange

    emi "We've been over this already, Hisao. I've got to deal with this stuff on my own."

    hi "I won't accept that! You need my help, you just won't take it!"

    "My wording seems to have been a little off."

    show emicas angry
    with persistent.charachange

    emi "Need? I {b}need{/b} your help?"

    play music music_tragic fadein 0.5

    show emicas angry_up
    with persistent.charachange

    emi "Well, it's a good thing we met, isn't it? Because otherwise I guess I'd just be a broken human being, wouldn't I?"

    emi "No, it's a damn good thing that Hisao came along to save the day, isn't it? Because God knows I can't save myself, can I?"

    emi "I'm just the poor, emotionally damaged girl with no legs, right?"

    hi "Emi, you know I don't think that—"

    show emicas angry
    with persistent.charachange

    emi "Really? Because if you thought differently then I don't think you'd be here, saying I need your help."

    emi "I've gotten pretty far in life as a normal human being without you."

    hi "So what, nothing we've shared was important? I'm just the guy who hangs out with you?"

    show emicas awayfrown
    with persistent.charachange

    emi "You're my boyfriend, Hisao, not my savior."

    hi "Well no, that much is obvious. You won't even consider that I could be a help to you, will you?"

    hi "You'll just bottle it all up and hope that a run will solve your problems, or you'll come visit me and we'll fool around until you feel better."

    hi "That's not being a healthy human being, Emi. That's not what a relationship means."

    show emicas frown
    with persistent.charachange

    emi "Well it's what it means to me right now, Hisao."

    show emicas sad
    with persistent.charachange

    emi "I wish—"

    "She seems to reconsider her words just then. A flicker of pain, of doubt on her face. For a moment I think she's about to cry."

    show emicas frown
    with persistent.charachange

    "But the moment passes, and now she's composed herself again. Whatever that wish was will have to go unspoken."

    emi "Look, I just… I can't do this right now."

    hi "What, have a serious conversation? Be open? Be honest? Give a damn about anyone besides yourself and your problems?"

    show emicas angry_up
    with persistent.charachange

    emi "What do you know about my problems? Nothing! You don't know what I've been through, so don't pretend that you do."

    hi "I know you have nightmares, and I know your father's gone. What happened to him?"

    show emicas sad_up
    with persistent.charachange

    "Emi's head jerks backwards as if I've just slapped her. That brittle quality has gotten back into her voice."

    show emicas sad
    with persistent.charachange

    emi "That's enough."

    "This is stupid. This whole conversation has just been variations on Emi stonewalling me."

    hi "What, you won't even answer that question? Fine, keep your secrets. They can lie in the grave as far as I'm concerned."

    show emicas blush
    with persistent.charachange

    "Emi's eyes widen in shock. When she speaks again, it's in a voice that is low, dangerous."

    show emicas grit
    with persistent.charachange

    emi "Get out of my house, Hisao."

    "The sudden change in her tone snaps me out of my self-righteous anger and makes me realize with a dawning horror what I've just said."

    hi "Emi, I didn't mean—"

    stop music fadeout 2.0

    show emicas angry
    with persistent.charachange

    emi "I said {b}go{/b}, Hisao."

    emi "Tell my mother that she cooked a wonderful meal but you've forgotten a prior engagement, and get out of my house."

    "She's trembling now, shaking with anger, or sadness, or determination. Her voice is still low, controlled. Almost a growl."

    "I reach out to put an arm on her shoulder, to apologize for going too far, but she jerks away from my touch."

    show emicas angry_up
    with persistent.charachange

    emi "Get out."

    scene bg emi_dining at bgleft
    show meiko serious at center
    with locationchange

    "What can I do? I walk out of the kitchen and go to the living room, make my apology to Mrs. Ibarazaki, and let myself out."

    scene black
    with dissolve

    return

label a3ec4o2:
    "There's an awkward silence at the table for a while after Emi dashes off. I can't think of anything to say."

    show meiko serious
    with persistent.charachange

    "Emi's mother sighs, breaking the silence."

    play music music_moonlight fadein 5.0

    emm "Sorry about that, Hisao. I sometimes forget that Emi's touchy about certain subjects."

    emm "And I was talking about the wheelchair thing, too…"

    hi "Should I go after her?"

    show meiko worry
    with persistent.charachange

    emm "Heavens no! She didn't leave the table to continue the conversation, you know."

    hi "But if she's troubled, shouldn't someone help her?"

    show meiko serious
    with persistent.charachange

    emm "If it were anyone else, I'd say yes. But my daughter is stubborn as a mule, and if she wants to be alone it's best to let her be alone."

    emm "Otherwise she'll probably say something she'd regret, which would cause you to say something you'd regret, and I would prefer that dinner doesn't end with one or the both of you storming out of the house."

    show meiko happy
    with persistent.charachange

    emm "If that were to happen I'd be a terrible hostess, wouldn't I? I've already acted as a fool once today."

    hi "That's okay, I shouldn't have brought up the wheelchair, apparently."

    show meiko serious
    with persistent.charachange

    "Mrs. Ibarazaki frowns, clearly more bothered by Emi's omission than she'd let on."

    emm "I wish she wouldn't do that. It just makes me worry more, you know."

    hi "She does this often?"

    show meiko smile
    with persistent.charachange

    emm "What, running off to the bathroom? No, I can't say she does. Keep injuries from her mother, though? Well, that's a little more common."

    emm "Every time I catch her lying like that, she assures me that the only reason she didn't tell me is because it wasn't a big deal."

    hi "If it's any consolation, I'm sure the only reason I knew about it at all was because I saw her every day."

    show meiko happy
    with persistent.charachange

    "This elicits a dry chuckle from across the table. Mrs. Ibarazaki sighs, a little sadly."

    show meiko smile
    with persistent.charachange

    emm "Still hesitant about getting close to people, huh? I keep hoping that she'll get over that."

    emm "It's funny, really. She's bounced back so well from the accident in so many ways…"

    show meiko serious
    with persistent.charachange

    emm "I guess some things never really go away."

    "From the looks of it, the whole thing still bothers her, too."

    "She seems to be a little more willing to talk about the accident without Emi around, though."

    hi "Hey, I've got a question, if it's all right."

    show meiko smile
    with persistent.charachange

    emm "Oh?"

    hi "What else did Emi lose in that accident? The nurse said that she gets this way near the anniversary, and she won't talk about it to me…"

    show meiko happy
    with persistent.charachange

    emm "So you thought I'd fill you in, hmm?"

    hi "Er, yeah. Hopefully."

    show meiko serious
    with persistent.charachange

    emm "Well, there's a problem with that request, you know."

    hi "Let me guess: you promised Emi that you wouldn't tell anyone she didn't want to know, and you don't know if she wants me to know?"

    emm "Something like that. I promised Emi that she'd be the one to tell people the full story."

    hi "But isn't that important? I mean, it's clearly had a huge effect on her if she's still like this so long after the accident happened."

    show meiko worry
    with persistent.charachange

    emm "That's true. It did have a long-lasting effect on her. There are a few things that she'll probably never really get over."

    "For a moment Mrs. Ibarazaki looks incredibly saddened, as if an old wound is bothering her."

    emm "I suppose there are a few things I'll never really get over either…"

    show meiko happy
    with persistent.charachange

    "Another dry chuckle, and with a shake of her head Emi's mother banishes the memory."

    show meiko smile
    with persistent.charachange

    emm "Look, there's something you absolutely must understand about the way Emi thinks about the accident."

    hi "What's that?"

    emm "It wasn't a big deal."

    stop music fadeout 1.0

    "Somehow I manage to keep my mouth from falling open in surprise, but it takes some effort."

    "That has to be the most ridiculous thing I've ever heard."

    hi "I beg your pardon?"

    play music music_sadness fadein 3.0

    show meiko serious
    with persistent.charachange

    emm "Okay, maybe it's not that simple, but it's a pretty accurate summation. Emi believes that the accident did not define her, and that everything she lost that day didn't define her either."

    emm "She's not 'that girl who lost her legs,' she's 'The Fastest Thing on No Legs.' Her optimism and energy came out of that wreck without a scratch, as far as she's concerned."

    hi "Yet it goes beyond that, doesn't it? I mean, last night she told me that she refused to rely on me because it would make losing me too painful."

    show meiko smile
    with persistent.charachange

    emm "Not really. You said she won't tell you about the accident, even though you've asked her about it before."

    emm "The reason she won't talk about it when you ask is because to her it's not something you absolutely need to know. Even if she wasn't terrified of getting too close to anyone, she still wouldn't talk about it."

    hi "She's afraid of being close to me?"

    show meiko happy
    with persistent.charachange

    emm "Oh goodness me, yes. For all that talk about being unscathed by the accident, she's gained the ugly knowledge of how quickly it can all be over."

    show meiko smile
    with persistent.charachange

    emm "So she's not going to let people get especially close to her, and she certainly would resent any implication that she cannot work through this on her own."

    hi "But I don't think she {b}can{/b}."

    show meiko serious
    with persistent.charachange

    emm "Oh no? Are you sure you've been dating my daughter and not somebody else? Trust me Hisao, she could get through it on her own."

    hi "But she has nightmares, and can't sleep well, and—"

    show meiko smile
    with persistent.charachange

    emm "And she does this every year. Tell me, if she wasn't able to get through it on her own, do you really think she'd still be alive? She would've killed herself, or something equally melodramatic."

    hi "So what, I shouldn't try to help her?"

    show meiko serious
    with persistent.charachange

    emm "I didn't say that! I hate seeing my daughter like this, and knowing that she could rely on someone else would let me relax."

    emm "You just need to understand that accepting help goes against everything Emi thinks about herself and the way the world works."

    emm "If you still want to offer her help, then I guess that's your call. Honestly, I'd like you to, but it'd be silly not to warn you that it's not going to be easy."

    show meiko smile
    with persistent.charachange

    emm "You just need to be patient with her. She's already closer to you than anyone else she's ever met at Yamaku."

    hi "Well it sure doesn't feel like we're very close."

    show bg at center
    show meiko serious at tworight
    with charamovechangefaster

    show emicas evil at twoleft
    with charaenter

    stop music fadeout 0.3

    emi "Good, that makes this part easier."

    "Emi's voice nearly gives me a heart attack."

    hi "Whoa! Didn't hear you come back, Emi."

    show emicas angry
    with persistent.charachange

    emi "How convenient."

    hi "Wait, were you eavesdropping?"

    show emicas angry_up
    with persistent.charachange

    emi "Nope. Just happened to come back at the right moment, I guess."

    show meiko worry
    with persistent.charachange

    emm "Emi, Hisao was just—"

    "Emi holds up a finger, cutting her mother off."

    show emicas grit
    with persistent.charachange

    emi "On his way out of the house? Yeah, I know."

    "Emi's trembling with anger now, looking vaguely betrayed."

    emm "Emi, don't be ridiculous, we were just—"

    show emicas angry_up
    with persistent.charachange

    emi "You {b}promised{/b}!"

    play music music_rain fadein 0.5

    "The pain carried in that last word is almost too much for me to bear. The idea that I could hurt her that much is like being kicked in the gut."

    "Emi's mother looks similarly pained by the thought."

    emm "And I kept that promise! Just listen, there's no reason to go throwing people out of the house."

    "Emi's mother seems to be both angry at her daughter's outburst and embarrassed that I'm a witness to it."

    "There's only one real solution to this problem, I think."

    hi "It's okay. I'll go."

    emm "Now really, that seems a little unnecessary…"

    hi "Don't worry about it. Thank you for dinner, Mrs. Ibarazaki, and for the advice."

    show meiko serious
    with persistent.charachange

    emm "It was my pleasure, Hisao. I'm sorry we didn't get to the dessert."

    hi "That's okay. I have to watch what I eat anyway."

    hi "Good evening, Emi, Mrs. Ibarazaki."

    "The formality of our conversation, coupled with the fact that I'm getting ready to leave, seems to snap Emi out of her anger."

    show emicas frown
    with persistent.charachange

    emi "No, wait. I'm sorry, I've been so… and after last night I just thought… You don't have to go, I take it back, it's okay—"

    "I can't help but smile slightly. She can barely articulate her apology, and I really would like to stay…"

    "But I don't think I can, right now. I need to think about what her mother said, and about what I'm going to do about us."

    "I don't want to risk accidentally getting Emi angry again in her current state, either."

    hi "No, I think I'd better leave. You seem pretty shook up, and, well, I'd only wind up trying to help you again. I know you'd prefer I didn't, so I'm going to leave instead."

    show emicas sad
    with persistent.charachange

    emi "But—"

    hi "Hey, it's not a problem. You don't want a knight on a white charger, right? Just promise me one thing, okay?"

    show emicas frown
    with persistent.charachange

    emi "What?"

    hi "Don't be angry at your mom, okay? She was just giving me some advice, that's all."

    show emicas sad
    with persistent.charachange

    "Emi nods, hesitantly, like this simple idea is all that she can grab on to at this point. She's so terribly off-balance, but I can't do anything about that right now."

    emi "Okay."

    hi "See you tomorrow, okay? Running in the morning. Don't forget!"

    "I can see that I've hurt Emi by deciding to leave. But there's nothing I can do for her as things stand, and I know that she's too stubborn to admit that she wants me to stick around."

    "I watch various emotions cross Emi's face as she tries to process everything that's just happened."

    show emicas weaksmile
    with persistent.charachange

    "Shortly comes that calm look again, like last night, and that voice that tries so hard to sound careless."

    emi "Sure, Hisao. See you around."

    "Both of us are unwilling to concede emotion at this point, and I'm having a hard time keeping up my facade, so I turn on my heel and walk out the door."

    stop music fadeout 7.0

    scene bg emi_houseext
    with locationskip

    "I shut it behind me slowly, pausing for a moment as the latch catches, my hand on the doorknob."

    "Did I make the right decision just now? Should I have stayed and tried to work things out?"

    "No, I decide. Not in front of her mother like that. In spite of everything, I'd rather keep Emi's mother insulated from the sort of anger that surfaced last night."

    "Even though she's probably used to it, some protective instinct wants me to keep Emi's image as a cheerful girl intact."

    "With a start, I realize my hand is still resting on the knob. I take my hand away, put it in my pocket, and head down the slowly darkening street."

    scene bg school_dormhisao
    with shorttimeskip

    play music music_pearly fadein 1.0

    "I let out a long breath."

    "The wait until tomorrow morning comes isn't going to be easy."

    "In any case, I have to think on what to say to Emi. I must apologize, and I must get through to her somehow."

    "On that account, something has been on my mind for most of the way back to my room."

    "The letter of apology from Iwanako."

    "I was so concerned about my new life when I received it that I didn't even bother to really read it."

    "Now that I find myself in a similar position, my curiosity got rekindled. What did she want to let me know so badly?"

    "If nothing else, reading her thoughts might help me frame mine."

    "I remember tossing it away. Damn, where did I throw that thing?"

    "I check under my desk. That turns up nothing, so I look for harder-to-reach, more unlikely locations."

    "…"

    "Well, now I know where that lost sock went, at least."

    "Still no letter, though."

    "It's when I try sweeping my arm under my nightstand that I feel something crinkly jammed between it and the wall."

    "Grunting a little with the effort, I reach for my prize and soon manage to bring it into the light."

    "Bingo."

    play sound sfx_paper

    scene ev hisao_letter_open_2
    with locationchange

    "I sit at my desk and spread the crumpled paper open. A flick turns on the table light."

    "Skipping past the empty pleasantries, I look for the point where I stopped reading. Ah, here it is."

    call screen written_note(_("There are other things I want to say. I'm writing to you because I felt that there are things I should've said after the incident back in winter. I really regret that I wasn't able to say them in person, and I have no excuse for it.{vspace=150}"))

    call screen written_note(_("The truth is, the times when I visited you at the hospital made me worried about you. I am not talking about your health. You seemed to become more distant and disheartened. It was natural after something like that happened, I'm sure, but somehow I got the feeling that you had given up on something back then. Happiness, maybe?{vspace=30}"))

    "Giving up on happiness…"

    "This sounds unpleasantly familiar."

    call screen written_note(_("I wanted to somehow express my feelings, but the right words didn't come to me. I couldn't say anything to comfort you. I am really sorry for not being able to support you when it mattered the most, even though I like you so much. At least now, finally, I can be more honest.{vspace=120}"))

    call screen written_note(_("If I could go back to those quiet days in February and March, I'd tell you to not give up on yourself. That's what I would say. Maybe you wouldn't have drifted so far away if I had just said something. I hope you've managed to get back on your feet on your own.{vspace=120}"))

    call screen written_note(_("Now that the distance between us is also physical, it also feels more final, somehow. I wonder if we will meet again. Perhaps it's for the best if we don't? Still, if you would like to correspond with me, by all means write me back. I'd very much like to hear about your new school and how you are doing. I wish you all the best.\n\nSincerely, Iwanako"))

    "After finishing reading the letter I smooth it out carefully and set it aside on my desk."

    $ renpy.music.set_volume(0.5, 1.0, channel="music")

    nvl clear
    nvl show dissolve

    n "{vspace=90}Thank you, Iwanako. I wanted to answer 'yes' to your question on that snowy winter day, but I never got to."

    n "By the time we met again, it was too late."

    n "Or so I thought. What would have happened if I had behaved differently, back in that dismally sterile hospital room?"

    n "I'm sorry. There's no point in wondering now, but there's no point in trying to forget either."

    n "I am who I am because of all that happened to me and all I look forward to experience. Present, future, and past."

    stop music fadeout 2.0

    n "{vspace=60}And the past may just have taught me an important lesson now."

    $ renpy.music.set_volume(1.0, 2.0, channel="music")

    nvl clear
    nvl hide dissolve

    return

label a3ec5o1:
    "I'm not sure I like the idea of airing private matters to the Student Council."

    hi "Nothing major."

    show misha cross_frown
    with persistent.charachange

    mi "Hicchan, lying is a terrible thing to do~!"

    "She's not buying it."

    "Okay, give her something, but not too much."

    hi "We had a disagreement and haven't resolved it yet."

    show misha perky_confused
    with persistent.charachange

    mi "Oh? Why not?"

    hi "Because - look, I don't need to talk about this, okay?"

    hi "It's not a big deal, okay? I'm fine."

    show misha perky_sad
    with persistent.charachange

    mi "And Emi? Is she fine too, Hicchan?"

    stop music fadeout 4.0

    "Misha's voice has taken on a decidedly serious edge. This is ridiculous."

    hi "I don't know, okay? I haven't asked. Things are complicated right now."

    show misha hips_frown
    with persistent.charachange

    mi "What kind of man are you? Things get a little rough and you're going to hide from them?"

    play music music_rain fadein 4.0

    "Misha's sudden retort catches me completely off guard."

    show misha cross_frown
    with persistent.charachange

    mi "Shicchan would call that a cowardly act, and she'd be right too!"

    mi "You two were close! Happy together! And you're just going to roll over and die without a fight?"

    mi "You should be willing to fight for your girlfriend, Hisao!"

    "It seems that Misha is channeling Shizune at the moment. It wouldn't surprise me to find out that Shizune gave her a script to follow based on my answer."

    "Misha points an imperious arm at the classroom door."

    show misha sign_smile
    with persistent.charachange

    mi "Now you get out of the classroom and patch things up!"

    hi "Um, we've still got afternoon classes…"

    "This doesn't seem to dissuade Misha."

    show misha hips_smile
    with persistent.charachange

    mi "Then after class! You'd better do it, Hicchan! It's important that you don't leave things like this!"

    hi "Why?"

    show misha cross_frown
    with persistent.charachange

    "Misha regards me as one would regard an animal's droppings."

    mi "Didn't you care about her, Hisao? That's important, isn't it?"

    "Huh. She's right."

    "I did… I do care about her."

    "Don't I?"

    hi "Okay. I'll see her after class."

    show misha hips_grin
    with persistent.charachange

    mi "Great~! I'll let Shicchan know you're okay, then~!"

    "The lilt returns. I guess that means that Misha isn't angry at me any more."

    hide misha
    with charaexit

    "She waves and disappears down the hallway, and I eat my lunch."

    scene bg school_scienceroom
    with shorttimeskip

    "While afternoon classes draw to a close, I prepare myself for the task ahead."

    "I have to see Emi; Misha was at least correct about that. Leaving the question of Emi and me an open issue won't work."

    "At the very least, I need to apologize for what I said."

    "I consider going to her room to find her, but she's probably still at the track."

    scene bg school_courtyard
    with locationskip

    "The steps out of the main building and down the path to the track make me feel like a doomed man."

    "I have a twisting, horrible feeling in my gut that this is all going to go horribly wrong, that I'm not going to accomplish anything."

    "Except for maybe driving the final nail in the coffin of whatever it was Emi and I had."

    stop music fadeout 2.0

    scene bg school_track
    with locationskip

    "There she is, just as expected, running laps around the track after everyone else has gone to shower and dinner."

    "I don't wave, or even make my presence known. I just sit down on the bleachers and watch her run her laps."

    show emi basic_confused_gym:
        center
        xpos 0.6
        easein 0.5 center
    with charaenter

    show emi at center

    "It takes her a few trips around the track before she notices me, after which she skids to a stop, eyes wide in surprise."

    show emi basic_annoyed_gym
    with charachangealways

    show emi basic_grin_gym
    with charachangealways

    "Surprise is quickly masked by anger, which in turn fades behind a mask that I already know is impenetrable."

    emi "What are you doing here?"

    "Not quite the response I'd hoped for, but at this point I don't have much of a choice."

    hi "I wanted to apologize for what I said the other day."

    show emi basic_confused_gym
    with persistent.charachange

    emi "The other day?"

    show emi basic_closedgrin_gym
    with persistent.charachange

    "She laughs, a curt exclamation of disbelief."

    play music music_sadness fadein 0.5

    show emi basic_grin_gym
    with persistent.charachange

    emi "It's been almost a week, Hisao."

    hi "Yeah, well… better late than never, right?"

    show emi sad_annoyed_gym
    with persistent.charachange

    "Emi crosses her arms and stares at me coolly, as if sizing me up. Finally, she nods."

    show emi sad_grin_gym
    with persistent.charachange

    emi "Hmmph. I suppose you're right. Water under the bridge, then. I forgive you."

    show emi basic_grin_gym
    with persistent.charachange

    emi "Is that all?"

    show emi:
        easeout 0.5 xpos 0.3 alpha 0.0

    pause 0.5

    hide emi

    "Her almost impatient question catches me so off-guard that she's halfway down the track before I think to shout after her."

    hi "No, wait!"

    show emi basic_annoyed_gym:
        center
        xpos 0.4
        easein 0.5 center
    with charaenter

    show emi at center

    "Emi stops, turns, and walks back to me, breathing a little heavily and looking annoyed at my interruption."

    emi "What?"

    "Okay, I need to make this right, somehow. I have to know where I stand, maybe patch things up."

    hi "Can you at least sit down?"

    show emi sad_annoyed_gym
    with persistent.charachange

    emi "I think we're okay talking here."

    hi "Fine, sure. Look, about us…"

    "I pause, trying to think of a good way to phrase what I'm about to say."

    "But before I can launch into an impassioned plea for giving me another chance, Emi's already spoken."

    show emi sad_shy_gym
    with persistent.charachange

    emi "There's no more us, Hisao."

    hi "Why not?"

    show emi sad_pout_gym
    with persistent.charachange

    emi "We're just not right for each other."

    "She delivers this outrageous statement without even looking in my eyes."

    hi "I don't believe you! We're great with one another!"

    show emi basic_annoyed_gym
    with persistent.charachange

    emi "Says the guy apologizing for getting thrown out of my house last week."

    hi "It was a fight! I said something really, incredibly stupid and apologized for it!"

    show emi sad_angry_gym
    with persistent.charachange

    emi "And how many times had we already discussed the problem that started the fight? How many times had I told you that there was a set boundary that I wouldn't cross, and how many times did you keep trying to cross it?"

    hi "Because your boundary was stupid!"

    show emi sad_annoyed_gym
    with persistent.charachange

    "Emi rolls her eyes, folds her arm across her chest, and cocks her head to the side."

    emi "Do you see this, Hisao? This is why we're not right for one another!"

    "Her voice softens a little, and she reaches out to stroke my cheek."

    show emi sad_grin_gym_close
    with characlose

    emi "You're a good guy, but we're not going to work."

    "With a horrible lurching feeling, I realize that she's been practicing this. Maybe every day since I left her house."

    "Even the cheek-stroke seems rehearsed, like something out of a movie."

    "She never intended to give me another chance."

    "Hell, she probably would have been fine with never seeing me again."

    hi "So that's it, then? Nothing else to say but 'Gee, it was fun while it lasted, but so long?'"

    show emi basic_closedgrin_gym_close
    with persistent.charachange

    "This actually seems to amuse Emi far more than I wanted it to. She gives a rather morbid sounding chuckle."

    emi "That's how I've lived my life, Hisao. You should know that by now."

    show emi sad_grin_gym_close
    with persistent.charachange

    emi "And it was fun."

    "A sad smile. She shivers slightly, and the smile vanishes."

    show emi sad_shy_gym_close
    with persistent.charachange

    emi "But it's over now. It's for the best."

    "I want to yell, to scream at her. Make her see reason, that this is stupid, the whole act. That she's just afraid of me, afraid of what being close to someone means."

    "I want to tell her that I love her and that I can't just give up on her at the drop of a hat."

    "Except… there's no point. She's made up her mind. We're done."

    hi "Fine."

    show emi sad_grin_gym_close
    with persistent.charachange

    "Emi nods, satisfied. I want to hit something."

    emi "Good."

    show emi basic_grin_gym_close
    with persistent.charachange

    "She brightens with a false cheeriness."

    emi "See you around, Hisao."

    hi "No you won't. You won't even try."

    show emi basic_grin_gym_close:
        easeout 0.5 xpos 0.3 alpha 0.0

    pause 0.5

    hide emi

    "She shrugs, as if to say 'Have it your way,' and turns her back on me once more, quickly accelerating around the curve of the track."

    "I feel numb. This is it. The end of the road for us, whatever that was. Closure, at least."

    "Emi rounds the track again without sparing me a second glance. She's running much faster now, and I can't help but think of that first run together."

    "I ran to catch you, to try to prove I wasn't as weak as I knew I was. But it ended badly for me, didn't it?"

    "And now, you're off running too fast for me again, and I have the choice to run after you again."

    "But I won't. Not this time. You'd never let me catch you."

    stop music fadeout 6.0

    scene bg school_dormhisao
    with shorttimeskip

    "I don't even notice walking away from the track, or walking into my room, or pulling a book out of my bag to read."

    "Just before bed, I reset my alarm. Emi and I have had our final encounter."

    scene black
    with shuteye

    "We don't speak again after that."

    $ ach("emibad_achieve")

    return

label a3ec5o2:
    "Well, I suppose someone else knowing about my problem can't hurt. Heck, maybe Misha can even offer some advice."

    hi "We had a fight at her house."

    hi "I keep trying to get close to her, and she won't let me get close, and…"

    hi "I said something stupid, and she threw me out."

    show misha perky_sad
    with persistent.charachange

    mi "Have you talked to her since then?"

    "Misha looks genuinely concerned. I'm surprised, as I'd almost expected her to drop the subject after finding out what the trouble was."

    "Even more surprising is how quickly I find myself spilling my guts to her."

    hi "No, I haven't. I just can't bring myself to face her after that."

    hi "I made a complete fool of myself, and she probably hates me now anyway. Especially since I haven't seen her since then."

    show misha sign_smile
    with persistent.charachange

    mi "You're pretty slow, Hicchan."

    stop music fadeout 4.0

    "This doesn't sound like advice."

    hi "Huh?"

    show misha hips_frown
    with persistent.charachange

    "Misha places her hands on her hips and launches into a speech that would sound more plausible coming from Shizune."

    mi "The solution to your problem is simple! You have to go and apologize to her! Leaving things like this will just make things worse!"

    mi "You can't know that she hates you now unless she tells you! Otherwise, there's no evidence that what you fear is true!"

    mi "And if you really care about her, shouldn't you be worried about how she's taking all this?"

    play music music_innocence fadein 1.0

    "With a sudden start, I realize that she's right. I've kept waking up to an early alarm because part of me wants to meet Emi at the track for our runs."

    "I've kept running, because I know that Emi would worry about me if I didn't stay healthy."

    "When I went on the roof yesterday, I was half-hoping that she would be up there, and felt disappointed when she wasn't."

    hi "I'm an idiot."

    show misha hips_grin
    with persistent.charachange

    mi "Kinda, Hicchan~!"

    show misha sign_smile
    with persistent.charachange

    mi "So~! Go and apologize to her as soon as you can, okay~?"

    "I open my mouth to say that I'll do it right away, but the lunch bell rings and I realize that I still have afternoon classes to attend."

    hi "First thing after class is over, I'll go see her. I promise."

    hi "And uh, thanks for the advice, I guess."

    show misha hips_grin
    with persistent.charachange

    "Misha beams at me, as if I were a child that had just learned his ABCs."

    mi "Good! I'll let Shicchan know that you're okay, then~!"

    hi "Er, yeah. You do that."

    hide misha
    with charaexit

    "With a wave (and completely disregarding the fact that people are starting to trickle back into the classroom, as opposed to out of it), Misha departs the classroom."

    "I suppose she and Shizune have student council business again."

    scene bg school_scienceroom
    with shorttimeskip

    "While the afternoon wears on, I find myself impatient for lessons to end. I need to see Emi now."

    "I have to try to set things right. Even if Emi hates me now, I have to at least apologize."

    "I owe her that much."

    "Should I meet her in her room? No, I decide, it would delay things too much. If I know Emi, then I can find her at the track."

    "Still have no idea what I'm going to say when I get there, but I take comfort in knowing that Emi probably wouldn't have a plan for something like this either."

    "Play it by ear. Stop being nervous, and just get to the track. Figure the rest out when I get there."

    scene bg school_track
    with shorttimeskip

    "The track looms ahead, and another jolt of nerves hits me in the gut. I resist the urge to turn and walk away, and instead note with satisfaction that I was right and Emi is still running."

    "I don't make myself immediately known; I find a seat in the bleachers and watch her run instead, thinking back to earlier meetings."

    show emi basic_confused_gym:
        center
        xpos 0.6
        easein 0.5 center
    with charaenter

    show emi at center

    "After a few trips around the track, Emi notices me and skids to a halt, an expression of surprise that slides easily into one of anger."

    show emi basic_annoyed_gym
    with persistent.charachange

    emi "What are you doing here?"

    "Not quite the response I'd hoped for, but at this point I don't have much of a choice."

    hi "I wanted to apologize for what I said the other day."

    show emi basic_confused_gym
    with persistent.charachange

    emi "The other day?"

    show emi basic_closedgrin_gym
    with persistent.charachange

    "She laughs, a curt exclamation of disbelief."

    show emi basic_grin_gym
    with persistent.charachange

    emi "It's been almost a week, Hisao."

    hi "Yeah, well… better late than never, right?"

    show emi sad_annoyed_gym
    with persistent.charachange

    "Emi crosses her arms and stares at me coolly, as if sizing me up. Finally, she nods."

    show emi sad_grin_gym
    with persistent.charachange

    emi "Hmmph. I suppose you're right. Water under the bridge, then. I forgive you."

    show emi basic_grin_gym
    with persistent.charachange

    emi "Is that all?"

    show emi basic_grin_gym:
        easeout 0.5 xpos 0.3 alpha 0.0

    pause 0.5

    hide emi

    "Her almost impatient question catches me so off-guard that she's already halfway down the track before I think to shout after her."

    hi "No, wait!"

    scene bg school_track_on
    with locationchange

    "She doesn't seem to have heard me - or she doesn't want to hear me - and so I give chase, disregarding completely the fact that I am not dressed for it."

    scene bg school_track_running
    with Dissolve(2.0)

    "My feet hurt, and my shirt collar feels like a noose around my neck, but I still chase after her, because if I don't I'll lose my chance."

    "Emi hasn't started to really accelerate yet, which is probably the only reason why I'm able to catch up to her, to reach out and tap her on the shoulder, just before my legs give up running in dress shoes and stumble to a stop."

    scene bg school_track_on
    with Dissolve(2.0)

    "Surprisingly (fortunately?) all that running seems to have paid off. I'm short of breath, yes, but at least my heart isn't actively trying to force its way out of my ribcage."

    show emi basic_confused_gym_close at center
    with charaenter

    "My touch on her shoulder has stopped Emi, and while there is a flash of concern when she sees me catching my breath, it seems that she has a good idea of what I'm capable of too."

    "The concern is short-lived."

    show emi basic_annoyed_gym_close
    with persistent.charachange

    emi "What?"

    "She seems so irritated by my being still there that I almost lose my nerve, but I've lost my nerve enough."

    hi "I need to explain myself. Why I can't just let the matter rest."

    show emi sad_annoyed_gym_close
    with persistent.charachange

    "Emi folds her arms and bounces one blade on the ground in an approximation of tapping her foot impatiently. Angry as she is, and as nervous as I am, she still looks beautiful."

    emi "Okay, Hisao. Explain."

    hi "The thing is, I know that you're really sensitive about the accident and about your dad."

    "I can see Emi's face twitch at the mention of the two things that have been steadily driving us apart, or at least made me feel like we're being driven apart."

    hi "But that's why I want to know about them, I think."

    hi "Because I see how much they hurt you, and I want to be there to comfort you."

    hi "It makes me miserable, seeing you sleepless and depressed - and don't pretend you aren't, because I know, okay?"

    hi "I just remember that night when you fell asleep with me and had that nightmare, and that you were happy to have me there when you woke up."

    hi "I want to be able to be there for you like that whenever you need me to be."

    show emi sad_depressed_gym_close
    with persistent.charachange

    "The stern face cracks, slightly. Emi interrupts before I can continue further."

    emi "Just… stop right there. We can't see each other any more, okay?"

    show emi sad_pout_gym_close
    with persistent.charachange

    "She's rushing now, looking everywhere but at me. I'm surprised she doesn't bolt, she knows I can't catch her…"

    emi "We're not… we're not right for one another."

    hi "That's not true, and you know it."

    show emi sad_shy_gym_close
    with persistent.charachange

    emi "No, it's true. You're too—"

    hi "I know. I know that I've been pushy about knowing your past."

    hi "If you can't tell me yet, then at least let me be there even if I don't know the reason."

    hi "It's okay, I promise. I won't ask why you need comfort, I'll just give it freely."

    show emi sad_depressed_gym_close
    with persistent.charachange

    "Emi's shaking her head, and tears seem to be threatening the corners of her eyes."

    emi "Stop saying that!"

    hi "Why? Because you're afraid you'll take me up on it?"

    show emi sad_pout_gym_close
    with persistent.charachange

    emi "I'm not afraid!"

    "I can't keep the chiding tone from my voice as I respond."

    hi "Yes, you are. You told me so yourself, remember? That's okay, really it is."

    hi "However, it seems to me that someone who'd manage to come out of that wreck and still be as energetic and cheerful as you are would be determined enough to face that fear."

    show emi sad_angry_gym_close
    with persistent.charachange

    emi "Determination? What do you know about determination?"

    hi "I know that there's a girl so determined to take care of a total stranger that she'd steal his food at a festival."

    hi "I know that there's a girl so determined to help me with my own problems that she'd draw up a complete dietary and exercise plan, and that she'd not only draw up the plans, but she'd follow them with me, even when she couldn't run."

    hi "Determined enough to keep me at arm's length that she'd put herself through emotional pain if she thought it was the right thing to do."

    hi "Although, there's one thing that this determined girl didn't quite plan for, which was that I might feel that same kind of determination to keep her from being hurt."

    hi "I fell in love with you, and I refuse to let that be thrown away because you're afraid of losing me."

    show emi excited_sad_gym_close
    with persistent.charachange

    "What little control Emi still has at this point cracks, and I find myself suddenly enveloped in her embrace as she cries."

    emi "Why are you doing this? Why can't you just leave me alone?"

    show ev emi_forehead
    with dissolve

    "I hold her close and plant a kiss on the top of her head."

    hi "I'm sorry, Emi. You helped me when I first arrived, so now I have to help you. It's only fair."

    emi "You're utterly hopeless, did you know that?"

    "She hiccups and trembles a little."

    hi "Funny, I could say the same about you."

    emi "Can you do something for me, Hisao?"

    hi "Anything."

    scene bg school_track_on
    show emi sad_shy_gym_close at center
    with persistent.charachange

    emi "Can you go, now?"

    "It feels like she's just shoved a knife through my chest."

    hi "Go?"

    show emi sad_pout_gym_close
    with persistent.charachange

    emi "I need to… I need to think, okay?"

    emi "I can't just tell you everything yet. I'm still scared, and when you're around, I can't think clearly."

    emi "But do me another favor."

    hi "What's that?"

    show emi sad_grin_gym_close
    with persistent.charachange

    emi "Show up for our morning run tomorrow?"

    "I smile, feeling better than I have all week."

    hi "Of course. I wouldn't miss it for the world."

    show emi sad_grin_gym
    with charadistant

    "Emi steps back slowly, almost reluctantly. She sniffles a little and then grins at me, a real smile that lights up the track, overpowering the fading evening's light."

    show emi basic_grin_gym
    with persistent.charachange

    emi "See you tomorrow, Hisao."

    hi "Okay."

    show emi excited_amused_gym_close
    with characlose

    show emi basic_grin_gym
    with charadistant

    "She darts forward suddenly, planting a soft kiss on my lips, then steps back shyly."

    show emi basic_grin_gym:
        easeout 0.5 xpos 0.3 alpha 0.0

    pause 0.5

    hide emi

    "Spinning on her back foot, she takes off running again, and I know that our conversation's at an end."

    "My lips tingle with the warmth of that brief kiss and the memories of other, longer kisses."

    "I walk back to my room with a spring in my step."

    "Tomorrow when my alarm goes off, I'll get up."

    stop music fadeout 2.0

    return
