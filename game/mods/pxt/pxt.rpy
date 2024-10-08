label pxt_real_start:

label .pxt_a5s1:

scene black onlayer master
with fade

show black as bg onlayer master
with None

if commentary == True:

    show curtains onlayer master
    show audience onlayer master
    show philostrates onlayer master at left
    with dissolve

    phi "A play there is, my lord, some ten words long, which is as brief as I have known a play;"
    phi "But by ten words, my lord, it is too long, which makes it tedious:"
    phi "For in all the play there is not one word apt, one player fitted:"
    phi "And tragical, my noble lord, it is;"
    phi "For Pyramus therein doth kill himself: which when I saw rehears'd, I must confess, made mine eyes water;"
    phi "But more merry tears the passion of loud laughter never shed."

    the "What are they that do play it?"

    phi "Hard-handed men that work in Athens here, which never labour'd in their minds till now;"
    phi "And now have toil'd their unbreath'd memories with this same play against your nuptial."

    the "And we will hear it."

    phi "No, my noble lord, it is not for you:"
    phi "I have heard it over, and it is nothing, nothing in the world;"
    phi "Unless you can find sport in their intents, extremely stretch'd and conn'd with cruel pain, to do you service."

    the "I will hear that play; For never anything can be amiss when simpleness and duty tender it."
    the "Go, bring them in: and take your places, ladies. "

    hide philostrates onlayer master
    with easeoutleft



    hip "I love not to see wretchedness o'er-charged, and duty in his service perishing."

    the "Why, gentle sweet, you shall see no such thing."

    hip "He says they can do nothing in this kind."

    the "The kinder we, to give them thanks for nothing."
    the "Our sport shall be to take what they mistake:"
    the "And what poor duty cannot do, noble respect takes it in might, not merit."
    the "Where I have come, great clerks have purposed to greet me with premeditated welcomes;"
    the "Where I have seen them shiver and look pale, make periods in the midst of sentences,"
    the "Throttle their practis'd accent in their fears, "
    the "And, in conclusion, dumbly have broke off, not paying me a welcome."
    the "Trust me, sweet, out of this silence yet I pick'd a welcome;"
    the "And in the modesty of fearful duty I read as much as from the rattling tongue of saucy and audacious eloquence."
    the "Love, therefore, and tongue-tied simplicity in least speak most to my capacity."



    show philostrates onlayer master at left
    with easeinleft

    phi "So please your grace, the prologue is address'd."

    the "Let him approach."


nvl show dissolve
nvl clear

pr "If we offend, it is with our good will."
pr "That you should think, we come not to offend,"
pr "But with good will. To show our simple skill,"
pr "That is the true beginning of our end."
pr "Consider then, we come but in despite."
pr "We do not come, as minding to content you,"
pr "Our true intent is. All for your delight"
pr "We are not here. That you should here repent you,"
pr "The actors are at hand: and, by their show,"
pr "You shall know all that you are like to know,"

nvl clear

if commentary == True:
    the "This fellow doth not stand upon points."
    lys "He hath rid his prologue like a rough colt; he knows not the stop. A good moral, my lord: it is not enough to speak, but to speak true."
    hip "Indeed he hath played on this prologue like a child on a recorder; a sound, but not in government."
    the "His speech was like a tangled chain; nothing impaired, but all disordered. Who is next?"

    show bg arcadia behind curtains onlayer master
    with None

    hide curtains onlayer master
    with easeouttop



play music "mods/pxt/music/tam-n06.ogg" fadein 1.0

show bg arcadia onlayer master
show pyramus smile behind audience at offscreenright onlayer master
show thisbe smile behind audience at offscreenright onlayer master
show wall smile behind audience at offscreenright onlayer master
show moon smile behind audience at offscreenright onlayer master
show lion smile behind audience at offscreenright onlayer master
with dissolve

nvl clear
nvl show

pr "Gentles, perchance you wonder at this show;"
pr "But wonder on, till truth make all things plain."

show pyramus smile onlayer master
with ease

pr "This man is Pyramus, if you would know;"

show pyramus smile onlayer master at offscreenleft
show thisbe smile onlayer master
with ease

pr "This beauteous lady Thisby is certain."

