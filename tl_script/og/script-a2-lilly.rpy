label en_L1:

window hide None

scene black onlayer master
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao onlayer master
with openeye

window show

"I wake to the annoying din of my alarm clock, its bright red numerals lighting up my face."

play music music_dreamy fadein 2.0

"It's the same alarm clock I had at home, one of the few remaining artifacts from my days before coming to Yamaku. I'd hoped that using it would help ease my transition into this new life."

"No such luck, though."

"Groggily dragging myself out of bed, I wipe the sleep out of my eyes, then reach over to my desk. I open a couple of the bottles of medication strewn across it, and swallow a few pills dry."

"By now, the process is starting to become automatic - something I should be glad for, given their purpose."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene bg school_dormbathroom onlayer master
with locationskip

"Feeling much more awake than before, I wander into the bathroom."

play ambient sfx_shower fadein 8.0

show steam onlayer master
with charaenter

"While the shower warms up, my mind begins to wander as my new daily routine begins once again."

"The bright colors of the fireworks fill my mind, as do the two girls with whom I spent my time watching them. It feels strange to be moved so much by people I know so little about."

"Then again, I suppose these aren't normal circumstances. At least I have someone to talk to, now, aside from my schoolmate next door."

stop ambient fadeout 2.0

hide steam onlayer master
with charaexit

"With the time left before school begins today waning, I begin to get ready for class."

$ renpy.music.set_volume(1.0, 3.0, channel="music")

scene bg school_scienceroom onlayer master
with shorttimeskip

"Walking through the door into the classroom, I notice that I'm still somewhat early. I see about five or six students milling around, most of them looking as if they'd rather be still in bed."

"It's at times like this that I appreciate being a morning person. That said, two students in particular seem just as perky as always."

hi "Hi Shizune, hi Misha."

show shizu behind_blank onlayer master at tworight
show misha perky_smile onlayer master at twoleft
with charaenter

"I suddenly realize that my greeting would be lost on the former, so I quickly follow it up with a wave. She doesn't seem overly bothered."

"Or interested, for that matter."

show shizu basic_normal onlayer master
with charachange

shi "…"

show misha hips_grin onlayer master
with charachange

mi "Hello, Hicchan~! Are you feeling well?"

"I can only assume her greeting comes from Shizune. It's hard to tell if she's speaking as herself or Shizune, sometimes."

hi "Better than most everyone else, I guess. You two seem bright and chipper."

show misha sign_smile onlayer master
with charachange

show misha perky_smile onlayer master
show shizu basic_frown onlayer master
with charachange

"Misha signs this back to Shizune as I say it, eliciting a somewhat terse answer, if her sharp and rapid arm movements are any indication."

"Considering that these two made such a big deal out of the festival preparations, I probably should've chosen my words more carefully."

show shizu behind_frown onlayer master
with charachange

shi "…!"

show misha hips_grin onlayer master
with charachange

mi "Since you're a new student, we've been cutting you some slack. Please don't expect this kind of task-dodging to be allowed in the future."

"Misha looks as if she's about to add her own comment, but quickly goes back to interpreting as Shizune continues, unabated."

show shizu basic_frown onlayer master
show misha sign_smile onlayer master
with charachange

mi "While your contribution to class 3-2's stall is appreciated—"

"Huh. Word sure got around quickly. That, or these two have their fingers on the pulse of the school."

show misha hips_frown onlayer master
with charachange

mi "—we would prefer your efforts to be focused on the task at hand. Namely, your own class."

"As much as I hate to admit it, they do have a point. Before I can respond, though, Shizune adds something more, which draws a smile from Misha."

show shizu behind_blank onlayer master
with charachange

shi "…"

show misha perky_smile onlayer master
with charachange

mi "Did you enjoy the festival, then~?"

"Lecture over, I guess."

hi "Yeah, it was good. Did you two enjoy it?"

show shizu behind_smile onlayer master
show misha hips_grin onlayer master
with charachange

"Shizune gives a short nod as Misha grins and bounces her head up and down. The contrast, side-by-side, is amusing."

"Out of the corner of my eye, I notice more students starting to trickle into the classroom. A quick glance at my watch confirms that they're a few minutes late."

show hanako emb_downtimid onlayer master at offscreenright
with None

show misha hips_grin onlayer master at left
show shizu behind_smile onlayer master at Transform(xpos=0.48)
show hanako emb_downsmile onlayer master at Transform(xpos=1.0, xanchor=0.7)
show bg school_scienceroom onlayer master at bgleft
with charamove

"I look over to Hanako's seat and realize that she's already there, and contentedly reading a book. It makes me wonder just how long she's been there without me noticing."

show misha hips_grin onlayer master:
    ease 1.0 xpos 0.2
show shizu behind_smile onlayer master:
    ease 1.0 tworight
show hanako emb_downsmile onlayer master:
    ease 1.0 offscreenright
show bg school_scienceroom onlayer master:
    ease 1.0 center
with None

hide misha onlayer master
hide shizu onlayer master
hide hanako onlayer master
with Dissolve(1.0)

"With heavy footsteps coming up the hallway signaling Mutou's arrival, our idle talking comes to an end and I take my seat next to Misha."

"As the door slides open, he strides through with a ponderous gait. His posture is even worse than usual, and his eyes are barely staying open. I guess my quip to Lilly and Hanako about the staff was misplaced."

play ambient sfx_paperruffling

"Everyone opens their books as he reaches his desk, and the first class of the new week begins."

stop music fadeout 3.0
stop ambient fadeout 0.5

with shorttimeskip

play sound sfx_normalbell

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

"I rub my eyes as the lunch bell rings out, glad for the temporary reprieve from work."

show lilly basic_smileclosed onlayer master at offscreenleft
with None

show bg school_scienceroom onlayer master at bgright
show lilly cane_smileclosed onlayer master at Transform(xanchor=0.2)
with charamove

"I'm entirely unsurprised when I look over to the door and see Lilly standing there, cane in hand, patiently waiting for Hanako."

"Considering her acceptance of my request to join them yesterday, I decide to spend my lunchtime with them rather than eat alone."

show hanako emb_smile onlayer master at Alphain(0.5), Slide(0.5,0.5,0.4,0.5,0.5)
with Pause(0.5)

hide hanako onlayer master
hide lilly onlayer master
with charaexit

"Hanako moves surprisingly fast to meet her companion, and the two enter the hallway before I can catch up."

stop ambient fadeout 1.0

scene bg school_hallway3 onlayer master
show lilly back_listen onlayer master at twoleft
show lillyprop back_cane onlayer master at twoleft
show hanako emb_downsmile onlayer master at tworight
with locationchange

show hanako def_shock onlayer master
with vpunch

"Lilly's head turns slightly, registering the sound of footsteps behind her. As Hanako notices and follows her lead, she almost jumps in surprise."

show hanako defarms_strain onlayer master
with charachange

ha "Hi… Hisao?"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play music music_normal fadein 2.0

show hanako emb_blushtimid onlayer master
with charachange

ha "I mean… um… hello, Hisao…"

hi "Hi. Sorry if I startled you."

show lilly cane_smile onlayer master
hide lillyprop onlayer master
with charachange

"Lilly turns to greet me, helped in her orientation by Hanako."

show lilly cane_smileclosed onlayer master
with charachange

li "Good afternoon, Hisao. Are you joining us?"

hi "If it's no trouble. There's not much else to do, really."

show lilly cane_smile onlayer master
with charachange

"Lilly gives a small nod, as if to silently brush away any idea that it would be troubling in the least."

scene bg school_staircase2 onlayer master
with locationchange

with Pause(0.3)

scene bg school_hallway2 onlayer master
with locationchange

"We descend one set of stairs and walk down the hallway to the usual room, our pace somewhat quicker than usual thanks to Lilly using Hanako for direction, rather than her cane and the railings."

scene bg school_miyagi onlayer master
with locationchange

"As expected, it's deserted. The sounds of the other clubs can only barely be heard as sunlight streams into the room from outside."

"Looking around the room, I notice a couple of empty easels propped up against a wall that I don't think were there before. The art club must use this room as extra storage."

show hanako emb_smile onlayer master
with charaenter

ha "Should I get the chess set out?"

"Hanako's voice seems less tense when she's directly addressing Lilly."

show hanako emb_smile onlayer master at tworight
show bg school_miyagi onlayer master at bgright
with charamove

show lilly cane_weaksmile onlayer master at twoleft
with charaenter

li "Yes. I'll make tea while you sort the pieces."

hi "Ah, I can do that for you, if you'd like."

show lilly cane_surprised onlayer master
with charachange

with Pause(0.3)

show lilly cane_planned onlayer master
with charachange

"She ponders the offer for a moment before smiling, confirming that I've made the right choice. Her face is remarkably easy to read."

show lilly cane_satisfied onlayer master
with charachange

li "Very well. Thank you."

show lilly cane_satisfied onlayer master:
    ease 0.5 ypos 1.3
    "lilly basic_cheerful" with Dissolve(0.5, alpha=True)
    ease 0.5 ypos 1.0
with Pause(1.0)

hide lilly onlayer master
hide hanako onlayer master
with charaexit

"She slides her retracted cane into the handle of her bag and sets it against one of the table legs, before taking a seat opposite Hanako."

"As I prepare tea for the three of us, I can hear the small wooden pieces being set on the board. I wonder how good Lilly is at chess, given her circumstances."

"By the time I place the steaming teacups onto the table, Lilly and Hanako have already moved their first pieces as they nibble on sandwiches and rice balls from their respective bags."

$ renpy.music.set_volume(0.5, 2.0, channel="music")

show chessboard onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"I note that the chessboard they're using has holes in the middle of each square and pegs on the bottom of the pieces, and has each dark square slightly raised."

"Watching Lilly's fingers skating over the board, tracing out the positions of the pieces, makes me marvel a little at the simple ingenuity of the design. It must be specifically made for blind players."

$ renpy.music.set_volume(1.0, 5.0, channel="music")

show chessboard onlayer master:
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide chessboard onlayer master
with None

hi "Here you go."

scene bg tearoom_everyone_noon onlayer master
show tearoom_hanae happy onlayer master
show tearoom_lillye smileclosed onlayer master
show tearoom_hisaoe hsmile onlayer master
show tearoom_chess onlayer master
with locationskip

"Hanako gives a small nod as I put down the cup next to her side of the board. Lilly's hand ventures sideways slightly, so I gently place the cup touching the tips of her fingers; a gesture she seems to appreciate."

show tearoom_hisaoe outside onlayer master
with charachange

"I finally take a seat and silently sip my tea as the two play. The contrast in their appearances while playing is interesting to watch."

show tearoom_hanae open onlayer master
with charachange

"Hanako looks closely at the board, her face one of focused concentration. Lilly, on the other hand, keeps her head level and maintains her calm neutrality."

"Lilly's gentle voice addresses both of us as she continues to play."

show tearoom_lillye smile onlayer master
with charachange

li "How was class, now that the festival's over?"

show tearoom_hanae shy onlayer master
show tearoom_hisaoe hthink onlayer master
with charachange

"I look to Hanako to see whether she'll answer first, but see that she's doing the same."

show tearoom_hisaoe sigh onlayer master
with charachange

hi "Not… great. Half the class seemed to be dozing off, even including the teacher. Not to mention a test on top of all that."

show tearoom_hanae happy onlayer master
with charachange

"Hanako quietly adds her own agreement with this."

show tearoom_lillye ara onlayer master
with charachange

li "I could imagine that being a bit difficult for you, being a transfer student."

show tearoom_hisaoe lsmile onlayer master
with charachange

hi "Well, I think I did fine. Other than the shock of a test coming so early, science is probably my best subject."

show tearoom_hisaoe hsmile onlayer master
with charachange

hi "How'd you do, Hanako?"

show tearoom_hanae open onlayer master
with charachange

ha "Me? Ah… okay… I guess…"

"Hanako's too sincere to be able to pull off lying very well. That much is obvious."

show tearoom_lillye thinking onlayer master
with charachange

"Lilly's smile slips very slightly. From her reaction, Hanako mustn't be skilled enough at academics to do very well without preparation."

show tearoom_hisaoe lsmile onlayer master
with charachange

hi "How did your class handle it, Lilly?"

show tearoom_lillye giggle onlayer master
with charachange

li "It went surprisingly well, actually. Only one student was absent, which was better than what the teacher expected."

show tearoom_hanae shy onlayer master
show tearoom_lillye smileclosed onlayer master
with charachange

"With the topic all but run dry, the two concentrate on their chess game once again."

show tearoom_hisaoe relief onlayer master
with charachange

"I can't say I've ever liked the idea of chess as a spectator sport, but given its unique nature, for once I'm rapt in watching the game unfold."

show tearoom_hisaoe outside onlayer master
show tearoom_hanae sad onlayer master
with shorttimeskip

"As time wears on, both of them demonstrate decent skill at playing the game. Having captured two more pawns than Hanako, Lilly has the upper hand, but only slightly."

show tearoom_hanae open onlayer master
show tearoom_hisaoe hunsure onlayer master
with charachange

"…until Hanako makes a strange move with her queen. Seizing upon this lapse in judgment, Lilly takes the piece with her knight."

show tearoom_hanae shy onlayer master
with charachange

"Without hesitation, Hanako moves a pawn to take Lilly's rook on the opposite side of the board, and promotes it to queen."

show tearoom_lillye thinking onlayer master
show tearoom_hisaoe lunsure onlayer master
with charachange

"Lilly's face falters as her fingers move over the pieces and she realizes that she just fell to Hanako's trap. It's a little distracting to have the board traced out after each move, even if it's out of necessity."

"Judging by Hanako's lack of reaction, she must be used to this. She and Lilly must have played at least a few games of chess against each other, after all."

ha "Check."

show tearoom_hisaoe hsmile onlayer master
with charachange

hi "That's not bad at all. Nice, Hanako."

show tearoom_hanae happy onlayer master
with charachange

"The compliment causes her to flower into a surprised blush."

ha "Th-thank you. I didn't… think it would work."

show tearoom_hisaoe lsmile onlayer master
with charachange

"I look over to Lilly, her fingers having just finished tracing out the position of her remaining pieces in an attempt to extricate her king from this bind."

li "I think this is checkmate…"

show tearoom_hisaoe loops onlayer master
with charachange

hi "Hmm?"

show tearoom_hisaoe relief onlayer master
with charachange

"I take another look at the board to confirm."

"Sure enough, her king has nowhere to escape without being threatened by another piece. My earlier question as to which of them is better at this has just been answered."

show tearoom_hisaoe sigh onlayer master
with charachange

hi "So it is."

show tearoom_lillye weaksmile onlayer master
with charachange

"Lilly gives a small sigh as Hanako smiles. From their reactions, this seems like a fairly usual result."

show tearoom_hisaoe lsmile onlayer master
with charachange

hi "How long have you two been playing?"

show tearoom_hisaoe hsmile onlayer master
show tearoom_hanae sad onlayer master

with charachange

ha "Since… I was young."

show tearoom_lillye smileclosed onlayer master
show tearoom_hisaoe lsmile onlayer master
with charachange

"Lilly nods at Hanako's brief answer."

show tearoom_lillye smile onlayer master
with charachange

li "Hanako taught me how to play soon after I met her. I can beat her every now and then… but that's a rarity. I don't seem to have the right mindset for it."

"If Lilly came to Yamaku at the start of high school, and met Hanako when she moved to the dorms, that'd mean she's only been playing for about one year."

"After seeing Hanako's level of play, I'm not too surprised Lilly has trouble beating her."

show tearoom_hanae happy onlayer master
show tearoom_hisaoe hthink onlayer master
with charachange

ha "But… she's better at languages than I am, so…"

show tearoom_lillye ara onlayer master
show tearoom_hisaoe lthink onlayer master
with charachange

"Lilly gives an appreciative, if slightly amused, smile at Hanako's quick reversal of her compliment."

show tearoom_lillye weaksmile onlayer master
with charachange

li "Well, that's how it is."

stop music fadeout 3.0
play sound sfx_warningbell

"Much to everyone's surprise, the bell suddenly rings, heralding an end to the lunch break."

show tearoom_lillye thinking onlayer master
show tearoom_hisaoe loops onlayer master
with charachange

li "Hmm, that game lasted longer than I thought it did."

hi "Same. I guess we'd better get back to class."

show tearoom_hanae shy onlayer master
show tearoom_lillye weaksmile onlayer master
show tearoom_hisaoe thinkclosed onlayer master
with charachange

"Hanako's already in the middle of packing up, so I take Lilly's bag and offer it to her. To my surprise, she takes it and nods, but then places it back down on the table."

play music music_daily fadein 2.0

scene bg school_miyagi onlayer master
show lilly basic_smileclosed onlayer master at twoleft
show hanako basic_normal onlayer master at tworight
with locationskip

li "Hisao, may I make a request?"

hi "Sure, go ahead."

show lilly basic_smile onlayer master at twoleft
with charachange

li "Would you mind if I were to quickly feel your face?"

hi "Oh, uh… no, go ahead. I don't mind."

"The question takes me severely off guard, but once I regain my composure it seems sensible enough. So far Lilly's had no idea what I actually look like, and this would be her only way to find out."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

show ev lilly_touch_uni onlayer master
with GenericWhiteout(0.5,0.1,3.0)

"Lilly raises her right hand, which I take in mine and guide to my face before letting go."

"The room is entirely silent as Lilly's hand moves over and around my features, from my chin, to my cheeks, to everywhere else."

"I expected this to feel a lot more disquieting than it does. I suppose that's because the action is entirely a matter of practicality, being functionally no different to simply looking at someone's face."

"Her hand is soft, but what takes me by surprise is the length of her fingers, not to mention how sure even the slightest of her movements are. I have no doubt that her level of tactile feeling would be far beyond mine."

"Her hand briefly runs once through my hair before retreating. I'm sure that every inch of my face has been committed to her memory. It's only now, too, that I realize Hanako has been silently watching the entire time."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_miyagi onlayer master
show hanako basic_distant onlayer master at tworight
show lilly basic_weaksmile_close onlayer master at twoleft
with whiteout

li "Thank you for letting me do that, Hisao."

show lilly basic_smile_close onlayer master at twoleft
with charachange

li "And if I might add, I think you are quite handsome."

"I blush a little at her remark, before raising a questioning eyebrow."

hi "But if you can't see, how…"

show lilly basic_pout_close onlayer master at twoleft
with charachange

li "Just because I can't see, that doesn't mean I don't have my own preferences."

show hanako emb_timid onlayer master at tworight
with charachange

ha "Um, we'd better go now…"

hi "Yeah, that's a good point. I guess we'll see you later then, Lilly."

scene bg school_hallway2 onlayer master
show lilly basic_smile onlayer master at twoleft
show hanako emb_smile onlayer master at tworight
with locationskip

"Walking through the hallways back to our classrooms, I notice that Hanako seems quieter than before, but also more comfortable."

"Lilly, her hand on Hanako's shoulder, seems to pick up on her assured pace as well, smiling as they walk."

"If I could spend the rest of my time at Yamaku like this, I don't think it'd be so bad. All that's needed for joy are small exchanges of happiness, after all."

scene bg school_scienceroom onlayer master
with locationskip

play sound sfx_rumble

"As I reach my desk and set my bag beside it, I realize something. Or rather, my stomach does."

"I was so busy with those two, I forgot to buy lunch…"

stop music fadeout 2.0

scene black onlayer master
with dissolve



label en_L2:

scene bg school_dormhisao onlayer master
with locationchange

"Saturday. My second most favorite day of the week."

"This is almost entirely due to the fact that it is the day with the second least amount of school, with class ending at the beginning of lunch."

scene bg school_dormhallway onlayer master
with locationchange

"I open my door confidently, myself being more than confident of being able to get enjoyment out of the fine weather and shorter class length."

scene bg school_dormhallground onlayer master
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_footsteps_hard

"I confidently stride down the hallway and down the stairs to the lobby of the male dorms."

$ renpy.music.set_volume(0.6, 4.0, channel="ambient")

"I confidently look behind me to see whose footsteps are approaching."

$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

"I… lose my confidence in this day being enjoyable."

stop ambient
play music music_kenji fadein 0.5

show kenji happy onlayer master:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter

ke "Hey man. Sup?"

hi "Not much I guess, just looking forward to the afternoon. You?"

show kenji happy_close onlayer master at center
with characlose

"He wraps an arm around my slumped shoulders far too comfortably. Something's up."

show kenji neutral_close onlayer master
with charachange

ke "Let's step outside, shall we?"

hi "I was just about to, before you stopped me."

show kenji tsun_close onlayer master
with charachange

scene bg school_dormext_full onlayer master
with locationchange

"He doesn't take my reaction to his theatrics well. Ignoring him, I walk outside and start down the steps."

"It doesn't take too long for him to catch up with me again. I wonder if he wants money, or to rant about another conspiracy. Maybe both."

show kenji tsun onlayer master:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter

ke "I've got a bone to pick with you."

hi "Uh huh."

ke "It's about that blonde. You know who I'm talking about."

"Conspiracy it is. For a moment I contemplate feigning ignorance, but realize this will go quicker if I just let him get it all out."

hi "Lilly? The one from your class?"

show kenji rage onlayer master at center
with vpunch

