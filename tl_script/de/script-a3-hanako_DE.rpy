label de_H11:

scene bg school_miyagi_ss onlayer master
show hanako basic_distant_close_ss onlayer master at center
with locationchange

"Das helle Licht des Nachmittags, in das der Raum getaucht ist, weicht langsam dem Abendrot. Eine Uhr tickt im Hintergrund gemächlich vor sich hin. Sie ist kaum zu hören."


"Aber egal, wie lange ich warte, das Ergebnis kann ich nicht verhindern."


"Die zierliche Spielfigur gibt ein leises „Klack” von sich, als sie auf dem Brett aufsetzt."


show hanako basic_normal_close_ss onlayer master
with charachange

"Wie eine Maschine macht Hanako ihre Züge nur Augenblicke nach meinen."


"Es ist beschämend. Im Gegensatz zu meinen Fünf-Minuten-Zügen scheint sie genau zu wissen, was sie vorhat."


show hanako basic_smile_close_ss onlayer master
with charachange

play music music_tranquil fadein 3.0

ha "Matt."


hi "Wieder einmal… Wie steht's dann? 3-2?"


show hanako cover_bashful_close_ss onlayer master
with charachange

ha "Patts zählen nicht."


hi "Mist. Du wirst jeden Tag besser darin."


"Das, oder sie hat sich zurückgehalten. Ich hätte das bei unserer ersten Begegnung nie gedacht, aber sie hat wirklich ein Händchen für dieses Spiel."


"Schach ist anscheinend ein beliebter Zeitvertreib für uns zwei geworden; wir verstecken uns im Teezimmer und spielen ein oder zwei Runden nach dem Unterricht."


"Hier drin kann man die Schüler draußen gerade noch herumlaufen hören."
"Die Alltagsgeräusche von unten erinnern mich ein bisschen an mein Leben vor der Yamaku, obwohl ich mir mittlerweile sehr wohl bewusst bin, dass das ein Leben ist, zu dem ich nie wieder zurückkehren werde."


hi "Lust auf noch eine Runde?"


show hanako basic_worry_close_ss onlayer master
with charachange

ha "Ich… Ich muss meine Hausaufgaben fertigmachen…"


hi "Oh. Na gut, ich seh dich dann morgen."


show hanako basic_distant_close_ss onlayer master
with charachange

ha "Aber… Was ist damit…"


"Hanako zeigt auf das Teeservice, das um das größtenteils leere Schachbrett herum steht."


hi "Mach dir darüber keine Gedanken. Das mach ich schon."


show hanako basic_normal_close_ss onlayer master
with charachange

ha "Oh… Okay…"


show hanako basic_bashful_close_ss onlayer master
with charachange

ha "Bi-Bis dann."


hi "Bis später."


hide hanako onlayer master
with charaexit

"Hanako geht, während ich anfange aufzuräumen."


"Die gelegentlichen Pfiffe und der Jubel der Sportklubs draußen werden seltener, und irgendwann wird es still."


"Ein Teil von mir will immer noch bei irgendeiner Mannschaft mitmachen. Da ich vor meinem Unfall Fußball und andere Sportarten gespielt habe, glaube ich, dass es völlig normal ist, wenn ich bei Sachen nostalgisch werde, die ich nicht mehr tun kann."


"Aber ich habe noch andere Gründe, warum ich so oft hier bin. Wegen dieser Gründe finde ich es auch nicht so schlimm, diesen Teil von mir zu verlieren."
"Lilly ist mittlerweile eine gute Freundin, aber es sind die kleinen Wortwechsel mit Hanako, die mir besonders lieb sind."


"Die kleinen Erfolge, die ich jeden Tag feiere, wenn ich immer mehr davon sehe, wie sie unter ihrem selbstgeschaffenen Panzer ist. Vor allem deswegen komme ich hierher."


"Als ich die Tassen und Untertassen wegräume, höre ich vor der Tür jemanden reden. Kurz halte ich inne, um zu lauschen. Ich kann hören, dass es Hanako und Lilly sind, und beschließe rauszugehen, um nachzusehen."


scene bg school_hallway2 onlayer master
show lilly basic_weaksmile onlayer master at twoleft
show hanako emb_downtimid onlayer master at tworight
with locationchange

li "Bist du ganz sicher?"


ha "Ich… Ich bin sicher…"


show hanako emb_timid onlayer master
with charachange

ha "Ah, Hisao."


"Leicht überrascht dreht sich Hanako um, als sie bemerkt, dass ich mich nähere. Lilly hat sie wohl gerade noch erwischt, als sie dabei war zu gehen."


show lilly basic_smile onlayer master
with charachange

li "Ach, Hisao ist auch da?"


hi "Tag Lilly. Was ist los?"


show lilly basic_smileclosed onlayer master
with charachange

li "Ich habe gehofft, dass ihr Zwei mich jetzt, wo ich mit meinen Klassensprecherpflichten für heute fertig bin, zum Tee ins Shanghai begleitet. Es wäre doch nett, zur Abwechslung mal aus der Schule rauszukommen."


hi "Ich wäre dabei, aber ich glaube, Hanako hatte noch was zu tun…?"


show hanako basic_smile onlayer master
with charachange

ha "E-Es… ist nicht so viel…"


show lilly behind_cheerful onlayer master
with charachange

li "Wunderbar. Dann ist das wohl beschlossen."


stop music fadeout 2.0

scene bg suburb_shanghaiint onlayer master at Fullpan(3.0, dir="left")
with shorttimeskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

"Ich lasse meine Augen durch das Café schweifen, als wir Drei eintreten. Wie üblich sind höchstens eine handvoll Leute da, und der Geräuschpegel liegt bei einem leisen Summen im Hintergrund."


scene bg suburb_shanghaiint onlayer master at left
show hanako emb_emb onlayer master:
    xpos 0.4 xanchor 0.5
show lilly cane_smileclosed onlayer master at twoleft
with charaenter

play music music_dreamy fadein 6.0

"Lillys Griff um Hanakos Arm verbleibt genau so, wie er den ganzen langsamen Fußmarsch den Hügel hinunter zum Dorf war. Allerdings ist schwer zu sagen, aus welchem Grund – um Lilly zu leiten, oder um Hanako zu beruhigen."


show lilly basic_smile onlayer master
with charachange

"Als Yuuko schnell zu uns herüber eilt, lässt Lilly Hanakos Arm kurz los, um ihren Gehstock zusammenzuschieben, greift dann aber gleich wieder nach ihr."


show yuukoshang closedhappy_up onlayer master at tworight
with charaenter

yu "Willkommen im Shanghai! Darf ich eure Bestellung aufnehmen?"


show yuukoshang neutral_up onlayer master at Transform(ypos=1.25)
with Dissolvemove(0.5)

show yuukoshang neutral_down onlayer master at tworight
with dissolvecharamove

"Durch ihre gut ausgeführte und professionelle Vorstellung ist sie in guter Laune und verbeugt sich tief. Eine erfrischend andere Yuuko als sonst."


show lilly basic_smileclosed onlayer master
with charachange

li "Nur Tee, bitte. Hanako, Hisao?"


hi "Ich hätte gerne ein Stück Kuchen und einen Kaffee."


show hanako basic_smile onlayer master
with charachange

ha "Nur… T-Tee… bitte."


show yuukoshang smile_up onlayer master
with charachange

yu "Kommt sofort. Bitte setzt euch, wo ihr wollt, ich bin gleich wieder da."


hide yuukoshang onlayer master
with charaexit

"Yuuko zeigt uns ein Lächeln und nickt, bevor sie zur Theke schlurft und wir uns schnell zu einigen leeren Plätzen am Fenster aufmachen."


hide hanako onlayer master
hide lilly onlayer master
with charaexit

show bg suburb_shanghaiint onlayer master at right
with charamove_slow

show lilly basic_sleepy_close onlayer master:
    twoleft
    easein 1.0 ypos 1.1
show hanako basic_smile_close onlayer master:
    tworight
    easein 1.0 ypos 1.09
with charaenter

"Wir rutschen auf unsere Plätze, die Mädchen auf der einen Seite, wobei Lillys Gehstock neben ihnen liegt, und ich auf der anderen. Ich stelle fest, dass Hanako etwas nicht macht, was sie sonst so oft tut."


"Sie schaut nicht auf den Boden und versteckt sich hinter ihrer blinden Begleitung, während sie sich dabei eifrig einzureden versucht, dass die Welt um sie herum nicht existiert."
"Sie hält lediglich ihren Blick gesenkt und hilft Lilly."


hi "Bist du okay, Lilly? Du siehst müde aus."


show lilly basic_weaksmile_close onlayer master:
    twoleft
    ypos 1.1
with charachange

"Leicht senkt sie ihren Kopf, wobei sie ein bisschen verlegen wirkt, weil sie es sich anmerken hat lassen."


li "Die Arbeit eines Klassensprechers kann sehr anstrengend sein, wenn man bedenkt, dass das bedeutet, oft mit dem Schülerrat zu tun zu haben."


show lilly basic_sleepy_close onlayer master
with charachange

li "Wirklich sehr anstrengend."


show hanako basic_normal_close onlayer master:
    tworight
    ypos 1.09
with charachange

ha "Wie… machen sich die anderen Klassensprecher?"


show lilly basic_reminisce_close onlayer master
with charachange

li "Besser als ich, aber nicht sehr viel. Shizune ist eine strenge Zuchtmeisterin, egal um wen es geht."


hi "Hört sich nicht so an, als würdest du an dem Job besonders Gefallen finden. Warum machst du ihn überhaupt, wenn er so schlimm ist?"


show lilly basic_displeased_close onlayer master
with charachange

li "Klassensprecher zu sein ist schön, und mit der Verantwortung kann ich gut genug umgehen. Es ist nur, dass die Leute, mit denen man zu tun hat, manchmal…"



"Sie verstummt langsam, wobei sie den Satz an einer günstigen Stelle abbricht. Es ist schwer, sich vorzustellen, wie Lilly flucht, aber ich nehme an, wenn irgendjemand sie dazu bringen könnte, dann wäre es Shizune."


show hanako cover_worry_close onlayer master
with charachange

"Hanako scheint die Aussicht auf so einen Streit ein bisschen mitzunehmen, aber bevor ich das Thema ein wenig davon abbringen kann, steht sie auf."


show hanako basic_worry_close onlayer master at tworight
with dissolvecharamove

show lilly basic_surprised_close onlayer master
with charachange

li "Hanako?"


show hanako defarms_strain_close onlayer master
with charachange

ha "Ich… bin gleich wieder da."


hide hanako onlayer master
with charaexit

"Mit diesen Worten geht sie in Richtung Toilette. Ich schätze, das ist eine Art, mit der Situation umzugehen, falls das wirklich ihre Absicht war."


show bg suburb_shanghaiint onlayer master at center
show lilly basic_concerned_close onlayer master at Position(xpos=0.5)
with dissolvecharamove

"Lilly sieht jedoch ein bisschen verletzt aus."


hi "Mach dir darüber keine Sorgen. Ich glaube nicht, dass es deinetwegen war."


show lilly basic_oops_close onlayer master
with charachange

li "Aber…"


hi "Ich glaube, sie ist in letzter Zeit stärker geworden. Das hast du selbst gesehen… oder…?"


"Das war jetzt unglücklich ausgedrückt. Zum Glück wirkt Lilly nicht beleidigt, und mittlerweile sollte ich wirklich nicht mehr so viel Angst davor haben, in ihrer Nähe in dieses Fettnäpfchen zu treten."


show lilly basic_sleepy_close onlayer master
with charachange

li "Möglich. Manchmal… ist das schwer zu sagen."


"Einen Moment lang herrscht Stille, bevor zwei Teetassen, ein Kuchen und eine Tasse mit dampfend heißem Kaffee vor uns auftauchen."


show bg suburb_shanghaiint onlayer master at right
show lilly basic_sleepy_close onlayer master at Position(xpos=0.3)
with charamove

show yuukoshang closedhappy_down onlayer master at tworight
with charaenter

"Mir fällt auf, dass Yuuko besonders darauf achtet, die Teetasse mit Kontakt zu Lillys Fingerspitzen hinzustellen, sodass sie weiß, wo sie steht."


show yuukoshang closedhappy_up onlayer master
with charachange

yu "Bitte sehr."


hi "Danke, Yuuko."


show lilly basic_weaksmile_close onlayer master
with charachange

li "Danke."


hide yuukoshang onlayer master
with charaexit

"Nach einer schnellen und leisen Verbeugung verschwindet die brillentragende Bedienung."


show bg suburb_shanghaiint onlayer master at center
show lilly basic_weaksmile_close onlayer master at Position(xpos=0.5)
with charamove

li "Ah ja, genau. Ich wollte dich etwas fragen, und jetzt wäre der richtige Moment dafür."


hi "Ich bin ganz Ohr."


show lilly basic_smileclosed_close onlayer master
with charachange

li "Hanako hat bald Geburtstag, und ich habe gehofft, du würdest mich vielleicht dieses Wochenende in die Stadt begleiten, um ein Geschenk zu kaufen."


"Hanako hat bald Geburtstag? Ich nehme an, das wäre eine gute Möglichkeit, sie ein wenig aufzuheitern."
"Genau wie Yuuko scheint sie immer auf der Schwelle zu entweder Panik oder Depression zu stehen – und mit Ausnahme unserer Schachpartien habe ich noch nie gesehen, dass ihr etwas wirklich Spaß macht."


"Davon abgesehen hört es sich ganz gut an, das Wochenende damit zu verbringen, mit einer Freundin die Stadt besser kennenzulernen."


hi "Klar, würde ich gerne. Hast du irgendwelche Pläne, was du für ihren Geburtstag machen willst? Eine Party oder so?"


show lilly basic_weaksmile_close onlayer master
with charachange

li "Da Hanako nun mal Hanako ist, wäre vielleicht etwas im kleinen Rahmen-"


show lilly basic_listen_close onlayer master
with charachange

"Lilly unterbricht sich plötzlich selbst, und ich wundere mich warum, als sie ihre Tasse an ihre Lippen führt und trinkt."


"Ein paar Sekunden darauf kann ich über ihre Schulter hinweg sehen, wie Hanako zurückkommt. Lillys Gehör muss wirklich sehr gut sein, wenn es das Geräusch der Toilettentür war, das sie gewarnt hat."


show bg suburb_shanghaiint onlayer master at bgleft
show lilly basic_listen_close onlayer master at Position(xpos=0.3)
with charamove

show hanako basic_normal_close onlayer master:
    tworight
    easein 1.0 ypos 1.09
with charaenter

"Hanako nimmt erneut Platz und fängt sofort an, ihren Tee zu trinken. Bald essen und trinken wir drei in Ruhe, während die Sonne untergeht."


"Es ist eine schöne Art, den Rest des Abends zu verbringen, und es bringt mich dazu, die leise und ruhige Umgebung der Yamaku zu schätzen. Ich glaube, ich beginne wirklich, das Leben hier zu mögen, so abgeschieden es auch sein mag."


stop ambient fadeout 2.0

scene bg suburb_shanghaiint onlayer master at bgleft
show lilly basic_smileclosed_close onlayer master:
    twoleft
    ypos 1.1
show hanako basic_smile_close onlayer master:
    tworight
    ypos 1.09
with shorttimeskip

"Ich trinke den letzten Rest meines Kaffees und stelle die Tasse auf dem Tisch ab, während die Mädchen sich unterhalten."
"Der Kaffee hier ist ein bisschen bitter für meinen Geschmack, aber immer noch ziemlich gut. Auf alle Fälle besser als der, den ich selbst machen kann."


"Die Unterhaltung der Mädchen dreht sich hauptsächlich um ihre jeweiligen Lesevorlieben, was mich ein bisschen auf ein ähnliches Thema neugierig macht."


hi "Hey Hanako, ich hab mich gerade gefragt… abgesehen von Schach und Lesen – hast du irgendwelche Hobbys oder gibt es etwas, was du gerne machst?"


show hanako emb_timid_close onlayer master
with charachange

"Sie wird sofort stumm und wirkt völlig überrascht. Sie kann kaum glauben, dass irgendjemand daran Interesse hat, ihr eine solche Frage zu stellen. Sie braucht ein bisschen Zeit, um eine Antwort zu formulieren."


show hanako emb_downsmile_close onlayer master
with charachange

ha "Ähm… Ich glaube… ich singe auch ganz gerne. Ich kann auch ganz gut mit Computern umgehen, aber ich… benutze sie nicht so oft."


"Singen ist nicht gerade, was ich erwartet hatte. Es fällt mir schwer, mir ihre Gesangsstimme vorzustellen, wenn man bedenkt, wie leise sie spricht. "


show lilly basic_smile_close onlayer master
with charachange

"Lilly hingegen nickt einfach nur. Sie weiß das wohl schon alles, da sie schon seit einem Jahr oder so mit Hanako befreundet ist."


show hanako cover_bashful_close onlayer master
with charachange

ha "W-Was ist mit… d-d…"


hi "Mir?"


show hanako basic_bashful_close onlayer master
with charachange

"Sie zögert, bevor sie rasch ihren Kopf auf und ab schnellen lässt. Logisch, dass ich von meinen Hobbys sprechen soll, nachdem sie mir von ihren erzählt hat."


hi "Da wäre Schach, offensichtlich, aber auch… hmm…"


hi "Fußball war da auch noch, aber das kann ich nicht mehr wirklich machen. Im Krankenhaus habe ich mit Lesen angefangen… ähm…"


show hanako basic_normal_close onlayer master
show lilly basic_sleepy_close onlayer master
with charachange

"Das fällt überraschend schwer. Lilly und Hanako sehen bei der Richtung, in die das Ganze läuft, ein bisschen abgeschreckt aus, und je mehr ich darüber nachdenke, desto mehr bin ich es auch."


show lilly basic_weaksmile_close onlayer master
with charachange

li "Hört sich so an, als hättest du seit deinem Unfall einige neue Sachen für dich entdeckt."


"Typisch Lilly. Das ist wohl die positivste Seite, die man dem, was ich gesagt habe, abgewinnen konnte, ohne unaufrichtig zu klingen. Hanako schweigt allerdings."


"Sobald eine Situation schwierig wird, flüchtet sie sich offenbar immer in Schweigen, um nicht alles noch schlimmer zu machen. Entweder das, oder sie flüchtet buchstäblich."


$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_phone

show lilly basic_surprised_close onlayer master
show hanako cover_worry_close onlayer master
with charachange

"Ein leises Klingeln unterbricht uns. Als Lilly in ihre Tasche greift, wird klar, dass es von ihrem Handy kommt."


show lilly basic_weaksmile_close onlayer master
with charachange

li "Entschuldigung…"


show hanako basic_normal_close onlayer master
with charachange

ha "S-Schon okay…"


show lilly invis_close onlayer master at Position(ypos=1.0)
with dissolvecharamove

hide lilly onlayer master
with None

"Lilly nickt kurz, bevor sie von ihrem Platz rutscht und den Anruf ein bisschen weiter entfernt entgegennimmt, um uns zwei nicht zu stören."


hi "Muss schön sein, beliebt zu sein."


show hanako cover_bashful_close onlayer master
with charachange

"Hanako lächelt, aber sie nimmt meinen Köder für ein neues Gesprächsthema nicht auf."


$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene black onlayer master
with shuteye

"Letztendlich lehne ich mich einfach zurück, schließe meine Augen und entspanne mich, so gut ich kann."


hi "Es ist schön ruhig hier. Ich frage mich, wie es wohl gewesen wäre, an einem Ort wie diesem aufzuwachsen anstatt in der Stadt."


ha "D-Du kommst aus der Stadt?"


"Sieht so aus, als hätte ich etwas gefunden, worüber sie reden will."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg suburb_shanghaiint onlayer master at center
show hanako basic_smile_close onlayer master:
    center
    ypos 1.09
with openeye

hi "Ja. Man könnte sagen, ich war durch und durch ein Großstadtkind."


show hanako basic_worry_close onlayer master
with charachange

ha "H-Hört sich an, als hätte sich vieles verändert…"


hi "Hat es. Ich bin mir aber noch nicht ganz sicher, was ich von dem Ganzen halten soll. Es ist ein kleiner Kulturschock – auf mehr als eine Art."


hi "Du musst so etwas auch erlebt haben, als du zum ersten Mal an die Yamaku gekommen bist, stimmt's? Ich könnte mir vorstellen, dass das den meisten neuen Schülern passiert."


show hanako basic_distant_close onlayer master
with charachange

ha "N-Nicht wirklich…"


"Hanakos Blick richtet sich ein wenig zur Seite, so als wollte sie nicht weiterreden. Neugierig neige ich meinen Kopf zur Seite, aber es verstreichen ein paar Sekunden ohne eine Antwort."


scene bg suburb_shanghaiint onlayer master at bgright
show hanako basic_distant_close onlayer master:
    tworight
    ypos 1.09
with charamove

show lilly back_pout onlayer master at twoleft
with charaenter

stop music fadeout 8.0

li "Aber können wir uns darum nicht am Montag kümmern? Die Konsequenzen haben sich schon kaum vom letzten…"


show lilly back_listen onlayer master
with charachange

li "Ich verstehe. Ich versuche, sie davon abzubringen. Du weißt, wie sie ist, wenn sie sich etwas in den Kopf gesetzt hat."


li "Ja, danke. Ich melde mich dann später bei dir. Auf Wiederhören."


show lilly basic_displeased onlayer master
with charachange

"Lillys Telefonat endet mit dem Geräusch ihres zuklappenden Handys. Sie kommt zu unserem Tisch zurück, setzt sich aber nicht."


hi "Musst du gehen?"


show lilly basic_concerned onlayer master
with charachange

li "Leider. Die Klassensprecher-Pflichten rufen wieder einmal."


show hanako cover_worry_close onlayer master
with charachange

ha "I-Ich kann mit dir kommen."


show lilly basic_weaksmile onlayer master
with charachange

li "Ist schon gut, Hanako. Ich gehe bloß direkt zum Schülerrat. Es ist nicht nötig, sich meinetwegen einen schönen Abend zu verderben."


show lilly basic_smile onlayer master
with charachange

li "Außerdem, wenn du mich auf meinem Weg zurück zur Schule begleitest, wer würde dann dem armen Hisao Gesellschaft leisten?"


show hanako basic_normal_close onlayer master
with charachange

ha "Okay…"


show lilly basic_weaksmile onlayer master
with charachange

li "Ich kann heute Abend zum Tee wieder zu euch stoßen, wenn ihr wollt. Den werde ich vielleicht brauchen."


show lilly cane_weaksmile onlayer master
with charachange

"Wir einigen uns auf diesen Plan. Hanako überreicht Lilly ihren Gehstock, und Lilly verabschiedet sich von uns beiden."


hide lilly onlayer master
with charaexit

"Trotz meines Angebots, für Lilly zu bezahlen, besteht sie darauf, uns ihren Anteil an der Rechnung zu geben und bittet uns, Yuuko von ihr zu grüßen."


play music music_dreamy fadein 4.0

show bg suburb_shanghaiint onlayer master at center
show hanako basic_normal_close onlayer master:
    center
    ypos 1.09
with charamove

"Und dann… sind wir allein. Es mag ja schön und gut sein, mich und Hanako allein zu lassen, damit wir ein bisschen Zeit zusammen haben, aber das bedeutet üblicherweise bloß, dass wir für eine Weile schweigend nebeneinander sitzen."


"Ich frage mich, wie ich auf Hanako wohl wirke."
"Ich habe mich selbst nie als furchteinflößend gesehen, aber wenn jemand in meinem Alter sich in meiner Nähe so benimmt, macht mich das sehr selbstkritisch. Als ob es meine Schuld wäre, dass sie so beunruhigt ist."


"Sie würde sich vielleicht mehr an Menschen gewöhnen, wenn sie aufhören würde, sich in der Schule so abzusondern, aber andererseits…"
"Wenn sogar Menschen, die viel älter sind als sie, eine so starke Reaktion zeigen, nachdem sie einen einzigen Blick auf ihr Gesicht geworfen haben, fühlt sie sich vielleicht genauso wie ich jetzt."


"Es ist ein wahrer Teufelskreis."
"Wenn sie an der Yamaku bleibt, wird sie sich nicht daran gewöhnen, unter Leute zu kommen, aber wenn sie die Schule verlässt, wird vielleicht jede ihrer Anstrengungen von Leuten zunichte gemacht, die nicht mit ihren Narben umgehen können."


hi "Sollen wir noch etwas bestellen? Immerhin hatten wir kein richtiges Abendessen."


show hanako basic_smile_close onlayer master
with charachange

"Das heitert Hanako auf, und sie nickt energisch, froh darüber, dass ich das Thema für sie angesprochen habe. Ich erhasche Yuukos Blick, worauf sie pflichtbewusst herüber kommt, um unsere Bestellung aufzunehmen."


scene bg suburb_shanghaiint onlayer master at bgright
show hanako basic_smile_close onlayer master:
    tworight
    ypos 1.09
with charamove

show yuukoshang neutral_down onlayer master at twoleft
with charaenter

yu "Wollt ihr noch etwas?"


hi "Ich nehme bloß das Spezial-Sandwich und eine heiße Schokolade. Für Kaffee ist es jetzt ein bisschen spät. Hanako?"


show hanako cover_bashful_close onlayer master
with charachange

ha "I-Ich… nehme dasselbe…"


hide yuukoshang onlayer master
with charaexit

"Nach einem Nicken und einer Verbeugung dreht sich Yuuko um und kehrt hinter den Tresen zurück, wo sie sich daran macht, Brot und Zutaten herauszusuchen und die Maschine zu bedienen, um unsere Getränke zu machen."


show yuukoshang smile_up onlayer master at twoleft
show hanako basic_bashful_close onlayer master
with charaenter

"Wir sprechen kein Wort, bis Yuuko zurückkommt. Sie lächelt und gibt uns unser Essen und unsere Getränke, bevor sie zu einem Gast geht, der nach ihr gerufen hat."


hide yuukoshang onlayer master
with charaexit

show bg suburb_shanghaiint onlayer master at center
show hanako basic_bashful_close onlayer master:
    center
    ypos 1.09
with dissolvecharamove

"Ich gebe auf, eine richtige Unterhaltung von meiner Begleiterin zu erwarten, und beschließe, einfach nur das Essen zu genießen, so wenig es auch sein mag."


"Es schmeckt gut, so wie die meisten Gerichte hier. Nach ein paar Bissen bemerke ich, dass etwas fehlt. Und zwar die Essensgeräusche von Hanako."


show hanako basic_distant_close onlayer master
with charachange

"Als ich sie wieder anschaue, sehe ich, wie sie hinter ihrem unberührten Sandwich herumzappelt."


hi "Keinen Hunger?"


show hanako cover_worry_close onlayer master
with charachange

"Sie schüttelt ihren Kopf. Sogar als sie das macht, leistet die Haarsträhne, die sie über der rechten Seite ihres Gesichts trägt, ganze Arbeit und versteckt diese fast komplett."


ha "D-Das ist es nicht."


hi "Och. Ich war schon bereit, deine Portion auch zu essen."


show hanako basic_worry_close onlayer master
with charachange

ha "Du hast… bedrückt gewirkt. I-Ist… irgendwas?"


"Es überrascht mich, dass sie glaubt, ich wäre derjenige, der besorgt aussieht, aber wenn ich noch mal darüber nachdenke, hat sie vermutlich Recht."
"Auf meinem Gesicht haben sich vielleicht meine Gefühle gezeigt, ohne dass ich es gemerkt habe, und sie ist nicht gerade schwer von Begriff – ganz im Gegenteil."


hi "Wir sind Freunde, oder?"


show hanako emb_downsad_close onlayer master
with charachange

ha "Freunde…"


"Ihrer Stimmlage und ihrer zusammenschrumpfenden Haltung nach zu urteilen, scheint es so, als hätte ich noch ein weiteres Fettnäpfchen erwischt."


"Das ist noch ein Grund, warum es so schwer ist, mit ihr umzugehen; die psychologischen Barrieren, die sie zwischen sich selbst und anderen aufbaut. Dabei sind ich und höchstwahrscheinlich sogar Lilly eingeschlossen."


show hanako basic_bashful_close onlayer master
with charachange

ha "I-Ich finde, das sind wir…"



"Auf Hanakos ehrliche Antwort bin ich nicht gefasst, noch dazu, weil ich schon fast die Hoffnung aufgegeben hatte, überhaupt eine Antwort zu bekommen."


hi "Aha…"


show hanako basic_worry_close onlayer master
with charachange

ha "Liege ich falsch? T-Tut mir leid, i-ich…"


hi "Nein, es ist nur… es ist beruhigend, dass du mir zustimmst."


hi "Um aufzugreifen, was du vorher gesagt hast: Seit ich auf die Yamaku gekommen bin, bin ich etwas unsicher, wie ich mich anderen gegenüber verhalten soll."


"Ich muss ein bisschen schmunzeln. Es ist überraschend, was für eine Erleichterung das war. Ich spüre, wie ich anfange zu lächeln, während ich meine Tasse heiße Schokolade nehme und sie an meine Lippen setze."


hi "Au! Das ist heiß…"


show hanako emb_downsmile_close onlayer master
with charachange

ha "D-Darum…"


show hanako emb_smile_close onlayer master
with charachange

ha "Darum hab ich noch nicht gegessen. I-Ich hab gewartet… dass meine heiße Schokolade zuerst abkühlt."


hi "Dann warte ich wohl."


"Wir beide kichern ein bisschen. Die Situation ist eigentlich nicht so lustig, aber aus irgendeinem Grund… fühlt es sich so an, als wäre es die natürlichste Sache der Welt, jetzt zu lachen."


"Ich schätze, wir waren beide ein bisschen angespannt. Ich war so damit beschäftigt zu glauben, dass Hanako ein Problem hat, dass sie mich daran erinnern musste, dass ich auch unsicher war."


"Aber wie dem auch sei… Es ist doch ganz nett. Es ist ganz nett, jemanden zu haben, der auf seine eigene Art so an mich denkt."


$ renpy.music.set_volume(1.0, 0.0, channel="sound")
stop music fadeout 8.0

scene bg school_dormext_full_ni onlayer master
with shorttimeskip

"Nach einem langen, schweigsamen Marsch den Hügel hinauf und auf das Schulgelände, stehen wir zwischen den beiden Wohnheimen."


"Nachtwächter patrouillieren regelmäßig zwischen den Wohnheimen für Jungs und Mädchen, sowohl zur Sicherheit als auch um bei medizinischen Notfällen schnell Alarm schlagen zu können."
"Der diensthabende Nachtwächter bemerkt uns, nickt kurz und patrouilliert dann weiter."


show hanako emb_downtimid_ni onlayer master at center
with charaenter

"Ein lautes Gähnen entfährt Hanako, bevor sie sich die Hand vorhalten kann. Ich bin mir recht sicher, dass sie mittlerweile ziemlich müde ist."


hi "Ich sollte dann besser auf mein Zimmer gehen. Bis morgen, Hanako."


show hanako emb_smile_ni onlayer master
with charachange

ha "G-Gute Nacht…"


hide hanako onlayer master
with charaexit

"Wir trennen uns und gehen in unterschiedliche Richtungen, ehe ich mich umdrehe und zurückschaue."


show hanako basic_smile_ni onlayer master
with charaenter

"Dort steht Hanako und winkt mir mit einem Lächeln im Gesicht zu. Ich lächle und winke zurück. Nach ein paar Sekunden dreht sie sich um, geht die Stufen zum Wohnheim hoch und verschwindet durch die Tür."


hide hanako onlayer master
with charaexit

"Diese kleinen Momente, die wir miteinander teilen, fühlen sich an wie ein kleiner Schatz. Eins ist sicher; ich will dieses kleine, zarte Lächeln, das sie so selten in der Gesellschaft von so wenigen Menschen aufsetzt, beschützen."


"Ich denke über diese Gefühle nach, die ich in Hanakos Nähe habe, und über die Gelegenheiten, bei denen ich etwas für sie tun kann… Ob sie vielleicht der Anfang von etwas Tieferem sind als das, was wir jetzt zusammen haben."


scene black onlayer master
with dissolve



label de_H12:

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play music music_happiness fadein 2.0

scene bg school_track onlayer master
with locationchange

"Die Sommersonne heute ist fast schon einmalig, doch zusammen mit der sauberen Landluft ist sie umso besser."


"Die Mitglieder des Leichtathletikklubs blödeln auf dem Sportplatz vor mir herum; manche spielen Fußball, andere unterhalten sich, und ein paar lachen, als zwei von ihnen so tun, als würden sie miteinander raufen."


"Keiner von ihnen schenkt mir Beachtung, während ich unter dem Schatten eines besonders großen Baums allein im Gras sitze. Es ist ein schöner und friedlicher Moment nach einem trostlosen Schultag."


play ambient sfx_footsteps_soft fadein 4.0

"Ich habe vor meiner Herzattacke ziemlich oft Fußball gespielt, darum dachte ich mir, ich könnte in Nostalgie schwelgen, wenn ich ihnen zuschaue. Was ich jetzt allerdings fühle, ist weit davon entfernt."


stop ambient fadeout 0.3

show miki smile onlayer master:
    center
    easein 1.0 ypos 1.12
with charaenter

"Ich kann hinter mir Schritte näherkommen hören, und als ich mich zur Seite drehe, setzt sich eine meiner Klassenkameradinnen neben mich."
"Ich bin überrascht, weil wir zwei bis jetzt nicht viel miteinander geredet haben, und ich dachte nicht, dass mich hier irgendjemand bemerken würde."


show miki grinclosed onlayer master:
    center
    ypos 1.12
with charachange

mk "Was geht?"


hi "Hi. Miura, richtig?"


show miki wink onlayer master
with charachange

mk "Nenn mich einfach Miki. Nachnamen sind zu spießig."


hi "Okay. Hisao."


show miki smile onlayer master
with charachange

"Wir schauen beide wieder auf den Sportplatz, wo das Spiel abläuft. Sieht so aus, als würden sie sich bereit machen, eine zweite Runde zu spielen, da sich alle auf ihre Positionen verteilen und der Ball in die Mitte des Feldes getragen wird."


"Und tatsächlich kommt der Pfiff, der die Partie startet, und sie sind gleich wieder voll dabei."


hi "Willst du nicht spielen?"


show miki grinclosed onlayer master
with charachange

mk "Nee, ich ruhe mich nur ein bisschen aus."


show miki wink onlayer master
with charachange

mk "Was ist mit dir? Du hast schon irgendwie ausgesehen, als wolltest du spielen, als du uns vorhin beobachtet hast."


"Also hat mich doch jemand bemerkt."


hi "Ist 'ne lange Geschichte."


show miki grin onlayer master
with charachange

"Ich kann in ihrem Gesicht lesen, dass ich sie neugierig gemacht habe."


hi "Ich bin auf dieser Schule, weil ich herzkrank bin. Ich kann nicht mehr wirklich Fußball spielen."


show miki smile onlayer master
with charachange

mk "Wolltest ein Fußballer werden, was?"


hi "Nein, ich hab's eigentlich bloß zum Spaß gemacht. Meine Freunde haben gespielt, also hab ich auch gespielt."


hi "Vor meinem Unfall hätte jeder von denen, die dort spielen, ich sein können. Aber irgendwie hab ich auch gar nicht das Verlangen, wieder damit anzufangen. Ist ein bisschen schwer, das zu erklären."


"Ich bin durch die Zeit, in der ich gespielt habe, immer noch recht fit, auch wenn ich mittlerweile nicht mehr so stark bin. Außerdem bin ich mit den anderen Klubmitgliedern gut ausgekommen."


"Wenn ich so darüber nachdenke, sollte ich echt ein blödes Gefühl dabei haben, jemanden beim Spielen zu beobachten, wenn ich es nicht mehr kann. Trotzdem ist es nicht so."
"Vielleicht ist das ja gut: Es zeigt, dass ich darüber hinweg bin und dass ich bereit bin, ein neuer Mensch zu werden."


hi "Tut mir leid, ich schweife ab."


show miki grinclosed onlayer master
with charachange

mk "Schon okay. Ich bin sogar froh, das zu hören."


show miki smile onlayer master
with charachange

mk "Hört sich an, als wäre bei dir wirklich alles in Ordnung. Manche, die auf die Yamaku kommen, sind anfangs ziemlich verkorkst."


hi "Du bist dann also im Leichtathletikklub?"


show miki grin onlayer master
with charachange

mk "Jupp. Schon seit ich hier angekommen bin."


hi "Du bist nicht zufällig mit Emi befreundet? Klein, schnelle Läuferin, keine Beine? Ich glaube, es gibt nicht allzu viele Mädchen im Leichtathletikteam."


show miki grinclosed onlayer master
with charachange

mk "Haha, Emi. Jeder kennt sie, was?"


show miki smile onlayer master
with charachange

mk "Aber ne. Ich komme irgendwie besser mit Jungs zurecht, daher reden Emi und ich nicht wirklich viel. Wie auch immer, was ist mit dir?"


hi "Ah, na ja, ich bin eigentlich in keinen Klubs – jedenfalls in keinen richtigen."


show miki wink onlayer master
with charachange

mk "Du bist aber oft mit Hanako und dieser blonden Amazone zusammen, oder?"


"Blonde Amazone… Ich schätze, Lilly hat zumindest die passende Größe, wenn die Beschreibung auch ansonsten ziemlich unpassend ist. Ich nicke, ohne weiter darauf einzugehen."


show miki grinclosed onlayer master
with charachange

mk "Dann mach dir keine Sorgen darüber. Solange du ein paar Freunde hast, musst du keinem Klub beitreten."


"Ein lauter Pfiff vom Spielfeld erregt unsere Aufmerksamkeit. Einer der Spieler liegt am Boden und umklammert sein Bein. Die anderen hören auf zu spielen und laufen langsam zu ihm hin, während Miki das Gesicht verzieht."


show miki serious onlayer master
with charachange

mk "Autsch, das sieht schmerzhaft aus. Der Typ hat echt Pech."


"Während sie weiterhin aufs Spielfeld schaut, muss ich an ihre eigenen Verletzungen denken. Ihr linker Arm, der eher in einem Stumpf als einer Hand endet, ist schon seit ich auf der Yamaku bin bandagiert, und ihre Verletzung sieht schon älter aus."


