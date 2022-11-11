# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a4_rin:
    label .illusions_for_people:
        scene bg school_scienceroom
        with locationchange

        play music music_normal fadein 3.0

        "I make it in time for class, though not in time for breakfast."

        "The classroom is bathing in the gentle light of the sun."

        "This means that it's going to be intolerably hot in the afternoon. For now, though, it's pleasant."

        "I look at Misha and Shizune's animated discussion about whatever, Hanako staring out of the classroom window, Mutou stumbling into the classroom four minutes late and with no recollection of what he's supposed to be teaching today."

        "I could never imagine dropping out of school just like that, even if it's only for a few weeks."

        "On the other hand, Rin doesn't seem to have a problem with the idea, or going through with it."

        "Then again, somehow I got caught along in her insane isolation, even if we ended up hurting each other."

        "Or did we? Maybe only I got hurt."

        scene bg school_scienceroom_ss
        with shorttimeskip

        "It takes me until late in the afternoon to realize that today is Monday. The art club meets today."

        "Not just that. Due to the exams, this will be the last art club meeting before summer vacation."

        if believes_in_rin and not _in_replay:
            "I have no real business going there…"

            "But I want to talk with the teacher."

            scene bg school_hallway3
            with locationchange

            "So, I end up loitering awkwardly in front of the art room, waiting for the meeting to end."

            no "That's it for this trimester, everyone!"

            "His voice is loud enough to be heard through the door and way too enthusiastic for it to be genuine."

            no "The next meeting is after summer vacations, on the Monday of the first week of next term."

            no "I hope to see everyone there again!"

            no "Have a nice vacation!"

            play ambient sfx_crowd_indoors fadein 1.0
            stop music fadeout 4.0

            show crowd
            with charaenter

            "There's a confused answering chorus of voices, and the door to the classroom opens, releasing a flow of students."

            "I wait for everyone else to leave, so that I can talk to Nomiya alone. It's almost dinnertime, so I don't have to wait too long."

            stop ambient fadeout 2.0

            scene bg school_classroomart_ss
            with locationchange
        else:
            "Without Rin, it feels pretty pointless to go there, but I want to talk with the teacher."

            scene bg school_classroomart_ss
            with locationskip

            "The meeting itself isn't noteworthy, just as my skills with water colors are not worth mentioning."

            "Nomiya tries to encourage and advise me without sounding too condescending, but he's not doing a very good job of it."

            "If nothing else, joining the art club has taught me that I like art. It would be nice if I could actually try and make some art in the art club, though."

            "After the fruits of everyone's labor have been piled into a neat stack on the teacher's desk, he clears his throat to give a little speech."

            show nomiya talk at center
            with charaenter

            no "That's it for this trimester, everyone!"

            "His voice is pretty loud and way too enthusiastic for it to be genuine."

            show nomiya smile
            with charachange

            no "The next meeting is after summer vacations, on the Monday of the first week of next term."

            no "I hope to see everyone there again!"

            show nomiya veryhappy
            with charachange

            no "Have a nice vacation!"

            hide nomiya
            with charaexit

            stop music fadeout 4.0

            "Everyone wishes him a nice vacation back as they file out the door."

            "I stay behind, waiting until the two of us are alone. It's almost dinnertime, so I don't have to wait long."

        "Nomiya is looking through the paintings, some of which are actually pretty nice."

        "Rin might outclass everyone else in the art club, but she isn't the only one with talent."

        hi "Excuse me, teacher…"

        play music music_happiness fadein 2.0

        show nomiya smile at center
        with charaenter

        no "Hmm? What is it, Nakai?"

        "He raises his eyebrows questioningly, smiling widely."

        hi "It's about Rin…"

        show nomiya frown
        with charachange

        no "Oh? Is something wrong with Tezuka?"

        hi "No, but…"

        "I hesitate for a split second, not certain how to say what I want to say, giving Nomiya enough time to start blabbering by himself."

        show nomiya smile
        with charachange

        no "I saw her a few days ago when I was passing by at Sae's gallery."

        no "She said she'd get one or two more paintings done for the exhibition."

        show nomiya talk
        with charachange

        no "I was quite pleased, she's a surprisingly hard worker. I'd always thought she was a bit lazy, doing what she wants instead of the assignments…"

        "He seems to notice my anxiety and realizes he is digressing, shutting up before finishing the thought."

        show nomiya smile
        with charachange

        no "Ah, but you had something to talk about. What is it?"

        hi "I don't know… she feels detached from everything, as if she can't think of anything but the exhibition."

        show nomiya frown
        with charachange

        no "Well, isn't that good? She is focused on her painting, as she should be."

        hi "Yeah, but this is different. It's like she's obsessed. I went to see her, and…"

        show nomiya serious
        with charachange

        no "Have you been bothering her?"

        "He cuts in before I finish saying what I meant to say, instantly looking quite irritated."

        hi "No… I don't… think so."

        hi "I'm just concerned because she's stopped coming to school completely. She feels strange, too."

        hi "Stranger than usual, at the very least."

        show nomiya stern
        with charachange

        no "Humbug! This is much more important for her than some lousy math class, or physics, or whatever."

        no "This is exactly why this school is so flexible, to give every student a chance to fulfill themselves."

        show nomiya serious
        with charachange

        no "Tezuka is a painter, so she should paint, no? And have an exhibition. That's what artists do. She should be allowed to concentrate on that, not these other frivolous classes. She should be encouraged."

        no "If you think about it, it's really quite obvious."

        "His counterarguments are not very convincing, but I'm having a hard time trying to make any kind of rebuttal."

        "My grudging silence is interpreted as assent, and Nomiya turns to shuffle the stack of turned-in assignments on his desk like a deck of cards."

        show nomiya smile
        with charachange

        no "I have to say, while we're talking about Tezuka's exhibition…"

        no "I'm very excited to see how it turns out."

        show nomiya dreamy
        with charachange

        no "She's still so young, yet has such wonderful skill, and style!"

        "He's talking to the air, to relax the mood that got a bit too negative."

        show nomiya talk
        with charachange

        no "I take it that you will be attending?"

        hi "Yeah, I guess so."

        show nomiya smile
        with charachange

        no "Well, we'll meet there next."

        stop music fadeout 3.0

        scene bg school_hallway3
        with locationchange

        "I take that as my cue to leave. And I do, although I'm not happy about it."

        "My message didn't get through, to say the least."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .demused:
        nvl clear

        scene bg school_scienceroom_bw
        with locationchange

        nvl show dissolve

        play music music_night fadein 1.0

        n "{vspace=270}The day after that, all the missed opportunities and things I should have said come crashing down on me. There's nothing left to do afterwards but brood."

        nvl clear
        nvl hide dissolve

        with shorttimeskip

        nvl show dissolve

        n "{vspace=270}Second day. I begin to feel anxious. I start doubting my doubt and it feels stupid, especially since I still can't think about anything else than Rin."

        nvl clear
        nvl hide dissolve

        with shorttimeskip

        nvl show dissolve

        n "{vspace=270}Third day. Japanese exam, {b}and{/b} world history exam. Great. The thing I hate most about her is that she can make me feel this awful even though I should be focusing on entirely different stuff right now."

        nvl clear
        nvl hide dissolve

        with shorttimeskip

        nvl show dissolve

        n "{vspace=270}Fourth day. Math exam. We have a math exam. It goes how it goes. I don't care."

        nvl clear
        nvl hide dissolve

        with shorttimeskip

        nvl show dissolve

        n "{vspace=270}Fifth day. Nomiya asks me again if I will attend the exhibition opening. I can't say no to him even though I seriously want to. I just don't want to discuss with him anything Rin-related so it's just better to take the path of least resistance."

        nvl clear
        nvl hide dissolve

        stop music fadeout 2.0

        scene bg school_dormhallway
        show rin basic_absent at center
        with shorttimeskip

        "On the sixth day, the day before the exhibition opening, I find Rin standing in the hallway in front of my room when I return to the dorms after dinner."

        play music music_rain fadein 6.0 

        hi "What are you doing here?"

        "My tone is angrier than I intended. I'm a little disappointed that I was unable to restrain myself, but it can't be helped."

        "Rin just stands there, like she just happened to coincidentally be standing around here where she has no business being. The way she reacts so coolly to everything annoys me now."

        "This is not good. It's been six days, and the sight of her has me boiling. She hasn't even opened her mouth yet."

        show rin basic_deadpan
        with charachange

        rin "Finished painting."

        hi "Shouldn't you be at the gallery? Preparing?"

        show rin basic_awayabsent
        with charachange

        rin "They said no."

        "I guess the gallery owner does that part then, getting the paintings framed, hung on the walls and whatnot."

        hi "So, why are you here?"

        show rin basic_deadpannormal
        with charachange

        rin "Felt like it."

        "This same old stupid pattern emerges again; me asking her questions to which she replies with answers that don't answer anything, because it's the only other way we can converse."

        "Apart from me listening to her blabbering about whatever, which isn't really a conversation."

        "Is this a play? Are there some unseen roles that we have unknowingly set ourselves into, dictating the rules of engagement whenever we see each other, inevitably leading to us hurting each other?"

        "Her nonchalant answers accompanied by even more nonchalant shrugs leave me none the wiser. I guess I should be happy that the exhibition preparations are complete."

        play sound sfx_dooropen

        scene bg school_dormhisao
        with locationchange

        "When I walk into my room, I hear her footsteps following me in."

        "I didn't invite her in. I won't ask her to leave."

        show rin basic_awayabsent:
            center
            alpha 0.0
            ease 0.5 ypos 1.15 alpha 1.0
        with Pause(0.5)

        show rin:
            parallel:
                ease 0.3 center
            parallel:
                "rin basic_absent" with Dissolve(0.3)

        stop music fadeout 6.0

        "She claims my bed without asking permission, making me wish that I had taken the time to make it before I left in the morning, then stands up again as though she sat on hot coals."

        show rin basic_absent at center

        "I half-lean against the single corner of my desktop that isn't cluttered with stuff, to rest my legs at least a little bit."

        show rin basic_awayabsent
        with charachange

        "Rin spends a few moments glancing curiously around my room. It makes me realize that she's never seen it before."

        "For a moment, she actually looks like she's concentrating. Trying to get everything. This must be the eye for detail that makes her an artist."

        show rin basic_absent
        with charachange

        "Since the room is small, she quickly runs out of things to look at, but nothing else transpires, allowing the uncomfortable silence to take over the atmosphere."

        "The mood is chilly to say the least, and both of us are on guard, waiting for the other to make the first move."

        "Of course, Rin could play this game forever. So it has to be me."

        hi "So…"

        "I give up because she'd never try to open conversation, and because it seems that she wants to say something, and I want to get it over with."

        "Why else would she be here if she didn't want to talk?"

        "I don't know what to say myself. I want to be angry, but I can't bring myself to yell at her or anything."

        "My voice catches her attention, and she tries to search for words as well, but it seems that she is not entirely certain as to why she's here either."

        show rin basic_absent_close:
            center
            ypos 1.05
            easein 0.5 ypos 1.0
        with characlose

        show rin at center

        "And so, Rin simply takes a few steps to close the distance between us and rises on the tips of her toes to even out the height difference…"

        show rin basic_lucid_superclose
        with charachange

        centered "'It was a bad idea.'"

        centered "'Maybe you should forget about it, and I will too.'"

        "It's a reflex, and almost as an afterthought, the words 'no,' 'yes' and 'maybe' simultaneously surface inside my mind."

        "My hand is between her lips and mine, a wall that I raised to guard against… something."

        "Her breath feels warm against my fingers. The scent of her skin lingers about, the mysterious indescribable sensation that captures me and draws my eyes deep into hers."

        show rin basic_surprised_close
        with charachange

        play music music_moonlight fadein 0.5

        "The look in her eyes is surprised, quizzical as to why the impertinent hand prevented her advances."

        "Her eyes are really big and glistening with moisture, and staring right into my own with a soft gaze that I'm having a hard time to match."

        "Rin's half-open mouth makes her look even more confused, although the sensual way her lips are arching is signaling something completely different."

        show rin basic_upset_close
        with charachange

        rin "Please."

        show rin negative_angry_close
        with charachange

        rin "I need you."

        "The words come from her throat as a coarse whisper meant only for me, bypassing her tongue and teeth without giving them any chance to interrupt."

        show rin negative_angry
        with Dissolve(0.15)
        with vpunch

        "They sober me in an instant, and I clumsily flinch back to get a little bit of distance between us, painfully scraping against my desk in the process."

        "Maybe it's her choice of words, maybe the way she says it, but something in it puts me off."

        "Something is wrong, something is terribly wrong again."

        hi "Need me for what?"

        "All the unpleasant feelings emerge again, and I feel my heartbeat suddenly increasing at least tenfold."

        show rin basic_absent
        with charachange

        "Rin's eyes go out of focus and back again as her body relaxes from its tensed state, and she stands upright again."

        show rin basic_deadpanupset
        with charachange

        rin "I don't think I was thinking about anything. Why do you draw patterns in that dust on your night table?"

        show rin basic_awayabsent
        with charachange

        rin "There is a word for that kind of thing but I can't remember…"

        "Her remark almost throws me off track and I glance over her shoulder at the small table next to my bed, but I can't see anything from this distance."

        "So she needs me for nothing specific?"

        "Just happened to come by because she thought I'd be glad to see her after she shut me out, no complaints accepted, for a week."

        "Completely altruistic motives?"

        "Felt like it?"

        hi "Bullshit. I can answer myself."

        hi "To play mind games with whenever you want, to kiss whenever you want, to ignore whenever you want, to fulfill your whims whenever you want?"

        hi "Is that it? What you need me for?"

        "My voice is sounding very angry again, even to myself."

        extend " Good."

        show rin basic_absent
        with charachange

        "Rin too finally catches the mood and her curious expression changes instantly to something more uncharacteristic."

        show rin negative_sad
        with charachange

        rin "No—"

        "She leaves it at that, her eyes restlessly wandering around, searching the room as if the words she tries to find were written in the tapestries of my walls."

        hi "Then what?"

        show rin negative_confused
        with charachange

        stop music fadeout 2.0

        rin "I needed to paint."

        "Paint."

        "Of course. That's what artists do."

        "The words reverberate through my being, beating in my blood over the piercing whistle of my anger."

        play music music_tragic fadein 2.0

        hi "Don't give me that, Rin! I'm not some damn muse of yours, free to play with for the sake of painting!"

        hi "I am not some medium for whatever you aspire to, I am me!"

        hi "So what if I don't know anything about my future?"

        hi "There's things I want, and things I care about! Even I can dream of things other than nightmares!"

        "I'm yelling, but I'm way past the point of caring about things like that."

        show rin negative_sad
        with charachange

        "Rin looks down at her toes and wiggles them a little melancholically while she takes in my outburst without saying anything to defend herself."

        "Only after I have finished does she try to respond somehow."

        show rin basic_sad
        with charachange

        rin "I can't do anything else. Or I can do all sorts of things, but I… can't… do."

        show rin basic_upset
        with charachange

        rin "It's the only thing I sort of do properly. Most of the time."

        "I understand completely. Art first, everything else second, or thousandth."

        hi "What about me? Am I nothing? When I was interested in art, did that make you feel like I was a little interesting, for a little while?"

        hi "Tell me. I really want to know. Did you ever think about my perspective, or is it just all you?"

        "The words rise like bile in my throat."

        show rin basic_surprised
        with charachange

        "She looks alarmed. And also completely uncomprehending, as if she just doesn't understand what I'm angry about."

        "I can't believe she could be so stupid."

        show rin negative_sad
        with charachange

        rin "I didn't want to—?"

        "This time it's Rin who interrupts herself in midsentence."

        show rin basic_upset
        with charachange

        rin "Don't you understand? I can't."

        hi "Can't what?"

        hi "You never explain! How am I supposed to understand anything if you never say anything?"

        hi "Why don't you ever talk?"

        hi "Say something!"

        "But she doesn't."

        "Venting my anger at her feels satisfying. It feels wrong to take so much satisfaction in it, but I can't stop."

        show rin negative_annoyed
        with charachange

        "Not wanting to face my anger head-on, Rin turns around to steadfastly look out of my window even though there is nothing to look at."

        "The worst of my ire gone, I shut up as I can't be bothered to keep on yelling at the back of her head, so silence finally returns."

        "I try to discern some hints of her reaction through my adrenaline-distorted vision."

        "My feedback was not the best kind, but I hope Rin got the clue that she just can't ignore everything else whenever she feels like it."

        "I'd hate it if she didn't. She never ever listens to anything, she's so unaffected by the world around her."

        "Not this time, it seems."

        "Her body is shaking like from holding back tears, but I already know that Rin is not crying."

        "Her indifference made me so furious. Now that it's gone, I'm at a loss. I wonder…"

        "Did I go too far?"

        hi "Look, I—"

        show rin negative_angry
        with charachange

        rin "Go away."

        rin "Go away, Hisao."

        "Her voice is tiny and tired as she says this, but I hear the words clear as day."

        "…"

        "What is there to say any more?"

        hi "This is my room."

        "The blunt, hollow remark is a fitting conclusion for this unpleasant discussion that became an even more unpleasant and very one-sided yelling match."

        show rin basic_lucid
        with charachange

        "After a moment of collecting herself Rin just gives up, I can see it from the way she slumps her shoulders, and walks out."

        hide rin
        with charaexit

        "Even though she deliberately looks to the other direction, I can see how she's biting the corner of her lip so hard it might start bleeding if she won't stop."

        "As she makes her exit, I realize that she left the door open when she came in and my yelling must've echoed around the dorm hallways."

        "I sigh. Now that she's gone, I am left alone with my guilt."

        "As the thumping in my chest slowly subdues, anxiety replaces it."

        "Somehow, I feel that none of this would've ever happened if not for me."

        "No matter how infuriating, unbearable and outrageous Rin is, she is not the Rin I thought I knew."

        "The Rin that I expected Rin to be."

        "…"

        "Was it me who caused all this by talking Rin into taking her chances with the exhibition?"

        "Am I directly responsible for Rin becoming like she has been for the past weeks?"

        "I can't think of any other explanation for her weird behavior than the exhibition and all the things that came along with it."

        "Maybe it was the only way that could have brought us closer, but all it did was separate us further away from each other, and now beyond the reach of either of us."

        play sound sfx_impact2
        with vpunch

        "I bang my head hard against the wall."

        play sound sfx_impact2
        with vpunch

        stop music fadeout 4.0

        "Twice, to make sure it hurts."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .the_scene:
        $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
        play ambient sfx_traffic fadein 0.5

        scene bg gallery_ext
        with locationchange

        "A headache is relentlessly thumping against the back of my head as I push open the door to the 22nd Corner."

        "Apart from that, I'm perfectly calm."

        $ renpy.music.set_volume(0.1, 1.0, channel="ambient")

        nvl clear
        nvl show dissolve

        n "{vspace=60}After venting on Rin all that anger that I had bottled inside, it felt like a great weight had been lifted from my heart."

        n "The tension that had grasped my mind for the past few weeks faded away without leaving even a shadow behind."

        n "In this nearly Zen-like state of enlightenment I realized that perhaps it was a bad idea to yell at her like that."

        n "{vspace=30}I really meant it, but what good does blowing up like that do? Nothing."

        n "I am not like that. I don't normally yell at people. I don't know why I did yesterday."

        n "So I keep feeling really guilty about it and wanting to take my words back."

        n "{vspace=60}Rin is probably upset too. Even more than my own behavior, her reaction shocked me."

        nvl clear

        n "{vspace=30}I've always thought of her as unchanging, detached from her surroundings so that seeing my yelling get her so upset felt… out of place."

        n "{vspace=30}I wonder if she understands how I feel?"

        n "In Rin's world everything seems to be so absolute and subjective… absolutely subjective, as if she was completely unable to see things from other points of view than her own."

        n "But ultimately, is anyone able to do it? Maybe objectivity and altruism are just illusions for people who like to think of themselves as compassionate."

        n "Just like art is an illusion for people who think reality is merely a veil for something greater."

        n "Even when you stop thinking that the world revolves around you or start thinking outside of the mythical box, you are just inside another, bigger box that you can't escape."

        n "{vspace=30}Maybe that, ultimately, makes her like the rest of us."

        stop ambient fadeout 1.0

        nvl clear
        nvl hide dissolve

        play sound sfx_storebell
        $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
        play ambient sfx_crowd_indoors fadein 0.5

        scene bg gallery_int
        show crowd
        with locationchange

        play music music_ease fadein 3.0

        "I step through the door to find a gallery full of illusioned people."

        "Despite Sae's remarks during my earlier visits I always thought it was very spacious, but now when it's crowded like this it looks positively cramped."

        show sae smile behind crowd at center
        with charaenter

        "I immediately notice Sae standing in the middle of a lively discussion, busily chattering with some old gentlemen."

        "She's actually pretty tall and kind of cool-looking, so she stands out in the crowd."

        "There are a few dozen wine glasses laid on the tables along the back wall, filled with burgundy liquid. A vast majority of the guests are sipping from their own glasses."

        "The socialites and art connoisseurs are mingling happily, exchanging mild opinions about Rin's art which seems to be a secondary object of interest for most."

        "I feel distanced, excluded from the other people here."

        "I can't claim even at a stretch to be a social chameleon, so this situation is quite unnerving."

        "Since I don't blend into the crowd at all, I just fake that I do, trying to look as cool and smooth as I can."

        "I wonder how Rin is handling all this. If it was me, I would be quite freaked out."

        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

        scene bg gallery_exhibition
        show crowd
        with locationchange

        "Throwing the anxiety aside, I try to carefully navigate through the crowd, stealing peeks at the framed paintings now hanging on the walls."

        $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

        scene rin_exhibition_paintings:
            xalign 0.0
            warp acdc_warp 40.0 xalign 1.0
        with locationchange

        "Rin's exhibition takes about half of the gallery's wall space. Some paintings are less familiar than others, but I recognize most of them."

        "Some I've seen being created at the club meetings after all, or remember from the time when Rin was choosing her portfolio."

        "I note that a couple of the unfinished paintings are framed and on the wall as well. Maybe that's what they call coincidental art?"

        "Even Rin's failures, if you can call them that, became exhibits of her skill. Quite paradoxical."

        $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

        scene bg gallery_exhibition
        show crowd
        with locationchange

        "She herself is nowhere to be seen, which is strange because even though it's crowded, the gallery {b}is{/b} pretty small."

        "It's fine, sort of. I don't know how to face her after yesterday. Maybe I shouldn't have even come."

        "But I promised various people, Rin included, that I would, so…"

        "Damn, it sounds like I do the things I do because some kind of instinctual properness compels me to, not because it would be sensible (or not)."

        scene bg gallery_int at right
        show sae smile at center
        show crowd at right
        with locationchange

        "I sneak closer to Sae to wait for a lull in the conversation so I can chat her up too."

        "Even though her voice is almost completely buried under the general background noise, I hear bits and pieces of her talking about Rin."

        sa "Yes, she is a high schooler at a local school… even though she's graduating next year I'm sure various art schools would be interested in…"

        sa "…I thought it'd be interesting to have an exhibition of someone who is still in early stages of development…"

        "It's so strange, it's like Rin is some kind of mini-celebrity even though this is nothing but a small exhibition opening at a small art gallery of a small town."

        sa "In fact, there is a friend of mine from…"

        play sound sfx_impact
        with vpunch

        mystery "It's Hisao!"

        "My eavesdropping is interrupted by a familiar voice and a familiar slap to the back. I don't need to guess the source of either, even without turning around."

        hi "Hi Emi."

        $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

        show emicas happy:
            center xpos 0.15 alpha 0.0
            ease 1.0 center alpha 1.0
        show sae:
            ease 1.0 xpos 0.75 alpha 0.0
        with None

        show bg at left
        show crowd at left
        with charamovefaster

        hide sae

        emi "Hi! Are you like, a representative of the art club or something? I don't see anyone else from the school here…"

        hi "Umm… I don't know, really. I guess I am if that's the case."

        hi "What about you?"

        show emicas neutral
        with charachange

        emi "What about me?"

        hi "Err…"

        show emicas angry_up
        with charachange

        emi "You didn't think I'm interested in art? Is that it, Hisao?"

        hi "No, that's not what I… well, maybe a little, if you put it that way."

        hi "I mean, even though you hang out with Rin I've never heard you talk about art with her so…"

        show emicas awayfrown_up
        with charachange

        "Emi huffs and looks around her, looking discontented."

        show emicas closedsmile
        with charachange

        emi "It's true, I don't get it at all, but she came to my track meet so I thought it's only fair to return the favor."

        show emicas wink_close
        with characlose

        "She leans closer, trying to look confidential but only managing to look conspiring."

        emi "Do you {b}get{/b} art?"

        hi "No. No, I don't."

        hi "At all."

        show emicas closedsmile_close
        with charachange

        "My emphasizing headshake draws a giggle and a cheery headshake of her own out of Emi."

        show emicas happy_close
        with charachange

        emi "Me neither!"

        show emicas wink_close
        with charachange

        emi "Hey, let's go talk with Rin! I bet you haven't yet, because I haven't either."

        show emicas happy_up_close
        with charachange

        emi "Come on!"

        show nomiya smile behind emicas:
            center xpos 0.8 alpha 0.0
            ease 1.0 xpos 0.55 alpha 1.0
        show rin basic_awayabsent:
            center xpos 1.1 alpha 0.0
            ease 1.0 xpos 0.85 alpha 1.0
        show emicas neutral_close:
            ease 1.0 xpos 0.15
        with None

        show bg at center
        show crowd at center
        with charamovefaster

        "Before she has a chance to forcefully drag me to Rin, Nomiya appears behind her with Rin in his tow."

        "She's not dressed for the occasion, instead opting for the usual school uniform and unkempt hair."

        "Maybe her natural look is what suits her the best."

        show emicas happy_close
        with charachange

        emi "Hello, teacher! Hi, Rin!"

        "Unfazed, Emi greets the teacher cheerfully, causing him to turn around and look down confusedly."

        show nomiya frown
        with charachange

        no "Who are you?"

        show emicas frown_up_close
        with charachange

        emi "I'm Emi, from school, class 3-4. Don't you remember?"

        "She looks positively shocked at the prospect that there could be a person who doesn't know her."

        show nomiya talk
        with charachange

        no "Oh, sorry. You are in the same class as Tezuka is, right?"

        show emicas wink_close
        with charachange

        emi "Yeah!"

        show nomiya smile
        with charachange

        no "You'll have to pardon me, I have trouble remembering students who don't take art."

        show emicas closedsmile_up_close
        with charachange

        emi "Don't mind, don't mind!"

        show emicas happy_close
        with charachange

        emi "Hi Rin!"

        show rin basic_deadpan
        with charachange

        rin "Hello."

        show emicas happy_up_close
        with charachange

        emi "Congratulations for your super cool art thing! I'm sure you'll be a big hit!"

        "She throws her arms into the air for boisterous emphasis, almost hitting me in the face."

        show emicas wink_up_close
        with charachange

        emi "And look, Hisao came too!"

        show rin relaxed_nonchalant
        with charachange

        "Rin doesn't look at me, nor does she greet me."

        hi "Congratulations, Rin."

        "She keeps averting her gaze, pointedly looking at her sandals."

        show emicas closedsmile_close
        with charachange

        "Oblivious to the tension between us and ignorant of what happened yesterday, Emi keeps on blabbering about this and that to an unresponsive Rin."

        "I guess she's used to not getting much out of her at times."

        stop music fadeout 5.0
        $ renpy.music.set_volume(1.0, 3.0, channel="ambient")

        show sae neutral behind rin:
            center xpos 1.25 alpha 0.0
            ease 1.0 xpos 0.8 alpha 1.0
        show emicas:
            ease 1.0 xpos -0.35 alpha 0.0
        with None

        show bg at right
        show crowd at right
        show nomiya:
            xpos 0.25
        show rin:
            xpos 0.55
        with charamovefaster

        hide emicas

        "Before long, Nomiya and Sae turn to Rin, introducing her."

        "Expecting it, I catch the second of confusion when the guests see her arms."

        show sae smile
        with charachange

        "Sae is luckily on the ball and briefly explains about our school."

        "Doubtful faces quickly change to curious."

        "Man" "Would you mind telling us something about your art?"

        "Man" "I thought the development is quite easily noticeable, what do you yourself think of the differences between the older and more current works?"

        "Man" "It's quite rare for someone so young to dabble into abstraction."

        "Woman" "It would've been interesting to see how you work!"

        "Man" "Oh, definitely! I assume you use your feet? Must've been a great trouble to learn it, you should be proud."

        show rin basic_surprised
        with charachange

        rin "I… ummm…"

        play music music_rain fadein 8.0

        "Man" "Will you be pursuing a career as an artist after school?"

        "She is bombarded with so many questions she can't even hope to answer all of them."

        "Maybe that's for the best, Rin tends to talk nonsense more than occasionally."

        "Man" "So where do you get your ideas?"

        show rin relaxed_boredom
        with charachange

        rin "That's the fourth, I mean fifth worst…"

        "Rin keeps stumbling with her words, looking more and more vexed by the expectant inquiries."

        show rin negative_annoyed
        with charachange

        rin "Ah…"

        "Everyone is waiting for her to say something, but she looks like a cat got her tongue."

        "Each question piling up just adds to her distress."

        show rin basic_sad
        with charachange

        "I fail to hear the question that is the proverbial one too many."

        "It's like a motor stalling."

        show rin basic_sad:
            1.2
            parallel:
                easeout 0.5 ypos 1.2
            parallel:
                "rin basic_lucid" with Dissolve(0.3)
        with Pause(1.5)

        stop ambient fadeout 7.0

        scene ev rin_gallery:
            truecenter
            zoom 0.9
            easein 30.0 zoom 1.0
        with Dissolve(0.2)
        play sound sfx_pillow
        with vpunch

        "Rin just freezes for a long, long second until she falls on her knees, hitting the floor ungracefully like a sack of potatoes."

        "Woman" "Are you all right?"

        rin "I don't know…"

        no "Tezuka? What's wrong, girl?"

        rin "I don't know what's wrong…"

        "A terrible silence falls upon the people gathered around Rin."

        "Everyone is petrified, not knowing how to react to her sudden… seizure, or something."

        "She breathes with deep, trembling gasps as if she was running out of air, staring ahead of herself with hollow eyes."

        play sound sfx_rustling
        stop music fadeout 1.0

        scene bg gallery_int at right
        show crowd at right
        show nomiya serious:
            center
            xpos 0.25
        show rin negative_sad_close:
            center
            xpos 0.55 ypos 1.2
            ease 0.8 ypos 1.0
        show sae scowl:
            center
            xpos 0.8
        with locationchange

        show rin:
            center
            xpos 0.55

        "Seeing that nobody does anything, I force myself to step to Rin and lift her up from the floor, letting her lean against me to keep standing."

        hi "Would you like some fresh air? OK, let's go outside for a bit."

        "I don't even wait for her to answer before grasping her shoulder and pulling her past the stunned-looking Nomiya, Sae, Emi and guests."

        hi "Excuse us."

        play sound sfx_storebell
        $ renpy.music.set_volume(0.2, 0.0, channel="ambient")
        play ambient sfx_traffic fadein 1.0

        scene bg gallery_ext
        with locationchange

        "The cool evening breeze hits my face at the door."

        show rin negative_sad_close_ni at center
        with charaenter

        "I let go of Rin and she leans against the stone wall, trying to catch her breath."

        hi "Are you all right?"

        show rin negative_confused_close_ni
        with charachange

        rin "I couldn't say anything…"

        "Rin is still not looking at me, so I look away too."

        play music music_dreamy fadein 4.0

        "The streetlights and colored neon signs twist my vision into a blur of near-blindness, forcing me to look back."

        "At least she talks, even if she's not directing her words to me."

        hi "What did you want to say?"

        "Maybe both of us can imagine that we are talking to an invisible friend."

        show rin basic_sad_close_ni
        with charachange

        rin "I don't know."

        show rin negative_sad_close_ni
        with charachange

        rin "Something that would have meant something."

        "…"

        "The silence lasts for a long time."

        "I don't feel comfortable being alone with Rin. I am not good at imagining things that don't exist, do… or that things that exist, don't."

        hi "We should go back in."

        hi "The guests Sae invited are in there, they probably want to meet you and talk with you."

        hi "You know, ask you questions and stuff. About those paintings you worked so hard for."

        show rin negative_angry_close_ni
        with charachange

        rin "I don't want them to ask me questions like that. I can never say the right things."

        hi "What do you want then?"

        "…"

        show rin relaxed_doubt_close_ni
        with charachange

        menu:
            with menueffect
            rin "That someone wouldn't have to ask questions from me."

            "But aren't you happy people are interested in your paintings?":
                $ is_true = True

                call a4rc1o1

            "But if you found someone like that, then what?":
                $ is_true = False

                call a4rc1o2

        if _in_replay:
            return

    call timeskip

    if is_true:
        label .wavelength:
            call separate_of_dg_and_wl

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=60}Vacation, huh?"

            n "Some people will stay at the school even over the holidays, some will go back to their families."

            n "I probably should make the trip back home and report to my parents that I'm alive and well."

            n "{vspace=30}Not much to do at the school anyway, I suppose."

            n "Next trimester will be stressful. Everyone will have to seriously start thinking about what to do after graduation."

            n "{vspace=60}Including me…"

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl clear
            nvl hide dissolve

            scene ev rin_doodle_all
            with silentwhiteout

            "A look at my doodles convinces me to stop trying to salvage them. It's a mess of lifeless lines, a waste of paper if it wasn't the flip side of my exam."

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=90}Maybe it's because I didn't really set out to draw anything in particular."

            n "I just wanted to kill some time, so the drawing became exactly like I am."

            n "Without a direction to go to."

            n "{vspace=60}It'd be easier if I had some special talent, like Rin."

            n "She has it easy."

            n "It makes me kind of jealous."

            n "It pisses me off that she herself can't seem to be happy about it."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl clear
            nvl hide dissolve

            scene bg school_scienceroom
            show muto smile at center
            with locationskip

            mu "Aaaand… time!"

            "Mutou's call for the end of the exam draws groans of displeasure from half the class."

            "I don't blame them, the exam was kinda tricky."

            "Mutou expects a lot from our class, even though he's not strict at all. I guess he'd like all of us to become scientists."

            show muto normal
            with charachange

            mu "Put down your pencils and turn in your papers please."

            "The biggest groan comes from the desk to my side."

            show misha perky_sad_close:
                center xpos -0.2 ypos 1.13 alpha 0.0
                ease 1.0 xpos 0.15 alpha 1.0
            with None

            show bg at bgright
            show muto at tworight
            with charamovefaster

            show misha:
                center
                xpos 0.15 ypos 1.13

            "Misha's despair is almost tangible."

            "The dark aura of lost hope emanating from her seat makes me simultaneously frightened of and sympathetic to her."

            show muto smile
            with charachange

            mu "Now then, there should be homeroom before you are free, but I only have a few announcements to make so this should be over quickly…"

            "His announcements are never important, so I listen to him only with one ear."

            "Misha seems to be too down in the dumps to even pretend attentiveness."

            "She slumps her head against the desktop, looking stricken."

            hi "Cheer up, Misha."

            hi "It's vacation! Don't worry about the test."

            show misha sign_smile_close
            with charachange

            mi "Thanks, Hicchan."

            "Her frown becomes a small smile, and a sparkle of excitement lights in her eyes."

            show misha perky_smile_close
            with charachange

            mi "What're you going to do over your summer vacation, Hicchan?"

            show misha hips_smile_close
            with charachange

            mi "I'm going to Shicchan's place, they have this awesome and super cool mansion! I'm so excited~!"

            show misha hips_grin_close
            with charachange

            mi "I'm sure it'll be the bestest summer vacation ever~!"

            "She seems to have forgotten all about her misery in a few seconds and bounces up and down on her seat as if to pump up her excitement."

            hi "I don't really have any plans, I guess…"

            show misha sign_smile_close
            with charachange

            mi "Is that so~? Maybe you should—"

            show misha perky_confused_close
            with charachange

            "A finger tapping her shoulder steals Misha's attention away from me."

            show muto irritated
            with charachange

            "Shizune points to Mutou, who is expectantly looking back at the two of them."

            show misha sign_confused_close
            with charachange

            mi "Oops! Sorry, Shicchan, I didn't notice teacher finished already, ehehe~."

            "She clears her throat and takes a deep breath…"

            show misha hips_grin_close:
                ypos 1.0
            with charamovechangefaster

            mi "Stand!"

            "I stand up with everyone."

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=60}Since I came here, I've always wondered about something."

            n "What do the wheelchair-bound students think about this daily tradition, being unable to do it 'properly?'"

            n "Is it a faux pas to keep to this tradition in a place that bypasses many others for convenience?"

            n "Even though I never asked anyone, during these short weeks here I've come to the conclusion that they definitely are not insulted."

            n "They understand."

            n "That's what I like about this school. Nobody is too uptight about anything, everyone is so… considerate and understanding of each other."

            stop music fadeout 4.0

            n "{vspace=60}I wish the whole world could be like this."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl clear
            nvl hide dissolve

            scene black
            with locationchange

            mi "Booooow!"

            scene bg school_dormhisao
            with shorttimeskip

            play sound sfx_paper
            play music music_tranquil fadein 3.0

            "I turn the page slowly, listening to the rustling sound the paper makes when my fingers grasp it."

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=30}I'm restless."

            n "It's the summer vacation."

            n "No class, no homework, no art club meetings. Just free time to spend however I want."

            n "It doesn't feel like anything."

            n "I tried to cheer up Misha, but I'm not feeling too cheery myself."

            n "To be honest, the free time is intimidating. It reminds me of the hospital and the long, meaningless days that had to be filled somehow."

            n "The only difference is that there I was bound to the ward, guarded by the Cerberus-like nurses."

            n "Reading was a good solution back then, but the thought of spending my summer vacation reading books feels… nerdy."

            n "That has nothing to do with the fact that I'm reading even now… I'm just killing time and trying to fight my anxiety."

            n "Besides, my mind is on other matters, stretching in too many directions to make sense of any of them."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl clear
            nvl hide dissolve

            "Thus, the book I've been on since Tuesday is progressing s{w=0.3}l{w=0.3}o{w=0.3}w{w=0.3}l{w=0.3}y{w=0.3}."

            "It feels like this book is taking me longer to read than it took the author to write."

            "I try to put it down for a while, then read some again, start all over from the beginning, read each page twice."

            "Nothing works, I have zero concentration."

            "Taking it with me just in case, I head out to get some fresh air and inspiration as to what to do."

            scene bg school_courtyard
            with locationskip

            "I make my way to the quad, passing by students heading for the gates."

            "The hastiest ones are leaving for their homes already, judging from the luggage some are dragging with them."

            "I guess that no matter how hospitable Yamaku is, home is still home. Still, I heard some people will be staying here over the vacation."

            "The quad is big enough for its center to be shadowless no matter how high or low the sun is."

            "I stop in the middle and bask in the warmth."

            "The brightness makes me squint my eyes when I look towards the main building."

            "It looks all but abandoned already."

            "Yuuko wasn't at work today, so the next time I can get books from the school library is after vacation."

            "There is a public library somewhere, I'm sure, but I'm feeling too lethargic to find out where it is."

            scene bg school_lobby
            with locationskip

            "The hall is equally dead so I have to content myself with returning to the dorms, ending my leisurely walk sooner than I expected."

            "Then again, I wasn't quite sure what I was expecting in the first place."

            scene bg school_girlsdormhall
            with locationskip

            "On a moment's impulse I enter the girls' dorm to see if Rin or Emi are there."

            "Neither is, so I go back to my own room to dwell on my lethargy."

            scene bg school_dormhisao
            with locationskip

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=60}I should talk things through with Rin."

            n "She really bothers me."

            n "{vspace=60}Defying the conceptual equivalent of gravity, she balances on the thin line zigzagging between insanity, incomprehensibility and instability."

            n "Rin affects me too. She challenges me in ways that I didn't know… or more accurately, didn't hope existed."

            n "{vspace=60}I've started to wonder whether these feelings are really love, or I was just fooling myself."

            n "Surely, it would be insanity to consider that?"

            nvl clear

            n "{vspace=60}For the rest of the day, Rin, the hospital, Yamaku and vacation swirl through my head."

            n "{vspace=30}I can't concentrate even on concentrating."

            n "{vspace=30}Thoughts seem to come and go haphazardly, fragmented into too-small pieces of cognition."

            n "{vspace=30}I pick up the book and manage to read a hundred pages, but I'm sure by tomorrow I'll have no recollection of what happened in the story."

            n "{vspace=30}I try to clean up my room, but even that proves to be too bothersome, too time-consuming and requiring too much attention to detail."

            n "It's usually like this. When you have 'nothing to do,' you do nothing even if you could."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl hide dissolve
            nvl clear

            scene bg school_dormhisao_blurred_ss
            show phone mobile at truecenter
            with shorttimeskip

            "As expected, mom calls me and I end up promising to see if I can get a train ticket for tomorrow, or failing that, the day after."

            nvl clear

            show phone mobile:
                easeout 1.0 ypos 0.7 alpha 0.0

            scene bg school_dormhisao_ss
            show phone mobile:
                truecenter
                easeout 1.0 ypos 0.7 alpha 0.0
            with locationchange

            pause 0.5

            hide phone

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl show dissolve

            n "{vspace=60}Maybe I'll go downtown tomorrow anyway. I could do some shopping or something."

            n "It's not that I need anything, but maybe there are summer sales, and I could pick up… something."

            stop music fadeout 10.0

            n "{vspace=60}…Why am I trying to force myself?"

            n "Before, I was content with having nothing to do, save for kicking the ball every now and then at the field."

            n "Now it seems that I can't settle down at all."

            n "{vspace=30}Is it because I have changed, or because my world has changed?"

            nvl hide dissolve
            nvl clear

            scene bg school_dormhisao_ni
            with shorttimeskip

            "By eleven, the darkness bids me to sleep."

            show pills:
                truecenter
                ypos 0.7 alpha 1.0
                easein 1.0 truecenter alpha 1.0
            with Pause(1.0)

            show pills at truecenter

            "The medication bottles are innocuously arranged on my night table, not at all beckoning, rather pointedly reminding me of the reality instead."

            "It's evening so I have to open three bottles, extract one large oval-shaped one, two small round ones and one large flat that has to be cut into half, close the bottles and chug down the medications with a chaser of fresh tap water."

            show pills:
                easeout 1.0 ypos 0.7 alpha 0.0
            with Pause(1.0)

            hide pills

            "The water tastes metallic on my tongue."

            "I swallow it along with the pills anyway and head to the bathroom."

            scene bg school_dormbathroom
            with locationskip

            "The mindless job of brushing my teeth is fit for trying to sort my thoughts."

            "One emerges from the mass, clearly rising above the others."

            nvl clear
            nvl show dissolve

            n "{vspace=270}I want to see Rin."

            n "I can't let my outburst of anger be the last thing between us before the vacation."

            nvl hide dissolve
            nvl clear

            scene bg school_dormhisao_ni
            with locationskip

            nvl show dissolve

            n "{vspace=240}I have to see her, tomorrow."

            n "Sleep overcomes my confused mind with more ease than it should."

            nvl hide dissolve
            nvl clear

            scene black
            with shuteye

            if _in_replay:
                return

        call timeskip

        label .blue_period:
            $ renpy.music.set_volume(1.0, 0.0, channel="music")
            $ renpy.music.set_volume(0.7, 0.0, channel="ambient")
            play ambient sfx_rain fadein 1.0

            scene bg misc_sky_rn
            show rain normal
            show hisaowindow
            with locationchange

            "Rain is falling on my summer vacation like an uncountable number of small bad omens."

            "Luckily I'm not superstitious, but the bad weather makes me downcast too."

            "It's been like this since morning and there is no end in sight."

            "An impenetrable gray mass of clouds shadows the sky as much as it shadows my mood."

            "In a bout of defiance, I finished cleaning up this morning, but after that was done I ended up staring out of the window in hope of the weather clearing."

            "The incessant drumming of rainfall against the roof and the pavement is mesmerizing, a droning background noise to lose your mind into."

            "…"

            "… …"

            $ renpy.music.set_volume(0.4, 1.0, channel="ambient")

            scene bg school_dormhisao_rn
            with locationchange

            "This won't do, I have to get a move on."

            "Should I pack now, or later?"

            $ renpy.music.set_volume(0.2, 1.0, channel="ambient")

            scene bg school_dormhallway
            with locationchange

            "I decide on the latter and make my way outside, pausing briefly at Kenji's door to listen to the odd clunking sounds from the other side."

            show rain normal behind bg

            "I don't dare to knock, out of the fear of finding out what he is doing."

            $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

            scene bg school_dormext_full_rn
            show rain normal
            with locationskip

            "Braving the rain from under my trusty umbrella, I cross the space to the girls' dorm."

            $ renpy.music.set_volume(0.2, 1.0, channel="ambient")

            scene bg school_girlsdormhall
            with locationskip

            play sound sfx_doorknock2

            "Knocking on Rin's door yields no answer, but the door behind me opens instead."

            play sound sfx_dooropen

            show emicas happy:
                center xpos 0.3 alpha 0.0
                ease 1.0 center alpha 1.0
            with Pause(1.0)

            show emicas at center

            play music music_emi fadein 0.5

            emi "Hisao? Hi!"

            show emicas awayfrown
            with charachange

            emi "Terrible weather. I even missed my morning jog."

            "She frowns, but I would be glad if I was her. Emi's morning jogs are anything but leisurely."

            hi "Oh, hi, I was—"

            show emicas neutral
            with charachange

            emi "If you're looking for Rin, I don't think she is there."

            hi "Have you seen her recently?"

            show emicas grin_up
            with charachange

            emi "Yeah, just this morning when I woke her up."

            "The mention of waking up makes Emi yawn like a cat, and makes me feel silly."

            "Of course she has seen Rin. Emi wakes her up and helps her get dressed on most mornings, even makes her lunch boxes every now and then."

            "They are like sisters, even though they seem to have nothing in common."

            if not what_about_emi:
                "I wonder which one is the elder sister? Probably Emi, against all odds."

                "She is really diligent, even though she gives the feeling of someone who would be a total airhead."

                "Why does it feel odd that she is so dutiful under that cheery grin of hers?"

            show emicas frown_up
            with charachange

            emi "She left for the gallery a few hours ago… hey, are you listening?"

            "Maybe I'm making a funny face or something, since Emi tilts her face quizzically, looking at me with her eyes round and inquisitive."

            show emicas neutral
            with charachange

            emi "Hmm?"

            "Her innocent face seems to request my attention."

            hi "Yeah, I'm listening…"

            show emicas weaksmile
            with charachange

            emi "Can I ask you a question?"

            hi "Yeah, of course."

            show emicas awayfrown
            with charachange

            "She furrows her brow, licking her lips as if to prepare for something."

            show emicas frown
            with charachange

            emi "Why do you care so much about Rin?"

            show emicas neutral
            with charachange

            emi "I mean, you probably hang around her more than I do, and we even slept in the same bed sometimes until, er, lately."

            hi "After she banned you because you ravaged her hair?"

            show emicas blush
            with charachange

            "A shock of horror widens Emi's eyes at least twofold, making them seem even more saucer-like than usual, while a healthy blush rises on her cheeks and ears."

            show emicas angry_up
            with charachange

            emi "She told?! Ohhh… I'm going to strangle that Rin or something other horrible…"

            "I hold back my laughter, lest she direct her disdain at me."

            show emicas closedsmile
            with charachange

            "Emi recuperates quickly from the embarrassment and seems to forgive Rin in the same instant, getting her focus back on me."

            show emicas smile
            with charachange

            emi "Anyway, are you in love with her or something?"

            "Uh oh. This really feels like an elder sister questioning a suitor. Emi is kinda nosy, and not in a good happy way, if there even is one to begin with."

            "She'd make a good partner for Misha, to be honest. The horror."

            hi "That's already your second question, so I don't think I have to answer."

            "I try to conjure up a front made of pure, crystallized cool and uninvolvement."

            "I wonder whether I manage to fool even myself."

            show emicas evil
            with charachange

            "At least Emi is waggling her eyebrows dangerously, with a nasty smirk on her lips."

            emi "Is that a yes?"

            hi "No, it's not a yes."

            show emicas neutral
            with charachange

            "Obviously unsatisfied at my refusal to answer her way-too-intimate question, she has enough sense to back off."

            show emicas wink
            with charachange

            "Doesn't stop her from sticking out her tongue at me like a kid, and giggling again."

            show emicas closedsmile
            with charachange

            emi "If that's your answer, I don't think I have to talk with you any more."

            "It's easy to see that she's not really angry."

            show emicas happy
            with charachange

            emi "Besides, I have to go pack now. Mom will be worried if I miss my bus."

            emi "Seeya!"

            hi "Yeah, bye."

            stop music fadeout 4.0

            hide emicas
            with charaexit

            play sound sfx_doorclose

            "She retreats back into her room, leaving me alone in the hallway."

            "What's between me and Rin is not her business, right?"

            "That's why I ended up not saying anything about our fight to Emi. Rin must have not said anything either."

            "I guess… even though they are friends, there are things they don't talk about."

            "…"

            "So, if Rin is at the gallery, I'd have to go all the way there."

            "Now that I managed to get out of my room, I suppose it's not that much of a bother to go downtown."

            "I could go get a ticket, but the train back home will have to wait, at least until tomorrow."

            "No way I'm going to carry baggage to the train station in this rain, even if there's not that much of it."

            $ renpy.music.set_volume(1.0, 3.0, channel="ambient")

            scene bg city_street4_rn
            show rain normal
            with shorttimeskip

            "Rain makes all outlines seem very unstable, as if they were fading away."

            "The townscape turns into a shapeless collection of various fuzzy tones of gray, instead of distinct forms of buildings and cars."

            "Those poor souls who are forced into the downpour try to make as much haste as they possibly can, pitying each other for their shared misery."

            scene bg gallery_ext_rn
            with locationchange

            "I turn the final corner, the twenty-second corner so to say, and immediately feel stupid for being amused by my own pun."

            "The door beckons me with promises of warmth."

            $ renpy.music.set_volume(0.2, 1.0, channel="ambient")
            play sound sfx_storebell 
            play music music_soothing fadein 0.5

            scene bg gallery_int
            with locationchange

            "The rainwater dripping from my umbrella makes interesting, almost artistic patterns on the floor."

            "I am not wet, apart from my shoes that leave small puddles in my wake, completing the rainwater-artwork."

            show nomiya smile at twoleft
            show sae neutral at tworight
            with charaenter

            "Nomiya is here too, chatting with Sae at the back of the gallery. Rin's nowhere to be seen, though."

            "Maybe she's upstairs."

            "There are no customers though, which figures, considering the bucketloads of water dropping on the neck of anyone daring to brave the weather today."

            show sae smile
            with charachange

            sa "Welcome."

            hi "Hello. Sorry to interrupt…"

            show nomiya talk
            with charachange

            no "Ah, good afternoon Nakai."

            show nomiya smile
            with charachange

            no "Came all the way here for a visit?"

            hi "Ah… no, I think it was just an impulse. I was around the neighborhood, shopping, and decided to stop by."

            "My reflexive reaction is a white lie, which surprises myself."

            "Maybe I just don't want to say that I came specifically to see Rin, even though that much must be obvious."

            show sae doubt
            with charachange

            sa "My, you chose a bad day for shopping. Would you like some tea to warm you up?"

            hi "Thank you but I'm fine, really."

            hi "The weather could be better though. Rain on the first day of vacations is a bit depressing."

            show nomiya veryhappy
            show sae neutral
            with charachange

            no "Hahaha! Well, I'm sure it'll get better."

            "Nomiya offers his hearty laughter, bordering on abrasive."

            hi "Rain doesn't get you down, teacher?"

            show nomiya smile
            with charachange

            no "Well, I do prefer clear weather as well. I was actually leaving just now to meet someone, and I'd prefer not getting my jacket soaked. It's very expensive."

            show nomiya talk
            with charachange

            no "But of course I'm in a good mood!"

            show nomiya smile
            with charachange

            no "What did you think about the exhibition? It was wonderful, wasn't it?"

            hi "Yeah, it was very fancy."

            "My unenthusiastic answer only spurs him to carry on, walking around the gallery while blabbering about the opening."

            "He talks more and louder when he is moving. It's something I noticed at the club meetings too."

            show nomiya veryhappy
            with charachange

            no "We got to talk with many good people and make valuable contacts."

            show nomiya smile
            with charachange

            no "One of Tezuka's paintings even got sold, to a collector from Osaka."

            $ renpy.music.set_volume(0.1, 1.0, channel="ambient")

            show rin_exhibition_sold at center
            with locationchange

            "I follow his eyes to an empty space in the wall. I can't even remember which painting was hanging on that spot."

            "Well, it's gone now."

            $ renpy.music.set_volume(0.2, 1.0, channel="ambient")

            hide rin_exhibition_sold
            show nomiya talk
            with charachange

            no "It was lucky that she was all right despite that dizzy spell."

            show nomiya smile
            with charachange

            no "She got a little quiet though, so I told her to rest well. Then again she's always been pretty shy."

            "Shy? Whatever, I just nod along with the teacher."

            show nomiya talktongue
            with charachange

            no "The reception was very positive in general. I might be able to get one of my friends to write a little article on a magazine to—"

            sa "Shinichi, your meeting. You're making Mr. Takahashi wait."

            show nomiya serious
            with charachange

            "Sae's remark makes him stop in his tracks and check his watch."

            "Nomiya frowns in displeasure at the interruption to his tirade."

            show nomiya smile
            with charachange

            no "Oh, right. Yes, well, I'll be off then. We'll meet in September, Nakai."

            hi "Bye."

            hide nomiya
            with charaexit

            play sound sfx_storebell
            stop music fadeout 4.0

            "Wow. Teacher really doesn't hold back when it comes to Rin's budding artist career."

            "I guess it takes a lot to succeed, but I suppose his job would be easier if Rin was more cooperative."

            $ renpy.music.set_volume(0.1, 1.0, channel="ambient")
            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=30}She's too indecisive even though she's doing just fine. Like that 'dizzy spell' from the night before."

            n "She just got freaked out or something, and I didn't do anything to help her."

            n "{vspace=30}I sigh."

            n "It feels like the gap between me and Rin is only widening."

            n "She's going to become something great while I'm still feeling like I'm bogged down, despite promising myself to try and make something of my life."

            n "On top of that, we had that fight and the longer we keep not talking, the harder the wounds become to heal."

            n "If that even is what we want. I never found out what Rin felt, and now I'm not sure what I feel myself."

            n "I wish I could understand her. But Rin is not very open for interpretation."

            n "Not that she's hiding anything, she just seems to defy my attempts at making sense of what she is talking about on any given day."

            $ renpy.music.set_volume(0.2, 1.0, channel="ambient")
            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl hide dissolve
            nvl clear

            show sae smile
            with charachange

            sa "Something on your mind?"

            "I realize I've been spacing out in the middle of the gallery for who knows how long."

            hi "Ahh… nothing special…"

            "I pretend to study the closest paintings to distract her."

            $ renpy.music.set_volume(0.1, 1.0, channel="ambient")
            play music music_another fadein 0.5

            scene rin_exhibition_c:
                truecenter
                ease 30.0 zoom 1.1
            with locationchange

            "I've seen it before."

            "The now all-too-familiar strokes of color, twisting and melting into each other seemingly randomly still manage to feel like there is something happening behind the scenes, so to speak."

            "Rin's style is so much like her. Abstract, incomprehensible, colorful."

            "Mysterious."

            "I wonder if to understand an artist, one must understand art?"

            $ renpy.music.set_volume(0.2, 1.0, channel="ambient")

            scene bg gallery_int
            with locationchange

            hi "Umm… I may have a question."

            show sae smile at center
            with charaenter

            sa "Oh?"

            "She looks up from the magazine she was idly leafing through, seeming delighted at my display of unspecified interest."

            hi "How do you interpret art?"

            show sae doubt
            with charachange

            sa "What do you mean?"

            "Her eyebrows rise high into questioning arcs, as if the question was too complicated to even begin to answer without clarification."

            hi "Sorry if I'm asking something stupid."

            hi "I don't think I really understand art like the pros do."

            show sae smile
            with charachange

            sa "Oh, there's no trick to it."

            "Sae waves my question away with a simple but efficient flick of her wrist."

            show sae neutral
            with charachange

            sa "Everyone interprets art as they will, and interpretation is as much in the eye of the beholder as in the intentions of the creator."

            sa "'Pros' have their own way, because there is this thing called art theory."

            sa "There are patterns in art, just like in everything, and we assume that it's possible to draw some conclusions from observing those patterns."

            "Her voice is like a teacher's, lecturing and adding emphasis on random words to keep the listeners on their toes."

            show sae smile
            with charachange

            sa "In the end, I suppose it's pretty meaningless."

            "She moves to musing seemingly to herself, muttering loud enough for me to clearly hear."

            sa "A good piece of art will make you feel something and that's all there is to it."

            sa "Feelings change and they affect the art we create and the art we see."

            hi "But…"

            show sae neutral
            with charachange

            sa "I'll tell you a story."

            hi "Do you have to? The last one was depressing…"

            sa "It's important. Listen…"

            sa "About a hundred years ago a little known painter got news that his friend, a man called Casagemas, had committed suicide."

            sa "This happened while he was away and hadn't seen his friend for a while."

            sa "So obviously he must have felt even more conflicted than you normally would after hearing of such a thing."

            sa "For four years after that, our main character did nothing but monochromatic paintings because he was so deeply affected by the news."

            sa "Whatever he did, he always kept returning to that same color until it let him out of its grasp."

            "She takes a little pause to check whether I'm still following."

            "I am, to an extent, so I give her the prompt that storytellers seem to live for."

            hi "So…"

            "It's hard to continue from that, as I can't seem to come up with the question she wants me to come up with."

            "Like a half-baked Socrates, she thought she laid out all the tools for revelation in front of me."

            show sae doubt
            with charachange

            sa "Don't you see the point yet?"

            "Only, her student proved to be too dense to get it."

            show sae scowl
            with charachange

            "She looks discontent at my slowness."

            sa "Picasso's Blue Period is one of the most lauded in the history of art, but who knows what he felt when he worked on those masterpieces?"

            sa "Sadness? Longing? Regret?"

            sa "Nobody can tell."

            sa "If you now see one of his Blue Period paintings, you'd probably interpret it differently from before you knew about Picasso's friend Casagemas."

            show sae neutral
            with charachange

            sa "Experiencing art is always personal, only interactive by chance or circumstances."

            sa "There are a million explanations for any given piece of art, but it might be that none of them are what the creator intended."

            show sae smile
            with charachange

            sa "No man is an island, you know?"

            "I nod without understanding what that last remark meant."

            "What she said made sense otherwise, except for one thing."

            "If art is communication like Rin said, but everyone is talking their own secret language like Sae said, what can anyone ever hope to communicate?"

            "It seems so futile, and pointless."

            "Art really is not a thing for me."

            $ renpy.music.set_volume(0.1, 1.0, channel="ambient")

            scene bg gallery_exhibition
            with locationchange

            "Sae returns to her art magazine, and I make a round in the gallery, trying to see what Rin can see in her own paintings."

            "A soothing mood takes hold of the gallery surrounded by the rainstorm, the big windows making the transparent isolation feel more comfortable."

            play sound sfx_storebell
            stop music fadeout 2.0

            "A tinkle of the bell disrupts the tranquil mood."

            $ renpy.music.set_volume(0.2, 1.0, channel="ambient")

            scene bg gallery_int
            with locationchange

            show rin relaxed_nonchalant at center
            with charaenter

            "Rin pushes the door open with her shoulder and steps in."

            "I had almost forgotten that she was the reason why I came to the gallery in the first place."

            show rin relaxed_boredom
            with charachange

            rin "I think I'm ready—{w=0.3}{nw}"

            show rin relaxed_surprised
            with charachange

            "She pauses mid-sentence, noticing my presence."

            "The needle-dropping silence lasts for exactly one and a half seconds, not enough for either me or Sae to open our mouths, but enough for Rin to react."

            show rin negative_annoyed
            with charachange

            rin "I'm going for a walk."

            hide rin
            with charaexit

            play sound sfx_storebell

            "Heading back outside with a reckless pace uncharacteristic of herself, Rin seems to forget that it's still raining."

            "Without giving it any real thought, I grab my umbrella and hurry after her."

            play sound sfx_storebell
            $ renpy.music.set_volume(1.0, 2.0, channel="ambient")

            scene bg city_street4_rn
            show rain normal
            show rin negative_spaciness_close_rn behind rain
            with locationskip

            "I catch Rin around the corner, open the umbrella and lift it above the two of us while still having to almost run to keep up with her."

            "She doesn't protest me running after her nor me giving her shelter against the rain, eventually slowing her pace down so I can match it without an immediate danger of overexerting myself."

            "I relax from the rush, assessing the situation."

            "The last time I held my umbrella to guard both of us against the rain, I didn't think too much about it."

            "But now, all the things that happened since then are gathering into a freezing cold ball around my stomach."

            "Being close to her makes me uncomfortable, and I feel myself flustering slightly."

            "It's hard to get words out of my mouth, as it feels suddenly very, very dry."

            "Still, it's not like I can back off."

            hi "Why do you keep running away?"

            show rin negative_annoyed_close_rn
            with charachange

            rin "I don't want to talk to you."

            hi "I want to talk to you."

            show rin negative_confused_close_rn
            with charachange

            rin "It hurts every time I do."

            hi "Sometimes it can't be helped."

            show rin negative_sad_close_rn
            with charachange

            rin "I don't want to hurt."

            hi "Fine. We don't have to talk."

            show rin relaxed_doubt_close_rn
            with charachange

            rin "What should we do?"

            hi "Let's just keep walking."

            show rin relaxed_surprised_close_rn
            with charachange

            rin "Just walking?"

            hi "Just walking."

            show rin basic_absent_close_rn
            with charachange

            rin "Okay."

            if _in_replay:
                return

        label .the_world_only_can_you_see:
            play music music_dreamy fadein 2.0
            $ renpy.music.set_volume(1.0, 2.0, channel="ambient")
            $ renpy.music.play(sfx_rain, fadein=2.0, if_changed=True, channel="ambient")

            play sound sfx_whiteout

            scene white
            with Dissolve(1.0)

            scene ev rin_rain_away_close:
                yalign 1.0
                warp acdc_warp 20.0 yalign 0.0
            show rain normal
            with Dissolve(1.0)

            "Our footsteps go 'splish splash' in the shallow puddles forming on the streets as we walk through the rainfall."

            "Rin, now walking beside me in her unhurried and relaxed manner, doesn't seem to be even a bit bothered by the fact that she is getting wet even though she needn't to."

            "She is partially out of the protective shelter of my umbrella, despite it being more than big enough for the two of us."

            "It's as if she doesn't even notice the rain drenching her shirt."

            "…"

            "Rin's demeanor always evokes mental images of meditative calm, even when she might be in inner turmoil."

            "But I don't think that is meditation. That is just getting soaked in rain."

            "I wish I could be more calm too."

            "I've become too involved with Rin to retain my usual aloofness."

            "It feels like I have become one of those people who fool themselves into thinking they are objective, only to find out they are the worst kind of liars."

            "Illusions to fool ourselves, what better way to make one feel like a good person?"

            "It might be better to lose that illusion."

            show ev rin_rain_away_close at topleft
            show ovl rin_rain_hisaotowards_close behind rain at topright
            with charachange

            hi "I'll be going back home for some time so I thought I'd come to see you before that."

            "I could have thought of a better conversation opener, but Rin actively refusing to talk makes it hard."

            rin "That's good. I might have thought that you'd have been kidnapped otherwise."

            hi "You can't keep running away from everything. Not even from me trying to talk seriously."

            rin "I'm always serious. Also I seem to be running very slowly right now."

            rin "Maybe I should take lessons from Emi."

            "It's futile. Like talking to a brick wall that randomly spouts sarcastic nonsense back at you."

            hi "Think of your exhibition opening. What if you had run away?"

            "Rin doesn't answer to that, she just keeps walking. Or running slowly, escaping from me into her silence."

            "She has a knack for being alone in company, I've noticed."

            scene bg city_street3_rn
            show rain normal
            with locationchange

            "We head down the street, then turn left, then three times right, then left again."

            "It's like that night from some time ago, we keep choosing directions randomly because it doesn't matter where we are going."

            "All that matters is walking and the sound of raindrops drumming against the umbrella."

            "Water flows down from the roofs of the buildings and into the storm drains in wide rivers."

            "Even though I try to step over them, my feet are getting wet through my shoes."

            "We keep walking in silence that just begs to be broken again. I'm sure I am the only one feeling like this, though."

            scene ev rin_rain_away
            show ovl rin_rain_hisaotowards at topright
            show rain normal
            with locationchange

            hi "Why did you have the exhibition?"

            "Rin just shrugs sullenly and looks in the other direction. I give up at this point."

            hide ovl
            with charachangealways

            $ renpy.music.set_volume(0.5, 1.0, channel="ambient")
            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=90}It's pointless."

            n "{vspace=30}What did she want to accomplish? What she said at the night of the opening made me feel that there was something… something special she wanted."

            n "It felt to me that Rin hoped for something unattainable."

            n "She set the bar high and inside her own head she failed, no matter how much people liked her works."

            n "It's understandable to lack realism; most people do, even if not quite on the extreme level Rin takes it to."

            n "{vspace=30}But it's not a reason to live in your private world that accepts no visitors."

            nvl clear

            n "{vspace=90}You can't bend the world to fit your twisted, megalomaniac cosmology where everything works just like you want."

            n "{vspace=30}That's what frustrates me the most in Rin."

            n "{vspace=30}She wants the world to live by her rules, disregarding everything that conflicts with those as irrelevant or unnecessary."

            n "I can't believe how anyone in Yamaku could not have the bare minimum perception to understand that the world can sometimes be very unfair."

            n "I'm sure she's not the only one who wishes some things were different, but we can at least grasp the facts as they are."

            $ renpy.music.set_volume(1.0, 1.0, channel="ambient")
            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl hide dissolve
            nvl clear

            scene bg city_street4_rn
            show rain normal
            show rin negative_spaciness_close_rn behind rain at center
            with locationchange

            "I take a sideways glance at Rin, who is looking up at our dome-shaped cover. It is a poor replacement for a real sky in its monochrome bleakness."

            "The rain just keeps falling."

            "Just like the clouds today, Rin doesn't really give the feeling of wanting to be watched."

            "She sulks, in unison with the sky that she loves so."

            "I shouldn't have come. Her presence only reminds me of how angry I got because of these exact same reasons, and how those reasons probably can't ever change."

            "Even though I want to say I'm sorry, even though I don't want us to break apart, I can't bring myself to say either of these things."

            scene bg misc_sky_rn
            hide rin
            with locationchange

            "We keep measuring the rain-drenched streets one step at a time."

            "Often, when you walk with someone else, your steps become synchronized as if through some weird subconscious pact."

            "I noticed that ours never do."

            stop music fadeout 5.0
            $ renpy.music.set_volume(0.3, 3.0, channel="ambient")

            scene bg misc_sky_rays
            show rain light
            with Dissolve(3.0)

            "Time passes, and the strikes against the drumskin of my umbrella fade as the clouds above slowly disperse to reveal a cerulean blue."

            show rain:
                alpha 1.0
                linear 5.0 alpha 0.0

            stop ambient fadeout 9.0

            "Eventually the rain yields enough for me to close the umbrella, shaking the excess water off before I do."

            "While I wrestle with the mechanism, Rin stops so abruptly that I take five steps before realizing that she's not with me any more."

            "Stupid umbrella seems to be jammed."

            play music music_innocence fadein 6.0

            scene ev rin_trueend_normal:
                truecenter
                zoom 1.2 rotate -6
                easein 6.0 zoom 1.0 rotate 0
            with locationchange

            "When I turn around, I find her staring at me with an impassive face."

            rin "I wanted someone to say 'I understand how you feel.'"

            rin "Wouldn't that be great?"

            "Is that an answer to the question from before? I'm not sure."

            hi "Yeah… but why is it so important?"

            scene ev rin_trueend_sad at truecenter
            with locationchange

            rin "Because otherwise… I don't know if I can bear this."

            "I was still in the middle of folding my umbrella so I just answered something to get the conversation going, but what she says now freezes my blood."

            scene ev rin_trueend_closed
            with locationchange

            rin "If someone says a joke and laughs, you laugh with them, right? Because a joy doubled is a joy tripled, right?"

            scene ev rin_trueend_smile
            with locationchange

            rin "If someone is hurt and sad, you comfort and hug them, right? Because that way—"

            rin "…"

            "She pauses, her mouth still halfway open, then remembers to close it."

            scene ev rin_trueend_normal
            with locationchange

            "A gloom sets on her face and simultaneously on my heart."

            rin "I don't know why the right words never come out."

            rin "I don't know why I can laugh only when I make myself."

            rin "I don't know why everything stays only inside me, even when it feels like I'm going to burst."

            "Her flat, expressionless face does not waver even when she says that."

            "Her usual steady voice becomes only slightly quieter than normal."

            rin "But who… who would ever want to feel like that?"

            "Rin looks at me and I imagine the sadness reflecting from her eyes, whether it really is there or not."

            rin "I don't."

            rin "I don't want to feel like that."

            "We stay silent for a little while after that."

            "Rin because she said all she has to say at once, I because I have no clue how to process what she just said."

            "I don't understand what Rin is saying. Or I do, but I don't want to."

            "For the first time both of these things happen, and it has to be simultaneously."

            "The irony is not lost on me."

            hi "I… think everyone wants to be understood. That's universal."

            hi "But… that is impossible. Not only for me, but for anyone."

            hi "Sae said so too."

            hi "You affect other people and are affected by them, but in the end, you see everything the way only you do."

            hi "All people… are alone. We just use each other to alleviate that loneliness."

            "I wonder why I put it like that. It just felt that what Sae told me rang true, as if I had always thought like that without knowing it."

            "It feels like she articulated my thoughts in clear, simple words and that stupid story about Picasso."

            scene ev rin_trueend_closed
            with locationchange

            "Rin droops her head like a withering flower, letting her bangs fall in front of her eyes so that I can't see them."

            rin "Why do you say that when you made me feel otherwise?"

            rin "It's unfair."

            "The shaky voice that says those words does not belong to Rin."

            scene ev rin_trueend_sad
            with locationchange

            rin "I really thought you could be different. That I wouldn't have to be alone."

            "It's a bitter voice of disappointment, spoken through clenched teeth and a quivering chest."

            hi "I'm sorry…"

            rin "If you are, why do you say something unfair like that?"

            "Her demanding tone invokes no particular feeling in me, apart from sadness that has been there since yesterday evening."

            "She doesn't intimidate me at all. Not any more."

            "Rin is not a prodigal art genius, nor an unpredictable idiot savant who could tear the logic lobe of my brain into shreds whenever she opened her mouth."

            "She is just a girl that I thought I loved, a loved one who wanted to be my friend, a friend whom I let down."

            hi "I say that, because saying otherwise would feel like lying."

            scene ev rin_trueend_normal
            with locationchange

            rin "Why?"

            "Simple questions are the hardest ones. I have to close my eyes so I can focus my thoughts enough to answer her."

            hi "I'm no artist. I can never be on the same level with you."

            hi "There is a world only you can see, and to be part of it I would have to become you."

            hi "That's something I can't do, no matter how much you wish me to."

            "Rin takes in my explanation without batting an eyelash."

            rin "I'm not a real artist either."

            rin "I just paint because it makes me feel like I can really feel something."

            scene ev rin_trueend_weaksmile
            with locationchange

            "She holds her breath for a while before releasing it in a long, sigh-like flow."

            scene ev rin_trueend_closed
            with locationchange

            rin "That's why I'll do it."

            rin "I have decided. I'll do it. If even Hisao says that, then that's what I will do."

            hi "Do what?"

            "Rin starting a little shows that she had regressed into talking to herself again, but I'm glad I can snap her back even now."

            scene ev rin_trueend_normal
            with locationchange

            rin "Teacher and Sae have talked with someone who is a very important person. I got a scholarship for a big art school in Tokyo."

            rin "He said I could transfer there and start after the summer is over, if I wanted to."

            rin "I don't really get why—"

            stop music fadeout 10.0

            hi "Hold on, what? Why didn't you tell?"

            scene ev rin_trueend_smile
            with locationchange

            rin "I just did. You are the first one I told because I decided it just now."

            "She keeps her cool, looking only mildly surprised at my shocked interjection."

            "It's ridiculous how easily she can say something so life-changing."

            "I can't believe it. After what happened in February, I have had enough change for this year."

            "Even if things are going badly right now, I don't want everything to change."

            hi "But what about Yamaku? Don't you want to graduate with everyone?"

            "My plea evokes no emotion."

            rin "Everyone who?"

            hi "Emi, me, everyone!"

            "I feel my pulse rising unnervingly, and my breathing becomes fast and shallow."

            "I don't want this to happen."

            rin "Their life is not mine."

            rin "You just said that everyone is alone."

            hi "I didn't mean it like that—"

            rin "You always said that you'd have to seize the day and start living your life."

            rin "I have to live my life too."

            "Rin is twisting my words to justify running away again. It makes me angry."

            "Her ease, finality and seriousness in announcing this is unacceptable."

            "As if changing your life is something you can do on a moment's whim! No!"

            hi "How can you say that? Why don't you even try to belong?"

            "The desperate accusation has no effect. It feels like I am once again out of weapons, that I can't reach through to her no matter what I try."

            "Rin is so frustratingly absolute in her own judgment that it might make me hate her if I didn't love her, even though I don't know which way I am feeling any more."

            scene ev rin_trueend_normal
            with locationchange

            rin "Maybe I am that kind of a person. The kind that belongs only to herself."

            hi "I won't accept that."

            "Her nonchalant eyes do not seem to care whether I accept her decision or not."

            "…"

            "The pause lets me cool down, to find my sensibilities."

            "While I do, the parting rainclouds reveal a setting sun that still has time to shine its last few warming rays before calling it a day."

            "A mosaic of light and shadow spreads on the walls of the buildings, on the street and the fence circling a park on the other side of the street."

            "Rin's shadow is long enough to reach my feet."

            "It's like one of those western movies, with two cowboys staring each other down, ready to sling their guns at each other."

            "The one who loses his nerve will eat lead."

            "I realize I would have the disadvantage because the sun is behind Rin, stinging my eyes."

            scene ev rin_trueend_sad
            with locationchange

            rin "Do you hate me?"

            "She draws first and I have no counter."

            hi "I don't know."

            "Did I lose?"

            hi "Even if I did, what would it matter?"

            "I scramble for words, words that could salvage this. I find none."

            hi "You are my friend, I promised you that. I am not the kind of guy who forgets about promises."

            hi "I think that is the most important thing. We could try to—"

            scene ev rin_trueend_normal
            with locationchange

            rin "Don't say it."

            scene ev rin_trueend_hug
            with locationchange

            play music music_friendship fadein 4.0

            "Predicting what I was going to say, Rin throws herself into my arms, pressing her body against mine."

            "I feel her rising to her tiptoes to match my height and snuggle closer."

            "The scent of her hair is that of rain and paint thinner. Her body feels as cold as always. Her breathing against my neck is as hot as always."

            "It's funny how all of those feel so familiar even though Rin, as a whole, does not."

            scene ev rin_trueend_hugclosed
            with locationchange

            rin "Are you sure you can't hate me?"

            "Rin whispers into my ear so close I can feel the movements of her lips against my earlobe."

            "It's teasing, taunting. If this was some other kind of situation I'm sure it would tickle tantalizingly and I would giggle even though I'm a guy."

            rin "It would be easier if you did."

            hi "Dunno. It's pretty hard when you are hugging me like that."

            scene ev rin_trueend_sad
            with locationchange

            "I wonder if it's because of my sullen voice, but she takes a step back, looking wistfully at her short arms."

            "I wish she hadn't done that."

            rin "I can't hug anyone, Hisao."

            rin "I'm a bad person like that."

            scene ev rin_trueend_normal
            with locationchange

            rin "That's why I have to go."

            "She disarms me completely with three simple sentences, rendering me unable to argue any more."

            "And since I can't, Rin is free to continue as she wills, shifting her weight from one foot to the other before she does."

            scene ev rin_trueend_smile
            with locationchange

            rin "I will learn to hug people in my own way."

            rin "I'm sure I can become a real artist."

            rin "But if I do… I might not be able to be me any more."

            "The hint of a smile on her lips is a betrayal, a false sign of self-confidence in a future that even Rin can't foresee."

            "I'd want to interpret it as a sign of hope, but I know better."

            "Rin just keeps smiling that awkward, forced smile of hers."

            rin "That's why… please forget about me, and I will forget about you too."

            rin "I'm sure that—{w=0.5}{nw}"

            scene ev rin_trueend_sad
            with locationchange

            "She chokes in the middle of saying something I would never come to hear."

            "I don't think I'd wanted to hear it anyway."

            "This is not fair."

            "Rin is not joking. Rin is always serious. But I can't accept it, I can't."

            "Forget about you? How could I ever…?"

            "That's what I'd like to say. But I don't know how I would continue. I can't come up with anything good to say, so I have to challenge her."

            hi "How can you say such a thing?"

            scene ev rin_trueend_normal
            with locationchange

            "Rin raises her eyes to meet mine, they are serious and deep, a perfect image of the uncharted territory I always thought they were."

            "Even now, I can't read her emotions from those unblinking, jade irises that never could reflect what they saw."

            rin "It's easy. After all, I am good at forgetting things."

            "…"

            "Her unfairness is choking my throat, but I manage to utter the question burning my mind."

            hi "So, is this it? Is this goodbye?"

            "…"

            "Rin kept looking at me gently, without answering my question."

            "From her eyes I could see that she didn't even need to say anything."

            "There were no more words for us."

            stop music fadeout 12.0

            scene ev rin_trueend_gone
            with locationchange

            "She turned around and walked off without looking back."

            "All around me, the world kept changing, little by little, but I was left standing there."

            show ev:
                "ev rin_trueend_gone_ni" with Dissolve(10.0)

            "The sun dropped below the horizon, casting long and thin shadows across the street."

            "In the waning light, Rin's distancing back seemed to be like from a faraway dream."

            "The gap between us grew slowly."

            "The ripples on the puddles she stepped on expanded until they met the limits of their tiny existence and disappeared without a trace."

            "Her words stayed frozen deep inside my heart."

            if _in_replay:
                return
    else:
        label .desperate_glory:
            call separate_of_dg_and_wl

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=30}Vacation, huh?"

            n "Some people will stay at the school even over the holidays, some will go back to their families."

            n "I don't know what to do. I should go buy a train ticket for my trip back home, but I can't bring myself to do it."

            n "I bet I'm going to get a call from home again. Mom's going to pester me about when I'm coming back, and I'm not going to know what to answer."

            n "{vspace=30}This is really lousy. In the current state of things with Rin, it feels like I can't just bail out of here and pretend we are through."

            n "{vspace=30}And now, she has other problems of her own. I thought that the exhibition opening would give her a breather, but I was sorely mistaken."

            n "{vspace=60}The tangle just seems to thicken."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl clear
            nvl hide dissolve

            play sound sfx_doorknock

            "A sharp knock on the door interrupts the quiet but frantic mood of the last 15 minutes of the exam."

            show muto normal at center
            with charaenter

            $ renpy.music.set_volume(0.2, 0.0, channel="sound")

            mu "Come in."

            stop music fadeout 1.0
            $ renpy.music.set_volume(1.0, 8.0, channel="sound")
            play sound sfx_footsteps_hard

            show bg at bgleft
            show muto at twoleft
            with charamove

            show nomiya serious at tworight
            with charaenter

            "The opening door reveals the art teacher, who steps in with his jacket swirling around him as though in a gust of wind."

            "He glances at Mutou, who glances back at him."

            play music music_tension

            show muto irritated
            show nomiya stern
            with charachange

            "A frown spreads simultaneously on both of their faces as the men measure each other with their gazes."

            no "Excuse me, could I borrow Mr. Nakai for a moment?"

            mu "Excuse {b}me{/b}, Mr. Nomiya, but we are in the middle of an exam here."

            "A chilly atmosphere suddenly spreads in the middle of the summer afternoon as the two men try to stare each other down."

            show nomiya serious
            with charachange

            no "This is urgent, and it seems that Nakai has already finished."

            "Both men turn to look at me, staring at me like a pair of basilisks trying to petrify a tasty snack."

            "It's true that I've been idle for a good while now, so Nomiya is right, but…"

            show muto normal
            with charachange

            mu "Nakai, would you like to check your answers one more time?"

            "Mutou speaks with an odd intonation, weighting certain words as if trying to send a message."

            "The pressure from their stares makes me rapidly shake my head, which is apparently interpreted as an answer of some sort."

            stop music fadeout 6.0

            show muto irritated
            with charachange

            mu "Very well. Nakai, go with Mr. Nomiya, if you please."

            mu "Take your bag with you and bring your test paper to my desk."

            show muto smile
            with charachange

            mu "You have a nice vacation."

            hi "Umm. Er, you too, teacher."

            "The entire world… well, at least the classroom seems to hold its breath just for me, putting the exam on hold until I stand up, collect my stuff and walk to the door."

            "I can feel the stares in the back of my neck. My classmates probably think I'm in for some detention or something, on the last day of the school before summer vacation."

            "I don't know what the teacher wants from me, but I can guess it probably is not detention and also that it probably has something to do with Rin again."

            scene bg school_hallway3
            with locationchange

            play sound sfx_doorslam
            with vpunch

            "Nomiya doesn't take me anywhere, contenting himself with the hallway as it's completely abandoned."

            show nomiya serious at center
            with charaenter

            play music music_pearly fadein 1.0

            no "Do you know where Tezuka is?"

            "So she is trying to avoid the teacher… par for the course, probably."

            "I wonder if she realizes that she can't avoid dealing with this indefinitely."

            hi "I have no idea."

            hi "You have probably asked in her homeroom next door."

            show nomiya stern
            with charachange

            no "Of course I have! I have searched every nook and cranny of this blasted school and the girls' dorm."

            no "You are the last one to see her since yesterday and you are her friend."

            show nomiya serious
            with charachange

            no "Work with me here. Aren't you worried?"

            "I am, but I don't know what I could do."

            "Rin did something incomprehensible yesterday, even for her."

            "She seemed really confused."

            hi "Maybe she just wants some time to think then. I got the feeling that she had second thoughts about having that exhibition."

            "Or something. She really didn't explain what was wrong."

            show nomiya frown
            with charachange

            no "What second thoughts?"

            hi "I dunno. Just got that feeling."

            "I am being a little dishonest with the teacher, but this is not something I should be meddling with."

            "He came to me… yes, why? Maybe he thinks I'm some kind of confidant of Rin's, but I don't think I can help with this matter."

            show nomiya serious
            with charachange

            "The teacher huffs and scratches his head in confusion."

            no "What's up with that girl? This is so unlike her, she's always been so goal-driven."

            "'Goal-driven?' Those don't really strike me as words to describe Rin with."

            "To me, she always felt obsessive at best."

            hi "Er, I don't mean to be rude, but wasn't it you who pushed Rin to that direction in the first place?"

            show nomiya dreamy
            with charachange

            no "Her goal is my goal. That is a mentor's job."

            hi "I guess so. I just don't know if painting can make her happy."

            show nomiya stern
            with charachange

            no "That's pretty preposterous of you to say, Nakai."

            "He suddenly sounds pretty irate. Did I say something stupid?"

            show nomiya serious
            with charachange

            no "You don't understand, do you? It is not a question of happiness. For every gain there is a sacrifice to be made."

            show nomiya stern
            with charachange

            no "There is no free lunch, but could I… would I let that girl waste away her talent if she has a moment of doubt? Never!"

            no "Painting is work just like any other. Tezuka might make it look like child's play to you, but she works hard every day to make her art."

            no "To become extraordinary, one has to make an extraordinary effort."

            "The more the teacher talks, the more I feel that Rin doesn't think like that, even though I have no idea how she thinks."

            show nomiya serious
            with charachange

            no "I can very well understand why she would sacrifice her summer vacation and make up for the lost classes and exams to get a chance at showing her art."

            no "This is the path she has taken, and to go all the way, that's not easy."

            no "I know she is young, and things are hard for her just like for all the kids here in this school, but that's no excuse."

            "He is finished."

            hi "But—"

            show nomiya smile
            with charachange

            no "Do you have anything like what art is to Tezuka?"

            hi "No…"

            "That's right. I have only vague ideas of my future, no goal to shoot for, no dream to blindly reach for."

            "I joined the art club in search of something I could be interested in, to get inspired by."

            "Did I find something like that?"

            "All I found in the end… was Rin."

            hi "No, I don't have a passion like that."

            show nomiya serious
            with charachange

            no "Then you can't understand."

            "His flat statement allows no counterargument."

            hi "But… she might not understand even herself."

            "Still, I carry on arguing, out of spite if for nothing else."

            show nomiya stern
            with charachange

            no "How could she not? She's been at it so hard for the past few weeks that she put off even coming to school, not to say anything about attending class. Don't be ridiculous."

            "I don't think I'm being ridiculous, but as I have no rebuttal, Nomiya seems to consider this one his win."

            show nomiya smile
            with charachange

            no "At any rate, the opening was quite successful despite Tezuka hardly showing up."

            no "Many people were interested in her work and one piece was even sold for a reasonable price."

            hi "Well, that's nice isn't it?"

            show nomiya veryhappy
            with charachange

            no "Yes, it's fantastic news! I hoped that Tezuka would come to her senses when she heard about this, but…"

            "He sighs and takes off his glasses, cleaning them against his jacket before putting them on his nose again."

            show nomiya smile
            with charachange

            no "At any rate, I should be going. There is this mess to be settled with Sae and everyone."

            no "If you see Tezuka, please ask her to come see me. Otherwise, have a nice vacation."

            hi "Thanks…"

            stop music fadeout 6.0
            play sound sfx_footsteps_hard
            $ renpy.music.set_volume(0.0, 4.0, channel="sound")

            hide nomiya
            with charaexit

            "After he has disappeared around the corner, I ponder where Rin could really be."

            "It feels like she has not one, but at least half a dozen of these 'secret places.'"

            "I balance between the desire to solve this tangle and to drop it for good."

            "The disused classroom is just a few feet away."

            "What to do?"

            "…"

            $ renpy.music.set_volume(1.0, 0.0, channel="sound")
            play sound sfx_dooropen

            scene bg school_room34
            with locationchange

            "As I push open the door, only the shadows greet me from the inside."

            hi "Hey there."

            if _in_replay:
                return

        label .problems_of_self_referential_logic:
            scene bg school_room34

            show rin negative_spaciness
            with charaenter

            play music music_drama fadein 6.0

            "She's standing in the middle of the sunlit room, peering through the gaps of the curtains out into the yard."

            "Like so often before, she doesn't start or jump, just calmly waits for me to make the first move."

            "It's as if she is trying to become a permanent part of the furniture."

            hi "The teacher is looking for you."

            "A blank look over her shoulder is all I get, accompanied by a cryptic nonexpression on her face."

            rin "Are you looking for me too?"

            hi "Nah, I already found you, didn't I?"

            rin "Did you?"

            show rin negative_annoyed
            with charachange

            "She furrows her brow, looking so puzzled that it makes me wonder if the question was asked in all seriousness."

            "Maybe it was."

            hi "Are you talking metaphorically now?"

            show rin negative_spaciness
            with charachange

            rin "Do you mean like eels, caves and dark, stormy nights?"

            show rin negative_sad
            with charachange

            rin "I am bad at talking like that."

            "…"

            play sound sfx_doorclose

            "The abruptly-ended greetings give me the chance to close the door behind me and sit down on a dust-covered desktop."

            show rin basic_absent
            with charachange

            "Rin stays standing, but at least she turns around."

            "I soon wish she didn't though, so oppressive is her expectant stare."

            "This is her place and I'm an intruder, although a tolerated one. Despite that, she still waits for me to say something."

            "If I only knew what."

            "…"

            "The sunlit silence presses me towards decisions."

            "I came here without really thinking what I would do, apart from delivering Nomiya's short message in case Rin was here."

            "She was, and now I don't know what else I want to say… what else I should say?"

            "I hover between my two options for a moment."

            "Rin being troubled troubles me too. It's a surprising revelation, almost as big as realizing that she really is troubled was."

            "Nothing I can do would probably help, and I might be partially to blame too."

            "Does it mean I should just wash my hands of her?"

            "Didn't think so."

            hi "So… what's wrong?"

            "…"

            show rin relaxed_nonchalant
            with charachange

            rin "Nothing."

            "She starts to turn away again, as if trying to physically exit a conversation she doesn't want to have."

            hi "Rin, stop trying to dodge me or I'll leave."

            show rin relaxed_boredom
            with charachange

            rin "Okay."

            hi "Do you want me to leave?"

            show rin relaxed_doubt
            with charachange

            rin "Are you still angry?"

            "It took us - or was it only me? - ten seconds to swamp the conversation into this."

            "I wish we could erase the past, or failing that, forget all about it."

            "I've wished for that more than once in the last few months."

            hi "Let's put that aside for the time being, all right?"

            show rin basic_absent
            with charachange

            rin "If you say so."

            hi "I do. So… what's wrong?"

            hi "Sae and Nomiya were not too happy that you just ran off yesterday."

            hi "You left them in quite a pinch, and I suppose the teacher wants some kind of an explanation."

            hi "It seemed like you just threw out everything you had worked for. And I don't get why."

            show rin basic_deadpanupset
            with charachange

            rin "Did I make a mistake?"

            "My reprimanding and her flat answer go so much against the usual expectations and presumed interactions that it might just as well be somebody else talking."

            "Neither of us is like we used to be, this stiff, constricting feeling I get every time I look at Rin nowadays seems to be mirrored in her own behavior."

            "I hate things that go irreparably wrong. Ever since February, I have hated them."

            "What can I say?"

            "Her question is trailed by a compelling, quizzical stare that makes me sigh and frown."

            "Conversations nobody wants to have are the worst."

            hi "I don't know. I mean, it's not the end of the world but it probably was pretty stupid."

            show rin relaxed_nonchalant
            with charachange

            "She responds with a sigh of her own, although hers is not nearly as heavy as mine was."

            show rin relaxed_sleepy
            with charachange

            rin "I just couldn't do it."

            hi "But… why? What's wrong?"

            show rin negative_annoyed
            with charachange

            "A pause, a furrowed brow, a quiet voice."

            rin "Let it be, Hisao."

            rin "I don't think I can really explain it in a way that would make sense."

            "Yeah, Rin doesn't want to have this conversation either. That may be for the better."

            "But how rare of her, to admit that even she has some kind of limits."

            "I always thought Rin was all but ignorant of her tendency to get distracted, so much that she inadvertently obfuscates everything she says."

            "…"

            hi "You never explain {b}anything{/b} in a way that would make sense."

            show rin basic_absent
            with charachange

            rin "Nobody else has ever asked me to."

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "I guess that's how it is."

            n "But I always wanted to make sense of you, to find out who you are."

            n "I still want to, can't you see?"

            n "…"

            n "I know you can't."

            n "But I do."

            n "Is that why I keep this up? It pains you as much as it pains me. It's unlikely to be of any use to either."

            n "We did things and said things that can't be undone."

            n "It's as if… you and me being close to each other just hurts us both, but we still deliberately keep doing it."

            n "Isn't that silly?"

            n "Even now, I can see how you force yourself to respond even though you owe me nothing."

            n "Even if it's hard to talk about things like this."

            n "Why?"

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl hide dissolve
            nvl clear

            hi "Why is it that you paint?"

            show rin basic_awayabsent
            with charachange

            rin "I… because I don't know what else I could do."

            rin "It's like this feeling that there is no choice, that it's the only possibility."

            show rin basic_sad
            with charachange

            rin "Like when there are only watermelon-flavored popsicles left in the store but you need to eat a popsicle."

            "Her poor metaphor aside, she didn't really answer anything. If possible, this makes even less sense than not knowing."

            hi "But… if you don't want to paint…"

            show rin negative_spaciness
            with charachange

            rin "Not like that. You had to come to this school even though you probably didn't want to have a heart attack."

            show rin negative_annoyed
            with charachange

            "She pauses, frowning as if something in what she said didn't please her."

            show rin basic_lucid
            with charachange

            rin "At least I think you wouldn't."

            "Her careful follow-up is followed in turn by another, shorter pause with another, smaller frown."

            show rin basic_deadpanupset
            with charachange

            rin "Would you like to have a heart attack?"

            hi "No, I wouldn't and I didn't want to."

            show rin basic_deadpansurprised
            with charachange

            rin "But you're doing fine, aren't you? Or are you still sad about it?"

            "Rin's question makes me realize that I haven't really thought about my illness for weeks."

            "Aside from chugging down my medication every day there has been no need to concern myself with my broken heart, which I'm only thankful for, really."

            "Getting to know new people, a new school, a new town… a new life, it all has caught me and made the past fade away."

            hi "No… heh, I guess even I can't dwell on the past indefinitely."

            show rin basic_awayabsent
            with charachange

            rin "See? Even watermelon doesn't really taste bad if you have to eat it."

            "Her half-nonsensical closure seems to put an end to the subject in Rin's mind, so I just nod in uncertain confirmation."

            "…"

            "…"

            "There are two kinds of silences: awkward ones that you want to break, and comfortable ones that you don't mind."

            "The first kind is bad, because it makes your thoughts go awry. Like mine do, now."

            "Looking at Rin makes me feel bad."

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=30}I don't want to feel like this."

            n "Looking at Rin makes me feel… exhausted. I really tried my best, she tried to… I have no idea."

            n "But we ended up like this, and she ended up screwing up her exhibition opening."

            n "It feels like we are at a dead end."

            n "There is no direction to continue to."

            n "I reached out for her yesterday, thinking it would be the last time."

            n "She walked away."

            n "'I want to be me.'"

            n "What the heck does that even mean? Rin, if anyone, is most definitely herself."

            n "I feel kinda relieved that I am not the one to blame, but this still grates on my mind."

            n "Why did she run away? It didn't make sense yesterday. It doesn't make sense today."

            n "The things she said feel like they should make sense but they just don't, to me."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl hide dissolve
            nvl clear

            hi "You know, about that thing you just said…"

            show rin basic_absent
            with charachange

            rin "Which one of them?"

            hi "Umm… painting… Sae said something like that to me before… that a true artist does not paint because she wants to, but because she {b}must{/b}."

            hi "And I've been wondering about what she said. Why do artists {b}have{/b} to paint?"

            "My question is probably pretty stupid. At least Rin looks at me in the blank way that seems to say so."

            show rin basic_deadpannormal
            with charachange

            rin "I don't know. Am I an artist?"

            hi "Well, you paint stuff and you have an exhibition too. I'd say you qualify."

            show rin basic_deadpancontemplation
            with charachange

            rin "I think I still don't know, but okay."

            "The thinking pause that follows seems to last for half an eternity."

            "Unlike most people, Rin doesn't flavor her thinking pauses by body language or saying 'like' or 'umm' or anything."

            "I've noticed that I might prefer her way. The usual way even annoys me, as if people were so infatuated by the sound of their own voice they just have to keep making some noise even when they are just thinking what they could say next."

            "Rin just… comes to a full stop while she is thinking. It's disconcerting, because reacting to people spacing out is always hard, but she comes off as less obnoxious."

            show rin basic_lucid
            with charachange

            rin "I think I want someone to see what's inside me. Not the way doctors and serial killers do."

            show rin basic_absent
            with charachange

            rin "The way that doesn't make me feel lonely."

            show rin relaxed_boredom
            with charachange

            rin "This is what you call metaphorical, you see."

            hi "Please don't lecture me about self-evident things."

            show rin basic_deadpansurprised
            with charachange

            rin "It's not self-evident that this is self-evident."

            hi "So, you present a painting to someone and expect him to magically see a glimpse of your soul?"

            show rin negative_angry
            with charachange

            rin "It's not like that. It's just a little like that but not really. Don't you understand?"

            hi "I do… and I don't."

            hi "You know, I feel a little bit of despair every time you ask that question."

            show rin basic_absent
            with charachange

            rin "What question?"

            hi "About whether I understand you or not."

            "She seems almost surprised at my clarification."

            show rin basic_lucid
            with charachange

            rin "Oh, it's not really a question. It's one of those kind that you don't have to answer."

            hi "Rhetorical."

            show rin basic_absent
            with charachange

            rin "Yeah, that's the word, a question that is not a question is a rhetorical question. How nice."

            rin "That reminds me, it doesn't really make sense. What kind of a question is one that isn't a question?"

            hi "A rhetorical one."

            rin "What kind of an answer is an answer that doesn't answer anything?"

            hi "Is that a rhetorical question?"

            show rin basic_deadpanupset
            with charachange

            rin "You are not funny."

            show rin basic_awayabsent
            with charachange

            rin "But if you don't like it, would you like me to say something else instead?"

            show rin basic_lucid
            with charachange

            rin "I don't have any good ones though. How about… 'Your pants are on fire?'"

            show rin basic_absent
            with charachange

            rin "This can be our secret language."

            "Rin's honest-to-goodness silliness, made twice more ridiculous by the fact that I know she is dead serious, derails me like it always does."

            "It's like some kind of a safety lock to prevent me from becoming too much of a worrywart, dragging even my own thoughts off the ground where they should be."

            "It makes me smile confusedly, but only on the inside."

            "Even though the corners of my mouth are not drawing into a grin, I'm still impressed by her ease of wrecking any attempt at being too serious."

            "Could she (should she will so) forget and ignore things that bug her, things that bother her?"

            "Could she (should she will so) be free of whatever burden being her means?"

            "Or am I the only one who feels burdened by being myself?"

            hi "No thanks."

            hi "But still, the times when I feel that I am on the same page as you are pretty rare."

            hi "It feels like… there is this huge gap and sometimes you just go to the other side, and I don't… have any way to reach to you from where I am."

            hi "It's like you are in some completely different place at times."

            hi "Even though you are right here."

            "That's right."

            "There is an insurmountable discontinuity, an imaginary glass wall that blocks comprehension from happening."

            "There might be such a gap between any two people, but with Rin, it feels more tangible."

            "Rin does not react to my thoughts, not to the ones I uttered aloud nor the ones I did not."

            hi "It's even worse with art."

            hi "I'm not very good at art, I admit it."

            hi "I joined the art club 'cause I thought it could be interesting."

            hi "And I guess it is. I like art, I like your art too, but just like with you, I can't comprehend it."

            hi "And I'm pretty sure nobody really can."

            show rin relaxed_doubt
            with charachange

            "This seems to worry her slightly."

            rin "Do you think so?"

            hi "Yeah. I guess that art is meant to be interpreted, not understood. That's how I'd put it."

            show rin relaxed_sleepy
            with charachange

            rin "That's a sad thought."

            hi "I guess it might feel like one."

            hi "Does it make you feel sad for yourself?"

            show rin basic_lucid
            with charachange

            "Rin thinks about this for a while, and then shakes her head surprisingly vehemently."

            show rin basic_deadpannormal
            with charachange

            "The first thing she focuses her eyes on afterward is me."

            "Both of these things make me glad, and relieved."

            hi "That's good, isn't it? Anyway, you should go see the teacher and apologize properly."

            hi "I think he is worried about you."

            hi "Can you do that?"

            show rin basic_absent
            with charachange

            "This time, she nods her head."

            stop music fadeout 4.0

            "Only, it's not as vehement."

            if _in_replay:
                return

        label .measuring_shadows:
            scene bg school_hallway3
            with locationchange

            "The hallway is empty, almost intimidating."

            "Nomiya's 'office' is the art classroom at the other end of the third floor hallway."

            show rin basic_absent at center
            with charaenter

            "Our steps echo disturbingly. The atmosphere is unlike on a normal afternoon. It feels like the school knows that nobody will be coming back for a month, too."

            "The door is open, but not very inviting."

            hi "I'll… um, wait outside."

            show rin relaxed_nonchalant
            with charachangealways

            pause 0.2

            show rin:
                ease 1.0 tworight alpha 0.0
            with Pause(1.0)

            hide rin

            "Nodding barely noticeably, Rin strides in without stopping, and naturally, without knocking."

            "Maybe that's why it takes a few seconds before I hear the teacher's voice from inside."

            no "There you are!"

            rin "Hello."

            "A conflict arises: should I stay here or go somewhere else?"

            "I'm not sure if I even want to eavesdrop on them."

            "…"

            show bg at right
            with charamove

            "Manners lose to curiosity, and so I stay close enough to listen in."

            "Their voices echo in the hallway, but no matter."

            "There is nobody around, save for me."

            play music music_tragic fadein 8.0

            no "Dear girl, what on Earth were you thinking, leaving like that on the big night?"

            rin "I couldn't say anything."

            "Compared to Nomiya's scolding tone, Rin sounds awfully quiet and withdrawn."

            "Her words seem to drown under his."

            no "I have to say, I am very disappointed in you, Tezuka."

            rin "It was no good at all."

            no "Never mind all the things I did for you, but what about Sae? What about all the guests who wanted to meet you?"

            rin "There was nobody. Even Hisao…"

            no "You have embarrassed us very badly, Tezuka."

            no "Reputation is what counts, surely you know that?"

            rin "It's all right. I don't need it."

            no "'Don't need!' What do you think you know?"

            "Rin's replies only seem to agitate the teacher more, his voice rising with every sentence."

            no "The path of an artist is a thorny one, I'll tell you that! Thorny!"

            no "You have to see the big picture! There will be bad times and good times!"

            rin "Things are like they are. It'll be all right even—"

            no "You might now think that it's oh so wonderful and easy, but how far would you have gotten without me?"

            no "I won't always be there for you!"

            no "When you lie on the floor of your minuscule room, your rent three weeks late, your mind blank for the fourth week straight, then you will wish that you had listened to old Nomiya a bit more."

            no "When you keep measuring how the shadow of your chair becomes longer over the spring because that's all your lethargy allows, maybe that's when you will start caring about your career!"

            rin "That doesn't matter."

            no "Your resolve is not enough."

            rin "I am not a resolved person."

            no "You are not a resolved person…"

            play sound sfx_impact2
            with vpunch

            no "Then tell me, why… why… WHY DID WE GO THROUGH ALL THIS TROUBLE IF IT AMOUNTS TO A MOSQUITO'S SHIT?"

            "Oh dear, the teacher blew a fuse."

            "Him yelling at Rin makes me feel bystander's guilt. If I had gone with her, maybe he wouldn't have gotten so angry."

            "If I had not let her run away, he wouldn't have gotten angry in the first place."

            "I still could go and save her… I don't think I can."

            "I was the same. I yelled at Rin too, and I'm feeling all the more embarrassed about it now."

            "I felt justified to vent my anger at her face just because… just because I felt it was her fault that I was so frustrated."

            "I was no more justified than the teacher is."

            "…"

            "A terrible silence sets upon the hallway."

            "Rin does not have anything to say to Nomiya."

            "Whether she has run out of answers or she knows that arguing would only make him angrier is anyone's guess."

            "The teacher has nothing more to say either, it seems, or maybe he just ran out of breath."

            "For a moment, I imagine the two of them just staring at each other, one full of red-hot anger, the other full of… yes, what?"

            "I can't tell how Rin feels, not before, not now."

            "Teacher seems to expect Rin to say something too, but since she doesn't he finally continues in a quieter, but not less angry voice."

            no "What worth is there in doing so much work if the outcome is… nothing?"

            "Still, Rin will not say anything."

            no "I'm sorry. I shouldn't have gotten so excited."

            "He does not sound sorry at all. Rather, his tone is cold and sharp, like he was spitting the words out of his mouth."

            no "It seems that I was expecting too much. You are not an artist after all."

            "Yeah, not sorry at all."

            show nomiya serious:
                tworight
                alpha 0.0
                parallel:
                    linear 1.0 center
                parallel:
                    linear 0.4 alpha 1.0
                    0.2
                    linear 0.4 alpha 0.0
            with Pause(1.0)

            hide nomiya

            stop music fadeout 4.0

            "He storms out of the club room and down the stairs without noticing me."

            "After he is gone, I peek carefully inside the classroom."

            scene bg school_nomiya at right
            show rin basic_awayabsent at center
            with locationchange

            "Rin is left standing there, in front of the teacher's desk."

            show rin negative_spaciness
            with charachange

            rin "I couldn't say I am sorry."

            "She says it into the humid air of the classroom, not to me."

            "But since the room won't answer her, I will have to."

            hi "That was unfair of him… He was angry, but still…"

            "I can't decide how to end my sentence. Disdaining the teacher feels like disdaining my own behavior from two days ago."

            "Stupid, but correct in hindsight."

            show rin negative_spaciness_close
            with characlose

            "Rin won't answer, staying petrified where she stands, so I walk up to her."

            "She stood up for herself. In a way. I didn't expect that."

            "I can't determine whether it's unbecoming or not, but either way, she did it."

            "Against me, she never did."

            "I sort of wish she had, maybe I would not feel this bad then."

            "Lately, it really seems that I've been wishing for all kinds of things."

            hi "Rin?"

            show rin negative_annoyed_close
            with charachange

            rin "Go away."

            if _in_replay:
                return

        label .raison_detre:
            scene bg school_nomiya at right
            show rin negative_annoyed_close at center

            play music music_sadness fadein 6.0

            hi "Why… what are you saying?"

            show rin negative_angry_close
            with charachange

            rin "You're angry with me too, right?"

            rin "I thought you were my friend. I thought he was, too."

            "Her voice is unlike I've ever heard it, it's bitter, sharp like needles, and she keeps staring pointedly at her toes."

            hi "I don't think it's about that."

            hi "He wanted you to be something you are not. And…"

            show rin basic_surprised_close
            with charachange

            "I take a deep breath and finally catch her eyes in my own, locking our gazes."

            hi "…I'm sorry. I wanted us to be something else too… more than friends."

            hi "Maybe that's why I couldn't contain myself and became so frustrated, just like the teacher did."

            show rin relaxed_doubt_close
            with charachange

            rin "What more? There is nothing more to me than me, that's all I am. I don't understand that."

            "Well… the answer should be obvious, right?"

            "I remember myself, thinking of the purpose of friendship. To put up with everything and anything, to be there for your friend."

            "Did I fail as a friend, thinking it could be a stepping stone for something else?"

            "Maybe because of those thoughts, I didn't manage to put up with things, to keep it together."

            "As outrageous as Rin is and was, I shouldn't have let myself get caught into that, especially when I started feeling the way I did towards her."

            "So, did I fail?"

            "That's what her eyes seem to ask."

            "…"

            hi "I'm sorry, Rin."

            hi "I might not be able to be your friend."

            hi "I don't think I could ever be a good friend to you."

            "I say these things because they are true, not because one of us would like to hear them."

            "But they are something that must be said."

            "The finality of my words creates a shaking silence, for what could either of us add to that?"

            "…"

            show rin negative_confused_close
            with charachange

            rin "Why? Why does all this happen?"

            show rin negative_sad_close
            with charachange

            rin "People are doing things I don't ask for and don't want and everyone keeps getting angry at me, I have no idea what is going on any more and can't stop feeling like I want to run away from everything…"

            show rin basic_lucid_close
            with charachange

            "She shuts her eyes tight and breathes out deeply, calmly."

            show rin basic_upset_close
            with charachange

            "When the eyelids open, all I can see is dark green desperation."

            rin "{b}I have no idea what's wrong with me!{/b}"

            "Her frenetic outburst stupefies me for a moment, and for a heartbeat we just gaze into each other's face."

            "Seeing her confused eyes desperately looking for answers from mine only makes me sad, because I know I have none."

            hi "I don't know either."

            hi "But you know, you yourself said that things are not right nor wrong."

            hi "They just are."

            hi "You either accept them, work to change them or give up."

            hi "It's not that I hate you, or that teacher Nomiya does."

            hi "I just… think that I am the kind of person who gives up when he feels he can't go on."

            hi "And even if you hate it, this… this is… how things are."

            "I'm saying pretty cruel things but I can't stop myself, the words keep rolling off my tongue with slow, hard certainty."

            show rin basic_surprised_close
            with charachange

            "I can see them hitting Rin almost like physical blows."

            "As the wetness gathers into the corners of her eyes, they are still wide with the shock of rejection."

            show rin basic_crying_close
            with charachange

            "As the tears start rolling down her pale cheeks, she does nothing to stop them."

            "As they fall down on the floor one by one, she stands still, staring at me with a gaze full of hollow disbelief."

            rin "…"

            "But reality catches up."

            show rin negative_crying_superclose
            with vpunch

            "Rin slumps forward as if she was deflating, and buries her face as deep in my shirt as she can."

            "Rin is heavy and featherlight when I support her weight."

            "She doesn't really sob or bawl, just leans against me, letting her tears burn through my shirt into the skin underneath."

            "And I let her, bringing my hand around her shoulders in a clumsy hug that does no good to comfort her."

            "I can feel Rin's vertebrae against my fingertips, like hard and jagged reminders of how messed up things are."

            "Her slim shoulder quivering against my palm is a pitiable sight, and the hopelessness of being part of the cause for Rin's sadness keeps shredding my heart."

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=120}To make a girl cry is the most despicable thing to do."

            n "{vspace=30}Even Rin. Especially Rin."

            n "{vspace=30}Behind that veil of aloofness, Rin is just a human being too."

            n "Just as confused, scared and lost as any of us is."

            n "Most of the time it seems that there is no rhyme or reason for what Rin does and says, but for once, I think I really understand how she feels."

            n "{vspace=60}But no words can express it, and no words can make it better."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl clear

            show bg:
                "bg school_nomiya_ss" with Dissolve(8.0)
            show rin:
                "rin negative_crying_superclose_ss" with Dissolve(8.0)

            stop music fadeout 5.0

            n "{vspace=150}So wordless we stay, quietly waiting for her tears to run out."

            n "Time passes agonizingly slowly, even the lazy specks of dust floating in the air seem to pause into a standstill."

            n "The obligatory wall clock is ticking distractingly from above the door."

            n "I decide against counting the seconds, because it would make them feel longer."

            n "{vspace=60}…"

            play music music_serene fadein 9.0

            nvl hide dissolve
            nvl clear

            show rin basic_crying_superclose_ss
            with charachange

            "Eventually Rin stirs a little and still smothering herself against my chest, mutters into my shirt."

            rin "Let me be here for a while."

            show rin negative_crying_superclose_ss
            with charachange

            rin "Please, Hisao."

            rin "Just give me a little while."

            "A soothing deluge spreads into my consciousness, the knowledge that while being here for Rin is all I can do for her, that's all she wants right now, even after all we've gone through."

            hi "Sure."

            "So she stays there."

            "But I still can't bring myself to draw her closer so I could embrace her properly."

            "It's because doing it would just make me so sad that I don't know if I could bear it."

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=60}The realization that we might never really be able to become what we want to be for the other crystallizes into my mind as a diamond-hard enlightenment."

            n "A pang surges through my heart like an electric shock."

            n "It's painful."

            n "This clarity… hurts."

            n "What can we be for each other? What meaning is there for us to desperately cling to each other even though it seems so futile?"

            n "What should I say to Rin? How can I make her feel better?"

            n "I do not know any of those things, and I fear knowing them would only hurt more."

            n "Forcefully, I push all of that out of my mind because I don't want to be thinking of hurtful truths."

            n "My thoughts calm down soon enough, the sadness disperses until all that is left is me and Rin and the tender feeling of her warmth and softness against my chest."

            nvl clear

            n "{vspace=60}When did I fall in love with her?"

            n "I can't remember, but I'm certain it was way before the warm touch of her lips on my own, on that orange-colored afternoon when she was sick with cold and I went to see her because of unclear reasons."

            n "Her carefree attitude, the air of otherness around her, all the things that make Rin herself… those things captured me with irresistible force."

            n "The way she could take in anything and everything giving it only the value she herself placed, weighing all things fairly and without prejudice, seeing the world as she wanted."

            n "This is something I could never do, and Rin was probably more of a muse to me than anything ever was to her."

            n "She seemed so free to me, truly a free spirit. While I, constantly worrying about everything, seemed so inhibited that it was almost embarrassing."

            n "Maybe that's why I latched so tightly on to Rin, trying to get inside her world that was so different from my own bleak life."

            nvl clear

            n "{vspace=60}Before I noticed it, that irresistible force had pulled me dangerously close to her, but it turned out to be way too alien for me."

            n "And I had forgotten Newton, of all things."

            n "The gravitational force is inversely proportional to the square of the distance between the objects…"

            n "So if two people feel something for each other…"

            n "Heh."

            n "Even though feelings are not governed by the constants of the universe, I can't help thinking that for some time now I've been a satellite to Rin's brightly shining planet."

            n "{vspace=30}Planet Rin."

            n "{vspace=30}The thought makes me almost laugh, she really does seem to be from another planet at times, minus green skin and possibly some tentacles."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl hide dissolve
            nvl clear

            show rin negative_sad_close_ss
            with charadistant

            "Perhaps because of my stifled laughter, Rin pulls away and I let her go, feeling the cold when her warmth goes away, and slight embarrassment for letting my thoughts run wild like that."

            "I credit that as Rin being a bad influence on me, while being glad at the same time that she can't read thoughts for real."

            "Rin's bitter tears have dried up, and she looks a little more like herself again."

            show rin basic_sad_close_ss
            with charachange

            "The lost look in her eyes is still there though. Her gaze wanders around restlessly before stopping at me."

            rin "What happened just now?"

            rin "Can you tell me?"

            hi "What? What do you mean?"

            show rin basic_upset_close_ss
            with charachange

            rin "I cried."

            "She says that hesitantly, as if not believing it herself."

            hi "Yes…"

            "…"

            "She keeps staring at me, as if pleading guidance so that she wouldn't have to feel so lost."

            "…"

            show rin basic_sad_close_ss
            with charachange

            rin "Why?"

            hi "You were sad."

            hi "Is that what you want me to say? But isn't that obvious?"

            show rin negative_confused_close_ss
            with charachange

            rin "I don't know. It feels weird to cry."

            hi "What? I don't believe it. I mean, everyone does that. It's nor—"

            "I bite my tongue before I finish my argument about normality."

            "Norms do not apply to the person I'm talking to."

            show rin negative_worried_close_ss
            with charachange

            rin "It always felt so wrong, different from what is in me. Like I couldn't really tell what I felt."

            rin "So I started thinking that maybe I don't know what I'm feeling. Maybe it's me who is wrong—"

            rin "I thought those kinds of things."

            show rin negative_sad_close_ss
            with charachange

            rin "I thought… that painting was enough because it felt that I did at least that right."

            rin "That all that is inside me could become a picture if I tried really hard. And it could."

            rin "But it doesn't feel like it's enough any more. Because if nobody else can see that, I will still be alone."

            show rin basic_absent_close_ss
            with charachange

            rin "Was it wrong to try? Everyone got really angry at me for that."

            stop music fadeout 6.0

            "I've rarely heard Rin say this much at once before."

            "Once she finishes, she simply shuts up, looking so neutral that it's hard to believe she just said what she did."

            "I don't know what to think."

            "…"

            "Rin was desperate for someone to look at her paintings, and somehow see right through them into her soul, to understand her feelings…"

            "Because… she felt she could not express them in any other way?"

            "How can one say whether that is right or wrong?"

            "Could it be that all this time she's been trying to reach out to me like I've tried to reach out to her?"

            "…"

            "I sit down on a desk to think, and to rest my legs that kept us both standing for a long while."

            play music music_innocence fadein 12.0

            hi "You know, when I read a good book or look at a starry sky or whatever, sometimes I too feel something… profound, like a… shoot, I don't know how to describe it."

            hi "But the instant I try to put it into words I feel that I lose something, it doesn't feel as real, as true as it did inside my head."

            hi "It feels a bit phony. Damn, even what I just said felt phony."

            "I offer a smile that is meant to be between funny and self-deprecating, but Rin doesn't react."

            hi "Anyway…"

            hi "It might be that nobody can ever express their true feelings so that others understand."

            hi "Reality has no chance of living up to what someone has inside their head."

            hi "Nothing can match that. Not even your paintings, except maybe for you."

            hi "But I suppose you can't keep everything inside, you'd explode for real then."

            hi "What I'm trying to say is… I don't think it's wrong to express your feelings, even if you use painting as your conduit."

            hi "You just can't expect people to understand you any better than they would if you did it any other way."

            hi "In fact, you can't expect people to understand you at all."

            hi "It's because everything is so subjective. You see the world the way you do, but it's different from everyone else."

            show rin basic_sad_close_ss
            with charachange

            rin "But isn't that terrible?"

            hi "I guess it is, in a way."

            "…"

            show rin relaxed_doubt_close_ss
            with charachange

            "She frowns, looking probably as stricken as she can. Which is not much, but it's enough for me to understand that Rin is not particularly happy."

            rin "I think it might make me sad after all."

            hi "Yeah. I know."

            hi "I wish I could do something to help it."

            "I don't think I sound bitter, even though I am, a little."

            "This is my problem. I cannot be what Rin wants for her. And for the same reason, she can't do the same for me either."

            "…"

            show rin negative_worried_close_ss
            with charachange

            "She makes a difficult face, carefully trying to pick the words she wants to say."

            "So Rin has times when it's hard to say anything, too."

            show rin basic_sad_close_ss
            with charachange

            rin "It can't be helped, I think."

            show rin basic_absent_close_ss
            with charachange

            rin "…but… if you say that…"

            show rin basic_awayabsent_close_ss
            with charachange

            rin "It makes me feel a little better."

            "…"

            "It's funny how some seemingly irrelevant things are the most significant ones at times like this."

            "Like how Rin's voice is very very small, barely audible when she says that."

            "And how even her short bangs can cover her eyes when she looks downwards."

            show rin basic_blush_close_ss
            with charachange

            "And how they can't cover the deep red color rising on her cheeks and all the way to the tips of her ears."

            "They turn into a very interesting shade of red."

            "A deafening silence follows."

            "It's very awkward, as if I saw something that wasn't meant to be seen, even if it wasn't on purpose."

            "I don't know what to say to that, but I keep feeling like I should know."

            "She doesn't either."

            "Still, it feels like there is no momentum to lose even if we keep silent."

            "Like we have some weird, wordless connection that would hold even so."

            show rin relaxed_nonchalant_close_ss
            with charachange

            "Rin keeps shifting her weight from one foot to the other restlessly, looking everywhere around the room except at me."

            "She is the one who finally breaks the spell."

            show rin basic_deadpan_close_ss
            with charachange

            rin "Can we go? I don't want to stay here."

            hi "Oh, yeah, of course. Where?"

            "My reply is covering my nervousness as badly as her question is covering hers."

            show rin relaxed_sleepy_close_ss
            with charachange

            rin "You can go wherever you like. I want to sleep. I haven't really slept for a few weeks."

            show rin basic_lucid_close_ss
            with charachange

            rin "It feels like there is a flock of light blue butterflies inside my head. It makes it hard to think properly."

            show rin basic_deadpannormal_close_ss
            with charachange

            rin "The kind that you think is too blue to really exist, like Emi's panties this morning."

            show rin negative_spaciness_close_ss
            with Dissolve(0.1)

            show rin basic_absent_close_ss
            with Dissolve(0.1)

            show rin negative_spaciness_close_ss
            with Dissolve(0.05)

            show rin basic_absent_close_ss
            with Dissolve(0.05)

            show rin negative_spaciness_close_ss
            with Dissolve(0.05)

            show rin basic_absent_close_ss
            with Dissolve(0.05)

            show rin negative_spaciness_close_ss
            with Dissolve(0.1)

            show rin basic_deadpannormal_close_ss
            with Dissolve(0.2)

            "She shakes her head, and I almost expect a couple of ultramarine-colored Morphos to pop out of her ears."

            show rin basic_deadpanamused_close_ss
            with charachange

            "A small smile tugs upwards the corners of her mouth."

            rin "That reminds me. The blue, not the panties."

            show rin basic_deadpandelight_close_ss
            with charachange

            rin "The word for a flock of butterflies is a swarm. I looked it up."

            "That makes my eyebrow rise into a questioning arch."

            hi "Why don't you use it then?"

            show rin basic_absent_close_ss
            with charachange

            rin "I like the other word better."

            "Why look it up in the first place, then?"

            hi "Then you should use it, right?"

            show rin basic_awayabsent_close_ss
            with charachange

            "She nods and falls silent, her gaze escaping mine to the side, attracted by the dark orange sunlight refracting from the windows."

            "We stay like that for a little while: me silently looking at her silently looking out of the window."

            hi "Hey… you all right now?"

            show rin basic_absent_close_ss
            with charachange

            "She glances at me from the corner of her eye, looking wistful again. The sunlight's reflection doesn't betray any more of her inner feelings."

            rin "I'll need to think about that."

            "I want to continue this conversation, grasping at those straws that she finally revealed to even exist."

            show rin basic_awayabsent_close_ss
            with charachange

            "But Rin is looking out of the window so absentmindedly that I know she won't be responsive in any way that would make sense."

            "It's like some kind of defense mechanism of hers, to avoid being sensible."

            "Her mind is like a butterfly in itself, always fluttering somewhere away whenever it's stirred."

            "Just when I thought I could see behind her veil, she jumps out of my reach again."

            "Maybe that's just how Rin is."

            "Maybe that's something I should just accept to get some peace of mind."

            hi "Okay."

            hi "I'll walk you back to the dorms then."

            show rin basic_absent_close_ss
            with charachange

            rin "Thanks."

            show rin basic_lucid_close_ss
            with charachange

            rin "Really."

            stop music fadeout 12.0

            scene bg school_hallway3
            with locationchange

            "The empty hallways of the school devoid of its students feel very lonely."

            "Less than one hour after the summer vacation began, the building seems to be deserted, and all that intrudes on the stillness of the hallways are our footsteps."

            "The change is sudden, but it shows how the building is just an empty shell, dead without its students and teachers."

            "It's as though the school has become a private world for only the two of us, a desolate place filled with silence and chalk dust."

            scene bg school_staircase2_ss
            show rin relaxed_sleepy_close_ss at twoleft
            with locationchange

            rin "I think I have to change."

            "She says it out of the blue while we walk down the staircase from the third floor, still managing to feel like she is mirroring what I was thinking just before."

            hi "That's what people must do, sometimes."

            nvl clear
            nvl show dissolve

            n "{vspace=240}That's the last thing we say to each other that day, even though there would be so much to talk about."

            n "And even those words drown in the all-encompassing silence, disappearing into the stagnant air as if they were never said."

            nvl clear
            nvl hide dissolve

            scene black
            with dissolve

            if _in_replay:
                return

        call timeskip

        label .wb_and_ws:
            play music music_dreamy fadein 2.0

            scene bg school_dormhisao_rn
            with charachange

            $ renpy.music.set_volume(0.4, 0.0, channel="ambient")
            play ambient sfx_rain fadein 1.0

            "The first day of summer vacation is a disappointment."

            "I woke up. Water came down from the leaden sky in Biblical proportions."

            "I was optimistic at the time."

            "A quick summer shower, I thought. Torrents of rain for a few minutes, then it's gone."

            "No such luck."

            $ renpy.music.set_volume(0.7, 1.0, channel="ambient")

            scene bg misc_sky_rn
            show rain normal
            show hisaowindow
            with locationchange

            "Rainwater is relentlessly pouring down from the blue-gray sky outside, streaming down the glass of my window in small brooks and rivers and gathering together to form miniature ponds on the walkways."

            "Just like it has done for the past two and a half hours."

            $ renpy.music.set_volume(0.4, 1.0, channel="ambient")

            scene bg school_dormhisao_rn
            with charachange

            "So I've been half-assedly cleaning up in between half-assedly reading a book, packing my stuff on the side when I get bored of the first two."

            "The weather drags my spirits pretty down too, making it harder to do anything properly."

            play sound sfx_impact2

            "Something bumping quite loudly against my door rouses me from my apathy."

            "I hope it's not Kenji and his crazy indoors bowling alley."

            "…"

            "I hear no more sounds from the corridor until I walk to the door and open it."

            play sound sfx_dooropen
            $ renpy.music.set_volume(0.2, 1.0, channel="ambient")
            stop music fadeout 2.0

            scene bg school_dormhallway
            show rin basic_absent
            with locationchange

            "Rin."

            "I wish seeing her would evoke some more emotion in me, but for one, I'm too surprised that she came to see me and for two, she is soaking wet."

            "Her uniform shirt is drenched and she is standing in a self-created puddle."

            "Droplets of rainwater are dripping from her short bangs and sliding down her nose until they fall down from the tip."

            "One.{w=0.7} By.{w=0.7} One."

            hi "Umm… hi."

            hi "How are you feeling?"

            show rin basic_deadpannormal
            with charachange

            rin "Medium normal."

            play music music_rin fadein 2.0

            "The relative questionability of her statement aside, she sure doesn't look too good."

            hi "You're all wet."

            show rin basic_absent
            with charachange

            rin "It's because I come from the outside. Do you know it?"

            hi "Why'd you be outside? It's raining buckets out there, if you haven't noticed."

            show rin basic_deadpancontemplation
            with charachange

            rin "I haven't. It's raining pretty hard though. I was on a walk."

            hi "Is this what you call 'wallowing in self-pity?'"

            show rin basic_deadpanupset
            with charachange

            rin "Do you think I'm pitiful?"

            hi "No, I implied that you think you are."

            show rin basic_awayabsent
            with charachange

            rin "I'm not, and rain is not a sad thing."

            show rin basic_absent
            with charachange

            rin "Don't you ever walk in the rain?"

            hi "I do, but only with proper equipment, like an umbrella."

            show rin basic_lucid
            with charachange

            rin "You just need to imagine you have a blue umbrella with white stripes."

            hi "It might be tough when rain is falling on my head."

            show rin basic_deadpannormal
            with charachange

            rin "Just imagine harder."

            "…"

            "Yeah, she definitely is back to normal."

            "Those half-sarcastic, inconsiderate remarks that really push my buttons even though she doesn't mean it, that vacant, spaced-out stare that always expects more than it gives."

            "It's so… very much like her."

            show rin basic_deadpan
            with charachange

            rin "I may need to come in. I need some help with this water and clothes I'm wearing."

            "My brain quickly solves this equation, and I stumble with my words, a stark display of contrast against Rin's easygoing self-invitation."

            hi "But, Emi…"

            show rin basic_lucid
            with charachange

            "Rin shakes her head vehemently, causing water to sprinkle everywhere."

            rin "She left."

            show rin basic_awayabsent
            with charachange

            rin "Besides she would just worry and fuss until she could not worry or fuss any more, which always takes a troublesomely long time."

            show rin basic_absent
            with charachange

            rin "It's in fact longer than I want to hear her fussing, and I thought you probably are not the fussing kind."

            $ renpy.music.set_volume(0.4, 1.0, channel="ambient")

            scene bg misc_sky_rn
            show rain normal
            show hisaowindow
            with locationchange

            show rin relaxed_nonchalant_close_rn:
                center alpha 0.0
                ease 0.5 ypos 1.1 alpha 1.0

            stop music fadeout 8.0
            play sound sfx_rustling

            "She slumps down on my desk with a squishy sound."

            "Her soaked clothes are making the desk and everything on it wet but she doesn't care."

            "…"

            hi "Okay. Fine. I'll help you out."

            hi "I have a towel somewhere. Do you want dry clothes? Is a uniform fine? I'm taller than you, but…"

            show rin basic_lucid_close_rn
            with charachange

            rin "Everything is fine."

            show bg school_dormhisao_rn as bg2
            with locationchange

            "With a little searching I find a fresh uniform and a fluffy towel from the depths of my closet."

            hide bg2
            with locationchange

            "The towel in one hand and the uniform in the other, I turn to face Rin again, uncertain of the next step."

            "There is something wrong with me, a normal guy would just—{w=1.0}{nw}"

            show rin basic_absent_close_rn
            with charachange

            rin "Stop worrying. It is not a problem."

            "She probably could see right through my hesitant demeanor."

            "As if I was completely transparent to her."

            "I push my anxiety away and concentrate on the eight buttons lined on her shirt, just like mine has."

            "Only the first button is an obstacle, and after getting it over I undo the others with slightly less shaking hands."

            $ renpy.music.set_volume(0.2, 1.0, channel="ambient")
            play music music_heart fadein 0.5

            scene ev rin_wet_pan_down:
                center
                yalign 1.0
                easein 20.0 yalign 0.0
            with whiteout

            "Throwing the soaked shirt aside, I reveal Rin's pale upper body, shrouded only in her light blue brassiere which instantly reminds me of her saying it's her favorite color."

            "I try not to think too much about… stuff, but it's hard not to look at her body with what I can only think of as mixed feelings."

            "I don't know what to think of this, so I just watch her. Rin looks… brittle."

            "She is like a shell, a fragile thing just barely holding together."

            "Her ribs, each of them visible under her pale skin, are moving up and down in the rhythm of her breaths."

            "Rin always struck me as quite thin, but I realize now that the manic creative period before the exhibition opening might've caused her to lose weight."

            "Did she eat properly and enough? Definitely not and probably not."

            "This ugly, yet beautiful bare minimum of a human body that belongs to someone I care about is a contradiction of aesthetics in itself, oddly becoming of her."

            "My eyes follow her collarbone to her shoulder and down her arm until the abrupt end."

            "No, it's less than the bare minimum, I think with a passing pang of sadness and some guilt for thinking like that."

            scene ev rin_wet_arms:
                center
                xalign 0.0
                linear 20.0 xalign 1.0
            with flash

            "Her arms, degenerated into almost nothing but bone and skin due to lack of use, look very short now that the long sleeves of her uniform are not covering them:"

            "My lack of any negative reaction makes me think that I've actually grown pretty accustomed of the various physical abnormalities of my schoolmates."

            "I always wondered why Rin keeps her shirt sleeves long, only tying them in a simple knot at where the elbow would be."

            "It seems a bit impractical, but then again she is not exactly the pinnacle of practicality."

            "Maybe she likes it, maybe it is somehow important to her. Maybe there is no deeper meaning to it."

            "I feel like asking, and almost do, but Rin's miserable state requires a higher priority of my attention."

            scene ev rin_wet_face_down:
                center
                yalign 0.0
            with flash

            "She's stopped talking too, after we ran out of spiky greetings."

            "I guess there is no need for chitchat then."

            scene ev rin_wet_towel_down
            with charachangeev

            "I pick up the towel from the bed and wrap it around her head, rumpling it all over her hair until most of the rainwater is hopefully soaked into the fabric."

            scene ev rin_wet_towel_up
            with charachangeev

            "She peeks from below the towel at me, looking up with impassive eyes."

            "It looks like she wants to say something without saying it."

            "It's that kind of a look."

            "But I can't read what she is thinking about from her face, so I just keep on fussing with the towel around her shoulders and hair."

            "The silence is oppressive, terrifying."

            "Communication between us has suddenly been reduced to the movements of my hands and the towel, and Rin swaying her body to and fro."

            "My jagged breathing and her quiet breaths, trying to find a common rhythm that just is not there."

            "I think I can hear her heartbeats, or maybe they are just mine redoubled."

            "As I brush a rogue strand of hair aside from her ear, Rin suddenly presses her cheek against the back of my hand."

            "The contact is electric, a jolt of current surging through me."

            scene ev rin_wet_towel_touch
            with charachangeev

            "Whether she seeks comfort, warmth or just my touch I wouldn't know, but I can't help touching her back, caressing her soft cheek with my hand."

            "And with closed eyes, she kisses me, on the fingers, counting the joints with her lips…"

            "I am saddened beyond my expressive capability."

            "Here we are, a boy and girl, both in love or something like that with each other, or maybe not… and yet…"

            $ renpy.music.set_volume(0.1, 1.0, channel="ambient")
            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=30}Something is broken, I can feel it in me and in Rin; in the way our gazes merely brush against each other, shying away from contact; in her closed, timid posture and in my way of touching her like a china doll, afraid of shattering her delicate form."

            n "In how we are closer than we have ever been, yet I'm not feeling happy. It's like yesterday."

            n "When did tenderness and forlornness become one and the same word, acts of affection start invoking only longing? …How, why did we end up like this?"

            n "'No, don't answer that,' I'd like to say to myself, but fighting against the omniscience of self-awareness is a lost cause."

            n "Still, I am here, and Rin is here, and it feels like she might be able to solve whatever problems she has."

            n "And if she can, why couldn't I? Why couldn't we?"

            n "It feels like taking that step is too much, too difficult, too uncertain."

            n "So for now, all I can do is dry her up so she won't get a cold again."

            $ renpy.music.set_volume(0.2, 1.0, channel="ambient")
            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl hide dissolve
            nvl clear

            scene ev rin_wet_face_up
            with charachangeev

            "I pet her head, trying to sort out the hair that refuses to be sorted out even when wet."

            "A pair of dark, glazed eyes follows my every movement."

            hi "Pants too?"

            scene ev rin_wet_face_down
            with charachangeev

            "She nods an answer, leans back and spreads her legs, with a grotesquely inviting gesture that makes a nasty feeling crawl up and down my spine like a bad premonition."

            "It's not enough to sober me though, as the silence is starting to make me feel detached from myself."

            "I move automatically, without thinking even though I should; I should talk to her about this, or at least about something."

            "The silence is a spell, a pact that has bound us to this private world made of the dull sound of rainfall and the soft feel of her skin against my fingers."

            "The button of her trousers is fastened tight, but it opens surprisingly easily."

            "Slipping them off is hard, mostly because she is sitting on them, with no intention of standing up to ease my task."

            scene evh rin_h2_pan_surprise:
                xalign 0.5 yalign 0.0
            with whiteout

            "I kneel down uncomfortably and titillatingly between her legs so I can quickly dry her bare feet, remembering that they are as important to her as hands are to me."

            "As I work the towel up from her ankles, Rin brushes her thigh against my cheek and nudges the small of my back with her heel to make me come closer."

            "I look up to meet her silent stare that was waiting for me to look up."

            "That unassuming, expectant stare seems to say that the ball is in my court."

            "…"

            "I fleetingly brush my hand against her inner thigh."

            show evh rin_h2_pan_away
            with charachangeev

            "The touch makes her gasp sharply, as if she was trying to hold back breathing."

            "What if I do this, then?"

            show evh rin_h2_pan_closed
            with charachangeev

            "The small kiss I place on her thigh is enough to make Rin lose her composure, to shut her eyes, to squeal almost inaudibly."

            "…Is that what you want too? Would it be all right now? To take this step?"

            show evh:
                acdc_warp 8.0 yalign 1.0

            "…What if? Maybe if…"

            "Hazy thoughts float somewhere in the back of my unfocused mind."

            "Somehow, this whole situation is making it hard to think, as if my head was full of cotton fluff."

            "But that's all right. It seems thinking is not something we need right now."

            show evh rin_h2_nopan_closed:
                yalign 1.0
            with Dissolvemove(0.5)

            $ renpy.music.play(music_heart, fadein=0.5, if_changed=True)

            "By the grace of vastly smaller amount of fabric, slipping off Rin's panties is considerably easier than her trousers."

            "They disappear past my field of vision, sliding somewhere away down her legs."

            "It seems I did a poor job with the towel, since Rin's legs are still wet from the rain."

            "Well, whatever."

            show evh rin_h2_hisao_closed
            with charachangeev

            "Guided by instinct more than rationality, I move closer and taste the different kind of wetness."

            "She responds to me, to the slow movements of my tongue on her skin, to my kisses on her flesh."

            "Her muscles tense and relax in the rhythm, as if what I am doing was uncomfortable."

            "To hear Rin trying not to make a sound when I suck on her is… unreal."

            "This whole morning has been so unreal, like the surreal intangibility of an awakening dream."

            "I can't believe I am doing this, to her, now. But I am going with the flow."

            "Besides, the point of no return was a thousand miles ago."

            "I move around, try to do things to her, to find the places where her weakness lies, to tease her, to drive her mad with pleasure because I want to, I want to do this to her."

            "But she doesn't squeal, she doesn't squirm, for maybe I can't make Rin any madder than she already is, whatever I do."

            "Her ragged, heavy breathing mixed with unintelligible moans is that of a lunatic, but I do not cause it."

            "I only release that from her."

            "She becomes more and more moist, and I drink from her, feeling a heat growing inside myself."

            "I try to reach her deepest places, to feel all of her I can this way."

            "My every action is met with a different reaction, but all of those are out of pure lust."

            show evh rin_h2_hisao_closed:
                acdc_warp 16.0 yalign 0.0

            "Rin is lost in desire, willing to let anything happen to her if I do it right now."

            "She becomes closer and closer to the moment of release, but the way to that is an uphill slope of madness."

            "Still, she is going that way."

            "The muscles don't relax any more between the waves of ecstatic spasms."

            "Rin just becomes tenser and tenser, contracting so much that it must be physically painful, but I do not let go."

            "I keep going, and I know she wants it too, she desperately wants me to do this to her."

            "A leg curls around my shoulders and draws me closer, so close that I think that I'm going to choke."

            "I keep going because it's the only possibility."

            stop music fadeout 8.0
            stop ambient fadeout 12.0

            "As I push the button that drives her into gasping for breath, locking her leg into a cramp against my back, losing her mind in the sensation, at that precise moment I seem to forget all that was meant to be, all that should be."

            "All I know is that she came here and… I think there was a towel at some point, too."

            "None of it matters, all that matters is this, what we have now."

            "Her orgasm surges through me too, exciting me in a completely new way."

            "It makes me feel anxious, nervous. Bothered."

            show evh rin_h2_hisao_away:
                yalign 0.0
            with Dissolvemove(0.5)

            "As her body relaxes, I try to kiss her down there again, but it startles her, causing her to jump."

            show evh rin_h2_hisao_surprise
            with charachangeev

            rin "No… Hisao… Enough."

            rin "Come here."

            scene bg school_dormhisao_rn
            with locationchange

            "I stand up to remove the last piece of clothing Rin has."

            "She leans against me to catch her breath, tickling me with warm air exhaled into my shirt."

            "Blindly, I reach behind her back to feel my way below her shoulder blades, to find the contraption that fastens her bra."

            "It opens more easily than I thought, falling to the floor somewhere."

            play music music_romance fadein 10.0

            scene ev rin_pair_base_clothes
            show rp_hisao normal at truecenter
            show rp_rin normal at truecenter
            with whiteout

            "Her bare skin against me is a sensation so wonderful that I want to have more of it, and I do, embracing her."

            "Rin's hair smells of rain, and I realize that I'm not hearing the sound of rainfall any more."

            "It's a sobering thing. The cushion that enveloped us into a reality of our own is now gone, and I realize more clearly what is happening."

            show rp_hisao frown
            with charachangeev

            hi "You know, this really is not what friends should be doing."

            "I whisper, once again noticing how such a simple matter as talking can be overbearingly difficult at times."

            show rp_rin talk
            with charachangeev

            rin "Will you stop being my friend?"

            "That wasn't what I meant, but her serious tone and the layers of connotations behind Rin's question give me pause."

            show rp_hisao smile
            with charachangeev

            hi "Nah."

            show rp_rin smile
            with charachangeev

            rin "I… think it might be all right. Even if you did."

            "I hug her and smile into her hair, understanding Rin perfectly for once."

            show rp_rin frown
            with charachangeev

            rin "You are wet."

            "The remnants of water on her skin have drained into my shirt."

            "Somehow, even her statements of the obvious make me glad right now."

            show rp_hisao normal
            with charachangeev

            hi "You're right. I am. But that's your fault."

            show rp_rin normal
            with charachangeev

            rin "I want to see you."

            play sound sfx_rustling

            scene ev rin_pair_base
            with charachangeev

            "I comply, standing back to open the buttons of my shirt, much more quickly than when I undid Rin's buttons."

            "A sudden sense of haste strikes me, spurring me to rush forward."

            "Every second I'm not touching Rin is a second wasted, a chance lost."

            "My belt buckle proves an obstacle despite my ability to open it in an eyeblink under normal circumstances."

            show rp_rin closed
            with charachangeev

            "While I fumble with it, I don't notice Rin bringing her foot up between us until she starts tracing my chest with her toe."

            show rp_hisao frown
            with charachangeev

            "I look down to see what she's looking at…"

            hi "My heart…"

            "I reflexively flinch back, covering the scar tissue in the middle of my chest."

            "The shallow mark that the surgery following my heart attack left on my body has healed already but… well, it's not a particularly pretty sight if not overly repulsive either."

            "It's barely noticeable, but she does have an eye for detail. Is this why she said she wanted to see me?"

            "I had sorta forgotten about this because of all this mess with Rin, but now all the unpleasant things connected to my condition surface at once, rushing through my mind like a flash flood."

            "And oh God all the stories about old guys getting heart attacks when having sex, what if…"

            show rp_rin talk
            with charachangeev

            rin "Hisao."

            "…"

            "Realizing that I might just have spoiled the mood, I stumble to explain myself."

            show rp_hisao normal
            with charachangeev

            hi "Ah… sorry, it's just that…"

            show rp_rin smile
            with charachangeev

            rin "Let me touch you."

            "Her eyes are sultry, inviting as she sits there bare naked without an inkling of shame. I never thought Rin could look like that."

            $ renpy.music.set_volume(0.1, 1.0, channel="ambient")
            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=60}Yeah, I know this is not how it should go."

            n "Even though Rin is right here, even though there should be no more questions, no obstacles, not this maddening feeling that something is constantly wrong…"

            n "The same feeling that clutched my heart yesterday makes its appearance."

            n "We are together. In a way that is difficult to define, it eludes description as stubbornly as it evades change."

            n "{vspace=30}Would a relationship like this be all right? Could we ever change to become closer?"

            n "Even though we would stay together for all of eternity, we might never find our mutual understanding."

            n "But there is no such thing as eternity. This may mean that we will not be together forever."

            n "If not our differences, then the flow of time will pull us apart with irresistible force."

            nvl clear

            n "{vspace=60}Rin is a creature of the moment, of whim and of impulse."

            n "{vspace=30}I am nothing of the sort."

            n "{vspace=30}This is a fact that I can understand very clearly."

            n "If for no other reason, for this reason I should grasp this moment. Even if it's the only moment we will ever have, I should not let myself spoil it."

            n "Even if I can't escape myself. Rin can't either, I know it now."

            n "{vspace=30}We both have things we can't let go, things we can't not think."

            n "Feelings we can't not feel."

            n "But she allows herself to want me without any restraint. Here and now."

            $ renpy.music.set_volume(0.2, 1.0, channel="ambient")
            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl clear
            nvl hide dissolve

            show rp_hisao frown
            with charachangeev

            hi "I'm sorry, you know…"

            show rp_rin closed
            with charachangeev

            rin "Hisao, you really have to stop worrying."

            "Rin interrupts me before I get further, which is good because I don't know what I could have said."

            "Her voice, void of its usual spaciness, scolds me softly, without an edge."

            show rp_rin smile
            with charachangeev

            rin "You really have to learn to let go."

            "She scans me calmly, almost calculatingly."

            "I wonder what I look like through her eyes."

            "Damn. They are so green it almost hurts."

            "I always was so enchanted by her eyes, those mysterious, captivating eyes that always were too restless for their own good."

            "But I was also always intimidated by them."

            "Yeah. Rin is intimidating, on more than one level and especially right now."

            "She is frighteningly lucid, the goosebumps on her skin giving away that she is cold, or scared too."

            "Either way, I steel myself and step back to Rin, embracing her to feel her in my arms again and to banish my doubts."

            "The sight of her gentle, loving eyes seems to melt those doubts away like the last snow of winter."

            scene evh rin_h_closed
            with whiteout

            "She presses her head against my shoulder, seeking a place to rest herself in, leaning against me like I lean against her."

            rin "Let go."

            "Yes."

            scene evh rin_h_left
            with charachangeev

            rin "You should forget about stuff like future and past, it's not like you can change those kinds of things."

            "I wanted to say something to her, but I have lost my voice so I just mumble something unintelligible at her."

            rin "You should just be with me now."

            "Maybe she understood what I wanted to say even if I didn't."

            rin "Come here."

            hi "I am here."

            scene evh rin_h_normal
            with charachangeev

            rin "Come closer."

            "My entire body is thinking only in positives now so I do, hugging her more tightly."

            scene evh rin_h_right
            with charachangeev

            rin "Closer."

            "I press my lower body against hers."

            "She tenses a little. Just a little."

            scene evh rin_h_closed_close
            with characlose

            rin "Closer."

            "Her final plead is more like a prayer."

            "There is only one way to be any closer than this."

            "I reach down between us and guide myself, sinking myself into her."

            scene evh rin_h_strain_close
            with charachangeev

            "Every muscle in Rin's body stiffens at the same time."

            scene evh rin_h_strain
            with charadistant

            "She doesn't say anything, or wince, so I push deeper, eventually moving out."

            "And again. And she moves with me."

            "Our movements melt together into one continuous string of back and forth, in and out."

            "All sensations become sharper, amplified tenfold."

            "My brain gave up interpreting all this stimulation ages ago, and now I am left with no choice but to feel all of this with my entire body."

            "It's like that for Rin too, I know it. I can see it. I can feel it."

            "She breathes sharply in and out, losing all composure and grace, breathes warmly against my shoulder."

            "Between those fragile breaths, she sometimes kisses me tenderly, gently, as if she was unsure how to do it properly."

            "But there is no hesitation."

            "Desperately clinging to me, drawing me closer so that I can fill all of her, she moves against me, around me so that it's hard to say where I stop and she begins."

            "We take it slowly, excruciatingly slowly, as if we had all the time in the world even though we have only this moment and nothing beyond that."

            "That feeling is—{w=0.7}{nw}"

            scene evh rin_h_normal_close
            with characlose

            rin "Wait…"

            "I stop moving, slightly alarmed."

            "Maybe it hurts, or…"

            scene evh rin_h_right_close
            with charachangeev

            "She looks at me in a way that I can't really begin to interpret."

            rin "Is this it?"

            hi "…Huh?"

            rin "You said I don't have to be alone."

            scene evh rin_h_left_close
            with charachangeev

            "Her eyes are full of an innocent, fuzzyheaded confusion that makes me chuckle a little and pet the back of her head."

            hi "Yeah. This is what I meant."

            hi "That you have someone you can come to when you get soaked in a rain."

            hi "It means you are not alone."

            hi "If there is such a person for you."

            scene evh rin_h_closed_close
            with charachangeev

            "She answers with a kiss, reminding me that we have stopped moving for no real reason."

            "So we start from the top, almost at the same time, each mirroring the rhythm of the other."

            "I move faster, faster in and out of her, my sweat mixing with hers, glistening on our shared skin like diamonds and pearls."

            scene evh rin_h_strain:
                truecenter
                zoom 1.2
                easein 20.0 zoom 1.0
            with charadistant

            "She moves faster, grinding herself against me in the throes of our desire."

            "The intoxicating scent of her lust, the mind-blanking feeling that connects our bodies, the sense of all rational thought draining from my mind."

            "All those burn my consciousness just like the compelling feeling in my body burns my instincts."

            "As those feelings grow, Rin makes no signs of stopping."

            "She curls her feet behind my lower back, forcing me to drive myself inside her as deep as physically possible, each millimeter sending waves through my spine."

            "My mind blacks out as the world erupts into a flash of bright white blindness."

            stop music fadeout 2.0
            stop ambient fadeout 2.0

            scene white
            with Dissolve(2.0)

            pause 4.0

            if _in_replay:
                return

        label .proof_of_existence:
            scene white

            $ renpy.music.set_volume(0.1, 0.0, channel="music")
            play music music_timeskip fadein 4.0

            centered_b "Present{fast}" with Dissolve(4.0)

            nvl clear

            nb "'Present' is a fleeting and vague concept at best."

            nb "The moment between the past and the future?"

            nb "That doesn't really mean anything."

            nb "Thinking too much about things that don't make sense is a waste of time."

            nb "That's why living through the present is always the best option."

            nb "Besides, for us who can't foresee the future and who forget the past too easily, present is really the only proof of our existence."

            nb "Even though existence will go on even if you forget about it for a while, it's good to seize the day at least every once in a while."

            nvl clear

            centered_alive "That way… you can confirm that you are, in fact…"

            show alivetext _("That way… you can confirm that you are, in fact…")
            with Dissolve(3.0)

            pause

            show alivetext _("That way… you can confirm that you are, in fact… alive.")
            with Dissolve(3.0)

            $ renpy.pause()

            stop music fadeout 4.0

            scene bg school_dormhisao
            with Dissolve(4.0)

            $ renpy.music.set_volume(1.0, 0.0, channel="music")
            play music music_dreamy fadein 4.0

            "I am pretty sure that the girl who is standing there half-naked, staring out of the window of my room, has a much better grasp of 'present' than I do."

            "As for me… well, right now I'm somewhat confused by my present state, since I should try to locate my shirt and not stare at Rin's butt."

            "But I just can't stop looking at her."

            scene bg misc_sky
            show hisaowindow
            show rinpan relaxed_nonchalant_close at center
            with locationchange

            "She is so close to the glass that her nose is probably going to leave a mark."

            "At least her breathing does, when it condenses on the rain-cooled window glass before quickly disappearing again."

            "My shuffling around to get dressed doesn't rouse Rin from her contemplation, which is fine, really. I don't mind the silences as much as I used to."

            "Only after I'm almost finished with buttoning up my shirt does Rin say something, still without turning to look at me."

            show rinpan relaxed_boredom_close
            with charachange

            rin "Let's go somewhere."

            hi "Where?"

            "I can only assume she is inviting me and not the windowsill, but it's a fair guess."

            show rinpan basic_lucid_close
            with charachange

            rin "I know."

            hi "What?"

            show rinpan basic_deadpan_close
            with charachange

            rin "Help me get dressed."

            show rinpan basic_awayabsent_close
            with charachange

            rin "I think today is the day."

            show rinpan basic_deadpanupset_close
            with charachange

            rin "Come on, clothes."

            "Clothes, clothes… what an impatient tone."

            "I crouch down to pick up her bra from the floor where it had fallen, discarded in the haste of undressing and forgotten there."

            "Hanging it from between my fingers like a dead fish, the same hesitation that grasped me when I was undressing Rin is creeping inside my head again."

            "Is intimacy really something this difficult for me to handle?"

            show rinpan basic_deadpancontemplation_close
            with charachange

            rin "Come on, you got it off just fine. This is the same but the other way around. It's like talking backwards."

            show rinpan basic_deadpan_close
            with charachange

            rin "Ysae s'ti tub, drah smees."

            "Perplexed by her sudden and prodigious display of mental processing capacity, I forget to attempt reversing her gibberish back."

            "I'm pretty sure I couldn't switch to talking backwards that fluidly even with some practice."

            hi "Umm, could you repeat that?"

            show rinpan basic_lucid_close
            with charachange

            rin "Ysae s'ti tub, drah smees."

            "…"

            hi "Got it. Fine, I'll give it a try."

            "Rin was right, the locking mechanism is simple enough, and I get the little plastic hooks right on the third attempt."

            hi "There."

            show rinpan basic_deadpandelight_close
            with charachange

            rin "Ti tsujda ot evah uoy won."

            hi "What? Please stop that, I don't speak backwardese."

            show rinpan basic_lucid_close
            with charachange

            "She shakes her head as if needing to banish the backwards way of thinking with a physical gesture."

            "I know a few people who could benefit from that kind of ability."

            show rinpan relaxed_nonchalant_close
            with charachange

            rin "I got stuck. Now you have to adjust it."

            hi "Adjust?"

            show rinpan basic_deadpan_close
            with charachange

            rin "That's what I said."

            hi "No, I asked what you meant."

            show rinpan basic_lucid_close
            with charachange

            rin "You know, so that they are… fine."

            "Oh. Fine, you say?"

            "…"

            "As I have no idea when her breasts are supposed to be 'fine,' I end up fumbling around her chest for a good while without really getting anywhere."

            "Not that I would complain, but Rin does."

            show rinpan basic_deadpanupset_close
            with charachange

            rin "Emi is better than you at this."

            "Her impatient tone ticks me off, even though I can't really disagree. Rin suddenly seems to be in an awful hurry."

            hi "Yeah well excuse me, could that be because she is a {b}girl{/b} and can actually relate?"

            show rinpan basic_deadpanamused_close
            with charachange

            rin "I don't think so, she has just about as much chest as you do."

            "…"

            stop music fadeout 5.0

            hide rinpan
            show rin basic_absent_close
            with shorttimeskip

            "With her bra and breasts eventually 'fine' as they should, the rest of her clothes are considerably easier to put on."

            hide rin
            with charaexit

            "Rin launches towards the door even though her shirt is not even buttoned up all the way yet."

            "Left with little choice, I run after her."

            $ renpy.music.set_volume(0.5, 0.0, channel="ambient")
            $ renpy.music.set_volume(1.0, 0.0, channel="music")
            play music music_soothing fadein 2.0
            play ambient sfx_parkambience fadein 0.5

            scene bg school_gardens
            with locationskip

            "As soon as I realize that we are heading for the side entrance leading to the forest, I think I know where Rin wanted to go, although I couldn't say why she'd want to go there."

            "Then again, I can't really assume my guesses to be anywhere near correct when Rin is concerned, not even for a quite generous definition of 'correct.'"

            $ renpy.music.set_volume(0.6, 0.5, channel="ambient")
            $ renpy.music.set_volume(0.8, 0.5, channel="music")

            scene bg school_forest1
            with locationskip

            "The forest behind the walls smells of rain, the last raindrops are still dripping from the wet undergrowth into the earth despite the rain being gone for a while already."

            "We stroll along with an unhurried pace that Rin sets, giving me time to take in the calming atmosphere."

            "I think I can hear Rin saying hello to at least three different trees while she walks past them, but I ignore it, just like the trees do."

            "She leads me to the narrow side path leading up to the hilltops, as I guessed."

            scene bg worrytree at center
            with locationchange

            "I peek through the canopy trying to find a rainbow, but there doesn't seem to be one."

            "It's perfect weather for rainbows. The sun is shining low, and rain has passed not too long ago."

            "Well, whatever."

            $ renpy.music.set_volume(0.7, 0.5, channel="ambient")
            $ renpy.music.set_volume(0.6, 0.5, channel="music")

            scene bg school_forest2
            with locationchange

            "I lower my eyes from the treetops to see the gaunt back of the girl who is climbing up the hill slowly, without losing her balance."

            "A few steps ahead of me on the path, but still within my reach."

            "I don't think I ever could reach a rainbow, but reaching Rin… it seems less impossible than it used to seem."

            $ renpy.music.set_volume(1.0, 0.5, channel="ambient")
            $ renpy.music.set_volume(0.4, 0.5, channel="music")

            scene bg school_hilltop_border_summer
            with locationchange

            "The clear sky greeting us from above the meadow clearing seems vast and beautiful."

            "A strong wind is herding the rainclouds away from the town, to the other side of the mountains in the distance."

            "The sight is pretty, but…"

            "…"

            stop music fadeout 6.0

            show dandelionsbg thin
            show dandelionsfg thin

            "A speck of white flies past the edge my peripheral vision, but when I turn to look, it's already gone."

            "Another follows, then a third."

            "Before I realize it, dozens of almost invisible small tufts of white are flying all around us."

            show rin basic_delight behind dandelionsfg at center
            with charaenter

            rin "Look, the flowers."

            "Ah. I see it now."

            $ renpy.music.set_volume(1.5, 0.5, channel="ambient")
            $ renpy.music.set_volume(1.0, 0.0, channel="music")

            scene bg school_hilltop_summer
            show dandelionsbg dense
            show dandelionsfg dense
            with locationchange

            play music music_comfort fadein 0.5

            "The sea of dandelions that covered the hilltop on our last visit has changed over the days."

            "Where there was bright yellow before, there is now fluffy white."

            "Some of the flowers have already shed their seeds, but many are still waiting for a suitable gust of wind."

            "Today those gusts are not in short demand, every now and then they shake the grass thoroughly, and suddenly the air is thick with dandelion seeds."

            "One by one, the seeds separate from the flower heads and are lifted away."

            "A commonplace event, but one that seems to fascinate Rin for some reason."

            $ renpy.music.set_volume(1.0, 0.5, channel="ambient")

            show rin negative_spaciness behind dandelionsfg at center
            with charaenter

            "She's turning her head from side to side, marveling at the change happening all around her as the seeds fly away."

            "I watch them too, following the white tufts floating with the wind towards the horizon, and imagine that I can see them even after they disappear from my sight."

            "…"

            show rin basic_awayabsent
            with charachange

            rin "Hisao."

            hi "What is it?"

            show rin basic_absent
            with charachange

            rin "Do you love me?"

            "I snap to attention, to meet her suddenly very serious face that is not looking only at the flowers any more."

            "What a tough question, asked just like that, out of the blue."

            "Still, her bluntness compels me to answer rapidly."

            hi "I don't know. Maybe I do."

            "Maybe too rapidly."

            show rin basic_deadpannormal
            with charachange

            rin "What does that mean?"

            hi "…I don't know."

            show rin basic_lucid
            with charachange

            "Rin sighs, perhaps unhappy with my wishy-washy answer. I would be too."

            show rin relaxed_nonchalant
            with charachange

            rin "Me neither."

            show rin relaxed_boredom
            with charachange

            rin "I don't think I know much about love."

            hi "…"

            hi "…It's fine, isn't it?"

            show rin basic_lucid
            with charachange

            "'How should I know?', the shrug of her shoulders seems to say, hesitating to give a firmer answer."

            "She stays silent for only a second too long, but even that second isn't long enough for me to think ahead…"

            show rin basic_absent
            with charachange

            rin "I love you."

            "Those three words freeze me in place like a rabbit staring into headlights, but I'm not a rabbit and I'm just staring into Rin's eyes that seem far, far too impassive for what she just let out of her mouth."

            show rin basic_deadpanupset
            with charachange

            "Rin looks pretty serious though, until she sticks out her tongue, frowns a little and confuses me even more than her words did."

            "Why does she look mildly unhappy?"

            "Was it a confession of her deepest feelings, a test to see how I would react, a test to see how she would react?"

            show rin basic_awayabsent
            with charachange

            rin "It tastes weird."

            hi "…Tastes?"

            show rin basic_lucid
            with charachange

            rin "Yeah. So weird."

            "She laughs, maybe nervously or so I want to think, but stops midway when she notices how strange it sounds."

            show rin negative_spaciness
            with charachange

            rin "Like… I don't know what, I… don't think there is a word for this."

            "Rin keeps on talking as though there was no meaning behind her words, steady and careless words dropping from the same tongue that formed the more important ones."

            show rin negative_worried
            with charachange

            rin "A word for… ummm…"

            "Except."

            show rin negative_annoyed
            with charachange

            rin "…it's like…"

            "She can't."

            show rin basic_deadpanupset
            with charachange

            rin "…"

            "Find the words."

            show rin basic_sad
            with charachange

            rin "…"

            "Rin just keeps staring at me, stumbling with her words as if her brain suddenly ground to a halt."

            "She looks awfully confused, much like how I feel right now as I wait for her to explain."

            "But she doesn't, she just blinks a few times, the flutter of her long lashes catching my fancy because she looks like she is petrified otherwise."

            "Until I realize what they were fighting against."

            show rin basic_crying
            with charachange

            "It's those weird tears again, not associated with sadness or happiness, not pitiable sobbing nor laughter of joy."

            "Just tears, spontaneously and without a warning, like that one time in her classroom."

            rin "Ah."

            "Just a few of them, not enough to make a fuss about, so Rin doesn't make a move to hide them even after noticing."

            "Rin cries, looking like she has no idea why, and somehow a great uneasiness grows in my chest when I look into her watery eyes that stare right back at me."

            "It petrifies me too, the shock of the incomprehensibility of this situation."

            "I just don't know what is happening any more."

            hi "Rin? What's wrong?"

            rin "I…"

            show rin negative_crying
            with charachange

            "She shakes her head in confusion, stumbling to get the words out of her mouth."

            show rin basic_crying
            with charachange

            rin "Sorry…"

            rin "I might be a little afraid of you."

            "The words are muttered slowly, with a small voice that is as disbelieving of what it's saying as I am."

            hi "What? Why?"

            show rin basic_sad
            with charachange

            rin "I don't know. Saying that just made me feel like that."

            show rin basic_absent
            with charachange

            rin "People cry when they are afraid, right?"

            show rin basic_awayabsent
            with charachange

            rin "See? I can do it too."

            "She's averting her gaze now, deliberately not looking at me. It bewilders me, at least as much as what she is saying."

            show rin negative_annoyed
            with charachange

            rin "I… I sometimes, with you, want to run away so badly but I can't move it's like my legs turn into lemon panna cotta pudding and my heart feels like it's going to explode and…"

            show rin negative_sad
            with charachange

            "She slumps her shoulders melancholically."

            rin "Has a thing like this ever happened to you?"

            "…I remember the leaden sky above the frozen forest and the sound of the leafless branches clacking against each other."

            "It's like a memory from another life."

            hi "Yeah. Once."

            hi "My heart hurt a lot back then, too."

            show rin basic_surprised
            with charachange

            rin "But I thought your thing was not contagious."

            "I shake my head and a tiny, slightly forced smile rises on my lips."

            "The other ailment of my heart could very well be contagious and I wouldn't care a bit."

            hi "What are you afraid of? I never thought I was scary."

            show rin negative_confused
            with charachange

            "Rin shakes her head desperately, as if knowing that the tangle inside her mind won't be undone with just that."

            rin "You make me feel that I should be someone else than me."

            show rin negative_sad
            with charachange

            rin "It's a scary thing."

            show rin negative_worried
            with charachange

            rin "It happens when you are being nice to me. Like yesterday."

            rin "I never know what to do at times like that. It's hard."

            "Her voice is barely audible, a whispered admission of something that is too embarrassing to even think, not to mention to say aloud."

            "Rin has never been one to be embarrassed so she does utter it aloud, only timidly as if by instinct."

            show rin basic_upset
            with charachange

            rin "But I want to do something. But I don't know if this me can."

            "For a moment, we just stare at each other as if waiting for the other to say something."

            "…"

            show rin basic_upset_close
            with characlose

            hi "You are so stupid."

            show rin relaxed_surprised_superclose
            with characlose

            "Rin's lips taste salty and scared against mine."

            play sound sfx_heartslow
            show heartattack alpha
            with Dissolve (0.1)

            hide heartattack
            with Dissolve (0.4)

            "As I grasp her into an embrace, I feel my heart thumping in my chest painfully."

            play sound sfx_heartslow
            show heartattack alpha
            with Dissolve (0.1)

            hide heartattack
            with Dissolve (0.4)

            $ renpy.music.set_volume(0.5, 1.0, channel="music")
            $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

            nvl clear
            nvl show dissolve

            n "{vspace=60}Even though I am glad that she can say things like that, they make me sad after all."

            n "Rin's spirit, her passion, her strength. All those things that I hold dear are the ones I don't want to change."

            n "How should I treat them? Where are they headed to? Is that future irrevocably different from mine?"

            n "That anxiety will never loose its grip on my heart, but I think I could learn to live with it."

            n "Slowly, the pain in my heart dies out, and it settles into the same rhythm as Rin's."

            n "{vspace=60}We listen to that for some time."

            n "…"

            $ renpy.music.set_volume(1.0, 1.0, channel="music")
            $ renpy.music.set_volume(1.0, 1.0, channel="ambient")
            stop music fadeout 8.0

            nvl hide dissolve
            nvl clear

            show rin basic_blush_close
            with charadistant

            "After our lips break apart, it takes a while for either of us to realize that we can say something now."

            "…"

            show rin basic_sad_close
            with charachange

            rin "See?"

            show rin relaxed_doubt_close
            with charachange

            rin "You are a really kind person, even when you are not."

            rin "It's the most scariest thing ever."

            show rin relaxed_sleepy_close
            with charachange

            rin "I think… that all I was ever afraid of is your kindness."

            "…"

            hi "Is it bad? Even if you are afraid?"

            show rin basic_lucid_close
            with charachange

            "She thinks about this for a while, furrowing her brow as though this was some kind of hard math problem."

            show rin basic_deadpanamused_close
            with charachange

            rin "No. I'm all right with it. It's fine, if it's you."

            "Like a weight lifted from my chest, her words elate my heart, filling it with… I don't know, happiness?"

            "What else could it be?"

            "This time my smile is genuine."

            show rin basic_deadpanamused
            with charadistant

            "Rin steps back, still smiling gently at me like I do at her."

            show dandelion full:
                alpha 0.0 xalign 0.5 yanchor 1.0 ypos 1.2
                easein 1.0 ypos 1.0 alpha 1.0
            with None

            hide dandelionsfg
            hide dandelionsbg
            show dandelionbg behind dandelion
            show dandelions_blurbg behind dandelion
            show dandelions_blurfg behind dandelion
            with Dissolve(1.0)

            show rin basic_deadpanamused behind dandelionbg

            "While she wipes her face on her shoulder, I pick up a round, plump dandelion clock and bring it to my pursed lips."

            show dandelion gone
            with Dissolve(1.0)

            "Pfff…"

            "They spread out into the wind that picks them up to carry them to a new home."

            "To think, only a few short weeks ago they were so different."

            "This is change."

            "…"

            show dandelion:
                easeout 1.0 alpha 0.0 yanchor 1.0 ypos 1.2
            with None

            hide dandelionbg
            hide dandelions_blurbg
            hide dandelions_blurfg
            show dandelionsbg dense behind rin
            show dandelionsfg dense
            with Dissolve(1.0)

            hide dandelion

            hi "Hey, so the flowers became what they were meant to become, like you said the last time."

            hi "What about you? Did you become a true artist? Or did you not, because you ran away?"

            show rin basic_deadpancontemplation
            with charachange

            "She pauses for a while to ponder my question…"

            show rin relaxed_nonchalant
            with charachange

            "…and shrugs her shoulders."

            "It almost makes me laugh."

            "The carefree easiness of her gesture is a lovely thing, a sign of how Rin can, truly and really, without any restraints whatsoever, shed the entire weight of the world from her shoulders, should she will so."

            "She is, in every possible and probably a few impossible ways… free."

            "And I think I might love her for that."

            show rin basic_absent
            with charachange

            rin "I don't think it matters."

            show rin basic_deadpandelight
            with charachange

            rin "Let's just watch the clouds for today."

            play music music_twinkle fadein 2.0

            scene evbg rin_goodend_base:
                xalign 0.0
                1.0
                easein 20.0 xalign 1.0
            show dandelionsbg dense
            show rin goodend_1:
                xalign -0.5
                1.0
                easein 20.0 xalign 1.0
            show dandelionsfg dense
            show evfg rin_goodend:
                xalign -1.0
                1.0
                easein 20.0 xalign 1.0
            with whiteout

            "She takes five steps to climb on a large rock so she can rise as high as it's possible here, and stands on tiptoes."

            "When you reach for the clouds, every inch counts."

            hi "Sure, let's watch the clouds. It's good to do something you really want to do, every now and then."

            rin "Yeah. You are probably right."

            "I glance upwards at the blue sky opening high above us."

            "It's a deep, cerulean vastness that spreads to fill my entire field of vision and beyond."

            "Yet Rin stays on her rock, peering at the distant horizon where the rain clouds are drifting farther away from us."

            rin "I have decided something."

            "That dreaming voice of hers, spoken to the wind that carries it to my ears, is lacking resolve in tone but is full of it in meaning."

            rin "It's all right to be me after all."

            $ renpy.music.set_volume(0.5, 1.0, channel="music")
            $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

            nvl clear
            nvl show dissolve

            n "{vspace=90}It's all right? Her decisions always seem to be pretty… far out."

            n "Well, I suppose that is an important realization."

            n "Coming to terms with oneself, accepting yourself, being fine with what you are."

            n "A simple resolution of heart that for some people is overbearingly hard to do, if not impossible."

            n "I do realize well enough that I might also be one of those people."

            n "Rin too… "

            n "Maybe we are not that different after all."

            n "Maybe to accept someone else, you must first accept yourself."

            n "Maybe that is a necessary step, which we didn't take until now."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")
            $ renpy.music.set_volume(1.0, 1.0, channel="ambient")

            nvl hide dissolve
            nvl clear

            "Looking at her standing on that rock, I believe that she can find whatever she is looking for."

            "And so can I."

            show evbg at right
            show rin goodend_1b at right
            show evfg at right
            with charachangealways

            "The wind catches her hair and clothes, and Rin spreads her short arms into an embrace that is so very very tiny, but as wide as she can ever do."

            "For a moment it looks like she herself might take flight, and I have to hold myself back to not reach for her shoulder, to not drag her back to me."

            "But this picture is something I can only watch, it is something for me to remember."

            "Rin's sleeves are flapping freely in the wind, her hair wildly tousled by it, her skin touched by the setting sun."

            "Her sleek form that I've come to adore is quivering in the cool wind that carries the small white specks past her, each a beginning of a new flower."

            "All that is engraved inside my heart."

            "Like those tiny seeds scattered into the wind, I'm sure that Rin too can take her place in this world without the need to create her own inside of it."

            "Maybe she believes it too, and standing as close to heaven as possible, she is giving the world a big hug."

            "To me it seems like the entire world really could fit there, between those small arms of hers, inside of her all-encompassing embrace."

            show rin goodend_2
            with charachange

            rin "Hisao?"

            "She looks at me in the same way she calls my name, carelessly over her shoulder with a strange happiness in her voice and in her eyes."

            show evbg:
                acdc_warp 12.0 zoom 1.15
            show rin goodend_2_hires:
                zoom 0.769
                acdc_warp 12.0 zoom 1.0
            show evfg:
                acdc_warp 12.0 zoom 1.45
            with charachangealways

            "I gaze into those mysterious, dark eyes that are curiously twinkling from below her auburn hair."

            "Although I'm too far from her to see it, I'm sure they are reflecting my image."

            hi "What is it?"

            rin "What's the word for when it feels inside your heart that everything in the world is all right?"

            stop music fadeout 4.0
            stop ambient fadeout 4.0

            if _in_replay:
                return

    return