ke "You're on first name terms with her?!"

"He looks positively shocked at this development. Did he not expect me to be able to answer?"

show kenji tsun onlayer master
with charachange

"He gathers himself and coughs into his fist. Dramatically, like everything he does."

ke "Well, never mind that. I'm here to warn you. You know. Man to man."

hi "Warn me about what? Lilly?"

ke "Yeah. You don't know her, man."

"It's mostly true. I've only known her and Hanako for less than two weeks, and even then we've just been exchanging banal chatter about school as we while away lunch."

hi "I'm pretty sure you don't either."

ke "That's not the point. You're the one spending inordinate amounts of time with her."

"It distresses me that someone like Kenji, who's probably as far out of the loop as one could possibly get, knows about such a trivial fact as who I choose to befriend."

"Then again… I am a transfer student, and she's not only the representative of their class, but also a tall blonde."

"Maybe I should appreciate this ranting as a warning that the rumor mill exists in this school, and that I'm firmly within it."

hi "It's just lunch. Nothing special."

show kenji neutral onlayer master
with charachange

ke "Look, man, under the bridge. See this bridge? You're under it. A man's gotta do what a man's gotta do to get intel."

show kenji tsun onlayer master
with charachange

ke "I just want to make sure you don't end up too far under the bridge."

hi "You're losing me, Kenji."

show kenji happy onlayer master
with charachange

ke "That's okay, lots of people get lost. That's why I'm here to help."

scene bg school_gardens onlayer master
show kenji neutral onlayer master
with locationskip

ke "Just be careful around her, okay? She looks all harmless on the outside, but I've heard shit. Bad shit."

show kenji tsun onlayer master
with charachange

ke "You know the Student Council, right?"

"He seems to involuntarily shudder as he says the words. Putting him and Shizune together in a room is an amusing mental exercise. I wonder if they've met."

hi "Yeah, Shizune and Misha are in my class. I seem to have dodged the draft, though."

show kenji happy onlayer master
with charachange

ke "Good man. Good man."

show kenji tsun onlayer master
with charachange

ke "But this blonde? She was there. In the Student Council. Right. Damn. There."

hi "I see. And?"

ke "And she's not there now."

stop music fadeout 3.0

hi "…"

ke "Seriously, think about it. Something must have gone down."

"I stop walking for a moment, giving the idea more thought than I probably should."

"It would explain that fight the two had, at least in part. Wait, no, not really. Even leaving the Student Council would need a catalyst."

"In the end, it doesn't explain much at all. Other than the fact that their feud goes back some ways."

hi "I guess you have a point. I'm not seeing how that really affects me, though."

show kenji neutral onlayer master
with charachange

ke "Okay, now field this one. Lilly's foreign, obviously."

hi "Obviously."

ke "Now, what nationality is she?"

"I open my mouth to give the answer, but realize that I have none. In fact, I've given the matter very little thought."

"Given that she has no accent and acts perfectly Japanese, I suppose it never really seemed important. Now that he mentions it though, I am rather curious."

hi "To be honest, I don't know. Maybe English? They like tea."

"I probably shouldn't resort to stereotypes, but that's the only lead I have."

show kenji happy onlayer master
with charachange

play music music_kenji fadein 1.0

ke "You're not thinking. Luckily, you have me here to think for you."

hi "Gee, thanks."

"He brushes off the quip effortlessly."

show kenji neutral onlayer master
with charachange

ke "Now answer me this: who has lots of social power, is filthy stinking rich - you know blondes are all rich, right? - has a long history of disputes and used to belong to a much larger organization?"

hi "The Roman Catholic Church?"

show kenji tsun onlayer master
with charachange

ke "…Well okay, there's that."

show kenji neutral onlayer master
with charachange

ke "But there's also the Mafia. Come on. Rich, foreign, there's no way she doesn't have connections to them."

"I have reason to doubt the logic of his deductions, but he shows no sign of stopping."

scene bg school_hallway3 onlayer master
show kenji neutral onlayer master
with locationskip

ke "So do you know where I think she's from?"

hi "Italy?"

show kenji tsun onlayer master
with charachange

ke "Mainland Italy's small-time, dude. She has to be from Sicily. All those mafioso types come from there."

show kenji happy onlayer master
with charachange

ke "Wait, no, Russia. Damn, this could be bad. The Mafia there is serious business, man; Ex-KGB everywhere, paramilitaries, hardcore smuggling, and—"

hi "Wait, wait, stop, just slow down a sec. What point are you trying to get at here?"

show kenji neutral onlayer master
with charachange

ke "You don't know what she'll do, man. I won't get in your way - agents don't operate like that - but I just want you to be careful."

show kenji tsun onlayer master
with charachange

ke "When the time comes, we'll need all the help we can get. I don't want to lose you, comrade."

"Well, at least he's concerned for me. Kinda."

stop music fadeout 4.0

show kenji tsun onlayer master:
    center
    easeout 0.5 xpos 0.6 alpha 0.0
with None

"I wave goodbye to him as we separate out to our respective classes, but I'm not sure that he sees the gesture."

scene bg school_scienceroom onlayer master
with shorttimeskip

play ambient sfx_crowd_indoors fadein 2.0

"Piling my books into my bag, I catch a glimpse of the library books I'd borrowed last week. I might as well return them, considering they took all of two days to finish."

"I briefly consider inviting Hanako along to the library, but she's already gone. It'll probably be better for my studying if I'm alone anyway."

"With a quick stretch and a wave to a couple of classmates who give the same to me, I make my way out of the classroom."

stop ambient fadeout 1.0

scene bg school_library onlayer master
with locationskip

"As I open my bag and shove the books through the returns slot in the front counter, I notice a strange person behind the desk. Old and graying, she must be Yuuko's replacement when she's working at the café."

"I begin looking for a free table, a task made somewhat difficult considering that, despite there not being many students in here, they're all sitting at their own tables."

"Noticing a familiar head of hair, I walk over to one near the Braille section."

show lilly basic_smileclosed onlayer master
with charaenter

"It's hard to tell whether Lilly's concentrating hard or not, her placid expression holding perfectly still as her finger slides across the dot-filled pages of her book."

hi "Hi. Mind if I sit here?"

show lilly basic_surprised onlayer master
with charachange

li "Hmm? Oh, no problem at all…"

"She trails off, evidently still focused on her business at hand."

play music music_lilly fadein 10.0

show lilly basic_smile onlayer master
with charachange

li "Ah, Hisao."

show lilly basic_smileclosed onlayer master
with charachange

"She gives a nod of greeting as I sit opposite her at the table, pluck a chemistry textbook out of my bag and quickly thumb to the chapter we're covering in class."

"For a while, we sit there and read, each in our own way."

"Seeing her reminds me of what Kenji said this morning, though. That and the fact that I've never seen someone read in Braille before makes me keep throwing glances at her."

"I kind of feel guilty about it, given that she has no way to realize I'm doing so, so I decide to just ask her about it. Her lineage isn't exactly a state secret, after all, and there is another thing I've only just noticed from her movements."

hi "Hey Lilly, mind if I ask a question?"

show lilly basic_smile onlayer master
with charachange

li "Not at all. Is anything wrong?"

hi "I was just wondering… you're at least part foreign, right?"

show lilly basic_giggle onlayer master
with charachange

"She gives a small giggle before setting down her book."

show lilly basic_cheerful onlayer master
with charachange

li "I've always been amused at how squeamish people are about that. Akira's mentioned how much she and I look different from most others before."

show lilly basic_smile onlayer master
with charachange

li "The details are a bit complicated, but I'm half Japanese, half Scottish."

"…Scottish? That was not exactly my first guess. It takes some effort to not blurt it out loud."

"I try to conjure images of the place in my mind. I think as far as the UK goes, Scotland isn't bad to live in… but I'm not really sure."

"My first guess of England was surprisingly close, at least geographically. That does leave another question though."

hi "But you have no accent…?"

show lilly basic_weaksmile onlayer master
with charachange

li "That's where the details begin. I was born and raised in Japan, despite my mother being foreign."

hi "Ah, I get it."

"Hold on, if she moved to the dorms simply due to Akira working longer hours…"

hi "So they don't live near the school?"

show lilly basic_reminisce onlayer master
with charachange

"She gives a small sigh, as if she didn't expect me to go any deeper. Was her previous frankness just a front?"

li "Not… exactly. It's been a long time since we've actually met."

"I feel like I'm not getting the whole story, but I don't really want to go unduly prying into her situation. Her about-face shows she feels kind of awkward about it."

hi "So… do you speak much English? To be honest I don't know that much about Scotland, but at least I know that's the main language there."

"It takes her a moment to collect herself, appreciating the change in topic."

show lilly basic_smileclosed onlayer master
with charachange

li "That's right. My family mostly used Japanese around the house when I was young, but they made sure Akira and I knew our Scottish side just as well."

show lilly basic_smile onlayer master
with charachange

li "I'm fluent in the language, but I'm also studying it in school. To keep my skills up and to have the qualifications on paper, mainly."

hi "So you're bilingual? That's pretty impressive."

show lilly basic_weaksmile onlayer master
with charachange

li "I wouldn't go that far. Having parents who can speak the language is a large advantage, and English books in Braille aren't too hard to buy or import. With Yuuko's help, at least."

show lilly basic_smileclosed onlayer master
with charachange

li "There's a relatively high demand for local English teachers here anyway, which also helps give me some motivation to learn it well."

"Demand for English teachers? For a moment, I wonder why she brought this up."

hi "You're planning to be an English teacher?"

show lilly basic_cheerful onlayer master
with charachange

"She gives an enthusiastic nod."

"It must be nice, having such a definite future in mind. I've never really given much thought to mine, so I'm kind of envious."

hi "Hmm…"

show lilly basic_smile onlayer master
with charachange

li "What's wrong?"

hi "It's just… I could see you as a teacher pretty easily. It suits you."

show lilly basic_emb onlayer master
with charachange

"For a moment, she's speechless. She lowers her face a little and lets out a nervous giggle, something I've never seen her do before."

"With Lilly's role as a class representative and her dependable nature, teaching does seem to be a line of work fitting her personality."

hi "Sorry, that was probably a little much. It is true, though."

show lilly basic_weaksmile onlayer master
with charachange

"Waving her hand in front of her face dismissively, she quickly recovers."

li "It's not that, it's just that… only one person's ever said that to me before."

stop music fadeout 8.0

"A short, somewhat awkward silence follows the discussion. Without knowing it, I ended up steering into a troublesome topic again."

"I should try to cheer her up a little. It was me who went and got her brooding, after all."

hi "Want to go grab lunch at the cafeteria after this?"

"It might perk her up a bit, or at least take her mind off her apparently complicated family situation."

show lilly basic_planned onlayer master
with charachange

"Going by her smile, it seems to have the intended effect."

show lilly basic_ara onlayer master
with charachange

li "I appreciate the thought, but the food there…"

"Quite a quick redirection of the conversation. She does have a point though - the food there isn't the greatest."

hi "Maybe the Shanghai? We could ask Hanako if she wants to come as well."

show lilly basic_surprised onlayer master
with charachange

li "Ah…"

hi "What is it?"

show lilly basic_weaksmile onlayer master
with charachange

li "I almost forgot, until you reminded me. Hanako's birthday is coming up soon, and I was going to go shopping in the city for a present tomorrow."

hi "If that's an invitation, I'd be happy to accompany you."

"The ability to get more used to the layout of the city would probably be a good thing. I have barely set foot in there, so I'd be hopelessly lost by myself."

show lilly basic_smile onlayer master
with charachange

"She gives a nod, signaling that she happily approves of this plan for Sunday."

"We eventually get back to our books, though before I begin reading again I steal one last glance at her."

"Maybe I've been thinking on my situation too much. After all, everybody here would have their own unique circumstances."

"The chance to get outside and clear my head will probably do me good."

scene black onlayer master
with dissolve



label en_L3:

play ambient sfx_traffic fadein 10.0

scene black onlayer master
with None

scene bg city_street1 onlayer master at Fullpan(16.0, "left")
with locationchange

"Bored of standing in place and watching the television in a shop window, I pull myself away from the tacky display with little effort."

"After living at Yamaku, the city seems like an entirely different world."

"No running in the halls. Calm and orderly conduct is to be used at all times in the classrooms. Students are to exit rooms after checking both directions for oncomers. Elevators are reserved for movement-impaired students. Single file on stairs."

"Compared to such strict, almost regimental, standards, the city's shopping arcade might as well be a strange country."

"While the school may have its fair share of hustle and bustle during the festival, the outside world is much different."

"It's strange. Having lived in a metropolitan city before my accident, this should feel more natural than Yamaku and the surrounding town ever could."

"Yet it feels foreign, somehow. The elevated walkways and tall buildings, each adorned with billboards taller than any three people, don't do anything to distract me from the passing crowd's reactions."

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

show lilly cane_smileclosed_cas_close onlayer master:
    center
    xpos 0.2
    easein 1.0 twoleft
show bg city_street1 onlayer master at left
with Dissolve(1.0)

"Lilly keeps one hand on my shoulder, the other holding her cane which taps the ground with a metronome-like steadiness. Looking over to her, that neutral smile of hers still holds."

"Having only seen her in school uniform, I'd not have recognized her as she sat on a bench waiting for me to come, if not for her cane propped up against it and her distinctive hair."

"I can't tell whether they're glancing at her due to her height, her foreign looks, her obvious blindness, or all three. Not that any of those would make the situation any less uncomfortable than it is."

show lilly cane_smile_cas_close onlayer master
with charachange

li "Do you have any ideas of where to look first, Hisao?"

"Her soft voice breaks me out of my line of thought."

"I can't imagine that she's failing to notice the attention she garners, but she seems unfazed by it. I get the feeling she's the type to enjoy walking outside, so she might be used to it by now."

hi "Not really. This is my first time in this city, so I've got no idea of where to go."

show lilly cane_listen_cas_close onlayer master
with charachange

"She furrows her brow in thought, planning a route for us to take. And, come to think of it, a way to communicate it."

"Something I'd noticed in the time I've been with her is how, when deep in thought, she lacks close to any form of body language to show it."

"Her expression may change, but not a hint of movement shows. She seems to have little in the way of sweeping physical gestures in general though, so I've assumed it's part of her reserved nature."

show lilly cane_weaksmile_cas_close onlayer master
with charachange

li "Is there a large electronics store near here?"

"I take a quick look around, mostly finding clothing stores. After a few seconds I notice a store with a bright blue sign some distance away that fits her description."

hi "Yep, it's just a bit ahead of us. Should we go in that direction?"

show lilly cane_smile_cas_close onlayer master
with charachange

"Thankfully, it's just the information she needed. With a nod we start off and head towards Lilly's unknown destination, landmarks being our guide."

stop ambient fadeout 2.0

scene ev icecream onlayer master
with shorttimeskip

play music music_happiness fadein 2.0

"Storeowner" "Here you go. One vanilla, one chocolate."

scene bg city_street2 onlayer master at center
with locationchange

"I hand the money over the counter and take the cones to the railing that Lilly's sitting on."

"I can't believe I let her trick me like this. She not only led me to an ice cream stall, but also got me to buy her some. At least she gave me the money for hers."

show lilly cane_smileclosed_cas onlayer master at Transform(xanchor=0.5, xpos=0.2, ypos=0.2, yanchor=0.0)
with charaenter

"Sure enough, she's patiently waiting where I'd left her. I guess she was planning on making the day an event, rather than a simple shopping trip."

show lilly cane_smileclosed_cas onlayer master:
    ease 1.0 xpos 0.5 xanchor 0.5 ypos 0.15
show bg city_street2 onlayer master:
    ease 1.0 left
with None

show lilly basic_satisfied_cas_close onlayer master:
    xanchor 0.5 xpos 0.2 ypos 0.2 yanchor 0.0
    ease 1.0 xpos 0.5 xanchor 0.5 ypos 0.15
show bg city_street2 onlayer master:
    ease 1.0 left
with Dissolve(1.0)

"I call out to her and slowly place the vanilla cone in her outstretched hands, being careful to make sure she has a good hold of it before letting go."

"At least her tastes are fairly normal. I was worried she'd ask for some weird flavor when she first asked."

hi "Here's the change."

show lilly basic_smileclosed_cas_close onlayer master at Transform(xalign=0.5, ypos=0.15)
with charachange

li "It's okay, keep it."

"I move to protest, but realize the futility of doing so over such a small amount. I slip the coin into my pocket, supplementing my meager allowance ever so slightly."

show lilly basic_smileclosed_cas_close onlayer master
with charachange

"Lilly shows no signs of wanting to get up, so I take a seat beside her and start eating my own ice cream."

hi "The summer weather's nice. Hopefully it will hold out for a while."

show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "You too? I'm beginning to think I'm the only person who prefers winter."

"I contemplate her statement for a long moment."

hi "Yeah, I think you might be."

show lilly basic_pout_cas_close onlayer master
with charachange

"It draws the intended reaction. She's cute when she's pouting."

hi "Still, I can't really imagine what's so good about winter. You can't go out without bundling up, and you still freeze anyway."

show lilly basic_reminisce_cas_close onlayer master
with charachange

li "I used to live further north, where there'd be plenty of snow to play in, so it's a little nostalgic. I don't like the heat very much, either."

hi "At least you can wear a skirt, so don't complain about that."

show lilly basic_giggle_cas_close onlayer master
with charachange

"She gives an amused giggle as we both get back to finishing off our already melting cones."

play ambient sfx_crowd_outdoors fadein 2.0

hide lilly onlayer master
show crowd onlayer master at left
with shorttimeskip

"I idly sit and watch the crowds going by as we eat, catching bits and pieces of conversation."

show lilly basic_satisfied_cas_close onlayer master at Transform(xalign=0.5, ypos=0.15)
with charaenter

"Looking to Lilly, I see her dutifully licking her ice cream from the top downwards, blissfully unaware of the fact that it's beginning to melt."

hi "It's melting."

show lilly basic_surprised_cas_close onlayer master
with charachange

li "Where?"

hi "Um… down a bit?"

show lilly basic_listen_cas_close onlayer master
with charachange

"She lowers her mouth from the top of the cone, but has no idea of exactly where the ice cream's dripping. What follows is a game of guiding her left and right until she finally finds it."

"To any onlooker, it must seem absolutely bizarre - a girl with her eyes closed turning her cone over and over as the guy next to her gives instructions. A strange variant of childhood blindfold games, maybe."

show lilly basic_smileclosed_cas_close onlayer master
with shorttimeskip

"In good time we finally finish our treats, and while away the time conversing casually."

stop music fadeout 3.0

show lilly back_listen_cas_close onlayer master
with charachange

"Caught mid-sentence, Lilly perks her head in her trademark manner. It's an unmistakable sign that something's caught her attention."

show lilly back_smileclosed_cas_close onlayer master
with charachange

li "Ah…"

hi "What is it?"

show lilly back_smile_cas_close onlayer master
with charachange

li "Is Akira somewhere over there? I think I heard her."

show lilly back_smile_cas_close onlayer master at Transform(xpos=0.25)
show crowd onlayer master:
    bgright
    xpos 0.55
show bg city_street2 onlayer master:
    bgright
    xpos 0.55
with dissolvecharamove




"I raise an eyebrow as I look in the direction she's facing, somewhat doubtful of her ability to pick out Akira's lone voice in the din."

show akira basic_boo behind crowd onlayer master:
    tworight
    xpos 0.78 ypos 1.13
with charaenter

"Sure enough though, a blonde girl in a suit can be seen through the tiny gaps between people walking every which way."

"I raise a hand and wave, trying to catch her attention."

hi "Satou! Hey, Satou!"

show akira basic_smile onlayer master
with charachange

"She stops in her tracks and looks towards me, evidently noticing my calls. As she does, I notice someone walking beside her."

"I can't get a good look at whoever it is though, before the two begin walking towards where we are."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
play music music_ease fadein 4.0

show akira basic_smile onlayer master:
    ease 1.0 ypos 1.0 alpha 0.0
with None

show akira basic_smile as akira2 behind lilly onlayer master:
    tworight
    xpos 0.78 ypos 1.13 alpha 0.0
    ease 1.0 ypos 1.0 alpha 1.0
with Pause(1.0)

hide akira onlayer master
with None

show lilly back_smile_cas_close onlayer master at Transform(yalign=1.0)
with charamove

"As they reach us, Lilly and I stand and dust ourselves off."

show lilly back_giggle_cas_close onlayer master
with charachange

li "Akira?"

hide akira2 onlayer master
show akira basic_laugh behind lilly onlayer master:
    tworight
    xpos 0.78 ypos 1.0
with charachange

aki "Hey, you two."

show lilly back_giggle_cas_close onlayer master at Transform(xpos=0.1)
show akira basic_smile onlayer master at Transform(xanchor=0.5, xpos=0.6)
show crowd onlayer master at center
show bg city_street2 onlayer master at center
with dissolvecharamove

show hideaki bored behind akira at right onlayer master
with charaenter

"She nods towards me, a gesture which I quickly return. My gaze shifts towards the young girl next to her, and our eyes meet. As they do, Akira plops a hand onto her head, a move which doesn't seem to faze her."

show hideaki normal onlayer master
with charachange