"Sie wendet sich wieder mir zu und erwischt mich dabei, wie ich ihren Arm anstarre. Eine peinliche Stille breitet sich aus. Dabei legt sie ihren bandagierten Arm in ihren Schoß und hält ihn mit ihrer verbliebenen Hand fest."


hi "T-Tut mir leid. Ich schätze, ich bin immer noch ein bisschen…"


show miki smile onlayer master
with charachange

mk "Ist schon okay. Wirklich."


"Sie klingt unbekümmert, aber keiner von uns sagt danach etwas."
"Jeder behinderte Schüler hier hat seine eigene Art, mit seinen Problemen umzugehen, und dass manche ihren Zustand als lästig empfinden, ist nur allzu natürlich. Immerhin gehöre ich auch zu denen."


"Der Verletzte vom Fußballmatch schafft es mit ein bisschen Hilfe, wieder auf die Beine zu kommen, und humpelt vom Spielfeld, wobei er einen Arm über die Schulter eines Mitspielers gelegt hat, um sich zu stützen."
"Hat sich wahrscheinlich nur einen Muskel gezerrt, wenn er noch laufen kann."


"Es ertönt wieder ein Pfiff und das Spiel geht mit einem Mann weniger auf dem Feld weiter."


show miki whistle onlayer master
with charachange

mk "Sich mit Hanako und der Blonden rumzutreiben… Du bist mit ziemlich seltsamen Leuten unterwegs."


hi "Wieso?"


show miki serious onlayer master
with charachange

mk "Es ist nur, dass Hanako irgendwie… Ich weiß nicht."


hi "Schüchtern ist?"


mk "Nein, das meine ich eigentlich nicht. Es ist nur… dass sie ein paar Probleme hat, glaube ich. Ich kann es nicht wirklich schön ausdrücken."


show miki wink onlayer master
with charachange

mk "Nicht, dass ich sie nicht für ein nettes Mädchen halten würde… Sie ist total nett."


show miki serious onlayer master
with charachange

mk "Es ist nur… schwer, mit ihr umzugehen."


"Hört sich so an, als hätte Miki – oder zumindest ein paar andere aus der Klasse – früher schon versucht, Hanako näherzukommen. Und dass es nicht gut gelaufen ist."


"Ich finde ihr Urteil recht hart, wenn man bedenkt, dass alle – nicht nur Leute an dieser Schule – ihre eigenen Probleme haben."
"Andererseits kenne ich Hanako noch nicht so lange, darum würde es mich nicht überraschen, wenn da etwas wäre, worüber ich nicht Bescheid weiß."


hi "Ich nehme es einfach, wie es kommt. Sie ist ein netter Mensch, und ich denke, das sollte alles sein, was zählt."


"Miki kneift die Augen ein bisschen zusammen, und ihr Lächeln wird breiter."


show miki grin onlayer master
with charachange

mk "Du magst sie ziemlich gern, was?"


label de_choiceH12:
menu:
    with menueffect
    "Miki nimmt definitiv kein Blatt vor den Mund."
    "Gib es zu.":




        return m1
    "Leugne es.":


        return m2


label de_H12a:

hi "Um ganz ehrlich zu sein… Ja, ich mag sie. Ich fände es nett, wenn du es niemandem erzählst."


show miki wink onlayer master
with charachange

mk "Hey, whoa, du kannst mir vertrauen. Keine Sorge."


show miki grinclosed onlayer master
with charachange

mk "Ehrlich gesagt finde ich das irgendwie süß. Wenn du's versuchen willst, lass dich nicht von mir aufhalten."


hi "Danke."


"Das sagt sie vielleicht, aber sie hat gerade davon gesprochen, dass Hanako „Probleme” hat. Ich will mich an meine Worte halten. Hanakos Probleme spielen keine Rolle; ich werde mit allem fertig, was kommt, weil ich ihr helfen will."


"Falls es nur die geringste Chance gibt, Hanako aus ihrer Depression und Einsamkeit herauszuholen, dann sollte ich darauf hinarbeiten, egal was kommt. Wenn sie einen Prinzen braucht, dann werde ich dieser Prinz sein."


"Als ich an eine mögliche Beziehung denke, kann ich sehen, wie Miki mich angrinst, während sie mein Gesicht beobachtet. Es besteht kein Zweifel daran, dass ich rot bin, und den Blick von ihr abzuwenden, bringt sie nur zum Lachen."



label de_H12b:

hi "Ich glaube nicht. Wir sind nur Freunde."


show miki serious onlayer master
with charachange

mk "Ohh. Ich dachte einen Moment lang, ich hätte da etwas Schnuckeliges entdeckt. Ich verstehe; Mädchen und Jungs können wohl doch einfach nur Freunde sein."


"Was sie sagt, stimmt, auch wenn ich für Hanako Gefühle habe. Im Moment sind wir gute Freunde, und ich will das nicht kaputt machen, aber ich will auch mehr als das für sie sein. Es ist schwierig."



label de_H12c:

"Miki wirkt anders als die anderen Mädchen. Mit ihr zu reden, fühlt sich eher so an, als würde man mit einem Jungen reden als mit einem Mädchen."
"Dass sie sagt, sie würde männliche Gesellschaft bevorzugen, hilft auch nicht, diesen Eindruck zu vertreiben."


"Ein Blick auf meine Uhr verrät mir, dass die Mittagspause in ein paar Minuten vorbei ist. Zeit, sich auf den Weg zurück zum Klassenzimmer zu machen."


hi "Die Mittagspause ist gleich um. Sollen wir zurückgehen?"


show miki smile onlayer master
with charachange

mk "Ja, das sollten wir."


show miki smile onlayer master at center
with charamove

"Ich rappele mich vom Gras auf, klopfe mir den Staub ab und biete Miki eine Hand an, um ihr auch aufzuhelfen. Sie greift zu und zieht sich mühelos hoch, wobei man sehen kann, wie sich die Muskeln ihrer straffen, nackten Arme bewegen."


hi "Was ich noch fragen wollte, warum trägst du nicht die normale Mädchenbluse?"


show miki whistle onlayer master
with charachange

mk "Äh, die ist zu heiß und einengend. Die Uniform der Jungs ist sowieso viel besser."


"Sie wedelt ein bisschen mit ihren Armen herum, um ihr Argument zu unterstreichen, was den Nebeneffekt hat, dass sie einen bestimmten Teil ihres Körpers zeigt, der von der Bluse besonders eingeengt wäre."


scene bg school_gardens onlayer master
with locationchange

"Während wir uns durch die Gärten auf den Weg zurück zum Hauptgebäude machen, reden wir noch etwas miteinander."


show miki smile onlayer master at center
with charaenter

mk "Hört sich an, als würdest du dich gut einleben. Das freut mich. Es war eine ziemliche Überraschung, dass so spät im Jahr noch jemand zu uns wechselt – immerhin sind schon bald die Prüfungen."


hi "Erinnere mich nicht daran…"


show miki grinclosed onlayer master
with charachange

mk "Haha, mach dir über die keinen Kopf. Pauke einfach dafür, und alles wird gut."


hi "Das hört sich nicht nach einem guten Ratschlag an."


show miki grin onlayer master
with charachange

"Sie klopft ein paar Mal auf meine Schulter und grinst dabei. Ich glaube, sie nimmt die Schule nicht allzu ernst."


show miki wink onlayer master
with charachange

mk "Du siehst aus wie ein schlauer Kerl, und Mutou hat schon richtig Gefallen an dir gefunden. Ihr seid wie ein Herz und eine Seele."


hi "Jetzt muss ich nur noch herausfinden, ob das gut oder schlecht ist."


hi "Ich weiß immer noch nicht, was ich von dieser Schule halten soll. Ich bin schon seit einigen Wochen hier, aber ich fühle mich manchmal immer noch benommen."


show miki smile onlayer master
with charachange

mk "Du wirst dich schon daran gewöhnen, lass dir einfach ein wenig Zeit. Es ist nur eine Oberschule, so wie jede andere auch."


"Bei ihr hört sich das so einfach an, aber so habe ich es noch nie gesehen."
"Für mich symbolisierte diese Schule eine deutliche Veränderung in meinem Leben. Ich war nicht länger normal; ich war „anders”, und sollte mit anderen, die „anders” sind, unterrichtet werden."


"Und doch gehe ich zurück zum Unterricht und rede während der Mittagspause ganz beiläufig mit einer Klassenkameradin, nachdem ich ein paar anderen beim Fußballspielen zugesehen habe – alles ganz normal. Vielleicht hat sie Recht."


"Vielleicht sollte ich Hanako genauso sehen. Jeder hat seine eigenen Probleme; das ist wohl kaum etwas, das auf die Yamaku beschränkt ist. Schließlich ist es nur eine Oberschule, so wie jede andere auch."


"Als wir weiterreden, merke ich, dass ich lächle. Miki und ich sind in fast allen Belangen völlig unterschiedlich, aber es fühlt sich gut an, einen weiteren Klassenkameraden ein wenig besser kennengelernt zu haben."


stop music fadeout 2.0

scene black onlayer master
with dissolve



label de_H13:

play music music_daily fadein 2.0
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg misc_sky onlayer master
with locationchange

"Eine leichte Brise bläst mir den Duft des Frühsommers um die Nase, während ich auf Lilly warte."


"Kleine weiße Wolken durchbrechen die eintönige Färbung des blauen Himmels."


li "Hisao? Bist du hier?"


"Lillys Stimme weht auf der Brise mit, als wären sie ein und dasselbe."


"Ich unterbreche meinen Blick in den Himmel, um Lilly anzuschauen."


$ renpy.music.set_volume(0.8, 1.0, channel="ambient")

scene bg school_gate onlayer master
show lilly cane_surprised_cas onlayer master at center
with locationchange

"Mit einem pfirsichfarbenen, schulterfreien Pullover und einem hellbraunen, knöchellangen Rock passend zu hellbraunen Sandalen, ist sie ein ziemlicher Blickfang."


hi "Ja, ich bin hier, Lilly. Neben dem Tor."


hi "Hast du dich von Hanako davonschleichen können?"


show lilly cane_weaksmile_cas onlayer master
with charachange

li "Ja. Es ist nicht ungewöhnlich, dass ich an den Wochenenden weggehe, darum glaube ich nicht, dass sie etwas bemerkt hat."


show lilly cane_sleepy_cas onlayer master
with charachange

li "Das, und… sie trifft sich mit jemandem."


"Lilly schürzt ihre Lippen, als ob sie vielleicht ihren Mund hätte halten sollen. Ich finde es fast ein bisschen schwer zu glauben."


hi "Hanako trifft sich mit jemandem? Echt?"


show lilly cane_weaksmile_cas onlayer master
with charachange

li "Nein, es ist nur… Hin und wieder trifft sie sich am Wochenende mit ihrer Therapeutin."


hi "Oh. Na ja. Das ergibt wohl Sinn."


show lilly cane_reminisce_cas onlayer master
with charachange

"Lilly reibt sich den Arm als wäre ihr das Thema unangenehm. Nach einem Blick in ihr beunruhigtes Gesicht suche ich schnell ein anderes Thema."


hi "Öhm…"


show lilly cane_surprised_cas onlayer master
with charachange

li "Ja?"


hi "Ich hab mich nur gefragt… Kommst du denn ganz allein in der Stadt zurecht?"


show lilly cane_listen_cas onlayer master
with charachange

"Lilly seufzt wegen meiner Betroffenheit rund um ihre Blindheit. Manchmal bin ich selbst mein schlimmster Feind."


li "Tue ich, ja. Es ist allerdings einfacher, wenn ich mit einem Freund oder meiner Schwester unterwegs bin."


"Ich frage mich, wie Lilly mit ihrer Schwester auskommt. Da ich ein Einzelkind bin, ist es schwer, sich vorzustellen, wie es wäre, Geschwister zu haben, daher bin ich ein bisschen neidisch auf sie."


hi "Okay. Nun, der Bus kommt in ein paar Minuten, also sollten uns wohl besser ranhalten."



show lilly cane_weaksmile_cas onlayer master
with charachange

li "Allerdings. Wenn wir den verpassen, müssten wir lange warten."


stop music fadeout 6.0
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_road onlayer master
with locationchange

"Und damit brechen wir zur Bushaltestelle auf dem Hügel auf. Sie ist nicht weit vom Schultor entfernt und somit ziemlich günstig gelegen."


hi "Von hier hat man einen schönen Ausblick. Da ich aus der Stadt komme, habe ich so eine Landschaft nie wirklich zu Gesicht bekommen, geschweige denn jeden Tag."


show lilly cane_smile_cas onlayer master at center
with charaenter

li "Die Gegend ist auch für mich angenehm. Sie ist ruhig und weit ab vom Lärm und den Gerüchen der Stadt."


show lilly back_listen_cas onlayer master
show lillyprop back_cane onlayer master at center
with charachange

"Lillys Kopf schnellt auf eine für sie typische Weise hoch und gibt damit zu erkennen, dass sie etwas gehört hat."


show lilly back_smile_cas onlayer master
with charachange

li "Oh, da kommt der Bus…"


"Ich schaue die Straße hinab und sehe, wie der Bus den Hügel hochrumpelt. Ihr Gehör ist ziemlich nützlich."


"Der Bus kämpft sich die Straße hinauf und braucht nicht lange, um die Bushaltestelle zu erreichen. Innerhalb einer Minute sind wir auf dem Weg in die Stadt."


stop ambient fadeout 2.0

scene bg city_street1 onlayer master
with shorttimeskip

play music music_ease fadein 2.0
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

"Als ich so in der Stadt herumlaufe, erwachen in mir starke nostalgische Gefühle. Die Gerüche, der Verkehr, die hohen Gebäude überall… Meiner Heimatstadt ziemlich ähnlich, bis auf die Hochwege."


"Es ist ein leicht komisches Gefühl, in einer Stadt so lässig herumzuschlendern, wie ich es in einem Park tun würde, nur dass Autos unter mir hinweg schießen."


"Während ich eifrig über das technische Meisterwerk in Form des erhöhten Gehsteigs nachdenke, werde ich überrascht."


show lilly cane_smileclosed_cas_close onlayer master:
    center
    xpos 0.4
    easein 1.0 xpos 0.5
with charaenter

"Ich brauche einen Augenblick, um zu bemerken, dass Lilly sich mit ihrem Arm bei mir eingehakt hat, während sie ihren Gehstock mit der anderen Hand vor sich ausstreckt."


"Ich schrecke kurz auf, aber ich kann mich soweit unter Kontrolle halten, dass Lilly es nicht bemerkt. Obwohl es nicht das erste Mal ist, dass Lilly sich auf meine Führung verlässt, hat sie sich bisher immer nur an meinem Ärmel festgehalten."


"Logisch, dass es für sie einfacher ist, sich in einer überfüllten und komplexen Gegend wie der Stadt zurechtzufinden, wenn sie sich sicher festhält, aber ich bin an solch einen Körperkontakt lange nicht so gewohnt wie Lilly."


"Als mir endlich bewusst wird, dass die Stille zwischen uns immer länger anhält, während Lilly darauf wartet, dass ich losgehe, bringe ich schnell mein Gehirn in Gang."


hi "Weißt du, es hat mich ziemlich überrascht, dass Hanako gerne singt. Hast du sie jemals singen gehört?"


show lilly cane_smile_cas_close onlayer master at center
with charachange

li "Allerdings, das habe ich. Wir waren schon mehrmals zusammen mit meiner Schwester beim Karaoke. Ich kann nicht behaupten, dass ich daran sonderlich Gefallen finde, aber die zwei mögen es."


"Vielleicht passt Karaoke doch besser zu Hanako als ich dachte. Nur sie und Leute, die sie kennt, ganz allein in einem kleinen Raum."


"Das wäre eine seltene Chance für sie, sich zu öffnen, ohne dass jemand da ist, der über sie urteilt."


hi "Vielleicht wäre es ganz nett, sie in die Stadt zu einer Karaoke-Geburtstagsparty einzuladen, wenn sie das mag."


show lilly cane_sleepy_cas_close onlayer master
with charachange

li "Hmm. Ich weiß nicht, ob sie mit der Aufregung zurechtkommen würde."


"Ich will gerade widersprechen, aber ihr Gesicht verrät mir, dass sie noch ein wenig über den Vorschlag nachdenkt. Es dauert einige Zeit, bis sie zu einem Ergebnis kommt."


show lilly cane_weaksmile_cas_close onlayer master
with charachange

li "Andererseits ist das Beste, was wir für Hanako im Moment tun können, ihr ein paar schöne Geburtstagserinnerungen zu schaffen. Sie andauernd so zu behandeln, als wäre sie nicht normal, ist keine Hilfe."


hi "Ich glaube, du hast Recht; wenn sie endlich positive Erinnerungen sammelt, kommt sie vielleicht wieder auf die Beine."


"Wenn wir ihr etwas kaufen, dass sie jeden Tag sehen kann, lenkt sie das vielleicht von ihrer Vergangenheit ab und erinnert sie daran, dass sie Freunde hat."


"Und ich denke, dass Hanako auf jeden Fall mit so etwas umgehen kann. Während der Zeit, die ich mit ihr verbracht habe, habe ich gelernt, dass sie nicht ganz so zerbrechlich ist, wie ich zuerst dachte."


hi "Wollen wir dann los? Ich kenne mich in der Gegend nicht so gut aus."


show lilly cane_smileclosed_cas_close onlayer master
with charachange

stop music fadeout 6.0

li "Also gut. Ich würde vorschlagen, dass wir zuerst etwas essen."


hi "Gegessen hab ich auch noch nicht. Hört sich nach einer guten Idee an."


show lilly cane_cheerful_cas_close onlayer master
with charachange

li "Pass auf, dass du etwas Schönes aussuchst, Hisao."


"Sie lächelt neckisch, was mich reflexartig mit einem Lächeln antworten lässt, auch wenn sie es nicht sehen kann."


hi "Das mache ich, keine Sorge."


stop ambient fadeout 1.0
play music music_another fadein 4.0
scene bg city_karaokeint onlayer master
with locationskip

"Sobald wir drin sind, bestelle ich zwei Stück Kuchen und Tee dazu und bringe es zurück an unseren Tisch."


show lilly basic_smileclosed_cas_close onlayer master:
    center
    ypos 1.1
with charaenter

"Ich denke, das Café sollte Lilly gefallen – klein und ruhig, aber gut gepflegt und einigermaßen vornehm. Ihrem feinen Lächeln nach weiß ich… nicht wirklich, ob es die richtige Wahl war."


"Es ist immerhin sehr, sehr selten, dass sie nicht lächelt."


"Nichtsdestotrotz setze ich mich neben sie an einen der Ecktische und stelle unser kleines Mahl ab."


show lilly basic_planned_cas_close onlayer master
with charachange

"Lilly hebt vorsichtig ihren Kopf über das Kuchenstück vor ihr und nimmt das Aroma auf."


show lilly basic_cheerful_cas_close onlayer master
with charachange

li "Zitronenkuchen, nicht wahr? Danke, Hisao."


hi "Keine Ursache. Der Tee steht direkt daneben, also pass auf, dass du ihn nicht umwirfst."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

"Sie nickt dankbar, aber ihrem müden Lächeln nach zu urteilen, war die Warnung nicht wirklich nötig. Ich nehme an, das Geräusch beim Abstellen hat ihr die Position verraten."


"Wir greifen kurzerhand zu, wobei wir beide größtenteils schweigen. Lilly ist nicht der Typ für Gespräche beim Essen, und von mir kann ich das auch nicht behaupten."


"Irgendwann sind wir mit dem Essen fertig und kurz darauf auch mit dem letzten Rest unseres Tees. Lilly bricht als erste das Schweigen."


show lilly basic_smile_cas_close onlayer master
with charachange

li "Das war sehr lecker. Ich muss sagen, deine Wahl war ziemlich gut, Hisao."


hi "Das ist das erste Mal, dass ich mich wirklich in der Stadt umgeschaut habe, darum konnte ich eigentlich nur danach gehen, was nett aussah."


hi "Ah… mist. Tut mir leid."


"Ich fühle mich echt schlecht, weil ich in Lillys Nähe versehentlich vom Sehen gesprochen habe, aber es scheint ihr nicht sonderlich viel auszumachen. Sie sieht angesichts meines peinlichen Versuchs, mich zu entschuldigen, fast belustigt aus."


show lilly basic_smileclosed_cas_close onlayer master
with charachange

li "Du bist rücksichtsvoll, Hisao, aber manchmal fürchte ich, dass du es übertreibst. Du musst meinetwegen nicht deine Ausdrucksweise ändern."


"Lilly kann wirklich gut mit ihrer Behinderung umgehen. Ich will immer noch schnell das Thema wechseln, weil ich nicht behaupten kann, ihr Selbstvertrauen in dieser Angelegenheit zu teilen."


hi "Lebst du schon sehr lange hier? Scheint so, als würdest du dich hier schon ziemlich gut auskennen."


show lilly basic_planned_cas_close onlayer master
with charachange

"Bei diesem Gedanken winkt sie schnell verneinend ab. "


show lilly basic_smile_cas_close onlayer master
with charachange

li "Nein, nichts dergleichen. Ich bin schon auf der Yamaku, seit ich zur Oberschule gehe, aber ich bin nicht viel in der Stadt herumgekommen, weil Akira, meine Schwester, mich immer abgeholt und hingebracht hat."


hi "Oh, stimmt. Du hast erwähnt, dass du erst seit Kurzem im Wohnheim wohnst."


"Es ist ziemlich überraschend. Ich hatte einfach angenommen, dass sie schon mindestens hier wohnt, seit sie an diese Schule gekommen ist – also zumindest ein paar Jahre."


show lilly basic_smileclosed_cas_close onlayer master
with charachange

li "Ich habe die längste Zeit meines Lebens mit meiner Familie zusammengewohnt, danach nur mit meiner Schwester."
li "Weil meine Familie schon vor einiger Zeit nach Inverness gezogen war und Akira länger arbeiten musste, musste ich letztendlich umziehen."


hi "Inverness? Ist das nicht irgendwo in Schottland?"


show lilly basic_surprised_cas_close onlayer master
with charachange

li "Oh, habe ich dir das nicht erzählt? Meine Familie lebt in Schottland, dem Geburtsort meiner Mutter. Väterlicherseits ist meine Familie aber größtenteils Japanisch."


"Hm. Die Frage, woher Lilly ihr Aussehen hat, ging mir schon hin und wieder durch den Kopf, aber ich habe nie daran gedacht zu fragen. Das wäre dann die Erklärung dafür."


hi "Ehrlich gesagt wäre ich darauf nie gekommen. Da du keinen Akzent hast, schätze ich, du bist hier geboren?"


show lilly basic_giggle_cas_close onlayer master
with charachange

li "Volle Punktzahl. Ich bin allerdings froh über meine Herkunft, weil ich ohne sie wahrscheinlich nicht in so jungen Jahren Englisch gelernt hätte."


show lilly basic_smile_cas_close onlayer master
with charachange

li "Und was ist mit dir, Hisao?"


hi "Was soll mit mir sein?"


"Sie denkt einen Augenblick nach. Sie hätte sich wohl vorher überlegen sollen, was sie mich fragen will, bevor sie das Thema wechselt."


show lilly basic_weaksmile_cas_close onlayer master
with charachange

li "Ich nehme mal… Was sind deine Pläne für die Zukunft?"


hi "Ehrlich gesagt hab ich darüber in letzter Zeit nicht viel nachgedacht."


hi "Nach meiner Herzattacke und den anschließenden Monaten im Krankenhaus war es genug für mich, mein Leben hier mit dir und Hanako zu genießen."


"Genau genommen habe ich seit einiger Zeit nicht über eine „Zukunft” nachgedacht. Es erscheint fast sinnlos."


show lilly basic_sleepy_cas_close onlayer master
with charachange

li "Das ist dein letztes Schuljahr. Danach musst du auf die eine oder andere Art für dich selbst sorgen."


hi "Es ist ja nicht so, als ob ich das nicht wüsste. Ich hab seitdem nur nicht viel darüber nachgedacht…"


show lilly basic_weaksmile_cas_close onlayer master
with charachange

"Sie öffnet den Mund, um weiterzureden, aber stattdessen seufzt sie leicht. Scheinbar hat sie eingesehen, dass sie nicht wirklich genug über meine Situation weiß, um tiefer in das Thema einzutauchen."


li "Nun ja, wir gehen das alle anders an. Ich hoffe nur, dass du jede Chance ergreifst, auf die du stößt."


hi "… Verstehe. Ich werde darüber nachdenken."


stop music fadeout 2.0

$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

scene bg city_street2 onlayer master
show lilly cane_smileclosed_cas_close onlayer master
with shorttimeskip

"Als wir wieder hinaus in die Stadt gehen, hakt Lilly sich wieder bei mir ein."


show lilly cane_smile_cas_close onlayer master
with charachange

li "Also, ist dir irgendein gutes Geschenk eingefallen?"


hi "Ehrlich gesagt, nein. Ich war nie gut im Geschenke Aussuchen."


show lilly cane_weaksmile_cas_close onlayer master
with charachange

li "So albern es sich anhört, aber vielleicht sollten wir uns einfach… umschauen?"


"Dass Lilly diese Worte von sich gibt, irritiert mich für einen Moment."


hi "Ähm… okay. Wie machen wir das?"


show lilly cane_cheerful_cas_close onlayer master
with charachange

li "Das ist genau die Reaktion, die ich erwartet hatte. Es ist einfach; du kannst dir die Schaufenster ansehen und mir sagen, was da ist."


show lilly cane_smileclosed_cas_close onlayer master
with charachange

li "Wenn etwas Interessantes dabei ist, fällt uns vielleicht etwas ein."


hi "Okay… Ich weiß noch nicht so recht, aber ich verlasse mich auf dich."


show lilly cane_smile_cas_close onlayer master
with charachange

li "Ich denke, wir kriegen das hin. Bei Hanako, meiner Schwester und mir klappt es ganz gut."


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg city_street3 onlayer master
with locationskip

"Mit dieser simplen und recht optimistischen Aussage von Lilly brechen wir zum Einkaufsviertel der Stadt auf, und ich fange an, Lilly alles zu beschreiben, was ich sehe."


"Es ist schwierig, sich Hanako bei einem Schaufensterbummel vorzustellen. Weder wirkt sie so, als würde sie viel auf Mode geben noch habe ich mitbekommen, wie sie Zeitschriften oder Ähnliches liest."
"Genau genommen ist Lesen das einzige Hobby, das ich von ihr kenne."


hi "Da ist ein Haushaltswarenladen direkt geradeaus. Sieht aber so aus, als gäbe es da hauptsächlich Geschirr."


show lilly cane_sleepy_cas_close onlayer master at center
with charaenter

li "Ich kann mir nicht vorstellen, dass sie das wirklich brauchen würde, und was würde das wohl für eine Botschaft senden?"


hi "Ähm… „Koch mehr”? Das ist keine so schlechte Idee, vielleicht…"


show lilly cane_weaksmile_cas_close onlayer master
with charachange

li "Manchmal ist es besser, die Dinge ruhen zu lassen, Hisao."


"Wieder einmal bekomme ich das Gefühl, dass Hanakos Abenteuer in der Küche nicht immer erfolgreich sind. Lilly musste ihr wohl manchmal helfen."


hi "Mal sehen, als nächstes kommt ein Bücherladen… Das hört sich doch gut an. Sie liest ständig."


show lilly cane_concerned_cas_close onlayer master
with charachange

li "Ja, aber bei Büchern gibt es ein Problem: Ich weiß nicht genau, was sie schon gelesen hat und was nicht."


hi "Wie wäre es dann mit einem Gutschein?"


show lilly cane_listen_cas_close onlayer master
with charachange

li "Es gibt nichts Unpersönlicheres als jemandem einen Gutschein zu schenken. Das ist, als würde man sagen „Ich kenne dich nicht gut genug, um herauszufinden, was dir gefällt.”"


hi "Ich hab immer gedacht, man geht auf Nummer sicher, dass derjenige kriegt, was er will."


show lilly cane_displeased_cas_close onlayer master
with charachange

li "Du machst Menschen Geschenke, um ihnen den Grad deiner Zuneigung zu zeigen. Wenn du dich nicht auf ein einfaches Geschenk für sie festlegen kannst, wie viel sind sie dir dann wert?"


hi "Okay, okay, keine Gutscheine."


"Lilly wirkt überaus leidenschaftlich bei diesem Thema, aber ich weiß, was sie meint. Wenn man vorhat, etwas für jemanden zu kaufen, dann sollte man sich wenigstens ein paar Gedanken darüber machen."


"Wenn ich etwas für Hanako besorgen will, das sie jeden Tag an uns erinnert, was bringt dann ein Gutschein?"


hi "Was hast du Hanako denn letztes Jahr geschenkt?"


show lilly cane_smile_cas_close onlayer master
with charachange

li "Eine Porzellanpuppe. Ich dachte mir, wenn sie jemanden zum Reden hat, dann hilft ihr das vielleicht, ihren Schmerz zu lindern."


show lilly cane_weaksmile_cas_close onlayer master
with charachange

li "Immerhin wird eine Puppe sie niemals kritisieren."


hi "Also soll ich nach einem Puppenladen suchen?"


show lilly cane_smileclosed_cas_close onlayer master
with charachange

li "Wenn du so freundlich wärst, nach einem Ausschau zu halten, wäre ich dir dankbar."


hi "Klingt gut, allerdings wünschte ich, du hättest das früher erwähnt."


show lilly cane_cheerful_cas_close onlayer master
with charachange

li "Aber wenn ich das getan hätte, dann hättest du nicht angefangen, selbst nachzudenken, oder?"


"Wieder einmal hat Lilly nicht ganz Unrecht."
"Mein Gehirn analysiert gerade jeden Laden, an dem wir vorbeikommen, auf mögliche Geschenke. Wenn Lilly von Anfang an einen Puppenladen angesprochen hätte, wäre mir nichts anderes mehr in den Sinn gekommen."


$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg city_street4 onlayer master
with locationskip

"Wir wandern durch die Straßen der Stadt, finden aber nichts, was an einen Puppenladen erinnert – oder irgendetwas, das ich als passendes Geschenk bezeichnen würde."


"So suchend durch die Straßen zu gehen, ist wirklich entspannend. Die Geschehnisse von letzter Woche verblassen, und ich freue mich darauf, Hanako ihr Geschenk zu geben…"


"… das heißt, falls ich eines finde."


hi "Das ist hoffnungslos. Ich dachte, wir würden auf jeden Fall etwas in der Stadt finden. Und ich bin mir sicher, dass wir diese Straße vorher schon mindestens einmal entlanggelaufen sind."


show lilly cane_oops_cas_close onlayer master at center
with charaenter

li "Das hört sich fast so an, als würdest du aufgeben, Hisao."


hi "Tu ich nicht, aber es ist um einiges schwieriger als ich dachte."


show lilly cane_smileclosed_cas_close onlayer master
with charachange

li "Versuch, deinen Gedanken freien Lauf zu lassen. Vielleicht sollten wir mal in ein paar Läden hineingehen und uns umsehen?"


hi "Das könnte funktionieren. Ich war noch nie gut im Schaufensterbummeln."


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg city_street3 onlayer master at right
with locationskip

"Lilly und ich drehen noch einmal eine Runde durch die Stadt und schauen dieses Mal kurz in die Läden, die uns auffallen. Letzten Endes finden wir aber nichts, was sonderlich gut passen würde."


"Hanakos Geschmack ist dank ihres äußerst zurückgezogenen Wesens bestenfalls recht schwer einzuordnen. Und den Vorlieben, die wir kennen, kann man nur schwer gerecht werden."


show lilly cane_sleepy_cas_close onlayer master at center
with charaenter

li "Können wir kurz Pause machen? Ich bin ein bisschen erschöpft."


show lilly cane_sleepy_cas_close onlayer master:
    ypos 1.05
with charamove

show bg city_street3 onlayer master at left
show lilly invis onlayer master:
    xpos 0.8
    ypos 1.05
with dissolvecharamove

"Ich bin einverstanden und lasse Lilly gegen ein Geländer gelehnt zurück, um sich auszuruhen, während ich von einem Getränkeautomaten in der Nähe etwas zu Trinken hole."


"Nachdem ich eine Limonade für mich selbst gezogen habe, stehe ich ratlos vor dem Getränkeautomaten."
"Da ich nicht wirklich weiß, was Lilly gerne trinkt, beschließe ich einfach zu raten und nehme etwas, das ein bisschen mädchenhaft aber nicht zu seltsam wirkt: Milch mit Erdbeergeschmack."


show bg city_street3 onlayer master at right
show lilly cane_weaksmile_cas_close onlayer master:
    center
    ypos 1.05
with dissolvecharamove

hi "Wieder da."


"Ich gehe zu ihr und lege das Trinkpäckchen in ihre ausgestreckten Hände, wobei ich darauf achte, dass sie es festhält, bevor ich loslasse."


show lilly cane_smile_cas_close onlayer master
with charachange

"Sie ertastet seine Konturen, bevor sie es öffnet und einen sehr zaghaften Schluck nimmt. Ihr anerkennendes Lächeln sagt mir, dass ich die richtige Wahl getroffen habe. Wir beide machen ein paar Minuten lang Pause und trinken schweigend."


$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_phone

show lilly cane_surprised_cas_close onlayer master
with charachange

"Ein vertrautes Klingeln ertönt leise aus Lillys Richtung. Schnell entschuldigt sie sich, während ihre Hand in ihre Tasche wandert und ihr Handy herausholt."


show lilly cane_weaksmile_cas_close onlayer master
with charachange

li "Stört es dich, wenn ich rangehe?"


hi "Schon okay, keine Sorge."


show lilly back_listen_cas_close onlayer master
show lillyprop back_cane_close onlayer master:
    center
    ypos 1.05
with charachange

"Sie nickt mir dankend zu, bevor sie sich umdreht, ihr Handy aufklappt und es an ihr Ohr hebt, um den Anruf anzunehmen."


show lilly back_smile_cas_close onlayer master
with charachange

"Lillys Stimme nach zu urteilen, ist die Person am anderen Ende zweifellos irgendein Freund. Schnell höre ich auf, dem Gespräch zu folgen, weil die kurzen Fetzen, die Lilly von sich gibt, sich nach mehr als Tratsch anhören."


"Ohne andere Beschäftigung ertappe ich mich dabei, wie ich Lilly beobachte. Sie ist ein wirklich hübsches Mädchen, was ihrer Beliebtheit an der Schule wohl kaum schadet."
"Es ist interessant, wie sehr sich Hanako und Lilly unterscheiden, sowohl in ihren Persönlichkeiten als auch ihrem Aussehen."


show lilly back_smileclosed_cas_close onlayer master
with charachange

"Ein paar Minuten lang lehne ich mich einfach zurück und trinke, während ich sie beobachte."
"Es dauert nicht lange, dann verabschiedet sich Lilly von ihrem Gesprächspartner und legt auf. Sie steckt das Handy zurück in ihre Tasche und lehnt sich wie zuvor mit dem Rücken gegen das Geländer."


hide lillyprop onlayer master
show lilly cane_weaksmile_cas_close onlayer master
with charachange

li "Tut mir leid, nur ein Schulfreund."


$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_can_clatter

"Ich nehme einen letzten Schluck aus meiner Dose, bevor ich sie in den Mülleimer werfe. Lilly gibt mir kurz darauf ihr Trinkpäckchen, das sie relativ schnell geleert hat, damit ich es wegwerfe."


$ renpy.music.set_volume(0.1, 2.0, channel="ambient")

hi "Du scheinst viele Freunde zu haben."


show lilly cane_smile_cas_close onlayer master
with charachange

li "Oh?"


"Lilly wartet neugierig darauf, dass ich fortfahre."


hi "Ich dachte nur gerade, dass du und Hanako euch sehr stark unterscheidet. Du kennst viel mehr Leute, und Hanako würde vieles, was du tust, niemals machen."


show lilly cane_giggle_cas_close onlayer master
with charachange

li "Du scheinst ziemlich viel über Hanako nachzudenken."


hi "Ich weiß nicht. Es ist nur… dass sie rätselhaft ist, schätze ich. Ich will irgendwie mehr über sie erfahren, und das ist nicht so einfach."


show lilly cane_weaksmile_cas_close onlayer master
with charachange

li "Klingt fast so, als würdest du an deiner Beziehung zu ihr zweifeln."


hi "Das ist es, glaub ich, nicht. Ich will einfach nur mehr für sie tun, weil ich ihr Freund bin und so. Ich weiß nicht mal wirklich, was sie von mir hält."


show lilly cane_smile_cas_close onlayer master
with charachange

"Diese Aussage scheint Lilly sehr interessant zu finden. Ich frage mich, ob Hanako ihr irgendwas über mich gesagt hat."


show lilly cane_smileclosed_cas_close onlayer master at center
with dissolvecharamove

"Ich bin kurz davor zu fragen, was sie gerade denkt, als sie sich von dem Geländer aufrappelt."


show lilly cane_cheerful_cas_close onlayer master
with charachange

li "Wollen wir dann los?"


"Ihre Stimme und ihr Gesichtsausdruck verraten, dass sie mit mir spielt. Lilly weiß ganz genau, dass sie mich hängenlässt."


"Seufzend stoße ich mich auch von dem Geländer ab und sehe mich kurz um. Wir haben zu tun, darum werde ich einfach später versuchen, wieder darauf zurückzukommen."


"Zwischen einem Zeitungsstand und einem Mini-Markt ist ein kleines Geschäft. Auf dem Schild über der Tür steht in verzierter englischer Schrift: „Othello's Antiquitäten”."


"Wenn wir daran vorbeigelaufen wären, hätten wir es leicht übersehen können, aber da wir stillstehen und ich mich gezielt umgesehen habe, fällt es gerade so auf."


$ renpy.music.set_volume(0.3, 6.0, channel="ambient")

hi "Sag mal, Lilly… Diese Puppe, die du für Hanako gekauft hast – war die neu?"


show lilly cane_smile_cas_close onlayer master
with charachange

li "Äh, ja, aber ich glaube, ich verstehe nicht ganz, was du meinst."