show thisbe smile onlayer master at offscreenleft
show wall smile onlayer master
with ease

pr "This man, with lime and rough-cast, doth present"
pr "Wall, that vile Wall which did these lovers sunder;"
pr "And through Wall's chink, poor souls, they are content"
pr "To whisper, at the which let no man wonder."

show wall smile onlayer master at offscreenleft
show moon smile onlayer master
with ease

pr "This man, with lanthorn, dog, and bush of thorn,"
pr "Presenteth Moonshine: for, if you will know,"
pr "By moonshine did these lovers think no scorn"
pr "To meet at Ninus' tomb, there, there to woo."

nvl clear

show moon smile onlayer master at offscreenleft
show lion smile onlayer master
with ease

pr "This grisly beast, which by name Lion hight,"
pr "The trusty Thisby, coming first by night,"
pr "Did scare away, or rather did affright;"
pr "And as she fled, her mantle she did fall;"
pr "Which Lion vile with bloody mouth did stain:"
pr "Anon comes Pyramus, sweet youth, and tall,"
pr "And finds his trusty Thisby's mantle slain;"
pr "Whereat with blade, with bloody blameful blade,"
pr "He bravely broach'd his boiling bloody breast;"
pr "And Thisby, tarrying in mulberry shade,"
pr "His dagger drew, and died. For all the rest,"
pr "Let Lion, Moonshine, Wall, and lovers twain,"
pr "At large discourse while here they do remain."

nvl clear

show lion smile onlayer master at offscreenleft
with ease

hide pyramus onlayer master
hide thisbe onlayer master
hide wall onlayer master
hide moon onlayer master
hide lion onlayer master
with None

stop music fadeout 2.0



if commentary == True:
    the "I wonder if the lion be to speak."
    dem "No wonder, my lord: one lion may, when many asses do."

play music "mods/pxt/music/tam-n09.ogg" fadein 1.0

show wall happy behind audience onlayer master
with easeinbottom

wa "In this same interlude it doth befall"
wa "That I, one Snout by name, present a wall:"

show wall smile onlayer master
with dissolve

wa "And such a wall as I would have you think"
wa "That had in it a crannied hole or chink,"
wa "Through which the lovers, Pyramus and Thisby,"
wa "Did whisper often very secretly."

show wall downtrodden onlayer master
with dissolve

wa "This loam, this rough-cast, and this stone, doth show"
wa "That I am that same wall; the truth is so:"
wa "And this the cranny is, right and sinister,"
wa "Through which the fearful lovers are to whisper."

if commentary == True:
    the "Would you desire lime and hair to speak better?"
    dem "It is the wittiest partition that ever I heard discourse, my lord."
    the "Pyramus draws near the wall; silence."



stop music fadeout 0.5

show pyramus neutral behind audience at offscreenleft onlayer master
with None

show pyramus neutral onlayer master at left
show wall downtrodden onlayer master at right
with ease

play music "mods/pxt/music/tamhe08.ogg" fadein 1.0

py "O grim-look'd night! O night with hue so black!"
py "O night, which ever art when day is not!"
py "O night, O night, alack, alack, alack,"
py "I fear my Thisby's promise is forgot!—"

show pyramus angry onlayer master at left
with dissolve

py "And thou, O wall, O sweet, O lovely wall,"
py "That stand'st between her father's ground and mine;"
py "Thou wall, O wall, O sweet and lovely wall,"
py "Show me thy chink, to blink through with mine eyne."

show wall embarrassed onlayer master at right
with dissolve



show pyramus happy onlayer master at left
with dissolve

py "Thanks, courteous wall: Jove shield thee well for this!"
py "But what see what see I? No Thisby do I see."

show pyramus angry onlayer master at left
with dissolve

py "O wicked wall, through whom I see no bliss,"
py "Curs'd be thy stones for thus deceiving me!"

if commentary == True:
    the "The wall, methinks, being sensible, should curse again."

    show pyramus smile onlayer master at left
    with dissolve

    py "No, in truth, sir, he should not. 'Deceiving me' is Thisby's cue: she is to enter now, and I am to spy her through the wall."
    py "You shall see it will fall pat as I told you."