hh "I don't believe we've met. I'm Hideaki. Pleased to meet you, Hisao."

"A guy's name, huh? Guess I just dodged a bullet there. He bows, somewhat restrained by Akira's hand being on his head."

show lilly basic_smileclosed_cas_close onlayer master at Transform(xpos=0.18)
with charachange

li "Oh, Hideaki's here too? Are you well?"

show hideaki thinking onlayer master
with charachange

hh "Akira's been taking very good care of me, thank you."

show akira basic_laugh onlayer master
show hideaki sad onlayer master
with charachange

"Akira grins as if to affirm the point and rubs his head hard, dragging it around in a circular motion. His dreary face during this is somewhat amusing."

show akira basic_smile onlayer master
with charachange

aki "Uncle's out on business again, so I'm just taking him around town for today."

show akira basic_boo onlayer master
with charachange

aki "I'd have preferred to be spending the day on a date with my boyfriend, but…"

show hideaki closed_up onlayer master
with charachange

"Hideaki gives a cough to try and redirect Akira's thoughts."

"As he does so, though, I find mine wandering. They're related? And further, as first cousins? I suppose that explains why she's taking care of him in any case."

hi "Come to think of it, Hideaki, how did you know my name?"

show hideaki serious onlayer master
with charachange

hh "Akira told me. Being a Yamaku student, I suppose you're disabled in some way?"

hi "Not everyone in Yamaku's disabled…"

"Which I only learned a handful of days ago. I give silent thanks to Shizune and Misha for their stream of information about how the school works."

"Because of them, I found out that since the school will accept practically anybody suffering from non-mental disabilities, it doesn't discriminate against healthy people either."

"It seems unlikely that many in good health would enroll there though. While the standard of education is pretty high, it's extremely isolated and very much focused on helping disabled students."

show hideaki angry_up onlayer master
with charachange

hh "You're dodging the question."

"Damn, he's sharp."

"Before I can say another word though, he decides to take a stab at it himself."

show hideaki evil onlayer master
with charachange

hh "If I were to call it myself… your heart?"

$ renpy.music.set_volume(0.5, 0.5, channel="music")
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show akira basic_lost onlayer master
show lilly basic_listen_cas_close onlayer master
with charachange

"Akira looks mildly curiously at me, her interest piqued as well. That sure was a lucky guess."

hi "How did you…?"

$ renpy.music.set_volume(1.0, 10.0, channel="music")
$ renpy.music.set_volume(0.5, 10.0, channel="ambient")

show hideaki thinking onlayer master
with charachange

hh "You show no missing limbs or deformities, so external disabilities are out."

show hideaki serious onlayer master
with charachange

hh "Considering the lack of any strange mannerisms, it's also unlikely that you'd have any mental disability."

show lilly basic_planned_cas_close onlayer master
with charachange

li "But Yamaku doesn't take mentally disabled students."

show hideaki bored onlayer master
with charachange

hh "I know."

show hideaki serious_up onlayer master
with charachange

hh "Leaving that aside, the only possibility left is that of internal disabilities."

show hideaki happy onlayer master
with charachange

hh "I didn't know which one you might bear, so I guessed. Correctly, as it turns out. And your reaction confirmed my guess."

show akira basic_smile onlayer master
with charachange

"More than a little bemused, I look to Akira. She grins and shrugs, obviously taking some enjoyment out of her partner's deductions."

"He's sharp, yes, but more than a little unsympathetic. Logical, but lacking in tact. His attitude reminds me of Shizune, in a way, as do his looks."

show hideaki disapproves onlayer master
with charachange

hh "May I ask why you're staring at me? Surely I'm not that unusual a specimen."

"Does he not know how unusual he looks? I could overlook the spats and clothing as just being coincidental, but the ribbon in his hair really is too much."

"This is entirely beside the point, though."

hi "Sorry. You just remind me of someone."

play sound sfx_impact

show akira basic_boo onlayer master
show hideaki surprise_up onlayer master
with vpunch

"Akira gives him a sharp jab with her elbow."

show akira basic_laugh onlayer master
with charachange

aki "Told ya you're not that much different from her."

show hideaki closed_up onlayer master
with charachange

"He coughs into his hand to try and maintain an upright and serious demeanor."

hh "I see you've met my sister, then. Perhaps my full name might help you."

show hideaki serious onlayer master
with charachange

hh "I am Hideaki Hakamichi. You are probably thinking of my sister, Shizune Hakamichi."

"Oh, so he's Shizune's brother."

"Wait a minute, if Hideaki is the son of Akira's uncle, and Shizune is his sister, then that means Lilly and Shizune's fathers are brothers-in-law. Therefore…"

hi "Lilly and Shizune are first cousins?"

show lilly basic_concerned_cas_close onlayer master
show akira basic_smile onlayer master
with charachange

"Lilly groans in an uncharacteristically unrestrained manner. The reaction earns an amused smirk from her sister."

"The enmity between the two just took on another meaning. I had thought it simply a matter of difficulty of communication between the two, but a family feud makes things much more complicated."


show akira basic_laugh onlayer master
with charachange

aki "You can choose your friends, but you can't choose your family."

show akira basic_boo onlayer master
with charachange

"She gives a halfhearted shrug. She mustn't give as much weight to the two's conflict as I do."

show akira basic_smile onlayer master
with charachange

aki "Well, that's how it is. What're you two up to anyway on this fine day?"

show lilly basic_smileclosed_cas_close onlayer master
with charachange

li "We're shopping for Hanako's birthday present. The day will be coming up soon, so this is the last chance we'll have before school starts again for the week."

stop music fadeout 7.0

show akira basic_lost onlayer master
with charachange

"Akira makes a strange face, as if Lilly had just said that the sky wasn't blue and the clouds not white."

aki "Isn't her birthday on the tenth next month?"

show lilly basic_surprised_cas_close onlayer master
with charachange

li "Yes… Why? Is something wrong?"

show akira basic_resigned onlayer master
with charachange

"Akira's face seems to collapse. It's an utterly unbefitting expression for someone so rowdy and headstrong."

aki "The folks didn't call you yet?"

show lilly basic_oops_cas_close onlayer master
show hideaki confused onlayer master
with charachange

"As Lilly shakes her head cluelessly, I look at Hideaki to see if he knows anything about this. A simple shrug is his only answer."

show akira basic_boo onlayer master
with charachange

"For a moment, Akira ponders what to do before smiling once again. The fact that she can hide her emotions so quickly and effectively is unsettling."

show akira basic_smile onlayer master
with charachange

aki "Hey Shortie, sorry, but could you hang with Hisao for a while?"

$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

show hideaki normal onlayer master
with charachange

show lilly basic_oops_cas_close onlayer master:
    parallel:
        easeout 1.0 xpos -0.5
    parallel:
        linear 0.7 alpha 0.0
show akira basic_smile onlayer master:
    parallel:
        easeout 1.0 xanchor 1.0 xpos 0.0
    parallel:
        linear 0.7 alpha 0.0
show hideaki normal onlayer master:
    ease 1.0 center
show bg city_street2 onlayer master:
    ease 1.0 right
show crowd onlayer master:
    ease 1.0 right
with Pause(1.0)

hide lilly onlayer master
hide akira onlayer master
with None

"He nods and waves her off, Akira placing an arm on Lilly's shoulder as she guides her away and out of earshot."

"And so, I'm alone with “Shortie.”"

hi "So… nice weather, isn't it?"

show hideaki thinking onlayer master at center
with charachange

hh "It seems so."

"…"

hi "I guess they dumped us."

show hideaki serious onlayer master
with charachange

hh "Indeed."

"What a farcical attempt at smalltalk. I've got no idea of how to talk to this guy, and his robotic responses aren't helping. Blood and a stone come to mind."

show hideaki triangle onlayer master
with charachange

"Without another word, he begins to rock on his feet in an obvious gesture of boredom with this discussion. He really is like a little kid, despite his serious demeanor."

"Suspecting the conversation over, I decide to accomplish what I came here to do in the first place."

hi "I'm going to go search for a present. Coming?"

show hideaki normal onlayer master
with charachange

hh "Not much else to do."

stop ambient fadeout 0.5

scene bg city_street3 onlayer master
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

"In a little while, we come to a small shop beside a convenience store."

"For once the store windows aren't filled with electronics and computer games, but dolls, stuffed bears and all manners of wood-crafted oddities."

hi "Othello's… Antiques?"

"An antique store? Well, if there's anything in this town that'd suit Hanako, I guess it'd be here."

"I reach for the old-looking door handle, but pull back at the last minute as I realize my companion's gone adrift."

hi "Not coming in?"

show hideaki triangle onlayer master at center
with charaenter

hh "I'll just be in the newsstand for a while. Don't mind me."

"His voice makes it painfully clear he has zero interest in what's in the store, and that he doesn't feel obligated to follow me."

hide hideaki onlayer master
with charaexit

"As he wanders off without another word, I push the thick wooden door and enter the store, a bell above me ringing out."

stop ambient fadeout 0.5
play sound sfx_storebell

scene bg city_othello onlayer master at Fullpan(10.0, dir="left")
with locationskip

play music music_soothing fadein 0.5

"The musty smell of old books and wooden shelves is distinctly anachronistic."

"I look to the counter beside the door. The graying man behind it sits there silently, reading a tattered book. He certainly fits the look of the place."

"Slowly wandering through the aisles, the person I'm reminded of as I inspect each handcrafted or imported oddity in turn isn't Hanako."

"Crouching down, I examine the ancient oak desk inside the shop window."

"At least thirty dolls, all varying wildly in size and make. The only similarity between them is the long Victorian dresses they wear."

"I turn the price tag of one that looks to be about waist-height."

"…It's not in my price bracket. At all."

"I do the same to each of them, getting more and more depressed as they get smaller and smaller in size."

"That is, until I reach the very smallest one. It's affordable, just, yet of quality make and with long, auburn hair and a little blue dress."

"I decide that it's the kind of present Hanako would appreciate. Pretty-looking, and far from gaudy."

"After I carefully pick it up, I decide to keep looking around the store. I'm not sure whether it's because I like the atmosphere or out of simple curiosity."

stop music fadeout 2.0

show bg city_othello onlayer master at left
with None

"Peeking around the corner before I go to the next aisle, I see that the shelves in this one are stocked with wooden toys; from toy cars to intricate automatons."

show musicbox closed onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Tucked behind a line of nutcrackers, I notice a little plain wooden box. It feels surprisingly light as I pick it up with my free hand."

show musicbox open onlayer master:
    ypos 0.5 alpha 1.0
with charachange

play music music_musicbox

"The lid only needs the smallest movement to pop open, the little metal drum inside beginning to rotate immediately."

"For seconds on end, I simply stand there listening to the palm-sized melody."

"As it plays, I take the tiny price tag in my fingers and bring it up to my face, the minuscule cursive writing taking some effort to read."

"It's affordable… sort of."

show musicbox closed onlayer master
with charachange

play sound sfx_switch
stop music

show musicbox closed onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide musicbox onlayer master
with None

"Grimacing slightly, I close the lid and make my way to the counter with doll and music box in hand."

show shopkeep surprised onlayer master at center
with charaenter

"When I lay the two on the counter, the man behind it sits up and takes stock of them. He doesn't hide very well his surprise at someone of my age buying them."

show shopkeep thinking onlayer master
with charachange

"It's painful, but I hand over the money for the two and leave the store with a small opaque bag in hand."

play ambient sfx_traffic fadein 0.5

scene bg city_street3 onlayer master
show hideaki serious onlayer master at center
with locationchange

"Hideaki being there takes me by surprise."

hi "Oh… hi. I thought you'd be at the newsstand."

show hideaki bored onlayer master
with charachange

hh "Akira gave me a call. She's waiting for us at the fountain with Lilly."

"At least that solves the issue of trying to find them again."

$ renpy.music.set_volume(0.4, 0.5, channel="ambient")

scene bg city_street2 onlayer master
with locationskip

"We head off back to the fountain. Hideaki's immaculate posture and presentation despite his appearance makes for a strange contrast even as we walk."

show lilly cane_reminisce_cas onlayer master at twoleft
show akira basic_boo onlayer master at tworight
with charaenter

"Lilly and Akira stand there waiting for us, their faces hard to read."

show akira basic_smile onlayer master at tworight
with charachange

aki "Hey. You ready to go, Shortie?"

show bg city_street2 onlayer master at bgleft
show lilly cane_reminisce_cas onlayer master at left
show akira basic_smile onlayer master at Transform(xpos=0.55)
with charamove

show hideaki happy onlayer master at right
with charaenter

"Hideaki's mood seems to improve as he rejoins her."

show hideaki happy_up onlayer master
with charachange

aki "Seeya Lilly, Hisao. Tell Hanako I said happy birthday."

hi "We will. Bye."

show lilly cane_weaksmile_cas onlayer master
with charachange

li "Goodbye, Akira."

hide akira onlayer master
hide hideaki onlayer master
show lilly cane_reminisce_cas onlayer master
with charaexit

show lilly cane_reminisce_cas onlayer master at center
show bg city_street2 onlayer master at bgright
with charamove

"And with that, the two disappear into the fracas of the afternoon city crowd."

"Turning to Lilly, I notice she's carrying a small bag. It's now that I realize why her disposition felt different from before; while Lilly's typically the type to wear her emotions on her sleeve, her expression and tone are clouded and difficult to read."

"It's more than a little off-putting, but given the effort she's making to hide her emotions, I doubt she wants to be cornered on why she's feeling this way."

hi "Already bought Hanako a present?"

show lilly cane_weaksmile_cas onlayer master
with charachange

li "Yes. Have you?"

hi "Yeah."

show lilly cane_sleepy_cas onlayer master
with charachange

li "Shall we head back to the bus stop then?"

hi "Okay. There should be a bus back to Yamaku pretty soon."

"And with that, we begin to walk."

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

scene bg city_street1 onlayer master
show lilly cane_concerned_cas_close onlayer master at twoleft
with locationskip

"It feels strange compared to before. Lilly's hand on my forearm feels unusually tense, and the whole atmosphere is extraordinarily awkward."

"The silence continues for a long while. I really don't like seeing her like this."

show lilly cane_sleepy_cas_close onlayer master
with charachange

li "Hanako's birthday party is going to have to be held earlier. Is the fourth going to be all right for you?"

"I have no other possible obligations anyway, so I reflexively nod. Only afterwards do I remember that doing so is pointless, and quickly answer so by speech."

"She tries to collect herself, a task that looks almost pitiable in how plain it is to see how distant her thoughts are."

show lilly cane_weaksmile_cas_close onlayer master
with charachange

li "Sorry, Hisao. You said the bus would be coming soon, right?"

hi "That's right."

"But now that she says that, I have an idea."

hi "Actually, do you have anything to do later today?"

show lilly cane_oops_cas_close onlayer master
with charachange

li "I… don't believe so. Why do you ask?"

hi "This is the point where I'd normally take your hand and rush you somewhere, but even without that, you'll have to trust me. Okay?"

show lilly cane_surprised_cas_close onlayer master
with charachange

"I take her hand and gently lead her on, her distant face replaced by one of mild surprise and curiosity."

stop ambient fadeout 2.0

scene bg city_karaokeint onlayer master
with shorttimeskip

$ renpy.music.set_volume(1.0, 10.0, channel="ambient")
play music music_another fadein 2.0

"As the waitress sets the cup of tea and cup of coffee that I'd ordered onto the table, I thank her before she takes her leave."

"Truth be told, I really lucked out in finding this café. I didn't really know where I was going, rather I was just looking for any café that looked relatively nice."

"Having managed to recover a little, Lilly tentatively sips at her cup as I take a long gulp of the coffee in front of me."

"As I hoped, her face lights up as she realizes what flavor it is."

show lilly basic_weaksmile_cas_close onlayer master at Transform(xalign=0.5, ypos=0.15, yanchor=0.0)
with charaenter

li "Ah… this is wonderful!"

show lilly basic_surprised_cas_close onlayer master
with charachange

li "Hisao, how did you know that this was…?"

"I'd asked for French vanilla black tea, hedging my bets that it would be her favorite flavor, or at least one she liked. While I don't really know much about tea, it sounded like one she might appreciate."

"…on the basis of her liking vanilla ice cream. A tea connoisseur I am definitely not."

hi "It was a lucky guess. You really like tea, don't you?"

show lilly basic_smileclosed_cas_close onlayer master
with charachange

"She puts her teacup down and gives a tiny nod, that familiar small smile thankfully perched on her face once again."

show lilly basic_smile_cas_close onlayer master
with charachange

li "Drinking tea is… calming, I think."

hi "With the amount you drink, are you sure you're not addicted to it? Caffeine addiction's pretty common nowadays."

show lilly basic_giggle_cas_close onlayer master
with charachange

li "Did I ever say I wasn't?"

"She lets out a giggle as my head drops. We all have our vices, I suppose, and there are worse things to be addicted to."

hi "French vanilla black tea, huh? I'll have to remember that."

show lilly basic_smileclosed_cas_close onlayer master
with charachange

"For a while, we both silently drink. It's comforting to have someone like her nearby in such new surroundings, even if it's just the two of us sitting in silence."

"I begin to wonder if this feeling is the same for her, until she sets down her cup."

show lilly basic_emb_cas_close onlayer master
with charachange

li "Hisao, do you mind if I ask you a slightly odd question?"

hi "That depends on the question, I guess."

show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "I was wondering… what your favorite color is. Everyone has one, after all."

"I almost reply before realizing why the seemingly mundane question is actually quite strange."

hi "My favorite color? But…"

show lilly basic_pout_cas_close onlayer master
with charachange

"She gives a pouting look, wanting me to answer anyway. While the answer seems unavoidably wasted on her, there isn't any harm in giving it."

hi "I've always had a thing for green. I'd say that's my favorite."

show lilly basic_satisfied_cas_close onlayer master
with charachange

li "Green, is it? What things do you think of when contemplating that color?"

hi "I suppose… grass fields and trees in summer. The Army as well, with camouflage."

show lilly basic_planned_cas_close onlayer master
with charachange

li "Men always seem to like the military."

show lilly basic_smile_cas_close onlayer master
with charachange

li "But… that sounds like a nice color. A very nice color."

"She nods her head a little, as if approving of the choice. Considering how foreign the concept of color is to her mind, labeling it by association seems reasonable enough."

hi "If everyone has a favorite color, then what's yours?"

show lilly basic_smileclosed_cas_close onlayer master
with charachange

li "White. I'm told that's the color of snow, and of ice cream."

hi "You're no better than me then, if you only like that color because of a favorite food. I guess white is nice too, though."

hi "And speaking of colors, it'll be getting dark soon. Let me help you up."

show lilly basic_smile_cas_close onlayer master
with charachange

show lilly basic_smile_cas_close onlayer master at center
with charamove

"Lilly offers her hand, which I take in mine to help lever her up from her seat at the table. Its softness compared to mine takes me off guard, as I'm really not used to such casual contact."

"It doesn't seem to bother her at all though. While it seems obvious why, it feels like just one more ladylike aspect to her."

"As her hand moves to her pocket, I quickly cut her off."

hi "Don't worry, I'll pay for this."

show lilly basic_cheerful_cas_close onlayer master at center
with charachange

li "Oh. Thank you, Hisao."

"She gives an earnest smile at the gesture, a reward much greater than that of her words."

stop music fadeout 2.0

scene bg suburb_roadcenter_ni onlayer master
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")
play ambient sfx_cicadas fadein 0.5

"By the time we step off the bus, it's well and truly dark."

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

scene bg school_road_ni onlayer master
with locationskip

"We make our way up the hill in silence, both of us behaving a little awkwardly, probably because of the day's events."

"While I'm still concerned over Lilly's withdrawn nature after meeting with her sister, the fact I managed to cheer her up even slightly feels like a personal victory."

"But… it feels like the air between us has changed. Maybe it's only a bit, but it's something I don't think either of us realized before."

show lilly cane_weaksmile_cas_ni onlayer master at center
with charaenter

li "That was… a date, wasn't it?"

"It was. That doesn't elude either of us, the question's answer being so self-evident as to be rhetorical."

"Awkward as it may be, I don't think this feeling is bad. In fact, quite the opposite. I don't know what it is, I certainly can't be sure, but it feels like something a little more than friendship."

"Understanding? Empathy? Searching for words to adequately describe it is difficult. Nonetheless…"

hi "Would you like do this again sometime, Lilly? Without shopping for presents?"

show lilly cane_emb_cas_ni onlayer master
with charachange

"The tentative question is met with the same look from Lilly as before. Her pale skin makes the rosy tint of her cheeks just slightly more noticeable and her face, though still pointed to the street ahead of her, lowers. Just a little."

show lilly cane_cheerful_cas_ni onlayer master
with charachange

li "…Okay."

stop ambient fadeout 2.0

scene black onlayer master
with dissolve




label en_L4:

scene bg school_girlsdormhall onlayer master
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

"I walk down the hall of the girls' dormitories, my schoolbag in hand."

"A doll lies inside, carefully placed on top of a small box. I've been carrying the box in there for a while now, still not sure of what to do with it."

"This whole situation, come to think of it, is bizarre."

"While I've known of Hanako's upcoming birthday party for a while now, I had no idea of exactly what the celebrations would be until I found a single note left in the abandoned tea room earlier today."