label separate_of_dg_and_wl:
    play music music_daily fadein 0.5

    scene bg school_scienceroom
    with locationchange

    "The last day before summer vacations is waning slowly."

    "Science is the final exam of the trimester and then we are free."

    "The collective yearning for liberty is almost palpable in the classroom, even though the weather seems a tad cloudy."

    "It might rain today, who knows."

    $ renpy.music.set_volume(0.5, 1.0, channel="music")

    scene ev rin_doodle
    with locationchange

    "I've already finished the test because it was pretty easy, so I'm doodling lazily on the flip side of the paper, waiting for Mutou to call time."

    "It also prevents Misha from trying to covertly look at my answers over my shoulder."

    "She might fool the inattentive teacher, but I can tell that she is trying to look."

    "I guess it's her best bet at passing the test. Doesn't make me feel any mercy though, so I just ignore her and look around me."

    $ renpy.music.set_volume(1.0, 1.0, channel="music")

    scene bg school_scienceroom
    with locationskip

    "It's quiet."

    "The only sounds in the classroom are the quiet shuffling of papers and Mutou's constant coughing."

    "It makes my awareness of the surroundings slowly drift to the backstage of consciousness, giving room to other things."

    return

label a4rc1o1:
    $ renpy.music.set_volume(0.2, 0.2, channel="ambient")

    hi "But aren't you happy people are interested in your paintings?"

    hi "I mean, isn't that why you went ahead with having the exhibition and all?"

    hi "Of course they would ask you questions, if they think it's interesting."

    show rin negative_annoyed_close_ni
    with charachange

    rin "It's like having sunrise twice in a row when you want to bathe naked in moonlight."

    show rin negative_angry_close_ni
    with charachange

    rin "Nice, but…"

    "…it's not good enough, I complete the sentence for her even though I don't understand her inappropriate metaphor."

    hi "I don't get it."

    hi "You should try to be happier. It's your big night, after all."

    hi "All these people are here to see your paintings. I think it's awesome."

    "I wait for her to say something, either for or against, but Rin keeps brooding."

    "She doesn't want to answer questions, or explain to me what's wrong."

    "If she had something to say, the words are left unspoken."

    "The words that she cannot say."

    "I shudder against the chill wind that blows in the streets, and its howling fills the silence."

    hi "We should go back in."

    hi "You've got everyone worried."

    stop ambient fadeout 0.5
    play sound sfx_storebell

    scene bg gallery_int
    show crowd
    show nomiya talk at twoleft
    show sae neutral at tworight
    with locationchange

    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    play ambient sfx_crowd_indoors fadein 2.0

    no "Ah, there you are! Feeling better? It can get pretty hot in here, a dizzy spell can catch you off guard."

    show nomiya veryhappy
    with charachange

    "He laughs brashly, almost obnoxiously."

    show nomiya talk
    with charachange

    no "You should drink something if you're feeling weak, Tezuka."

    show nomiya talk:
        center
        xpos 0.25
    show sae neutral:
        center
        xpos 0.8
    with charamove

    show rin basic_lucid:
        center
        xpos 0.55
    with charaenter

    "Rin nods weakly, but it seems to be enough to convince Nomiya that she is fine."

    "He pushes Rin a bit forward to introduce her to the person he was conversing with before."

    show nomiya smile
    with charachange

    no "So, about what we were talking about before…"

    "Man" "Ah yes, I'm very excited to meet…"

    stop music fadeout 8.0

    "I am shut out of the conversation, and the background noise of dozens of other discussions fills my ears with indistinct buzz."

    "Even Emi has disappeared somewhere."

    "Standing in the middle of a crowd is a surprisingly lonely feeling."

    "Not only Rin, but everyone else here seems to be a part of something I am not a part of."

    "I am happy for her, I really am, but it makes me feel that I haven't accomplished anything yet."

    "Rin is living proof of the potential of a human being. She overcame her disability, even made it a strength."

    stop ambient fadeout 4.0

    "She should be happy."

    "What is my potential?"

    "Rin made it this far, but how far can I go?"

    scene black
    with dissolve

    return