hi "Ich glaube, ich hab unseren Laden gefunden. Er ist auf der anderen Seite der Straße."


show lilly cane_surprised_cas_close onlayer master
with charachange

li "Oh? Was ist es für einer? Eine Art Spielzeugladen?"


hi "Es ist ein Antiquitätengeschäft. Ich glaube, wenn wir irgendwo etwas finden, dann wahrscheinlich dort."


show lilly cane_satisfied_cas_close onlayer master
with charachange

li "Wirklich? Ich wusste gar nicht, dass es in der Gegend überhaupt einen gibt."


hi "Wusste ich auch nicht. Ich hab ihn das erste Mal, als wir hier vorbei gekommen sind, übersehen. Er ist ziemlich gut versteckt."


show lilly cane_smileclosed_cas_close onlayer master
with charachange

li "Na gut, es kann nicht schaden, mal reinzuschauen."


"Von der neuen Entdeckung ermutigt klopfen wir uns den Staub von den Kleidern und gehen zu dem Geschäft. Lilly hakt sich wieder bei mir ein."


stop ambient fadeout 0.5

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_storebell
play music music_soothing fadein 0.5
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

scene bg city_othello onlayer master at right
with locationchange

"Über dem Laden liegt ein seltsamer, moschusartiger Duft. Er sieht eher wie eine Garage aus als ein Geschäft; Sachen sind ohne offensichtlichen Anschein von Ordnung auf dem Boden verstreut."


show shopkeep neutral onlayer master at center
with charaenter

"Der Ladenbesitzer wirft uns aus seinen auffallend kleinen Augen einen fast gelangweilten Blick zu. Sein Gesicht wirkt erschöpft und müde, und sein Kleidungsstil ist eindeutig unzeitgemäß."
"Er nickt uns höflich zu, bevor er sich wieder seinem Buch widmet."


hide shopkeep onlayer master
with charaexit

"Lilly klammert sich eng an meinen Arm, und ich muss meine Aufmerksamkeit aufteilen, um zum einen dafür zu sorgen, dass wir kein mögliches Geschenk für Hanako übersehen, und zum anderen, dass Lilly nicht versehentlich irgendwo anstößt."


show bg city_othello onlayer master at center
with charamove_slow

"Das ist wegen des willkürlichen Aufbaus des Ladens und der vielen Sachen, die aus den Regalen oder von den anderen Möbeln hervorstehen, ziemlich schwierig, aber schließlich erreichen wir einen alten Tisch, voll mit Puppen und Teddybären."


hi "Ich glaube, wir sind richtig. Es gibt hier so ziemlich jede Art von Puppe, die du dir vorstellen kannst."


show lilly cane_smileclosed_cas_close onlayer master at center
with charaenter

li "Das sollte uns die Auswahl erleichtern. Könntest du bitte eine für mich aussuchen, Hisao?"


"Ich hatte so ein Gefühl, dass es dazu kommen würde. In Gedanken mache ich mir ein Bild von Hanako und versuche, mir vorzustellen, welche der Puppen vor mir am besten zu ihr passt."


"Meine Augen schweifen über die Sammlung; jede einzelne ist so exquisit wie die vorige. Die schiere Anzahl an verschiedenen Arten ist überwältigend, aber letztendlich springt mir eine ins Auge."


hi "Hier, wie wär's mit der?"




"Ich nehme eine kleine Porzellanpuppe in die Hand, die wenigstens einigermaßen erschwinglich aussieht. Mit einem grünen Kleid aus der viktorianischen Zeit und einem kleinen braunen Hut auf den blonden Haaren sieht sie ein bisschen wie Lilly aus."


show lilly cane_listen_cas_close onlayer master
with charachange



"Behutsam gebe ich ihr die Puppe. Lilly befühlt sie vorsichtig mit den Händen, und macht dabei einen leicht konzentrierten Eindruck."


show lilly cane_smile_cas_close onlayer master
with charachange

li "Sie fühlt sich definitiv hübsch an. Glaubst du, sie passt zu Hanako?"


hi "Ich glaube, ja; sie würde gut in ihr Zimmer passen."


show lilly cane_smileclosed_cas_close onlayer master
with charachange

li "In diesem Fall vertraue ich deinem Urteil. Wirst du ihr auch etwas schenken, oder soll das ein gemeinsames Geschenk werden?"


hi "Hmm, ich weiß nicht. Ich denke, ich sollte ihr selbst etwas schenken, aber ich glaube nicht, dass es eine so gute Idee wäre, ihr noch eine Puppe zu schenken. Vielleicht…"


"Meine Stimme verstummt langsam, als ich mich in dem Laden umsehe. Auf einem Schreibtisch nicht weit von uns entfernt liegt ein schmuckvoller Kasten."


hi "Warte hier. Ich glaube, ich hab was gefunden…"


show lilly cane_ara_cas_close onlayer master
with charachange

li "Na so was, das ging schnell."




"Vorsichtig wandere ich durch eine Sammlung aus Kristallglaswaren und hebe den Kasten auf. Die hölzernen Seiten sind mit Schnitzereien bedeckt, die Schlachten um eine Burg herum darstellen."


"Die Oberseite sieht allerdings nur allzu vertraut aus. Auf dem hölzernen Deckel sind abwechselnd weiß und schwarz lackierte Quadrate angeordnet."


sk "Das ist ein wirklich schönes Stück. Ein Schachspiel aus Übersee."




show bg city_othello onlayer master at bgleft
show lilly cane_smileclosed_cas_close onlayer master at twoleft
with dissolvecharamove

show shopkeep neutral onlayer master at tworight
with charaenter

"Das plötzliche Erscheinen des Ladenbesitzers lässt mich leicht zusammenfahren; ich habe ihn überhaupt nicht näherkommen sehen."


"Ich nehme an, er will uns helfen, weil wir nicht wirklich so aussehen, als wüssten wir, was wir wollen – vielleicht will er uns auch im Auge behalten, weil er den Verdacht hat, dass wir etwas klauen könnten."


hi "Ich… suche nach einem Geschenk für eine Freundin."


show shopkeep happy onlayer master
with charachange

sk "Aha. In diesem Fall wäre dieses Schachspiel eine gute Wahl."


"Dann schlägt mir die Erkenntnis ins Gesicht. Das ist ein ziemlich hübsches Spiel, aber ich bin hier in einem Antiquitätenladen. Die sind nicht gerade für ihre Vorzugspreise bekannt."


hi "Wie alt ist es?"


show shopkeep neutral onlayer master
with charachange

sk "Das ist eine Replik. Ich würde es auf fünf Jahre schätzen."


hi "Verstehe. Wie viel?"


show shopkeep thinking onlayer master
with charachange

"Er überlegt kurz, bevor er es mir sagt – was leicht beunruhigend ist."


show shopkeep neutral onlayer master
with charachange

sk "Für 7.000 Yen können Sie es sofort mitnehmen."


"Ich stocke kurz; ich hatte nicht erwartet, so viel auszugeben, aber es erscheint mir perfekt. Andererseits ist das vielleicht ein Beleg dafür, wie gut er meine preisliche Schmerzgrenze einschätzen konnte."


hi "Können wir nicht 5.000 sagen?"


show shopkeep thinking onlayer master
with charachange

sk "5.500, weniger nicht."


hi "Überredet. Oh, und diese Puppe hätten wir auch noch gern…"


show shopkeep neutral onlayer master
with charachange

"Der Ladenbesitzer schaut über meine Schulter und richtet seine Aufmerksamkeit auf Lilly und die Puppe in ihren Händen. Er kneift die Augen zusammen und man kann sehen, wie er einen Moment braucht, um sich gedanklich umzustellen."


"Dabei wird sein Lächeln etwas dünner."


sk "Ah…"


"Ich schätze, das heißt, dass nicht alles in seinem Laden eine Replik ist."


show shopkeep thinking onlayer master
with charachange

sk "Sind Sie sich wirklich sicher, dass Sie diese Puppe wollen?"


show lilly cane_smile_cas_close onlayer master
with charachange

li "Ich vertraue auf das Urteilsvermögen meines Freundes."


show shopkeep surprised onlayer master
with charachange

sk "Ich verstehe…"


show lilly cane_smileclosed_cas_close onlayer master
with charachange

li "Wenn Sie sie dann bitte für mich einpacken könnten, das wäre sehr freundlich."


show shopkeep neutral onlayer master
with charachange

sk "Ja, natürlich, aber sie kostet 20.000 Yen…"


"Lilly greift in ihre Brieftasche und präsentiert vier frische 5.000 Yen-Scheine."


show lilly cane_cheerful_cas_close onlayer master
with charachange

li "Bitte sehr, 20.000 Yen."


show shopkeep thinking onlayer master
with charachange

"Der Ladenbesitzer nimmt das Geld und die Puppe und geht zurück zum Ladentisch. Ich nehme Lillys Arm und führe sie dorthin."


hi "Bist du dir sicher?"


show lilly cane_smileclosed_cas_close onlayer master
with charachange

li "Schon gut; Ich… habe genug Geld dafür. Wie gesagt, ich vertraue deinem Urteilsvermögen."


"Ich fühle mich aus zwei Gründen ein wenig schuldig; erstens, weil Lilly gerade einen Haufen Geld wegen meiner Empfehlung ausgegeben hat, und zweitens, weil ich glaube, dass mein Geschenk nicht genug wert ist."


"Jedoch scheint Lilly das Thema Geld immer ein bisschen unangenehm zu sein…"


show shopkeep neutral onlayer master
with charachange

"Ich reiche dem Ladenbesitzer mein Geschenk und das Geld dafür. Er verstaut es in der Kasse und ist danach beschäftigt damit, die Puppe und das Schachspiel einzupacken."


"Irgendwann ist er mit dem Verpacken der Geschenke fertig und gibt sie uns beiden."


show shopkeep happy onlayer master
with charachange

sk "Bitte seien Sie vorsichtig auf dem Heimweg, und besuchen Sie uns wieder."


hi "Danke."


show lilly cane_smile_cas_close onlayer master
with charachange

li "Natürlich, vielen Dank."


"Der Ladenbesitzer verbeugt sich tief, als wir das Geschäft verlassen."


stop music fadeout 6.0
$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

scene bg city_street3 onlayer master
with locationchange

show lilly cane_weaksmile_cas_close onlayer master at center
with charaenter

li "Nun, es hat uns den ganzen Tag gekostet, aber wir haben am Ende doch etwas gefunden."


hi "Das haben wir."


"Jetzt, da die Geschenke eingepackt sind, kann ich es kaum erwarten, sie Hanako zu geben. Das ist typisch beim Geschenkekaufen; man will die Reaktion des Empfängers sehen, wenn er herausfindet, was es ist."


"Und ein Teil von mir will zu Hanako zurück, nur um mit meinen eigenen Augen zu sehen, wie es ihr geht."


hi "Also, gehen wir nach Hause?"


show lilly cane_smile_cas_close onlayer master
with charachange

li "Ja. Wir sind heute ziemlich viel herumgelaufen, da habe ich nichts dagegen, mich in meinem Zimmer etwas auszuruhen."


"Lilly hat Recht. Jetzt, wo wir nicht mehr auf der Suche nach einem Geschäft sind, sind meine Beine müde geworden."


hi "Na dann, zurück zur Schule. Ich freue mich auch schon auf eine kleine Pause."


"Lilly streckt ihren Arm aus, und ich hake mich ein. Gemeinsam machen wir uns auf den Weg zurück zur Bushaltestelle."


stop ambient fadeout 2.0

scene black onlayer master
with dissolve



label de_H14:

play music music_pearly fadein 5.0

scene bg school_scienceroom onlayer master at right
with locationchange

"Mutou liest uns in seiner üblichen, monotonen Stimme der Reihe nach Gleichungen und Formeln direkt aus dem Buch vor."


"Ich halte es für möglich, dass er das, was er uns beibringt, aufrichtig toll findet; manchmal geht von ihm ein unbeholfener Funke an Leidenschaft aus, als ob er sich wirklich für den Stoff begeistern würde."


"Die meisten Tage sind aber wie dieser. Was wir gerade durchnehmen, ist recht einfach, darum fällt es mir zunehmend schwerer, mich auf ihn zu konzentrieren. Es dauert nicht lange, bis auch noch meine Beine wieder zu schmerzen anfangen."


"Ich bin kurz davor, den gestrigen Spaziergang durch die Stadt mit Lilly zu bereuen."


"Seit ich aus dem Krankenhaus heraus bin, habe ich mich körperlich nur sehr wenig betätigt. Zum örtlichen Laden an der Ecke und zurück zu laufen, zählt wohl kaum."
"Trotz Emis Bemühungen, als ich hier an der Schule angekommen bin, habe ich die Hoffnung, jemals wieder mein altes Fitnessniveau zu erreichen, größtenteils aufgegeben."


"Ich zweifle kaum daran, dass das der Grund dafür ist, warum mich ein Spaziergang durch die Stadt so beansprucht hat."
"Es ist deprimierend, und es erinnert mich an eine weitere Sache, die ich seit meiner Herzattacke nicht mehr tun kann. Dadurch fühle ich mich erbärmlich."


show muto normal onlayer master at twoleft
with charaenter

mu "Also… Ikezawa?"


show hanako defarms_shock onlayer master at tworight
with vpunch

"Es ist ungewöhnlich, dass Mutou eine Frage an Hanako richtet, aber es kann vorkommen. Ein bisschen erschrocken springt sie rasch auf und fixiert ihren Blick auf ihn."


"Sie weiß, wie selten es ist ist, dass Mutou sie aufruft, und somit auch, dass alle Augen im Klassenzimmer auf sie gerichtet sein werden. Auf diese Weise läuft sie nicht Gefahr, mit irgendjemand anderem in Blickkontakt zu geraten."


show hanako def_worry onlayer master
with charachange

ha "J-Ja?"


mu "In diesem speziellen Fall einer Redoxreaktion bringt die Verbrennungsreaktion von Methan ein weiteres Produkt hervor, das nicht aufgelistet ist. Dieses Produkt ist…?"


show hanako emb_downtimid onlayer master
with charachange

"Obwohl es eine sehr einfache Frage ist, wartet sie zögerlich, bevor sie antwortet, wobei sie leicht auf ihrer Unterlippe herumbeißt, als ob sie dadurch ihre Konzentration aufrecht erhalten würde."


show hanako emb_timid onlayer master
with charachange

ha "Ähm… W-Wärme?"


show muto smile onlayer master
with charachange

mu "Sehr gut. Das ist eine exotherme Reaktion, bei der die Reaktion mehr Wärme abgibt, als hineingesteckt wurde."


show hanako invis onlayer master:
    ypos 1.1
with dissolvecharamove

hide hanako onlayer master
with None

"Nach einem Nicken von Mutou setzt sich Hanako wieder und seufzt erleichtert."


"Ein wackeliger Start, aber es ist ein Anfang."


"Es wäre schön, an ihrem Geburtstag mit ihr auszugehen, irgendwo anders hin als in die übliche Abgeschiedenheit ihres Zimmers oder des Teezimmers."
"Bei dem Fortschritt, den sie bis jetzt gemacht hat, glaube ich nicht, dass es ein großes Problem für sie wäre, in die Stadt zu gehen."


show muto smile onlayer master at center
show bg school_scienceroom onlayer master at center
with charamove

mu "Also gut. Für den Rest der Stunde hätte ich gerne, dass ihr in Gruppen von drei oder vier Leuten die Aufgaben in Kapitel zwölf bearbeitet. Ich bin hier, falls ihr mich braucht."


$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 8.0

show muto invis onlayer master:
    ypos 1.1
with dissolvecharamove

hide muto onlayer master
with None

"Mutou setzt sich hinter seinen Tisch, zieht ein paar lose Blätter aus einem Ordner hervor und fängt an, seinen eigenen Papierkram zu machen. Ich dachte, Lehrer sollten so etwas nach dem Unterricht machen, nicht währenddessen."


show shizu invis_close onlayer master:
    tworight
    xpos 0.8
show misha invis_close onlayer master:
    twoleft
    xpos 0.2
with None

show shizu behind_blank_close onlayer master at tworight
show misha hips_smile_close onlayer master at twoleft
with dissolvecharamove

"Ich ignoriere ihn und schaue zu meiner Rechten, um jemanden auszusuchen, mit dem ich eine Gruppe bilden kann. Angesichts der zwei Gesichter, die mich von der Seite her angrinsen, glaube ich kaum, dass ich in dieser Angelegenheit etwas zu sagen habe."


hi "Ich nehme an, wir haben eine Gruppe."


show misha hips_grin_close onlayer master
with charachange

mi "Hicchan~! Du willst zusammenarbeiten? Okay, okay~! Das ist super! Es ist echt 'ne Weile her~!"


show shizu behind_blank_close onlayer master:
    ypos 1.09
show misha hips_smile_close onlayer master:
    ypos 1.09
with dissolvecharamove

"Die Klasse fängt lautstark an, die Tische herumzuschieben, und Shizune tut es ihnen gleich, indem sie ihren vor meinen stellt."
"In gewisser Hinsicht hat sie Glück, dass sie den Lärm im Klassenzimmer nicht hören kann. Es ist laut genug, um unangenehm zu sein."


"Um ehrlich zu sein, mit Shizune und Misha zu arbeiten, ist wahrscheinlich nicht schlecht – Shizune und ich sind in diesem Fach recht gut, und Misha… hat eine wirklich schöne Handschrift."


show hanako silhouette behind shizu onlayer master at center
with charaenter

"Als ich Misha anschaue, fällt mir eine große Gestalt hinter ihr auf. Der Schatten erregt auch Mishas Aufmerksamkeit, und sie dreht sich um, um sich dem dunkelhaarigen Beobachter zuzuwenden."


show shizu behind_blank_close onlayer master at Position(xpos=0.8)
show misha perky_smile_close onlayer master at Position(xpos=0.2)
show hanako basic_worry onlayer master
with dissolvecharamove

mi "Hallo, Hanako~!"



show hanako emb_timid onlayer master
with charachange

ha "Ähm… Hallo…"


"Nachdem sie aufsieht und den Blicken von Misha und mir folgt, bemerkt Shizune endlich Hanako. Schnell tippt sie Misha auf die Schulter, um auf sich aufmerksam zu machen und gestikuliert los."


show shizu adjust_happy_close onlayer master
with charachange

shi "…"


show misha sign_smile_close onlayer master
with charachange

mi "Shicchan sagt, falls du eine Gruppe suchst, kannst du in unsere kommen~!"


show hanako emb_downsmile onlayer master
with charachange

"Hanako sieht zu Boden und wird bei dem Angebot leicht rot. Von allen Leuten in der Klasse kennt Hanako uns drei am besten, da ist es nachvollziehbar, dass sie zuerst zu uns kommt."


"Andererseits kommt es anscheinend nur sehr selten vor, dass sie tatsächlich zu einer Gruppe geht, um ihr beizutreten."


hide hanako onlayer master
with charaexit

show shizu behind_smile_close onlayer master:
    tworight
    ypos 1.09
show misha hips_smile_close onlayer master:
    twoleft
    ypos 1.09
with dissolvecharamove

"Sie geht kurz, um ihren Tisch heranzuziehen, und Shizune und Misha drehen sich wieder zu mir um, sobald sie uns den Rücken gekehrt hat."


show shizu adjust_happy_close onlayer master
with charachange

shi "…"


show misha perky_smile_close onlayer master
with charachange

mi "Ich schätze, wir dürfen wieder miteinander spielen, Hicchan~! Du spielst kaum noch mit uns…"


hi "Ich frage mich warum? Ihr Zwei scheint immer irgendwas im Schilde zu führen."


show shizu basic_frown_close onlayer master
with charachange

shi "…"


show misha hips_frown_close onlayer master
with charachange

mi "Das war gemein, Hicchan… Fast würde ich glauben, du beleidigst mich~!"


show misha hips_grin_close onlayer master
with charachange

mi "Aber~! Du bist Hicchan, darum weiß ich, dass du nur Scherze machst!"


hi "Und du bist so verständnisvoll bei dem Thema; es wäre schrecklich, wenn jemand deine Gutmütigkeit ausnutzen würde – zum Beispiel, indem er dich dazu zwingt, ihm bei der Arbeit zu helfen."


show shizu adjust_smug_close onlayer master
with charachange

shi "…"


show misha cross_laugh_close onlayer master
with charachange

mi "Wahahaha~!"


"Shizune wirkt für einen Moment aufgeregt, weil sie überrascht ist, dass ich bereit bin, sie herauszufordern, aber als sie Hanako zurückkommen sieht, zieht sie sich lächelnd zurück. Mit den Psychospielchen ist heute wohl früher Schluss."


show hanako invis_close behind shizu onlayer master at center
with None

show shizu behind_blank_close onlayer master at Position(xpos=0.85)
show misha perky_smile_close onlayer master at Position(xpos=0.15)
show hanako emb_downtimid_close onlayer master at Position(ypos=1.09)
with dissolvecharamove

"Vorsichtig stellt Hanako ihren Tisch vor dem von Misha ab. Ihre Augen sind nach unten gerichtet, und ich frage mich warum, bis ich mich in der Klasse umschaue."


"Die meisten sind damit beschäftigt, sich in Gruppen zusammenzufinden, aber ein paar werfen ihr neugierige Blicke zu. Auf diese Entfernung ist es schwer zu sagen, ob das schon alles ist, oder ob sie auch über sie reden."


"Es ist seltsam. Keinen interessiert es, wenn Hanako aus der Klasse flüchtet, um sich vor Gruppenarbeit zu drücken, aber jetzt, wo sie sich einen Ruck gibt, starren sie alle an, als ob sie etwas falsch gemacht hätte."


"Wir machen uns auf der größeren Fläche breit, die durch die vier zusammengestellten Tische entstanden ist, und verteilen unsere Bücher und Arbeitsblätter darauf. Es dauert nicht lange, bis die ganze Klasse sich an die Arbeit macht."


show misha sign_smile_close onlayer master
with charachange

mi "Hi, Hanako~! Es ist schön, endlich mal mit dir zu arbeiten~."


show hanako basic_distant_close onlayer master
with charachange

ha "J-Ja."


show shizu adjust_smug_close onlayer master
with charachange

shi "…"


show misha hips_grin_close onlayer master
with charachange

mi "Bist du der Grund, warum Hicchan uns in letzter Zeit aus dem Weg gegangen ist~? Shicchan sagt, das ist ein bisschen unhöflich von ihm, aber wenn Hicchan Zeit mit einem süßen Mädchen verbringen will, ist das nachvollziehbar~!"


show hanako cover_worry_close onlayer master
with charachange

ha "I-Ich d-denke nicht, dass es das ist…"


"Hanako fängt an, unruhig herumzurutschen, da sie eine solche Aufmerksamkeit nicht gewohnt ist."


"Ich glaube, ein normaler Mensch hätte das Gespräch längst beendet, aber Misha ist wie der Gegenpol zu Hanako. Dazu gehört, für soziale Signale blind zu sein, während Hanako zu sensibel für sie ist."


"Darum schießen die Fragen nur so aus Misha heraus – zu schnell für mich, um sie zu unterbrechen und das Gespräch in eine angenehmere Richtung zu lenken."


stop music fadeout 7.0

show misha hips_smile_close onlayer master
with charachange

mi "Wirklich~? Er war gestern also nicht mit dir zusammen?"


show hanako emb_downsad_close onlayer master
with charachange

ha "N-Nein…"


"Ich kann schon spüren, wie meine Tarnung auffliegt. Lilly wollte nicht, dass Hanako weiß, dass wir unterwegs waren, um für sie Geschenke einzukaufen, und schon gar nicht, dass wir ihre Geburtstagsparty geplant haben."
"Es wäre nicht gut für sie, wenn sie es herausfände."


hi "Ja, ich hatte… etwas anderes zu tun. Ihr wisst doch, wie das ist…"


show shizu behind_blank_close onlayer master
with charachange

shi "…"


show misha sign_smile_close onlayer master
with charachange

mi "Wirklich~? Ich frage mich, was so wichtig war, dass Hicchan uns einfach so links liegen lässt~! Wenn es nicht war, um Zeit mit Hanako zu verbringen, was könnte es dann sein~? Wirklich interessant."


"Also das fühlt sich langsam an wie ein Verhör. Ich bin erstaunt, wie Misha es schafft, so einen Druck auszuüben, ohne es wirklich zu wollen."


show hanako defarms_strain_close onlayer master
with charachange

ha "W-Warst du mit L-Lilly zusammen?"


$ renpy.music.set_volume(0.3, 0.0, channel="ambient")

"Ganz plötzlich stolpert Hanako über die Antwort. Sie ist vielleicht furchtbar leise und schüchtern, aber sie hat eine gute Intuition."


hi "W-Wie kommst du darauf?"


show hanako emb_sad_close onlayer master
with charachange

ha "L-Lilly hat gestern etwas Ä-Ähnliches gesagt."


show shizu basic_happy_close onlayer master at Position(xpos=0.8)
with charachange

shi "…"


show misha hips_smile_close onlayer master
with charachange

mi "Verdächtig~! Hicchan~! Ich verlange eine Erklärung!"


hi "Hey, sollen wir nicht eigentlich die Aufgabe machen?"


show misha cross_smile_close onlayer master
with charachange

mi "Aber~! Es ist so geheimnisvoll… Sogar Hanako will es wissen~!"


"Ich drehe mich zu Hanako um. Es stimmt; ihr Gesichtsausdruck macht es offensichtlich, dass sie es auch wissen will, und ich ich glaube, wir sind über den Punkt hinaus, an dem ich mich vor einer Erklärung drücken könnte."


"In Gedanken entschuldige ich mich bei Lilly. Sie wollte es wirklich geheim halten, aber das scheint jetzt nicht mehr möglich."


"Ich spüre eine Welle von widersprüchlichen Emotionen, so durcheinander, dass ich sie nicht so einfach bestimmen kann, aber sie schwirren mir im Kopf herum, während ich versuche, mich zu beruhigen und zu reden."


hi "Also gut, ich sag's euch. Ich bin mit Lilly in die Stadt gegangen, aber es war nicht, wie ihr denkt."


hi "Lilly und ich haben… äh… für Hanakos Geburtsag… wir waren…"


"Die Katze ist aus dem Sack. Aber es sieht so aus, als würde Hanako es etwas besser aufnehmen als gedacht."


show misha perky_confused_close onlayer master
show shizu adjust_blush_close onlayer master at Position(xpos=0.85)
show hanako emb_downtimid_close onlayer master
with charachange

"In unserer kleinen Runde herrscht für kurze Zeit Stille, während Shizune und Misha sich betreten anschauen. Ich kann ihnen ansehen, dass sie nicht erwartet haben, dass ihr Spiel so endet."


"Misha sieht zu Hanako, um sich zu entschuldigen, und hält dann inne."
"Hanako starrt mit einem weinerlichen Gesichtsausdruck auf die Mitte ihres Tisches und verharrt fast bewegungslos. Ich schätze, ich lag falsch, als ich dachte, sie würde es gut aufnehmen."


show misha perky_sad_close onlayer master
with charachange

mi "Hanako? Es tut mir leid…"


"Für einige Sekunden passiert nichts, doch Hanako sieht auf und schüttelt den Kopf."


show hanako emb_timid_close onlayer master
with charachange

ha "E-Es… ist schon okay…"


"Sie macht ein merkwürdiges Gesicht, als wäre sie sehr müde. Es wirkt nicht natürlich, aber es ist nicht beunruhigend. Keiner will das derzeitige Gespräch fortführen, darum schlagen wir unsere Bücher auf und fangen mit der Gruppenarbeit an."


play music music_rain fadein 12.0
$ renpy.music.set_volume(0.5, 5.0, channel="ambient")

show shizu basic_normal2_close onlayer master at Position(xpos=0.8)
with charachange

"Es ist ziemlich langweilig. Die Gleichungen, die wir als Gruppe lösen sollen, werden eine Weile dauern, und der Großteil der Arbeit wird stumpfsinnig öde werden."


"Obwohl es nicht so schlecht gelaufen ist, wie es hätte können, ist es nicht gerade hilfreich, dass jetzt eine unangenehme Atmosphäre herrscht."


"In Shizunes Gesicht kann ich lesen, dass sie dieselben Erwartungen an unsere Arbeit stellt wie ich, und wir beide fangen an, die Ergebnisse unserer Gruppe aufzuschreiben."


show misha perky_confused_close onlayer master
with charachange

"Misha hingegen kaut auf ihrer Lippe herum und versucht ganz offensichtlich zu verstehen, was wir gerade machen. Hanako schaut still zu und saugt alles auf, was wir aufschreiben und was ich sage."


"Es ist eine Schande, dass sie so oft Abwesend ist. So, wie sie Informationen aufnimmt, glaube ich, dass sie in der Schule ziemlich gut wäre, wenn sie regelmäßig in den Unterricht käme."
"Ich frage mich, ob das vielleicht der Grund ist, warum Shizune so hart mit ihr umgeht."


show misha perky_smile_close onlayer master
with charachange

mi "Hey, Hanako, verstehst du das~?"


"Misha sieht zu Hanako, aber ich vermute eher, weil sie sich von ihr Beistand wegen ihrer Unwissenheit erhofft und nicht tatsächliche Hilfe."


show hanako emb_downtimid_close onlayer master
with charachange

ha "I-Ich… ähm… n-nicht wirklich… g-glaube ich…"


"Ich bin überrascht, wie angespannt sie bei ihrer Antwort ist, aber sie beruhigt sich wieder. Sie atmet aus. Die Art, wie ihr Oberkörper und ihr Kopf sich senken, erinnert mich an einen Ballon, aus dem die Luft entweicht."


hi "Alles okay bei dir? Ich kann mir diesen Teil ansehen, wenn du willst."


"Hanako schüttelt leicht den Kopf, aber ich glaube sowieso nicht, dass sie eine weitere Erklärung braucht – trotz ihrer Aussage."
"Schnell redet die völlige ahnungslose Misha dazwischen, und ich gehe schließlich langsam Schritt für Schritt durch, wie wir auf eines unserer Ergebnisse gekommen sind."


"Solche Momente erinnern mich daran, dass diese Arbeit vielleicht nicht für jeden stumpfsinnig ist, und ich nur dieses Gefühl habe, weil ich das Thema verstanden habe. Es ist ein befriedigendes Gefühl."


"Als Misha mit ihrer geballten Faust in ihre offene Hand schlägt, weil sie es verstanden hat, empfinde ich ein weiteres gutes Gefühl."
"Meine Erklärung ist zu ihr durchgedrungen, und sie schafft es, die nächste Gleichung mit nur geringer Hilfestellung selbst zu lösen."


"Währenddessen zeigt Hanako ungewöhnlicherweise keine Reaktion."


"Sie ist immer sehr still, aber man kann normalerweise noch ihre Augen durch das Klassenzimmer vor ihr streifen sehen, oder sie bewegt irgendwie unruhig ihre Hände oder ab und zu ihre Schultern."


"Im Moment fehlen all diese kleinen Bewegungen, an die ich mich gewöhnt hatte. Jemand, der sich gar nicht bewegt, ist auf jeden Fall seltsam. Sogar Misha merkt, dass etwas nicht stimmt."


show misha perky_confused_close onlayer master
with charachange

mi "Hanako? Sicher, dass bei dir alles in Ordnung ist?"


ha "J-Ja…"


hi "Bist du sicher?"


show hanako emb_downsad_close onlayer master
with charachange

ha "Mir geht's gut."


"Sie sagt es diesmal ein wenig eindringlicher, aber sie dreht sich weg, während sie es sagt. Das lässt mich nur an ihrer Antwort zweifeln, jedoch weiß ich, dass sie nicht weiter darüber reden will."


"Da ich heute bereits eine äußerst unangenehme Unterhaltung hinter mir habe, über die ich noch nicht ganz hinweg bin, will ich nicht weiter auf das Thema eingehen."


"Wir kehren wieder zu unserer Arbeit zurück und diskutieren jedes Mal, wenn Zweifel aufkommen, ob unsere Antwort richtig ist, aber mit der Zeit merke ich, dass Hanako überhaupt nichts sagt. Es ist frustrierend; sie hatte so viele Fortschritte gemacht."


"Es macht mich ein wenig wütend auf Shizune und Misha, weil sie die Überraschung enthüllt haben, die Lilly so gerne geheim halten wollte. Ich weiß, dass ich auch schuld bin. Vielleicht hätte ich die Fragen irgendwie umgehen können."


show shizu behind_frustrated_close onlayer master at Position(xpos=0.85)
with charachange

"Shizune hat Hanakos Stillschweigen auch bemerkt und wird ebenso nervös. Ich kann es in ihrem Gesicht sehen. Es ist eigenartig, dass Shizune trotz ihrer Taubheit früher als Misha bemerkt hat, dass Hanako ungewöhnlich still ist."


show shizu adjust_frown_close onlayer master
with charachange

shi "…"


show misha sign_smile_close onlayer master
with charachange

mi "Hanako, du bist zu still~. Du musst auch mitarbeiten~!"
mi "Irgendwann arbeiten wir vielleicht an einem größeren Projekt – an einem, das so groß ist, dass es wert ist, gefeiert zu werden, so mit Eis oder Kuchen. Wenn du nicht mitarbeitest, nehmen wir dich nicht mit~!"


"Ich weiß, dass sie versuchen, sie zu ärgern, um sie aus ihrem Panzer zu locken, aber ich glaube nicht, dass dieser Ansatz bei Hanako funktioniert. Dadurch fühlt sie sich nur noch schlechter."


hi "Leute, ärgert sie nicht so."


show shizu behind_smile_close onlayer master
with charachange

shi "…"


show misha hips_smile_close onlayer master
with charachange

mi "Hicchan, das ist alles nur Spaß~! Shicchan meint, sie ärgert sowieso jeden."


show misha perky_smile_close onlayer master
show shizu behind_blank_close onlayer master
with charachange

"Sie halten sich aber jetzt zurück. Misha wechselt das Thema, indem sie mir wieder eine Frage stellt. Als ich sehe, wie kompliziert das Problem ist, das ihr zu schaffen macht, weiß ich nicht, ob es ein gekonntes Ausweichmanöver war oder purer Zufall."


"Es kostet uns viel mehr Zeit als nötig, weil Shizune mir immer wieder widerspricht, während ich versuche, es Misha zu erklären, und Misha glaubt ihr eher als mir. So viel eher sogar, dass sie vergisst zu übersetzen, was Shizune sagt."


hi "Hey, uns geht irgendwie die Zeit aus. Wir sollten uns ein bisschen beeilen."


stop music fadeout 4.0

show misha perky_confused_close onlayer master
with charachange

mi "Hicchan~! Da hörst du dich fast ein bisschen wie Shicchan an…"


hi "Nur weil ich auf meine Uhr geschaut habe? Gott, ist das wirklich alles, was nötig ist? Zeiteinteilung, und schon bin ich der Schülerratspräsident?"


stop ambient fadeout 4.0

$ ksgallery_unlock("evul hanako_breakdown_down")
scene evbg hanako_breakdown onlayer master:
    truecenter
    1.0
    zoom 1.05 subpixel True
    easein 8.0 zoom 1.0
show evfg hanako_breakdown_down onlayer master:
    truecenter
    1.0
    zoom 1.1 subpixel True
    easein 8.0 zoom 1.0
with silentwhiteout

play music music_tragic fadein 8.0

"Ich schaue zu Hanakos Tisch, um nachzusehen, wie es bei ihr läuft – und erstarre. Unsere Blätter sind voll mit Gleichungen, aber Hanako hat erst die Hälfte. Es scheint, als hätte sie die letzten zwanzig Minuten nichts geschrieben."


"Sobald ich mir dessen bewusst werde, will ich mich selbst treten, weil ich so dumm war."


"Ich hätte wissen sollen, dass jemand, der so zerbrechlich ist wie Hanako, das Geschehene nicht einfach so abschütteln kann, aber ich war zu ungeduldig, von einer unangenehmen Situation wegzukommen, um es zu bemerken."


"Sie hat sich die letzte halbe Stunde langsam zurückgezogen und ich habe nichts bemerkt. Ihren Stift hält sie noch in der Hand, aber sie spielt nicht mit ihm, wie sie es sonst immer tut. Hanako bewegt sich einfach gar nicht."


$ ksgallery_unlock("evul hanako_breakdown_up")
scene evbg hanako_breakdown onlayer master:
    truecenter
    1.0
    zoom 1.0 subpixel False
show evfg hanako_breakdown_up onlayer master:
    truecenter
    zoom 1.0 subpixel False
with charachange

"Nur weil sie sich langsam weglehnt, als sie merkt, dass Shizune, Misha und ich sie anschauen, weiß ich, dass sie immer noch bei Bewusstsein ist. Wir schauen weg, und zumindest bei mir ist es teilweise aus Scham, weil es soweit gekommen ist."


"Obwohl sie von außen völlig teilnahmslos wirkt, weiß ich, dass es in ihrem Inneren anders aussieht."


"An was denkt sie wohl, während sie immer mehr versucht, sich in sich selbst zurückzuziehen, als ob sie durch reine Willenskraft irgendwie verschwinden könnte?"


"Alle sehen sie jetzt an; werfen zwischendurch kurze Blicke auf sie, während sie ihrer Arbeit den letzten Schliff verpassen."


"Misha versucht, sie zu fragen, was los ist, aber das macht es nur noch schlimmer. Wenn sie nicht an ihrem Sitz festgefroren wäre, würde sie wahrscheinlich sofort aus dem Raum stürzen."


$ ksgallery_unlock("evul hanako_breakdown_closed")
show evfg hanako_breakdown_closed onlayer master
with charachange

"Misha fragt so laut, dass sie im ganzen Klassenzimmer zu hören ist, und einen Moment lang bin ich kurz davor, sie anzuschnauzen, weil ich mir vorstellen kann, wie es Hanakos Gefühlslage noch verschlechtert."


"Natürlich würde das die Situation nur noch verschlimmern."


"Ich hatte geglaubt, Hanako sei stärker geworden – und das ist sie auch – aber es war noch nicht genug, und ich wollte einfach zu sehr daran glauben."
"Jetzt hat sie Angst, allein inmitten des Klassenzimmers, und es gibt nichts, was ich tun kann, ohne noch mehr Aufmerksamkeit auf sie zu lenken."