show pyramus happy onlayer master at left
with dissolve

py "—Yonder she comes."



show thisbe sad behind audience at offscreenright onlayer master
with None

show pyramus happy onlayer master at offscreenleft
show wall embarrassed onlayer master at left
show thisbe sad onlayer master at right
with ease

th "O wall, full often hast thou heard my moans,"
th "For parting my fair Pyramus and me:"
th "My cherry lips have often kiss'd thy stones:"
th "Thy stones with lime and hair knit up in thee."

show pyramus smile onlayer master at left
show wall embarrassed onlayer master at right
show thisbe sad onlayer master at offscreenright
with ease

py "I see a voice; now will I to the chink,"
py "To spy an I can hear my Thisby's face."

show pyramus happy onlayer master at left
with dissolve

py "Thisby!"

show pyramus smile onlayer master at offscreenleft
show wall embarrassed onlayer master at left
show thisbe shock onlayer master at right
with ease

th "My love! thou art my love, I think."

show pyramus smile onlayer master at left
show wall embarrassed onlayer master at right
show thisbe shock onlayer master at offscreenright
with ease

py "Think what thou wilt, I am thy lover's grace;"
py "And like Limander am I trusty still."

show pyramus smile onlayer master at offscreenleft
show wall embarrassed onlayer master at left
show thisbe smile onlayer master at right
with ease

th "And I like Helen, till the fates me kill."

show pyramus smile onlayer master at left
show wall embarrassed onlayer master at right
show thisbe smile onlayer master at offscreenright
with ease

py "Not Shafalus to Procrus was so true."

show pyramus smile onlayer master at offscreenleft
show wall embarrassed onlayer master at left
show thisbe smile onlayer master at right
with ease

th "As Shafalus to Procrus, I to you."

show pyramus happy onlayer master at left
show wall embarrassed onlayer master at right
show thisbe smile onlayer master at offscreenright
with ease

py "O, kiss me through the hole of this vile wall."

show pyramus happy onlayer master at offscreenleft
show wall embarrassed onlayer master at left
show thisbe happy onlayer master at right
with ease

th "I kiss the wall's hole, not your lips at all."

show pyramus happy onlayer master at left
show wall embarrassed onlayer master at right
show thisbe happy onlayer master at offscreenright
with ease

py "Wilt thou at Ninny's tomb meet me straightway?"

show pyramus happy onlayer master at offscreenleft
show wall embarrassed onlayer master at left
show thisbe happy onlayer master at right
with ease

th "'Tide life, 'tide death, I come without delay."

show wall happy onlayer master at left
with dissolve

wa "Thus have I, wall, my part discharged so;"
wa "And, being done, thus Wall away doth go."

show wall happy onlayer master at offscreenleft
show thisbe happy onlayer master at offscreenright
with ease

hide pyramus onlayer master
hide thisbe onlayer master
hide wall onlayer master
with None



if commentary == True:
    the "Now is the mural down between the two neighbours."
    dem "No remedy, my lord, when walls are so wilful to hear without warning."
    hip "This is the silliest stuff that ever I heard."
    the "The best in this kind are but shadows; and the worst are no worse, if imagination amend them."
    hip "It must be your imagination then, and not theirs."
    the "If we imagine no worse of them than they of themselves, they may pass for excellent men. Here come two noble beasts in, a moon and a lion."



stop music fadeout 0.5

show lion happy behind audience onlayer master
with easeinbottom

play music "mods/pxt/music/tam-n06.ogg" fadein 1.0

lio "You, ladies, you, whose gentle hearts do fear"
lio "The smallest monstrous mouse that creeps on floor,"
lio "May now, perchance, both quake and tremble here,"
lio "When lion rough in wildest rage doth roar."

show lion embarrassed onlayer master
with dissolve

lio "Then know that I, one Snug the joiner, am"
lio "A lion fell, nor else no lion's dam:"

show lion smile onlayer master
with dissolve

lio "For, if I should as lion come in strife"
lio "Into this place, 'twere pity on my life."