"I hold it up and read it again, doublechecking the instructions. The plain black handwriting's fairly legible despite Lilly's blindness, clearly thanks to considerable effort and care."

window hide

$ written_note(u"Hisao,\n\nWe'll be holding a party at my place. Please come at six o'clock to room 225 in the girls' dormitory.\nSorry for notifying you this way, but I have class representative duties.\n\n- Lilly Satou", text_args={"color":"#000000"})

window show

"Not reassured, I continue walking down the hallway until I reach Lilly's dormitory room. I hesitate for a second, but eventually give three sharp taps on the door."

play sound sfx_doorknock2
with Pause(0.5)

"A brief and muffled exchange of words can be heard from the other side. Listening closer, I can just pick out Hanako and Lilly's voices."

"As they finish, Lilly calls out."

li "Might that be Hisao?"

hi "Yep. I got the note you left for me."

li "You can come in, the door is unlocked."

"Glad that I managed to get the right room, I press down on the handle and let myself in."

play sound sfx_dooropen

"As the door swings open, my greeting to them is stolen from my mouth."

window hide

play music music_one fadein 10.0

scene ev lilly_bedroom onlayer master:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with GenericWhiteout(0.5,0.1,4.0)

window show

"Lilly sits at a low table in the center of the room in her pajamas, while on the other side sits Hanako in a nightgown. Being dressed in only my normal school clothes, I feel quite out of place."

"I steal a quick glance at the lovely sight of the two, my eyes tearing themselves from Lilly's long, thin and pale legs only with a measure of reluctance."

hi "H-hi. I… think I brought everything that was needed."

scene ev lilly_bedroom_large onlayer master:
    xpos -130 ypos -400 subpixel True
    acdc_warp 12.0 ypos -800
with flash

"She smiles and nods. I wonder if she's even aware of the pleasant sight she makes. The thin dark blue silk of her pajamas really suits her, accentuating both her eyes and her curves."

"The look of her last night, that tentative and almost shy demeanor, seems all but replaced by her coy nature. It's nice to see her confidence returned, though I can't help casting my mind back to how she looked back then."

scene ev lilly_bedroom_large onlayer master:
    xpos -830 ypos -200 subpixel True
    acdc_warp 12.0 ypos 0
with flash

"I look to Hanako, who nervously sits opposite her in her gown. It isn't a surprise that she'd wear something so conservative, though it definitely looks cute."

hi "Hi, Hanako. Happy birthday."

ha "Ah… th-thank you."

"She's unusually skittish, despite the fact that she's warmed up to me considerably over the weeks we've come to know each other. This is a pretty unusual situation, I guess."

scene ev lilly_bedroom onlayer master
with flash

li "Feel free to take a seat, Hisao. I'll just pour you two some tea."

hi "Sure thing."

$ renpy.music.set_volume(0.8, 2.0, channel="music")

scene bg school_dormlilly onlayer master
with locationchange

"Lilly takes the steaming red teapot from the side of the table and gently pours its contents into our teacups as I take a seat beside them, setting my bag against the nearby wall."

"With my senses returned and hormones somewhat calmer, I realize that this is the first time I've ever been in Lilly's room."

"The first thing I notice is the ambient smell, just slightly different from that in mine… probably faint perfume, or nail polish. It could be anything of a girl's, really."

"Another is the plain nature of the room, visually. Beige walls, a smart yet unadorned cabinet, the lack of posters or wall hangings. It's distinctly utilitarian, something I should have anticipated given her blindness."

"The only thing that really seems out of the ordinary is several piles of books sitting on the floor, each reaching from roughly knee height to waist height. Some of them have printed titles, others are entirely blank except for dots of Braille."

"The fact that the ones with printed titles are uniformly in English is interesting, though not completely unexpected. She did mention her parents impressing the language upon her and Akira, after all."

hi "Your room looks nice, Lilly."

show hanagown distant onlayer master:
    center
    ypos 1.15
with charaenter

"I hear a call of thanks from beside my shoulder. Looking back to Hanako, her gaze is fixed on her lap and her hands are nervously clutching her gown."

"It's now that I notice why. With these clothes on, the extent of her scarring is far more visible; reaching down her neck and out to cover her right shoulder."

"Considering this is a party for her, she doesn't really look like she's enjoying the experience now that I'm here."

hi "So how old are you turning? Eighteen?"

show hanagown worry onlayer master
with charachange

"Her look of surprise, not at all helped by her total lack of skill at hiding her feelings, shows that she was trying to mentally tune me out. This is really quite awkward."

ha "Y-yes."

hi "On the plus side, there's only two more years till you can drink. So who's older? You or Lilly?"

show hanagown normal onlayer master
with charachange

ha "Lilly. She had her birthday in… F-February. What about… yours?"

hi "Earlier this year, so it's already passed."

"Unstated is that it passed while I was stuck in the hospital. That was… a particularly low point of the experience."

show hanagown distant onlayer master
with charachange

show hanagown distant onlayer master:
    tworight
    ypos 1.15
show bg school_dormlilly onlayer master at bgright
with charamove

show lilly basic_smileclosed_paj onlayer master:
    twoleft
    ypos 1.2
with charaenter

play sound sfx_teacup

"Conversation with her dries up as quickly as expected. It isn't long before Lilly's finished preparing our drinks, setting down the three teacups in front of us."

"I pick mine up, immediately noticing a much stronger aroma and taste than the tea we've been having."

hi "Huh, it tastes different than the tea we have in school."

show lilly basic_smile_paj onlayer master
with charachange

li "It's a different variety, rather than the kind we've been having there. You've never tasted Orange Jaipur before?"

hi "Not… that I can remember. I usually drink coffee after all, like when we were in town. This is nice, though."

show hanagown normal onlayer master
with charachange

"As we settle down and sip, Hanako seems to become more relaxed, or at least a bit less tense about my presence."

"We all finish our cups at about the same time, with Hanako failing rather badly at hiding her anticipation for the cake that's sitting to the side, begging to be eaten."

stop music fadeout 4.0

"Come to think of it, I'm feeling very eager myself. First things first, though."

hi "Lilly?"

show lilly basic_planned_paj onlayer master
with charachange

li "Yes, now is good."

"Each of us knowing exactly what the other means, I lean sideways and dig around in my bag for the doll I bought Hanako as Lilly gets up and retrieves her gift."

"Hiding our gifts in our hands, we present them both on the table at the same time."

show lilly basic_cheerful_paj onlayer master
show hanagown normal_blush onlayer master
with charachange

$ doublespeak (li, hi, "Happy birthday!")

"Hanako silently sits looking at them for seconds on end, out of sheer surprise."

"My little wooden doll, replete with Victorian-era dress and little hat, lies next to a light brown and fluffy stuffed bear from Lilly."

show hanagown distant onlayer master
with charachange

"She clutches at her gown as she moves to speak, not taking her eyes off the modest presents."

show hanagown distant_blush onlayer master
with charachange

ha "Th… thank you… Lilly and… Hisao…"

play music music_serene fadein 6.0

scene unlock_ev lilly_hanako_hug_end onlayer master
show black onlayer master
show ev lilly_hanako_hug onlayer master:
    xalign 0.5 yalign 1.0 alpha 0.0 subpixel True
    parallel:
        linear 5.0 alpha 1.0
    parallel:
        easein 15.0 yanchor 0.0 ypos -0.15

with locationskip

"Her voice begins to crack as Lilly reaches forward, wrapping her in a soft embrace."

"The sight of Hanako holding Lilly so tightly is heartwarming, so much so that I couldn't wipe the smile off my face even if I wanted to."

"As Lilly gently rests her face on Hanako's head, she speaks so quietly and softly that I can barely hear."

li "Happy birthday, Hanako."

hi "Happy birthday."

"Hanako gives a small nod, holding on to Lilly for a time before breaking off and wiping an eye."

"I guess that for Hanako simply having someone, anyone, to be there and love her would be special. The fact that Lilly and I can now share that role for her is something I think I will always be grateful for."

scene ev hanako_presents1 onlayer master
with locationskip

"Hanako gently takes the doll and teddy bear, holding them both to her chest as she warmly smiles."

"For a long time, all three of us simply sit in happy silence. The quiet is not broken until Lilly's soft voice beckons."

li "Shall we have at the cake, then?"

scene bg school_dormlilly onlayer master
show lilly basic_smile_paj onlayer master:
    twoleft
    ypos 1.2
show hanagown smile onlayer master:
    tworight
    ypos 1.15
with locationskip

"Her proposal is met with two looks of unhidden anticipation."

hi "No argument from me."

ha "Okay."

stop music fadeout 2.0

scene bg school_dormlilly onlayer master
show lilly basic_smileclosed_paj onlayer master:
    twoleft
    ypos 1.2
show hanagown normal onlayer master:
    tworight
    ypos 1.15
with shorttimeskip

hi "Phew, that was good."

play music music_dreamy fadein 4.0

"I contentedly sit back, both Lilly and Hanako looking just as satisfied with the food as I. It took some effort, but we managed to finish off the cake in one go."

show hanagown normal_blush onlayer master
with charachange

ha "I don't think I could fit any more in."

show lilly basic_weaksmile_paj onlayer master
with charachange

li "I think next time I'll buy a smaller cake."

show hanagown smile onlayer master
with charachange

"Hanako and I give a chuckle, but I can't help noticing that, come this time next year, we'll have graduated from Yamaku."

"That fact is somewhat depressing, since I finally feel as if my life is starting to get back into some kind of order."

"Idly looking around Lilly's neat and orderly room, her books catch my eye once again."

"This may be a little impetuous, but my curiosity gets the better of me. Besides, I don't think she'll mind in any case."

hi "Hey Lilly, do you mind if I take a look at one of your books?"

show lilly basic_smile_paj onlayer master
with charachange

li "You're quite welcome to, Hisao."

show lilly basic_planned_paj onlayer master
with charachange

li "That said, if you can overcome two language barriers I will be quite impressed."

hi "Two? Braille and… oh right, English."

show lilly basic_smile_paj onlayer master
with charachange

"She gives a nod."

hi "I knew you were studying English, but I'm still amazed that you're this proficient at it."

show lilly basic_giggle_paj onlayer master
with charachange

li "One could say it's a perfect way to avoid people borrowing my collection."

"She says it in jest, but I am a little disappointed. Having all these books around me with no way of reading them feels like one big tease."

"Hanako giggles quietly as I reach over the closest pile, plucking the topmost book with only a cursory glance. “Death on the Nile,” in large letters on the cover, is the only printed text to be seen."

$ renpy.music.set_volume(0.5, 0.5, channel="music")
play sound sfx_paper
show ev braille onlayer master at Fullpan(10.0, dir="right")
with locationskip

"I sit down for a while with the book open on my lap as Lilly and Hanako talk."

"Try as I might to feel out the dots of Braille printed on each page, they seem to blend into one another and become indistinct."

"I'd thought this to be a lot easier than it actually is. With some practice though, I could see someone with a better sense of touch than mine managing to read at a pretty fast speed."

$ renpy.music.set_volume(1.0, 0.5, channel="music")

scene bg school_dormlilly onlayer master
show lilly basic_smileclosed_paj onlayer master:
    twoleft
    ypos 1.2
show hanagown normal onlayer master:
    tworight
    ypos 1.15
with locationskip

"Noticing a silence that had probably begun earlier, I look up from the dotted pages to see Lilly smiling as Hanako sips another cup of tea."

hi "Is something wrong?"

show lilly basic_smile_paj onlayer master
with charachange

li "Quite the opposite, your curiosity's quite endearing."

"I am inordinately pleased by the praise, though I can feel my cheeks heating up a little."

hi "Thanks, but I don't know how else I could act."

show lilly basic_weaksmile_paj onlayer master
with charachange

li "To be honest, I wasn't altogether sure of how you saw us, since you were a new transfer student from another school."

stop music fadeout 12.0

show lilly basic_reminisce_paj onlayer master
with charachange

li "If you'd pitied us, I would have been quite offended."

show hanagown distant onlayer master
with charachange

"There's a certain edge to Lilly's voice, one that I'd quite possibly place as pride. Glancing over to Hanako, she seems even more subdued than usual, looking towards Lilly rather than me."

hi "I wouldn't worry about that. Considering the position I've found myself in, I'm perhaps the last person that should be dispensing pity on others."

hi "My parents' first interactions with me after my heart attack… I wouldn't want anyone to see that kind of face."

show lilly basic_oops_paj onlayer master
show hanagown distant_blush onlayer master
with charachange

"I catch myself from going any further, but not soon enough. Both of the girls seem to be put off, Lilly especially."

show lilly basic_emb_paj onlayer master
show hanagown worry onlayer master
with charachange

li "I'm… sorry. I shouldn't have gone that far…"

show lilly basic_listen_paj onlayer master
with charachange

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_doorknock2

"An awkward silence reigns for a few beats, thankfully ended as Lilly's head perks up in a gesture I've come to easily recognize."

hi "Hear something?"

show lilly basic_surprised_paj onlayer master
with charachange

li "The door…"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

show lilly basic_surprised_paj onlayer master:
    left
    ypos 1.2
show hanagown distant_blush onlayer master at Transform(xpos=0.4)
show bg school_dormlilly onlayer master at bgleft
with charamove

"Everyone looks towards it, trusting in Lilly's senses. True enough, the door handle shudders and turns, a flash of yellow and black slipping through."

show akira basic_laugh onlayer master at right
with easeinright

play music music_running

show lilly basic_listen_paj onlayer master
show hanagown worry onlayer master
with vpunch

aki "Akira Satou is in the house! Happy birthday, Hanako!"

show hanagown worry_blush onlayer master
with charachange

ha "Ah… thank you…"

show akira basic_smile onlayer master at Transform(ypos=1.15, xpos=0.8, xanchor=0.5)
with dissolvecharamove

"Akira takes a seat at the table as she plops her tall bag beside her. She has her trademark boisterous air about her, making no small deal of her entrance."

show hanagown distant onlayer master
with charachange

"Hanako clutches her gown to steady herself, but doesn't appear too shaken after she settles down. I guess she must have met Akira before, not a huge surprise given how close Akira and Lilly are."

"Akira doesn't seem to be the least bit put off by Hanako's scarring, despite its prominence, but she also doesn't pull any punches in how she acts despite Hanako's shy nature."

show lilly basic_weaksmile_paj onlayer master
with charachange

li "I thought you said you'd have to work, Akira. Did you manage to get off for a while?"

show akira basic_boo onlayer master:
    ypos 1.15
with charachange

aki "Eh, kinda. I feel bad about ditching the guys doing overtime, so I gotta get back soon."

show akira basic_smile onlayer master
with charachange

aki "But I felt bad about not coming to your cute little Hanako's birthday too, so for now I'm here."

show hanagown smile onlayer master
with charachange

"She grins widely at Hanako, who flowers into a full blush as she pins her eyes downwards toward her lap. Her mouth seems to widen and retract over and over, as if she was trying to suppress a smile out of embarrassment."

"It's a little strange how her reaction seems to be more immediate and forceful than when she's embarrassed by the way she looks. All she manages to give in return is a tiny nod, failing to hide her appreciation to any great extent."

"Not that many people give her positive attention, I suppose. It makes me respect how well Akira can handle her, making her so happy, compared to what little I could do."

show akira basic_laugh onlayer master
with charachange

aki "Now then, before I go…"

play sound sfx_rustling

"She reaches into the bag beside her and grandly displays its contents."

show wine onlayer master:
    yalign 0.5 xanchor 0.0 xpos 1.0 alpha 0.0
    easein 1.0 alpha 1.0 xanchor 1.0
with Pause(1.0)

"Out come two large glass bottles, both with long French names on the labels."

show hanagown normal onlayer master
with charachange

"Hanako's expression is an odd mix of surprise and curiosity, and I suspect mine's no different. Lilly, not seeing the proceedings, is oblivious to what's going on."

show hanagown normal_blush onlayer master
with charachange

ha "Akira… this isn't…"

show lilly basic_surprised_paj onlayer master
with charachange

li "What is it?"

hi "Wine. One red, one white."

show lilly basic_pout_paj onlayer master
with charachange

li "A-Akira! That's…!"

show akira basic_smile onlayer master
with None

show wine onlayer master:
    easeout 1.0 alpha 0.0 xanchor 0.0
with Pause(1.0)

hide wine onlayer master
with None

aki "Relax, relax, it's not like Shizune's here to scold you."

hi "Lilly has a point, that's not exactly allowed on campus."

hi "…or anywhere, really. We're still short of the legal drinking age, remember?"

show akira basic_laugh onlayer master
with charachange

aki "Rich words for someone practically drooling as he examines a bottle."

"She got me there. I am genuinely interested in trying some, even just a little. While Hanako may not be handling one herself, her look does tell me that she's far from opposed to the notion as well."

show lilly basic_displeased_paj onlayer master
with charachange

"Lilly rubs her forehead, giving up the fight that she knows Akira would win due to simply not caring enough about those funny “rules” and “regulations.”"

show lilly basic_displeased_paj onlayer master
with charachange

li "Just don't breathe a word of this to anyone in the school, please. I beg of you."

show akira basic_smile onlayer master
with charachange

aki "I'm not stupid, don't worry."

show akira basic_boo onlayer master
with charachange

aki "That said, I gotta get back to work pretty soon."

show lilly basic_oops_paj onlayer master
with charachange

li "So soon? But you only just arrived…"

show akira basic_resigned onlayer master
with charachange

aki "Sorry, Lilly. Good to see you two again though, and you Hisao."

hi "See you later, then."

ha "Um… g-goodbye… Akira…"

show akira basic_resigned onlayer master at Transform(yalign=1.0)
with charamove

hide akira onlayer master
with charaexit

"She levers herself up with a grunt and waltzes out of the room, leaving us alone with the two items on the table."

show lilly basic_oops_paj onlayer master:
    twoleft
    ypos 1.2
show hanagown normal_blush onlayer master:
    tworight
    ypos 1.15
show bg school_dormlilly onlayer master at center
with charamove

hi "…Interesting."

show lilly basic_arablush_paj onlayer master
show hanagown normal onlayer master
with charachange

"Lilly gives a nervous giggle at her sister's antics as Hanako takes a wine bottle."

show hanagown distant_blush onlayer master
with charachange

ha "So…"

hi "What do you think, Lilly?"

show lilly basic_weaksmile_paj onlayer master
with charachange

"She rests her elbow on the table and pinches the bridge of her nose, thinking things through. She really doesn't seem to be able to keep up with her sister."

show lilly basic_smile_paj onlayer master
with charachange

stop music fadeout 3.0

li "Well… it's already here. We may as well have some."

"No sooner does she say it that I take a quick glance around the room for glasses."

scene bg school_dormlilly_ni onlayer master
with shorttimeskip

play music music_night fadein 0.5

"A small groan above me reminds me that Lilly retired to rest on her bed for a bit a few minutes ago."

"Almost completely drained of energy, I manage to stand up and drag myself to the side of the bed, sitting down and leaning my back against it."

show bg school_dormlilly_ni as ovl1 onlayer master:
    xalign 0.5 alpha 0.4 yalign 0.5 zoom 1.0
    ease 1.0 xalign 0.55 alpha 0.5 rotate 1 zoom 1.05
    ease 1.0 xalign 0.5 yalign 0.5 alpha 0.0 rotate 0 zoom 1.0

show bg school_dormlilly_ni as ovl2 onlayer master:
    xalign 0.5 alpha 0.4 yalign 0.5 zoom 1.0
    ease 1.0 xalign 0.45 alpha 0.5 rotate -1 zoom 1.05
    ease 1.0 xalign 0.5 yalign 0.5 alpha 0.0 rotate 0 zoom 1.0

hi "Good God."

show lilly basic_listen_paj_ni onlayer master:
    center
    ypos 1.2
with charaenter

li "Eugh…"

"Lilly's groan sounds lifeless."

hi "Too much to drink?"

show lilly basic_concerned_paj_ni onlayer master
with charachange

li "My head hurts."

hi "Yeah, too much to drink."

"I rest my head back and idly stare at the ceiling. What an unmitigated disaster."

"Like proper idiots, we all drank the night away with one glass after another. Hanako simply fell to the side asleep, and it's a miracle I don't feel as ill as Lilly."

show lilly basic_sad_paj_ni onlayer master
with charachange

li "Hey, Hisao? I'm sorry about today. I… didn't think this would happen."

hi "It's fine, Lilly. To tell the truth, I had a lot of fun today."

show lilly basic_weaksmile_paj_ni onlayer master
with charachange

li "Really?"

hi "Mmm. I think Hanako did too. No, she certainly did."

show lilly basic_reminisce_paj_ni onlayer master
with charachange

"There's a short silence, before another groan resounds from the supine Lilly."

hi "You okay?"

show lilly basic_weaksmile_paj_ni onlayer master
with charachange

li "As you said, I just drank too much. What's the time?"

hi "The time? Uh, it's…"

"I quickly look at my wristwatch, its numerals barely legible in the gloom."

hi "About midnight."

show lilly basic_concerned_paj_ni onlayer master
with charachange

li "Curfew's in effect, then."

hi "Yeah, guessed as much. We'll all have to sleep here for tonight."