"Es bringt mich zur Weißglut. Misha macht sich Sorgen, und sogar Shizune beißt auf ihrer Lippe herum."


"Keiner von uns weiß, wie wir mit dieser Situation umgehen sollen, also beschließe ich, Mutou zu rufen. Er kann das wohl besser beurteilen als wir."


"Ich schaue auf und schaffe es, Mutou auf mich aufmerksam zu machen, indem ich ihm stillschweigend signalisiere, dass er herkommen soll."
"Ich will so wenig Aufhebens wie möglich darum machen, denn wenn es etwas gibt, das die Situation noch verschlimmert, dann ist das, mehr Aufmerksamkeit auf sie zu ziehen."


"Ich weiß, dass Hanako sehen kann, wie jeder unsere Gruppe anstarrt. Besonders sie. Weil sie wissen, falls es ein Problem gibt, muss sie der Ursprung sein."


"Alle kennen sie, und es wäre das Erste, was ihnen in den Sinn kommen würde. Durch ihren Ruf als Schulschwänzer ist sie als ungewöhnlicher Mensch abgestempelt worden, sogar auf dieser ungewöhnlichen Schule."


"Wer weiß, wie viele Male sie schon angestarrt wurde. Vielleicht fürchtet sie sich vor den Blicken so sehr, weil sie schon so oft gesehen hat, wie die Klasse sie anstarrt, und weicht deswegen ängstlich vor ihnen zurück."


"Die Zeit, die Mutou braucht, um herüberzukommen, muss Hanako wie eine Ewigkeit vorkommen. Sie sieht aus, als würde sie jederzeit umfallen."


scene bg school_scienceroom onlayer master
show shizu behind_blank_close onlayer master:
    tworight
    xpos 0.85 ypos 1.09
show misha perky_sad_close onlayer master:
    twoleft
    xpos 0.15 ypos 1.09
show hanako emb_downtimid_close onlayer master:
    center
    ypos 1.09
show muto irritated behind shizu onlayer master at tworight
with dissolve

"Mutou setzt leise zur Frage an, was los sei, aber er fängt sich gerade noch, als er Hanako sieht."


show misha perky_sad_close onlayer master
with charachange

mi "Haben… wir sie verärgert…?"


show muto normal onlayer master
with charachange

mu "Keine Sorge."


"Mutou bückt sich, nachdem er Misha beruhigt hat, und sieht Hanako aufmerksam ins Gesicht."


show muto smile onlayer master
with charachange

mu "Hi, Ikezawa. Kann ich dir irgendwie helfen?"


"Seine Stimme ist gedämpft und einfühlsam. Alle um Hanako herum benehmen sich jetzt so ungewöhnlich, dass die ganze Klasse bemerkt hat, dass mit ihr etwas nicht stimmt."


show muto smile_close onlayer master
with characlose

"Hanako antwortet nicht, daher legt Mutou sanft eine Hand auf ihre Schulter."


show hanako emb_downsad_close onlayer master at centertremble_sit
with charachange

"Bei seiner Berührung fängt sie an zu zittern, aber sie sieht nicht einmal auf. Hanako starrt weiter auf die Gleichungen auf ihrem Tisch, wobei ihr Blick so unkonzentriert wirkt, dass ich kaum glaube, dass sie sie erkennen kann."


"Es geht ihr schlechter als vorher. Ich denke daran, dass sie kaum eine Stunde zuvor fast normal mit ihm reden konnte."


show muto irritated onlayer master
show hanako emb_downsad_close onlayer master:
    center
    ypos 1.09
with charadistant

"Mutou verzieht leicht das Gesicht, als er wieder aufsteht. Jetzt, da sein Gesichtsausdruck sich verändert hat, kann ich erkennen, dass er von den Geschehnissen auch nicht gerade unberührt geblieben ist."


show muto normal onlayer master
with charachange

"Er atmet tief ein, um sich zu beruhigen, und spricht dann mit sehr ruhiger Stimme. Ich bin etwas beeindruckt, wie schnell er die Kontrolle über die Lage übernimmt."


mu "Ist das alles? Es ist also alles in Ordnung?"


play ambient sfx_crowd_indoors fadein 8.0

"Mutous Worte scheinen an niemand Bestimmten gerichtet zu sein. Sie hören sich jedoch überzeugend genug an, sodass die meisten, die zu Hanako hergesehen haben, sich jetzt wegdrehen und sich wieder ihrer Arbeit widmen."


"Er wirft kurz einen Blick nach links und nach rechts. Einige an den Tischen um uns herum glotzen immer noch neugierig, aber ansonsten scheinen wir es geschafft zu haben, nicht allzu viel Aufmerksamkeit auf uns zu ziehen."


show muto smile onlayer master
with charachange

"Mutou bemerkt, dass ich mich auch umschaue und setzt sein übliches gekünsteltes Lächeln auf."


mu "Ich glaube, Ikezawa zuliebe wäre es ganz gut, sie irgendwohin zu bringen, wo die anderen nicht in ihrer Nähe sind."


mu "Nakai, Hakamichi; könntet ihr Ikezawa bitte aus dem Klassenzimmer bringen? Ich sorge dafür, dass alle ruhig bleiben, also kümmert euch nur um sie und sonst nichts, okay?"


show misha sign_confused_close onlayer master
show shizu behind_blank_close onlayer master
with charachange

"Er sieht Misha an und gibt ihr damit zu verstehen, dass sie seine Worte für Shizune übersetzen soll, aber bis dahin ist sie mit ihrer Übersetzung schon fast fertig."
"Es ist bemerkenswert, wie wenig sie beim Benutzen der Gebärdensprache nachdenken muss, da sie ansonsten immer noch ziemlich verwirrt wirkt."


show muto invis onlayer master
show misha perky_confused_close onlayer master
show shizu behind_blank_close onlayer master:
    xpos 0.85
    ypos 1.0
with dissolvecharamove

hide muto onlayer master
hide shizu onlayer master
with None

show shizu behind_blank_close behind hanako onlayer master:
    tworight
    xpos 0.85
    ypos 1.0
with None

"Nickend stehen Shizune und ich auf und nehmen Hanako in unsere Mitte. Mutou geht einen Schritt zurück, um uns Platz zu machen, und redet mit einem Tisch hinter uns, weil dort einige angefangen haben, darüber zu tuscheln, was gerade passiert."


show hanako emb_downsad_close onlayer master at center
with charamove

"Wir sehen uns an und beugen uns gemeinsam herunter, wobei wir jeweils einen Arm über unsere Schultern legen und anheben."


show hanako emb_downsad_close onlayer master:
    twoleft
    xpos 0.35
show shizu behind_blank_close onlayer master at tworight
show bg school_scienceroom onlayer master at bgleft
show misha invis_close onlayer master at Position (xpos=-0.1)
with dissolvecharamove

"Wir zwei gehen langsam los, um sicherzustellen, dass wir ihr nicht aus Versehen wehtun. So sehr wir auch versuchen, es normal aussehen zu lassen, bin mir sicher, dass wir viel mehr Blicke auf uns hätten, wenn Mutou nicht für Ablenkung sorgen würde."


"Glücklicherweise erreichen wir schließlich die Tür und gehen hindurch."


stop ambient fadeout 0.5

scene bg school_hallway3 onlayer master
with locationchange

"Es ist niemand draußen, also gehen wir den Gang entlang. Es sieht nicht so aus, als würde sie sich dadurch wohler fühlen als zuvor im Klassenzimmer. Ich frage sie, ob sie sich einfach hinsetzen will."


show shizu adjust_happy_close onlayer master at tworight
show hanako emb_downsad_close onlayer master:
    twoleft
    xpos 0.35
with charaenter

"Eine Weile stehen wir einfach auf der Stelle und warten, bis sie etwas sagt. Kurz streichelt Shizune zaghaft Hanakos Schulter, aber es kommt keine Reaktion."


show shizu behind_smile_close onlayer master
with charachange

"Schließlich schüttelt sie leicht ihren Kopf, als Shizune es noch einmal versucht. Wir schauen sie beide an, daher kriegen wir es sofort mit."


show shizu adjust_happy_close onlayer master
show hanako emb_sad_close onlayer master
with charachange

"Shizunes Hand verweilt wieder auf Hanakos Schulter, als sie zu sich kommt und ihren Kopf hebt, um zwei sehr besorgt und ängstlich dreinschauende Gesichter vor sich zu finden."


"Sie sieht uns eine Weile schweigsam an. Zunächst befürchte ich, sie würde ausflippen oder etwas Übertriebenes tun, aber diese Sorgen stellen sich als unberechtigt heraus."
"Ihr fast lebloser Gesichtsausdruck weicht langsam einer normaleren, zurückhaltenden Schüchternheit."


show hanako emb_downtimid_close onlayer master
with charachange

"Wortlos senkt sie ihren Kopf, wobei sie ihre Augen ausweichend zur Seite richtet. Sie wirkt verlegen, fast beschämt."


"Ich will etwas sagen, irgendetwas, um zu helfen, aber das kann ich nicht. Ich weiß nicht wirklich, was gerade passiert ist, geschweige denn, was der Grund dafür war. Ich fühle mich hilflos, und schäme mich dafür, nicht von Nutzen zu sein."


show shizu basic_normal2_close onlayer master
with charachange

"Shizune seufzt und sieht mich dann an. Sogar ohne Worte glaube ich zu wissen, was sie will."


hi "Ich bringe Hanako zu Doc. Ist das für dich in Ordnung?"


"Ich versuche mit den Händen zu erklären, was ich vorhabe, aber ich habe nicht das Gefühl, dass es wirklich richtig bei ihr ankommt."


show shizu behind_frustrated_close onlayer master
with charachange

"Als Antwort auf meine Versuche macht Shizune ein düsteres Gesicht und bestätigt damit meinen Eindruck."


show shizu adjust_frown_close onlayer master
with charachange

"Entschieden stößt sie mit dem Finger durch die Luft, zuerst zeigt sie auf mich, dann auf Hanako, und dann zu den Treppen. Sie wartet, bis ich nicke, bevor sie auf sich selbst zeigt und dann auf die Tür zum Klassenzimmer."


"Ich habe das Gefühl, Shizune ist darin viel besser als ich."


show shizu behind_blank_close onlayer master
with charachange

"Ich nicke ihr zu, immerhin ist ihre Idee dieselbe wie meine. Shizune macht Anstalten zu gehen, verlässt uns aber erst, nachdem sie eine Zeit lang Hanako angeschaut hat."


hide shizu onlayer master
with dissolve

hi "Ist es okay für dich, wenn ich dich zu Doc bringe?"


stop music fadeout 4.0

"Weder nickt Hanako noch sagt sie etwas, aber sie steht auf der Stelle von selbst auf, und als ich losgehe, folgt sie mir gehorsam. Ich habe schon über Katatonie gelesen, aber dieses Mal sehe ich es, glaube ich, mit eigenen Augen."



"Sie wirkt sehr müde. Nach allem, was passiert ist, ist das keine Überraschung."


stop music fadeout 1.0
scene bg school_nurseoffice onlayer master
with locationskip

"Nachdem Hanako schweigend ihre Schuhe ausgezogen und sich auf das Bett im Krankenzimmer gelegt hat, lassen Doc und ich sie allein."


play music music_hanako fadein 0.3

"Er zieht den Vorhang hinter uns zu. Wir beide setzen uns, und leise erzähle ich ziemlich ausführlich, was vorgefallen ist."


"Ich will verstehen, was passiert ist, und Doc ist wohl meine beste Chance, eine Erklärung zu bekommen."


show nurse concern onlayer master at center
with charaenter

"Immer wieder nickt er während meiner Ausführungen, wobei er gegen Ende besorgt aussieht."


nk "Das alles zu sehen, muss dich ziemlich beunruhigt haben."


hi "Das zu bestreiten wäre eine Lüge. Ich weiß, dass sie einen Zusammenbruch hatte, aber ich kann überhaupt nicht nachvollziehen, warum das passiert ist oder warum sie sich so benimmt."


"Er nickt, aber sein Gesicht ist düster."


hi "Sie wissen es auch nicht?"


nk "Also… Ja und nein. Es ist kompliziert."


nk "Ich nehme an, du hast irgendwann schon einmal vom Begriff der ärztlichen Schweigepflicht gehört?"


nk "In dieser Hinsicht ist das ein heikles Thema. Ich werde es ganz direkt sagen; das ist eine Angelegenheit für Ikezawa, mich und ihre Therapeutin."


"Ich will widersprechen, besinne mich aber eines Besseren. Ich will seine Worte nicht anerkennen, aber wenn ich rational darüber nachdenke, ergibt es absolut Sinn, was er sagt."


hi "Ich verstehe."


show nurse neutral onlayer master
with charachange

nk "Gut, gut. Ich wünschte, ich könnte mehr für dich tun, aber ich glaube, Ikezawa braucht jetzt keinen, der seine Nase in ihre Vergangenheit und ihre Gefühle steckt. Sie braucht nur jemanden, der für sie da ist."


nk "Sie braucht einen Freund."


show nurse fabulous onlayer master
with charachange

nk "Wenn du mich fragst, war es gut, dass du sie hergebracht hast. Hört sich auch so an, als wären du und deine Freunde gut mit der Situation fertig geworden."


show nurse grin onlayer master
with charachange

nk "Ich würde dir ja einen Lolli oder Sticker als Belohnung geben, aber dafür bist du vielleicht ein bisschen zu alt."


"Er zeigt mir ein freches Grinsen. Offensichtlich tut er sein Bestes, die Atmosphäre aufzuheitern. Mir ist nicht wirklich zum Lachen zumute, aber er schafft es, mir ein kleines Lächeln zu entlocken."


hi "Danke. Ähm, haben Sie was dagegen, wenn ich hier bei Hanako bleibe?"


show nurse neutral onlayer master
with charachange

nk "Der Gedanken ehrt dich, aber ich glaube, es wäre besser, sie vorerst in Ruhe zu lassen."


nk "Sie kann heute Abend wieder zurück in ihr Zimmer, dann könntest du sie besuchen."


"Ich nicke und stehe auf. Es fühlt sich an, als könnte ich in Gegenwart von Doc nichts anderes tun, als im zuzustimmen, aber das war mit den Ärzten im Krankenhaus genauso."


stop music fadeout 3.0

scene bg school_nursehall onlayer master
with locationchange

"Es ist ein weiter Weg zurück zum Klassenzimmer, da mein Kopf sich durch die ganzen plötzlichen Geschehnisse sehr schwer anfühlt."


scene bg school_scienceroom onlayer master
with locationskip

play music music_dreamy fadein 2.0
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

"Sogar als ich das Klassenzimmer wieder betrete, denke ich über Hanako nach."


"Bei dem Gedanken, wie ich mit ihr umgehen soll, habe ich einen Eisblock im Magen. Ich weiß immer noch nicht, was ich zu ihr sagen soll, wenn ich sie wieder sehe."


"Zum Glück schenkt mir die Klasse nicht viel Beachtung. Es gibt ein paar fragende Blicke, aber im Großen und Ganzen scheinen nicht viele zu wissen, was passiert ist."


"Mutou zieht seine Augenbrauen hoch, um auf sich aufmerksam zu machen, als ich an seinem Tisch vorbeikomme."


show muto normal onlayer master at center
with charaenter

mu "Nakai… Ich nehme an, Ikezawa ist jetzt im Krankenzimmer?"


hi "Ja. Ich habe sie hingebracht, und Doc meinte, sie soll sich ausruhen."


"Mutou nickt, womit er mir versichert, dass ich das Richtige getan habe. Er kratzt sich kurz am Kinn, bevor er von seinem Tisch aufsteht."


show muto smile onlayer master
with charachange

mu "Leute, ich will, dass ihr mit der Übung weitermacht. Nakai, komm bitte mit auf den Flur."


"Er spricht mit gedämpfter Stimme, aber er scheint sich nicht viel anders zu benehmen als sonst. Vielleicht ist das von einem Lehrer zu erwarten."


stop ambient fadeout 1.0
scene bg school_hallway3 onlayer master
with locationchange

"Als wir auf den Flur gehen, fällt mir auf, dass er einen kurzen Blick nach links und nach rechts wirft, um nachzusehen, ob irgendwelche Schüler herumlaufen."


"Im Gang ist fast kein Geräusch zu hören, aber mir fällt nichts ein, als darauf zu warten, dass Mutou anfängt zu reden."


show muto smile onlayer master at center
with charaenter

mu "Nakai, was denkst du, ist die Aufgabe dieser Schule?"


hi "Äh… Auf die Bedürfnisse von behinderten Schülern eingehen?"


show muto normal onlayer master
with charachange

"Mutou kratzt sich am Kopf, während er ihn schüttelt."


mu "Nein. Wenn wir das tun wollten, hätten wir eine komplett neue Schule gebaut. Einstöckig. Sprechende Tafeln. All so was."


mu "Sieh dich um, Nakai. In dieser Schule geht es darum, euch allen eine Zukunft zu geben, die euch bei normaler Schulausbildung verwehrt bleiben würde."


hi "Hm?"


mu "Sieh es mal so. Wenn wir wollten, dass du deinen Abschluss machst und direkt danach im Krankenhaus liegst, glaubst du, wir würden uns dann so viel Mühe geben?"


"Die Unverblümtheit in Mutous Worten verblüfft mich, wodurch ich meine aktuelle Lage ganz vergesse."


hi "Nein…"


mu "Ganz recht. Wir wollen, dass ihr alle als nützliche Mitglieder der Gesellschaft von dieser Schule geht."


hi "Ich… kann nicht ganz folgen, glaube ich…"


show muto smile onlayer master
with charachange

mu "Ich setze große Hoffnungen in dich, Nakai. Du bist bisher womöglich der einzige Schüler, der meinen Unterricht versteht."


"So etwas sollte ein Lehrer nicht so einfach zugeben."


mu "Du könntest es mit deinen wissenschaftlichen Forschungen auf der Universität sehr weit bringen. Hast du das jemals in Betracht gezogen?"


hi "Nein, hab ich nicht."


mu "Nun, was hast du dir denn vorgestellt? Also für deine Zukunft…"


hi "Ich… muss sagen, über meine Zukunft hab ich noch nicht viel nachgedacht."


"Für einen Augenblick kommt mir Lilly in den Sinn, die mir dieselbe Frage gestellt hat."


"Es sind nur knapp mehr als fünf Monate vergangen, seit ich nach Luft ringend am Boden gelegen habe. Es ist zu früh, um über die Zukunft nachzudenken, und außerdem erscheinen mir Hanakos Probleme im Moment viel größer."


show muto irritated onlayer master
with charachange

"Mutou seufzt missbilligend und fährt dann fort."


show muto normal onlayer master
with charachange

mu "Sieh es als eine Chance. Du hast hier grenzenlose Möglichkeiten, gute Lehrer und zusätzlich noch Doc und seine Mitarbeiter."


mu "Du solltest nichts anderes im Kopf haben als deine Zukunft."


hi "Äh… ja."


"Als ich den Kopf hebe, um ihm ins Gesicht zu sehen, kommt mir ein Gedanke; es ist fast als wäre Mutou dem eigentlichen Problem völlig ausgewichen."


hi "Verzeihen Sie, aber warum scheint sich keiner der Mitarbeiter dafür zu interessieren, wenn Hanako den Unterricht schwänzt?"


hi "Ich habe mehr als einmal beobachtet, wie Sie ihr beim Verlassen des Unterrichts zugesehen haben. Sollten Sie nicht wenigstens etwas sagen?"


show muto smile onlayer master
with charachange

mu "Na ja, Nakai, es ist nicht ganz so einfach. Jeder Schüler hier hat eigene Bedürfnisse; wenn das nicht so wäre, hätten wir hier nicht diese Schule."


mu "Ich würde dich zum Beispiel nicht im Unterricht behalten, wenn du Atemprobleme hast, oder?"


hi "Aber das ist nicht…"


"Mutou schneidet mir das Wort ab, bevor ich überhaupt daran denken kann, meinen Satz zu beenden."


show muto normal onlayer master
with charachange

mu "In Ikezawas Fall ist das ziemlich ähnlich. Aber anstatt einer Herzmassage oder einem Schrittmacher braucht sie Zeit und Abstand."


mu "Das Kollegium wurde schon am Tag ihrer Ankunft davon in Kenntnis gesetzt, deshalb lassen wir sie immer gehen, wenn ihr danach ist."


show muto smile onlayer master
with charachange

mu "Und auch wenn sie keine Top-Noten bekommt, scheint sie alle ihre Klausuren zu bestehen, also hat es ihr Lernvermögen nicht beeinflusst. Reicht das nicht?"


"Ich will widersprechen, aber ich kann keinen Fehler in seiner Argumentation entdecken. Obwohl ihr Leiden auf den ersten Blick rein körperlich wirkt, waren die Auswirkungen auf ihre Psyche die schlimmsten."


"Es gefällt mir aber immer noch nicht. Wälzt er die Verantwortung für ihr Problem nicht einfach nur ab? Sicherlich kann sie nicht ihr ganzes Leben so weitermachen."


show muto normal onlayer master
with charachange

mu "Ich verstehe, dass du an so etwas vielleicht noch nicht gewöhnt bist. Es war eine große Umstellung für dich. Allerdings ist euer Abschluss in weniger als einem Jahr."


mu "Vielleicht musst du dich an diese Schule gar nicht gewöhnen. Wenn du den Kopf unten hältst, bin ich sicher, dass du in deinen Klausuren gut genug abschneidest."


"Benommen nicke ich – eher um zu zeigen, dass ich zuhöre, als um zuzustimmen. Ich dachte, ich wäre dabei, mich an dieser Schule einzuleben, aber jetzt scheint es, als hätte ich mich da geirrt."


hi "Aber… was ist mit Hanako?"


mu "Ich glaube… nun, ich hoffe, dass ihre Leistung gut genug ist, dass sie tun kann, was sie will."


mu "Was das ist, weiß ich nicht. Nicht alle Schüler verlassen die Schule mit einer Vorstellung davon, was sie tun möchten… leider."


"Er achtet darauf, das letzte Wort zu betonen, als wäre es nicht schon unmissverständlich genug, und lässt mir einen Augenblick, um mir seine Worte durch den Kopf gehen zu lassen."


show muto smile onlayer master
with charachange

mu "Heute war ein anstrengender Tag für dich, und ich bezweifle, dass du dich nach allem, was passiert ist, sonderlich gut konzentrieren kannst. Daher erlaube ich dir, den Rest des Tages freizunehmen."


mu "Bisher hast du in diesem Kurs gute Noten. Deswegen glaube ich kaum, dass du Probleme haben wirst, den verpassten Stoff nachzuholen."


"Er lächelt mich an, als er mich lobt, als ob er es wiedergutmachen will, dass er bei seiner Belehrung eben so ernst war."


mu "Hol deine Sachen. Ich sehe dich dann morgen."


hi "Okay. Danke."


stop music fadeout 5.0

hide muto onlayer master
with charaexit

"Nach Mutous umständlichem Vortrag sind meine Gedanken völlig durcheinander. Ich bin immer noch nicht näher dran herauszufinden, was ich tun kann, um Hanako zu helfen – wenn überhaupt bin ich nach Mutous Worten noch viel verwirrter."


"Mich stört auch immer noch, dass Hanako mindestens genauso viel Hilfe von Shizune, der Feindin ihrer Freundin, bekommen hat wie von mir, aber ich weiß nicht, ob das einfach nur männlicher Stolz ist oder ein echtes Problem."


scene bg school_scienceroom onlayer master
with locationchange

"Während ich Hanakos und meine Sachen aus der Klasse hole, versuche ich weiterhin, meine Gefühle einzuordnen."


"Ich will ihr sagen, dass ich sie verstehe, und dass ich für sie da bin… aber obwohl ich das gestern erst getan habe, ist es mir jetzt nicht möglich."


"Ich wünschte, ich könnte."





label de_H15:

scene bg school_dormhisao_ss onlayer master
with shorttimeskip

play music music_night fadein 1.0

"Ich liege auf meinem Bett und versuche, meine Gedanken zu sammeln."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
window hide
nvl show dissolve

n "\n\nNach Hanakos Panikattacke bin ich dabei, unsere Beziehung noch einmal gründlich zu überdenken, und auch was ich über sie weiß."


n "Es war schwer genug für mich, vier Monate im Krankenhaus zu verbringen. Ein Blick auf ihre Narben sagt mir, dass sie viel länger in einem war als ich."


n "Wie dem auch sei, ich weiß so gut wie nichts über ihre Vergangenheit. Sie hat mir über den Hausbrand erzählt, aber nur das Nötigste."


n "Und was ist mit ihrer Familie? Danach habe ich Lilly immer noch nicht gefragt; es gab keine gute Gelegenheit, das Thema anzusprechen."


n "Ich weiß nicht, wo sie aufgewachsen ist, oder wie ihre alte Schule war. Ich weiß auch nichts über ihre alten Freunde, ihre Wünsche und Ziele. Nicht einmal welches Essen sie mag, oder welchen Musik- und Filmgeschmack sie hat… all die kleinen Dinge, die ich über meine alten Freunde wusste."


n "\n\nWas habe ich nur die ganze Zeit gemacht, in der ich mit ihr und Lilly zusammen war?"


$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(0.1, 0.0, channel="sound")
play sound sfx_normalbell

nvl clear
nvl hide dissolve
window show

"In der Ferne höre ich die Schulglocken, die das Ende des Unterrichts einläuten. Mit ein bisschen Glück merkt Lilly recht bald, dass weder Hanako noch ich da sind und geht zurück ins Wohnheim."


$ renpy.music.set_volume(0.5, 0.0, channel="sound")
stop music fadeout 0.5
play sound sfx_phone

"Mein Handy fängt an zu klingeln und reißt mich aus meinen Gedanken. Es erschreckt mich richtig, weil ich selten angerufen worden bin, seit ich hier bin."



scene bg school_dormhisao_blurred_ss onlayer master
show phone mobile onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

hi "Hallo, hier ist Hisao Nakai…"


li "Oh, Hisao. Bin ich froh, dass ich dich erreicht habe. Du warst nirgends, wo wir sonst sind, da dachte ich, das wäre die schnellste Möglichkeit, dich zu erreichen."


"Ich hätte mir wohl denken können, dass es Lilly ist, da sie eine der wenigen ist, denen ich meine Nummer gegeben habe. Sogar über das Telefon hört sich ihre Stimme leicht nervös an."


hi "Ich… Hanako und ich sind heute früher aus dem Unterricht. Sie hatte eine Art Panikattacke…"


"In der Leitung wird es still. Wenn das Rauschen im Hintergrund nicht wäre, hätte ich gedacht, dass Lilly aufgelegt hat."


li "Ich verstehe. Könntest du zu meinem Zimmer kommen? Ich würde gerne mit dir reden."


hi "Klar. Ich… ich würde es sogar sehr begrüßen, ein bisschen mit dir zu reden."


li "Gut… gut. Ich… habe auch ein paar schlechte Nachrichten. Ich glaube, wir sollten persönlich darüber reden."


"Es ist schwer, durch Lillys Stimme die Ernsthaftigkeit der Situation einzuschätzen. Sie klingt meistens so ruhig, aber das könnte sowohl etwas Gutes als auch etwas Schlechtes sein, je nachdem, wie man es betrachtet."


hi "Okay, bin gleich da."


show phone mobile onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao_ss onlayer master
show phone mobile onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone onlayer master
with None

"Ich schnappe mir Hanakos Schulsachen von meinem Tisch und mache mich direkt zu Lillys Zimmer auf."


scene bg school_girlsdormhall onlayer master
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2

"Ich klopfe an die Tür, und sie bittet mich gleich herein."


play music music_drama fadein 4.0

scene bg school_dormlilly onlayer master
show lilly basic_sleepy onlayer master:
    center
    ypos 1.17
with locationchange

"Lilly sitzt an dem Tisch in ihrem Zimmer. Sie sieht ein bisschen mitgenommen aus; wegen der schlechten Nachrichten, schätze ich."


"Ihrer einladenden Geste folgend setze ich mich ihr gegenüber hin und lege Hanakos Sachen auf den Tisch."


show lilly basic_weaksmile onlayer master
with charachange

li "Also, es hat keinen Sinn, wenn wir beide warten. Würdest du anfangen, Hisao? Was ist heute passiert?"


"Meine Erinnerung an den Vorfall fängt schon an zu verblassen, aber ich beschreibe es Lilly, so gut ich kann."


"Dass wir Hanako mit in die Gruppe aufgenommen haben, die Fragerei von Shizune und Misha, dass unser Ausflug in die Stadt aufgedeckt wurde, und die darauffolgende Panikattacke."


"Shizunes Reaktion erwähne ich fast nur beiläufig, aber Lilly scheint irgendwie erfreut zu sein, das zu hören."


"Ich schätze, Konkurrenten werden nicht ohne Grund zu Konkurrenten. Es muss eine Geschichte dazu geben, aber jetzt ist nicht die Zeit, sie zu erforschen."


show lilly basic_concerned onlayer master
with charachange

li "Verstehe. Sie hatte gesagt, ihre Stunden bei der Therapeutin helfen, aber ich hatte so meine Zweifel. Das ist ziemlich schade."


show lilly basic_reminisce onlayer master
with charachange

li "Ihr Geburtstag hat schon früher Probleme bereitet, aber ich hatte gehofft, es wäre durch deine Gegenwart besser geworden, und durch die intensivere Therapie."


show lilly basic_oops onlayer master
with charachange

li "Wo ist Hanako jetzt?"


hi "Das letzte Mal, als ich sie gesehen habe, war sie im Krankenzimmer. Ich schätze, sie ist mittlerweile wieder in ihrem Zimmer."


show lilly basic_sleepy onlayer master
with charachange

li "Sie war weder in der Bibliothek noch im Teezimmer, als ich nachgesehen habe, also ist das auch meine Vermutung."


hi "Du sagtest, du hast auch ein paar schlechte Nachrichten… Was ist los? Betrifft es Hanako?"


"Lilly verlagert ihre Position; die Art des Körpers zu sagen, dass sie nach den richtigen Worten sucht."


show lilly basic_concerned onlayer master
with charachange

li "Meine Tante ist schwer krank geworden. Ich fürchte, ich werde zurück nach Schottland fliegen, um sie zu besuchen und ein bisschen Zeit mit meiner Familie zu verbringen."


hi "Was? Geht es ihr gut? Wann fliegst du?"


show lilly basic_reminisce onlayer master
with charachange

li "Ich bin nicht ganz sicher, wie es ihr im Moment geht, aber das Letzte, was ich gehört habe, war, dass sie stabil ist. Ich werde am Samstag abreisen; das war der früheste Flug, den ich kriegen konnte."


"„Stabil”. Das ist der Code für „muss im Krankenhaus bleiben”. Ich war lange genug „stabil”, um das zu wissen – und um zu wissen, dass es nicht unbedingt heißen muss, dass man in guter Verfassung ist, sondern lediglich, dass sich nichts verändert."


"Das Gute ist, dass „stabil„ viel besser ist als „in kritischem Zustand”. Zumindest steht sie nicht am Rande des Todes."


hi "Stabil… Das klingt beruhigend."


show lilly basic_sad onlayer master
with charachange

li "Ja, aber das heißt, ich werde an Hanakos Geburtstag nicht hier sein."


show lilly basic_concerned onlayer master
with charachange

li "Ich wollte es dir jetzt erzählen, damit du dir etwas ausdenken kannst, bevor wir es Hanako sagen. Nach den heutigen Ereignissen bin ich aber nicht einmal sicher, ob es ein Problem wäre, wenn wir die Party einfach abblasen."


hi "Ich… glaube nicht, dass das eine so gute Idee ist. Hanako weiß jetzt schon, dass wir eine Party geplant haben; das wieder zurückzunehmen, erscheint mir falsch."


hi "Außerdem sollten wir etwas wegen deiner Abreise machen, oder?"


show lilly basic_weaksmile onlayer master
with charachange

li "Bei dir hört es sich so an, als ob ich nicht mehr zurückkommen würde. Wenn alles gut geht, sollte ich nur eine Woche weg sein, vielleicht auch zwei."


hi "Das ist zumindest eine gute Nachricht."


show lilly basic_oops onlayer master
with charachange

li "Was schlägst du in Anbetracht dessen dann vor?"


hi "Angesichts der Umstände glaube ich nicht, dass Karaoke wirklich angemessen ist. Du gehst nicht gerade aus dem schönsten Grund weg, da würde es sich falsch anfühlen, zu viel Spaß zu haben."


hi "Was hast du an ihrem Geburtstag letztes Jahr gemacht?"


show lilly basic_reminisce onlayer master
with charachange

li "Letztes Jahr… konnte ich sie buchstäblich nicht aus ihrem Zimmer rauskriegen. Sie hatte die Tür abgeschlossen."


li "Alles, was ich tun konnte, war Essen für sie draußen stehen zu lassen, damit sie wenigstens richtig isst."


"Ich glaube, so deprimiert habe ich Lilly noch nie gesehen. Ich habe Mitleid mit ihr, wenn ich daran denke, wie niedergeschlagen sie sein muss, weil sie ihrer besten Freundin nicht helfen kann."


hi "Vielleicht wäre es dann besser, die Party zu schmeißen, bevor du abreißt?"


show lilly basic_weaksmile onlayer master
with charachange

li "Das klingt wirklich nach der einfachsten Möglichkeit."


hi "Ich denke, wir sollten Hanako wenigstens davon erzählen – sowohl von deiner Reise als auch ihrer Party. Außerdem hab ich noch ihr Zeug aus dem Unterricht."


show lilly basic_smile onlayer master at center
with dissolvecharamove

li "Gutes Argument. Sollen wir gleich jetzt zu ihr gehen?"


hi "Ich… ich glaube, das wäre eine gute Idee."


"Ein Teil von mir will Hanako unbedingt sehen. Das letzte Mal, als ich sie gesehen habe, sah sie aus wie der wandelnde Tod, und in den letzten paar Stunden wurde ich allein bei dem Gedanken daran innerlich zerrissen."


stop music fadeout 4.0

scene bg school_girlsdormhall onlayer master
with locationchange

"Schweigend stehen wir auf und verlassen Lillys Zimmer. Hanakos Zimmer ist nebenan im selben Gang."


play sound sfx_doorknock2

"Auf unser leichtes Klopfen erhalten wir keine Antwort, aber es stellt sich heraus, dass die Tür offen ist. Lilly hält kurz inne, als die Klinke unter ihrer Hand sich unerwartet bewegt, und öffnet dann die Tür."


play music music_moonlight fadein 0.5

scene bg school_dormhanako_ni onlayer master at Fullpan(8.0)
with locationchange

"Hanakos Zimmer ist erschreckend kahl und monoton. Die schlichten weißen Wände sind nicht dekoriert, auf dem Bett liegt eine einfache dunkelblaue Decke, und nur ein paar Bücher, Papiere und rein zweckmäßige Gegenstände sind auf den Regalen."


"Sogar ihr Bettbezug ist einfarbig. Der ganze Raum wirkt so gedrückt wie Hanakos Charakter."


scene ev hanako_cry_closed onlayer master
with whiteout

"Hanako selbst liegt zusammengekauert auf dem Bett. Sie weint vielleicht nicht im Moment, aber ihre Augen sind fest verschlossen, um sie davon abzuhalten, und die Spuren ihrer Tränen sind immer noch auf ihren geröteten Wangen zu sehen."


"Leise gehe ich hinein und stelle ihre Tasche auf ihrem Tisch ab, da ich Angst habe, sie zu erschrecken."


li "Hallo, Hanako. Hisao hat mir erzählt, was heute passiert ist… Alles in Ordnung mit dir?"


show ev hanako_cry_away onlayer master
with charachange

"Hanakos Augen öffnen sich, wenn auch nur ein bisschen."


ha "Ich… bin okay…"


show ev hanako_cry_open onlayer master
with charachange

"Sie legt ihren Kopf leicht schief, um mich anzusehen, wobei sie meinen Gesichtsausdruck sieht, bevor ich ihn verstecken kann."


ha "E-Entschuldigt… d-dass ich euch S-Sorgen mache."


show ev hanako_cry_closed onlayer master
with charachange

ha "W-Wirklich… m-mir geht's j-jetzt gut…"


"Sie sieht weder so aus, als würde es ihr gut gehen, noch hört sie sich so an, obwohl sie immerhin ruhiger wirkt als zuvor. Sie sieht immer noch so aus, als könnte der kleinste Lufthauch sie emotional zusammenbrechen lassen."


hi "Ich hab es doch schon mal gesagt, oder? Du musst dich dafür nicht entschuldigen."


li "Hisao hat Recht. Wir… Ich… hätte so etwas wie eine Geburtstagsfeier nicht vor dir verheimlichen sollen."


"Ich kann sehen, wie Hanako bei dem Wort erzittert. Lilly bemerkt die Stille, die darauf folgt, und kniet sich zu Hanako herunter."


li "Mir sollte es leid tun, Hanako."


show ev hanako_cry_away onlayer master
with charachange

"Hanako öffnet ihre Augen und blickt Lilly prüfend an. Eine Weile beobachtet sie sie, wobei sie ihr Gesicht mit ihren dunklen, analytischen Augen genau betrachtet."


play sound sfx_rustling

scene bg school_dormhanako_ni onlayer master
show hanako emb_downsad_ni onlayer master:
    center
    ypos 1.3
    easein 1.0 ypos 1.15
with locationchange

"Lilly muss bei ihr wohl den richtigen Eindruck hinterlassen haben, da sie sich weit genug aufrappelt, um sich auf dem Bett aufzustützen und sich an dessen Kante zu setzen."
"Hanako zerbricht sich über viele Dinge den Kopf, aber in erster Linie darüber, dass sie anderen Schwierigkeiten macht."


show bg school_dormhanako_ni onlayer master at bgright
show hanako emb_downsad_ni onlayer master:
    xpos 0.6
    ypos 1.15
with charamove

show lilly invis onlayer master:
    twoleft
    xpos 0.4
with None

show lilly basic_weaksmile_ni onlayer master at Position(ypos=1.17)
with dissolvecharamove

