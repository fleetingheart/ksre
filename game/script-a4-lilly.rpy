# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a4_lilly:
    label .slow_steps:
        scene bg school_scienceroom
        with locationchange

        nvl clear
        nvl show dissolve

        $ renpy.music.set_volume(0.5, 1.0, channel="music")
        play music music_normal fadein 1.0

        n "{vspace=90}After the excitement of our trip to Hokkaido, it seems strange to be right back to the usual daily routine so soon. Indeed, it feels like a normal day, the same as any other."

        n "{vspace=30}Well, that's what I'd like to think, anyway."

        n "{vspace=30}To tell the truth, the atmosphere of the entire class, no, the entire school has changed."

        n "While an undercurrent of subdued trepidation had previously pervaded the class, now that the exams are in sight it's boiled over into frantic studying rarely seen otherwise."

        n "One day until exams start. It's horrific, really, that instead of studying we went and wasted our time up north. We were such model students, too."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl hide dissolve
        nvl clear

        show misha perky_confused_close:
            xpos -0.1 xanchor 0.5 alpha 0.0
            ease 1.0 xpos 0.1 alpha 1.0
        with None

        show bg at bgright
        with charamovefaster

        show misha:
            xpos 0.1 xanchor 0.5 alpha 1.0

        "Glancing around the class, even the bubbly, ever-energetic Misha seems oddly deflated. She sits at her desk, nervously chewing a pen while Mutou lectures from the front of the class."

        "Wait… on closer inspection, I do believe she's eating it."

        show misha:
            ease 1.0 xpos -0.1 alpha 0.0
        with None

        show bg at center
        with charamovefaster

        hide misha

        "Tearing my eyes from the sorry spectacle, I turn my attention elsewhere."

        show hanako defarms_strain:
            xpos 1.1 xanchor 0.5 alpha 0.0
            ease 1.0 xpos 0.94 alpha 1.0
        with None

        show bg at bgleft
        with charamovefaster

        show hanako:
            xpos 0.94 xanchor 0.5 alpha 1.0

        "Hanako sits frantically scribbling in her notebook, her face mere inches away from the page, seemingly trying to record every word that leaves Mutou's mouth."

        show shizu basic_normal:
            xpos 0.0 xanchor 0.5 alpha 0.0
            ease 1.0 xpos 0.3 alpha 1.0
        show misha perky_confused_close:
            xpos -0.1 xanchor 0.5 alpha 0.0
            ease 1.0 xpos 0.1 alpha 1.0
        show hanako:
            ease 1.0 xpos 1.1 alpha 0.0
        with None

        show bg at bgright
        with charamovefaster

        hide hanako
        show shizu:
            xpos 0.3 xanchor 0.5 alpha 1.0
        show misha:
            xpos 0.1 xanchor 0.5 alpha 1.0

        "Shizune's, well… Shizune. Cool as a cucumber, she sits diligently taking notes with her attention wholly focused on the front of the class."

        "Truth be told, it's what I should be doing as well, if not for the fact that I feel like I have a pretty good handle on what's being covered already."

        "I wonder how Lilly's doing. While she does have a good head on her, she has plenty on her plate, unlike me. Her class representative duties, taking care of Hanako, her other social contacts, her extra English studies… that girl really does take on a lot."

        scene bg school_scienceroom
        with shorttimeskip

        play sound sfx_normalbell

        "The lunchtime bell brings a sigh of relief from the entire class, Mutou being no exception. I get the feeling he much prefers the more laid-back atmosphere of his normal classes to the frantic pace of exam preparation we're subjected to right now."

        mi "Hicchan~…"

        show misha perky_sad_close:
            xpos 0.1 xanchor 0.5 alpha 0.0
            ease 1.0 twoleft
        with None

        show bg at bgright
        with charamovefaster

        show misha at twoleft

        mi "Help me~…"

        "I lower my eyelids to half-mast, making clear my intention of doing quite the opposite."

        mi "Help me, help me, help me~…"

        hi "Not going well?"

        show misha perky_confused_close
        with charachange

        mi "Shicchan's going to be fine, but I think I might die. Am I going to die, Hicchan? Will you let me die from all this work?"

        "How maudlin. Given that she's neither the brightest student in the class, nor the most diligent, it isn't a great surprise that she's finding it hard to cope with the workload."

        hi "Sorry Misha, but I've got my own work to do. I thought you and Shizune would be studying together over the long weekend, anyway?"

        show misha sign_sad_close
        with charachange

        mi "Studying's too boring to waste a holiday on, Hicchan! Shopping together was much more fun, wasn't it, Shicchan?"

        show shizu behind_blank behind misha at tworight
        with charaenter

        "It's only now that I realize Shizune's been looking over to us, and that Misha's arms have been moving likely all this time. I must be really zoned out to not have noticed."

        hi "What is it with girls and shopping, anyway? Even Lilly and Hanako have dragged me out with them a couple of times."

        show misha hips_grin_close
        with charachange

        mi "But you went anyway? It's so rare to see a guy that likes going shopping~…"

        hi "Well, my role would probably be best described as 'pack mule'. I can't say I share your enthusiasm about the experience."

        hi "Back to the exams; you studied after you got back from the days off, didn't you, Shizune?"

        show shizu basic_normal2
        with charachange

        shi "…"

        show misha sign_smile_close
        with charachange

        mi "Of course, Hicchan. It's only sensible to study in the days before…"

        show misha perky_sad_close
        with charachange

        mi "U~rgh."

        "Misha makes a sound vaguely similar to a dying cow as she realizes her folly and unceremoniously flops onto her desk, betrayed even by her best friend."

        show shizu basic_angry
        with charachange

        "Judging from Shizune's quite frustrated look at Misha, she probably told her to study as she did."

        hi "Don't worry, you can still gain some grades if you start studying now."

        hi "Maybe."

        "Misha does not seem overly amused. It seems the bubbly balloon of everlasting cheerfulness has been cruelly popped."

        show shizu behind_blank
        with charachange

        shi "…"

        show shizu behind_blank_close
        with characlose

        pause 0.3

        show shizu adjust_frown_close
        show misha perky_confused_close
        with vpunch

        "Shizune's signing goes unnoticed by the moping Misha, earning her a quick poke in the shoulder. It takes barely a moment for Misha to get back into form."

        show misha hips_smile_close
        with charachange

        mi "Oh, ah, so what did you do over the weekend, Hicchan?"

        hi "Just took a trip up north with Lilly and Hanako. It was pretty nice."

        show misha perky_smile_close
        show shizu behind_blank_close
        with charachange

        "I see both of them narrowing their eyes at me, their minds surely in the gutter. The fact that their suspicions are founded makes the situation all the more awkward."

        hi "We just studied and went sightseeing; there's nothing more to it."

        show misha cross_smile_close
        with charachange

        mi "Hmm~…"

        "After such a flagrant lie, I realize that it may not have been the best step, considering Shizune's connections and her total lack of restraint when it comes to questioning someone she suspects of telling untruths."

        "I really have no idea of how she's going to take it, but she'll find out eventually anyway. It isn't as if it's really her business whom I date, in any case."

        hi "And yes, Lilly and I are going out now."

        show misha hips_grin_close
        show shizu basic_normal2_close
        with charachange

        "While Misha receives the news with an enthusiastic smile, Shizune gives a look of mild surprise somewhat masked by her cool demeanor."

        show shizu behind_blank_close
        with charachange

        shi "…"

        show misha sign_smile_close
        with charachange

        mi "Whoever you date is your business. I hope you two go well together."

        "Misha gives a look that says this is the most quarter I could possibly receive on the matter. It's all I wanted, really."

        show shizu basic_normal2_close
        with charachange

        "After she says this, though, Shizune begins to sign something else, then stops herself and shakes her head at Misha to prevent her from translating."

        hide shizu
        with charaexit

        hide misha
        with charaexit

        "Normally I'd think this strange enough, but the awkwardly casual wave Shizune gives before walking off with Misha in tow adds to my confusion. Shizune's hardly the kind of person to pull a punch or communicate without forethought."

        "I shrug my shoulders at the duo's odd behavior and look towards Hanako's desk, but see that her chair's empty. She was definitely here before, so I guess she just didn't feel like waiting."

        "I'll go grab some food alone, then."

        stop music fadeout 2.0

        scene bg school_hallway2
        with shorttimeskip

        "Walking down the hallway to the unused room that's become a second home to three students in particular, I mournfully look down at the plastic-wrapped salad roll and juice box in my hand."

        "The cafeteria's food really is unappetizing. Maybe I'll consider this my penance for my recent indiscretions."

        "Opening the door, I notice one less quiet figure than I'd expected."

        scene ev lilly_tearoom
        with whiteout

        play music music_lilly fadein 3.0

        "It's strange. Despite having known Lilly for months, I can't help thinking back to the very first time I opened this door and saw her silently sitting in the sunlight."

        show ev lilly_tearoom_open
        with charachangeev

        "Just as she did then, she slowly opens her eyes, unmoving as they are, and calmly addresses me."

        li "Good morning, Hisao."

        hi "It's afternoon, I think."

        hi "Has Hanako been around? She skittered out of class without me even noticing."

        scene bg school_miyagi
        show lilly basic_listen_close:
            center
            ypos 1.1
        with locationchange

        "Lilly cradles her cheek thoughtfully as I take a seat, my bag taking its place against the closest leg of the table and my unsatisfying meal neatly set out in front of me."

        show lilly basic_reminisce_close
        with charachange

        li "She did appear… for a time. She said she had to study for the upcoming exams, and left for the library."

        "We find ourselves not entirely believing her words."

        hi "Well, at least her intentions are in the right place."

        show lilly basic_concerned_close
        with charachange

        li "She is sweet, but she needn't go this far to let us have our space. I might talk to her about it sometime."

        hi "Probably for the best."

        show lilly basic_weaksmile_close
        with charachange

        "For a while we quietly eat our meals, Lilly elegantly nibbling on her sandwiches and sipping her tea as I eat what tastes like a garden sandwiched in dry dough."

        "The atmosphere feels slightly strained, neither of us knowing quite what to say to each other now that our small talk has dried up."

        "Eventually we both finish our food, with no conversation forthcoming for quite some time. Eventually, though, Lilly's soft voice breaks the silence."

        show lilly basic_reminisce_close
        with charachange

        li "A lot happened back there… didn't it?"

        hi "Mm."

        "Again, silence. With both our minds on the same topic, though, I think I have my feelings on that sorted out."

        hi "I know everything happened in kind of a hurry, but… I don't regret anything that happened in Hokkaido. Not one thing."

        show lilly basic_oops_close
        with charachange

        li "Hisao…?"

        "Slightly tense, I take her hands in mine; half to feel her, half to settle my own nerves."

        hi "I stand by my words back there, Lilly. I love you, and I won't leave you. I only wish for you to think the same."

        show lilly basic_weaksmile_close
        with charachange

        "She silently reflects for a long time, which feels like an eternity."

        show lilly:
            ease 1.0 center alpha 0.0

        pause 1.0

        show lilly:
            center
            alpha 0.0

        "Her reverie comes to an end as she takes one hand from mine, placing it over them as she leans her body forwards and stands out of her chair."

        "After a moment's hesitation, her face slightly pensive, her lips meet mine for a brief moment."

        show lilly behind_cheerful_close:
            ease 1.0 ypos 1.1 alpha 1.0

        pause 1.0

        show lilly:
            center
            ypos 1.1 alpha 1.0

        "My mind feels as if it briefly stopped at that moment, barely registering Lilly sitting back in her chair and smiling back at me with ever so slightly reddened cheeks."

        show lilly basic_smileclosed_close
        with charachange

        li "Hearing that makes me very happy, Hisao. I would be glad to stay with you."

        hi "Maybe it would be good to slow things down a bit, compared to before. We still have school, after all, and our exams."

        show lilly basic_giggle_close
        with charachange

        "She gives a mischievous giggle, which proves to be contagious."

        show lilly basic_smileclosed_close
        with charachange

        li "That might be a good idea indeed."

        show lilly basic_smile_close
        with charachange

        li "Do you think you'll fare well in your exams? It's only one day until they arrive, as you say."

        hi "I probably should have studied more, but I think I've got a good enough head to manage."

        hi "That said, I had to bat off Misha and Shizune. Is your class as worried about the exams as mine?"

        show lilly basic_weaksmile_close
        with charachange

        "She lets out an exasperated sigh, all but confirming it. I'm thankful for the atmosphere becoming a bit lighter."

        li "I think so. I've already been asked for help by two of my classmates, and there'll no doubt be more."

        hi "Think of it as your first training in being a teacher, maybe?"

        show lilly basic_smile_close
        with charachange

        li "That's probably a good way to think of it."

        show lilly basic_smileclosed_close
        with charachange

        li "On that note, how are you faring in your English studies? I remember it was far from your strongest subject, and the few sentences you memorized to speak to my mother aren't likely to help."

        "Damn, right on the mark."

        hi "You got me. If you don't mind, would you be able to possibly help in that regard? Please?"

        show lilly basic_planned_close
        with charachange

        li "It would be my pleasure to help you, Hisao. But in exchange…"

        "She lowers her eyebrows at me, her coquettish nature tentatively coming to the fore."

        hi "No problem at all. You'd probably be better off with some help in your studies, though."

        show lilly behind_cheerful_close
        with charachange

        "She beams a smile at me, one of girlish victory that nearly makes me blush. I get the feeling she's aware of how to use her face to twist my judgment, so I should probably be more on guard."

        "Here and now though, a study group seems like an expedient way for both of us to shore up our more lacking skills."

        play sound sfx_warningbell

        "The school bell rings out, reminding us that time isn't going to stand still."

        hi "Huh, lunchtime's over already. It sure is easy to lose track of the time here."

        show lilly basic_weaksmile_close
        with charachange

        li "This room's so far from the other clubs and activities, not much sound can reach us. That's probably most of the reason why."

        show lilly at center
        with charamove

        "A place far from all the others, alone with just one person whom she loves. As Lilly stands and collects her bag and cane, my thoughts are cast back to the time we spent in Hokkaido."

        show lilly basic_satisfied_close
        with charachange

        li "Ah, before I go; Akira and I are having a homecoming party in my room tomorrow. Will you be able to come?"

        "…and back again."

        hi "My schedule is free, so I should be able to make enough room in my study time to make it."

        show lilly basic_smileclosed_close
        with charachange

        li "Good to hear, Hisao."

        hi "For what it's worth, I'm glad you're back from Scotland. Once exams are over, we should have some more time to ourselves."

        show lilly basic_smile_close
        with charachange

        li "Mm. Holidays start soon after, too."

        hi "We can start the holidays with Tanabata then, just as we promised at the school festival."

        show lilly basic_arablush_close
        with charachange

        "She brings her hand to her cheek and laughs slightly nervously, recalling the event as I silently thank myself for managing to remember."

        "It seems odd to see her react in such a way, though it's not like I never saw her embarrassed before."

        show lilly basic_weaksmile_close
        with charachange

        li "I'd… better be going. Farewell, Hisao."

        hi "Bye."

        hide lilly
        with charaexit

        stop music fadeout 6.0

        "Whether it's out of habit or just a stubborn desire for one small fragment of normality, I hold my hand up in farewell just as I always do. At least I'm consciously aware that I'm doing it now."

        "I think I'm beginning to see a bigger picture than I ever have before, not only with Lilly but also my life ahead."

        "The chains of my past are finally breaking."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .pajamas_and_suits:
        $ renpy.music.set_volume(0.8, 0.0, channel="music")
        play music music_ease fadein 4.0

        scene bg school_girlsdormhall
        with locationchange

        "Walking up the now slightly more familiar corridor of the girls' dormitories, I can hear the faint sound of laughter coming from up ahead."

        show bg at bgleft
        with charamove

        "It doesn't take long to identify the source as Lilly's room, though the deep timbre of the female voice unmistakably belongs not to her, but to her sister."

        play sound sfx_doorknock2

        "I rap my knuckles on the door with the usual three light taps, my hand barely retreating as the door swings open."

        show akira basic_smile:
            xanchor 0.5 xpos 1.0 alpha 0.0
            ease 1.0 xpos 0.9 alpha 1.0

        pause 1.0

        aki "Hey, Hisao."

        hi "Hey. Hello Lilly, Hanako."

        scene ev lilly_bedroom:
            truecenter
            zoom 1.0
            acdc_warp 8.0 zoom 1.03
        with locationchange

        "Hanako looks up tentatively, her hands buried in her oversized pink nightgown. From her side, Lilly turns sideways towards the direction of my voice and smiles."

        "It would be a flagrant lie to say I dislike the sight of her in those pajamas."

        "I catch Akira giving me a sidelong look with a knowing grin, to which I reply with a sharp glare."

        scene bg school_dormlilly at bgleft
        with locationchange

        "She takes the hint, shrugs and walks back to the low table in the center of the room. As I go to join her, Lilly gives me a nod of greeting and starts pouring me a cup of tea."

        show hanagown distant:
            twoleft
            ypos 1.14
        show akira basic_smile:
            tworight
            ypos 1.14
        with charaenter

        hi "It's nice to see you again, Hanako. You've been getting around recently."

        "Lilly wears a look of concentration as the light brown liquid, carefully measured by her finger as always, flows from the teapot into the cup."

        li "It seems Hanako has taken up helping one of the people in your class with the newspaper club. Naomi, I think?"

        show hanagown normal
        with charachange

        "Hanako gives an affirmative nod."

        "Even after spending about two months in the class, I still have trouble remembering the names of those students I rarely talk with."

        "It takes me a few mental contortions to connect the name with a face, but I eventually remember the girl that sits beside Hanako at the back of the class."

        "Naomi Inoue. A fairly average-looking girl, except for her bleached blonde hair."

        "Given her upbeat and straightforward personality, Naomi may have seen an opening to poach Hanako for her club when she enquired about joining one."

        "Either way, it's nice to see Hanako broadening her horizons. When I first met her, the idea of her joining a club with anyone but Lilly would have seemed utterly laughable."

        hi "That'd explain how busy you've been. Enjoying it?"

        show hanagown smile
        with charachange

        ha "Mm. It's… really interesting."

        "As always, Hanako's far from being talkative. Some things never change, and it seems that Hanako's personality is one of them; she'll likely always be one to shy away from being overly social."

        show hanagown smile:
            center
            ypos 1.14
        show akira basic_smile:
            right
            ypos 1.14
        show bg school_dormlilly at center
        with charamove

        show lilly basic_smileclosed_paj:
            left alpha 0.0
            ease 1.0 ypos 1.17 alpha 1.0

        pause 1.0

        "Warned by the sound of crockery against the table as Lilly gently places my drink in front on me, I thank her and take a long sip. Hanako and Lilly are attending to their own, and Akira is quaffing a mug of strong-smelling black coffee."

        show akira basic_laugh
        with charachange

        aki "You're a lucky bastard, Hisao."

        hi "Huh?"

        "I can't help grimacing at her teasing smile, still visible around the edges of the mug pressed to her lips."

        show akira basic_ending
        with charachange

        aki "Seeing my sister in her pajamas, there's a lotta men out there who'd like to be where you are."

        "I've seen a lot more than that of her, not that I'd admit it."

        show lilly basic_emb_paj
        with charachange

        li "Akira!"

        show akira basic_smile
        with charachange

        aki "Hey, I'm just teasing."

        "She leans over to me as much as she can, whispering with a sly grin written on her face."

        show akira basic_kill
        with charachange

        aki "And Hanako, too. You perv."

        hi "Hey, it was her idea."

        show hanagown distant_blush
        with charachange

        ha "Um, I… uh…"

        "We both look over to her, her face turned to the ground and her hands fidgeting in the lap of her nightgown."

        show hanagown smile
        with charachange

        ha "If… it's Hisao… I don't mind…"

        "Ah, this could be bad. I know Hanako's altogether too innocent to bother reading too much into such a thing, but the expression Akira directs at me is positively stormy."

        show lilly basic_concerned_paj
        show hanagown normal
        with charachange

        li "Um… Akira… please…"

        "It seems Lilly can sense Akira's sudden change in aura just as well as I, even without seeing it for herself."

        show akira basic_boo
        with charachange

        "Akira slowly looks away from me, like an attack dog leashed by its owner in the nick of time. I breathe a sigh of relief."

        "I can't think of a more appropriate time to try and change topics than around now."

        hi "If you don't mind me asking, Akira, what do you do for a living? I've never seen you out of that suit."

        show akira basic_laugh
        with charachange

        aki "Thinking about what to do with yourself after school's over, eh?"

        show akira basic_smile
        with charachange

        aki "I'm a lawyer. For the most part, I work in the legal department of the Japanese branch of our family's company."

        aki "The most boring possible answer, I suppose. Law's a pretty dry topic to most people."

        hi "Kinda."

        show akira basic_lost
        with charachange

        aki "Oi, you're not supposed to agree."

        show lilly basic_giggle_paj
        show hanagown normal
        show akira basic_smile
        with charachange

        "Lilly gives an amused giggle while holding her teacup and saucer, Hanako quickly joining her."

        "This friendly atmosphere between everyone is something I'd missed while Lilly and Akira were on their trip. While the dealings I had with Hanako didn't help, I think just not having Lilly around changed the mood."

        show lilly basic_smileclosed_paj
        with charachange

        li "It's nice to be back. I missed you, Hisao, and you too, Hanako."

        hi "Same goes for the both of us. I'm guessing your classmates were happy to see you back."

        show lilly basic_ara_paj
        with charachange

        li "In a manner of speaking, yes."

        show akira basic_laugh
        with charachange

        "Akira's amused snort shows she's well aware of Lilly's attitude towards such figures of speech. I imagine she'd have to be, given how long they've been together."

        show hanagown normal
        with charachange

        ha "Did you have fun in Scotland?"

        $ renpy.music.set_volume(0.1, 2.0, channel="music")

        "For a moment I wonder why she's asking, it having been quite a while since they came back, but then I remember everything that happened. We've simply not had time to look back, what with the exams and our Hokkaido trip."

        show lilly basic_reminisce_paj
        show akira basic_annoyed
        with charachange

        "Lilly's face goes distant for a moment, and the fact that Akira's first reaction is to look over to her sister doesn't escape me. Nonetheless, she quickly collects herself."

        $ renpy.music.set_volume(0.8, 0.4, channel="music")

        show akira basic_smile
        show lilly basic_weaksmile_paj
        with charachange

        li "It was… nice. I… we… hadn't met our family in such a long time, so it was a wonderful reunion."

        show akira basic_boo
        with charachange

        aki "Yeah, I guess that's right. Their house being beachside was the best part, though."

        "From her dismissive tone, I get the feeling Akira doesn't like their family as much as Lilly does."

        show lilly basic_giggle_paj
        with charachange

        li "You only liked that because you finally had time to play around."

        show akira basic_ending
        with charachange

        aki "Just 'cause I'm the better swimmer…"

        show lilly basic_smileclosed_paj
        with charachange

        li "I don't take after the athletic side of the family, that's all."

        show akira basic_laugh
        with charachange

        aki "Well, you can take heart in the fact that you got the height genes at least."

        show akira basic_boo
        with charachange

        aki "And the bust genes…"

        show lilly basic_weaksmile_paj
        with charachange

        li "That's not really the right kind of thing to say around others…"

        "Though Lilly pretends to scold Akira, she does so with an unmistakable, slightly cheeky grin on her face."

        show hanagown distant_blush
        with charachange

        "I doubt Akira really minds that, judging from her nonchalant expression. While I don't either, Hanako's looking down and blushing furiously beside me."

        "The sisters' antics aside, their parents really do lead a bourgeois lifestyle."

        "It seems utterly divorced from the life that Lilly and Akira have lived until now. I suppose practicality must have made the decision for them."

        "To have come from such a wealthy and well-connected lineage only adds to the almost noble air Lilly seems to have, though. It's a small wonder none of it seems to have rubbed off onto Akira."

        "They really are as little alike as siblings could be. Their only similarity seems to be their shared confidence, which can be both endearing and a headache at times."

        stop music fadeout 2.0

        scene bg school_dormlilly
        show lilly basic_smileclosed_paj:
            twoleft
            ypos 1.17
        show akira basic_smile:
            tworight
            ypos 1.14
        with shorttimeskip

        "Most of the night continues much the same, with Hanako eventually leaving the Satou sisters and me to ourselves as she heads back to her dorm room for a rest."

        "For a while, only the barely audible sound from Lilly's teacup and saucer can occasionally be heard as she slowly drinks. The silence is strained as Lilly and I wait for the elephant in the room to be addressed."

        show akira basic_boo
        with charachange

        aki "So…"

        $ renpy.music.set_volume(1.0, 0.0, channel="music")
        play music music_dreamy fadein 4.0

        show lilly basic_weaksmile_paj
        with charachange

        "Lilly dutifully puts her cup down, giving her sister her undivided attention."

        "With Lilly and me on one side of the low table and Akira at the other, this almost feels like a judge passing down a verdict."

        show akira basic_smile
        with charachange

        aki "I hear that you two are going out now?"

        "I glance sideways at Lilly to confirm her as the source of Akira's knowledge. She gives a gentle nod to Akira, which I mirror in affirmation."

        "Deciding that this is the proper time and place to do so, and Akira being the closest figure to a parent Lilly's had for much of her life, I bow deeply with my hands on the floor before me and my head very nearly the same."

        hi "I'll take good care of your sister, Akira. I promise you."

        show lilly basic_smile_paj
        with charachange

        li "See? He's a lovely young gentleman."

        "She must've heard my voice coming from a lower position than usual."

        "I slowly bring myself back up, my eyes tentatively looking to Akira from under my brow."

        "To tell the truth, I very much doubt my suited judge will raise any objections. She's very definitely the type to make her disapproval with others well known, something that lends her a measure of respect in my eyes."

        show akira basic_laugh
        with charachange

        aki "The old-fashioned kind, huh? Well, he's the kind of person I guessed you'd go for."

        show akira basic_smile
        with charachange

        aki "I don't have a problem with it, and I wish you two the best. Even if I didn't like it, I couldn't really do anything anyway."

        "I offer a nod of appreciation to her as Lilly gives a small sigh of relief, likely more out of duty than any actual belief Akira might have had any problems with us being together."

        show akira basic_evil
        with charachange

        aki "I do wonder though… how's the rest of the family taking it, particularly the part residing at Yamaku? Have you told her?"

        show lilly basic_listen_paj
        with charachange

        "Smiles turn to grimaces as Akira grins downright evilly. Those closest know how to twist the knife best, after all."

        show lilly basic_weaksmile_paj
        with charachange

        li "'Putting up with it' may be the best term for the situation. Don't you agree, Hisao?"

        hi "Yeah, that sounds about right. At least she's being reasonable about it."

        show akira basic_boo
        with charachange

        aki "Good to hear. That girl can be a handful at the best of times."

        show akira basic_smile
        with charachange

        aki "We sent a few messages back and forth during and just after the trip, and she was already busting my chops for seeing my boyfriend when we came back, after leaving Hideaki for so long. She really does care for the little guy."

        "I cast my mind back to Shizune's odd reaction after telling her about our relationship, but decide not to bring it up. It's no doubt simply born of their mutual antipathy, and Akira's comments only back that up."

        show akira basic_boo
        with charachange

        aki "Well then, that's settled. Gotta get to work early tomorrow, so I'd better be off."

        show akira basic_smile at tworight
        with charamove

        "She rises from the table with a grunt, her hand on her knee to push herself up. I just notice Akira's eyes lingering on Lilly for a couple of seconds before turning away, as she begins to take her leave."

        hide akira
        with charaexit

        "After she walks out the door, she stops and looks up thoughtfully before turning to us one last time."

        show akira basic_lost:
            xanchor 0.5 xpos 1.0 alpha 0.0
            ease 1.0 xpos 0.9 alpha 1.0

        pause 1.0

        aki "Oh yeah, I almost forgot to tell you."

        show akira basic_ending
        with charachange

        aki "Use protection. Every time."

        "I gag violently on the tea in my mouth. Contrary to my own, Lilly's composure holds perfectly as she seems entirely unfazed. I'm kind of impressed."

        show lilly basic_smile_paj
        with charachange

        li "We are, don't worry."

        show akira basic_smile
        with charachange

        aki "'Atta girl. Seeyas."

        show akira:
            ease 1.0 xanchor 0.5 xpos 1.0

        pause 1.0

        hide akira

        "And with that she turns and strides away, a hand held high as she disappears into the darkened hallway, closing the door behind her."

        show lilly basic_smile_paj:
            center
            ypos 1.17
        show bg school_dormlilly at bgright
        with charamove

        "The most reaction I can muster is flopping forwards onto the table, completely drained of energy and truly exhausted by her. Lilly's ability to hold her own against that suited devil is something I admire."

        hi "She really is incredibly blunt. I don't think I'll ever be able to keep up with your sister's energy."

        show lilly basic_smileclosed_paj_close:
            center
            ypos 1.1
        with characlose

        "As I feel Lilly's soft hand come to rest on my own, I roll my head to the side to see her gently smiling. For a long time, we simply sit beside each other silently."

        "Given her unquestionably unusual height, she is pretty much exactly as tall as I am; probably a couple of centimeters higher if anything. Like this, she appears even taller."

        "The feeling of her pale, soft hand against mine is a pleasant one, as is the sight of the thin silken pajamas she wears, showing her curves and collarbone."

        show lilly basic_smile_paj_close
        with charachange

        li "You do get on well though, even if you do say that."

        hi "I guess. You know, you two are a lot more alike than I first thought when I met you."

        show lilly basic_cheerful_paj_close
        with charachange

        li "Then it's a good thing I quickly stopped you from going after her, isn't it?"

        "Though she jokes about it, my assessment of my inability to keep up with Akira, either physically or mentally, was quite in earnest."

        "Lilly's slow-paced and ladylike, almost motherly, nature is perhaps the single thing that helped me most in my first weeks at Yamaku."

        "Come to think of it…"

        hi "Wait… since when were we using protection?"

        show lilly basic_pout_paj_close
        with charachange

        "As I give a curious look to my side, Lilly's cheeks puff out as she huffs at me."

        li "Unlike you, I remembered. The packet is in the cupboard next to the sink."

        "So, I'm not the only one of us that takes a pill. In hindsight, I feel rather thoughtless for not remembering at all and leaving it to Lilly."

        "Looking over to the cupboard she mentions, I notice again the knee-high piles of books around us that were here the other times I'd visited. For the most part, they're lined up against the wall to give a little more room around the table."

        hi "Why don't you get a bookshelf for your books? It's odd to see books just piled around, especially given that your room looks so neat and orderly otherwise."

        show lilly basic_smileclosed_paj_close
        with charachange

        li "They're easier to find this way; I know exactly which pile each book is in."

        hi "Wouldn't you still know that after putting each set on a different shelf?"

        show lilly basic_weaksmile_paj_close
        with charachange

        li "That may be, but…"

        "So she's not immune to bouts of laziness after all."

        hi "You have so many of them, it's kind of a shame we can't share our book sets despite both of us reading so much."

        show lilly basic_giggle_paj_close
        with charachange

        "She gives a short giggle."

        hi "Come to think of it, why do you order your books through Yuuko? I imagine there'd be plenty of sites that you could order books in Braille from, especially in English Braille. There are a lot of text-to-speech programs, too."

        show lilly basic_displeased_paj_close
        with charachange

        "She turns her head slightly away from me, which strikes me as somewhat surprising."

        li "I'm just… not all that good with computers. I'm all right with typewriters and braillers… but that's about it."

        "Her tone almost makes me chuckle. She's a prideful person, so admitting something like that must be difficult."

        "So, Lilly's the low-tech kind of person. Given her old-fashioned personality, it's not really a stunning surprise."

        hi "I wouldn't worry about it. A lot of people aren't really that good with them, so it's not that unusual."

        show lilly basic_concerned_paj_close
        with charachange

        li "'That' unusual…"

        "Now she's even more depressed. It feels like I'm twisting the knife, rather than healing her wounds."

        show lilly basic_weaksmile_paj_close
        with charachange

        "With a bit of squirming I shuffle my way closer to her, tentatively putting one hand around her waist to hug her. I'm still not really used to this kind of physical affection, but Lilly seems to like it."

        scene ev lilly_kissing
        with whiteout

        "Lilly smiles as she turns to face me, a kiss being the reward for giving in to her. She draws me in, brushing my upper lip with hers before pressing against both."

        "This way, every one of my senses is filled with her. The barely perceptible scent of her hair, her taste as her tongue fleetingly touches mine, the tenderness of her lips, the image of her filling my mind, the total silence apart from her faint breath…"

        "We may have kissed before, but even if this is more a kiss of simple affection than anything, it's still a new and pleasant sensation."

        scene bg school_dormlilly at bgright
        show lilly basic_cheerfulblush_paj_close:
            center
            ypos 1.1
        with locationchange

        "Judging from her vivid blush as she pulls back, it's obvious she feels the same as I do; even if we're entirely alone, it still feels a little embarrassing to open up to each other this much. "

        show lilly basic_smileclosed_paj_close
        with charachange

        li "If we take everything day by day, I think that would be for the best. Small steps, right?"

        hi "Yeah. Just small steps."

        "We have plenty of time to be together, even after the school year is over. As long as we move together, I think everything will work out okay; neither of us is going anywhere soon, after all."

        "For now, I'm just thankful for this small moment in time we can spend together."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .correct_procedure:
        scene bg school_nursehall
        with locationchange

        "I stand unmoving in front of the door to the nurse's office for what feels like at least a dozen minutes or so."

        "It's not like I never entered the small, beige room before, nor is it because of any feeling of childlike anxiety over the visit."

        "Maybe it's because the nurse's office is akin to a confessional, an admission that my body is flawed. The knowledge that such a fact is kept entirely confidential between the nurse and me hardly lessens the feeling."

        "Remembering that the bell to signal the end of lunch break will sound soon, I give a sigh and open the door. The burden will stay with me just this while longer."

        play music music_nurse fadein 0.5

        scene bg school_nurseoffice
        show nurse neutral at center
        with locationchange

        nk "Well now, if it isn't Nakai. Good to see you."

        show nurse grin
        with charachange

        nk "Or bad, I guess, considering that I'm a nurse."

        "He gives a small laugh, amused at his little joke. I find his humor lacking and somewhat off, but the fact that he can make light of such a situation is perhaps comforting, or at least distracting."

        show nurse neutral
        with charachange

        "His brief episode of entertainment over, he claps his hands together and gets down to business. I take a seat as he gestures for me to do so."

        "I wish the classrooms had seats this comfortable. I can feel my mind wandering as my eyes quickly scan the room, distracted by all the small changes since I last came."

        show nurse fabulous
        with charachange

        nk "Alrighty, so what brings you here? I haven't seen you often, so I assume your health's been good so far?"

        hi "Well, mostly."

        show nurse neutral
        with charachange

        nk "I see."

        "His smile drops as I trail off. I feel slightly guilty about it. It's these moments where I can't rationally call myself 'normal' that make me so reluctant to see the nurse. They're an admission that I'm different from everyone else."

        stop music fadeout 5.0

        hi "While I was on a trip during the long weekend, I had a few problems with my heart."

        "He hums very seriously and nods as he does so, urging me to go on."

        hi "I think it was… yeah, it was as I was walking a fairly long distance. I think the right term for it is a heart flutter."

        hi "I suddenly went weak at the knees and felt almost like I was having a small heart attack, but it passed in about half a minute. Even afterward though, I felt pretty fatigued and nauseous."

        show nurse concern
        with charachange

        nk "Hrm. Not good. Not good at all."

        nk "That was how many days ago, exactly? Did you do anything unusual, aside from exerting yourself, before the episode? Were you taking your medication properly?"

        "The nurse switches from awkward jokester to serious health professional mode, rattling off questions, making notes, and calling up stuff on his computer."

        "I tell him about my forgetting to take my pills that morning, and the preceding evening. It was a stupid thing to do, but I can't change anything about it now, except answer honestly and bite the bullet."

        "His seriousness evolves into a frown, and the talk evolves into an instant checkup."

        hide nurse
        with shorttimeskip

        "I finish buttoning up my shirt and again get motioned to take a seat in front of the nurse."

        show nurse concern at center
        with charaenter

        nk "Is this the first heart problem you've had since coming to Yamaku?"

        hi "I've had short pains in my chest before, just a couple of times, but they were more discomfort than anything like this."

        "He leans back in his chair, briefly resembling a white-coated Poirot as he mulls over the mysterious case of the heart flutter."

        "Moving his lips from side to side to show he's thinking, his nonexistent mustache wiggling, he eventually comes to a conclusion."

        show nurse fabulous
        with charachange

        play music music_nurse fadein 1.0

        nk "Well, you survived it. That's always on the plus side."

        "I blink at this one, then notice the nurse wearing his 'got you' face."

        "It's actually somewhat reassuring. I don't think he would crack jokes if things were really serious, so I keep silent and take my lumps."

        show nurse neutral
        with charachange

        nk "I'll have a talk with your doctor, but right now I suspect it's simply due to physical exertion."

        nk "Have you been keeping up with regular light exercise like I directed you to?"

        hi "I make sure to walk a reasonable amount every day. It's usually enough to work up a bit of a sweat, but then again I'm not really as fit as I used to be."

        nk "That should be enough, then. The main thing to keep in mind is to do regular low-stress exercise, not short bursts of sprinting and such."

        hi "I understand. Since leaving the hospital I've been a lot more focused on my studies, partly to take my mind off not being able to do more physical things."

        show nurse grin
        with charachange

        nk "It's good to hear you're coping well. Sudden lifestyle changes can be hard at the best of times, so I'm pleased to hear that you sound like you have everything in order. Almost everything, that is."

        show nurse neutral
        with charachange

        nk "Nevertheless, I want to keep a close eye on you for a while, just for observation's sake. Just to make sure things aren't going downhill, you understand."

        "That's something I really didn't want to hear. Since coming to Yamaku, all I've wanted to do is live as normal a life as possible."

        "'Observation' was one of the words I came to hate most during my hospital stay. For so long I felt as if I could have just walked straight out the hospital doors, if not for that 'observation' the doctors wanted so dearly."

        hi "Sure. Should I come in more often?"

        "He checks the calendar next to his computer, which seems to inflict on him a nasty case of furrowed brow. He spins back towards me after that."

        show nurse concern
        with charachange

        nk "The summer holidays are a bit of a pain, considering the timing…"

        nk "I'll check with your doctor to try and get a better handle on the situation and see how he wants to proceed, but I think you should just take things slowly and carefully for now."

        nk "What you're describing doesn't immediately sound like a recurring event, but it won't hurt to slow down a bit for a while, just to make sure."

        hi "What should I do for today?"

        "He looks over my shoulder at a clock hanging over the door. I'd never have noticed it if I hadn't followed his gaze."

        show nurse fabulous
        with charachange

        nk "It's nearly time for school to be over, so you may as well just leave early."

        "He gives me a sly wink, making sure that I understand he's doing me a favor."

        hi "Well, nurse's orders. Thanks."

        show nurse grin
        with charachange

        nk "That's what I'm here for, after all."

        show nurse neutral
        with charachange

        nk "I know you might not want to hear this, but you can't ignore your condition. Don't hesitate to see me if you have any further problems, or if you just have anything you want to ask. Bye."

        hide nurse
        with charaexit

        "He spins around and gets back to typing on the computer in front of him. I suppose I'll just read before waiting for Lilly by the gate, considering I don't have much else to do."

        stop music fadeout 3.0

        "Even as I leave, his words echo in my mind. My condition isn't something as limiting as many of the others here in Yamaku, and I don't want to burden Lilly with thinking about it."

        "If I just live life normally and avoid any short, sharp shocks, I should be okay. I won't let my condition rule me."

        scene bg school_gate_ss
        show lilly cane_smileclosed_ss at center
        with shorttimeskip

        play music music_tranquil fadein 3.0

        play sound sfx_normalbell

        "Lilly comes into view soon after the bells heralding the end of the school day ring out. She says farewell to a number of her classmates headed in the other direction, before beginning her weekly trip to the convenience store."

        hi "Afternoon, Lilly."

        show lilly cane_smile_ss
        with charachange

        "The immediate warm smile and relaxed demeanor she assumes upon noticing my presence are unexpectedly welcome."

        li "Hello, Hisao. Good afternoon to you too."

        show lilly cane_smileclosed_close_ss
        with characlose

        "She hesitates for a second, but eventually deigns to tilt her face forward and close her eyes. My lips meet hers with a measure of slight trepidation before we move off, hand in hand."

        "The fact that we're so close in height is somewhat useful at times, there being no need for either of us to turn our head upwards nor downwards in order to meet the other's."

        scene bg school_road_ss
        with locationchange

        "It doesn't take much time to leave the noise of the other students far behind us, the tapping of Lilly's cane in her free hand the only sound to be heard."

        "Silence, blissful silence, is all that greets us while we slowly walk in the setting sun's light."

        hi "I think I'm coming to really like this town. The huge, green, hilly expanse, the trees everywhere, the somewhat rustic little buildings…"

        show lilly cane_smile_close_ss at center
        with charaenter

        li "So you've come to appreciate the tranquility of it as well?"

        hi "I think so. I came from a metropolitan city near Tokyo, so the quiet of this town really alienated me when I first arrived."

        hi "After a while it became really nice, though. I think I prefer it to the hustle and bustle of my home city now."

        show lilly cane_smileclosed_close_ss
        with charachange

        li "While I preferred the quiet of such a rural town even when I first arrived, I suppose I had the advantage of growing up in a quiet area before I came."

        show lilly cane_weaksmile_close_ss
        with charachange

        li "Hanako said the surroundings are very pretty, too."

        "Lilly may say such a thing quite easily, but each time she mentions how others describe sights around her as beautiful or pretty, I feel a little put off."

        "I notice her expression becoming one of anticipation for some question or another. She always had a good sense for when somebody's not saying something that's on their mind, so I may as well speak up."

        hi "I was kind of wondering… uh, how to put this…"

        hi "Do you ever… regret that you can't see what things look like for yourself? It's just something I've been thinking about."

        show lilly cane_listen_close_ss
        with charachange

        "She thinks carefully for a time."

        show lilly cane_smileclosed_close_ss
        with charachange

        li "Do you ever regret that you can't hear people whispering on the other side of a room?"

        show lilly cane_smile_close_ss
        with charachange

        li "I can only speak for myself, but the fact that I can't see is the only way I've experienced life. Just as I cannot do something you can, you can't do something that I'm capable of."

        show lilly cane_weaksmile_close_ss
        with charachange

        li "The fact that the world is made for those who are sighted can be a pain sometimes, but there are many, many people who suffer much more than I because of the way the world is."

        hi "That does make sense, but still, it just feels kind of bad to describe something that you can't experience to you."

        show lilly cane_surprised_close_ss
        with charachange

        "She tilts her head quizzically, as if I'd just said something that makes very little sense at all."

        li "But I can experience it."

        show lilly cane_smile_close_ss
        with charachange

        li "You just said yourself that you like this area because of the way the surroundings are. I like this area for the very same reason."

        show lilly cane_smileclosed_close_ss
        with charachange

        li "Thanks to the fact that this is a small rustic town surrounded by trees, it gives some peace and quiet away from the din at school and the bustle, not to mention the smells, of the city."

        "I suppose it would also be much like the home she shared with Akira, as well."

        "Her outlook on it seems pretty sensible, and I'm not surprised that she's got a much better handle on her particular condition than I do on mine."

        "Just like how her coming from a location somewhat similar to Yamaku's surroundings let her become more acclimatized in a shorter time, being born blind affected her stance, by her own admission."

        "I should stop being so annoyed with myself over it, but I can't shake the feeling that I've depended on Lilly far too much, given the circumstances most have had to deal with in Yamaku."

        hi "That makes a lot of sense. You're pretty good at explaining, as always."

        hi "Come to think of it, where is Hanako anyway? She was with us for lunch."

        show lilly cane_weaksmile_close_ss
        with charachange

        li "It seems she's busy studying. The exams are far from over, and she said she wants to do better this year than the last."

        hi "While I admire her work ethic, she's really been trying to give us a lot of room alone recently."

        show lilly cane_reminisce_close_ss
        with charachange

        li "She's that type of person, I think; the kind that puts others' needs above her own at every chance. She's a sweet girl, even though so much has hurt her in the past."

        show lilly cane_weaksmile_close_ss
        with charachange

        li "I don't know… I feel like it's only now, when she's less close to me than ever, that she's truly finding herself."

        show lilly cane_smile_close_ss
        with charachange

        li "It was thanks to you that she began to become more confident, after all, not me."

        "I take my hand from hers and gently place it on her head."

        hi "The important thing is that you were there for her. I can't even imagine what she'd be like without having found someone like you. That much became obvious while you were in Scotland."

        hi "We're all still friends, so we've just got to have faith in her. I think she'll become a good person, and that much is thanks to you being there for her when she most needed it, just as you were there for me."

        show lilly cane_weaksmile_close_ss
        with charachange

        li "It makes me feel a bit childish when you sound so wise."

        hi "Well, I try."

        hi "Are you doing anything on the weekend, by any chance?"

        show lilly cane_surprised_close_ss
        with charachange

        li "Nothing that comes to mind. Why?"

        hi "Then how about a date on Sunday? It'd be something to do besides exam preparation."

        show lilly cane_smileclosed_close_ss
        with charachange

        "Countering my rapidly beating heart, she simply smiles and nods."

        li "That would be lovely."

        hi "Where would you like to go?"

        show lilly cane_displeased_close_ss
        with charachange

        "Her face suddenly changes to one of disapproval."

        li "You can't do that, Hisao. That's cheating."

        hi "Do what?"

        li "A gentleman should never ask a lady where to have a date."

        hi "Ah… oh."

        show lilly cane_smile_close_ss
        with charachange

        "Her smile quickly comes back, assuring me that she's far from serious."

        show lilly cane_smileclosed_close_ss
        with charachange

        li "Don't worry about it. I'll think about where we could go."

        hi "I'll leave it to you, then. I promise to decide on the next date, though."

        stop music fadeout 4.0

        "With our plans for the weekend made, the rest of the walk down the hill continues in silence."

        "The prospect of that lasting for any length of time, however, is shattered as I catch sight of a familiar figure waiting for us, her hand held high."

        show lilly at twoleft
        show bg at bgleft
        with charamove

        show akira basic_smile_ss at tworight
        with charaenter

        aki "Yo."

        scene bg suburb_konbiniint
        with shorttimeskip

        play music music_daily fadein 0.5

        "Storewoman" "Thank you, please come again!"

        scene bg suburb_konbiniext_ss
        with locationchange

        "The change in temperature as I step outside from the convenience store sends a chill up my spine. It feels like summer's starting to wind down."

        show lilly cane_weaksmile_ss at center
        with charaenter

        "Looking to my side, the same feeling seems to affect Lilly as well, though unlike me she doesn't manage to hide the fact. Something I didn't realize at first was how physically delicate she is, even compared to the likes of Hanako."

        "If I had to describe her, I'd have to say that she reminds me of a china doll."

        show akira basic_ending_ss behind lilly at center
        with charaenter

        show lilly cane_surprised_ss
        with vpunch

        show lilly cane_reminisce_ss at twoleft
        show akira at tworight
        show bg at bgleft
        with charamovechangefaster

        "Akira walks up behind her and gives a couple of hard pats on her shoulder, much to Lilly's consternation. For a moment she looks as envious of my status as an only child as I am of their close relationship."

        show lilly cane_listen_ss
        show akira basic_boo_ss
        with charachange

        "They talk between themselves for a few moments as I sort out my bags, their voices too low for me to catch, but eventually they break off and we begin the walk back to school."

        scene bg school_road_ss
        show akira basic_smile_ss at tworight
        with locationskip

        aki "Ah, it feels good to be out of that damned office. You kids don't know how good you have it here."

        show lilly cane_displeased_ss at twoleft
        with charaenter

        li "Kids…"

        show akira basic_laugh_ss
        with charachange

        aki "Tsch. 'You two,' then. Kids grow up so fast, nowadays."

        show lilly cane_pout_ss
        with charachange

        li "You're not old enough to say that."

        show akira basic_lost_ss
        with charachange

        aki "I don't know. Being around Hideaki makes me feel damned old; he's so precocious he reminds me of you when you were younger."

        show lilly cane_weaksmile_ss
        with charachange

        li "He's a nice boy. It would be a shame if Shizune comes to have too much of an influence on him."

        show akira basic_laugh_ss
        with charachange

        "Akira gives an amused snort at her sister's antipathy. She really doesn't seem to regard it as anything to make a serious fuss about, treating it more like a childhood spat."

        show akira basic_smile_ss
        with charachange

        "She looks over to me, apparently only just remembering that I'm here, and gives a small grin as she reaches towards her back pocket."

        hi "What is it?"

        show akira basic_ending_ss
        with charachange

        aki "Just a sec, let me dig it out…"

        "After quite some difficulty, she manages to retrieve her black leather wallet from her back pocket, quickly fishing out what looks to be a folded square of paper."

        "With Lilly all but unaware of what's happening, Akira unfolds the scrap and hands it to me."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        show stallphoto_insert:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0

        pause 1.0

        "An old photo of… what looks to be a younger Lilly and Shizune operating a noodle stall, with some other girl in the background. She looks vaguely familiar, but I can't quite pinpoint why."

        show lilly cane_smile_ss

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        show stallphoto_insert:
            easeout 1.0 ypos 0.7 alpha 0.0

        pause 1.0

        hide stallphoto_insert

        li "What is it, Akira?"

        show akira basic_boo_ss
        with charachange

        aki "I think you know."

        show lilly cane_listen_ss
        with charachange

        "Lilly mulls this over for a few moments before realization dawns on her."

        show lilly cane_surprised_ss
        with charachange

        li "Akira… you really needn't…"

        show akira basic_smile_ss
        with charachange

        aki "It's fine, isn't it? Besides, it's like the only photo I have of you two since you entered Yamaku where you're not at each other's throats."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        show stallphoto_insert:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0

        pause 1.0

        "I look back down to the photo in my hand."

        "It does seem strange to see Lilly and Shizune working together so dilligently without any sign of animosity. If the photo's of them during Yamaku's festival, that means it must have been taken one or two years ago."

        "In other words, the time when they were both in the Student Council together."

        hi "Who's the girl in the back? She looks kind of familiar."

        aki "Hah, I knew you wouldn't recognize her. It's Misha before she went and dyed her hair pink."

        hi "That's Misha? No way…"

        "It feels extremely strange to see Misha without her so very distinctive hairstyle. Judging from Akira's tone, she doesn't take favorably to Misha's idea of fashion."

        "I suppose that fact just accentuates how odd the situation looks. To think they were so friendly in the past… I wish I could do something to mend their relationship."

        li "You're being very quiet, Hisao."

        hi "It just feels kinda strange to see you all so friendly like this."

        "Lilly moves to say something, but stops herself. In the end, this isn't a matter for me; it's between Shizune and Lilly, and nobody else."

        li "Things change. Unfortunately."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        stop music fadeout 6.0

        show akira basic_resigned_ss
        show lilly cane_reminisce_ss

        show stallphoto_insert:
            easeout 1.0 ypos 0.7 alpha 0.0

        pause 1.0

        hide stallphoto_insert

        "I hand the photo back to Akira, who sighs as she folds it up and slides it back into her wallet. A little memory, quietly hidden away, to be pulled out again some time later."

        aki "Yeah, that they do."

        "Initially I think Akira's reaction to be simply in response to the situation between Lilly and Shizune, but she looks oddly glum compared to what I'd expect. Lilly's expression has clouded as well."

        hi "What's wrong?"

        show akira basic_boo_ss
        with charachange

        aki "Ah, it's just that I'll be going to Scotland fairly soon."

        hi "You're leaving for Scotland again?"

        show akira basic_lost_ss
        with charachange

        "For a long moment, Akira looks surprised. It's an ill-fitting expression for her."

        "After a glance at Lilly, she turns back to me as if she'd never done so."

        show akira basic_resigned_ss
        with charachange

        aki "Yeah. In a couple of weeks I'll be leaving for Inverness to work at the company's headquarters. It's a pretty big jump in corporate position, and it's not a chance that's going to come again."

        "So Akira's going to leave Japan, on what seems to be a permanent basis…"

        "I can't help feeling that my assumption that we could all happily while away our days, having fun in this isolated little world, is coming to an end. It's unsettling."

        "I look at Lilly, mildly surprised that she hasn't told me such a thing despite usually being so forthcoming."

        "She continues to walk with her face fixedly pointed ahead. I can't read her expression, nor can I even guess what's on her mind, which is discomforting given how it's usually easy for me to do both."

        "It reminds me of the time when we met at the Shanghai, just before what could be called our first date. At the time, all I could do was comfort her without knowing the cause, and now feels no different."

        scene bg school_dormext_full_ni
        show akira basic_resigned_ni at tworight
        show lilly cane_reminisce_ni at twoleft
        with shorttimeskip

        "As we finally reach the school dormitories once again, there's a somewhat awkward silence. I don't think I'm the only one who feels it."

        hi "See you tomorrow then, Lilly. Bye, Akira."

        show lilly cane_weaksmile_ni
        with charachange

        li "Good night, Hisao."

        show akira basic_smile_ni
        with charachange

        aki "Seeya."

        hide lilly
        hide akira
        with charaexit

        "And with that, they walk to the female dormitories."

        "Opening the door to the male dormitories, I stop and look back at them just moments before their figures disappear behind the heavy wooden door."

        "That was… a strange moment when Akira said she was leaving. While that wasn't the first time when my thoughts regarding my new life have been called into question, it's perhaps the first time to do it quite so profoundly."

        "I still don't know what to make of Akira's reaction, much less of Lilly's."

        "The night's chill reminds me to get back to my room before I catch something, my bags pulling down on my arms with seemingly redoubled weight."

        "If nothing else, I have a date with her set up for the weekend. I just need to stop overthinking stuff and get on with things as they are."

        "The exams are still ongoing, after all, and with the trimester's end and the summer holidays beginning soon, there'll be plenty to keep me busy for a while."

        "As I give a yawn and retreat inside, my thoughts turn to what Lilly will decide to set as the location of our weekend rendezvous."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .out_and_about:
        scene bg city_restaurant:
            xalign 0.0
            warp acdc_warp 10.0 xalign 1.0
        with dissolve

        play music music_jazz

        "I'm pretty sure this is about the last thing I had in mind when Lilly said she'd decide where to have our date."

        "No man nor woman is dressed in anything but their finest, their formality only matched by that of their surroundings; rich red wallpaper adorns the walls as the city lights far below flicker and glow."

        "Combined with the ambient hum of quiet speech and the high-pitched clattering of cutlery and wineglasses, the mood is very formal, yet relaxed enough for me not to feel too uptight despite this being our first real date."

        "Once we get seated, our waiter leaves to attend to others with a quick bow, after an appreciative nod from Lilly."

        "Far from depending on my help, Lilly's managed to navigate herself around surprisingly easily so far, despite the unfamiliar environment. A light brush here and there, and she's generally quite deft at orienting herself as needed."

        scene ev lilly_restaurant_listen at restaurant_out
        with whiteout

        "My eyes look to Lilly's. I can tell from her face that she's listening to her surroundings just as hard as I'm looking."

        "Though truth be told, my eyes are lingering on her each time they sweep across the room. The red cheongsam she's wearing accentuates her figure very well and shows off her legs. Even her hair is done up, and the scent of perfume is just noticeable."

        "While my black suit may be a rental, I managed to select an appropriate one. It feels surprisingly comfortable considering I've so rarely worn one, and fits the setting just as well as Lilly's attire."

        hi "I guess this is a new experience for both of us, then?"

        show ev lilly_restaurant_sheepish at restaurant_out
        with charachangeev

        "She turns somewhat sheepish."

        li "I've never come to a place such as this before, no."

        hi "One hell of a first date, that's for sure. It's going to be pretty hard for me to top this."

        "A small giggle. Even now, our nervousness is dissipating."

        "Her hand skates along the center of the table until it touches the menu, which she takes in both hands and brings to her face."

        li "Um, Hisao?"

        "As she lowers the beige, laminated sheet just below her eyes, I can see another sheepish look."

        "I doubt asking the waiter for a menu in Braille would be productive."

        hi "I can read it out for you, no problem."

        scene bg city_restaurant at right
        with locationchange

        "I take mine and give it a quick read, my small grin faltering."

        hi "Er, perhaps there is."

        show lilly basic_weaksmile_che_close:
            center
            ypos 1.1
        with charaenter

        li "What's wrong?"

        hi "There are quite a few items on here… and I'm not completely sure how to pronounce a couple of them."

        "One fine cuisine after another is listed. Most may be in Japanese, but a few are in English and French. I guess it's to be expected, but I have no idea what's in some of these."

        "Oh, this one I recognize. Wait, hang on…"

        hi "…You can cook that?"

        show lilly basic_giggle_che_close
        with charachange

        "A small giggle of amusement comes from behind the paper sheet."

        hi "Well, I could read them all out, but it'd take a few hours."

        show lilly basic_smile_che_close
        with charachange

        li "Is there anything with some kind of fish in it?"

        hi "Let's see…"

        "No. No. No. No. Aren't those poisonous? No. No. No. They eat that stuff? No. No. No. No… Ah, here we go."

        hi "A tuna salad seems to be a good bet. From the picture, it looks like it'd be pretty filling as well."

        show lilly basic_smileclosed_che_close
        with charachange

        li "That seems to be a reasonably safe option."

        hi "Let's order two, then. I'm pretty sure a couple of these dishes are from poisonous animals. I've had enough deadly run-ins for now."

        show lilly basic_weaksmile_che_close
        with charachange

        "Lilly maintains a smile, but there's a distinct lack of laughter. Black humor mustn't be her cup of tea, though to be honest I don't find it exceedingly funny either."

        li "There are certainly quite a few interesting smells wafting about. The same is true of the sights, I assume."

        hi "I've never been anywhere quite like this. A fancy Japanese teahouse on an occasion or two, but never anything this lavish nor European in styling."

        "Before another word can be said, a portly waiter in a distressingly tight vest appears at our table to take our orders."

        hi "Provençal Tuna Salade Niçoise, please. Two."

        "I hope I didn't mess up the pronunciation of that too badly. Even if I did, he doesn't show it."

        show lilly behind_cheerful_che_close
        with charachange

        li "And may I have a glass of Chardonnay, please. Hisao?"

        hi "Oh, uh, the same."

        "As the waiter nods and leaves, I suddenly realize what I said by absentmindedly mimicking Lilly's answer. I regret it pretty quickly."

        hi "Alcohol…"

        show lilly basic_pout_che_close
        with charachange

        li "Only a bit."

        "This girl has an odd propensity to getting hooked on things, I swear."

        hi "Surprising that they didn't ask for identification."

        hi "Then again, I guess we both do look mature for our age."

        show lilly basic_smileclosed_che_close
        with charachange

        li "I'll have to take your word for it. I'll add that this isn't what I'd call the type of place to ask such things, though."

        hi "Good point."

        "We both relax a little into our seats, trying to take our minds off the choking formality of the surroundings."

        "As soon as we do, the same waiter reappears at our table with two empty glasses and a bottle, the contents of which are quickly and professionally poured into the former."

        scene ev lilly_restaurant_wine:
            zoom 1.05 xalign 0.0 yalign 0.5
            easeout 8.0 zoom 1.0
        with flash

        "We both nod politely as he leaves, Lilly taking her glass and gently moving it from side to side. The liquid inside glistens as it moves around in the glass, and I have to admit it makes me a little less regretful for ordering the same."

        "I guess it must take effort to judge how the liquid inside is acting based only on its center of balance. Maybe it's like her origami; taking every little chance to practice her dexterity."

        hi "I guess I'm not surprised that you know about a place like this. Those who have money would, I suppose."

        "This reminds me of just how completely different our upbringings were. In Yamaku, it's easy to forget about social and economic disparity between students all wearing the same uniforms, living in the same dormitories."

        scene bg city_restaurant at right
        show lilly basic_smile_che_close:
            center
            ypos 1.1
        with flash

        li "Well, Akira was the one to tell me of it. She's come here before, apparently."

        "So that's what they were conspiring about on Friday."

        hi "And you chastise me for cheating?"

        show lilly basic_displeased_che_close
        with charachange

        li "That's not cheating. It's simply making use of personal contacts."

        hi "If you say so. Still, I get the feeling that you're more familiar with this kind of restaurant than I am."

        show lilly basic_reminisce_che_close
        with charachangealways

        show lilly basic_smileclosed_che_close
        with charachangealways

        "She pauses a moment, a wistful look on her face, before softly smiling. The compliment seems to brighten her mood."

        show lilly basic_planned_che_close
        with charachange

        li "You can thank my former school for that. If I were to appear any less, they'd be gravely disappointed."

        "She has mentioned her previous schooling before, but now I'm kind of curious. She seems to think a lot about her past, so I don't see any problem in asking."

        hi "What was that like?"

        show lilly basic_smile_che_close
        with charachange

        li "It was prestigious, all-girls and Catholic; these facts made my parents choose it for me. Many wealthy families sent their daughters there."

        hi "From how it sounds, life there must've been pretty strict."

        show lilly basic_weaksmile_che_close
        with charachange

        li "I wouldn't say it was a bad experience… but you're quite right; it was very strict. Thankfully, I managed to adapt well enough and make a number of friends."

        show lilly basic_reminisce_che_close
        with charachange

        li "Unfortunately, the same can't be said for my sister. She found the atmosphere and religious aspect suffocating, and ended up leaving for a job as soon as she was able to."

        show lilly basic_weaksmile_che_close
        with charachange

        "She gives a small, self-deprecating chuckle."

        li "I shouldn't complain about it though. Not many even have the chance to go to such a school."

        hi "Do you… resent your parents for sending you there, then leaving?"

        "She gently shakes her head."

        show lilly basic_reminisce_che_close
        with charachange

        li "My family is highly patriarchal. My father, business always on his mind, was entirely lost as to what to do with me."

        show lilly basic_weaksmile_che_close
        with charachange

        li "In the end, he made the decision that my education was of higher priority than staying with the family."

        li "He simply did what he thought was best."

        "To say such things so easily. What an unbelievable girl. That said, I'm a little surprised she doesn't think her blindness played any part at all… though maybe I'm being too harsh on her family."

        hi "You're too kind-hearted, you know that?"

        show lilly basic_surprised_che_close
        with charachange

        li "Hmm?"

        hi "Most would hate their parents for something like that."

        show lilly basic_weaksmile_che_close
        with charachange

        li "Well, some do…"

        "Oblivious to my raised eyebrow, she takes a sip from her glass. The wine slips down effortlessly, her fondness for it evidently helping her deal with the flavor of alcohol. I can't say the same goes for me."

        show lilly basic_smile_che_close
        with charachange

        li "What of yourself? What was your schooling like?"

        hi "Mine? Let's see…"

        hi "It was a fairly normal public school, I suppose, maybe a bit busier than the norm."

        hi "I did quite well in class and played in the soccer club. Since I am an only child and my parents both worked a lot, I wasted most of my free time and money at the arcade with my three friends."

        hi "No matter how much I played, though, I never did manage to beat Mai at any of those machines. Even Takumi and Shin lost to her whenever they tried. Then I'd be left trying to be the responsible adult when Shin and Mai fought. Again."

        hi "Just the four of us, aimlessly enjoying our childhood. Those were some pretty silly times."

        "I catch myself as I realize that I'm starting to zone out, the days of my old school disappearing to the night sky and bright city lights outside the window."

        "Lilly's face is an odd mixture of curiosity and sympathy. Given her strict schooling, I suppose something like this would seem an interesting contrast to the only life she's known."

        show lilly basic_satisfied_che_close
        with charachange

        li "It sounds like your previous school was a lot of fun."

        hi "I'm not really sure how much of it is nostalgia, but there are some nice memories."

        hi "That's in the past though. I can't go back there now, but through my accident I found a new life I'd never have imagined leading."

        hi "The peace and calm of Yamaku, a new direction for my future in science, the friendship of Shizune, Misha and Hanako, and most of all, you."

        scene ev lilly_touch_cheong
        with whiteout

        "She gives a deep, genuine smile as she moves her hands towards me, her fingers just lightly searching out my face before softly caressing my cheek."

        scene bg city_restaurant at right
        show lilly basic_smileclosed_che_close:
            center
            ypos 1.1
        with whiteout

        "Her hand reluctantly retreats after a second of warm silence, as we notice the waiter arriving with our meals."

        "Lilly does a deft job of covering her condition, except for the fact that her nod to him is slightly misaligned due to his silence."

        "She really seems to work hard at appearing as normal as possible in public. While I noticed it long ago, I still can't quite gauge whether it's a want to not be treated differently, a slight sense of vanity, or some mixture of both."

        scene ev lilly_restaurant_eat
        with shorttimeskip

        "The dish served lives up to the salad name, and the portion's pleasantly large. With sliced eggs and tomato, it looks very enticing indeed."

        "Lilly takes her knife in one hand and fork in the other, quickly getting to work on the dish as I do. It's later than when we usually have dinner, so we're both eager to dig in."

        scene ev lilly_restaurant_chew
        with locationchange

        "My cautious skewering of leaves and vaguely meat-like squares with my fork is matched by Lilly's silent and measured prodding and chewing."

        "An occasional tap around the sides of a piece of the food to work out its edges is the only giveaway to her lack of sight."

        scene bg city_restaurant at right
        with locationchange

        "I'm done with my meal in little time, Lilly taking the last few bites as I sit observing her."

        show lilly basic_smile_che_close:
            center
            ypos 1.1
        with charaenter

        li "Finished, Hisao?"

        hi "Yeah. It was pretty nice."

        "That much is very true. I never thought a simple salad could be so tasty and filling, but then again, I suppose that's why it costs so much to eat here."

        show lilly basic_smileclosed_che_close
        with charachange

        "Content with my appraisal, and evidently agreeing, Lilly gives a small nod."

        hi "You know, given that you're part foreign, exotic-looking and quite pretty, I'm surprised that nobody's ever confessed to you before."

        show lilly basic_planned_che_close
        with charachange

        li "You're assuming nobody did."

        "The simple statement takes me off guard. I shouldn't be surprised, given that I was complimenting her just moments before."

        hi "Really?"

        show lilly basic_smile_che_close
        with charachange

        li "I've received several confessions, both in this school and my previous one."

        show lilly basic_weaksmile_che_close
        with charachange

        li "Adolescence is a funny time."

        "She's kinda talking as if she's above it herself…"

        hi "Huh. How easily you say such a thing."

        show lilly basic_surprised_che_close
        with charachangealways

        show lilly basic_cheerful_che_close
        with charachangealways

        "Lilly looks surprised for a moment, before a playful smirk covers her face."

        li "Is that… jealousy?"

        hi "What? No. It isn't."

        show lilly basic_giggle_che_close
        with charachange

        li "You're a bad liar, Hisao. You should take that into account."

        show lilly basic_smileclosed_che_close
        with charachange

        li "Then again, I do appreciate how sincere you are. Even if you don't intend to be, sometimes."

        li "I think your honesty will always serve you well when dealing with others."

        "I clear my throat in mock disapproval of this whole business and try to steer the conversation elsewhere."

        hi "To tell the truth, though, I do prefer solitude to being surrounded by others. I don't think I could maintain a social circle like you do."

        show lilly basic_listen_che_close
        with charachange

        "She contemplates this for a moment."

        show lilly basic_smile_che_close
        with charachange

        li "I don't think that's true either."

        show lilly basic_smileclosed_che_close
        with charachange

        li "I've seen how gentle and caring you are around Hanako, and you get on marvelously well with others, even those whom you hardly know. I think you're quite adept at social situations."

        show lilly basic_cheerful_che_close
        with charachange

        li "But on that note, what of your confessions, Hisao? I'm sure someone like you must have had at least one admirer."

        "As I open my mouth to speak, I can feel my face turn slightly dour. At times like this, I secretly appreciate the fact that she can't see my expressions."

        hi "Just… one. Her name was Iwanako."

        hi "It was when she confessed to me that I had my heart attack. There in the woods, during winter."

        show lilly basic_oops_che_close
        with charachange

        "Lilly finds herself speechless, not expecting for the topic to move into such an area."

        "My condition has always been something of a concern for her, something that I strive to minimize despite my body's best efforts to the contrary."

        hi "Afterwards, she visited me for a while when I was in the hospital. For weeks she came in and talked. It was usually just smalltalk or classroom gossip, but that was enough."

        hi "But eventually… she just stopped coming."

        hi "She was there every day. Then every other day. Then once a week. Then finally, one day, she just stopped visiting entirely."

        show lilly basic_sleepy_che_close
        with charachange

        li "Did you ever… see her again?"

        menu:
            with menueffect
            "Wrapped in my own little world, I shake my head before remembering the futility of the gesture."

            "Mention the letter." if True:
                $ mention_the_letter = True

                call a4lc1o1
            "Drop the subject." if True:
                $ mention_the_letter = False

                call a4lc1o2

        "Seconds pass in silence before Lilly speaks again."

        show lilly basic_sad_che_close
        with charachange

        li "Moving to Yamaku must have been hard for you, having your friends and even your girlfriend taken from you for no fault of your own."

        hi "The worst of it passed while I was in the hospital. When all that surrounds you is four white walls and a small television, your mind takes on a life of its own."

        hi "It's like my old school, I guess. I just try not to dwell on what's happened and keep thinking ahead."

        hi "All that reminiscing does is get me down, and it's largely thanks to you that it feels like things are finally getting back on track."

        show lilly basic_veryemb_che_close
        with charachange

        li "That's… pleasing to hear, Hisao."

        "She lowers her face slightly, her expression pensive. I guess I went too far and embarrassed her."

        hi "I suppose you went through something a bit like what I did when you entered Yamaku anyway, right? I imagine the vast majority of our school's students did, after all."

        hi "You said yourself that you made friends in your old school. I can't imagine many followed you."

        show lilly basic_displeased_che_close
        with charachange

        "Lilly's deep smile drops, her expression unexpectedly darkening. Even her hands retreat to her lap."

        "After a long while, she speaks."

        show lilly basic_reminisce_che_close
        with charachange

        li "Hisao… can you promise not to tell anyone else what I'm about to—"

        hi "I promise."

        "She looks slightly taken aback by my serious tone, but then relents and smiles weakly before continuing."

        show lilly basic_weaksmile_che_close
        with charachange

        li "When I moved to Yamaku, I did regret losing the friends I'd had at my other school."

        show lilly basic_reminisce_che_close
        with charachange

        li "But there was one person whom I most regretted not seeing again. He was the reason I took up English as a future career."

        "'He?' Considering she came from an all-girls school, that can't have been a schoolmate then…"

        li "I rejected the confessions I'd received until then for him. Every time I improved my English skills, his praise was my most treasured reward."

        show lilly basic_weaksmile_che_close
        with charachange

        li "It's funny, isn't it? Someone like me, able to boast about the people who have set eyes on me, liking someone so utterly unattainable as my tutor."

        li "It truly is the most ridiculous thing…"

        hi "Did you…?"

        "She quickly shakes her head from side to side."

        show lilly basic_displeased_che_close
        with charachange

        li "I couldn't. Even then, I knew it was impossible."

        "A silence reigns over both of us."

        "This does seem to explain her ardent focus on her future in teaching English, but I can't help thinking of her confession to me."

        "She lost him without ever letting her feelings be known… did she somehow fear that would happen again, but with me?"

        "I don't really know what to make of it. I've heard of such relationships before; taboos born of such things as puberty and youth. The fact that she had the good judgment not to act on it, though, is heartening."

        show lilly basic_emb_che_close
        with charachange

        li "I know this must sound strange, but please… don't think of me…"

        hi "Why would I think any less of you for that?"

        hi "To be honest, I think he must have been a very nice person if you liked him so much. Not only that, but you stopped yourself before going too far."

        pause 1.0

        show lilly basic_arablush_che_close
        with charachange

        "For a moment, she looks somewhat lost. Most unexpectedly though, it isn't a second before she starts to laugh. The sound takes me off guard. It's not a giggle, nor a restrained chuckle, but honest and genuine laughter."

        "I find myself smiling, and not just at her display of relief and happiness, but for her to trust me enough to let me see this most private of secrets."

        scene ev lilly_touch_cheong
        with whiteout

        "Before I realize it, I feel her palm touching my face. Her touch is gentle as ever, with her thumb slowly stroking my cheek."

        li "You're kind, Hisao. I really do love you."

        "Seeing her face like this, with her palm gently caressing my face… I think tonight has been a wonderful night."

        hi "I guess we've both had pretty weird pasts, eh?"

        li "I think by most standards, our present is rather odd as well."

        "I smile and hang my head. This woman can easily run rings around me, of that I'm quite sure."

        scene bg city_restaurant at right
        with whiteout

        "I look back around the room with its continuing quiet hum of patrons."

        hi "This place probably fits into the 'odd' category, too."

        show lilly basic_weaksmile_che_close:
            center
            ypos 1.1
        with charaenter

        li "It is a tad… overbearing."

        hi "That's one word for it, yes."

        "I catch the eye of a scurrying waiter, a short, scrawny guy no older than twenty. He kind of reminds me of Kenji, though unlike him the waiter isn't dressed for winter during midsummer."

        show lilly basic_smileclosed_che_close
        with charachange

        "After a curt bow and an offer to remove our plates, Lilly asks for the bill politely and softly."

        "With expert coordination, he maneuvers around the tables, our plates in hand, to retrieve our bill."

        "In no time he reappears through the doors, smartly handing our bill to Lilly."

        show lilly basic_smile_che_close
        with charachange

        "…who promptly hands it to me, causing him to raise an eyebrow."

        "As I read the small computer-printed leaflet, the cost is considerably more than I expected."

        show lilly basic_surprised_che_close
        with charachange

        li "Hisao?"

        hi "Oh… uh…"

        show lilly basic_smileclosed_che_close
        with charachange

        "I quickly stammer out the amount, to which Lilly merely nods and reaches for her purse."

        "Giving her card to the waiter, he disappears once again."

        hi "That was… a disproportionately large amount of money."

        show lilly basic_emb_che_close
        with charachange

        "The statement seems to make Lilly slightly uncomfortable."

        show lilly basic_weaksmile_che_close
        with charachange

        li "My family leaves me more than enough for my education. The same goes for my sister, though she dislikes being reminded of that fact."

        show lilly behind_cheerful_che_close
        with charachange

        li "That said, I too dislike throwing money about. But this one time I think I can make an exception. Just for you."

        hi "Not only did you choose our date, but you paid for both of us as well…"

        "I take the bridge of my nose in my fingers."

        hi "I can't believe how high you have set the bar for our next date."

        show lilly basic_giggle_che_close
        with charachange

        "She gives a small giggle."

        show lilly basic_smileclosed_che_close
        with charachange

        li "I'll be looking forward to it, Hisao."

        "The waiter reappears beside us, as if by magic, and hands Lilly's card back to her. Evidently picking up on her lack of sight, he places the card in her hand with an extra, perhaps unneeded, amount of firmness to make sure of her grip."

        "Leaving, he exercises a measure of diplomacy by keeping a neutral face despite my own expression."

        "Clapping my hands together, I stand up from my seat in order to bring an end to our night out."

        hi "Shall we be off then, m'lady?"

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .a_mornings_reverse:
        scene black
        with Dissolve(2.0)

        scene bg school_dormhisao_ni
        with vpunch

        hi "Gyah!"

        "I snap upwards out of my sheets and sit bolt upright in bed, as if an electric shock had just run through my entire body."

        "The night air feels cold against the sweat on my bare skin, my breathing short and rugged nearly to the point of hyperventilation."

        "Mind racing, I bring my hand to my head in an attempt to soothe my body's panicked state. It takes me a number of seconds to realize my hand is shaking violently, even as I press it against my face."

        "More seconds pass in complete silence, my desperate attempts to subdue my body and mind slowly, thankfully, working."

        "Gathering myself, I start taking measure of the state I'm in. It feels like I've run a marathon, every muscle feeling tensed and sweat practically pouring off me."

        "I carefully direct my attention to the beating in my chest, measuring out the rhythm in my head. Sure enough, my unreliable heart is functioning properly, for once."

        "Just… what the hell was that?"

        "A heart attack? A bad nightmare? Medicine side-effects? I've heard about panic attacks, and this does seem to have the hallmarks of one…"

        "I can't even be bothered thinking about it right now. I feel utterly exhausted yet completely awake, after this experience."

        "I look over to the other side of my bed, the pale white of the silent figure's face almost glowing in the nighttime darkness of the room. Just the sight of her is enough to calm me down significantly."

        scene ev lilly_sleeping_smile:
            truecenter
            acdc_warp 20.0 zoom 1.05
        with locationchange

        "Her graceful demeanor persists even while she's asleep, her perfectly measured breathing and gentle face making it impossible to tell whether she's awake or truly sleeping."

        "Giving in to temptation, I delicately run my fingertips over her hand. Her skin is soft to the touch, as it always has been, yet warm even in the cold night."

        "It's at times like this, silently appreciating each other's presence, that I feel we're closest."

        "My fingers stop at her wrist and I bring my hand back down to the bed beside me."

        "I'm not entirely sure why, but as we became ever closer to each other, it felt as if something grew between us. I'm not entirely sure what it is, nor whether it existed before we'd fallen in love."

        "Everything is moving so fast. I don't mind it at all, but it feels unlike Lilly to be pushing things this much."

        scene bg school_dormhallway
        with shorttimeskip

        play music music_dreamy fadein 2.0

        "Thankfully, there aren't any students milling around in the hallways at this hour of the morning, lest I be interrogated on why I'm carrying two plates of breakfast to my room while dressed in an obviously hastily-donned uniform."

        "That isn't to say things like this never happen, of course. A single security guard patrolling between two sets of bedrooms situated right next to each other is a very small force, compared to adolescent hormones."

        "Come to think of it, the fact that it's Monday morning probably helps. I'm not really sure why, but Mondays seem to bother me less than they do most others."

        "It takes a little creative use of my hands and elbow, but eventually I manage to work the door to my dormitory room open."

        scene bg school_dormhisao
        show lilly basic_sleepy_paj at center
        with locationchange

        "Stepping inside, I see Lilly just getting up from the bed and tiredly rubbing her eyes. She looks a mess, just like most other times I've seen her soon after she wakes. She really isn't a morning person."

        hi "Sorry, I didn't mean to wake you."

        show lilly basic_displeased_paj
        with charachange

        "She groggily shakes her head. The morning light illuminating her makes for a very pleasant sight."

        show lilly basic_weaksmile_paj
        with charachange

        li "It's okay, I needed to get up anyway. What time is it?"

        "I put my plate down on my desk and turn the clock around to check the time."

        hi "Still early. Don't worry, there's plenty of time left before school."

        show lilly basic_smileclosed_paj:
            ypos 1.2
        with charamovechangefaster

        "She sits on the side of the bed and begins to sniff the air. As she does so, I quickly move her plate away and put it on the desk beside mine."

        hi "Yes, I got us some breakfast. Shower and clothes come first, though."

        scene ev lilly_kissing
        with flash

        "She stands still for a moment with her chin pointed slightly out. I gladly acquiesce and press my lips to hers, savoring the soft feeling before breaking off."

        scene bg school_dormhisao
        with locationchange

        "With a small, sweet smile, apparently quite satisfied, she slowly makes her way to the showers."

        "I stretch to try and wake myself up a little more, briefly looking at the steaming dishes on the desk. Rice, fish, miso soup and some vegetables; a standard breakfast for a somewhat unusual day."

        "I grab the bottles from my desk and start taking my daily regimen of pills."

        show pills:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0

        pause 1.0

        "Sometimes I wonder what these things are even good for, given all the troubles I've had since the initial accident. I can't even say that it doesn't hurt to take them, considering the side effects so far."

        "Well, whatever. Doctor's orders are that I have to take them, and rationality suggests that I'd be well served to trust his judgment over mine."

        show pills:
            easeout 1.0 ypos 0.7 alpha 0.0

        pause 1.0

        hide pills

        "It doesn't take long for the noise of the shower to cease, a quick one apparently being fine for Lilly given the circumstances."

        show lilly basic_smile_paj:
            center
            xpos 0.55
            easein 0.5 xpos 0.5
        with charaenter

        "Emerging from the bathroom, she looks significantly more awake, having had the chance to collect herself."

        show lilly basic_smile_paj_close at center
        with characlose

        show lilly basic_smileclosed_paj_close:
            ypos 1.1
        with charamovechangefaster

        "Without a word, I gently take her hand in mine and guide her to my desk. Considering I don't have a table in my room as she does, it'll have to do."

        li "Thank you, Hisao. What did you prepare for breakfast?"

        hi "Just rice and some vegetables. Something fast."

        show lilly basic_ara_paj_close
        with charachange

        "Her face lights up at the revelation."

        show lilly basic_satisfied_paj_close
        with charachange

        li "That's quite a breakfast. This is normal for you?"

        "Now she's just being nice. I have little doubt, considering her past, that this isn't exactly a high class meal by her standards."

        hi "Breakfast is the most important meal of the day. Just because we're students, doesn't mean we can take it lightly."

        "That's my belief, anyway. From what others I've talked to have said, I might be in the minority."

        show lilly basic_smileclosed_paj_close
        with charachange

        "I take a seat on the side of my bed and begin eating together with Lilly, her chopsticks lightly tapping out the outlines of the vegetables just as I'd noticed her do during our date."

        show lilly basic_smile_paj_close
        with charachange

        li "This is quite nice, Hisao. I had no idea you could cook this well."

        "This time she's much more genuine, I can tell that much. That said, cooking really isn't anything special at all; after a bit of practice it's pretty easy to make a simple dish."

        hi "Most of the credit goes to modern technology; still, after years of cooking for myself, I should hope so."

        hi "I got bored of eating instant noodles and ordering pizza every time my parents were both working, so I taught myself how to make a few meals. I'm still trying to get the knack of it, though."

        show lilly basic_cheerful_paj_close
        with charachange

        li "You'll make a good wife someday, Hisao."

        "I take a grain of rice and place it onto my thumb, before carefully taking aim and giving it a good flick."

        show lilly basic_surprised_paj_close
        with vpunch

        "Lilly jumps a little as it hits her cheek, right on target."

        show lilly basic_pout_paj_close
        with charachange

        "I can't help chuckling a little at her expense as she lowers her brow and tries her best to assume a harsh and serious expression."

        show lilly basic_sleepy_paj_close
        with charachange

        li "Oh, that's right…"

        hi "What is it?"

        show lilly basic_concerned_paj_close
        with charachange

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        li "Did you have any problem sleeping last night? You seemed restless."

        "So she was awake back then, or at least partly so. Whether it was my heart or a nightmare caused by the side effects of my medicine, the last thing I want is for her to be worrying about me even more."

        "Even before my relationship with Lilly, I'd felt my body was a drag on everything I did. My body is my burden alone, so as long as I'm with her, I'll continue to act as normally as possible."

        hi "No, not particularly."

        show lilly basic_reminisce_paj_close
        with charachange

        li "Is that so… that's good, then."

        $ renpy.music.set_volume(1.0, 4.0, channel="music")

        "Luckily, she seems to take me at my word."

        show lilly basic_weaksmile_paj_close
        with charachange

        li "Come to think of it, there was something else I wanted to ask."

        hi "Oh?"

        show lilly basic_smileclosed_paj_close
        with charachange

        li "How should I put it…"

        show lilly basic_smile_paj_close
        with charachange

        li "When you dream… do you see people and objects?"

        hi "Yes, of course I… oh."

        "I feel more than a little sheepish for that slip of the tongue, however earnest it may be. Lilly looks unperturbed, though."

        show lilly basic_smileclosed_paj_close
        with charachange

        li "But you don't taste, feel, nor smell things?"

        "I move to answer, but find myself stuck before thinking about it. The more I mull it over, the more I realize that her hypothesis is correct."

        hi "That's… true, I guess. I never looked at it that way. Are you saying that you do?"

        show lilly basic_smile_paj_close
        with charachange

        li "For the most part I only hear in dreams, but yes, sometimes I touch and smell things as well."

        show lilly basic_planned_paj_close
        with charachange

        li "I'm just asking since Akira thought it very strange that I did when I brought it up with her. If you don't either, then maybe it's due to my blindness."

        hi "That would make sense. You rely on your other senses more than me, so maybe that affects your dreams as well."

        "The wonders of the human body, I guess."

        "For the rest of the time before school, we quietly eat the hearty breakfast in front of us, exchanging a few small pieces of smalltalk as we do."

        stop music fadeout 2.0

        scene bg school_dormext_full
        with shorttimeskip

        "A quick peek out of the door assures nobody's looking directly at the entrance for the boys' dormitories, so we walk out with the path clear."

        play music music_soothing fadein 4.0

        hi "Ah, the weather's good today."

        "I stretch as Lilly and I make our way outside, the bright morning's sun beaming down on us."

        "By now a few students can be seen doing the same, making their way to the main school building either from the dorms or through the main gate."

        show lilly cane_smile_close at center
        with charaenter

        li "It does feel nice and warm."

        "Our hands linked and her cane tapping the ground, we begin in earnest our trip to the school building and join the chatting throngs of students around us."

        show lilly cane_smileclosed_close
        with charachange

        li "This would be the last day of exams, no?"

        hi "Yeah. How're you going in them?"

        show lilly cane_concerned_close
        with charachange

        li "Fairly well, all things considered. You seem a bit stressed by them, though."

        hi "It's that obvious, huh?"

        hi "I don't think it's just the exams, though. A lot of stuff's been happening in a short amount of time, and I'm not doing that well on the humanities subjects."

        show lilly cane_smileclosed_close
        with charachange

        li "You're doing well in science though, aren't you?"

        hi "Well, it would be hard not to do well in science for me. Come to think of it, didn't you say before that you weren't very good at science and maths?"

        show lilly cane_oops_close
        with charachange

        "She suddenly looks very sheepish, my remark no doubt hitting home. Lilly's sense of pride really can be a double-edged sword."

        show lilly cane_smile_close
        with charachange

        li "Well, aside from that… have you ever given thought to what you might do with that ability? It seems a pity to waste it."

        hi "A bit, mostly at Mutou's prompting."

        hi "In any case, I'll probably end up doing science as a career in some form."

        show lilly cane_smileclosed_close
        with charachange

        li "That's good to hear, Hisao."

        scene bg school_gardens at bgleft
        with locationchange

        stop music fadeout 0.3
        with vpunch

        "As we enter the gardens, I suddenly receive an unsolicited pat on the back."

        "The green-dressed culprit dances around to meet me, evidently not paying any heed to Lilly at my side."

        play music music_kenji fadein 0.5

        show kenji neutral:
            center
            xpos 0.55
            easein 0.5 center
        with charaenter

        show kenji at center

        ke "Hey man, what's up? Haven't seen you in a while."

        hi "Hey. Just been busy lately with the exams and stuff."

        show kenji tsun
        with charachange

        ke "Exams, ekshmams. A true Renaissance man needs no study to excel in such things."

        "Kenji does strike me as the kind of person that does well in school, even if he has a horrid attendance record and poor work ethic, so I've little reason to doubt his ability."

        "To be honest, I'm a little envious of him; between studying for exams and my time with Lilly, I've had practically no time to myself. Maybe this is a bit like how Yuuko feels."

        show kenji at tworight
        show bg at center
        with charamove

        show lilly cane_smile_close at twoleft
        with charaenter

        li "Good morning, Setou. It's good to hear you're doing well."

        "It feels slightly odd to see Lilly speaking so formally. She's come to address me more casually over the months, though I have seen her speak more formally to classmates from time to time as well."

        "Some people never change, I guess. Not that I'd say her calm and polite manner is a bad thing; it was one of the reasons I liked being around her to begin with, after all."

        "Kenji seems to take a moment to work out who it is beside me, and probably hasn't noticed us holding hands either. I wonder if those glasses of his actually do anything."

        show kenji neutral
        with charachange

        ke "Oh, hey Lilly. Good luck on your exams, too."

        show kenji tsun 
        with charachange

        ke "I'll see you after school then, man."

        "The slight edge to his voice makes me think those words are meant to be an imperative rather than a casual farewell. I guess I'll have to smooth things over later."

        hi "Sure. Seeya."

        show kenji:
            ease 1.0 xpos 0.6 alpha 0.0

        pause 1.0

        hide kenji

        "Kenji nods curtly. He moves to pass by us, but he's too busy glaring in Lilly's general direction to take notice of her cane."

        show lilly cane_surprised_close at twoleft
        with charachange

        "Before I can try to react and save the situation, Kenji trips and reflexively reaches out for a handhold. Unfortunately, said handhold turns out to be Lilly's arm."

        show lilly cane_surprised_close:
            easeout 0.3 ypos 1.2 alpha 0.0

        pause 0.5

        play sound sfx_pillow
        hide lilly
        with vpunch

        call screen doublespeak(ke, _("Whoa!"), li, _("Ah!"))

        "Both fall to the ground in a sprawling heap, with me left feeling rather helpless."

        hi "Ah, damn. Are you two okay?"

        show kenji neutral:
            center
            ypos 1.2 alpha 0.0
            ease 1.0 center alpha 1.0

        pause 1.0

        "Kenji quickly rises back up, seemingly unfazed by the accident."

        ke "No problem, man, no problem. This is nothing, my body can take much worse abuse."

        "Lilly lies facedown on the grass. She doesn't look hurt by the incident; more startled than anything. I move closer to offer her my help."

        hi "Are you all right, Lilly?"

        show kenji happy
        with charachange

        ke "Hey, Satou?"

        "Kenji offers her a hand, tentatively touching hers to let her know what he's doing."

        "He says some odious things sometimes, but I do think he may be a genuinely good person at heart. I imagine he feels pretty bad about this."

        stop music fadeout 2.0

        "To his surprise and mine, though, Lilly pounds on the ground with her fist without warning."

        play sound sfx_impact
        with vpunch

        li "Dammit!"

        show kenji tsun
        with charachange

        "Kenji freezes, entirely caught by surprise at her outburst. I'm just as shocked; she never acted like this before, not even around Shizune."

        ke "Uh…"

        show lilly cane_mad_close:
            twoleft
            ypos 1.2 alpha 0.0
            ease 1.0 twoleft alpha 1.0

        pause 1.0

        "Seemingly only now remembering that there are people around her, Lilly slowly climbs to her feet. Her face as she does so makes me retreat a little."

        show lilly back_listen_close
        show lillyprop back_cane_close at twoleft
        with charachange

        "I only catch a glimpse of her expression before she turns away, but it's not something I'll forget soon."

        "She showed plenty of annoyance during her clashes with Shizune, but this flash of anger was something else. There's no way that this is just about this petty incident."

        hide lilly
        hide lillyprop
        with charaexit

        "She pauses for a moment before sighing and walking on ahead. I really don't know what to make of this."

        hi "I'll, uh… talk to you later, dude. See you."

        ke "Yeah, seeya."

        hide kenji
        with charaexit

        "Kenji scratches the back of his head trying to find something to say, then shrugs and walks away, giving us a wide berth."

        show bg school_gardens at right
        with charamove

        show lilly back_listen at center
        show lillyprop back_cane at center
        with charaenter

        "I quickly catch up to Lilly. She turns her head a little to acknowledge my presence, but nothing else."

        "I should probably scold her for lashing out like that, but I also don't want to get into a shouting match with her. She's still very obviously annoyed."

        "In the end, I keep my mouth shut and wait for her to cool off."

        scene bg school_hallway3
        with shorttimeskip

        "After a quiet walk in, we eventually reach the top of the third floor stairs and the junction where we part every day."

        show lilly cane_listen_close at center
        with charaenter

        "I turn to Lilly before she leaves. While I do like the comfortable and warm silences we usually share, this was anything but. I don't want to leave things like this."

        hi "You seem… quieter than usual recently. Is anything wrong?"

        show lilly cane_displeased_close
        with charachange

        "She shakes her head almost automatically, as if to dispel any notion that I need to worry about her."

        li "It's just the exams taking their toll. I'll be fine."

        "I don't think that's the reason. I very nearly say so, but decide against it. There's no point trying to draw it out of her if she doesn't want to tell me, especially when she's in a foul mood like this."

        hi "If you're sure. I'll see you later, then."

        hide lilly
        with charaexit

        "As I turn down the hall to go to my classroom, Lilly's soft voice rings out from behind me."

        show lilly cane_concerned at center
        with charaenter

        li "Hisao, um…"

        hi "Yeah?"

        li "…"

        li "I'm sorry."

        hide lilly
        with charaexit

        "With that, Lilly makes off down the hallway to her own classroom, her hand skating along the metal railings."

        "I stand still and watch her until she turns into her classroom and out of sight, before going to my own class with a fair measure of reluctance."

        scene bg school_scienceroom at left
        with locationchange

        play music music_normal fadein 4.0

        "As usual, I'm early. Mutou is fiddling with folders and papers on his desk as he prepares for the day while a handful of students mill about, chatting away."

        "While my feelings about Lilly haven't dissipated, far from it, her mention of my exam performance did remind me that I have my own life's journey to attend to."

        "After thinking about it, I have realized that I do genuinely want to pursue science in some form as a career, rather than it simply being the path of least resistance."

        "Until now though, I didn't have much of an idea of where in the field I wanted to go. Just 'science' is a pretty broad category of jobs."

        "Something Lilly mentioned earlier focused my thoughts. Something I'd only idly pondered about before, I'd not seriously considered following this specific path."

        show bg at right
        with charamove

        "I walk up to Mutou's desk, his attention too focused on preparing for the day's lessons to notice my approach. It's the same every day."

        hi "Good morning."

        show muto normal at center
        with charaenter

        "He looks up with an expression of mild surprise that's quickly replaced by his typical awkward smile."

        show muto smile
        with charachange

        mu "Good morning, Nakai. Can I help you?"

        hi "Do you mind if I ask you something?"

        "He looks down at his messy pile of books on the desk, before putting down the papers in his hand and standing up with some difficulty to properly address me."

        mu "That's what I'm here for, after all. Ask away."

        hi "I was just wondering… what would you say is the motivation behind teaching?"

        "He thinks on this question for a few moments before responding, evidently far from having a prepared answer."

        show muto normal
        with charachange

        mu "If you talk to ten different teachers, I think you'll get ten different answers to that question."

        mu "While I can only speak for myself, I'd say that I teach because… hmm…"

        "He sinks into thought again, carefully assessing the way he wishes to present his idea."

        show muto smile
        with charachange

        mu "Think of it this way; when you were a child, you probably played with sticks and pebbles in moving water such as the gutter or puddles, right?"

        hi "Yeah. I think a lot of people do that when they're young."

        show muto normal
        with charachange

        mu "Well, it's not just when they're young for some, though it does take on another form. My point is, though, that when one is doing that, they're curious about how the water will flow or be changed."

        mu "Everyone, even at that young age, possesses an intense wonderment about how the world around them works, even in its smallest forms."

        mu "I still feel that sense of wonderment about the universe. Even just reading about new discoveries or classic experiments gives me a renewed sense of awe at how marvelous everything is, from the farthest stars to the smallest puddle."

        show muto smile
        with charachange

        mu "I just hope that I can give others even a small piece of that wonderment I feel. If I can do that, even if it's just for one person, I think that I can be happy as a teacher."

        "He scratches his head as he mentally reviews what he's said."

        "I feel like I understand him better now. Even if he's awkward around others, he does have a genuine want to be around them and offer them a piece of his self that he values."

        "What Lilly told me yesterday rings in my ears. 'I think you get on well with others,' huh. She always did say I was unusually curious…"

        show muto normal
        with charachange

        mu "Sorry if that was a little meandering. Does it answer your question?"

        hi "It does, thank you."

        hi "I also had another question, actually."

        mu "Oh? What might that be?"

        hi "Um… do you have any college brochures or guides? It's about time I started getting some applications in."

        "He nods and bends down to look inside his desk. As he does so, I notice that he is wearing a remarkably genuine smile. I don't think I've ever really seen him act this natural around others."

        "Perhaps this isn't Mutou, the teacher, but rather Mutou, the person."

        show muto smile
        with charachange

        mu "Here. If you need any more, feel free to ask."

        "He hands me about half a dozen brochures and booklets of various colors and sizes, which I take eagerly."

        "Yes, it will be this information which I'll use to forge my own future. I think now, after all this time and all these trials, I can finally start to see the big picture of my life ahead of me."

        "My body may be like this, but my mind is still very much able."

        hi "Thank you."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .blackout:
        scene black
        with dissolve

        nvl clear
        nvl show dissolve

        n "{vspace=60}'This is strange.'"

        play music music_pearly fadein 5.0

        show ev hisao_teacup:
            truecenter
            alpha 0.0
            linear 30.0 alpha 0.5

        n "{vspace=60}That single thought has graced my mind a countless number of times since my life here began."

        n "It feels like an easy way to discard a troubling question, as if simply labeling something with those three words will make it go away, or at least not worth thinking about any further."

        n "My life before my heart attack feels more blurry every time I try to remember it, and my mind struggles to keep up with all the events suddenly happening around me since."

        n "I heard somewhere that this is what it feels like to be left stranded in a country with only the most basic understanding of the local language."

        n "Indeed, when I think about it, that seems a marvelously apt analogy for what's happened to me."

        nvl clear

        n "{vspace=60}But such situations are also supposed to make you very capable in that language very fast, as you're forced to learn it in order to survive. Put another way, the situation becomes 'sink or swim.'"

        n "{vspace=30}I wonder if I've really managed to swim, after all this time."

        n "The exams are stressing me out a lot, even though they're finally coming to an end, but I have remained in Mutou's favor, and I have some sort of direction for my future now."

        n "But I keep using that stupid, meaningless phrase."

        n "{vspace=60}'This is strange.'"

        nvl clear

        n "{vspace=60}It really is amazing how fast one comes to accept being surrounded by people with sometimes incredibly jarring disabilities and conditions."

        n "So much so, that I really wonder why I feel so much like a foreigner."

        n "{vspace=30}It certainly isn't for lack of socialization or friends. I've come to know most of my classmates on first-name terms, and know a few others around the school. Whether they're missing an arm or a leg, the students here are just like anyone else of their age."

        n "{vspace=60}I can navigate the halls that I once lost myself in with an ease I'd not expected to ever have, thanks to the school's logical layout, and can engage my teachers in comfortable discussion."

        nvl clear
        nvl hide dissolve

        scene ev hisao_teacup:
            truecenter
            acdc_warp 20.0 zoom 0.8
        with locationchange

        "I swirl around gently the tea in my cup, the reflected image of my face becoming distorted by the moving liquid."

        "This is strange… I used to hate drinking tea."

        hi "Maybe I'm thinking too much."

        play sound sfx_teacup

        "The familiar sound of china rattling from a teacup touching an accompanying saucer rings out."

        li "Is something the matter?"

        hi "Don't worry, it's nothing."

        scene bg school_dormlilly
        show hanagown normal:
            tworight
            ypos 1.15
        show lilly basic_smileclosed_paj:
            twoleft
            ypos 1.2
        with whiteout

        "I take a long sip of the tea in front of me as the girls do."

        "Just whiling away the time in Lilly's room sipping tea with her and Hanako. It feels familiar, almost nostalgic."

        hi "So how's your work in the newspaper club going, Hanako?"

        show lilly basic_satisfied_paj
        with charachange

        li "I want to know too, it sounds like it would be quite interesting."

        show hanagown distant
        with charachange

        "Hanako's face turns down at the attention placed upon her, though her smile belies the fact that she genuinely likes being the center of interest for the two of us."

        ha "It's… good. I think I'm getting better at it."

        ha "Naomi and a couple of her friends handle most of the jobs… getting stories and stuff."

        show hanagown smile
        with charachange

        ha "I just do the computer things, like putting the stories together and getting it printed. I-it's nice, since I can sit and concentrate."

        "I see Lilly's low-tech nature isn't shared by Hanako. While sitting in a room compiling other people's newspaper articles into documents doesn't strike me as overly outgoing, it is heartening to see her widening her circle of friends."

        "Baby steps, I guess. It's probably a bit much to be expecting her to become a socialite like Lilly."

        show lilly basic_oops_paj
        with charachange

        li "How are you finding Naomi? I've heard she can be quite troublesome at times."

        "And Lilly's going into her mothering mode over Hanako. Letting go of her is something she's had to learn."

        show hanagown worry
        with charachange

        "Hanako scratches her cheek, thinking on her answer."

        show hanagown smile
        with charachange

        ha "Naomi's… nice. She's a bit loud sometimes, and a bit tiring… but she's really helpful. Her friends are nice, too."

        show lilly basic_cheerful_paj
        with charachange

        li "That's wonderful to hear, Hanako. I'm glad you've found a source of such enjoyment."

        "Lilly's smile is warm and genuine, but I can sense a touch of wistfulness to it as well. Hanako seems to miss that entirely, but I don't think for a second that I'm imagining it."

        "I suppose it's because I've slowly come to pay more and more attention to everything going on around me. With things seemingly happening faster and faster, it feels like I'll miss something if I'm not as observant as possible."

        "With the exams, my newfound love life, trying to fit in some studying regarding my options for college and university, and my heart condition applying the brakes on everything at irritatingly random times, my brain's been in overdrive recently."

        "It makes me appreciate the rare quiet times such as these."

        "I guess this is why Lilly came to appreciate her weekly walks to the convenience store and her tea parties with Hanako, despite her like of being surrounded by others; they gave her a moment of peace in a chaotic and busy life."

        hi "Thank god the exams are over, eh?"

        show lilly basic_giggle_paj
        with charachange

        "The comment draws an earnest chuckle from both of the girls. It seems like everybody's been a lot happier since the exams ended, last week."

        hi "So what're you doing for the summer holidays, Hanako? Only…"

        "I quickly count the days in my head. Today's Monday, and school finishes on Saturday…"

        hi "…five days to go, after all."

        show hanagown normal
        with charachange

        ha "I was thinking of… traveling. Just… around a bit."

        show hanagown smile
        with charachange

        ha "There's a lot of places I want to see, and… I think I have enough money to pay for the bus and train rides. Naomi and one of the other girls in the newspaper club said they might come along, too."

        "Her look indicates she's given the matter quite a lot of thought. I'm kind of surprised that she's contemplating something like this."

        "It seems she's really become intent on striking out on her own."

        show lilly basic_smile_paj
        with charachange

        li "Is there anywhere in particular you're thinking of going?"

        show hanagown distant_blush
        with charachange

        ha "I was thinking that… Kyoto sounds nice. I-I think I'll try to go to a few places… though."

        show lilly basic_cheerful_paj
        with charachange

        "Lilly nods in approval, happy with Hanako's plans."

        "While I cast my eyes to Lilly, I refrain from asking her the same question. She's been evasive with her plans for the future for a long time now, but I never seem to get a good time to broach the subject alone with her."

        "Every time it comes up in conversation, it feels like she's either unsure of herself or simply dodging the question. It's troubling."

        hi "Be sure to call sometime while you're out and about. I gave you my number before, right?"

        show hanagown smile
        with charachange

        "Hanako gives a quick nod, a happy smile on her face."

        "It's strange to see how happy people seem to become when they have a goal to work towards. Yuuko seems to brighten whenever her university aspirations are brought up, and now Hanako is just the same."

        "So why do I still feel this uncertainty? And why Lilly, too?"

        "Relationships really can be irritatingly troublesome, sometimes."

        show hanagown worry
        with charachange

        ha "Oh, um… wh-what time is it?"

        hi "Hmm? Oh…"

        "It takes me a second to remember that Lilly's clock doesn't have any visual feedback. I really should know, given how many times I've been in her room."

        "Nevertheless, I take my watch from my bag and quickly check it, the reason for her asking becoming clear."

        hi "It's about twenty past ten. Nearly curfew."

        show hanagown normal at tworight
        with charamovechangefaster

        "Hanako rises to her feet, dusting herself off and neatening her gown after doing so."

        show hanagown smile
        with charachange

        ha "I'd… better be going, then. Good night Lilly, Hisao."

        stop music fadeout 5.0

        show lilly basic_smileclosed_paj
        with charachange

        li "Sleep well, Hanako."

        hi "Seeya tomorrow."

        hide hanagown
        with dissolve

        "With that, she walks to the door and quietly makes her exit."

        show lilly at twoleft
        show bg at bgright
        with charamove

        "…"

        "Silence."

        "This seems to be happening more and more between Lilly and me, recently. After a few seconds, I finally find something to talk about."

        play music music_another fadein 4.0

        hi "Oh yeah, I talked to Mutou on Friday, and finally checked out some guides on college and how to apply for it."

        show lilly basic_smile_paj
        with charachange

        li "That's good news. If you're going to be applying for colleges, I assume you have some idea in mind of what you might do in the future?"

        hi "I think I've settled on becoming a science teacher. It's going to take a while to get through university and everything to be qualified, but I think it'll be worth it."

        show lilly basic_satisfied_paj
        with charachange

        "Lilly's face brightens considerably at the news. I suppose, with her wish to become a teacher, she's delighted I'd take the same kind of path."

        li "So, you've decided on a career of teaching…"

        show lilly basic_smile_paj
        with charachange

        li "I think that path suits you most excellently, Hisao."

        "I smile and nod. This time, even if I know she can't see me doing so, I know she feels it."

        show lilly basic_planned_paj
        with charachange

        li "I imagine Mutou would have taken to the news well?"

        hi "That's one word for it."

        hi "Hey Lilly?"

        show lilly basic_smile_paj
        with charachange

        li "Yes?"

        hi "I know you want to be a teacher, but…"

        "For a second, I wonder whether I should really ask her the question on my mind, but that's quickly brushed aside by the fact that this is rather late to have second thoughts."

        show lilly basic_smileclosed_paj
        with charachange

        li "Surely you don't still think I'd be offended by something regarding my blindness."

        "Her accusing tone is betrayed by her grinning face, amused at my awkwardness in raising the topic. Some things never change."

        hi "Good point, I guess."

        hi "I was just thinking whether or not being blind would be a hindrance, what with your ambitions to become a teacher and all."

        show lilly basic_surprised_paj
        with charachange

        "She looks mildly surprised before giving the question some thought. I refuse to think she's never actually pondered this issue before."

        show lilly basic_emb_paj
        with charachange

        li "I wonder… Hisao, could you close your eyes for a moment?"

        hi "O… kay?"

        "Raising an eyebrow, I do as she requests."

        $ renpy.music.set_volume(0.5, 2.0, channel="music")

        scene black
        with shuteye

        "I have no idea what she has in mind, and my questions only increase as I peek out from one eye."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        scene bg school_dormlilly at bgright
        show lilly basic_smileclosed_paj_close at center
        with openeye

        "Taking the black ribbon she usually wears in her hair from the cabinet beside her bed, she advances towards me while running it through her fingers to remove any stray hairs remaining on the piece of cloth."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        scene black
        with softwipedown

        "I suddenly click on to her intentions as I feel the black strip make contact with my face, wrapping around my head and over my eyes."

        hi "Um… what exactly is this for?"

        li "It's a little test, Hisao. Since you seem to be wondering, I'll let you see things as I do for a time."

        "Huh, so that's what this is about."

        "To be honest, this actually sounds kind of fun. Childish and rather silly to anyone who would be watching, but a bit of silly fun never hurt anyone."

        "I stand up with a heave, my hands quickly moving out in front of me to warn me of any obstacles."

        hi "Okay, now what?"

        li "Now, touch me."

        hi "If you say so. Now then…"

        "I slowly make my way forwards, towards the sound of Lilly's voice."

        "My walking speed could barely even be called a shuffle, the entire experience feeling alien enough that I don't want to risk inadvertently tripping over anything, such as her table or her haphazard piles of books."

        play sound sfx_rustling

        "Something soft, yet solid, brushes against my left leg. Further inspection reveals it to be Lilly's bed."

        "I move onwards, finding myself thankful that Lilly's room is so neat and tidy. Even the piles of books she has are generally kept close to the wall, well out of harm's way."

        play sound sfx_pillow

        "The hard wall pressing against my outstretched hands makes me furrow my brow in frustration."

        hi "Hey Lilly, where are you?"

        li "What are you doing over there? I'm over here."

        "Lilly's voice comes from the other side of the room, far from where it was before, even to my untrained ears. If she's going out of her way to avoid me reaching her, then is this just a game to her?"

        "…Of course it is. Compared to a life where even the concept of sight is an abstract one, a few minutes in a blindfold are nothing."

        "I guess she's made her point; she's more than capable of navigating her room, and further, I've seen how independent she is even when compared to many of the others in Yamaku."

        "Well, even if this is just a game, I may as well play it wholeheartedly."

        "With a pace much quicker than before I move towards the source of her voice, deftly sidestepping the table in the center of her room thanks to remembering its position."

        hi "I've got you now!"

        "She gives an impish giggle, one just long enough to work out that she's passing just beside me."

        play sound sfx_impact2
        with vpunch

        "I quickly turn around to face the new directio— the table wasn't there before!"

        hi "Ow… ow… ow…"

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        scene bg school_dormlilly
        with softwipeup

        "I slowly sit up next to the table, raising my blindfold as I rub my aching head."

        play sound sfx_impact
        with vpunch

        "I give an irritated kick to the table that's sitting just in front of where I fell. Utterly pointless, but the thing deserved it."

        show lilly basic_oops_paj_close at center
        with charaenter

        li "Hisao?"

        "Lilly's still standing just to my side, obviously unsure of what's befallen me."

        hi "Sorry. I kinda fell over."

        show lilly basic_concerned_paj_close
        with charachange

        li "Are you hurt?"

        hi "My head hurts, but I think I'm okay. I think the table moved in order to trip me over."

        show lilly basic_giggle_paj_close:
            ypos 1.1
        with charamovechangefaster

        "She giggles as she walks over and takes a seat beside me, her hand resting on my own."

        show lilly basic_weaksmile_paj_close
        with charachange

        li "I suppose that's the end of that then?"

        hi "I think so."

        hi "But I also think I get the point. Though I do wish it hadn't involved such a headache."

        show lilly basic_surprised_paj_close
        with charachange

        "Lilly suddenly looks blank."

        li "Point?"

        "And I return an extraordinarily flat look."

        hi "That was just for fun?"

        show lilly basic_reminisce_paj_close
        with charachange

        li "I just thought it might ease you up a little about the subject. You always seem to tiptoe around it, after all."

        show lilly basic_smileclosed_paj_close
        with charachange

        li "In regard to teaching, sight isn't that important. There are plenty of classes taught by entirely blind teachers, and more than enough resources for me to learn the subject."

        show lilly basic_smile_paj_close
        with charachange

        li "It's as simple as that, really."

        "I slump my shoulders and give a snort of amusement."

        hi "Yeah, I understand. I guess we'll both just have to work hard to reach our goals, then."

        stop music fadeout 4.0

        show lilly basic_cheerful_paj_close
        with charachange

        li "Hmm…"

        hi "What is it?"

        "With a little hesitation, Lilly pushes forward her chin and closes her eyes in an unmistakable gesture."

        scene ev lilly_kissing
        with whiteout

        play music music_one fadein 1.0

        "I accept gladly, our lips touching. As they do, I suddenly feel her hand snaking up my chest from underneath my shirt. The feeling of her hand against my bare skin is enough to make my heart suddenly accelerate."

        "So she's in that kind of mood again?"

        "Well, I'm hardly one to complain. She does genuinely like this, and even with all my medications, my libido is thankfully still intact."

        "I lean into the kiss further, holding her hand tightly as I feel it tracing the contours of my chest."

        scene bg school_dormlilly
        show lilly basic_smileclosed_paj_close:
            center
            ypos 1.1
        with whiteout

        "Eventually we break off from one another, the room silent but for our breathing."

        show lilly basic_surprised_paj_close
        with charachange

        li "Hey, Hisao?"

        hi "Yeah?"

        show lilly basic_emb_paj_close
        with charachange

        li "I don't suppose… you could wear the blindfold again?"

        "Her tentative suggestion takes me by surprise."

        "I suppose she wants to introduce me to sex through her eyes as well. Or just wants to find out what I'll be like during the act while hampered by the blindfold."

        $ renpy.music.set_volume(0.5, 0.0, channel="music")

        scene black
        with softwipedown

        "With a measure of unease tempered by curiosity, I do as she says and lower the blindfold over my eyes. The world becomes dark once again."

        "I reflexively tense as I feel Lilly's hand gently brush the side of my face, entirely unable to anticipate her touch."

        "I really need to get more used to contact like this. Even after the weeks we've been going out, it isn't as natural for me as it is for her."

        "…Silence?"

        hi "Hey, Lilly…"

        li "Shh."

        "I obediently follow her instruction and quietly listen, trying to make out something, anything, that's happening around me."

        "Compared to before when I was chasing Lilly, the need to carefully navigate the room's obstacles now gone, I can take my time and concentrate much harder on listening."

        "It takes a while, but I can eventually pick out the soft sound of her breathing in the otherwise dead silent room."

        "In… out… in… out…"

        "Measuring it against my own breathing, I realize it's definitely deeper than normal, especially for her."

        "Another sound makes its way to my ears, one that I can't identify immediately. I don't think I've heard it before, but…"

        "My heart skips a beat as I realize the source, my hand almost reflexively reaching out towards it. Her face feels softer than usual under my touch, her head just barely turning in acknowledgment towards the fingers on her cheek."

        li "Hisao…"

        "I gulp and take a moment to try and calm down. I need all the concentration I can muster while I'm like this in order to fully take in my surroundings."

        "After a few deep breaths, I think I've managed to collect myself. With a touch so light that it wouldn't disturb a feather, I start to move my hand down her body."

        "…and I can feel myself losing focus again, thanks to those thin silken pajamas of hers resting so perfectly over the curves of her body."

        "If she's like this, then that means she has to be sitting against her bed and facing me. Now, to continue."

        "…All right, this must be her hip. If I just move slowly downwards…"

        "Lilly's breath catches as my hand comes over hers, tentatively following her fingers between her legs and losing them as they go underneath her underwear."

        "Just the slightest moisture touches my fingertips, but it's enough to easily work out what she's doing."

        "My mind suddenly fills with visions of what she must be like in front of me right now. I'd never even imagined her doing this before, and being unable to see her doing the act only enhances the mood."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        scene bg school_dormlilly
        with softwipeup

        "I work the blindfold upwards, brushing out of my eyes a couple of hairs that were stuck to the ribbon before."

        "For a period of time I can only guess at, my mind goes completely blank. All I can do is stare as my newly-freed eyes take in everything in front of them."

        scene evh lilly_masturbate:
            truecenter
            zoom 1.1
            acdc_warp 10.0 zoom 1.0
        with flash

        "Just as I'd worked out, Lilly sits in front of me."

        "With one hand on the ground to steady herself, and the other's fingers lightly brushing between her legs, hidden by her dark blue underwear, I think it's the most erotic sight I've ever seen."

        "Once again I reach out and brush her hair from her face, her chin tilting outwards as she fills her pleasure-wrapped body with another breath of air."

        hi "Lilly…"

        "Lilly looks oddly cute as she smiles at my calling of her name. It always seems like it's at the moments when she's least attentive that she lets her most interesting emotions slip out."

        "It's not long before she works her fingers over herself faster than before, her excitement evidently rising, the scent of her sweat in the air only echoing that fact."

        "I sit in front of her. It's hardly as if my own arousal's holding still; it's taking every fiber of my being to let her continue by herself instead of pushing myself on top of her."

        scene evh lilly_masturbate_come_face
        with flash

        "It's strange… I'd initially found her clouded blue eyes to be distracting, almost disturbing in their lack of focus. That bothers me far less than it used to, now."

        "My attention refocuses on her as she lets out a whimper, her breath coming much faster than before and her hips subtly rocking."

        scene evh lilly_masturbate_come
        with flash

        "No sooner do I realize how close to the edge Lilly's become, that her breath catches. Her eyes clasp shut as every muscle in her body seems to contract, and she unmistakably reaches her climax."

        "For only a scant few seconds she tightens, huddled in ecstasy before her body relaxes and a long, drained sigh comes from her lips."

        scene bg school_dormlilly
        with locationchange

        "I… just have no idea what to say. Silence reigns while I simply watch her, hair hanging over her face as she sits exhausted."

        show lilly basic_emb_paj_close:
            center
            ypos 1.1
        with charaenter

        li "Hisao…"

        "When she reaches out to brush my face, my urges take complete control of my body. Without so much as a second thought, I push myself over her frame."

        "It's an unusual feeling, being like this. I feel oddly powerful, holding myself above her blank face. As though, for the first time since the accident so long ago, I feel physically strong."

        hi "Lilly… I want you."

        show lilly basic_weaksmile_paj_close
        with charachange

        "To my surprise, she smiles weakly before reaching upwards to feel the side of my face. It's an almost cheeky expression, of the kind which she usually gives only after getting something out of me."

        hi "You… wanted me to do this?"

        show lilly basic_smileclosed_paj_close
        with charachange

        "She holds her smile and gives a silent nod. I guess it was an effective way to make me take the initiative for once."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        scene black
        with softwipedown

        "And, again to my surprise, she gives the ribbon still around my head a sharp tug downwards. Once again, I'm lost in complete blackness."

        li "I told you… to keep it on… didn't I?"

        "That teasing edge to Lilly's voice, punctuated by her breathing… she never seems to lose her ability to take control of a situation."

        "But this time… this one time…"

        li "Ah, Hisao!? What are you—?"

        "I slide my hands underneath her, soft silk and skin pressing into my hands as I gently raise her body, with a measure of difficulty."

        "While I wouldn't describe her as heavy… her height makes her more than a handful to try and lift."

        "It only takes a couple of carefully placed steps to feel the edge of her bed against my legs, my lowering of Lilly onto her sheets just as gentle as when I raised her."

        hi "Your bed will be more comfortable than the floor, right?"

        li "Always the gentleman, aren't you?"

        "I quickly run my hands down Lilly's long, shapely legs, their allure far from diminished without the luxury of sight, and pull off her pajama shorts and underwear from her ankle."

        "I have no idea where those just went…"

        "Well, I guess it doesn't matter. They'll be somewhere around."

        "With a minimum of fuss, I shuffle down my own pajama trousers and underwear, positioning myself between her legs. Or at least, where I think is between her legs."

        "With one hand on her bed to steady myself, my right moves tentatively downwards."

        "Uh, whoops. My first contact with her is my palm clumsily meeting the front of her nose."

        "She giggles a little before turning her head sideways. Taking my cue, I gently cradle her cheek and use my thumb to feel the contours of her face as she so often does with me."

        "This would be a lot easier if she wasn't moving her face into my hand, but the feeling of her nuzzling into it is nice."

        "I swallow to try and steady myself, take my other hand from the bed and use it to guide myself into her."

        "As soon as I feel her warmth around me, I quickly realize just how turned on I am."

        "With my sight gone I'm free to concentrate far more on my other senses, including tactile feeling. The entire experience feels more vivid, more intense than it's been before."

        "I slowly start to move my hips back and forth, my heart beating wildly in excitement."

        "I feel Lilly's eyes clenching shut, the movement of her cheek under my thumb reminding me of the gentle hold I have on the side of her face."

        "It's hard to stop myself from being completely overwhelmed. It's hard to think that this is what sex is usually like for her, experienced through every sense but the one I hold dearest."

        "From her cheek to her neck, I begin to slide my hand downwards to take in the feeling of her body."

        "The contours of her collarbone… the light dew resting on her skin…"

        "My sense of smell is stimulated by the scent of her sweat and mine hanging in the air. Even the ambient smell, noticeably different from that of my own room, adds to the feeling."

        "When I move my hand to her supple breast, her soft mewling fills my ears, along with the sound of our act."

        "The skin under my hand moves back and forth with each thrust, my grip on it tightening as my lust for the near-naked body of Lilly before me grows."

        "I can even feel her small nipple against my palm. My hand slides further and my fingers pluck it through the thin silk of her pajama top."

        "Her whimpering sounds turn to moans as she fills with the same pleasure as I. I can feel my heart beating loudly in my chest, and her own beating underneath my hand."

        "I can feel her hands clasp my wrists, their grip surprisingly tight as her chest rises in overwhelming pleasure."

        scene black
        with dissolve

        "More… I want more…"

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.7)

        "I can feel my chest tightening as I rock back and forth frantically, both of us entirely taken with ourselves."

        $ renpy.music.set_volume(0.4, 0.5, channel="music")

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.7)

        "Nothing… that unusual… I just need to take deeper breaths to steady… myself…"

        $ renpy.music.set_volume(0.3, 0.5, channel="music")

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.7)

        pause 0.7

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.2)

        "This feeling is just… normal…"

        $ renpy.music.set_volume(0.2, 0.5, channel="music")

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.2)

        pause 0.7

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.2)

        hi "Aah… aaaaaaaah…"

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.2)

        pause 0.7

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.2)

        "This isn't… I can't… this pain is too much…!"

        play sound sfx_heartstop
        show heartattack alpha
        with Dissolve (0.1)

        stop music fadeout 0.3

        show heartattack residual
        with Dissolve (0.8)

        hi "AAAAARGH!"

        with vpunch

        "I stumble backwards from Lilly with unseemly haste, clumsily hitting the back of my foot against the table and falling to the ground with an unceremonious crash."

        "Breathing wildly, I frantically scrape at the ribbon over my eyes as I lay on my back. I have to get this off, I have to get this off…"

        scene white
        with softwipeup

        scene bg misc_ceiling
        show heartattack residual
        with locationchange

        "For a moment, everything goes blank. As the rush of newfound light assaults my eyes, my breathing slows from the brink of hyperventilation."

        $ renpy.music.set_volume(1.0, 0.0, channel="music")
        play music music_tragic fadein 4.0

        hide heartattack
        with Dissolve(3.0)

        "Seconds pass, and I carefully measure out the rhythm of my heartbeats with every ounce of concentration I can muster."

        "My heart is… normal. It's back to normal."

        "My body feels utterly bizarre as I lay dazed on the floor looking at the ceiling. The adrenaline from before is still pouring through my veins, but my mind is completely exhausted."

        "I prop myself up as I hear Lilly getting off the bed and coming towards me."

        show bg misc_ceiling_blur as bg2:
            center
            alpha 0.0
            linear 1.0 alpha 1.0
        show lilly superclose_shock:
            xalign 0.5 yanchor 0.5 ypos 0.15 rotate 180 alpha 0.0
            easein 1.0 ypos 0.3 alpha 1.0

        pause 1.0

        show bg misc_ceiling_blur as bg2 at center
        show lilly:
            xalign 0.5 yanchor 0.5 ypos 0.3 rotate 180

        li "Hisao? Are you okay? Hisao!?"

        hi "I'm fine, Lilly. I'm… fine."

        show lilly superclose
        with charachange

        "She gives a sigh of relief, her worried expression collapsing."

        "Her face afterward is the very last I'd ever wanted to see from her. It's a face I'd detested when I first saw my parents in the hospital all those months ago."

        "Pity. Lilly… pities me."

        scene black
        with shuteye

        "I just close my eyes and turn away, powerless. I feel like throwing up."

        play sound sfx_rustling

        "I can hear the sound of Lilly moving away and quickly attending to herself, the ruffling of her clothing being pulled back on after a moment of searching just barely audible."

        hi "Sorry…"

        scene bg school_dormlilly
        show lilly basic_concerned_paj at center
        with openeye

        "She slowly shakes her head as she finishes buttoning up her top. Her kind smile looks so fragile, so delicate, that it makes my heart sink."

        show lilly basic_concerned_paj_close
        with characlose

        show lilly:
            ypos 1.1
        with charamove

        "Approaching carefully, she feels out the edge of the low table before taking a seat next to me, putting her arms around my chest."

        li "I'm sorry, Hisao. I shouldn't have pushed my desires onto you."

        hi "You don't need to apologize. I'd normally be fine, you've seen that much before."

        hi "I guess I shouldn't have tried to push myself so far."

        "My eyelids feel heavy. Calmly sitting next to her like this is probably letting the adrenaline work itself out of my system, and letting my mind relax."

        show lilly basic_oops_paj_close
        with charachange

        li "So that's… why you never took the lead…?"

        hi "Yeah. I guess it's a good thing you like to, huh?"

        show lilly basic_weaksmile_paj_close
        with charachange

        "The joke seems to lighten her expression a little, a fact which helps let me feel less unease about my unreliable self."

        "Lilly's head comes to rest on my shoulder as I struggle to keep my eyes open, with more difficulty after each blink. I feel completely drained."

        li "It's okay, Hisao. It's all okay."

        stop music fadeout 5.0

        "No sooner does she say this than a small, quiet tune escapes her lips. Entirely too tired to think, all I can do is listen to her soft humming."

        "It's a soft, almost melancholic tune. It sounds familiar, but the more I try to remember its origin the less I seem able to concentrate."

        "The feeling and scent of her head gently resting on my shoulder and her warm body against my side are soothing. The soft humming of her voice, too, relaxes my mind as much as her warmth relaxes my muscles."

        "This singular, quiet moment… after all this fracas, it makes me realize just how exhausted I've become. I can feel my eyelids slowly becoming heavier and heavier."

        "Even with the chaos of before, I wish this moment would last forever."

        "Lilly and I together, sharing a single, solitary occasion together, just as we used to."

        "But if that's the case… why does she feel… further away than she's ever felt before?"

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .context:
        scene bg school_library
        with locationchange

        play sound sfx_doorslam
        play music music_happiness fadein 2.0

        "The loud clatter of books falling into the return slot abruptly breaks the grip of silence over the school library."

        "It's become a habit for me to come to the library at least once a week. Not only does the reading itself keep me busy, but discussing books with Hanako and Lilly also does."

        show yuuko panic_up at center
        with charaenter

        "Obviously startled, Yuuko suddenly twists towards the direction of the noise. I'd have thought her used to people dropping books by now, since she does work here."

        show yuuko neutral_down
        with charachange

        yu "Oh, hello Hisao. Back again?"

        "It takes me a moment to respond, my mind still distracted by the familiar melody of Lilly's humming that's hardly left my ears in the several days it's been since I fell asleep to it."

        hi "Hmm? Oh, yeah. Just returning some books I borrowed."

        "She casts her eyes downwards, presumably to the bin the books dropped into."

        show yuuko closedhappy_down
        with charachange

        yu "You're a very heavy reader, aren't you?"

        hi "It's become a bit of a routine now. Passes the time, at least."

        show yuuko worried_up
        with charachange

        yu "I wish I had free time to pass…"

        "From smalltalk to depression in less than five seconds. I think that's a new record for her. She seems a bit down in general today, even compared to normal."

        "Considering she has to work two jobs just to support herself, I could see how that would take a toll on her lifestyle."

        "Come to think of it, the pay for her job here can't be all that bad. The idea of staff in such a prestigious private school going hungry strikes me as counterintuitive."

        hi "Working two jobs must take a lot of time. I'd probably never manage it."

        show yuuko neutral_up
        with charachange

        yu "You're lucky, being a student. Do you think you'll be able to go to university?"

        "If she's asking, then I guess that's the expected result of having this kind of education. Private schools like this don't exactly come cheap."

        hi "I… guess. I have the money, I think."

        hi "I've got plans which will require going to one, and my grades are good enough. It's more a matter of how I'll pay to do so."

        show yuuko worried_down
        with charachange

        yu "University costs so much that I'm having to work two jobs to afford to enter it… paying for daily expenses too makes it a lot harder."

        show yuuko neutral_down
        with charachange

        yu "If you're reading this much though, that means you're doing well in school, right?"

        "Interesting logical jump. Not an altogether wrong one, though."

        hi "I suppose so. I didn't find any of the exams very hard, aside from maybe one or two."

        hi "Do you mind if I ask what studies you're pursuing in university?"

        show yuuko happy_up
        with charachange

        "Yuuko appears to genuinely brighten at the question."

        show yuuko closedhappy_up
        with charachange

        yu "Anthropology. To be specific, I'm specializing in the history of classical era Athenian civilization and democracy."

        "She really seems to know her stuff. Such enthusiasm is to be admired, and it's nice to see her genuinely excited about something."

        "I guess even somebody like Yuuko can be happy if she has a visible road ahead of her."

        hi "That's good to hear. If you—{w=0.6}{nw}"

        stop music fadeout 0.5
        play sound sfx_phone

        show yuuko panic_up
        with vpunch

        "Both of us jump at the sudden interruption coming from my pocket."

        scene bg school_hallway3
        with locationchange

        "Apologizing profusely and quickly shuffling into the hallway as I fumble with the cover of my mobile phone, I glance at the screen."

        "…Weird. It's a mobile number I don't recognize. Considering I can count the number of people with my number on one hand, I briefly wonder whether it's some telemarketer that lucked out."

        scene bg school_hallway3_blurred
        show phone mobile:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0
        with locationchange

        pause 0.5

        hi "Hello, Hisao Nakai speaking."

        mystery "Geez, pick up faster next time. Anyway, guess who?"

        play music music_comedy fadein 1.0

        "It only takes me a second to recognize the distinctively deep, brusque voice."

        hi "Hey, Misha. Didn't expect you to call me."

        aki "Huh!? Ya actually think I sound like her?"

        hi "Not at all, Akira. I don't remember giving you my number though, so I thought I'd mess with you."

        aki "Oh, that? I got Lilly to give it to me. Not hard."

        "She positively brims with pride at the statement. She's trying to get me caught up in her pace, I know it."

        "I suppose I shouldn't be surprised that the two would share my number though, given how close they are."

        hi "So, what's up?"

        aki "You free right now?"

        hi "I… guess? Why?"

        aki "Could you meet me at the park in town? I just want to talk to you about some stuff."

        hi "Is that an invitation to a date?"

        aki "What? Of course not…"

        stop music fadeout 5.0

        "She sounds suddenly crestfallen, her previous teasing nature having instantaneously left. It seems strange for her."

        hi "Anyway, I don't see why not. When do you want to meet?"

        aki "Kind of… now. Ish."

        hi "Wait, right now? But it's—"

        "The dead silence suddenly coming from the phone announces the fact that she has unceremoniously hung up."

        show phone mobile:
            easeout 1.0 ypos 0.7 alpha 0.0

        scene bg school_hallway3
        show phone mobile:
            truecenter
            easeout 1.0 ypos 0.7 alpha 0.0
        with locationchange

        pause 0.5

        hide phone

        "For a long time I just stand there, staring at the 'CALL ENDED' message on the screen while replaying the conversation in my head."

        hi "What the hell, Akira?"

        scene bg suburb_park_ss
        with shorttimeskip

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        play ambient sfx_parkambience fadein 2.0

        "Throwing a glance up and down the street, I cross the road and step into the park."

        "I've learned to pace myself on such walks, mostly because Lilly's slower speed during our forays into town means I have to consciously slow myself down."

        "That aside, I hope Akira didn't expect me to be immediately prompt."

        scene ev akira_park:
            right
            acdc_warp 15.0 zoom 0.8
        with whiteout

        play music music_night

        "It takes only a couple of seconds to spot her, waiting on a bench with a can of beer in her hand."

        "The look she gives me as I walk up lacks any hint of acknowledgment or greeting."

        hi "What's with that look? I needn't have come, you know."

        aki "I knew you would. You're that kind of person, after all."

        scene bg suburb_park_ss
        with locationchange

        play sound sfx_can_clatter

        "I lower my brow at her remark as she disposes of the can, emptied by the time I arrived, and a metallic clatter rings out. Akira takes a seat on the old wooden bench, and I follow her lead."

        play sound sfx_can

        "She takes another can of beer from beside her and opens it before speaking, taking a large gulp. She seems to really like that stuff."

        hi "I suppose I don't need to ask what this is about, or rather, who it's about?"

        show akira basic_resigned_close_ss at tworight
        with charaenter

        aki "I heard from Lilly that you asked about our family."

        "They share more than phone numbers, that's for sure. I'd probably be very worried right now if it weren't for the total lack of malice in her voice. Rather, her tone sounds almost wistful."

        hi "Idle curiosity, mostly."

        hi "…I have to admit, I'd never have guessed you two were half Scottish."

        show akira basic_ending_close_ss
        with charachange

        "She gives a wry chuckle of amusement."

        show akira basic_smile_close_ss
        with charachange

        aki "I've heard that before, trust me."

        show akira basic_distant_close_ss
        with charachange

        "The small smile falls from her face, her eyes looking ahead distantly."

        "Aside from the occasional elderly couple talking as they slowly walk the meandering paths, and the odd aging car, it's pleasantly quiet."

        show akira basic_lost_close_ss
        with charachange

        aki "She didn't tell you everything though, did she?"

        hi "It was pretty brief. Your parents live in Scotland, she hasn't met them since she was twelve, and she wants to meet them again."

        show akira basic_annoyed_close_ss
        with charachange

        aki "It's always surprised me how devoted she is to our parents, for all the good they did us."

        "The way she says it sounds almost derisive. She gives a small sigh, as if to quickly brush the feelings away."

        show akira basic_resigned_close_ss
        with charachange

        aki "Why do you think they left, Hisao?"

        hi "Why do I think they left?"

        hi "From what Lilly told me, it was because of work. I guess a pretty decently-paying job was involved as well, given the way your parents seem to live."

        hi "So Lilly went to a private school, and that's why she carries herself with the airs and graces of the upper class."

        aki "Yeah. Since the business in Inverness boomed, our father decided to move directly to the same city as its headquarters."

        show akira basic_smile_close_ss
        with charachange

        aki "That's just the conclusion I'd thought you'd come to, though. You're too good-natured."

        hi "You don't think they left for their career?"

        show akira basic_resigned_close_ss
        with charachange

        aki "I'm sitting here bitching to you about it. What do you think?"

        show akira basic_lost_close_ss
        with charachange

        aki "Yamaku Academy. I've always felt that place was kinda creepy; like it was an isolated hideaway for those 'proper society' doesn't want to see nor hear."

        show akira basic_annoyed_close_ss
        with charachange

        aki "They probably just rue the fact that Lilly wasn't old enough to be shoved there by the time they left."

        "A long silence follows her abrupt and very harsh criticism of her own parents, and Yamaku."

        "Lilly's blindness is hardly something that could be simply ignored for a high-class family attempting to keep up appearances, much less so when a lucrative offer is on the table."

        "Eventually Akira gives a derisive snort, her feelings coming to a head."

        aki "Moving to secure our financial future with his new job posting. Even at the time I hardly believed it."

        "Not wanting to simply be an avenue for her venting, I gently try to steer the discussion."

        hi "So you stayed in Japan with Lilly, then?"

        show akira basic_resigned_close_ss
        with charachange

        aki "Either I stayed with her, or she went to live with an ailing grandmother and grandfather."

        hi "What about Shizune's family? If you're cousins, then…"

        show akira basic_annoyed_close_ss
        with charachange

        aki "Our fathers hate each other. I'd have been more than happy to tell them to go screw themselves and live with them anyway, but Lilly wouldn't have wanted that."

        show akira basic_resigned_close_ss
        with charachange

        aki "I'd also had an offer for a job by then, so we did our best to keep our parents' house in proper shape, and tried to continue our lives as if they'd never left."

        hi "So you just lived by yourselves?"

        show akira basic_lost_close_ss
        with charachange

        aki "Basically. Lilly had school and I had my job, so we weren't exactly languishing."

        aki "With her schooling, her study, and having to do chores while I worked, though, I can't help feeling like I failed her. In the end, I tried to be there for her, and screwed it up."

        show akira basic_annoyed_close_ss
        with charachange

        aki "…Expecting a nineteen-year-old to be a mother for a blind child. It's ridiculous."

        "So… Lilly and Akira lived alone after their parents moved, with Lilly largely taking care of herself. I guess that explains her apparent independence, compared to many in Yamaku."

        "I may have lived alone much of the time since my parents both worked, but that's… just something else entirely."

        show akira basic_resigned_close_ss
        with charachange

        aki "Sorry for making you listen to my moaning, Hisao."

        hi "I don't mind at all, but… do you mind if I ask why you're telling me all this?"

        show akira basic_smile_close_ss
        with charachange

        aki "Hmph. You always were curious."

        show akira basic_distant_close_ss
        with charachange

        aki "Context, I suppose."

        aki "Life isn't a fairytale, Hisao. Some people have to learn that the hard way."

        "She takes a long drink from the can in her hand, her face becoming more depressed than distant."

        stop music fadeout 2.0

        show akira basic_resigned_close_ss
        with charachange

        aki "I broke up with my boyfriend a few days ago. After I leave, we're not going to be able to see each other again."

        aki "But that's how life is. You can't just set your life up and expect it to stay that way forever; sometimes stuff happens that you have to roll with, even if it means hurting yourself or others."

        "She takes a long breath before looking up at the bright orange sky."

        show akira basic_distant_close_ss
        with charachange

        aki "Damn… if I smoked, I could take a nice, long drag right about now and look kinda cool."

        "I want to respond, to help her in whatever way I can, but I feel utterly useless. This kind of situation is one I've never been in, and I simply don't have the experience to say anything meaningful to comfort her."

        "Akira looks over and evidently picks up on this, much to my embarrassment."

        show akira basic_lost_close_ss
        with charachange

        aki "I must look pretty pathetic right now, whining about this to someone I barely know."

        hi "Hardly, and I'm pretty much an expert on looking pathetic."

        show akira basic_ending_close_ss
        with charachange

        "She gives a chuckle, the act feeling like a personal victory for me."

        show akira basic_smile_close_ss
        with charachange

        aki "You're a good kid, Hisao. When I said that I approved of you being with my sister, I wasn't joking or just being nice."

        show akira basic_smile_ss:
            tworight
            ypos 1.1
            ease 0.5 tworight
        with charadistant

        show akira at tworight

        play sound sfx_can_clatter

        "She picks herself up off the seat with a grunt, one that seems ill-fitting given her age, and throws the now empty can into the bin after one last swig."

        show akira basic_boo_ss
        with charachange

        aki "It's just unfortunate that doesn't really count for much in this world."

        show akira basic_resigned_ss
        with charachange

        aki "When I said that I was leaving for Scotland, I was doing it because a good position opened up in our company's headquarters."

        aki "When our folks told me that when we were at their place, though, they also gave Lilly a summons to rejoin them in Inverness."

        play music music_sadness fadein 0.5

        "No way…"

        "Her evasiveness when asked about her future… that awkwardness that had steadily grown between us… that uncharacteristic outburst of anger…"

        "All of them suddenly fit into place."

        "The same family that she reminisced about after Hanako's birthday party, the same family that left her and Akira to themselves after taking flight to greener pastures…"

        "Now I feel stupid for never cornering Lilly on what was bugging her. I'd never even considered if something had happened during her trip to her family's home at Inverness."

        "And now, a sense of unease grows in my chest. If her family has summoned her to join them in Scotland, all the way on the other side of the Earth…"

        hi "Has she… accepted?"

        show akira basic_lost_ss
        with charachange

        aki "Lilly hasn't told me whether she plans to accept, and it seems she hasn't told you, either."

        aki "That's why I called you down here to talk, Hisao."

        hi "Context, huh…"

        "I sit back, my feelings of worry and frustration no doubt written all over my face."

        show akira basic_resigned_ss
        with charachange

        aki "Lilly's a strong person, Hisao, but she's not infallible."

        aki "I guess it's my job to worry about her, being her older sister, but I think that you deserve to know."

        hi "I understand."

        show akira basic_lost_ss
        with charachange

        aki "You okay? You sound depressed."

        hi "No, I'm just… thinking."

        show akira basic_ending_ss
        with charachange

        aki "That's good. Thinking is good. Being rash won't get you anywhere."

        show akira basic_boo_ss
        with charachange

        "She looks at her watch, barely moving her wrist."

        show akira basic_lost_ss
        with charachange

        aki "I've got to go. Will you be okay?"

        hi "I'll be fine, don't worry. I'll have to talk to Lilly about it and get everything sorted out."

        show akira basic_smile_ss
        with charachange

        "She gives a smile, but it doesn't feel all that genuine or sincere."

        "Really, both of us are dancing around the fact that Lilly's on the precipice of the biggest decision of her life and is trying to take the entire burden on herself."

        "And part of that burden is the matter of our relationship."

        stop music fadeout 5.0
        hide akira
        with charaexit

        "By the time I look up, Akira's already walking off with her hand held up."

        "For the first time in a long while, I finally have an answer to something. Perhaps not even that. But at least I now have the right question to ask."

        "'Will you leave, or stay?'"

        stop ambient fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .a_faraway_future:
        scene bg suburb_roadcenter_rn
        show rain normal
        with locationchange

        play ambient sfx_rain fadein 4.0

        hi "Hurry, Lilly!"

        show lilly basic_concerned_cas_close_rn behind rain at center
        with charaenter

        li "I'm moving as fast as I can!"

        "I can barely make out Lilly's voice over the deafening pounding of the rain. Even though I dislike pulling her around, the situation calls for it."

        "I turn forward, my free hand over my head in a futile attempt to keep at least my hair dry. My vision seems to be in grayscale. This really is rotten weather for summer, and the last kind of climate I'd want for a date."

        "A pity. I'd even checked the weather forecast beforehand, one of the very few times I've ever done so, only for it to say that Sunday afternoon would be fine."

        "Looking to Lilly, her shoulders are by now completely drenched, with her right hand holding tightly to mine and her left gripping her retracted cane."

        "This horrid downpour came on just as we were between our destination and Yamaku, so we decided to try rushing the rest of the distance rather than doubling back."

        "Entirely unused to running this fast, Lilly's using all her concentration just to avoid tripping over."

        show lilly basic_oops_cas_close_rn
        with charachange

        li "Hisao, do you know where we're going!?"

        "Even she's reduced to shouting to try and be heard over the combined noise of the wind and the rain."

        hi "The Sha—"

        "The rest of my voice is completely drowned out by an even heavier burst of rain."

        show lilly basic_sad_cas_close_rn
        with charachange

        li "The what!?"

        hi "The Shanghai!"

        show lilly basic_concerned_cas_close_rn
        with charachange

        li "How far is it!?"

        hi "It shouldn't be far now!"

        scene bg suburb_shanghaiext_rn
        show rain normal
        show lilly basic_concerned_cas_close_rn behind rain at center
        with shorttimeskip

        "It doesn't take long before I call out to her once again."

        hi "It looks like we're safe, it's just up ahead!"

        "I quickly pull up to a stop just in front of the familiar exterior, the lantern outside still giving off its reliable glow, and wait for Lilly to catch her breath before going in."

        hi "Ladies first."

        play sound sfx_storebell

        show lilly basic_smileclosed_cas_close_rn
        with charachange

        pause 0.5

        hide lilly
        with charaexit

        "The tiny bell inside rings out when I hold the door open for her, a smile and a polite nod being my reward before entering myself."

        $ renpy.music.set_volume(0.1, 1.0, channel="ambient")
        play music music_dreamy fadein 3.0

        scene bg suburb_shanghaiint
        show lilly basic_smileclosed_cas at center
        with locationchange

        "As I step in behind her and wipe my feet, only a quick glance is necessary to notice the distinct lack of activity. The Shanghai doesn't seem to get much in the way of patronage, and today is no different. Only a couple of tables are occupied."

        "Summoned by the bell's ringing, a most expected person comes to greet us."

        show bg at bgleft
        show lilly at twoleft
        with charamove

        show yuukoshang happy_up at tworight
        with charaenter

        yu "Welcome to the Shanghai!"

        "Yuuko looks chipper today. Trying to predict her moods is pretty hard, but it's a nice change from the norm."

        show lilly basic_smile_cas
        with charachange

        li "Hello, Yuuko."

        hi "Hey."

        show yuukoshang closedhappy_down
        with charachange

        yu "Good afternoon, you two."

        show yuukoshang neutral_down:
            ypos 1.25
        with Dissolvemove(0.2)

        pause 0.2

        show yuukoshang at tworight
        with charamove

        "She takes a deep bow, somewhat taken aback as she rights herself again and gets a better look at us."

        show yuukoshang worried_down
        with charachange

        yu "What happened to you? You both look…"

        "Her eyes drift towards the glass of the door behind us."

        show yuukoshang panic_up
        with charachange

        yu "Oh. Oh dear."

        hi "We're inside now, at least. I think that's the most important thing."

        show lilly basic_weaksmile_cas
        with charachange

        li "It's nice and cozy. You're lucky to be working inside today."

        show yuukoshang smile_down
        with charachange

        yu "It has been nice and quiet. I like days like this."

        show yuukoshang worried_down
        with charachange

        yu "Oh wait, um, sorry… is there anything you'd like?"

        show lilly basic_smile_cas
        with charachange

        li "French vanilla tea, please."

        hi "I'll have the same."

        show yuukoshang closedhappy_up
        with charachange

        yu "Right. Coming right up."

        hide yuukoshang
        with charaexit

        "She quickly skitters off with a determined look on her face, trying very hard not to forget our orders. If nothing else, she is at least dedicated to her jobs."

        show bg at center
        show lilly basic_smileclosed_cas_close at center
        with charamovechangefaster

        show lilly:
            ypos 1.1
        with charamove

        "I lead Lilly to an empty seat before the two of us settle down. As usual, there's a large difference between my exhausted flopping down into my seat and Lilly's delicate sliding into hers, her cane set beside her."

        "For a while I just idly watch the rain falling outside. The occasional person runs down the street trying to stay as dry as possible, hands often tightly gripping a rain-soaked umbrella."

        "Lilly sits just as quietly as I, her eyes closed as she intently listens to all that's happening."

        "It's a comfortable, relaxing silence that exists between us; just the type that we'd so often shared together in the past months."

        stop music fadeout 5.0

        "For Lilly, at least."

        "I can't help replaying the words of her sister in my mind, at times contrasting them to both our time spent together since I entered Yamaku, and to the way we've been since we started dating."

        "No matter how much I try, I can't work Lilly out. It's as if the harder I try to second-guess her emotions and her potential decision, the more difficult it becomes to reach a clear conclusion."

        "It makes me doubt whether I'd ever really understood her. In the end, I'm going to have to ask, even though I very much want to avoid doing so."

        show lilly basic_smile_cas_close
        with charachange

        li "You seem quiet today, Hisao."

        hi "Really?"

        show lilly basic_ara_cas_close
        with charachange

        li "You seemed so enthusiastic about taking me out on a date, I'd assumed you had something specific you wanted to do."

        hi "No, not really. Just wanted to spend some time with you."

        show lilly basic_weaksmile_cas_close
        with charachange

        li "Is that so…"

        hi "Fine. There was one thing."

        show lilly basic_cheerful_cas_close
        with charachange

        "A little grin finds its way onto Lilly's face, her knowing full well that she's bested me. It makes what I want to say all the more awkward."

        hi "It was just… Akira and I were talking."

        show lilly basic_surprised_cas_close
        with charachange

        li "Oh?"

        hi "What's with that tone?"

        show lilly basic_weaksmile_cas_close
        with charachange

        li "You two do seem to get on well, don't you?"

        hi "Well, I do think she's a pretty cool person to talk with. It'd be nice if any of the teachers were anything like her."

        show lilly basic_sleepy_cas_close
        with charachange

        li "'Cool…'"

        "For a moment I try to place her tone of voice, my mouth curling into a smirk as I realize it."

        hi "You're not jealous, are you?"

        show lilly basic_pout_cas_close
        with charachange

        li "I'm not jealous!"

        "After her teasing me over such a thing on our first date, I don't feel too bad having a little laugh at her expense this time around."

        "As we settle down though, it's only a minor distraction from the real point of why I brought Lilly here."

        hi "Don't worry, it was mostly just everyday stuff. That said, there was something Akira mentioned that I wanted to talk to you about."

        hi "When you went to see your family in Inverness a while back, she said…"

        show lilly basic_reminisce_cas_close
        with charachange

        li "Akira told you about my family's summons, hasn't she?"

        play music music_drama fadein 2.0

        "Seconds tick by while I try to read Lilly's face, an odd mixture of feelings written on it. She seems annoyed, but also somewhat confused."

        show bg at bgleft
        show lilly:
            twoleft
            ypos 1.1
        with charamove

        show yuukoshang neutral_up at tworight
        with charaenter

        yu "Um… here…"

        "Yuuko tentatively slides our drinks onto the table, her presence oddly small."

        hide yuukoshang
        with charaexit

        show bg at center
        show lilly:
            center
            ypos 1.1
        with charamove

        "As she walks back to the counter after a quick, polite nod, I realize the air between me and Lilly is thick and our expressions are both somewhat pensive."

        show lilly basic_displeased_cas_close
        with charachange

        li "Even though she says I should lead my own life, she still interferes at the worst times…"

        hi "I don't think you should blame Akira here. She's just looking out for you, and it's not like I can't understand her concern over this."

        show lilly basic_weaksmile_cas_close
        with charachange

        "Lilly's irritation gives way to an awkward, and largely unsuccessful, attempt to mask her feelings. She really doesn't deal well with being cornered on personal topics."

        li "I know, but… I just wanted some more time. I knew you'd have figured it out eventually, but…"

        hi "You were intentionally hiding this from me? For how long were you planning to do so?"

        show lilly basic_displeased_cas_close
        with charachange

        li "As I said, I simply wanted more time to think it through. I wanted to be sure of my decision before telling you."

        hi "What did you decide to do, in the end?"

        "I know what I want her to say, but an awful feeling refuses to leave my gut."

        show lilly basic_sleepy_cas_close
        with charachange

        li "My family does dearly want me to return to them, and Akira will be going as well. I could still teach as a career, whether it be here or there."

        hi "So… you're going."

        hi "How long have you known? I already know you were asked when you first went to Scotland, about a month ago."

        show lilly basic_concerned_cas_close
        with charachange

        li "Some… time."

        "My frustration very nearly boils over. The fact that she's done this affects me more than it should."

        "For her to not only be leaving but to have been actively hiding her own plans from me, and after seeming for so long to be the one solid pillar of support and reliability I could depend on…"

        "It feels as if the foundation underneath me is suddenly shifting drastically, much faster than I can adapt to. Perhaps this isn't so much frustration as sheer unease."

        hi "Lilly…"

        show lilly basic_sad_cas_close
        with charachange

        li "I'm sorry, I just… I wanted to think this through completely. I wasn't trying to take advantage of you, please—"

        hi "I know, Lilly. I know. This is just really sudden."

        hi "I guess this means that once you go, we'll be breaking up?"

        "For one of the few times I've seen since I met her, she's genuinely lost for words."

        "She doesn't look surprised, no doubt because the fact had dawned on her once she became sure of her decision, but rather, she appears genuinely unsure of how to deal with the situation now that it's in front of her."

        show lilly basic_oops_cas_close
        with charachange

        li "W-we could try pursuing a long-distance relationship. They're getting more and more common these days, after all…"

        "Even as she says it, the tone of her voice gives away that she doesn't truly believe what she's saying."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")
        $ renpy.music.set_volume(0.05, 1.0, channel="ambient")

        nvl clear
        nvl show dissolve

        n "{vspace=90}Lilly is far too old-fashioned to be able to cope with a relationship without any kind of physical presence, and even I am, to an extent. All we would ever be to each other would be a voice from the other side of the world."

        n "In the end, trying to rationalize everything is futile. Any attempts to try and connect what's happening with the future or past just seem to get more difficult the more I concentrate."

        n "Those quiet moments when we just walked side by side, the precious time we spent with Hanako and Akira, the casual chatter we had during lunchtimes, the times we made love, the confessions of our feelings to each other…"

        n "{vspace=90}All pointless. All just a fleeting moment in our young lives."

        $ renpy.music.set_volume(0.1, 1.0, channel="ambient")
        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl hide dissolve
        nvl clear

        hi "We're just two children pretending to be adults, aren't we?"

        show lilly basic_sad_cas_close
        with charachange

        "A long, long silence hangs in the air between us. The noise of the other patrons drinking and talking only makes the situation feel more strange and disconnected."

        "Lilly's face remains low, her dejected expression clouding it."

        stop music fadeout 4.0

        show lilly basic_concerned_cas_close
        with charachange

        li "I'm sorry, Hisao."

        "A simple apology, and no more. She's left entirely without any further response or comment."

        "With a long sigh, I gather what's left of my thoughts and ask the final question I have for her."

        hi "When will you be going?"

        show lilly basic_sad_cas_close
        with charachange

        li "I'll be leaving with Akira, so it'll be a little less than a week."

        hi "The beginning of summer holidays?"

        show lilly basic_sleepy_cas_close
        with charachange

        li "Just a little afterward, yes."

        "Her tone is unusually slow and steady, her apologetic and depressed mood all the more written to her face as she tries to hide it in her voice."

        "In the end, I can't even keep my promise of going to Tanabata with her before she leaves."

        stop ambient fadeout 14.0
        show ev hisao_teacup:
            truecenter
            zoom 0.85
            acdc_warp 15.0 zoom 0.8
        with locationchange

        "I look down, seeing my face reflected in the by now lukewarm cup of neglected tea sitting in front of me."

        "I really thought I'd left this kind of expression behind."

        "For a while I just stare down into the still surface, trying to sort through my emotions to get at what course of action I should take, whether it be right now or in the future."

        "But, just as before, the effort is wasted."

        hide ev
        show lilly basic_reminisce_cas_close
        with locationchange

        "I glance up to see Lilly gently sipping her cooled tea without complaint, her face drawn and shoulders slumped. She looks to be deep in thought too, a strangely cold atmosphere coming between us as we isolate ourselves to mull things over."

        "Even as Lilly's cup slowly empties, mine remains untouched."

        "It's a long time before I notice the rain dying down outside and the few other patrons of the Shanghai having left."

        scene bg school_dormhallway
        with shorttimeskip

        stop ambient
        play music music_moonlight fadein 0.5

        "The chill of the rapidly darkening evening permeates the dormitory hallways. While trudging down the corridor to my room, I see an unwelcome movement from up ahead."

        show kenji happy:
            center
            xpos 0.4
            easein 0.5 center
        with charaenter

        show kenji at center

        "Sure enough, the opening of the door opposite mine heralds the arrival of a bespectacled Kenji."

        ke "Hey man, what's…"

        show kenji tsun
        with charachange

        ke "Woah dude, you look awful, I think. You okay?"

        "He really has a knack for making any situation better."

        hi "I… don't really want to go into it. It's late."

        show kenji neutral
        with charachange

        ke "Okay. That's cool."

        ke "If you ever want to talk about it, I'm, you know, here."

        "I look at him for a moment before surrendering my stern front and awkwardly scratching the back of my neck, embarrassed by my standoffish response to him."

        hi "Thanks, Kenji."

        show kenji happy
        with charachange

        ke "Hey, it's cool. That's what friends are for, right?"

        hi "Yeah, you're right. Um, seeya."

        scene bg school_dormhisao_ni
        with locationchange

        "I open the door to my own dorm room and close it behind me as he quickly waves me off."

        play sound sfx_doorslam

        "The solid thud the door makes against the door frame sounds out a final call for the life I've led since coming to Yamaku."

        "I just stand in my darkened room, fruitlessly attempting to work out what I should do from this point onwards."

        "Just what should I do…?"

        $ renpy.music.set_volume(1.0, 0.0, channel="ambient")
        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .farewell:
        scene bg school_scienceroom
        with locationchange

        "As class ends, I simply rest my head on my hand and stare out of the window to pass the time."

        $ renpy.music.set_volume(0.5, 0.0, channel="music")
        play music music_normal fadein 2.0

        nvl clear
        nvl show dissolve

        n "{vspace=60}It's been a few days since Lilly told me her plans. I haven't been to our ordinary lunchtime haunt since then, not that there would be much point."

        n "Hanako's been busy with the newspaper club she's newly joined, and has even begun talking in class with Naomi every now and then."

        n "Even Lilly, aside from the fact that a meeting between us would've been awkward in any case, has been run off her feet with class representative duties as the summer holidays approach."

        n "And now, they're just about here. With the end of today's bell, the summer holidays will have begun."

        n "{vspace=90}I suppose that all I'll end up doing will be visiting my parents for the duration and lazing about my old home, now that my previous plans are entirely askew."

        nvl clear

        n "{vspace=60}Meanwhile, Akira and Lilly will be en route to Scotland, to live out the rest of their lives there."

        n "No matter how hard I try to rationalize the idea that once the summer holidays begin, my life will return to the way it was, it simply refuses to happen."

        n "Everyone's moving on with their lives. Lilly's rejoining her family, Akira's moving up in her father's business, Hanako's gaining new friends and hobbies, and even Yuuko's moving ahead with her university aspirations."

        n "Even I'm moving forward, in the end. With the grades I've gotten so far in Yamaku, much less after such a rocky beginning, the path to get into teaching science as a career seems straightforward."

        n "{vspace=60}I suppose I should at least be happy about that much, but it doesn't really seem to help."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl hide dissolve
        nvl clear

        mi "Hicchan~!"

        "I quickly stop my ruminating and turn to face the bubbly voice beside me, putting on the most upbeat expression I can muster."

        show misha hips_smile at twoleft
        show shizu behind_smile at tworight
        with charaenter

        "As expected, Shizune stands flanking her. I have a sneaking suspicion they want something from me."

        hi "Hey Misha, Shizune. What's up?"

        show misha hips_grin
        with charachange

        mi "Well~…"

        show misha perky_smile
        with charachange

        mi "Shicchan and I were thinking~…"

        show misha sign_smile
        with charachange

        mi "Since we're just two poor little girls that need help with all the work we've been given just before the holidays begin~…"

        hi "Sure, I can help."

        show misha perky_sad
        with charachange

        mi "But Hicchan, we're really nee—"

        stop music fadeout 0.2

        show misha perky_confused
        with charachange

        mi "What?"

        "I think I broke Misha."

        show shizu behind_blank
        with charachange

        "Even Shizune raises an eyebrow at her accomplice's shuddering stop in her tracks."

        show misha hips_grin
        with charachange

        mi "So you'll help us, Hicchan?"

        hi "I just said I would, didn't I?"

        "It's hardly like I have anything better to do. Maybe helping them with their work will help take my mind off the situation."

        "Misha seems genuinely ecstatic with my response, but Shizune's expression is clouded and difficult to read. I find myself quickly averting my eyes from her own, as it almost looks like a face of pity. No doubt, it must just be my imagination."

        scene bg school_council
        with shorttimeskip

        play music music_daily fadein 0.5

        "This is hardly the first time I've been in the student council room. Indeed, I've found myself down here often, either to help Lilly with class rep work, or to sort out one thing or another with the Student Council itself."

        "Now, though, it's quite a different place."

        show sc_comp:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0

        pause 1.0

        "Papers and folders are strewn across every table in the room, only a solitary little black laptop atop a single desk sticking out from the mess."

        "It looks positively ancient, and I'd guess it has been valiantly serving its task in archiving information for years and years."

        show sc_comp:
            easeout 1.0 ypos 0.7 alpha 0.0

        pause 1.0

        hide sc_comp

        hi "So, what needs doing? This looks like a lot to do."

        show misha hips_smile at twoleft
        show shizu behind_frown at tworight
        with charaenter

        shi "…"

        "Shizune's expression becomes determined as she signs. It's a worrying look."

        show misha hips_grin
        with charachange

        mi "Everything, Hicchan!"

        "My worry was well placed."

        hi "Everything… you say?"

        show shizu basic_normal
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "What's left on the desks is what needs to be done."

        show misha perky_smile
        with charachange

        mi "It all needs to be digitally recorded, which is what the laptop is for."

        hi "And I'm guessing that I'll be the one doing this?"

        show shizu behind_smile
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "Shicchan says she saw you with the computers in the library a few days ago, and that you seemed really good with them~."

        "Good with computers? I can touch-type, I guess, but it still seems like an overestimation of my skills."

        hi "I was just typing up homework…"

        hi "Wait, Shizune was watching me do that?"

        show shizu adjust_smug
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "One must know their allies before they can know their enemies, of course~."

        show misha cross_grin
        with charachange

        mi "Wow, that's pretty wise…"

        "For once, it's not very hard to work out who said what."

        "Nonetheless, it doesn't seem worth fighting over. Sitting at a computer doing some typing hardly seems onerous, as far as tasks to help Shizune and Misha go."

        show shizu basic_normal
        with charachange

        shi "…"

        show misha perky_smile
        with charachange

        mi "Besides, it will help to take your mind off things~."

        hi "Take my mind off things? Take my mind off what things?"

        show misha perky_confused
        with charachange

        "Misha's face goes blank as she translates this for Shizune, though the latter's response is only to glance away towards the window after briefly signing."

        show shizu behind_blank
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        show shizu basic_normal2
        with charachange

        "Misha's face quickly returns to a smile as she translates back. She was confused, I guess, but Shizune is harder to pin down."

        show misha cross_smile
        with charachange

        mi "I was just thinking you may like to get your mind off the exams, of course~."

        hi "Either way, we may as well get into it sooner rather than later. I'll go along with you."

        show misha hips_smile
        with charachange

        mi "That's the spirit, Hicchan~!"

        scene bg school_council
        with shorttimeskip

        "And that's the fifth spreadsheet compiled and saved. Time for the next month's…"

        "After a little bit of fussing around, we all managed to get a bit more organized."

        "Shizune's been gathering up the loose sheets and, thankfully, sorting them into a neat pile next to me. Meanwhile, Misha's been handling the manual writing work, her girly pink pen leaving its unmistakable mark on paper after paper."

        "Once I got myself into a rhythm, this really wasn't so bad. Shizune and Misha also seem to be in the swing of things, wordlessly communicating as they go about their business with fervor."

        "I periodically glance at the sheet beside the laptop, apparently a list of student names and matching addresses, as I dutifully enter the data written on it. I don't pay a lot of attention to what I'm typing in until I reach about midway down the page."

        "Hakamichi… class 3-3… Huh. Her family's home is in Saitama."

        "My idle curiosity is ended abruptly as three light taps can be heard rapping on the door."

        show misha perky_smile:
            twoleft
            xpos 0.4
            easein 0.5 twoleft
        with charaenter

        show misha at twoleft

        "Misha quickly skips over to check who it is, tapping Shizune's shoulder on the way past to let her companion know what's happening."

        show misha hips_grin
        with charachange

        mi "Ah, you're here~."

        hi "Hmm? Who is it?"

        "With a slight pause to enter Shizune's data into the file along with all the others, I look up to check who's at the door."

        stop music fadeout 0.5

        show lilly basic_weaksmile_cas:
            left
            xpos -0.2 alpha 0.0
            ease 1.0 left alpha 1.0
        with None
        show lilly
        show bg at bgright
        show misha at center
        with charamovefaster

        show lilly at left

        "…Lilly?"

        "After giving a cursory nod to Misha in greeting, she perks her head up in her trademark manner."

        show lilly basic_surprised_cas
        with charachange

        li "Is that Hisao?"

        "She's pretty darned good at working out my voice from the smallest of phrases nowadays."

        hi "Yeah, it's me. Um… hey."

        show lilly basic_reminisce_cas
        with charachange

        "The atmosphere feels slightly awkward as she bows. Neither of us knows quite how intimate we should be around each other, given she's leaving in just a matter of hours."

        "This is a fact that, thankfully, neither the oblivious Misha nor the hardworking Shizune pick up on."

        hi "So… you've got work to do as well?"

        show lilly basic_sleepy_cas
        with charachange

        li "Unfortunately. I arrived as soon as I could, but my class held me up with a surprise farewell party, and I had to get changed."

        "I glance down at the laptop's clock. It's pretty much the end of lunchtime, so I'm guessing Lilly managed to wrangle the last period off as well."

        show lilly basic_weaksmile_cas
        with charachange

        li "I take it Shizune is here as well?"

        play music music_shizune fadein 3.0

        show shizu behind_blank at right
        with charaenter

        shi "…"

        show misha cross_smile
        with charachange

        mi "Of course!"

        show shizu adjust_smug
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "And I've been here during all of lunchtime as well!"

        "That last comment was really not needed. Shizune's baiting Lilly into another argument, I can feel it."

        show lilly basic_displeased_cas
        with charachange

        li "I'm sorry I can't be as hardworking as you, Shizune. I'll endeavor to hire more lackeys to do my work in future, I assure you."

        "And Lilly just took the bait, escalating things further."

        show shizu basic_frown
        with charachange

        shi "…"

        show misha hips_frown
        with charachange

        mi "But aren't you the one always outsourcing work to your classmates~?"

        show lilly basic_listen_cas
        with charachange

        li "The difference is that they choose to help, unlike your tyrannical grip on your own class."

        show shizu behind_frown
        with charachange

        shi "…"

        show misha cross_smile
        with charachange

        mi "Tyranny works~! Even if we did things differently, we still got the same results, right~?"

        show lilly basic_displeased_cas
        with charachange

        li "This is school, not a police state. You will have to remind me when you were appointed class monarch, I'm afraid."

        show shizu cross_angry
        with charachange

        shi "…"

        show misha cross_frown
        with charachange

        mi "You have to seize power, it's not as good if it's just handed to you~! But I guess you wouldn't really understand that, right~?"

        show shizu adjust_angry
        with charachange

        shi "…"

        show misha hips_smile
        with charachange

        mi "You'll also have to remind me when monarchs were elected into their positions~."

        "Lilly positively bristles at this. Shizune's two-hit combo forces her onto defense."

        show lilly basic_displeased_cas
        with charachange

        li "Yet for all your vaunted power, you cannot get one person to help you without forcing him."

        show shizu behind_frustrated
        with charachange

        shi "…"

        show misha sign_smile
        with charachange

        mi "But Hisao volunteered~! He's such a hard worker, he's doing this instead of meaningless socialization, right~?"

        show lilly basic_listen_cas
        with charachange

        li "Is that so. Hisao?"

        "Ah, this is bad. I've really ended up between a rock and a hard place."

        "As much as it may pain me to do this, the truth has at least a chance of stopping this argument here and now."

        hi "It's okay, Lilly, they didn't harass me to come or anything."

        show lilly basic_displeased_cas
        with charachange

        "Lilly gives me a disapproving grimace, silently radiating her strong feelings of displeasure in my general direction."

        "She can be quite scary when she wants to be, though thankfully that isn't often."

        show shizu cross_angry
        with charachange

        shi "…"

        show misha hips_frown
        with charachange

        mi "Hicchan, you make that sound like it's a regular occurrence~…"

        hi "It isn't?"

        hi "In the end, it doesn't matter so long as everything's getting done at a good pace. Let's just get this work over with so we can go home."

        hide shizu
        with charaexit

        hide lilly
        with charaexit

        hide misha
        with charaexit

        "Shizune snorts derisively and gets back to marking off the sheet in front of her, while Lilly sighs and finds her way along the room with her hand following the filing cabinets lined along the wall."

        "This would mark the only time I've managed to successfully defuse one of these situations, but the grudging ceasefire built around mutual fear and respect makes this feel more like the Cold War than any real peace."

        "I can't take all the credit though; Lilly's leaving has surely affected Shizune to some extent, to make her give up so easily."

        show bg at center
        with charamove

        show lilly basic_listen_cas at center
        with charaenter

        "Moments before getting back to my work, I notice Lilly reaching up to grab something from above a filing cabinet. I almost offer to help, but her height gives her ample ability to take it down safely."

        show lilly basic_displeased_cas:
            ypos 1.15
        with charamovechangefaster

        "Once she sets the strangely shaped device on the desk beside me, I realize just what it is… sort of… as she takes the old green covering off and sits down."

        show brailler:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0

        pause 1.0

        "At first glance it seems to be an old metallic blue typewriter, but it doesn't take me long to realize it's far from ordinary."

        "It has far fewer keys than expected, and those it has show no lettering printed on them. Only the shadows cast by the tiny Braille dots on them give a hint to the thing's purpose."

        hi "Blind typewriter?"

        show lilly basic_smile_cas
        with None

        show brailler:
            easeout 1.0 ypos 0.7 alpha 0.0

        pause 1.0

        hide brailler

        li "Oh, this? Well, you're not far off."

        li "It's normally called a Perkins Brailler, but it's basically a typewriter for the blind, yes. It presses Braille into the page rather than text, which is why it has fewer keys."

        hi "Huh… that's really neat."

        show lilly basic_cheerful_cas
        with charachange

        "She gives a lighthearted grin at my curiosity over it. I have to admit that it appeals to my sense of novelty."

        hide lilly
        with charaexit

        "Without further ado, we each get back to our allotted tasks. The loud clunking of the mechanics in Lilly's Brailler and the tapping of the laptop's old and weary keyboard quickly fill the room."

        "It's a nice atmosphere, really. Everyone knows what they have to do, and Lilly and I get to sit beside each other and exchange the odd word as we work away."

        "Nostalgic. That's what it feels like."

        "It's pleasant, but just slightly stained with the knowledge that our time together is nearing its end."

        show lilly basic_smile_cas:
            center
            ypos 1.15
        with charaenter

        li "Excuse me, Misha?"

        show bg at bgleft
        show lilly:
            twoleft
            ypos 1.15
        with charamove

        show misha hips_smile at tworight
        with charaenter

        "To properly address her, Misha bounces over from the filing cabinet she's peering into, in spite of Lilly's lack of sight. For a moment I think it strange, but then realize it's exactly what I do."

        mi "What's up?"

        show lilly basic_weaksmile_cas
        with charachange

        li "Could you ask Shizune where the attendance records for class 3-2 are? I think they've been moved."

        show misha hips_grin
        with charachange

        mi "Okie dokie!"

        hide misha
        with charaexit

        stop music fadeout 8.0

        "And with that, she flitters off to Shizune, who's working at a table behind us."

        "Lilly's familiarity with the council room, and the efficiency with which she works, remind me that she, Misha and Shizune used to all work together in the Student Council."

        "Maybe this is a fitting end for her stay in Yamaku; working away just like she used to, surrounded by those she loves and, at least, liked."

        "I look up, getting taken off-guard by Shizune sorting through a drawer, rather than Misha."

        show shizu behind_blank at tworight
        with charaenter

        "Sure enough, she plucks out a manila folder, entirely blank save for the just barely visible bumps on its front, and holds it in front of Lilly."

        "Lilly's hand flits over it to check what it is, her fingers feeling out the dots of Braille and confirming it's what she asked for."

        show lilly basic_smile_cas
        with charachange

        li "Thank you, Misha."

        "No reply."

        show shizu behind_smile
        with charachange

        "No reply, that is, save for an odd grin… no… smile… on Shizune's face."

        show ev lilly_sheets:
            truecenter
            zoom 1.05
            easein 10.0 zoom 1.0
        with whiteout

        "A couple of seconds pass before Lilly clicks that it isn't Misha behind her, but Shizune. Her momentary look of surprise is replaced by a slightly bashful smile."

        "For a few moments, the room is all but still and silent."

        "Eventually, though, Shizune strides back to her workstation and Lilly begins typing once again."

        "It only lasted a handful of seconds in all, but it feels like years of communication were made up for in that one silent exchange."

        scene bg school_council_ss at right
        with shorttimeskip

        play music music_tranquil fadein 3.0

        hi "There, finished."

        "I lean my head back and rub my eyes to try and work away their weariness. Staring at that small and rather poor screen has taken its toll."

        show lilly basic_smile_cas_ss:
            center
            ypos 1.15
        with charaenter

        li "Excellent timing; the only thing left is to file these away and I'll have my workload finished as well."

        hi "Good. I can pack up the Brailler and put it away while you do that."

        show lilly basic_smileclosed_cas_ss
        with charachange

        li "Thank you, Hisao."

        hi "Misha, are you and Shizune far from being done?"

        "I look around for the two as I replace the cover over the Brailler, only to see them waiting at the door. I guess they must be waiting for us."

        scene bg school_council_ss at left
        show misha hips_smile_ss at center
        show shizu behind_blank_ss at right
        show lilly basic_smileclosed_cas_ss at left
        with shorttimeskip

        "With a minimum of wasted time, we file and pack up everything that remains and join them."

        hi "Thanks for waiting, you two."

        show misha hips_grin_ss
        with charachange

        mi "We couldn't just take off without you, Hicchan, you've been a great help!"

        show shizu behind_smile_ss
        with charachange

        "Shizune nods approvingly, pleased with my efforts."

        hi "I guess… that's the last class representative work done and over with, then."

        show lilly basic_smile_cas_ss
        with charachange

        li "That's right."

        show misha perky_sad_ss
        with charachange

        mi "I'll miss you, Lilly. I think it was fun working with you."

        show lilly basic_weaksmile_cas_ss
        with charachange

        li "Thank you, Misha. It's been good working with you… and Shizune."

        show shizu basic_normal_ss
        with charachange

        "Shizune thinks for a moment before formulating her response. It's not that she often communicates without thinking, quite the opposite, but this time it's even more considered than usual."

        show shizu adjust_smug_ss
        with charachange

        shi "…"

        show misha perky_confused_ss
        with charachange

        "Misha looks a little surprised before passing on the message."

        show misha hips_smile_ss
        with charachange

        mi "Shizune says… you'd better do your work over there better than you did it here."

        show lilly basic_giggle_cas_ss
        with charachange

        "Far from taking offense, Lilly giggles into her hand."

        show lilly basic_smileclosed_cas_ss
        with charachange

        li "If that's the case, then please tell Shizune to give those still here a little more understanding in the future."

        "Competitive until the last. Maybe Shizune and Lilly aren't so different after all."

        show shizu behind_smile_ss
        with charachange

        shi "…"

        show misha hips_grin_ss
        with charachange

        mi "Shicchan says that she'll be checking to make sure you live up to your end of the promise."

        show lilly basic_cheerful_cas_ss
        with charachange

        li "Then that's how it will be."

        show lilly basic_smile_cas_ss
        with charachange

        li "I'd better be off, then. Goodbye, Shizune. Goodbye, Misha."

        show lilly basic_smileclosed_cas_close_ss
        with characlose

        li "Hisao?"

        "Lilly takes a hold of my arm in hers, there being no need for a cane if I'm here to guide her. With a nod of farewell to the two, we set off out the door and make our way to the school grounds."

        "As I turn to wave goodbye to them, I notice Shizune's gaze lingering on Lilly. They may annoy each other, but family bonds aren't easily broken."

        scene bg school_courtyard_ss
        with locationskip

        hi "Got all your papers sorted, then?"

        show lilly basic_smileclosed_cas_ss at center
        with charaenter

        li "Yes, they've all been filled out and handed in."

        hi "On top of things as always, aren't you?"

        show lilly basic_weaksmile_cas_ss
        with charachange

        stop music fadeout 4.0

        "She gives an earnest smile at the compliment, but it feels as if her happiness is just a veneer over the fact that she's fully aware of how much she's leaving behind."

        "It reminds me of how she was like when I first met her; always smiling, always that little bit aloof, always that little distance away from everybody."

        "Even now, she still maintains that air around many others, especially those she's not close to. I had hoped that our time together would have changed that fact."

        scene bg school_gardens_ss
        with locationchange

        "Our pace slows, the two of us coming to a halt in the all but empty school gardens."

        show lilly basic_weaksmile_cas_ss at center
        with charaenter

        li "Hisao? Is something the…"

        play music music_comfort

        show lilly basic_surprised_cas_close_ss
        with vpunch

        "Lilly's words are cut short as I turn and wrap my arms around her, pulling her tight. I may not usually be given to such impulsive actions, but I just want to be close to her, even if it's the last time I'll be able to."

        "All the other students have retreated to their dormitories and homes, only the ruffling of leaves in the breeze making any sound whatsoever."

        show ev lilly_touch_cas
        with charachange

        "As I draw back, I can see she has dropped her carefully maintained smile."

        "Her hand hesitates, wanting neither to leave nor to stay on my features."

        "She is putting up a brave show, but her slight trembling gives her away. Lilly may be able to control herself well, but even she can't hold her composure together now."

        "This is the woman I've come to love, but also the one who in all too short a time will leave the country forever."

        li "I'm sorry, Hisao."

        hi "It's okay. You've got your own life to lead, after all."

        scene bg school_girlsdormhall
        with shorttimeskip

        "We walk up the hallway in the girls' dormitory hand in hand, our emotions by now largely quelled. Nevertheless, our hands grip each other's much more tightly than before."

        "Faint, muffled voices can be heard from Lilly's room, the origins of which aren't difficult to guess."

        scene bg school_dormlilly
        with locationchange

        show hanako emb_downsad:
            tworight alpha 0.0
            ease 1.0 xpos 0.4 alpha 1.0
        show lilly basic_weaksmile_cas:
            twoleft alpha 0.0
            ease 1.0 alpha 1.0

        pause 1.0

        show hanako:
            tworight
            xpos 0.4
        show lilly at twoleft
        with None

        show lilly basic_surprised_cas
        with vpunch

        "The moment she opens the door, Hanako bursts through and wraps her arms around Lilly, taking her very obviously by surprise."

        ha "Lilly! Lilly!"

        show lilly basic_oops_cas
        with charachange

        li "Ha-Hanako…?"

        show hanako emb_downtimid
        with charachange

        ha "I'm going to miss you… Lilly…"

        show lilly basic_weaksmile_cas
        with charachange

        "As expected, she's on the verge of tears. Lilly gently rubs Hanako's hair with her hand in response, then pulls back and gives a warm, reassuring smile."

        show akira basic_lost:
            right ypos 1.15 alpha 0.0
            ease 1.0 right alpha 1.0

        pause 1.0

        show akira at right

        "Looking beyond Hanako, Akira can be seen getting up from the side of Lilly's bed and scratching her head."

        show akira basic_smile
        with charachange

        "Her eyes turn from Lilly and Hanako to me, a stilted, weak smile hanging on her face. I try to return a more genuinely happy look, but the result is probably just the same."

        show akira basic_boo
        with charachange

        aki "So, everything set? Managed to hold back from killing Shizune?"

        show lilly basic_giggle_cas
        with charachange

        "The comment draws an amused giggle from her sister."

        li "Yes, I have everything in order, and yes, I managed not to. Have you packed everything you need?"

        show akira basic_smile
        with charachange

        aki "Got the two bags right here, but there's still some stuff left at the Hakamichis' home. I can pick that up while we wait there for tomorrow evening's flight, though."

        "Akira gives the two large black traveling bags on the floor a hearty pat. She probably came to help pack and make sure everything was in order on Lilly's end, before going together with her."

        show hanako cover_worry at center
        with charamovechangefaster

        ha "Lilly… will you be okay… over there?"

        show lilly basic_smileclosed_cas
        with charachange

        li "I'll be all right, I assure you. I'll have Akira looking after me as well, and you know that she's reliable."

        show hanako basic_worry
        with charachange

        ha "But…"

        show lilly basic_smile_cas
        with charachange

        li "Don't worry, Hanako. I have your phone number after all, so we can stay in touch. With Akira's help, I could send you things over the Internet as well."

        show akira basic_boo
        with charachange

        aki "Hey, don't use me just because you won't learn how to use a computer."

        show lilly basic_giggle_cas
        show hanako basic_smile
        with charachange

        "Hanako and Lilly both giggle briefly, the mood lightening ever so little."

        show lilly basic_smileclosed_cas
        with charachange

        li "That goes for you too though, Hisao. I promise I'll contact you once I'm in Scotland."

        hi "I know. I'll be looking forward to it."

        "Her offer may be kind, but we both know that this is tantamount to breaking up. Neither of us has any illusions as to how well we'd manage a long-distance relationship."

        "With nary a word of prompting, the four of us begin the long, solemn walk to the school gate."

        scene bg school_gate_ni at bgleft
        with shorttimeskip

        "The numerous lamps scattered around the Yamaku grounds fail to do much more than provide pinpoints of light in an otherwise dense darkness."

        "A car parked on the road just outside the school grounds comes into view, its shining black exterior reflecting the dimly lit lamps of Yamaku. I call out to Akira in an effort to alleviate a bit the heavy atmosphere."

        hi "That your car? What kind is it?"

        show akira basic_smile_ni at center
        with charaenter

        aki "Don't know much about cars, do you? It's a Lancer Evo. Solid and speedy."

        "Well, it's not as if her comment on my knowledge is off the mark. I've never really taken an interest in them."

        show akira basic_resigned_ni
        with charachange

        "She gives a small sigh."

        show akira basic_lost_ni
        with charachange

        aki "She's been good. Pity I have to part with it tomorrow, just like the summerhouse. You guys were the last to visit it before it changed hands."

        "Turning back from my rather faulty attempt at smalltalk, I glance at Hanako and Lilly, following behind us."

        show akira at tworight
        show bg at center
        with charamove

        show hanako emb_downtimid_ni:
            xpos 0.4 xanchor 0.5
        show lilly basic_weaksmile_cas_ni at twoleft
        with charaenter

        "By rights, Hanako should be leading Lilly, but it's rather definitely the other way around as she clings tightly to Lilly's arm."

        "It's a depressing sight."

        show akira basic_resigned_ni
        with charachange

        aki "So… I guess this is it."

        show lilly basic_reminisce_cas_ni
        with charachange

        li "Indeed."

        "Although the time for everyone to say their farewells is now, nobody really wants to take the first step. It's as if the longer nobody speaks, the better the chances of them simply not leaving."

        show hanako emb_downsad_ni
        with charachange

        ha "Lilly… do you really have to go?"

        show lilly basic_concerned_cas_ni
        with charachange

        li "I'm sorry, Hanako. I won't be leaving you forever, though; I can still call you. Hisao will still be here as well."

        "I nod, but Hanako just clutches all the tighter to Lilly's arm."

        "After spending so long without anyone to call family, it must be excruciating to have to say goodbye to the one person that was as close to a mother as anyone could have been in her life."

        show lilly basic_sad_cas_ni
        with charachange

        "Lilly lets out a long, sad breath. All Akira and I can really do is stand by quietly on the sidelines, since the only person that can solve this would be Lilly herself."

        "Eventually, Lilly pulls her arm from Hanako's grip and holds both of her shoulders gently, a much more decisive way of address than I've ever seen Lilly take with her."

        show lilly basic_reminisce_cas_ni
        with charachange

        li "Hanako, remember when we first met?"

        show lilly basic_weaksmile_cas_ni
        with charachange

        li "When you entered my room for the first time after overhearing my consoling of a friend, you didn't say a single word for the entire night. Even as I poured you tea and talked, you sat silently and simply listened to what I said."

        li "It took many quiet meetings like that before you began to open up to me, but as you began to, I felt some of the happiest moments I've ever felt."

        show lilly basic_sleepy_cas_ni
        with charachange

        li "I didn't become your friend because I pitied you, Hanako. I became your friend because I knew you were hiding not just from me, but from everyone."

        li "Your ambitions, personality, interests, tastes… I didn't know any of them, and neither did anybody else."

        show lilly basic_weaksmile_cas_ni
        with charachange

        li "As you showed yourself to me though, I began to realize the person that you were, and became sure that our meeting was a very special moment."

        show hanako emb_blushtimid_ni
        with charachange

        ha "But I…"

        "Lilly cuts her words short as she brings her hand to Hanako's head and brushes her bangs to the side, gently pressing her lips to Hanako's forehead."

        show lilly basic_smile_cas_ni
        with charachange

        "As she pulls her head back, leaving Hanako all but speechless and her eyes moist, Lilly beams a wide smile."

        li "I believe you are a very beautiful person, Hanako, and I am certain that you will become a strong and confident woman."

        li "You are a very dear friend, and someone whom I love very much. Just like Hisao, I will never forget you for as long as I live."

        show lilly basic_smileclosed_cas_ni
        with charachange

        li "I may be leaving, but you have your own life here to lead. Just as I do, you have your own friends and hobbies, and your own hopes after graduation. I want you to devote yourself to them, even after I'm not around any more."

        show lilly basic_smile_cas_ni
        with charachange

        li "That is why I think you will be okay. Because you are your own self, with your own life. You yourself proved that to me."

        show hanako emb_downtimid_ni
        with charachange

        "Hanako lowers her head in embarrassment, but nods as she does so."

        ha "I… I understand…"

        ha "I know I have to say goodbye… I know you have to go your own way…"

        show hanako emb_smile_ni
        with charachange

        ha "But… thank you, Lilly. For everything."

        show lilly basic_reminisce_cas_ni
        with charachange

        li "Thank you, Hanako. Will you be okay?"

        "There are a few seconds of silence before the answer comes."

        show hanako cover_smile_ni
        with charachange

        ha "I will."

        show lilly basic_smile_cas_ni
        with charachange

        "Lilly smiles, undoubtedly at least partly in relief."

        show lilly basic_smileclosed_cas_ni
        with charachange

        li "That makes me very happy, then. Goodbye."

        show hanako basic_bashful_ni
        with charachange

        ha "Goodbye… Lilly."

        show lilly basic_weaksmile_cas_ni
        with charachange

        li "And farewell to you as well, Hisao."

        hi "Goodbye. I'll miss you."

        show lilly basic_weaksmile_cas_close_ni
        with characlose

        "She pauses for a moment before walking up to me. Her right hand, outstretched in front of her, takes a hold of my shoulder."

        "Her left hand slowly and daintily reaches towards my face, taking my cheek in her palm."

        show lilly basic_smile_cas_close_ni
        with charachange

        "For a while she simply holds my face, her fingers just slightly moving to take in its contours. Usually her hand would be warm when doing such a thing, but the night air's given her skin a cool edge."

        "I'm not sure how long we stay like this, her clouded eyes pointed just below my own as she wears a wistful, almost distant smile. Eventually, though, I take her cold hand in mine."

        "It's difficult to do so, but with a slight sigh I gently remove her hand from my cheek."

        hi "I hope you have a long and happy life, Lilly, no matter where you might go."

        show lilly basic_weaksmile_cas_close_ni
        with charachange

        li "Thank you. I'll make sure to."

        "She takes a long, trembling breath before turning slightly towards Akira's direction."

        show lilly back_sad_cas_close_ni
        with charachange

        li "Akira…"

        show akira basic_lost_ni
        with charachange

        aki "Okay."

        show hanako at left
        show lilly back_sad_cas_ni at center
        show bg at right
        with charamovechangefaster

        "With a nod, she takes Lilly's hand and begins to guide her to the car parked outside the gates. They both walk slowly and deliberately, as if their movements had been rehearsed in advance."

        "It's strange to feel like this now, watching somebody leave Yamaku. The feeling of unease I have now reminds me of the first time I walked through those black wrought iron gates, that always looked far too pompous for what they were."

        "As they leave, all of us know full well that our lives are irreversibly changing. I'd always told myself that I just have to take life as it comes, but everything's changing so fast, so suddenly."

        "In the end, Lilly's an irreplaceable part of the lives of both Hanako and me."

        "The noise of Akira opening the passenger door for Lilly brings me out of my thoughts, her hand waving back as Lilly gets in."

        show akira basic_smile_ni
        with charachange

        aki "Seeya guys! Take care of yourselves!"

        show lilly basic_weaksmile_cas_ni
        with charachange

        li "Goodbye Hanako, goodbye Hisao!"

        show hanako cover_smile_ni
        with charachange

        "Hanako's hand quickly shoots up, her face brightened by her enthusiastic farewell."

        ha "Goodbye Lilly! Goodbye!"

        hi "See you, Akira, and goodbye Lilly!"

        hide lilly
        hide akira
        with charaexit

        "The door shuts as we all put on our best happy farewell faces, Akira getting in the car herself and starting it up in short measure."

        "Lilly's hand can just be seen waving through the tinted windows, both of our hands waving high as well."

        "Just as every other time I've done such things, I can't quite work out precisely why I, or Hanako, wave to her given that she'd never see us doing so. But it doesn't matter."

        "Even after that black, shiny car goes down the hill and disappears into the dark night, we carry on waving and seeing Akira and Lilly off."

        stop music fadeout 5.0

        "And then… they're gone."

        show bg at center
        show hanako basic_normal_ni at center
        with charamovechangefaster

        "A strange stillness takes over as our hands return to our sides."

        "I don't quite know what I should do or how I should feel. In the end, we just stand there silently staring down at where the car disappeared from sight."

        ha "Goodbye… Lilly."

        show hanako basic_normal_close_ni
        with characlose

        "All I can do in response to her quiet, mournful goodbye is to place a hand on her shoulder."

        show hanako basic_distant_close_ni
        with charachange

        "She looks at me for a few moments before looking back down the hill, secure in the knowledge that I'm still around for her."

        "What we'll do from now doesn't seem all that uncertain. We all have our own ambitions now, just as Lilly said."

        "But even so, it feels like there's a certain missing part in both of our lives now. Something that can never be replaced."

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    if not (want_true and address_it and mention_the_letter):
        return

    call timeskip

    label .false_cadence:
        scene bg school_hallway2
        with locationchange

        play music music_daily fadein 1.0

        "The snap of my mobile phone's closing contrasts with the ambient chatter and noise audible even in the hallway outside the library."

        "It's the first day of the summer holidays. A time that had perpetually seemed so far away, and yet it's now not only here but also made painfully obvious by the students, or lack thereof, left in the school."

        "Most students have returned home to spend the holidays with relatives by now. The few that are left are mostly chatting between themselves, usually about what they intend to do in the coming weeks."

        "It makes me feel like the odd one out, for taking advantage of the school library being open for the first several days of the holidays."

        "Ostensibly it's for students to drop off any books they've borrowed and have yet to return, and for those who'll have their parents pick them up, to help pass the time until they get whisked away."

        "Thanks to the recent lengthy phone call from my parents, which had so rudely woken me from my sleeping on a beanbag at the back of the library, I'm now in the latter category."

        "Sliding my phone back into my pocket, this time remembering to set it to silent, I go back into the quiet and wholly placid room."

        scene bg school_library_ss
        with locationchange

        "It's a nostalgic sight. Just as when Lilly first led me to the library, the orange tint of sunset bathes the room in its light while Hanako sits on a beanbag silently reading and Yuuko fusses, just barely visible behind the counter."

        "Hanako especially has been noticeably more quiet than usual since yesterday's happenings, but I can't really blame her."

        "It wasn't just me that depended on that person, after all."

        "I quietly walk back to the beanbag near her where I'd sat before, being doubly careful not to make any unnecessary noise."

        scene ev hana_library
        with locationchange

        show ev hana_library_read
        with charachangeev

        "The soft puff it gives as the bag takes my weight makes Hanako's eyes flick towards me, but only for a second."

        "I get the feeling that Hanako's been quiet only partly out of sadness following Lilly's departure."

        "Rather, she seems more thoughtful and measured than I'd expected; perhaps due to her desire of working out how to deal with Lilly's leaving rather than just being depressed over it. It makes me a little proud of her."

        hi "Hey, Hanako?"

        show ev hana_library
        with charachangeev

        ha "Y-yeah?"

        hi "Still going ahead with your idea of traveling?"

        "She gives a determined nod."

        ha "I'll be starting in a day or two. Naomi's decided to come with me, too."

        hi "Wow, quick start. Where're you two headed to first?"

        ha "I think we're going to start by going north… then loop down and go southward."

        hi "So… Hokkaido's going to be first?"

        "She gives another nod, more tentative than the last. The significance of that place is not lost on either of us."

        hi "Do you know how you're going to handle the traveling expenses and accommodations?"

        ha "Yeah, I've worked everything out. I think it should be okay. Naomi says she has her side worked out, too."

        hi "You know that if you need anything you can just call, right? I gave you my number before. Any time of the day is fine."

        show ev hana_library_smile
        with charachangeev

        "She gives a smile, which in itself feels like a small personal victory."

        ha "I know."

        ha "Th-thanks… Hisao."

        "Maybe Lilly was right. Although I may offer Hanako any help I can possibly give, I feel as if I know she doesn't need it."

        "She really has grown."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=90}Hanako's plans for her holidays are in sharp contrast to my simple following of my parents' suggestion to stay with them."

        n "Holidays had always made me feel less excited than most, though, so maybe this is just a return to the status quo."

        n "{vspace=30}Before my heart attack, I'd always lived so aimlessly that holidays weren't all that much different from my everyday life anyway."

        n "After school I'd wander around a bit in the city, often hanging out with some friends, before making my way home to eat dinner with usually one of my parents, but rarely both."

        n "Their work schedules didn't leave much time for them to be home, and going there straight from school would just have meant I'd end up feeling bored. I was an urbanite through and through."

        nvl clear

        n "{vspace=90}Since coming to Yamaku though, it feels like I've fundamentally changed as a person. The phone call with my parents erased any traces of doubt I might have held on that, in any case."

        n "While before I had exercised a fairly normal level of independence for a teenager, that being not a whole lot, my parents were more than pleased to hear of my newfound ability in taking care of myself."

        n "Laundry, cooking for myself, cleaning, all in addition to other general chores that come from living without parents around… just little menial things I've had to pick up, but with relative ease."

        n "{vspace=30}When I think about it, I'd always depended on them, even if they hadn't been at home all the time. To say I never depended on anyone after moving to the Yamaku dormitories would be far from the truth, though."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl clear
        nvl hide dissolve

        yu "Um… excuse me…"

        stop music fadeout 3.0

        scene bg school_library_ss
        show yuuko worried_down_ss at center
        with locationchange

        "The two of us look up at the awkwardly fidgeting figure in front of us. Some things never change."

        show yuuko worried_up_ss
        with charachange

        yu "It's getting close to closing time, so um…"

        "Oh, right. I'd forgotten that the library closes earlier during the holidays."

        "Hanako and I both get up and dust ourselves off, placing our books back on the shelf behind us. The fact that our tastes in reading material have a fair amount of overlap is useful at times."

        "With a bow to Yuuko to apologize for taking so much time, Hanako takes her leave of us."

        show bg at bgleft
        show yuuko worried_down_ss at twoleft
        with charamovechangefaster

        show hanako basic_normal_ss at tworight
        with charaenter

        ha "See you tomorrow, Hisao."

        hi "Bye."

        hide hanako
        with charaexit

        "And with that, she walks out of the large, wooden, aging doors that herald the entrance to the library."

        play music music_happiness fadein 3.0

        show bg at center
        show yuuko neutral_down_ss at center
        with charamovechangefaster

        yu "She's a quiet person, isn't she?"

        "I suppose I should be surprised at a staff member sharing personal opinions like this, but after knowing Yuuko for a while it's largely expected. Our relationship is more personal, rather than one with her acting as an authority figure."

        hi "Yeah, I think that's just how she is."

        hi "She's got a lot more confidence in herself these days, though."

        show yuuko smile_down_ss
        with charachange

        yu "I don't know her as well as you do, but I think I agree. It's nice to see her talking to people here; she never used to do that before."

        hi "Hey, Yuuko… you know about Lilly's leaving, right?"

        show yuuko worried_down_ss
        with charachange

        yu "She told me herself a few days ago. It must be hard, leaving everyone behind like she is."

        "She quickly looks back to me after she says this, probably remembering that I went to her for advice on the relationship between Lilly and me before."

        show yuuko worried_up_ss
        with charachange

        yu "Are you going to be okay?"

        "That's… a difficult question. It's something I'd rather not think about for now, though, given more pressing issues."

        hi "Something seems kind of off about this whole deal, don't you think?"

        "Yuuko appears to think for a while, absentmindedly scrunching her face up in a variety of creative ways as she does so."

        show yuuko worried_down_ss
        with charachange

        yu "I don't think I really know her well enough to make that kind of judgment."

        yu "I'm sorry I can't be more help."

        hi "Nah, that's fine. I'm just sort of thinking aloud."

        "I give a deep sigh and scratch my head in frustration."

        hi "There's just so much stuff happening at once that I have no control over… it feels like I'm being swamped."

        show yuuko neutral_down_ss
        with charachange

        yu "I think everyone goes through times like that."

        yu "What's important is to concentrate on what you can do, rather than what you can't do. At least, that's how I see it."

        show yuuko smile_down_ss
        with charachange

        yu "If I didn't think like that, I don't think I'd be able to manage my life as it is."

        "She says it with a smile and a light tone, but her words are far from any kind of joke. Being pulled between two jobs as she is, just to hopefully make enough money not only to live, but also for university, must be exhausting."

        "Perhaps that's why, coming from her, this feels like it has more meaning than if it had come from most others."

        hi "I guess you've got a point there."

        hi "Thank you for your advice once again, Yuuko."

        show yuuko closedhappy_down_ss:
            ease 0.5 ypos 1.2
        with charachange

        pause 0.2

        show yuuko:
            ease 0.5 center
            linear 0.5 alpha 0.0
        with charamove

        "She bows deeply and smiles again, before making her way back to the counter where she spends so much of her time."

        stop music fadeout 2.0

        scene bg school_dormhisao_ni
        with shorttimeskip

        "The tiny wings of the cardboard crane in my fingers are only just visible in the dim light of my room, just a little of the moonlight being able to peek through the curtains and around their edges."

        show origami_hand:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0
        with None
        show bg school_dormhisao_blurred_ni
        with Dissolve(1.0)

        play music music_twinkle fadein 10.0

        "I lie still in my dark bed for a long time, idly looking up at the little origami bird."

        "It feels like a lot's happened since Lilly folded this, but at the same time it feels like very little has changed."

        "Compared to everyone else, I'm back to square one. I might have a newfound idea of where I want to go in life, but that's hardly something that affects me now."

        "Hanako changed, I know that much. If anything, she just makes me feel like I've got no excuse to be like this, considering her previous situation."

        "Lilly, though…"

        "I turn the bird in my fingers another way, looking at it from yet another angle."

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=60}When I first met her, she seemed aloof and perhaps somewhat distant. Her actions were always careful, measured and precise, and her carefully maintained composure always gave the appearance of unerring confidence and serenity."

        n "In time, she became less formal. Just a bit, but enough. It felt good to see her lowering her inhibitions around me, and opening up, even just a little, of her own accord; it felt as if I was seeing her real self slowly become more vibrant and visible."

        n "{vspace=30}Now, though, I'm beginning to have doubts."

        n "{vspace=30}Perhaps they're to be expected after what is, effectively, the two of us breaking up. They don't feel new or strange though, but rather like an old book being found and dusted off."

        n "I soon realized after meeting Lilly that she saw me as she did Hanako; as someone who needed help and care. At first, I simply thought that we'd be fine as friends, helping each other through our limited time together in school."

        nvl clear

        n "{vspace=60}But then I began to treasure our moments together more and more, from our quiet walks to our talking over lunch. The good sides of her personality became ever more obvious, and ever more likable."

        n "The absence caused by Lilly's trip to Scotland to visit her long-distant family and sick aunt only made me realize how much I liked just being around her, and I had thought that she felt a similar way."

        n "{vspace=30}For her, though, maybe that wasn't everything to our relationship."

        n "{vspace=30}Even after she returned to Japan, that just meant she lost her family once again after meeting them for such a brief time."

        n "She lived so much of her life without her family around, not to mention with Akira working long hours, that she had little choice but to be like that."

        nvl clear

        n "{vspace=60}I had thought her sense of independence to be a good and admirable trait. It was in stark difference to my reliance on my parents before my heart attack, as reluctant as I may have been to admit it."

        n "However, it also meant that she never let people get too close to her."

        n "She lost her family likely due to her blindness, went to a different school from anybody she knew because of it, and worked all the harder to make sure she didn't end up a burden on her sister and those around her."

        n "{vspace=30}And now, Akira's going to Inverness, just like the family she thought she'd lost."

        n "She never told me of her plans, as conflicted as she was about them."

        n "Lilly didn't want to be a burden on anyone, including me."

        n "{vspace=60}…I'm an idiot."

        nvl clear

        n "{vspace=60}I never questioned it. I never tried to be there or asked when she needed me to."

        n "I just set my life up and expected it to stay that way forever, with the two of us having a nice long relationship where we pushed forwards towards our future together."

        n "{vspace=30}A small pit of frustration and anger at myself wells up in my chest."

        n "{vspace=30}I just let everything happen, never even trying to help Lilly."

        n "{vspace=30}Just her being there was enough. I thought I could keep going on if that were true."

        n "But that could never have been enough. It was a childlike dependence on somebody, without any attempt to understand or help their situation."

        n "Thanks to that, I lost Lilly. I lost the one person I loved most because I wasn't there for her when she needed me."

        stop music fadeout 5.0

        nvl clear
        nvl hide dissolve

        show origami_hand:
            easeout 1.0 ypos 0.7 alpha 0.0
        with None
        show bg school_dormhisao_ni
        with Dissolve (1.0)

        hide origami_hand

        "With an increasingly angry feeling washing over me, I turn over and set the crane back on the desk next to my clock, the place where it has lived since that day when she folded it for me."

        "Since that day when she herself said that my burdens needn't be my own."

        "The obnoxious bright red numerals of my alarm clock shine through the darkness of the room onto my tired eyes."

        "Ten o'clock. Evening. Curfew will be soon."

        hi "I wonder…"

        "Akira mentioned they'd be leaving this evening."

        "I've no idea exactly when their flight is… but that means there's a chance, however small, that they might not have already left."

        "Adrenaline starts to move through my body as I sit up on my bed, my eyes suddenly wide with possibility."

        "There's no guarantee they haven't left, indeed it's likely that they already have, but there's also a chance they haven't, however small it may be."

        "Just this once, just as I should have before…"

        play sound sfx_switch

        show bg school_dormhisao
        with Dissolve(0.2)

        $ renpy.music.set_volume(1.0, 0.0, channel="music")
        play music music_friendship fadein 9.0

        "I stand up and rush over to my cabinet, throwing out some clothes as fast as I can and sliding them on in quick succession."

        "Each second that goes by is a second that I can't regain, a second that may mean the difference between catching them and losing them forever."

        "Even if I fail, I have to try. I can't let her leave everything behind without even trying to stop her. Without, just this once, being there for her."

        "With the last of my clothes slipped on, I hastily grab the phone off the desk. Luckily, the number for a local taxi company is still in my call history."

        show bg school_dormhisao_blurred
        show phone mobile:
            alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7
            easein 1.0 ypos 0.5 alpha 1.0
        with locationchange

        pause 0.5

        "A gruff, unenthusiastic voice announces the name of the company while I pace around the room. It takes some effort to slow down my voice and keep it clear over the phone."

        scene bg school_dormext_full_ni
        with locationskip

        "The chilly night air sweeps against me as I open the dormitory door, but nevertheless I keep up my brisk speed as I half-jog, half-run out to the school gates."

        "It may not be curfew just yet, but it's precariously close. If there were a guard around they'd no doubt have some questions for me, but it looks like I've managed to come out just before they arrive, or they're around a corner."

        scene bg school_gardens_ni
        with locationchange

        "My pace picks up as I make my way through the school gardens, their night-time allure all but lost when I begin to run to the school gate."

        scene bg school_courtyard_ni
        with locationchange

        "The lamps of the courtyard, dim as they are, provide just enough illumination to light the way and prevent me from tripping over. The buildings themselves take on a rustic, almost antique-looking edge when I glance at them."

        "Looking back, it seems strange that they once appeared so dark and looming to me. Now they just look to be somewhat anachronistic school buildings, the same as any others bar their age."

        scene bg school_gate_ni
        with locationchange

        "Leaving the gates behind me, I pull up to a stop just before the taxi. Parked just as Akira's car had been, its gaudy and brightly lit sign looks out of place in the quiet country backdrop."

        "I impatiently squeeze myself through the door, giving the driver the address for where the two should hopefully be staying."

        scene bg shizu_houseext_ni
        with shorttimeskip

        "By the time the taxi pulls up after its trip at maddeningly casual speed, it's well and truly deep into the night."

        "The house is truly enormous, its sheer size much larger than I'd expected, and ominously still. Fearing the worst, I ask the driver to stay just in case my efforts are for naught."

        "A single press on the fancy intercom system outside the gate produces a short electronic melody in the otherwise silent road. It's not long before a somewhat deep, gruff voice can be heard from it."

        mystery "This is the Hakamichi residence. Please state your name and why you're bothering us this late."

        "I press on despite inwardly wincing at the reasonable annoyance audible in his voice."

        hi "It's Hisao Nakai. I was hoping to meet Lilly or Akira, if they're still here."

        "Surprisingly, I manage to summon quite some energy to my voice, enough to make the other side of the intercom silent."

        scene bg shizu_houseext_lights
        with Dissolve(0.2)

        "A few seconds pass, but just before I press the button again and ask what's going on, a light turns on outside the front door."

        "I strain my eyes to try and make out who is coming through, but as he comes past a large parked car with fishing rods sticking out the back, his identity becomes clear."

        "His face is typically placid and emotionless as he saunters up to the gate. He's still childlike in his mannerisms, despite his demeanor. With the press of a few buttons from behind the fence, the gate slowly opens."

        show hideaki surprise_ni at center
        with charaenter

        hh "Hisao? What are you doing here?"

        "I think this is the most emotion I've ever heard from his voice, not that it would be hard to reach that mark."

        hi "Akira told me that she and Lilly would be staying here before they left for their flight."

        hi "I need to talk to Lilly, just one last time. Are they still here?"

        show hideaki sad_ni
        with charachange

        "The look on his face says everything."

        "I failed. I was too late. The one time when I actually needed to act quickly, and…"

        show hideaki serious_up_ni
        with charachange

        hh "Actually… it's possible…"

        hi "What? What is it?"

        show hideaki confused_ni
        with charachange

        "He's a bit taken aback by my fervor, but I can't help it at this point."

        show hideaki normal_ni
        with charachange

        hh "They left not long ago; only a few minutes before you arrived, in fact. If you go straight to the airport, you might be able to… Hisao!?"

        "I dart back towards the waiting taxi, grabbing what little money is left in my pocket as I go."

        hi "Thanks, Hideaki!"

        "With that I take a seat, and in short order bark out my destination."

        scene bg city_street4_ni
        show crowd_ni
        with shorttimeskip

        play ambient sfx_crowd_outdoors fadein 2.0

        "My chest beats wildly as I tear down the street, my body twisting this way and that to slip between the pedestrians walking back and forth beside me."

        "With the road solidly blocked by taxis and other cars, dropping off passengers and picking up others in the time they have to wait, we ended up having to stop almost a block away."

        "But that's in the past now. What matters is reaching Lilly."

        "One foot hits the ground, the other quickly following without the slightest thought, as if my legs have taken on a life of their own and all my mind can do is concentrate on the view ahead of me."

        "Just one glimpse of that long hair of hers. That long, yellow hair that was the same color as the wheat that stretched as far as the eye could see."

        "In the end, I depended on Lilly, just like Hanako did. Even after we started going out, it still doesn't feel like she really ever let herself depend on me."

        "Except for one moment. That one moment where we held each other tightly on that bright yellow field."

        "At that time she must have feared losing me just as she did everyone else. That's why, just this once…"

        "The night air wraps around me, draining every last remnant of warmth out of my body, to the extent that it feels more like midwinter than a summer night."

        "My fingers, my hands, my feet… they all feel increasingly cold."

        "The sound of the passing crowds is reduced to no more than a background hum while the sound of my shoes hitting the pavement echoes loudly, every step surging towards the person I have to catch."

        "Forced by my chest tightening in response to the cold of the night, I rest an arm over it to try and settle it down."

        scene bg hosp_ext_ni
        show crowd_ni
        with locationchange

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.7)

        "When the airport comes into view, though, I realize this feeling as one I've felt before."

        "Not now… of all the times for this, please not now."

        "I take a gulp and soldier on regardless, pushing my body as far as it will go."

        "Sweat pours off me as I hurtle forward, my shoulder hitting someone's side and my mind suddenly flooding with emotions and memories."

        "I continue on without an apology. I have to keep moving now. If I stop, I'm not sure I could begin again, and even if I could it would all be for naught if I'm not in time."

        with vpunch

        "I hit another person, then another, offering little resistance to getting bounced about."

        "My feet feel numb. My arms are losing all feeling. My chest forces me to hunch over awkwardly, tightening ever more."

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.2)

        "That afternoon in the snow… that time when my life irreversibly changed… images of Iwanako and that damned letter flash over and over in my mind, the first love I'd lost thanks to my condition."

        "I can't let that happen again. I don't care what happens to me any more, I just need to see her one last time."

        "…There!"

        scene ev lilly_airport
        with flash

        "A sliver of yellow and white comes into view some distance down the road, her figure silhouetted by the lights emanating from the airport entrance."

        hi "Lilly! Lilly!"

        hi "Lilly! Stop, please! Lilly!"

        "Come on Lilly, I know your hearing's far beyond nor—"

        scene bg hosp_ext_ni:
            xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
            linear 0.1 rotate -6 zoom 1.2
        show crowd_ni:
            xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
            linear 0.1 rotate -6 zoom 1.2
        with vpunch

        play sound sfx_impact

        hi "Gah!"

        "My view suddenly spins out of control and ends up on the ground, my body haphazardly sprawled after hitting someone and stumbling over."

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.2)

        "Before I can assess the damage, an unbelievable pain ignites in my body. All my thoughts are blanked as I curl up and frantically clutch at my chest."

        mystery "Hey, are you okay? That was a really bad fall."

        "This pain… I can't…"

        hi "Argh… aaaaaargh!"

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.2)

        "Any sharp knock could do me in. Any overexertion. I thought I could overcome my limits this once…"

        mystery "Something's wrong with him!"

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.8)

        mystery "What's the matter, are…"

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.2)

        pause 0.7

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.8)

        "The voices of those gathering around me are gradually replaced by a loud ringing in my ears. By now I'm unable to move my head, my eyes turn upwards to see the mute moving of their lips."

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.8)

        pause 0.15

        play sound sfx_heartslow
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.8)

        play sound sfx_heartfast
        show heartattack alpha
        with Dissolve (0.1)

        hide heartattack alpha
        with Dissolve (0.8)

        pause 0.05

        play sound sfx_heartstop
        show heartattack alpha
        with Dissolve (0.1)

        stop ambient fadeout 0.3

        show heartattack residual
        with Dissolve (0.8)

        "Even as I clutch my chest, I realize I can't feel my fingers any more, nor my feet. It feels like my entire body is shutting down, starting from my extremities."

        scene ev lilly_airport_end:
            truecenter
            zoom 1.2 rotate -8
            easein 12.0 zoom 1.0 rotate 0
        with Fade(1.0, 0.5, 1.0)

        "With one last effort, I turn my head down the road towards the airport entrance that's casting its light over me."

        "Lilly is there, behind the crowd. Her head is tilted, but only just slightly."

        show passoutOP1

        "I can feel my vision dimming as I try to yell out, but nothing emerges from my mouth despite my best efforts. Slowly but surely, my vision begins to black out the scene before me."

        "So… this is how it ends."

        "I failed. I was so close, so very close, but at the very last moment my condition seized my chance at a new life and dragged me back."

        "Now I'm going to die, sprawled out just meters from an airport, with a crowd of babbling people surrounding me and with Lilly leaving for Scotland just a little distance ahead."

        hi "Li… lly…"

        stop music fadeout 4.0

        "That last word extinguishes the last of my energy. The world falls into a deep, inescapable blackness as every muscle in my body shuts down."

        "I'm sorry, Lilly."

        "I was too late."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .under_a_maudlin_sky:
        scene white
        with dissolve

        "…"

        "……"

        "………"

        "What's… going on…?"

        "As I slowly open my eyes, a bright, white light assaults my retinas."

        "For minutes I just lay where I am, mindlessly staring ahead while my scattered thoughts coalesce in my slowly waking mind."

        scene bg hosp_ceiling:
            alpha 0.0
            linear 5.0 alpha 1.0

        "Slowly but surely, the white begins to come into focus as a bare expanse begins to be drawn across my field of vision."

        "It's only when the light fixture comes into view that my mind clicks that this is the ceiling above me."

        scene bg hosp_room2
        with locationchange

        "Slowly levering myself up, I silently absorb through all my senses the details of the room I'm in."

        "The smell and taste of strong bleach hang in the air, lending the impression of a place just slightly too clean to be natural."

        "Inoffensive pale peach-colored walls, all perfectly painted without a crack, stain or imperfection. A single framed painting hangs on the wall, perfectly straightened. Like the walls, it's as boring and inoffensive as can be."

        "My attention's grabbed by the translucent curtain waving across my vision, my eyes following it to the open window it covers."

        "When I move my right arm to try to lift myself up and look through it, I feel the catheter dig in uncomfortably. It's only now, too, that I notice the cannula tubes winding around my cheeks and into my nose."

        "After some fidgeting, I settle for just looking around the corner of the window."

        scene ev lilly_hospitalwindow
        with whiteout

        "Beyond the thick leaves of several large trees, I can see the greenery below, backing out onto a field. A customary island of green on the outskirts of the city."

        "Judging by the sun outside, it's noon. Of which day, though, I'm not sure."

        "So… I'm in a hospital once again."

        "I let out a long, tired breath as I try to collect my scattered thoughts, my mind seemingly cast in a dozen directions all at once with as many emotions running through me."

        scene bg hosp_room2
        with locationchange

        "After slowly lying back down, I decide to start at the beginning; why I'm here."

        "I cast my mind back, but I can't work out a smooth recollection of what happened. The events of last night… or whichever night it was… come back more as a series of snapshots than any cohesive memory."

        scene bg school_dormhisao_ni_fb
        show origami_fb at center
        show noiseoverlay
        with flash

        "Lying on my bed looking at the origami bird."

        scene bg shizu_houseext_lights_fb
        show hideaki serious_up_fb at center
        show noiseoverlay
        with flash

        "Talking to Hideaki outside the Hakamichi residence."

        scene bg hosp_ext_fb
        show crowd_still1_fb at center
        show noiseoverlay
        with flash

        "Running down the street, passing pedestrians and bumping into more and more of them."

        scene bg hosp_ext_fb:
            xalign 0.5 yalign 0.52 rotate -6 zoom 1.2
        show crowd_still2_fb:
            xalign 0.5 yalign 0.52 rotate -6 zoom 1.2
        show noiseoverlay
        with flash

        "Falling."

        scene ev lilly_airport_end_fb
        show noiseoverlay
        with flash

        "Looking up at the searingly bright airport entrance, seeing Lilly's back as I lay on the ground…"

        "…"

        scene bg hosp_room2
        with fade

        "The silence of the private room suddenly feels overwhelming."

        play music music_rain fadein 2.0

        nvl clear
        nvl show dissolve

        n "{vspace=30}So that's it. I had my chance to correct my mistake, and I blew it."

        n "Whether I was at fault for neglecting my medication and disregarding to pace myself, or my body was for giving out so soon, it doesn't matter now."

        n "All that matters is that, once again, I'm alone."

        n "The pastel blue pillow yields with little resistance as I let myself fall back onto the bed, its starchy case, along with the starchy sheets, providing little comfort."

        n "Compared to the darkness of last night's events, the bright light of the room around me is striking. All it does, though, is emphasize how otherworldly places like this are."

        n "{vspace=30}Arrhythmia."

        n "{vspace=30}A strange word. A foreign, alien one. One that you don't want to be in the same room with."

        n "A rare condition. It causes the heart to act erratically and occasionally beat way too fast. It can be fatal."

        nvl clear

        n "{vspace=30}'It was a miracle that you were able to go on so long without anything happening,' they said."

        n "And then, it did. My condition had taken away everything; my old school was of no importance any more. My home was reduced to a faraway place. Both my friends and my first love simply stopped visiting after a length of time."

        n "I became cynical and embittered. Distant and subdued. In my defense, no person could avoid that after such a thing happening to them, but nonetheless I left the hospital as a very definitely changed person."

        n "Things changed. I made new friends in Hanako, Shizune and Misha. I found a new sense of 'home' in my dormitory, a new interest in science and the world around me, and I found a direction to my life that I had never felt before."

        n "{vspace=30}But I'd also discovered other things."

        n "The sense of isolation in Yamaku and its surrounds was not entirely unwelcome, the quiet giving a peace of mind I might not have found elsewhere, but it gave the area a feeling of being pushed out of the way, of being kept out of sight."

        nvl clear

        n "{vspace=60}People in the streets would sometimes glance awkwardly, or quickly turn their heads as they realized they were staring. Even if my condition wasn't visible, my uniform was."

        n "Even if it weren't, I was still different. I took seventeen pills a day, morning, midday and night. My scar, though hidden behind clothing, was still a permanent mark of my condition. And most of all, there was the very real possibility of death."

        n "A bad fall. An absentminded hard hit on the back. A simple sprint taken too far. Anything could have set my heart off, and several times I teetered on the edge of the abyss even with all the care I took of myself."

        n "{vspace=30}But that was fine. I could have lived with all that."

        n "Because there was one final thing I'd found, or rather refound, after entering Yamaku."

        n "{vspace=30}Which was once again snatched away before my eyes."

        nvl clear

        n "{vspace=30}It's only now that I realize just how delicate my newfound sense of happiness was. Everything depended on her, the linchpin of my life since I first entered Yamaku as a sullen, confused and aimless transfer student."

        n "Lilly Satou was the one person I could depend upon above all others, and who reciprocated the love that I felt for her. But I failed her, and only realized it all too late."

        n "I thought that I could just set my life up and continue that way forever, but the real world doesn't work like that. I finally realized the meaning of those words, only to be struck down as I confronted my failure to do so in time."

        n "{vspace=30}…"

        n "{vspace=30}The surroundings I'm in now are all too familiar. It's as if Yamaku was but a dream, and I'm still recovering from my first major heart attack."

        n "Maybe that's why I feel so tired. It feels almost as if I've lived the entire last few months of my life in the space of minutes."

        nvl hide dissolve
        nvl clear

        scene black
        with shuteye

        "The weight of my eyelids closes my eyes, my physical and mental exhaustion letting me offer no resistance."

        "Unintelligible mumbling from ahead of the bed stirs me out of my sleep."

        "With my eyes still closed, I can focus and make out someone, presumably a nurse, bidding farewell to a doctor."

        scene bg hosp_room2
        with openeye

        "As I open my eyes, I notice the door closing in my peripheral vision."

        "The doctor stands reading some notes off a clipboard held in his hand, carefully looking over the pages."

        "After consulting his obviously very important documents, he looks up and notices my gaze. It's now that I notice something slightly odd about his expression and general disposition, but I can't quite put my finger on it."

        "Doctor" "Ah, I see you're awake… Mr. Nakai."

        "His quick glance to my bed end, to verify my name, shows that his documents obviously didn't have it written on them."

        "Doctor" "I must admit this is a bit unfortunate; your parents visited just earlier while you were asleep. I could notify them you're awake now, if you'd like."

        hi "Um… thanks. That would be good."

        "I give a somewhat dazed reply, most likely the one he'd expect, before really thinking about what I'm saying."

        "Doctor" "Not a problem."

        "Doctor" "If you have any questions you'd like to ask, I'll be happy to answer them. That is, unless you'd prefer to rest; the anaesthetic's still going to be affecting you a bit, I'm afraid."

        "The anaesthetic… of course. That'd be why I felt so strange the first time I woke up."

        "I slowly shake my head, not wanting to dislodge any pipes or cause myself any more discomfort than necessary. The doctor politely puts down his clipboard in response."

        hi "I guess my main question is… what exactly happened?"

        "Doctor" "To put it simply, you've unfortunately had another heart attack. While not as severe as your first, you were very lucky it occurred so close to a hospital."

        "Doctor" "After being stabilized, you were taken to the operating room. What followed was keyhole surgery in order to insert a temporary pacemaker."

        "Doctor" "All in all, the incident happened two days ago, with emergency treatment being carried out very soon afterward. Since then, we've kept you under close observation while you were asleep."

        hi "Will I be all right? Are there any lasting problems?"

        "Doctor" "Compared to the procedure carried out for your first heart attack, this was relatively minor."

        "Doctor" "While you will have to undergo surgery once more in a few days' time to remove the pacemaker, assuming there are no complications, there should be no lasting implications."

        "He continues talking, the subject shifting to a repetition of facts about arrhythmia and my medications that I already know for the most part. I start to nod and feign interest, while my mind drifts."

        "I begin to think about how perfectly hung the inoffensive painting hanging on the wall behind his shoulder is, and how neat and sterile the surroundings are, even including the doctor himself."

        "Doctor" "If my mumbling bores you, you are quite welcome to say so, Mr. Nakai. Lord knows, I lose track of myself sometimes."

        "He gives a short chuckle at his self-deprecating joke as I grimace awkwardly, having been rather badly caught out."

        "The doctor's chuckle sounds different from that of the nurse at Yamaku though, come to think of it. As I ponder why, I realize why the man in front of me feels just that little bit 'off'."

        "His smile is neat and sterile. He delivers his little joke perfectly, with a customary inoffensive chuckle."

        "It is like, rather than talking to the man whose name is neatly printed on the nametag pinned to his lab coat, I'm merely interacting with an actor reading off a prerehearsed script, every action having been choreographed beforehand."

        "I suppose he has to be this way though, being a doctor."

        "He has to keep his neat and sterile smile when chatting to the girl with cancer slowly spreading through her body, when reassuring the woman who'll surely die from childbirth, and with every other terminally and critically ill patient."

        "That little bit of distance. That little bit of aloofness."

        "It makes me wonder if I've been too harsh, especially considering it's a disposition far from being adopted only by people in his profession."

        "After all, the one I loved kept that same distance from others herself."

        "Looking up to the doctor again, I realize I've been in thought with my head bowed for some time."

        "Doctor" "I understand you must still be tired. You've been through a lot, and as I mentioned before, the anaesthetic would still be affecting you."

        "Doctor" "If you don't mind, I'll let you get some rest and tell your parents you've woken up for you."

        hi "I think… that would be good. Thank you."

        stop music fadeout 6.0

        "He gives a curt nod before picking up his clipboard and making his way to the large white door in the corner of the room, closing it behind him with a thud."

        "In the end, I'm alone again."

        "Lilly's gone. Akira's gone. Hanako would be traveling, and even my parents have already left the hospital."

        "Four pale peach walls, one white ceiling, and a single open window to look out towards the world outside."

        "It's hard to think of the future when the past is crowded around you, claustrophobic in its neat, sterile, starchy, bleach-smelling grip."

        "Lost for what to do or focus on, I content myself with sleeping the time away as if this were all just another dream like Yamaku had been."

        scene black
        with dissolve

        if _in_replay:
            return

    label .under_a_bright_sky:
        scene white
        with dissolve

        "White."

        "A sterile, clean white for a sterile, clean room."

        $ renpy.music.set_volume(0.05, 0.0, channel="music")
        play music music_musicbox fadein 10.0

        show bg hosp_ceiling:
            alpha 0.0
            linear 5.0 alpha 1.0

        "My eyes open, and I simply stare at the ceiling for some time. It's about as interesting as the television would be, mounted in its metal rack hanging off the ceiling ahead of the bed."

        "Indeed, the television saw its entire use during the time my parents were here. Left on quietly as they waited for me to wake, it was about as banal as it had been the first time I'd ended up in the hospital."

        "Earlier today an attending nurse had offered to turn off the EKG's speakers. I refused simply because the sound is so entirely normal to me now."

        "It's almost comforting, in a way. The metronome-like regularity gives at least some feeling that time is moving, even in a place such as this."

        "After some time of listening to its beeping while I fully awaken, though, I realize there's another sound in the room."

        $ renpy.music.set_volume(0.1, 5.0, channel="music")

        "Concentrating all my efforts on listening, a task made rather easy by the lack of distractions, a tiny tinny melody can be heard."

        "Light and quiet, the music sounds almost fragile as it's dwarfed by the EKG's pulses."

        scene bg hosp_room2
        with locationchange

        "Tilting my head just slightly to the side in an effort to see the source of the melody without dislodging any of the sensors and pipes stuck onto me, I notice a little wooden box sitting on the nightstand next to the bed."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        show musicbox open:
            truecenter
            ypos 0.7 alpha 0.0
            easein 1.0 truecenter alpha 1.0

        pause 1.0

        "My mouth opens just slightly while I silently watch the tiny yellow metal drum slowly rotate inside, the little bumps on its surface gradually moving in and out of sight."

        "This music box… it's the one I gave…"

        show musicbox:
            easeout 1.0 ypos 0.7 alpha 0.0

        pause 1.0

        hide musicbox

        "The creaking of the door breaks me out of my reverie, my head and heart remaining still as my eyes turn to see who comes through."

        "Long tan skirt… peach off-the-shoulder sweater… pale, almost porcelain skin… blue clouded eyes and long, yellow hair…"

        show lilly basic_reminisce_cas at center
        with charaenter

        "All I can do is stare as Lilly slowly walks into the room, her fingers lightly running over the wall for orientation, and my mind comes to a shuddering halt."

        hi "L… Lilly…?"

        show lilly basic_oops_cas
        with charachange

        "She stops midstride, her entire body tensing."

        li "Hisao? Was that you?"

        "Her voice is quiet and pensive, echoing her expression."

        hi "I thought you were…"

        show lilly basic_sad_cas
        with charachange

        "Lilly takes one tentative step forward, then another, as if she were holding herself back."

        show lilly basic_sad_cas_close
        with characlose

        "Her control over her composure is for naught though, and she finally rushes over to where I lay as the last of her resistance falls."

        scene ev lilly_hospitalclosed at l_hosp_out
        with whiteout

        "I'm slightly taken aback when she grabs hold of me, hunching over as tears begin to fall from her cheeks, since only minutes ago I thought she was on the other side of the world. After a moment of hesitation, I rest my right hand on her soft shoulder."

        li "Hisao! Hisao!"

        "Lilly's body trembles as her tears blot the pale green sheets, her emotions flooding through her carefully maintained exterior."

        "With her face now closer, and made easier to see for her pale skin being lit by the sunlight from the window, I notice her cheeks being redder than they should be."

        hi "It's okay, Lilly. I'm okay. You don't need to—"

        scene ev lilly_hospital at l_hosp_out
        with charachangeev

        "She rights herself quickly, her crying forcefully stifled with both sadness and stubbornness remaining in her moistened eyes. Her prideful nature, always having been something to contend with, takes me off guard."

        li "Stop telling me not to worry about you, Hisao!"

        li "Just this once… let me cry…"

        "I'm caught speechless. She waits for a response, but her composure breaks again after a handful of seconds."

        scene ev lilly_hospitalclosed at l_hosp_out
        with charachangeev

        "I swallow hard to try and settle my own emotions while she weeps onto my bed, a strange mixture of relief and depression welling up."

        "Lilly's… here. She's really here. If I couldn't feel her skin under my hand, I'd hardly believe my own eyes. My efforts weren't for nothing; my body's attempt to take away everything that was important to me once again has been foiled."

        "But now… I don't feel as happy about it as I thought I would."

        "Seeing her here, crying like this over me… this is the one thing I'd wanted to avoid since coming to love her, no, even since leaving the hospital."

        hi "I'm sorry, Lilly. It's my fault I'm here; I shouldn't have tried to push myself so far."

        "I give a self-deprecating snort."

        hi "After months of keeping myself together so nobody'd worry over me, I went and did something like this. I guess I'm pretty dumb."

        scene bg hosp_room2
        show lilly basic_weaksmile_cas_close at center
        with whiteout

        "With a couple of sniffs and a long breath, Lilly manages to pull herself together and calm down a little."

        "Despite her red cheeks, moist eyes and the lines of her tears still visible, she delicately wears that weak smile she seemed to so often give."

        li "You needn't blame yourself. I heard later that it happened as you were running down the road after me, right?"

        hi "Still…"

        "She wipes her eyes with the back of her hand, returning more to her old self as the rush of emotions wears off."

        show lilly basic_reminisce_cas_close
        with charachange

        li "Why did you run after me, Hisao?"

        show lilly basic_concerned_cas_close
        with charachange

        "I move to respond, but notice her face tightening."

        li "Even after I'd said goodbye, and I'd left Yamaku Academy…"

        "She takes a moment to steady herself, her emotions almost bubbling up once again."

        hi "I just wanted to say that I'm sorry."

        show lilly basic_surprised_cas_close
        with charachange

        li "Sorry?"

        hi "For the times when I wasn't there when you needed me."

        hi "Until now, I thought you just being there would be enough. I only needed you by my side to make any day feel better."

        hi "Even if my body may be like this, I want to help you, Lilly; to be there when you need someone."

        show lilly basic_weaksmile_cas_close
        with charachange

        li "But you always were there, Hisao…"

        hi "Why did you want to go to Scotland, Lilly?"

        show lilly basic_sleepy_cas_close
        with charachange

        li "Why…? I told you before: because Akira was going, and because of my family's summons to their home."

        hi "Why didn't you say that you wanted to go?"

        show lilly basic_oops_cas_close
        with charachange

        li "I—"

        hi "I'm not stubborn often, but this one time I think I need to be. I want you to stay here, Lilly."

        hi "I want you to stay where everyone you know lives, and where all your dreams and ambitions were made. If you choose to stay, I'll never leave your side. I won't let you lose another person."

        hi "When I had my heart attack, I was snatched away from everyone and everywhere I knew. You showed me a new life after I came to Yamaku. I'd lost my past, but you showed me a future."

        hi "It's true that I haven't always been there for you. I'm unreliable, sometimes I lied, and I thought I'd come to understand you when I hadn't even understood myself."

        hi "Be that as it may, I want to give you a future as well. I want to be there for you, to share both your burdens and your happiness, just like I promised back in Hokkaido."

        hi "I want you to trust me. I know I had problems coming to put my trust in you, after losing so many people I'd known after my heart attack, but that's how I know that being unable to trust others can feel awful."

        hi "That's why I can't watch you just throw everything away like this. I never want you to go through what I did. I would do anything to stop that."

        show lilly basic_weaksmile_cas_close
        with charachange

        li "You can be quite steadfast when you want to be, can't you?"

        hi "As I said, it isn't often."

        "My weak smile drops, though, as the IV in my arm digs in a little. It's a harsh reminder of my tether to my condition."

        show lilly basic_concerned_cas_close
        with charachange

        "Lilly's face tenses as I let out a small gasp of pain, immediately making me wish I'd stifled it better. All I can do is sigh in defeat."

        hi "I tried to not let anyone worry over me for the entire time since I left the hospital, but I can't even stop the one person I love most from crying over me."

        hi "Even if I might finally be able to put my feelings into words, I feel pretty useless with a body like this."

        hi "Every time I tried to reach towards something, it was just snatched away, and even now things only turned out for the better due to luck."

        hi "I guess that's something else I should apologize for. All I can ever do is make you worry. Even now, there's very little chance I'll live anywhere near a full life."

        "The feeling of Lilly's warm, soft hand moving over my left cheek makes me lift my head up, her smile gentle and warm as she touches me."

        show lilly basic_smileclosed_cas_close
        with charachange

        li "I think that is something very natural for you to say. You were always so sincere and self-conscious."

        show lilly basic_smile_cas_close
        with charachange

        li "You were also reserved and mild-mannered, and patient to a fault with Hanako, yet curious about everything and everyone."

        show lilly basic_weaksmile_cas_close
        with charachange

        li "When I said I missed you while I was with my family, I wasn't lying or exaggerating. The thought of you was never far from my mind, and helped me through that time."

        show lilly basic_reminisce_cas_close
        with charachange

        li "That's why I was so confused about what to do when my family summoned me. Even after I thought I had made my decision, you tried your hardest to challenge me about it."

        show lilly basic_weaksmile_cas_close
        with charachange

        li "I didn't confess to you out of pity or believing you were somehow different from what you are. I confessed because I never want to lose you, and want you to always be a part of my life, no matter what might change."

        show lilly basic_smileclosed_cas_close
        with charachange

        li "You are a very beautiful person, Hisao. Your heart changes none of that, so please, don't apologize for yourself any more."

        "For a long time, silence reigns in the room."

        "I'm not really sure what this newly born feeling inside of me is, but it pales into insignificance as I wordlessly gaze at Lilly's smiling face, warm and gentle as it has always been."

        "It's only as her thumb crosses my cheek, wiping away a single drop of moisture, that I realize this is all I've ever wanted."

        "For what feels like the first time, I give an earnest, wide smile. As Lilly feels it against her palm, she returns the gesture."

        "More time passes before either of us says a word, neither of us needing speech to communicate our feelings to each other."

        hi "I know I can't promise you that I'll always be around, or that we'll be together forever."

        "With some difficulty I slowly lift my hand, placing it on her pale shoulder."

        hi "But… I think I can at least take you to next year's Tanabata festival, to make up for making you miss this year's."

        show lilly basic_emb_cas_close
        with charachange

        "Lilly's expression is one of surprise, though I can't say I blame her."

        li "You… remembered that?"

        hi "I've got a pretty good memory. Sometimes."

        show lilly basic_giggle_cas_close
        with charachange

        "She raises her head a little and takes her hand from my cheek, giving a small, amused giggle. I smile absentmindedly at how earnest it is, almost girlish in its lightness."

        show lilly basic_cheerful_cas
        with charadistant

        "Still smiling warmly, she collects herself and stands upright with a hand resting on my chest."

        "It feels like I'm seeing her for the first time, the sun from the window glowing behind her just as it did when I first walked into that room where she was drinking tea."

        show lilly basic_smile_cas
        with charachange

        li "Very well then. Shall we make it a promise between the both of us to go to next year's Tanabata together?"

        "Even if she can't see me doing so, I nod approvingly."

        hi "I promise."

        show lilly basic_smileclosed_cas
        with charachange

        li "I promise."

        stop music fadeout 4.0

        if _in_replay:
            return

    label .forwards:
        play ambient sfx_parkambience fadein 6.0

        scene bg lilly_hilltop
        with Dissolve(3.0)

        play music music_lilly fadein 5.0

        "Akira, Lilly and I silently sit on the grassy embankment high above the local town, the breeze gently blowing through the cloudless sky."

        "We may be just a few minutes' walk from town, on a hill just outside its limits, but the view is entirely unexpected."

        show lilly basic_smileclosed_cas_close:
            left
            ypos 1.1
        with charaenter

        "Lilly sits beside me, her eyes closed, as the gentle breeze flows through her hair."

        li "This is a nice area."

        hi "Yeah. I never knew a place like this was anywhere near Yamaku."

        show akira basic_ending_close:
            right
            ypos 1.1
        with charaenter

        aki "And I had to be the one to find it, of course."

        "Akira's grin is genuine, but her tone is slightly different from her usual carefree nature."

        show akira basic_smile_close
        with charachange

        aki "It's good that you're outta the hospital though, Hisao."

        hi "Nobody's more glad than I am. I can't stand hospitals."

        aki "So, you two going back to the school tomorrow?"

        call screen doublespeak(hi, _("Yup."), li, _("Yup."))

        show akira basic_ending_close
        with charachange

        "Akira chuckles in amusement before looking back out to the town below, the trees between the buildings swaying in the wind."

        hi "Pity we couldn't go up north for the summer holidays, or get to Tanabata."

        show lilly basic_weaksmile_cas_close
        with charachange

        li "I wouldn't worry, there's always next time."

        show akira basic_smile_close
        with charachange

        aki "You'll be graduating before the next summer vacation, won't ya?"

        hi "Yeah. There'll still be college after that, mind."

        aki "Going to the same one?"

        show lilly basic_smile_cas_close
        with charachange

        li "Likely. We both have high enough scores to meet the entry requirements."

        hi "You sound so sure…"

        show lilly basic_cheerful_cas_close
        with charachange

        li "Don't worry, you're better than I in most subjects."

        hi "I guess we'll work it out in due time."

        show akira basic_laugh_close
        with charachange

        aki "That's the way. Just enjoy yourselves in Yamaku while you're there."

        show lilly basic_weaksmile_cas_close
        with charachange

        "Lilly gives a sad sigh at the distinction made between Akira and the two of us."

        show lilly basic_reminisce_cas_close
        with charachange

        li "Do you really need to go back to Scotland?"

        show akira basic_resigned_close
        with charachange

        aki "Yeah. The folks are already out for my blood as it is."

        hi "You weren't meant to stay this long?"

        show akira basic_ending_close
        with charachange

        "She gives her trademark wide grin."

        aki "Setting my boyfriend up with a passport took some time."

        hi "You're taking him with you?"

        show akira basic_smile_close
        with charachange

        aki "Just for a while at first. He's a surprisingly worldly guy, so I think he'll do just fine."

        show akira basic_lost_close
        with charachange

        "Akira gives an amused snort."

        aki "If our father had his way, I'd have gone a long while ago."

        show akira basic_laugh_close
        with charachange

        aki "I just couldn't pass up an excuse to stay with my favorite little sister a little while longer though."

        show lilly basic_smileclosed_cas_close
        with charachange

        "She leans right and gives Lilly a tight playful hug, cheering her up considerably."

        li "It's nice to be with you one last time, though."

        hi "For what it's worth, I'm in the same boat."

        show akira basic_smile_close
        with charachange

        aki "Heh, thanks you two. I'll try and come back sometime, don't worry."

        show lilly basic_reminisce_cas_close
        with charachange

        li "It's a shame that the business keeps you so busy."

        show akira basic_lost_close
        with charachange

        aki "The place won't run itself, I'm afraid, and I think it's going to be just the same over there."

        show akira basic_smile_close
        with charachange

        aki "Considering that, I'd better get going."

        hi "Have fun over there, Akira."

        show akira basic_laugh_close
        with charachange

        aki "Haha, will do."

        show akira basic_smile_close at right
        with charamovechangefaster

        "With a slight grunt, she lifts herself with her hands and stands up, dusting herself off as she does so."

        show akira basic_lost_close
        with charachange

        aki "Well, I'd better be off. The plane won't wait for me, after all."

        "She has a certain unusual wistfulness in the tone of her voice, her eyes firmly planted on her sister."

        show lilly basic_weaksmile_cas_close
        with charachange

        li "I'll be okay, Akira."

        show akira basic_resigned_close
        with charachange

        aki "Yeah, I know."

        show lilly basic_smileclosed_cas_close
        with charachange

        li "Come now, it isn't that bad. You'll be able to see us again soon."

        "It is strange to have Lilly reassuring a doubting Akira for once. She really has changed."

        show lilly basic_smile_cas_close
        with charachange

        li "Goodbye, Akira."

        hi "'Bye."

        show akira basic_smile_close
        with charachange

        "For a second, the dark-clad figure looks down at the both of us, smiling widely. Perhaps more widely than I've ever seen her do before."

        show akira basic_boo at tworight
        with charadistant

        "She lets out a long, slightly wavering breath to steady herself before leaving, but eventually slips her hand in her pocket and turns on her heel."

        "And with that she walks away, one hand held in the air as she goes."

        show akira basic_ending
        with charachange

        aki "Seeya later, you two!"

        hide akira
        with charaexit

        "A jazz tune with no beat, melody or direction to the very end."

        show bg at bgright
        show lilly basic_smileclosed_cas_close at center
        with charamovechangefaster

        "After a few moments of sitting silently, Lilly and I pick ourselves up and dust ourselves off."

        "Turning towards her with a broad smile, I hold out my hand."

        hi "Shall we be off, then?"

        "She takes my hand in hers, with a gentle nod and a smile as beautiful and warm as ever."

        show lilly basic_cheerful_cas_close
        with charachange

        li "Indeed we shall, Hisao."

        scene unlock_ev lilly_goodend
        show evbg lilly_goodend:
            truecenter
            zoom 3.0
            1.0
            linear 0.5 zoom 0.9
            easein 12.0 zoom 0.8
        show evfg lilly_goodend:
            truecenter
            zoom 6.0
            1.0
            linear 0.5 zoom 1.2
            easein 12.0 zoom 0.8
        with whiteout

        "As we set off towards the school, that wonderful smile engraves itself onto my memory. That wonderful smile that we both share."

        "Our pasts may be scattered and at times overshadowed by sadness, but they're also an irrevocable part of our lives and personalities. Even if I could change a single thing, I wouldn't, because my past was what led me here."

        "That's why, even with all that's happened to us before, and all that may well befall us… together, we'll keep walking forwards."

        "Forwards… towards the future. Our future."

        stop ambient fadeout 2.0
        stop music fadeout 2.0

        scene black
        with Dissolve(1.0)

        pause 1.0

        if _in_replay:
            return

    return