"As soon as I say it, I hear the sheets moving as Lilly starts to sit up."

show lilly basic_oops_paj_ni onlayer master
with charachange

li "Hanako…"

hi "Ah, no, go back to sleep, don't try to get up."

show lilly basic_displeased_paj_ni onlayer master
with charachange

li "Hisao, I have to…"

hi "You're in worse shape than me by any stretch. Get some rest."

show lilly basic_oops_paj_ni onlayer master
with charachange

li "But what about…"

hi "I'll grab some spare blankets and put them over her, don't worry."

hide lilly onlayer master
with charaexit

"As I give a deep yawn and stand to retrieve them, I hear her lie back down with a soft thud."

li "Thank you, Hisao."

hi "No problem, it's the least I can do. You look outright wasted."

li "I'm not… wasted… just a little bit… tired."

"She starts pouting, a slight slur beginning to distort her words as the alcohol takes hold of her again. I grab a couple of blankets rolled up at the end of her bed."

"Quietly walking over to Hanako, I carefully lay the blankets over her peacefully sleeping figure, making sure not to wake her up."

"The thick smell of alcohol coming off her breath makes me doubt she'd wake up no matter what I did, though."

"I stand and take one last measure of the room."

stop music fadeout 4.0

"Two girls, both very drunk, and one guy sleeping overnight with them in the female students' dorm. What a scandal that'd be if it broke out."

"As I move to sit back down at the side of the bed, I steal one last glance at Lilly."

"Her sprawling, disheveled figure lies resting peacefully, slightly turned to the side."

"I crouch down to get a better look."

play music music_comfort

scene ev lilly_sleeping onlayer master:
    truecenter zoom 1.05 subpixel True
    acdc_warp 20.0 zoom 1.0
with locationchange

"Her white skin blends in with the white pillow of the bed, a look of slumber-born peacefulness on her face."

"Usually she seems so confident and forward, always there and caring for Hanako. Now, though, she seems painfully delicate."

"I think back to Hanako's presents."

"I thought it'd be a nice occasion for her, but I'd hardly expected it to be so moving."

"One birthday after another, year after year."

"Just she and Lilly, all alone."

"…I guess it wasn't just the presents she liked."

scene bg school_dormlilly_ni onlayer master
with locationchange

"Resigning myself to an uncomfortable sleep, I sit down at the side of the bed once again and rest my tired arms beside me."

li "Hey, Hisao."

"Lilly's voice is so quiet I can barely hear it. She must be on the verge of sleep."

scene ev lilly_sleeping onlayer master:
with locationchange

hi "Yeah?"

scene ev lilly_sleeping_smile onlayer master
with charachange

li "Thank you."

hi "Thank you? For what?"

li "For being here."

hi "…That's okay."

scene bg school_dormlilly_ni onlayer master
with locationchange

"As I hear a deep breath, it's obvious Lilly's gone to sleep."

"After closing my eyes, it doesn't take long for slumber to take me as well."

stop music fadeout 2.0

window hide

scene black onlayer master
with shuteye



label en_L5:

window hide None

scene black onlayer master
with Pause(4.0)

stop music

window show

mystery "Hisao?"

mystery "Hisao, are you…?"

"The soft, barely audible voice lingering in my ears slowly wakes me. I wish I could be awoken like this more often."

"With a mumble, I slowly open my…"

scene bg school_dormlilly onlayer master
show lilly superclose onlayer master
with openeye_shock

show lilly superclose_shock onlayer master
with Dissolve(0.2)

$ doublespeak(hi, li, "Whoa!", "Ah!")

play sound sfx_impact2

show lilly superclose_ouch onlayer master
with vpunch

show lilly basic_concerned_paj onlayer master:
    xalign 0.5 yanchor 1.0 ypos 1.2
    ease 0.4 ypos 1.4
with Dissolve(0.2)

"Taken by surprise at the face hovering curiously mere millimeters from mine, I make our heads collide with a harsh thud. The impact of our foreheads causes both of us to fall backwards and yelp in pain, Lilly sounding more like a squeak toy than a person."

hi "Ow, ow, ow."

play music music_happiness fadein 6.0

"I slowly rub my forehead with one hand, supporting myself with the other. Lilly lies a few feet ahead doing just the same, her face obviously pained."

hi "Ah… sorry. Your face was kinda close and I acted on reflex. You okay?"

show lilly basic_concerned_paj onlayer master:
    ease 1.0 ypos 1.2
with Pause(0.5)

li "My head…"

"It seems she's not actually okay. Come to think of it, I doubt that the impact alone is what's causing her head so much pain."

hi "Hangover? You drank a fair bit, last night."

show lilly basic_sad_paj onlayer master:
    ypos 1.2
with charachange

"She silently nods in confirmation as I lever myself up."

show lilly basic_concerned_paj onlayer master:
    ease 1.0 ypos 1.0
with Pause(0.5)

"I offer a hand to her, and help her back onto her feet. Glancing behind her, I find that Hanako's still fast asleep."

show lilly basic_reminisce_paj onlayer master at center
with charachange

li "It's not fair… I only drank as much as you did…"

hi "That's very different from what I remember. And anyway, girls have a lower tolerance than men."

show lilly basic_displeased_paj onlayer master
with charachange

li "That doesn't help."

hi "Fine, I'll get you a glass of water. Just be careful not to trip over Hanako."

hide lilly onlayer master
with charaexit

"I rub the sleep out of my eyes, or at least some of it, as I walk to the counter. Tending to someone with a hangover isn't the way I like to spend a morning."

"It only takes a few seconds for the glass to fill, the clear water reflecting the sliver of light that makes it through the thin curtains."

"It looks like Lilly's taken a seat on the side of the bed. I walk over to her while taking care to step over the peacefully sleeping Hanako, and place the glass into her outstretched hands."

show lilly basic_weaksmile_paj_close onlayer master:
    center
    ypos 1.2
with charaenter

li "Thank you."

hi "No problem."

stop music fadeout 12.0

"I take a seat next to her, the soft bed having a surprising amount of give."

"She drinks slowly and methodically. A long silence passes with only Hanako's soft breathing to be heard."

show lilly basic_reminisce_paj_close onlayer master
with charachange

"With some measure of guilt, I look at Lilly's face and attempt to read her expression. Her brow is furrowed, and she looks to be lost in thought."

show lilly basic_emb_paj_close onlayer master
with charachange

"For a moment I hesitate, but eventually place a hand on her shoulder in an attempt to reassure her. I didn't expect her to flinch rather noticeably at that, though."

hi "Ah, sorry. I didn't mean to—"

show lilly basic_sad_paj_close onlayer master
with charachange

"Lilly quickly shakes her head, in a manner somewhat more violent than usual for her."

"She takes a long breath to steady herself before letting her head sink."

show lilly basic_weaksmile_paj_close onlayer master
with charachange

li "I must look terrible right now…"

"I move to protest, but quickly realize that it would be futile to do so. That said, I want her to open up more."

hi "If you want to talk about anything, I'm here."

show lilly basic_displeased_paj_close onlayer master
with charachange

"Lilly gives a self-deprecating snort, as if to mock her own emotions."

show lilly basic_reminisce_paj_close onlayer master
with charachange

li "There's just… a lot happening right now."

show lilly basic_sad_paj_close onlayer master
with charachange

li "I'm sorry for being so strange recently, especially back when we were in town. Even now I'm a bit confused about everything."

hi "Believe me, I know how that feels."

show lilly basic_weaksmile_paj_close onlayer master
with charachange

"She smiles wistfully, resting a cheek on the backs of her fingers."

li "We're a couple of broken young fools, aren't we?"

hi "Come on, don't say that. Come graduation, we'll be back out into the real world."

"The real world? Sometimes I surprise myself with the way I think about things. I guess the strange, divorced feeling of Yamaku and the surrounding town compared to the outside world still hasn't become natural."

"Maybe it never will. It's strange, in hindsight; being isolated from society like this doesn't feel as bad as it probably should. A wry grin on her face, Lilly seems to share the same sense of amusement at the idea."

"Eventually, though, her smile drops."

show lilly basic_displeased_paj_close onlayer master
with charachange

li "I'll be going back to Scotland for a week or two, soon."

hi "Is that why we had to reschedule Hanako's birthday party?"

"She gives an affirmative nod."

hi "You'll be able to see your family again, at least. You're not looking forward to it?"

show lilly basic_concerned_paj_close onlayer master
with charachange

li "I haven't met my family in six years. I don't even know how to act around them any more."

"Wait… what? My mouth hangs open as I try to process what she said."

play music music_moonlight fadein 6.0

"If she's eighteen, that means she'd have been only twelve when they left. I may have seen very little of my parents, what with them both working long hours, but that's…"

"I feel utterly useless as I struggle to find some way to respond."

hi "That's… but, why?"

show lilly basic_reminisce_paj_close onlayer master
with charachange

li "Why did they leave, or why are they inviting Akira and me back?"

hi "Both, I suppose."

show lilly basic_sleepy_paj_close onlayer master
with charachange

li "My father's business has its headquarters in Scotland, and an executive position became available for him there. In the end, he had to move permanently."

li "My mother followed him, but Akira and I stayed in Japan for the sake of both Akira's job within the Japanese branch of my father's company, and my education."

show lilly basic_concerned_paj_close onlayer master
with charachange

li "As for the latter… one of my aunts is gravely sick."

hi "Ah. I'm… sorry."

show lilly basic_weaksmile_paj_close onlayer master
with charachange

li "Don't be. It feels strange, really. We're being summoned there for her, yet we've barely met before. I can't even remember the sound of her voice."

"Equally strange is the total lack of antipathy she feels towards her family for doing such a thing. I can't help feeling slightly humbled."

"That said, her wistful exterior is just hiding her emotions. Seeing her like this is depressing."

stop music fadeout 5.0

"Knowing what to do, I lift myself off the bed. Lilly notices the bed's movements, her head perking up and her hand reaching sideways to feel where I was."

show lilly basic_oops_paj_close onlayer master
with charachange

li "Hisao…?"

play sound sfx_rustling

"I walk over to my bag, still leaning against the wall. Unbuckling the front flap and retrieving the opaque bag from within, I take the small, plain box in my hands."

hi "Hold your hands out, Lilly."

show lilly basic_surprised_paj_close onlayer master
with charachange

"She looks surprised for a moment, but eventually acquiesces."

show lilly basic_surprised_paj_close onlayer master:
    ease 1.0 xpos 0.4
show bg school_dormlilly onlayer master:
    center
    ease 1.0 xpos 0.4
with Pause (1.0)

show musicbox closed behind lilly onlayer master:
    alpha 0.0  zoom 0.5  xanchor 0.0 xpos 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.6 alpha 1.0
show boxstrip behind lilly onlayer master:
    alpha 0.0  zoom 0.5  xanchor 1.0 xpos 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.6 alpha 1.0
with Pause (1.0)

"I'm amused by her look of curiosity when I place the music box into her open palms, her typically delicate way of handling it making it seem as if it were fragile enough to break if breathed on."

stop music fadeout 2.0

"She wordlessly brings it in front of her face, her slender fingers feeling out its contours and patterning."

"Eventually her fingers find the recessed line between the lid and body of the box, and her thumb effortlessly pops open the lid."

show musicbox open onlayer master:
    xpos 0.5 ypos 0.6 alpha 1.0
with charachange

play music music_musicbox

"I take a seat on the bed next to her, watching her face silently and intently."

"She sits completely motionless as she listens to the diminutive tinny melody, her mouth just slightly open."

show musicbox closed onlayer master
show lilly basic_smileclosed_paj_close onlayer master:
    xpos 0.4
with charachange

play sound sfx_switch
stop music

show musicbox closed onlayer master:
    ease 1.0 ypos 0.7 alpha 0.0
show boxstrip onlayer master:
    ease 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

show lilly basic_smileclosed_paj_close onlayer master:
    ease 1.0 xpos 0.5
show bg school_dormlilly onlayer master:
    ease 1.0 center
with Pause (1.0)

hide musicbox onlayer master
hide boxstrip onlayer master

"It takes a long while before she closes the lid with a small snap, bringing the curtain down on the miniature performance playing in her hands."

"The smile on her face, gentle and wistful, shows that I made the right decision."

hi "Think of it as a going away present for your trip to Scotland."

show lilly basic_smile_paj_close onlayer master:
    xpos 0.5
with charachange

li "I will…"

play sound sfx_rustling

show lilly basic_smile_paj_close onlayer master:
    twoleft
    ypos 1.2
show bg school_dormlilly onlayer master at bgleft
with charamove

"A restless shuffling can be heard from the floor in front of us, the sound having woken Hanako."

show hanagown distant onlayer master:
    tworight
    ypos 1.3
    easein 1.0 ypos 1.1
with Dissolve(1.0)

"She climbs out of the blankets I put over her, looking befuddled and wiping the sleep from her eyes."

hi "I see you're finally up."

show hanagown normal onlayer master:
    ypos 1.1
with charachange

ha "Hmm? What?"

show lilly basic_planned_paj_close onlayer master
with charachange

"Hanako looks around the room with her eyes only half open, her mind far from being as awake as her body. Her dazed state makes me and Lilly chuckle."

show lilly basic_planned_paj_close onlayer master:
    ease 1.0 twoleft
with Pause(1.0)

show lilly basic_planned_paj onlayer master at twoleft
with charadistant

"As Lilly gets off the bed and tends to Hanako, I take one last look around the room."

hi "I guess I'd better get going, then. There'll be questions if I am seen leaving the girls' dormitories in the morning."

show lilly basic_smile_paj onlayer master
with charachange

li "Goodbye, Hisao."

show hanagown smile onlayer master
with charachange

ha "Oh… goodbye."

"I stand and walk to the door, picking up my somewhat lighter bag along the way."

scene bg school_girlsdormhall onlayer master
with locationchange

"After I leave the room and enter the hallway, though, I hear Lilly's footsteps behind me."

hi "Hmm? What's wrong?"

show lilly basic_smileclosed_paj_close onlayer master:
    yalign 1.0 xpos 0.3 xanchor 0.5
    easein 1.0 xpos 0.5
with Dissolve(1.0)

"Without a word, she strides up to me. I freeze as I feel her hand slide onto my cheek, seemingly every nerve taking in the feeling of her fingers and palm upon it."

play music music_romance

"Immediately after, her face slowly moves next to mine, a light, momentary touch of her lips brushing against my other cheek."

"For a moment, everything seems to stand still. I absentmindedly bring my fingers to my cheek, as if to try and recapture that fleeting feeling."

hi "Lilly…"

show lilly basic_smile_paj_close onlayer master at center
with charachange

li "That's my thank you, Hisao."

hi "Thank you…?"

show lilly basic_cheerful_paj_close onlayer master
with charachange

li "For your present. Have a nice day in school."

show lilly basic_cheerful_paj_close onlayer master:
    easeout 1.0 xpos 0.3 alpha 0.0
with Pause(1.0)

hide lilly onlayer master
with None

"And with that, she disappears behind her door and gently closes it, the muffled voices of her and Hanako audible through it much as they were yesterday night."

"…"

"…I think I'd be hard pressed not to have a nice day, after that."

show bg school_courtyard onlayer master
with locationskip

"I walk away with a certain spring to my step. I think there were some people around that glanced at me emerging from the girl's dormitory building, but I find it difficult to care."

stop music fadeout 2.0

scene black onlayer master
with dissolve



label en_L6i:

scene black onlayer master
with None

mi "Hicchan~."

hi "Go away."

mi "Hicchan~."

hi "Leave me alone."

mi "Come on, Hicchan~."

hi "Hmph, let me sleep."

"After two nights of not being able to sleep at all, the last thing I want is to be woken when I finally manage to."

"It may be the last period of class, with a textbook as my pillow, but I'll take whatever sleep I can get by this point."

mi "See Hicchan, even Shicchan wants you to get up~!"

"I don't care what Shizune wants, leave me alone."

mi "Geez, Hicchan, I'll just have to wake…"

"Wait, Misha's going to…?"

mi "…you…"

"This is bad!"

play music music_running

scene bg school_scienceroom onlayer master
show misha hips_grin_close onlayer master at center
with vpunch

hi "I'M UP!, I'M UP! YOU DON'T… have to…"

"I can feel my face flowering into a scarlet red blush."

"The students still in class are sitting bolt upright and staring at the shouting fool who was sleeping just moments before."

hi "…Dammit."

play sound sfx_impact2
with vpunch

"I let my head smack back down on the table with a noticeable thud."

show misha cross_laugh_close onlayer master
with charachange

mi "Wahahahahaha~!"

"Misha's trademark uncontrolled laughter reverberates through the classroom."

show shizu invis behind misha onlayer master:
    center
    xpos 0.95
with None

show misha hips_grin_close onlayer master at twoleft
show shizu adjust_happy onlayer master at tworight
show bg school_scienceroom onlayer master at bgleft
with dissolvecharamove

"As I turn my mournful eyes to the bespectacled Shizune beside her, she carefully adjusts her glasses, desperately trying to maintain a look of serious disapproval."

"Narrowing my eyes, I can see the badly-hidden grin spreading across her face."

hi "Et tu, Shizune?"

show shizu behind_blank onlayer master
with Dissolve(0.3)

"Shizune looks away quickly as she crosses her arms tightly, barely on the edge of her control."

show misha cross_laugh_close onlayer master
with charachange

mi "Wahahahahahaha~!"

"Misha's laughter doubles in volume as she glances at Shizune. All I can do is drag my hand down my face in resignation."

hi "You two…"

show misha sign_smile_close onlayer master
with charachange

mi "Who was the one who slept in class, Hicchan~?"

hi "Yeah, yeah, it was me."

show misha hips_frown_close onlayer master
with charachange

mi "Poor Shicchan was having a fit trying to wake you up. Weren't you?"

show shizu basic_angry onlayer master
with charachange

"I move my eyes back to the standoffish Shizune, who with a single huff of confirmation returns to looking away with her arms crossed."

hi "Why was Shizune trying to wake me up?"

show misha hips_smile_close onlayer master
with charachange

mi "Shicchan wanted to give you the handouts the substitute teacher gave out while Hicchan was sleeping."

hi "Handouts?"

play sound sfx_paper
show shizu behind_frown_close onlayer master
show misha hips_frown_close onlayer master
show blanknote onlayer master at truecenter
with vpunch

"I suddenly find two sheets of paper thrust down in front of my face."

show blanknote onlayer master at Transform(xpos=0.3)
with charamove

"Following the hand holding them, I see the still-pouting figure looking down at me with a distinct scowl. I guess I really am in the wrong here."

hi "…Ah. Um, sorry about that."

stop music fadeout 8.0

"No dice. Her irritated face still holds. I clasp my hands together and flick my head downwards in apology."

hi "Very, very sorry."

show shizu behind_frustrated_close onlayer master
with charachange

show blanknote onlayer master:
    easeout 0.5 ypos 0.8 alpha 0.0
with Pause(0.5)

hide blanknote onlayer master
with None

"She huffs and simply drops the papers on the desk."

hi "Damn."

show shizu adjust_angry_close onlayer master
show misha sign_smile_close onlayer master
with charachange

"I look up over my hands to see Shizune and Misha signing frantically to each other, a look of frustration on Shizune's face."

show shizu basic_angry_close onlayer master
with charachange

shi "…!"

"It looks to be less of a dialogue and more of a tirade, punctuated with sidelong glances at me. To say it's unsettling is an understatement."

hi "Um…"

show shizu behind_frown_close onlayer master
show misha hips_frown_close onlayer master
with Dissolve(0.3)

"The two suddenly stop signing and look at me in unison, both having exactly the same look of disapproval. In one fluid motion, Misha's hand suddenly extends high above me and comes rocketing down."

scene black onlayer master
with None

play sound sfx_impact2
play music music_running

"Before I can even hope to react, my head is sent bouncing up and down like a jack-in-the-box." with vpunch

"I quickly bring my hands to my head, more out of reflex than actual pain."

hi "Ow! What was that for!?"

scene bg school_scienceroom onlayer master at bgleft
show shizu adjust_smug_close onlayer master at tworight
show misha hips_grin_close onlayer master at twoleft
with openeye

"I open my eyes to see the two grinning at each other while exchanging an enthusiastic thumbs-up."

show misha hips_smile_close onlayer master
show shizu behind_smile_close onlayer master
with charachange

mi "Shicchan says she forgives you now, Hicchan~!"

hi "Could you forgive me with a little less force next time?"

show misha cross_laugh_close onlayer master
with charachange

mi "Wahahahaha~!"

"I look at the two with a blank face. Misha and Shizune: one, Hisao: nil."

show shizu adjust_happy_close onlayer master
with charachange

shi "…"

show misha hips_grin_close onlayer master
with charachange

mi "Oh, Shicchan also says that you should check your student mail more often~!"

show letter_insert onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"She produces a bright yellow envelope and hands it over with an exuberant grin."

"Strange. Who could have written me a letter? Now is not the time and most definitely not the place to find out, though."

show letter_insert onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert onlayer master
with None

"Giving up on the nap so cruelly stolen from me, I rub my forehead and slowly get up, putting the sheets and envelope in my bag before swinging it over my shoulder."