label a4rc1o2:
    $ renpy.music.set_volume(0.2, 0.2, channel="ambient")

    hi "But if you found someone like that, then what?"

    hi "Do you really think that it would be some kind of be-all, end-all thing, star-crossed lovers and happily ever after?"

    show rin basic_absent_close_ni
    with charachange

    "My question is met with a blank stare, the darkness in her eyes unfazed by the thinly veiled bitterness."

    show rin negative_worried_close_ni
    with charachange

    rin "No, I don't think that."

    show rin negative_annoyed_close_ni
    with charachange

    rin "But at least then I wouldn't have to be alone."

    "She whispers the words to the lights of the town but I hear them anyway."

    show rin negative_sad_close_ni
    with charachange

    rin "I shouldn't have done this. Not yet."

    hi "The exhibition?"

    show rin basic_lucid_close_ni
    with charachange

    "She nods and closes her eyes, breathing calmly out as if to prove she can, and then continues talking to herself."

    hi "Why? Wrong conjunction of the planets?"

    show rin basic_sad_close_ni
    with charachange

    rin "No, not that. I double-checked, and I got up with the right, I mean left, foot and did everything else left, I mean right."

    show rin negative_sad_close_ni
    with charachange

    rin "It's me."

    show rin negative_worried_close_ni
    with charachange

    rin "I was wrong."

    hide rin
    with charaexit

    "She stands straight and stretches before stepping past me out into the street."

    hi "Wait, where are you going?"

    show rin basic_absent_ni
    with charaenter

    "She stops on her tracks and turns around, looking at me quizzically."

    show rin basic_awayabsent_ni
    with charachange

    rin "School. I'm leaving."

    hi "What… why?"

    show rin basic_absent_ni
    with charachange

    rin "Because I want to be me."

    $ renpy.music.set_volume(0.4, 1.0, channel="ambient")

    hide rin
    with charaexit

    "Rin walks off, leaving me behind utterly confused."

    hi "Rin!"

    "But… something she said really touched me, or maybe it was the way she said it."

    "Maybe it was the fact that {b}she{/b} said it."

    "I want to say something back to her, before I forget this feeling again."

    "As if granting me a wish, Rin stops in her tracks. She doesn't turn around, just keeps waiting for me to say what I want to even though I didn't have time to think what…"

    hi "Rin… listen. I… I don't believe you have to be alone, even if you never meet anyone like that."

    "I don't know if she heard my words, but either way, she doesn't react in any way."

    "For the final time, she starts walking away from the gallery."

    play sound sfx_storebell
    stop ambient fadeout 0.5

    scene bg gallery_int
    show crowd at center
    show nomiya frown at twoleft
    show sae doubt at tworight
    with locationchange

    $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
    play ambient sfx_crowd_indoors fadein 2.0

    no "So? Where's Tezuka?"

    "I can only shake my head, but as it doesn't seem to be a sufficient answer I have to say something."

    hi "She ran away."

    show nomiya stern
    with charachange

    no "What?"

    "The horrific realization spreads on his face like wildfire."

    show nomiya serious
    with charachange

    no "This is a fiasco! Catastrophe!"

    no "What is that girl thinking, the most important event of her life, and she just runs off?"

    show nomiya stern
    with charachange

    no "And you! Why didn't you stop her? I'm going to hold you personally responsible…"

    show sae neutral
    with charachange

    "Sae interrupts him, holding her hands up calmingly."

    "It's good she intervened; the teacher was starting to get a few weird looks from the nearby guests."

    show sae smile
    with charachange

    sa "Now, now, Shinichi. She probably just had stage fright. I don't know her as well as you people do, but I did get the image that she is somewhat peculiar."

    sa "This kind of thing can happen."

    show sae neutral
    with charachange

    sa "It'll be fine. I'll explain that she suddenly became ill. The guests will surely understand."

    show nomiya frown
    with charachange

    no "But…"

    show sae smile
    with charachange

    sa "Look around you, everyone seems to be rather happy with their free wine and chitchat."

    show nomiya serious
    with charachange

    no "The guests will be fine, but we are missing on opportunities here! Networking, making contacts and acquaintances!"

    show emicas frown_close:
        center xpos -0.35 alpha 0.0
        ease 1.0 xpos 0.15 alpha 1.0
    with None

    show bg gallery_int at left
    show crowd at left
    show nomiya serious:
        xpos 0.5
    show sae smile:
        xpos 0.9
    with charamovefaster

    "As the adults keep arguing about something that can't be helped, Emi tugs my sleeve to get my attention."

    "She doesn't look very happy either."

    show emicas awayfrown_close
    with charachange

    emi "Come on."

    hi "Where?"

    show emicas frown_up_close
    with charachange

    emi "We are going to find Rin and kick her ass."

    hi "What?"

    show emicas angry_close
    with charachange

    emi "I can't believe it, she is so stupid!"

    emi "That Rin, how can she do this? I'm telling you, she doesn't have a bit of common sense in her head!"

    "Emi is seriously angry, only missing steam rising from her ears."

    "I guess I understand Emi, she is {b}that{/b} kind of a person."

    "'Give up' has never felt like a part of her vocabulary, and maybe she feels it shouldn't be a part of anyone's vocabulary."

    hi "It's probably best to leave her alone for tonight."

    show emicas angry_up_close
    with charachange

    emi "What? Are you a Rin expert now?"

    "She takes a firm stance and puts her hands on her hips confrontationally."

    "It's like she wants to pick a fight with me too."

    hi "No, I don't think that's even possible in the first place."

    hi "I just don't think kicking her ass would do her any good."

    show emicas frown_close
    with charachange

    "My melancholic remark surprisingly works, as Emi slumps her shoulders a little and sighs."

    emi "I know that."

    hi "You do?"

    stop music fadeout 2.0

    show emicas awayfrown_close
    with charachange

    emi "The last time I did that, it changed nothing."

    stop ambient fadeout 1.0

    scene ev busride_ni
    with locationskip

    $ renpy.music.set_volume(1.0, 1.0, channel="ambient")
    play ambient sfx_businterior fadein 2.0

    "The ride back to school in an empty late-night bus is silent."

    "Both of us keep staring at the lights flashing past the windows without saying a word."

    stop ambient fadeout 1.0

    scene bg school_dormext_full_ni
    with locationskip

    play music music_soothing fadein 0.5

    "The nightly grounds are quiet, lit only by the wan moon and yellow lamp posts."

    "We say our goodnights in front of my dormitory."

    show emicas awayfrown_up_ni at center
    with charaenter

    "Emi reflexively clenching her fists compels me to ensure that she won't assault Rin the moment I let her out of my sight."

    hi "Promise me to not go scold her?"

    show emicas angry_up_ni
    with charachange

    "She looks up at me, her eyes again flaring with anger that I match with as calming a stare as I can."

    "It's only easy to face an angry woman if you are not the target of her ire."

    "After a minute of the mismatched staring contest, she sighs and shakes her head in defeat."

    show emicas closedsmile_ni
    with charachange

    emi "You are too nice, Hisao."

    show emicas weaksmile_ni
    with charachange

    emi "Did you know that?"

    "Hints of a smile are tugging the corners of her mouth as she says that, and she seems a lot more relaxed."

    "What a sudden change of mood."

    "Maybe she wasn't as angry as it seemed to begin with."

    "Maybe her moods change easily."

    hi "If I was, I would've let you have your way."

    show emicas wink_ni
    with charachange

    emi "Does that mean you are only nice to Rin?"

    "Both of us are hiding our concern behind empty jokes, but at least it puts me in a good mood."

    "Emi waggles her eyebrows with a half-amused smirk, trying to push my buttons. Not gonna work."

    hi "No, it just means I'm not nice only to you."

    show emicas angry_up_ni
    with charachange

    emi "HEY!"

    stop music fadeout 2.0

    hi "Good night, Emi."

    scene black
    with dissolve

    return
