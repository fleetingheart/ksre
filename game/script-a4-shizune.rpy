# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

label a4_shizune:
    label .grand_strategy:
        scene bg school_library
        with locationchange

        play music music_happiness fadein 2.0

        "Only a day later, the weekend has already arrived. I drop a heavy stack of books on the librarian's desk, not meaning to slam them, but they weigh so much that it happens anyway."

        $ renpy.music.set_volume(1.0, 0.0, channel="sound")
        play sound sfx_impact

        show yuuko panic_up:
            center
            ypos 1.2 alpha 0.0
            easein 0.25 center alpha 1.0
        with vpunch

        show yuuko panic_up at center

        "Yuuko bolts out of her chair with enough force to dislodge her glasses. She barely holds on to them."

        show yuuko neutral_up
        with charachange

        yu "Oh, hi."

        hi "Sorry. I'm here to return all those books I was supposed to."

        show yuuko worried_down
        with charachange

        yu "That's great, but I wish you had brought them back sooner. It wouldn't be a problem if the library had more copies of everything, but it doesn't… and they act like that's my fault."

        hi "'They?'"

        show yuuko panic_down
        with charachange

        yu "Other students. They can be… um, pretty pushy."

        hi "Sorry. It just kind of slipped my mind. It's been a pretty rough couple of days."

        show yuuko worried_down
        with charachange

        yu "Oh… Um, I suppose you don't want to talk about it…"

        $ renpy.music.set_volume(0.5, 1.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=60}Yuuko meekly turns to the task of logging all the books I've brought back as returned, treating them with extreme care and precision, like she's a bomb disposal technician rather than a librarian."

        n "Over the past couple of days, I've been thinking about something Misha said. Of course, I'd thought about everything she said, but one thing in particular keeps coming back. She talked about how she didn't want to miss people or think about being apart from them any more."

        n "When I recalled those words, they stopped me cold, like a sharp slap across the cheek. In just a few months, we'll be graduating. Misha and Shizune were nearly inseparable, but after graduation, they might never see each other again. I wonder if that thought is what started all of this."

        n "If Misha were to try and talk to Shizune about it, Shizune likely wouldn't think about it at all. It would sadden her, and for that reason, she would try and toss it away. For someone like Shizune, who is so quick to suppress her worries, it would be easy."

        nvl clear

        n "{vspace=60}Misha turned out to be more sensitive than she seemed. It would have crushed her, even more so because Shizune's reaction could come off as pretty cold. I don't know if that's how Shizune handled it, but it seems likely, and I can understand why she would act that way."

        n "I can also understand why Misha would be troubled by the thought of drifting away from someone who is such an important part of her. I'd never thought about graduation until that moment."

        n "Then I began to think things like, 'Has it really only been less than a year?' I started thinking of everyone I've met. Not only Shizune and Misha, but everyone else. They were fond thoughts. Then, I thought of losing them. Suddenly, I could understand Misha's anxieties."

        n "{vspace=30}It could be nice to talk to someone about it."

        $ renpy.music.set_volume(1.0, 1.0, channel="music")

        nvl hide dissolve
        nvl clear

        hi "Actually, I kind of want to."

        show yuuko worried_up
        with charachange

        yu "With whom?"

        "I can sense an obvious tinge of apprehension in her voice."

        hi "With you."

        show yuuko neurotic_up
        with charachange

        yu "Ah… Really? Are you sure? W-why me?"

        hi "Because you're an adult."

        show yuuko neurotic_down
        with charachange

        yu "That's it? Ahhhh… that's…"

        "Wincing, she fidgets a little in her seat, trying to get comfortable in a pretty uncomfortable-looking way. I guess this means she's okay with it."

        hi "Is it hard, being an adult?"

        show yuuko cry_down
        with charachange

        yu "Yes."

        show yuuko panic_down
        with charachange

        yu "I don't think I'm that old, though… It's surprising that students now, l-like Shizune and you, wear stuff like perfumes or cologne… I never did. I still don't use them…"

        show yuuko worried_up
        with charachange

        yu "Um, by the way, you're not wearing your grape cologne today."

        hi "Yeah, it wasn't working out for me."

        show yuuko worried_down
        with charachange

        yu "Oh, that's good. I thought the same thing… Sorry."

        "Yuuko looks genuinely sorry, and I feel a pang of guilt. I smile, despite myself. A tiny lie like that can come back to bite me in the butt."

        "For Misha, trying to conceal how she felt in order to put on a happy face for Shizune for so long must have been crushing."

        hi "Someone I know brought up that we're going to be graduating, and I realized that I've never thought about it before."

        hi "I feel stupid that I could go so long and never think about these things. I've met a lot of great people, and I've never thought about what it's going to be like to graduate and maybe never see them again."

        show yuuko neutral_down
        with charachange

        yu "There are still ways you could keep in touch…"

        hi "Yeah, I guess. I feel childish. I know everyone is going through the same thing, probably. I bet you hear this kind of problem a lot."

        show yuuko worried_down
        with charachange

        yu "N-no… I haven't been working here that long…"

        show yuuko worried_up
        with charachange

        yu "I worried about the same thing when I graduated from high school. Um, I didn't go to school here, though. I also miss my friends… and I wish I had kept in touch with them better. I should have tried harder."

        "Yuuko isn't really helping me feel better, and she clams up quickly when she sees it on my face."

        hi "I don't want to look back and have those same regrets."

        hi "I wonder if Shizune even thinks about that kind of stuff. Because she goes on sometimes, about how she doesn't want to live with any regrets."

        show yuuko panic_up
        with charachange

        yu "Wow… That sounds impossible, to me…"

        "I nod, only halfway wanting to agree."

        show yuuko closedhappy_up
        with charachange

        yu "Even so… I think that is kind of admirable, too… Kind of brave. Don't you think so?"

        hi "'Brave' is a new way to put it."

        show yuuko neutral_down
        with charachange

        "Yuuko shakes her head insistently."

        yu "It's true, though. And also kind of intimidating…"

        hi "Geez. You shouldn't be intimidated by high schoolers."

        show yuuko worried_up
        with charachange

        yu "I'll try…"

        hide yuuko
        with charaexit

        "She turns away to start folding a sticky note over and over. Pretty idle behavior for a university student, but more importantly, I wonder if I said the wrong thing to her."

        "Being around Shizune for so long, I can't stop reading as much as I can into every moment of silence."

        "If Yuuko were the type of person who didn't get intimidated by high schoolers, it probably wouldn't be so easy to talk to her."

        "It's all too easy to want to shed some negative quality of yours. When I think of everyone I know, it's those qualities that I like the best."

        show yuuko worried_up at center
        with charaenter

        yu "Um…"

        show yuuko smile_down
        with charachange

        yu "I don't think I really regret it. I thought, as long as I could remember the good times, that was enough."

        show yuuko worried_down
        with charachange

        yu "I don't know. …Sorry."

        "I notice a couple students starting to trickle into the library, and decide that my time is up."

        hi "No, that was helpful."

        hi "I feel like two of my friends are fighting because one of them is taking the fact that we might not see each other again after we graduate really hard. And the other is probably being stoic about it, which only makes it worse."

        hi "I don't get how I'm supposed to handle this kind of situation. It doesn't seem like the kind of problem where I'll have to end up taking a side, but it could turn out that way, and then I have no idea what I'm going to do."

        show yuuko neutral_down
        with charachange

        yu "You should tell them they shouldn't fight."

        hi "I know. Fighting is bad."

        hi "It's not Shizune and Misha, by the way."

        show yuuko worried_up
        with charachange

        yu "Okay… Um, I wasn't really thinking that, though…"

        "How embarrassing. Even though I knew it would be, I still feel my cheeks redden, and even so, I still said something so transparent and blatantly a lie. But it could be that sometimes that is the right way."

        hi "Do you have any books about people who have to make hard decisions?"

        show yuuko happy_down
        with charachange

        yu "We have a lot of self-help books…"

        "It's funny that I can find that surprising, because I wouldn't have only a few months ago."

        hi "I meant 'about,' not 'for.' There aren't many, right?"

        show yuuko worried_down
        with charachange

        yu "Yes. Um, not many, I mean."

        stop music fadeout 3.0

        "Though I feel a bit apprehensive about it, I want to talk to Shizune. I don't understand why I feel nervous about it, and that disgusts me a little."

        scene bg school_council
        with locationskip

        "It also motivates me to look for her, right then and there, although I don't have to look very hard. She's in the student council room, as always."

        play music music_pearly fadein 5.0

        show shizu behind_blank at center
        with charaenter

        "Worryingly, Misha isn't with her. When Shizune notices me and looks up from her paperwork, the first thing I ask is where she is."

        show shizu basic_normal2
        with charachange

        ssh "I don't know."

        "There is so much uncertainty in her answer that I can't let it go just like that."

        his "She's missing a lot of school."

        show shizu adjust_happy
        with charachange

        ssh "Are you the attendance police?"

        his "That's really strange, coming from the Student Council president."

        show shizu adjust_smug
        with charachange

        "Shizune hides a laugh behind a cupped hand, and I start to think that I might be worrying for nothing, but then her laughter slowly fades away to a more serious and pensive expression."

        show shizu basic_normal
        with charachange

        ssh "You're right."

        show shizu behind_blank
        with charachange

        ssh "Yesterday,"

        show shizu adjust_happy
        with charachange

        "I catch the hint of a knowing smile on her face when she sees my poorly-hidden panic at the word. Despite her best efforts, she can't help being satisfied in eliciting surprise from everyone else, to the very end."

        "Even then, I can see that she has bigger concerns from how quickly her smile vanishes."

        show shizu basic_angry
        with charachange

        ssh "…before either of you noticed me, I saw what you were saying. I'm not stupid."

        show shizu behind_frown
        with charachange

        ssh "If I hadn't, I could still see through Misha while we were walking back. Even if she hadn't told me everything later. She didn't make a big deal out of it, but any way you look at it, it's my fault, isn't it?"

        his "What did she tell you?"

        show shizu adjust_frown
        with charachange

        "Shizune winces at the question, though it's clear she's been expecting it. She follows it up with a very grand gesture."

        show shizu basic_normal2
        with charachange

        ssh "A lot."

        show shizu adjust_frown
        with charachange

        ssh "Like, that I can be selfish, and confusing. I try too hard to bring people around me, and then push them away."

        show shizu basic_normal2
        with charachange

        ssh "I didn't know what I should do. I thought she was right to mention all of those things, so I just agreed with her, but that only made things worse."

        show shizu behind_sad
        with charachange

        ssh "I don't understand."

        "Adjusting her glasses, she looks pretty tired. I hope it isn't because she's been busy avoiding Misha, but I can't help considering the possibility, seeing where this conversation is going."

        show shizu adjust_smug
        with charachange

        ssh "It's true. Even the Student Council being this small, and us always being swamped with work, is my fault. I might have even ended up driving a lot of people off, and away from the Student Council, acting like that."

        "Shizune wags a finger mischievously, acknowledging that 'might' is an understatement. However, from how wearily she does it, it's obvious the humor is only to put me at ease, and therefore not genuine."

        show shizu basic_normal
        with charachange

        ssh "Like Lilly, for instance. She was the first person to join when I started trying to recruit people again after everyone else left, because they couldn't stand me, I guess."

        show shizu adjust_happy
        with charachange

        ssh "We managed to put together the last festival, and even ran a booth together at the last minute."

        show shizu behind_frown
        with charachange

        ssh "But I didn't like her because I thought she was selfish, always holding us up in order to tend to one friend of hers or another, and leaving Misha and me alone to sort out things involving the whole school by ourselves."

        show shizu cross_angry
        with charachange

        ssh "If there were any problem she was going through, she would leave us high and dry while she panicked over it, and wouldn't come back until it was solved."

        show shizu adjust_angry
        with charachange

        ssh "She would focus on it one hundred percent, and be too preoccupied to focus on any student council work!"

        show shizu behind_frustrated
        with charachange

        ssh "That was the worst, to me, that she could be so nice and still take so many people for granted. Why even join the Student Council, then? It seemed so shortsighted and selfish, don't you think?"

        show shizu basic_normal2
        with charachange

        ssh "But, it's actually me who's that way."

        show shizu adjust_frown
        with charachange

        ssh "Like Misha said, always trying to pull people close to me and then shutting them out."

        show shizu behind_sad
        with charachange

        ssh "That is how I've treated her, which makes me a bad friend. And it feels like I did the same thing to you, then, so I guess I'm a bad girlfriend, too, even if Misha says that you might as well replace her."

        show shizu basic_normal2
        with charachange

        ssh "I'm angry that I screwed things up enough for it to get this out of hand. All I wanted was to…"

        stop music fadeout 3.0

        "She pauses to look for the right words, tenting her fingers in concentration."

        show shizu behind_blank
        with charachange

        ssh "Make people happy, I think."

        show shizu adjust_happy
        with charachange

        ssh "Even though that seems like a simple way to put it."

        "As she rests her head against her hand, Shizune's bangs fall delicately across her eyes, hidden behind those polished glasses reflecting just the tiniest bit of light."

        "It may be wrong to think so, but right now, she seems especially beautiful. Like a more complete person."

        "It feels like this is my first chance to respond to her outpouring of emotions. Replacing Misha as Shizune's interpreter? Misha must be joking."

        "It took all my energy to keep up with her just now, her signing filled with gestures that I've never seen before."

        "Likely, they're habits picked up from Misha, and developed from years of them being together. I could never replace someone so close to her."

        his "I like you because I like you, not because I got tricked into it by you."

        "Despite how hard she tried, anyway. I continue to stare back into her eyes, as sharp as ever. The first time I saw them, they had seemed a bit intimidating to me. Like the eyes of a predator. That hasn't changed, which I find reassuring."

        show shizu basic_normal
        with charachange

        ssh "I still want to make everyone happy."

        his "Starting with Misha?"

        play music music_shizune fadein 6.0

        show shizu basic_frown
        with charachange

        "Shizune looks a bit annoyed that I would imply she would start with anyone else, and smiles confidently, as though a friend's sadness is a physical opponent she can just strangle into submission."

        show shizu behind_frustrated
        with charachange

        ssh "Of course; obviously; naturally."

        show shizu adjust_noglasses
        with charachange

        "Taking off her glasses, she leans back in her chair and lets out a sigh. It's the first time I've seen her without them on, but I don't get a good look before she slips them back on."

        show shizu behind_smile
        with charachange

        ssh "But, I'm too tired to start today. First thing tomorrow."

        show shizu basic_normal
        with charachange

        ssh "Do you want to help?"

        his "Yeah."

        show shizu adjust_happy
        with charachange

        ssh "And… I have other student council stuff you could help me with, while you're at it."

        "Although it turns out that there isn't much other work at all."

        stop music fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .off_by_one:
        scene black
        with dissolve

        pause 2.0

        play sound sfx_doorknock

        pause 2.0

        scene bg school_dormhisao
        with openeye

        play sound sfx_doorknock

        "There's no school today, so I expected to be able to sleep in late. Unfortunately, I'm awakened by someone mercilessly pounding on my door at eight in the morning."

        "At first, I think it could be Kenji, but when my shouts of annoyance go unanswered, I realize it's Shizune."

        play sound sfx_dooropen

        scene bg school_dormhallway
        show shizu adjust_happy_close at center
        with locationchange

        play music music_another fadein 0.5

        show shizu behind_blank
        with charadistant

        "She immediately backs away from the door when I open it, quickly concealing something behind her back. Kind of ominous."

        his "What's that? Is it a surprise? I don't really like surprises."

        show shizu behind_frown
        with charachange

        "The displeased expression on her face says that she wants me to stop being such a wet blanket, but she's too busy fumbling with what's behind her back to sign it."

        show shizu adjust_smug
        with charachange

        "It must be frustrating for her, because seconds later, she swings the object out, proudly, and also a little dangerously."

        show shizu basic_happy
        with charachange

        ssh "Ta-da. A picnic basket. We can have lunch together, the three of us."

        "It's not really a basket, it looks more like a plastic bag. Taking a quick look inside, I can see that most of the food inside is also store-bought, not homemade. Some items still have the price stickers on."

        "There's a very diverse selection here, though. Even a tiny tin of caviar. I'm slowly becoming more impressed with this lunch. I pick a grape out of there and pop it in my mouth."

        show shizu adjust_frown
        with charachange

        ssh "Don't just take things like that! I spent all night perfecting this final weapon."

        show shizu adjust_frown:
            ease 0.5 ypos 1.2

        pause 0.5

        play sound sfx_pillow

        show shizu basic_normal:
            ease 0.5 center
        with charachange

        show shizu at center

        "Shizune places it down on the ground to free up her hands, and immediately starts playfully tapping it between her feet like a soccer ball. Definitely not what you should do to anything you're going to call a 'final weapon.'"

        show shizu adjust_happy
        with charachange

        ssh "All part of my 'get-Misha-to-stop-being-so-depressed' plan. I stayed up all last night working on it."

        show shizu behind_smile
        with charachange

        ssh "When we tried to order in last time, Misha barely got anything, and used it as an excuse to leave early. I won't let her get off so easily this time. The food is already here. She'll have to sit down and eat with us."

        show shizu basic_happy
        with charachange

        ssh "It's the perfect bait. Doesn't everything look irresistible? I tried to make it myself, but I don't know how to make it look all fancy, so I ended up buying everything. Still looks delicious, doesn't it? It should be."

        "She's very perky today, juiced up on the thought of cheering Misha up. Although it's odd to see her so happy about it, I know that she's just as unsure now as she was yesterday."

        "The only thing that has changed is that by viewing it as another sort of challenge for herself, she can put her worries aside and throw herself into it recklessly."

        "It has worked well enough for Shizune so far. It wouldn't surprise me if it's the only way she knows how to live."

        his "It's a little early, though…"

        show shizu adjust_frown
        with charachange

        ssh "It's already eight in the morning, that's late! Even Misha gets up at eight or nine. She goes to bed at 7:00 p.m., but that isn't important."

        his "It's very important."

        show shizu basic_normal_close
        with characlose

        "Shizune ignores me, gagging my hands by taking them in hers instead of a more proper rebuttal. The way she lingers against me a moment longer than expected feels really comforting."

        show shizu adjust_happy_close
        with charachange

        ssh "The point is, she's awake right now, walking around somewhere. Let's go find her."

        scene bg school_courtyard at bgleft
        with locationskip

        "She sprints out the door impatiently, and her gusto as she drags me along looking for Misha makes me feel more like I'm following a hunter on a safari than looking for a mutual friend."

        "We don't have to look very hard. Even cropped short, her pink hair stands out. The fact that she's just meandering around the grounds out in the open makes it even easier. Now I'm sounding like a safari hunter."

        show shizu adjust_happy_close at tworight
        with charaenter

        shi "…!"

        hi "Misha!"

        show mishashort hips_smile behind shizu at twoleft
        with charaenter

        mi "Huh~?"

        hi "We were just looking for you."

        show shizu behind_smile_close
        with charachange

        ssh "It's a good day for a picnic, you should join us. We even have caviar; not sturgeon, of course, but really tasty."

        show mishashort perky_confused
        with charachange

        mi "Caviar? Surgeon?"

        "Apparently finding it annoying to have to explain anything at length with only one hand, Shizune gives up quickly."

        show shizu adjust_frown_close
        with charachange

        ssh "Fish eggs."

        show mishashort sign_confused
        with charachange

        mi "What?"

        show shizu behind_smile_close
        with charachange

        ssh "It tastes good."

        show mishashort cross_smile
        with charachange

        mi "Sorry, Shicchan, I think I'll pass for today."

        show shizu basic_angry_close
        with charachange

        "When Misha starts to walk away, Shizune holds the bag out towards me, needing me to take it so that her hands can be free."

        show mishashort:
            ease 1.0 center
        show bg:
            ease 1.0 center
        show shizu behind mishashort:
            ease 0.5 tworight xpos 0.725

        pause 0.5

        show shizu behind_blank behind mishashort:
            ease 0.5 xpos 0.75
        with charadistant

        show mishashort perky_confused:
            center
            xpos 0.35
        show shizu:
            tworight
            xpos 0.65
        show bg:
            center
            xpos 0.43
        with charamovechangefaster

        "As soon as it's out of her hands, she darts in front of Misha, cutting her off."

        show shizu adjust_happy
        with charachange

        ssh "I made so much food, though."

        show mishashort perky_sad
        with charachange

        mi "Sorry, I'm just not hungry right now."

        show shizu behind_blank
        with charachange

        shi "…"

        show shizu behind_frown
        with charachange

        ssh "When are you going to be hungry, then?"

        show mishashort hips_frown
        with charachange

        mi "Shicchan, that's impossible to know~."

        show shizu adjust_frown
        with charachange

        ssh "You can guess."

        "The tension between them infuriates Shizune, and she's trying to deal with it by trying to tear through it. But that approach isn't going to work."

        "I'd thought, and hoped, that Misha had gotten herself together, but I guess she was just cut too deep by what happened."

        "In that case, it's really out of anyone's hands. I believe that Shizune might understand that, on some level. If she didn't, she wouldn't have any doubts at all."

        "Because she can't speak, though, I've learned to notice her hesitation. It's very clear; she might as well be screaming."

        show mishashort sign_smile
        with charachangealways

        hide mishashort
        with charaexit

        stop music fadeout 5.0

        "Misha waves her hands in front of her, not wanting to continue the discussion any further, and quickly slips away. Shizune fumes silently, reluctant to let her go but having no way to keep her here."

        "As Misha's back grows smaller in the distance, I wonder where she's heading off to. Is Shizune wondering the same thing, as she bites her lip in frustration?"

        "I want to touch her reassuringly on the shoulder, but I stop myself, not knowing if it's the right thing to do."

        "Not because she looks fragile, vulnerable, or sad. It's the opposite. After a while, her expression belies no emotion at all. Only contemplation. Suddenly, she whirls around."

        play music music_dreamy fadein 4.0

        show shizu basic_angry at center
        show bg at right
        with charamovechangefaster

        ssh "Now all this food is going to go to waste."

        his "Yeah."

        show shizu behind_sad
        with charachange

        ssh "That makes me mad."

        "Although it's obvious Shizune is more hurt than mad. The bag dangling from my hand feels like it's filled with lead."

        show shizu behind_blank
        with charachange

        call screen doublespeak(ssh, _("Let's go on a date."), his, _("Let's use it, then."))

        show shizu adjust_blush
        with charachange

        shi "…"

        show shizu basic_normal
        with charachange

        ssh "Where do you want to go?"

        his "I don't know."

        show shizu behind_blank
        with charachange

        ssh "The roof."

        show shizu adjust_happy
        with charachange

        ssh "It's my favorite spot."

        "A wry smile appears on her face, disappearing just as quickly."

        play ambient sfx_rooftop fadein 1.0

        scene bg school_roof
        show shizu behind_frown_close at center
        with shorttimeskip

        "On the roof, I immediately crack open the caviar, ignoring a derisive look from Shizune all the while. I end up putting it down immediately."

        his "Where are the toast points?"

        show shizu basic_normal2_close
        with charachange

        ssh "I didn't make any. Like I told you, I bought everything."

        his "Not toast points, though…"

        show shizu adjust_frown_close
        with charachange

        ssh "Why is that important? Anyway, they don't sell just toast points. That would be stupid."

        his "I bet they do."

        show shizu behind_blank_close
        with charachange

        ssh "Maybe in stores for the exceptionally lazy, but not here. Why don't you use a tortilla chip?"

        his "A tortilla chip is not the same."

        show shizu basic_frown_close
        with charachange

        ssh "They're both triangles. Stop being such a princess. I didn't know there was a proper way to eat caviar, this is the first I'm hearing of it."

        his "It's not the same thing at all."

        show shizu adjust_smug_close
        with charachange

        "I can't be decadent like this. And anyway, how can she not know? She lives in a huge mansion. Shizune takes the opportunity to scoop half the tin onto a single chip in the meantime."

        his "Hey!"

        "I'm sure it doesn't even taste good like that."

        show shizu behind_smile_close
        with charachange

        shi "…"

        "There is too much food here for two people. Because we can't communicate with each other while we eat, both Shizune and I have a lot of time to sit in silence and think about the fact that Misha, the person she set all this up for, isn't here."

        show shizu basic_angry_close
        with charachange

        ssh "It's annoying that she isn't here. I can't even enjoy my meal like this."

        "I stare at the paper cup next to her, still half-full of juice."

        his "I thought you didn't want all this food to go to waste."

        show shizu adjust_frown_close
        with charachange

        ssh "I wanted Misha to be here, too. That was the whole point. I wasn't able to accomplish what I wanted to, so it doesn't taste good."

        show shizu behind_blank_close
        with charachange

        ssh "You should eat it. Eat more."

        his "I want the fried things, though. You keep eating them all, even though you say they don't taste good."

        show shizu basic_normal_close
        with charachange

        ssh "Fried things are always delicious. There is always an exception for them."

        his "You'll get fat."

        his "I think you're being too aggressive."

        show shizu behind_blank_close
        with charachange

        ssh "It's like I told you yesterday, I'm only trying to cheer her up."

        his "Yeah, but it seems more like you're planning a military campaign."

        show shizu basic_normal2_close
        with charachange

        ssh "I'm only trying to take it seriously."

        show shizu behind_sad_close
        with charachange

        ssh "…And this is the only way I know how to do it seriously."

        show shizu basic_normal2_close
        with charachange

        ssh "I feel so powerless. I hate it. I can't even yell at her, too, even though I want to. Yelling is for serious occasions, right?"

        his "Yeah."

        show shizu adjust_frown_close
        with charachange

        ssh "You should yell at Misha for me. You can tell her that I want her to stop being so down. Even if she feels sad and alone, it's no reason to stay gloomy forever."

        his "Why don't you?"

        show shizu basic_frown_close
        with charachange

        ssh "I already did."

        show shizu behind_blank_close
        with charachange

        ssh "Over a game of dice."

        show shizu basic_happy_close
        with charachange

        ssh "Under-Over, to be exact. I won! Five times!"

        "Only the two of them would take so much pride in winning games of pure chance."

        show shizu adjust_frown_close
        with charachange

        ssh "Then, I tried to talk to her, but it didn't go so well, obviously."

        his "Well, so did I. I tried and failed."

        show shizu basic_normal2_close
        with charachange

        ssh "My goal has always been to do everything better, though."

        his "Yeah, your one-upmanship is really something."

        show shizu behind_frustrated_close
        with charachange

        ssh "But I failed too…"

        show shizu basic_normal2_close
        with charachange

        ssh "That's why I want your help."

        show shizu behind_sad_close
        with charachange

        ssh "I don't understand what I'm supposed to do any more."

        "For someone like Shizune, who has only ever interacted with the world by locking horns with every obstacle in her path, understanding only goes so far."

        $ renpy.music.set_volume(0.5, 2.0, channel="music")
        $ renpy.music.set_volume(0.5, 2.0, channel="ambient")

        scene bg misc_sky:
            xalign 0.0
            warp acdc_warp 30.0 xalign 1.0
        with locationchange

        nvl clear
        nvl show dissolve

        n "{vspace=60}I want to tell her that she doesn't have to worry. That she is great at cheering people up, because she managed to cheer me up, my first week here."

        n "In retrospect, I must have looked like kind of a dick, being in such a sour mood from the moment I came here. Even though I don't think I was being unreasonable."

        n "Even having months to digest it, finding out that you have a heart defect like I did is hard to deal with. I'd had had much less time to mull over suddenly being transferred to Yamaku, on top of that."

        n "{vspace=60}Spending the festival with Shizune really helped me out of a rut. I was happy, enough to forget that the entire time it had felt as though she were manipulating me. I understand now that I had allowed myself to be manipulated."

        nvl clear

        n "{vspace=60}Even though I felt like I was at the bottom of the world, I still wanted to have a normal life again, I'm sure, because I enjoy what I have now. I think it must be the same for everyone. Including Misha. Everyone wants someone there to pull them up, out of their self-pity."

        n "It's just that Misha always wanted Shizune to be that person, but because they can't be together, I think Misha feels that she can't accept Shizune's hand. And that frustrates Shizune. But if she could cheer up a stranger like me, then she'll die trying with Misha."

        n "{vspace=30}I can see it in her eyes, too. Though she tries to treat it like any other problem in her life, Shizune cannot do that with Misha's depression. Her thought processes are entirely different, in some ways more careful, in some ways more reckless and frenetic. She cares that much more."

        nvl clear

        n "{vspace=150}I end up not saying anything. Partly because sitting next to her like this, just the two of us, is pleasant enough in itself that I don't want to interrupt the moment with a question."

        n "{vspace=60}And partly for a more cowardly reason. I've started to think they weren't, but I don't know if her actions that day might not have been an afterthought, or even a fluke, just a collection of coincidences. I don't know if that would change anything, but I'm uncomfortable thinking about it."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")
        $ renpy.music.set_volume(1.0, 2.0, channel="ambient")

        nvl hide dissolve
        nvl clear

        scene bg school_roof
        with locationchange

        stop music fadeout 5.0

        "The fence behind me trembles slightly, and I turn to see that it's because Shizune has fallen asleep leaning against it. Considering she was up all night, it's not surprising."

        "Where does all that motivation come from? Not just in regards to Misha. I'm cynical, so it's hard for me to just accept that anyone can simply be that strong."

        "My first thought was that maybe it's because she hates herself. It's very plausible."

        "Leaning against her, I feel sad knowing that that might be the case. But it could be that we're similar in that we both want to be better people."

        stop ambient fadeout 2.0

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .invasion:
        scene bg school_dormhisao
        with openeye

        play music music_daily fadein 8.0

        "It seems like I ate too much yesterday, because I wake up in the morning feeling just nauseous enough for it to be a problem."

        "I really can't postpone going into town for shopping, though. So despite wanting to roll over and sleep it away, I force myself to get up and dress instead."

        scene bg suburb_roadcenter
        with locationskip

        "Somewhere between buying toothpaste and a few other groceries, I end up walking it off. Then, I feel hungry. After stopping for breakfast, it hits me how much time has gone by."

        "I hadn't expected to be out this long at all. I'm not even sure if I bothered to lock my door. I should really get back."

        scene bg school_dormhallway
        show hideaki bored at center
        with locationskip

        "When I get back to the dorm, I see Hideaki standing in front of my room from the entrance. I can think of few things more unexpected, and I can't help thinking I might have a heart attack just from the surprise. Fortunately, it doesn't happen."

        show hideaki normal
        with charachange

        "As soon as he sees me, he says hello in his usual detached way. I'm a little slow to reply to him, so he repeats the greeting, without missing a beat."

        show hideaki triangle
        with charachange

        hh "Hello."

        show hideaki normal
        with charachange

        hh "Is something wrong?"

        hi "I'm just surprised to see you here."

        "Not as surprised as I could have been, since it's impossible to mistake him for anyone else. I'd recognize those weird clothes anywhere. Come to think of it, I've really surrounded myself with distinctive-looking people lately."

        show hideaki confused
        with charachange

        "Hideaki's head lolls slightly to one side, a little too easily."

        hh "Why? Is it unusual to see someone's family come to see them?"

        hi "Well… yeah, actually."

        show hideaki surprise_up
        with charachangealways

        show hideaki bored
        with charachangealways

        "So, Hideaki isn't such a robot after all. In fact, it's almost as if he's more caught off guard by the fact he even can be caught off guard, but he recovers quickly."

        "Nevertheless, in that brief moment, he looks his age. That uncomfortable side of his seems like the more honest, and I wouldn't mind seeing more of it."

        "Not so much, though, that I'd go out of my way to pry. Only Shizune would be that zealous. That my thoughts get so far is proof she is rubbing off on me."

        hi "I'd think that you'd have a reason, that's all."

        show hideaki triangle
        with charachange

        hh "There is one."

        hi "See? Anyway, we can talk while we're looking for her. That's why you're here, right?"

        show hideaki normal_up
        with charachange

        hh "Shizune is in the student council room. I was looking for you. We might take a trip soon, a family trip. Do you think she would want to come with us?"

        hi "Yeah, I don't know. She's kind of been on the warpath lately, with a lot of stuff. And once she's focused on something, she won't just drop it. …I guess you would know that."

        show hideaki closed_up
        with charachange

        hh "Mm."

        scene bg school_courtyard
        with locationskip

        "Hideaki looks much more at ease walking around than I did my first week."

        hi "So, this isn't your first time here?"

        "Just throwing it out there. Of course, completely ignoring the surrounding environment could just run in the family. It'd explain why Hideaki seems so distant from Shizune. I get the feeling there's more to it than just her deafness."

        show hideaki bored at center
        with charaenter

        hh "No, but this is the first time I could walk around so much. It is kind of weird here. I bumped into a person who told me women are not allowed in the dorms."

        show hideaki disapproves
        with charachange

        hh "After I told him I am not a woman, he told me I was misleading, and then accused me of being an assassin."

        show hideaki normal
        with charachange

        hh "I was warned that he was not only invincible, but strong enough to probably destroy the building with a punch, or at least knock over the painting hanging in the hallway. By the way, that painting is actually screwed to the wall."

        hi "Yeah, that's the guy across the hall from me. He's okay."

        show hideaki triangle
        with charachange

        hh "I see. Oh, you left your door open. It was unlocked when I came here."

        "I'm a little annoyed that Hideaki knows that. The only way he could is if he had opened my door. But the feeling passes."

        hi "It doesn't matter."

        hi "I have nothing to hide, or steal."

        show hideaki happy_up
        with charachange

        hh "Your soccer ball is really nice."

        hi "That's one of the things that doesn't matter."

        show hideaki serious
        with charachange

        hh "If you are a soccer player, a soccer ball is very important."

        "I guess it is. The thought makes me smile."

        scene bg school_lobby
        show hideaki closed_up at center
        with locationskip

        hh "I'm here because my father bought a new phone, and he wanted to update Shizune, in case she needs to call him. I thought that you should know, too, since you're her boyfriend, aren't you?"

        hi "Yeah…"

        hi "…Why?"

        show hideaki bored
        with charachange

        hh "Just in case there is something wrong, or she needs anything."

        "It isn't what I meant, but I'll go along."

        hi "Even if she did, she probably wouldn't call."

        show hideaki triangle
        with charachange

        hh "That is how she is."

        hi "Well, if you know… Coming all the way here for that, though? He could have updated her via e-mail."

        show hideaki closed_up
        with charachange

        hh "He does not like using e-mails."

        hi "That's so old-fashioned. Don't tell me he still does business through regular mail, or something."

        stop music fadeout 3.0

        "Silence. Now it's my turn to feel awkward. Is Hideaki taking it literally, or did I hit the mark?"

        "Nah. I'm sure that what it really comes down to is that he does want to see his daughter and stay in contact with her. In the end, they are still family, after all. Even though they play at being at each other's throats."

        scene bg school_council
        show jigoro smug at tworight
        show shizu basic_normal2 at twoleft
        with locationskip

        play music music_happiness fadein 2.0

        "The door to the student council room is open, and Hideaki and I walk in on Jigoro in mid-rant. He sees us, but decides that it's not something worth stopping rambling at Shizune over. This is really shaking my faith in my previous assumption."

        show jigoro angry
        with charachange

        hx "When I was in the Student Council, our room was smaller. Colder, too. Like working out of a meat locker. Not like you spoiled kids. What a waste. Sitting here in your giant room, doing nothing."

        show shizu behind_frown
        with charachange

        shi "…"

        hx "Aren't there only three of you? That makes having so many desks only seem like an unnecessary display of mindless decadence. Appalling. You must use the desks you need, and not one more. It is part of my code."

        "It may be odd of me to think so, but… hearing only one half of a conversation is pretty strange. Also, that's some code."

        "Now that I've arrived, he changes the subject, and starts talking about the reason he's here."

        show jigoro neutral
        with charachange

        hx "Hideaki and I are going on a trip."

        show shizu basic_normal2
        with charachange

        shi "…"

        show jigoro angry
        with charachange

        hx "What are you doing? Does everyone who uses sign language mumble while they do it?"

        hi "No, but I'm just an amateur. It helps me think. It's kind of like force of habit."

        hx "Just an amateur… unbelievable… Fine."

        "He turns back to Shizune just in time to catch her shaking her head from side to side."

        show jigoro neutral
        with charachange

        hx "Are you sure you won't be coming along?"

        show shizu adjust_frown
        with charachange

        "She reiterates the gesture."

        show jigoro angry
        with charachange

        hx "Fine."

        show jigoro neutral
        with charachange

        hx "Can you tell her to call me if she needs anything?"

        hi "Yes."

        hi "I really think sending an e-mail would have been easier, though."

        show jigoro angry
        with charachange

        hx "I'm not going to read e-mails on my phone. If she won't speak, she can call Hideaki. I suppose if I have to be reached, you would have to call me, or that other girl would have to call me. …Hmph. Actually, all three of you can just call Hideaki."

        hide jigoro
        with charaexit

        stop music fadeout 3.0

        "And with that, he swiftly turns and leaves, Hideaki trailing behind him. A long trip, for something that took five minutes."

        "Neither of them can express their feelings very well. In Shizune's case, I have to question whether she would if she could. It explains a lot, but she doesn't seem unhappy with the arrangement. Even so, I wonder if she might be."

        play sound sfx_doorclose

        pause 1.0

        show shizu basic_normal at center
        show bg at bgright
        with charamovechangefaster

        play music music_normal fadein 3.0

        "When the door closes behind them, leaving Shizune and me by ourselves, she lets out a deep breath that seems to echo in the silence of the room."

        show shizu behind_frown
        with charachange

        ssh "It's totally ridiculous asking me to go on a trip. The timing couldn't be worse, it overlaps the student council elections, for one. Second, I haven't even cheered up Misha. If you consider that, it's annoying to even have anything else to think about."

        his "Yeah, but you might be too focused on all of that stuff right now."

        show shizu adjust_frown
        with charachange

        "Shizune adjusts her glasses roughly."

        show shizu behind_frown
        with charachange

        ssh "Completely, one hundred percent right. The minute I decided I was going to cheer up Misha, everything else went on the back burner, I suppose."

        his "I think your dad might care about you more than he lets on."

        show shizu basic_normal
        with charachange

        ssh "I know."

        his "So, then, it could be a good idea—"

        show shizu adjust_frown
        with charachange

        ssh "No."

        "And then again, more firmly, as if for both of us."

        show shizu cross_angry
        with charachange

        ssh "No."

        show shizu basic_frown
        with charachange

        ssh "After coming this far, I can't take a break. A vacation would be jarring. It would be like waking up in a different life. Yesterday was like my vacation. So now we have to go all-in."

        show shizu behind_blank
        with charachange

        ssh "I'm sorry, but it's just how I am."

        $ renpy.music.set_volume(0.5, 2.0, channel="music")

        nvl clear
        nvl show dissolve

        n "{vspace=60}I remember what Yuuko said, that she found Shizune brave, in a kind of way. I think I understand what she meant, and I have to agree. Even though it could also be called recklessness, and foolishness, and pointless stubbornness, I guess you could call it 'bravery' too."

        n "However, I can see that there is a fundamental flaw in Shizune's thinking that I hadn't noticed until now."

        n "{vspace=30}I'm sure that Shizune has reflected longer, and more arduously than I could, about where she messed up to create such a bad situation between her and Misha. However, as typical for her, she wouldn't let it hold her back and immediately set out to fix the problem."

        n "This completely ignores a large part of the problem: Misha herself. Moving from critical introspection to holding Misha up as part of a goal causes the person to get lost in the shuffle. Shizune has 'said' a lot in the past few days, but nothing about how Misha feels."

        nvl clear

        n "{vspace=60}Shizune's way of thinking is abnormal. Few normal people would reject a friend, and then expect things to go back to the way they were so easily. Shizune does, because she sees life as, if I had to put it simply, capable of being segmented and compartmentalized."

        n "Misha, like anyone else, sees it as a whole experience. A long, continuous journey, where one moment of heartache can follow you forever."

        n "For Shizune, an event is an event, and few of them cross over. Life is compartmentalized around triumphs, failures, and decisions, where each one stands as its own story. It's why the thought of a vacation is jarring to her. It's why she can only appreciate people's immediate emotions."

        n "It's exactly how someone obsessed with living in the moment would think, really."

        n "Likewise, Shizune can see Misha as a friend, but I doubt that she has ever thought of Misha as anything more until recently. Or questioned anything about her. 'Misha is Misha' would be enough for her, even if to Misha it must be unbelievably stifling."

        nvl clear

        n "{vspace=30}Shizune is just Shizune to herself. It's likely she doesn't even think about the aftereffects of her actions in the long term, as long as they stir up other people's lives. To Misha, though, I'm sure it made her seem almost heroic. Like Yuuko admiring her bravery, and even myself."

        n "And Shizune's thoughts on that sentiment are that it was good she could touch someone's life. But it ends there. It's easy to captivate; much harder to nurture. On to the next thing. Thinking of life in terms of almost completely isolated events has a tendency to isolate a person, too."

        n "Though she's trying to remedy it now, the point remains: There is simply no way Shizune could have avoided hurting Misha. Her emotional investment in Shizune was something Shizune couldn't account for, so she didn't. Combined with her personality, it was inevitable."

        n "Both of them have pretty much told me all of that in bits and pieces over the past couple months I've known them."

        n "{vspace=30}In the middle of considering their differences, an idea begins to take shape in my mind."

        $ renpy.music.set_volume(1.0, 2.0, channel="music")

        nvl hide dissolve
        nvl clear

        his "Are you working on your plan right now? This second?"

        his "Your cheer-up-Misha plan."

        show shizu basic_happy
        with charachange

        ssh "Of course. I was thinking about it the whole time I was being yelled at."

        show shizu adjust_happy
        with charachange

        "Flicking her glasses up the bridge of her nose with an oddly triumphant air, she taps her finger against her temple."

        show shizu behind_smile
        with charachange

        ssh "It's multitasking!"

        stop music fadeout 4.0

        "Really? Isn't it more like you're able to concentrate on something like that because you can't hear? Well, whatever. When I ask her what she thinks of mine, it turns out we've both arrived at a similar idea."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    label .parfait:
        scene bg school_scienceroom at bgleft
        with locationchange

        play music music_pearly fadein 5.0

        "Although it makes me feel kind of uneasy, since we're talking about a human being, the first step is to corner Misha."

        "Though the situation is a little too much like something out of a cop drama for me, it's come to this because talking to her normally is proving to be near impossible."

        "But we do have classes together. Even the very first class of the day."

        show shizu behind_blank:
            center xpos 0.75 alpha 0.0
            ease 1.0 tworight alpha 1.0
        show mishashort perky_confused_close:
            center xpos 0.15 alpha 0.0
            ease 1.0 twoleft alpha 1.0

        pause 1.0

        show shizu at tworight
        show mishashort at twoleft

        "Although it takes a while for the announcement to come, the second that I hear we're going to be working in groups today, Shizune and I try to make sure Misha is in ours."

        hi "You know, I think Mutou assigns a suspiciously large amount of group work and self-study, don't you think so?"

        show mishashort perky_smile_close
        with charachange

        mi "Hm~, but it's easy, so it's ok, right~?"

        hi "Yeah? There's other stuff that I've been thinking about lately, that might not be okay, though."

        "Misha nods after each sentence, then brushes it all aside."

        show mishashort sign_confused_close
        with charachange

        mi "I thought about it, and~… I don't do enough work when I work with you and Shicchan! So, I'm going to try harder today. So~!, don't distract me, Hicchan~. I have to stay focused~."

        show shizu behind_frustrated
        with charachange

        "That was an annoyingly transparent dodge. Shizune doesn't look too happy either, since Misha didn't bother to sign any of it, opting to twirl a pen in her hands instead."

        "From the shaky way she was doing it, I'm sure it was so she wouldn't sign anything inadvertently."

        "From the way Misha looks, distracted and uneasy, I doubt it's because she wants to keep Shizune out of the loop for any malicious reason. Although, it's still obviously a way of distancing Shizune from herself."

        hi "Shizune wants to talk to you."

        show mishashort perky_sad_close
        with charachange

        mi "…"

        show mishashort perky_confused_close
        with charachange

        mi "Can't it wait until later, Hicchan?"

        show shizu basic_angry
        with charachange

        ssh "No."

        hi "Why not now?"

        show mishashort sign_confused_close
        with charachange

        mi "We're in the middle of class~…"

        "Now she's spinning a pen in each hand. I'm beginning to think her signing has turned into a kind of nervous tic for her. This isn't a good replacement, although the sight of her dual wielding is pretty impressive."

        hi "After class, then."

        scene bg school_scienceroom at bgleft
        with shorttimeskip

        "After class, I don't waste a second bringing it back up."

        show shizu behind_frown:
            center xpos 0.75 alpha 0.0
            ease 1.0 tworight alpha 1.0
        show mishashort perky_sad_close:
            center xpos 0.15 alpha 0.0
            ease 1.0 twoleft alpha 1.0
        with None
        show bg at center
        with charamovefaster

        show shizu at tworight
        show mishashort at twoleft

        "As everyone else files out of the classroom, leaving the three of us alone, Misha takes increasingly longer glances in every direction except forward."

        hi "Do you want to get something to eat?"

        show mishashort hips_frown_close
        with charachange

        mi "Why do you and Shicchan keep asking me if I want to eat something~? ~Hicchan?"

        hi "Because we're all headed to the cafeteria, and we haven't eaten together in a long time. So, why not?"

        show mishashort perky_confused_close
        with charachange

        mi "Is this about the Student Council?"

        show shizu behind_blank
        with charachange

        shi "…"

        show mishashort perky_sad_close
        with charachange

        "Taking Shizune's lack of a reply as admission, Misha sighs."

        show mishashort hips_frown_close
        with charachange

        mi "Shicchan, is that all you ever think about?"

        stop music fadeout 5.0

        hide mishashort
        with charaexit

        "Before Shizune can reply, she leaves. I have to say, I'm not left feeling very confident after what's just happened."

        show shizu at center
        show bg at bgleft
        with charamove

        "Neither of us were expecting it to go smoothly, but it would have been nice."

        show shizu adjust_frown
        with charachange

        "Reading my mind, Shizune curls a finger around her glasses for awhile before signing."

        show shizu basic_angry
        with charachange

        ssh "I know what you're thinking, but no, it's not that I think we should give her some space now. I told you I wouldn't give up so easily."

        his "Yeah, well, now I'm starting to wonder if it's not too soon."

        show shizu behind_frown
        with charachange

        ssh "Cold feet?"

        show shizu adjust_frown
        with charachange

        ssh "Well, I'm not going to. That would be giving up on her."

        show shizu behind_blank
        with charachange

        ssh "There's a fine line between helping someone and smothering them. But I just want Misha to pull herself together and stop acting so weird."

        show shizu basic_normal
        with charachange

        ssh "I know she can do it. Even if she wants to try, people don't change overnight. If they could, the world would be a much easier place."

        his "Okay, you win."

        his "Then I guess this is the part where we split up and look for her."

        "Though I'm the only one who is really supposed to find her."

        show shizu adjust_happy
        with charachange

        play music music_tranquil fadein 3.0

        ssh "If I run into her first, I'll call your cell phone."

        "Smiling, Shizune takes out her cell phone, turning it on to prepare. I notice that she has an extremely high number of unread messages, and looking at her expression, so does she. Twirling it around by the strap a couple of times, she grimaces."

        show shizu behind_frown
        with charachange

        ssh "I don't like using this thing."

        show shizu basic_angry
        with charachange

        ssh "Why can't I just snap my fingers?"

        his "And then what? I'm not a dog. And it doesn't travel as far as a phone signal."

        show shizu behind_smile
        with charachange

        his "You're having a lot of fun with this, aren't you?"

        "Shaking her head from side to side, she continues."

        show shizu adjust_happy
        with charachange

        ssh "It's obvious where she will go. You can't look for her on the school grounds, she would want to go as far away as she can."

        show shizu behind_blank
        with charachange

        ssh "Check the tea shop? It's usually empty this early; Misha loves to go there if she feels like skipping class, and she loves the parfaits they have there."

        "'You really know a lot about her.' But she would overthink it, and turn it into something that would seem a lot more backhanded than it actually is, so I choose to just nod and leave instead, until I feel her holding on to my sleeve."

        show shizu basic_normal_close
        with characlose

        hi "What?"

        "I say instinctively, forgetting that she can't hear me."

        show shizu behind_smile_close
        with charachange

        ssh "It feels nice that I don't have to do it all by myself any more, because I can trust you. I'm really happy."

        "It makes me happy to hear it. I can't think of a way to respond, and end up only nodding again."

        play ambient sfx_crowd_indoors fadein 2.0

        scene bg school_lobby
        show mishashort perky_confused:
            center
            xpos 0.6
            ypos 1.05
        show crowd
        with locationskip

        "Heading outside, I catch a glimpse of pink hair behind some other girl's head, and as I head that way, I realize that this isn't the way you go if you want to leave school."

        "It's the way to the student council room. If I wanted to avoid Shizune, I wouldn't head there."

        "It's strange that Misha would be going in that direction, then. Maybe she wants to talk things over with Shizune."

        "In which case, I have to wonder if letting things play out naturally would be such a bad idea after all, especially if it seems to be going in a good direction."

        show mishashort hips_smile at center
        show crowd behind mishashort
        with Dissolvemove(0.7)

        "Suddenly, Misha stops and spins around, catching me by surprise."

        show mishashort hips_grin
        with charachange

        mi "Surprise~, Hicchan~! Were you looking for me? I had a feeling~!"

        "I was going to say 'Hey, I was just looking for you', but I suppose that's no good now."

        show mishashort hips_grin:
            easeout 0.7 xpos 1.0 alpha 0.0

        pause 0.7

        hide mishashort

        "She isn't even finished with her sentence before she blows past me, heading for the exit. I have to admit that Misha is infuriatingly sharper than I'd expected. Also, surprisingly fast."

        stop ambient fadeout 2.0

        scene bg school_courtyard
        with locationskip

        "Although it's more physical activity than I think I should be getting, I manage to catch up with her halfway to the gate."

        hi "You're really being the rudest woman in the world right now."

        hi "Can you just stop trying to run away for one second? I want to talk to you."

        show mishashort cross_smile at center
        with charaenter

        "Misha turns on her heel, looking mildly amused, and raises her hands as if to tell me to go on. Now that I've got her attention, though, it's hard to think of the right thing to say."

        hi "Where are you going now?"

        show mishashort sign_smile
        with charachange

        mi "The Shanghai~."

        hi "Can I go with you, then?"

        show mishashort perky_confused
        with charachange

        "Waiting for her to answer feels like an eternity. It's almost as if I can hear my wristwatch ticking off the individual seconds."

        show mishashort hips_smile
        with charachange

        mi "Okay, then, Hicchan."

        stop music fadeout 3.0

        "I get the sense that she only agreed because she doesn't want to argue any more today."

        scene bg suburb_shanghaiint
        show mishashort perky_smile:
            center
            ypos 1.02
        with shorttimeskip

        pause 0.2

        play sound sfx_storebell
        show mishashort perky_confused:
            ease 0.1 ypos 1.0
            ease 0.2 ypos 1.02

        pause 0.3

        show mishashort:
            center
            ypos 1.02

        "When we get there, a couple comes in after us, causing Misha to jump slightly at the noise."

        show mishashort perky_smile_close:
            center
            ypos 1.1
        with charamovechangefaster

        "Seeing that it isn't Shizune, she relaxes again, smiling almost as usual to order a parfait from Yuuko, and sliding into the nearest booth."

        hi "You ran off too fast. You could have at least waited to see what she was going to say."

        show mishashort hips_frown_close
        with charachange

        "Misha's angry reaction tells me it could be that she was afraid of what Shizune might say."

        mi "Why are you both doing this, Hicchan?"

        hi "Because Shizune still wants to be your friend. I guess that for her it's kinda like launching a nuclear missile from a submarine, you need two keys to do it."

        show mishashort perky_confused_close
        with charachange

        mi "…"

        hi "What else can she do, though?"

        "She isn't automatically signing whatever she hears or says any more, and I'm sure that is the reason Shizune's been having so much trouble with her."

        hi "If she tried to just talk it over, you wouldn't listen."

        show mishashort perky_sad_close
        with charachange

        play music music_night fadein 6.0

        "Misha's guilty expression tells me I've hit the mark."

        hi "Do you really hate Shizune that much?"

        show mishashort sign_confused_close
        with charachange

        mi "No, Hicchan. I told you that."

        show mishashort perky_confused_close
        with charachange

        "She answers without even flinching, idly playing with a spoon."

        hi "Yeah, I know."

        hi "I'm sure she knows it too, but I wonder if it might be easier if you did."

        hi "The only thing she's really thought about for the last week is how to make you happy. Since Shizune is still attached to you. Yesterday, though, she thought that maybe it would be easiest for you if you just hated her."

        hi "Since you didn't tell her you hate her, Shizune thinks that you can both still be friends. She's like that, only thinking in extremes."

        "Her parfait is starting to melt, the ingredients coming together in tiny rivers that remind me of the growing roots of a tree being shown through time-lapse photography."

        show mishashort cross_frown_close
        with charachange

        mi "That's stupid. Shicchan isn't that stupid, Hicchan. Don't be ridiculous~."

        hi "It's got nothing to do with intelligence. Smart people can do stupid things. And anyway, isn't it true? I was terrified last week when we talked, but at the end, I was relieved because it sounded like things might go back to normal."

        hi "I wasn't expecting you two to have a fight right after."

        show mishashort perky_confused_close
        with charachange

        mi "It wasn't a fight, Hicchan. It was just me yelling at her."

        "I've noticed that Misha's voice never really changes in tone, just volume. It's so low with guilt that I can hardly believe it came from her."

        hi "Either way, I was happy, because I thought you and her could still be friends. Since she needs you."

        show mishashort sign_confused_close
        with charachange

        mi "Hm~. No she doesn't, Hicchan."

        hi "So? How do you know that? There's a lot of things Shizune doesn't…"

        "Vocalize? Say? Talk about? I'm afraid if I say the wrong thing, it'll ruin the mood. I get to finally have a conversation with her and don't want to screw it up. I wonder if this is the first time she's had an honest conversation with me."

        hi "Just because she didn't tell you doesn't mean she doesn't like you."

        show mishashort hips_frown_close
        with charachange

        mi "That doesn't make sense…"

        hi "Yes, it does. Otherwise, she would argue back."

        show mishashort hips_grin_close
        with charachange

        mi "Wahaha~."

        hi "You don't think so? She picks fights with everyone, so why not you? Obviously, because you're her friend, and she values you. And Shizune is hurt, too."

        hi "She's just awful at showing her feelings. Usually does it the wrong way, too. But she still likes you."

        show mishashort perky_confused_close
        with charachange

        mi "Hicchan, do you remember when I said I didn't want to hate Shicchan, or upset her? The truth is~, I ended up doing both. Now it's like there's, like, an awkwardness between us. It's hard to explain."

        hi "Both of you are so stubborn. You were talking about how you didn't want to drift apart from Shizune, but then you're going to let it happen."

        hi "And Shizune is just as bad. She wants to be your friend, but respects you too much to be as aggressive as she'd be with anyone else."

        "And I'm sure that Misha interprets Shizune giving her space as a lack of caring."

        show mishashort perky_sad_close
        with charachange

        mi "I screwed up already, Hicchan. It'll happen again~, I'm sure. When I think about it that way, I don't know what I'm supposed to do. It feels like either way, I'll end up making things worse. Then, it might be better if I didn't do anything at all, right~?"

        hi "Don't be ridiculous. Why would you even think that way in the first place? Be more positive."

        "'It should be easy for you,' I want to say, but that would be presumptuous."

        show mishashort hips_smile_close
        with charachange

        mi "Hicchan~, I never knew you were so optimistic. I never expected it."

        hi "…"

        show mishashort perky_smile_close
        with charachange

        mi "You always act so gloomy when I try and surprise you."

        hi "No, this is a recent thing. Really. I just hate it when people give up easily now."

        show mishashort cross_grin_close
        with charachange

        mi "Haha~."

        show mishashort perky_smile_close
        with charachange

        mi "'Now,' huh~…?"

        hi "It makes me mad when people give up. I used to think that giving up was kind of like running away, since that's how people always describe it, but now that I think about it, it's usually more like throwing something away."

        hi "When you run away from something, you can think of it as still being there. So, I was in the hospital, and I didn't just want to run away from my problems, I wanted to never think about them again."

        "Misha eats a spoonful of her gray ice cream goo. Did she only just remember it was there now, or could it be she likes it that way?"

        hi "Anyway, my point is, you can't do that. People are too sentimental to just throw their memories out like that."

        hi "It's impossible. Shizune can't think of life in terms of anything but winning and losing; don't you think she wishes she didn't have to remember the parts where she loses?"

        hi "You can't pick and choose, though. That's like wanting to live in a bubble. The worst part is, your way of thinking is so wasteful. It's making you so pessimistic you're afraid of everything."

        stop music fadeout 4.0

        hi "Come on."

        "I grab her hand as I wave Yuuko over with the other to pay for our food. "

        show mishashort sign_confused_close
        with charachange

        mi "Where are we going now?"

        hi "Back to school before lunch is over, but I want to check out a few places before then."

        scene bg school_gate:
            right
            linear 30.0 left
        with locationskip

        play music music_comfort

        "Although I start feeling tired even after doing what could be described as on the level of a brisk jog at best, Misha and I eventually make it to the gate of the school with a little over ten minutes to spare."

        hi "I didn't even want to really come to this school, you know. I didn't have a choice. When I got to this gate, I'm sure a part of me was thinking, 'What a depressing place.'"

        hi "It doesn't look depressing at all, though. Well, I still thought I had everything figured out. I felt practically like another person."

        hi "If I could, I'd go back and tell myself to stop thinking he can write everything off at a glance, and acting like his life is already over, and he can never have fun again."

        scene bg school_gardens:
            right
            linear 30.0 left
        with locationskip

        "The school grounds are still littered with quite a few people. It's lunchtime, so it's typical."

        hi "This is where you and Shizune had me helping you put together two festivals. What a lot of hard work. I thought, 'I don't have time for this.'"

        hi "When I look back on it, though, I didn't do all that much. I also didn't have anything better to do. I'd have just spent the time alone."

        scene bg school_scienceroom:
            right
            linear 30.0 left
        with locationskip

        "I drag her to our homeroom next, which is empty except for Mutou trying to eat a sandwich before classes resume."

        hi "Every time I thought of either of you, I wished you would leave me alone. Whether it was here, or…"

        scene bg school_lobby
        with locationskip

        "Leaving Mutou to his lunch, we head for the nearby vending machine, and I grab a soda while I still have five minutes to drink it. I've spent an entire lunch period with Misha; longer than both Shizune and I have managed to find to talk to her in days."

        hi "…Following me to the cafeteria, or trying to corner me after half my classes."

        hi "I never realized we only talked like four times. It really was all in my head. I only barely realized it now."

        show mishashort hips_smile at center
        with charaenter

        mi "I remember that, Hicchan. But~, I know where all of these places are, too."

        hi "Wait, let me finish my guided tour. Since we're running out of time. By the way, do you want a soda?"

        scene bg school_staircase2
        with locationchange

        "Making our way to the stairwell, I'm glad that I don't have to pull her by the hand any more."

        hi "You get dizzy on stairs, right?"

        show mishashort perky_sad_close at twoleft
        with charaenter

        mi "Yeah~."

        hi "I guess just here is good enough, then."

        show mishashort:
            twoleft
            ypos 1.2
        with charamovefaster

        "I lean against the wall as Misha sits down on the steps, across from me."

        hi "Do you ever miss the people you went to school with in elementary school, or middle school?"

        show mishashort perky_confused_close
        with charachange

        mi "No."

        "That was fast. She didn't even have to think about it. I find myself cringing reflexively."

        hi "I had more friends in my old school, but I don't talk to them any more. It almost feels like that was another lifetime ago. Which is sad, really."

        hi "Sometimes I want to talk to them again, but I know I can't. I'm scared, and embarrassed, things like that. They're too far away for me to go see them. Then I think about calling them, but I don't know most of their numbers."

        hi "And I left on a sour note. So why would they want to see me again?"

        hi "It feels like I should just forget about it, but I still think about it anyway and regret that I didn't try harder to stay in touch somehow."

        hi "And I start to think that maybe feeling like I should forget about it is wrong. It would be an insult to all those people I had fun with and a waste of all the good times."

        hi "Like I said before, even if there are some bad times, too, it's all right if you can look back on them as happy memories."

        hi "But I didn't even think about it then. So, it was like I woke up one day and realized I had no friends. I just let myself lose all my friends, and it felt awful. I'd really hate it if you and Shizune ended up the same way. That's all."

        show mishashort perky_sad_close
        with charachange

        mi "'That's all~.'"

        hi "It makes me sad to think that you'll do the same thing and push away your friend. Especially because you're not far away from Shizune; I mean, you even live in the same dorm."

        mi "Friend, hm~…"

        show mishashort perky_confused_close
        with charachange

        mi "Aren't you my friend, too, Hicchan?"

        hi "Yeah."

        hi "You slept through all of it, but the fireworks were really nice way back, at the festival."

        hi "My first time seeing fireworks like that. And my first time really seeing the sky in a while. And, I'd never really looked at the stars before then, either."

        "I had thumbed through a book about them while I was in the hospital, though, and learned a lot."

        "Like that stars aren't just burning, they're more like a constant chain of explosions, so far away that some of the stars I'd be seeing would have been burnt out for thousands of years already."

        "It's that their light would only just then be reaching Earth. I saw a mockup comparing the size of the planet to our sun, and then that to other suns. Japan wasn't even visible on the tiny Earth in that book."

        hi "You know what I'd never realized?"

        show mishashort perky_smile_close
        with charachange

        "She looks at me expectantly."

        hi "They're amazingly shiny."

        show mishashort hips_grin_close
        with charachange

        mi "Ahahaha~."

        hi "It's true."

        show mishashort perky_confused_close
        with charachange

        mi "Why're you doing this, Hicchan?"

        hi "Doing what?"

        show mishashort cross_frown_close
        with charachange

        mi "I'm not stupid."

        hi "I don't know. A bunch of reasons. Because you're Shizune's friend? And I liked how close you were? And maybe I'm trying to tell you that we all have our low points, but giving up is stupid. Anyway, it seems worth the trouble."

        show mishashort sign_smile_close
        with charachange

        mi "That's the only reason?"

        hi "And you're my friend."

        show mishashort hips_smile_close
        with charachange

        mi "That's it?"

        hi "Can't I do something for no reason?"

        show mishashort hips_grin_close
        with charachange

        mi "Wahaha~. You can, you can~, but~, I want to know."

        hi "Well, what else do you want to hear?"

        play sound sfx_warningbell
        stop music fadeout 3.0

        "The bell rings before Misha can reply, so she ends up laughing instead."

        scene black
        with dissolve

        if _in_replay:
            return

    call timeskip

    if refuse_misha:
        label .the_summit:
            "I see less of Misha in the following days. But I don't worry, because when I do see her, she looks a bit more like her old self each time."

            "Once it's clear enough that I don't have to be afraid of it being my wishful thinking coloring my perceptions, I start to relax again."

            pause 1.0

            scene bg school_dormhisao
            with openeye

            "I wake up very early and feeling sick on Sunday. I went to sleep too early last night, too. Something's also wrong with my curtains, and they won't close completely."

            "Because of that, I can't even attempt to go back to sleep. The sun hits me in the eyes every time. I'm sure this is probably why I woke up so early this morning as well."

            play sound sfx_doorknock

            "Being this sick and tired is a perfect storm of frustration. I'm almost glad when there's a knock at the door."

            scene bg school_dormhallway
            show kenji neutral at center
            with locationchange

            play music music_kenji fadein 0.5

            "It's a familiar person holding an almost completely eaten apple in his hand. Taking one last bite, he attempts to shoot it into my trash can and misses completely, and it smashes apart on the wall two meters too high."

            "To be fair, most of the pieces afterwards do manage to fall into the trash can, but I'm pretty sure no one is so brazen that they would be aiming to do something like this on purpose."

            show kenji happy
            with charachange

            ke "Perfect shot!"

            show kenji neutral
            with charachange

            ke "Sup, roomie?"

            hi "I'm not your roomie, we don't live in the same room."

            show kenji tsun
            with charachange

            ke "It doesn't matter."

            hi "It does, you should at least know the difference between living in the same building and living in the same room."

            show kenji neutral
            with charachange

            ke "I need to use your room."

            hi "For what?"

            "I messed up, I should have said 'absolutely not.'"

            show kenji tsun
            with charachange

            ke "The Student Council keeps delivering my mail, even though I asked them to put it in my locker or something."

            ke "But they keep putting it under my door, delivering my mail without me noticing it, so today, I'm lying in wait to catch them in the act… like a detective, or a safari hunter."

            show kenji neutral
            with charachange

            ke "I need to chill in your room for today and look through the little peephole or I won't be able to catch them in the act. And maybe tomorrow, too."

            show kenji happy
            with charachange

            ke "It'll be awesome, we'll get pizza, on both days. Or should we get pizza on just one day, and something else on the other day? But what? And which day is pizza day?"

            hi "Not today. Never. You know, I'm in the Student Council. Why didn't you just ask me about this?"

            "If he had, I would have been able to find out very easily and wouldn't have to have Kenji in my room. It's win-win, except I guess this way he might be able to get a pizza out of me. I start thinking that maybe that was Kenji's intention."

            "But… No, I doubt it. There's no way he could plan something that elaborate."

            show kenji tsun
            with charachange

            ke "You know?"

            hi "When they deliver mail? Well, no. They just hand me my mail when I go to Student Council, usually. The point is, I could find out by asking them. Then I'd know and I could tell you. That's how people find things out, by asking."

            show kenji neutral
            with charachange

            ke "Not cavemen. Aw yeah, no response to that, right? Checkmate."

            hi "…Use your own peephole."

            show kenji tsun
            with charachange

            ke "What if they see me?"

            hi "They can't, that's how peepholes work. It's like a one-way glass."

            show kenji happy
            with charachange

            ke "For real? Well… No way. They'll be expecting me to be in my room, anyway. They'll sense my presence and know I'm there. They'd never expect me to actually be in the room across the hall."

            hi "I'm going to go to the student council room and go get your mail for you, right now."

            show kenji tsun
            with charachange

            ke "Then I guess I can't let you leave."

            hi "That's dumb. What if I have to use the toilet?"

            show kenji neutral
            with charachange

            ke "Your games won't work on me."

            scene bg school_dormhisao
            with locationchange

            "I sit down at my desk and start doing my homework for the weekend."

            hi "You know, you're going to have to leave eventually, so you can't stay here forever, or keep me here forever. I mean, this is my room to start with."

            show kenji neutral at tworight
            with charaenter

            ke "Yeah, I don't think I can. What time's the mail usually come?"

            hi "Now."

            show kenji tsun
            with charachange

            ke "Why are women so slow?"

            hi "Why do you care so much about the mail anyway? Are you expecting something?"

            show kenji neutral
            with charachange

            ke "I'm always expecting something. …Not today, though."

            hi "Do you want them to send something? Do you even send mail?"

            show kenji tsun
            with charachange

            ke "Nope! That's how they get you. I haven't used the mail since I was eight. Sent a letter to Lego asking them to make Dragonball Legos."

            show kenji happy
            with charachange

            ke "They said they couldn't get the rights and gave me some coupons. Totally worth it, but after that I made sure to stay off the radar."

            show kenji neutral
            with charachange

            ke "You don't use mail, do you?"

            hi "I wrote to my parents last week."

            show kenji tsun
            with charachange

            ke "But that's how they get you!"

            hi "Yes, I should have known. Maybe that's why they put that microchip in me the next day."

            show kenji neutral
            with charachange

            ke "So… the rumors were true."

            "I'd like to know what rumor mill he got that from."

            hi "I was kidding. It's a joke."

            show kenji tsun
            with charachange

            ke "Joke? Damn. You would joke on me? I guess this is how it feels… to have jokes cracked on. I never thought it'd happen to me. This is a serious issue. Man, I think you are not appreciating the depths of my dilemma."

            ke "It's a work in many acts. Complicated acts, with many players. It's really hard, okay? After I'm done I'm gonna eat a whole fish, to celebrate. Aaaah, shit. I wanted a pizza, though. I still want pizza. Can I get fish on the pizza? Do they do that now?"

            hi "You're going to be paying for it. You still haven't paid me back, and I'm not hungry right now anyway."

            show kenji neutral
            with charachange

            ke "Not in the mood for pizza? That's just not possible, son."

            show kenji tsun
            with charachange

            ke "It's got to be pizza, anyway. I'm in the pizza stage of my life. Before I was in an ice cream stage, but my girlfriend kept eating all the strawberry out of my Neapolitan. It'll probably happen to you, too."

            "It's hard to tell if he's serious half the time; I can only see his expression when he's not nose deep in my door."

            hi "I doubt that. Hey, you know that I do have a girlfriend, right? Not Iwanako, either. The Student Council president, actually."

            show kenji neutral
            with charachange

            ke "Old news."

            hi "What? Seriously?"

            show kenji happy
            with charachange

            ke "I have my sources."

            show kenji tsun
            with charachange

            ke "Anyway… Then it dawned on me that I'd gotten fat from all that ice cream. It was a rude awakening. Like sleeping on a beach and getting hit by a wave that destroys your sand castle."

            show kenji neutral
            with charachange

            ke "I started running. Had to lose the pounds. But maybe… I was really running away from myself."

            play sound sfx_doorknock
            stop music
            show kenji rage:
                tworight
                ease 0.3 twoleft
            with vpunch

            "A sudden and continuous knocking causes him to leap backwards far enough to hit the wall all the way behind him. I take the opportunity to walk over and open the door."

            play sound sfx_dooropen

            scene bg school_dormhallway
            show shizu behind_blank at center
            with locationchange

            ssh "Good morning. What's up?"

            ke "I hear if you salt the doorway they can't enter uninvited."

            play music music_comedy fadein 4.0

            scene bg school_dormhisao
            show kenji neutral at center
            with whip_left

            hi "I'm not going to put salt in my doorway."

            show kenji happy
            with charachange

            ke "But… you're considering it. Good."

            scene bg school_dormhallway
            show shizu behind_blank at center
            with whip_right

            hi "Good morning. Are you here to deliver the mail?"

            show shizu adjust_happy
            with charachange

            "Nodding, Shizune waves a couple envelopes between our faces. I take them from her, freeing up her hands for conversation."

            show shizu basic_normal2
            with charachange

            ssh "How did you know, how did you know?"

            hi "You were hiding it behind your back in a really obvious way."

            ke "Hiding what?"

            scene bg school_dormhisao
            show kenji tsun at center
            with whip_left

            hi "The mail."

            scene bg school_dormhallway
            show shizu basic_normal2 at center
            with whip_right

            pause 0.2

            show shizu adjust_smug
            with charachange

            ssh "It's okay, I wasn't trying very hard to hide it in the first place."

            hi "That's not like you. You're the type of person who'd go 'anything worth trying is worth trying hard.'"

            ke "Girls taking initiative? And what about me? I've been using that phrase for years. Where's my parade, dawg?"

            ke "I spit literary gold and you women just steal it and wear it out like a two-for-one sundress. You're all like the Picard to my Kirk. Or you could even be Janeway."

            show shizu behind_frown
            with charachange

            ssh "Not all the time. Are you making fun of me?"

            show shizu adjust_happy
            with charachange

            "Finally noticing Kenji, she gives him a wave."

            scene bg school_dormhisao
            show kenji tsun at center
            with whip_left

            hi "Hey, Kenji, the Student Council president says hi."

            show kenji neutral
            with charachange

            ke "Hi."

            scene bg school_dormhallway
            show shizu behind_blank at center
            with whip_right

            ssh "Introduce me. I have no idea what he was saying, but it looked confident."

            "Oh yes, no one is better at saying that kind of stuff confidently."

            hi "I already did. I even introduced you by title. This is Kenji, he's the guy across the hall. His room is right behind you. Anyway, do you have his mail too?"

            show shizu adjust_happy
            with charachange

            ssh "I'm only delivering your mail because it was there. I have early access! It's all about location. Consider it as a perk of being in the Student Council."

            "That doesn't sound very fair. She takes a lot of liberties with her position. At least they're small ones."

            if not side_lilly and wait_for_shizu or _in_replay:
                ssh "This is the first time I've really been able to see your room."

                "It's a blatant lie, or she'd have signed it much faster. I'm sure Shizune remembers that it's not the first time."
            else:
                ssh "I never got to enter your room before. It's interesting."

            show shizu basic_frown
            with charachange

            ssh "Why does he get to see your room and I can't? Is it a guy thing?"

            hi "It's not a secret club being a guy."

            ke "It should be. With rings. Rings with big-ass emblems. And gold!"

            show shizu adjust_smug
            with charachange

            ssh "Are you sure? Are you really sure? I always thought that there was a secret brotherhood of men."

            ke "Why's she ignoring me? Let me tell her about the guy club. Also, what's up with the hand signals? Is she trying to hex me or something?"

            scene bg school_dormhisao
            show kenji tsun at center
            with whip_left

            hi "No, stay out of this. I'll have to translate anything you say to her, and I'm not sure if I could even handle it. And she'll probably misunderstand it, and then you'll probably misunderstand the reply, and I'll have to translate your rebuttal."

            show kenji happy
            with charachange

            ke "Rebuttal? Why would I rebutt? I like my butt."

            scene bg school_dormhallway
            show shizu behind_frustrated at center
            with whip_right

            ssh "What is he saying?"

            hi "He says he has no rebuttal."

            show shizu basic_normal
            with charachange

            ssh "Rebuttal to what? I haven't even begun to challenge him yet."

            "I don't like the way she put that. So, it appears that she wants to. But about what? It doesn't matter, since it wouldn't end well."

            hi "Don't pick fights where there are none."

            show shizu adjust_frown
            with charachange

            ssh "I've never met your friends. Why can't I? It looks like he's… being passionate."

            "I suppose with the way he's flailing around it would be stupid to expect Shizune to think otherwise. Anyway, I'd better change the subject."

            "Not that it would be likely to work on her, but I'm sure that she has to have come here for a reason, other than just to drop my mail off."

            "If it was something that tiny she wouldn't have even bothered knocking."

            hi "You didn't come here just to give me my mail or chat up my friends, did you?"

            play sound sfx_snap

            "Shizune snaps her fingers in mock frustration. It's as cringe-inducingly loud as ever."

            show shizu basic_normal
            with charachange

            ssh "You're right."

            show shizu behind_smile
            with charachange

            ssh "Let's go somewhere again."

            hi "Do you have somewhere in mind already?"

            show shizu adjust_smug
            with charachange

            ssh "You're right again. Let's go to the usual place."

            "She whips out a bag of neatly wrapped containers from just outside of the doorframe. I'm guessing they're filled with food, and this time, it doesn't look store-bought. Setting it down between her feet, she continues."

            show shizu behind_smile
            with charachange

            call screen doublespeak(ke, _("Is that for me?"), ssh, _("This was the real surprise. See?"))

            show shizu adjust_smug
            with charachange

            ssh "I have to have something over everyone at the very end."

            "I agree, in the way people normally do when someone makes a statement in front of them that tells more than they meant to tell."

            show kenji tsun:
                center xpos 0.0
                ease 1.0 twoleft
            show bg at bgright
            show shizu behind_smile at tworight
            with charamovechangefaster

            ke "Well, fine, if you're both going to ignore me, I'm out of here. So cruel. You'll regret this!"

            stop music fadeout 2.0

            hide kenji
            with charaexit

            scene ev shizu_roof at shizu_roof_in
            with shorttimeskip

            play ambient sfx_rooftop fadein 1.0
            play music music_soothing fadein 0.5

            "Not long afterwards, we find ourselves on the school roof."

            "Is it normally deserted at this time, on a nice day like this, on the weekend? No, of course not. I can only think that it's because of Shizune. Not that clearing out a roof would require anything more than posting a sign on the door."

            "The empty plastic containers Shizune had packed our meal in lie next to me. It was another quiet meal, since holding chopsticks prevents us from saying much to each other."

            "While it's not blowing hard enough to be a problem, the wind is a little strong today. It blows the plastic bag loose from under the empty containers, so it whips around for a bit before rolling over my legs and getting caught on the tip of Shizune's shoe."

            scene ev shizu_roof_towardsangry at shizu_roof_in
            with charachangeev

            "Immediately, she grabs it and starts signing, not looking happy that I'm laughing at her, even though she's trying not to let out a laugh herself. With the bag in the way, however, she has to eventually sit on it to continue."

            ssh "Very funny."

            scene ev shizu_roof_towardsnormal at shizu_roof_in
            with charachangeev

            ssh "How was it?"

            scene ev shizu_roof2_towardsnormal at shizu_roof_in
            with charachangeev

            his "The food? It tasted familiar."

            scene ev shizu_roof2_towardsangry at shizu_roof_in
            with charachangeev

            ssh "That means it was bad."

            scene ev shizu_roof_towardsangry at shizu_roof_in
            with charachangeev

            his "No, no. I remember eating this exact meal before, when you made it."

            "Not exactly the same. The fried shrimp was new."

            ssh "It's the only thing I know how to make, but I should have improved."

            his "How many times have you made it before?"

            scene ev shizu_roof_towardsnormal at shizu_roof_in
            with charachangeev

            ssh "This is the second time."

            his "Making this particular meal?"

            scene ev shizu_roof at shizu_roof_in
            with charachangeev

            ssh "Cooking."

            scene ev shizu_roof_smile at shizu_roof_in
            with charachangeev

            ssh "Next time, it's your turn to try it."

            scene ev shizu_roof_towardsangry at shizu_roof_in
            with charachangeev

            "The way she keeps tugging on the corner of the bag is bothering me. I think I know why she's doing it."

            scene ev shizu_roof2_towardsangry at shizu_roof_in
            with charachangeev

            his "Is it really bugging you that much?"

            scene ev shizu_roof2_towardsnormal at shizu_roof_in
            with charachangeev

            ssh "I want to pack them up properly."

            scene ev shizu_roof_towardsnormal at shizu_roof_in
            with charachangeev

            his "It's okay, I'll get them."

            "As I'm picking them up, I realize she must have brought a lot of food to be able to fill all these containers. I didn't even eat much. Shizune must have some metabolism in order to pack all that away."

            stop music fadeout 1.0
            play sound sfx_impact

            scene black
            with vpunch

            "Even though I've only been up for a second, it's long enough to stupidly trip over my own feet. Barely managing to break my fall, I end up landing on my elbows and knees right next to Shizune's lap."

            scene bg school_roof
            with locationchange

            play sound sfx_heartslow
            show heartattack alpha
            with Dissolve (0.1)

            hide heartattack
            with Dissolve (0.7)

            "As I pull myself back up, hand gingerly held on my chest, all I can think about is how my knees hurt and how this fall could have killed me. I feel nauseous."

            "Shizune gives a helpful push on my shoulder to help me upright, though I notice her eyeing me oddly. Unfortunately, even a light shove is enough to take me by surprise."

            show shizu basic_normal2_close:
                center
                ypos 1.1
            with charaenter

            ssh "Are you okay?"

            "I nod, but we don't return to sitting beside each other. Naturally, being alone with Shizune is going to involve a lot of silence, but I only start to notice it now. The typical sign of awkwardness. Again, she's the one to break the ice."

            show shizu behind_smile_close
            with charachange

            ssh "I was expecting you to try something dirty."

            hi "…"

            show shizu behind_sad_close
            with charachange

            "And now the mood is back to awkward."

            his "How's Misha?"

            show shizu basic_normal_close
            with charachange

            play music music_twinkle fadein 6.0

            ssh "Misha seems happier now, back to her old self. I thought this would be a good way to celebrate, and to thank you for helping her."

            "Her hand stumbles for a bit on the last word."

            his "You think too much like a businesswoman."

            show shizu behind_blank_close
            with charachange

            ssh "I can't help it, it's how I've been taught to do things."

            show shizu adjust_happy_close
            with charachange

            ssh "It makes me happy that you're asking about Misha. It would be more accurate to say 'back to her real self.' She would only be back to her old self to you."

            show shizu basic_normal_close
            with charachange

            ssh "The Misha you know is completely different from the one I think of, when I think of the first time we met. Even though I think she looks better cheerful and smiling, that isn't how she typically is."

            show shizu behind_blank_close
            with charachange

            ssh "I wonder if it's true for you, too?"

            "I don't answer."

            his "Well, if Misha is happy, then it doesn't matter, if it worked out in the end. Your plan worked."

            his "You knew her just as well as you said. You knew everything she would say. If your idea was just that I'd speak for you, though, doesn't that just make me your puppet? I didn't do anything, then."

            show shizu cross_angry_close
            with charachange

            ssh "Not true. It was your idea first."

            show shizu basic_frown_close
            with charachange

            ssh "I was wrong. I have a way of seeing things that is very flawed, now that I've thought about it. I'm sure you know. Sometimes, I treat everything like a competition between myself and everyone else. Even when it doesn't make sense to."

            "Sometimes?"

            show shizu behind_blank_close
            with charachange

            ssh "I know very well how easy it is to ignore someone if they can only communicate with you through sign. I should have asked for help. But I was so sure I could do it on my own. It was actually a brave thing you did. Even if you won't take credit for it."

            show shizu basic_normal_close
            with charachange

            ssh "Aside from that, you've really become kind of admirable lately."

            "It's strange having her compliment me while her facial expression hasn't changed in the slightest."

            show shizu adjust_frown_close
            with charachange

            ssh "But!"

            show shizu basic_happy_close
            with charachange

            ssh "'People don't change so easily.' According to you. Am I right?"

            "She winks, clearly enjoying herself very much."

            his "Does Misha tell you everything?"

            show shizu behind_blank_close
            with charachange

            ssh "Almost everything."

            his "I guess you're going to tell me that I'm wrong about that, aren't you?"

            show shizu basic_normal2_close
            with charachange

            ssh "Yes and no."

            show shizu adjust_frown_close
            with charachange

            ssh "I'm the one who told Misha that before anyone else. But she took it too far, and changed the meaning. It's not easy, but she acts like that makes it impossible."

            show shizu basic_normal_close
            with charachange

            ssh "It's possible, if you go little by little. I'm considering trying to be less competitive."

            his "I thought you enjoyed that, though."

            show shizu behind_smile_close
            with charachange

            ssh "Maybe just a little. That's why I specifically used 'less.'"

            "She leans against the fence. I have things I want to say to her, but it doesn't seem like the right time for it, somehow. It's a feeling I have. I can tell she isn't done just yet."

            show shizu basic_normal2_close
            with charachange

            ssh "A lot of people think I try too hard."

            show shizu adjust_happy_close
            with charachange

            ssh "Well… I've always thought that I try to try just enough."

            "The sound the fence makes as she pushes against it, and the delicate clink of her sleeve buttons scraping against the links, are oddly soothing. So is the breeze gently picking up behind me. I can hear people below us."

            show shizu basic_normal_close
            with charachange

            "Shizune's eyes dart below us as well, and I wonder if she still thinks about what she might be missing out on. The attention-grabbing way she tends to snap her fingers proves she has an understanding of how other people perceive sound."

            show shizu:
                ease 1.0 center alpha 0.0

            pause 1.0

            hide shizu

            "It must be odd, being able to understand that much, but unable to experience it yourself. She starts walking slowly around the perimeter of the roof, still scraping her buttons against the fence. It isn't rhythmic at all, though not for a lack of trying."

            show shizu basic_normal_close:
                twoleft
                ease 1.0 center
            with Dissolve(1.0)

            show shizu at center

            "I sort of zone out in thought while she does, and am rudely snapped out of it when she circles around completely and taps me on the shoulder."

            show shizu behind_blank_close
            with charachange

            ssh "Do you remember what we were talking about?"

            his "When? Now? Of course, it just happened."

            show shizu basic_angry_close
            with charachange

            ssh "It's been almost ten minutes."

            show shizu adjust_frown_close
            with charachange

            ssh "When I first saw you, you seemed like you were very attached to the idea of feeling sorry for yourself."

            "That stings, even if it is true."

            show shizu behind_smile_close
            with charachange

            ssh "Sorry, sorry."

            show shizu basic_normal_close
            with charachange

            ssh "It made me want to cheer you up at first sight. I was scared it would be for nothing, though. I couldn't help thinking it would be hard to change your mind."

            show shizu behind_smile_close
            with charachange

            ssh "But you did. I thought that was very surprising, and also that you might be kind of easily influenced. Still, I was surprised. It made me reconsider a lot of things. Like… that maybe everything was worth it in the end."

            his "Everything?"

            show shizu adjust_happy_close
            with charachange

            stop music fadeout 4.0

            ssh "—That's why I like you."

            his "I see."

            "It's nice to finally know."

            stop ambient fadeout 2.0

            scene black
            with dissolve

            if _in_replay:
                return

        call timeskip

        label .succession:
            scene bg school_council_ss at right
            show mishashort hips_smile_close_ss at closeleft
            show shizu behind_blank_close_ss at closeright
            with locationchange

            play music music_ease

            hi "…And remember, you have to take this job seriously. Too many people think you can just slack off, and that it isn't important. That is a dangerous way of thinking."

            show mishashort cross_frown_close_ss
            with charachange

            mi "Definitely~. You can't take it too seriously~! If you aren't always thinking big, thinking positive, and if you show any signs of weakness, people will start to think you're incompetent, you know~."

            show mishashort sign_confused_close_ss
            with charachange

            mi "And soon you won't be able to do anything because your power is going to be delegated off to others piece by piece, and you'll be left with nothing. That's what happened last time~."

            show mishashort hips_grin_close_ss
            with charachange

            mi "So~! Remember~, it may seem like an easy job, but a lot of carnage can happen in this room. Ahaha~. And~, out of it. Dealing with school staff, too! Even trying to get a budget report from a class rep can be a fight to the death~, sometimes."

            hi "…Yeah. It's kill or be killed. There are no friends in the pits and you take no prisoners. …Are you sure about this? Is this right?"

            show shizu basic_angry_close_ss
            with charachange

            ssh "You don't seem excited enough, I have to make sure it's getting through properly. Once more, with feeling!"

            show aoi_keiko:
                yalign 1.0 xanchor 0.5 xpos 0.0 alpha 0.0

            play sound sfx_flash

            show mishashort:
                xpos 1.1 alpha 0.0
            show shizu:
                xpos 1.6 alpha 0.0
            show bg at left
            show aoi_keiko:
                center alpha 1.0
            with charamovefastest

            "Shizune twists her hands like a maestro for emphasis, visibly intimidating the two girls standing at attention in front of us. To think this all started because one of them asked if she wasn't taking her job too seriously."

            ssh "Do you understand!?"

            hi "Do you understand? Pretend I'm shouting it."

            "Aoi" "Okay, okay! Aaargh! This Student Council is so weird."

            "Keiko" "Yes, sir."

            hi "'Sir?' Who are you guys talking to, anyway?"

            play sound sfx_flash

            show mishashort hips_smile_close_ss:
                closeleft
                alpha 1.0
            show shizu adjust_frown_close_ss:
                closeright
                alpha 1.0
            show aoi_keiko:
                yalign 1.0 xanchor 0.5 xpos 0.0 alpha 0.0
            show bg at right
            with charamovefastest

            ssh "It's not weird! You have to think of it as a job. If you want, think of it like they are paying you with the right to use this great office."

            play sound sfx_flash

            show mishashort:
                xpos 1.1 alpha 0.0
            show shizu:
                xpos 1.6 alpha 0.0
            show aoi_keiko:
                center alpha 1.0
            show bg at left
            with charamovefastest

            hi "You want another lecture?"

            "Aoi" "Noooo…"

            ssh "You can go now."

            stop music fadeout 5.0

            scene bg school_council_ss
            show mishashort perky_smile_ss:
                twoleft
                ypos 1.1
            with shorttimeskip

            "Just like that, the hour-long student council orientation is over. Personally, I thought it was about fifty minutes too long, and also found it funny that it incorporated a tour of a school that we have all been going to for a while, but I guess it didn't hurt."

            "I expect Shizune to fall back into her chair, since she has been on edge all day, but she doesn't. She continues pacing the room restlessly."

            play music music_shizune fadein 1.0

            show shizu adjust_frown_ss:
                center xpos 1.0
                ease 1.0 tworight
            with Dissolve(1.0)

            show shizu at tworight

            ssh "They still have a long way to go! Right now, they're a joke."

            show mishashort sign_confused_ss
            with charachange

            mi "Eh?"

            hi "What?"

            show shizu behind_frustrated_ss
            with charachange

            ssh "They think they can be the new Student Council? They're so unfocused. You can really see the lack of experience. This was our best year yet; I don't think they have what it takes to be our follow-up act."

            show shizu basic_frown_ss
            with charachange

            ssh "And I know there are more of them than those two girls. Where are they? They're like the heavily-marketed but mediocre, big-budget, critically-panned sequel to the acclaimed, low-budget sleeper hit."

            show mishashort perky_confused_ss
            show shizu behind_blank_ss:
                ypos 1.1
            with charamovechangefaster

            "Eventually, she does stop and sit down."

            hi "Are you going to miss it?"

            show shizu basic_normal_ss
            with charachange

            ssh "Obviously."

            show mishashort perky_sad_ss
            with charachange

            mi "Hm~… I'd be happier if I didn't have to leave, too."

            show mishashort hips_smile_ss
            with charachange

            mi "I like being in the Student Council, even if it can be tiring, too."

            hi "Yeah, it's definitely tiring."

            show mishashort hips_grin_ss
            with charachange

            mi "Only because Shicchan is always trying to do more than she has to~."

            show shizu adjust_frown_ss
            with charachange

            ssh "You're forgetting that if I did the bare minimum, we wouldn't do anything all year except hand out flyers, collect surveys, and plan the next student council election so the next Student Council could sit around for another year of doing nothing."

            show shizu behind_frown_ss
            with charachange

            ssh "Asking me to let that happen? Don't be ridiculous. In a Student Council like that there wouldn't even be any power to play around with."

            show shizu adjust_happy_ss
            with charachange

            ssh "I'm just happy that even though I clearly need to ride them harder, those two aren't bad. Not there yet, but the new Student Council should be in good hands."

            hi "How can you tell?"

            show shizu behind_smile_ss
            with charachange

            ssh "After the festival, they asked me if we could also organize a Halloween event, like a haunted house or something along those lines. They had a bunch of other ideas, as well."

            show shizu adjust_smug_ss
            with charachange

            ssh "Of course my response was 'no.' I had Misha tell them to do it themselves, if they wanted it so badly. They were angry, for some reason."

            show mishashort cross_laugh_ss
            with charachange

            mi "Ahaha~."

            hi "Of course they'd be angry if you said that."

            "And Misha delivering the message wouldn't help."

            show mishashort cross_smile_ss
            show shizu behind_blank_ss
            with charachange

            ssh "I was angry too."

            show shizu basic_frown_ss
            with charachange

            ssh "All of a sudden, they want so much. If they wanted a haunted house, or a traditional-style café, or a trip to the beach, or whatever other cliché thing, why didn't they try to organize it before? It was like they were taking advantage of me."

            show shizu behind_frown_ss
            with charachange

            ssh "I worked hard to organize those festivals, and in return they came to me with 'That was nice, but can you do this now? How about doing this? It's what I really want.'"

            show mishashort sign_smile_ss
            with charachange

            mi "Shicchan was wrong~, though."

            show shizu basic_happy_ss
            with charachange

            ssh "Right. They wanted to join the Student Council so they could make it happen. I made them feel jealous and riled them up. That can be a kind of motivation too."

            show shizu adjust_happy_ss
            with charachange

            ssh "The desire to do something great spreads, even if it's to show me up. They decided to take me up on the challenge nonetheless."

            show shizu behind_blank_ss
            with charachange

            ssh "I'm impressed. Well, for now. I would have to see how it plays out a little longer in order to know for sure."

            play sound sfx_snap

            show shizu adjust_happy_ss
            show mishashort perky_confused_ss:
                ease 0.1 ypos 1.05
                ease 0.1 ypos 1.1
            with vpunch

            "She snaps her fingers suddenly, which sends Misha almost bolting out of her seat. Interesting, I guess it is impossible to get used to."

            show shizu basic_happy_ss
            with charachange

            ssh "That's right! We were going to have a party to celebrate passing the reins to the new Student Council, weren't we? Why not have that now? Or at least plan it now, and have it tomorrow."

            hi "But they're not even in charge yet. In fact, that's the first thing you told them: 'You're not in charge yet.' It seems premature."

            show shizu adjust_frown_ss
            with charachange

            shi "…"

            show shizu behind_blank_ss
            with charachange

            ssh "Misha, what do you think?"

            show mishashort hips_smile_ss
            with charachange

            mi "Hmmm~, I agree, it's too early. Plus~, I don't think I could go anyway. Sorry~! In fact, I was going to leave right now."

            ssh "Why not?"

            show mishashort hips_grin_ss
            with charachange

            mi "No~ comment~!"

            show shizu adjust_frown_ss
            with charachange

            ssh "Come on, tell me."

            show mishashort perky_confused_ss
            with charachange

            mi "Well… okay~!"

            "Way to not crack under pressure, Misha."

            show mishashort sign_confused_ss
            with charachange

            mi "I thought about it, and~… Even if I didn't want to go, I would say yes~! Usually~. It's the kind of person I am. I really should stop doing that, and this is a good place to start, I think."

            show mishashort perky_sad_ss
            with charachange

            mi "If it's a celebration to say goodbye, I don't want it. It would be too sad~. I want to do something else instead. And after all, Hicchan, you and Shicchan will still be here tomorrow. It doesn't seem right."

            show mishashort hips_grin_ss
            with charachange

            mi "Besides, I have other school things I have to do today~! I can't drop them just like that."

            show shizu adjust_frown_ss
            with charachange

            ssh "We can postpone it."

            show mishashort hips_frown_ss
            with charachange

            mi "No. No early goodbyes~!"

            "She looks very firm as she says this."

            hi "Aren't you going to go now, though?"

            show mishashort hips_grin_ss
            with charachange

            mi "Hm~? Oh, that's right~! Wahaha~!"

            show mishashort perky_smile_ss at twoleft
            with Dissolvemove(0.7)

            show mishashort sign_smile_ss
            with charachangealways

            mi "Okay, besides now, no too-early goodbyes, okay?"

            show shizu behind_blank_ss
            with charachange

            ssh "I get it."

            show mishashort hips_grin_ss
            with charachange

            mi "Okay, later~!"

            stop music fadeout 4.0

            hide mishashort
            with charaexit

            show bg school_council_ss:
                center
                parallel:
                    "bg school_council_ni" with Dissolve(5.0)
                parallel:
                    ease 5.0 bgleft
            show shizu behind_blank_ss:
                parallel:
                    "shizu behind_blank" with Dissolve(5.0)
                parallel:
                    ease 5.0 xpos 0.5

            "With that, it's just Shizune and me left alone in the student council room."

            play music music_dreamy fadein 4.0

            pause 2.0

            "Sunset slowly changes to night as we sit in silence, both searching for something to say."

            show bg school_council_ni at bgleft
            show shizu adjust_frown:
                center
                ypos 1.1
            with Dissolvemove(0.5)

            ssh "Would it really be that bad?"

            his "Yeah. I didn't think about it like that, but Misha's right. Parties set a mood, and it would be a sad one. A sad party doesn't sound like a whole lot of fun."

            show shizu basic_angry
            with charachange

            ssh "Why would it be sad?"

            "Is it a trick question? I'm sure of it. Shizune's eyes pierce into mine, waiting for my answer with a detached, analytical stare that I haven't seen in a while, but feels familiar anyway."

            "I consider my answer carefully, but also what it means for her to ask me."

            "It could be that Shizune finds it depressing as well. Or it could be that she doesn't understand why anyone would find it depressing. Both are equally plausible."

            his "I had a thought that when you graduate, that's it. It's going to be the end of the Student Council. I was wondering if you had the same idea."

            show shizu behind_frown
            with charachange

            ssh "Don't be stupid. I look forward to it. I won't be a student any more, so the expectations are going to be completely different. People's expectations of me, and my expectations about everything else. It seems exciting!"

            show shizu adjust_frown
            with charachange

            ssh "As for the Student Council, it should be in good enough hands. I don't have anything to be sad about."

            his "I don't think you're being honest. You looked upset about having to give the Student Council up not even a few weeks ago. It wasn't about leaving it to a bunch of newbies either, it was having to stop doing student council work at all."

            show shizu behind_smile
            with charachange

            "Unexpectedly, Shizune smiles."

            his "So, you're not disagreeing."

            his "Then it doesn't make sense. Why would you want to have a party about it?"

            show shizu basic_normal
            with charachange

            ssh "I'm trying to get over it. Besides… Goodbye celebrations are very important. People say the first step is the most crucial, but following it through and finishing cleanly are just as important, right?"

            his "I guess that is true."

            show shizu adjust_smug
            with charachange

            ssh "Anyway, I don't consider it goodbye. But it's still an event. You still have to go through the proper motions."

            show shizu behind_blank
            with charachange

            stop music fadeout 4.0

            ssh "Aren't you going to?"

            his "Aren't I going to what?"

            show shizu basic_normal
            with charachange

            ssh "Kiss me, of course."

            his "Is that 'the proper motions?'"

            show shizu behind_blank
            with charachange

            ssh "It would be normal, wouldn't it? The natural thing to do."

            "It's time to act decisively. If I don't, I'm sure my heart will explode."

            show shizu adjust_blush_close
            with charachange

            "I kiss her immediately, so quickly that I don't even have time to enjoy it. Even though she was prepared for it, Shizune blushes a deep red. I feel a similar heat rising in my neck and cheeks."

            play music music_one fadein 4.0

            scene evh shizu_undressing_clothed_stare
            with whiteout

            "I move in for another kiss, but as I do so, she moves backwards at the same time and impishly jumps onto the cabinet behind her. Alone, in the total silence of the room, we just look at each other for a while."

            scene evh shizu_undressing_clothed_kiss
            with charachangeev

            "This time, I kiss her more deeply. Her lips are light and dry, and open a tiny bit. I'm only able to appreciate the sensation for a moment before Shizune starts kissing me back forcefully."

            "Her bangs brush against my closed eyelids as I let myself sink deeper into the kiss. I can feel the shape of her body through her clothes, which only makes me hold Shizune tighter."

            scene evh shizu_undressing_clothed_blush
            with charachangeev

            "It takes some effort for the both of us to draw back from each other. We're both blushing, both from the kiss and thoughts of what's to come, and I'm far from the only one breathing a little heavier."

            "As Shizune begins to take off my tie, I start undoing her blouse. It takes a while to figure it out. I'd never really thought about how our school's blouses work before."

            "Shizune's blouse is a little tight on her, and her arms get stuck for a moment because of it. I find myself peeling it off of her, although with the way she's trying to wriggle out of it at the same time, it isn't easy. The sight is a little comical."

            play sound sfx_rustling

            scene evh shizu_undressing_unclothed_closed
            with charachangeev

            "Once Shizune's arms are free, she slides out of her shirt, her skirt falling around her knees with it after she unhitches it and works it off her legs. The only thing covering her now are her bra and panties."

            "Her figure is curvaceous and taut, and the healthy color of her skin contrasts with the black of her underwear. It's a wonderful sight, especially against the background of the moonlight through the window."

            scene evh shizu_undressing_unclothed_blush
            with charachangeev

            "She looks at my chest and works the buttons of my shirt one by one. The process is greatly slowed by my hands moving up and down her thighs. It's a little amusing to play with her like this."

            scene evh shizu_undressing_unclothed_kiss
            with charachangeev

            "Eventually, finally, my shirt falls to the ground. Shizune surprises me by quickly pulling me in for a deep kiss without warning, but I quickly return the gesture."

            scene evh shizu_undressing_unclothed_talk
            with charachangeev

            ssh "Why are you bolder today than on the roof?"

            ssh "Or in your room?"

            "I try to think of a good answer, but it isn't easy. How would I be able to respond to that even if I could? There's no way to, unless I were to say that bureaucracy really puts me in the mood."

            "My shirt having been disposed of, Shizune moves on to my belt, and I decide to help her undo it instead of answering her question. I don't think it would do much good to at this point."

            scene bg school_council_ni
            with locationchange

            "It's not hard to get off, and falls to the ground with a metallic clunk. I move in for another kiss and begin to slide my hand up her side, but she suddenly lurches forwards, making me stumble backward."

            "The stiff edge of the table behind me was the furthest thing from my mind, until I feel it stabbing into my lower back. I hadn't even noticed it was there. It makes me grab Shizune a little tighter as we fall back onto the surface of the table."

            scene evh shizu_pushdown
            with charachangeev

            "I hold back a sigh as Shizune victoriously holds herself above me. She's won again."

            "I'm distracted until Shizune's bra falls on me, seemingly like it dropped out of the sky. I end up laughing, despite how hard I try not to, and it's contagious enough that Shizune starts to as well."

            "Freed from her bra, her breasts are larger than I'd thought, even though they were noticeably large through her shirt already. She picks up her bra with her fingers and flicks it off as my hands move over her body."

            "Straddling me with her knees on the table, Shizune slips her underwear off, with my hands moving from her hips unconsciously to help her. I catch a glimpse of my watch. It's only been a few minutes, but it felt like so much longer."

            "She eases herself downwards, closer and closer until our bare chests are touching, her breasts feeling strange against the scar over my heart."

            scene evh shizu_straddle_open
            with whiteout

            pause 7.0

            "When Shizune sits up, I feel myself slipping inside, slowly enveloped by her below as her breasts lift away from my torso. An attack from two fronts, I think dryly considering the situation. How like her."

            scene evh shizu_straddle_tease
            with charachangeev

            ssh "I should just stop now, and leave you stewing in your lust."

            "She says, as she starts grinding herself against me, causing me to blink at the sudden pleasure. Very funny, Shizune. I soon lose track of my thoughts."

            scene evh shizu_straddle_closed
            with charachangeev

            shi "…sss."

            "Shizune bites her lip to muffle her voice from coming out. An unwanted voice. This is the most I've ever heard of it, and she blushes once she realizes she let it slip out."

            "To cover it up, Shizune drives herself against me harder, causing me to jolt against her, driving my erection deeper into her."

            "I thrust my hips towards her at the sudden sensation of movement, and Shizune fights against me, trying to pin me back down when I manage to pull my arms out from under me."

            scene evh shizu_straddle_smile
            with charachangeev

            "In that moment, her hips thrust back with even greater force in response."

            "The sound of Shizune's soft, restrained moans, and the sight of her bountiful breasts moving up and down each time her hips buckle against mine, grow more arousing with time in the stillness of the student council room."

            shi "Mmphh…"

            shi "…nn…"

            "I almost can't take it any more. The pleasurable sensations welling up between my legs, multiplied by the pressure of Shizune's weight on top of me, make it hard for me to think. My hips start bucking by themselves."

            "Shizune's hands push mine down onto the table. Every motion of hers is a push of some kind."

            "The table under us rattles under our combined weight. I doubt it would collapse, but the noise is really something."

            scene evh shizu_straddle_come
            with charachangeev

            "Not that Shizune notices. Her pace only grows faster, until it feels as though she might shove me across the table with how forceful she is being. Without warning, her movements come to a final crescendo."

            scene bg school_council_ni
            with locationchange
            with vpunch

            "Suddenly, she stops, almost falling onto me with enough speed that if she didn't catch herself, it would probably have knocked us unconscious. The worst situation possible, if someone happened to walk in while we were knocked out."

            "I'm surprised, but not enough to forget that we're both naked and the sudden, painful interruption that just happened."

            "Why did this have to happen? Was it intentional, to leave me stewing in my own lust? Shizune lets out her breath sheepishly, realizing it at the same time as I do."

            show shizu behind_blank_nak at center
            with charaenter

            ssh "Sorry, I tripped, or slipped, or something like that."

            his "I had a thought, is the door unlocked?"

            hide shizu
            with charaexit

            "She quickly gets off the table and bolts over to check, and locks it, unlocks it, and locks it again, pulling on the knob just to make sure. When she's finally sure, she makes an out-of-place motion with her hands."

            show shizu behind_smile_nak at center
            with charaenter

            ssh "Safe!"

            his "I'm glad you can take things so lightly."

            show shizu behind_frown_nak
            with charachange

            ssh "I didn't do it on purpose. Why don't you take the lead, then?"

            show shizu behind_smilelow_nak
            with charachange

            ssh "Come on."

            hide shizu
            with charaexit

            "I grab Shizune by the shoulders and try to put her onto the table instead. Her brow scrunches in displeasure as the edge of the table pokes her in the back, just as it did to me. She opts to help herself up onto it."

            scene evh shizu_table_smile
            with dissolve

            "This is also the first time I've seen Shizune lying down unclothed. The contours of her collarbone and breasts are beautiful, and my eyes follow them down to her shapely hips. A delicate hourglass figure."

            "I run my hands along the curve of her body, from her shoulders on down."

            "I slowly insert myself into Shizune up to the hilt. An intense warmth and tightness immediately surround me, and I start pistoning into her to pick up where we left off before."

            "Her body feels so hot against my skin, each time our hips meet with each thrust, and where we're holding each other. I feel like I'll be scalded by her body heat."

            "On top of that, I feel more sensitive now than before, and find myself pushing into Shizune harder to make up for it."

            scene evh shizu_table_normal
            with charachangeev

            "My hand glides around the curve of her thigh and I carefully tease her with my hand as well, almost losing my balance when she reacts strongly, snapping upwards and back into my groin and nearly pushing us both to the floor."

            "Moving my hands up, I grab her prominent breasts and fondle them as I've always wanted to. They feel even larger than they appear, and overflow my hands, soft and perfectly shaped."

            "She squirms under me as I flick my fingers over her nipples, and twists her arms around mine instead, gripping my fingers and drawing me closer. It feels like I'm wrestling her; the lock is inescapable."

            "From the first time our hands met, I guess we were connected."

            "Whether it's through her pulling me from one student council event to another, or holding hands as lovers, I think it's been the same, the confidence that comes across in the way she grasps my hand."

            "Her hands writhe across the surface of the table, and grabbing onto it, she hooks her legs around my back, pressing us closer together, connecting us even more closely and entrapping me inside her."

            scene evh shizu_table_comeopen
            with charachange

            "Her inner walls are so hot and tight, and with her pushing up against me, the friction only increases, sending me over the top."

            scene evh shizu_table_comeclosed
            with whiteout

            stop music fadeout 4.0

            "All too soon, the feeling ends. All I can do afterwards is stay inside of her with my hands holding the table, both for lack of energy and because her legs are still locking me in. For Shizune's part, she smiles almost dreamily."

            "The sight makes me smile as well. Her legs slowly fall, allowing me to extract myself."

            scene bg school_council_ni
            with locationchange

            "Exhausted, I lean back against a desk and try to regain my breath before putting my clothes back on."

            "I notice a dull, hot throbbing in my chest as I button my shirt back up. It puts a bad aftertaste on everything that just happened."

            show shizu behind_smile_nak at center
            with charaenter

            ssh "It was a lucky break that Misha couldn't be here, wasn't it?"

            his "You're in an unusually joking mood today."

            his "I wonder what she had to do."

            show shizu behind_blank_nak
            with charachange

            "Shizune traces the air lazily with a finger and points to the door."

            ssh "Go see for yourself."

            his "Why don't you just tell me?"

            show shizu behind_smile_nak
            with charachange

            ssh "It's more interesting if you see for yourself. Seeing is believing."

            his "Sure. Clever. Maybe I will. What about you, are you going to stay here all day? It's getting late."

            show shizu behind_blank_nak
            with charachange

            ssh "It feels like my last day as Student Council president, so maybe I'll sleep here tonight. It could be the last chance I have to sleep at my desk, like after a long day trying to meet a deadline."

            his "That's weird."

            his "I'll sleep in my bed."

            ssh "Sleeping sitting up is a skill. A very useful one."

            his "Right."

            scene bg school_lobby_ni
            with locationchange

            "For a moment after I leave the room, I actually do consider seeing what Misha is up to, just because Shizune made it sound so secretive, as if she were building a time machine or something. But in the end I decide not to."

            if _in_replay:
                return

        label .sneaking_mission:
            scene bg school_courtyard_ni
            with locationskip

            "The night air is pleasant at this time of year. It's refreshing and a little humid, but not so chilly as to make it uncomfortable to stay outside for a while. It's late enough for the courtyard to be all but deserted, too."

            "After Shizune and I said our farewells to each other, I'd set out to return to my dormitory room. I didn't even make it all the way there, though, before getting distracted."

            "It doesn't seem like a bad idea to go see what Misha is up to. I have nothing better to do. No homework. I'm out of anything worth reading. On top of that, I simply want to know."

            scene bg school_lobby_ni
            with locationchange

            "This isn't my first time being in the main building after hours, but usually, it's as I'm leaving the place with Shizune and Misha after a long day at the Student Council. Not entering it alone."

            "The atmosphere is quiet, a word I would not normally use to describe these halls. It's a little creepy. A light starts flickering up ahead. This seems like a horror movie moment waiting to happen."

            play sound sfx_rustling
            with vpunch

            "Feeling a hand on my shoulder, I stiffen reflexively."

            "It's not Misha, or else there would be hands clamped over my eyes and a sing-song 'guess who' accompanying them. So, who is it? I hope it's not Kenji, or at least that it's someone I know, or this will take a turn for the weird."

            show shizu behind_blank_close_ni:
                tworight
                ease 1.0 center
            with Dissolve(1.0)

            show shizu at center

            play music music_happiness fadein 4.0

            "Whoever it is quickly slips in front of me. It's Shizune."

            hi "What are you doing here?"

            "I'm so relieved that I forget to sign it."

            show shizu adjust_frown_close_ni
            with charachange

            "Shizune puts a finger up to her lips. I guess even though she can't hear, she has some idea of what loudness is, and can tell from my expression that I was being loud. And apparently, being loud isn't a good thing right now."

            "But then, why is Misha her interpreter?"

            his "Oh, very funny. Why are you here?"

            show shizu basic_normal_close_ni
            with charachange

            ssh "I was waiting for you to come see. I knew you would show up. It took you a while, though."

            his "You've been waiting here?"

            show shizu behind_blank_close_ni
            with charachange

            ssh "Yes, but that isn't important. We have to be stealthy, if we don't want Misha to detect us. Tell me if I'm not being stealthy enough, okay?"

            show shizu basic_normal_close_ni
            with charachange

            "With that, Shizune starts slowly tiptoeing through the middle of the hall. I pat her on the shoulder to get her attention."

            his "That's not stealthy."

            his "Why do we have to be stealthy?"

            show shizu behind_frustrated_close_ni
            with charachange

            "She refuses to answer, probably because signing and walking stealthily at the same time doesn't look easy."

            scene bg school_hallway3_ni
            with locationskip

            "Before I know it, we're in front of our homeroom."

            stop music fadeout 0.5
            play sound sfx_snap
            with vpunch

            "Suddenly, a sound like the crack of a whip pierces the air, followed by a familiar expression of frustration."

            "I'm sure a sound like that isn't good for my heart. Not to mention, everything sounds about a million times louder with how silent it is. It's coming from inside the room, and I sidle up to Shizune to get a look inside."

            scene ev misha_nightclass:
                center
                xpos 0.4
            show ovl misha_nightclass_aperture at left
            with silentwhiteout

            play music music_comedy fadein 0.5

            mu "Can you stop throwing your pencil, please? How do you even throw a pencil that loudly?"

            ssh "He looks very flustered."

            "What an understatement. I sympathize with Mutou. I was able to hear Misha's pen break the sound barrier even through a wall and a thick classroom door. It probably blew out his eardrums and left an imprint on the wall."

            show ev misha_nightclass:
                ease 1.0 xpos 0.23 xanchor 0.0
            show ovl misha_nightclass_aperture:
                ease 1.0 right

            mi "I'm not throwing it~, when I get nervous, I like to spin it around, but~, then I forget I'm holding onto it, and—"

            mu "It doesn't matter, either way, there shouldn't be pencils flying around. I get enough of that during regular school hours, I don't need it after hours."

            mi "R-right~! Sorry."

            mu "Whatever, just stop throwing, or releasing, or dropping things, please. Teachers have work, too."

            scene bg school_hallway3_ni
            show shizu behind_blank_close_ni at center
            with locationchange

            "I notice Shizune watching the same scene I am. Mutou is yelling at the top of his lungs, and Misha is being Misha."

            "I can hear them reasonably well through the door. But Shizune obviously can't hear anything at all. So, I wonder what watching this is like for her."

            "She must know, since she understands well enough to want me to see it too, but I have to wonder if she ever feels like she's missing out on something, having to work that much harder to understand what she's observing."

            show shizu basic_normal_close_ni
            with charachange

            ssh "It looks like she is taking supplementary lessons. Is she?"

            his "Yeah."

            "I answer, despite knowing the question is completely rhetorical."

            show shizu behind_smile_close_ni
            with charachange

            ssh "Misha told me she really wants to be a sign language teacher in the future. If she can get a recommendation, she can study overseas for it. That is why she is working so hard. Her grades were always kind of on the low side."

            his "Now I feel guilty. I haven't even thought about what I'm going to do yet."

            show shizu adjust_smug_close_ni
            with charachange

            ssh "Neither have I!"

            "The cheerful way that she signs it is very unlike her, and is very obviously false."

            show shizu basic_normal2_close_ni
            with charachange

            ssh "Let's get out of here, we don't want to be seen. It would be a problem if we were caught standing out here like idiots."

            his "Where? The student council room?"

            show shizu adjust_happy_close_ni
            with charachange

            stop music fadeout 3.0

            show shizu:
                ease 1.0 xpos 0.7 alpha 0.0

            pause 1.0

            hide shizu

            "Shaking her head, she slips into the classroom across the hall instead."

            scene bg school_room34_ni
            with locationchange

            his "Great hiding place."

            show shizu behind_blank_ni at center
            with charaenter

            ssh "You're unusually sarcastic, lately. With the door closed it's a good one. Anyway, wasn't it interesting?"

            his "Yes, but I'm not really surprised."

            play sound sfx_doorclose

            show shizu adjust_smug_ni:
                center
                ypos 1.1
            with charamovechangefaster

            "I close the door behind us, prompting Shizune to laugh soundlessly as she slides into a chair. For a second, it depresses me. I want to hear her real laugh."

            show shizu behind_smile_ni
            with charachange

            play music music_innocence fadein 10.0

            ssh "I was. I've been looking down on Misha. I didn't think she had a goal at all. But it turns out that I was wrong, I made a careless assumption. I thought Misha was as aimless as I was. I was stupid. I lost."

            show shizu basic_normal_close_ni
            with charachange

            "Shizune pauses to crack her knuckles, then folds her hands over each other, and leans forward in her chair. In the abnormal quiet of the building, I can hear Mutou yelling at Misha again even across a hallway and through two doors."

            "Shizune's eyes are locked on mine, unblinking behind the gleaming lenses of her glasses, observing my reaction to her words."

            "This is a test. Her opinion of people is rarely formed from how they respond to questions; it's how they respond to statements that counts."

            "In hindsight, it makes sense. Shizune's inability to speak, as well as just her personality in general, means that anything she 'says' is a big commitment on her part. Everything."

            "For that reason, I sometimes doubt she says anything without a hidden agenda behind it."

            "That sounds remarkably paranoid. Even Kenji would think so. Unfortunately, I'm so caught up in thinking about it that I forget to give her an answer. She takes it as there not being one. There was an invisible time limit to this test, shorter than usual."

            show shizu adjust_smug_close_ni
            with charachange

            ssh "Just as I thought."

            his "What do you mean?"

            show shizu behind_blank_close_ni
            with charachange

            ssh "You don't agree?"

            his "Not really, it's not that. I don't get it."

            show shizu basic_normal2_close_ni
            with charachange

            ssh "I want to force my will on people."

            "How refreshingly honest."

            show shizu behind_frown_close_ni
            with charachange

            ssh "Don't give me a weird look like that. It's not like that was always my intention."

            show shizu basic_normal_close_ni
            with charachange

            ssh "At first, I was just bored. I wanted to see someone's passion for something. Then I could try and beat them. I wanted to test their ability or their convictions."

            show shizu adjust_frown_close_ni
            with charachange

            ssh "But it was impossible, no one has any passion for anything in this school. They just want to keep to themselves."

            show shizu behind_frustrated_close_ni
            with charachange

            ssh "I can't believe it. It's too boring that way. I thought that there was no way these drab people could be for real. It goes beyond not wanting to make waves."

            show shizu adjust_angry_close_ni
            with charachange

            ssh "They had to have some interests. They had to be hiding something. I wanted to expose it, and reveal it, and drag it out."

            show shizu behind_blank_close_ni
            with charachange

            ssh "One of the most successful ways to get people to open up to you, and cheer them up, is to open up with a story about yourself. And then you ease them into telling you about themselves."

            show shizu adjust_happy_close_ni
            with charachange

            ssh "It's like give and take, but with an element of manipulation, which makes it interesting."

            show shizu behind_blank_close_ni
            with charachange

            ssh "I can't do that. If I attempt to have Misha talk about me, for me, it makes me seem arrogant. The message has to go through a messenger. I'm standing next to Misha, telling her to tell someone about me."

            show shizu adjust_frown_close_ni
            with charachange

            ssh "You don't have to be able to read sign language to see that. If I were forced to sit through that, I would think I was arrogant, too."

            show shizu basic_angry_close_ni
            with charachange

            ssh "I was frustrated; I couldn't figure out a way to have a conversation with anyone but Misha. No one would open up to me."

            show shizu behind_frown_close_ni
            with charachange

            ssh "I came to the conclusion that I can't make people confide in me, or believe in me. I can only hope to create things, and show them to people, and hope they make them happy. Or I could be more forceful and hope it would eventually stick to someone."

            "I guess that would be me. Feels vaguely depressing."

            show shizu basic_normal_close_ni
            with charachange

            ssh "Somewhere along the line, I think I started to ignore Misha, or see her as less of a person, or something like that. I took her for granted, I think would be the best way to put it. It was like she was just an extension of myself."

            show shizu behind_sad_close_ni
            with charachange

            ssh "I forgot that the whole time, Misha was there, opening up to me, and giving a hundred percent every day."

            show shizu basic_angry_close_ni at center
            with Dissolvemove(0.7)

            ssh "I missed what I was looking for, because it was in plain sight. How stupid of me. I really did become arrogant. That's why I've lost. I'm more shortsighted than I was back then. I went in reverse."

            "She's pacing back and forth now, almost brooding, yet still filled with so much energy that she can't stand to stop moving."

            "If you got her to hold two wires I'm sure Shizune could power a light bulb. It's odd that I could have such a lighthearted thought while she's being so serious."

            show shizu adjust_frown_close_ni
            with charachange

            ssh "And in spite of that, Misha tells me that I'm her inspiration. Isn't that ridiculous? I'm not the kind of person who can inspire others."

            show shizu behind_blank_close_ni
            with charachange

            ssh "Even if a person who inspires you is flawed, it can be acceptable. I've thought about this. There is even acceptable hypocrisy."

            show shizu basic_normal2_close_ni
            with charachange

            ssh "For instance… If your hero was an athlete, but unsportsmanlike, they could still be respected for their athletic ability, even if they had shortcomings as a person."

            play sound sfx_snap
            show shizu adjust_angry_close_ni
            with charachange

            ssh "However,"

            "She snaps her fingers briskly. It sounds like a thunderclap in the empty room, and Shizune takes a few seconds to stretch her fingers. Come to think of it, this is the most she has ever signed."

            show shizu cross_angry_close_ni
            with charachange

            ssh "If someone like me has no goals, it would be totally unacceptable. It'd be the worst kind of hypocrisy. And hypocrites don't deserve responsibility over anything, they can't even manage themselves."

            "How incredibly pessimistic. It makes me angry to think about it."

            "I would hate myself just a few months ago. This must be how I looked to others."

            "And, funny enough, it was Shizune and Misha who convinced me to stop. Without them I'm sure things would be much different, and not for the better. "

            "Lately, I feel as though we pass around our miseries as much as we're supported by each other, but I think it just comes with the territory of having friends and being close to someone."

            his "You're the leader anyway."

            show shizu behind_frown_close_ni
            with charachange

            ssh "That is only because no one else wants to be."

            his "But that means you still are, since people are putting their trust in you anyway. In fact, doesn't that make it more important?"

            his "Either way, you are the leader, you are the inspirational figure or whatever you want to call it. You're responsible for what you tame."

            his "I read that in a book somewhere."

            show shizu basic_normal_close_ni
            with charachange

            ssh "That's clever."

            "Shizune only seems to show what she's feeling on her face when she wants to, but I don't think she's being sarcastic."

            show shizu adjust_frown_close_ni
            with charachange

            ssh "I don't want to 'tame' anyone, though."

            his "Being the leader and being looked up to, then. Same thing."

            show shizu behind_frustrated_close_ni
            with charachange

            ssh "I never wanted to be the leader, it just ends up that way."

            his "I don't believe that, all you do is try to grab more and more responsibility."

            show shizu adjust_frown_close_ni
            with charachange

            ssh "Wait, wait. I wasn't going to tell you that I don't enjoy it. I don't care about being the leader, but I don't mind. I don't care about being the best, but I don't mind. You're right, though, about me wanting responsibility."

            show shizu basic_happy_close_ni
            with charachange

            ssh "Of course I want more responsibility. Having responsibility makes me feel alive. That's why I joined the Student Council: If there is no pressure, I just can't stand it."

            show shizu behind_blank_close_ni
            with charachange

            ssh "Even so, now I'm the leader. I always thought being the leader meant you give orders, but it really is more."

            show shizu adjust_frown_close_ni
            with charachange

            ssh "It's about having a goal. If I don't have a goal, then it's pointless. People would only be following me for my own enjoyment. It would be selfish."

            "It's a strangely moral viewpoint for a person who seems to love one-upping others so much."

            show shizu basic_normal2_close_ni
            with charachange

            "Resting her chin on her tented fingers, Shizune looks disarmingly childish as she thinks hard about her problem. The expression on her face is a little comical, because it's too obvious, and therefore, very unlike her."

            his "It comes with the job. I think you'd have to be a leader. You wouldn't be satisfied with anything else, you would just get bored."

            show shizu basic_frown_close_ni
            with charachange

            "Shizune doesn't reply, but from her annoyed expression, I think I've guessed correctly."

            his "I've been thinking that I need a little direction, too."

            show shizu adjust_happy_close_ni
            with charachange

            ssh "Were you told that it's important to contribute to society?"

            "What an unusual response. It's so out of nowhere that I don't know how to respond. And it also bothers me, though I don't know why. Possibly because it doesn't seem like something that would come from her."

            "So I start to think that it isn't Shizune's thought at all. I wonder who told her that. Well, it was probably her dad. But there is a chance that she came up with it on her own. If so, would it be because she can't hear?"

            his "Why do you say that?"

            show shizu behind_blank_close_ni
            with charachange

            ssh "Just because."

            his "I don't believe it."

            his "I guess that's right, though."

            show shizu basic_normal_close_ni
            with charachange

            ssh "I see."

            show shizu adjust_frown_close_ni
            with charachange

            ssh "I don't know if it's the same for me. I hate it."

            "I think everyone wants a purpose. Looking back, it makes sense that Shizune doesn't have one. All that energy would otherwise have been directed at something."

            "Since she had nothing to channel it towards, Shizune lashed out in all directions. Reminds me of a downed power line flailing in a storm: furious and incandescent, but aimless and dangerous. Just like Shizune."

            "I want to say that this is why she feels the need to turn everything into a competition, but… that's probably just how she is. Having a goal to put that energy towards is just the next level."

            show shizu behind_blank_close_ni
            with charachange

            ssh "How about this? I could go into business. My family is well connected, so it shouldn't be too hard. …That comes off sounding a little unethical and nepotistic, doesn't it?"

            his "A little."

            show shizu adjust_frown_close_ni
            with charachange

            ssh "I won't coast, though. I'll work hard, until I'm at the very apex."

            ssh "When I have as much money as possible, so much that it'll be like I won't know what to do with it, I'll move on to the next step. After sitting on it for a while, of course, like a fairy tale dragon."

            his "You want to be…?"

            show shizu basic_happy_close_ni
            with charachange

            ssh "A philanthropist!"

            hi "…"

            show shizu adjust_smug_close_ni
            with charachange

            ssh "Tsk tsk. What were you thinking? That I want to be a miser?"

            show shizu behind_blank_close_ni
            with charachange

            ssh "Well, it's true, it is a part of the plan. Don't sell me short and stop there, though."

            stop music fadeout 8.0

            "Shizune still looks uneasy. Of course; even if she did seem to resolve her problem quickly, no one can get over their anxieties that fast. No one can solve their problems that easily."

            "The important thing is, it looks as though she has her heart set on trying. It's still hard to tell whether that drive of hers comes from a good or bad place."

            "But she has something to hold on to now. I can genuinely believe that she does. I'm happy for her. And at the same time, I feel a little cold. I'm the one who's behind. Now, I'm the only one without a goal."

            scene black
            with dissolve

            if _in_replay:
                return

        call timeskip

        label .infinity:
            nvl clear

            $ renpy.music.set_volume(0.5, 0.0, channel="music")
            play music music_daily fadein 0.5

            scene bg school_dormhisao_bw
            with dissolve

            nvl show dissolve

            n "{vspace=270}There haven't been any further disruptions since that week."

            nvl clear

            n "{vspace=30}Of course, that's what I thought the week before that. And Shizune and Misha's sudden, newfound clarity had left me feeling a little lost and envious. I thought there was no way I could rest easy at the time."

            n "But fortunately, nothing came of my worries. Then before I knew it, there was enough to deal with in school that I even managed to put them off my mind. And still, everything was fine."

            n "I was wrong. I'd seen Shizune and Misha's carefully hidden vulnerabilities; but they were still strong."

            n "Now, we're going to be graduating soon. I've grown so comfortable here that it kind of crept up on me. When it did, I felt sad and didn't want to think about it. So, I didn't. Not until recently."

            n "About a week ago, I started making a list of people I thought I should say goodbye to before graduation. The first rule I laid out for myself was that I would try not to write them down in any kind of special order, like least important to most important."

            n "Somehow, it ended up like that anyway, even though it also ended up being a shorter list than I expected it to be. Kenji is somewhere in the middle."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl hide dissolve
            nvl clear

            scene bg school_dormhisao
            show kenji neutral at center
            with locationchange

            ke "They said I would have to graduate eventually. Well, I showed them. I've lived here rent free for more than long enough. If you take into account the rising cost of land, I think you could say I've won in the end."

            show kenji happy
            with charachange

            ke "No, you know what? I did win. History will acknowledge me as the victor."

            hi "The victor of what?"

            ke "I managed to stay out of sight, and slip through the cracks. I beat the system."

            hi "If you put it that way, it sounds like you just ran away from the system."

            ke "Sometimes, running is the greatest form of victory; like in the Olympics."

            "I'm too tired to argue with him. Who's he kidding? Everyone knows the shot put is the best Olympic event, in any case."

            hi "So, what you're basically saying is, you won't miss it?"

            show kenji neutral
            with charachange

            ke "Miss what?"

            hi "School, dummy."

            show kenji tsun
            with charachange

            ke "No. I told you, this place is too filled with feminists. It's beyond saving. But at least I'll be able to get out before it reaches critical mass. I'll only come back, years later, when they build a statue to honor me."

            hi "Do they do the ten year later reunion thing here?"

            show kenji neutral
            with charachange

            ke "How would I know that? Probably. Anyway, I have to start packing now. Take care of yourself, man."

            hi "You should have packed a week ago, like I did."

            "Not that I had much to pack."

            show kenji tsun
            with charachange

            ke "That's not how it goes. You're supposed to do everything at the last minute. Men are better at doing everything at the last minute, the last minute can have more productivity than like, the entire week before it. It's how we keep shit fair."

            show kenji neutral
            with charachange

            ke "Pffft, you'll never understand our manly ways."

            hi "You take care of yourself, too."

            show kenji happy
            with charachange

            show kenji:
                ease 1.0 right alpha 0.0

            pause 1.0

            play sound sfx_doorslam

            hide kenji
            with vpunch

            "With a salute, he shoots backwards through the door, slamming it shut behind him hard enough that the entire dorm probably heard it. I've noticed that a lot of people slam doors here. Maybe it's a local thing."

            "'Take care of myself.' It's the first time I've heard him say it. Usually he ends our conversations with something like, 'seeya.' 'I'll pay you back later, man.' Well, he was a little annoying sometimes, but I'll miss him. I cross him off my list mentally."

            "The list is very short now, and I once again discard the notion of going through it in any kind of order. Like I said, I never had that intention."

            scene bg school_dormhallway
            with locationchange

            "So, I go out to look for Shizune and Misha. I can only think of one place they could be. The student council room, of course."

            play ambient sfx_crowd_indoors fadein 2.0

            scene bg school_lobby
            show crowd
            with locationskip

            "Turning the corner, I almost bump into a small group of students. For a second, a bitter feeling flashes through me, since for all I know, that could have been fatal."

            "It's the new Student Council. There aren't a lot of them, but a lot more than three. Which is good, since it means there's enough of them that they can each have their own title."

            "It would have been cool if I could have had a little desk plaque with my name and title on it. I don't think they do that now, or ever did, unfortunately."

            "The new Student Council surrounds me while I'm thinking. If anyone were looking at this from afar, it would be a pretty sinister sight."

            "Maybe they have come to finally get back on me for calling them 'the new Student Council' all those times. I was just translating for Shizune, but I guess I should have been less lazy and more tactful. I regret nothing."

            "I find myself being thanked for 'everything I've done.'"

            "I'm being thanked. This should make me happy, considering how often I would think to myself that being in the Student Council was a completely thankless job. It does make me happy, but I can't enjoy it fully."

            $ renpy.music.set_volume(0.5, 1.0, channel="music")
            $ renpy.music.set_volume(0.5, 1.0, channel="ambient")

            nvl clear
            nvl show dissolve

            n "{vspace=60}I wonder how things would have turned out if our Student Council had grown as large as the one that's set to replace us."

            n "Even though they've only got two or three other members, it's enough that they have set roles. Not like us, where Shizune seemed to be the president, but that was it."

            n "The new council thanking me gives me a strange feeling. It's like coming back home and seeing that a tree you nurtured years before has grown. But I feel like I didn't nurture that tree enough. I wonder what more I could have done."

            n "It would likely make Shizune furious that I would feel distant from what I did in the Student Council this way, or that I'd imply I didn't do enough, but it's true. I was only following her."

            n "{vspace=30}So, in a way, I also feel like I'm viewing that same tree from far away. As if I'm seeing it from the window of a train as it passes by."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")
            $ renpy.music.set_volume(1.0, 1.0, channel="ambient")
            stop music fadeout 4.0

            nvl hide dissolve
            nvl clear

            "I indulged in these thoughts for too long. When I snap out of it, I realize that I'm still standing there, surrounded by the new Student Council. I do the only thing I can do, and apologize for zoning out. Then, I thank them back."

            stop ambient fadeout 0.5

            scene bg school_council
            with locationchange

            play music music_normal fadein 3.0

            "When they walk away, I enter the student council room, which looks a lot messier, but seems to have gained a computer."

            "It makes sense; I recall hearing one of the clipboard girls talking about her plans to use a computer to make all the boring data entry Shizune does more tolerable."

            "I can't remember which one said it, though. Aoi seems to be the more ambitious one, but then again, Keiko appears more serious. Well, it doesn't matter now."

            "I'm not alone in the room, but instead of finding Shizune here like I expected, it's just Misha. She's sitting on Shizune's desk, like Shizune herself often does, swinging her legs back and forth."

            show mishashort hips_grin:
                center ypos 1.2
                ease 0.5 center
            with Dissolve(0.5)

            show mishashort at center

            "When our eyes meet, she hops off and inexplicably poses like a superhero."

            mi "Hi, Hicchan~! I'm surprised to see you here~!"

            hi "What are you doing?"

            show mishashort cross_smile
            with charachange

            mi "You first~."

            hi "I was looking for Shizune."

            show mishashort cross_grin
            with charachange

            mi "Me, too~! I thought she would be here, but I got Hicchan instead~!"

            hi "Gee, thanks."

            show mishashort sign_smile
            with charachange

            mi "Wahaha! Well~, this is good. Really, really~. I wanted to talk to you, anyway~."

            hi "About what?"

            "I take the time to glance around the room a little more. I see a hot plate. They are really living high."

            show mishashort perky_sad
            with charachange

            mi "I wanted to say sorry~, of course~, for all the trouble I made for you and Shicchan."

            hi "Don't call it 'trouble.'"

            show mishashort sign_confused
            with charachange

            mi "Right~, right~."

            hi "Don't apologize to Shizune."

            show mishashort hips_smile
            with charachange

            mi "Ahaha~. Right~, right~. But that isn't why I'm here, Hicchan. I wouldn't apologize to Shicchan. Since you're here, I want to ask you a question."

            show mishashort perky_confused
            with charachange

            mi "Hicchan, what do you think it would take for Shicchan to be happy?"

            hi "World domination, obviously."

            show mishashort cross_laugh
            with charachange

            mi "Wahaha~!"

            show mishashort hips_smile
            with charachange

            mi "Even though you're joking, Hicchan~… No, even if she could, it wouldn't make Shicchan happy. Only for a little while."

            show mishashort sign_smile
            with charachange

            mi "Hicchan, have you ever heard of artists who tear up their paintings as soon as they finish them? Such people really exist in the world, you know~!"

            show mishashort perky_smile
            with charachange

            mi "I remembered it all of a sudden. It's just like Shicchan, now that I think about it. Whenever Shicchan sets up a challenge for herself and completes it, she acts like her skills have no meaning any more."

            show mishashort perky_confused
            with charachange

            mi "I wonder~, is it because she can't create anything permanent?"

            show mishashort perky_sad
            with charachange

            mi "It's just like those artists, and how they want to create a piece of art to leave behind~, a really great one~, but can't do it. It's really obvious when I look back at it~, but~, I didn't see it before. Now, I'm scared. I wonder if Shicchan will ever be happy."

            hi "No, I don't think so. Not about her ever being happy. I think you're wrong. Shizune is actually happy more often than I'd thought."

            hi "I think it's actually kind of amazing. Usually, people don't think about that kind of stuff until they're middle aged or dying. Then they think 'I want to leave something behind' or 'I want to be remembered.'"

            "Like me."

            "Only I skipped ahead a little. My life was short, and seemed even shorter after my heart attack."

            "I didn't think about what I was leaving behind, because I very quickly thought there was almost nothing I was leaving behind. So all that was left was for me to stew in my own bitterness."

            hi "Shizune already wants to leave her mark somewhere. But she wants to do it by helping people. That's why celebrations are so important to her. She even wants to be a philanthropist."

            hi "I think it's the best way to live, living on by what you give to others. Even if it's for a selfish reason, that's okay, too."

            hi "Shizune is already happy, because if something goes well, there will always be someone else to see it and remember it. That's what makes her happy."

            "Misha sighs, arms stiff at her sides, hands tapping the air softly."

            show mishashort sign_sad
            with charachange

            mi "Before, I still thought… hm~… I might be able to make Shizune happy; and I was in a good place to do it before. Since I was her interpreter, I could always be with her. Maybe…"

            show mishashort perky_confused
            with charachange

            mi "And~, I thought I would do it by becoming like… Shicchan's shadow."

            show mishashort perky_sad
            with charachange

            mi "I kept trying even when she rejected me. It felt like I was stuck and I couldn't do anything but watch Shicchan's back getting smaller while she kept going. I was scared, even though I should have just accepted it."

            mi "It's hard. Maybe I could have at least understood Shicchan~."

            show mishashort cross_smile
            with charachange

            mi "But it looks like I was completely wrong after all~… I didn't even know that, or think about it… Shicchan would call it a complete loss."

            show mishashort cross_frown
            with charachange

            mi "Okay~, I'm done. That's it, Hicchan~. But~! Since you're the one who knows Shicchan best of all, you can't make her cry. Or I'll be angry~!"

            show mishashort hips_smile
            with charachange

            mi "I'm going to go overseas after this. I even have letters of recommendation, or I don't think I would be able to normally~! Maybe I'll study and become a sign language teacher over there? Who knows~!"

            show mishashort hips_grin
            with charachange

            mi "That means~! You have to look after Shicchan, okay?"

            stop music fadeout 8.0

            "Misha's smile is as honest as ever, but she's obviously changed. The look in her eyes is that of a much more attentive girl. It seems to be true that hardship builds wisdom. It reminds me of the look in Shizune's eyes."

            "I wonder what Shizune might have been through to have become who she is. I can take a guess. Or maybe she was always like that. I want to see her even more, and suggest to Misha that we should look for her together."

            "Of course, it's just a pretext to spend more time with a friend. It's strange how it hasn't been long since we last hung out together, the three of us, in the span of a routine student council day. Yet, it seems like it was long ago."

            "Thinking about the future can put that kind of lens over the past."

            "Speaking of lenses…"

            scene bg school_courtyard at bgleft
            show yuuko neutral_up at center
            with locationskip

            play music music_ease fadein 8.0

            "Outside, Yuuko is standing around, fiddling with a tiny, modern-looking camera in her hands. It would be unnoticeable if it weren't metallic enough to reflect the sunlight. Misha calls out to her. I thought we were supposed to be looking for Shizune."

            show yuuko at tworight
            show bg at center
            with charamove

            show mishashort hips_grin at twoleft
            with charaenter

            mi "Hi~ hi~!"

            show mishashort cross_smile
            with charachange

            mi "What are you doing~?"

            show yuuko closedhappy_down
            with charachange

            yu "I'm just taking photos of everyone."

            show mishashort hips_grin
            with charachange

            mi "That's obvious~!"

            "Awkward. Misha, I'll never forget how you taught me that someone can hold so many secrets, and still have a massive lack of tact."

            hi "Where's my photo?"

            show yuuko worried_up
            with charachange

            yu "Y-you want a copy? I… don't know. Well… Only if you promise to keep it a secret, or else everyone will want one too."

            show mishashort cross_smile
            with charachange

            mi "That happened to me in elementary school, only it was with candy~!"

            show yuuko smile_up
            with charachange

            yu "Okay… I'll take a photo of you now, then…"

            hi "Ah, wait, I'm not ready. I was just kidding."

            show mishashort sign_smile
            with charachange

            mi "Hicchan, make a peace sign~!"

            hi "I'm not going to do that."

            play sound sfx_camera
            with cameraflash

            "The camera flash goes off, blinding me."

            show mishashort perky_confused
            show yuuko worried_down
            with charachange

            "Yuuko shields herself behind it, letting out a moan of frustration. You're not supposed to turn the flash on outdoors."

            show yuuko:
                ease 1.0 right alpha 0.0

            pause 1.0

            show yuuko:
                right
                alpha 0.0

            "She starts apologizing unnecessarily, and then quietly slips away."

            hi "Ah, wait."

            show yuuko worried_up:
                ease 1.0 tworight alpha 1.0

            pause 1.0

            show yuuko at tworight

            yu "Yes?"

            show mishashort sign_smile
            with charachange

            mi "Did you see Shicchan around here~?"

            show yuuko neutral_up
            with charachange

            yu "Yes… In front of the gate."

            hi "Thanks."

            "I can barely get it out before I have to start following behind Misha."

            play ambient sfx_crowd_outdoors fadein 3.0

            scene bg school_gate
            show crowd
            show shizu behind_blank at center
            with locationskip

            "Fortunately, not for very long. The gate is barely a minute's walk from here, even though even that can be tiring for me sometimes. We see Shizune with the Student Council; they're probably thanking her too."

            $ renpy.music.set_volume(0.3, 1.0, channel="ambient")

            show shizu adjust_frown
            with charachange

            hide crowd
            with charaexit

            "As soon as she sees us, she shoos them away. Which is very easy, since I doubt any of them can understand sign language or use it, so they're not too sad about leaving."

            "Which in turn makes me wonder why they would thank her without someone who can, but it's the thought that counts."

            show mishashort hips_grin behind shizu:
                twoleft
                ease 0.4 xpos 0.36
            show shizu adjust_blush
            with Dissolvemove(0.4)

            show bg at bgright
            show mishashort perky_smile at twoleft
            show shizu behind_smile at tworight
            with charamovechangefaster

            "Misha immediately hugs Shizune, and then leans against the gate, next to her. I, on the other hand, decide to hang back a little, and let them talk. After all, Misha wanted to talk to Shizune this whole time. I can wait."

            show shizu:
                xpos 0.4 alpha 0.0
            show mishashort:
                xpos 0.0 alpha 0.0
            show bg at right
            with charamovechangefaster

            "I even turn away, so I don't 'eavesdrop' on their conversation."

            "I end up losing track of the time."

            "When I look at my watch, it's already been ten minutes. I wonder if they're done, and turn around to find them behind me."

            show mishashort:
                twoleft alpha 1.0
            show shizu behind_blank:
                tworight alpha 1.0
            show bg at bgright
            with charamovechangefaster

            ssh "What are you thinking about?"

            hi "Boring philosophical things that I don't want to talk about. Don't worry, I'm not thinking about it too hard."

            show shizu adjust_smug
            with charachange

            ssh "Good. Getting philosophical at a time like this would be the worst thing you could do."

            hi "Yeah. I just want to stand here for a bit. It's relaxing."

            show mishashort hips_grin
            with charachange

            mi "Wahaha~! It was~ a busy week."

            hi "Not really, not for me."

            $ renpy.music.set_volume(0.5, 1.0, channel="music")
            $ renpy.music.set_volume(0.1, 1.0, channel="ambient")

            nvl clear
            nvl show dissolve

            n "{vspace=120}I know that they must have been busy. But I think I know what I want to do now, and when it hit me, I didn't feel particularly fired up, or anxious."

            n "It is the opposite. I feel at peace for the first time in a long time, and I want to savor that feeling a little more."

            n "{vspace=30}I think that I want to teach here."

            n "{vspace=30}As soon as I thought this, a long, winding road appeared in my mind. An uncertain road, that leads back here."

            nvl clear

            n "{vspace=120}I wonder if I'll be able to meet someone in the future like me. Someone filled with bitterness."

            n "I want to talk to that person, since I can't talk to myself. I want to tell them that life is too short; something that couldn't be told to me, only shown. I want to do it without pity."

            n "If I had been pitied, I'm sure that I'd have only died a little more. When I think about that first week, I still think about how well it went. So well that it could only be called the result of kindness. I feel like I want to show others the same kindness."

            n "{vspace=30}And I also want to keep chasing Shizune."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")
            $ renpy.music.set_volume(0.3, 1.0, channel="ambient")

            nvl hide dissolve
            nvl clear

            show mishashort perky_smile
            with charachange

            mi "What did the new Student Council want, Shicchan~?"

            "It's hard to daydream when you have to deal with Misha's voice."

            hi "I didn't know that they had someone who knew sign language."

            show shizu behind_smile
            with charachange

            ssh "They don't. I think it was most likely just a goodbye, so I appreciate it, even though I couldn't tell them."

            show shizu basic_normal
            with charachange

            ssh "How did you know I was here?"

            hi "Is it supposed to be a secret? Anyway, we just asked Yuuko. Did she take a photo of you, too?"

            show shizu behind_blank
            with charachange

            ssh "Yes, without asking me first. Since Yuuko doing anything spur-of-the-moment is rare, though, I'll let it go."

            play sound sfx_snap
            show shizu basic_sparkle
            with charachange

            "She snaps her fingers, more because I think she likes it, than out of realization of an idea."

            show shizu behind_smile
            with charachange

            ssh "We should take a photo of the three of us."

            show shizu adjust_happy
            with charachange

            ssh "We haven't taken a student council photo yet. Now's the perfect chance."

            show shizu basic_normal
            with charachange

            ssh "But, if I have to look at this picture a year from now, I don't want us staring back at me."

            mi "Hm~? What does that mean, Shicchan?"

            show shizu adjust_frown
            with charachange

            ssh "Pictures are supposed to capture the moment, isn't that right? Without a doubt. They're not portraits. Just standing around would be so stiff. It wouldn't even capture how I feel."

            show shizu behind_smile
            with charachange

            ssh "I feel like we'll meet again. So, this isn't an occasion to take such a serious photo. It should be a 'see you later' type of photo; not a big deal. It should be something more… festive."

            hi "Oh boy."

            show shizu basic_happy
            with charachange

            ssh "Like this. Follow me."

            show shizu adjust_smug
            with charachangealways

            show shizu behind_smile
            with charachangealways

            "Shizune poses like a musketeer, so quickly that I'm sure even she knows it's silly."

            show mishashort cross_laugh
            with charachange

            mi "Ahahaha~!"

            hi "Do we really have to do… such a cheesy pose?"

            show shizu adjust_happy
            with charachange

            ssh "I can think of no better pose. Misha, go find Yuuko!"

            show mishashort sign_smile
            with charachange

            mi "I don't like this pose either, but I think it's kind of nice~."

            hi "That doesn't even make sense."

            show mishashort:
                ease 1.0 xpos 0.0 alpha 0.0

            pause 1.0

            "She's already gone, and returns dragging Yuuko behind her."

            show yuuko neutral_up at left
            show mishashort hips_grin:
                center
                alpha 1.0
            show bg at left
            show shizu behind_smile_close:
                tworight
                xpos 0.83
            with charamovechangefaster

            "The flash is off. A red LED blinks three times above it after Yuuko's finger presses the button. Shizune glances at both of us to make sure we have the timing down. Synchronize watches. We jump."

            play sound sfx_camera
            $ renpy.music.set_volume(0.0, 0.5, channel="ambient")

            scene ev shizu_goodend
            with cameraflashlong

            ssh "I bet that turned out excellently."

            ssh "Okay, …"

            mi "Now, let's get one with Yuuko, too~!"

            yu "N-no, please…"

            hi "That's not necessary."

            "I want a copy of this photo, too."

            scene ev shizu_goodend_pan
            with charachangeev

            "I'll likely die younger than the average person. My life could unexpectedly burn out at any time. I don't have any time to waste, then. I want to live as much as possible. I also want to see other people smile from what I've made and done."

            "Living vicariously through the happiness of others doesn't seem so bad. Feeling joy through another person's happiness doesn't seem like such a bad thing. It's the easiest way I can think of to draw out my own life, and give it distinction."

            "Maybe this is the meaning that Shizune has found for herself, although it's just my theory. People find themselves alone often in their lives, and without direction."

            "However, people can take refuge in moments of happiness. They can dot a person's life like stops on a train map. Or waypoints of memory on a long trail."

            "These individual moments, on reflection, can give a person's life fulfillment. Every friend, and festival, and joyful meeting, and joyful parting."

            "I want to be able to ask Shizune one day if I'm right. I want to spend the time I have with her. Finally, I want to make Shizune smile for herself."

            $ renpy.music.set_volume(0.3, 1.0, channel="ambient")

            scene bg school_gate at left
            show mishashort perky_smile at twoleft
            show shizu behind_smile_close at tworight
            with locationchange

            hi "I love you."

            "I pause, wondering if she'll look at me, confused, and ask why I'd say it out of the blue. She doesn't."

            hi "Do they do that reunion thing here?"

            show shizu adjust_happy_close
            with charachange

            ssh "Of course they do."

            show mishashort sign_smile
            with charachange

            mi "A Student Council member should know that~!"

            show shizu behind_smile_close
            with charachange

            ssh "Sooner than that, though, okay?"

            show shizu adjust_happy_close
            with charachange

            ssh "Both of you."

            show mishashort hips_grin
            with charachange

            mi "Right~!"

            hi "Yeah."

            show shizu basic_happy_close
            with charachange

            ssh "Yuuko! You do the pose, too!"

            show shizu adjust_happy_close
            with charachange

            ssh "Afterwards, we can go for tea."

            "Shizune laughs, as if she doesn't have a care in the world, Misha's laughter joining with hers as easily as if it were her own. We'll meet again."

            stop ambient fadeout 2.0
            stop music fadeout 2.0

            if _in_replay:
                return
    else:
        label .present_tense:
            play music music_pearly

            scene bg school_scienceroom
            with locationchange

            "The next day, Misha is back in class, although still looking pretty sullen. Not that I was expecting her to magically feel better; that would be asking the impossible considering what happened."

            "This time it's Shizune who's out. At first, it almost makes me laugh that suddenly whenever one is in class the other isn't. But thinking about it, there's nothing funny at all about it. In fact, I find it hard to concentrate on my work because of it."

            "It could be that she's just sick. Or she could simply be skipping class. It could also be something more serious, and I'm tempted to ask Misha if she knows, but I end up doing nothing."

            "I don't regret stepping in yesterday, scared that Misha would do something rash."

            play sound sfx_normalbell

            "But now I feel like I should give her some space. Eventually, the bell rings, and Misha gets up for lunch along with everyone else. I decide to eat lunch in an empty classroom today… just not this one."

            scene bg school_hallway3
            with locationchange

            "Unfortunately, a lot of other students seem to have the same idea, so there aren't a whole lot of empty classrooms to go around. Finally, as I'm about to give up on the idea, I find a dark one at the end of the hall."

            scene bg school_miyagi
            show lilly back_surprise:
                center
                ypos 1.15
            with locationchange

            "On turning the lights on, however, I find out that this one isn't empty either. Lilly's head turns in my direction, which freaks me out before I realize she probably heard me flipping the light switch."

            show lilly basic_listen
            with charachange

            li "Hello."

            hi "Hey, Lilly. I didn't think anyone else would be here."

            show lilly basic_weaksmile
            with charachange

            li "Is that you, Hisao?"

            hi "Yeah, but you probably knew that already."

            "I turn to leave, which prompts Lilly to quickly speak up."

            show lilly basic_smile
            with charachange

            li "You don't have to leave so quickly. We can both have lunch in the same room. As a matter of fact, I would prefer to eat with someone else."

            "I'm about to ask her how she knew I was here to eat lunch, but brush it aside. It's just simple common sense, and I don't want to seem too easily impressed."

            show lilly basic_smile_close:
                center
                ypos 1.1
            with characlose

            "I take a seat at the desk in front of Lilly, after reversing it to face hers. I've heard that our minds fill in a lot of what we see based on how we remember seeing it once before, or our expectations."

            "Mostly for efficiency, so as to not have to process everything you look at individually."

            "Lilly never seems to stop to question any noise. So, I wonder, is it because her mind is filling in context every time? Or does she not care and just sort of accept things as they fall into place?"

            "On her desk there are just a few cookies and a thermos of tea. She must be one of those light lunch types. I bite into my sandwich. Some of the ingredients spill out the back end."

            show lilly basic_ara_close
            with charachange

            li "We haven't spoken in a long time, I'm surprised that you still remember my name."

            hi "Mmphffmm?"

            show lilly basic_smileclosed_close
            with charachange

            li "It must be very busy in the Student Council."

            hi "It's different every week. Some weeks are pretty slow, some weeks I consider taking a sick day."

            "Hold on, Lilly, I need a second to catch my breath from inhaling that sandwich."

            show lilly basic_smile_close
            with charachange

            li "And how has it been lately?"

            hi "Unpredictable."

            play sound sfx_snap

            show lilly basic_oops_close
            with vpunch

            "I snap my fingers, which, from her facial expression, upsets her a lot."

            show lilly basic_reminisce_close
            with charachange

            li "I think that you have been hanging out around those two too much."

            hi "I guess it is one of Shizune's trademarks. Personally, I like it."

            show lilly basic_displeased_close
            with charachange

            li "I ignore it."

            "Her tone doesn't change even slightly, but Lilly's mood has obviously dipped."

            hi "Doesn't seem like it would be easy to. I've been trying to figure out how she can make it so loud, but I think I'm damaging my knuckles."

            show lilly behind_displeased_close
            with charachange

            li "Even if it were loud enough to break the windows, I would ignore it. I'm not a trained seal; I have that luxury."

            hi "Are you still mad about that?"

            "I ask the question as carefully and diplomatically as possible, although in the end I'm only asking to satisfy my curiosity."

            show lilly basic_weaksmile_close
            with charachange

            li "No, of course not, although I don't like Shizune."

            show lilly basic_reminisce_close
            with charachange

            li "We were in the Student Council together for a brief time."

            hi "I heard."

            show lilly basic_sleepy_close
            with charachange

            li "I wish you hadn't been so quick to join."

            show lilly basic_listen_close
            with charachange

            li "I don't like the way Shizune runs the Student Council. Did you know that she scared off most of the old members? That is why I think she tries to surround herself with people who won't oppose her."

            show lilly basic_reminisce_close
            with charachange

            li "And they don't. It's like a dependency bubble."

            "I'm sure that Shizune is aware of what Lilly is saying. After all, I can remember her specifically denying it a couple times, which I'd always thought was strange."

            "They say that the more specific a denial is, the more likely it is that the allegations are true. In this case, I think I'd disagree. Shizune is the one subject on which her opinion could be called less than objective."

            hi "Did you tell her that?"

            show lilly basic_displeased_close
            with charachange

            li "Very often."

            "Lilly stops to polish off the last of her tea. I'm running behind on finishing my own lunch and take advantage of the pause to eat as much as possible."

            show lilly basic_sleepy_close
            with charachange

            li "All of her friends are related to the Student Council, like Misha."

            li "I heard things are touchy between her and Misha. Did they have a fight?"

            hi "Not really."

            show lilly basic_surprised_close
            with charachange

            li "Is that so?"

            show lilly basic_reminisce_close
            with charachange

            li "Either way, there is no point in attempting to force them to make up. Always try to confront everything head-on is what Shizune would do, but it doesn't work in the real world. At some point, it's just being stubborn, not bravery or good intentions."

            hi "That's a little general, don't you think?"

            show lilly basic_smileclosed_close
            with charachange

            li "Hm, I suppose."

            show lilly basic_weaksmile_close
            with charachange

            li "What do you think is the best to have with tea? Cookies, or scones? I like them both, in different ways. I couldn't possibly choose."

            show lilly basic_displeased_close
            with charachange

            li "I don't like people who constantly force me to pick sides or want to turn everything into a contest."

            li "When I joined the Student Council, I thought it would just mean helping everything run smoothly and helping people out, like being the class representative."

            show lilly basic_reminisce_close
            with charachange

            li "Instead, every day consisted of having Shizune stomp around, using Misha like a megaphone, to talk about how we had to outdo the last Student Council, and create more and more events, and make them increasingly larger."

            hi "But then the two of you basically want the same thing. All that stuff makes things exciting. I didn't really get it at first, but it's not some ego project. People like fireworks, and soba huts, candied apples, and dress-up days, or whatever."

            hi "The more the Student Council does, the more responsibility the school gives us. It means extra work, but in a way, it also means more freedom."

            hi "You have the pull to do things like organize a big festival, and they'll think you're capable enough to handle it instead of just rejecting it instantly."

            hi "Anyway, I want that too, now. It's got its share of pointless busywork, but there are moments that make it worth it when everything comes together. It gives me something to do. If I were to just go to school day in, day out, I think I'd explode."

            show lilly basic_weaksmile_close
            with charachange

            li "I think Yamaku is much more easygoing than other schools."

            "Yamaku isn't other schools, though."

            "I start slipping into another, familiar mentality. In some ways, it's almost too easygoing."

            "And if I were a different person I'm sure that I would find how easygoing it was to be stifling, though in any other school, such easiness would just be the normal flow of life."

            "But here, the uneventfulness would be compounded. It would feel different, because I'm not a normal person, after all."

            "I'd be reminded of it every time I heard the blood beating in my temples. I'd feel patronized and weak, and my bitterness would only grow."

            hi "Yeah, sure."

            hi "The point is, I think I understand what it's all about now. You're really giving Shizune too much of a hard time."

            show lilly basic_sleepy_close
            with charachange

            li "That might be true, but when it comes to how she treats individual people, she doesn't do very well."

            "Unfortunately, that one is a little harder to argue."

            show lilly basic_smile_close
            with charachange

            li "Do you have the time? I like to go to class ten minutes before the bell."

            hi "Then you're right on time if you go now."

            show lilly:
                ease 1.0 center alpha 0.0

            pause 1.0

            hide lilly

            stop music fadeout 4.0

            "Excusing herself, Lilly leaves, and I sit listening to the clicking of her cane on the floor fading into the mumble of other students having conversations in the other classrooms and in the hall."

            "I feel exhausted, and completely forget that I wanted to talk to Shizune today."

            scene black
            with dissolve

            if _in_replay:
                return

        call timeskip

        label .spiral:
            scene bg school_hallway3
            with locationchange

            "After classes the next day, I instantly head towards the student council room to talk to Shizune."

            "Even though she's in class, trying to cut her off and have a conversation with her near the doorway or out in the hall could be a little obstructive."

            scene bg school_lobby
            with locationchange

            "Better to try and meet up with her at the student council room. I take my time heading there, getting a juice from the vending machine on the way."

            "I also go over what I want to say to her in my head. It's nothing too important, only a few questions about upcoming events."

            scene bg school_council
            with locationchange

            play music music_rain fadein 8.0

            "The door is unlocked when I get there. I'd think the room was empty too, if I couldn't see Shizune's bag perched on her desk, with the top of her head peeking from behind it. It looks as though she's built herself a little fort."

            show shizu basic_normal at center
            with charaenter

            "Shizune gives a wave from behind her bag, before picking it up with a finger and moving it out of the way."

            "But after that, she immediately goes back to tapping her pen against the desk and staring into a checklist as if it held the meaning of life itself in it."

            show shizu adjust_frown
            with charachange

            ssh "What do you need?"

            his "I wanted to see if there was anything I could help with. Like all that over there, what are those?"

            "I point to the medium-sized stack of folders beside her, but she waves her hand dismissively."

            show shizu behind_blank
            with charachange

            ssh "I can handle it myself."

            his "Then what about the elections?"

            his "Also, where's Misha?"

            show shizu behind_sad
            with charachange

            shi "…"

            show shizu basic_normal2
            with charachange

            ssh "It's going okay. And I told Misha that I was going to handle everything myself."

            his "Why?"

            "Shizune spins a pen in her hand slowly, working it between each of her fingers, like a needle through a patch of cloth."

            show shizu behind_blank
            with charachange

            ssh "No reason."

            his "Really?"

            show shizu adjust_frown
            with charachange

            ssh "No reason."

            "She signs it again for emphasis, to shut down the notion that there's anything more behind it. But there is, since she's definitely not acting normally."

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=120}'What's with the silent treatment?' is the phrase that immediately springs to mind, even though it is hardly the time for humor. It does describe how I feel. We can't communicate normally, so I appreciate the few ways we can. To be shut out like this hurts."

            n "It's obvious that whatever her reasons, it's going to be pretty much impossible to talk to Shizune today. Beyond just being stubborn, she seems depressed, but with the way our conversation is going already, I don't see myself being able to find out what she's depressed about."

            n "{vspace=30}Somehow, that only makes me want to find out more. And that means I have to ask Misha. The problem is, I don't really know where Misha goes in her spare time."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")
            stop music fadeout 3.0

            nvl hide dissolve
            nvl clear

            scene bg school_lobby
            with shorttimeskip

            "After asking way more people than I should if they've noticed a girl with bright pink hair around, and getting way more negative answers than expected, I finally find a couple who have seen her."

            scene bg school_cafeteria
            show mishashort perky_smile at center
            with locationchange

            play music music_moonlight fadein 8.0

            "By the time I reach the cafeteria, where Misha has apparently been this entire time, I've been around the whole school twice, and am very tired. I realize I've passed by her before, and just didn't see her behind a pillar."

            hi "Why are you better at finding me than I am at finding you?"

            show mishashort hips_smile
            with charachange

            mi "You were looking for me, Hicchan?"

            show mishashort hips_grin
            with charachange

            mi "Hm~… Who knows~? I think it's just coincidence."

            hi "You know, the whole point of coincidences is that they aren't consistent."

            show mishashort cross_laugh
            with charachange

            mi "Hahaha~."

            hi "Are you having a really late lunch?"

            show mishashort sign_smile
            with charachange

            mi "I didn't get to eat at lunchtime, so yeah~! But~, not too much, so I can still have dinner."

            show mishashort perky_smile
            with charachange

            mi "Did you want to talk to me about something, Hicchan?"

            "I don't waste any time."

            hi "Yeah. The reason I'm here… Did you notice Shizune has been kind of moody today?"

            show mishashort perky_confused
            with charachange

            mi "I wanted to ask you the same thing, Hicchan~."

            show mishashort perky_sad
            with charachange

            mi "Well~, except, she's been this way for a couple of days now."

            hi "I see."

            show mishashort sign_confused
            with charachange

            mi "Hicchan, do you think it's because of something I did? Do you think I got upset at Shicchan, like last time?"

            hi "No. She seems angrier at me, anyway."

            "I'm not lying, I really don't. Unfortunately, my attempts to assure her of that don't seem to be going so well. In her own way, Misha is pretty stubborn, too."

            scene bg school_dormhisao_ss
            with locationskip

            "Eventually, I just head back to my dorm. The last few days have been nothing but a continuously frustrating experience, and they left me drained. I feel tired enough that I decide to take a nap, hoping that maybe I'll figure things out in my sleep."

            stop music fadeout 3.0

            scene black
            with shuteye

            pause 2.0

            scene bg school_dormhisao_ni
            with openeye

            play music music_night fadein 1.0

            "When I wake up, I feel more refreshed, but still without clarity. The only thing that has changed is that it's dark outside."

            "From opening the window a little, I can tell the weather is still kind of nice. After dry-swallowing my nighttime pills, I take a little walk to the vending machines."

            scene bg school_lobby_ni
            with locationskip

            "They're out of everything I'd normally get, so I mash my hand against the buttons until something pops out."

            scene bg school_courtyard_ni
            with locationchange

            "The lights are off in the main building, including the student council room. Just an offhand observation."

            play sound sfx_rustling

            "As I'm thinking to myself, I hear a rustling behind me. I've seen this movie before, and that is a very ominous sound to hear, alone at night."

            show kenji happy_ni at center
            with charaenter

            "Luckily, it's just Kenji, and he wanders out of the bushes in an unusually cheery mood."

            ke "Hey."

            hi "What the hell? Do you just creep up on people at night and casually go 'hey' a lot?"

            show kenji neutral_ni
            with charachange

            ke "No, that'd be weird. I knew it was you. I have extremely good night vision. Maybe it's because I'm superhuman."

            hi "What are you doing here, then?"

            show kenji tsun_ni
            with charachange

            ke "I could ask you the same thing. What are YOU doing here?"

            "I consider just telling him the truth, but quickly decide against it. It would take too long to explain."

            hi "Howling at the moon."

            show kenji neutral_ni
            with charachange

            ke "I do that too, sometimes. The moon isn't out tonight, though."

            "I barely even hear him, feeling a bit resentful at the interruption."

            $ renpy.music.set_volume(0.5, 1.0, channel="music")

            nvl clear
            nvl show dissolve

            n "{vspace=60}I lied to Shizune through my teeth that nothing was wrong. Or, to be more exact, I lied through my hands. And at the exact same time, I was carrying on an entirely different conversation with Misha."

            n "That conversation, understandably, could upset Shizune. But there was no way that she could have heard it. Even Misha's hands, usually signing all her thoughts, were completely still. Even if they weren't, I was standing in front of her, blocking them from Shizune's view."

            n "The only way that Shizune could listen in on that conversation would be if she could read lips. Pretty much the first thing I'd asked about when taking sign language was about lip reading, just out of curiosity. It's not easy, nor is it perfect… so I'd never considered it until now."

            n "{vspace=30}It would make sense, and the room for misunderstandings while reading lips wouldn't help."

            $ renpy.music.set_volume(1.0, 1.0, channel="music")

            nvl hide dissolve
            nvl clear

            ke "…So I realized that I could use the cover of darkness to buy milk. Usually, I only go out when it's raining or I can shroud myself in a sea of bikers, or tourists. This is much more consistent… I'm spending too much money on milk now, though."

            show kenji happy_ni
            with charachange

            ke "You seem kind of mopey or out of it or something. Don't think too hard, a man has to be all about action! You can think about stuff all day, but changing the situation around by doing something is the best way."

            ke "I do things all the time without thinking about it. That's why in middle school they called me 'causes many problems.' I thought it was cool; sounds like an Indian name."

            hi "I'm not really in the mood."

            show kenji neutral_ni
            with charachange

            ke "Having a bad day?"

            hi "Yeah, I don't know. I'm kind of distracted right now."

            stop music fadeout 7.0

            hide kenji
            with dissolve

            "So distracted that it doesn't hit me until he leaves that his was actually kind of sound advice. I think Shizune would have given me the same suggestion. By then, it's too late to thank him politely."

            "I already responded in the rudest tone possible. I just feel like an ass."

            "In retrospect, these past few days I've regretted every action I've taken. The worst part is that I haven't taken the time to stew over them, and in doing so, learn from them. This only leads to - has led to - more regrets."

            scene black
            with dissolve

            if _in_replay:
                return

        call timeskip

        label .terminal:
            play music music_dreamy fadein 2.0

            scene bg school_dormhisao
            with locationchange

            play sound sfx_doorknock2

            "The next morning, as I'm getting dressed, I hear a knock at my door. Quickly putting on the rest of my clothes, I open it, without really stopping to think about who could be behind it."

            scene bg school_dormhallway
            show shizu basic_normal at center
            with locationchange

            "It turns out to be Shizune."

            show shizu behind_blank
            with charachange

            ssh "Misha told me that you were looking for me."

            "I'm a bit hurt that I don't even get a 'good morning,' but it's not too big a deal."

            his "I was."

            show shizu basic_normal2
            with charachange

            ssh "But you found me yesterday."

            "Shizune's fingers trace a crack in the wall. It seems like she's trying her best to look distant."

            show shizu adjust_smug
            with charachange

            ssh "Well, I didn't make it easy, did I?"

            his "It's all right."

            show shizu behind_blank
            with charachange

            ssh "That's why I'm here. We can talk today. Although… I kind of want to go somewhere else."

            his "What about class?"

            show shizu adjust_smug
            with charachange

            ssh "It's fine, it's fine."

            show shizu basic_normal2
            with charachange

            ssh "How about we take a walk around the school? Everywhere except the main building is going to be deserted. The first period bell should be ringing right now."

            "I take a quick glance at my watch and see that she's right."

            his "Okay."

            stop music fadeout 6.0

            show shizu basic_angry
            with charachange

            shi "…"

            his "Is there something wrong?"

            show shizu behind_blank
            with charachange

            ssh "Why do you think there is something wrong?"

            his "Because you're obviously upset. I could just tell."

            his "It's what I wanted to talk to you about."

            show shizu basic_normal2
            with charachange

            "Shizune quickly cracks her knuckles while I sign to her."

            show shizu behind_blank
            with charachange

            ssh "Apparently, I'm easier to read than I'd thought. I was trying hard to hide it. Can you tell what I'm thinking right now?"

            hide shizu
            with charaexit

            "I don't respond, and Shizune heads towards the door, slowly enough that I can tell she wants me to follow her. Her hands are folded behind her back, which is arched against them as though she is about to bend over backwards at any second."

            scene bg school_courtyard
            with locationchange

            "Outside, I see Shizune is right. The school is completely deserted. Although it's not my first time seeing the school like this, it's kind of eerie."

            scene bg school_backexit at right
            with locationchange

            "Shizune acts almost as though I'm not there, browsing a vending machine and taking a slow and winding path until we end up behind the main building."

            show shizu basic_normal_close:
                tworight
                ease 1.0 ypos 1.05
            with Dissolve(1.0)

            "Finally, she leans against a wall and faces me, but it's like I've forgotten how to start a conversation."

            play music music_sadness fadein 8.0

            show shizu behind_blank_close
            with charachange

            ssh "There is a saying. 'You don't know how much you've screwed up until you screw up.'"

            his "Who says that?"

            show shizu basic_normal2_close
            with charachange

            ssh "I guess it's me."

            show shizu basic_angry_close
            with charachange

            "Reconsidering her train of thought, she waves her hands in frustration."

            show shizu behind_blank_close
            with charachange

            ssh "Okay, I'll put it differently."

            show shizu basic_normal_close
            with charachange

            ssh "When I was younger, we had to make posters for Earth Day in school. There was another girl in my class whom everyone considered the best artist."

            show shizu behind_blank_close
            with charachange

            ssh "It wasn't because she could draw better than everyone else, it was how much she could fit into a single picture."

            show shizu adjust_frown_close
            with charachange

            ssh "I wanted to be better than her, so I made countless posters until I ended up with the best possible one. I had to be the best and have the greatest one. In the end, everyone liked my poster the most of all, even the teacher."

            show shizu basic_normal_close
            with charachange

            ssh "A week later, it was meaningless. I threw it in the trash."

            show shizu behind_blank_close
            with charachange

            ssh "I think I've told you something like this before."

            his "Yeah."

            show shizu basic_angry_close
            with charachange

            ssh "When I feel like I'm finished, I wish I could just wipe the slate clean. Whether I succeed or not. I put Misha through a lot, and even dragged you into it."

            show shizu adjust_frown_close
            with charachange

            ssh "And every point where I could have solved this silly situation, or prevented it from happening in the first place, keeps coming back to me."

            show shizu behind_sad_close
            with charachange

            ssh "It's the worst feeling. Especially when I feel like I've done nothing right and everything wrong. Like recently. It's the worst kind of failure. I feel like a failure on every level."

            show shizu basic_normal2_close
            with charachange

            ssh "I wish I could wipe away everything I've done and just be alone, since all I've done is mess with Misha for two years. And jerk you around for a year for selfish reasons."

            his "It's fine."

            show shizu adjust_frown_close
            with charachange

            ssh "No, it's not. You don't understand. I was just thinking about it; everything I do feels like I have to beat someone else. Everyone else, even. If that is how it is, then what are my relationships with people? They almost feel the same."

            "I can see where this is going."

            show shizu behind_sad_close
            with charachange

            ssh "The point is that I've messed up so many people by being selfish, and now I want to be away from other people for a while."

            his "Even me?"

            "There's a pause."

            show shizu basic_normal_close
            with charachange

            ssh "Yes."

            "Followed by an even longer pause, this time from me."

            his "I see."

            his "That's the most selfish thing you could do."

            his "It's just you making another decision by yourself."

            show shizu basic_normal2_close
            with charachange

            shi "…"

            "For a minute, it looks as though she's considering the best way to respond, but in the end, she simply nods. Which, I think, is the best way to respond anyway."

            "It's very like her, to be roundabout even now, but ultimately without excuses."

            "All my emotions simmer inside me. I see a kettle in front of me, water rolling inside it, so close that I can touch it and feel the heat radiating off of it. I'm glad for the distraction, because I know there's no recourse or bargaining possible."

            show shizu adjust_frown_close
            with charachange

            ssh "You told me that everything was fine, but it wasn't true, was it?"

            show shizu behind_sad_close
            with charachange

            ssh "I can't believe it ever again, then."

            hi "All right."

            show shizu:
                xpos 0.85 alpha 0.0
            show bg at center
            with charamovechangefaster

            hide shizu

            "Not even bothering to sign it, I stand up. My hands are in my pockets, fingering my loose change. The morning air is cold against my face."

            scene ev shizu_badend:
                xalign 0.0 yalign 0.5 zoom 1.1
                acdc_warp 10.0 zoom 1.0
            with locationchange

            "As I look back at her, she seems very lonely. I'm reminded of myself. I've made that expression before. Maybe it's on my face right now. It feels like the image of such a lonely girl will stick in my mind forever."

            "Every moment where I could have prevented this, or solved the problem, comes back to me. It makes me smile in a way without amusement."

            stop music fadeout 4.0

            if _in_replay:
                return

    return