show misha cross_laugh onlayer master at Transform(yalign=1.0, xanchor=0.5, xpos=0.355)
show shizu behind_smile onlayer master at Transform(yalign=1.0, xanchor=0.5, xpos=0.615)
with charadistant

"I take a step back and move to depart with a small bow, while Misha clutches her sides laughing and Shizune nods back in a curt farewell."

stop music fadeout 3.0
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3 onlayer master
show crowd onlayer master
with locationchange

"I join the flow of students exiting the open door, and turn the corner into the hallway."

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

show hanako emb_downtimid onlayer master at center
with charaenter

"…only to end up face to face with Hanako."

hi "Whoa. Uh, hey Hanako."

show hanako emb_timid onlayer master
with charachange

ha "Good afternoon… Hisao."

show hanako emb_downtimid onlayer master
with charachange

"Silence falls between us as busily chatting students pass us by. She's fidgeting constantly, her eyes drawn to her rather unremarkable footwear."

"I take the bridge of my nose in my fingers while I blink my eyes heavily in an attempt to make things seem clearer. I'm barely staying awake as it is."

hi "Hanako, you want to say something. What is it?"

show hanako emb_blushing onlayer master
with charachange

ha "U-um… I wanted to… give you this…"

hi "Hmm?"

show hanako basic_worry onlayer master
with charachange

"She holds out a small rectangular piece of paper. I blink again to make out the text through barely open eyes, slowly starting to make out what's written."

window hide

$ written_note("\nEggs x2\nBread loaf x1\nWhole-grain cereal x1\nThyme x1\n")

window show

play music music_happiness fadein 0.5

hi "…A shopping list?"

"I look upwards, raising an eyebrow."

show hanako emb_timid onlayer master
with charachange

ha "I usually go shopping with Lilly but I can't come, so…"

hi "You want me to run errands for you?"

show hanako defarms_shock onlayer master
with charachange

ha "I-it's okay if you don't want to! I just thought that, maybe, um…"

"She's panicking. I sigh. Yet another battle lost, though this time by a weakly-fought surrender."

"I smile tiredly and rest a hand on her head to calm her down."

hi "It's fine, I was going to go anyway. Just the stuff on this list?"

show hanako def_worry onlayer master
with charachange

"She nods then bows deeply, twice, as if to make her gratitude perfectly clear."

show hanako cover_distant onlayer master
with charachange

ha "W-we were going to meet outside the school gates at six… thank you, I was going to get it, but I need to study for the test tomorrow."

hi "Test? Ah, that's right, science. How're you doing with it?"

show hanako cover_bashful onlayer master
with charachange

"She brightens ever so slightly."

show hanako basic_bashful onlayer master
with charachange

ha "I've been… spending more time on it than before. I think I can do… okay."

hi "Good work, then."

show hanako basic_smile onlayer master
with charachange

"She too starts smiling, and much more earnestly than I at that."

"I have full confidence that I can do fine in it without any extra studying, but the fact that she's putting in the effort instead of just reading in the library is heartening."

hi "I'll grab your stuff and take it to your dorm in the evening. Seeya."

stop music fadeout 3.0
$ renpy.music.set_volume(1.0, 3.0, channel="ambient")

hide hanako onlayer master
with charaexit

"With a small wave, we part ways."

"I'll go do my homework before meeting Lilly. I should be able to take care of it in time."

stop ambient fadeout 1.0

scene bg school_gate_ss onlayer master
with shorttimeskip

play music music_soothing fadein 2.0

"Wrangling with a particularly complicated math problem has caused me to be a little bit late for my meeting with Lilly."

"Only a couple of minutes, but enough to make me step smartly out into the courtyard and to the school gate."

scene bg school_road_ss onlayer master
with locationchange

"I make a right turn and start my way towards the small town below, leaving a few students turning the other way to the bus station."

"I slip my right hand into my pocket as I walk in the orange sunlight of dusk."

"Thankfully the sweltering summer heat's started to die down, making way for a pleasant cool breeze."

show lilly back_listen_ss onlayer master at center
show lillyprop back_cane_ss onlayer master at center
with charaenter

"When I stretch my hands high above my head, a familiar figure takes form, cane in her right hand."

hi "Ah, Lilly."

show lilly cane_listen_ss onlayer master
hide lillyprop onlayer master
with charachange

"She stops and turns around, swiveling her head slightly to try and work out exactly where the voice came from."

hi "Hey. It's me."

"I quickly catch up to her, coming in beside her and matching her slow pace as we resume walking."

show lilly cane_smile_ss onlayer master
with charachange

li "Good afternoon, Hisao."

hi "Hi there."

scene bg misc_sky_ss onlayer master at Fullpan(10.0, dir="right")
with locationchange

"I glance up at the sky."

"A distinct tinge of orange discolors the clouds, washing the footpath in its light. Long shadows from the trees fall across the wide road down the hill."

scene bg school_road_ss onlayer master
show lilly cane_smileclosed_ss onlayer master
with charachange

li "So, Hisao, what brings you here?"

hi "Just going to town to grab some groceries. Hanako sent me."

show lilly cane_surprised_ss onlayer master
with charachange

li "Hanako sent you?"

hi "Yeah, said she needed to study for a test tomorrow. I was going to come down anyway, so I'll just buy her stuff as well."

"Unspoken is that Lilly really could use some help to get food, but it's an obvious fact that neither of us needs to state."

show lilly cane_weaksmile_ss onlayer master
with charachange

li "It's good to hear she's studying for it."

hi "I thought the same thing when she asked me to come with you."

hide lilly onlayer master
with charaexit

"We continue walking down the street, the familiar sound of her cane echoing through the air as we go. Except for the occasional passing car and the leaves whispering in the branches, there's a blissful silence."

"Thank God I can finally relax for the first time today."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene evbg lilly_sunsetwalk onlayer master:
    truecenter subpixel True zoom 0.9
    acdc_warp 20.0 zoom 1.0
show evfg lilly_sunsetwalk onlayer master:
    truecenter subpixel True zoom 0.85
    acdc_warp 20.0 zoom 1.0
with locationskip

"I glance over at Lilly."

"That porcelain face of hers never seems to lack that air of relaxed confidence. I guess the same could be said of her personality, too."

"As she silently walks, her face remaining pointed to the street ahead of her, I look ahead and savor the cool air blowing over my face."

"This is probably the calmest moment I've had since the about-face my life took so recently."

"To have it while walking to get some groceries. What a weird life."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_road_ss onlayer master
with locationskip

"I feel the crumpled-up note rubbing against my hand in my pocket, and pull it out to check its contents."

hi "Let's see here… eggs, bread, cereal, thyme, lettuce, shaved ham…"

show lilly cane_weaksmile_ss onlayer master
with charaenter

li "That sounds like quite a bit to carry back along with your own."

hi "Yeah. Just how much does this girl eat anyway?"

"My mind suddenly clicks that yes, there actually is a person beside me."

hi "W-wait, I mean…"

show lilly cane_giggle_ss onlayer master
with charachange

"She laughs wholeheartedly."

show lilly cane_planned_ss onlayer master
with charachange

li "My my, Hisao."

"Her giggles punctuate her words, though she's making little effort to suppress them."

show lilly cane_satisfied_ss onlayer master
with charachange

li "Quite direct today, aren't we?"

hi "Yeah, you got me there. Still, it is quite a bit."

show lilly cane_smileclosed_ss onlayer master
with charachange

li "Usually I go shopping with Hanako, so I know what she buys. It's the same thing every week."

hi "Huh. She a good cook?"

show lilly cane_weaksmile_ss onlayer master
with charachange

"She gives a nervous giggle."

li "It's usually me who ends up cooking. I used to do so for Akira, so it's no problem doing it for Hanako as well."

hi "You can cook? But…"

show lilly cane_cheerful_ss onlayer master
with charachange

"A short hum with an amused lilt emanates from beside me. I wonder if the fact that she seems amused by my comments so often is actually genuine, or rather just from a want to make me more comfortable in addressing her blindness?"

show lilly cane_smileclosed_ss onlayer master
with charachange

li "There are ways around it. Some meals are more difficult to cook than others because of being unable to see what I'm doing, but it usually only takes a little more time. Fingers can double as very useful measurement tools, for example."

"It makes sense, but she'd have to be pretty careful not to hurt herself. I wonder how many times that's happened, given that it sounds like she's cooked alone for possibly years while Akira worked and her parents were gone."

"With that, the conversation trails off."

"Compared to the awkward silences of Hanako, Lilly seems genuinely content to say what she thinks and stay quiet when there's nothing to say."

"The slick road under my feet is bathed in an orange glow, the occasional fallen leaf crunching underfoot as we walk. I let out a deep yawn, my lack of sleep coming back to haunt me."

show lilly cane_smile_ss onlayer master
with charachange

li "Did you not get much sleep last night?"

hi "I couldn't sleep at all for the last two nights. Probably insomnia."

stop music fadeout 8.0

show lilly cane_oops_ss onlayer master
with charachange

"Lilly's face suddenly becomes worried. It feels like a personal failure every time she gets worried about my well-being, even if it's genuinely nice to know someone cares."

li "You have insomnia? Aren't you going to see the nurse about it?"

hi "Nah, no real need. It's happened before a few times. My meds screw with my sleeping occasionally."

show lilly cane_concerned_ss onlayer master
with charachange

li "…Ah. I'm… sorry."

hi "Come on, it's not your fault. At least I shouldn't have any trouble getting to sleep tonight."

show lilly cane_sleepy_ss onlayer master
with charachange

li "You do worry me sometimes."

hi "I… worry you?"

"I reach around and scratch the back of my neck. I kind of want to address this."

hi "Hey, Lilly…"

show lilly cane_smile_ss onlayer master
with charachange

li "Hmm?"

hi "I don't mean to sound weird, but… please try to forget about my heart condition."

show lilly cane_oops_ss onlayer master
with charachange

"She looks kind of lost. I hardly blame her."

hi "I guess what I'm trying to get at is… just don't treat me differently because of it."

show lilly cane_emb_ss onlayer master
with charachange

"She bows her head slightly, her white cheeks reddening almost imperceptibly."

li "It's only natural to worry about those around you…"

hi "Well, it's still nice to know there's someone like that out there."

show lilly cane_smileclosed_ss onlayer master
with charachange

"It may be somewhat embarrassing to say, but it's the truth. Lilly takes a breath to regain her composure and manages a gentle smile, though her cheeks remain flushed."

"The final downhill walk to the store passes in silence."

scene bg suburb_konbiniint onlayer master
with shorttimeskip

play music music_daily fadein 4.0

"Storewoman" "Welcome!"

hi "I suppose I'll get my stuff first and Hanako's on the second round."

show lilly cane_smileclosed onlayer master at center
with charaenter

"I grab two well-worn red baskets from the stack beside the entrance and pass one to Lilly."

show lilly cane_smileclosed onlayer master at Transform(ypos=800)
with charamove

show lilly basic_smileclosed onlayer master at Transform(ypos=800)
with charachange

show lilly basic_smileclosed onlayer master at center
with charamove

"Just as she did before, she lays it on the ground and slides her retracted cane between the basket's handles before picking it back up with her right hand."

$ renpy.music.set_volume(0.5, 0.5, channel="music")

show lilly basic_smileclosed onlayer master at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with None

show lilly basic_smileclosed_close onlayer master at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with Dissolve(1.0)

"When she takes hold of my arm in her own, I'm surprised at just how fast this kind of casual contact became so natural. Mostly due to necessity, no doubt."

show lilly basic_smile_close onlayer master at twoleft
with charachange

li "Shall we?"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

hi "Sure."

"While we navigate around the store, the odd person occasionally passing us pays us no heed at all. It's nice, compared to the stares and whispers around the city."

show lilly basic_smileclosed_close onlayer master
with charachange

"As we reach each aisle, I quickly check with Lilly what she needs and grab it along with what I want, putting our items into their respective baskets."

"It's an odd feeling, to be depended on so much for something so basic as shopping. Hanako would be practically a necessity for her to pick out what she wants, after all."

hi "Right, I'm pretty much done with both my stuff and Hanako's. You needing anything else, Lilly?"

show lilly basic_smile_close onlayer master
with charachange

li "No, this should be everything."

hi "Off we go, then."

"Oddly, there's a queue a mile long. Considering the store's only large enough to warrant one counter, seems like it'll take a while."

hi "Damn."

show lilly basic_surprised_close onlayer master
with charachange

"Lilly gives an inquisitive look, unable to see the reason for my complaint."

hi "The queue's really long. Looks like we'll have to wait."

show lilly basic_weaksmile_close onlayer master
with charachange

li "How strange."

"Sharing the same mood of resignation, we reluctantly take our place at the end of the line."

$ renpy.music.set_volume(0.5, 10.0, channel="music")

"One person finishes, the line moves up. Another person finishes, the line moves up."

"By the time we finally reach the head of the line, I'm so close to dozing off that Lilly has to gently pat me on the back for me to move up."

show lilly basic_oops_close onlayer master
with charachange

li "Hisao… Hisao!"

$ renpy.music.set_volume(1.0, 0.3, channel="music")

hi "Hmm? Ah, sorry."

show lilly basic_displeased_close onlayer master
with charachange

"She gives a short sigh of consternation as I move up, getting the groceries for Hanako and me put into separate bags."

"Storewoman" "Thank you, please come again!"

stop music fadeout 5.0

scene bg suburb_konbiniext_ni onlayer master
show lilly basic_smileclosed_ni onlayer master
with locationskip

"By the time we emerge from the store, Lilly's holding a single bag while I struggle to carry four, both hands well and truly full. It's a lot of work, but thankfully the items in them are light."

"Even without looking skyward it's obvious that a surprising amount of time's passed, the road outside being dark and lit by streetlamps."

show lilly cane_smile_ni onlayer master
with charachange

"Once Lilly retrieves her cane, we set out back to the dormitories the way we came, leaving the welcoming warm glow of the store."

scene bg school_road_ni onlayer master
with locationskip

play music music_dreamy fadein 8.0

"Despite the road being empty of cars, the full bags abundantly make up for the lack of noise, constantly clunking and squeaking together."

show lilly cane_ara_ni onlayer master
with charaenter

li "My my, Hisao, it's good to find that you're eating well."

hi "I'm a growing guy after all, I need to eat all I can!"

show lilly cane_weaksmile_ni onlayer master
with charachange

li "Hmm… it must be nice, being a man."

hi "W-what?"

"Seemingly not noticing, or ignoring, my surprise at the completely out-of-left-field comment, she continues on without missing a beat."

show lilly cane_smile_ni onlayer master
with charachange

li "Weight doesn't really bother you when eating, most of the time."

hi "I get what you mean. Women tend to worry about stuff like that more than we do, I guess."

show lilly cane_smileclosed_ni onlayer master
with charachange

li "Exactly. It makes me somewhat envious, to be honest."

hi "Well, it's not like we can outright ignore it."

"With an affirmative nod, we continue on our walk."

hi "Huh, that's right."

show lilly cane_smile_ni onlayer master
with charachange

li "What is it?"

hi "Hanako mentioned your birthday was earlier this year. Do anything special for it?"

show lilly cane_listen_ni onlayer master
with charachange

"She gives a long pause, lost in thought for a few seconds as she recalls the event."

show lilly cane_weaksmile_ni onlayer master
with charachange

li "Not really. It was just Hanako and me having a little party during the night after school."

hi "Your birthday's supposed to be a big event, you know."

"Sounds like a pretty lonely way to spend a birthday, just her and Hanako staying overnight."

"Birthdays always felt like a family occasion for me. They were a time when, in spite of their full-time jobs, both my parents would make an effort to be there for the day or at least for a party beforehand."

"It reminds me of how Lilly mentioned she hadn't seen her family in such a long time, and even ended up moving away from Akira's house afterwards."

"But I guess it's the same in situations as mundane as these. Considering her inability to read the packaging, just getting groceries would be a pain without somebody else around."

"In the end, she just has Hanako and me, and Akira when she's off from work."

"Be that as it may, she still seems to have many more distant friends among the students, not to mention people like Yuuko."

"It seems to be her own choice that there's such a separation between those who are close to her, and those who she only socializes with."

"It humbles me a little to see how much Lilly seems to have her life set up and going just as she wants."

"Yet Hanako is there for her to celebrate her birthday, and I'm here helping her with shopping. It's a weird kind of symbiosis, I suppose."

show lilly cane_oops_ni onlayer master
with charachange

li "Are you all right, Hisao?"

hi "Sorry?"

li "You just seemed to go very quiet, that's all."

hi "Ah, sorry. I was just thinking."

show lilly cane_smileclosed_ni onlayer master
with charachange

li "Oh?"

label en_choiceL6_1:
menu:
    with menueffect
    "Ah, now I've piqued her curiosity. It feels kind of overly personal to talk about though…"
    "Avoid the subject.":


        return m1
    "Tell the truth.":

        return m2

label en_L6a:


hi "I was just thinking about some of the stuff that's happened, don't worry."

stop music fadeout 2.0

show lilly cane_listen_close_ni onlayer master
with characlose

li "Hmm?"

"She leans in even closer, forcing me to move sideways."

hi "Come on, don't you ever do that as well?"

show lilly cane_cheerful_close_ni onlayer master
with charadistant

li "You make it sound as if you're hiding something…"

play music music_lilly fadein 4.0

"Erk. Why must this girl be so perceptive?"

"Glancing back at her face though, she wears a cute, playful smile."

"She's… playing with me? Even so, I'd rather not pursue this with her."

hi "I told you, it's nothing."

show lilly cane_displeased_close_ni onlayer master
with charachange

"Lilly furrows her brow in disapproval."

li "Is that so?"

hi "Yes, it is."

show lilly cane_surprised_close_ni onlayer master
with charachange

li "You're a very bad liar, Hisao."

hi "That's true, but that's why I'm not lying. I'm a very trustworthy person."

show lilly cane_weaksmile_close_ni onlayer master
with charachange

li "I'm sure you are. I think I can forgive you just this once, though."

hi "Forgive? What for, exactly?"

show lilly cane_giggle_close_ni onlayer master
with charachange

with Pause(0.2)

show lilly cane_smile_ni onlayer master
with charadistant

"She giggles a little before resuming her quiet walking. Just what is she thinking now?"

stop music fadeout 4.0

"I look up to the dark sky as I slump my shoulders."

"I think this is something I have to sort out for myself, rather than relying on her for everything."

label en_L6b:


hi "It was just kind of… I was thinking about how you seem to have everything so sorted out, even with Hanako relying on you. I can admit that even I kind of relied on you when I first transferred in."

hi "I think it's a good quality to have."

"I turn to Lilly, surveying her reaction."

stop music fadeout 2.0

show lilly cane_listen_close_ni onlayer master
with characlose

"She's forcing herself to look forward and furrowing her brow quite a bit. Her face looks a bit awkward, as if she was trying to find just the right words."

hi "…Lilly?"

show lilly cane_weaksmile_close_ni onlayer master
with charachange

li "I would thank you, but… assuming that I don't rely on the presence of others is too much. You'd be wrong to think that Hanako simply depends on me with nothing in return."

"She seems to have a bit of trouble saying it, even though it's largely what I'd thought already."

"If she's tried so hard to maintain her independence, as anyone would have had to in her position, sighted or not, maybe she finds it hard to talk about her own needs."

"It's only now that I realize an omission in what she says, though. I decide to follow it up, largely in jest, to avoid things getting too personal."

hi "Oh? And what about me?"

play music music_lilly fadein 2.0

show lilly cane_smile_ni onlayer master
with charadistant

"She suddenly runs ahead of me and turns, blocking me off."

show lilly behind_cheerful_ni onlayer master
with charachange

"With a smile, she holds her hands behind her as she leans forwards."

li "You're different."

show lilly back_giggle_ni onlayer master
show lillyprop back_cane_ni onlayer master
with charachange

"And with that, she turns back and continues to walk ahead of me, a newfound spring in her step."

"All I can do is raise an eyebrow and give a dazed grin. I don't think I've ever seen this playful and teasing side of her before."

"So… I'm “different”. It's hard to work out the exact context, but knowing her, this ambiguity was intended."

"Our relationship has been changing, at the very least simply because I've begun to stand on my own feet more and started getting more curious about the situation of those around me."

"As to why… probably a mix of personal curiosity, and a want to try and work out how to deal with my situation."

"I'm less sure of Lilly, though. That's why her own statement, so similar to my own feelings towards her, throws me off so much."

"Watching her make her way up the street, cane tapping from left to right, I decide to settle the matter later, and just smile. This is a nice side to her, and I don't want to forget it."

stop music fadeout 2.0

label en_L6c:


scene bg school_girlsdormhall onlayer master
with shorttimeskip

play music music_normal fadein 4.0

"Eventually we get to the girl's dormitories, both my arms aching from the weight of two sets of groceries."

hi "Hah… we're finally here. Phew."

show lilly invis onlayer master:
    right
    xpos 0.95
with None

show lilly cane_smileclosed onlayer master at right
with dissolvecharamove

"I bend down to wipe my forehead with the back of my hand. Lilly stops in front of her door and sets down her bag, fishing around in her pocket for the key."

show lilly cane_smile onlayer master
with charachange

li "Thank you, Hisao. I really appreciate your help."

hi "Ah, this is nothing."