"Als Lilly Hanakos Bewegungen hört, beugt sie sich nach vorne und tastet nach der Bettkante. Schließlich setzt sie sich neben sie und nimmt mit beiden Händen Hanakos linke."


"Das Gefühl, fehl am Platz zu sein, wenn die zwei zusammen sind, hat mit der Zeit nachgelassen, aber ab und zu ist es immer noch präsent. Das ist einer dieser Momente, denke ich."


hi "Lilly, wenn ich gehen soll…"


show hanako emb_sad_ni onlayer master
with charachange

ha "Bitte… bleib…"


show lilly basic_surprised_ni onlayer master
with charachange

"Wir beide, Lilly und ich, sind überrascht, dass Hanako ihren Mut zusammennimmt. Ich kann ihr nur ein halb gemurmeltes „Okay” als Antwort geben und setze mich auf ihren Schreibtischstuhl."


show lilly basic_concerned_ni onlayer master
with charachange

li "Hanako, ich fürchte, ich habe schlechte Nachrichten."


"Lilly verkündet jetzt also die Neuigkeiten. Da Hanako mir einen so klaren Vertrauensbeweis ausgesprochen hat, denkt Lilly vielleicht, dass der Moment gerade gut ist – oder zumindest, so gut er nur sein kann."


show lilly basic_sad_ni onlayer master
with charachange

li "Meine Tante ist krank geworden, darum muss ich für eine Weile zu meiner Familie."


show hanako cover_worry_ni onlayer master
with charachange

"Die Reue in Hanakos Gesicht weicht Sorge."


ha "Deine… Familie… Du meinst in Schottland, oder?"


show lilly basic_reminisce_ni onlayer master
with charachange

li "Genau. Akira und ich werden am Samstag abreisen."


show hanako defarms_strain_ni onlayer master
with charachange

ha "A-Also gehst du weg?"


show lilly basic_weaksmile_ni onlayer master
with charachange

li "Ich werde nicht lange weg sein. Wahrscheinlich nur eine Woche oder zwei. Ich bin zurück, bevor du es merkst, und Hisao ist doch da, stimmt's?"


hi "Genau, ich gehe nirgendwohin."


show hanako basic_worry_ni onlayer master
with charachange

"Hanako scheint das kaum zu trösten, aber sie schafft es, irgendwo in sich ein wenig Entschlossenheit aufzutreiben."


ha "W-Wird deine Tante wieder gesund?"


show lilly basic_reminisce_ni onlayer master
with charachange

li "Ich bin mir nicht sicher."


"Es wird still. Es ist deprimierend, dass es das Unglück eines anderen ist, das Hanako wieder aus ihrem Tief zieht."


"Ich bringe den anderen Anlass zur Sprache, aus dem wir hier sind, um zumindest teilweise von der trostlosen Atmosphäre abzulenken, die den Raum durchdringt."


hi "Jedenfalls dachten wir, es wäre eine gute Idee, eine Abschiedsparty für Lilly zu machen, und wir könnten dann auch gleich… ja…"


"Ich bremse mich, bevor ich ihren Geburtstag erwähnen kann, da er in ihr derartig erbitterte Gefühle auszulösen scheint."


"Lilly drückt sanft Hanakos Hand."


show lilly basic_weaksmile_ni onlayer master
with charachange

li "Ist das okay für dich, Hanako? Nichts Großes oder Aufwendiges, nur eine kleine Feier in meinem Zimmer."


show hanako def_worry_ni onlayer master
with charachange

ha "A-Also nur in der Schule? Nur wir?"


show lilly basic_smileclosed_ni onlayer master
with charachange

li "Genau, nur wir drei. Wenn du willst, kann ich auch Akira fragen, ob sie kommt."


show hanako basic_normal_ni onlayer master
with charachange

ha "O-Okay. D-Du bist nur eine Woche weg?"


show lilly basic_smile_ni onlayer master
with charachange

li "Eine Woche oder zwei, ja. Ich verspreche dir, dass es nicht länger dauern wird."


show hanako cover_distant_ni onlayer master
with charachange

ha "O-Okay…"


"Die meisten wären bestürzt, davon zu hören, dass ein Familienmitglied eines Freundes krank geworden ist, und empfänden Freude bei einer Party, aber bei Hanako wirkt es, als wären beide Ereignisse auf demselben Level."


hi "Also gut. Du siehst aus, als könntest du etwas Ruhe gebrauchen, Hanako. Vielleicht wäre es am besten, wenn wir fürs Erste alle in unsere Zimmer zurückgehen."


show lilly basic_weaksmile_ni onlayer master
with charachange

li "Du weißt, wenn irgendetwas ist, kannst du immer mit mir oder Hisao reden, ja?"


"Lillys Stimme hört sich nachdenklich an, was für einen so selbstbewussten Menschen wie sie ungewöhnlich ist."


show hanako basic_bashful_ni onlayer master
with charachange

ha "Ich… verstehe. Danke, Lilly, Hisao."


show lilly basic_smileclosed_ni onlayer master at Position(ypos=1.0)
with dissolvecharamove

li "Na gut. Gute Nacht, Hanako."


show hanako basic_normal_ni onlayer master
with charachange

ha "Nacht…"


stop music fadeout 4.0

scene bg school_girlsdormhall onlayer master
with locationchange

"Ich atme lange aus, nachdem die Tür sich hinter uns geschlossen hat. Es fühlt sich ein bisschen so an, als wäre ich lange unter Wasser gewesen und hätte erst jetzt wieder zum Atmen an die Luft kommen können."


show lilly basic_concerned onlayer master at center
with charaenter

"Lilly scheint es auch nicht gut zu gehen. Sie sieht blass und schlapp aus."


hi "Bist du okay?"


li "Ich bin nur ein bisschen müde. Es war… hektisch in letzter Zeit."


hi "Hast du überhaupt geschlafen? „Ein bisschen müde” hört sich untertrieben an, so wie du aussiehst."


show lilly basic_sleepy onlayer master
with charachange

li "Ich glaube, ich habe ein paar Stunden Schlaf vor dem Unterricht gekriegt. Ich bin in Ordnung."


"Ich habe ein schlechtes Gewissen, Lilly jetzt so zu drängen. Ich glaube, wir sind beide durch die ganzen Ereignisse ziemlich müde geworden."


hi "Ich denke, du solltest dich ausruhen. Es war ein anstrengender Tag, und es ist nicht gut für deinen Teint, wenn du aufbleibst."


show lilly basic_weaksmile onlayer master
with charachange

li "Nett, dass du dir Sorgen machst, Hisao. Also dann, gute Nacht."


hi "Okay. Nacht, Lilly."


hide lilly onlayer master
with charaexit

"Als Lilly die Tür zu ihrem Zimmer öffnet, mache ich mich auf den Weg zu meinem eigenen."


scene ev hanako_cry_closed_fb onlayer master
show noiseoverlay onlayer master
with flash

"Als ich den stillen Gang entlanggehe, kriege ich das Bild von Hanako nicht aus meinem Kopf. Aufgewühlt und bemitleidenswert liegt sie hilflos da und hat Tränen auf ihren Wangen."
"Ich hatte begonnen zu glauben, sie sei einfach ein normaler, wenn auch extrem schüchterner Mensch, aber ihre Probleme sitzen viel tiefer."


"Wenn sie so zerbrechlich und verletzlich ist, wäre es nicht richtig, unsere Beziehung noch weiter voranzutreiben als jetzt. Mehr als ihr Freund muss ich nicht sein, um sie zu beschützen – um zu verhindern, dass so etwas nie wieder passiert."


"Die Tatsache, dass meine Gefühle für sie vielleicht darüber hinausgehen… das ist nicht mehr von Bedeutung. Hanako ist mir sehr wichtig, und deswegen kann ich sie nicht ausnutzen."


"Aber trotzdem… ich spüre immer noch einen Stich, wenn ich daran denke."


scene bg school_girlsdormhall onlayer master
with flash

"Fürs Erste muss ich schlafen. Morgen wird hoffentlich ein besserer Tag."


scene black onlayer master
with dissolve



label de_H16:

scene bg school_scienceroom onlayer master
with locationchange

"Hanako ist auffälliger, wenn sie abwesend ist, als wenn sie im Klassenzimmer ist."


"Ich kann fühlen, wie ihr leerer Tisch nach mir ruft. Ich ertappe mich dabei, andauernd über meine Schulter zu blicken, in der Hoffnung, dass ich halluziniere und Hanako auf magische Weise auftaucht."


"Sie achtet darauf, im Unterricht so wenig wie möglich aufzufallen, und obwohl es ihr in letzter Zeit besser geht, hat sich das nie geändert."


"Im Unterricht achtet nie jemand auf sie, und jetzt, wo sie nicht da ist, bemerkt niemand, dass sie fehlt. Es ist, als ob sie einfach nie existiert hätte."


"Lilly hat ja gesagt, dass Hanakos Fernbleiben vom Unterricht nichts Ungewöhnliches war, bevor ich sie getroffen habe, aber es ist trotzdem ziemlich beunruhigend."


play sound sfx_normalbell

"Das Läuten am Ende des Unterrichts lässt mich aufschrecken. Erst jetzt merke ich, dass Misha mich mit ihrem Bleistift in die Seite stupst, um meine Aufmerksamkeit zu erregen."


show shizu invis onlayer master:
    center
    xpos 0.4
show misha invis_close onlayer master:
    center
    xpos 0.1
with None

show bg school_scienceroom onlayer master at bgright
show misha sign_smile_close onlayer master at Position(xpos=0.2)
show shizu behind_blank onlayer master at center
with dissolvecharamove

play music music_normal fadein 3.0

mi "Hallo… ist jemand zu Hause~?"


hi "Hey, hör auf damit."


show misha hips_grin_close onlayer master
with charachange

mi "Ah! Na also! Willkommen zurück auf der Erde, Hicchan~!"


hi "Wovon sprichst du?"


show misha hips_smile_close onlayer master
with charachange

mi "Du warst so in deiner eigenen Welt; ich dachte schon, du willst Kontakt mit Außerirdischen aufnehmen."


"Ich habe letzte Nacht nicht wirklich viel geschlafen, darum zweifle ich nicht an Mishas Worten."
"Ich bin mir nicht sicher, ob es an den Nebenwirkungen meiner Medizin, Hanakos gestriger Panikattacke, meiner Sorge um sie, oder an allen drei Gründen zusammen lag."


"Müde gähne ich und stütze mein Kinn mit meiner Hand ab, weil ich daran erinnert wurde, wie schlecht ich geschlafen habe."


show misha perky_confused_close onlayer master
with charachange

mi "Hey, ist wirklich alles okay bei dir? Das gestern hat mich auch ein wenig aus dem Konzept gebracht…"


hi "Ja… Ja, glaub ich. Ich wollte aber wieder mit Hanako reden."


show misha perky_smile_close onlayer master
with charachange

mi "Hast du sie gestern Abend gesehen?"


hi "Ja, Lilly und ich haben mit ihr geredet."


hi "Ähm, das hört sich vielleicht ein bisschen seltsam an, aber kannst du Shizune „danke” sagen? Sowohl von mir… als auch von Lilly."


"Ich weiß, dass Lilly Shizune genau genommen nicht gedankt hat, aber ihrer Reaktion letzter Nacht konnte ich erkennen, dass sie es wollte. Zumindest will ich das glauben."


show shizu adjust_blush onlayer master
with charachange

show shizu cross_angry onlayer master
with charachange

shi "…"


show misha sign_confused_close onlayer master
with charachange

mi "Äh… Ich glaube, was Shicchan sagen will, ist „Keine Ursache.”"


"Die wütenden Gesten und erröteten Wangen von Shizune verraten mir, dass sie etwas völlig anderes gesagt hat. Bei ihrem offensichtlich verlegenen Gesichtsausdruck muss ich schmunzeln."


show misha perky_confused_close onlayer master
with charachange

mi "Was ist so lustig, Hicchan~? War es etwas, was wir gesagt haben?"


hi "Nein, nein, das ist es nicht. Ich habe nur gerade gedacht, wie süß Shizune manchmal sein kann."


show misha cross_laugh_close onlayer master
with charachange

mi "Wahahaha~! Du hast Recht~! Shicchan ist wirklich süß, besonders wenn sie es nicht sein will!"


"Mir fällt auf, dass Misha ihre Antwort nicht gebärdet. Wahrscheinlich kann Shizune noch so süß sein – dass sie wirklich wütend wird, will sie trotzdem nicht riskieren."


show shizu adjust_frown onlayer master
with charachange

"Wie dem auch sei, Shizune beruhigt sich schnell und gebärdet Misha etwas anderes."


show shizu behind_smile onlayer master
with charachange

shi "…"


show misha perky_smile_close onlayer master
with charachange

mi "Oh~? Okay… Hicchan, Shicchan will, dass du mit uns zu Abend isst."


hi "Abendessen, ja?"


"Damit ich nicht von ihren flehenden Blicken beeinflusst werde, drehe ich mich ein Stück von ihnen weg und denke darüber nach."


"Die Einladung ist definitiv verlockend. Ein Abendessen mit zwei süßen Mädels ist jedenfalls keine schlechte Sache. Der Gedanke an Hanako, wie sie in ihrem Zimmer eingesperrt ist, spukt mir aber andauernd im Kopf herum."



hi "Tut mir leid, ich muss passen."


show misha perky_sad_close onlayer master
with charachange

mi "Oooch…"


show shizu behind_frown onlayer master
with charachange

"Misha gibt meine Antwort nicht weiter, aber Shizune bemerkt es auch so schnell genug und macht ein enttäuschtes Gesicht."


show shizu basic_normal2 onlayer master
with charachange

"Sie bewegt ihre Arme, vermutlich um irgendwie zu protestieren oder mich zu zwingen, aber sie überlegt es sich anders und tippt zweimal auf Mishas Schulter. Als Misha sich umdreht, ist ein Schulterzucken alles, was Shizune zu der Sache zu sagen hat."


show misha perky_confused_close onlayer master
with charachange

mi "Na ja. Es ist deine Entscheidung, Hicchan."


hi "Ich verspreche, dass ich ein andermal mit euch esse, falls das hilft."


show misha perky_smile_close onlayer master
show shizu behind_blank onlayer master
with charachange

"Mishas Miene hellt sich bei meiner Aussage auf, aber Shizune teilt ihre Begeisterung nicht. Sie lässt Misha durch ein Zucken ihres Kopfes wissen, dass sie ihr folgen soll, und hebt einfach die Hand, um mir schweigend zum Abschied zu winken."


hide misha onlayer master
hide shizu onlayer master
with charaexit

stop music fadeout 3.0

"Als die zwei zur Tür rausgehen, erwidere ich die Geste, bis sie außer Sicht sind."


"Ich dachte nicht, dass sie so enttäuscht sein würden, und deshalb habe ich ein bisschen ein schlechtes Gewissen dabei, sie abgewiesen zu haben. Trotzdem, ich habe zu tun."


scene bg school_girlsdormhall onlayer master at right
with shorttimeskip

"Im Mädchenwohnheim ist es heute besonders chaotisch, da einige Mädchen im Gemeinschaftsraum im Erdgeschoss lautstark Spiele spielen und fernsehen. Ich kann ihre Stimmen sogar jetzt hören, wo ich vor Hanakos Tür stehe."


"Ein seltsamer Gegensatz zu der Leere, die in ihrem Stockwerk herrscht. Die Stimmen von unten lassen es noch einsamer erscheinen."


"Ich hatte gehofft, Hanako wäre heute im Unterricht. Erst recht, nachdem Lilly und ich letzte Nacht mit ihr geredet haben. Aber ich denke, ich sollte ihr das nicht übel nehmen."
"Es war ein ziemlich unangenehmer Vorfall, und ihn am eigenen Leib zu erfahren, muss noch viel schlimmer gewesen sein."


scene bg school_dormhanako_ni onlayer master
show hanagown worry_close onlayer master:
    center
    xpos 0.39
show expression Solid("#00000022") onlayer master
show hanako_door_base onlayer master at right
show hanako_door_door onlayer master at left
with locationchange

play sound sfx_doorknock2

"Da ich nicht weiß, wie sie sich fühlt, atme ich kurz durch, bevor ich ein paar Mal fest an ihre braune Tür klopfe."


"Alles, was ich tun kann, ist herumzustehen und warten, wobei ich versuche, nicht ängstlich zu werden."


"Als einige Sekunden vergehen, glaube ich schon, sie würde vielleicht schlafen und hätte mein Klopfen nicht gehört, aber bevor ich meine Hand heben kann, um noch einmal zu klopfen, bewegt sich die Türklinke."


play sound sfx_dooropen

show hanako_door_door onlayer master:
    xpos -0.05
with charamove

"Die Tür öffnet sich einen Spalt, und ein Auge taucht darin auf. Der Spalt ist gerade groß genug, dass es hindurch spähen kann. Ich bin mir sicher, dieses Mädchen würde ein Guckloch in ihre Zimmertür einbauen, wenn es erlaubt wäre."


"Ich stehe nur da und lächle sie an. Ich denke, Worte wären hier doch nicht wirklich hilfreich."


"Sie erwidert das Lächeln, wobei sie mich wortlos anschaut. Der Spalt ist nicht groß genug, um ihr Gesicht zu sehen, und ich kann nur raten, was sie gerade denkt."


"Es vergeht einige Zeit, während wir uns gegenseitig anschauen. Nur die fröhlichen Geräusche aus dem Erdgeschoss sind zu hören."


hide hanagown onlayer master
with charaexit

"Ich weiß nicht, wie lange es dauert, aber schließlich verschwindet das Auge. Ich frage mich immer noch, ob sie mich reinlässt oder aussperrt, doch dann geht die Tür langsam knarrend auf."


play sound sfx_door_creak

show hanako_door_door onlayer master:
    easeout 1.0 xpos -0.2
show hanako_door_base onlayer master:
    easeout 1.0 xpos 1.1
show bg school_dormhanako_ni onlayer master:
    center
    easeout 1.0 xpos 0.55
with None

scene bg school_dormhanako onlayer master
show hanagown normal onlayer master at center
with silentwhiteout

play music music_comfort

"Jetzt, wo ich sie und das Schlafzimmer hinter ihr voll im Blick habe, ist das Erste, was mir auffällt, dass Hanakos Haare ganz feucht sind. Sie hat vor kurzem geduscht. Das wird durch den Duft von Shampoo, der mir entgegenweht, noch offensichtlicher."


"Sie sieht neugierig aus, als ob sie nicht genau weiß, was sie von mir halten soll. Trotzdem bin ich mir nicht wirklich sicher, was sie denkt."


"Es fühlt sich so an, als wäre sie für lange Zeit weg gewesen, jetzt zurückgekehrt, und keiner von uns weiß, was wir einander sagen sollen."


show hanagown distant onlayer master
with charachange

"Hanako fällt auf, dass sie starrt, und schaut peinlich berührt weg, bevor sie sich zur Seite dreht und auf ihre Füße schaut. Ich beschließe, das als Einladung zu nehmen und gehe an ihr vorbei ins Zimmer. Dabei schließe ich hinter mir die Tür."


"Ich kann sehen, wie sie mit ihren Händen in den Falten des übergroßen Bademantels herumfummelt, der ihr von den Schultern hängt. Ich versuche, mich darauf zu konzentrieren, was ich sagen will, aber ihr Duft benebelt meine Sinne."


"Zu meiner Überraschung bin es nicht ich, sondern Hanako, die das Schweigen bricht."


show hanagown normal onlayer master
with charachange

ha "Warum…"


hi "Weil… ähm…"


"… Warum bin ich hergekommen?"


"Ich habe mir Sorgen um Hanako gemacht, also bin ich zu ihrem Zimmer gekommen. Sie hat mich – wie erhofft – hereingelassen und dann… was? Was wollte ich tun? Was wollte ich sagen?"


"Warum habe ich das nicht durchdacht, bevor ich hergekommen bin…"


"Ich will wieder gutmachen, was ich meiner Meinung nach verursacht habe – zumindest teilweise. Ich will ihr wieder näherkommen und sie glücklich sehen. Wie kann ich das tun, wenn ich überhaupt nichts von ihr weiß?"


"Ich frage mich… Ich frage mich, ob Iwanako genauso gefühlt hat, als sie mich in dem sterilen, pastellblauen Krankenbett liegen sah."


hi "Ich äh… ich… ähm…"


"Ein tiefer Seufzer hilft, meine Nerven ein wenig zu beruhigen, und ich höre auf zu stammeln. Ich glaube nicht, dass ich in der Gegenwart eines anderen jemals so nervös war."
"In diesem Zustand kann ich mir schwer vorstellen zu lügen, und auch wenn ich mich dazu überwinden könnte, würde Hanako es sofort durchschauen."


hi "Ich weiß es nicht. Ich… wollte dich einfach sehen, glaube ich."


show hanagown smile onlayer master
with charachange

"Ihre Finger werden ruhig, was mich leicht überrascht. Als ich zu ihrem Gesicht aufschaue, zeigt sie mir ein süßes Lächeln und nickt. Diese Antwort war für sie befriedigend?"


ha "Ähm… Wo du schon da bist…"


show hanagown distant_blush onlayer master
with charachange

ha "Ich würde gern… eine Runde Schach mit dir spielen…"


"Fast lasse ich ungläubig meinen Mund offen stehen, weil sie einfach nur Schach spielen will, nachdem ich mir so viele Gedanken gemacht habe. Als ich ihr ins Gesicht blicke, sehe ich dort ein unsicheres Lächeln und begreife, dass es mehr als das ist."


"Sie hätte die Tür nicht aufmachen müssen. Sie hätte sie zumachen können, sobald sie mein Gesicht gesehen hat. Sie hätte mich bitten können zu gehen."


"Sie hätte mich an vielen Stellen zurückweisen können, aber sie hat es nicht getan. Jetzt will sie mit diesem gelassenen Gesichtsausdruck, dass ich dasselbe Spiel spiele, das wir gespielt haben, als wir zum ersten Mal allein zusammen waren."


"Eine Welle der Erleichterung strömt durch meinen Körper."


"Alles wird gut. Hanako hat mich in ihre Welt gelassen. Ich glaube, solange wir auf diese Weise zusammen sein können, wird alles gut."


hi "Es wäre mir ein Vergnügen."


stop music fadeout 2.0

scene black onlayer master
with dissolve



label de_H17:

scene bg school_girlsdormhall onlayer master
with locationchange

"Endlich ist der Tag gekommen, an dem Hanakos Geburtstagsparty stattfinden soll."


"Um ehrlich sein, freue ich mich darauf, Hanako und Lilly wieder in ihren Pyjamas zu sehen."
"Hanakos Bademantel finde ich mittlerweile ziemlich süß, auch wenn er etwas konservativ ist, und Lillys Shorts und ihr dünnes seidenes Top sind eine hübsche Kombination."


"Aber die Party leidet ein wenig unter der Erinnerung an Hanakos Reaktion darauf."


"Ich verstehe immer noch nicht wirklich, was passiert ist, da ich nur eine vage Vorstellung von den möglichen Ursachen habe. Ich glaube, die Antwort darauf zu finden, wird nicht so einfach sein, wie sie zu fragen."


play sound sfx_doorknock2

"Mit diesen Gedanken in meinem Kopf klopfe ich an die Tür neben Hanakos."


li "Bist du das, Hisao?"


hi "Ja, ich bin's."


"Ich kann das Getrappel von Schritten hören, die sich der Tür nähern, und kurz darauf ein Klicken, als das Schloss entriegelt wird. Ich glaube nicht, dass ich Lillys Tür jemals verschlossen erlebt habe. Das macht mich ein wenig misstrauisch."


"Als die Tür aufgeht, ist der Anblick… etwas enttäuschend für eine Geburtstagsparty."


play music music_ease fadein 1.0

scene ev lilly_bedroom onlayer master
with locationchange

"Mit einem kurzen Lächeln und einem Nicken kehrt Hanako zur ihrem Platz am Tisch zurück, dann schließe ich die Tür und – in der Annahme, sie wollen es so belassen – sperre sie zu."


"Als ich das tue, fällt mir auf, dass das Bild vor mir einer abendlichen Teeparty gleicht. Genau so einer, wie die zwei sie sonst immer machen. Das sollte mich irgendwie nicht überraschen, denke ich."


scene ev lilly_bedroom_large onlayer master:
    ypos 0 xpos -860
with locationchange

"Zu meiner Erleichterung sieht Hanako einigermaßen entspannt aus. Die Auszeit vom Unterricht hat ihr wohl gut getan und ihr Zeit gegeben, sich ein wenig zu erholen."


scene bg school_dormlilly onlayer master
show lilly basic_smileclosed_paj onlayer master:
    twoleft
    ypos 1.2
show hanagown distant onlayer master:
    tworight
    ypos 1.17
with locationchange

"Ich setze mich zu den beiden an den niedrigen Tisch in der Mitte von Lillys Zimmer, während die bunte Teekanne zwischen uns vor sich hin dampft."


"Eine große braune Tasche neben Lilly erregt meine Aufmerksamkeit. Heimlich versuche ich ein paar Mal, einen Blick hinein zu werfen, aber von hier aus kann ich nicht richtig hineinsehen."


"Wenn ich Hanako so anschaue, ist sie anscheinend genauso neugierig wie ich."


hi "Hey, Lilly?"


"Lilly leert die Teetasse, die sie an ihre Lippen gehoben hat, setzt sie dann ab und schenkt mir ihre Aufmerksamkeit."


show lilly basic_smile_paj onlayer master
with charachange

li "Ja?"


hi "Ich frage mich nur, was das für eine braune Tasche ist…"


"Sie hält kurz inne und zeigt uns dann ein leicht freches Lächeln."


show lilly basic_cheerful_paj onlayer master
with charachange

li "Das ist Akiras Geschenk. Bedauerlicherweise sagte sie, dass sie arbeiten muss und nicht kommen kann."


"Lilly beugt sich vor und fühlt nach dem Gegenstand in der Tasche, bevor sie ihren Arm hebt."


"Ich ziehe eine Augenbraue hoch, als nicht nur einer, sondern zwei Gegenstände aus der Tasche auftauchen. Lilly hält die gläsernen Flaschenhälse mit einer Hand hoch. Darum war also die Tür zugesperrt."


show wine onlayer master:
    yalign 0.5 xanchor 0.0 xpos 1.0 alpha 0.0
    easein 1.0 alpha 1.0 xanchor 1.0
with Pause(1.0)

ha "Wein…"


"Zwei dumpfe Geräusche sind zu hören, als sie die Flaschen auf dem Tisch abstellt; eine rot, eine weiß. Ich möchte glauben, dass der Wein nicht echt ist – also alkoholfrei – aber wenn das so wäre, gäbe es keinen Grund, so vorsichtig zu sein."


hi "Alkohol? Wirklich? Bist du dir sicher, dass das eine gute Idee ist?"


show lilly basic_smileclosed_paj onlayer master
with charachange

"Lilly lächelt höflich und kichert. Das überzeugt mich nicht wirklich."


li "Das ist das Geschenk meiner Schwester. Ich weiß, es ist etwas fragwürdig, aber ein bisschen sollte nicht schaden."


"Wenn sich Lilly wirklich daran stören würde, hätte sie wohl nicht so einfach zugestimmt."
"Davon abgesehen, hatte ich Akira als ernst und verantwortungsbewusst eingeschätzt, ungefähr wie eine ältere Lilly, aber scheinbar lag ich falsch. Wir sind noch nicht einmal alt genug, um trinken zu dürfen."


hi "Na wenn das so ist, will ich mich nicht beschweren. Sie sehen auch gar nicht mal schlecht aus."


"Ich bin zwar kein Weinkenner, aber die Flaschen sehen zumindest schön aus."
"Abgesehen von dem ein oder anderen Glas Wein, das mir mein Vater heimlich beim Abendessen gegeben hat, habe ich nicht wirklich genug getrunken, um mich auszukennen."


show hanagown smile onlayer master
with None

show wine onlayer master:
    easeout 1.0 alpha 0.0 xanchor 0.0
with Pause(1.0)

hide wine onlayer master
with None

"Erstens das, und ich kann auch nicht behaupten, dass ich eine völlig weiße Weste habe. Hanakos Gesichtsausdruck nach zu urteilen, denkt sie genauso, und es ist ja sowieso ihr Geburtstag."


show lilly basic_smile_paj onlayer master
with charachange

li "Soll ich eine aufmachen?"


hi "Klar. Ich hole ein paar-{w=0.3}{nw}"


$ renpy.music.set_volume(0.5, 0.5, channel="music")
$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2

show lilly basic_displeased_paj onlayer master
show hanagown worry onlayer master
with vpunch

"Mein Herz setzt kurz aus, als drei mal laut an Lillys Tür geklopft wird. Hanakos Kopf schnellt herum, und Lilly schließt ihre Augen, während sie angespannt lauscht. Keiner von uns will auffliegen."


show lilly basic_oops_paj onlayer master
with charachange

li "Wer ist da?"


mystery "Lasst mich rein, mir ist kalt!"


show lilly basic_weaksmile_paj onlayer master
with charachange

$ renpy.music.set_volume(1.0, 6.0, channel="music")

"Lilly seufzt erleichtert und signalisiert Hanako, dass sie die Tür öffnen soll."


show hanagown invis onlayer master at tworight
with dissolvecharamove

hide hanagown onlayer master
with None

"Nachdem sie eine Weile an ihrem Bademantel gezupft hat, steht sie gehorsam auf. Anscheinend ist sie immer noch nicht ganz sicher, wer es ist, aber sie vertraut Lilly genug, um ihrer Bitte nachzukommen."


"Als Hanako die Tür öffnet, kann ich über ihre Schulter hinweg bloß eine in einen dunklen Anzug gekleidete, blonde Person erkennen."


mystery "Alles Gute zum Geburtstag, Hanako."


ha "D-Danke… Akira…"


"Hanako verbeugt sich leicht, wobei sie nervös mit ihren Fingern herumspielt. Das ist also Lillys mysteriöse Schwester."


show bg school_dormlilly onlayer master at bgleft
show lilly basic_weaksmile_paj onlayer master:
    left
    ypos 1.2
with charamove

show hanagown invis onlayer master at center
show akira invis onlayer master at right
with None

show hanagown normal onlayer master at Position(ypos=1.17)
show akira basic_smile onlayer master:
    right
    xpos 0.95
with dissolvecharamove

"Nachdem Akira die Tür hinter sich geschlossen hat, folgt sie Hanako zum Tisch, was mir jede Menge Zeit gibt, sie genau zu betrachten."


"Sie ist ungefähr genauso groß wie Hanako und hat kurze blonde Haare, die ziemlich grob geschnitten wurden. Das in Verbindung mit ihren eher bescheidenen Brüsten, dem männlichen Aufzug und der tiefen Stimme, lässt sie ziemlich androgyn wirken."


show akira basic_ending onlayer master at Position(ypos=1.18)
with dissolvecharamove

"Kurzerhand lässt sie sich mir gegenüber am Tisch hinplumpsen."


show lilly basic_smile_paj onlayer master
with charachange

li "Schön, dass du doch noch bei uns sein kannst, Akira. Konntest du von der Arbeit weg?"


show akira basic_boo onlayer master
with charachange

aki "Jepp. Ich muss gleich wieder zurück, aber ich konnte mir genug Zeit nehmen, um herzufahren."


show akira basic_smile onlayer master
with charachange

aki "Das ist dann also Hisao?"


"Sie lächelt mir selbstbewusst entgegen, also nicke ich höflich zurück. Wenn man bedenkt, dass sie direkt dazu übergegangen ist, meinen Vornamen zu benutzen, ist sie weit weniger förmlich als ihre Erscheinung vermuten lässt."


"Moment. Wenn sie bereits weiß, wer ich bin, dann heißt das, dass Lilly mit ihr über mich gesprochen hat. Ich frage mich, was sie erzählt hat."


show lilly basic_smileclosed_paj onlayer master
with charachange

li "Tut mir leid, euch nicht vorgestellt zu haben, Hisao. Das ist Akira Satou, meine ältere Schwester."


hi "Alles klar. Schön, dich kennenzulernen."


show akira basic_ending onlayer master
show hanagown worry onlayer master:
    0.1
    ease 0.1 ypos 1.15
    ease 0.1 ypos 1.17
with Dissolve(0.1)

"Akira klatscht laut in die Hände, was Hanako etwas erschreckt."


show akira basic_lost onlayer master
with charachange

"Akira hat es bemerkt und sieht für den Bruchteil einer Sekunde unsicher aus, bevor sie wieder in Fahrt kommt."


show akira basic_smile onlayer master
with charachange

"Erst jetzt fällt mir auf, dass Akira Hanakos Narben nicht übermäßig beachtet hat. Hanako scheint sich in Akiras Nähe auch wohlzufühlen, man könnte sogar sagen, sie sieht entspannt aus."


show akira basic_laugh onlayer master
with charachange

aki "Also dann, ich nehme an, die Geschenke sind angekommen? Es gibt keinen Grund zu warten, angesichts der Tatsache, dass Hisao und das Geburtstagskind richtig ungeduldig aussehen."


show lilly basic_cheerful_paj onlayer master
with charachange

"Lilly kichert, als ich mich verlegen wegdrehe, da ich ein bisschen beschämt bin, meine Neugierde nicht verbergen zu können."
"Hanakos Augen verraten mir allerdings, dass sie den Wein mit mir zusammen probieren will, darum versuche ich gleichgültig dreinzuschauen, was mir mehr schlecht als recht gelingt."


show lilly basic_smile_paj onlayer master
show akira basic_smile onlayer master
show hanagown distant onlayer master
with charachange

"Ohne große Mühe schafft Akira es, die erste Flasche zu entkorken, und Hanako holt ein paar Gläser, bevor ich diese mit Weißwein fülle."


"Irgendwo habe ich gehört, dass Weißwein weniger Alkohol hat als Rotwein, darum glaube ich, es wäre am besten, damit anzufangen."


hi "Auf Hanako, und auf Lillys Ausflug."


show lilly basic_giggle_paj onlayer master
show akira basic_laugh onlayer master
with charachange

$ doublespeak (li, aki, "Cheers!")


show hanagown smile onlayer master
with charachange

ha "C-Cheers…"


show lilly basic_smileclosed_paj onlayer master
show akira basic_smile onlayer master
with charachange

"Nachdem wir, wie es sich gehört, die Gläser erhoben haben, nehmen wir alle ein paar Schlucke von der blassgelben Flüssigkeit."
"Es schmeckt überhaupt nicht wie das Zeug, das ich mit meinen Eltern getrunken habe. Der Alkohol wird fast völlig vom fruchtigen Geschmack überdeckt."


"Vielleicht sollte richtiger Wein so schmecken. Es ist aber auch möglich, dass Akira einfach einen Wein ausgewählt hat, der eher unseren Geschmack trifft, da noch keiner von uns an Alkohol gewöhnt ist."


"Oder zumindest hoffe ich, dass das keiner von uns ist."


hi "Gar nicht schlecht. Ich hätte etwas… Herberes erwartet."


show akira basic_ending onlayer master
with charachange

aki "Wenn du ihn nicht gemocht hättest, hätte ich ein paar andere Sorten anbieten können."


hi "Klingt so, als würdest du dich mit Weinen auskennen."


show akira basic_smile onlayer master
with charachange

aki "Nur ein bisschen; ich stehe eher auf Bier."


show akira basic_laugh onlayer master
with charachange

aki "Das mit dem Trinken habe ich aber drauf."


"Als ob sie es beweisen wollte, schenkt sie sich nach, setzt das Glas an ihre Lippen und wirft ihren Kopf in den Nacken."


stop music fadeout 6.0

show akira basic_smile onlayer master
show hanagown normal onlayer master
with charachange

"Hanako und ich schauen schweigend zu, wie der ganze Inhalt des Glases in Akiras Mund verschwindet. Ich weiß nicht, ob mich das beeindruckt oder abschreckt, aber ich habe definitiv nicht den Drang, es nachzumachen."


show lilly basic_displeased_paj onlayer master
with charachange

"Lilly verzieht bei der Prahlerei ihrer Schwester ein wenig das Gesicht. Allerdings stelle ich fest, dass sie gleichzeitig an ihrem Glas nippt."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Also. Jetzt, da Akiras Geschenk geöffnet und gekostet wurde, sollen wir dann mit unseren weitermachen?"


show hanagown worry onlayer master
with charachange

ha "G-Geschenke?"


play music music_twinkle fadein 6.0

show lilly basic_smile_paj onlayer master
with charachange

li "Ganz genau, wir haben dir Geschenke besorgt. Es ist immerhin dein Geburtstag."


show lilly basic_smileclosed_paj onlayer master
with charachange

li "Das ist von mir."


"Lilly holt die sorgfältig verpackte Puppe unter ihrem Tisch hervor und überreicht sie Hanako."


"Hanako geht mit dem Geschenk um, als wäre es aus Glas. Sie dreht es vorsichtig um, um das Klebeband vom Geschenkpapier abzureißen. Schließlich löst sich das Papier von der Puppe und offenbart das Smaragdgrün des Puppenkleids."


show hanagown normal_blush onlayer master
with charachange

ha "Sie ist… wunderschön."


"Ich weiß nicht, welche Reaktion ich von Hanako erwartet habe. Da fast keine Puppen in ihrem Zimmer waren, dachte ich, dass sie sich nicht für sie interessieren würde, aber der Blick in ihren Augen sagt etwas anderes."


"Sie dreht die Puppe genauso behutsam um, wie sie mit dem Geschenkpapier umgegangen ist, als ob sie damit rechnen würde, dass sie in ihren Händen auseinanderbricht."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Ich bin froh, dass sie dir gefällt. Hisao hat sie ausgesucht, um ehrlich zu sein."


"Hanako erinnert sich plötzlich, dass sie nicht allein im Raum ist und löst sich aus dem Bann der Puppe."


show hanagown smile onlayer master
with charachange

ha "J-Ja, sie gefällt mir. D-Danke, Lilly und H-Hisao."


hi "Eigentlich hab ich etwas anderes für dich…"


"Ich greife in meine Tasche und hole das verpackte Schachspiel heraus."


hi "Bitte. Alles Gute."