if commentary == True:
    the "A very gentle beast, and of a good conscience."
    dem "The very best at a beast, my lord, that e'er I saw."
    lys "This lion is a very fox for his valour."
    the "True; and a goose for his discretion."
    dem "Not so, my lord; for his valour cannot carry his discretion, and the fox carries the goose."
    the "His discretion, I am sure, cannot carry his valour; for the goose carries not the fox. It is well; leave it to his discretion, and let us listen to the moon."

show lion smile onlayer master at left
with ease

show moon happy behind lion at right onlayer master
with dissolve

mo "This lanthorn doth the horned moon present:"

if commentary == True:
    dem "He should have worn the horns on his head."
    the "He is no crescent, and his horns are invisible within the circumference."

    show moon smile onlayer master at right
    with dissolve

    mo "This lanthorn doth the horned moon present;"

show moon blush onlayer master at right
with dissolve

mo "Myself the man i' the moon do seem to be."

if commentary == True:
    the "This is the greatest error of all the rest: the man should be put into the lantern. How is it else the man i' the moon?"
    dem "He dares not come there for the candle: for, you see, it is already in snuff."
    hip "I am aweary of this moon: would he would change!"
    the "It appears, by his small light of discretion, that he is in the wane: but yet, in courtesy, in all reason, we must stay the time."
    lys "Proceed, moon."

show moon embarrassed onlayer master at right
with dissolve

mo "All that I have to say, is to tell you that the lantern is the moon;"

show moon sad onlayer master at right
with dissolve

mo "I, the man i' the moon;"

show moon smile onlayer master at right
with dissolve

mo "This thorn-bush, my thorn-bush;"
mo "And this dog, my dog."

if commentary == True:
    dem "Why, all these should be in the lantern; for all these are in the moon. But silence; here comes Thisbe."



stop music fadeout 2.0

show thisbe happy behind audience at offscreenright onlayer master
with None

show thisbe happy onlayer master at right
show moon smile onlayer master
with ease

th "This is old Ninny's tomb. Where is my love?"

show lion shock onlayer master at left
with dissolve

lio "Oh!"



show thisbe shock onlayer master at right
with dissolve

hide thisbe onlayer master
with easeoutright

if commentary == True:
    dem "Well roared, lion."
    the "Well run, Thisbe."
    hip "Well shone, moon. —Truly, the moon shines with a good grace."



show lion happy onlayer master at left
with dissolve

hide lion onlayer master
with easeoutright

show moon smile onlayer master
with dissolve

if commentary == True:
    the "Well moused, lion."
    dem "And so comes Pyramus."
    lys "And then the lion vanishes."



show pyramus neutral behind audience at offscreenleft onlayer master
with None

play music "mods/pxt/music/tamhe01.ogg" fadein 1.0

show pyramus neutral onlayer master at left
show moon smile onlayer master at right
with ease

py "Sweet moon, I thank thee for thy sunny beams;"
py "I thank thee, moon, for shining now so bright:"
py "For, by thy gracious golden, glittering streams,"
py "I trust to take of truest Thisby's sight."

show pyramus angry onlayer master at left
with dissolve

py "But stay;—O spite!"
py "But mark,—poor knight,"
py "What dreadful dole is here!"
py "Eyes, do you see?"

show pyramus embarrassed onlayer master at left
with dissolve

py "How can it be?"
py "O dainty duck! O dear!"
py "Thy mantle good,"
py "What! stained with blood?"
py "Approach, ye furies fell!"
py "O fates! come, come;"

show pyramus angry onlayer master at left
with dissolve

py "Cut thread and thrum;"
py "Quail, rush, conclude, and quell!"

if commentary == True:
    the "This passion, and the death of a dear friend, would go near to make a man look sad."
    hip "Beshrew my heart, but I pity the man."

show pyramus embarrassed onlayer master at left
with dissolve

py "O wherefore, nature, didst thou lions frame?"
py "Since lion vile hath here deflower'd my dear;"
py "Which is—no, no—which was the fairest dame"
py "That liv'd, that lov'd, that lik'd, that look'd with cheer."
py "Come, tears, confound;"
py "Out, sword, and wound"
py "The pap of Pyramus:"

show pyramus angry onlayer master at left
with dissolve

