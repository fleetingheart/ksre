# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label summersclover_intro:
    stop music fadeout 2.0

    pause 1.0

    show text "An unauthorised Katawa Shoujo spin off" with dissolve

    pause 3.0

    hide text with dissolve

    pause 1.0

    scene bg splash with dissolve

    pause 5.0

    scene black with dissolve

    pause 2.0

    scene black


    n "{cps=60}I've always believed that there are many kinds of people.{/cps}"

    n "{cps=60}Those who calmly stroll through their uneventful lives, the ones who meander from this interest to another, they who walk in the shadow of others more notable than themselves, and so on.{/cps}"

    n "{cps=60}As for me... I was the type who ran. The people I wanted to be with, what I wanted to do with my life, where I wanted to be, I knew the answers to all those questions.{/cps}"

    n "{cps=60}I had my worries and concerns, of course, but those meant nothing when living with such purpose. My ambition was what set me free. For those fleeting years of my childhood, I was unstoppable.{/cps}"

    n "{cps=60}Three years ago, that world ended.{/cps}"


    nvl hide dissolve

    nvl clear

    scene black with fadeslow
    stop music
    pause 1.0
    play music sfx_tcard
    show neutral with fade
    show act1card with passingact
    pause 10.0
    stop music fadeout 2.0

    return