show hanagown normal onlayer master
with charachange

"Vorsichtig setzt Hanako Lillys Puppe neben sich ab und öffnet mein Geschenk mit derselben Sorgfalt, die sie dem von Lilly zuteil werden ließ."




"Kurz darauf sind die karierten Quadrate des Schachbretts zu sehen, und Hanako fährt sanft mit ihren Fingern über die geschnitzte Oberfläche."


show hanagown normal_blush onlayer master
with charachange

ha "Oh!"


"Fast zufällig löst sie den Verschluss des Deckels, wodurch sie sich selbst erschreckt. Sie öffnet ihn und holt eine der grauen Figuren heraus."


"Sie scheint genauso in die Schachfiguren vertieft zu sein, wie sie es vorher in die Puppe war."


hi "Sie sind aus Koralle. Echte Korallen, ungefärbt – hat man mir gesagt."


show hanagown smile onlayer master
with charachange

ha "Danke, Hisao…"


hi "Kein Problem. Es ist immerhin dein Geburtstag."


show hanagown distant onlayer master
with charachange

ha "Richtig… mein Geburtstag…"


"Wieder wirkt Hanakos Reaktion etwas daneben, aber sie macht vorsichtig den Deckel zu."


show akira basic_lost onlayer master
with charachange



"Mir fällt auf, dass Akiras Lächeln langsam sehr gezwungen aussieht. Ich frage mich, ob sie etwas darüber weiß, was im Unterricht passiert ist, da sie in Hanakos Nähe scheinbar extrem vorsichtig ist."


hi "Wir müssen dann bald wieder gegeneinander spielen."


show hanagown smile onlayer master
with charachange

ha "Ja m-müssen wir."



show ev hanako_presents2 onlayer master:
    truecenter
    subpixel True zoom 1.1
    acdc_warp 10.0 zoom 1.0
with whiteout

"Sie nimmt die Puppe, die sie von Lilly bekommen hat, und drückt sie zusammen mit dem kleinen Schachbrett an ihre Brust, wobei sie die Figur oben draufstellt."


"Das scheint sie einigermaßen zu beruhigen, und wir sitzen einfach eine Weile stillschweigend da."


"Ich glaube, das ist einer der wenigen Momente, in denen ich sie wirklich glücklich erlebt habe, indem sie die Freundschaft von zwei Menschen so fest an ihre Brust drückt, wie sie kann."


show akira basic_boo onlayer master
show lilly basic_smile_paj onlayer master
with None

hide ev onlayer master
with locationchange

ha "Danke, Lilly. Danke, Hisao."


show hanagown worry_blush onlayer master
with charachange

"Während sie uns dankt, entgleitet Hanako die Schachfigur und sie tastet hektisch danach, um sie wiederzufinden."


show hanagown distant onlayer master
with charachange

"Sobald sie sie gefunden hat, legt Hanako das Schachspiel hin und trinkt hastig von ihrem Wein. Es ist, als ob die reale Welt plötzlich wieder in ihr Bewusstsein gerauscht wäre, und der schnellste Ausweg daraus war in dem Glas."


hi "Hey, langsam, du solltest den nicht so schnell trinken…"


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Das ist eine Party, Hisao…"


"Trotz dieser Aussage klingt etwas Sorge in ihrer Stimme mit. Schließlich nimmt Lilly es hin und folgt Hanakos Beispiel, wenn auch nicht so eifrig."


"Sie scheint kleine Schlückchen aus ihrem Glas zu nehmen und den Wein dann auf ihrer Zunge ruhen zu lassen, bevor sie ihn hinunterschluckt. Ich beschließe, dass das wohl die beste Methode ist, und tue es ihr gleich."


hi "Da das hier ja auch so eine Art Abschiedsparty für dich ist, hoffe ich, dass du deinen Ausflug zumindest ein bisschen genießen kannst, Lilly. Hoffentlich wird deine Tante gesund."


show hanagown worry onlayer master
with charachange

ha "I-Ich hoffe auch, dass deine Tante gesund wird, Lilly…"


show lilly basic_surprised_paj onlayer master
with charachange

"Lilly und ich sind etwas davon erstaunt, dass Hanako Lilly trotz ihrer eigenen familiären Situation so eifrig alles Gute wünscht. Ich bin leicht beeindruckt."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Oh, danke euch beiden. Ich werde meiner Familie auf jeden Fall eure Wünsche überbringen, wenn ich sie treffe."


show akira basic_smile onlayer master
with charachange

aki "Am Ende wird alles gut, Lilly. Mach dir keinen Kopf."


"Weil die Stimmung im Raum spürbar düsterer geworden ist, versuche ich das Thema zu wechseln."


hi "Na dann, sollen wir den Kuchen anschneiden?"


show hanagown normal onlayer master
show lilly basic_smileclosed_paj onlayer master
show akira basic_ending onlayer master
with charachange

"Mein zaghafter Vorschlag hat den gewünschten Effekt, denn alle werden deutlich lockerer."


show hanagown normal_blush onlayer master
with charachange

ha "J-Ja, bitte…"


show lilly basic_surprised_paj onlayer master
with charachange

li "Kuchen? Ich wusste gar nicht, dass es Kuchen gibt…"


hi "Ich hab einen besorgt, bevor ich hergekommen bin – mitsamt ein paar Snacks."


show lilly basic_giggle_paj onlayer master
with charachange

li "Gut gemacht, Hisao. Wenigstens einer von uns hat daran gedacht."


"Alle scheinen die Ablenkung zu begrüßen, also hole ich den Kuchen aus meiner Tasche und schneide ihn an."


"Ich hätte nicht gedacht, dass es so gut wäre, Wein mit Schokoladenkuchen zu mischen, aber keiner von uns scheint Einwände zu haben. Das Gespräch wird erst einmal unterbrochen, während wir essen."


"Anfangs war ich von der Idee nicht so begeistert; nach Hanakos Panikattacke habe ich das Schlimmste für heute Nacht erwartet, aber ich glaube, Lillys Idee, ihr schöne Erinnerungen an ihren Geburtstag zu schaffen, funktioniert."


"Hanakos Reaktion auf ihre Geschenke hat mir gezeigt, dass sie wirklich dankbar war."


show lilly basic_smileclosed_paj onlayer master
show akira basic_smile onlayer master
show hanagown drunknormal onlayer master
with shorttimeskip

"Hanako versucht, sich ein weiteres Glas Wein einzuschenken, aber verschüttet ein bisschen davon auf dem Tisch."
"Sie hatte jetzt schon ein paar Gläser; wenn man also bedenkt, dass sie vorher noch nie Alkohol getrunken hat, ist es kein Wunder, dass sie etwas beschwipst ist."


show hanagown drunksad onlayer master
with charachange

ha "E-Entschuldige Lilly… Ich wollte keine Sauerei machen… ich…"


hi "Keine Sorge, ich mach schon…"


$ ksgallery_unlock("unlock_ev lilly_hanako_hug_end")
show ev lilly_hanako_hug onlayer master:
    xalign 0.5 yalign 1.0 subpixel True
    easein 12.0 yanchor 0.0 ypos -0.15
with whiteout

"Lilly lehnt sich zur Seite und nimmt die jammernde Hanako behutsam in die Arme."


li "Schon okay, Hanako. Ich bin einfach froh, dass du da bist."


"Als Antwort nickt Hanako bloß schwach. Ich nehme an, es passt, dass es Lilly sein würde, die sie so unterstützt. Ich habe keine Ahnung, wie Hanako wäre, wenn sie das nicht täte."


"Die Zwei so zu sehen, lässt es mich schätzen, dass ich so einem intimen Moment beiwohnen darf. Selbst Akira kann bei dem Anblick nichts anders, als zu lächeln."


"Ich hätte nie gedacht, dass ich so schnell neue Freunde finden würde, und ich bin noch dankbarer, dass es ausgerechnet die Zwei sind, mit denen ich mich angefreundet habe."


stop music fadeout 3.0

show lilly basic_cheerful_paj onlayer master:
    xpos 0.02
    ease 1.0 xpos 0.0
show hanagown drunksmile onlayer master:
    xpos 0.48
    ease 1.0 xpos 0.5
with None

hide ev onlayer master
with locationchange

"Langsam lassen sie voneinander ab. Hanako beruhigt sich ein bisschen, während ich mich schnell wieder meiner Aufgabe widme."


"Unter Lillys Teeservice finde ich ein Tuch und fange an, den Wein aufzuwischen. Als ich jedoch fertig bin, haben Hanako und Lilly die andere Flasche entkorkt und ihre Gläser gefüllt."


show akira basic_ending onlayer master
with charachange

aki "Anscheinend findet ihr Gefallen am Wein. Aber denkt dran, es nicht zu übertreiben."


"Wir alle nicken brav und geben ihr Recht, aber ihre Mahnung wirkt ein bisschen unsinnig, angesichts der Tatsache, dass sie es ist, die Minderjährige mit Alkohol versorgt."


play music music_comedy fadein 0.5

show lilly basic_cheerfulblush_paj onlayer master at Position(xpos=0.0)
show hanagown drunkgiggle onlayer master at Position(xpos=0.5)
show akira basic_boo onlayer master
with shorttimeskip

"Das zweite Glas Wein geht schon viel schneller runter als das erste, und bevor wir es merken, ist die zweite Flasche leer. Akira hilft uns zwar dabei, sie zu leeren, aber Hanako hat offenbar fast genauso viel getrunken wie sie."


"Mir ist ein bisschen schwindelig, aber ich denke, ich konnte meine Grenzen ziemlich gut einschätzen."
"Träge lächelt Hanako vor sich hin, während sie mit den Haaren ihrer Puppe spielt. Ich denke, es ist ziemlich sicher, dass sie… sich nicht so gut zurückgehalten hat wie ich."


"Ich glaube nicht, dass es Hanakos Absicht war, sich so zu betrinken, aber scheinbar hat sie der Alkohol wie auf einen Schlag getroffen. Sie hat eine sehr zierliche Figur, was beim Umgang mit Alkohol auch nicht gerade hilft."


"Lilly hält ihr Glas und fährt mit einem Finger über den Rand. Ihre Wangen sind rosa, aber sie schafft es, nicht elendig betrunken auszusehen. Akira ist, wie ich irgendwie erwartet habe, größtenteils unbeeinträchtigt."


"Ihr Lächeln könnte etwas breiter sein als zuvor… Vielleicht."


show hanagown drunkgiggle onlayer master:
    ease 0.1 ypos 1.15
    ease 0.1 ypos 1.17
with None

show hanagown drunkpout onlayer master
with charachange

"Hanako hat plötzlich einen Schluckauf und wirft versehentlich die Puppe um."


show hanagown drunksad onlayer master
with charachange

ha "Ich… glaube, ich sollte vielleicht ins Bett gehen. D-Danke, Hisao, danke Lilly und Aaaakiraaaa."


"Sie lallt bei Akiras Namen ziemlich stark und schafft es gerade noch, nicht mittendrin loszukichern. Sie ist völlig besoffen, und ich weiß nicht, ob ich ein schlechtes Gewissen haben sollte oder nicht, weil ich ihren Zustand lustig finde."


"Es ist wirklich seltsam, sie so unbekümmert zu sehen. Schade, dass sie nur mit Hilfe von Alkohol so ist."


show akira basic_ending onlayer master at Position(ypos=1.0)
with dissolvecharamove

aki "Hier, lass mich dir helfen."


"Akira erhebt sich langsam, um Hanako zu helfen, aber sie hört sofort auf, als Lilly sich laut räuspert."


show lilly basic_planned_paj onlayer master
with charachange

li "Hisao, würdest du bitte?"


show akira basic_lost onlayer master
with charachange

"Akira sieht etwas überrascht aus, und ich muss zugeben, dass ich es auch bin. Mich stört die Bitte überhaupt nicht – schon gar nicht, wenn sie von so einem Lächeln begleitet wird… Es kommt nur etwas unerwartet."


hi "K-Klar. Kein Problem."


hide hanagown onlayer master
with None

show hanagown drunksad onlayer master:
    center
    ypos 1.17
with None

show hanagown drunkgiggle_close onlayer master at Position(ypos=1.0)
show akira basic_smile onlayer master
with dissolvecharamove

stop music fadeout 4.0

"Ich hebe das Schachspiel auf und helfe Hanako beim Aufstehen. Ich fühle mich etwas verantwortlich, weil ich, neben Akira, wahrscheinlich der Nüchternste im Raum bin. Sie wiegt die Puppe in einer Hand und reicht mir die andere."




show hanagown drunkgiggle_close onlayer master:
    parallel:
        ease 0.5 xpos 0.45
        ease 1.5 xpos 0.55
        ease 0.5 center
    parallel:
        1.5
        "hanagown drunkgiggle_close_ni" with Dissolve(1.0, alpha=True)
show bg school_dormlilly onlayer master:
    ease 1.0 xpos 0.45
show akira basic_smile onlayer master:
    ease 1.0 xpos 1.0 alpha 0.0
show lilly basic_planned_paj onlayer master:
    ease 1.0 xpos 0.05 alpha 0.0
with None

show bg school_girlsdormhall onlayer master:
    center
    xpos 0.6
    ease 2.5 xpos 0.4
with Dissolve(1.0)

hide akira onlayer master
hide lilly onlayer master
with Pause(0.5)

show bg school_dormhanako_ni onlayer master:
    center
    xpos 0.45
    ease 1.0 center
with Dissolve(1.0)

"Wir stolpern durch die Tür hinaus auf den Gang und in Hanakos Zimmer. Auf dem Weg dorthin stößt sie mehre Male mit mir zusammen."


play sound sfx_switch

scene bg school_dormhanako onlayer master
show hanagown drunkgiggle_close onlayer master at center
with Dissolve(0.2)

"Im Zimmer schalte ich das Licht ein, während Hanako ihre Aufmerksamkeit auf das Regal über ihrem Schränkchen richtet. Darauf sitzt eine stilvolle Puppe, die in den nackten Raum starrt."


show hanagown drunksmile_close onlayer master
with charachange

ha "Na bitte… hier drin bist du sicher…"


show ev hanako_dolls onlayer master
with locationchange

"Hanako setzt die Puppe sachte neben die andere und glättet ihr Kleid."


"Schweigend sitzen sie da, die Haare und Kleider perfekt zurechtgemacht. Genauso wie die Teekanne in Lillys Zimmer dienen sie als deutlicher Kontrast zu dem tristen Weiß und Grau, das ihr Schlafzimmer durchzieht."




show hanagown drunksmile_close onlayer master:
    ease 0.25 ypos 1.05
    ease 1.0 ypos 1.0
with None

hide ev onlayer master
show hanagown drunkdistant onlayer master:
    ease 0.25 ypos 1.05
    ease 1.0 ypos 1.0
with charadistant

"Zufrieden damit, dass ihre Puppen – ihre zwei einzigen richtigen Besitztümer – sicher sind, macht Hanako einen Schritt zurück."
"Dabei schwankt sie heftig, und ich gehe einen Schritt vor, um sie im Fall der Fälle aufzufangen, aber sie findet ohne meine Hilfe wieder ihr Gleichgewicht."


"Eine Zeit lag stehen wir beide schweigend da, während Hanako nach unten auf das Schränkchen schaut."


show hanagown drunkdistant onlayer master:
    ease 1.0 xpos 0.48
    ease 1.0 xpos 0.5
    repeat
with Pause(0.5)


"Nach ein oder zwei Minuten fängt sie an, leicht von links nach rechts zu schwanken, was sehr beunruhigend ist."


hi "Kommst du… kommst du klar?"


show hanagown drunksmile onlayer master at center
with dissolvecharamove

"Hanako hebt den Kopf und dreht sich zu mir um, als ob ihr gerade erst wieder eingefallen wäre, dass ich auch im Zimmer bin."


show hanagown drunksmile_close onlayer master:
    ease 1.0 ypos 1.05
with vpunch

stop music fadeout 0.3
play sound sfx_pillow

"Überraschenderweise geht sie zwei Schritte auf mich zu und schlingt ihre Arme um mich, während sie ihren Kopf an meine Brust legt."


play music music_heart fadein 0.5

"Ich kann spüren, wie mein Herz schlägt, als ich das Gefühl habe, dass alle meine Sinne wieder zum Leben erwachen, nachdem sie durch den Alkohol vorher abgetötet waren."


"Der Geruch von Wein in ihrem Atem, ihre Finger, die ich durch meine Kleidung spüre, der Duft ihrer Haare unter meinem Kinn…"


"Meine Hände halte ich weiter von mir gestreckt, weil ich mich nicht traue, sie zu berühren. Die Verlockung, sie zu umarmen, ist da; sie zu umschließen, ihr zu sagen, dass alles in Ordnung ist… aber es fühlt sich falsch an. Richtig, richtig falsch."


hi "Hanako…"


show hanagown drunknormal_close onlayer master at Position(ypos=1.05)
with charachange

ha "Aber ich will bei diiiir und Lilly bleibeeeen."


"Hanako erinnert mich ein wenig an Misha, wenn sie so lallt. Sie wäre wahrscheinlich nicht erfreut, das zu hören."


hi "Du weißt, ich kann nicht. Du bist immerhin ein Mädchen und ich ein Junge, und Lilly muss schlafen."


show hanagown drunkpout_close onlayer master
with charachange

"Sie stöhnt enttäuscht. Es ist so ungewohnt, dass sie so direkt ist."


hi "Keine Sorge, ich seh dich morgen, okay?"


"Ich lege eine Hand auf ihren Kopf, um sie zu beruhigen, wobei ich beschließe, dass ich – was Körperkontakt angeht – nicht weiter gehen werde, solange sie in diesem Zustand ist."


"Hanako kuschelt sich mit ihrem Kopf an meine Brust. Das macht die Situation für mich noch unbehaglicher, und als ihre Umarmung intensiver wird, beschließe ich schnell, mich zurückziehen."


"Ich lege meine Hände auf ihre Schultern und drücke sie bestimmt aber sanft von mir. Sie umarmt mich dabei noch fester, aber schließlich gibt sie auf."


show hanagown drunkworry_close onlayer master
with charachange

ha "Ich will nicht, dass du gehst…"


hi "Hanako, bitte. Akira und Lilly kommen noch auf komische Gedanken, wenn ich hier so lange brauche."


"Das ist sogar die absolute Wahrheit. Ich will wirklich nichts riskieren, und ich fühle mich im Moment ziemlich unwohl."


"Ich sollte in ihr momentanes Verhalten nichts hineininterpretieren."
"Ich habe gelesen, dass abgesehen vom Heruntersetzen der Hemmschwellen durch Alkohol, Menschen sehr unterschiedlich auf Alkohol reagieren, was dann nicht zwingend die Realität widerspiegelt."


"Und sogar ohne diese Fakten, kann man das, was sie sagt, auf viele Arten auslegen. Solange es ihr gut geht, werde ich versuchen, so schnell wie möglich aus ihrem Zimmer zu kommen."


show hanagown drunkworry_close onlayer master:
    ease 0.1 ypos 1.03
    ease 0.1 ypos 1.05
with Pause(0.2)

"Hanako hickst noch einmal. Als sie aufsteht und bedrückt in die Mitte des Raumes schaut, sieht sie richtig enttäuscht aus."


"Ihr Wesen hat sich verändert, je mehr sie getrunken hat, und jetzt – mit mir ganz allein in ihrem Zimmer – hat ihre Heiterkeit von vorhin sie offenbar verlassen. Hat sie sich extra so fröhlich gestellt, nur damit wir uns keine Sorgen machen?"


"Auch wenn das stimmt… was könnte ich denn für sie tun? Immerhin mache ich doch genau dasselbe bezüglich meiner eigenen Krankheit."


show hanagown drunkworry_close onlayer master:
    ease 1.0 ypos 1.1 alpha 0.0
with Pause(1.0)

hide hanagown onlayer master
with None

"Während ich von meinen Gedanken Abstand nehme, schaffe ich es endlich, Hanako zu ihrem Bett zu treiben, aber ihre Versuche, den wilden Bettbezug zu zähmen, bleiben weitgehend erfolglos."


hi "Tut mir leid wegen heute Abend, Hanako. Ich weiß, du wirst dich wahrscheinlich an nichts mehr erinnern, aber… Alles Gute zum Geburtstag. Es tut mir leid, dass ich nicht mehr für dich tun konnte."


"Sie sieht kurz zu mir auf. Ich habe keine Ahnung, ob das, was ich gesagt habe, tatsächlich zu ihr durchgedrungen ist, aber jegliche Gelegenheit nachzufragen verfliegt, als sie friedlich ihre Augen schließt."


play sound sfx_switch

scene bg school_dormhanako_ni onlayer master
with Dissolve(0.2)

"Erleichtert seufze ich und weiche leise von ihr zurück. Als ich das Zimmer verlasse, schalte ich noch das Licht aus."


stop music fadeout 4.0

scene bg school_girlsdormhall onlayer master
with locationchange

"Bevor ich die Tür zu Lillys Zimmer öffne, zögere ich kurz und gehe schnell durch, was ich sagen soll, falls ich nach Hanako gefragt werde. Ein paar Sekunden später fällt mir immer noch nichts ein."


scene bg school_dormlilly onlayer master
show lilly basic_smileclosed_paj onlayer master:
    twoleft
    ypos 1.2
show akira basic_smile onlayer master:
    tworight
    ypos 1.18
with locationchange

"Ich öffne die Tür und achte darauf, die Tür hinter mir zuzumachen – für den Fall, dass vorbeikommende Schüler einen Blick auf den Wein erhaschen könnten. Dann wende ich mich den zwei Mädchen an dem niedrigen Tisch zu."


"Akira lächelt unbekümmert vor sich hin, so wie Lilly. Ich begrüße den Stimmungswechsel von Hanakos Zimmer."


show lilly basic_smile_paj onlayer master
with charachange

li "Bist du das, Hisao?"


hi "Ja. Ich habe Hanako ins Bett gebracht; sie schläft jetzt."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Das ist gut. Ich muss zugeben, dass ich nicht erwartet habe, dass sie so viel trinken würde."


show akira basic_lost onlayer master
with charachange

aki "Hey, ist schon in Ordnung. Sie ist jetzt sicher und warm zugedeckt in ihrem Bett. So, wie sie ist…"


"Sie verfällt in ein betretenes Schweigen, obwohl Lilly und ich wohl kaum anderer Meinung wären. Für jemanden, der so voller Sorge und Angst ist, wäre Alkohol ein einfacher Ausweg aus diesen ständig andauernden Gefühlen."


play music music_night fadein 4.0

"Ich wünschte, ich könnte mehr für sie tun. Ich fühle mich nutzlos."


"Als ich Lilly ansehe, muss ich daran denken, was ich mich in der Stadt gefragt habe. Meine Beziehung zu ihr ist freundschaftlich, und hat sich auch immer so angefühlt, aber ich denke, ich weiß jetzt warum."


"Lilly war sowohl für Hanako als auch für mich da, seit ich sie das erste Mal getroffen habe, aber sie ist bei jedem so. Sie tut ihr Bestes, um ihnen ein gutes Gefühl zu geben."


"Wenn man es so sieht, was ist dann die Verbindung zwischen mir und Hanako?"


"Nach der Rettung unserer Beziehung, nachdem ich versehentlich während des Unterrichts eine Panikattacke ausgelöst habe, habe ich das Gefühl, als wären wir wieder Freunde, aber sie geht mir nicht mehr aus dem Kopf."


"Ich kann nicht behaupten, irgendein anderes Mädchen auf diese Weise zu sehen, aber vielleicht ist das auch nur eine normale Reaktion auf jemanden, der sich so benimmt."


hi "Sag mal, Akira…"


show akira basic_boo onlayer master
with charachange

show akira basic_smile onlayer master
with charachange

"Sie gähnt, bevor sie zu mir sieht. Es wird langsam ziemlich spät."


hi "Du weißt, was mit Hanako passiert ist, oder?"


show akira basic_resigned onlayer master
with charachange

aki "Ja. Lilly hat es mir erzählt."


show akira basic_boo onlayer master
with charachange

aki "Ich habe ziemlich hart für eine Pause gekämpft, damit ich herkommen und ihren Geburtstag ein bisschen fröhlicher machen kann. Wir verstehen uns ziemlich gut."


"Es überrascht mich, dass von einer extrovertierten Person wie ihr zu hören, aber wenn Hanako sie durch Lilly kennengelernt hat, hatte sie vielleicht Zeit, sich an Akira zu gewöhnen."


show akira basic_smile onlayer master at tworight
with dissolvecharamove

aki "Und bei dem Stichwort… Ich mache mich wohl besser auf den Weg. Ich komme sowieso schon ein bisschen zu spät."


show lilly basic_oops_paj onlayer master
with charachange

li "Aber es ist schon so spät…"


show akira basic_boo onlayer master
with charachange

aki "Tut mir leid. Uns ist einiges an Arbeit aufgehalst worden, also heißt es Überstunden."


show akira invis onlayer master:
    xpos 0.8
with dissolvecharamove

"Sie hievt sich ächzend hoch und geht an mir vorbei zur Tür. Kurz bevor sie geht, dreht sie sich wieder zu uns."


show akira basic_lost onlayer master:
    tworight
with dissolvecharamove

aki "Die Abflugzeit und die anderen Sachen hast du nicht vergessen?"


show lilly basic_smileclosed_paj onlayer master
with charachange

li "Keine Sorge, es ist alles bereit. Ich muss nur packen, wenn die Zeit zum Abflug kommt."


show akira basic_ending onlayer master
with charachange

aki "Braves Mädchen. Ich seh euch dann später."


show akira invis onlayer master:
    xpos 0.8
with dissolvecharamove

hide akira onlayer master
with None

"Und damit verschwindet sie durch die Tür, während sie ihre Hand zum Abschied hebt."


show lilly basic_smileclosed_paj onlayer master at Position(xpos=0.5)
show bg school_dormlilly onlayer master at bgright
with charamove

hi "Deine Schwester ist wirklich… besonders."


show lilly basic_giggle_paj onlayer master
with charachange

"Über diese Bemerkung hätte ich wohl vorher gründlich nachdenken sollen. Wie auch immer, Lilly scheint meine Beurteilung ziemlich lustig zu finden."


hi "Geht's dir gut, nachdem du so viel getrunken hast? Bist du nicht betrunken und versteckst es einfach nur gut?"


show lilly basic_smileclosed_paj onlayer master
with charachange

li "Ich versichere dir, mir geht es ganz gut. Ich habe mich unter Kontrolle. Du scheinst dich auch recht gut im Griff zu haben, wenn ich das so sagen darf."


hi "Ja, na ja. Ich schätze, deine Zurückhaltung trifft auch auf mich zu."


"Ein klein wenig zögernd setze ich mich Lilly gegenüber an den Tisch. Ich will das direkt ansprechen, wenn es auch nur ist, um meine eigenen Gedanken zu ordnen."


hi "Ich wollte das schon lange fragen, aber es hat eine Weile gedauert, bis ich mich dazu entschließen konnte…"


hi "Hast du irgendeine Idee, was diese Panikattacke ausgelöst haben könnte? So wie ich das verstehe, hat es etwas mit ihrem Geburtstag zu tun, aber mehr weiß ich nicht."


hi "Sogar Akira war in ihrer Nähe sehr vorsichtig, also muss sie es auch wissen."


show lilly basic_reminisce_paj onlayer master
with charachange

"Lillys Lächeln verschwindet. Mit der Heiterkeit der Geburtstagsparty ist es jetzt endgültig vorbei."


li "Um ehrlich zu sein, bin ich mir auch nicht über alle Details im Klaren."


li "Hanako hat dir von dem Feuer erzählt. So viel habe ich auch von ihr erfahren, nachdem wir uns kennengelernt hatten und viel zusammen waren."


show lilly basic_concerned_paj onlayer master
with charachange

li "Mehr als das… hat sie mir ganz einfach nie erzählt."


hi "Sie hat es dir nie erzählt…"


show lilly basic_sad_paj onlayer master
with charachange

li "Wenn man vom Schlimmsten ausgeht, worauf kann sie zurückblicken? Ein einsames Leben und vermutlich den Tod ihrer Familie? Vielleicht geht sie sogar so weit und gibt sich selbst die Schuld am Tod ihrer Eltern?"


"Schon der Gedanke daran, wie wenig ich über Hanakos Vergangenheit weiß, ist traurig. All das durchlebt zu haben und mit den Erinnerungen daran leben zu müssen, muss noch unendlich viel schlimmer sein."


"Lilly wirkt ähnlich niedergeschlagen, aber ich kann sehen, wie sie ihre Fassung langsam zurückgewinnt."


"Ich denke, wir beide sprechen wegen des Weines offener als sonst, aber ich habe das Gefühl, dass es sowieso richtig ist, darüber zu reden."


hi "Ich fühle mich dabei irgendwie hilflos. Wenn man es so sieht, was könnte ich denn für sie tun?"


show lilly basic_sleepy_paj onlayer master
with charachange

li "Ich bin mir nicht ganz sicher, ob ich dir das sagen sollte, aber Hanako hat mir erzählt, dass du sie an dem Tag, nachdem wir nach ihr gesehen haben, besucht hast."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Ich muss zugeben, dass ich nicht gedacht hätte, dass sie – so kurz nach dem, was passiert ist – einen solchen Schritt machen würde. Von dir hätte ich es auch nicht erwartet. Ich finde, es war eine schöne Geste von dir."


hi "Das war doch nichts, ehrlich."


hi "Es ist nur so… In solchen Momenten denke ich manchmal, es wäre besser, wenn wir die Yamaku nie verlassen müssten, oder zumindest diese Stadt. Es ist so viel einfacher ohne Außenstehende."


"Ich hatte nicht erwartet, dass Lilly auf meine Aussage so besorgt reagiert, und eine Zeit lang wirkt sie in Gedanken versunken."


show lilly basic_oops_paj onlayer master
with charachange

"Sie setzt an, etwas zu sagen, bricht aber sofort ab und denkt noch einmal nach. Es ist ein bisschen beunruhigend."


show lilly basic_reminisce_paj onlayer master
with charachange

li "Ich glaube…"


show lilly basic_smile_paj onlayer master
with charachange

li "Sag mal, hast du am Freitag Abend schon etwas vor?"


hi "Freitag Abend? Nein…"


hi "Ist am Tag darauf nicht dein Flug nach Schottland? Ich glaube nicht, dass es eine gute Idee ist, dich schon so zu verausgaben, bevor du überhaupt da bist."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Das ist schon okay, um mich brauchst du dir keine Sorgen zu machen. Ich würde es ja morgen Abend machen, aber ich kann mir vorstellen, dass es Hanako da nicht so gut gehen wird."


"Bei dem Gedanken daran, wie es ihr morgen gehen wird, verziehe ich das Gesicht. Vielleicht sollten wir dankbar sein, dass sie sich bei ihrer geringen Alkoholtoleranz nicht einfach übergeben hat."


hi "Also, ich werde zu was auch immer du vorhast kommen können. Was ist es denn?"


show lilly basic_smileclosed_paj onlayer master
with charachange

li "Nichts Besonderes, das versichere ich dir. Nur ein kleiner Ausflug."


show lilly basic_cheerful_paj onlayer master
with charachange

li "Und du solltest besser los, Hisao. Bis zur Ausgangssperre kann es nicht mehr lange hin sein."


"Oh Mist, die Ausgangssperre. Die hatte ich völlig vergessen."


"Ich schaue auf die Uhr bei Lillys Bett, aber das ist anscheinend eine besondere ohne Ziffern. Angesichts Lillys Leiden ist das nur logisch."


"Da ich nicht riskieren will, von einem hochnäsigen Nachtwächter belehrt zu werden, folge ich ihrem Rat und mache mich auf den Weg in mein Zimmer."


hi "Na gut. Dann sehe ich dich und Hanako wohl morgen, angenommen ihr beide schafft es, morgens aufzustehen."


show lilly basic_smileclosed_paj onlayer master
with charachange

li "Danke, dass du an uns denkst, Hisao. Bis dann."


scene bg school_girlsdormhall onlayer master
with locationchange

"Mit diesen Worten verlasse ich ihr Zimmer und gehe auf den Korridor hinaus."


"Ich hoffe, ihre Idee ist gut."


stop music fadeout 2.0

scene black onlayer master
with dissolve



label de_H18:

scene black onlayer master
with dissolve

play sound sfx_doorknock

"Jemand hämmert mit seiner Faust an die Tür. Es fühlt sich an, als würde er einen Nagel in meinen Kopf geschlagen."


"Ein-, zwei-, dreimal. Ich seufze genervt und ertrage es, während ich meine Augen fest schließe, innig hoffend, dass er wieder geht – wer auch immer es ist."


"Ich fühle mich furchtbar. Mein Gesicht fühlt sich an, als wäre es aus Blei, meine Arme sind schwer, und mir ist ziemlich übel."
"Seit ich vor einer halben Stunde aufgewacht bin, fühle ich mich so, und ich kann nicht die Energie aufbringen, mich aus dem Bett aufzuraffen."


"Das… nennt man also einen Kater."


"Ich frage mich, ob das nicht vielleicht sogar die beste Therapie für Teenager ist, die verzweifelt versuchen, sich erwachsen zu fühlen, indem sie trinken. Angesichts der Tatsache, wie unangenehm es sich anfühlt, will ich es nicht wiederholen."


play sound sfx_doorknock

"Wieder klopft es ein paar Mal, und das Geräusch hallt in dem kleinen Zimmer wider. Ich wünschte, der Jemand würde endlich aufgeben; ich habe nicht die Absicht, seinetwegen aufzustehen."


"Sekunden vergehen und werden zu Minuten. Da nicht mehr an die Tür geklopft wird, ist der Jemand wohl gegangen. Gott sei Dank."


play music music_dreamy fadein 2.0

scene bg school_dormhisao onlayer master
with openeye

"Als ich auf die Uhr schaue, sehe ich, dass die Zeit langsam gekommen ist, wo ich ernsthaft daran denken sollte, mich anzuziehen und für den Unterricht fertig zu machen. Ich glaube aber nicht, dass ich das schaffe."


"Ich hasse es, den Unterricht zu schwänzen, aber ich glaube nicht, dass ich unter diesen Umständen viel zustandebringen würde. Außerdem weiß ich schon ohne im Spiegel nachzusehen, dass ich schlimm aussehe."


scene bg school_hallway3 onlayer master
with shorttimeskip

"Durch das morgendliche Treiben kann ich eine Weile vor dem Klassenzimmer stehen bleiben ohne sofort aufzufallen. Hoffentlich stellt Mutou mir keine unangenehmen Fragen, weil ich gestern nicht da war."


"Ich war krank, das ist die Wahrheit. Ich muss nur den Grund dafür verbergen."


"Zuversichtlich, dass ich durch taktisches Weglassen von bestimmten Details davonkomme, schreite ich ins Klassenzimmer und versuche dabei, so normal wie möglich auszusehen."


scene bg school_scienceroom onlayer master
with locationchange

"Sofort als ich die Tür aufmache und einen Schritt vorwärts mache, spüre ich ein Dutzend Blicke auf mir. Das bilde ich mir unmöglich ein; sie versuchen nicht einmal, es zu verbergen."


show hanako emb_emb onlayer master:
    tworight
    ypos 1.15
with charaenter

show hanako emb_downtimid onlayer master
with charachange

"Meine Augen schweifen kurz durch das Klassenzimmer, und ich entdecke Hanako. Unsere Blicke treffen sich für einen Moment, woraufhin sie ihren Kopf senkt und konzentriert auf ihren Schreibtisch starrt."


"Hat sie alles ausgeplaudert? Mutou ist zwar ganz in Ordnung für einen Lehrer, aber Alkoholkonsum von Minderjährigen nimmt man nicht gerade auf die leichte Schulter."


"Nervös schaue ich zu ihm."


show muto normal onlayer master at twoleft
with charaenter

mu "Geht es dir heute besser?"


hi "Ja. Danke."


"Er weist mich an, mich an meinem Platz zu setzen. Auf dem Weg dorthin fühlen sich meine Beine an wie Besenstiele. Das wird ein langer Tag."


scene bg school_scienceroom onlayer master at bgleft
with shorttimeskip

stop music fadeout 2.0
play sound sfx_normalbell

"Sobald die Mittagsglocke läutet, gehe ich zu Hanakos Tisch, um nachzufragen, was los ist."


hi "Hanako… hast du Mutou etwas…?"


show hanako emb_emb onlayer master:
    center
    ypos 1.15
with charaenter

"Sie sieht zu mir auf und schüttelt den Kopf. Was für eine Erleichterung."


show hanako emb_downtimid onlayer master
with charachange

ha "Es ist nur…"


hi "Nur…"


mi "Hallöchen, Hicchan. Schön, dich heute wiederzusehen~!"


show bg school_scienceroom onlayer master at bgright
show hanako emb_downtimid onlayer master:
    right
    ypos 1.15
with dissolvecharamove

show shizu basic_sparkle onlayer master at center
show misha perky_smile onlayer master at twoleft
with charaenter

play music music_happiness fadein 2.0

"Ich verziehe das Gesicht und drehe mich zu der unverwechselbaren Stimme hinter mir um. Diese Stimme klang viel zu fröhlich, als dass sie noch angenehm wäre, sogar wenn sie von Misha kommt."


"Mishas fröhliches Lächeln ist nichts Ungewöhnliches. Das von Shizune ist allerdings ein schlechtes Zeichen. Das Lächeln, das sie gerade aufhat, hat sich in mein Gehirn als ihr „Du gehörst mir”-Lächeln eingebrannt."


hi "Hi Shizune, Misha. Ihr ähm… scheint froh zu sein, mich zu sehen."


show shizu adjust_smug onlayer master
with charachange

shi "…?"


show misha hips_grin onlayer master
with charachange

mi "Ging's dir gestern nicht gut, Hicchan~?"


hi "Nein, mir ging's nicht gut. Aber jetzt geht es mir besser."


show shizu behind_smile onlayer master
with charachange

shi "…"


show misha cross_smile onlayer master
with charachange

mi "Schön zu hören, Hicchan."


"Warum habe ich das Gefühl, dass mich Shizune in eine Falle lockt?"


hi "Das hört sich nicht wirklich an, als wäre es dir ernst damit."