py "Ay, that left pap,"
py "Where heart doth hop:—"
py "Thus die I,{w} thus,{w} thus,{w} thus."

show pyramus embarrassed onlayer master at left
show moon sad onlayer master at right
with dissolve

py "Now am I dead,"
py "Now am I fled;"
py "My soul is in the sky:"
py "Tongue, lose thy light!"
py "Moon, take thy flight!"
py "Now die,{w} die,{w} die,{w} die,{w} die."

hide pyramus onlayer master
with easeoutbottom

hide moon onlayer master
with easeoutright



if commentary == True:
    dem "No die, but an ace, for him; for he is but one."
    lys "Less than an ace, man; for he is dead; he is nothing."
    the "With the help of a surgeon he might yet recover and prove an ass."
    hip "How chance moonshine is gone before Thisbe comes back and finds her lover?"
    the "She will find him by starlight.—Here she comes; and her passion ends the play."



show thisbe smile behind audience onlayer master
with easeinright

if commentary == True:
    hip "Methinks she should not use a long one for such a Pyramus: I hope she will be brief."
    dem "A mote will turn the balance, which Pyramus, which Thisbe, is the better."
    lys "She hath spied him already with those sweet eyes."
    dem "And thus she moans, videlicet.—"

show thisbe shock onlayer master
with dissolve

th "Asleep, my love?"
th "What, dead, my dove?"

show thisbe sad onlayer master
with dissolve

th "O Pyramus, arise,"
th "Speak, speak. Quite dumb?"
th "Dead, dead? A tomb"
th "Must cover thy sweet eyes."
th "These lily lips,"
th "This cherry nose,"
th "These yellow cowslip cheeks,"
th "Are gone, are gone:"

show thisbe cry onlayer master
with dissolve

th "Lovers, make moan!"
th "His eyes were green as leeks."
th "O Sisters Three,"
th "Come, come to me,"
th "With hands as pale as milk;"
th "Lay them in gore,"
th "Since you have shore"
th "With shears his thread of silk."

show thisbe sad onlayer master
with dissolve

th "Tongue, not a word:—"
th "Come, trusty sword;"
th "Come, blade, my breast imbrue;"
th "And farewell, friends:—"
th "Thus Thisby ends;"
th "Adieu,{w} adieu,{w} adieu."



stop music fadeout 5.0

hide thisbe onlayer master
with easeoutbottom

if commentary == True:

    show curtains behind audience onlayer master
    with easeintop

    the "Moonshine and lion are left to bury the dead."
    dem "Ay, and wall too."


    show pyramus smile behind audience onlayer master
    with easeinbottom

    bo "No, I assure you; the wall is down that parted their fathers. Will it please you to see the epilogue, or to hear a Bergomask dance between two of our company?"

    the "No epilogue, I pray you; for your play needs no excuse. "
    the "Never excuse; for when the players are all dead there need none to be blamed."
    the "Marry, if he that writ it had played Pyramus, and hang'd himself in Thisbe's garter, it would have been a fine tragedy: and so it is, truly; and very notably discharged. "
    the "But come, your Bergomask; let your epilogue alone. "

scene black onlayer master
with fade

with Pause(2.0)

default creditss = Text(_("""
    {image=gui/icons/flourish_left.png} {b}Writing{/b} {image=gui/icons/flourish_right.png}
    Peter Quince

    {image=gui/icons/flourish_left.png} {b}Sprites{/b} {image=gui/icons/flourish_right.png}
    http://senji4.uijin.com/
    http://www.vita-chi.net/

    {image=gui/icons/flourish_left.png} {b}Backgrounds{/b} {image=gui/icons/flourish_right.png}
    Kaikei Sozai Mise (http://shass.sakura.ne.jp/)
    gustty (http://www.flickr.com/people/gustty/)

    {image=gui/icons/flourish_left.png} {b}Music{/b} {image=gui/icons/flourish_right.png}
    TAM Music Factory (http://www.tam-music.com/)

    {image=gui/icons/flourish_left.png} {b}Special Thanks{/b} {image=gui/icons/flourish_right.png}
    Aura
    """), color="#ffffff", text_align=0.5, size=47, xalign=0.5)

show text creditss with dissolve
with Pause(10.0)