label a4lc1o1:
    "The memory of that single letter Iwanako sent me comes back to my mind."

    hi "I never saw her again, but after I was sent to Yamaku… she wrote me one letter."

    "Lilly's face shows an expression I know well. I've piqued her interest. I'd be slightly offended that it's simply a matter of curiosity for her, but she's never been very good at masking her reactions."

    hi "In hindsight, it really didn't say much. What was going on in my old class, how she was faring, and, almost as an afterthought, that it was probably best for the both of us that we don't see each other again."

    hi "After reading it, I ended up reassessing a lot of things I thought I'd managed to work out. For the most part, that letter reminded me that the world around me was still moving, and just how much I'd become isolated from it."

    hi "And… I guess it also reminded me of what I'd lost."

    show lilly basic_emb_che_close
    with charachange

    "She gives the information some thought before her face lights up in realization. No doubt she's worked out that it was this letter which had contributed to my angst during that lunch on the rooftop."

    "It's a rare sight to see Lilly quite so lost for words, her entire persona is a little deflated from her earlier rapt interest. As charismatic as she is, in the end that isn't any replacement for life nor relationship experience."

    show lilly basic_reminisce_che_close
    with charachange

    li "Perhaps… it is better she sent it than not."

    hi "How's that?"

    show lilly basic_weaksmile_che_close
    with charachange

    li "It can be difficult to work out how best to communicate with those you haven't met in a long time. All the more so, considering your separate situations."

    li "Instead of doing what was easiest, she built up the courage to talk to you one last time; not only for her sake but, from how it sounds, for yours as well."

    hi "Maybe. I don't hate her for it, not that I really ever did, but… I don't know."

    "Probably a more noncommittal answer than I should give, but it isn't without cause. I've never looked at the situation from Iwanako's perspective like that before."

    return

label a4lc1o2:
    "I really don't want to bring up Iwanako any more than necessary. This date is, after all, for me and Lilly. I don't want to think about a previous relationship at a time like this."

    hi "No, that was the last I saw of her. We never talked again, either."

    return