show shizu adjust_happy onlayer master
with charachange

shi "…"


show misha hips_smile onlayer master
with charachange

mi "Oh nein, Hicchan. Wir sind wirklich froh, dass es dir jetzt besser geht~."


show shizu basic_happy onlayer master
with charachange

shi "…"


"Shizune sprüht nur so vor Glück. Es gibt nur einen Grund, warum sie so sein könnte… Oh nein."


show misha perky_smile onlayer master
with charachange

mi "Wir haben uns sogar ziemliche Sorgen um dich gemacht. Immerhin…"


show misha sign_smile onlayer master
with charachange

mi "… waren du, Hanako und Lilly alle am selben Tag nicht im Unterricht."


"Ja, sie hat uns erwischt. Und zwar voll und ganz, sodass ich nur geschlagen seufzen kann."


hi "Ich schätze, ihr habt eure eigene Theorie darüber. Könntet ihr es einfach nur… niemandem sagen?"


show misha cross_smile onlayer master
with charachange

mi "Dafür ist es ein bisschen spät, Hicchan~."


"Sie hat wohl Recht, angesichts der Blicke, die beim Betreten des Klassenzimmers auf mich gerichtet waren. Noch scheint es aber ein vager Verdacht zu sein und noch keine echte Anschuldigung, also haben wir vermutlich kein Problem."


show hanako emb_downsad onlayer master
with charachange

"Hanako senkt ihren Kopf noch weiter. Solch eine Aufmerksamkeit ist für mich schon lästig, geschweige denn für sie. Shizunes und Mishas Reaktion nach haben sie das auch bemerkt."


show shizu basic_angry onlayer master
with charachange

shi "…"


show misha hips_frown onlayer master
with charachange

mi "Der einzige Grund, warum wir es dir so schwer machen, ist, weil du uns gestern Vormittag ignoriert hast~!"


"Gestern Vormittag? Es dauert eine Weile, bis ich mich daran erinnere, was passiert ist, weil ich wegen meines Katers kaum klar denken konnte."


hi "Oh, ja, da hat wer geklopft. Das wart ihr Zwei?"


show shizu behind_frown onlayer master
with charachange

shi "…"


show misha cross_frown onlayer master
with charachange

mi "Das waren wir, und du hast uns da eine Ewigkeit stehen lassen, nachdem wir so viel auf uns genommen haben, um früh am Morgen zu deinem Zimmer zu kommen."


hi "Tut mir leid, ich hatte ein… Problem mit meinem Magen? Ein Problem mit meinem Magen."


"Sie kaufen es mir nicht ab. Das kann ich ihnen nicht verübeln."


show shizu behind_frustrated onlayer master
with charachange

"Resigniert lässt Shizune ihren Kopf fallen und greift in ihre Tasche."


"Etwas weiß-gelbes steht ein bisschen heraus, und als sie es herauszieht, erweist es sich als ein ziemlich fröhlich verziertes Kuvert."


show letter_insert onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Da sie es in meine Richtung hält, nehme ich es automatisch an."


mi "Das versuchen wir dir schon so lange zu geben, Hicchan! Du schaust nicht in deinen…"


stop music fadeout 5.0

"Mishas Stimme rückt in den Hintergrund, als ich erkenne, was auf dem Kuvert steht."


stop music fadeout 0.3

hi "Iwanako…"


"Einen Moment lang starre ich auf das Kuvert, bis mir plötzlich wieder einfällt, dass ich nicht allein bin."


show misha cross_smile onlayer master
show shizu behind_blank onlayer master
show hanako emb_timid onlayer master
with None

show letter_insert onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert onlayer master
with None

"Die Blicke der Leute um mich herum fühlen sich sehr seltsam an, etwas aufdringlich. Ich will jetzt irgendwie allein sein."


show hanako emb_sad onlayer master
with charachange

ha "Iwanako…?"


hi "Ach nichts. Ich danke euch beiden, dass ihr mir das gebracht habt."


show misha hips_grin onlayer master
with charachange

mi "Das würde ich aber auch meinen, nach allem, was wir durchgemacht haben~."


show misha hips_frown onlayer master
with charachange

"Ich mache einen Schritt zurück und verabschiede mich."
"Misha schmollt sogar theatralisch, als ich zur Tür herausgehe, aber Shizune und Hanako sind wegen meiner Reaktion nach wie vor ganz offensichtlich neugierig. Ich hoffe, sie fragen mich später nicht darüber aus. "


$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg school_gardens2 onlayer master
with locationskip

play music music_serene fadein 2.0

"Wie immer ist der Duft der Gärten sehr angenehm. Abgesehen von ihrer schieren Größe ist eines der offensichtlichsten Anzeichen dafür, wie vermögend diese Schule ist, die Fläche und der Zustand der Außenanlagen."


"Man kann etliche Schüler beim Mittagessen, Plaudern und Spielen auf den hellgrünen Rasenflächen beobachten."
"Sogar einige der Lehrer genießen hier den Sommer, während sie die Schüler beaufsichtigen und die langen zementierten Wege entlang spazieren."


"In meiner Heimatstadt gab es nie einen solchen Anblick. Auf Ausflügen vielleicht, aber sicher nie in der Schule oder irgendwo in meiner Wohngegend."


"Sogar die Bank, auf die ich mich zum Lesen gesetzt habe, ist dank der Sommersonne wärmer und erinnert mich daran, warum ich den Schulblazer noch kein einziges Mal getragen habe."


show letter_open_insert onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Wenn man es so betrachtet, passen die Sonnenblumen und die strahlenden gelben Farbtupfer, die das Papier verzieren, wirklich gut zu dieser Jahreszeit. Wenn doch nur die Worte darauf auch so passend wären."


"Da war ich, so sicher, dass ich über sie hinweg bin, und dann taucht dieses lästige Ding auf."


"Ihre Handschrift wirkt bestenfalls vage vertraut, und erst jetzt, als ich es sehe, erinnere ich mich daran, dass sie oft mit einem rosa Stift geschrieben hat. Sie war immer ziemlich mädchenhaft. Eine bessere Beschreibung fällt mir nicht ein."


"Sie war auch recht zierlich. Mir war nie klar, ob ich das an ihr mochte oder nicht, jedoch ist mit der Ankunft dieses Briefes diese Frage wohl größtenteils irrelevant geworden."


"Am Anfang des Briefes geht es hauptsächlich darum, was in ihrem Leben so abläuft. Meine alte Klasse hatte einen guten Start ins neue Schuljahr, viele haben Angst vor den künftigen Prüfungen und so weiter."


"Aber er endet mit einer sehr persönlichen, wenn auch kurzen Botschaft. Ein bisschen fühlt es sich so an, als hätte sie den Großteil des Briefes nur geschrieben, um den Schluss abzumildern."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

$ written_note("Ich wollte irgendwie meine Gefühle zum Ausdruck bringen, aber ich habe einfach nicht die richtigen Worte gefunden. Ich konnte nichts sagen, um dich zu trösten. Es tut mir wirklich leid, dass ich dich nicht unterstützen konnte, als du mich am nötigsten gebraucht hast. Zumindest kann ich jetzt, nach so langer Zeit, ehrlicher sein.\n\n\n\n")


$ written_note("Wenn ich zu diesen stillen Tagen im Februar und März zurückkehren könnte, würde ich dir sagen, dass du dich nicht aufgeben sollst. Vielleicht hättest du dich nicht so weit von mir entfernt, wenn ich einfach nur etwas gesagt hätte. Ich hoffe, du hast es auch ohne mich geschafft, wieder auf die Beine zu kommen.\n\n\n\n")


$ written_note("Jetzt, wo die Entfernung zwischen uns auch physisch ist, fühlt sich alles irgendwie endgültiger an. Ich frage mich, ob wir uns irgendwann einmal wiedersehen. Vielleicht wäre es besser, wenn nicht? Trotzdem, wenn du mir antworten willst, schreib mir bitte zurück. Ich würde wirklich gerne erfahren, wie es dir an deiner neuen Schule geht. Ich wünsche dir alles Gute.\n\nDeine Iwanako")


window show

$ renpy.music.set_volume(1.0, 1.0, channel="music")

"Und damit war's das. Unsere Beziehung ist vorbei. Schön, sauber und ordentlich, ohne Unklarheiten."


"Ich habe mich nie an irgendwelche Hoffnungen geklammert, dass sie je neu beginnen könnte. Als sie mich das letzte Mal besuchte, sagten wir beide nichts außer einem Wort, als sie sich zum letzten Mal verabschiedete. „Lebwohl.”"


"Wie dem auch sei… das hier fühlt sich endgültiger an. Der Schlussstrich unter einem Experiment, an dem wir uns beide versucht haben und das uns nicht gelungen ist."


show letter_open_insert onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_open_insert onlayer master
with None

"Ein lauter Schrei lässt mich vom Brief aufblicken. Es sind nur ein paar herumlaufende Schüler, zu denen ein in der Nähe stehender Lehrer hinübergeht, um mit ihnen zu reden."


mystery "Alles in Ordnung?"


show yuuko neutral_down onlayer master at center
with charaenter

"Neben mir höre ich eine zaghafte Stimme. Einen Moment lang glaube ich, es sei Hanako, aber in Wirklichkeit ist es Yuuko."


hi "Oh, hallo Yuuko. Ich dachte, du wärst in der Bibliothek."


show yuuko closedhappy_up onlayer master
with charachange

"Passend zur Atmosphäre lächelt sie gut gelaunt und entfaltet die Verpackung eines Brötchens in ihrer Hand. Es springt wohl jemand für sie ein, während sie sich etwas zu Essen geholt hat."


"Das erinnert mich daran, dass ich noch nichts gegessen habe. Aber ich bin nicht hungrig, und einmal das Mittagessen auszulassen, schadet nicht."


show yuuko smile_up onlayer master
with charachange

yu "Was dagegen, wenn ich mich zu dir setze?"


hi "Nein, nur zu."


show yuuko neutral_down onlayer master at Position(ypos=1.15)
with dissolvecharamove

"Während Yuuko sich setzt, lasse ich schnell den Brief wieder in seinen Umschlag gleiten und in meiner Tasche verschwinden, die gegen die Bank gelehnt ist. Sie wirft die Verpackung in einen Mülleimer neben uns."


"Da ich nichts anderes zu tun habe, lehne ich mich zurück und genieße die Sonne so gut ich kann, während ich schweigend über den Brief nachdenke."


"Das saftige Gras, der klare, blaue Himmel… Alles sieht so anders aus als damals. Sogar die Umgebung der Schule – vom Hügel bis zu den Wäldern drum herum – ist das komplette Gegenteil von der städtischen Kulisse, an die ich mich erinnere."


"Vielleicht fühlt sich so Heimweh an. Andererseits ist es kein völlig negatives Gefühl; die Atmosphäre in der Gegend um Yamaku ist – obwohl sie völlig anders ist – auch angenehm. Ich glaube, ich könnte mich daran gewöhnen."


show yuuko smile_down onlayer master
with charachange

yu "Hey, Hisao?"


hi "Ja?"


show yuuko worried_down onlayer master
with charachange

yu "Du hast meine Frage vorher nicht beantwortet. Ich wollte nichts sagen, aber du siehst besorgt aus."


show yuuko panic_up onlayer master
with charachange

yu "Wenn du aber nichts sagen willst, dann ist das okay, das macht gar nichts. Ähm, t-tut mir leid, dass ich so etwas Komisches frage…"


hi "Schon okay."


hi "Es ist nur… Ich habe einen Brief von jemandem bekommen, den ich kannte, bevor ich hierher kam. Er hat mich zum Nachdenken gebracht."


hi "Ich dachte, ich hätte es geschafft, die meisten Probleme zu bewältigen, die mein Unfall mit sich brachte, aber jetzt bin ich mir nicht so sicher. Irgendwie wünschte ich, ich hätte ihn nie gelesen."


show yuuko worried_up onlayer master
with charachange

yu "Ich glaube nicht, dass das gut ist, Hisao."


show yuuko neutral_down onlayer master
with charachange

yu "Als mein Freund mich verließ, tat er das aus heiteren Himmel, und er sagte mir nie warum. Zuerst war ich deswegen ziemlich niedergeschlagen, aber ich entschied mich, ihm zu vergeben."


hi "Du hast ihm vergeben? Hätte er nicht wenigstens richtig mit dir darüber reden können?"


yu "Er war schon immer einer von denen, die es schwer finden, anderen näherzukommen."


yu "Letztendlich kam ich zu dem Schluss, dass ich mich nicht ohne Grund in ihn verliebt hatte. Er war ein guter Mensch, und ich glaube, wenn ich in seiner Position gewesen wäre, hätte ich es vermutlich genauso schwer gefunden, mit ihm zu reden."


hi "Ich… verstehe nicht wirklich, wie das mit meinem Brief zusammenhängt."


show yuuko worried_up onlayer master
with charachange

yu "Ich meine, dass… Ähm, wie soll ich das sagen…"


yu "Es muss sehr schwer für denjenigen gewesen sein, diesen Brief zu schicken. Wenn er ihn geschickt hat, dann hat er wohl sehr genau darüber nachgedacht, was er schreibt."


"Iwanako hat es fertiggebracht, diesen Brief zu schreiben, und unsere Beziehung endgültig zu beenden – etwas, was ich nie geschafft habe."


"Und ich sitze hier und versuche, Hanako so gut ich kann zu beschützen und ihr zu helfen – besonders jetzt, wo Lilly für eine Weile weg ist. Dabei komme ich nicht einmal mit meinen eigenen Problemen klar."


show yuuko neutral_down onlayer master
with charachange

yu "Ergibt das Sinn?"


"Sie hat meine ausbleibende Antwort und meine gerunzelte Stirn als Zweifel aufgefasst. Sie liest wirklich zu viel in Gesichtern, genauso wie eine gewisse andere Person."


hi "Ja, das ergibt Sinn."


hi "Der Brief war nur irgendwie ein Schock. Ich glaube, ich habe versucht, mir vorzumachen, dass mein Leben neu begonnen hat, als ich auf die Yamaku kam, aber jetzt ist mir plötzlich klar, dass das nicht stimmt."
hi "Ich bin ein bisschen ratlos, wie ich mit diesen Gefühlen fertig werden soll."


show yuuko worried_down onlayer master
with charachange

yu "Ich glaube, damit kann ich dir nicht wirklich helfen. Tut mir leid."


hi "Schon gut. Mit dir zu reden, hat mir geholfen, meine Gedanken ein wenig in Ordnung zu bringen. Also trotzdem Danke."


show yuuko closedhappy_down onlayer master
with charachange

"Sie nickt und lächelt süß. Yuuko ist ein nettes Mädchen, da ist es schade, dass sie so oft so nervös ist."


play sound sfx_warningbell

show yuuko panic_up onlayer master
with vpunch

"Wir schrecken beide auf, als die Schulglocke läutet."


yu "Ah, ich hätte vor dem Läuten zurück sein sollen!"


hi "Ups…"


show yuuko worried_up onlayer master at center
with Dissolvemove(0.3)

"Sie springt von der Bank auf und rennt fast los, ohne ein weiteres Wort zu verlieren, aber sie dreht sich noch einmal um, als ihr einfällt, dass wir eben noch geredet haben."


show yuuko neutral_up onlayer master
with charachange

yu "Bis später, Hisao. Kopf hoch, okay?"


hi "Ich versuch's. Danke, Yuuko."


stop music fadeout 9.0

hide yuuko onlayer master
with charaexit

"Mit einer kurzen Verbeugung verlässt mich Yuuko und eilt zur Bibliothek. Ihr Abflug erregt die Aufmerksamkeit einiger vorbeigehender Schüler, die lustlos zu ihren Klassenzimmern zurücktrotten, nachdem sie ihren Spaß hatten."


"Widerwillig stehe ich von der Bank auf und schließe mich ihnen an."


"Sogar als ich durch die Gärten zurück zum Hauptgebäude gehe, geht mir der Brief in meiner Tasche nicht richtig aus dem Kopf."


stop ambient fadeout 2.0
stop music fadeout 2.0

scene black onlayer master
with dissolve



label de_H19:

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

scene bg city_street2_ni onlayer master
with locationchange

"Durch die Stadt zu wandern, ruft ein starkes nostalgisches Gefühl hervor. Während Yamaku das Gegenteil meines vorigen Wohnorts ist, fühlt sich die Stadt nachts erstaunlich vertraut an."


"Meine Augen wandern von den grellen elektronischen Tafeln am nächtlichen Himmel über die Straßenlampen, die die Dunkelheit erhellen, zu den Geschäftsmännern, die es sich nach der Arbeit gut gehen lassen, und den Pärchen auf ihren Dates."


"Auch wenn ich nicht wollte, könnte ich nicht anders, als jeden Aspekt der Stadt aufzusaugen. Dieses vertraute Gefühl genieße ich wie ein süßes Bonbon auf meiner Zunge."


show akira basic_boo_ni onlayer master:
    center
    xpos 0.59
show lilly cane_smileclosed_cas_ni onlayer master:
    center
    xpos 0.41
with charaenter

"Lilly geht zu meiner Linken und lässt ihren Gehstock hin und her schaukeln. Als Führung klammert sie sich an den Arm ihrer Schwester, während sie sich mit ihr unterhält."


"Verglichen mit einer Taxi- oder Busfahrt ist es viel angenehmer, bei Akira in ihrem recht schönen Auto mitzufahren."


show hanako invis_close onlayer master:
    center
    xpos 1.0
with None

scene bg city_street2_ni onlayer master at bgleft
show akira basic_boo_ni onlayer master:
    center
    xpos 0.39
show lilly cane_smileclosed_cas_ni onlayer master:
    center
    xpos 0.21
show hanako basic_distant_cas_close_ni onlayer master at tworight
with dissolvecharamove

"Jedoch vielleicht nicht für die Person rechts von mir. Während Lilly an den Fahrstil ihrer Schwester gewohnt ist und ich ein wenig Aufregung ganz gut fand, hat sich Hanako die meiste Zeit fest an die Tür geklammert."


show hanako basic_smile_cas_close_ni onlayer master
with charachange

ha "N-Nachts sieht alles so s-schön aus…"


show hanako emb_downtimid_cas_close_ni onlayer master
with charachange

"Rasch sieht sie wieder zu Boden, als sich versehentlich ihre Blicke mit jemandem kreuzen."


hi "Ja, stimmt."


"Meine Antwort ist nicht sonderlich wohl überlegt, weil ich so abgelenkt bin, dass es mir schwer fällt, ein einfaches Gespräch zu führen."


"Abgesehen vom Anblick der Stadt ist einer der Gründe dafür Hanakos Anblick."


"Das ist das erste Mal, dass ich sie etwas anderes tragen sehe als ihre Schuluniform oder ihren Pyjama. Es hat mich überrascht, als wir uns am Schultor trafen und ich ihr Outfit zum ersten Mal sah."


"So tief wie sie ihren Kopf senkt, wenn jemand an uns vorbeigeht, vermute ich, dass ihre Mütze nicht nur ein Fashion-Statement ist."


"Während ich anfangs skeptisch gegenüber Lillys Plan war, mit uns in die Stadt zu gehen, wurde es mit Einbruch der Nacht offensichtlich, dass sie sich Gedanken darüber gemacht hatte."
"Nur wenige Menschen haben Hanako wirklich Beachtung geschenkt, da ihre Narben durch die Dunkelheit gut versteckt sind."


hi "Also… Wir sind in der Stadt. Irgendwelche Ideen, was wir machen könnten?"


show akira basic_smile_ni onlayer master
with charachange

"Von Akira kommt ein strahlendes Lächeln. Irgendetwas sagt mir, dass sie diejenige ist, die diese Entscheidung trifft, auch wenn ihre Schwester vielleicht den Ausflug ursprünglich vorgeschlagen hat."


show akira basic_ending_ni onlayer master
with charachange

aki "Wirst du schon sehen. Komm einfach mit."


"Ich nicke und tue mein Bestes, das Gesicht nicht zu verziehen. Nach dem, was auf Hanakos Geburtstagsparty passiert ist, vertraue ich Akiras Urteilsvermögen nicht so ganz."


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.1, 0.0, channel="music")
play music music_jazz fadein 14.0

scene bg city_street3_ni onlayer master
with locationchange

"Wir gehen weiter, und mir fällt auf, dass wir an immer mehr Cafés, Restaurants und anderen Lokalen vorbeigehen."


"Von Zeit zu Zeit kommt ein Mann im Anzug aus einer Bar, meistens wird er von einem anderen Mann gestützt, aber größtenteils kommen die Kunden in diesem Teil der Stadt jung und modisch daher."


"Aus den Lokalen, an denen wir vorbeigehen, kommt Musik der unterschiedlichsten Richtungen."
"Die Dissonanzen der sich überlagernden Musik sollten unangenehm klingen, aber sie erinnern mich so sehr an die Zeit, die ich mit meinen alten Freunden in der Stadt verbracht habe, dass sie mir egal sind."


"Hanako und ich sind ein bisschen hinter Lilly und Akira zurückgeblieben. Damit ist es vorbei, als ich ein dumpfes Geräusch neben mir höre."


show hanako defarms_shock_cas_ni onlayer master
with vpunch

ha "E-E-Entschuldigung…!"


"Bis sie sich von ihrer entschuldigenden Verbeugung wieder erhoben hat, geht der Geschäftsmann mittleren Alters, mit dem sie zusammengestoßen ist, schon wieder weiter, nachdem er eine halbherzige Entschuldigung gemurmelt hat."


show hanako emb_downtimid_cas_ni onlayer master
with charachange

"Hanako scheint von dem Vorfall ein wenig mitgenommen zu sein, und als sie schnell ein paar Schritte nach vorne macht, um zu mir aufzuschließen, sehe ich, dass sie abermals ihren Kopf hängen lässt."
"Wahrscheinlich ist sie mit ihm zusammengestoßen, weil sie auf den Boden geschaut hat und nicht wohin sie geht."


show hanako emb_timid_cas_close_ni onlayer master
with charachange

"Ich gehe ein wenig zur Seite, lege eine Hand auf ihre mir abgewandte Schulter und ziehe sie zu mir."


ha "Hisao?"


hi "Schon in Ordnung. Du kannst näher bei mir laufen, wenn du willst."


show hanako emb_smile_cas_close_ni onlayer master
with charachange

"Hanako zögert, aber schließlich ist sie einverstanden und nickt."


stop ambient fadeout 1.0
$ renpy.music.set_volume(0.5, 10.0, channel="music")

scene bg city_karaokeext_ni onlayer master
show crowd_ni onlayer master
show akira basic_smile_ni onlayer master:
    center
    xpos 0.39
show lilly cane_listen_cas_ni onlayer master:
    center
    xpos 0.21
show hanako basic_smile_cas_close_ni onlayer master at tworight
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0

"Nachdem ich schon ein paar Mal dachte, wir wären an Akiras Ziel angekommen, sind wir schließlich da. Mittlerweile sind wir unter den Hochwegen und an den am aufdringlichsten und grellsten beleuchteten Orten vorbei."


"Ein wenig bin ich überrascht. Das durchschnittliche Alter der Passanten hier ist unverkennbar höher, und es riecht ziemlich stark nach Zigarettenrauch."
"Die Gegend ist aber keineswegs heruntergekommen, und es ist ganz amüsant Lillys Reaktion auf den Rauchgeruch zu beobachten."


"Obwohl sie von den leisen Gesprächen um uns herum verdeckt wird, kann man Jazzmusik von drinnen hören. Wenn man nach oben auf das nur schwach beleuchtete Schild blickt, wird klar warum."


hi "Ein Jazzclub. Ich muss zugeben, das hatte ich nicht erwartet."


show lilly cane_giggle_cas_ni onlayer master
with charachange

"Lilly schnaubt vergnügt und lächelt."


show lilly cane_smileclosed_cas_ni onlayer master
with charachange

li "Irgendwie habe ich das Gefühl, ich hätte es wissen sollen, Akira."


"Während wir draußen reden, fällt mir auf, dass wir mehr und mehr merkwürdige Blicke ernten. Auf peinliche Weise fällt den Leuten selbst auf, dass sie starren und schauen weg, was es nur noch offensichtlicher macht."


"Das habe ich gelegentlich bemerkt, als wir unterwegs waren, aber jetzt ist es deutlich auffälliger."


"So etwas hatte ich früher nie erlebt. Ein durchschnittlich aussehender japanischer Teenager, der nur ein bisschen größer ist als normal, zieht normalerweise keine Aufmerksamkeit auf sich, ohne sich darum zu bemühen."


show akira basic_laugh_ni onlayer master
with charachange

aki "Hey, kommt schon. Nur weil ihr Teenager seit, heißt das nicht, dass ihr es nicht mal probieren könnt. Oder?"


hi "Na ja… Ich hab nichts gegen die Musik, wenn es das ist, was du meinst."


show hanako cover_bashful_cas_close_ni onlayer master
with charachange

ha "I-Ich… hab auch nichts… dagegen…"


"Sie schafft es gerade so, die Worte herauszupressen. Es ist ganz anders, als wenn wir allein in der Schule sind, und es enttäuscht mich ein wenig, dass sie so nervös wegen eines Stadtausflugs ist, auf dem wir uns eigentlich amüsieren wollten."


"Es ist schwer, Hanakos Gesicht zu lesen, wenn sie die ganze Zeit nach unten sieht. Kein Wunder, dass sie deswegen selten in die Stadt geht, und ich bin ein wenig dankbar, dass ich meine Narben so leicht verstecken kann."


"Lilly zieht auf ähnliche Weise Blicke auf sich, aber der Grund ist zweifellos ein anderer. Sie sieht kaum aus, als wäre sie von hier, und dasselbe gilt für ihre Schwester. Das kann man aus der Ferne viel eher erkennen, als dass sie blind ist."


"Sie kann es vielleicht nicht sehen, aber ich zweifle kaum daran, dass sie hören kann, welche komischen Bemerkungen die Leute flüstern, die glauben, sie seien außer Hörweite."


"Wie dem auch sei, man sieht ihr weder Verärgerung noch Freude wegen der Aufmerksamkeit an."


hide akira onlayer master
hide lilly onlayer master
with charaexit

"Akira ist jedoch genauso selbstsicher wie immer. Mit einem Lächeln im Gesicht tritt sie mit Lilly an ihrer Seite ein, und wir Zwei folgen ihnen."


stop ambient fadeout 1.0
$ renpy.music.set_volume(1.0, 10.0, channel="music")

scene bg city_clubint onlayer master:
    center
    xpos 0.6
show crowd onlayer master
with locationchange