label summersclover_ch1:
    scene bg school_gardens_ss #black
    with dissolve

    play music music_tranquil fadein 6.0 ##was Miki's theme in original script # start with Miki's theme
    $ persistent.song2 = True

    window show

    play sound sfx_can_clatter

    "The rattle of a can hitting the vending machine rings out across the empty school grounds. With the orange of sunset settling over the campus, everyone's retreated to their dormitories and homes for an early start to their studying and various hobbies."

    "Without much else to do, I wander through the gardens while drinking to make the best of the unusually quiet surrounds."

    "Summer's biting particularly hard this year. At least, that's what everybody's been complaining about lately. I don't really see the problem, but I've always been more used to hot weather than others."

    "With little around me to think about, beyond the occasional sip from the can, my mind turns to something that has been bugging me."

    "Every day feels the same. The school week begins, I attend classes, school week ends. Laze around for the weekend, and then it all repeats once more. 'Stagnant' is probably the best word for it."

    "It's not that I hate such a life. Compared to how I've lived before now, it's something I feel I should probably treasure."

    "But my life is also finite. No matter how blissfully unaware I am of it, time still passes. Maybe it's summer holidays that've focused my thinking, or maybe the exams beforehand. Either way, this way of living will end."

    scene bg school_track_ss
    with locationchange

    play ambient sfx_parkambience fadein 1.5
    $ renpy.music.set_volume(0.5, 1.5, channel="music")

    "Emerging through the line of trees separating the track from the main grounds, the movement of a lone person immediately catches my eye."

    "His figure casts a long shadow in the evening's light as he slowly runs along the far side of the track. Looks like it's hard going, with his arms swaying to and fro as he valiantly pushes himself onwards."

    "I idle up to the side of the track and take another swig. It's a welcome distraction from my troubling thoughts."

    "As he comes around the corner, it's possible to finally get a good look at him."

    "I'd recognise those disheveled locks of Hisao's anywhere. While his natural habitat may be the classroom, I've seen him spluttering around the track alongside Emi a couple of times before."

    "Dressed, as always, in his shirt without the bothersome jacket, it's clear that he has a nice build. That said, despite his solid chest and broad shoulders, there's an unassuming air to him. Perhaps it's due to his rather plain face, or just his subdued nature from having recently changed schools."

    "Without anything in particular to say to the boy, I just take another sip of my drink as he continues up the track."

    "Maybe the normal thing to do here would be to cheer him on for throwing himself at the track with such gusto, but it really doesn't look like he's enjoying the ordeal."

    "His running form is becoming worse and worse, and his speed is noticeably slowing. Even the bird that's swooped down to peck at something left in the grass doesn't bother moving as he runs by."

    "It reminds me of how I used to throw myself at the track, running however many laps I could before I broke from exhaustion."

    "I move to take another swig from my can as he comes back around, only to find it lacking. With my attention briefly diverted from Hisao to my sadly empty drink, I'm take mildly off guard as he stumbles off the track and comes to a haphazard stop just ahead of me."

    #stop music fadeout 2.0

    $ renpy.music.set_volume(1.0, 4.0, channel="music") # restoring music volume

    show hisao_talk_small_u with dissolve
    $ renpy.music.set_volume(0.5, 1.5, channel="music")
    #play music music_pearly fadein 1.0 #this is so loud it drowns out the park sfx :/ ##was afternoon music in original script

    hi "Can I... help you...?"

    "Not knowing if he'd even be able to hear me past his panting, I let him collect himself for a few seconds before answering."

    mk "Just watchin'."

    hi "Yeah... I can see that."

    show hisao_wtf_u with charachange
    hide hisao_talk_small_u

    stop music fadeout 1.0
    stop ambient fadeout 1.0

    "He clutches at his knees and tries his best to regulate his breathing, but it's in vain. It's when he clutches at his chest and his breathing noticeably rises in pitch that I start to get a bit worried."

    mk "You okay? Looks like you kinda overdid it, there."

    hi "I'm fine. Totally fine."

    "If he's going to be like that, all that I can do is take a step back and let him recuperate."

    "Beyond his breathing and a slight breeze in the trees, there's nothing to be heard. It reminds me just how alone we are, likely being the only two people in the entire school grounds right now."

    show hisao_erm_u with charachange
    hide hisao_wtf_u

    play music music_pearly fadein 1.0
    play ambient sfx_parkambience fadein 1.0
    $ persistent.song3 = True

    "After who knows how much time, he finally manages to compose himself and stand upright, sweat still tricking down the side of his face. There's a sickly wheeze to his breathing, but I don't think he wants to be reminded of it."

    hi "Miura, right? I'm Hisao Nakai."

    mk "The mysterious transfer student himself. Pleased to meet ya."

    hi "What brings you out here, anyway?"

    mk "Just grabbin' a drink. You?"

    hi "Missed my morning run. E... I mean, Ibarazaki, said I should run in the evening to make up for it."

    mk "Don't worry, I know Emi. Damn near all the school does."

    "I nod towards the track, the bird still out there trying to drag a left over food packet away."

    mk "Just how long have you been out here?"

    hi "A while. I should probably just cut my losses and get dinner, but she'd kill me if I skipped out."

    mk "Man, just give up."

    "Come to think of it, this might be a good chance. Dinner alone is boring, and if I can twist him into paying for a meal, all the better."

    mk "If you're hungry, I know a good place if you're up for it."

    show hisao_talk_small_u with charachange
    hide hisao_erm_u

    "He looks a little startled by the suggestion, running a hand through his hair as he tries to settle himself down and think things through. I can practically see the gears turning in his head as he selects his choice."

    mk "C'mon, a hot girl's asking you to eat with her. You're gonna refuse that?"

    show hisao_heh_u with charachange
    hide hisao_talk_small_u

    hi "They say modesty is a virtue."

    mk "Never said I was a virtuous person."

    "May as well wait things out as he continues with his deliberation, as I'm pretty confident I know what the reply will be. Sure enough, he finally comes up with an answer."

    show hisao_smile_u with charachange
    hide hisao_heh_u

    hi "Fine, I'll go along with you."

    stop ambient fadeout 2.0
    stop music fadeout 2.0

    $ renpy.music.set_volume(1.0, 4.0, channel="music") # restoring music volume

    #centered "~ Timeskip ~" with dissolve
    scene bg suburb_shanghaiext_ss
    with shorttimeskip #locationchange

    "The Shanghai's location within the nearby town has always been convenient. I had thought even this might be too much for Hisao given his exhaustion, but he managed to drag himself here just fine."

    play sound sfx_storebell

    scene bg suburb_shanghaiint
    with locationchange

    play music music_miki fadein 1.0
    $ persistent.song4 = True

    $ renpy.music.set_volume(0.5, .5, channel="ambient")
    play ambient sfx_crowd_indoors fadein 1.0

    show hisao_erm_u at centersit
    with dissolve
    hide hisao_heh_u

    "I like the uniforms they have here, even if they do strike me as a little unconventional. Our meals placed before us, the waitress takes her leave to attend to a handful of other customers at the opposite end of the cafe."
    "Not being especially hungry, my meal's just a slice of pie and a drink. Hisao's pack of sandwiches don't look like it'll last for long, one of them already having disappeared into his mouth."

    "He catches me staring, awkwardly holding the next midair while looking mildly embarrassed."

    hi "Sorry, I just..."

    mk "It's normal to be hungry after exercise, man. Go ahead and stuff your face."

    show hisao_talk_small_u at centersit with charachange
    hide hisao_erm_u at centersit

    "Hisao obediently does so, though with a touch more delicacy than before."

    mk "So what's the story with Emi, anyway?"

    hi "She just pushes me to exercise with her sometimes. Guess she enjoys the company. I mean, like you do now."

    mk "Doesn't seem like you enjoy the experience much."

    hi "Well, I do want to get back into shape. As much as I can, anyway."

    show hisao_frown_u at centersit with charachange
    hide hisao_talk_small_u at centersit

    "He pulls his cuff up his arm a little, taking a loose flab of skin from his forearm and giving it a pinch as he frowns. He sure is pale under his shirt, though maybe I'm not the best judge of that."

    mk "You sure found the right person if you want to be whipped into shape. Just make sure she doesn't kill you first."

    hi "Believe me, she's come close."

    "His tone is way too serious for a throwaway joke. Surely she's not that much of a slave driver."

    "Taking a bite into my own food, it turns out I'm surprisingly hungry myself. The two of us end up stuffing down our food in no time, crumbs littering the table in the aftermath."

    show hisao_erm_u at centersit with charachange
    hide hisao_frown_u at centersit

    "With dinner finished, Hisao leans back in his seat and contentedly pats his stomach. I run my finger around the inside of my mouth to work out the remnants stuck to my teeth, savouring the taste of the last little bits I manage to find."

    "At first I take Hisao's staring out the window to be a sign of boredom, but one careless glance gives his game away. He's trying to distract himself from the bandaged stump resting on the table."

    "I'd hardly think worse of someone for looking at it; being distracted by something out of the ordinary is completely normal. I just give a smile, hoping to make him relax a bit."

    hi "Sorry."

    mk "Believe me, you're not the first to notice. It's not like a missing hand is exactly subtle."

    "Hoping, and succeeding, to defuse the situation a bit, I grin and waggle my stump in the air a little to emphasise the point. It's delightfully easy to read Hisao's emotions, even when he's trying his best to suppress them."

    hi "I still have no idea what to make of this place."

    mk "Town, or Yamaku?"

    "He just raises an eyebrow."

    mk "What's the problem with it?"

    hi "Hmm... I think 'confronting' would probably be the right word."

    hi "It's not every day you see someone with half their face heavily scarred, or have to try and communicate with someone who can't hear. Then there's the obvious example of Emi."

    mk "Well, I mean, you're not wrong. Being a transfer student would make that a lot worse, too."

    mk "Try coming at that from another angle, though - what're we doing now?"

    hi "Chatting at a cafe?"

    mk "And what'd you do today before that?"

    hi "Woke up, got dressed, went to classes, had lunch and tea in a club room, more classes, went to run on the track, and then started chatting with you."

    mk "Isn't that a pretty normal high school day?"

    show hisao_talk_small_u at centersit with charachange
    hide hisao_erm_u at centersit
    show hisao_erm_u at centersit with charachange #followed by hisao_erm to make an opne-close mouth animation
    hide hisao_talk_small_u at centersit

    "He moves to protest, but finds himself searching for words. However reluctantly it may be, he backs down once he realises that I have a point."

    mk "You'll get used to it soon enough. If everyone else at school seems cool with it, that's only because we all had a head start of years."

    show hisao_talk_small_u at centersit with charachange
    hide hisao_erm_u at centersit

    hi "And if I accidentally offend someone? I almost did just then, remember?"

    mk "Then... so what? Just find someone else to talk to. There's hundreds of people here to pick from. Hell, you're talking to me easily enough."

    show hisao_erm_u at centersit with charachange
    hide hisao_talk_small_u at centersit

    hi "A pretty normal high school, huh..."

    mk "Exactly. Just pick up some friends, find your groove, and ride the rest of the year out. You'll be fine."

    "He turns to look out the window, reflecting on the conversation. That expression of contemplation suits him well."

    "Evidently coming to a conclusion, he gives a nod before turning back to me."

    show hisao_smile_u at centersit with charachange
    hide hisao_erm_u at centersit

    hi "Thanks. I'll keep that in mind."

    stop music fadeout 1.0

    "The smile he gives me is kinda sweet. Weak, but terribly sincere. All I can do in response is give a satisfied grin back."

    "Such a chance meeting might not change much for me, but if I can help Hisao get on the right track, at least I'll have been useful to someone."

    "The weather really is nice today."

    ##stop music fadeout 2.5

    stop ambient fadeout 2.5
    $ renpy.music.set_volume(1.0, .5, channel="ambient")

    window hide

    scene black with dissolve

    call summersclover_timeskip

    return