show lilly cane_smileclosed onlayer master
with charachange

li "It might be nothing to you, but it's… definitely something for me."

show lilly invis onlayer master:
    right
    xpos 1.05
with dissolvecharamove

play sound sfx_doorclose

hide lilly onlayer master
with None

"And with that, she steps through her door, closing it behind her."

"I blink. Those were nothing but honest thanks, but I can't help feeling something different about them."

"Anyway, I have something else to do before I can mull on that at my leisure."

scene bg school_dormhanako_ni onlayer master
show hanako emb_timid_close onlayer master:
    center
    xpos 0.45
show hanako_door_base onlayer master at right
show hanako_door_door onlayer master at left
with locationchange

play sound sfx_doorknock2

"I turn back to the door to Hanako's room and proceed to knock twice in quick succession, the bags still in my hand rustling together."

play sound sfx_dooropen

show hanako_door_door onlayer master:
    xpos -0.05
with charamove

"After a couple of seconds, the door slowly opens. If one weren't looking closely, they could be forgiven for thinking it hadn't moved at all."

"I twist my head to the side to try and peer through the tiny sliver of a gap between the door and the doorframe."

hi "Hey Hanako, I've got your stuff."

show hanako basic_normal_close onlayer master at Position(xpos=0.4)
with charachange

ha "Ah!"

show hanako_door_door onlayer master:
    xpos -0.3
show bg school_dormhanako onlayer master
with dissolvecharamove

"With that, she opens the door completely, making her plain room visible over her shoulder. Sparsely decorated, it's probably even more unremarkable than my room."

"I hold out my right arm, both bags almost pulling it straight back down with their weight."

show hanako emb_smile_close onlayer master
with charachange

ha "Th-thank you, Hisao."

show hanako emb_downtimid_close onlayer master
with charachange

ha "I'm sorry to make you… carry them all this way."

hi "It's fine, don't worry. Just don't make me do it every day, okay?"

show hanako basic_normal_close onlayer master
with charachange

"I pass the bags to her as I give a lighthearted chuckle. After the initial transfer of weight she manages to take them easily."

hi "I'll be off then. 'Night, Hanako."

show hanako cover_bashful_close onlayer master
with charachange

ha "Good night. Um, s-see you in class… tomorrow…"

show hanako_door_door onlayer master at left
with charamove

play sound sfx_doorclose

"With a deep bow, her groceries still held in both hands, she steps back and shuts the door."

stop music fadeout 5.0

scene bg school_dormext_full_ni onlayer master
with locationskip

"Making my way back to my own dorm, I put one bag into my other hand to balance them out."

"Even as I do so, I can't get Lilly's lighthearted smile out of my mind. When I'd first met her, it would have been nearly impossible to imagine her like that."

"Indeed, it feels like we've become closer in the past few weeks since I first got to know both her and Hanako."

"The time that I spend with her each day. The small exchanges of happiness we share. Those small moments of joy as I get closer to her."

"I'm far from certain, but I don't think these are just the normal feelings of friendship."

scene bg school_dormhisao onlayer master
with locationskip

"Once I return to my room, I store away my groceries and begin getting ready for the night."

show letter_insert onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"I swap the school books in my bag for those I'll need tomorrow, pulling out the yellow envelope Misha gave me earlier in the process."

"I got so sidetracked by one thing after another that I couldn't deal with it earlier. Who could have written me, I wonder?"

"The name neatly adorning the back of the envelope freezes me in my tracks. It's been so long since I've seen her writing, there's little chance I could have identified it as hers otherwise."

"“Iwanako.”"

"Why… should she have written me? I can't think of any good reason for her to do this."

"I almost don't open the letter, but there'd be little point to that. If I just left it alone, its mere existence would gnaw at me until I did something about it."

scene ev hisao_letter_open onlayer master
with shorttimeskip

play music music_rain fadein 6.0

"I look down at the piece of paper on my desk, its bright and summery decoration beaming happily at me."

"The lettering is in pink, jarring badly with the yellow sunflower border on the card. The handwriting is neat, the characters having been written thoughtfully and with an unusual amount of care."

"I'd barely given the letter a second thought when it was given to me, but now I can't get its contents out of my mind."

window hide
nvl clear
nvl show dissolve

n "\n\n\nWhile I'd like to say that I don't know why she used such an old-fashioned method of communication, considering a phone call or an email would be both much faster and easier, the answer feels obvious enough given the content."

n "A letter leaves a comfortable distance between the sender and the recipient. Unlike a phone, it isn't required that you engage in conversation, and unlike email, there is less expectation of an immediate reply."

n "\nStatements such as “the third-years seem to be very anxious about the final exams,” and “it's so weird to think we are already seniors, isn't it?” are just smalltalk. Smalltalk that could have been achieved by simply replying to any of the messages I'd sent her while in hospital."

n "The ending, though, is the true reason she sent this. The last couple of lines, added almost as an afterthought."

nvl clear
nvl hide dissolve

play sound sfx_paper

scene ev hisao_letter_open_2 onlayer master
with locationchange

nvl show dissolve

n "\n\n\n\n\n\n\n“I wonder if we will meet again. Perhaps it's for the best if we don't?”"

n "It's a statement that should hurt. I've always heard breakups are nasty stuff, but it feels like this is simply a reaffirmation of what we both already knew instead."

n "It's the preceding text, no more than smalltalk, that makes me feel most uneasy. I can't figure out why, no matter how long I sit here and look down at this bright and summery piece of paper."

nvl clear

n "\n\n\n\n\n\n\n\n“If you would like to correspond with me, by all means write me back.”"

n "It's plainly obvious that this is not the type of letter to be replied to. In the end, this letter is no more than a simple abdication of responsibility; a final statement to reassure herself that our relationship is over."

stop music fadeout 3.0

nvl hide dissolve
nvl clear

scene bg school_dormhisao onlayer master
with locationchange

window show

"As such, I find I have little problem in scrunching the letter and envelope into a ball and tossing it into the wastebin, ridding myself of its existence."

"I go to bed with mixed feelings, cheated out of a pleasant evening by this intruder from the past."

"Ironically, it takes a while before I can manage to sleep."

scene black onlayer master
with dissolve

$ suppress_window_after_timeskip = True

label en_L7:

window hide None

scene black onlayer master
with dissolve

nvl show dissolve

n "\n\n\n\nI sweat profusely, awaiting the dreaded moment."


$ renpy.music.set_volume(0.7, 0.0, channel="music")
play music music_tension fadein 6.0

n "Each tick of the clock tenses my muscles that much more, every minute making more hairs stand on end."

n "It's coming for me, I can feel it."

play sound sfx_slide

n "\n\n{image=vfx/reddash.png}{color=#FF0000}{b}Death.{/b}{/color}"

n "\n\nDeath in the form of a single sheet of paper."

$ renpy.music.set_volume(1.0, 0.5, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom onlayer master at bgright
with locationchange

window show

"I take the small pile of papers from the student in front of me and pass it backwards after plucking off the top piece."

"Looking to the top right of the page, I find my fears realized within that small red circle."

stop music
play sound sfx_thunder
with vpunch

"Forty-three."

"I hang my head and sigh in resignation. Cursing under my breath, I can feel the aura of a similar sentiment rising from the entire class. It's strange, but that fact lifts my mood by a minuscule amount."

"Misery loves company, I suppose."

"As the teacher opens her mouth, the room braces for the inevitable onslaught…"

play music music_normal fadein 1.0

play sound sfx_normalbell

"…only to be saved at the last minute."

"We quickly move to collect our bags and leave for lunch post-haste, but the teacher delivers a parting broadside."

"Teacher" "We'll be discussing the test scores next lesson. Needless to say, there will be quite some discussion to be had."

"A collective groan resounds from the class, now reduced to shuffling out dejectedly."

scene bg school_hallway3 onlayer master at bgright
with locationchange

"I push the sheet into my bag as I walk along the hallway, crumpling it in the process. It's enough that such a troublesome letter ended up on my desk yesterday, and now this."

hi "I hate English…"

stop music fadeout 0.7

mystery "HI—{w=0.3}SA—{w=0.3}O!"

"A stern female voice gruffly calls out from behind me."

play music music_tension

"I freeze on the spot, my face becoming like stone. It's as if I can feel my brain disconnecting from my body."

"My eyes slowly shift right, trying to catch a glimpse of the disembodied voice."

stop music fadeout 0.3

"…nothing?"

"My face begins to slip as time passes, and I decide to risk turning my head. Ever so slowly, I twist it to the—"

play sound sfx_impact

hi "GYAAAAH!" with vpunch

"I jump into the air and drop my bag, yelling out in surprise."

"As I recover and regain my composure, I turn to see… I should have known."

hi "Emi."

play music music_running

show emi excited_proud onlayer master at center
with charaenter

emi "Gotcha, Hisao."

"She stands there with a mischievous grin on her face, hands forward and fingers pointed inwards. She was the one who jabbed my ribs with her fingers."

"I look down at her with a grimace, rubbing my hair in frustration."

hi "That's no way to greet someone, you know."

show emi sad_pout onlayer master
with charachange

emi "You have no sense of humor."

hi "I left my sense of humor in my English class. Complain to the teacher if you want it given back to me."

show emi sad_shy onlayer master
with charachange

"She pulls her best puppy-dog eyes on me as she pouts. Lilly's managed to build up my resistance to the tactic, but Emi's short stature adds enough to the effect to make me relent."

hi "So, how are things? I haven't seen you around for a while."

show emi basic_closedgrin onlayer master
with charachange

emi "Same old, same old. I run so fast, nobody wants to join me on my morning runs."

show emi basic_annoyed onlayer master
with charachange

emi "It's a real pain."

"Her modesty never fails to amuse me."

show emi basic_grin onlayer master
with charachange

emi "Although…"

"Uh oh."

show emi sad_shy onlayer master
with charachange

emi "You know what I'm thinking, don't you Hisao?"

"Wearing my emotions on my sleeve is one of my worst habits. She's seen right through me."

"Fortunately, I see somebody else approaching us that will give me an out."

hi "Oh, hi Hanako."

show emi sad_shy onlayer master at twoleft
show bg school_hallway3 onlayer master at center
with charamove

show hanako emb_downtimid onlayer master at tworight
with charaenter

"I give her a welcoming wave, and try my best at looking like I haven't noticed Emi's pouting face. She gives a small wave back."

show hanako emb_smile onlayer master
with charachange

ha "H-hello, Hisao… Emi."

show emi basic_closedgrin onlayer master
with charachange

emi "Hey Hanako."

hi "I'll join you and Lilly in a sec."

hi "Actually, speaking of lunchtime company, it's odd to see you without Rin, Emi."

show emi basic_shock onlayer master
show hanako defarms_shock onlayer master
with vpunch

emi "Ah! Rin!"

stop music fadeout 3.0

hide emi onlayer master
with easeoutleft

"Without a second word, she forgets all about us and bolts off up the hallway. She must've forgotten she was waiting for her."

"Hanako and I stand speechless, only able to helplessly stand and watch this ball of seemingly boundless energy dash off."

play music music_running

show emi basic_closedgrin onlayer master at left
with easeinleft

emi "Oh yeah, Hisao…"

"She suddenly stops herself just before vanishing around the corner to the rooftop staircase, spinning around to meet our bemused faces."

show emi excited_proud onlayer master
with charachange

emi "I hate English too."

stop music fadeout 4.0

hide emi onlayer master
with easeoutleft

"And with that, she disappears."

"All I can do is hang my head and give a long sigh, thoroughly left in the dust."

show hanako basic_smile onlayer master
with charachange

"As I hear a short giggle coming from behind me, I turn to see Hanako smiling at the corner my attacker rounded."

play music music_daily fadein 4.0

show hanako basic_smile onlayer master at center
show bg school_hallway3 onlayer master at bgleft
with charamove

"I pick up my dropped bag from the floor and quickly dust it off."

hi "Afternoon. Been busy?"

show hanako def_worry onlayer master
with charachange

ha "You don't… like English?"

hi "Hmm? Oh, uh, nah. I had a test on it a while back, and Emi caught me brooding about the results."

show hanako emb_downsad onlayer master
with charachange

ha "Ah, sorry…"

"She averts her gaze, guilt written onto her face. A casual observer would think she'd just accidentally reminded me of a dead relative."

hi "Come on, it's not your fault. How're you doing in it?"

show hanako emb_sad onlayer master
with charachange

"She looks up, though still avoids meeting my eyes."

show hanako basic_worry onlayer master
with charachange

ha "All right, I… suppose."

"An awkward silence passes. They seem all too common around Hanako."

show hanako basic_bashful onlayer master
with charachange

ha "Oh, Lilly asked if… you'd like to join us for lunch on the roof."

"I guess I don't exactly have any pressing engagements to attend to."

hi "Sure, I'll be right up."

show hanako cover_distant onlayer master
with charachange

ha "Um, I'll… go get my lunch from the cafeteria now… then."

hi "Go on. You don't need my approval to leave, you know."

show hanako basic_smile onlayer master
with charachange

ha "O-okay. I'll… be going then."

hide hanako onlayer master
with charaexit

stop music fadeout 5.0

"She gives a skittish reply, a small nod and quickly makes off towards the cafeteria."

play ambient sfx_crowd_indoors fadein 2.0

show crowd onlayer master:
    bgleft
    alpha 0.0
    parallel:
        ease 1.0 center
    parallel:
        linear 2.0 alpha 1.0
with None

show bg school_hallway3 onlayer master at center
with dissolvecharamove

"I guess she must've forgotten to bring lunch today. As I walk through the hallways, more and more students start to come out of classrooms and pass me, going in the same direction as Hanako went."

"By the time I manage to make it to the stairs, I'm having to push my way past a busily chatting throng of students."

stop ambient fadeout 0.5

scene bg school_staircase1 onlayer master
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_rooftop

"I finally manage to get past the last of the crowd and round the staircase, slumping slightly in relief and slowing my pace before I open the door to the roof."

play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

scene bg school_roof onlayer master
show white onlayer master
with locationchange

hi "Ah, damn!"

"I momentarily avert my eyes, all but blinded by the harsh summer sun."

show white onlayer master:
    alpha 1.0
    linear 10.0 alpha 0.0

show lilly basic_smile behind white onlayer master:
    left
    ypos 1.2
show emi basic_grin behind white onlayer master:
    center
    ypos 1.15
show rin basic_absent behind white onlayer master:
    right
    ypos 1.17
with charaenter

mystery "Hmm?"

play music music_soothing fadein 8.0

"As I slowly regain my vision, the surroundings finally take form."

"Lilly, Emi and Rin sit together on the rooftop, the top of the hilltop forest around Yamaku visible past the fence around them, as if to frame the view."

show emi basic_closedgrin onlayer master
with charachange

emi "Ah, Hisao!"

show lilly basic_smileclosed onlayer master
show rin basic_deadpannormal onlayer master
with charachange

"Lilly and Rin give a quick nod of acknowledgment and a deep nod of greeting respectively."


"I start walking towards the rather mismatched trio, and can't help marveling at the speed with which Emi devours the rest of her half-eaten banana."

hi "Hey. Strange to see you three together like this."

show lilly basic_weaksmile onlayer master
with charachange

li "It seems to have been quite the day of coincidences; Emi and Rin decided to eat on the roof just as Hanako and I decided to."

show emi basic_annoyed onlayer master
with charachange

emi "You stole it! This spot was ours!"

hi "Simmer down, you can't steal a place in the school."

"I plonk myself down beside Lilly, the four of us creating a semicircle."

show rin basic_deadpanupset onlayer master
with charachange

rin "I think she is right."

hi "You too?"

show rin basic_deadpan onlayer master
with charachange

rin "The butterfly is her accomplice."

hi "The butter…"

"As I glance around, sure enough, a small yellow butterfly floats across my field of vision."

hi "So tell me, how did this butterfly help Lilly “steal” this spot?"

show rin basic_lucid onlayer master
with charachange

rin "It scouted out our conversation and told her."

"I should've known better than to expect sound reasoning from Rin. Regardless, I guess it wouldn't hurt to play along."

hi "You're telling me she can talk to butterflies?"

show rin basic_awayabsent onlayer master
with charachange

rin "There are people who can talk to horses, called horse whisperers."

show rin basic_deadpanamused onlayer master
with charachange

rin "Lilly must be a butterfly whisperer."

"I bury my head in my hands as Emi rounds on her strange companion. She doesn't seem to share Rin's sense of humor."

show emi basic_confused onlayer master
with charachange

emi "Whisperers don't work like that."

"Emi and Rin continue their banter as I turn to Lilly, who's busily finishing off her small box of curry and rice."

hi "So what brought you up here, anyway?"

show lilly basic_smile onlayer master
with charachange

li "A little fresh air every now and again doesn't hurt."

show emi basic_shock onlayer master
with charachange

emi "Ah!"

"Emi breaks off from her vain attempts to introduce the concept of logic to Rin."

show emi sad_annoyed onlayer master
with charachange

emi "That was why we came up here too!"

"Something tells me it was her idea alone, and that Rin only got dragged up here on Emi's whim. Then again, the same could probably be said of Lilly and Hanako."

show lilly basic_weaksmile onlayer master
with charachange

li "Now, now. We can share."

$ renpy.music.set_volume(0.001, 1.0, channel="music")

play sound sfx_door_creak


show lilly basic_surprised onlayer master
show emi basic_hes onlayer master
show rin basic_awayabsent onlayer master
with charachange

"The creaking of the door to the roof can be heard as soon as she says the words. A moment of silence falls over us as everyone's attention focuses on the figure appearing from it."

show lilly basic_surprised onlayer master:
    xanchor 0.5 xpos 0.4
show emi basic_hes onlayer master:
    xpos 0.68
show rin basic_awayabsent onlayer master:
    xpos 1.08
show bg school_roof onlayer master at bgright
hide white onlayer master
with charamove

show hanako basic_distant onlayer master:
    xanchor 1.0 xpos 0.0 yalign 1.0
    easein 3.0 xanchor 0.0 xpos -0.06
    ease 1.0 ypos 1.17
with None

"Hanako slowly walks over to us, her eyes pinned to the ground, silently ruing the attention she's attracting. She tenses, just barely, when her eyes meet Rin's."

"I can't help raising an eyebrow as she walks over to us and sits next to me, doing her utmost to avoid looking up even as she brings her cafeteria bread to her mouth."

show rin basic_absent onlayer master
show emi basic_grin onlayer master
show hanako basic_normal onlayer master:
    xanchor 0.0 xpos -0.06 ypos 1.17
with charachange

hi "So how do you and Emi know each other, anyways?"

$ renpy.music.set_volume(1.0, 8.0, channel="music")

show lilly basic_smileclosed onlayer master
show rin basic_awayabsent onlayer master
with charachange

li "Emi's somewhat well known around the school for her athletic ability. She's the fastest member of the track and field club by some margin, even beating Miki Miura at the track meet last week."

"Miki Miura… ah, that tanned girl from the front of my class. Considering her height and toned body, being able to beat her is quite an accomplishment."

show emi excited_amused onlayer master
with charachange

"Looking over to Emi, it's very clear she's well aware of this fact as she beams proudly."

show emi excited_happy onlayer master
with charachange

emi "So, Hisao. What was your score in English?"

"Ouch."

show rin basic_absent onlayer master
with charachange

hi "No comment."

show emi basic_annoyed onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Boo~."

"She puffs her cheeks and pouts, but it doesn't take long for her to bounce back."

show emi excited_proud onlayer master
with charachange

emi "All right, if I tell you mine, you have to tell me yours. Deal?"

stop music fadeout 4.0

show rin basic_absent onlayer master
with charachange

hi "Fine, fine."

show emi basic_closedhappy onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Okay, on the count of three, we both say our results."

show emi excited_joy onlayer master
with charachange

emi "One…{w=1.0} Two…{w=1.0} Three!{w=1.0}{nw}"

show emi basic_closedgrin onlayer master
with charachange

$ doublespeak (hi, emi, "…", "Thirty-two!")

"I beam a mischievous grin."

play music music_comedy

show hanako cover_smile onlayer master
show lilly basic_cheerful onlayer master
show rin basic_amused onlayer master
show emi excited_sad onlayer master
with charachange
with vpunch
play sound sfx_impact

emi "Ah! Evil! Evil, evil, evil, evil!"

show rin basic_absent onlayer master
with charachange

hi "You said it, not me. Still, the fact that you managed an even lower score than me is kind of amazing."

show emi sad_grit onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Grr~!"

"She looks and sounds like a small terrier growling at an intruder. I can't say it's the most threatening sight I've seen."

show lilly basic_displeased onlayer master
show hanako basic_normal onlayer master
with charachange

li "Either way, scoring higher than thirty-two isn't something to boast about, much less scoring below it. For any subject."

show rin basic_absent onlayer master
with charachange

hi "Yes, Lilly."

show rin basic_awayabsent onlayer master
show emi sad_shy onlayer master
with charachange

emi "Sorry, Lilly."

show lilly basic_smile onlayer master
with charachange

li "I could help you with your English, if you'd like. It would be my pleasure to—"

show emi basic_closedgrin onlayer master
with charachange

emi "No, no, that's fine. But I appreciate the thought. Really."

show lilly basic_reminisce onlayer master
show hanako basic_smile onlayer master
show rin basic_deadpanamused onlayer master
with charachange

"Lilly looks slightly deflated, her hopes of imparting her knowledge dashed. Judging from the badly hidden laughter of the rest of us, neither she nor Emi seem to have garnered too much pity."

stop music fadeout 0.5
$ renpy.music.set_volume(0.0, 4.0, channel="ambient")

window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.7)