$ renpy.music.set_volume(0.8, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0

"Ich hatte erwartet, dass sich meine Augen an das Licht im Inneren gewöhnen müssten, aber es ist nicht viel heller als draußen."


"Die Musik von vorher ist jetzt deutlicher zu hören. Dazu gesellen sich das Geräusch von auf Tischen und Tresen herumrutschenden Gläsern und die rauchigen Stimmen der Gäste."
"Ein Blick zu meiner Rechten offenbart den Ursprung der Musik – ein paar Tische weiter spielt eine Jazzgruppe."


"Offenbar sind die meisten Gäste Männer, und obwohl eine Handvoll Frauen anwesend ist, scheint niemand jünger als dreißig zu sein. Abgesehen von uns natürlich."


"Es fühlt sich ein bisschen so an, als wären wir in die 20er Jahre gestolpert, und die Atmosphäre ist recht angenehm. Allein wegen meines Alters fühle ich mich nicht ganz wohl, aber wäre ich älter, würde ich mich wahrscheinlich wie zu Hause fühlen."


show hanako basic_smile_cas_close onlayer master at tworight
with charaenter

"Hanako wirkt jetzt ein bisschen entspannter, was vermutlich daran liegt, dass niemand auf sie achtet. Alle reden miteinander, trinken oder sehen der Band zu."


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

show akira basic_smile behind crowd onlayer master:
    center
    easein 1.0 ypos 1.06
hide crowd onlayer master
with Dissolve(1.0)

"Ohne sich überhaupt umzusehen, setzt sich Akira lässig an den Tresen. Wahrscheinlich war sie schon einmal hier."


show lilly basic_smileclosed_cas onlayer master:
    twoleft
    xpos 0.25
    easein 1.0 ypos 1.1
with Dissolve(1.0)

"Lilly schiebt ihren Stock zusammen, tastet nach dem Barhocker und dem Rand des Tresens und setzt sich dann neben ihre Schwester."
"Nachdem der Barkeeper kurz aufgehört hat ein Glas zu polieren, um einen Blick auf sie zu werfen, kommt er herüber."


"Barkeeper" "Guten Abend, meine Damen. Was soll es sein?"



show akira basic_ending onlayer master:
    center
    ypos 1.06
with charachange

aki "Nur einen Scotch, danke. Lilly?"


show lilly basic_cheerful_cas onlayer master:
    twoleft
    xpos 0.25 ypos 1.1
with charachange

li "Kann ich ein Glas Cham—{w=0.5}{nw}"


show lilly basic_surprised_cas onlayer master
show akira basic_boo onlayer master
with vpunch

"Ein in schwarz gekleideter Ellbogen trifft sie hart in die Seite."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Orangensaft, bitte."


"Barkeeper" "Kein Problem, kommt sofort."


"Er fängt an, ihre Gläser zu füllen. Einige Sekunden vergehen, bis Akira plötzlich einfällt, dass Hanako und ich auch noch da sind, und dreht sich zu uns um."


show akira basic_smile onlayer master
with charachange

aki "Trinkt ihr Zwei was? Oder wollt ihr einfach da rumstehen?"


"Hanako wird anscheinend ein wenig unruhig. Egal wo wir uns hinsetzen, es wird jemand direkt neben ihr sitzen, und ich finde nicht, dass man ihr abkauft, dass sie älter als zwanzig ist – im Gegensatz zu Lilly."


show bg city_clubint onlayer master:
    xpos 0.4
show akira basic_smile onlayer master:
    xpos 0.3
show lilly basic_weaksmile_cas onlayer master:
    xpos 0.05
show hanako basic_smile_cas_close onlayer master:
    xpos 0.5
with charamove

"Als ich mich umsehe, entdecke ich zu unserer Rechten in der Ecke ein paar Billardtische – und im Moment werden sie nicht benutzt."


"Ich blicke zu Hanako und bin kurz davor zu fragen, ob sie spielen will, aber sie schaut bereits sehnsüchtig in dieselbe Richtung. Vielleicht bedeutet es etwas, dass wir mittlerweile mit nur wenigen Worten auskommen."


hi "Wir gehen da drüben Pool spielen."


show akira basic_boo onlayer master
with charachange

"Akira lehnt sich zurück, um an mir vorbeizusehen, zuckt dann mit den Achseln und setzt sich wieder gerade."


show lilly basic_giggle_cas onlayer master
with charachange

li "Offenbar musst du mit mir allein vorliebnehmen. Wie schade."


show akira basic_smile onlayer master
with charachange

aki "Viel Spaß, ihr Zwei."


$ renpy.music.set_volume(0.8, 1.0, channel="music")
stop ambient fadeout 14.0

hide hanako onlayer master
with charaexit

"Wir drehen uns um und machen uns auf den Weg in die abgeschiedene Ecke. Hanako geht voraus."


"Die Aussicht auf ein schönes, ruhiges Spiel weit weg von allen anderen lässt sie spürbar schneller gehen. Ihre Augen bleiben fest auf ihr Ziel fixiert."


scene bg city_clubpool onlayer master
with locationchange

"Dank der hellen Deckenlampen ist der Turniertisch trotz der ihn umgebenden Dunkelheit gut beleuchtet. Ein großes Bild von… etwas… hängt an der Wand."


"In dieser Ecke des Klubs laufen nicht viele Leute herum, und ich kann sehen, wie Hanako dadurch ein bisschen entspannter wird."


show hanako basic_smile_cas onlayer master at center
with charaenter

ha "W-Weißt du… w-wie man spielt?"


hi "Ich bin kein Profi, aber ja, weiß ich."


show hanako basic_bashful_cas onlayer master
with charachange

ha "Dann ähm… 8-Ball?"


hi "Klar."


hide hanako onlayer master
with charaexit

"Hanako holt die Kreide und zwei Billardqueues von einer Reihe Halterungen an einer der Wand, während ich die Kugeln aus den Taschen des Tisches einsammle und das Dreieck von einer Ablage darunter nehme."


"Geduldig wartet sie, während ich den Tisch vorbereite."
"Nachdem ich die letzte Kugel in das Dreieck gesteckt und ein paar abschließende Korrekturen gemacht habe, muss ich mit dem Perfektionisten in mir kämpfen, weil ich die untere Reihe der Kugeln genau senkrecht zum Rahmen ausrichten will."


"Jetzt, da die Kugeln angeordnet sind und wir loslegen können, trete ich zurück und nehme mein Queue entgegen, das sie mir entgegenstreckt. Rasch überprüfe ich die Spitze und stelle fest, dass sie in gutem Zustand ist."


hi "Du hast also schon mal gespielt?"


show hanako cover_bashful_cas onlayer master
with charaenter

ha "Einmal… oder zweimal. Ich k-kenne gewissermaßen… die Regeln."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

"Es herrscht eine etwas unbehagliche Atmosphäre. Sie ist immer noch ziemlich nervös – verständlicherweise, da wir ja in der Öffentlichkeit sind."


"Irgendwann wird das Schweigen sogar für Hanako zu viel, und sie fängt leise an zu stottern."


$ renpy.music.set_volume(0.8, 1.0, channel="music")

show hanako basic_worry_cas onlayer master
with charachange

ha "W-Wer… s-stößt an?"


"Ich überlege kurz, greife dann in meine Tasche und ziehe eine Münze hervor."


hi "Ich nehme Kopf, du Zahl."


"Nachdem Hanako zustimmend genickt hat, werfe ich die Münze in die Luft, fange sie auf und lege sie umgekehrt auf meinen linken Handrücken."


hi "Sieht aus, als dürftest du anstoßen."


$ ksgallery_unlock("ev hanako_billiards_distant")
scene ev hanako_billiards_break onlayer master
with locationchange

"Hanako nickt wieder und geht dann am Ende des Tisches in Position."


"Normalerweise ist sie nicht so still in meiner Gegenwart. Ich bin mir nicht ganz sicher, ob das daran liegt, dass ihr gerade ein kleines Detail über ihre Vergangenheit herausgerutscht ist."


scene bg city_clubpool onlayer master
with flash

play sound sfx_billiards_break

"In einer geübten Bewegung zieht Hanako das Queue zurück und lässt es dann genau in der Mitte der weißen Kugel dumpf aufschlagen. Die Kugel schlittert über die glatte, grüne Fläche und kracht dann in die vorsichtig aufgereihten Kugeln am anderen Ende."


"Mit Höchstgeschwindigkeit jagen Kugeln über den Tisch. Der Anstoß war gut, denn die Kugeln liegen schön auf dem Tisch verteilt. Schon flitzen meine Augen von einer zur anderen, um auszusuchen, welche am einfachsten einzulochen ist."


play sound sfx_billiards

"Hanako tritt zur Seite, und ich versuche mein Glück."


show hanako basic_smile_cas onlayer master at center
with charaenter

ha "Sehr gut."


"Erst nachdem Hanako diese Bemerkung gemacht hat, fällt mir auf, dass ich die Kugel eingelocht habe."


"Ich schaue sie an und bemerke ein kleines Lächeln in ihrem Gesicht. Schön, dass sie beim Spielen etwas lockerer wird."


hi "Dann hab ich wohl die Halben."


show hanako cover_distant_cas onlayer master
with charachange

"Ich mache einen Schritt zurück, sodass sie ihren nächsten Stoß machen kann, aber sie kommt nicht zum Tisch. Vielmehr senkt sie leicht ihren Blick und reibt ihren Arm."


"Mittlerweile weiß ich, dass sie so eine Geste macht, wenn sie etwas sagen will, aber nicht genügend Selbstsicherheit dazu hat."


hi "Was ist los?"


show hanako cover_bashful_cas onlayer master
with charachange

ha "D-Du hast… nur so schön… g-gelächelt. Magst du… Billard?"


"Ich seufze und lehne mich zurück an den Tisch."


hi "Ich mag Billard, ja. Allerdings glaube ich, dass ich gelächelt habe, weil es mich an früher erinnert."


show hanako def_worry_cas onlayer master
with charachange

"Fragend neigt Hanako den Kopf zur Seite."


hi "Ich und meine Freunde haben früher in den Spielhallen in unserer Nachbarschaft oft gespielt, auch abends."


show hanako basic_worry_cas onlayer master
with charachange

ha "H-Haben deine Eltern nicht…"


hi "Meine Eltern haben beide gearbeitet, daher hat es sie nicht gekümmert, ob ich zu Hause bin. Mit der Schularbeit hatte ich auch kaum Probleme, darum hatte ich reichlich Zeit, mich Abends anders zu beschäftigen."


show hanako basic_distant_cas onlayer master
with charachange

"Da Hanakos Schüchternheit die Oberhand gewinnt, ebbt unsere Unterhaltung ab. Ich stehe vom Tisch auf und lasse sie stoßen."



scene ev hanako_billiards_smile onlayer master
with locationchange

"Es liegen nicht viele Volle an guten Stellen, darum beugt sich Hanako vor und nimmt sich etwas Zeit, um sich richtig zu positionieren."


scene ev hanako_billiards_smile_close onlayer master:
    truecenter
    zoom 1.0 subpixel True
    easein 6.0 zoom 0.8
with flash

"Hanakos Gesichtsausdruck ist derselbe, wie bei unseren Schachspielen – entspannt aber voll konzentriert. Manchmal sprechen Sportler davon, dass sie in einem Zustand sind, in dem sie alles Unwichtige ausblenden. Ich frage mich, ob sie das kann."


"Ihre Haltung ist gut – auf jeden Fall besser als meine. Sie ist ziemliche nahe dran, nach dem Lehrbuch zu spielen, während ich mich in irgendeine Position verdrehe, bei der ich das Gefühl habe, dass es die natürlichste Art ist, den Stoß zu machen."


scene ev hanako_billiards_serious onlayer master
with locationchange

"Sie richtet das Queue aus, zieht es zurück und macht ein paar Übungsstöße, um sich zu vergewissern, dass sie richtig steht."


"Hanako nimmt Spiele so ernst. Es ist das einzige Hobby, das ich von ihr kenne, abgesehen von Lesen. Es ist ein schönes Gefühl, so ein Erlebnis mit ihr zu teilen."


scene bg city_clubpool onlayer master
with flash

play sound sfx_billiards

"Nach genauer Überlegung macht sie den Stoß, und die weiße Kugel fliegt auf eine andere zu, die in einem etwas ungünstigen Winkel nahe einer Ecke liegt."


"Hanakos sorgfältige Vorbereitung zahlt sich aus. Die weiße Kugel trifft und stößt die andere in Richtung Ecktasche. Einen Moment lang sieht es so aus, als würde sie direkt am Rand der Tasche liegen bleiben, aber dann kippt sie gerade so hinein."


hi "Mann, das war ein schwieriger Stoß. Wenn du das hinkriegst, habe ich nur wenig Hoffnung."


show hanako emb_emb_cas onlayer master at center
with charaenter

ha "So gut… b-bin ich nicht…"


hi "Es war nicht nur der Stoß; sogar als du gezielt hast, hast du sehr ernst gewirkt. Beim Schach bist du auch so."


show hanako emb_downsmile_cas onlayer master
with charachange

"Das Lob bringt sie ein wenig in Verlegenheit. Sie lehnt den Queue gegen den Tisch, bleibt stehen und dreht sich zu mir um."


ha "Ich mag… solche Sachen einfach…"


"Sie spielt angespannt mit ihren Fingern."


show hanako emb_downtimid_cas onlayer master
with charachange

ha "Als ich im Waisenhaus war… hab ich… e-einfach weiter das gemacht… was mir vorher auch gefallen hat."


ha "Wenn ich m-mit den anderen gespielt habe, d-dann hat das den Betreuern gereicht, also…"


"So habe ich nie darüber nachgedacht. Die Betreuer eines Waisenhauses sind natürlich darauf aus, dass jedes Kind wenigstens ein paar Freunde findet."


hi "Wenn ich fragen darf… Wie war es für dich im Waisenhaus?"


show hanako emb_sad_cas onlayer master
with charachange

ha "W-Warum willst du das wissen?"


"Ich habe einen Nerv getroffen, aber dass sie überhaupt geantwortet hat, zeigt, dass es zumindest eine Chance für eine Antwort auf meine Frage gibt. Früher wäre sie dieser Frage wahrscheinlich ausgewichen, ohne ein Wort zu verlieren."


show hanako emb_blushing_cas onlayer master
with charachange

ha "Ich… sage es dir, aber…"


hi "Aber…?"


show hanako cover_worry_cas onlayer master
with charachange

ha "Sagst du… m-mir, wer I-Iwa… n-nako… ist?"


$ renpy.music.set_volume(0.2, 1.0, channel="music")

hi "Iwanako…? Oh, der Brief."


"Ich frage mich, wie lange sie auf den richtigen Zeitpunkt gewartet hat, um diese Frage zu stellen. Ich bin überrascht, zögere aber nicht. Wenn man etwas wissen will, muss man eben auch etwas von sich preisgeben."


$ renpy.music.set_volume(1.0, 8.0, channel="music")
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 8.0

hi "Ich… mochte sie früher mal."


show hanako basic_normal_cas onlayer master
with charachange

"Ihre Nervosität hat nachgelassen, zumindest nach ihrer Frage. Ihre Neugier siegt, und ich fühle mich etwas unwohl dabei, genau darüber ausgefragt zu werden."


"Ich kann hier unmöglich meine Gefühle für Iwanako ausschütten. Sogar nach meinem Gespräch mit Yuuko heute habe ich selbst keine Ahnung, was ich für sie empfinde, und ich will das Thema in Hanakos Beisein vermeiden."


show hanako def_worry_cas onlayer master
with charachange

"Hanako scheint mit dem Ende des Gesprächs nicht allzu zufrieden zu sein, aber sie fragt nicht weiter nach. Sie hat es gerade so geschafft, mich überhaupt zu fragen, ohne zu wissen, dass das Thema mir unangenehm sein könnte."


"Schließlich setze ich zu meinem Stoß an. Da wir uns nicht unterhalten, treten das Geplapper der anderen Gäste und die Band am anderen Ende des Klubs in den Vordergrund."


hide hanako onlayer master
with charaexit

"Ich habe einen Stoß ausgemacht, der nicht allzu schwer aussieht, und versuche mein Glück."


play sound sfx_billiards

"Die weiße Kugel gibt der anderen einen Schubs. Die Richtung stimmt ungefähr, aber mein Stoß war zu kräftig. Sie streift die Ecke des Lochs und wird zur Seite abgelenkt, sodass sie nur an der Tasche vorbeigeht."


"Ich beiße leicht die Zähne zusammen. Ich war einmal ziemlich gut in Billard, und so viel schlechter geworden zu sein, ist frustrierend."


"Ich ziehe mich zurück und lasse Hanako stoßen, wobei ich einen Blick zum Tresen hinüber werfe, an dem Lilly und Akira sitzen. Sie unterhalten sich eifrig und haben scheinbar eine gute Zeit."


scene ev hanako_billiards_serious onlayer master
with locationchange

"Als Hanako zum Stoß ansetzt, drehe ich mich wieder um. Mit demselben Gesichtsausdruck wie zuvor geht sie in Position und stößt scharf zu."


scene bg city_clubpool onlayer master
with flash

play sound sfx_billiards

"Wie vorher versenkt sie die Kugel, die sie im Visier hatte. Allerdings ist der Stoß noch sauberer als der letzte. Sieht so aus, als würde sie mit dem Spiel langsam warm werden."


hi "Sehr schön."


"Sie zögert einen Moment und fängt dann an, mit mir zu sprechen, ohne den Kopf zu drehen."


scene ev hanako_billiards_smile_med onlayer master
with locationchange

ha "Das Waisenhaus… war schön. Es hat sich ein bisschen so angefühlt wie die Yamaku… und die Betreuer waren w-wirklich nett."


show ev hanako_billiards_distant_med onlayer master
with charachange

ha "Aber im Laufe der Jahre ist mir etwas klar geworden. Ich war a-anders."


"Es ist ungewohnt zu hören, wie sie so offen über sich selbst spricht. Man kann hören, wie sie die Worte herauspresst. Das erinnert mich daran, wie sie darauf beharrte, mir über den Brand zu erzählen."


"Hanako hat wohl das Gefühl, dass sie mir von so etwas erzählen muss, wenn ich dazu bereit bin, ihr von meiner Vergangenheit zu berichten."


"Als sie weiterspricht, wird ihr Griff um das Queue fester."


$ ksgallery_unlock("ev hanako_billiards_timid")
show ev hanako_billiards_timid_med onlayer master
with charachange

ha "Die m-meisten Kinder dort waren frei zur Adoption, so wie ich. Aber im Gegensatz zu mir… sind sie allmählich gegangen, e-einer nach dem anderen. Als ich zur Yamaku ging, gehörte ich… zu den ältesten Kindern dort."


ha "Eine Zeit lang h-half ich mit den j-jüngeren Kindern, a-aber irgendwann…"


scene bg city_clubpool onlayer master
with locationchange

"Ich lege eine Hand auf ihre Schulter. Mittlerweile zwingt sie sich."


hi "Ist schon okay."


show hanako emb_blushtimid_cas_close onlayer master at center
with charaenter

"Für einen Moment wirkt sie leicht überrascht, aber dann nickt sie, setzt ihr Queue ab und dreht sich zu mir."


show hanako basic_worry_cas_close onlayer master
with charachange

ha "Glaubst du… wirklich?"


hi "Ja, das tue ich. Auch wenn Lilly weg ist, bin doch ich da, um dich zu beschützen, hab ich Recht?"


show hanako basic_normal_cas_close onlayer master
with charachange

"Hanako sieht mich lange Zeit an, und ich weiß nicht, was ich tun soll."


"Ihre Miene hat sich nicht geändert, denn sie blickt immer noch etwas betrübt drein. Aber stille Momente sind zwischen uns nichts Ungewöhnliches. Ich glaube, dieses leicht komische Gefühl kommt, weil sie dauerhaften Blickkontakt hält."


"Es fühlt sich an, als ob sie über mich urteilen würde. Ein sehr seltsames und irgendwie unangenehmes Gefühl."


hi "Hanako…?"


show hanako cover_smile_cas_close onlayer master
with charachange

ha "I-Ich verstehe. Danke."


"Sie lächelt und wendet sich etwas ab, aber es wirkt gekünstelt. Hanako ist nicht gerade gut darin, Gefühle vorzutäuschen, und dieses Mal ist keine Ausnahme."


hide hanako onlayer master
with charaexit

"Ich nähere mich dem Tisch und will meinen Stoß machen, um mich abzulenken, aber es scheint nicht zu funktionieren. Glaubt sie, ich wäre nicht in der Lage, ihr zu helfen? Ist sie von mir enttäuscht?"


"Wahrscheinlich denke ich zu viel darüber nach. Obwohl ihr Schweigen inzwischen zum Alltag gehört, wünschte ich manchmal, sie würde mehr reden."


play sound sfx_billiards

"Mit einem dumpfen Stoß lasse ich die weiße Kugel über den Tisch auf mein Ziel zuschlittern."


show hanako def_strain_cas onlayer master at center
with charachange

ha "Ah…"


"Im gleichen Moment wie ich sieht Hanako, was passiert. Die Kugel trifft hart auf, wobei die Halbe, die ich versenken wollte, in Richtung schwarze Kugel abdriftet."


"Während Hanako und ich gespannt zuschauen, treffen sie tatsächlich aufeinander, und die schwarze Kugel rollt gemächlich in eine Ecktasche."


show hanako basic_smile_cas onlayer master
with charachange

"Ich kann nur noch seufzen. Allerdings lächelt Hanako anscheinend wieder, also war es vielleicht nicht umsonst."


hi "Das war ein grauenhafter Stoß. Du gewinnst. Anscheinend bin ich nach all der Zeit tatsächlich ein bisschen eingerostet."


hide hanako onlayer master
with charaexit

"Hanako beugt sich vor und fängt an, alle verbleibenden Kugeln in die nächsten Taschen zu schießen. Fast hätte ich gefragt, ob wir noch einmal spielen, aber ein kurzer Blick auf meine Uhr bestätigt, dass es langsam ziemlich spät wird."


"Lilly und Akira sitzen offenbar immer noch trinkend am Tresen. Wir müssen sie wohl wegzerren."


ha "Ähm, Hisao…"


scene ev hanako_billiards_distant onlayer master
with locationchange

"Ich drehe mich wieder zu Hanako, die immer noch den Tisch im Blick hat und Kugeln einlocht. Ihre Stimme klingt anders als vorher."


scene ev hanako_billiards_smile onlayer master
with charachange

ha "Ich… bin auch für dich da…"


stop ambient fadeout 2.0

hi "Ah…"


"Plötzlich werde ich rot. Wenn man bedenkt, was ich vorher gesagt habe, ist es völlig natürlich, dass sie so antwortet, aber es ist trotzdem überraschend, die Worte tatsächlich zu hören."


scene ev hanako_billiards_smile_close onlayer master:
    xalign 0.0 yalign 0.0 zoom 0.8 subpixel True
    acdc_warp 20.0 zoom 1.0
with locationchange

"Was für eine Beziehung habe ich nur mit diesem Mädchen? Ich will sie beschützen, sie glücklich machen… Ich weiß nicht wirklich, ob es so etwas wie Liebe ist, aber es sind auch nicht dieselben Gefühle, die ich für Lilly habe."


"Sie tut mir leid, weil sie in ihrem Leben so viel durchmachen musste. Ihre Eltern starben bei einem Brand, und sie lebte für den Großteil ihrer Kindheit in einem Waisenhaus… So ein Leben kann ich mir nicht einmal vorstellen."


"Aber ich habe das Gefühl, dass ich nur so wenig für sie tun kann, besonders jetzt, wenn Lilly das Land verlassen wird."


stop music fadeout 10.0

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 4.0

scene bg city_karaokeext onlayer master
show akira basic_boo_ni onlayer master:
    center
    xpos 0.39
show lilly cane_smileclosed_cas_ni onlayer master:
    center
    xpos 0.21
show hanako basic_normal_cas_close_ni onlayer master at tworight
with locationskip

"Hanako und ich räumen den Tisch und die Queues fertig auf und nehmen auf dem Weg aus dem Klub Lilly und Akira mit."


"Ich habe das Gefühl, als hätte sich zwischen Hanako und mir etwas geändert. Was es ist, kann ich nicht ganz einordnen, aber Hanako benimmt sich jetzt anders. Wenn überhaupt, fühlt es sich an, als wären wir weiter voneinander entfernt."


show akira basic_smile_ni onlayer master
with charachange

aki "Und, hattet ihr Spaß?"


show hanako emb_smile_cas_close_ni onlayer master
with charachange

"Hanako und ich nicken beide zustimmend. Es war ein gutes Spiel, und wir haben beide mehr übereinander erfahren. Es ist also eine ehrliche Antwort."


show lilly cane_sleepy_cas_ni onlayer master
with charachange

"Lilly scheint ein wenig abgelenkt zu sein."


hi "Machst du dir Gedanken über deine Reise, Lilly?"


"Sie hält inne, bevor sie seufzt und sich ein schwaches Lächeln abringt."


show lilly cane_weaksmile_cas_ni onlayer master
with charachange

li "Ein wenig. Das ist eine ziemlich große Sache."


show akira basic_laugh_ni onlayer master
show lilly cane_surprised_cas_ni onlayer master
with vpunch

"Für diese Bemerkung bekommt sie von ihrer Schwester einen Klaps auf die Schulter. Hanako gibt ihr ebenfalls ein Lächeln zurück."


show hanako basic_smile_cas_close_ni onlayer master
with charachange

ha "Das wird schon, Lilly. Ich hoffe, du kannst deine Zeit dort drüben genießen."


show lilly cane_smile_cas_ni onlayer master
with charachange

li "Danke, Hanako. Ich werde es versuchen. Immerhin ist es schön, mal wieder bei meiner Familie zu sein, egal wie kurz es auch sein mag."


"Mit diesen Worten machen wir uns auf den Weg zum Parkplatz, auf dem Akiras Auto steht. Unser Gespräch geht noch weiter, aber es ist hauptsächlich Smalltalk."


stop ambient fadeout 2.0
stop music fadeout 2.0

scene black onlayer master
with dissolve



label de_H20:

play music music_daily fadein 2.0

scene bg school_girlsdormhall onlayer master
show lilly basic_smile_cas onlayer master at twoleft
show hanako basic_normal_cas onlayer master at tworight
with locationchange

hi "Also gut. Nimmst du den Bus, Lilly?"


show lilly basic_smileclosed_cas onlayer master
with charachange

"Lilly zeigt auf einen großen Reisekoffer, der neben ihr steht."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Ich werde das mitnehmen müssen, darum habe ich ein Taxi gerufen. Es kommt in ungefähr fünf Minuten zum Schultor."


hi "Ah, alles klar."


show lilly basic_sleepy_cas onlayer master:
    ypos 1.1
with dissolvecharamove

"Lilly greift nach unten und fühlt nach dem Griff ihres Koffers. Sein Gewicht macht ihr Probleme, darum biete ich schnell an, ihn für sie zu tragen."


show lilly basic_smileclosed_cas onlayer master at twoleft
with dissolvecharamove

li "Das ist sehr nett von dir, Hisao."


"Sie hat nichts dagegen, also nehme ich ihn. Leicht würde ich den Koffer nicht nennen, aber schwer ist er auch nicht gerade. Ich glaube nicht, dass er mir zu schwer werden wird."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "Also gut, danke. Wir sollten uns aber beeilen. Falls das Taxi weg ist, wird es eine Zeit dauern, ein neues zu rufen. Bist du so weit, Hanako?"


show hanako cover_worry_cas onlayer master at tworight
with charachange

ha "J-Ja. Lasst uns gehen."


$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg school_gate onlayer master at bgright
with locationskip

"Wir eilen so schnell es geht zu den Toren, nur um zu sehen, dass das Taxi noch gar nicht da ist."


hi "Na ja, es gibt nichts Besseres als ein bisschen Frühsport. Doc meinte, ich soll welchen machen."


show lilly basic_weaksmile_cas onlayer master at center
with charaenter

li "Ich glaube, er hatte wohl etwas anderes im Sinn, Hisao. Und wahrscheinlich etwas regelmäßiger. Oder hast du vor, jeden Tag Gepäck zu schleppen?"


hi "Wohl eher nicht. Sieht so aus als müssten wir sowieso etwas warten. Wie lange sollen wir auf das Taxi warten, bis wir wieder anrufen?"


show lilly basic_smileclosed_cas onlayer master
with charachange

li "Ich würde sagen noch zehn Minuten, Aber bisher haben sie mich nie im Stich gelassen. Es ist vermutlich bloß ein bisschen viel los auf den Straßen."


hi "Also gut."


hi "Wie lange dauert denn der Flug nach Schottland."


show lilly basic_smile_cas onlayer master
with charachange

li "Etwa sechzehn Stunden, falls ich mich richtig erinnere. Mit den verschiedenen Zeitzonen ist das etwas schwer zu sagen."


show bg school_gate onlayer master at center
show lilly basic_smile_cas onlayer master at twoleft
with charamove

show hanako defarms_worry_cas onlayer master at tworight
with charaenter

ha "So lange…"


"Jetzt fällt mir auf, dass Hanako ungewöhnlich still ist, sogar für ihre Verhältnisse. Sie kommt mit Stress nicht gut klar, daher sieht sie etwas verspannt aus."


hi "Ja, ich kann mir nicht vorstellen, so lange in einem Flieger zu sitzen."


"Ich bin bisher nur für einen kurzen Familienurlaub in den Norden geflogen, darum ist das wirklich schwer nachzuvollziehen."
"Wenn Hanako einen so großen Teil ihrer Kindheit in einem Waisenhaus verbracht hat, ist sie wahrscheinlich nur wenig gereist, geschweige denn geflogen."


show lilly basic_weaksmile_cas onlayer master
with charachange

li "So schlimm ist es nicht. Die meiste Zeit werde ich schlafen oder mein Englisch aufpolieren. Hier benutze ich mein Englisch fast nicht, also muss ich mich wieder ein bisschen daran gewöhnen."


show hanako cover_worry_cas onlayer master
with charachange

ha "W-Wird dein Akzent… Probleme machen?"


show lilly basic_smile_cas onlayer master
with charachange

li "Darüber würde ich mir nicht zu viele Sorgen machen. Anfangs wird es vielleicht ein Problem sein, aber sobald ich mich daran gewöhnt habe, sollte alles gut gehen."


show hanako basic_worry_cas onlayer master at Position(ypos=1.14)
show lilly basic_smileclosed_cas onlayer master at Position(ypos=1.17)
with dissolvecharamove

"Schweigend setzen wir uns alle auf die kleine Bank neben den Schultoren."


"Obwohl ich weiß, dass Lilly wegfährt, fällt mir merkwürdigerweise nichts ein, was ich zu ihr sagen könnte. Vielleicht ist es so, weil Lilly so verlässlich ist. Sie ist nicht diejenige, um die ich mir am meisten Gedanken mache."


show hanako emb_downsad_cas onlayer master
with charachange

"Lilly kann es vielleicht nicht sehen, aber Hanako kaut nervös auf ihren Fingernägeln herum. Ich will gerade mit ihr reden, doch bevor ich dazu komme, höre ich ein Auto den Hügel hochkommen."


hi "Ah, ich glaube, das Taxi kommt gerade…"


show lilly basic_cheerful_cas onlayer master
with charachange

li "Gut erkannt, Hisao. Ich habe es auch gerade erst gehört."


"Das macht mich ein klein wenig Stolz. Dass ich etwas zur gleichen Zeit wie Lilly bemerkt habe, heißt wohl, dass ich meine Umgebung bewusster wahrnehme."


"Jedenfalls müssen wir weder die Taxifirma anrufen noch brauchen wir uns Gedanken darüber zu machen, dass Lilly ihren Flug verpasst."


show hanako basic_worry_cas onlayer master at tworight
show lilly basic_smileclosed_cas onlayer master at twoleft
with dissolvecharamove

"Sobald das Taxi bei uns stehen bleibt, fährt der Fahrer das Fenster herunter und lehnt sich herüber. Nachdem wir bestätigt haben, dass Lilly dieselbe Lilly Satou ist, die die Fahrt gebucht hat, holen wir ihr Gepäck."


hide lilly onlayer master
with charaexit

"Der Fahrer öffnet den Kofferraum des Taxis und nimmt Lillys Reisekoffer. Während Lilly auf den Rücksitz klettert, lädt er ihn in den Kofferraum und klappt ihn zu."


"Nachdem er sich wieder auf seinen Platz gesetzt und die Türen geschlossen hat, wartet er, bis wir uns verabschiedet haben."


show hanako emb_downtimid_cas onlayer master
with charachange

ha "Gute Reise, Lilly."


hi "Pass auf dich auf."


"Hanako sieht verständlicherweise niedergeschlagen aus, und das hört man sogar in ihrer Stimme."


li "Natürlich mache ich das. Ich werde bald wieder zurück sein, keine Sorge. Und es gibt ja immer noch jemanden, der für dich da ist, stimmt's Hisao?"


hi "Ja, natürlich."


show hanako emb_blushtimid_cas_close onlayer master
with characlose

"Ich wende mich Hanako zu und lächle. Dabei lege ich meine Hand auf ihre Schulter."


show hanako emb_downtimid_cas_close onlayer master
with charachange

"Sie schafft es nur ein paar Sekunden lang, mir in die Augen zu sehen. Ihre Wangen sind die ganze Zeit über rot. Dann blickt sie wieder zu Lilly."


hi "Bis dann, Lilly."


show hanako basic_worry_cas_close onlayer master
with charachange

ha "Auf Wiedersehen!"


stop music fadeout 6.0

"Mit deutlicher Zurückhaltung verabschiedet sich Lilly von uns beiden. Der Fahrer schmeißt den Motor kurzerhand wieder an, und sie beginnen ihre Fahrt den Hügel hinunter in Richtung Flughafen."


"Sogar nachdem sie aus unserem Sichtfeld verschwunden sind, bleiben wir beide eine ganze Weile an den Toren stehen. Wir wissen nicht wirklich, was wir tun sollen."


show bg school_gate onlayer master at bgleft
show hanako basic_worry_cas_close onlayer master at center
with charamove

hi "Also, was willst du machen?"


show hanako def_worry_cas_close onlayer master
with charachange

ha "Ich… weiß nicht."


label de_choiceH20:
menu:
    with menueffect
    "Willst du in die Stadt gehen?":


        return m1
    "Wie wär's, wenn wir für heute Schluss machen?":


        return m2



label de_H20_1:

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")

"Die Bushaltestelle, die wie ein stiller Wächter bei den Schultoren steht, bringt mich auf eine seltsame Idee."


hi "Willst du in die Stadt gehen und nach einem Buchladen Ausschau halten oder so? Den Rest des Tages haben wir frei."


"Es ist gewagt, weil Hanako nicht gerne in die Stadt geht. Dass wir es sogar in der Dunkelheit geschafft haben, sie dorthin zu schleppen, ist für mich kleines Wunder, aber ich will wirklich mehr Zeit mir ihr verbringen."


"Wie auch immer, sie wird wahrscheinlich ablehnen und wieder…"


show hanako basic_smile_cas_close onlayer master
with charachange

ha "Okay."


hi "Wirklich?"


show hanako basic_bashful_cas_close onlayer master
with charachange

ha "W-Wirklich. Gehen wir."


"Ich weiß nicht, warum Hanako sich entschlossen hat zuzustimmen, aber ich werde sie nicht bitten, ihre Meinung zu ändern."


stop ambient fadeout 2.0

scene bg city_street2 onlayer master
show crowd onlayer master
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0

"Als ich aus dem Bus aussteige, fällt mir sofort auf, dass um uns herum sehr viele Menschen sind. Im Nachhinein war das eigentlich logisch; natürlich ist an einem Samstagnachmittag in der Innenstadt viel los."


show hanako emb_downtimid_cas_close onlayer master at center
with charaenter

"Hanako weicht an meine Seite zurück, und ich kann ihre Hand spüren, wie sie meinen Arm fest umklammert. Ihr Körper ist ganz nah an meinem und sie hält ihren Kopf so weit unten, dass ihre Mütze den Großteil ihrer Narben verdeckt."


hi "Also äh, wo sollen wir hingehen? Einen Buchladen?"


"Das Geschenk für Hanako und meine allgemeinen Haushaltskosten haben mein Budget ganz schön erschöpft, aber ein paar Bücher sollte ich mir leisten können. Dafür versuche ich sowieso immer, ein bisschen Geld zurückzulegen."


"Einen Moment lang dachte ich, Hanako hätte mich nicht gehört, aber dann blicke ich zur Seite und sehe, dass sie fast unmerklich nickt."


show hanako emb_smile_cas_close onlayer master
with charachange

ha "O-Okay. K-Kennst du einen?"


hi "Ich kenne tatsächlich einen. Wir sind an ein paar vorbeigekommen, als Lilly und ich nach Geschenken für dich gesucht haben…"


show hanako emb_downsad_cas_close onlayer master
with charachange

"Hanakos Miene verdunkelt sich ein bisschen. Ich muss daran denken, ihren Geburtstag nicht mehr anzusprechen."


show hanako emb_timid_cas_close onlayer master
with charachange

ha "Habt ihr beide… viel Zeit miteinander verbracht?"


"Oder vielleicht habe ich die Situation falsch eingeschätzt."


hi "Immerhin wollten wir sicher sein, dass wir das richtige Geschenk haben."


show hanako emb_smile_cas_close onlayer master
with charachange

"Hanako lächelt und wird ein bisschen rot. Das ist bei ihr ein seltener Anblick."


hi "Jedenfalls sollte direkt geradeaus ein Buchladen sein. Willst du reinschauen?"


show hanako basic_bashful_cas_close onlayer master
with charachange

ha "S-Sicher."


scene bg city_street1 onlayer master
show crowd onlayer master
with locationchange

"Die Menge wird dichter, während wir entlang der Hochwege zum Buchladen gehen. Hanako klammert sich jetzt auch mit ihrem anderen Arm an mich, wodurch wir etwas langsamer vorankommen."


"Während wir so dahingehen, bringt mich der Verkehrslärm auf eine mögliche Ablenkung für sie."


hi "Sag mal, Hanako… Hast du dir schon überlegt, wann du Autofahren lernst?"


show hanako cover_worry_cas_close onlayer master
with charachange

ha "A-Autofahren?"


hi "Ja. In gewisser Hinsicht hast du Glück; es gibt nicht sonderlich viele Schüler an der Yamaku, die fahren dürfen."


"Es ist nicht das beste Gesprächsthema, aber ich will versuchen, Hanako von der Situation abzulenken. Im Moment ist sie wirklich sehr nervös."


"Andererseits habe ich die Situation für sie nur noch unangenehmer gemacht, weil sie vermutlich noch nie darüber nachgedacht hat. Ich wünschte, ich hätte nichts gesagt."


stop ambient fadeout 0.5

scene bg city_street3 onlayer master at left
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

"Bald stehen wir vor einem der Buchläden, an denen Lilly und ich bei unserer Suche vorbeigekommen sind."


hi "Welcher anständige Buchladen hat Samstags geschlossen?"


show hanako def_worry_cas_close onlayer master at center
with charaenter

ha "Buchläden… machen nicht mehr viel Geld, wegen des Internets. Vielleicht mussten sie an den Wochenenden einfach zumachen?"


"Anscheinend kennt sie sich mit Technologie recht gut aus. Ich schätze, das passt gut zu jemandem, der es genießt, allein zu sein."


hi "Hm, das ergibt wohl Sinn… Es ist einfacher, Bücher online zu finden. Jedenfalls können wir die Idee wohl vergessen. Gibt es irgendetwas anderes, was du tun willst?"


show hanako emb_smile_cas_close onlayer master
with charachange

ha "W-Wenn es… keine Umstände macht… könntest du mir zeigen, wo du mein Geschenk gekauft hast?"


hi "Klar, kein Problem. Es ist nicht weit von hier."


hide hanako onlayer master
with charaexit

show bg city_street3 onlayer master at right
with charamove_slow

"Ich mache mich in Richtung des Ladens auf, wobei ich mir nicht ganz sicher bin, wo er genau ist. Ich will keine Wiederholung vom letzten Mal; da sind wir den halben Tag ziellos umhergewandert."


hi "Da sind wir: Othello's Antiquitäten."


show hanako basic_normal_cas_close onlayer master at center
with charaenter

ha "E-Er ist klein."


hi "Na ja, stimmt. Es hat einige Zeit gedauert, bis Lilly und ich ihn gefunden haben."


show hanako basic_distant_cas_close onlayer master
with charachange

ha "Können wir reingehen?"


hi "Warum nicht? Er hat offen."


stop ambient fadeout 0.5
play sound sfx_storebell
play music music_soothing fadein 0.5

scene bg city_othello onlayer master
with locationchange

"Hanako drückt die Tür auf und geht vor mir hinein. Wieder ist der Laden leer bis auf den Besitzer."


show shopkeep neutral onlayer master at center
with charaenter

"Seine Miene verfinstert sich ein wenig, als er mich sieht."


sk "Oh, Sie sind nicht hier, um etwas zurückzugeben, oder? Moment, das ist nicht das Mädchen, mit dem Sie letztes Mal da waren…"


hi "Äh, nein. Wir wollen nichts zurückgeben. Wir waren nur in der Stadt und wollten uns hier noch mal umsehen."


show shopkeep thinking onlayer master
with charachange

"Der Ladenbesitzer denkt ziemlich lange darüber nach. Ich schätze, er ist nicht daran gewöhnt, dass regelmäßig Oberschüler in seinen Laden kommen."


show shopkeep happy onlayer master
with charachange

sk "Ist das vielleicht die Freundin, für die Sie Geschenke gekauft haben?"


hi "Ja genau. Die Geschenke waren für sie."


show shopkeep happy onlayer master at twoleft
show bg city_othello onlayer master at bgleft
with charamove

show hanako defarms_strain_cas_close onlayer master at tworight
with charaenter

"Der Ladenbesitzer wendet sich Hanako zu, die auf der Stelle erstarrt wie ein Reh im Scheinwerferlicht."


show shopkeep surprised onlayer master
with charachange

"Er will sie ansprechen, hält dann aber etwas verdutzt inne."


show shopkeep thinking onlayer master
with charachange

"Ihm wird klar, dass er sie anstarrt und sieht zur Seite. Er spricht uns indirekt an. Sein Blick ist unbehaglich und angespannt, so wie sein ganzer Körper."


"Ich will wütend auf ihn sein, aber ich weiß ganz genau, dass ich instinktiv dieselbe Reaktion hatte, als ich sie das erste Mal sah. Erst Überraschung, dann Neugier, dann ein peinlicher Blick, während ich den Anblick verarbeitete."


show hanako emb_downsad_cas_close onlayer master
with charachange

"Hanako sieht nicht so panisch aus wie zuvor… aber ich glaube, der Eindruck, der jetzt von ihr ausgeht, ist schlimmer. Sie ist weder wütend noch verärgert. Wenn überhaupt wirkt sie entschuldigend."


show shopkeep neutral onlayer master
with charachange

sk "Da haben Sie aber Glück, junge Dame. Freunde zu haben, denen Sie so wichtig sind."


show hanako emb_downtimid_cas_close onlayer master
with charachange

ha "D-Danke…"


"Wenn ich nicht so viel mit Hanako zu tun hätte, wäre mir nicht einmal aufgefallen, dass sie etwas gesagt hat. Andererseits war das Gemurmel des Ladenbesitzers auch kaum zu verstehen – zum Teil weil er in eine andere Richtung spricht."


hide hanako onlayer master
with charaexit

show bg city_othello onlayer master at left
show shopkeep invis onlayer master:
    xpos 0.6 alpha 0.0
with dissolvecharamove

"Hanako macht sich auf in den Laden und bestaunt die diversen ausgestellten Gegenstände. Sie findet die Puppenabteilung und verbringt Minuten damit, jede einzelne genau zu studieren."


"Es ist eine Seite von Hanako, die ich bisher kaum zu Gesicht bekommen habe. Ich war erstaunt, als Lilly mir erzählte, dass sie Puppen mag. Und noch erstaunter war ich, als ich ihre „Sammlung” auf ihrem Schränkchen entdeckte."


show hanako basic_normal_cas_close onlayer master at center
with charaenter

"Jetzt, da sie abgelenkt ist und fern vom Sichtfeld des Ladenbesitzers, sieht sie etwas besser aus, aber ich bin von der ganzen Erfahrung immer noch ziemlich verunsichert."


"Ich habe zwar selbst Probleme, aber Fremde haben noch nie so auf mich reagiert, als ob ich für sie völlig fremdartig wäre."


show hanako basic_smile_cas_close onlayer master
with charachange

ha "Das ist ein schöner Laden."


hi "Ja, er ist anders als ich erwartet hatte. Willst du etwas kaufen?"


show hanako cover_worry_cas_close onlayer master
with charachange

ha "I-Ich habe kein Geld dabei."


hi "Na ja, wir können jederzeit wiederkommen."


"Zumindest jetzt, wo ich weiß, wie man hierher findet."


show hanako cover_bashful_cas_close onlayer master
with charachange

ha "K-Können wir?"


hi "Natürlich. Wir können so oft hierher kommen wie du willst."


show hanako basic_bashful_cas_close onlayer master
with charachange

ha "D-Danke."


hi "Du brauchst mir nicht zu danken; ich hatte fast vergessen, wo der Laden ist."


"Ich denke nicht, dass einer von uns beiden wirklich glaubt, was wir sagen. Wir wiederholen eher das, wovon wir denken, es sagen zu müssen."


show hanako emb_smile_cas_close onlayer master
with charachange

ha "K-Können wir jetzt zurück zur Schule gehen?"


hi "Sicher doch. Gehen wir."


stop music fadeout 5.0
play ambient sfx_traffic fadein 2.0

scene bg city_street3 onlayer master at right
with locationchange

"Als wir uns zur Bushaltestelle aufmachen, sehe ich, wie der Ladenbesitzer aus dem hinteren Bereich des Ladens hinter dem Vorhang hervorlugt."


"Ich bin mir nicht sicher, was der Blick, den er ihr zuwirft, bedeuten soll. Er wirkt etwas seltsam, und die Tatsache, dass Hanako es nicht gesehen hat, ist sowohl eine Erleichterung als auch ein wenig frustrierend."


stop ambient fadeout 2.0

scene bg school_dormext_full onlayer master
with shorttimeskip

"Sobald wir den Bereich aus Beton zwischen den Wohnheimen erreicht haben, bleiben Hanako und ich stehen. Auf dem Rückweg aus der Stadt haben wir kaum ein Wort gewechselt."


show hanako basic_bashful_cas onlayer master at center
with charaenter

ha "Also dann. Tschüss."


hi "Willst du einen Tee oder so? Wie wär's mit einem Spiel?"


show hanako emb_emb_cas onlayer master
with charachange

"Peinlich berührt schüttelt Hanako ihren Kopf."


ha "Ich… bin müde. Vielleicht später? Ich muss Hausaufgaben machen…"


"Sie klingt ein wenig niedergeschlagen. Hanako will ganz klar nichts mehr unternehmen, aber ich nehme an, sie hat ein bisschen was nachzuholen für die Schule; sie hat ein paar Tage gefehlt."


hi "Ah, Hausaufgaben. Danke für die Erinnerung; ich hab auch einen Haufen zu machen. Ich sehe dich dann wohl morgen."


show hanako basic_smile_cas onlayer master
with charachange

ha "Bis dann, Hisao."


hide hanako onlayer master
with charaexit

"Bevor ich mich verabschieden kann, hat Hanako sich umgedreht und ist in Richtung Mädchenwohnheim gegangen."


"Eine Weile schaue ich auf die Tür, durch die sie verschwindet, und mache mich dann auf zu meinem eigenen Zimmer."


"Heute war ein anstrengender Tag."


$ renpy.music.set_volume(1.0, 0.0, channel="ambient")



label de_H20_2:

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")

hi "Ich weiß nicht, wie es mit dir steht, aber ich glaube, ich mache ein Schläfchen. Mein Kopf bringt mich um."


show hanako basic_distant_cas_close onlayer master
with charachange

"Hanakos Erleichterung nach zu urteilen, kann ich nur annehmen, dass ich richtig geraten habe. Ich glaube nicht, dass sie etwas unternehmen will."


hide hanako onlayer master
with charaexit

"Wortlos dreht sie sich um und geht zurück durch das Schultor."


scene bg school_dormext_full onlayer master
with locationskip

"Zusammen gehen wir den ganzen Weg zurück zu den Wohnheimen und bleiben unbeholfen dort stehen, wo wir uns trennen müssen."


show hanako cover_distant_cas onlayer master at center
with charaenter

ha "Also dann. T-Tschüss."


hi "Willst du später einen Tee oder so? Wie wär's mit einem Spiel?"


show hanako emb_timid_cas onlayer master
with charachange

"Peinlich berührt schüttelt Hanako ihren Kopf."


show hanako emb_downtimid_cas onlayer master
with charachange

ha "Ich… ich bin müde. Vielleicht morgen? Ich muss Hausaufgaben machen…"


"Ich nehme an, sie hat ein bisschen was nachzuholen für die Schule; immerhin sie hat ein paar Tage gefehlt."


hi "Ah, Hausaufgaben. Danke für die Erinnerung; ich hab auch einen Haufen zu machen. Ich sehe dich dann wohl morgen."


show hanako emb_downsmile_cas onlayer master
with charachange

ha "Bis dann, Hisao."


hide hanako onlayer master
with charaexit

"Bevor ich mich verabschieden kann, hat Hanako sich umgedreht und ist in Richtung Mädchenwohnheim gegangen."


"Eine Weile schaue ich auf die Tür, durch die sie verschwindet, und mache mich dann auf zu meinem eigenen Zimmer."


"Morgen wird ein besserer Tag."


stop ambient fadeout 1.0
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