window show

"As I sit happily laughing though, I feel my voice suddenly cut off as my chest clenches."

window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.7)

window show

"I sit in silence for a few seconds, all my concentration forced on my heartbeat. It's only a small pain, but the ache feels like it's growing."

play music music_tragic fadein 0.5

window hide

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

window show

"Breathe deeply… breathe deeply…"

window hide

play sound sfx_heartfast
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

window show

"I glance upward to try and keep at least some of my attention on my surroundings, to see Emi suddenly freezing when she notices the expression of pain on my face out of the corner of her eye."

show emi basic_hes onlayer master
with charachange

emi "Hey, Hisao… are you okay?"

show hanako def_worry onlayer master
show lilly basic_surprised onlayer master
show rin basic_deadpanupset onlayer master
with charachange

hi "Yeah, I'm… fine…"

window hide

play sound sfx_heartfast
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

window show

"I look back down and redouble my efforts to try and stay calm, clenching my fists to try and dull the pain."

window hide

play sound sfx_heartfast
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

with Pause (0.7)

play sound sfx_heartslow
show heartattack alpha onlayer master
with Dissolve (0.1)

hide heartattack alpha onlayer master
with Dissolve (0.2)

stop music fadeout 4.0

window show

"It takes a short time, but the pain, thankfully, begins to fade."

$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

"When I look back up, there's only silence and pensive faces to be seen. I guess I'd better explain myself."

play music music_rain fadein 10.0

hi "Arrhythmia. I'm fine, it's… just a heart flutter."

show lilly basic_listen onlayer master
with charachange

li "Are you sure? Should we get the nurse?"

show hanako def_worry onlayer master:
    ypos 1.0
with ease

"Taking her cue, Hanako quickly picks herself up and begins to dash to the door."

hi "Hanako, stop. Lilly, I'm fine."

show rin basic_deadpan onlayer master
with charachange

rin "You look like a wet, wrinkled tomato."

hi "Huh?"

"As I bring my hand to my forehead, I can feel the beads of sweat gathered on it and dab them off with my cuff."

hi "Thanks. I told you, I'm fine. I'm just kind of… fragile, I guess."

show hanako basic_worry onlayer master
with charachange

show hanako basic_worry onlayer master:
    ypos 1.17
with charamove

show emi sad_shy onlayer master
show rin basic_deadpanupset onlayer master
show lilly basic_sleepy onlayer master
with charachange

"The entire atmosphere's changed from one of gaiety to downcast faces, the situation being too awkward for anyone to know exactly how to react."

"And of course, the whole thing is thanks to me. It just had to happen now, around others."

stop music fadeout 8.0

show lilly basic_weaksmile onlayer master
with charachange

li "Oh, Emi?"

show emi basic_hes onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Hmm?"

"She looks up, a box of juice halfway to her mouth."

show lilly basic_smileclosed onlayer master
with charachange

li "I haven't told you of my score yet, have I?"

show emi basic_annoyed onlayer master
with charachange

emi "Yeah, well. You're half-foreign, so your score doesn't count anyway."

"Lifting an eyebrow, I inquisitively turn to Lilly."

show rin basic_absent onlayer master
with charachange

hi "What was your test result, anyway?"

show lilly basic_cheerful onlayer master

"She gives a cheeky grin."

show rin basic_awayabsent onlayer master
show lilly basic_planned onlayer master
with charachange

li "One hundred percent. Perfect score."

play music music_lilly fadein 0.5

"No way. All I can do is hang my mouth open in wonder."

"Considering those tests are insane even for some native speakers, I can only imagine she's gone and done something like committing to mind part of the dictionary. A gift for rote memorization, maybe."

show rin basic_absent onlayer master
with charachange

hi "That's…"

show rin basic_awayabsent onlayer master
show emi sad_pout onlayer master
with charachange

emi "See! Only someone part-foreign could get a score that good."

show rin basic_absent onlayer master
with charachange

hi "“See”…"

show rin basic_awayabsent onlayer master
show emi basic_closedsweat onlayer master
with charachange

emi "Er…"

show lilly basic_giggle onlayer master
show hanako basic_smile onlayer master
with charachange

"Lilly and I grin at Emi's expense, her reaction identical to mine when I'd first tripped on that little landmine. Lilly's foreign ancestry does raise a point, though."

show rin basic_absent onlayer master
with charachange

hi "Ah, that's right. You leave tomorrow for Scotland, don't you?"

show rin basic_awayabsent onlayer master
show lilly basic_smile onlayer master
with charachange

li "That's correct. Emi heard some rumors about it; it seems word's spreading quickly, considering I only told a friend in my class a couple of days ago."

show emi sad_grin onlayer master
with charachange

emi "It must be so nice to go halfway around the world on a holiday."

show emi excited_happy onlayer master
with charachange

emi "Hey, could you buy me something while you're there?"

show rin basic_absent onlayer master
with charachange

hi "Don't be too shy now."

show lilly basic_giggle onlayer master
with charachange

"Lilly gives a lighthearted giggle, evidently fully expecting Emi's bluntness."

"The rest of the lunch continues much the same as before, the jauntiness from before my heart flutter thankfully returning in full."

stop music fadeout 8.0

scene bg school_roof onlayer master
show lilly basic_smileclosed onlayer master:
    center
    ypos 1.2
with shorttimeskip

"As everyone files off with the appropriate farewells, only Lilly and I are left."

hi "Hey, Lilly?"

"She packs the last of her things into her bag and clips it shut, before perking her head up slightly."

show lilly basic_smile onlayer master
with charachange

li "Hmm?"

hi "Um… thanks for breaking the silence back there. I kind of wanted to stop it, but didn't really know how to."

"As much as I'd like to sound less morose about it, the letter from yesterday, screwing up a test so badly in class, and now my heart make things very hard indeed."

show lilly basic_weaksmile onlayer master
with charachange

"She gives an indulgent smile and nods. I hope she hasn't picked up on it, but knowing her, it's unlikely that she hasn't."

li "Emi's strong, but only human. We do worry about you, Hisao."

hi "Hold on, why would I worry you?"

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

show lilly basic_displeased onlayer master
with charachange

"Her smiling face collapses, becoming uncomfortably serious."

li "Hisao, we are not ignorant of your situation."

li "Unli…"

show lilly basic_concerned onlayer master
with charachange

"She suddenly cuts herself short, unsure of whether she should say what she intends to. I give a weak smile and rest my hand on her shoulder."

play music music_twinkle fadein 10.0

hi "Don't. It's enough that I worry about it. I don't want you all to shoulder my burden."

show lilly basic_oops onlayer master
with charachange

li "But…"

hi "If you all worry about it, I have to worry about your worrying. If… that makes sense."

hi "I'm fine, okay?"

show lilly basic_reminisce onlayer master
with charachange

"For a moment she looks to be lost in thought, carefully pondering how to react."

show lilly basic_weaksmile onlayer master
with charachange

li "Hisao, do you have any paper left from your food's packaging?"

hi "I… think so? I'll just check."

play sound sfx_rustling

"I rummage around in my bag for the leftovers from lunch, eventually finding a paper square from my sandwich's package."

"My eyebrow raised and my expression rather quizzical, I gently place the square into Lilly's hand. Without another word, she brings her fingers around it to feel out its edges."

show lilly basic_smile onlayer master
with charachange

li "This should be large enough…"

"With both of us seated on the roof, the minutes to the lesson ticking away, she proceeds to lay the item on the ground and begin her work in earnest."

show lilly basic_smileclosed onlayer master
with charachange

"Wrapped in silence, I watch her fingers move about on the small square with amazing dexterity. A small fold here, a larger fold there, her fingertips keep a slow but sure pace."

"Looking up, her expression is calm and placid. The fact her face is pointed well above the sheet in front of her makes the sight of her work all the more curious."

"Her shoulders slump a bit after finishing one final fold, her work apparently done. It's only when she holds the item up in her hands that I realize what it is."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene white onlayer master
with dissolve

with Pause(0.1)

scene ev lilly_crane onlayer master:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with Dissolve(4.0)

"A small origami crane."

"Light brown thanks to the packaging used, the result looks quite delicate and precise."

hi "You can do origami?"

li "I taught myself how to do it when I was younger. It improved my dexterity a bit."

hi "Huh…"

"A little baffled, I carefully take the small bird from her pale cupped hands as if it would break from the slightest breath. It seems to be folded quite well, and holds its shape easily."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_roof onlayer master
show lilly cane_smile onlayer master at center
with locationskip

"We both grab our bags and head out the door, Lilly extending her cane as she does so."

stop ambient fadeout 2.0

scene bg school_hallway3 onlayer master
with locationskip

"I hold Lilly's handiwork up to my face for further inspection while we walk down the hallway, her hand running along the silver handrails for orientation."

"If she taught herself origami to improve her dexterity, with the use of her hands meaning so much to her given her condition… ah, so that's it."

"I smile as I realize the bird's meaning."

"“Everyone here has had to find their own ways of dealing with their conditions. You aren't alone here when you have problems.”"

hi "Thanks, Lilly. I appreciate this."

show lilly cane_cheerful onlayer master
with charaenter

"She gives a sweet smile and a nod, not using words where none need be used, in her typical manner."

show lilly cane_smileclosed onlayer master
with charachange

li "All I ask is that you take care of yourself, Hisao."

hi "Don't worry, I will."

show lilly cane_smile onlayer master
with charachange

li "Promise?"

hi "Promise."

hide lilly onlayer master
with charaexit

stop music fadeout 7.0

"And with that, we part ways."

"To be honest, I don't know what annoys me more - the fact that I could die at any moment, or the fact that everyone knows that."

"I guess I'll just take each day as it comes. As the unexpected present in my hand reminds me, I'm not alone here. Even though I may be like this, I'm not alone."

"If they worry, if anyone worries, I'll smile."

"I'll smile enough for all their worries to go away."

scene black onlayer master
with dissolve



label en_L8:

scene black onlayer master
with dissolve

play sound sfx_normalbell

scene bg school_scienceroom onlayer master
show muto normal onlayer master at center
with locationchange

"The moment the bell rings out, a collective sigh of relief comes from everyone."

play music music_happiness fadein 2.0

"Much of the morning's been taken up by a droning lecture on stoichiometry, a topic entirely unbefitting of the insufferable heat permeating the classroom."

hide muto onlayer master
with charaexit

"Knowing that attempting to teach anything more would be an exercise in futility, Mutou gives up and begins clearing the teaching materials from his desk for the day."

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

show hanako basic_normal onlayer master at center
with charaenter

"As meaningless banter starts filling the classroom, I notice Hanako getting up and coming to my desk. She's been a lot less withdrawn lately, something which gives me a small measure of satisfaction."

show hanako basic_smile onlayer master
with charachange

ha "Hello, Hisao."

hi "Hey. Want to go pick up Lilly, then? It's close to the time when she'd need to get going if she's going to make the flight."

show hanako cover_worry onlayer master
with charachange

ha "Um… about that…"

show hanako basic_worry onlayer master
with charachange

ha "She said she might be held up a bit by her classmates."

"I suppose that makes sense. Her class usually gets off a little earlier than ours, so Lilly would normally have just come to our classroom. Her class must be sending her off."

hi "Well, never mind. We can wait outside her classroom for once, right?"

show hanako emb_smile onlayer master
with charachange

"She gives a small giggle before nodding, the two of us taking our things and leaving for 3-2's classroom."

stop ambient fadeout 1.0

scene bg school_hallway3 onlayer master
with locationchange

"When we reach our destination, I stop in idle amusement at the scene inside."

"One of the shorter girls from the class has Lilly wrapped in an enthusiastic hug, her head no higher than Lilly's chin. Her other friends, of which there are several, are gathered around her as well. Lilly simply smiles kindly and hugs her back."

"I guess Lilly must be pretty popular. Compared to Shizune's harsh but fair dictatorship of 3-3, Lilly seems more like a mother figure for 3-2, to say nothing of her height and looks."

"Kenji's pointedly cool demeanor as he packs up his things at his seat in the back corner of the classroom is expected. He's no doubt far from a fan of the fuss being made about Lilly's leaving."

"Looking beside me and seeing Hanako following my gaze, I decide to finally enter the room."

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_room32 onlayer master
show crowd onlayer master at center
show lilly basic_surprised onlayer master at center
with locationchange

hi "'Afternoon, Lilly. It's just me and Hanako."

show lilly basic_surprised onlayer master at twoleft
show crowd onlayer master at bgleft
show bg school_room32 onlayer master at bgleft
with dissolvecharamove

show hanako emb_downtimid onlayer master at tworight
with charaenter

"Hanako withers noticeably when exposed to the din being made around Lilly. Try as she might, I doubt she'll ever completely get over her social anxiety."

show hanako emb_emb onlayer master at tworight
with charaenter

ha "Hello…"

"Lilly manages to work out our position reasonably well, her classmate detaching herself without a second word. A look of slight exasperation is written on Lilly's face, though I can't say I blame her."

show lilly basic_smileclosed onlayer master
with charachange

li "Hello Hisao, Hanako. Do we have much time before the flight leaves?"

"I give a quick glance at my watch. Taking the trip to the airport into account, there's a good ten, maybe fifteen minutes left while still allowing for contingencies."

hi "Yeah, we still have a few minutes to kill. I wouldn't worry about missing it yet."

"Classmate" "Ah, is this Hanako?"

"Uh oh. I think we've just inadvertently become entangled in Lilly's social web."

"The girl is probably part of the legally-blind faction of the class like Kenji, given her almost windowpane-like spectacles. Her short, roughly-cut hair gives her a look that fits her excitable expression."

show hanako def_shock onlayer master
with charachange

ha "H-hello… um…"

"She takes Hanako's hand and pulls it up and down enthusiastically. I really don't get how girls can be so social to someone they only know as the friend of a friend."

"While Hanako exchanges nervous greetings, I look around the room for my short and overdressed next-door neighbor. Try as I might, he seems to have slipped out of the classroom without anyone noticing."

"For a moment I try to think of possible career paths that could reasonably benefit from his single skill, before putting my mind to more pertinent matters."

show lilly basic_smile onlayer master
show hanako cover_distant onlayer master
with charachange

"Lilly seems pleased, if somewhat guarded, about the enthusiasm Hanako's suddenly excited from those around her. She might not see it, but Hanako's much less panicked about the affair than I'd anticipated."

"Shuffling my way through the gaggle of classmates, I eventually manage to reach her."

hi "Don't worry, Hanako's fine."

show lilly basic_weaksmile onlayer master
with charachange

li "Thank you. I thought she might be overwhelmed by them."

"Classmate" "Don't worry, we'll be gentle!"

show lilly basic_concerned onlayer master
with charachange

"Both of us grimace in unison. Hanako's nervous grin stays plastered on her face as another couple of girls moves in to meet her."

"It's kind of amazing that even just a month ago she'd never have been able to cope with a situation such as this. Even when I first met her, the two of us completely alone, she sprinted from the library."

hi "So, got everything you need?"

show lilly basic_smile onlayer master
with charachange

li "It's all packed. I just have to go by my room to pick it up on the way, and Hanako and I need to change."

hi "I guess we'd better get going, then. Hanako?"

show hanako cover_bashful onlayer master
with charachange

"Hanako's head flicks up towards us in a flash, her face rather unmistakably appreciating the chance to extricate herself from the small group gathered around her."

show hanako basic_bashful onlayer master
with charachange

stop music fadeout 2.0

ha "C-coming!"

stop ambient fadeout 0.5

scene bg hosp_ext onlayer master
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0
play music music_tranquil fadein 3.0

"The long taxi ride to the airport is surprisingly pleasant, despite the three of us being rather squashed together to fit in the small back seat. On the other hand, maybe “despite” isn't the right word."

"Lilly pays the fare to the driver as we file out, Hanako's eyes flittering left and right. Thankfully there aren't too many people around, most of them being inside the main building rather than milling around outside."

show akira basic_boo onlayer master at tworight
show hideaki bored onlayer master:
    yalign 1.0 xanchor 0.5 xpos 0.9
with charaenter

"It isn't hard to spot Akira and Hideaki leaning against a fence while talking to pass the time. A large black travel bag, complete with wheels and travel handle, leans against the fence alongside them."

show hideaki surprise_up onlayer master
with charachange

"Hideaki's the first to notice us, pointing us out to Akira who gives an overenthusiastic wave."

show akira basic_laugh onlayer master
with charachange

aki "Hey! He~y!"

"I grab Lilly's travel bag for her as we go to meet the two, earning a nod of appreciation."

show akira basic_smile onlayer master
show hideaki normal onlayer master
with charachange

aki "I've got all my stuff here, you got yours? Plane ticket as well?"

show lilly basic_smileclosed_cas onlayer master at twoleft
with charaenter

li "Don't worry, I have everything. You?"

show akira basic_laugh onlayer master
with charachange

aki "Yep. All ready to go."

show hideaki evil onlayer master
with charachange

hh "Not without some problems along the way, I might add."

play sound sfx_impact

show akira basic_kill onlayer master
show hideaki ohshit onlayer master
with vpunch

"The snide remark has his head roughly dragged around by a very firmly clamped-on hand."

show akira basic_boo onlayer master
show hideaki sad onlayer master
with charachange

aki "Haha yeah, I kinda sorta forgot it was in my trousers' pocket. Trousers that I'd put in the wash…"

show lilly basic_concerned_cas onlayer master
with charachange

li "Oh no…"

show akira basic_laugh onlayer master
with charachange

aki "Don't worry, don't worry. Did you know you can print out tickets if you order online nowadays? It's really cool."

show hideaki bored onlayer master
with charachange

"Hideaki's pained expression says that this wasn't a solution found quickly. It could have been worse, I guess."

show lilly basic_weaksmile_cas onlayer master
with charachange

li "We'd better start off then. Check-in should be ready by now."

show akira basic_lost onlayer master
with charachange

stop music fadeout 2.0

aki "Yeah, you're right."

"There's a certain amount of wistfulness in both their voices. To say nothing of the people left behind, meeting their family again after all these years would be big for them."

show hanako emb_sad_cas onlayer master at center
with charaenter

play music music_serene fadein 4.0

ha "Lilly…"

"Hanako wraps Lilly in a gentle hug to say goodbye, one which is warmly reciprocated. Lilly and I share a brief hug afterward, each of us saying our goodbyes."

"Beside us, Akira and Hideaki break off from a small hug and a word or two between them. It would probably look quite nice if not for the almost comical height difference between the two."

show lilly basic_smile_cas onlayer master
show akira basic_smile onlayer master
show hanako emb_downtimid_cas onlayer master
show hideaki normal onlayer master
with charachange

"Lilly takes ahold of her sister's arm once all that needs to be said in farewells is said, the two walking past the huge glass doors."

show lilly back_smileclosed_cas onlayer master
with charachange

li "Goodbye Hisao, Hanako!"

show akira basic_laugh onlayer master
with charachange

aki "Seeya! Don't do anything stupid, Shortie!"

hide lilly onlayer master
hide akira onlayer master
with charaexit

"We wave at them until they disappear from sight in the throng of people moving about inside."

"And then… we're alone."

hi "Well… that's that."

show hideaki bored onlayer master
with charachange

"I turn to see Hideaki already beginning to walk off."

hi "Seeya."

show hideaki bored_up onlayer master
with charachange

show hideaki invis onlayer master:
    xpos 1.0
with dissolvecharamove

hide hideaki onlayer master
with None

"He throws a hand into the air, in a manner I'd expect of Akira. In the end, it's just Hanako and me left standing outside."

show hanako emb_timid_cas onlayer master
with charachange

"I rest my hand on her shoulder. She absentmindedly gazes towards the front doors of the building, as if she might catch a glimpse of either of the two before they disappear."

hi "Don't worry, the time'll pass fast."

show hanako basic_normal_cas onlayer master
with charachange

"She hesitates for a moment, but eventually nods."

"With the scorching heat of the summer sun beaming down on us, we make our way to the nearby bus stop."

hide hanako onlayer master
with charaexit

"It's strange, really. Just when I'd begun to see Lilly differently, she leaves on what almost feels like a pilgrimage to the past."

"In a way, though, that's just what I've been doing since coming to Yamaku."

"As much as I may reflect on everything that's happened to me, I really am hardly unique. Everyone has their own circumstances and separate paths to get where they are now."

"Yet I still can't really work out how I should proceed. My life may have practically been reset, and I still can't find anything that satisfactorily fills the hole I still feel in myself."

"Maybe Lilly's leaving will be a good thing for me. Without her to lean on, I'll need to do more for myself. I'll have to be there for Hanako as well."

"It feels strange to have so much changing so quickly after my months in that hospital that seemed to exist so separately from reality, but that's all the more reason for me to keep focused."

"I can't let any opportunity slip out of my fingers in my attempt to rebuild my life."

stop music fadeout 3.0
stop ambient fadeout 3.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
