label de_R1:






window hide None

scene bg school_scienceroom onlayer master
with locationchange

with Pause(1.0)

play music music_normal fadein 6.0

window show

"Es ist schon halb neun, aber der Unterricht hat noch nicht angefangen. Eigentlich hätten wir Physik, aber unser Lehrer ist nirgends zu sehen."


"Hätte ich das vorher gewusst, wäre ich auch liegen geblieben."


play sound sfx_doorslam
with vpunch

"Plötzlich wird die Tür des Klassenzimmers aufgerissen, und Mutou grummelt uns seine morgendliche Begrüßung entgegen."


show muto normal onlayer master at center
with charaenter

mu "Guten morgen, miteinander!"


"Mutou sieht aus, als hätte er die ganze Nacht nicht geschlafen."


"Die Bartstoppeln, sein Haar, das noch zerwühlter ist als sonst, und das fleckige Hemd hinterlassen einen nicht gerade schmeichelhaften Eindruck."


"Ich schätze, er hatte letzte Nacht auch seinen Spaß auf dem Fest."


show muto irritated onlayer master
with charachange

mu "Entschuldigt bitte die Verspätung, aber ich hatte ein paar unerwartete Probleme. Ich mache mir normalerweise nichts aus solchen Festen, aber ich hoffe, ihr hattet euren Spaß."


mu "Solche Feste sind schließlich wichtig für euch. Sie bescheren euch eine kleine Ruhepause von eurem Schulalltag."


show muto normal onlayer master
with charachange

"Die Reaktion der Klasse ist mal mehr, mal weniger enthusiastisch, und Mutou beginnt, die Anwesenheitsliste zu prüfen."


mu "Also dann. Das heutige Thema ist Teilchenphysik…"


hide muto onlayer master
with shorttimeskip

"Nach kurzer Zeit versinke ich, zusammen mit dem Rest der Klasse, in einen komaartigen Zustand. Mutous langatmige Vorträge passieren meine Gehörgänge, ohne in meinem Gehirn registriert zu werden."


show muto normal onlayer master at center
with charaenter

mu "Nun, wer könnte uns die Lösung für dieses Problem verraten?"


"Er hat eine relativ einfache Gleichung an die Tafel geschrieben und versucht nun verzweifelt, die Klasse zur Mitarbeit zu bewegen."


show muto irritated onlayer master
with charachange

mu "Niemand? Na kommt schon. Nakai, wie sieht's aus?"


"Mit dem Gefühl, unfair herausgepickt worden zu sein, antworte ich ihm. Seine wirren Gesichtszüge verziehen sich zu einem Lächeln, mit dem man kleine Kinder erschrecken könnte."


show muto smile onlayer master
with charachange

mu "Ganz genau! Sehr gut Nakai!"


"Es ist gleichermaßen irritierend und schmeichelhaft, dass er sich nur eine Woche, nachdem ich die Schule gewechselt habe, an meinen Namen erinnert."


"Ich hatte bisher den Eindruck, dass Mutou ernsthafte Schwierigkeiten damit hat, sich die Namen seiner Schüler überhaupt zu merken, und die meisten von ihnen sind seit dem ersten Jahr der Oberstufe hier."


"Im Raum breitet sich eine triste Stimmung aus. Nach dem Fest versuchen die Schüler und Lehrer gleichermaßen, zu ihrem Tagesrhythmus zurückzufinden."


"Ich schätze, die letzte Woche war für alle ziemlich hektisch."


play sound sfx_normalbell

stop music fadeout 2.0

"Nicht eine Minute zu früh läutet die Klingel die Mittagspause ein."


scene bg school_hallway3 onlayer master
with locationchange

play music music_running

mystery "AUS DEM WEG! WICHTIGE ANGELEGENHEITEN!"



"Ich drehe meinen Kopf und sehe gerade noch, wie ein paar der anderen zur Seite springen, um einer Gestalt auszuweichen, die vom Ende des Korridors auf das Treppenhaus zustürmt."


"Als ich bemerke, dass ich in der Mitte dieses Korridors stehe – mitten in der Bahn des heranrauschenden, menschlichen Geschosses – ist es bereits zu spät."


"Ich versuche, zurück durch die Tür zu springen. Unglücklicherweise weicht die Person, die auf mich zugerannt kommt, in dieselbe Richtung aus."


"Innerhalb eines Bruchteils der darauf folgenden Sekunde fallen mir – beinahe gleichzeitig – mehrere Dinge auf."


"Als erstes erkenne ich, dass es sich bei dem Mädchen, mit dem ich mich auf Kollisionskurs bin, um Emi handelt."


"Zweitens stelle ich fest, dass es mir irgendwie natürlich vorkommt, wieder von Emi umgerannt zu werden. Ich würde mich fast wohlfühlen, wären da nicht die reflexartige Panik und Angst."


"Und drittens scheint Emi beim Rennen einen ein riesigen Stapel Papiere zu tragen."


play sound sfx_pillow
with vpunch

"Wir stoßen zusammen, aber dieses Mal trifft der Aufprall zum Glück hauptsächlich meinen Arm."


show emi sad_depressed onlayer master at center
with charamoveinbottom

emi "Auaaaa… Warum passiert so was immer mir?"


hi "Ja, warum nur. Könnte es möglicherweise damit zu tun haben, dass du durch die Gänge rennst, als wäre der Leibhaftige hinter dir her?"


show emi sad_shy onlayer master
with charachange

"Als Reaktion auf meine Kritik wimmert sie kleinlaut und schaut mich an wie ein verletzter Welpe. Der Anblick lässt mich meine schnippische Bemerkung bereuen, kaum dass ich sie ausgesprochen habe."


show emi sad_pout onlayer master
with charachange

emi "Aber… ich hatte es eilig."


hi "Hab ich gemerkt."


emi "Tut mir leid."


hi "Schon okay."


show emi sad_shy onlayer master
with charachange

"Emi gibt noch ein letztes, schwaches Wimmern von sich und reibt sich mit zu Boden gerichtetem Blick die Stirn, als könne sie den Schmerz so lindern."


"Als sie bemerkt, dass ihr eben noch ordentlicher Papierstapel in einem riesigen Durcheinander über den Fußboden verteilt wurde, entweicht ihr ein entsetztes Jaulen."


show emi basic_shock onlayer master
with charachange

emi "Aah! Die Ausdrucke! Oh nein, oh nein, was mach ich nur? Mein Lehrer wird mir die Hölle heiß machen, wenn sie schmutzig werden."


hi "Sie werden schon in Ordnung sein. Sammeln wir sie wieder auf; das wird schon."


"Nachdem wir das Papier wieder aufgesammelt haben, versucht Emi, den durcheinander geratenen Stapel in ihrem Arm wieder in die alte Ordnung zu bringen."


show emi basic_grin onlayer master
with charachange

emi "Wo willst du hin?"


hi "Ich hatte kein bestimmtes Ziel. Wollte nur nicht mit Mutou allein im Klassenzimmer bleiben. Ich glaube, er hat einen Kater."


show emi excited_happy onlayer master
with charachange

emi "Hast du schon zu Mittag gegessen?"


hi "Noch nicht, aber ich bin auch nicht besonders hungrig."


show emi basic_confused onlayer master
with charachange

"Sie sieht mich ungläubig an, als ließe sie diese Aussage an meinem Verstand zweifeln."


show emi excited_proud onlayer master
with charachange

emi "Du solltest aufs Dach gehen! Ich hab Rin versprochen, dass ich mit ihr zu Mittag esse. Ich wette, sie würde sich über die Gesellschaft freuen."


"Oh oh. Meine Mahlzeiten mit Rin waren bisher immer etwas seltsam."


"Ich weiß, worauf diese Unterhaltung hinausläuft, und es ist schwierig, sich zu widersetzen. Ich habe also kaum eine andere Wahl als mitzuspielen."


hi "Okay, Ich besorge vorher noch ein paar Brote oder so."


show emi basic_closedgrin onlayer master
with charachange

"Bevor ich noch etwas anderes sagen kann, beginnt Emi zu strahlen."


show emi basic_grin onlayer master
with charachange

emi "Nein, nein. Ich geh die hier noch superschnell abliefern, und dann kauf ich uns etwas zum Mittagessen. Für Rin natürlich auch. Was für ein Brot magst du?"


hi "Schon okay, du musst wirklich nicht…"


show emi excited_proud onlayer master
with charachange

emi "Mach dir keine unnötigen Gedanken, das passt schon. Sieh's als Entschuldigung an. Ich bin im Handumdrehen wieder zurück."


hi "Genau deswegen mache ich mir ja Sorgen. Bau nicht noch einen Unfall."


"Emi beginnt, den Gang entlangzulaufen, schaut dabei aber nicht nach vorne, weil sie immer noch mit mir redet."


show emi basic_closedhappy onlayer master
with charachange

emi "Werd ich nicht!"


hide emi onlayer master
with charaexit

stop music fadeout 4.5

"Berühmte letzte Worte. Sie ist schon dabei, die Treppe hinunterzujoggen, während sie mir dieses nicht gerade beruhigende Versprechen zuruft."


$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 2.0

scene bg school_staircase1 onlayer master
with locationchange

"Leise seufzend mache ich mich auf den Weg, ihr zu folgen. Anstatt die Stufen hinunterzugehen, steige ich aber nach oben."


"Die letzten paar Stufen zum Dach sind nicht beleuchtet und ein wenig unheimlich."


play sound sfx_dooropen

"Die Tür quietscht in schwachem Protest, als ich sie aufschiebe."


play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 0.5, channel="ambient")


scene bg school_roof onlayer master
with Fade(0.5, 0.0, 2.0, color="#FFF")

"Rin ist auch hier, wie Emi gesagt hat. Aus irgendeinem Grund liegt sie aber auf dem Rücken am anderen Ende des kiesbedeckten Daches."


"Bereits ahnend, dass wieder etwas unnötig Schräges geschehen wird, laufe ich so langsam wie möglich zu ihr."


scene ev rin_roof_boredom onlayer master
with locationchange

rin "Halloooo."


"Sie klingt sehr verschlafen und streckt den letzten Teil des Wortes, als unterdrücke sie dabei ein Gähnen; ihre Augen sind aber weit geöffnet."


show hisao rin_roof onlayer master
with charaenter

"Ich schaue zu ihr nach unten, wobei mein Schatten auf ihr Gesicht fällt."


hi "Was machst du da?"


show ev rin_roof_doubt onlayer master
with charachange

"Rin hebt eine Augenbraue."


show ev rin_roof_nonchalant onlayer master
with charachange

rin "Ich dachte, du hättest ein Herzproblem, kein Augenproblem."


"Sie hinterfragt die Rationalität meiner völlig berechtigten Frage und macht sich noch nicht mal die Mühe, auch nur den Kopf zu drehen, um mich anzuschauen."


"Rins Klugscheißerei kann einen wirklich zur Weißglut treiben. Das Schlimmste daran ist aber, dass ich mir nicht sicher bin, ob sie das mit Absicht macht oder nicht."


hi "Also gut, dann lass es mich anders ausdrücken:"


hi "Warum liegst du auf dem Rücken auf dem Dach?"


show ev rin_roof_boredom onlayer master
with charachange

"Sie zuckt träge mit den Schultern und schnieft gleichgültig."


rin "Ich versuche zu erleben. Die meisten Leute machen das vermutlich nicht genug."


hi "Was genau versuchst du hier denn zu erleben? Ich weiß es nicht wirklich, aber es gibt wahrscheinlich einen Grund, warum die meisten nicht… was auch immer machen."


"Sie spielt wieder Katz und Maus mit mir. Jeder Versuch, ein Gespräch in Gang zu bringen, wird mit Rätseln beantwortet, die ich nicht ausknobeln will."


"Ignorieren will ich sie aber auch nicht."


show ev rin_roof_nonchalant onlayer master
with charachange

rin "Na ja, aber der Grund ist, dass alle zu beschäftigt mit ihrem Leben sind, um auf die wirklich wichtigen Dinge zu achten."


hi "Wie den Himmel zu beobachten?"


show ev rin_roof_surprised onlayer master
with charachange

"Sie wendet ihren Blick vom Himmel ab und sieht mich endlich direkt an. Die durchdringende Tiefe ihrer Augen, wenn sie sie erst einmal auf etwas richtet, ist verblüffend."


rin "Weißt du, wenn du ein Mädchen wärst, könnte ich dein Höschen sehen."


hi "Wenn ich ein Mädchen wäre, dann würde ich gar nicht erst so nah an jemanden herangehen, der einen Blick auf meine Unterwäsche erhaschen will. So viel Verstand habe ich noch."


show ev rin_roof_boredom onlayer master
with charachange

rin "Würd ich auch nicht, aber manchmal lässt sich's nicht vermeiden. So wie jetzt zum Beispiel."


show ev rin_roof_nonchalant onlayer master
with charachange

rin "Um dir die Wahrheit zu sagen, will ich dir aber nicht mal wirklich aufs Höschen gucken."


rin "Unterhosen sind die Seele eines Mädchens. Du solltest nicht heimlich die Seele von jemand anderem angucken. Auch wenn du kein Mädchen bist."


hi "Ich glaube, als Junge kann ich das verstehen. Für uns sind sie so eine Art sagenumwobenes Objekt, das sich unserem Verständnis entzieht."


show ev rin_roof_surprised onlayer master
with charachange

rin "Ja, genau dafür halte ich sie auch. Was für ein Zufall."


hi "Und was für einer."


hi "Hattest du heute morgen Geschichte?"


show ev rin_roof_doubt onlayer master
with charachange

rin "Ich hab geschwänzt."


hi "Um das hier zu machen?"


show ev rin_roof_boredom onlayer master
with charachange

rin "Na ja, ich mache nicht wirklich, wonach es aussieht, dass ich es mache, oder zumindest glaube ich, dass das, was ich mache, nicht so aussieht, wie ich aussehe, aber von deiner Perspektive aus…"


extend "vermutlich…"


rin "Ja, ich habe für das hier geschwänzt."


hi "Welchen Grund du auch haben magst, er ist vermutlich genauso gut wie jeder andere."


hide hisao onlayer master
with charaexit

play sound sfx_rustling

scene bg school_roof onlayer master
with locationchange

"Meinen müden Beinen nachgebend setze ich mich neben Rin aufs Dach."


"Die Kiesel sind nicht gerade das bequemste Bett der Welt, aber wenn sie es aushält, dann sollte ich auch in der Lage dazu sein."


rin "Worauf wartest du?"


hi "Hmm?"


rin "Versuch's."


stop music fadeout 2.0
$ renpy.music.set_volume(0.4, 3.0, channel="ambient")

"Ich lege meinen Kopf in den Nacken, um zu sehen, was sie sieht."


scene bg misc_sky onlayer master at Fullpan(40.0)
with locationchange

"Der silbrig-blaue Himmel, gesprenkelt mit einer Herde Wolkenschafe, füllt mein gesamtes Blickfeld."


"Es ist zwar schön, aber der Anblick ist trotz des guten Wetters nichts besonderes."


"Ich zucke mit den Schultern und versuche dabei so gut ich kann, die gleichgültige Art zu imitieren, die Rin mittlerweile zur Vollkommenheit gebracht zu haben scheint, und lege mich auf den Rücken."


"Die Steine drücken bei der kleinsten Gewichtsverlagerung durch das dünne Hemd gegen meinen Rücken und zwingen mich, so ruhig wie möglich liegen zu bleiben."


"Ich versuche, das unangenehme Gefühl zu ignorieren und konzentriere mich stattdessen auf die unendliche Weite über uns."


"Weit oben treiben die Sommerwolken still über das Himmelsgewölbe."


"Keiner von uns hat mehr etwas zu sagen, daher legt sich Stille über das Dach."


"Der unterdrückte Lärm von Schülern beim Mittagessen, Zikaden in den Bäumen und Verkehr, der an der Schule vorbeibrummt, summen angenehm irgendwo im Hintergrund."


hi "Hör mal, ich hatte viel Spaß gestern."


rin "Hattest du?"


hi "Na ja, um ehrlich zu sein nicht. Aber es war in Ordnung. Es war wahrscheinlich die längste Zeit, die ich an derselben Stelle gesessen habe, ohne etwas zu tun. Beeindruckend irgendwie."


"Ich versuche, die Worte so überzeugend wie möglich klingen zu lassen."


rin "Ist das beeindruckend?"


hi "Ich finde schon. Ich bin normalerweise zu unruhig, um irgendetwas in der Art zu machen."


rin "Ich denke, ich hatte Spaß."


"Eine Wolke zieht über uns vorbei und wirft ihren Schatten auf die Schule."


"Ich bekomme von dem plötzlichen Wechsel von Sonne zu Schatten eine Gänsehaut."


"Ich merke, dass der Sommer noch nicht ganz seinen Höhepunkt erreicht hat."


"Das einzige Anzeichen dafür, dass Zeit verstreicht, ist die langsame Bewegung der Wolken, die in Richtung Dorf ziehen."


"Vereinzelte Strahlen goldenen Sonnenlichts fallen durch die Wolkenlücken und blenden mich jedes Mal für einen Moment, wenn sie mir direkt in die Augen scheinen."


"Das Blau des Himmels wirkt so unerreichbar."


"Das erinnert mich an meine Zeit im Krankenhaus, wo ich mich jeden Tag zu Tode gelangweilt habe."


"Irgendwie war es nach einer Weile nicht mehr von Bedeutung. Ich lernte, dass es noch andere Dinge gibt als immer nur fernzusehen und mit Leuten zu tratschen, die ich noch nicht einmal leiden konnte."


"Es ist ein durch und durch beruhigender Anblick, der auch auf meine anderen Sinne ausstrahlt, bis schließlich auch mein Gehirn einen zen-gleichen Zustand erreicht."


"Ein Flugzeug zieht vorbei und lässt auf seinem Weg zwei dünne Kondensstreifen zurück. Sie sehen aus, als habe jemand zwei Kreidelinien vom einen Ende des Himmels zum anderen gezogen."


"Wo es wohl hinfliegt?"


"Das tiefe Dröhnen seiner Triebwerke dringt bis hinunter an meine Ohren, obwohl es kaum hörbar ist über den Lärm des Schulhofs."


stop ambient fadeout 8.0
$ renpy.music.set_volume(1.0, 10.0, channel="ambient")

rin "Es ist schön."


hi "Es ist schön, aber ich verstehe nicht, warum es wichtiger ist, als zur Schule zu gehen."


rin "Ist es nicht gut, etwas zu tun, das man mag?"


rin "Von Zeit zu Zeit?"


hi "Natürlich, aber—"


stop sound

emi "Was macht ihr da?"


"Emi hat sich an uns herangeschlichen, ohne dass wir es gemerkt haben, und ist nur noch einen Schritt von mir entfernt. In ihren Armen hält sie mehrere mit Plastikfolie umwickelte Päckchen."


show emi excited_happy_close onlayer master:
    xalign 0.5 yanchor 1.0 ypos 1.2
    easein 0.5 center
show bg misc_sky onlayer master at right
with charaenter

"Sie lehnt sich nach vorne und schaut mich an. Dabei überschattet sie mein Gesicht fast genauso, wie ich zuvor Rin überschattet habe."


"Ich frage mich, wie komisch das aussieht, uns beide hier oben auf dem Rücken liegen zu sehen."


hi "Das habe ich auch sie gefragt."


rin "Ich würde mir mehr Gedanken darüber machen, was du tust. Wenn ich du wäre, würde ich nicht so nahe an Leute herankommen, die dein Höschen sehen können."


play sound sfx_pillow

show emi sad_angry_close onlayer master
with vpunch

play music music_comedy fadein 0.5

emi "Rin!"


show emi sad_angry_close onlayer master:
    easeout 0.5 ypos 1.2 alpha 0.0
with None

scene bg school_roof onlayer master
with locationchange

show emi basic_hes onlayer master:
    xalign 0.5 yanchor 1.0 ypos 1.1
    easein 0.5 center
with charaenter

"Emis Stimme klingt empört, aber sie tritt schnell ein paar Schritte zurück und presst so abrupt die Hände gegen die Vorderseite ihres Rocks, dass sie die Brotpäckchen fallen lässt, die sie im Arm hatte."


"Ich wende schnell meine Augen ab und werfe Rin einen wütenden Blick zu. Sie tut so, als würde sie mich nicht sehen."


show emi basic_shock onlayer master
with charachange

emi "So was würde Hisao nie machen, stimmt's?"


hi "Genau."


play sound sfx_rustling

show emi basic_shock onlayer master:
    parallel:
        ease 0.5 ypos 1.17
    parallel:
        "emi basic_annoyed" with Dissolve(0.5, alpha=True)
    ease 0.5 ypos 1.0
with Pause(1.0)

"Emi schaut Rin finster an, dann kniet sie sich hin, um die Boxen aufzuheben."


play ambient sfx_rooftop fadein 8.0

show emi basic_grin_close onlayer master
with characlose

show emi basic_grin_close onlayer master:
    ypos 1.12
with charamove

"Sie wischt den Staub von ihnen ab und schlüpft geschickt an mir vorbei auf Rins andere Seite, wo sie sich schließlich hinsetzt."


emi "Wie dem auch sei, hier sind eure Brote. Tut mir leid, dass es so lange gedauert hat."


hi "Schon okay. Danke für die Einladung."


"Ich setze mich auf und nehme Emis Brot dankbar entgegen."


"Mit Heißhunger machen wir uns daran, die simple Mahlzeit zu verzehren. Das Brot schmeckt überraschend gut und füllt meinen Magen problemlos."


show rin invis onlayer master:
    yanchor 1.0 ypos 1.2 xanchor 0.5 xpos 1.0
with None

show emi basic_grin_close onlayer master:
    xpos 0.3
show bg school_roof onlayer master at bgleft
show rin basic_awayabsent_close onlayer master:
    ease 1.0 ypos 1.07 xpos 0.9
with dissolvecharamove

"Aus dem Augenwinkel verfolge ich das Geschick, mit dem Rin ihr Brot zwischen den Füßen handhabt."


show emi excited_proud_close onlayer master
with charachange

emi "Ich hab dich die letzten paar Tage nicht mehr auf dem Sportplatz gesehen."


show rin basic_absent_close onlayer master:
    ypos 1.07 xpos 0.9
with charachange

hi "Oh. Genau, ich… dachte, es wäre ein zu schweres Programm für den Einstieg."


show rin basic_awayabsent_close onlayer master
show emi basic_hes_close onlayer master
with charachange

emi "Also hast du etwas anderes gemacht?"


show rin basic_absent_close onlayer master
with charachange

hi "Ich hab über meine Optionen nachgedacht."


show emi basic_annoyed_close onlayer master
with charachange

"Sie runzelt die Stirn, fragt aber nicht weiter nach – wofür ich ihr auch dankbar bin."


"Emi scheint ziemlich eigensinnig zu sein, und ich würde es wirklich gerne vermeiden, täglich von ihr deswegen belästigt zu werden. Ich habe schon genug mit Shizune und Misha zu tun."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

play sound sfx_warningbell
show rin basic_awayabsent_close onlayer master
show emi basic_shock_close onlayer master
with charachange

"Kaum sind wir mit dem Essen fertig, ruft uns die Klingel zurück in unsere Klassenzimmer."


stop ambient fadeout 0.5
$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_scienceroom onlayer master
with locationskip

show misha sign_smile onlayer master at center
with charaenter

mi "Hicchan!"


"Misha winkt mir zu, kaum dass ich den Raum betreten habe, und beginnt zu reden, noch bevor ich das Zimmer durchquert habe."


show misha hips_smile onlayer master
with charachange

mi "Wie war das Fest? Hattest du Spaß?"


hi "Äh… Da bin ich mir noch nicht so ganz sicher. Ich würde mal sagen, „vermutlich”."


hi "Wieso?"


show misha hips_grin onlayer master
with charachange

mi "Wahaha~, nur so, nur so!"


"Ihre Augen funkeln auf eine Art, die mir sagt, dass sie sicher nicht einfach so fragt. Ich kann ihre Motive aber noch nicht einmal erahnen."


hide misha onlayer master
with charaexit

"Da unsere Englischlehrerin just in diesem Moment den Raum betritt, können wir unsere Unterhaltung nicht fortsetzen, und Misha greift auf Plan B zurück."


window hide

show misha hips_grin_close onlayer master at offscreenleft
with None

show misha perky_smile_close onlayer master:
    xpos 0.1 xanchor 0.5
show bg school_scienceroom onlayer master at left
with charamove

$ written_note(u"Ich war den ganzen Tag mit Shicchan unterwegs. Wir hatten eine Menge Spaß!", text_args={"color":"#FF2AAA"})


$ written_note(u"Hättet ihr nicht arbeiten müssen?")


show misha hips_grin_close onlayer master
with charachange

$ written_note(u"Keine Sorge! Es lief alles richtig gut.", text_args={"color":"#FF2AAA"})


window show

"Ich antworte nicht darauf, und sie lässt mich in Ruhe, als Shizune ihre Aufmerksamkeit für sich beansprucht."


stop music fadeout 12.0

show misha invis onlayer master at offscreenleft
with dissolvecharamove

hide misha onlayer master
show bg school_scienceroom onlayer master:
    subpixel True yalign 0.0
    ease 30.0 zoom 1.1
with None

"Meine eigene Aufmerksamkeit jedoch ist nach draußen gerichtet."


"Jetzt, wo ich von hier drinnen durch das Fenster und das Blattwerk dahinter schaue, scheint der Himmel kleiner zu sein."


"Ich kann nur einen kleinen blauen Fleck erhaschen; alles andere ist verdeckt von dem Durcheinander in meinem Blickfeld."


"Welche „Erfahrung” hat sich Rin vom Betrachten des Himmels erhofft? Sicher hat sie es schon einmal gemacht. Alle haben das."


"Es hat keinen Sinn zu versuchen, ihre Gedanken zu erraten, aber wenn ich das nicht mache, habe ich keine Entschuldigung, mich nicht auf die Worte der Lehrerin zu konzentrieren."


"Ich starre auf die Kritzeleien, die auf der Tafel erscheinen, und versuche, ihren Sinn auszumachen – mit wenig Erfolg."


"Englisch ist wirklich nicht mein Lieblingsfach. Wir haben eine starke gegenseitige Abneigung."


stop music fadeout 2.0


label de_R2:

scene bg school_hallway3 onlayer master
with shorttimeskip

play music music_normal fadein 3.0
play sound sfx_normalbell

"Die drückende Wärme der Nachmittagssonne dringt in den Korridor und lässt die Luft zäh und schwer erscheinen."


"Mein Körper fühlt sich träge und schwer an, als ich mich zum Kunstraum zwei Türen weiter schleppe."


"Vermutlich ist das einer der Gründe, warum ich noch keinem Klub beigetreten bin. Nachmittage sind zum Arbeiten einfach nicht geeignet."


scene ev rin_artclass1 onlayer master
with locationchange

"Ich klopfe an die Tür des Kunstraums und öffne sie. Ein Mädchen, das mit ein paar wichtig aussehenden Papierrollen herumhantiert, dreht sich zu mir um und mustert mich neugierig. Schließlich lächelt sie mich mit leicht verwirrtem Blick an."


show ev rin_artclass2 onlayer master
with charachange

"Schülerin" "Hallo…?"


hi "Das hier ist doch der Kunstklub, richtig?"


"Schülerin" "Jepp. Lust beizutreten?"


hi "So in etwa. Kann auch sein, dass ich das bereits getan habe. Mal schauen."


show ev rin_artclass3 onlayer master
with charachange

"Wir lächeln einander kurz an. Sie wirkt nach wie vor verwirrt, aber irgendwie lässt dadurch meine Nervosität etwas nach."


"Schüler" "Super! Setz dich doch. Wir fangen an, sobald Herr Nomiya kommt."


show ev rin_artclass4 onlayer master
with charachange

"Ohne lange nach einem guten Platz Ausschau zu halten, gehe ich zügig zum hinteren Teil des Raumes und lasse mich auf einem freien Stuhl etwas abseits der anderen nieder."


"Ein paar der anderen Klubmitglieder räkeln sich auf ihren Stühlen, während wir auf den Lehrer warten. Rin sitzt allein am Fenster und schaut nach draußen."
"Abgesehen von einem Typen aus meiner Klasse, mit dem ich nie wirklich gut auskam, ist sie die einzige Person im Raum, die ich kenne."


"Keiner der anderen kommt, um mich zu begrüßen. Vielleicht kommt das erst später? Für den Moment begnüge ich mich mit der Rolle des stillen Beobachters."


"Einer der Jungen trägt eine Sonnenbrille. Normalerweise wäre das im Inneren eines Gebäudes ein merkwürdiger Anblick. Yamaku ist aber nicht normal. Wahrscheinlich ist er der blinde Schüler, von dem Rin gesprochen hat."


stop music fadeout 2.0
play sound sfx_footsteps_hard fadein 0.2

scene bg school_classroomart onlayer master at left
with locationchange

"Die Wartezeit erweist sich als äußerst kurz."


stop sound
play music music_happiness fadein 2.0

show nomiya smile onlayer master at center
with charaenter

"Mit drei langen Schritten läuft Nomiya zu seinem Schreibtisch, lächelt und setzt zu einer temperamentvollen Begrüßung an."


show nomiya veryhappy onlayer master
with charachange

no "Schönen Nachmittag, euch allen!"


show nomiya talk onlayer master
with charachange

no "Zunächst einmal das Wichtigste: Hisao dort drüben ist unser neuestes Mitglied. Ich hoffe, ihr werdet gut miteinander auskommen."


"Er zwinkert mir auf eine etwas verstörende Art zu."


"Alle acht Mitglieder des Klubs, mich eingerechnet, erwidern seinen Gruß, jedoch mit bedeutend weniger Enthusiasmus. Dennoch sitzen nun alle aufrecht und beginnen aufzupassen."


show nomiya smile onlayer master
with charachange

no "Ich glaube, einige von euch haben immer noch Projekte, an denen sie arbeiten müssen, also würde ich euch bitten, daran weiterzuarbeiten, wenn ihr wollt."


show nomiya talk onlayer master
with charachange

no "Was den Rest von euch angeht, habe ich mir gedacht, dass wir heute ein paar Portraitskizzen machen könnten."


show nomiya veryhappy onlayer master
with charachange

no "Was haltet ihr davon?"


"Außer leisem Gemurmel gibt niemand eine verständliche Antwort, was Nomiya anscheinend als einhellige Zustimmung interpretiert."


show nomiya talk onlayer master
with charachange

no "Also dann! Alle, die nicht an einem anderen Projekt arbeiten, suchen sich einen Partner und fertigen eine Skizze voneinander an."


no "Ihr solltet in der Lage sein, diese Übung heute noch abzuschließen. Wenn nicht, könnt ihr auch nächstes Mal weitermachen, oder es noch mal versuchen, wenn ihr die Aufgabe interessant fandet."


show nomiya veryhappy onlayer master
with charachange

no "Denkt daran, auf Licht und Schatten zu achten, und gebt euer Bestes!"


"Einen Partner suchen? Ich kenne so gut wie keinen hier! Plötzlich fühle ich mich ziemlich unbehaglich. Ich wünschte, einer der anderen würde mich fragen, ob wir uns zusammentun sollen."


hide nomiya onlayer master
with charaexit

"Die Anderen stehen auf und rücken ihre Stühle dichter zusammen, aber keiner von ihnen kommt zu mir."


"Bald haben alle einen Partner gefunden. Freunde tun sich zusammen, aber ich bleibe allein zurück."


"Alle außer Rin."


show bg school_classroomart onlayer master at right
with charamove

"Sie sitzt in der äußersten Ecke des Klassenzimmers und starrt noch immer aus dem Fenster, als würde sie Nomiyas Aufgabe überhaupt nicht interessieren."


"Da sie außer mir die Einzige ohne Partner ist, mache ich mich auf den Weg zu ihrem Platz."


"Ich kann ihr Gesicht nicht sehen, da ihr Haar das Meiste davon verdeckt und sie von mir weg sieht."


hi "Rin?"


"Keine Antwort."


hi "Hey, hast du Lust, mit mir zusammen zu arbeiten? Du bist die Einzige hier, die ich kenne…"


show rin basic_absent onlayer master at center
with charaenter

"Endlich scheint sie von meiner Anwesenheit Notiz genommen zu haben. Ihr Kopf dreht sich roboterhaft zu mir, als sie schaut, wer sie angesprochen hat."


"…"


"Rin antwortet nicht, und ich will die Frage auch nicht wiederholen. Ich bin mir sicher, dass sie mich schon beim ersten Mal verstanden hat."


"…"


"Warum antwortet sie nicht? Es kann doch kein so schreckliches Schicksal sein, mit mir zusammenarbeiten zu müssen, oder etwa doch?"


"Sie sieht mir nicht ins Gesicht und starrt stattdessen direkt auf meine Brust und meinen Bauch."


"…"


show rin basic_deadpan onlayer master
with charachange

rin "Oh, okay. Warum nicht?"


"…"


hi "Okay. Gut. Großartig! Ich hole schnell unsere Sachen."


hide rin onlayer master
with charaexit

show bg school_classroomart onlayer master at left
with charamove

"Es verwirrt mich, die Materialien auch nur anzuschauen, die Nomiya für die heutige Sitzung vorbereitet hat. Anstelle von Graphit oder Bleistiften sollen wir anscheinend Tuscheskizzen machen."


"Ich habe so was noch nie gemacht."


"Nomiya scheint jedoch Vertrauen in meine Lernfähigkeit zu haben."


show nomiya veryhappy onlayer master at center
with charaenter

no "Ganz einfach!"


show nomiya smile onlayer master
with charachange

no "Als erstes zeichnest du die Umrisse mit Tusche. Du lässt sie trocknen, und dann schattierst du mit verdünnter Tusche. Das nennt man Ausziehtusche. Es funktioniert genau wie mit Wasserfarben. "


show nomiya talk onlayer master
with charachange

no "Wenn du dich damit nicht wohlfühlst, dann nimm für die Konturen einen Stift anstelle des Pinsels."


hi "Alles klar."


hide nomiya onlayer master
with charaexit

"Ich nehme mir Papier, Wasserbehälter, einen Stift für mich, einen Pinsel für Rin und Tusche für uns beide und gehe zurück zu ihr."


show bg school_classroomart onlayer master at right
with charamove

show rin basic_absent_close onlayer master:
    center
    ypos 1.1
with charaenter

"Ich schnappe mir einen der nahestehenden Stühle und setze mich Rin direkt gegenüber."


show rin negative_spaciness_close onlayer master
with charachange

stop music fadeout 1.0

rin "Willst du, dass ich es mit dem Fuß oder mit dem Mund mache?"


hi "Was?"


play music music_another fadein 2.0

show rin relaxed_surprised_close onlayer master
with charachange

"Sie legt den Kopf zur Seite und sieht mich fragend an, als könne sie nicht verstehen, dass ich die Frage nicht verstanden habe."


show rin basic_deadpan_close onlayer master
with charachange

rin "Für mich ist beides okay. Du wirst aber besser aussehen, wenn ich es mit dem Fuß mache."


hi "Wenn es für dich keinen Unterschied macht, dann mit dem Fuß."


show rin basic_deadpannormal_close onlayer master at center
with dissolvecharamove

"Als Antwort bekomme ich nur ein Nicken, während Rin von ihrem Stuhl aufsteht und ihre Sandalen von den Füßen kickt."


show rin basic_awayabsent_close onlayer master:
    center
    ypos 1.17
with dissolvecharamove

"In zwei fließenden Bewegungen greift sie erst eines der Blätter und legt es vor sich auf den Boden. Dann klemmt sie sich den Pinsel zwischen die Zehen und setzt sich schließlich in einer merkwürdigen Position mit überkreuzten Beinen auf den Boden."


"Obwohl ich sie schon praktisch alles mit ihren Füßen habe machen sehen, ist diese Demonstration von Geschick so beeindruckend, dass ich sie wie gebannt anstarre."


show rin negative_annoyed_close onlayer master
with charachange

"Rin betrachtet konzentriert das leere Blatt, während die Spitze ihres Pinsels erwartungsvoll über dem Papier schwebt."


show rin basic_deadpancontemplation_close onlayer master
with charachange

"Als sie den Kopf hebt, um zu sehen, ob ich bereit bin, wende ich schnell den Blick ab."


show rin basic_deadpan_close onlayer master
with charachange

rin "Ich fange an. Such dir eine Pose aus."


hi "Was für eine Art von Pose?"


show rin basic_lucid_close onlayer master
with charachange

rin "Ganz egal. Darum geht's ja. Du musst die Zeichnung anhand des Eindrucks dessen machen, was du siehst, und nicht schon vorher entscheiden."


"Ich teste verschiedene Posen, aber im Endeffekt sitze ich einfach auf meinem Stuhl und lasse die Hände schlaff zwischen den Knien hängen."


show rin basic_deadpanupset_close onlayer master
with charachange

"Ich schaue sie an, und für einen Moment tut sie dasselbe, bevor sie schließlich beginnt."


"Rins Blick ist bohrend aber teilnahmslos, als ob sie versuchen würde, einen Teil von mir in sich aufzunehmen. Ich fühle mich, als würde ich unter dem Druck ihres Blicks zusammenschrumpfen."


"Ich bekomme das Gefühl, dass Rin mich zum ersten Mal seit wir uns kennen tatsächlich ansieht, anstatt nur in meine grobe Richtung zu schauen."


show rin negative_annoyed_close onlayer master
with charachange

"Sie malt mit selbstsicheren aber dennoch gewagten Schwüngen ihres feinen Pinsels, als wären ihr die zerstörerischen Konsequenzen eines versehentlich falsch gesetzten Striches egal."


show rin basic_absent_close onlayer master at center
with dissolvecharamove

"Als sie mit den Konturen zufrieden ist, streckt sie ihren Rücken und ihre Beine und steht auf, um für mich Modell zu stehen."


show rin basic_awayabsent_close onlayer master
with charachange

"Sie sieht mich dabei allerdings nicht an. Stattdessen lässt sie ihren Blick durch den Raum wandern, was mir die Sache ein wenig erleichtert. Es ist einfacher, jemanden anzustarren, wenn derjenige nicht zurück starrt."


"Dennoch fällt es mir schwer, etwas zu Papier zu bringen."


"Ich bin nicht gerade künstlerisch veranlagt, daher habe ich Angst, dass mein Portrait etwas entstellend werden könnte – insbesondere verglichen mit dem Können meiner Partnerin."


"Ich will mich nicht schon beim ersten Versuch zu sehr blamieren."


"Hinzu kommt noch, dass Rin bei der ganzen Sache nicht gerade hilfreich ist."


show rin negative_annoyed_close onlayer master
with charachange

"Sie hält keine zehn Sekunden still, legt ihren Kopf mal auf die eine, mal auf die andere Seite, um ihr Werk zu beurteilen, beißt sich unzufrieden auf die Unterlippe und verlagert ständig ihr Gewicht, als stünde sie auf glühenden Kohlen."


show rin basic_awayabsent_close onlayer master:
    center
    ypos 1.17
with dissolvecharamove

"Zu guter Letzt schaffe ich es schließlich auch, ein wenig Fortschritt mit meiner Zeichnung zu machen, und nachdem die Konturen endlich fertig sind, beginnen wir mit der Schattierung."


show rin basic_awayabsent_close onlayer master:
    tworight
    ypos 1.17
show bg school_classroomart onlayer master at center
with charamove

show nomiya smile behind rin onlayer master at twoleft
with charaenter

"Nach einer Weile kommt Nomiya vorbei und kommentiert die Anfänge unserer Skizzen."


show nomiya veryhappy onlayer master
with charachange

no "Sehr gut! Stehende Figuren sind für Anfänger einfacher zu verstehen."


hi "Aber ich habe mir die Pose nicht mal ausgesucht…"


hide nomiya onlayer master
with charaexit

"Verwirrt schaue ich erst ihn und dann Rin an, aber er ist schon auf dem Weg zur nächsten Gruppe, und Rin wirkt weiterhin teilnahmslos."


show rin basic_awayabsent_close onlayer master:
    center
    ypos 1.17
show bg school_classroomart onlayer master at right
with charamove

"Wie auch schon beim Malen des Mauerbildes ist Rin so sehr in ihre Arbeit vertieft, dass sie mich, das Klassenzimmer und alles andere außerhalb ihrer eigenen kleinen Welt ausgeblendet zu haben scheint."


"Von Zeit zu Zeit lehnt sie sich zurück – vermutlich um ihr Werk aus einer anderen Perspektive zu betrachten. Ab und an lehnt sie sich nach vorne und lehnt sich so weit nach unten, dass ihre Nase beinahe das Papier berührt."


"Dieses ständige vor und zurück wirkt extrem albern."


"Wie zum Beweis, dass sie noch nicht völlig in eine andere Welt abgedriftet ist, beginnt Rin plötzlich zu sprechen."


show rin negative_spaciness_close onlayer master
with charachange

rin "Hast du schon Spaß?"


"Sie hebt ihren Blick nicht von der Zeichnung, was gut ist. Das Brechen der Stille sendet einen Schock durch meinen Körper, als stünde ich plötzlich unter Strom."


hi " Ich… weiß noch nicht. Ist schwer zu sagen."


show rin basic_awayabsent_close onlayer master
with charachange

"Ich kann ihre Antwort nicht verstehen, da sie plötzlich eine geflüsterte Privatunterhaltung mit ihrem Bild zu haben scheint."


"Ich verstehe nicht, wie sie so gut zeichnen kann, obwohl sie die Aufmerksamkeitsspanne eines Schmetterlings hat."


"Da sie ihr Interesse verloren zu haben scheint, wende ich mich wieder der Arbeit an meinem eigenen Bild zu."


"Ich versuche, Rins Haaren etwas Textur zu verleihen. Ich will irgendwie einfangen, wie das goldene Sonnenlicht des Nachtmittags ihr rotes, zerzaustes Haar zu entflammen scheint, und es in Schwarz- und Grautönen wiedergeben."


"Dieser Stift und das Fläschchen Tinte scheinen mir lausige, inadäquate Werkzeuge für diese Aufgabe zu sein."


"Minuten vergehen, aber die Zeichnung sieht Rin noch kein bisschen ähnlicher als zuvor. Ihre Stimme reißt mich schließlich aus meiner Verzweiflung."


show rin basic_deadpannormal_close onlayer master
with charachange

rin "Und jetzt?"


hi "Wie bitte?"


show rin basic_deadpan_close onlayer master
with charachange

rin "Hast du schon Spaß?"


hi "Warum fragst du das immer wieder?"


show rin basic_deadpancontemplation_close onlayer master
with charachange

rin "Weil es ein Klub ist, oder? Klubs sollen Spaß machen. Du bist beigetreten, um Spaß zu haben. Hast du Spaß?"


hi "Ist es wichtig, dass ich Spaß habe?"


show rin basic_deadpanupset_close onlayer master
with charachange

rin "… Ja."


hi "… Okay, ich habe Spaß."


show rin basic_lucid_close onlayer master
with charachange

rin "Gut."


"Ich frage mich, ob ich das gesagt habe, um sie zufriedenzustellen oder weil es wirklich so ist. Ich bin mir wirklich nicht sicher."


"Schlecht finde ich das Ganze aber auch nicht. So viel kann ich schon mal ehrlich sagen. Fürs Erste reicht mir das."


stop music fadeout 2.0

scene bg school_classroomart onlayer master at right
with shorttimeskip

"Während die Zeit, die wir für die Übung bekommen haben, schnell verstreicht, versuche ich verzweifelt, meine grauenhafte Zeichnung zu verbessern, aber sie scheint kein bisschen besser zu werden."


"Ich will noch mal von vorne anfangen, aber was für einen Sinn hätte das? Dafür ist auch gar keine Zeit mehr."


play music music_daily fadein 2.0

no "Okay ihr Lieben, das war's für heute! Bitte legt die Zeichnungen auf meinen Schreibtisch. Ich sehe euch dann am nächsten Montag wieder!"


show ovl rinbyhisao onlayer master:
    center
    ypos 1.5 alpha 0.0
    easein 1.0 ypos 1.0 alpha 1.0
with Pause(1.0)

"Ich werfe einen flüchtigen Blick auf mein Portrait. Es sieht nicht gerade wie Rin aus. Man könnte wohl schon behaupten, dass es sie darstellt, aber damit wäre man noch großzügig."


"Die Nase und der Kiefer sehen grässlich aus, und die Schattierungen sind furchtbar. Zugegeben, es war mein erster Versuch, mit Tusche zu malen, aber es ist trotzdem ziemlich schlecht."


rin "Das ist nicht schlecht."


show rin basic_deadpanamused_close behind ovl onlayer master at center
with None

show ovl rinbyhisao onlayer master:
    easeout 1.0 ypos 1.5 alpha 0.0
with Pause(1.0)

hide ovl onlayer master
with None

"Sie hat sich von hinten an mich angeschlichen, während ich in Gedanken versunken war."


hi "Verdammt. Ich hatte gehofft, ich könnte das Portrait zum Lehrer schmuggeln, ohne dass du es siehst."


show rin basic_surprised_close onlayer master
with charachange

rin " Warum?"


hi "Ich bin nicht wirklich zufrieden damit. Ich wünschte, ich könnte besser zeichnen."


show rin basic_deadpannormal_close onlayer master
with charachange

rin "Du brauchst nur etwas Übung. Könntest du meine Zeichnung auch nach vorne bringen?"


"Selbst neugierig geworden, wie die Zeichnung geworden ist, werfe ich einen Blick auf das Bild. Ausgehend davon, wie Rin beim Zeichnen aussah, war sie wirklich voll bei der Sache."


show ovl hisaobyrin onlayer master:
    center
    ypos 1.5 alpha 0.0
    easein 1.0 ypos 1.0 alpha 1.0
with Pause(1.0)

"Es ist fantastisch. Die scheinbar willkürlichen Striche formen irgendwie ein Abbild meines Gesichts, von der Form meines Kinns bis zu meinem zerwühlten Haar und dem etwas düsteren Gesichtsausdruck."


label de_choiceR2:
menu:
    with menueffect
    "Ihr Bild ist umwerfend."
    "Du bist fantastisch!":




        return m1
    "Ich wünschte, ich wäre so gut wie du.":


        return m2

label de_R2a:

hi "Wow, du bist fantastisch."


rin "So fantastisch ist es nicht."


rin "Aber danke."


label de_R2b:

hi "Wow, ich wünschte, ich wäre so gut wie du. Ich schäme mich schon fast."


rin "Müsstest du nicht ich sein, um so gut zu sein wie ich? Ich glaube nicht, dass du ich sein willst."


hi "Nein, ich denke nicht. Aber vielleicht irgendwas in die Richtung."


label de_R2c:

show ovl hisaobyrin onlayer master:
    yalign 0.0 subpixel True
    easein 20.0 zoom 1.1
with None

"Ich schaue mir ihr Werk noch einmal genauer an. Die langsam trocknende Tinte glänzt noch."


hi "Ich sehe ziemlich grimmig aus."


rin "Ja, du siehst ziemlich grimmig aus. Ich meine, du hast Recht; aber ansonsten stimmt es auch. Also der Hisao hier, nicht der, den ich gemacht hab."


hi "Tue ich das?"


rin "Find ich zumindest."


"Ihre einfache Aussage bringt mich plötzlich schwer in Verlegenheit. Ich fühle mich, als bräuchte ich sofort einen Spiegel, um Rin entweder zu bestätigen oder zu widerlegen. Es ist ein unangenehmes Gefühl."


"Vielleicht bildet sie sich das aber auch nur ein. Ich hoffe, dass sie es sich bloß einbildet und dass ich nicht für jeden so aussehe wie auf dem Bild."


"Es ist ein gutes Bild, aber irgendwie hat es eine wirklich bedrückende Wirkung auf mich."


show rin basic_absent_close onlayer master
with None

show ovl hisaobyrin onlayer master:
    easeout 1.0 ypos 1.5 alpha 0.0
with Pause(1.0)

hide ovl onlayer master
with None

hi "Verstehe. Wie dem auch sei, es sieht wirklich gut aus. Du bist wirklich erstaunlich."


show rin basic_deadpandelight_close onlayer master
with charachange

rin "Danke. Es freut mich, dass ich dich malen konnte. Du bist eine interessante Person."


hi "Du bist auch interessant, aber das hat mir nicht viel geholfen."


"Meine Selbstachtung existiert heute praktisch nicht, aber Rin ignoriert das alles. Ich wusste, dass ich nie an sie heranreichen würde, aber den Unterschied noch einmal so vor Augen geführt zu bekommen, ist ziemlich demütigend."


show rin basic_awayabsent_close onlayer master
with charachange

rin "Weißt du, ich hab versucht, dich so aussehen zu lassen, als ob du viel nachdenkst, weil du viel am Nachdenken bist."


show rin basic_deadpanamused_close onlayer master
with charachange

rin "Und ja, ich hab die mit-dem-Leben-fertig Pose wohl etwas übertrieben, aber so sind Zyniker nun mal, oder?"


"Ich will eine schlagfertige Antwort geben, aber Nomiya lässt mir keine Zeit zum Nachdenken, indem er uns in Richtung Tür scheucht."


show rin basic_deadpanamused_close onlayer master at tworight
show bg school_classroomart onlayer master at center
with charamove

show nomiya talk behind rin onlayer master at twoleft
with charaenter

no "Beeilt euch, ihr Zwei!"


"Während wir am Plaudern waren, hat sich der Rest des Klubs verabschiedet."


hide rin onlayer master
with charaexit

"Ich schnappe mir schnell unsere Zeichnungen und bringe sie zu Nomiyas Schreibtisch. Dann eile ich hinter Rin her, die das Zimmer bereits verlassen hat."


stop music fadeout 4.0


label de_R3:

scene bg school_hallway3 onlayer master
with locationchange

"Zu meiner Überraschung ist sie nicht im Gang. Ich frage mich, wohin sie in den paar Sekunden verschwunden ist. Wäre nett gewesen, noch etwas zu plaudern."


"Nicht dass ich viel zu sagen gehabt hätte – außer, dass ich ihr noch das mit dem Zyniker hätte heimzahlen können."


"Es ist überraschend spät. Ich bin bereits daran gewöhnt, dass der Unterricht jeden Tag zur selben Zeit endet; daher macht sich die zusätzliche Stunde bemerkbar. Vor allem in meinem Bauch."


"Mein knurrender Magen erinnert mich daran, wie ausgehungert ich bin. Ich bin so hungrig, dass ich alles probieren würde, was man uns in der Cafeteria als essbar auftischt. "


scene bg school_cafeteria onlayer master
with locationskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0

"Selbst beim Anblick der heutigen Delikatesse – geheimnisvolle, frittierte Klumpen – gerät meine eiserne Entschlossenheit nicht ins Wanken. Ich schlinge die Mahlzeit herunter, ohne überhaupt etwas zu schmecken – was vermutlich auch besser so ist."


"Ich habe nicht viele Hausaufgaben, aber das Bisschen, das ich habe, wird sich nicht von allein erledigen, also mache ich mich auf den Weg zurück zum Wohnheim."


stop ambient fadeout 0.5
scene bg school_dormhallway onlayer master
with locationskip

$ renpy.music.set_volume(0.0, 2.0, channel="ambient")
play sound sfx_doorknock2

"Bereit für etwas Ablenkung nach den Hausaufgaben, klopfe ich an Kenjis Tür."


"Er antwortet von der anderen Seite, aber ich verstehe nichts von dem, was er gesagt hat. Ich versuche, die Tür zu öffnen, aber sie ist abgeschlossen."


show kenji neutral onlayer master at Slide(0.2,0.5,0.3,0.5,1.0)
with charaenter

"Nach mehreren Sekunden höre ich das Klicken der Schlösser, und die Tür öffnet sich."


hi "Hi. Hey, könnte ich mir ein Buch von dir ausleihen? Die Bibliothek hatte schon geschlossen, als ich mit meinem Klub fertig war."


show kenji tsun onlayer master
with charachange

"Er kneift die Augen noch stärker zusammen als sonst, und seine Augenbrauen beginnen nervös zu zucken."


play music music_kenji fadein 2.0

ke "Klub? Das ist gefährlich, Mann. Indoktrination, Gruppendenken, Gehirnwäsche, such dir was aus."


ke "Oberschul-Klubs sähen die Saat der Verschwörung. Hast du eine Ahnung, wie viele Geheimbünde aus Oberschul-Klubs hervorgegangen sind?"


ke "Pass auf, was du machst, und wage dich nicht zu weit vor, sonst kommst du vielleicht nicht wieder zurück."


hi "Okay, Kenji. Also, was ist jetzt mit dem Buch?"


show kenji neutral onlayer master
with charachange

ke "Äh, klar, aber gib sie wieder zurück, und pass auf, dass du keins meiner Bücher beschädigst. Keine Getränke, keine Essensflecken, keine Körperflüssigkeiten, capisce?"


hi "Sicher. Danke."


show kenji invis onlayer master:
    xpos 0.2
with dissolvecharamove

"Anstatt mich hereinzulassen, tritt er von der Tür zurück und schließt sie wieder."


show kenji neutral onlayer master at Slide(0.2,0.5,0.3,0.5,1.0)
with charachange

"Nach ein paar Sekunden kehrt er mit drei dicken Büchern zurück und gibt sie mir."


"Beim Aufschlagen des Obersten begrüßt mich ein vertrautes Emblem, das auf die Indexseite gestempelt wurde."


hi "Ähm, deine Bücher? Die sind aus der Schulbibliothek."


show kenji happy onlayer master
with charachange

ke "Jetzt sind es meine."


hi "Du hast sie gestohlen?"


show kenji tsun onlayer master
with charachange

ke "Was redest du da, Mann? Ich habe sie aus der Unterjochung durch die Feministen-Bewegung befreit, die die Bibliothek kontrolliert."


hi "Sag jetzt bitte nicht „Unterjochung durch die Feministen-Bewegung” bezieht sich auf die arme Bibliothekarin Yuuko. Sie könnte nicht einmal ein nasses Handtuch unterdrücken."


show kenji invis onlayer master:
    xpos 0.2
with dissolvecharamove

hide kenji onlayer master
with None

stop music fadeout 3.0

"Kenji wendet sich ab und murmelt etwas, das ich nicht verstehe, bevor er die Tür hinter sich schließt."


scene bg school_dormbathroom onlayer master
with locationchange

play ambient sfx_shower fadein 1.0

"Bevor ich in mein eigenes Zimmer zurückkehre, gehe ich ins Bad. Während ich meine Hände wasche, fällt mir mein Abbild in der Reflektion des Spiegels über dem Waschbecken ins Auge."


$ ksgallery_unlock("ev hisao_mirror_800")
scene ev hisao_mirror onlayer master:
    zoom 1.0 xalign 0.5 yalign 0.5 subpixel True
    ease 20.0 zoom 0.8
with locationchange

"Ich versuche, die Grimmigkeit zu finden, die Rin in mir gesehen hat, aber im Spiegel sehe ich nur mein normales Ich, das auf mich zurück starrt."


"Ich versuche mir einzureden, dass ich immer so ausgesehen habe, aber ich merke, dass ich mich nicht daran erinnern kann, wie ich vor einem halben Jahr ausgesehen habe."


stop ambient fadeout 6.0

$ suppress_window_after_timeskip = True

scene black onlayer master
with Dissolve(2.0)


label de_R4:

window hide None

scene black onlayer master with dissolve

scene bg school_dormhisao onlayer master
with openeye

window show

"Ich wache schweißgebadet auf, als wäre ich im Schlaf einen Halbmarathon gelaufen."


play music music_pearly fadein 5.0

"Seltsam… Ich kann mich nicht erinnern, schlecht geschlafen zu haben. Ein kleiner Anflug von Sorge durchzuckt mich; es ist beunruhigend, dass mein Herz nun schon im Schlaf Probleme macht, sodass ich es nicht einmal mitbekomme."


"Abgesehen von der merkwürdigen Erschöpfung nach dem Aufwachen fühle ich mich aber völlig in Ordnung."


"Mein Mund ist immer noch völlig ausgetrocknet, und ich habe nichts zu trinken. Mir bleibt also nichts anderes übrig, als meine Medikamente im Bad zu nehmen. Aus einer Laune heraus beschließe ich, bei der Gelegenheit auch gleich zu duschen."


scene bg school_dormbathroom onlayer master
show steam onlayer master
with locationskip

play ambient sfx_shower fadein 1.0

"Während ich unter der Dusche stehe, beschließe ich, dass das als Frühsport durchgeht, wenn ich noch einen schönen halbstündigen Spaziergang nach der Schule drauflege."


"Natürlich will ich keine Komplikationen riskieren, indem ich jetzt laufen gehe. Davon abgesehen wird Emi nichts davon erfahren, und ich glaube, sie hat mich sowieso schon so gut wie abgeschrieben."


"Spazieren wäre generell gut. Allein schon, um die Umgebung etwas kennenzulernen."


"Auf den Hügeln hinter der Schule ist ein großer Wald… oder ich könnte hinunter in den Mini-Mark gehen."


hide steam onlayer master
with charaexit
stop ambient fadeout 1.0

"Während ich mir noch die Feuchtigkeit von der Haut reibe, mache ich mich auf die Suche nach meiner Uniform."


"Ich knöpfe mir schnell das Hemd zu und streife mir meine Hose über, bevor ich nach draußen gehe."


scene bg school_courtyard onlayer master
with locationskip

"Normalerweise würde ich um diese Jahreszeit ungeduldig auf die Sommerferien warten. Nach nur etwas mehr als einer Woche an der Schule bleibt dieses Gefühl jedoch aus."


"Ich bin immer noch dabei, mich an das Schulleben und die abrupte, unangenehme Wendung zu gewöhnen, die mein Leben genommen hat. Ich hatte noch nicht die Zeit, mich mit dem Thema zu beschäftigen."


"Außerdem wird es eine nette Überraschung für mich, wenn die Ferien anfangen, ohne dass ich es erwarte. Insbesondere weil bald die Trimester-Abschlussprüfungen beginnen."


"Immerhin muss ich nichts aufholen. Meine Gewissenhaftigkeit macht sich endlich bezahlt."


"Ich schiebe mich an den Jungs vorbei, die in der Tür stehen, und lasse mich auf meinen Platz fallen."


stop music fadeout 2.0

scene bg school_scienceroom onlayer master
with locationskip

"Aus dem Augenwinkel kann ich sehen, wie Shizune und Misha ihre gezwungenermaßen bewegte Unterhaltung unterbrechen und sich beinahe gleichzeitig in meine Richtung drehen."


"Sie wollen offensichtlich etwas von mir; das erkenne ich daran, wie Shizune lächelt. Es ist zu aufdringlich fröhlich, um ehrlich zu wirken, und zu berechnend, um spontan sein."


show shizu behind_smile onlayer master at tworight
show misha perky_smile onlayer master at twoleft
with charaenter

play music music_normal fadein 2.0

mi "Guten Morgen~!"


"Ihre Begrüßung besteht zu einhundert Prozent aus Energie und Fröhlichkeit."


hi "Morgen."


"Es gelingt mir nicht, auch nur eines von beidem in meine Antwort zu legen."


show misha perky_confused onlayer master
with charachange

mi "Du siehst nicht gerade munter aus."


hi "Kein Wunder. Ich fühle mich auch nicht gerade munter. Ich glaube, ich hab schlecht geschlafen, aber ich weiß nicht, ob es daran liegt."


show misha hips_grin_close onlayer master
with vpunch

"Sie schlägt mir auf den Rücken und grinst."


show misha hips_smile_close onlayer master
with charachange

mi "Kopf hoch! Heute ist ein fantastischer Tag~!"


show shizu basic_normal2 onlayer master
with charachange

"Ich schaue weiter zu Shizune. Sie hat einen merkwürdig konzentrierten Gesichtsausdruck, aber als sich unsere Blicke kreuzen, runzelt sie leicht die Stirn und sieht weg."


show shizu adjust_happy onlayer master
with charachange

"Für einen Moment denke ich, dass Shizune meine Sorgen irgendwie erahnt hat und nun über eine Antwort nachgrübelt. Dann aber rückt sie ihre Brille zurecht und mit ihr auch ihre Gesichtszüge."


show shizu basic_happy onlayer master
with charachange

shi "…"


show misha sign_smile_close onlayer master
with charachange

mi "Na ja, jedenfalls haben wir uns gefragt, ob du noch Interesse an der Stelle im Schülerrat hast, weil wir dir nämlich ein Angebot machen werden, das du nicht ablehnen kannst~."


hi "Moment, was? Ihr dreht mir die Worte im Mund um. Ich habe nie behauptet, dass ich interessiert wäre."


show shizu adjust_smug onlayer master
with charachange

shi "…"


mi "Vielleicht nicht direkt, aber wäre es nicht schön, jeden Tag mit uns zu verbringen und dabei gleichzeitig noch der Schule zu helfen?"


hi "Also, um ehrlich zu sein, bin ich… Ich bin mehr oder weniger schon in einem Klub. Es wäre also ziemlich schwierig für mich, jetzt auch noch dem Schülerrat beizutreten."


hi "Selbst wenn ich wollte, was ich wie gesagt nicht tue."


show shizu behind_blank onlayer master
with charachange

shi "…"


show misha cross_smile_close onlayer master
with charachange

mi "Ach ja? Welcher Klub ist es denn, Hicchan~?"


hi "Der Kunstklub."


show shizu cross_angry onlayer master
with charachange

shi "…"


"Shizunes Augen schimmern düster, während sie mich anstarrt."
"So wie sie gerade aussieht, würde es mich nicht wundern, wenn der Kunstclub noch vor der Mittagspause sein Budget gestrichen bekäme, oder Nomiya auf mysteriöse Weise verschwinden würde."


hide shizu onlayer master
hide misha onlayer master
with charaexit

"Bevor sie etwas dazu sagen kann, betritt endlich der Lehrer das Klassenzimmer und schafft mir damit die beiden vom Hals. Die anderen beginnen in ihren Rucksäcken nach Büchern und Stiften zu wühlen."


"Ich bin dem Kunstclub beigetreten, aber das erste Treffen hat mein Selbstbewusstsein nicht gerade gesteigert. Ich bin mir nicht ganz sicher, wofür ich das mache."


"Ich wünschte, ich könnte so gut malen wie Rin. Allerdings weiß ich auch nicht, was ich tun würde, wenn ich es könnte. Wofür würde ich dieses Talent nutzen? Ich weiß es wirklich nicht."


$ renpy.music.set_volume(0.5,  1.0, channel="music")

show ev hisaobird_0 onlayer master:
    center
    alpha 0.0 ypos 1.5
    easein 0.5 alpha 1.0 ypos 1.0
with Pause(0.5)

"Ich ignoriere die einschläfernde Stimme des Lehrers, schlage eine leere Seite in meinem Buch auf und setze das gespitzte Graphit des Bleistifts an."


"Was soll ich zeichnen?"


"Mir fällt nichts wirklich Gutes ein."


show ev hisaobird_1 onlayer master:
    center
    alpha 1.0
with charachange

"Ich zögere und setze ab. Der zurückgebliebene schwarze Fleck auf der zuvor leeren Seite stört mich irgendwie."


"Ich scheine noch nicht einmal bis zur Startlinie zu kommen – vom eigentlichen Start ganz zu schweigen. Es fühlt sich beinahe so an, als würde mich eine unsichtbare Kraft zurückhalten."
"Zu allem Überfluss erinnert mich dieses Gefühl an meinen gescheiterten Versuch, mit Emi zu joggen."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

show ev hisaobird_1 onlayer master:
    center
    easeout 0.5 alpha 0.0 ypos 1.5
show bg school_scienceroom onlayer master:
    yalign 0.0
    ease 20.0 zoom 1.1
with Pause(0.5)

hide ev onlayer master
with None

"Ich schaue verzweifelt aus dem Fenster. Genau in diesem Moment hebt ein Vogel von einem der Kirschbäume ab, die überall auf dem Schulgelände wachsen."


"Ich kann ihn nicht wirklich genau erkennen, und es ist auch nicht so, dass ich die winzigen Vögel voneinander unterscheiden könnte, aber ich wähle ihn trotzdem als Motiv."


$ renpy.music.set_volume(0.5,  1.0, channel="music")

show ev hisaobird_1 onlayer master:
    center
    alpha 0.0 ypos 1.5
    easein 0.5 alpha 1.0 ypos 1.0
with Pause(0.5)

show ev hisaobird_2 onlayer master:
    center
    alpha 1.0
with charachange

"Mit dem Bild des Vogels vor meinem inneren Auge, wende ich mich wieder dem Notizbuch zu und ziehe zum Start bewusst eine dicke Linie über das Blatt."


"Sie scheint sich über mich lustig zu machen, da ich nicht direkt weiterzeichnen kann. Aber es ist ein Anfang. Einen Anfang zu haben, ist gut."


show ev hisaobird_3 onlayer master
with charachange

"Langsam zeichne ich das Bild auf die Seite meines Notizbuches. Das Bild in meinem Kopf wird dabei immer klarer, je mehr die Zeichnung Gestalt annimmt."


show ev hisaobird_4 onlayer master
with charachange

"Es ist wirklich nichts, nur ein namenloser Vogel auf dem Papier, aber darauf kommt es nicht an."



show ev hisaobird_5 onlayer master
with charachange

"Während ich meine Bemühungen fortsetze, verschwindet mein anfängliches Zögern zusammen mit der Stimme des Lehrers in den Hintergrund."
"In meinem Kopf formen die Federn ein einfaches Muster, aber auf dem Papier sind sie trotz meiner Bemühungen nur ein Gewirr aus zu vielen groben Linien."


show ev hisaobird_6 onlayer master
with charachange

"Ich merke, dass ich nicht wirklich weiß, wie die Flügel eines Vogels aussehen sollten, selbst wenn ich versuche, darüber nachzudenken."
"Ich lege sogar den Bleistift hin, schließe für einen Moment die Augen und versuche, in meinen Gedanken die Form eines Flügels nachzuzeichnen."


show ev hisaobird_7 onlayer master
with charachange

"Plötzlich so ernst an die Sache heranzugehen, frustriert mich ein wenig."


show ev hisaobird_8 onlayer master
with charachange

"Der Kunstunterricht in der Mittelschule war die „einfache” Stunde zwischen den anstrengenden Fächern wie Mathe oder Japanisch. Kunst hat aber auch noch eine andere Seite, die man erst sieht, wenn man nicht nur herumalbert."


show ev hisaobird_9 onlayer master
with charachange

"Es ist beinahe etwas vollkommen anderes."


stop music fadeout 0.5

mi "Hicchan?"


show bg school_scienceroom behind ev onlayer master:
    center
    zoom 1.0
show shizu behind_blank_close behind ev onlayer master at closeright
show misha cross_smile_close behind ev onlayer master at closeleft
with None

show ev hisaobird_9 onlayer master:
    center
    easeout 0.5 alpha 0.0 ypos 1.5
with Pause(0.5)

hide ev onlayer master
with None

"Ich blicke auf und sehe, wie die beiden Mädchen mich anstarren."


$ renpy.music.set_volume(1.0,  0.0, channel="music")
play music music_comedy fadein 1.0

"Misha und Shizune haben ihre Stühle zu meinem Tisch getragen und stehen jetzt an meiner Seite und betrachten meine Zeichnung."


hi "Wie lange steht ihr beiden schon hier?"


show misha hips_grin_close onlayer master
with charachange

mi "Ich glaube, du brauchst mehr Übung."


show shizu basic_normal_close onlayer master
with charachange

"Shizune zeichnet ein paar scharfe Gesten in die Luft zwischen sich und Misha."


show misha sign_smile_close onlayer master
with charachange

mi "Shicchan sieht das auch so."


"Rin hat gestern genau dasselbe gesagt, aber warum klang es bei ihr weniger herablassend?"


hi "Ihr solltet nicht Urteilen, bevor ich fertig bin."


hi "Davon abgesehen, wisst ihr nicht, dass es Pech bringt, ein unfertiges Werk anzuschauen?"


show misha cross_laugh_close onlayer master
with charachange

"Misha bricht in unbändiges Gelächter aus."


show misha hips_grin_close onlayer master
with charachange

mi "Was? Sei nicht albern~! Das kann doch gar nicht sein."


hi "Meinetwegen."


show shizu adjust_frown_close onlayer master
with charachange

"Shizunes Augenbrauen ziehen sich gefährlich zusammen, und die Bewegungen ihrer Hände werden ruckartig, als würde sie ein Messer schwingen."


show shizu behind_frown_close onlayer master
with charachange

shi "…"


show misha hips_frown_close onlayer master
with charachange

mi "Du solltest lernen, konstruktive Kritik besser zu vertragen."


hi "Das würde ich, wenn ihr mir welche geben würdet."


"Ich weiß, dass ich zu defensiv werde und dass Shizune das ausnutzt, aber ich kann nichts dagegen machen."


hi "Was macht ihr Zwei überhaupt hier?"


show shizu basic_frown_close onlayer master
with charachange

shi "…"


"Misha wedelt mahnend mit dem Finger vor meiner Nase."


show misha sign_smile_close onlayer master
with charachange

mi "Tss, Tss, Hicchan. Hast du dem Lehrer überhaupt nicht zugehört?"


show shizu behind_blank_close onlayer master
with charachange

shi "…"


show misha hips_smile_close onlayer master
with charachange

mi "Wir haben jetzt Gruppenarbeit."


"Ich nicke niedergeschlagen und überlasse es den beiden, die Führung zu übernehmen."


show misha hips_grin_close onlayer master
with charachange

mi "Also, was hältst du von der Stunde heute?"


hi "Nicht viel… Ich habe kein bisschen zugehört."


show misha hips_frown_close onlayer master
with charachange

"Misha schlägt sich mit der Hand gegen die Stirn und schüttelt theatralisch den Kopf."


mi "Was sollen wir nur mit dir machen, Hicchan?"


"Zum Glück sind Shizune und Misha zusammen effektiver als drei oder vier normale Menschen, daher kann ich mich für den Großteil der Aufgaben zurücklehnen."


"Ich versuche mein Bestes, wenigstens ein bisschen beizutragen, aber letzten Endes bin ich die meiste Zeit nutzlos."


stop music fadeout 2.0

scene bg school_scienceroom onlayer master
with shorttimeskip

play sound sfx_normalbell

"Der Lehrer behält uns bis fünf Minuten, nachdem es zur Mittagspause geklingelt hat, im Klassenzimmer, lässt uns aber schließlich doch gehen."


"Ich stopfe meine Bücher schnell in meine Tasche, während Misha und Shizune ihre Stühle zurück an ihre eigenen Plätze tragen."


"Die fehlgeschlagene Vogelzeichnung endet zusammengeknüllt in meiner Hosentasche, während ich nach draußen eile."


stop music fadeout 2.0

scene black onlayer master
with dissolve


label de_R5:

scene black onlayer master
with locationchange

"Nach dieser Stunde – und den gesamten Rest der Woche – laufe ich immer wieder Rin über den Weg."


window hide

scene bg school_hallway3 onlayer master
show crowd onlayer master
show rin basic_absent onlayer master at center
with delayblinds

play ambient sfx_crowd_indoors fadein 2.0

window show

rin "Hallo."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve

play music music_daily fadein 2.0

n "\n\nDas an sich ist auch nicht weiter überraschend. Unsere Klassenzimmer liegen direkt nebeneinander. Aber anders als normale Leute laufen wir nicht aneinander vorbei, sondern halten für einen Augenblick inne, wenn wir uns treffen."


n "Jedes Mal reden wir ein wenig, oder verbringen einfach nur stillschweigend etwas Zeit miteinander."


n "Ich glaube, ich gewöhne mich langsam daran, in Rins Gegenwart zu schweigen. Die Stille erscheint mir nicht mehr so unangenehm. Wie sie bin ich von Natur aus eher introvertiert, daher passen wir ganz gut zusammen."


n "Ich glaube, dass es für jemanden an dieser Schule eher ungewöhnlich ist, so still zu sein. Die meisten Leute hier scheinen gerne neue Kontakte zu knüpfen."


n "\nDas ist etwas, dass mir bereits aufgefallen ist, obwohl ich noch nicht sehr lange hier bin: Die Menschen hier reden viel, und sie reden die ganze Zeit."


nvl clear

n "\n\nEs kommt selten vor, dass ich jemanden sehe, der einfach nur gedankenverloren herumsitzt oder sonstwas treibt. Klar gibt es solche Leute hier auch; diese Hanako und mich, um nur zwei Beispiele aus meiner eigenen Klasse zu nennen. Im Großen und Ganzen sind sie aber eine Minderheit."


n "Wie dem auch sei, ich würde es nicht gerade „normal” nennen, wie Rin und ich die Zeit miteinander verbringen; aber es ist immerhin etwas."


n "Dabei stört mich die Art unserer Treffen eigentlich gar nicht; nur die Tatsache, dass sie überhaupt vorkommen verwirrt mich."


n "Ich würde nicht behaupten, dass wir uns zueinander hingezogen fühlen, aber so benehmen wir uns jedenfalls."


n "\n\nDieses Gefühl aufkeimender Freundschaft wird allerdings jedes Mal wieder komplett zerstört, sobald Rin ihren Mund öffnet."


nvl hide dissolve
nvl clear
window show

stop music fadeout 0.5
stop ambient fadeout 0.5

show rin basic_deadpannormal_close onlayer master
with characlose

rin "Kann ich mir deinen Herzschlag anhören?"


play music music_rin fadein 0.5
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 4.0

"Sie gibt das oder ähnlich irres Zeug von sich, und ich darf schauen, wie ich mit dem Unsinn klarkomme, den ihr Kopf im Verlauf der letzen Stunde ausgebrütet hat, weil sie der Unterricht nicht interessiert."


"Es scheint, als habe Rin Gefallen an meiner Krankheit gefunden, was wohl mit ihrem Interesse an ungewöhnlichen Behinderungen und den damit einhergehenden Konsequenzen zusammenhängt."


"Da ich, verwirrt wie ich bin, eine Sekunde zu lange vor ihr stehen bleibe, folgert sie, dass es wohl nötig ist, ihre Bitte weiter zu erläutern."


show rin basic_deadpan_close onlayer master
with charachange

rin "Ich weiß, dass ich kann, aber ich meine, lässt du mich auch?"


hi "Warum?"


show rin relaxed_doubt_close onlayer master
with charachange

rin "Brauche ich einen Grund? Ich bin meistens ziemlich schlecht mit Gründen."


hi "Nicht unbedingt, aber wenn du es machen willst, dann hast du ja vermutlich auch einen Grund."


show rin basic_deadpanamused_close onlayer master
with charachange

rin "Das ist ziemlich clever. Du bist schlauer als du aussiehst."


hi "Davon abgesehen wäre es mir lieber, wenn du das nicht tätest. Ich finde, solche Sachen sollten privat bleiben."


show rin basic_deadpandelight_close onlayer master
with charachange

rin "Privat. Verstehe."


hi "Ich kann dir aber etwas erzählen, wenn es dich interessiert. Ich bin sicher, dass es das tut. Mein Herzschlag klingt ziemlich komisch. Wegen der… du weißt schon, meinem Zustand."


hi "Und ich höre es. Die ganze Zeit."


show rin negative_spaciness_close onlayer master
with charachange

rin "Also bist du paranoid."


"Es ist keine Frage, sondern eine Feststellung."


hi "Nein, ich bin nicht paranoid. Die Ärzte meinten, dass ein übermäßiger Fokus auf den eigenen Herzschlag ein häufiges Symptom ist für meinen… Zustand."


show rin basic_deadpannormal_close onlayer master
with charachange

rin "Also ist es für dich normal, paranoid zu sein."


"Auch das ist keine Frage."


hi "Man könnte auch sagen, dass es schon nicht normal für mich ist, überhaupt so zu sein, aber was soll's."


hi "Paranoia passt gut zu mir."


show rin basic_lucid_close onlayer master
with charachange

rin "Ich glaube nicht, dass das etwas ist, was wirklich zu irgendjemandem oder irgendetwas passen kann."


show rin basic_deadpan_close onlayer master
with charachange

rin "Weißt du, ich hab heute eine Orange gegessen – zum Frühstück."


hi "Wie war sie?"


"Ich bin ein klein wenig Stolz darauf, mit Rins plötzlichem Themenwechsel mithalten zu können."


show rin basic_amused_close onlayer master
with charachange

rin "Ausgezeichnet. Ich erinnere mich nicht, wann ich das letzte Mal eine Orange gegessen habe. Weil es nervig ist, sie zu schälen."


show rin basic_delight_close onlayer master
with charachange

rin "Das steht auf der Liste mit Sachen, die ich noch lernen will."


hi "Wie kommt es dann, dass du eine zum Frühstück hattest?"


show rin basic_deadpanamused_close onlayer master
with charachange

rin "Emi hatte welche, also hat sie eine für mich geschält."


hi "Schön für dich."


show rin relaxed_nonchalant_close onlayer master
with charachange

stop music fadeout 6.0

"Rin reckt sich, gähnt und sagt nichts weiter."


"Sie wirft mir einen Blick aus dem Augenwinkel zu, während sie die vorbeigehenden Leute mustert, aber ich kann nicht genau sagen weshalb."


"Mir fällt allerdings auf, dass ich zum ersten Mal mit jemandem normal über meine Verfassung reden konnte. Gewissermaßen."


stop ambient fadeout 4.0

"Eine Gruppe Jungs läuft an uns vorbei zu Rins Klassenzimmer, aber sie schenkt ihnen keine Beachtung. Sie ihr auch nicht. Angeregt durch die Stille, lasse ich meine Gedanken schweifen."


window hide
nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5,  0.0, channel="music")
play music music_pearly fadein 1.0

n "\n\n\nVielleicht hätte ich sie doch meinen Herzschlag hören lassen sollen. Ist ja nicht so, dass es einen Unterschied machen würde. Im Endeffekt macht nichts wirklich einen Unterschied."


n "Ich fange schon wieder an, mich ohne Grund depressiv zu fühlen. Es ist wie eine Flutwelle aus dem Nichts, die über mein Bewusstsein fegt und mich unter Wasser drückt."


n "Ich spüre, wie mir ein Seufzen entweicht, wende mich von Rin ab und tue so, als würde ich ein Plakat an der Wand lesen. Es ist Werbung für das Schulfest, und damit für ein Ereignis, das bereits fast eine Woche zurückliegt."


n "Der Unterschied zwischen mir und Rin ist, dass ich wahrscheinlich vor meinem 30. Geburtstag tot sein werde, während sie ohne Hilfe keine Orangen essen kann."


n "\n\nIch bin mir nicht sicher, wer von uns beiden schlimmer dran ist."





nvl hide dissolve
nvl clear

scene black onlayer master
with delayblinds

nvl show dissolve

n "\n\n\nIch versuche, mein Zeitgefühl zurückzugewinnen, aber es fällt mir schwer. Ich bin immer noch an den Rhythmus des Krankenhauses gewöhnt, in dem Nebensächlichkeiten wie Wochentage oder die Tageszeit keine Rolle spielten."


n "Alles blieb gleich, egal was geschah."


n "Zeit und ihre Bedeutung wieder einschätzen zu lernen, ist eine merkwürdige Erfahrung, und ich spüre, wie ich Gefallen daran finde, Ereignisse wieder auf diese Art einzuordnen zu können."


show ev watch_black onlayer master:
    center
    alpha 0.0
    linear 1.0 alpha 1.0

n "Das Ticken einer Uhr ist erstaunlich angenehm, und ich entschließe mich, ab sofort eine analoge Armbanduhr zu tragen, auch wenn ich das früher nie getan habe."



n "\nAls ich Rin am Donnerstag endlich etwas frage, was mich schon die ganze Woche beschäftigt, ist es bereits Mittag."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve

scene bg watchhallway_blur onlayer master
show ev watch_worn onlayer master:
    xalign 0.5 yalign 0.5
with locationchange

window show

"Es ist ungefähr 11:06 oder 11:07. Meine Uhr hat keinen Sekundenzeiger. Es ist ein altmodisches Modell mit schwarzem Lederarmband und Titangehäuse."


"Sie ist nicht besonders auffällig, aber das muss eine Uhr auch nicht sein."


show ev watch_worn onlayer master:
    easeout 0.5 ypos 1.0 alpha 0.0
with None

show bg school_hallway3 onlayer master
show crowd behind ev onlayer master
show rin basic_awayabsent behind ev at center onlayer master
show ev watch_worn onlayer master:
    easeout 0.5 ypos 1.0 alpha 0.0
with locationchange

hide ev onlayer master
with None

play ambient sfx_crowd_indoors fadein 2.0

hi "Hey."


show rin basic_absent onlayer master
with charachange

hi "Erinnerst du dich an das Bild, das du von mir gemalt hast? Als du meintest, dass ich darauf finster und grimmig oder so wirke?"


hi "Ich würde gerne wissen, was du damit gemeint hast."


show rin negative_spaciness onlayer master
with charachange

"Sie sieht mich schräg an und neigt ihren Kopf ein paar Grad nach links, sagt aber zunächst nichts."


rin "Na ja, also…"


show rin basic_deadpanupset onlayer master
with charachange

stop ambient fadeout 2.0
stop music fadeout 2.0

rin "Wir kennen uns seit zwei Wochen, und ich hab dich noch kein einziges Mal lächeln sehen."


"Ihre trockene Feststellung verschlägt mir die Sprache."


window hide
nvl clear
nvl show dissolve

n "\n\n\nHabe ich aufgehört zu lächeln?"


n "\nMir bleibt nichts anderes übrig, als ihren Worten Glauben zu schenken. Sie hat keinen Grund zu lügen."


n "Irgendetwas stört mich an der Art, wie sie das formuliert. Ich sehe sie für einen Moment missmutig an, versuche dann aber, ein weniger depressives Gesicht zu machen."


n "Es stimmt, ich war in den letzten paar Monaten nicht gerade gut drauf."


n "Ist das so auffällig, dass es jemand wie Rin in der kurzen Zeit, die wir miteinander verbracht haben, schon merkt?"


n "Sollte ich versuchen, Rin öfter anzulächeln? Vielleicht würde jemand, der selbst ein so neutrales Gesicht hat wie sie, das begrüßen."


n "\nHabe ich wirklich aufgehört zu lächeln?"


nvl hide dissolve
nvl clear
window show

play ambient sfx_crowd_indoors fadein 2.0

hi "Ich verstehe."


hi "Sollte ich mehr lächeln?"


show rin relaxed_nonchalant onlayer master
with charachange

rin "Macht mir beides nichts. Sei wie du bist; du kannst ohnehin nichts daran ändern, Hisao zu sein."


hi "Aber es stört dich?"


show rin basic_absent onlayer master
with charachange

rin "Ist mir nur aufgefallen, mehr nicht."


show emi excited_smile onlayer master:
    tworight
    xpos -0.5
with None

show rin basic_absent onlayer master at tworight
show crowd onlayer master at bgright
show bg school_hallway3 onlayer master at bgright
show emi excited_smile onlayer master at twoleft
with charamove

play music music_emi fadein 0.2

"Emi kommt den Gang entlang gehüpft, kommt mit einem Sprung vor uns zum Stehen und gibt Rin einen leichten Klaps auf die Schulter."


show emi basic_happy onlayer master
with charachange

emi "Bereit zum Mittagessen?"


show rin basic_deadpanupset onlayer master
with charachange

rin "Kommt drauf an, was es heute gibt. Erinnerst du dich an den Eintopf im März? Nie wieder."


show emi basic_closedgrin onlayer master
with charachange

emi "Na dann los. Ich bin am Verhungern!"


hide emi onlayer master
hide rin onlayer master
with charaexit

"Gerade als sie gehen wollen, dreht Emi sich lächelnd zu mir um, als wäre ihr noch etwas eingefallen."


show emi sad_grin onlayer master at center
with charaenter

emi "Ach übrigens, Hisao…"


"Ihre Stimme klingt zuckersüß und viel zu nett, um ehrlich zu sein. Ich kann die Falle förmlich spüren, in die mich dieser kleine Gesundheitsteufel locken will."


"Ich weiß schon, was sie mir sagen will, bevor sie auch nur den Mund öffnet. Immerhin habe ich die gesamte Woche versucht, ihr aus dem Weg zu gehen."


show emi excited_proud onlayer master
with charachange

emi "Ich habe dich die ganze Woche noch nicht auf der Laufbahn gesehen."


hi "Vielleicht war ich ja da, als du gerade woanders warst."


show emi sad_annoyed onlayer master
with charachange

emi "Das ist unmöglich. Ich bin die ganze Zeit da."


hi "Aber du schläfst und gehst zum Unterricht."


show emi basic_annoyed onlayer master
with charachange

emi "Das mache ich zur selben Zeit wie du auch."


hi "Ja, ja, ich weiß. Ich hab mich nur… nicht dazu aufraffen können."


hi "Verpfeif mich nicht beim Doc, okay?"


hi "Laufen ist einfach nicht so mein Ding, und ich hab noch keine passende Alternative gefunden."


show emi excited_happy onlayer master
with charachange

emi "Warum kommst du am Wochenende nicht einfach mit zum Sportfest? Vielleicht inspiriert dich das."


hi "Sportfest?"


show emi basic_happy onlayer master
with charachange

emi "Ja! Leute von ein paar anderen Schulen treffen sich hier zu einem kleinen Leichtathletikwettbewerb. Ist am Sonntag Nachmittag."


"Mir fällt kein Grund ein, nicht hinzugehen."


hi "Klar. Ich komme und feuere dich an. Ich schätze mal, du wirst laufen?"


show emi excited_proud onlayer master
with charachange

emi "Klar! Du wirst mir zusehen können, wie ich sie alle plattmache!"


show emi basic_grin onlayer master
with charachange

emi "Also, bis später dann! Wenn ich nicht bald etwas zu essen kriege, sterbe ich."


hi "Wir sehen uns später."


hide emi onlayer master
with charaexit

stop music fadeout 3.0

hi "Tschüss Rin. Nächstes Mal lächle ich, versprochen."


"Ich rufe ihr noch hinterher. Danach komme ich mir ein wenig blöd vor und frage mich, warum ich überhaupt etwas gesagt habe."


stop ambient fadeout 1.0

scene ev hisao_mirror_800 onlayer master
with shorttimeskip

"Nach Einbruch der Nacht – und nachdem ich mich vergewissert habe, dass Kenji nicht ins Bad hineinplatzt – stelle ich mich vor den Spiegel und lächle mein Spiegelbild an."


"Das andere Ich, das mich aus dem Spiegel heraus angrinst, sieht furchtbar künstlich aus."


scene black onlayer master
with dissolve


label de_R6:

play music music_happiness fadein 2.0

scene bg school_library onlayer master
with locationchange

"Nachdem ich Kenjis Bücher innerhalb weniger Nächte durchgelesen habe, gehe ich zurück in die Bibliothek, in der Annahme, dass das der sicherere Weg ist, um meine Lesesucht zu befriedigen."


"Wo ich schon mal dabei bin, gebe ich – zu Yuukos Freude – auch gleich Kenjis gestohlene Bücher zurück. Woher ich sie habe, behalte ich aber für mich."


show yuuko happy_down onlayer master at center
with charaenter

yu "Wow, du liest ziemlich viel, oder?"


hi "Ja, schätze, das tue ich."


hi "Ich meine, wirklich – sogar ich finde es merkwürdig. Ich glaube, ich habe eine Leseabhängigkeit entwickelt. Vielleicht bin ich ein Junkie."


show yuuko panic_up onlayer master
with charachange

yu "Nein, nein, so hab ich das nicht gemeint. Es ist überhaupt nicht merkwürdig, und es ist viel besser, wenn man lesesüchtig ist als… nach etwas anderem süchtig zu sein."


hi "Ja, ich weiß. Es war ein Witz."


"Ich lächle sie beruhigend an und lege die Bücher auf den Schalter, damit Yuuko sie als geliehen verbuchen kann. Ich fühle mich müde, daher setze ich mich auf einen der freien Stühle vor ihrem Tisch."


show yuuko neutral_up onlayer master
with charachange

"Während Yuuko den überschaubaren Haufen Lesematerial durchgeht, den ich zusammengetragen habe, lasse ich meinen Blick durch die Bibliothek schweifen."


hide yuuko onlayer master
with charaexit

"An den Tischen unterhalten sich zwei Mädchen mit gedämpfter Stimme, anstatt an ihren Hausaufgaben zu arbeiten."


"Die kurzhaarige bemerkt, dass ich in ihre Richtung schaue, und winkt mir zu. Als ich den Gruß erwidere, werfen sie sich einen Blick zu und kichern gemeinsam."


"Ich bin mir nicht sicher, was ich davon halten soll, beschließe dann aber, dass es etwas Gutes ist. Das Mädchen, das mir zugewunken hat, leidet an einer furchtbaren Art von Epilepsie."


"Vor ein paar Tagen habe ich einen ihrer Anfälle mitbekommen. Es war das Verstörendste und Beängstigenste, was ich seit Langem gesehen habe."


"Nichtsdestotrotz sitzt sie da und plauscht glücklich über Gott und die Welt, als hätte sie keine anderen Sorgen."


hi "Weißt du, diese Schule ist wirklich etwas besonderes."


show yuuko panic_up onlayer master
with charaenter

"Yuuko blickt leicht alarmiert von den Büchern auf, die sie gerade durchgegangen ist. Sie rückt ihre Brille zurecht und setzt ein nervöses, verwirrtes Lächeln auf."


show yuuko smile_down onlayer master
with charachange

yu "Wie meinst du das?"


hi "Ich weiß nicht genau, wie ich es erklären soll. Es ist einfach nur… Alle sind so… aktiv, oder… Wie soll ich sagen?"


hi "Ich bin zwar noch nicht so lange hier, aber ich habe einfach das Gefühl, alle sprühen hier vor Energie – und damit meine ich nicht nur die Sache mit dem Fest."


hi "Alle reden mehr, arbeiten härter und sind einfach… lebendiger… als an jeder anderen Schule, die ich bisher gesehen habe."



"Ich ringe nach Worten, aber ich spüre, dass alles, was ich sage, ehrlich gemeint ist."


label de_choiceR6:
menu:
    with menueffect
    hi "Diese Schule fühlt sich so lebendig an."
    "Es ist erfrischend.":




        return m1
    "Ich komme mir vor, als hinge ich fest.":


        return m2

label de_R6a:

hi "Klar, solche Typen gab es an meiner alten Schule auch, aber nicht so viele. Irgendwie kommt mir die Atmosphäre hier intensiver vor."


hi "Ich glaube, wenn ich mich auf einen Grund festlegen müsste, dann den, dass es hier alle wirklich zu schätzen wissen, zur Schule gehen zu können."


label de_R6b:

hi "Die Schule gibt mir das Gefühl, als müsste ich mich auch langsam in Bewegung setzen. Egal in welche Richtung."


label de_R6c:

show yuuko worried_up onlayer master
with charachange

yu "Ich finde nicht, dass das etwas Schlechtes ist."


hi "Ja… Ich auch nicht."


"Plötzlich merke ich, dass ich Yuuko einfach mit meinen Gedanken vollgeplappert habe. So schreckhaft wie sie ist, hoffe ich, dass ich sie nicht überfordert habe."


"Ihr Blick zeigt mehr Neugier als Entsetzen, also hoffe ich, dass sie okay ist."


hi "Entschuldige, dass ich plötzlich über so komisches Zeug rede. Ich wollte dich nicht belästigen."


show yuuko smile_down onlayer master
with charachange

yu "Oh nein, das macht mir gar nichts aus. Ich freue mich zuzuhören, wenn dir nach Reden zumute ist."


show yuuko neutral_down onlayer master
with charachange

yu "Dann komme ich mir auch ein wenig zuverlässig vor."


"Yuuko lächelt mich süß und ein wenig ironisch an. Ich antworte mit einem dankbaren Lächeln meinerseits."


"Sie schiebt mir meine Bücher ordentlich gestapelt über den Schalter. Ich stehe auf und nehme sie entgegen."


show yuuko closedhappy_up onlayer master
with charachange

yu "Bitte schön."


hi "Danke."


show yuuko neutral_up onlayer master
with charachange

yu "Ich vermute, wir werden uns wiedersehen. Du kannst kommen, wann immer du magst."


"Yuukos Freundlichkeit ist herzerwärmend."


hi "Du kannst dich darauf verlassen. Bis später."


stop music fadeout 2.0

scene black onlayer master
with dissolve


label de_R7:


scene bg school_courtyard onlayer master
show crowd onlayer master
with locationchange
play ambient sfx_crowd_outdoors fadein 7.0

"Der Morgen des Sportfestes begrüßt mich mit strahlendem Sonnenschein und kristallblauen Himmel."


"Während ich gemächlich zur Laufbahn schlendere, beschließe ich, dass das ein gutes Zeichen ist. Ich bin mir nur nicht sicher, für was. Ich scheine diesem Ereignis weit weniger abgewinnen zu können als der Rest der Schule."


"Mein Interesse daran, anderen beim Sport zuzuschauen, ist noch geringer als das, selbst mitzumachen. Emi anzufeuern ist ein guter Grund trotzdem hinzugehen."


"Ich verspreche mir keine bewusstseinserweiternde Erfahrung von dem Ganzen, aber schaden kann es auch nicht. Vermutlich würde ich die Zeit sonst eh nur eingepfercht in meinem Zimmer mit Lesen verbringen."


scene bg school_track onlayer master
show crowd onlayer master
show rin basic_absent onlayer master at center
with locationchange

"Als ich die Tribünen erreiche, entdecke ich Rin in der Menge. Kurz darauf bemerkt sie mich ebenfalls."


show rin basic_deadpannormal onlayer master
with charachange

rin "Du bist gekommen."


hi "Natürlich. Ich hab doch gesagt, dass ich komme, oder?"


show rin basic_deadpanamused onlayer master
with charachange

rin "Das heißt nicht unbedingt, dass du es auch tust."


show rin basic_awayabsent onlayer master
with charachange

rin "Viele Leute sagen Dinge, die sie nicht ernst meinen."


hi "Nun, ich zumindest nicht."


play music music_soothing fadein 0.5

show rin negative_spaciness onlayer master
with charachange

"Rin zuckt mit den Schultern. Anscheinend langweilt sie unser Gespräch, und sie macht auf dem Absatz kehrt und geht zurück auf die Tribüne."


hi "Bist du aufgeregt?"


show rin basic_deadpan onlayer master
with charachange

rin "Nicht wirklich."


hi "Ich auch nicht."


show rin basic_absent onlayer master
with charachange

rin "Warum bist du dann gekommen?"


hi "Das könnte ich dich auch fragen."


"Sie antwortet nicht, also entscheide ich mich, es ihr gleichzutun."


"Wir betreten die Tribüne, und Rin nickt in Richtung der oberen Ränge."


show rin negative_spaciness onlayer master at center
with charaenter

rin "Da oben."


show rin basic_deadpancontemplation onlayer master
with charachange

"Rin geht voran, und bald nehmen wir in einer fast leeren Reihe Platz."


$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

show rin basic_deadpancontemplation onlayer master at tworight
show bg school_track onlayer master at bgright
show crowd onlayer master:
    linear 1.0 alpha 0.0
with charamove

hide crowd onlayer master
show meiko smile onlayer master at twoleft
with charaenter

"Neben Rin sitzt eine ältere Frau – ich nehme an, die Mutter von irgendjemandem."


"Sie hat ziemlich langes Haar, das zu einem Zopf geflochten ist. Als sie Rin sieht, grinst sie sie an. Ihr Lächeln kommt mir irgendwie bekannt vor."


show meiko happy onlayer master
with charachange

emm_ "Na, das ist ja eine Überraschung."


show meiko wink onlayer master
with charachange

emm_ "Ich dachte, du wolltest dir was zum Essen holen, keinen Jungen."


hi "Hä?"


show rin basic_surprised onlayer master
with charachange

rin "Ist das schlimm?"


show meiko happy onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Die Frau lacht und schüttelt ihren Kopf, offenbar nicht in der Lage, etwas auf Rins Bemerkung zu erwidern. Ich kenne das Gefühl."


show meiko smile onlayer master
with charachange

emm_ "Na ja, du warst ja schon immer jemand, der eine Sache holen will und mit einer anderen zurückkommt."


emm_ "Aber wo hab ich denn meine Manieren. Ich habe mich noch gar nicht vorgestellt."


emm_ "Ich bin Meiko Ibarazaki. Wenn du Rin kennst, dann bin ich sicher, dass du auch meiner Tochter zumindest schon begegnet bist."


show meiko happy onlayer master
with charachange

emm "Freut mich, dich kennenzulernen."


"Nun, das erklärt alles."
"Sie sieht aus wie eine größere, ältere und mütterlichere Version von Emi."


"Abgesehen davon, dass ihre Haare einen Tick dunkler sind als die ihrer Tochter, ist die Ähnlichkeit wirklich unverkennbar."


show rin basic_absent onlayer master
show meiko smile onlayer master
with charachange

hi "Tut mir leid, ich bin Hisao. Hisao Nakai. Freut mich, Sie kennenzulernen."


show rin basic_lucid onlayer master
with charachange

rin "Ich bin Rin Tezuka."


show meiko happy onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Frau Ibarazaki lacht erneut, lehnt sich etwas in ihrem Sitz zurück und hebt eine Augenbraue. Der Apfel ist wirklich nicht weit vom Stamm gefallen."


$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show meiko serious onlayer master
with charachange

stop music fadeout 1.0

emm "So, nachdem wir uns jetzt alle kennengelernt haben – seit wann seid ihr beiden zusammen?"


"Meine Antwort ist nichts als Stille, während mein Gehirn sich bemüht, in Gang zu kommen. Aber kurz bevor ich eine hastig gestammelte Antwort herausbekomme, bricht Emis Mutter wieder in Gelächter aus."


play music music_soothing fadein 0.5
$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

show meiko happy onlayer master
with charachange

emm "Ha! Du wirst leicht rot, nicht wahr?"


"Ich weiß nicht, ob man in so einer Situation überhaupt seine Würde bewahren kann, also murmele ich nur kurz eine Antwort."


show meiko smile onlayer master
show rin basic_absent onlayer master
with charachange 

hi "Wir sind nicht—"


show meiko happy onlayer master
show rin basic_awayabsent onlayer master
with charachange

emm "Ich weiß, aber es ist so lustig zu sehen, wie du dich windest."


show meiko wink onlayer master
with charachange

emm "Es tut mir leid. Vergib einer alten Frau ihre kleinen Freuden."


"Sie kichert ein wenig in sich hinein."


"Alte Frau?"


"Sie sieht für mich alles andere als alt aus."


show rin basic_absent onlayer master
with charachange

hi "Ich denke, ich kann ein Auge zudrücken."


show meiko happy onlayer master
show rin basic_awayabsent onlayer master
with charachange

emm "Sehr nett von dir."


stop music fadeout 6.0

show rin basic_deadpan onlayer master
with charachange

rin "Es geht los."


stop ambient fadeout 2.0

scene ev emitrack_blocks onlayer master at Fullpan(12.0, dir="left", time_warp=_ease_in_time_warp)
with locationskip

"Ich richte meine Aufmerksamkeit auf die Laufbahn, wo man sich gerade auf den ersten Sprint vorbereitet."


"Sieht aus wie der 400-Meter Lauf."


"Ich suche das Läuferfeld ab, bis ich Emi finde."


scene ev emitrack_blocks_close onlayer master
with flash

"Sie lächelt, auf ihrem Gesicht ein fast schon frecher Ausdruck."


show insert startpistol onlayer master at right
with easeinright

"Der Starter hebt seine Pistole."


$ renpy.music.set_volume(0.5, 0.0, channel="ambient")

play sound sfx_startpistol
play ambient sfx_emisprinting

scene ev emitrack_running onlayer master at Fullpan(1.0, dir="left", time_warp=_ease_in_time_warp)
with silentflash

"Emi fliegt geradezu von ihrem Startblock."



"Es ist fantastisch. Schon als die Läuferinnen auf der innersten Spur zusammen kommen, setzt sich Emi an die Spitze des Feldes."


"Als sie um die letzte Kurve läuft, haben einige andere Läuferinnen zu ihr aufgeschlossen."


"Aber dann legt Emi einen Schlussspurt hin, nach dem alle anderen mindestens eine halbe Sekunde zurück liegen."


scene ev emitrack_finish onlayer master
with locationchange

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

"Frau Ibarazaki johlt, schreit und klatscht und benimmt sich generell so wie alle anderen Eltern, die ihre Kinder anfeuern."


"Emi verlässt die Laufbahn. Sieht aus als wäre sie mit ihrer Leistung zufrieden."


play music music_daily fadein 2.0

scene bg school_track onlayer master at bgright
show meiko happy onlayer master at twoleft
show rin basic_deadpandelight onlayer master at tworight
with locationchange

"Ich jubele zusammen mit den anderen."


"Die Ansagerin (die sich verdächtig nach Misha anhört) verliest fröhlich das Ergebnis."


show meiko smile onlayer master
show rin basic_awayabsent onlayer master
with charachange

emm "Ich glaube, sie ist seit dem letzten Mal noch schneller geworden."


show rin basic_absent onlayer master
with charachange

hi "Das war unglaublich."


show meiko happy onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Frau Ibarazaki grinst stolz."


emm "Emi ist eine tolle Läuferin."


show meiko smile onlayer master
with charachange

"Wir beruhigen uns etwas, während die nächste Disziplin vorbereitet wird."


"Ich bin überrascht, als Emi wieder die Laufbahn betritt."


show rin basic_absent onlayer master
with charachange

hi "Moment mal, ist sie nicht gerade schon gelaufen?"


"Emis Mutter nickt."


show rin basic_awayabsent onlayer master
with charachange

emm "Ja, aber sie läuft in mehreren Disziplinen, vor allem in den Sprints."


show meiko happy onlayer master
with charachange

emm "Es ist ein großes Pensum, aber Emi schafft das."


"So wie es aussieht, hat sie Recht."


"Emi sieht nicht müde aus. Es ist, als wäre sie den vorigen Wettbewerb gar nicht gelaufen."


"Wenn ihr T-Shirt nicht schon verschwitzt wäre, würde man es gar nicht merken."


show rin basic_absent onlayer master
with charachange

hi "Was ist das jetzt für eine Disziplin?"


show meiko smile onlayer master
show rin basic_awayabsent onlayer master
with charachange

emm "Das ist der 200-Meter Lauf."


emm "Sie läuft noch diesen Wettbewerb, dann die 100 Meter und die Staffel."


show rin basic_absent onlayer master
with charachange

hi "Aha."


show rin negative_spaciness onlayer master
with charachange

play sound sfx_startpistol
play ambient sfx_emisprinting

"Wieder erklingt der Schuss, und wieder fliegt Emi von Startblock."


"Ein klopfendes Geräusch lenkt mich von dem Rennen ab."


"Es ist Rins Fuß."


"Sie scheint von dem Rennen total gefesselt zu sein."


show meiko happy onlayer master
with charachange

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

"Emis Mutter jubelt wieder. Ich nehme an, das Rennen ist vorbei."


"Sprints dauern eben nicht wirklich lange."



hi "Dein Fuß."


show rin relaxed_surprised onlayer master
show meiko smile onlayer master
with charachange

rin "Hmm?"


hi "Du hast die ganze Zeit auf die Tribüne gestampft."


show rin basic_deadpan onlayer master
with charachange

rin "Oh."


hi "Du scheinst dich ja wirklich für so was zu interessieren. Das hätte ich nicht gedacht. Du hattest doch gesagt, es würde nichts Aufregendes werden."


show rin relaxed_nonchalant onlayer master
with charachange

rin "Hmm, da hast du wohl Recht."


rin "Ist nicht wirklich interessant."


show rin basic_deadpannormal onlayer master
with charachange

rin "Aber ich schaue Emi zu, nicht dem Wettkampf."


hi "Wie meinst du das?"


show rin basic_lucid onlayer master
with charachange

rin "Emi ist am meisten Emi, wenn sie läuft."


rin "Man sieht sie nicht oft, wenn sie am emisten ist."


show rin basic_deadpanamused onlayer master
with charachange

rin "Aber hier kann man. Sie sehen. Siehst du?"


"Sie lenkt meine Aufmerksamkeit wieder auf die Laufbahn, wo gleich der 100-Meter Lauf startet."


stop music fadeout 6.0
stop sound fadeout 2.0

scene ev emitrack_blocks_close onlayer master
with locationskip

"Ich beobachte Emi genau."


"Als sie an den Startblock herantritt, scheint sich ihr ganzer Körper zu entspannen, aber es ist eine falsche Entspannung."


"Ich kann sehen, dass sie in Wirklichkeit wie eine gespannte Feder ist."


scene ev emitrack_blocks_close_grin onlayer master
with locationchange

"Als der Rennleiter die Läuferinnen auf ihre Positionen schickt, schnellt ihr Kopf nach oben, und ihre Augen verengen sich etwas."


"Sie zieht ihre Mundwinkel nach oben. Ich bin mir nicht sicher, ob das ein Grinsen oder ein Zähnefletschen sein soll."


play sound sfx_startpistol
play ambient sfx_emisprinting

scene ev emi_run_face_zoomin onlayer master
with locationskip

"Als die Pistole losgeht, ist es, als ob man sie von der Leine gelassen hätte."
"Es ist als ob sie schon die ganze Zeit mit rasender Geschwindigkeit gelaufen wäre und wir es nur nicht sehen konnten, bis die Starterpistole die Illusion der Bewegungslosigkeit zerstört hat."


stop ambient fadeout 1.0
play sound sfx_crowd_cheer

"Sobald sie die Ziellinie überquert hat, verschwindet der grimmige Ausdruck von ihrem Gesicht, ersetzt durch ihr normales Grinsen."


"Der siegreiche General kommt nach Hause zurück."


hi "Fantastisch."


hi "Sie ist wirklich fantastisch. Ich habe noch nie jemanden so schnell laufen sehen."


scene bg school_track onlayer master at bgright
show meiko smile onlayer master at twoleft
show rin basic_deadpanamused onlayer master at tworight
with locationchange

emm "Von mir hat sie das nicht. Ich bin viel zu entspannt für diese Rennerei."


stop sound fadeout 9.0

show meiko worry onlayer master
show rin basic_awayabsent onlayer master
with charachange

emm "Nein, Emi hat ihr Talent einzig und allein von ihrem Vater."


"Als sie Emis Vater erwähnt, sieht Frau Ibarazaki wehmütig, fast traurig aus."


emm "Er hat ihr das alles beigebracht, weißt du?"


show rin basic_absent onlayer master
with charachange

hi "Wirklich? Das wusste ich gar nicht."


"Ich belasse es dabei und sage erst einmal nichts mehr. Das scheint eine persönliche Angelegenheit zu sein, und ich sollte besser nicht weiter nachfragen."


play sound sfx_cellphone

"Aus Frau Ibarazakis Jackentasche erklingt ein piepsendes Geräusch. Sie holt ihr Handy heraus und schaut auf das Display."


show meiko serious onlayer master
show rin basic_awayabsent onlayer master
with charachange

emm "Eine SMS? Ernsthaft?"


emm "Wie alt ist er? Sechzehn?"


hi "Hmm?"


show meiko smile onlayer master
with charachange

emm "Ach, nichts."


show meiko wink onlayer master
with charachange

emm "Ich treffe mich noch mit einem Freund."


show meiko happy onlayer master
with charachange

emm "Sagst du Emi bitte, dass ich sehr stolz auf sie bin und dass ich sie heute Abend noch anrufe?"


show rin basic_absent onlayer master
with charachange

hi "Natürlich."


hide meiko onlayer master
with charaexit

show rin basic_absent onlayer master at center
show bg school_track onlayer master at center
with charamove

show rin basic_awayabsent onlayer master
with shorttimeskip

play music music_tranquil fadein 2.0

"Während wir auf den Beginn des Staffellaufs warten, schiele ich zu Rin. Sie zeigt keinerlei Interesse an ihrer Umgebung, mich eingeschlossen."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve




n "„Emi ist am emisten wenn sie läuft.”"


n "Jetzt wo ich darüber nachdenke, ergibt es Sinn. Nachdem ich sie rennen gesehen habe, fällt es mir nicht schwer zu glauben, dass Emi auf der Laufbahn alles gibt."


n "Sport ist für sie mehr als nur ein Hobby oder ein Wettbewerb. Es ist ein grundlegender Bestandteil ihres Lebens."


n "Wie ist das dann mit Rin? Geht es ihr beim Malen genauso? Wenn ich an ihre Hartnäckigkeit vor dem Fest denke, könnte man das leicht annehmen."


n "War Rin also „am rinsten” als ich ihr beim Malen des Wandbildes zugesehen habe?"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show

"Der Staffellauf fängt bald an, aber Emi ist nirgends zu sehen."


hi "Ich dachte Emi läuft auch in der Staffel."


show rin basic_deadpan onlayer master
with charachange

rin "Sie ist die Schlussläuferin."


show rin basic_deadpannormal onlayer master
with charachange

rin "Es dauert noch eine Weile bis sie dran ist."


hi "Aha."


show rin basic_deadpandelight onlayer master
with charachange

rin "Hast du es gesehen?"


hi "Was?"


rin "Emi wenn sie am emisten ist."


hi "Vielleicht."


show rin basic_deadpanupset onlayer master
with charachange

rin "Hmm. Vielleicht dieses Mal."


play sound sfx_startpistol

"Das Rennen beginnt, und ich feuere Emis Teamkameraden an, wenn sie den Stab übergeben."


play ambient sfx_emisprinting

scene ev emitrack_running onlayer master:
    truecenter zoom 1.0 subpixel True
    ease 20.0 zoom 1.05 xalign 0.0 yalign 0.0
with locationskip

"Schließlich sprintet Emi zur letzten Übergabe auf die Bahn."


"Und wieder bin ich sprachlos, wie elegant sie aussieht wenn sie läuft."


"Es ist sieht wirklich wunderschön aus."


"Dieser Ausdruck von Entschlossenheit und Furchtlosigkeit auf ihrem Gesicht verstärkt diesen Eindruck nur noch."


"Das ist Emi wenn sie am emisten ist."


stop ambient fadeout 1.0
play sound sfx_crowd_cheer

show ev emitrack_finish onlayer master
with locationskip

"Mit einem letzten langen Schritt fliegt Emi – zwar nur knapp vor der nächsten Läuferin, aber immernoch als Erste – über die Ziellinie."


$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

scene bg school_track onlayer master
show rin negative_worried onlayer master at center
with locationskip

show rin basic_absent onlayer master
with charachange

rin "Na ja, lass uns runter gehen."


rin "Wir müssen ja die Siegerin krönen."


show rin basic_deadpanamused onlayer master
with charachange

rin "Sieh zu ob du einen Lorbeerzweig findest."


hi "Das wird nicht leicht."


show rin basic_deadpannormal onlayer master
with charachange

"Rin zuckt mit den Schultern."


show rin basic_deadpan onlayer master
with charachange

rin "Zumindest haben wir es versucht."


stop music fadeout 5.0
stop sound fadeout 5.0
play ambient sfx_crowd_outdoors fadein 2.0

scene bg school_track_on onlayer master
show crowd onlayer master
show rin basic_awayabsent onlayer master at center
with locationskip

"Emi ist umringt von ihren Teamkameraden, die ihr alle zu ihrem Lauf gratulieren."


"Rin scheint zu warten, bis Emi bemerkt, dass wir da sind."


"Es ist wohl einfach nicht ihr Stil, Aufmerksamkeit auf sich zu lenken – oder überhaupt eine Regung zu zeigen die über Schulterzucken hinausgeht."


"Da ich ungeduldiger bin als Rin, winke ich Emi an ihrer Stelle zu. Sie schaut auf und grinst uns glücklich an."


show bg school_track_on onlayer master at bgright
show crowd onlayer master at bgright
show rin basic_awayabsent onlayer master at tworight
with charamove

play music music_emi fadein 1.0

show emi basic_closedhappy_gym onlayer master at twoleft
with charaenter

emi "Hey, ihr seid gekommen!"


show rin basic_deadpanupset onlayer master
with charachange

rin "Wir hätten dir einen Lorbeerzweig mitgebracht, aber Hisao hat keinen gefunden."


show emi basic_grin_gym onlayer master
with charachange

hi "Hey, du aber auch nicht."


show rin basic_deadpan onlayer master
with charachange

rin "Es war nicht meine Aufgabe zu suchen."


hi "Wann haben wir Aufgaben verteilt?"


show rin basic_deadpannormal onlayer master
with charachange

rin "Als ich gesagt habe „Sieh zu ob du einen Lorbeerzweig findest.”"


show rin basic_deadpandelight onlayer master
with charachange

rin "Pass doch auf, wenn man mit dir redet."


"Ich zucke mit den Schultern. Anscheinend färbt Rin auf mich ab."


hi "Sieht aus als wäre es doch meine Schuld, Emi."


show emi basic_closedhappy_gym onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Emi lacht Rin und mich an."


show emi basic_happy_gym onlayer master
with charachange

emi "Schon okay, Ich bin sicher, du wirst es irgendwie wieder gut machen."


show rin basic_absent onlayer master
with charachange

hi "Äh, klar."


show rin basic_awayabsent onlayer master
show emi excited_amused_gym onlayer master
with charachange

emi "Prima! Also, wie war ich?"


show rin basic_absent onlayer master
with charachange

hi "Sehr beeindruckend."


show emi basic_closedgrin_gym onlayer master
with charachange

"Emi scheint mit diesem Urteil zufrieden zu sein."


"Ich erwähne nicht, wie viel beeindruckender ihre Leistung angesichts ihrer fehlenden Beine ist. Ich denke, das weiß sie auch selbst."


"Außerdem habe ich das Gefühl, dass ich ihre Leistung damit irgendwie schmälern würde."


show emi basic_grin_gym onlayer master
show rin basic_awayabsent onlayer master
with charachange  

emi "Schön das zu hören! Ich hatte schon Angst ich hätte bei der Staffel etwas zu langsam ausgesehen, aber es lief wohl doch alles okay, hm?"


show emi basic_closedgrin_gym onlayer master
with charachange

"Emi kichert, dann scheint ihr etwas einzufallen."


show emi basic_happy_gym onlayer master
with charachange

emi "Ach ja, bevor ich es vergesse…"


emi "Rin und ich wollen nächsten Sonntag was unternehmen, um den Sieg heute zu feiern!"


show emi excited_proud_gym onlayer master
with charachange

emi "Du solltest mitkommen!"


show emi sad_grin_gym onlayer master
with charachange

emi "Normalerweise machen wir das immer am Tag darauf, aber weil das Turnier dieses Mal an einem Sonntag ist, hab ich Unterricht und Hausaufgaben und all das Zeug."


show rin basic_absent onlayer master
with charachange

hi "Klar, ich würde mich freuen."


show rin basic_awayabsent onlayer master
show emi excited_laugh_gym onlayer master
with charachange

emi "Klasse! Dann ist es also abgemacht!"


show rin basic_absent onlayer master
with charachange

hi "Ach ja. Deine Mutter lässt dir ausrichten, dass sie stolz auf dich ist."


hi "Sie will dich heute Abend noch anrufen."


show emi basic_happy_gym onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Ich wusste doch, dass ich sie auf der Tribüne gesehen habe!"


show emi basic_closedhappy_gym onlayer master
with charachange

emi "Ich bin froh, dass sie es geschafft hat!"


"Teamkamerad" "Hey, Emi! Du verpasst noch die Preisverleihung!"


show emi basic_shock_gym onlayer master
with charachange

emi "Ach ja, danke!"


show emi basic_grin_gym onlayer master
with charadistant

"Sie wendet sich Rin und mir zu."


emi "Ihr müsst dazu nicht hier bleiben. Das dauert immer ewig."


show emi excited_proud_gym onlayer master
with charachange

emi "Außerdem solltest du dich an deine Hausaufgaben machen, wenn du nicht zu lange auf bleiben willst, Hisao."


play sound sfx_emipacing

hide emi onlayer master
with easeoutleft

stop sound fadeout 2.0

show bg school_track_on onlayer master at center
show crowd onlayer master at center
show rin basic_awayabsent onlayer master at center
with charamove

stop music fadeout 5.0

"Emi läuft zurück zu ihren Mannschaftskameraden und lässt Rin und mich allein zurück."


"Keiner von uns beiden hat auch nur das geringste Interesse an den anschließenden Feierlichkeiten, also machen wir uns still auf den Weg zurück zum Wohnheim."


$ renpy.music.set_volume(0.3, 2.0, channel="ambient")

scene bg school_courtyard onlayer master
show crowd onlayer master
show rin relaxed_nonchalant onlayer master at center
with locationskip

"Rin gähnt, ohne dabei zu versuchen sich zurückzuhalten, und scharrt unruhig mit den Füßen."


"Ich fühle mich unbehaglich, aber es ist nicht so extrem, wie es mit jemand anderem als Rin in meiner Gesellschaft wäre. Dennoch hänge ich in der Luft und weiß nicht, was ich als nächstes sagen soll."


hi "Emi war großartig, nicht wahr?"


show rin basic_deadpannormal onlayer master
with charachange

rin "Sie war großartig. Ich bin sehr eifersüchtig auf sie."


hi "Warum?"


show rin basic_awayabsent onlayer master
with charachange

rin "Wie ich gesagt habe, findest du es nicht toll, wenn du wirklich du selbst sein kannst?"


"Es klingt komisch, das aus Rins Mund zu hören."


hi "Ich kann mir nicht vorstellen, dass ausgerechnet du Probleme damit haben sollst, einen Weg zu finden, um dich selbst auszudrücken."


hi "Hast du nicht deine Bilder?"


show rin basic_absent onlayer master
with charachange

stop ambient fadeout 1.0

"Sie dreht sich um und sieht mich an. Zum ersten Mal sehe ich in ihren Augen diesen seltsamen, leeren Ausdruck, der wohl nur bei ihr zu finden ist."


rin "Nein, weißt du, das Problem ist, dass ich mir nicht wirklich sicher bin, wer ich bin."


stop ambient fadeout 1.0
scene black onlayer master
with dissolve


label de_R8:

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
scene bg school_classroomart onlayer master at right
with locationchange

"Das heutige Treffen des Kunstclubs liegt momentan auf Eis, da alle auf Nomiyas Ankunft warten. Ich nutze die dadurch entstandene Zeit, um Rin meine Theorie über die Yamaku zu erläutern."


"Ich habe versucht herauszufinden, was genau mir an dieser Schule so besonders erscheint; dieses gewisse Etwas, das ich Yuuko neulich so erfolglos zu beschreiben versucht habe."


"Es ist immer noch schwer in Worte zu fassen, aber das Sportfest und die Zeit, die ich damit verbracht habe, meine Mitschüler zu beobachten, haben mir geholfen, meine Ideen etwas weiterzuentwickeln."


show rin basic_absent_close onlayer master at center
with charaenter

hi "Ist dir aufgefallen, dass Menschen die ganze Zeit reden?"


hi "Ich kann es nicht wirklich erklären, aber…"


"Und wieder scheitere ich bei dem Versuch, meine Beobachtungen in Worte zu fassen."


"Die Schule ist stark von Cliquen durchzogen, und ich fange gerade erst an, die Feinheiten dieses Netzwerks der Beliebtheit zu begreifen. Trotzdem kann ich mich an keine Schule erinnern, an der ich ein solches Zugehörigkeitsgefühl verspürt habe."


hi "Was ich damit sagen will ist, dass diese Schule nicht so ist wie andere Schulen. Oder zumindest die Schüler sind es nicht, selbst wenn man von den offensichtlichen Gründen einmal absieht."


hi "… Weißt du, was ich meine?"


show rin basic_deadpan_close onlayer master
with charachange

rin "Ich weiß nicht, was du meinst."


hi "Oh, na ja dann… ach komm, was soll's."


"Ich würde das Thema gerne weiter vertiefen, aber in diesem Moment betritt Nomiya den Raum."


hide rin onlayer master
with charaexit

show bg school_classroomart onlayer master at left
with charamove

show nomiya smile onlayer master at center
with charaenter

play music music_happiness fadein 2.0

"Der Lehrer wischt sich den Schweiß von der Stirn und atmet schwer. Er lässt seinen Blick kurz durch den Raum schweifen, bevor er schließlich ein wenig zur Ruhe kommt."


show nomiya veryhappy onlayer master
with charachange

no "Halli hallo; tut mir leid, dass ich so spät bin."



show nomiya talk onlayer master
with charachange

no "Sind alle da? Gut!"


no "Ich muss gestehen, dass ich für heute nicht wirklich etwas vorbereitet habe, weil ich in letzter Zeit extrem beschäftigt war. Ich bin mir aber sicher, dass uns etwas Unterhaltsames einfallen wird."


show nomiya frown onlayer master
with charachange

no "Hat irgendwer Vorschläge? Ich dachte mir, wir könnten mal wieder eine Diskussionsrunde starten. Wir hatten jetzt schon eine ganze Weile keine mehr, und ich zumindest fand die letzte herrlich amüsant."


"Es gibt vereinzeltes Gemurmel, aber keiner spricht sich laut für oder gegen Nomiyas Vorschlag aus."


show nomiya talk onlayer master
with charachange

no "Wir könnten uns mit den verschiedenen Strömungen der Kunst befassen. Oder hat jemand ein gutes Thema?"


no "Na los, ruft einfach etwas rein. Es kann ruhig komisch oder albern sein, wir werden schon etwas Interessantes daraus machen!"


"Keiner scheint mutig genug, um einen Vorschlag zu machen."


"Als die bedrückende Stille weiter ungebrochen bleibt, hebe ich meine Hand."


show nomiya smile onlayer master
with charachange

no "Oho? Unser neuster Freund scheint etwas auf dem Herzen zu haben. Lass hören, Junge, lass hören!"


hi "Äh, also… ich weiß nicht, wie es den anderen geht, aber ich habe mich schon immer gefragt, warum Kunst überhaupt existiert."


stop music fadeout 2.0

"Meine Stimme verstummt. Stille breitet sich im Raum aus, und keiner greift meine kleinlaut vorgetragene Frage auf."


"Dann bricht der Lehrer in Gelächter aus."


show nomiya veryhappy onlayer master
with charachange

no "Hohoho, großartig!"


no "Sehr gut, wirklich sehr gut. Gleich zu Beginn die schweren Geschütze auffahren, was?"


no "Großartig!"


"Für einen Moment schiebt er glucksend ein paar Papiere auf seinem Schreibtisch umher. Als er damit fertig ist, scheint er eine Entscheidung gefällt zu haben."


show nomiya smile onlayer master
with charachange

no "Also dann. Lasst es uns angehen und sehen, wohin es uns führt, okay?"


show nomiya talktongue onlayer master
with charachange

no "Herrje, selbst so ein alter Haudegen wie ich kann im Angesicht von so ungestümem Enthusiasmus nicht ruhig bleiben. Oh ja!"


show nomiya smile onlayer master
with charachange

no "Lasst mich einen Augenblick nachdenken, damit ich einen guten Einstieg für uns finden kann."


"Aus irgendeinem Grund scheint der Lehrer vor Begeisterung beinahe zu platzen. Er kritzelt ein paar Dinge auf eines der Blätter vor sich und beginnt dann, seine Brille mit einem Taschentuch zu reinigen."


show nomiya dreamy onlayer master
with charachange

"Er wirft sich in Pose und legt eine übertrieben dramatische, künstlerische Pause ein, die bestimmt eine halbe Minute anhält."


"Es ist so still, dass man eine Stecknadel fallen hören könnte."


show nomiya talk onlayer master
with charachange

play music music_another fadein 0.5

no "Lasst uns zunächst einmal ein paar Fragen stellen, die wir beantwortet haben möchten, wie etwa „Was ist Kunst?” und „Warum existiert Kunst?”"


show nomiya smile onlayer master
with charachange

no "Hat jemand eine Frage, die damit zusammenhängen könnte?"


"Der Junge mit der Sonnenbrille meldet sich beinahe ohne Verzögerung zu Wort. Seine Stimme ist sanft und leise, und es fällt mir schwer zu verstehen, was er sagt."


"Junge mit Sonnenbrille" "Was macht einen Künstler aus?"


"Nach ihm wird eine weitere Frage gestellt."


"Schüler" "Wenn ich einen Karton mit Wasser fülle und es Kunst nenne, ist es dann Kunst?"


show nomiya veryhappy onlayer master
with charachange

"Darüber lachen alle, sogar der Lehrer."


no "Großartig! Wunderbar, allesamt!"


show nomiya talk onlayer master
with charachange

no "Lasst mich zu Beginn noch sagen, dass es sich hier auf keinem Fall um eine klare Angelegenheit handelt. Ich werde euch daher keine Antworten geben, sondern nur aus meiner eigenen Perspektive sprechen."


no "Gelehrte haben sich seit Menschengedenken über diese Art von Fragen gestritten und dabei nie wirklich einen allgemein akzeptierten Konsens erreicht."


show nomiya smile onlayer master
with charachange

no "Es gibt allerdings ein paar Punkte, in denen sich die meisten relativ einig sind. Bleibt nur zu hoffen, dass sie für euch auch akzeptabel sind."


show nomiya dreamy onlayer master
with charachange

no "Kurz gesagt definiert sich die Kunst selbst. Sie kann nicht einfach starr von außen definiert werden, weil ihre Grenzen von den Kräften in ihrem Inneren ständig neu bestimmt werden."


show nomiya serious onlayer master
with charachange

no "Jeden Tag denkt sich irgendwer irgendwo etwas völlig Unfassbares aus, das alles bisher dagewesene infrage stellt."


show nomiya frown onlayer master
with charachange

no "Der Hauptgrund dafür ist, dass Kunst sich nicht an die rationale Seite des Verstands richtet, sondern auf die Intuition, den Instinkt, die Urtriebe wirkt."
no "Es würde euch sehr schwer fallen zu erklären, warum euch ein bestimmtes Stück oder ein Stil so gut gefällt, nicht wahr?"


"Er wartet nicht auf eine Antwort, bevor er fortfährt."


show nomiya veryhappy onlayer master
with charachange

no "Das ist der Grund dafür."


show nomiya frown onlayer master
with charachange

no "Also ist Kunst dieses wilde, unkontrollierbare Etwas, das irgendwo tief in unserem Unterbewusstsein schlummert. Aber warum existiert sie?"


"Anscheinend erwartet Nomiya, dass jemand eine Vermutung einwirft, aber da keiner es wagt, seine beherzte Rede zu unterbrechen, fährt er fort."


show nomiya dreamy onlayer master
with charachange

no "Das war eine Fangfrage! Wisst ihr, Kunst ist ihre eigene Daseinsberechtigung."


show nomiya talk onlayer master
with charachange

no "Allgemein gesagt könnte man behaupten, dass die Kunst für nichts anderes existiert als für sich selbst. Sie ist etwas, das nur existiert, um eine Spur in der Geschichte zu hinterlassen."


show nomiya serious onlayer master
with charachange

no "Es ist der Trotz eines Sterblichen im Angesicht der Dunkelheit, wie es einmal so schön formuliert wurde. Kunst ist wahrhaft der Beweis unserer Existenz."
no "Ihr solltet wissen, dass menschliche Kultur und Zivilisation eng mit der Existenz von Kunst verknüpft sind."


show nomiya frown onlayer master
with charachange

no "Nun, wie steht es mit Künstlern? Was bringt einen Menschen dazu, sein Leben etwas zu widmen, das so launisch und mysteriös ist, dass es sich sogar einer Definition verwehrt?"


show nomiya serious onlayer master
with charachange

no "Auf diese Frage gibt es so viele Antworten wie Künstler, aber wenn ich es in Worte fassen müsste… Ein Künstler macht keine Kunst, weil er es kann, sondern weil er es muss."


"Nomiya macht eine kurze Pause und lässt seinen Blick mit lodernder Begeisterung über sein Publikum schweifen."


show nomiya frown onlayer master
with charachange

no "Es ist offensichtlich, dass Kunst die Seele jedes einzelnen menschlichen Wesens auf andere Weise berührt. Wenn ihr also die Möglichkeit hättet, auf so grundlegende Art mit euren Mitmenschen in Verbindung zu treten, wie könntet ihr nicht?"


show nomiya talk onlayer master
with charachange

no "Es gibt ein Gedicht, das ich sehr mag, und seinen bekanntesten Teil werde ich euch jetzt vortragen. Ich persönlich finde, dass es die Essenz der Kunst und was es heißt, ein Künstler zu sein, besser einfängt als alles andere."


stop music fadeout 2.5

"Nomiya lehnt sich gegen den Schreibtisch und räuspert sich zur Vorbereitung."


"Den Blick auf einen weit entfernten Ort gerichtet, spricht er die Worte mit seiner sanften Bass-Stimme in die schwere Nachmittagsluft hinein."


show nomiya dreamy onlayer master
with charachange

play music music_one fadein 0.5

no "Um die Welt in einem Sandkorn zu seh'n."


extend "\nUnd den Himmel in einer wilden Blume,"


no "Halte die Unendlichkeit auf deiner flachen Hand."


extend "\nUnd die Ewigkeit in einer Stunde."










"Nach Ende des kurzen Vortrags herrscht eine ernste und unglaublich unangenehme Stille. Keiner wagt es, auch nur ein Wort von sich zu geben."


"Nomiya räuspert sich erneut."


show nomiya talk onlayer master
with charachange

no "Ein Künstler zu sein bedeutet, die Welt in einem Sandkorn zu sehen."


show nomiya dreamy onlayer master
with charachange

no "Wisst ihr, Kinder, ohne Kunst gäbe es nicht viel, für das es sich zu leben lohnt auf dieser Welt. Es ist eine sehr tiefgründige Angelegenheit."


"Offenbar ist er von dem Gedanken sehr ergriffen. Ich warte nur noch auf die einsame Träne, die ihm die Wange hinunter rollt, aber sie bleibt aus."


show rin invis onlayer master at offscreenright
with None

show nomiya invis onlayer master at twoleft
show bg school_classroomart onlayer master at bgleft
show rin basic_awayabsent_close onlayer master:
    xpos 0.9 xanchor 0.5
with dissolvecharamove

hide nomiya onlayer master
with None

"Ich wende mich an Rin und flüstere ihr zu."


hi "Also, was genau ist daran jetzt eine Diskussionsrunde?"


"Sie zuckt als Antwort lässig mit den Schultern."


show rin basic_deadpan_close onlayer master
with charachange

rin "Die davor waren genauso."


"Zu seiner Verteidigung muss man sagen, dass Nomiya sich alle Mühe gibt, eine Diskussion anzuleiern, aber der Klub scheint abgeneigt mitzumachen."


"Ich habe ein schlechtes Gewissen, überhaupt den Mund aufgemacht zu haben. Vielleicht wäre uns das Ganze sonst erspart geblieben."


stop music fadeout 1.5

show rin basic_awayabsent_close onlayer master
with shorttimeskip

play music music_normal fadein 2.0

"Gegen Ende des Treffens merke ich, dass wir heute weder Pinsel noch Farbe auch nur angefasst haben und bin ein wenig enttäuscht."


show nomiya smile onlayer master at twoleft
with charaenter

"Auf einmal steht Nomiya genau neben uns. Er scheint immer noch im Rausch der Rede zu sein, die er gehalten hat."


"Sein Rasierwasser riecht nach Moschus und zuckersüß und bereitet mir umgehend Kopfschmerzen, obwohl ich eigentlich nicht empfindlich auf Parfüm reagiere. Er schaut Rin an wie ein hungriger Wolf."


show nomiya talk onlayer master
with charachange

no "Tezuka, kannst du dich noch an Frau Saionji erinnern, die uns während des Schulfests besucht hat?"


show rin basic_deadpannormal_close onlayer master
with charachange

rin "Ich glaub schon."


show nomiya veryhappy onlayer master
with charachange

no "Ich habe dir etwas Großartiges zu sagen."


show nomiya smile onlayer master
with charachange

no "Die Sache ist die: Sie ist in dieser Gegend eine äußerst bekannte Galeristin. Wie es aussieht, könnte ich sie vielleicht dazu bringen, ein paar deiner Arbeiten auszustellen."


"Er beendet seinen Satz mit einer dramatischen Geste. Anscheinend erwartet er angesichts dieser Neuigkeiten irgendeine Art von freudig geschockter Reaktion von Rin, aber sie starrt ihn nur ausdruckslos an."


show nomiya veryhappy onlayer master
with charachange

no "Prächtig, was? Das könnte eine echte Chance für uns sein, um voranzukommen, Mädel."


show rin basic_surprised_close onlayer master
with charachange

rin "Aber…"


show nomiya frown onlayer master
with charachange

no "Schon gut, ich weiß, was du sagen willst. Ja, es wird sicher keine leichte Angelegenheit, aber ich denke, dass es eine absolut fantastische Chance ist."


no "Ehrlich gesagt wäre ich nicht im Geringsten überrascht, wenn wir damit groß rauskämen! Das könnte der erste Schritt sein! Und dann, wenn wir in aller Munde sind, dann schmieden wir das Eisen, solange es heiß ist! Stimmt's, Nakai?"


hi "Äh, ja, das klingt wirklich großartig. Wenn man so was mag."


show nomiya veryhappy onlayer master
with charachange

no "Siehst du? Wir sollten diese Chance auf keinen Fall verpassen! Hab ich nicht Recht?"


show rin negative_confused_close onlayer master
with charachange

rin "Ich bin nicht… wirklich."


stop music fadeout 7.0

"Aus irgendeinem Grund scheint Rin beunruhigt zu sein. Ich kann nur nicht verstehen weshalb. Was Nomiya sagt klingt durchaus so, als könnte es eine großartige Sache sein."


"Sie klingt allerdings ziemlich niedergeschlagen und durcheinander. So habe ich habe sie noch nie gesehen."


show nomiya talk onlayer master
with charachange

no "Also, was denkst du?"


"Rin schaut nach oben in das strahlende Gesicht ihres Lehrers, dann wieder zurück auf ihren Schreibtisch."


show rin negative_worried_close onlayer master
with charachange

rin "Ich werd drüber nachdenken."


"Nomiya scheint von Rins Mangel an überschäumender Begeisterung nun doch etwas bestürzt zu sein. Dann lächelt er sie breit an und streicht ihr sanft über den Kopf."


show nomiya smile onlayer master
with charachange

no "Braves Mädchen."


hide rin onlayer master
hide nomiya onlayer master
with charaexit

"Das Klubtreffen ist endlich vorbei, und als ich langsam meine Sachen zusammensuche und helfe aufzuräumen, fühle ich mich aus irgendeinem Grund erschöpft. Es gibt aber nicht viel zu tun, sodass es schnell wieder vorbei ist."



label de_R9:

scene bg school_staircase2 onlayer master
show rin negative_spaciness_close onlayer master at tworight
with locationskip

"Ich schließe zu Rin auf, die den Kunstraum nur einen Moment vor mir verlassen hat, und wir laufen die Treppen hinunter ins Erdgeschoss."
"Während ich versuche, mir Nomiyas leidenschaftliche Rede über Kunst noch einmal durch den Kopf gehen zu lassen, scheint Rin in Gedanken versunken zu sein."


"Für sie kein ungewöhnlicher Zustand, wie ich gelernt habe, aber irgendetwas an ihrem Gesichtsausdruck beunruhigt mich."


hi "Was gäbe ich jetzt um deine Gedanken."


show rin basic_deadpancontemplation_close onlayer master
with charachange

rin "Vermutlich zu wenig."


hi "Du bewertest deine Gedanken einfach nur zu hoch."


show rin basic_lucid_close onlayer master
with charachange

rin "Ich würde sie sowieso nicht verkaufen können. Ich bin mir noch nicht sicher, was ich denke. Das wäre dann auch Betrug – als würde man einem Kind den Lutscher klauen."


hi "Das ist Diebstahl, kein Betrug."


show rin basic_deadpanupset_close onlayer master
with charachange

rin "Ich muss darüber nachdenken, was ich denke."


hi "Geht es um das, was Herr Nomiya gesagt hat? Deine Arbeiten ausstellen zu lassen und so?"


scene bg school_lobby onlayer master
with locationchange

"Sie antwortet nicht, bleibt aber stehen, als wir die Eingangshalle erreichen."


"Wir sind die einzigen weit und breit, weshalb es sehr still ist. Ein paar Stockwerke über uns hört man das Echo der Schritte von jemandem, der den Gang entlangeilt."


show rin negative_annoyed onlayer master at center
with charaenter

rin "Ich glaube, ich gehe irgendwo anderswo hin."


"Ich glaube, sie ist tatsächlich beunruhigt."


hi "Willst du Gesellschaft?"


hi "Ich kann nicht versprechen, dass ich eine große Hilfe bei der Denkerei sein werde, aber es ist nicht so, als ob ich sonst noch etwas zu tun hätte, und Doc meinte, ich soll mich bewegen."


show rin basic_absent onlayer master
with charachange

rin "Wenn du magst."


play ambient sfx_parkambience fadein 20.0

scene bg school_backexit onlayer master
with locationskip

"Rin führt mich nach draußen zu der Mauer hinter dem Wohnheim. Dort befindet sich ein kleines schwarzes Tor, aus demselben Schmiedeeisen wie das Eingangstor. Es führt zu einem schattigen Wäldchen hinter der Schule."


"Das Tor ist rostig, so als ob es nicht viel benutzt würde. Es steht jedoch offen, also gehen wir hindurch. Es ist Schülern nicht verboten, das Gelände zu verlassen, aber irgendwie fühle ich mich unwohl dabei."


scene bg school_forest1 onlayer master
with locationchange

"Ein Pfad führt tiefer in den Wald. Große Zelkoven und Ahornbäume rauschen im Wind. Unter ihrem Geäst entstehen kühle Flecken an den Stellen, an denen ihre Schatten den Boden berühren."


"Der Wald riecht stark nach Erde. Mir ist fast schon kalt, obwohl es einer der heißesten Tage mitten im Hochsommer ist."


"Rin trottet voraus wie ein Schlafwandler. Trittsicher, aber ohne erkennbares Ziel im Kopf. Ihre Gedanken scheinen irgendwo anders zu sein. Ich folge ihr mit ein paar Schritten Abstand und achte eher darauf, wohin ich meine Füße setze."


"Der Pfad folgt der leichten Steigung des Geländes, führt dabei aber auch manchmal ein kurzes Stück bergab, bevor er wieder aufwärts geht."
"Die gedeckten Braun- und Grautöne der Stämme säumen den Weg auf beiden Seiten, aufgelockert durch Farne und anderes Gestrüpp."


scene bg school_forest2 onlayer master
with locationchange

"Nach einer Weile beginne ich, mir Sorgen zu machen. Der Pfad ist immer noch breit und nicht überwuchert, also besteht keine Gefahr, sich zu verirren, aber es sieht auch nicht so aus, als hätten wir ein bestimmtes Ziel."


"Es ist ja in Ordnung, ziellos ein wenig umherzuwandern, aber ich will auch nicht so weit laufen, dass ich zu müde für den Rückweg bin."


scene bg school_forestclearing onlayer master
with locationchange

"Ich komme ein wenig außer Atem, und meine Beine fühlen sich schwer an. Ich will anhalten, um wieder zu Atem zu kommen und meine Beine auszuruhen, aber Rin läuft immer weiter."


hi "Wohin gehen wir? Oder gehen wir überhaupt irgendwo hin?"


show rin basic_deadpan onlayer master at center
with charaenter

rin "Sorgenbaum."


hi "Verstehe."


hi "Und was genau ist ein Sorgenbaum?"


show rin negative_spaciness onlayer master
with charachange

rin "Es ist einfach ein Baum. Wie der hier."


"Sie bleibt vor einem besonders großen Ahornbaum stehen, der vielleicht der Sorgenbaum sein könnte. Oder auch nicht. Sein üppiges Blattwerk wiegt sich leicht im Wind, der durch die kleine Lichtung weht, die wir betreten haben."


hi "Hab ich mir schon fast gedacht."


show rin basic_deadpanupset onlayer master
with charachange

rin "Es gibt Leute, die glauben, dass man hierher kommen muss, um sich im eigenen Elend zu suhlen, wenn einem elend ist, nur dass ich mit „Leute” mich meine und der Baum nicht wirklich einen Namen hat."


hi "Also… wenn du Kummer hast, redest du mit einem Baum darüber?"


show rin basic_deadpan onlayer master
with charachange

rin "Nein. Was? Man kann nicht mit Bäumen reden. Was glaubst du, was ich bin? Verrückt?"


hi "Nein… So hab ich das nicht gemeint."


show rin basic_lucid onlayer master
with charachange

rin "Oder vielleicht redest du ja mit Bäumen? Tut mir leid, ich wollte damit nicht sagen, dass du verrückt bist. Obwohl du es wahrscheinlich bist, wenn du mit Bäumen redest."


show rin negative_confused onlayer master
with charachange

rin "Ich würde es auf jedem Fall nicht empfehlen. Die Leute werden denken, dass du ein komischer Kauz bist."


hi "Nein, ich… ach, vergiss es einfach."


"Sie sieht etwas verwirrt aus, was ich ihr aber auch kein bisschen verübeln kann. Sie neigt ihren Kopf ein wenig zur Seite, bevor ihre Gesichtszüge wieder ihre übliche Form annehmen."


show rin basic_absent onlayer master
with charachange

rin "Okay. Ich bin gut im Sachen vergessen."


hi "Also warum sind wir hier? Hast du Kummer?"


"Ich kann die Miene, die sie macht, einfach nicht deuten. Ich hasse es, wie schlecht ich darin bin, Rins Stimmung zu lesen."


show rin negative_worried onlayer master
with charachange

"Sie antwortet nicht gleich, fast so, als wäre sie sich ihrer momentanen Stimmung selbst nicht ganz sicher. Ihr leerer Blick verzieht sich zu einer weiteren undeutbaren Miene, während sie ihr Gewicht von einem Fuß auf den anderen verlagert."


show rin basic_deadpancontemplation onlayer master
with charachange

"Endlich zu einer Entscheidung gekommen, zuckt sie schließlich mit den Schultern. Ich fange an, diese Geste wirklich zu hassen. Sie bedeutet rein gar nichts."


show rin basic_deadpanupset onlayer master
with charachange

rin "Vielleicht. Ich fühle mich einfach nur, als würde ich im Wasser versinken. Ich weiß nicht, was ich machen soll."


show rin negative_confused onlayer master
with charachange

rin "Ich weiß nicht, wohin ich gehen sollte, das ist alles."
rin "Vielleicht ist es keine große Sache, aber ich dachte, laufen könnte vielleicht helfen. Ich dachte, vielleicht… Wenn ich irgendwo hingehen würde, dann wüsste ich, wohin ich gehen sollte. Ich weiß nicht wirklich, ob es geholfen hat."


show rin negative_worried onlayer master
with charachange

rin "Es wäre wirklich logisch gewesen, wenn Laufen geholfen hätte zu entscheiden, wohin man gehen soll."


hi "Du willst also nicht versuchen, eine Ausstellung zu bekommen? Oder vielmehr weißt du nicht, ob du willst oder nicht? Entscheidungsschwierigkeiten?"


"Rin ordnet im Stillen ihre Gedanken und sagt für eine Weile nichts. Die Stille wird durch Vogelgezwitscher von irgendwo aus den Baumwipfeln gebrochen, gefolgt von raschelnden Blättern, als die Vögel zum Flug abheben."


show rin basic_awayabsent onlayer master
with charachange

rin "Vielleicht. Ich bin nicht sicher, ob ich so was machen sollte. Bisher habe ich nur für mich selbst gemalt."


show rin basic_absent onlayer master
with charachange

rin "Ich glaube nicht, dass ich meine Sachen zur Schau stellen könnte, so wie ich jetzt bin. Dieses Ich könnte es nicht."


"Ihre Begründung klingt nach einer mageren Ausrede. Ich setze meinen typischen, finsteren Blick auf, aber sie bemerkt es nicht."


hi "Ich versteh's nicht. Der Lehrer glaubt, du könntest es. Ich glaube nicht, dass er den Vorschlag sonst überhaupt gemacht hätte. Es klang sogar so, als würde er Gefallen von Freunden dafür einfordern."


show rin relaxed_nonchalant onlayer master
with charachange

rin "Ich weiß. Er hat wirklich viel für mich getan. Aber das könnte zu viel sein."


show rin negative_confused onlayer master
with charachange

rin "Jemand zu werden, der es tun kann, könnte ziemlich schwierig sein. Vielleicht könnte ich es gar nicht. Er kann es nicht für mich machen, und wenn ich es ihn versuchen lasse, würde ich nur immer tiefer sinken."


"Rin steht vor dem großen Ahornbaum und dreht sich von mir weg. Ich will die paar Meter, die zwischen uns liegen, überwinden und… Ich weiß auch nicht. Mein Ärger ist auf einmal verflogen, und ich habe Mitleid mit ihr."


hi "Ich weiß genau, wie du dich fühlst."


hi "Na ja, vielleicht auch nicht, aber trotzdem."


hi "Ich glaube, ich habe mich das ganze Jahr nicht so gefühlt, als hätte tatsächlich Kontrolle über mein Leben. Ich schwimme einfach hilflos mit dem Strom."


hi "An diese Schule zu kommen zum Beispiel. Ich habe mir das nicht wirklich ausgesucht, und ich habe mir ganz sicher nicht diesen Punkt in meinem Leben ausgesucht, um herauszufinden, dass ich… diese Krankheit habe."


"Ich kann es immer noch kaum aussprechen."


hi "Es ist, als ob… Ja, es ist genau so, als wäre man unter Wasser. Als könnte man nicht einmal atmen."


show rin basic_sad onlayer master
with charachange

"Mit trauriger Miene wendet sich Rin wieder mir zu."


rin "Ist das der Grund, warum du immer so traurig aussiehst? Ich will nicht so traurig aussehen wie du. Sehe ich für dich so aus, wie du für mich aussiehst?"


hi "Ich sehe doch nicht die ganze Zeit traurig aus."


hi "Es ist nur… Ich weiß nicht, was ich fühlen soll, oder was für ein Gesicht ich machen sollte."


show rin basic_upset onlayer master
with charachange

rin "Ich auch nicht. Sehe ich gerade traurig aus?"


hi "Nicht wirklich. Du siehst aus wie immer, finde ich."


show rin negative_sad onlayer master
with charachange

rin "Aber ich versinke."


show rin negative_worried onlayer master
with charachange

rin "Ich sollte versuchen zu treiben. Nach oben, wie eine Gummiente. Quack, quack, ganz gelb und unheimlich."


"Ich muss ein paar Sekunden darüber nachdenken, ich welche Richtung ich dieses Gespräch lenken soll, merke dann aber, dass es egal ist."


hi "Du findest Gummienten unheimlich?"


show rin basic_surprised onlayer master
with charachange

rin "Du nicht? Ich finde, sie sehen extrem gruselig aus. Alles, was Augen hat aber nicht lebt, ist unheimlich. Wie Gummienten und Reflektionen in Spiegeln."


show rin basic_surprised onlayer master:
    ease 0.5 ypos 1.2 alpha 0.0
with Pause(0.5)

hide rin onlayer master
with None
play sound sfx_rustling

"Sie plumpst auf den Waldboden und lehnt sich an den Baum, den sie Sorgenbaum getauft hat. Nachdem ich eine Minute darüber nachgedacht habe, was ich tun soll, setze ich mich ebenfalls, einen Meter neben ihr."


play sound sfx_rustling
$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

scene bg worrytree onlayer master:
    xalign 0.5 yalign 1.0 subpixel True
    acdc_warp 30.0 yalign 0.0
with whiteout

"Der Wald umschließt uns in seiner Umarmung, und seine Stille legt sich über uns."


"Wir sitzen da, ohne etwas zu sagen. Ich spüre buchstäblich, wie die Zeit vergeht."


"Flecken aus Sonnenlicht, das durch das Blätterdach des Ahornbaums fällt, übersähen die kleine Lichtung mit einem komplexen Muster. Einer der Flecken fällt direkt auf mich und spendet mir seine Wärme."


"Ich denke darüber nach, was ich für mich selbst und vielleicht auch für Rin tun könnte. Für den Moment beobachte ich sie einfach von hier aus weiter."


"Manchmal legt sie ihren Kopf so weit zurück, dass es beinahe schmerzhaft aussieht, und starrt nach oben auf den kleinen Ausschnitt des Himmels, der durch das Blattwerk des Sorgenbaumes zu sehen ist."


"Manchmal starrt sie auch einfach nur mit leerem Blick geradeaus, als könne sie etwas sehen, das knapp außerhalb ihrer Reichweite liegt."
"Sie flüstert immer wieder etwas vor sich hin, aber so leise, dass ich sie nicht hören kann, obwohl ich direkt neben ihr sitze."


"Ich sehe nur, wie sich ihre Lippen bewegen, als wäre sie mitten in einer weit entfernen Traumwelt."


"Ich merke, dass ich mich nicht mehr so enorm einsam fühle wie sonst, wenn ich Nachts im Bett liege und versuche einzuschlafen."


"Vielleicht bin ich Rin ähnlicher als ich dachte."


"Ich kann entweder aufgeben und unter dem Gewicht den ganzen Mists in meinem Leben begraben bleiben, oder ich versuche mich ändern."


"Ihre Entscheidung ist eine andere, aber irgendwie doch gleich."


"Im Gegensatz zu ihr weiß ich allerdings, dass ich nicht für immer so bleiben kann, wie ich bin."


label de_choiceR9:

menu:
    with menueffect
    "Ich muss mich ändern."
    "Ich will mehr wie Rin werden.":




        return m1
    "Ich will mehr wie Emi werden.":


        return m2

label de_R9a:

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")
"Rin könnte es bestimmt schaffen. Sie scheint zwar an sich selbst zu zweifeln, aber ich habe keine Zweifel an ihrer Stärke."


"Sie könnte es schaffen, selbst wenn sie es nicht kann."


label de_R9b:

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")
"Emi hat es bestimmt schon geschafft. Sie ist so fröhlich und energiegeladen, wie eine Läuferin ohne Beine nur sein kann."


"Wenn jemals jemand eine Behinderung „besiegt” hat, dann sie."


label de_R9c:

"Bei dem Gedanken daran fühle auch ich mich etwas besser. Ich lehne mich zurück gegen den Baum und atme lange aus, so als wäre es das erste Mal seit langer Zeit."


show bg worrytree_ss onlayer master:
    yalign 1.0
with shorttimeskip

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

"So verharren wir auf der kleinen Lichtung, bis es zu dämmern beginnt und die Schatten länger werden. Als es langsam kühl wird, verlassen wir den Wald auf demselben Weg, auf dem wir gekommen sind."


scene bg school_forest2_ss onlayer master
show rin negative_spaciness_ss onlayer master at center
with locationchange

"Es scheint nicht so, als habe Rin eine Entscheidung getroffen."


hi "Ich frage mich, ob es eine gute Idee von mir war mitzukommen."


show rin basic_absent_ss onlayer master
with charachange

rin "Schon okay. Macht mir nichts. Ich bin sicher, den Bäumen, der Erde und den Steinen macht es auch nichts. Hat es dir was gemacht?"


hi "Nein, überhaupt nicht. Ich glaube, es hat mir sogar auch geholfen."


$ renpy.music.set_volume(0.4, 1.0, channel="ambient")
scene bg school_forest1_ni onlayer master
with locationskip

"Auf unserem Weg zurück zum Wohnheim wechselt die Farbe des Himmels zu einem dunklen Ultramarin. Die ersten Sterne blinzeln sanft und kaum sichtbar wie kleine Glühwürmchen durch das Geäst der Bäume."


"Rins Gegenwart macht mich auf einmal sehr verlegen."


window hide
nvl clear
nvl show dissolve

stop ambient fadeout 2.0

n "\n\n\n\nIch habe seit der Sache mit Iwanako nicht viel über Mädchen nachgedacht."


n "Diese Situation ist in etwa die gleiche wie damals, aber um ehrlich zu sein, kann man was wohl kaum vergleichen. Nicht mit Rin."


n "Und doch… fühlt es sich gut an, neben ihr zu gehen, selbst wenn es nicht mehr ist als das."


n "Am Anfang hat mich Rin mit ihrem unvorhersehbaren Verhalten ganz schön verunsichert. Mittlerweile kommt es mir aber so vor, als wäre ich zuletzt etwas mehr zur Ruhe gekommen."


n "Ich konnte mich ein bisschen entspannen. Ich fühle mich zufrieden, auch wenn das wohl mehr an mir selbst liegt als an Rin."


n "Sie scheint an vielen Dingen keinerlei Interesse zu haben, aber irgendetwas an ihr hat mein Interesse geweckt."


nvl clear

n "\n\n\nEs ist nicht so, als ob ich sie beeindrucken will; Rin wirklich zu beeindrucken bedürfte vermutlich eines nahezu übermenschlichen Kraftaktes, einfach nur weil sie so ist, wie sie ist. Nein, der Grund ist dieses drängende Gefühl, dass ich Rin nicht enttäuschen sollte."


n "Es ist wirklich seltsam. Ich frage mich, weshalb ich begonnen habe, so zu denken. Ich habe keine Ahnung, was für Erwartungen sie überhaupt an irgendetwas hat."


n "Wie könnte ich sie also enttäuschen? Rin hat diese bescheidene Art an sich und spricht nicht wirklich oft über Dinge. Selbst das heutige Geständnis ihres Selbstzweifels hat mich ein wenig überrumpelt."


n "Ich glaube, ich will mehr mit ihr reden."


n "Plötzlich wird mir klar, dass Rin im Prinzip die einzige Person ist, mit der ich überhaupt noch rede, wenn man einmal davon absieht, was ich von Shizune, Misha oder Kenji zu ertragen habe. Eine etwas deprimierende Erkenntnis."


nvl clear
nvl hide dissolve

scene bg school_dormext_full_ni onlayer master at bgright
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_cicadas fadein 1.0

window show

"Als hätten ihn meine düsteren Gedanken heraufbeschworen, treffen wir vor dem Wohnheim auf Kenji selbst."


show kenji tsun_ni onlayer master at center
with charaenter

"Es ist schon seltsam, ihn draußen dabei zu beobachten, wie er „frische Luft schnappen” geht. Wenigstens dämmert es bereits; ein Teil von mir rechnet wohl damit, dass sich Kenji auflösen würde, wenn er direktem Sonnenlicht ausgesetzt wäre."


"Kenji selbst scheint auch ziemlich verunsichert zu sein. Er steht da und macht den Eindruck, als würde er auf etwas warten, ohne dabei aber selbst zu wissen, worum es sich handeln könnte."


hi "Hey, Kenji. Was treibst du hier draußen?"


show kenji tsun_ni onlayer master at twoleft
show bg school_dormext_full_ni onlayer master at center
with charamove

show rin basic_awayabsent_ni onlayer master at tworight
with charaenter

rin "Hallo."


stop ambient fadeout 0.2

show kenji rage_ni onlayer master
with charachange
with vpunch

ke "Wer seid ihr?"


play music music_tension

show rin basic_absent_ni onlayer master
with charachange

hi "Ich bin's, Hisao. Äh… Ich bin mir nicht sicher, ob du Tezuka aus Klasse 3-4 kennst?"


show kenji tsun_ni onlayer master
with charachange

"An seinem Gesicht kann ich erkennen, dass er Rin nicht nur nicht kennt, sondern dass er sie selbst auf diese kurze Distanz nicht richtig sehen kann."


show kenji happy_ni onlayer master
show rin basic_awayabsent_ni onlayer master
with charachange

stop music fadeout 0.5

ke "Oh, was geht, Jungs?"


play music music_kenji
play ambient sfx_cicadas fadein 6.0

"Kenji streckt enthusiastisch seine Hand aus, beinahe direkt in Rins Magen."


show rin negative_spaciness_ni onlayer master
with charachange

"Rin betrachtet verwirrt seine ausgestreckte Hand, bis Kenji sich räuspert und die Hand zurückzieht."


show kenji neutral_ni onlayer master
with charachange

"Es hat beinahe etwas Cooles, wie er die darauf folgende peinliche Stille überspielt. Nicht, dass ich der geschmeidigste Mensch auf Erden wäre, aber ich glaube nicht, dass ich Kenjis Level auch nur nahe komme."


"Ich glaube, mein Respekt für Kenji ist gerade ein kleines bisschen gewachsen."


show rin basic_absent_ni onlayer master
with charachange

hi "Wartest du auf jemanden?"


show kenji tsun_close_ni onlayer master
with characlose

"Er beugt sich näher an uns heran und senkt seine Stimme zu einem nervösen Flüstern. Ich sehe seine Gesichtsmuskulatur zucken."


ke "Komm schon, Kumpel, du weißt, dass ich in der Öffentlichkeit nicht frei reden kann. Sie könnten vielleicht zuhören."


ke "Ich muss wo hin und etwas Zeug abholen, und ich will nicht, dass diese schnüffelnden Weiber aus dem Schülerrat mir auf die Schliche kommen."


ke "Außerdem vertraue ich deinem Freund nicht. Nichts Persönliches. Bist du sicher, dass er vertrauenswürdig ist?"


"Ich spiele kurz mit dem Gedanken, Kenji über Rins Geschlecht aufzuklären, aber das könnte für einen oder sogar beide böse enden. Ich entscheide mich dagegen."


hi "Ja, ich bin sicher."


show kenji neutral_ni onlayer master
show rin basic_awayabsent_ni onlayer master
with charadistant

"Er wendet sich von mir zu Rin, und ich habe augenblicklich das Gefühl, dass ich die beiden daran hindern muss, miteinander zu sprechen, koste es was es wolle. Abgesehen von physischer Gewalt gibt es allerdings nicht viel, was ich tun könnte."


show kenji happy_ni onlayer master
with charachange

ke "Wärst du in dem Fall interessiert daran, etwas über die größte Bedrohung der Menschheit seit Erfindung des Vegetarismus zu erfahren?"


"Er klingt wie ein Staubsaugervertreter."


show rin basic_deadpan_ni onlayer master
with charachange

rin "Ich dachte, es wäre Sonntag."


show kenji neutral_ni onlayer master
show rin basic_awayabsent_ni onlayer master
with charachange

ke "Ich verstehe, dass du nicht eingeweiht bist. Ja Mann, ich rede hier von menschenfressenden Kühen. Die wenigsten Leute wissen, was ich weiß, ich bin also nicht überrascht."


show kenji happy_ni onlayer master
with charachange

ke "Wir können hier nicht reden, aber wenn du eine Broschüre willst, komm Montags oder Mittwochs nach Beginn der Ausgangssperre zu meinem Zimmer."


"Er greift plötzlich in seine Tasche und zieht einen Kugelschreiber und etwas, das nach einem Kassenzettel aussieht, heraus."


"Kenji kritzelt wild auf dem Fetzen Papier herum und streckt ihn dann Rin entgegen."


show kenji neutral_ni onlayer master
with charachange

ke "Das ist das Passwort. Präg es dir ein, und dann vernichte jede Spur dieses Dokuments. Iss es, verbrenn es, lös es in Säure auf, egal was."


"Da Rin nicht dazu in der Lage ist, nehme ich Kenji den Zettel ab und werfe einen Blick darauf. Es ist in der Tat ein Kassenzettel, anscheinend für zwei Reisbällchen und fünf Packungen Streichhölzer. Ich hoffe, er plant nicht, irgendwas anzuzünden."


"Auf der anderen Seite steht nur ein Wort."


window hide

$ written_note(u"HONIGMUFFIN")


show rin basic_absent_ni onlayer master
with charachange

window show

"Ich zeige auch Rin den Zettel, aber sie zeigt keine Reaktion."


show rin basic_awayabsent_ni onlayer master
with charachange

rin "Danke."


show kenji tsun_ni onlayer master
with charachange

ke "Jo, Hisao. Bist du immer noch in diesem Klub? Der Klub der dunklen Künste?"


show rin basic_absent_ni onlayer master
with charachange

hi "Der bildenden Künste. Aber ja, wir hatten gerade heute ein Treffen."


show rin basic_awayabsent_ni onlayer master
show kenji neutral_ni onlayer master
with charachange

ke "Bist du auch auf der Hut? Keine zwielichtigen Gehirnwäscheaktionen am Laufen? Nichts persönliches, Kumpel, aber ich muss den Überblick behalten."


show kenji tsun_ni onlayer master
with charachange

ke "Kann mich nicht auf frischer Tat ertappen lassen. Apropos, du solltest wirklich ein bisschen später duschen. Man muss den persönlichen Freiraum anderer respektieren. Nichts Persönliches."


"Kenji schaut sich um, als habe er etwas gehört, und strafft seine Jacke."


show kenji neutral_ni onlayer master
with charachange

ke "Okay, ich muss abhauen, bevor es zu spät wird. Bis später, Jungs. Viel Glück."


hide kenji onlayer master
with charaexit

show bg school_dormext_full_ni onlayer master at bgleft
show rin basic_deadpanupset_ni onlayer master at center
with dissolvecharamove
stop music fadeout 4.0

"Kenji macht sich mit schnellen Schritten in Richtung des Eingangstors davon. Rin sieht ihm stirnrunzelnd nach."


"Wir sehen schweigend Kenjis verschwindender Kontur hinterher."


show rin basic_deadpancontemplation_ni onlayer master
with charachange

rin "Was ist sein Problem?"


hi "Also, er ist wohl hier, weil er beinahe blind ist."


show rin basic_deadpansurprised_ni onlayer master
with charachange

rin "Oh. Verstehe."


stop ambient fadeout 2.0

scene black onlayer master
with dissolve


label de_R10:

scene ev hisao_letter_closed onlayer master
with locationchange

"Schon am Umschlag erkenne ich, dass es nichts Offizielles sein kann. Allem Anschein nach hat mir tatsächlich jemand einen altmodischen, handgeschriebenen Brief geschickt."


"Wer macht sich heutzutage überhaupt noch die Mühe mit so etwas? Aber egal wie ich es auch drehe und wende, liegt doch definitiv ein Brief auf meinem Schreibtisch."


scene bg school_dormhisao onlayer master
with locationchange

"Der Unterricht ist für heute vorbei. Den Magen schwer von dem üppigen Mittagessen, das ich unerwarteterweise in der Cafeteria hatte, kehre ich zurück ins Wohnheim."
"Ich habe vor, zunächst meine Hausaufgaben zu erledigen und das Abendessen entweder ausfallen zu lassen oder nur leicht zu essen."


"Es kommt mir so vor, als würde ich weniger essen als früher. Vielleicht verbrauche ich nicht mehr so viel Energie, weil ich ich praktisch nichts mehr tue außer zu lesen."


"Davon abgesehen hat der Brief auf meinem Schreibtisch mich neugierig gemacht."


scene ev hisao_letter_closed onlayer master:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    acdc_warp 10.0 zoom 1.0
with locationchange

"Es ist die erste Post, die ich hier an der Yamaku überhaupt bekommen habe. Das allein wäre ja schon etwas Besonderes, selbst wenn es kein handgeschriebener Brief wäre."


"Was mich aber noch weitaus mehr beunruhigt als die Art des Briefes, ist der fein säuberlich auf die Rückseite des Umschlags geschriebene Name des Absenders."


"Iwanako."


"Ich habe keine Ahnung, aus welchem Grund sie mir schreiben sollte. Ich habe zu niemandem aus meiner alten Klasse Kontakt gehabt, seit ich die Schule gewechselt habe, und Iwanako ist so ziemlich die Letzte, von der ich einen Brief erwartet hätte."


window hide
nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_rain fadein 4.0

n "\n\n\nUnser letztes Treffen verlief schrecklich unangenehm, nahezu peinlich. Sie kam zu mir ins Krankenhaus, schälte mir aus Höflichkeit einen Apfel, und dann saßen wir uns praktisch eine halbe Stunde schweigend gegenüber."


n "Sie sagte schließlich „lebwohl” und schloss die Tür, ohne mir dabei in die Augen zu sehen."


n "Vielleicht war es auch das einzig logische Ende für eine Reihe von Besuchen, die für sie wahrscheinlich genauso schmerzhaft waren wie für mich."


n "Jedes Mal, wenn sie mich im Krankenhaus besuchte, wollte ich mit ihr sprechen, aber etwas hielt mich immer zurück, und jedes Mal, wenn ich nichts sagte, wurde das nächste Mal nur noch schwieriger."


n "Iwanako wirkte schon immer zerbrechlich – fast so, als könnte sie bei der kleinsten Berührung in tausend Teile zerspringen. Anfangs war es vielleicht sogar genau diese Zerbrechlichkeit, die mich zu ihr hingezogen hat, aber nach dem, was damals passiert ist, fühlte es sich so an, als wäre sie wirklich zerbrochen."


nvl clear

n "\n\n\n\n\nSie sah so traurig aus, dass ich nichts sagen wollte, aus Angst, damit vielleicht alles noch viel schlimmer zu machen, und ich konnte die richtigen Worte nie finden."


n "Ich sagte ihr, dass es nicht ihre Schuld war. Sie nickte, und ich glaube wirklich, dass sie verstand, dass es früher oder später auch ohne sie so gekommen wäre."


n "Und doch sah sie jedes Mal so hoffnungslos traurig aus, wenn sie diese Tür öffnete und mein Zimmer betrat."


n "Deshalb gelang es mir nie, die Dinge zu sagen, die ich sagen wollte. Im Endeffekt hat sie das vielleicht sogar noch mehr verletzt."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene ev hisao_letter_open onlayer master
with locationchange

window show

"Vorsichtig öffne ich den Umschlag und ziehe das gefaltete Stück Papier heraus."


window hide

$ written_note("Lieber Hisao,\n\nWie geht es dir? Ich hoffe, dir geht es gut, und dir gefällt es an deiner neuen Schule. Alle hier vermissen dich. Fast unsere gesamte zweite Klasse ist nun zusammen in Klasse 3-1, also haben wir uns von Anfang an gut einfinden können. Ich bin sicher, du wärst auch in diese Klasse gekommen.")


$ written_note("Im Moment sind alle Drittklässler schon sehr angespannt wegen der Abschlussprüfungen, obwohl es noch so lange hin ist. Die Lehrer liegen uns ständig damit in den Ohren – sogar der alte Herr Tachibana, der übrigens dieses Jahr unser Klassenlehrer ist. Hättest du das gedacht? Ich war mir sicher, dass er nach unserem zweiten Jahr in Pension gehen würde, aber er nervt immer noch alle wegen der Examen.\n")


$ written_note("Ich glaube, das ist der Hauptgrund, warum alle Drittklässler so nervös sind. Ich muss zugeben, dass ich auch langsam mein Selbstvertrauen verliere, obwohl ich in Prüfungen bisher immer recht gut abgeschnitten habe.\n\n\n\n\n")


$ written_note("Es ist so seltsam, dass wir plötzlich die Ältesten sind, nicht wahr? Die Zeit ist so schnell vergangen. Ich frage mich, wo sie hin ist. Die neuen Erstklässler sehen so jung und irgendwie unschuldig aus. Ich frage mich immer wieder, ob ich in meinem ersten Jahr genauso war. Ich habe schon das ganze erste Trimester so ein nostalgisches Gefühl.\n\n\n")


$ written_note("Es gibt noch andere Dinge, die ich dir sagen will. Ich schreibe dir, weil ich das Gefühl hatte, dass ich dir nach dem Vorfall im Winter noch vieles hätte sagen sollen. Ich bedaure wirklich, dass ich es dir nicht persönlich sagen konnte, und ich habe dafür keine Entschuldigung.\n\n\n\n\n")


$ written_note("Die Wahrheit ist, immer wenn ich dich im Krankenhaus besucht habe, war ich sehr besorgt um dich. Ich rede nicht über deine Gesundheit. Du schienst dich immer mehr von mir zu entfernen und den Mut zu verlieren. Ich bin sicher, das ist ganz normal, nachdem so etwas passiert, aber irgendwie hatte ich das Gefühl, dass du damals irgendetwas aufgegeben hast. Glück, vielleicht?\n")


$ written_note("Ich wollte irgendwie meine Gefühle zum Ausdruck bringen, aber ich habe einfach nicht die richtigen Worte gefunden. Ich konnte nichts sagen, um dich zu trösten. Es tut mir wirklich leid, dass ich dich nicht unterstützen konnte, als du mich am nötigsten gebraucht hast. Zumindest kann ich jetzt, nach so langer Zeit, ehrlicher sein.\n\n\n\n")


$ written_note("Wenn ich zu diesen stillen Tagen im Februar und März zurückkehren könnte, würde ich dir sagen, dass du dich nicht aufgeben sollst. Vielleicht hättest du dich nicht so weit von mir entfernt, wenn ich einfach nur etwas gesagt hätte. Ich hoffe, du hast es auch ohne mich geschafft, wieder auf die Beine zu kommen.\n\n\n\n")


$ written_note("Jetzt, wo die Entfernung zwischen uns auch physisch ist, fühlt sich alles irgendwie endgültiger an. Ich frage mich, ob wir uns irgendwann einmal wiedersehen. Vielleicht wäre es besser, wenn nicht? Trotzdem, wenn du mir antworten willst, schreib mir bitte zurück. Ich würde wirklich gerne erfahren, wie es dir an deiner neuen Schule geht. Ich wünsche dir alles Gute.\n\nDeine Iwanako")


window show

"Nachdem ich den Brief gelesen habe, falte ich ihn zusammen und lege ihn auf meinen Schreibtisch."


"Ich weiß nicht, was ich davon halten soll. Ich fühle mich leer und verwirrt."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nWarum jetzt, nach all dieser Zeit?"


n "Erst gestern habe ich entschieden, dass ich nicht so bleiben kann, wie ich bin – dass ich versuchen muss, mein Leben auf die Reihe zu kriegen. Diesen Brief zu lesen, erinnert mich nur an all das, was hätte sein können."


n "Natürlich wünsche ich mir, dass ich nicht hier sein müsste. Ich wäre lieber wieder in derselben Klasse wie Iwanako. Vielleicht würden wir jeden Tag miteinander reden und zusammen ausgehen."


n "\nMein Leben hatte andere Pläne."


n "Auf die Erinnerung daran hätte ich gut verzichten können. Iwanako musste diesen Brief für sich selbst schreiben, und ich bin froh, dass sie es konnte, aber es wäre besser gewesen, wenn ich ihn nicht gelesen hätte."


n "\nNatürlich hat sie Recht. Ich dachte mir gestern genau das Gleiche. Ich bin damals in ein Loch voller Depressionen gefallen, und jetzt muss ich versuchen, wieder hinaus zu klettern."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_dormhisao onlayer master
with locationchange

window show

"Ich reiße eine Seite aus meinem Notizheft, und nachdem ich eine Weile über die Formulierung nachgegrübelt habe, schreibe ich eine kurze Antwort an Iwanako."


"Es fällt mir schwer, wirklich ehrlich zu ihr zu sein, aber ich versuche zumindest einigermaßen überzeugend zu klingen. Yamaku erwähne ich mit keinem Wort."


"Ich glaube nicht, dass sie mir noch einmal schreiben wird, aber darüber bin ich auch kein bisschen traurig. Ich falte meinen Brief zusammen, und mangels eines Briefumschlags lege ich ihn neben Iwanakos Brief. Ich werde ihn später abschicken."


"Danach lege ich mich zurück auf mein Bett und schaue an die eintönig graue Decke."


"Ein Vogel zwitschert vor meinem Fenster, und ein plötzlicher Windstoß bringt meine Vorhänge zum flattern. Der Sommernachmittag fühlt sich still an, so als hätte jemand für einen kurzen Moment die Zeit gestoppt."


"Ich denke an all die Dinge, die ich verloren habe und nie zurück bekommen werde."


stop music fadeout 2.0

scene black onlayer master
with dissolve

$ suppress_window_after_timeskip = True


label de_R11:

window hide None

play music music_night

scene bg misc_sky onlayer master at Fullpan(60.0)
with locationchange

nvl clear
nvl show dissolve

n "Und so gingen die trägen Junitage ins Land."


n "Ich schicke meinen Brief an Iwanako und erhalte keine Antwort."


n "Seit ich mich entschlossen habe, mein altes Ich hinter mir zu lassen, beobachte ich meine Mitschüler noch genauer als zuvor, in der Hoffnung zu verstehen, wie andere mit ihren Problemen umgehen."


n "Mir fallen auf einmal Dinge auf, die mir früher entgangen sind, und ich frage mich, ob ich mich gleich zweimal geirrt habe."



n "Oberflächlich betrachtet weichen alle hier von der Norm ab, sind dabei aber gleichzeitig so unglaublich normal, dass ich es erst gar nicht fassen konnte. Ich bewunderte die Art, wie meine neuen Mitschüler es geschafft haben, meine Vorurteile auszuräumen, indem sie einfach nur sie selbst waren."


n "Jetzt, da ich mich allmählich an sie gewöhnt habe, beginne ich neue Nuancen im Verhalten der Menschen zu entdecken, die mich täglich umgeben."


n "Überall umgibt mich diese sanfte, betäubend traurige Atmosphäre."


n "Ich kann sehen, wie sehr sich alle anstrengen müssen, um auch nur halbwegs gut durch den Tag zu kommen, und dass es sie genauso sehr belastet wie mich."


n "Selbst das strahlendste Lächeln wirkt etwas verhalten, jeder Wutausbruch ein kleines bisschen gedämpft. Die Nuancen sind subtil, aber definitiv vorhanden."


nvl clear

n "Ich versuche zu verstehen, was all das bedeutet, was ich von den anderen lernen kann. Ich frage mich, ob jeder – irgendwo tief in seinem Innern – genauso verloren ist wie ich. Gibt es hier auch nur Einen, der wirklich Frieden gefunden hat? Ich spüre, wie ich erneut beginne, an mir zu zweifeln."


n "Ich kann nicht sagen, ob die Schüler hier glücklich sind, unglücklich, oder ob sie einfach nur gelernt haben, damit umzugehen und jetzt in einer Art gefühllosem Vakuum stecken. So wie ich diesen Frühling."


n "Ich entziehe mich diesen Gefühlen, indem ich mich auf einen turmhohen Stapel Bücher stürze, den ich von Yuukos Heiligtum in mein Zimmer trage. Nachdem ich allerdings merke, dass mich das nur noch weiter isoliert, gehe ich öfter in den Kunstclub. Eigentlich immer, wenn ich Zeit habe."


n "Rin scheint dort mehr Zeit zu verbringen als in ihrem Klassenzimmer."


n "Ich habe sie oft auf die Tür am Ende unseres Korridors zuwanken sehen. Die hölzerne Tür und das Zimmer dahinter, gefüllt mit dem Geruch von Farbe und Papier, scheinen ihr mehr zu bedeuten, als der gesamte Rest der Welt."


n "Sie behauptet, sie habe eine Sondergenehmigung, den Raum zu nutzen, woran ich auch nicht zweifle. Ich glaube, es gibt nichts, das Nomiya ihr verweigern würde."


n "Er ist scheinbar so vernarrt in sie wie ein Onkel in seine Lieblingsnichte."


nvl clear

n "\n\n\nDas Objekt seiner Zuneigung jedoch hat keine Favoriten. Sie meint zwar, dass sie zu schätzen weiß, wie sehr sich der Lehrer für sie engagiert, aber selbst wenn sie das sagt, bleibt ihre Miene immer dieselbe."


n "Es ist, als würde sie über einen besonders unscheinbaren Stein sprechen, den sie neulich einmal gesehen hat. Ich werde aus der Beziehung der beiden einfach nicht schlau."


n "Rin scheint niemanden an sich heranzulassen. Ich glaube, nicht einmal Emi könnte von sich behaupten, die Kluft überwunden zu haben, die Rin vom Rest der Welt zu trennen scheint."


n "\n\nIch verstehe es nicht. Sie scheint so gleichgültig zu sein und gleichzeitig doch so leidenschaftlich."


play sound sfx_normalbell

n "Von irgendwoher hört man die Schulglocke läuten – zum letzten Mal für heute."


stop music fadeout 5.0

nvl hide dissolve
nvl clear

scene bg school_classroomart onlayer master
with locationchange

window show

"Ich merke, dass ich schon wer weiß wie lange nicht mehr bei der Sache bin. Benommen setze ich mich auf und versuche, so unverdächtig wie möglich auszusehen."


"Ich hole tief Luft, und der beißende Geruch von Leinöl und Terpentin mischt sich in meiner Nase. Ich fühle mich müde und mir ist schwindelig."


"Es ist schon spät, und einige der Klubmitglieder sind bereits weg. Nur noch Rin, ich, der Lehrer und zwei andere Mädchen, die gerade dabei sind zusammenzupacken, sind noch übrig."


play music music_soothing fadein 4.0

scene ev rin_painting_base onlayer master
with locationchange

"Rin sitzt rechts von mir und arbeitet langsam an einem Bild, während ich mir die Zeit vertreibe. Ich glaube nicht, dass sie gemerkt hat, dass ich sie die ganze Zeit beobachtet habe."


scene ev rin_painting_foot onlayer master:
    xalign 0.5 yalign 0.0 subpixel True
    ease 7.0 yalign 1.0
with locationchange

"Mit einer flinken Bewegung ihres dünnen Knöchels taucht sie den Pinsel in die purpurne Farbe und presst ihn dann sanft gegen die Leinwand. Ein Fleck beginnt sich auszubreiten, als ob der Pinsel bluten würde."


"Ihr Fortschritt ist praktisch zum Stillstand gekommen. Mittlerweile habe ich herausgefunden, dass das gefährlich ist für ihre Technik, da sie fertig sein muss, bevor die Farbe getrocknet ist."


"Mir wird klar, dass ich buchstäblich Farbe beim Trocknen zusehe. Irgendwie ist mir aber nicht langweilig, obwohl ich gerade abgedriftet bin."


window hide

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene ev rin_painting_base onlayer master
with locationchange

nvl clear
nvl show dissolve

n "\n\nDie meiste Zeit geht es im Kunstclub ziemlich entspannt zu, und jeder kann machen, was er will. Wenn uns Nomiya nicht gerade wieder bestimmte Techniken oder Stile beibringen möchte, von denen er begeistert ist, steht es jedem frei, seine eigenen Interessen zu verfolgen."


n "Mangels eines solchen Interesses treibe ich weiter ziellos umher. Ich versuche mal dies, mal jenes, aber nichts hinterlässt einen wirklich bleibenden Eindruck. Erschwerend kommt noch hinzu, dass ich für nichts ein besonderes Talent zu haben scheine."


n "Na ja, ich wurde für meine Versuche mit Wasserfarben gelobt und hatte auch selbst ein ganz gutes Gefühl dabei, aber das war's dann auch."


n "Ich schätze, das war zu erwarten. Ich bin dem Kunstclub schließlich aus einer Laune heraus beigetreten."


n "Ich denke darüber nach, ob ich vielleicht aus dem Klub austreten sollte, wenn es sowieso sinnlos ist. Andererseits ist sinnlos auch nicht wirklich schlimm, und ich kann nicht behaupten, dass ich unglücklich wäre."


n "\nUnbefriedigt vielleicht, aber dafür kann niemand außer mir etwas."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_classroomart onlayer master
with locationchange

window show

"Als die beiden Mädchen den Raum mit einem fröhlichen „Tschüss” verlassen, steht Nomiya von seinem Schreibtisch auf. Sein Stuhl rutscht mit einem lauten Quietschen zurück und zerreißt die harmonische Stille des Nachmittags."



"Er klopft den Stapel Papiere in seiner Hand zweimal gegen den Tisch, um ihn zu Ordnen und streckt sich dann."


show nomiya smile onlayer master
with charaenter

no "Ich habe gleich ein Lehrertreffen, deshalb kann ich nicht bleiben. Ich muss später noch etwas Papierkram erledigen. Wenn du so lange hierbleiben willst, können wir uns danach noch unterhalten. Entschuldige bitte."


"Es sind zwei Menschen im Raum, aber er spricht eigentlich nur mit einem von uns."
"Nomiya macht Überstunden, um Rin nach Ende des Klubs noch Privatunterricht zu geben, und ich würde wetten, dass er seinen Plan, Rins Kunst in einer Galerie ausstellen zu lassen, noch einmal diskutieren möchte."


scene ev rin_painting_base onlayer master
with locationchange

rin "Ist schon in Ordnung. Ich denke, ich werde wahrscheinlich da sein, aber es wäre auch nicht schlimm, wenn nicht. Ich hab gerade nicht viel am Laufen."


"Rin antwortet, ohne ihre Augen von dem Bild abzuwenden, das sie gerade bearbeitet. Der Tonfall ist weder von der höflichen Sorte, die man einem Lehrer gegenüber eigentlich erwarten würde, noch ist es ihr üblicher Monoton."


no "Ich muss also keine Suchpartie losschicken, wenn du nicht hier bist?"


rin "Ja, nein danke. Ich mag keine Partys. Wir können später reden."


scene bg school_classroomart onlayer master
show nomiya veryhappy onlayer master
with locationchange

no "Braves Mädchen."


hide nomiya onlayer master
with charaexit

stop music fadeout 6.0

"Lächelnd nimmt sich Nomiya den Rest seiner Papiere und macht sich auf den Weg zur Tür. Ich werfe einen Blick auf die Uhr darüber und dann auf meine eigene, um sicherzugehen."


"Sie gehen um drei Minuten unterschiedlich, aber nichtsdestotrotz ist das Treffen des Kunstclubs inzwischen vorbei."


"Rin scheint darauf fixiert zu sein, weiter an ihrem Werk zu arbeiten, während sie auf den Lehrer wartet."


"Ich kann mir kaum vorstellen, wie ihr Gespräch unter vier Augen ablaufen würde."


"Würden sie überhaupt irgendetwas diskutieren? Rin ist mit Worten immer so zurückhaltend, und wenn sie dann doch etwas sagt, ist es schwierig zu verstehen, wovon sie eigentlich spricht."


"Vielleicht redet Nomiya auch nur die ganze Zeit und lässt Rin einfach von seinem endlosen Quell des Kunstwissens absorbieren, was sie möchte, wie er es in den Treffen des Kunstclubs zu tun pflegt."
"Wie eine Sonnenblume, die sich dem Leuchten der Sonne zuwendet."


scene ev rin_painting_base onlayer master
with locationchange

hi "Macht es dir etwas aus, wenn ich hierbleibe? Ich äh… dachte, ich könnte es vielleicht noch einmal mit den Wasserfarben versuchen."


"Ich platze mehr oder weniger unabsichtlich mit meiner Entschuldigung heraus und komme mir danach etwas lächerlich vor. Rin lässt ihr Bild nicht aus den Augen."


rin "Okay."


scene bg school_classroomart onlayer master
with locationchange

"Ich rutsche auf meinem Stuhl umher und hole mir dann ein Glas Wasser, Pinsel, Farben und etwas Papier. Das Geräusch meiner Schritte durchdringt die Stille des Nachmittags."


"Bevor es losgeht, versuche ich mich daran zu erinnern, was uns der Lehrer gesagt hat. Eine wichtige Philosophie des Mediums: Mit Wasserfarben zu arbeiten, bedeutet mehr mit dem Wasser zu arbeiten als mit der Farbe."
"Mit diesen Worten im Hinterkopf tauche ich den winzigen schwarzen Pinsel in das Wasserglas."


"Ich mische Gelb und Blau in dem Versuch, die sonnendurchfluteten Baumwipfel vor dem Fenster zu treffen. Die Sonne steht tief, daher sind die Gelbtöne stärker betont, und alles sieht dunkler aus."


"Ich kann das, was meine Hand mit der Farbe macht, noch immer nicht ganz mit dem koordinieren, was meine Augen sehen, aber für mein Niveau ist es ein annehmbarer Versuch."


"Nach einer Weile beginnt meine Konzentration zu schwinden. Ich lege das Papier zur Seite und beschließe, stattdessen Rin eine Weile bei der Arbeit zuzusehen."


"'Eine Weile' wird erst zu einer 'langen Weile', dann zu einer 'sehr langen Weile'."


play music music_dreamy fadein 1.0

scene ev rin_painting_base onlayer master
with locationchange

"Rin malt und ist mit jeder Faser ihres Körpers auf den Pinsel zwischen ihren schlanken Zehen konzentriert und darauf, wie das Bild Strich für Strich zum Leben erweckt wird."


"Sie wirkt entschlossen, aber dabei gleichzeitig auch irgendwie entspannt, wie sie den Pinsel scheinbar mühelos umherbewegt, ohne auch nur einmal zu zögern."
"Farben treffen und trennen sich wieder, mischen sich und überdecken einander auf der Leinwand, die sich Rins stummen Willen zu beugen scheint."


"Ich weiß nicht das Geringste über Komposition, Struktur oder irgendetwas anderes in der Richtung, aber ich mag Rins Bild wirklich sehr. Ich mag, wie sie aussieht, wenn sie malt."


"Wie üblich treibt mich die Stille zwischen uns dazu, etwas zu sagen, anstatt einfach darauf zu warten, dass sie sich öffnet. Sie würde vielleicht auch gar nichts sagen."


hi "Macht es dir etwas aus, wenn wir ein wenig miteinander sprechen?"


scene ev rin_painting_reply onlayer master
with locationchange

rin "Macht mir nichts aus."


hi "Ich wollte dich fragen, warum du dich wegen der Sache, die Nomiya für dich organisieren will, so seltsam benimmst."


"Rin nimmt eine der Farbtuben und drückt mit ihren Zehen beinahe so mühelos etwas Farbe auf die Palette, wie jemand mit opponierbaren Daumen es tun würde. Beim Griff nach dem Pinsel antwortet sie."


scene ev rin_painting_concerned onlayer master
with locationchange

rin "Viele Dinge. Und ein paar Nicht-Dinge. Undinge. Ich glaube, das ist nicht das richtige Wort."


hi "Möchtest du darüber reden?"


"Ich versuche, das unangenehme Gefühl zu unterdrücken, das in mir aufsteigt, während ich unbeholfen meine Hand nach ihr ausstrecke."
"Rins Fokus weicht nicht von ihrem Bild ab, auf dem sie mehr und mehr Farbe verteilt. Ihre Lippen formen eine perfekte, gerade Linie, während sie sich auf die Arbeit konzentriert."


scene ev rin_painting_base onlayer master
with locationchange

rin "Nicht wirklich."


scene ev rin_painting_reply onlayer master
with locationchange

rin "Reden ist schwierig. Ich meine, es ist nicht schwierig, ich rede sogar jetzt gerade. Aber die richtigen Dinge zu sagen, ist wirklich schwer für mich."


scene ev rin_painting_concerned onlayer master
with locationchange

rin "Egal was, ich kann einfach nicht die Dinge sagen, die ich will."


hi "Das klingt seltsam."


scene ev rin_painting_base onlayer master
with locationchange

rin "Es stimmt. Ich sage andauernd alle möglichen Sachen, die ich nicht wirklich meine."
rin "Und manchmal vergesse ich Wörter und benutze dann die falschen Wörter. Ich denke mir sogar neue Wörter aus für Sachen, die schon welche haben. Das ist das Schlimmste an der Sache."


rin "Ich werde richtig unruhig, und alles, was rauskommt, ist nur noch Durcheinander, und nicht einmal ich verstehe, was ich eigentlich sagen wollte."


scene ev rin_painting_concerned onlayer master
with locationchange

rin "Ich glaube, irgendwas stimmt nicht mit mir, dass ich so bin. Erinnerst du dich noch, als ich sagte, dass ich nur an vier Dinge gleichzeitig denken kann?"


"Ich nicke schweigend."


scene ev rin_painting_reply onlayer master
with locationchange

rin "Es sind nicht wirklich vier. Ich meine, es sind vier, aber alles andere ist auch noch da, im Hintergrund irgendwo. Als wäre man gleichzeitig in einem Vergnügungspark und einem Bienenstock. Aber darum geht es nicht."


rin "Ich konnte das mal besser. So sechs oder sieben Dinge. Zumindest glaube ich das. Ich komme mir vor, als würde ich dümmer."


hi "Ich glaube, jeder hat mal Momente, in denen man sich so fühlt, als könne man nicht das Richtige sagen."


scene ev rin_painting_base onlayer master
with locationchange

rin "Aber so ist es die ganze Zeit. Stärker und tiefer. Ja, tiefer ist ein gutes Wort. Ich mag dieses Wort. Tiefer."


rin "Es ist dieses Gefühl unter Wasser zu sein. Vielleicht ist es auch nur Kunst."


scene ev rin_painting_reply onlayer master
with locationchange

rin "Je mehr ich male, desto mehr Worte vergesse ich. Vielleicht vergesse ich irgendwann komplett, wie man spricht."


rin "Es fühlt sich so an, als würde ich langsam alles vergessen. Erinnerst du dich, was du vor drei Jahren über Zeug dachtest?"


rin "Ich nicht."


"Es folgt eine lange Pause, während derer sich die Zeit um sich selbst zu krümmen scheint, fast so als würde sie sich zu einem Knoten verziehen. Ich glaube, ich habe Rin noch nie so ernst und für so lange über irgendetwas reden hören."


scene ev rin_painting_concerned onlayer master
with locationchange

rin "Es ist, als würde ich aus der Welt verschwinden."


scene ev rin_painting_faceconcerned onlayer master:
    xalign 0.5 yalign 0.5 zoom 1.0 subpixel True
    easein 10.0 zoom 1.05
with locationchange

"Rins Fuß hat aufgehört, sich über die Leinwand zu bewegen, und sie starrt regungslos auf ihr Bild, als blicke sie auf einen weit entfernten Horizont."


"Für einen Moment glitzert das Sonnenlicht in ihren Augenwinkeln. Etwas scheint aus den Tiefen ihres Wesens an die Oberfläche gestiegen zu sein, und sie atmet tief aus."


scene bg school_classroomart onlayer master
show rin basic_lucid_close onlayer master:
    tworight
    ypos 1.1
    0.2
    "rin basic_awayabsent_close" with Dissolve(0.3, alpha=True)
with locationchange

stop music fadeout 0.3

"Dann blinzelt sie, und es ist verschwunden."


show rin basic_absent_close onlayer master
with charachange

rin "Bilder bleiben. Wenn ich meine alten Sachen anschaue, dann erinnere ich mich, was ich dachte, als ich sie gemacht habe."


show rin basic_lucid_close onlayer master
with charachange

rin "Mit ihnen fühle ich mich so, als könnte ich bei all den alten Ichs sein, als ich noch ein anderes Ich war."


show rin basic_awayabsent_close onlayer master
with charachange

rin "Sie sind wohl der Beweis für meine Existenz."


"Sie benutzt genau dieselben Worte wie Nomiya, als er mit uns über das Wesen der Kunst sprach. Ich hätte nicht gedacht, dass Rin damals aufgepasst hat."
"Ich frage mich, ob sie zugehört hat, oder ob sie dieselbe leidenschaftliche Rede von Nomiya schon einmal gehört hat."


"So oder so fühle ich mich überwältigt."


hi "Mann, bist du kompliziert. Ich hätte angefangen, Tagebuch zu schreiben."


show rin basic_absent_close onlayer master
with charachange

show rin basic_awayabsent_close onlayer master
with charachange

"Ihre Augen zucken kurz in meine Richtung und dann zurück auf ihr Bild, aber sie greift nicht mehr nach dem Pinsel."


play music music_rin fadein 0.5

rin "Das ist eine geniale Idee. Warum ist mir das nie eingefallen?"


hi "Bist du gerade sarkastisch?"


show rin basic_deadpan_close onlayer master
with charachange

rin "Was ist Sarkasmus?"


"Ich spreche sie nicht auf den Witz an, falls es überhaupt einer war."


show rin basic_awayabsent_close onlayer master
with charachange

"Genau in diesem Moment kehrt Nomiya von seiner Besprechung zurück."
"Leicht überrascht, mich neben seiner Lieblingsschülerin zu sehen, begrüßt er uns mit einem besonders theatralischen Winken. Dann schreitet er ungestümen Schrittes zu seinem Tisch und lässt seine Papiere darauf fallen."


"Er greift nach einem Taschentuch und reinigt seine Brille mit akribischer Sorgfalt, bevor er zu uns herüber kommt."


"Bevor er in Hörweite ist, flüstert Rin mir noch schnell etwas zu."


stop music fadeout 0.5

show rin basic_absent_close onlayer master
with charachange

rin "Veränderungen sind für mich das Furchteinflößendste auf der Welt."


show rin basic_upset_close onlayer master
with charachange

rin "Und ich weiß wirklich nicht, ob ich zu jemandem werden will, der das machen kann, von dem der Lehrer will, dass ich ich es mache. Ich weiß nicht, ob ich es könnte, selbst wenn ich es wollte."


show nomiya talk behind rin onlayer master at twoleft
with charaenter

no "Da bin ich wieder!"



$ doublespeak(hi,rin,"Hallo.")


show nomiya smile onlayer master
with charachange

play music music_pearly fadein 5.0

no "Was ist los?"


"Er schmunzelt etwas verschmitzt, während er uns beide weiter mit unverhohlener Neugier ansieht."


hi "Ah, gar nichts. Wir haben gerade über diese Sache mit ihrer Bekannten und der Galerie gesprochen. Für Rins Arbeiten. Mehr oder weniger."


show nomiya veryhappy onlayer master
with charachange

no "Oho? Irgendwelche Beschlüsse?"


"Ich schaue zu Rin, die versucht, ihre irritierten Gesichtszüge neu zu sortieren."































label de_choiceR11aaa:
menu:
    with menueffect
    hi "Ich denke, ich habe dazu schon alles gesagt. Ich finde, du solltest es versuchen."
    "Ich glaube, du hättest großen Erfolg.":




        return m1
    "Weil es aufregend wäre.":


        return m4
    "Es sieht dir überhaupt nicht ähnlich, so zu zögern.":


        return m5

label de_choiceR11baa:
menu:
    with menueffect
    hi "Ich denke, ich habe dazu schon alles gesagt. Ich finde, du solltest es versuchen."
    "Du vergeudest sonst nur dein Talent.":




        return m2
    "Weil es aufregend wäre.":


        return m4
    "Es sieht dir überhaupt nicht ähnlich, so zu zögern.":


        return m5

label de_choiceR11aba:
menu:
    with menueffect
    hi "Ich denke, ich habe dazu schon alles gesagt. Ich finde, du solltest es versuchen."
    "Ich glaube, du hättest großen Erfolg.":




        return m1
    "Eine solche Chance bekommst du kein zweites Mal.":


        return m3
    "Es sieht dir überhaupt nicht ähnlich, so zu zögern.":


        return m5

label de_choiceR11aab:
menu:
    with menueffect
    hi "Ich denke, ich habe dazu schon alles gesagt. Ich finde, du solltest es versuchen."
    "Ich glaube, du hättest großen Erfolg.":




        return m1
    "Weil es aufregend wäre.":


        return m4
    "Du solltest deine Ziele höher stecken.":


        return m6

label de_choiceR11abb:
menu:
    with menueffect
    hi "Ich denke, ich habe dazu schon alles gesagt. Ich finde, du solltest es versuchen."
    "Ich glaube, du hättest großen Erfolg.":




        return m1
    "Eine solche Chance bekommst du kein zweites Mal.":


        return m3
    "Du solltest deine Ziele höher stecken.":


        return m6

label de_choiceR11bab:
menu:
    with menueffect
    hi "Ich denke, ich habe dazu schon alles gesagt. Ich finde, du solltest es versuchen."
    "Du vergeudest sonst nur dein Talent.":




        return m2
    "Weil es aufregend wäre.":


        return m4
    "Du solltest deine Ziele höher stecken.":


        return m6

label de_choiceR11bba:
menu:
    with menueffect
    hi "Ich denke, ich habe dazu schon alles gesagt. Ich finde, du solltest es versuchen."
    "Du vergeudest sonst nur dein Talent.":




        return m2
    "Eine solche Chance bekommst du kein zweites Mal.":


        return m3
    "Es sieht dir überhaupt nicht ähnlich, so zu zögern.":


        return m5

label de_choiceR11bbb:
menu:
    with menueffect
    hi "Ich denke, ich habe dazu schon alles gesagt. Ich finde, du solltest es versuchen."
    "Du vergeudest sonst nur dein Talent.":




        return m2
    "Eine solche Chance bekommst du kein zweites Mal.":


        return m3
    "Du solltest deine Ziele höher stecken.":


        return m6


label de_R11a:



hi "Ich glaube, du wärst total gefragt. Ich meine, deine Bilder sind wirklich unglaublich."


hi "Außerdem malst du mit deinen Füßen; das ist auch ziemlich cool. Ich wette, die Leute wären völlig von den Socken."


show rin basic_deadpanupset_close onlayer master
with charachange

rin "Das ist keine große Sache. Ich würde mit meinen Händen malen, wenn ich welche hätte."


hi "Oh… Tut mir leid. Entschuldige, so habe ich das nicht gemeint."


show rin negative_confused_close onlayer master
with charachange

"Rin wendet sich ab und starrt schwermütig auf ihr Bild. Ich würde am liebsten zurücknehmen, was ich gerade gesagt habe, wenn das der Grund für Rins Miene ist."


rin "Ich versteh schon."



label de_R11b:



hi "Du würdest dein Talent bloß vergeuden, wenn du nicht hingehst."


show rin basic_surprised_close onlayer master
with charachange

rin "Ver-was?"



hi "Vergeuden. Ich finde, es wäre eine Verschwendung, wenn andere Menschen deine Sachen nicht zu sehen bekämen."


"Ich versuche, sie etwas unter Druck zu setzen, um wenigstens ein bisschen Entschlossenheit aus ihr herauszukitzeln, doch Nomiya beschließt einzuschreiten."


show nomiya smile onlayer master
show rin basic_awayabsent_close onlayer master
with charachange

no "Na, ganz so schlimm ist die Sache nicht."


show nomiya talk onlayer master
with charachange

no "Ich finde auch, man muss das Eisen schmieden, solange es heiß ist, aber Tezuka ist ja immerhin erst achtzehn. Sie wird noch Zeit haben, und ihre Fähigkeiten werden reifen."


show nomiya veryhappy onlayer master
with charachange

no "Nichtsdestotrotz hat es viele Vorteile, wenn man seinen Durchbruch bereits in jungen Jahren wagt, sofern die Möglichkeit dazu besteht."


show rin basic_absent_close onlayer master
with charachange

hi "Schon, aber…"



label de_R11c:



hi "Also ich finde, der Lehrer hat wahrscheinlich Recht. Eine solche Chance kommt vielleicht nie wieder."


hi "Man bekommt nicht viele Chancen im Leben, und du solltest keine von ihnen verschwenden, selbst wenn du Zweifel hast."


show rin basic_absent_close onlayer master
with charachange

"Rin starrt mich ausdruckslos an. Es ist, als wären meine Worte für sie nicht von Bedeutung."



label de_R11d:



hi "Findest du nicht, dass es aufregend wäre? Ich an deiner Stelle würde durchdrehen vor Freude."


show nomiya talk onlayer master
with charachange

no "Hahaha, genau wie ich. Aber hier geht es mehr als nur ein Abenteuer. Es geht um deine Karriere und Zukunft. Obwohl nichts verwerflich daran ist, Freude an etwas zu haben."


"Nomiya verpasst meiner Aufregung einen sanften Dämpfer, aber ich lasse nicht locker."


hi "Mal im Ernst. Der Alltag ist so langweilig! Man macht jeden Tag dasselbe, auf die gleiche Art und Weise. Das wäre mal was anderes."



label de_R11e:



hi "Das sieht dir überhaupt nicht ähnlich. Du hast mir gesagt, dass man Dinge tun sollte, die man nicht tun kann, weil man es kann."


hi "Und jetzt, bei etwas derartig Wichtigen, bist du selbst völlig unentschlossen."



label de_R11f:



hi "Ich finde wirklich, du solltest deine Ziele höher stecken. Du solltest diese Chance nutzen."


hi "Selbst wenn alles schief läuft, hast du es zumindest versucht. Allein dafür lohnt es sich doch schon."


"Nomiya atmet scharf ein, und nach einer Weile langsam wieder aus, als ob er etwas dazu sagen wollte, es aber geschafft hat, sich zurückzuhalten. Schließlich antwortet Rin mir endlich."


show rin basic_surprised_close onlayer master
with charachange

rin "Du glaubst nicht, dass ich so wie ich bin gut genug bin?"


hi "Nein. Ich glaube, du verkaufst dich unter Wert, wenn du so denkst. Es ist feige."



label de_R11g:


show rin basic_deadpanupset_close onlayer master
show nomiya smile onlayer master
with charachange

"Rin sieht mich geistesabwesend an, ohne etwas zu sagen. Ich kann nicht einmal sagen, ob meine Worte eine Wirkung auf sie hatten."


hi "Ich verstehe es einfach nicht. Jeder andere würde vor Aufregung durchs Zimmer springen."


hi "Welchen Sinn hat es, hier im Kunstclub dein Bestes zu geben, wenn du dann nichts aus deinem Talent machst?"


hi "Ich verspreche dir, ich werde wütend auf dich sein, wenn du das nicht durchziehst."


"Meine Stimme wird lauter. Ich weiß nicht, weshalb ich das alles sage. Es ist, als würde ich von einer fremden Kraft gesteuert, über die ich keine Kontrolle habe, aber ich bin wirklich wütend."


"Bilder eines Briefes, geschrieben auf niedlichem Papier, blitzen vor meinem geistigen Auge auf. Bilder von den starren Gesichtern meiner Eltern und Ärzte. Bilder von der Zeit, die ich verschwendet habe."
"Sie vermischen sich mit meinen Gefühlen für Rin wie ein Strom aus geschmolzenem Metall."


show rin basic_deadpanupset_close onlayer master at tworight
with charamove

"Ich will weitermachen, aber plötzlich steht Rin auf."


rin "Na gut."


rin "Ich gehe."


hide rin onlayer master
with charaexit

"Sie schlendert aus dem Raum, ohne dass jemand etwas sagt. Ich starre ihr nach, immer noch kochend, allerdings mit der Stimme der Vernunft im Hinterkopf und der Frage, ob ich sie vielleicht auch wütend gemacht habe."


show nomiya veryhappy onlayer master at center
show bg school_classroomart onlayer master at bgright
with dissolvecharamove

"Der Lehrer gibt ein peinlich berührtes, aber dafür unglaublich lautes Lachen von sich."


show nomiya frown onlayer master
with charachange

no "Sie liegt dir wirklich sehr am Herzen, was?"



label de_R11h:


show rin basic_deadpanupset_close onlayer master
show nomiya smile onlayer master
with charachange

rin "Ich glaube nicht, dass ich darüber reden möchte."


rin "Ich gehe."


show rin basic_deadpanupset_close onlayer master at tworight
with charamove

hide rin onlayer master
with charaexit

"Rin steht auf und schlendert aus dem Raum, ohne dass noch jemand etwas sagt."


show nomiya smile onlayer master at center
show bg school_classroomart onlayer master at bgright
with charamove

hi "Es tut mir leid. Ich glaube, ich habe sie verärgert."


show nomiya veryhappy onlayer master
with charachange

no "Hahaha, mach dir deswegen keine Gedanken. Ich bin mir sicher, sie wird sich wieder einkriegen. Ich rede später noch einmal mit ihr."



label de_R11i:


show nomiya smile onlayer master
with charachange

no "Na na na, mein Junge. Es ist eine große Entscheidung, und obwohl ich Tezuka manchmal gerne selbst etwas entschlossener sehen würde, braucht sie Zeit, um darüber nachzudenken."


show nomiya frown onlayer master
with charachange

no "Warum lassen wir sie nicht entscheiden? Du hast gute Absichten, aber im Endeffekt kommt es auf ihre Gefühle an."


show nomiya veryhappy onlayer master
with charachange

no "Hast du noch etwas hinzuzufügen, Tezuka? Du warst schon den ganzen Nachmittag so still."


"Wir sehen zu Rin, die keinen unserer Blicke erwidert."


show rin basic_lucid_close onlayer master
with charachange

rin "Nein. Ich glaube, ich gehe."


show nomiya talk onlayer master
with charachange

no "Tust du das? Wie schade. Versprich mir aber, dass du mir bis nächste Woche eine Antwort geben wirst, okay?"


show rin basic_deadpanupset_close onlayer master
with charachange

rin "Ist gut."


show nomiya smile onlayer master
with charachange

no "Braves Mädchen."


show rin basic_deadpanupset_close onlayer master at tworight
with charamove

hide rin onlayer master
with charaexit

"Rin steht auf und schlendert aus dem Raum, ohne dass noch jemand etwas sagt."


show nomiya smile onlayer master at center
show bg school_classroomart onlayer master at bgright
with charamove


label de_R11j:


"Nomiya betrachtet mich über den Rand seiner runden, pinkfarbenen Brillen mit einem wohlwollenden Lächeln."


show nomiya talk onlayer master
with charachange

no "Du hast dich also mit ihr angefreundet, was Nakai?"


hi "Äh… na ja, so was in der Art, schätze ich. Hängt davon ab, wie man es betrachtet. Um ehrlich zu sein, bin ich mir nicht wirklich sicher."


"Es ist eher so, dass Rin und ich ab und zu miteinander rumhängen."
"Manchmal unterhalten wir uns dann – oder auch nicht – über etwas, das eher einer Philosophie-Satire gleicht, als einem normalen, alltäglichen Gespräch, das man zwischen zwei Freunden erwarten würde."


show nomiya frown onlayer master
with charachange

no "Na dann ist doch alles in bester Ordnung, oder? Du bist neu hier, und wir sollen Integration in die Schülerschaft fördern."
no "Ich kann mir die ganzen abgedroschenen Phrasen nie merken, die sie drüben in der Fakultät und bei den Treffen der Yamaku Stiftung von sich geben, aber so ist es nun mal."


show nomiya veryhappy onlayer master
with charachange

no "Tezuka ist auch nicht gerade der sozialste Mensch hier in der Gegend."


hi "Das können Sie laut sagen."


show nomiya smile onlayer master
with charachange

no "Also hat sie mit dir über meine Vorschläge gesprochen?"


hi "Oh, nein, nicht wirklich. Ich glaube, es war eher ich, der versucht hat, sie zu einer Entscheidung zu drängen. Vielleicht hätte ich das besser lassen sollen."


show nomiya talk onlayer master
with charachange

no "Nein, ich bin mir sicher, es war in Ordnung. Ich bin viel zu nachgiebig mit ihr, selbst wenn ich es nicht sein sollte. Ich weiß einfach nicht, wie ich mit Tezuka umgehen soll. Sie ist so stur und eigensinnig."


show nomiya talktongue onlayer master
with charachange

no "Ich frage mich, ob die ganzen anderen alten Säcke von Kunstlehrern, denen so ein junges, feuriges Wunderkind in die Hände gefallen ist, sich auch so gefühlt haben."



show nomiya smile onlayer master
with charachange

"Er kichert schelmisch in sich hinein und wendet sich dann Rins neustem Werk zu, das sie zum Trocknen auf der Staffelei gelassen hat. Sie ist so plötzlich verschwunden, dass ich mich frage, ob sie es wirklich für fertig hielt."


show nomiya talk onlayer master
with charachange

no "Na, dann lass uns das Bild mal betrachten."


"Er beugt sich nach vorne und wirft einen prüfenden Blick auf die Leinwand."


show nomiya frown_close onlayer master
with characlose

no "Es vereinnahmt einen völlig, was?"


show nomiya dreamy onlayer master
with charadistant

"Nomiya richtet sich mit verträumtem, nostalgischem Blick auf. Ich antworte nicht auf seine Frage, da er meine Zustimmung anscheinend als gegeben betrachtet."


show nomiya talk onlayer master
with charachange

no "Manchmal bleibe ich nach der Stunde hier, nur um Tezukas Bilder anzusehen."
no "Sie ist wirklich unglaublich – und das schon in diesem jungen Alter. Ich bekomme eine Gänsehaut, wenn ich nur daran denke, was mit ein paar Jahren Übung aus ihr werden könnte."


show nomiya frown onlayer master
with charachange

no "Du hast gefragt, was einen Künstler ausmacht, erinnerst du dich? Das ist es. Sie nehmen ein Stück der Welt und formen es nach ihrem Bilde. Metaphorisch gesprochen, natürlich."


show nomiya dreamy onlayer master
with charachange

no "Sie zu betrachten wirft die Frage in dir auf, wie sie die Welt wohl wahrnimmt. Es ist eine wundervolle Sache, so jung und voller Leidenschaft zu sein. Das ist die außergewöhnlichste Zeit deines Lebens. Das solltest du dir merken, Nakai."


hi "Jawohl."


show nomiya veryhappy onlayer master
with charachange

no "Es ist so absurd."


show nomiya frown onlayer master
with charachange

no "Die Menschen fragen Künstler immer, „Woher nimmst du nur deine Ideen?”, als ob Ideen etwas wären, das man für ein paar Groschen auf dem Markt kaufen könnte."


show nomiya serious onlayer master
with charachange

no "Du kannst Inspiration nicht erklären. Für Menschen wie Tezuka ist es wie atmen. Es ist ein Instinkt."


no "Ich habe in meinem Leben vielleicht einen oder zwei andere mit demselben Potential getroffen. Aber selbst wenn dein Potential noch so groß ist, hilft dir das nichts, solange du dich nicht anstrengst."


no "Es geht um Übung, Technik, Geschick. Male eine Stunde am Tag für ein paar Jahre, und selbst der hoffnungsloseste Fall wird zu einem passablen Künstler."


show nomiya talk onlayer master
with charachange

no "Tezuka ist nicht brillant, weil ihr das Talent dazu in die Wiege gelegt wurde. Sie ist brillant, weil sie härter daran arbeitet als jeder andere – vermutlich seit dem Moment, in dem sie gelernt hat, einen Stift zu halten."


show nomiya veryhappy onlayer master
with charachange

no "Und all das nur mit ihren Füßen. Absolut phänomenal."


"Stille legt sich über den Klubraum, als sich Nomiya wieder von Rins Bild in seinen Bann ziehen lässt und sanft Worte der Zustimmung in Richtung der noch immer feuchten Leinwand murmelt."


hi "Was für Sachen malen Sie eigentlich selbst?"


show nomiya smile onlayer master
with charachange

"Wie aus einem Traum gerissen sieht er mich an, scheinbar überrascht, dass ich überhaupt gesprochen habe."


show nomiya talk onlayer master
with charachange

no "Oh, ich male nicht. Nicht mehr."


show nomiya smile onlayer master
with charachange

no "Ich wurde Kunstlehrer, nachdem meine Karriere auf diesem Gebiet zu Ende gegangen war. Jetzt gebe ich nur noch mein Wissen an die nächste Generation weiter."


"Die Wortwahl des Lehrers ist eigenartig. Einerseits beantwortet sie die Frage, andererseits wirft sie neue auf. Ich würde gerne näher darauf eingehen, aber er schneidet mir das Wort ab, bevor ich dazu komme."


show nomiya veryhappy onlayer master
with charachange

no "Du solltest dich langsam auf den Weg machen, Junge. Es ist fast Zeit fürs Abendessen, oder?"


hi "Stimmt. Einen schönen Abend noch."


show nomiya smile onlayer master
with charachange

no "Dir auch."


scene bg school_hallway3 onlayer master
with locationchange

stop music fadeout 2.0

"Ich sammle schnell meine Sachen ein, trete hinaus in den verlassenen Korridor und lasse Nomiya mit seinen Gedanken allein."


"Das Wochenende steht vor der Tür. Es ist unglaublich, wie schnell die Zeit hier vergeht."


"Ich habe Emi versprochen, bei der Feier für ihren Triumph beim Sportfest letzte Woche dabei zu sein. Das sollte zumindest spaßig werden."


scene black onlayer master
with dissolve


label de_R12:


$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 3.0

scene bg school_courtyard_rn onlayer master
with locationchange

hi "Bist du sicher, dass du da hinwillst?"


"Das fantastische Wetter, das sich den ganzen Juni über gehalten hat, scheint schließlich doch sein Ende gefunden zu haben."
"Die dunklen Wolken, die über dem Dorf hängen, sehen bedenklich aus, und die Luft ist schwer und steht nahezu still wie vor einem Unwetter."


"Der Wetterbericht sagt für den Nachmittag eine Regenwahrscheinlichkeit von 60%% voraus. Vielleicht fängt heute die Regenzeit an."


show emi basic_grin_rn onlayer master at center
with charaenter

emi "Natürlich bin ich sicher! Darauf habe ich schon die ganze Woche gewartet!"


"Emi hatte ein Picknick in einem naheliegenden Park geplant – mit reichlich Snacks aus dem Mini-Markt. Bei der derzeitigen Wetterlage scheint das Vorhaben jedoch riskant."


show emi basic_annoyed_rn onlayer master
with charachange

emi "Ich habe noch ein paar andere Leute gefragt, ob sie mitwollen, aber sie meinten, das Wetter würde nicht halten. Wir werden ihnen beweisen, dass sie falsch lagen!"


hi "Inwiefern falsch?"


show emi excited_smile_rn onlayer master
with charachange

emi "Na du weißt doch, dass es immer regnet, wenn du denkst, es regnet nicht, und wenn du denkst, es wird regnen, dann bleibt es trocken. Wir gehen auf jeden Fall, also haben wir so oder so schon gewonnen!"



show emi basic_closedhappy_rn onlayer master
with charachange

emi "Ich habe wegen meines Trainings für das Sportfest wochenlang auf Süßigkeiten verzichtet, aber jetzt kann ich reinhauen, und es gibt nichts, was mich daran hindern könnte."


hi "Und ich dachte, der ganze Gesundheitskram wäre genau dein Ding."


show emi excited_proud_rn onlayer master
with charachange

emi "Ohoho, Hisao, wenn du wüsstest. Es gibt auf diesem Planet nicht ein einziges Mädchen, das keine Süßigkeiten liebt!"


show emi excited_proud_rn onlayer master at twoleft
show bg school_courtyard_rn onlayer master at bgleft
with charamove

show rin basic_deadpan_rn onlayer master at tworight
with charaenter

rin "Ich mag keine Süßigkeiten."


show emi excited_joy_rn onlayer master
show rin basic_awayabsent_rn onlayer master
with charachange

emi "Sie zählt nicht. Also, hab ich mich klar ausgedrückt?"


show rin basic_absent_rn onlayer master
with charachange

hi "Klipp und klar. Wir werden losziehen und uns mit Süßigkeiten vollstopfen."


show emi basic_closedgrin_rn onlayer master
show rin basic_awayabsent_rn onlayer master
with charachange

emi "Und wie wir das werden."


show emi excited_laugh_rn onlayer master
with charachange

emi "Ich werde es später wieder abtrainieren müssen, aber das ist es mir wert."


"Emi scheint fest entschlossen zu sein. Sie ist ganz aus dem Häuschen und quillt wie immer über vor Energie, aber etwas ist anders als sonst."


"Es scheint fast so, als könne sie sich selbst kaum davon abhalten, vor Freude auf und ab zu springen."


show emi excited_joy_rn onlayer master
with charachange

emi "Komm schon!"


hide emi onlayer master
hide rin onlayer master
with charaexit

"Ich greife nach dem hölzernen Griff meines Regenschirms und folge dann den beiden Mädchen, die den Eindruck erwecken, als hätten sie kein Problem damit, mich zurück zu lassen, sollte ich weiter trödeln."


"Mein Schirm ist wirklich elegant. Es ist die altmodische Sorte mit geschwungenem Griff und Metallspitze. Er gehörte meinem Großvater. Er sieht aus wie eine Antiquität, aber er ist in wirklich gutem Zustand; praktisch wie neu."


"Außerdem ist er ziemlich groß. Ich erinnere mich, wie mein Großvater, meine Großmutter und ich alle darunter gepasst haben, als uns eines Nachmittags beim Spazierengehen ein Unwetter überraschte. Ich war damals gerade mal neun oder zehn."


"Meine Großeltern sind mittlerweile nicht mehr unter uns, aber ich habe immer noch den Schirm, der mich trocken hält, wenn es regnet."


scene bg school_road_rn onlayer master
with locationskip

"Wir laufen im dunklen Schatten der Wolken entlang der Straße, die von der Schule zum Mini-Markt hinunter führt. Das Wetter scheint schlechter zu werden, und ich bin mir ziemlich sicher, gerade einen Tropfen abbekommen zu haben."


hi "Habt ihr nicht daran gedacht, euch Schirme mitzunehmen? Es sieht wirklich aus, als würde es jeden Moment regnen."


show rin basic_deadpancontemplation_rn onlayer master at tworight
show emi basic_grin_rn onlayer master at twoleft
with charaenter

"Rin schaut auf ihre schlaff herunterhängenden Ärmel und zuckt mit den Schultern."


show emi basic_closedgrin_rn onlayer master
show rin basic_awayabsent_rn onlayer master
with charachange

emi "Ich hab nicht mal einen. Davon abgesehen wird uns das bisschen Regen schon nicht umbringen."


"So wie sie sich vor mir aufbaut, scheint sie sich dessen ziemlich sicher zu sein."


show emi basic_happy_rn onlayer master
with charachange

emi "Wir sind nicht aus Zucker!"


show rin basic_absent_rn onlayer master
with charachange

hi "Ich dachte, gerade daraus seien Mädchen gemacht – besonders wenn man bedenkt, womit du dir heute den Bauch vollschlagen willst."


show emi sad_annoyed_rn onlayer master
with charachange

"Sie streckt mir zur Antwort nur die Zunge heraus."


hide emi onlayer master
hide rin onlayer master
with charaexit

"Der Weg von der Schule hinunter zum hiesigen Geschäftsviertel ist nicht weit, aber er ist auch nicht sonderlich kurz. Es geht nur bergab, daher fallen uns unsere Schritte nicht schwer, aber die Zeit dehnt sich dennoch wie ein Kaugummi."


"Die Distanz ist genau richtig, in einem Bereich, in dem man nicht erwartet, dass der Ausflug schnell vorbei ist, aber auf einen längeren Marsch bereitet man sich auch nicht vor."


"Also ist der Weg etwas zu lang, um ihn einfach schweigend zu absolvieren, obwohl es den Mädchen nichts auszumachen scheint."


"Rin läuft still voraus, anscheinend in Gedanken verloren. Ich bin mir nicht sicher, ob ich noch einmal versuchen soll, ein Gespräch zu starten. Das letzte Mal endete für keinen von uns gut."


"Seither habe ich kein Wort mehr mit ihr gewechselt."


"Emi auf der anderen Seite ist viel zu glücklich darüber, überhaupt unterwegs zu sein."


"Sie scheint bei jedem Schritt ein wenig in die Luft zu springen, hüpft über Risse in der Straße, oder balanciert auf der Bordsteinkante."
"Ab und zu macht sie eine Bemerkung zu etwas, worauf Rin eine fast schon mechanisch klingende, unsinnige Antwort gibt, die Emi zum Kichern bringt."


$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_rain fadein 5.0

scene bg suburb_roadcenter_rn onlayer master
with locationchange

"Als wir den Fuß des Hügels erreichen, beginnen die ersten Tropfen zu fallen. Ich spüre, wie einer von ihnen auf meinem Kopf landet und noch zwei weitere auf meiner Nase."


play sound sfx_thunder
stop music

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")
$ renpy.music.set_volume(1.0, 4.0, channel="music")
show rain light onlayer master
with dissolve

"Es sind nicht mehr nur eine oder zwei Regenwolken. Der gesamte Himmel über uns hat sich in ein von Schatten durchzogenes, graues Meer aus dunklen Wolken verwandelt."


show emi sad_pout_rn behind rain onlayer master at center
with charaenter

emi "Oh verdammt. Ich schätze, wir werden dann wohl doch kein Picknick haben."


hi "Was jetzt?"


show emi sad_pout_rn onlayer master at twoleft
show bg suburb_roadcenter_rn onlayer master at bgleft
with charamove

show rin negative_spaciness_rn behind rain onlayer master at tworight
with charaenter

rin "Vielleicht könnten wir ein Regenpicknick machen. Ein Picknick im Regen."


show emi basic_annoyed_rn onlayer master
with charachange

emi "Nein, wir würden uns bloß alle erkälten, und ich mag es nicht, wenn ich oder meine Snacks nass werden."


show rin relaxed_nonchalant_rn onlayer master
with charachange

rin "Ich mag es irgendwie. Nur nicht das mit den Snacks."


$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

show emi basic_concentrate_rn onlayer master
show rain medium onlayer master
with charachange
play sound sfx_rustling

"Emi überdenkt unsere problematische Situation für einen Moment, während ich meinen Schirm öffne und versuche, ihn so zu halten, dass wir alle darunter passen."


show emi basic_happy_rn onlayer master
with charachange

emi "Hey Hisao, warst du schon mal im Shanghai?"


show rin basic_absent_rn onlayer master
with charachange


label de_R12a:

hi "Das ist ein Café hier in der Nähe, oder? Ich hab davon gehört."



label de_R12b:

hi "Ja, unsere Klassensprecherin hat mich in der ersten Woche einmal dorthin mitgenommen."



label de_R12c:

show rin basic_awayabsent_rn onlayer master
show emi basic_grin_rn onlayer master
with charachange

emi "Es ist nett da. Lass uns dort hingehen und abwarten, bis der Regen vorbei ist. Wenn es wirklich nur ein kurzer Schauer ist, können wir danach immer noch picknicken gehen, und wenn es schlimmer wird, bestellen wir uns dort einfach einen Kuchen."


show rin basic_absent_rn onlayer master
with charachange

hide emi onlayer master
with charaexit

hide rin onlayer master
with charaexit

"Weder Rin noch ich haben eine bessere Idee, also folgen wir Emi strammen Schrittes in eine Seitenstraße."


$ renpy.music.set_volume(1.0, 6.0, channel="ambient")

scene bg suburb_shanghaiext_rn onlayer master
show rain normal onlayer master
with locationchange

"Das Café ist nur ein paar Blöcke entfernt, aber selbst mit dem Schirm können wir es nicht vermeiden, etwas nass zu werden. Der Regen wird immer heftiger."


"Die Tropfen hinterlassen winzige Punkte auf dem schwarzen Asphalt und zerlaufen schließlich zu größeren Flecken. Es ist, als entstünde vor unseren Augen ein pointillistisches Kunstwerk."


"Der Regen fällt in Strömen, trommelt auf die Dächer der geparkten Autos und fließt bereits in kleinen Bächen den Bordstein entlang."


"Das gelbe Licht, das durch die nassen Scheiben scheint, sieht warm und einladend aus."


play sound sfx_storebell
stop ambient fadeout 0.5
play music music_jazz fadein 2.0

scene bg suburb_shanghaiint onlayer master at left
with locationchange

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

"Ich schüttle das Regenwasser vom Schirm, und wir gehen gemeinsam hinein. Ich folge Emi zu einem freien Tisch in der hintersten Ecke des Cafés."


$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

"Es ist beinahe kein Platz mehr. Offenbar hatten auch noch anderen Leuten dieselbe Idee wie Emi, und nun sind alle zusammen mit uns an diesem kuscheligen Ort gestrandet."


scene bg suburb_shanghaiint onlayer master at Fullpan(5.0)
with None

"Lackierte hölzerne Säulen und Papierschirme mischen sich mit Tischen und Stühlen des Pariser Stils zu einem dissonant-harmonischen Kontrast von Alt und Neu."


"Aus dem Hintergrund hört man lockeren Jazz, der aber größtenteils im Stimmgewirr der anderen Gäste untergeht."



label de_R12d:


"Es gibt nur eine Kellnerin, die das ganze Haus bedient, hektisch von einem Tisch zum nächsten eilt und dabei versucht, nicht den Überblick zu verlieren. Zu meiner Überraschung kommt sie mir äußerst bekannt vor."


"Ich beobachte sie, wie sie ein Tablett mit Tee und Gebäck zu einem anderen Tisch mit Yamaku-Schülern bringt und eine Bestellung von einer Pärchen mittleren Alters, das uns gegenüber sitzt, entgegen nimmt, bevor sie sich schließlich uns zuwendet."


hi "Yuuko?"


show yuukoshang neurotic_up onlayer master at Slide(0.6,0.5,0.5,0.5,0.5)
show bg suburb_shanghaiint onlayer master at right
with charaenter

"Aus der Nähe betrachtet kann ich endlich sehen, dass sie es wirklich ist. Die Teilzeit-Bibliothekarin aus unserer Schule in voller Kellner-Montur. Es ist ein ziemlich niedliches Outfit, und ihre Haare sind zu passenden Knoten gebunden."


show yuukoshang worried_up onlayer master at center
with charachange

"Bei ihrem anderen Job macht sie mit dem einfachen, schüchternen Stil einen völlig anderen Eindruck. Yuuko wirkt verwirrt und blinzelt ein paar Mal, bevor sie sich daran erinnert, dass sie eigentlich etwas sagen wollte."


show yuukoshang panic_down onlayer master
with charachange

yu "Ähm… äh, willkommen im Shanghai."


hi "Hier arbeitest du also auch? Ich dachte, du würdest studieren oder so."


show yuukoshang neurotic_down onlayer master
with charachange

yu "Äh, ja, das auch. Es ist ein Teilzeitjob, wie du sehen kannst, hehe. Es ist Sonntag, also gibt es auch keine Vorlesungen."


show yuukoshang neutral_down onlayer master
with charachange

yu "Zum Glück. Heute war so viel los, dass ich mir ein zusätzliches Paar Arme wünsche. Na ja, egal. Ich bin etwas in Eile, wie ihr sehen könnt. Was darf ich euch bringen?"



label de_R12e:

"Ich bemerke, dass Yuuko heute Schicht hat, aber so hektisch wie sie von einem Tisch zum nächsten eilt, scheint es, als müsse sie das gesamte Haus allein bedienen."


"Ich beobachte sie, wie sie ein Tablett mit Tee und Gebäck zu einem anderen Tisch mit Yamaku-Schülern bringt und eine Bestellung von einer Pärchen mittleren Alters, das uns gegenüber sitzt, entgegen nimmt, bevor sie sich schließlich uns zuwendet."


hi "Hallo, Yuuko."


show yuukoshang neurotic_up onlayer master at Slide(0.6,0.5,0.5,0.5,0.5)
with charaenter

yu "Ähm… äh, willkommen im Shanghai."


hi "Du scheinst beschäftigt zu sein."



show yuukoshang neurotic_down onlayer master at center
with charachange

yu "Ahaha, ich bin hier total überfordert. Ich wünschte, ich hätte ein zusätzliches Paar Arme."


show yuukoshang neutral_down onlayer master
with charachange

yu "Was darf ich euch bringen?"



label de_R12f:

show emi excited_joy onlayer master at Slide(-0.1,0.0,0.0,0.0,0.5)
show rin basic_awayabsent onlayer master at Slide(1.05,1.0,0.95,1.0,0.5)
with charaenter

stop music fadeout 1.0
$ renpy.music.set_volume(0.4, 2.0, channel="ambient")

"Emi zögert nicht einmal eine Sekunde. Ihre Augen glitzern wie die eines Kindes in Süßwarenladen."


play music music_comedy fadein 1.0
show emi excited_amused onlayer master at left
with charachange

emi "Tee für alle! Und Kuchen für mich!"


show yuukoshang smile_up onlayer master
with charachange

"Yuuko versucht so formal und professionell wie möglich zu bleiben, während sie meine heißhungrige Gefährtin fröhlich anlächelt."


show yuukoshang smile_down onlayer master
with charachange

yu "Ähh… ja, heute haben wir Erdbeerkuchen, Himbeer-Sahnetorte oder Zitronen-Baisertorte zur Auswahl."


show emi basic_happy onlayer master
with charachange

emi "Erdbeer… nein, Zitrone! Nein, am besten bringst du mir beide!"


"Sie sieht mich herausfordernd an."


hi "Äh… Ich nehme nur Zitrone, bitte."


show rin basic_deadpan onlayer master at Position(xalign=1.0, xpos=0.95)
with charachange

rin "Nichts."


show emi basic_annoyed onlayer master
with charachange

"Emi sieht Rin mit einem Blick an, als habe sie gerade in eine Zitrone gebissen. Sie ist offensichtlich unzufrieden, dass Rin nicht mitisst."


emi "Och komm schon, Rin. Das ist doch unhöflich."


show rin relaxed_boredom onlayer master
with charachange

rin "Nichts, danke."


show emi basic_confused onlayer master
with charachange

emi "Nein, nein, du Dummerchen! Ich meinte, dass du auch etwas bestellen sollst."


show rin negative_spaciness onlayer master
with charachange

rin "Dann nehme ich einen Strohhalm. Meine Füße sind ganz nass."


show yuukoshang worried_up onlayer master
with charachange

yu "Entschuldigung?"


show rin basic_awayabsent onlayer master
with charachange

rin "Die Sorte, mit der man trinken kann. Einen bitte."


show yuukoshang worried_down onlayer master
with charachange

"Yuuko weiß offensichtlich nicht, was sie davon halten soll. Für einen Moment fummelt sie mit ihrem Stift herum und sieht dabei aus, als könne sie jeden Moment losheulen, bevor sie unsere Bestellung als abgeschlossen akzeptiert."


show yuukoshang neurotic_up onlayer master
with charachange

yu "Vielen Dank!"


show yuukoshang neurotic_down onlayer master at Transform(ypos=1.25)
with Dissolvemove(0.2)

with Pause(0.3)

show yuukoshang neurotic_down onlayer master at center
with charamove

hide yuukoshang onlayer master
with charaexit

show emi basic_grin onlayer master at twoleft
show rin basic_awayabsent onlayer master at tworight
with dissolvecharamove

$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

"Sie verbeugt sich etwas zu tief und zieht sich dann hinter den Tresen zurück."


"Nachdem das Schlimmste vorbei zu sein scheint, habe ich Gelegenheit, mich ein wenig zu entspannen und die Umgebung genauer zu untersuchen."


"Beinahe jeder Tisch ist besetzt mit Leuten, die froh sind, dem Regen entkommen zu sein. Die meisten von ihnen nippen dankbar an ihrem Tee, während sie darauf warten, wieder trocken zu werden."


"Gesprächsfetzen über das lausige Wetter und Diskussionen über die letzten Hausaufgaben dringen von den umliegenden Tischen an mein Ohr. Sie überlappen einander, aber sie alle werden vom Regen übertönt."


show emi basic_grin onlayer master at left
show rin basic_awayabsent onlayer master at Position(xpos=0.95, xalign=1.0)
with charamove

show yuukoshang smile_up onlayer master at center
with charaenter

$ renpy.music.set_volume(0.4, 2.0, channel="ambient")

"Nach einer Weile kehrt Yuuko zurück an unseren Tisch. Sie trägt ein Tablett mit einer großen Teekanne, drei Tassen, einem Stück Kuchen und zwei Stück Torte."


show yuukoshang neurotic_up onlayer master at centertremble
with charachange

with Pause(0.5)

show yuukoshang smile_down onlayer master at Transform(ypos=1.25)
with Dissolvemove(0.2)
play sound sfx_pillow

with Pause(0.3)

show yuukoshang smile_down onlayer master at center
with charamove

hide yuukoshang onlayer master
with charaexit

show emi basic_grin onlayer master at twoleft
show rin basic_awayabsent onlayer master at tworight
with dissolvecharamove

$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

"Mit einem Klappern stellt sie das Tablett auf unseren winzigen Tisch, wobei der Teekessel beinahe auf Rins Schoß landet. Bevor wir uns versehen, verbeugt sie sich nochmals und eilt zum nächsten Gast."


"Emi hat ihren Erdbeerkuchen schon die ganze Zeit mit hungrigen Augen angestarrt, aber irgendwie ist es ihr gelungen, sich zurückzuhalten, bis Yuuko außer Sicht war."


show emi excited_smile onlayer master
with charachange

"Sie greift genüsslich zu, während ich mich damit begnüge, uns Tee einzugießen und den Strohhalm in Rins Tasse zu platzieren."


show rin basic_deadpansurprised onlayer master
with charachange

"Rin sieht mit halb geschlossenen Augen zu, wie der Tee in der weißen Porzellantasse umherwirbelt, und wirkt dabei fast wie hypnotisiert."


show shangpai onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Ich nehme meine Gabel und betrachte das Essen vor mir. Der Kuchen, den ich bekommen habe, sieht perfekt aus, mit einer dicken Schicht Schaumgebäck auf einer cremigen Zitronensoße."


"Nach meinem ersten Bissen mache ich eine Pause und genieße die Kombination von herbem Zitrus und geschmeidiger, zuckeriger Meringe. Er ist ziemlich gut, wenngleich auch ein wenig zu süß für meinen Geschmack."


show emi excited_joy onlayer master
show rin basic_deadpannormal onlayer master
with None

show shangpai onlayer master:
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide shangpai onlayer master

emi "Fmegt fer gud."


"Sie spricht mit dem Mund voller Kuchen. Obwohl ihr Stück nicht gerade klein ist, ist es schon halb verschwunden."


show emi basic_grin onlayer master
with charachange

emi "Lass mich das mal probieren."


play sound sfx_slide2

show emi excited_happy_close onlayer master
show rin basic_absent onlayer master
with characlose

show emi basic_closedgrin onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Bevor ich etwas sagen kann, stößt sie mit ihrer Gabel in Richtung meiner köstlichen Torte, erwischt ein Stück und zieht sich damit zurück."


show emi basic_closedhappy onlayer master
with charachange

emi "Der ist auch ziemlich gut."


hi "Was soll das? Du hast selbst ein Stück davon!"


show emi excited_proud onlayer master
with charachange

emi "Schon, aber damit anzufangen, bevor ich mit meinem Kuchen fertig bin, wäre doch unhöflich, findest du nicht?"


"Ihre Unverfrorenheit schlägt dem Fass den Boden aus, aber der Gentleman in mir erlaubt keinen Gegenschlag."


show emi basic_grin onlayer master
with charachange

"Ich starre sie wütend an und bekomme als Antwort ihre schelmische Zunge zu sehen. Emi ist heute noch aufgedrehter als sonst, aber es macht mir nichts aus. Es tut ihr gut, etwas Dampf abzulassen."


"Ich nehme einen weiteren Schluck von dem Tee in meiner Tasse. Er ist gut und heiß, obwohl ich mir sonst nicht viel aus Tee mache, und die Atmosphäre hier im Café ist sehr entspannend."


"Es macht mir nichts aus, den Rest des Nachmittags hier zu verbringen, nicht einmal, als Emi ihre zweite Portion Erdbeerkuchen bestellt und Rin die meiste Zeit den vom Himmel strömenden Regen anstarrt."


show rain normal behind bg onlayer master
with None

"Selbst Yuuko verdreht die Augen, als das dritte Stück Kuchen genauso schnell in Emis bodenlosen Magen verschwindet wie die vorherigen zwei."


$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
play ambient sfx_rain fadein 1.0

show bg suburb_shanghaiext_rn as bg2 behind rain onlayer master
hide bg onlayer master
hide rin onlayer master
hide emi onlayer master
with shorttimeskip

show bg suburb_shanghaiext_rn behind rain onlayer master
hide bg2 onlayer master
with None

"Trotz der Zeit, die vergangenen ist, regnet es noch immer, als wir das Shanghai verlassen, auch wenn es seither etwas nachgelassen zu haben scheint."


hi "Ich hoffe, du lässt dir davon nicht die Laune verhageln."


show rin basic_awayabsent_rn behind rain onlayer master at center
with charaenter

rin "Aber es hat doch geregnet."


show rin basic_awayabsent_rn onlayer master at tworight
show bg suburb_shanghaiext_rn onlayer master at bgright
with charamove

show emi basic_closedgrin_rn behind rain onlayer master at twoleft
with charaenter

"Aber Emi scheint das alles kaum etwas auszumachen."


emi "Ach, das passt schon! Wir hatten doch Spaß, oder? Ich bin richtig gut drauf."


show emi basic_grin_rn onlayer master
with charachange

emi "Es regnet doch auch gar nicht mehr so stark. Ich würde am liebsten zurück zur Schule laufen, um diese überschüssige Energie loszuwerden und etwas von dem Kuchen abzutrainieren."


"Sie dehnt ihre Arme und streckt ihren Rücken wie eine Katze. Nachdem sie ihre Schultern zweimal durchgerollt hat, lächelt sie fröhlich."


show emi sad_grin_rn onlayer master
with charachange

emi "Mann, ich kann mit diesen Beinen aber nicht wirklich rennen, schon gar nicht bergauf. Ich wünschte, ich hätte meine anderen mitgebracht."


"So beiläufig ausgesprochen klingt diese Bemerkung merkwürdig, aber ich schätze, Emi wechselt ihre Beine wie andere Leute ihre Schuhe."


show emi excited_proud_rn onlayer master
with charachange

emi "Wenn ich richtig schnell laufe, ist das ja vielleicht wie Rennen. Ich glaube, das mach ich."


show rin basic_absent_rn onlayer master
with charachange

hi "Da werde ich bergauf aber nicht mithalten können. Ich bin wirklich nicht in Form. Außerdem wirst du ohne den Schirm nass werden."


show emi basic_grin_rn onlayer master
show rin basic_awayabsent_rn onlayer master
with charachange

emi "Es ist jetzt kaum noch ein Nieseln. Die paar Tropfen werden schon nicht schaden. Ich glaube, ich werde sogar noch zur Laufbahn gehen, wenn ich meine Beine gewechselt habe."


"Emi hüpft aus dem Schutz meines Schirms heraus und geht mit schnellen Schritten voran. Plötzlich scheint sie sich an etwas zu erinnern, hält an und dreht sich um."


show emi excited_smile_rn onlayer master
with charachange

emi "Bis morgen!"


show emi excited_proud_rn onlayer master
with charachange

emi "Iss mit uns auf dem Dach zu Mittag! Ich mach genug für drei."


show emi invis onlayer master at offscreenleft
show rin basic_absent_rn onlayer master at center
show bg suburb_shanghaiext_rn onlayer master at center
with dissolvecharamove

hide emi onlayer master
with None

stop music fadeout 5.0

"Rin und ich können nur noch zusehen, wie sie uns winkt und dann wieder davonstürmt. Bald darauf verschwindet sie hinter einer Straßenecke. Ich werde nie verstehen, warum Emi es ständig so eilig hat, irgendwo hin zu kommen."


hi "Willst du, dass ich mit dir zur Schule zurücklaufe, damit wenigstens einer von euch nicht nass wird?"


show rin basic_deadpan_rn onlayer master
with charachange

rin "Wenn es dich glücklich macht."


"Es scheint, als wolle keiner von uns die angespannte Atmosphäre von unserem Streit vor ein paar Tagen im Kunstclub wieder aufleben lassen, was mich sehr erleichtert. Ich möchte niemandem etwas nachtragen, und bin froh, dass Rin das genauso sieht."


"Damit steht fest, dass wir vorerst mit der Gegenwart des jeweils anderen zufrieden sind und beginnen, in dieselbe Richtung zu laufen wie Emi – wenngleich auch mit bedeutend langsamerer Geschwindigkeit."


hide rin onlayer master
hide bg onlayer master
show ev rin_rain_away_close behind rain onlayer master:
    xalign 0.5 yalign 1.0 subpixel True
    acdc_warp 20.0 yalign 0.0
with whiteout
$ renpy.music.set_volume(0.7, 4.0, channel="ambient")

"Ich gehe etwas näher an Rin heran, obwohl der Schirm auch so schon groß genug ist, dass wir beide darunter Platz finden. Ich kann spüren, wie ihre Wärme einen Kontrast zu der kalten, regnerischen Umgebung bietet."


"Die Regentropfen, die auf den Schirm treffen, erzeugen ein markantes Geräusch und spielen die abgehackte Melodie des Regens."






"Mir wird klar, dass ich schon seit einer Ewigkeit nicht mehr draußen im Regen unterwegs war. Ich atme ein und nehme den Geruch des Regens und das Gefühl dieses Wetters mit all meinen Sinnen auf."


"Die Welt schmilzt im Regen zu einem verschwommenen Fleck."


"Die Farben des Himmels haben sich verdunkelt, von Grau zu einem dunklen Blau mit ein paar Rottönen, die von den Reflektionen des Sonnenlichts in den Wolken hinzugemischt werden."
"Der tief hängende Himmel sieht schön aus, als ob ich meine Hand ausstrecken und ihn berühren könnte."


$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

rin "Habe ich dir erzählt, wie sehr ich Regen mag? Es ist wie malen. Wenn es regnet, fühle ich mich zugehörig."


"Beinahe wie ein Echo meiner Gedanken äußert Rin einen der ihren. Er entgleitet ihrem Mund und umkreist uns sanft."


rin "Alles sieht so weich aus, als ob alle Umrisse einfach verschwunden wären. Ich mag das."


rin "Es ist, als ob mich der Regen in den Arm nehmen würde."


"Ihre Stimme klingt anders als sonst. Sanfter und weicher. Ich frage mich, ob es allein am Regen liegt oder auch an der Stimmung, in die der Regen das stille Künstlermädchen gebracht hat."


show ev rin_rain_away_close behind rain onlayer master at Position(xalign=0.5, yalign=0.0)
show ovl rin_rain_hisaotowards_close behind rain onlayer master at Position(xalign=1.0, yalign=0.0)
with charachange

"Durch ihre Worte spüre ich diese Stimmung auch verstärkt in mir selbst."


hi "Ja. Ich mag Regenwetter auch. Von Zeit zu Zeit ist es angenehm."


hi " Ich frage mich, was das Besondere an Regen ist."


show ev rin_rain_towards_close onlayer master at Position(xalign=0.5, yalign=0.0)
hide ovl onlayer master
with charachange

rin "Alles."


show ev rin_rain_towards onlayer master:
    xalign 0.5 yalign 0.5 zoom 1.05 subpixel True
    ease 5.0 zoom 1.0
with locationchange

$ renpy.music.set_volume(0.35, 6.0, channel="ambient")

"Eine Stille folgt dieser Aussage, da sie keine Fortsetzung erlaubt. Ich entscheide mich, der Richtung der Unterhaltung einen kleinen Stoß zu geben."


hi "Aber weißt du, wenn du es magst, dich zu etwas zugehörig zu fühlen, warum hast du dann für ein Problem damit, anderen deine Bilder zu zeigen?"


hi "Willst du nicht mit anderen Menschen verbunden sein?"


show ev rin_rain_away onlayer master at Position(zoom=1.0)
show ovl rin_rain_hisaotowards behind rain onlayer master at Position(xalign=1.0, yalign=0.0)
with charachange

rin "Das ist nicht dasselbe. Du vergleichst Äpfel und Tintenfische."


"Ich habe das Thema angesprochen, das Rin vermeiden wollte, und sie verschließt sich wieder. Die Frage bleibt für den Rest des Weges unbeantwortet zwischen uns, und ich frage mich, was ich hätte sagen können, um wirklich zu Rin durchzudringen."


"Fühlt sie sich, als würde ihr eine Identität fehlen?"


"Sie hat einen starken Charakter, aber wenn man mich dazu zwingen würde, ihn zu erklären, bin ich mir nicht sicher, ob ich es könnte."
"Sie scheint jemand zu sein, der in ständigem Konflikt mit sich selbst steht. Ich weiß nie, was mich erwartet, wenn ich mit ihr spreche."


"Ich frage mich, wie sie selbst diese Dissonanz erlebt."


"Wenn Rin sich jeden Tag selbst fragt, „Wer bin ich?” und Tag für Tag wie eine Besessene Bilder malt, um sich selbst zu definieren, was hält sie von dieser Art zu leben?"


hide ovl onlayer master
with charachange

"Die Ironie dabei ist, dass das genau dieselbe Frage ist, die ich mir die letzten vier oder fünf Monate gestellt habe. Ich habe mich dabei fürchterlich gefühlt. Ich kann nur annehmen, dass das für sie eine Art Normalzustand ist."


hide ev onlayer master
show bg school_dormext_full_rn behind rain onlayer master
show rin basic_awayabsent_close_rn behind rain onlayer master at center
with shorttimeskip

$ renpy.music.set_volume(0.7, 1.0, channel="ambient")

"Als wir vor den Wohnheimen anhalten, wendet Rin mir ihr Gesicht zu, als ob sie meine Gedanken spüren könnte. Ihr Blick wandert über meine linke Schulter in den formlosen Regen."


"Ihre dunklen Augen scheinen das schwache Licht der Umgebung einzusaugen, wie das Gegenteil eines Spiegels."


"Dieser leere Blick lässt nichts hinaus. Wenn ich verstehen will, was hinter diesen Augen vor sich geht, muss ich es selbst herausfinden."


"Rin öffnet ihren Mund, schließt ihn dann aber wieder, ohne etwas zu sagen. Die Stille dauert ein paar Momente an, bevor sie einen Schritt in Richtung Mädchenwohnheim macht."


show rin basic_absent_rn onlayer master
with charadistant

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

rin "Bis morgen."


stop ambient fadeout 0.5

scene black onlayer master
with dissolve


label de_R13:

scene bg school_dormhisao onlayer master
with dissolve

"Am nächsten Morgen habe ich – wie bis auf Weiteres jeden zweiten Montag – einen Termin bei Doc."


"Ich darf dafür Morgens einen Teil der ersten Stunde ausfallen lassen, und ich habe auch kein Problem damit, den Rest ebenfalls zu verpassen."


"Aber anstatt dankbar dafür zu sein, Geschichte zu verpassen, verspüre ich nur Grauen bei dem Gedanken an diese Termine."


scene bg school_dormbathroom onlayer master
show steam onlayer master
with locationchange

play ambient sfx_shower fadein 0.5

"Ich wache zur gewohnten Zeit auf und wasche mich in dem Bad, das ich mir mit Kenji teile."


"Nachdem ich mein zerzaustes Haar gebändigt habe, ziehe ich mir schnell etwas an und schmeiße meine Wäsche in den Korb."


stop ambient fadeout 0.5
hide steam onlayer master
scene bg school_dormhisao onlayer master
with locationchange

"Ich packe meine Sachen für den heutigen Unterricht. Meine Hausaufgaben sind wie immer bereits erledigt, und so habe ich jetzt etwas Freizeit."


"Da es keinen Sinn hat, sich 20 Minuten in den Unterricht zu setzen, bevor ich wieder zum Doc müsste, lege ich mich auf mein Bett und lese in einem Buch, bis es Zeit ist zu gehen."


scene black onlayer master
with dissolve
scene bg school_nurseoffice onlayer master
with locationskip

play sound sfx_doorknock2

"Ungewöhnlicherweise ist die Tür zu Docs Büro sperrangelweit offen."
"Ich betrete den Raum mit einem Klopfen, und nach einem musternden Blick über den Rand seines Computerbildschirms, gibt er mir mit einer Geste und einem freundlichen 'Hallo' zu verstehen, dass ich mich setzen soll."


"Auf seinem Schreibtisch steht eine dampfende Tasse Kaffee – vermutlich nicht seine erste heute."


play music music_nurse fadein 0.5
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

show nurse neutral onlayer master at center
with charaenter

nk "Na, wie geht es uns denn an diesem wundervollen Morgen, Hisao?"


hi "Mir geht es gut, denke ich. Als ich aufgewacht bin, hatte ich einen etwas schweren Kopf, aber das lag vermutlich daran, dass es gestern wegen des Regens etwas kalt war."


show nurse fabulous onlayer master
with charachange

nk "Du auch, was? Ziemlich viele Schüler wurden ohne Schirm vom Regen überrascht. Wir waren heute morgen die meiste Zeit über damit beschäftigt, Masken zu verteilen und Schnupfen zu kurieren."
nk "Hmm… also gut, Zeit für deinen Gesundheitscheck. Gib mir deinen Arm."


show nurse neutral_close onlayer master
with characlose

"Mit ausdruckslosem Gesicht strecke ich ihm meinen linken Arm entgegen. Doc legt mir mit einer geübten Bewegung einen Stauschlauch um den Bizeps und macht sich an seine Arbeit."


"Ich glaube nicht, dass es jemanden gibt, der Spritzen tatsächlich mag, aber zumindest habe ich meine Abneigung gegen sie überwunden. Mittlerweile zucke ich kaum noch, wenn es soweit ist."


"Sobald das erledigt ist, folgt eine Messung des Blutdrucks, und dann gibt es noch Checklisten und Fragebögen zum ausfüllen. Doc nickt und kritzelt meine Antworten in die entsprechenden Felder."



show nurse grin_close onlayer master
with charachange

nk "Okay. Dann lass und noch abhören."


show nurse neutral_close onlayer master
with charachange
play sound sfx_rustling

"Ich knöpfe mein Hemd auf und lege es sorgfältig über die Lehne meines Stuhls, während er sein Stethoskop anlegt."


"Ich kenne die Reihenfolge, in der er Herzschlag und Atmung abhören wird bereits in- und auswendig. Ich beginne, tief und gleichmäßig zu atmen, ohne extra darum gebeten worden zu sein. Es ist mittlerweile zur Routine geworden. Für uns beide."


"Es ist merkwürdig, dass dies die einzigen Momente im Leben sind, in denen man sich wirklich nur auf die Atmung und sonst nichts anderes konzentriert. Ich finde das irgendwie lustig."


"Doc nimmt das kalte Stahlstethoskop von meiner Brust, platziert es ein paar Zentimeter weiter unten und horcht erneut. Der Kontakt mit dem Metall lässt mich kurz zurückzucken, obwohl ich ihn bereits erwartet hatte."



show nurse concern_close onlayer master
with charachange

"Er runzelt die Stirn, aber ich kann nicht erkennen, ob es daran liegt, dass er unzufrieden ist, oder ob er versucht, etwas Bestimmtes aus dem unregelmäßigen Rhythmus meines Herzschlags herauszuhören."


hi "Stimmt etwas nicht?"


nk "Bitte nicht sprechen."


"Ich verstumme und werde nervös. Doc ist nett, aber ich kann mich mit diesen Zwangsuntersuchungen einfach nicht anfreunden. Vermutlich werde ich ein Trauma davontragen und in Zukunft Arzttermine aller Art hassen."


show nurse concern onlayer master
with charadistant

"Schließlich hebt er die runde Metallplatte von meiner Brust und gestattet mir, wieder zu sprechen."


show nurse grin onlayer master
with charachange

nk "Es scheint alles in Ordnung zu sein. Fühlst du dich selbst auch gut?"


hi "Ich denke schon. Ich war gestern draußen, als es geregnet hat, und ich habe mich heute morgen ehrlich gesagt nicht ganz fit gefühlt. Vielleicht habe ich mich erkältet."


show nurse fabulous onlayer master
with charachange

nk "Warst du mit Emi unterwegs? Sie hat sich auch was eingefangen. Meine Kollegen haben ihr gesagt, sie soll ein oder zwei Tage im Bett bleiben."


hi "Wirklich? Ich meine, ich war mit ihr zusammen, aber ich habe nicht gewusst, dass sie krank geworden ist."


"Ich schätze, es war wohl doch dumm von ihr, ohne Schirm durch den Regen zu rennen."


show nurse neutral onlayer master
with charachange

nk "Ja. Na ja, lassen wir das. Bei dir scheint jedenfalls alles in Ordnung zu sein, aber denk daran, vorsichtig zu sein."


hi "Natürlich. Ich will auf keinen Fall wieder zurück ins Krankenhaus."


"Etwas in meiner Stimme – vermutlich die unterdrückte Panik – erregt seine Aufmerksamkeit, und er blickt von den Unterlagen auf, in die er bis eben noch vertieft war."


show nurse fabulous onlayer master
with charachange

nk "Hey, keine Angst. So wie die Dinge gerade stehen, müsste sich dein Zustand schon massiv verschlechtern, damit du wieder eingewiesen werden müsstest."


"Seine Worte sind nicht gerade tröstlich, aber jetzt darüber zu diskutieren, würde auch nichts daran ändern. Ich verabschiede mich, ohne weiter darauf einzugehen."


stop music fadeout 7.0

scene bg school_nursehall onlayer master
with locationchange

"Auf meinem Weg durch den Korridor, der vom Neben- zum Hauptgebäude führt, kommt mir eine jungen Pflegerin entgegen. Sie lächelt mich im Vorbeigehen an."


scene bg school_lobby onlayer master
with locationchange

$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

"Die Eingangshalle ist menschenleer, was angesichts des laufenden Unterrichts auch nicht weiter überrascht."
"Ich höre gedämpft Stimmen von Diskussionen, die hinter den Türen der Klassenzimmer im ersten Stock hervordringen."


"Ich werfe einen Blick auf meine Uhr. Ich müsste mich beeilen, um noch rechtzeitig zu meinem Klassenzimmer zu kommen, und darüber hinaus habe ich auch keine Lust, zum Unterricht zu gehen."
"Ich entscheide mich, aufs Dach zu klettern und eine extralange Mittagspause zu machen."


"Emi hatte versprochen, sie würde heute etwas für mich mitbringen, aber wenn sie krank ist, dann kann ich mir das wohl abschminken. Ich habe sowieso keinen Hunger, es ist also auch egal."


play ambient sfx_rooftop fadein 0.5
$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

scene bg school_staircase1 onlayer master
with locationchange

"Der Aufstieg über die steile Treppe hinauf aufs Dach ist seltsam befreiend, beinahe als würde ich mit jedem Schritt leichter werden."
"Ich verspüre eine gewisse Befriedigung, dass mich der Aufstieg nicht mehr so viel Kraft kostet wie bei meinem ersten Besuch hier."


"Ich schiebe die quietschende Tür am Ende der Treppe auf und trete hinaus ins Sonnenlicht."


play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
scene bg school_roof onlayer master
with Fade(0.5, 0.1, 2.0, color="#FFF")

"Der Maschendrahtzaun erlaubt eine großartige Aussicht über die Baumwipfel, bis hin zu den grauen Schemen der Stadt in der Ferne."


scene bg misc_sky onlayer master:
    left
    subpixel True
    linear 40.0 right
with locationchange

"Das trübe Wetter von gestern kommt mir vor wie eine schlechte Erinnerung. Es wirkt beinahe so, als müsste ich bloß meinen Arm ausstrecken, um den silbrig blauen Himmel berühren zu können."


"Ich vergesse für einen Moment, dass ich eigentlich schlechte Laune habe. Die Wärme der Sonne dringt durch meine Kleider und macht mich stattdessen schläfrig und träge."


scene bg school_roof onlayer master
with shorttimeskip
play sound sfx_normalbell

"Die Klingel läutet zur Mittagspause und zerrt mich aus meinen Tagträumen zurück in die Realität."


"Kurz darauf erwacht der Hof unter mir zum Leben. Schüler strömen aus den Türen hinunter ins Erdgeschoss mit der Absicht, bei diesem Wetter ihr Mittagessen auf dem Schulhof oder im Garten zu genießen."


"Als ich höre, wie die Tür zum Treppenhaus geöffnet wird, bemühe ich mich erst gar nicht nachzusehen, wer es ist."


"Der Eindringling kommt mit ungleichmäßigen Schritten auf mich zu. Bei jedem Schritt hört man die kleinen Flusskiesel knirschen, die das Dach bedecken."


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg misc_sky onlayer master
with locationchange

"Die Schritte stoppen ein Stück von mir entfernt, und es wird still. Ich sehe nach oben in die glühende Sonne und genieße einen Augenblick ihre Wärme auf meiner Haut."


rin "Was machst du da?"


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_roof onlayer master
show rin basic_absent onlayer master
with locationchange

"Der Höflichkeit halber drehe ich mich um und erblicke ihre hagere, zerbrechlich wirkende Gestalt. Sie sieht genauso aus wie immer. Ihre Haare wirken vielleicht noch einen Tick zerzauster als sonst, beinahe so als wäre sie eben erst aufgestanden."


"Sie steht da, ihr Gewicht auf einen Fuß verlagert, und betrachtet mich neugierig, als sei ich ein Artikel in einem Schaufenster."


hi "Ich weiß nicht. Tagträumen, schätze ich."


hi "Und du?"


show rin basic_deadpan onlayer master
with charachange

rin "Emi hat Essen versprochen. Normalerweise essen wir hier."


hi "Ich fürchte, da wirst du enttäuscht werden. Ich habe gehört, Emi hätte sich erkältet."


show rin relaxed_nonchalant onlayer master
with charachange

rin "Oh. Ich schätze, das ergibt Sinn. Sie war nicht im Unterricht."


hi "Man fängt sich im Juni allerdings auch nicht gerade oft eine Erkältung ein. Glaubst du, sie ist wirklich in dem Regen noch zur Laufbahn gegangen? Es wollte doch gestern gar nicht mehr aufhören zu schütten."



show rin basic_deadpanupset onlayer master
with charachange

rin "Wahrscheinlich."


hi "Im Regen?"


rin "Im Regen."


"Das klingt etwas übertrieben, nur um nicht hinter den Trainingsplan zurückzufallen. Aber Emi ist ein Dickkopf, also kann ich mir vorstellen, wie sie durch den Regen rennt, weil sie „es musste.”"


hi "Na ja, sie hat es offensichtlich übertrieben. Das wird wohl auch der Grund sein, warum sie sich erkältet hat."


hi "Aber irgendwie ist es schon cool."


show rin relaxed_boredom onlayer master
with charachange

rin "Wo wir gerade davon sprechen, ich fühle mich auch nicht so gut. Ich…"


stop ambient

show rin relaxed_sleepy onlayer master
with vpunch

rin "HA-TSCHI!"


play music music_another fadein 4.0

"Rin gelingt es nicht rechtzeitig, ein heftiges Niesen zu unterdrücken."
"Sie beugt ihren Kopf in Richtung Schulter, um ihre Nase daran abzuwischen, aber da ich der Meinung bin, dass das nicht sonderlich damenhaft wäre, ziehe ich ein Taschentuch aus meiner Hose und halte es ihr an die Nase."


show rin relaxed_sleepy_close onlayer master
with characlose

hi "Hier. Gesundheit."


show rin relaxed_doubt_close onlayer master
with charachange

rin "Ganke."


"Sie putzt ihre Nase, und ich tupfe sie sanft ab, bis sie sauber ist."


"Ihre Nase ist wirklich süß. Sie scheint überhaupt der femininste Teil von Rins Gesicht zu sein. Ich spüre, wie meine Wangen leicht erröten, aber Rin bemerkt es nicht."


show rin basic_lucid_close onlayer master
with charachange

rin "Danke – ich glaube, ich hab mir auch was eingefangen. Wie ich schon sagte."


hi "Hoffentlich nicht."


show rin basic_awayabsent_close onlayer master
with charachange

"Rin scheint sich wegen des Essens keine Gedanken zu machen, also bleiben wir trotz des Mangels an Verzehrbarem auf dem Dach. Sie kommt zu mir herüber, stellt sich neben mich an den Zaun und blickt mit mir in die Ferne."


"Es hat auch nicht den Anschein, als ob jemand diese Ruhe stören würde. Es ist still und friedlich."


stop music fadeout 2.0
play ambient sfx_rooftop fadein 3.0

scene bg school_roof onlayer master
with shorttimeskip

"Was macht man in der Mittagspause, wenn nicht essen?"


"Wie sich herausstellt, hat weder sie noch ich auch nur den Hauch einer Ahnung. Glücklicherweise ist Nichtstun eine Aktivität, die sehr gut auch ohne Ahnung auskommt."


"Obwohl die Sekunden und Minuten vergehen, ohne dass wir sie mit Gesprächen oder anderen sinnlosen Dingen wie Wolken beobachten verbringen, schreitet die Zeit unerbittlich voran."


"Ich schaue immer wieder auf meine Uhr, bis ich merke, wie sinnlos das eigentlich ist und damit aufhöre. Stattdessen versuche ich so lange es geht auszuhalten, bevor ich wieder darauf schaue. Vielleicht schaffe ich es ja sechs oder sieben Minuten."


show rin basic_awayabsent_close onlayer master at center
with charaenter

"Rin blickt weiter träge und stillschweigend auf die azurblaue Fläche über uns."


"Ich frage mich, warum wir meistens kaum ein Wort miteinander sprechen. Sie meinte, dass sie es nicht mag zu sprechen, weil sie Schwierigkeiten damit hätte, sich selbst richtig auszudrücken."


"Was mich betrifft, glaube ich, dass ich mich daran gewöhnt habe, als ich im Krankenhaus viel Zeit ohne Gesprächspartner verbracht habe."


"Meistens empfinde ich diese ruhige Atmosphäre zwischen uns als angenehm, und selbst wenn mich das Gefühl überkommt, das Schweigen brechen zu müssen, ist es immer schwer, mit Rin ein passendes Thema zu finden."


"Wir liegen auf derart verschiedenen Wellenlängen, dass es keinen gemeinsamen Nenner zu geben scheint."


hi "Was magst du so sehr am Himmel?"


show rin basic_deadpannormal_close onlayer master
with charachange

"Sie dreht sich zu mir um. Ihre Augen sind ernst und klar."


show rin basic_deadpan_close onlayer master
with charachange

rin "Himmel ist das einzige, das perfekt ist."


show rin basic_awayabsent_close onlayer master
with charachange

rin "Ich weiß es. Wenn du so möchtest, könnte man sagen, ich bin eine Expertin für Himmel. Und das bin ich, selbst wenn du nicht möchtest. Eine Himmelexpertin."



rin "Er ist immer anders, aber immer perfekt, auch wenn er anders ist."


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg misc_sky onlayer master at Fullpan (8.0)
with locationchange

"Ich folge ihrem Blick auf die endlose blaue Fläche und denke über ihre Worte nach."


hi "Wolltest du jemals etwas anderes sein?"


rin "Der Himmel zu sein wäre gar nicht so schlecht."


hi "Nein, ich meine, jemand anderes, eine andere Person. Auf eine normale Schule zu gehen wie jeder andere auch, ohne sich um all das Sorgen machen zu müssen…"


rin "All was?"


"Für einen Moment versuche ich, die richtigen Worte zu finden, schaffe es aber nicht, einen Satz daraus zu formulieren, den ich guten Gewissens aussprechen könnte."


hi "Ich will es nicht wirklich laut aussprechen."


rin "Versuch's. Ich bin nicht so gut im Gedankenlesen."


stop ambient fadeout 0.5
scene bg school_roof onlayer master
show rin basic_awayabsent_close onlayer master
with locationchange

hi "Hast du dir noch nie gewünscht, nicht behindert zu sein?"


"Sie denkt darüber nach und schüttelt dann mit gerunzelter Stirn ihren Kopf."


show rin negative_annoyed_close onlayer master
with charachange

rin "Das ist eine schwere Frage. Ich weiß nicht, was ich sagen soll."


hi "Es ist okay, wenn du nichts sagst."


hi "Aus irgendeinem Grund bin ich gerade nur so unglaublich unzufrieden mit dem, was ich jetzt bin, dass ich mich dauernd solches Zeug frage. Es fällt mir schwer, es zuzugeben, aber so ist es nun mal."


"Ehrlich gesagt fühle ich mich erleichtert, es endlich jemandem gesagt zu haben, selbst wenn es bloß Rin ist."


show rin negative_confused_close onlayer master
with charachange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play music music_serene fadein 8.0

rin "Ich glaube, ich will anders sein manchmal. Ich habe in letzter Zeit viel darüber nachgedacht, mich zu verändern, aber es macht mir etwas Angst. Wie Rückwärtslaufen mit geschlossenen Augen."


show rin negative_worried_close onlayer master
with charachange

rin "Der schwierigste Teil ist es zu wissen, wo deine Zehen nicht hinzeigen. Richtungen meine ich."


show rin basic_sad_close onlayer master
with charachange

rin "Selbst wenn ich gar nichts tue, würde ich nie gleich blieben."


show rin negative_spaciness_close onlayer master
with charachange

rin "Es ist wie mit meinen alten Bildern. Sie sind anders als das, was ich jetzt male, weil ich anders bin, aber sie sind immer noch meine Bilder, also ist etwas gleich. Das ist wirklich seltsam."


show rin basic_lucid_close onlayer master
with charachange

rin "Ich bin jeden Tag anders, aber ich bin immer noch jeden Tag ich. Wer bin ich dann?"


hi "Ist das ein Rätsel?"


show rin basic_deadpanupset_close onlayer master
with charachange

rin "Wenn du willst, dass es eins ist. Ich weiß aber die richtige Antwort nicht, also musst du selbst eine finden."


hi "Na ja, es ist der Himmel, oder? So wie du ihn vorhin beschrieben hast."


show rin basic_surprised_close onlayer master
with charachange

"Ich schaffe es tatsächlich, sie mit meiner Antwort zu überraschen. Vielleicht hatte sie das schon wieder vergessen."


show rin basic_deadpansurprised_close onlayer master
with charachange

rin "Das stimmt! Aber ich dachte an mich selbst, als ich das sagte. Sehr seltsam."


show rin basic_lucid_close onlayer master
with charachange

rin "Kann es sein, dass ich eigentlich der Himmel bin?"


hi "Ich glaube nicht, dass das möglich ist. Irgendwo ist ein Fehler in deiner Logik."


show rin basic_awayabsent_close onlayer master
with charachange

"Sie blickt schweigend nach unten. Ich kann sehen, wie sie ihre Herleitung schnell noch einmal im Kopf überprüft, mit dem Ergebnis aber scheinbar nicht ganz zufrieden ist."


show rin basic_deadpanupset_close onlayer master
with charachange

rin "Ja, vielleicht bin ich nicht der Himmel. Würde Sinn ergeben. Es fällt mir schwer zu sagen, was für eine Art Mensch ich bin."


hi "Da bist du nicht die Einzige."


show rin negative_spaciness_close onlayer master
with charachange

rin "Es ist, als wäre mein Kopf woanders als der Rest von mir."


hi "Unter Wasser."


show rin basic_awayabsent_close onlayer master
with charachange

rin "Ja. Ich frage mich, wie er da hingekommen ist."


"Ich habe keine passende Antwort, daher breitet sich für einen kurzen Moment Stille zwischen uns aus. Ich lenke meinen Blick auf den Himmel über uns."


$ renpy.music.set_volume(0.5, 2.0, channel="music")

window hide

scene bg misc_sky onlayer master
with locationchange

nvl clear
nvl show dissolve

n "\nDas letzte Mal, dass ich dem Himmel irgendeine Beachtung geschenkt habe… Ich schätze, es muss im Krankenhaus gewesen sein. Durch das Fenster in meinem Zimmer konnte ich nur einen dünnen Streifen des Himmels sehen. Wenn ich zum Fenster ging und mein Gesicht gegen das kalte Glas presste, wurde der Streifen größer, wenn auch nicht viel."


n "Dieser Himmel lies mich meine Trauer und meine Einsamkeit spüren. Er war eine Erinnerung an die Welt jenseits der Scheibe. Ich frage mich, ob es jenseits des Himmels, den wir hier vom Schuldach aus sehen können, auch eine andere Welt gibt."


n "Ich kann nicht damit aufhören, mein Leben an dieser Schule mit meiner Zeit im Krankenhaus zu vergleichen, auch wenn ich das nicht sollte. Ich bin nicht mehr dort."


n "Der schmale Himmelsstreifen hinter dem Fenster meines Zimmers, die Gesichter der Ärzte, die Gesichter meiner Eltern. Die grauweißen Wände überall. Iwanakos Brief, der die Worte, die sie niemals aussprach, widerhallen ließ wie ein Echo. All das gehört nun der Vergangenheit an."


n "Ich wünschte, ich könnte alles, was bisher geschah, vergessen und die Zeit würde für immer stehenbleiben. Dann gäbe es nur mich, Rin, den Himmel und eine endlose Mittagspause auf dem Dach. Unveränderlich und für immer perfekt."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve

window show

hi "Ich bin mir nicht sicher, ob ich diese Schule mag oder ob ich sie hasse."


rin "Ich hätte auch auf eine normale Schule gehen können, wenn ich gewollt hätte, aber ich habe mich entschieden, hierher zu kommen."


scene bg school_roof onlayer master
show rin relaxed_nonchalant_close onlayer master at center
with locationchange

hi "Warum?"


show rin relaxed_doubt_close onlayer master
with charachange

rin "Ich habe einfach entschieden, dass ich es will. Ungefähr so wie Melonen oder Pflaumenmarmelade."


hi "Denkst du, es war eine gute Entscheidung?"


hi "Ich meine, es gibt viel Gutes an dieser Schule, aber es gibt auch ein paar schlechte Dinge."


show rin basic_lucid_close onlayer master
with charachange

rin "Ich weiß."


show rin basic_awayabsent_close onlayer master
with charachange

rin "Ich sammle Menschen, weil sie interessant sind. Die Menschen hier sind wirklich einmalig. Die meisten. Aber nicht alle."


show rin negative_angry_close onlayer master
with charachange

rin "Manche halten es nicht aus. Sie leiden zu sehr. Manchmal wird es richtig schlimm, weißt du? Das sind die, die wehtun."


show rin basic_deadpanupset_close onlayer master
with charachange

rin "Ich frage mich, ob du auch so bist? Ich hoffe nicht. Ich mag solche Sachen nicht."


hi "Hey, ich bin nicht deine Fallstudie. Und ich werde nicht aufgeben oder sterben oder so was."


hi "Jedenfalls meinte ich, dass dieser Ort zu weit von der realen Welt entfernt ist."


show rin basic_surprised_close onlayer master
with charachange

rin "Was ist die reale Welt?"


hi "Alles da draußen. Echte Menschen mit normalen Alltagsleben, die zueinander passen wie ein großes Puzzle."


show rin relaxed_surprised_close onlayer master
with charachange

rin "Du denkst, gehören nicht dazu? Zu den echten Menschen?"


hi "Vielleicht nicht. Na ja, eigentlich schon. Ich meine nur, dass es sich anfühlt, als seien wir Überreste."


show rin negative_annoyed_close onlayer master
with charachange

"Rin denkt eine Weile nach. Sie beißt sich leicht auf die Lippe und kneift ihre mandelförmigen Augen zusammen wie ein Kind."


show rin basic_deadpansurprised_close onlayer master
with charachange

rin "Ist es schwer, behindert zu sein?"


"Die Frage bringt ihr ein leises Lachen meinerseits ein."


hi "Sag du es mir. Du bist schon bedeutend länger dabei als ich."


show rin negative_annoyed_close onlayer master
with charachange

"Sie denkt noch eine Weile darüber nach."


show rin basic_deadpancontemplation_close onlayer master
with charachange

rin "Ich fühle mich nicht wirklich behindert. Ich meine, ich mache so ziemlich alles anders, aber es ist nicht sonderlich schwer. Ich kann immer üben."


show rin basic_deadpandelight_close onlayer master
with charachange

rin "Ich habe dieses Jahr damit begonnen, Essenssachen zu üben. Ich denke, eines Tages will ich lernen, in einer richtigen Küche zu kochen."


hi "Das ist bewundernswert, aber ich glaube nicht, dass es nur um eine geistige Haltung geht."


show rin basic_lucid_close onlayer master
with charachange

rin "Vielleicht nicht für dich."


"Mir fällt nichts Schlagfertiges darauf ein, also stimme ich schweigend zu. Die ganze Situation wird immer verwirrender für mich."


"Ich weiß, was ich will, aber nicht, wie ich es erreichen kann."
"Rin scheint zu glauben, sie könne sich einfach in die Form zwängen, die sie glaubt haben zu müssen, aber sie kann sich dabei nicht entscheiden, ob sie ein Vogel oder ein Schmetterling sein möchte."


show rin basic_awayabsent_close onlayer master
with charachange

rin "Ich glaube, im Endeffekt bin ich auch nicht wirklich glücklich damit, wer ich bin, aber das bedeutet nicht, dass es mir leid tut, zu sein wer ich bin."


show rin relaxed_nonchalant_close onlayer master
with charachange

stop music fadeout 0.5

rin "Das ist es, was mit dir nicht stimmt, Hisao."


play sound sfx_rustling

scene bg school_roof_blurred onlayer master
show rin basic_lucid_superclose onlayer master at center
with characlose

"Ich habe gerade damit begonnen, diese ziemlich direkte Bemerkung zu verarbeiten, als Rin mich plötzlich umarmt."


hi "Was tust du?"


"Ich bin noch nie von einem Mädchen ohne Arme umarmt worden."
"Ehrlich gesagt fühlt es sich nicht wirklich an wie eine Umarmung. Durch die unbeholfene Art, wie sie ihren Körper an mich presst, und das Fehlen von Armen, die sich um mich schlingen, fühlt es sich eher so an, als wäre sie auf mich gefallen."


"Aber die Wärme einer echten Umarmung ist geblieben, und an ihr erkenne ich auch, worum es sich handelt."


show rin basic_deadpannormal_superclose onlayer master
with charachange

play music music_comfort fadein 9.0

rin "Ich umarme dich, Hisao."


hi "Das weiß ich, aber…"


show rin relaxed_doubt_superclose onlayer master
with charachange

rin "Ist es verkehrt? Ich dachte, das macht man so."


show rin relaxed_sleepy_superclose onlayer master
with charachange

rin "Ich bin in so was nicht wirklich gut. Das erste Mal, als mich Emi umarmte, war ich überrascht und habe ihr in den Bauch getreten. Ich kann ziemlich fest zutreten, deswegen hat sie mich danach nicht mehr so oft umarmt."


hi "Es ist nicht verkehrt. Es ist nur… Nein, es liegt an mir… Zur Zeit ist alles ein wenig schwer für mich. Ich komme mir vor, als könne ich auf nichts angemessen reagieren."


show rin relaxed_surprised_superclose onlayer master
with charachange

rin "Wirklich? Es ist also doch schwer, behindert zu sein?"


"Ich schätze, jetzt hat sie mich. Mir fehlt die Kraft, etwas dagegen hervorzubringen, aber ich fühle mich, als müsste ich trotzdem etwas loswerden."


hi "Na ja, also… Nein, es ist nicht schwer. Ich glaube, ich mache mir einfach nur zu viele Gedanken."


hi "Ich wünschte mir nur, ich würde mich nicht dauernd selbst so bemitleiden."


"Ich frage mich, ob ich schon immer so zerbrechlich war oder ob ich nach meinem Zwischenfall so geworden bin. Meine Welt wurde bisher noch nie so erschüttert, also lässt es sich nicht genau sagen."


show rin basic_lucid_superclose onlayer master
with charachange

"Rin drückt ihre Wange fest an mich. Ich kann die Wärme ihres Körpers an meinem spüren."


"Ihre Körpertemperatur fühlt sich sehr hoch an – als ob sie das Sonnenlicht in sich absorbiert hätte und es nun mit mir teilen würde. Vielleicht ist es aber auch nur ein ganz normaler Zustand für sie."


"Es ist das Tröstlichste, das ich seit langer, langer Zeit gespürt habe."


show rin basic_deadpan_superclose onlayer master
with charachange

rin "Wow, dein Herzschlag klingt wirklich total seltsam. Wie ein betrunkenes Schlagzeugorchester."


hi "Bitte sag so was nicht. Sonst fühle ich mich sehr unwohl."


"In einem Versuch, die Spannung zu lösen, lache ich dennoch über ihren Kommentar. Es klingt ein wenig zu gezwungen."


hi "Oh Mann, tut mir leid, ich bin völlig neben der Spur."


show rin basic_deadpannormal_superclose onlayer master
with charachange

rin "Schon gut. Das ist das Beste an dir."


hi "Das zu hören, macht mich nicht gerade glücklich."


scene bg school_roof onlayer master
show rin basic_deadpannormal_close onlayer master at center
with charadistant

"Sie entlässt mich aus ihrer Umarmung und versucht, ihr Gleichgewicht wiederzufinden. Eine bedrückende Stille legt sich über uns; ich schäme mich über mich selbst, und Rin versucht, einen Gesichtsausdruck zu finden, der ihr gefällt."


$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene bg misc_sky onlayer master
with locationchange

"Ich werfe noch einen letzten Blick nach oben."


hi "Dieses Dach ist wirklich großartig. Es ist, als wäre man dem Himmel ein kleines Stückchen näher."


rin "Ich kenne noch einen besseren Ort, aber da können wir in der Mittagspause nicht hin. Ich kann dich mal mitnehmen, wenn du willst."


play sound sfx_warningbell

"Die Klingel läutet zum Beginn des Mittagsunterrichts, und Rin steht auf, um nach unten zu gehen. Ich eile ihr nicht hinterher, sondern entscheide mich, noch ein wenig länger hier oben zu bleiben."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_roof onlayer master
show rin basic_awayabsent onlayer master at center
with locationchange

hi "Danke für die Umarmung."


show rin basic_lucid onlayer master
with charachange

rin "Danke, dass du mich nicht getreten hast."


hide rin onlayer master
with charaexit

"Nachdem Rin verschwunden ist, lasse ich meinen Tränen endlich freien Lauf und weine zum ersten und letzten Mal in meinem Leben wegen meines Zustandes."


"Danach stoße ich die leere Hülle von dem Jungen auf dem Krankenhausbett von mir. Für immer."


stop music fadeout 2.0
scene black onlayer master
with dissolve


label de_R14:

scene bg school_scienceroom onlayer master
with locationchange

"Zwei Tage später fühle ich mich etwas weniger elend. Ich mache sogar einen langen Spaziergang, so wie Doc es mir empfohlen hat. Bisher habe ich das vermieden, indem ich allerlei Entschuldigungen vorgeschoben habe."


"Auch im Unterricht fühle ich mich aktiver, sehr zur Freude unseres Physik-/Klassenlehrers, Herr Mutou, den ich mit richtigen und schnell vorgetragenen Antworten beglücke."


"Die Pause zwischen den beiden Morgenstunden ist zu kurz, um irgendetwas Sinnvolles zu tun, aber zu lang, um sie damit zu verbringen, im Klassenzimmer zu sitzen und nichts zu machen."


play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3 onlayer master
show crowd onlayer master
with locationchange

"Auf den Gang zu gehen ist nicht viel besser, aber meine steifen Muskeln zu strecken, ist ein sinnvollerer Zeitvertreib, als sitzen zu bleiben und sie noch steifer werden zu lassen."


"Die Tür des benachbarten Klassenzimmers öffnet sich, und die heraustretenden Schüler aus Klasse 3-4 füllen den sowieso schon belebten Gang. Es scheint, als habe ihr Lehrer seinen Unterricht ein paar Minuten überzogen."


"Unter ihnen ist Emi. Sie sieht, dass ich sie gesehen habe, weshalb ich beinahe aus Reflex wegsehe."


play music music_emi fadein 0.5

show emi basic_closedgrin onlayer master at center
with charaenter

"Ich kann mich allerdings noch zurückhalten, und Emi lächelt mich fröhlich an, während sie an den anderen Schülern vorbei auf mich zu hüpft."


"Emi wirkt ziemlich energiegeladen und zeigt kein Anzeichen von Krankheit oder dergleichen. Es scheint, als habe sie sich von ihrer Erkältung wieder erholt."


show emi basic_happy onlayer master
with charachange

emi "Hey! Guten Morgen!"


hi "Schön, dich wieder auf den Beinen zu sehen. Geht es dir wieder besser?"


"Sie sieht auf jeden Fall so aus, aber ich verspüre dennoch den Drang nachzufragen."


show emi excited_laugh onlayer master
with charachange

emi "Danke! Und ja, tut es. Es war nur eine kleine Erkältung, nichts Ernstes."


"Emi lacht selbstbewusst, als wolle sie ihren Worten Nachdruck verleihen. Einen Moment lang frage ich mich, was nach Emis Maßstäben als ernst gelten würde."


"Sie scheint es aber eilig zu haben, das Thema zu wechseln."


show emi excited_happy onlayer master
with charachange

hi "Wohin gehst du?"


show emi basic_closedgrin onlayer master
with charachange

emi "Zu Rins Zimmer, um zu sehen, ob sie schon wach ist."


hi "Oh? Hat sie die erste Stunde geschwänzt?"


show emi sad_grin onlayer master
with charachange

"Ein schelmisches Lächeln erscheint auf Emis Gesicht. Sie wirkt etwas verlegen."


emi "Äh… nicht ganz. Es scheint, als hätte sie sich meine Erkältung eingefangen."


hi "Tut mir leid, das zu hören. Na ja, sie war schließlich am Sonntag auch mit uns draußen im Regen. Als ich sie am Montag gesehen habe, fühlte sie sich auch schon nicht richtig gesund."


show emi basic_grin onlayer master
with charachange

emi "Ja. Jedenfalls werde ich Doc nach etwas Medizin für sie fragen, wenn es ihr nicht bald besser geht."


stop music fadeout 3.0

hide emi onlayer master
with charaexit

"Sie macht sich auf den Weg zum Mädchenwohnheim. Ich will mitgehen, um Rin eine gute Besserung zu wünschen. Ich will ihr sagen, dass es mir nun auch besser geht, aber es fühlt sich nicht richtig an."


"Ein schwer zu deutendes Gefühl bringt mich davon ab. Aus irgendeinem Grund gelingt es mir nicht, die Entschlossenheit aufzubringen, ihr zu folgen. Ist es das, was Iwanako durchgemacht hat, als sie versuchte, mir ihre Gefühle zu gestehen?"


stop ambient fadeout 2.0

scene black onlayer master
with dissolve


label de_R15:

scene bg school_girlsdormhall onlayer master
with locationchange

"Obwohl ich mich etwas fitter fühle, zögere ich noch damit, zu Rin zu gehen, um mit ihr zu sprechen."


"Es dauert noch zwei Tage, bis ich endlich den Mut aufbringe, zum Mädchenwohnheim zu gehen. Dort frage ich die erste Person, die ich treffe, nach dem Weg zu Rins Zimmer."




play sound sfx_doorknock2

"Ich klopfe an Rins Tür und warte."


$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_rustling
$ renpy.music.set_volume(1.0, 10.0, channel="sound")

"Nach ein paar Sekunden der Stille höre ich etwas von hinter der Tür rascheln."
"Ich beginne mich zu fragen, ob ich ihr vielleicht etwas hätte mitbringen sollen. Ein warmer Kaffee oder ein paar Orangen. Ich hätte sie ihr schälen können, aber was soll's. Jetzt ist es zu spät."


"Die Tür öffnet sich leise – sie war nicht abgeschlossen – und plötzlich starre ich Rin an, die ihrerseits zurückstarrt."


"Sie sieht aus, als sei sie gerade aus dem Bett gekrochen. Ihre Haare sind ein einziges Chaos."


show rinpan basic_deadpanamused onlayer master at Slide(1.05,1.0,1.0,1.0,0.5)
with charaenter

"… und sie hat fast nichts an."


"…"


show rinpan basic_amused onlayer master at right
with charachange

rin "Hallooooo."


play music music_rin fadein 0.5

"Rins grinst mich merkwürdig dämlich an. Ich bin mir nicht ganz sicher weshalb."


"Rin lächelt so selten, dass es sowieso immer unpassend wirkt. Insbesondere jetzt, wenn man bedenkt, dass sie halb nackt vor mir steht. Aus genau diesem Grund frage ich mich gerade auch ernsthaft, ob es richtig war herzukommen."


"Ihre Wangen sind rosarot angelaufen, was in starkem Widerspruch zu ihrer sonst kreidebleichen Haut steht, die so wirkt, als bekäme sie nicht genug Sonnenlicht. Ihre Stirn ist schweißnass, als ob sie Fieber hätte."


hi "Ähm, hi."


show rinpan basic_absent onlayer master
with charachange

"Und was jetzt? Ich habe nicht über diesen Punkt hinaus nachgedacht, und Rin starrt mich wieder mit ihren erwartungsvollen Augen an."


"Irgendetwas an dieser Situation bereitet mir ein sehr komisches Gefühl. Ihre Augen sind noch abwesender als sonst, und es scheint ihr schwer zu fallen, sie auf etwas zu fokussieren."


"Der Mangel an Kleidung ist beunruhigend, aber da es sie selbst nicht zu stören scheint, sollte ich mir wohl auch keine Gedanken machen."


"Zumindest versuche ich mir das einzureden."


hi "Äh, ich dachte, ich besuche dich mal, weil du nicht im Kunstklub warst… und ich wollte mit dir reden und dir gute Besserung wünschen."


"Rin zeigt keine Anzeichen, dass sie meine Worte zur Kenntnis genommen hat, was für mich die Frage aufwirft, ob sie meine Worte verstanden oder überhaupt gehört hat."


"Vielleicht liegt es am Fieber; sie könnte geschlafen haben, bevor ich geklopft habe."


show rinpan basic_deadpan onlayer master
with charachange

rin "Okay."


show rinpan basic_deadpan onlayer master:
    easeout 0.5 alpha 0.0 xpos 1.05
with Pause(0.5)

hide rinpan onlayer master
with None

"Sie macht auf dem Absatz kehrt und gibt den Weg in ihr kleines Zimmer frei. Vom Gang aus kann ich sehen, wie sie zu ihrem Bett läuft und sich halb auf das zerwühlte Bettlaken setzt und halb darauf fällt."


"Die offene Tür erscheint mir plötzlich wie ein größeres Hindernis als es die geschlossene jemals war, aber da Rin nichts mehr sagt, schreite ich hindurch in ihr Zimmer."


scene bg school_dormrin onlayer master
with locationchange

"Rin sitzt an die Wand gelehnt auf ihrem Bett, wodurch der einzige Stuhl im Raum für mich bleibt."


"Sie bleibt still, auch nachdem ich mich gesetzt habe. Wollte sie mich vielleicht ins Zimmer bitten, hat aber vergessen, es laut zu sagen? Eine implizierte Einladung sozusagen?"


show rinpan basic_deadpanamused onlayer master at twoleft
with charaenter

rin "Sehr aufregend. Mich hat noch nie jemand besucht."


"Das Brechen des Schweigens lenkt meine Aufmerksamkeit vom Zimmer auf dessen Bewohnerin, die gerade in einem äußerst komplexen Gedankenprozess zu stecken scheint."







show rinpan basic_awayabsent onlayer master
with charachange

rin "Eigentlich war das nicht richtig. Das mit dem Besuchen. Aber Emi zählt nicht – auch wenn sie mich besucht."


show rinpan basic_deadpan onlayer master
with charachange

rin "Sie verhätschelt mich immer viel zu sehr. Ich glaube, das macht ihr zu viel Spaß."


show rinpan basic_absent onlayer master
with charachange

rin "Ich glaube, ich habe vergessen, wie man selbst einen BH anlegt."


"Sie wirft einen müden Blick auf ihre Brust."


show rinpan basic_surprised onlayer master
with charachange

rin "Jetzt, wo ich darüber nachdenke, ist das vermutlich der Grund dafür, warum ich keinen anhabe."


"Es ist mir auch nicht entgangen, dass Rin ihr Hemd nicht zugeknöpft hat, aber ich versuche, meine Augen nicht von den ihren abzuwenden."


"Es ist ziemlich offensichtlich, dass sie sich nicht sonderlich viele Gedanken über ihren Körper macht. Dafür macht sich mein Körper gerade umso mehr Gedanken über ihren."


show rinpan relaxed_sleepy onlayer master
with charachange

rin "Heute kam sie um halb Acht, um mich zu wecken!"


show rinpan relaxed_doubt onlayer master
with charachange

rin "Kannst du dir das vorstellen?"


"Sie hält für einen Moment inne und wirft einen Blick in mein dummes Gesicht."


show rinpan basic_lucid onlayer master
with charachange

rin "Wenn ich es mir genau überlege, kannst du das vermutlich sogar. Ist ja nicht so wie der umgekehrte Regenbogenfisch, den ich mir heute morgen versucht habe vorzustellen. Das war schwierig."


hi "Na ja, das scheint eine ziemlich normale Zeit zum aufstehen zu sein, wenn du morgens in die Schule willst."


"Ich versuche, so vernünftig wie möglich zu klingen, um Rins wirres Gerede zu kompensieren."


show rinpan basic_deadpanupset onlayer master
with charachange

rin "Hab ihr gesagt, dass sie sich verziehen soll."


show rinpan relaxed_nonchalant onlayer master
with charachange

rin "Sie hat mir diese Pillen gegeben und gesagt, dass ich sie nehmen soll."


"Ich folge ihrem Blick zum Nachttisch und von dort zu dem darauf stehenden Behälter."


show pills onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

"Ich hebe ihn auf und drehe ihn in meiner Hand, bis ich das Etikett gefunden habe."


"Wirkstoff… Codein?"


show pills onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills onlayer master
with None

hi "Hast du die alle genommen?"


show rinpan relaxed_surprised onlayer master
with charachange

rin "Nein. Ja. Ich habe nicht alle gegessen, weil es so viele waren. Aber jetzt fühle ich mich besser."


show rinpan relaxed_sleepy onlayer master
with charachange

rin "Ehrlich gesagt… fühle ich mich richtig gut."


"Sie beginnt, mit dem Kopf zu kreisen, als würde sie entweder versuchen, ihre Nackenmuskulatur zu dehnen, oder gleich ohnmächtig werden."


"Sie hat mehrere von diesen Pillen genommen? Ist das nicht gefährlich? Zumindest muss es ein paar Nebeneffekte haben… die ich gerade wohl zu sehen bekomme."


show rinpan basic_deadpanupset onlayer master
with charachange

rin "Mir geht es wunderbar… Ich fühle mich gut… aber jemand soll das Summen aus meinem Kopf holen. Ich kann nicht klar denken."


"Rins Blick ist wieder genervt."


show rinpan basic_upset onlayer master
with charachange

rin "Es ist wie ganz viele von diesen Insektendingern… oder ein richtig großes Insekt."


show rinpan basic_awayabsent onlayer master
with charachange

rin "Mit vielen Flügeln. Ganz viel Farbe und so."


show rinpan basic_absent onlayer master
with charachange

rin "Wie nennt man die?"


show rinpan basic_deadpanamused onlayer master
with charachange

rin "Ah, schon gut. Ich weiß es wieder. Es sind Schmetterlinge."


"Ihre letzte Beobachtung bringt sie ein wenig zum Lächeln. Die kleine Pause in ihrem Monolog ist nicht lang genug, als dass ich etwas sagen könnte, um die Diskussion eventuell noch zu retten."


show rinpan basic_amused onlayer master
with charachange

rin "Ich liebe Schmetterlinge. Die sind das beste Tier."


show rinpan basic_awayabsent onlayer master
with charachange

rin "Hast du auf deinem Weg hierher welche gesehen?"


show rinpan basic_deadpansurprised onlayer master
with charachange

rin "Hisao."


"Sie spricht meinen Namen aus, als hätte sie ihn beinahe vergessen – vielleicht um klar zu machen, dass sie jetzt mit mir redet, anstatt ihre Gedanken jedem kundzutun, der vielleicht gerade zuhören könnte."


"Angesichts dieser merkwürdigen Situation hat es mir dir Sprache mehr oder weniger schon verschlagen, als Rin das erste Mal den Mund aufmachte. Da sie scheinbar nichts mehr hinzuzufügen hat, macht sich die Stille in dem kleinen Raum breit."


"Ich lasse erneut meinen Blick durch den Raum schweifen, in der Hoffnung, etwas zu finden, worüber man noch sprechen könnte."


"Rins Zimmer ist in etwa so klein wie meines. Das große Fenster, das den Großteil der Wand gegenüber der Tür einnimmt, öffnet sich ebenfalls nach Osten."


"Es sieht sehr normal aus, was mir merkwürdig erscheint. Ich hatte mit etwas… anderem gerechnet."


"Etwa ein dutzend Bilder – die meisten davon gemalt in Rins abstrakten Stil – und ein paar Poster bedecken fast die gesamte Wand, aber das ist der einzige echte Unterschied zwischen ihrem Zimmer und meinem."


"Ich würde den Raum nicht gerade als ästhetisch bezeichnen, aber er entspricht auch nicht meinen Vorstellungen von einem Mädchenzimmer."


"Ein leichter Geruch von Kunst… von Farbe und Papier hängt in der Luft. Es ist derselbe Geruch wie im Kunstklub."


"Rin ist nicht gerade um Ordnung bemüht. All ihre Sachen scheinen in verschiedenen Haufen im Zimmer verteilt zu sein."


hi "Dein Zimmer ist hübsch."


"Es ist eine hohle Phrase, die man verwendet, um Lücken in Unterhaltungen zu füllen, aber meine Kreativität lässt mich gerade ziemlich im Stich."


show rinpan relaxed_nonchalant onlayer master
with charachange

rin "Ja. Willst du, dass ich dich herumführe?"


"Sie blickt fragend an ihren halboffenen Hemd herab, und ich folge unweigerlich ihrem Blick bis zu ihrer Brust."


show rinpan relaxed_sleepy onlayer master
with charachange

rin "Oh… Ich schätze, das habe ich bereits."


"Ich kann es nicht leugnen, ganz gleich wie sehr ich versuche, mich zu benehmen."


show rinpan basic_absent onlayer master
with charachange

rin "Es ist sehr nett, dass du gekommen bist, um mich zu sehen."


show rinpan basic_deadpancontemplation onlayer master
with charachange

rin "Das macht mich ganz… wie sagt man doch gleich… du weißt schon, das Ding mit dem Zeug."


show rinpan basic_lucid onlayer master
with charachange

rin "Egal, du bist gekommen."


"Rins Gebrabbel erinnert mich daran, dass ich eigentlich einen Grund hatte herzukommen."


hi "Hey, das, worüber wir am Montag geredet haben. Auf dem Dach, erinnerst du dich?"


stop music fadeout 4.0

show rinpan relaxed_surprised onlayer master
with charachange

rin "Hmmm?"


"Rin scheint gerade alles andere als aufmerksam zu sein. Nicht, dass sie das je wäre. Ich platze damit heraus und rede es mir von der Seele."


hi "Ich wollte dir einfach nur sagen, dass ich denke, dass es mir in Zukunft besser gehen wird."


hi "Ich hasse es, so jämmerlich zu sein, also habe ich mich entschlossen, es ab sofort bleiben zu lassen."


hi "Das war's eigentlich schon…"



show rinpan relaxed_sleepy onlayer master
with charachange

rin "Okay. Ist das nicht gut?"


"Die schwammigen Worte fließen langsam und unkontrollierbar von ihren Lippen."


show rinpan relaxed_nonchalant onlayer master
with charachange

rin "Ich freue mich für dich, denke ich. Das ist es, was ich denke."


show rinpan basic_deadpannormal onlayer master
with charachange

rin "Du solltest nicht die ganze Zeit so traurig schauen. Ich meine, traurig aussehen ist okay, wenn du nicht traurig bist, aber du siehst so aus, als ob du wirklich traurig wärst."


show rinpan basic_deadpan onlayer master
with charachange

rin "Das ist nicht gut."


show rinpan basic_awayabsent onlayer master
with charachange

play music music_rin fadein 0.5

rin "Gehst du zu einer Art Trainingscamp, wo sie aus Jungen Männer machen? Oder zur Selbstfindung in die Berge?"


hi "Nein, das wohl eher nicht."


show rinpan basic_absent onlayer master
with charachange

rin "Oh. Ich schätze mal, das ist auch okay."


"Die Sätze kommen aus ihrem Mund und vermutlich ihrem Gehirn, einer nach dem anderen, mit kleineren Pausen dazwischen, was nicht gerade zur Verständlichkeit ihres Kauderwelschs beiträgt."


show rinpan relaxed_doubt onlayer master
with charachange

rin "Ich dachte nur, dass es eine gute Idee wäre. Vielleicht ist es keine."


"Rin beendet einen weiteren Satz und behält damit das letzte Wort über sich selbst. Eine beeindruckende Vorstellung, die ich bloß als mentales Schattenboxen beschreiben kann."


hi "Wenn ich schon dabei bin, mich zum Affen zu machen, kann ich mich auch gleich bei dir für den Blödsinn entschuldigen, den ich letzte Woche zu dir gesagt habe."


hi "Es ist deine Entscheidung, was du später einmal machen willst."


show rinpan basic_absent onlayer master
with charachange

"Sie scheint meine Worte nicht zu registrieren, aber dann beginnt in ihren Augen ein Verständnis aufzuleuchten, und sie beginnt ihren Kopf umherschaukeln zu lassen, was so gut wie alles bedeuten könnte."


show rinpan basic_deadpancontemplation onlayer master
with charachange

rin "Schon okay."


show rinpan basic_lucid onlayer master
with charachange

rin "Ich hab bestimmt auch Blödsinn gesagt."


rin "Es ist nur manchmal etwas schwer, meine Gedanken da zu behalten, wo ich sie haben will."


show rinpan relaxed_nonchalant onlayer master
with charachange

rin "Sie sind nicht besonders klar, zumindest meistens."


rin "Nicht dass ich will, dass sie klar sind… Ich wünschte nur, sie wären in irgendeiner Form."


rin "Rund ist nicht schlecht. Aber ich brauche das konkreter."


show rinpan relaxed_boredom onlayer master
with charachange

rin "Meine Gedanken sind ziemlich durcheinander."


show rinpan relaxed_sleepy onlayer master
with charachange

rin "Durcheinander."


show rinpan invis onlayer master:
    ypos 1.1
with dissolvecharamove

play sound sfx_pillow

scene ev rin_high_frown onlayer master
with locationchange




"Sie wiederholt das Wort mit einem melancholischen Tonfall. Dann lässt sie sich auf ihr Bett fallen, drückt ihren Kopf gegen ihr Kissen und schließt ihre Augen. "


rin "Genug. Müde. Du solltest gehen. Ich leg mich wieder hin."


scene ev rin_high_oneeye onlayer master
with locationchange

"Sie öffnet eines ihrer Augen, um mich anzusehen."





rin "Warst du es, der gerne schlafende Mädchen anschaut? Oder jemand anderes?"


rin "Vielleicht gab es auch mehrere von der Sorte."


scene ev rin_high_frown onlayer master
with locationchange

rin "Ich weiß nicht mehr."





rin "Du kannst dableiben, wenn du willst."


hi "Nein nein, ich gehe. Ich muss sowieso noch… meine Hausaufgaben erledigen."


stop music fadeout 2.0




scene bg school_dormrin onlayer master
with locationchange

"Ich stehe von meinem Stuhl auf und mache einen Schritt in Richtung Tür."


rin "Warte."


"Ihrer Aufforderung nachkommend bleibe ich stehen. Nicht, dass ich vorhatte, sofort abzuhauen."


scene ev rin_high_grin onlayer master
with locationchange






"Ich schaue über meine Schulter zu dem Mädchen, das wieder mit dem seltsamsten Lächeln auf ihrem Bett liegt."


"Sie sollte öfter lächeln."


rin "Ich kann dich zur Tür bringen."


scene ev rin_high_grinwide onlayer master
with locationchange




rin "Das ist das Mindeste, was man als Gentleman tun kann."





scene ev rin_high_smile onlayer master
with locationchange

"Rin kichert wie ein kleines Kind, was mir den letzten Zweifel daran nimmt, dass sie viel zu viel von ihrer Erkältungsmedizin genommen hat."


rin "Das wollte ich schon immer mal sagen."


scene bg school_dormrin onlayer master
with locationchange

show rinpan invis onlayer master:
    twoleft
    ypos 1.1    
with None

show rinpan basic_deadpandelight onlayer master at twoleft
with dissolvecharamove

"Langsam und mühsam setzt sich Rin im Bett auf. Mit noch mehr Mühe und noch langsamer steht sie schließlich ganz auf."


"Wie von einem männlichen Automatismus geleitet, senkt sich mein Blick sofort auf die Kurven ihrer Oberschenkel und die gestreiften Höschen. An diesem Punkt zwingen mich meine Manieren jedoch, wieder zu Rins Augen aufzusehen."


"Sogar das ist beinahe schon zu schwierig."


"Rin steht – wenn auch sehr wackelig. Es scheint, als habe sie abermals Schwierigkeiten, ihre sonst ordentliche Balance zu halten. Vermutlich eine Nebenwirkung des Medikaments."


show rinpan basic_deadpandelight onlayer master:
    ease 1.0 center
with None

show rinpan basic_deadpandelight_close onlayer master:
    twoleft
    ease 1.0 center
with Dissolve(1.0)

"Sie macht einen unsicheren Schritt in meine Richtung, dann noch einen kleineren, als sie bemerkt, dass es keine gute Idee ist, große Schritte zu machen."


"Ich spüre, wie sich meine Muskeln anspannen, als ich mich darauf vorbereite, sie aufzufangen, sollte sie stürzen."


play music music_twinkle fadein 3.0

scene ev rin_kiss onlayer master:
    center
    yalign 0.0 zoom 4.0 subpixel True
    easein 0.4 zoom 1.05
    easein 5.0 zoom 1.0
with flash

"Es gelingt ihr noch, zwei weitere Schritte zu machen, bevor sie gegen mich fällt."
"Zu meiner Überraschung hindern sie jedoch weder die Abwärtsbewegung noch der leichte Größenunterschied zwischen uns daran, ihre herzförmigen Lippen gegen meine zu pressen."


"Als sich unsere Lippen nach einem verwirrenden Moment, der nach nichts schmeckte außer… Rin, wieder trennen, blicke ich auf sie herab und suche nach einer Erklärung für das, was gerade geschehen ist."


$ renpy.music.set_volume(0.7, 2.0, channel="music")

scene bg school_dormrin onlayer master
show rinpan basic_deadpandelight_close onlayer master at center
with locationchange

"Das euphorische Grinsen eines Wahnsinnigen macht sich auf Rins Lippen breit und—"


show rinpan relaxed_sleepy_close onlayer master
with charachange

rin "Ich frage mich, ob ich mich daran morgen noch erinnern werde."


"Ich habe nicht die leiseste Ahnung, was ich antworten soll."


show rinpan relaxed_sleepy_close onlayer master:
    ease 1.0 twoleft
with None

show rinpan relaxed_sleepy onlayer master:
    center
    ease 1.0 twoleft
with Dissolve(1.0)

"Rin trennt unsere Körper voneinander, indem sie einen Schritt rückwärts macht, was mich erst realisieren lässt, dass sie überhaupt in Berührung standen."


show rinpan invis onlayer master:
    ypos 1.1
with dissolvecharamove

play sound sfx_pillow

"Der zweite Schritt ist eigentlich ein Sturz, glücklicherweise direkt auf ihr Bett."


"Der sanfte Aufprall von Rins dünnem Körper auf der Matratze durchbricht die Stille."


scene ev rin_high_open onlayer master
with locationchange

"Ich bewege mich schnell an ihre Seite, um zu sehen, ob sie sich verletzt hat, nur um von einem friedlich verträumten Gesicht begrüßt zu werden."


"Rin schläft."


"Sie liegt quer im Bett. Irgendwie hat sie es geschafft, im Stehen einzuschlafen und so zu fallen, dass sie sich dabei nicht verletzt hat."



"Wie sagt man? „Kinder und Betrunkene haben immer ihren Schutzengel dabei.”"


scene ev rin_high_sleep onlayer master
with locationchange

"Ich decke Rin so gut ich kann zu."


"Obwohl ich nicht sonderlich stark bin, fühlt sie sich sehr leicht an."


show ev rin_high_sleep onlayer master:
    subpixel True xalign 1.0 yalign 0.0
    ease 10.0 zoom 1.1
with None

"Ich stehe auf und sehe ihr rundes Gesicht, die dunklen, geschlossenen Wimpern auf ihren fiebrigen Wangen, der schlanke Körper, bedeckt von bleichen Tüchern."


"Rin schläft."


"Ein Konflikt – nein. Konflikte, Plural, brennen in mir. Ich denke darüber nach, Doc zu rufen, damit er ein Auge auf sie hat, entscheide mich dann aber dagegen."
"Nachdem ich noch einen Blick auf ihr friedliches Gesicht geworfen habe, beschließe ich, dass sie in Ordnung ist."


"Die restlichen Pillen nehme ich aber mit."


stop music fadeout 5.0

scene bg school_girlsdormhall onlayer master
with locationchange

"Ich verlasse das Zimmer und schließe leise die Tür hinter mir."


"Ich atme tief durch. Erst jetzt wird mir klar, dass ich für die letzte Minute den Atem angehalten habe. Ich brauche einen Moment, um mich und mein rasendes Herz zu beruhigen."


$ suppress_window_after_timeskip = True

scene black onlayer master
with dissolve


label de_R16:

window hide None

scene black onlayer master
with dissolve

play music music_pearly fadein 1.0

scene bg school_dormhisao onlayer master
with openeye

window show

"Gestern Abend fiel es mir schwer einzuschlafen, daher habe ich heute Morgen einen außerordentlich schweren Kopf. Ich überlege mir kurz, ob ich den Unterricht schwänzen soll, erinnere mich dann aber, dass ich ja von jetzt an stärker sein wollte."


scene bg school_courtyard onlayer master
with locationskip

"Ich steige brav auf, ziehe meine Uniform an und mache mich dann ohne zu frühstücken auf den Weg zum Hauptgebäude."


scene bg school_scienceroom onlayer master
with locationskip

"Ich sitze auf meinem Platz in Raum 3-3, winke wie jeden Morgen Misha und Shizune zum Gruß zu und lasse den Tag über mich ergehen."


with shorttimeskip

"Der Nachmittagsunterricht ist immer länger als die Morgenstunden. Daran ändert sich nichts, egal ob ich in Minuten zähle, oder in Kritzeleien in meinem Notizbuch."


"Heute bin ich besonders abgelenkt, weil ich immer wieder an Rin denken muss."


$ renpy.music.set_volume(0.5, 0.5, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\n\n\nHabe ich es geschafft, ihr richtig zu sagen, dass ich mich bessern möchte? Hat sie ein Wort von dem verstanden, was ich sagen wollte?"


n "Ich denke nach über den Kuss und dessen eventuelle Bedeutung. Sie war völlig neben der Spur, vielleicht bedeutet es gar nichts. Aber wir sind uns in letzter Zeit nähergekommen. Was bedeutet das alles?"


n "\n\n\nIch denke in letzter Zeit immer mehr über Rin nach. Ich frage mich, ob sie auch an mich denkt."


$ renpy.music.set_volume(1.0, 4.0, channel="music")
play sound sfx_normalbell
nvl clear
nvl hide dissolve
window show

"Das Klingeln der Glocke lässt mich zusammenzucken, und ich merke, dass ich die Hälfte der Stunde über nicht aufgepasst habe."


"Ich betrachte das Einzige, was ich in der letzten Stunde zustande gebracht habe: Eine Ansammlung von Skizzen, die am Rand meines Notizbuches entlanglaufen."


"Etwas enttäuscht von mir selbst packe ich meine Sachen und gehe hinaus in den Gang."


stop sound fadeout 0.5
$ renpy.music.set_volume(0.0, 1.0, channel="music")
scene bg school_hallway3 onlayer master
show rin basic_absent onlayer master at center
with locationchange

"Rin steht genau vor der Tür. Bei ihrem Anblick bleibe ich wie angewurzelt stehen."


"Ihre Haltung ist wie immer entspannt, aber ich fühle mich plötzlich, als hätte ich ein Brecheisen verschluckt. Es fällt mir schwer, ihr in die Augen zu sehen."


"Sie scheint keinerlei Schwierigkeiten zu haben, mich anzusehen, aber diese dunklen Augen bringen mich aus irgendeinem Grund völlig durcheinander."


"Es ist schwer, sie direkt anzusehen, also wende ich mich etwas zur Seite."


"Ich weiß nicht, was man in so einer Situation sagt."


"Andererseits weiß ich fast nie, was ich zu Rin sagen soll – völlig unabhängig von der Situation."


$ renpy.music.set_volume(1.0, 8.0, channel="music")

hi "Äh… hi."


show rin basic_deadpan onlayer master
with charachange

rin "Hallo."


"Ich versuche, die Unsicherheit in meiner Stimme zu unterdrücken und ganz normal zu sprechen. Plötzlich mache ich mir Gedanken darum, was ich mit meinen Hände tun soll. Aus irgendeinem Grund fühlt es sich an, als wären sie im Weg "


hi "Wie geht es dir? Du warst gestern ziemlich KO."


show rin basic_awayabsent onlayer master
with charachange

rin "Alles okay. Was meinst du mit gestern?"


hi "Du erinnerst dich nicht?"


show rin relaxed_disgust onlayer master
with charachange

"Sie neigt ihren Kopf auf die Seite wie ein Vogel und sieht etwas verwirrt aus."


rin "Erinnern woran? Ich hab ein ziemlich schlechtes Gedächtnis."


hi "An Gestern…"


show rin relaxed_surprised onlayer master
with charachange

rin "Was ist mit Gestern?"


hi "Ich bin vorbeigekommen, um nach dir zu sehen…"


show rin relaxed_nonchalant onlayer master
with charachange

rin "Ich kann mich nicht erinnern, dass so etwas passiert ist."


"Erinnert sie sich wirklich nicht? Ich weiß nicht, ob das gut oder schlecht ist, aber ich fühle mich nichtsdestotrotz enttäuscht."


show rin basic_lucid onlayer master
with charachange

rin "Ich erinnere mich aber, dass ich dir versprochen habe, dir einen Ort zu zeigen. Ist das wirklich passiert?"


show rin basic_awayabsent onlayer master
with charachange

rin "Vielleicht glaube ich auch nur, dass ich mich daran erinnere und tue es eigentlich gar nicht."


hi "Nein, das ist auch passiert."


show rin basic_absent onlayer master
with charachange

rin "Okay. Willst du hin?"


hi "Jetzt?"


show rin basic_deadpannormal onlayer master
with charachange

rin "Ja."


hi "Na ja, klar, warum nicht. Ist es weit?"


show rin basic_deadpan onlayer master
with charachange

rin "Ist es nicht."


$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
$ renpy.music.set_volume(0.8, 0.5, channel="music")
play ambient sfx_parkambience fadein 0.5

scene bg school_courtyard onlayer master
with locationskip

"Wir gehen zusammen die Treppen hinunter und dann nach draußen. Ein gewöhnlicher Sommertag mit surrenden Zikaden und allem, was dazu gehört. Es ist unglaublich heiß, und ohne die Klimaanlage der Klassenzimmer beginne ich sofort zu schwitzen."


scene bg school_gardens onlayer master
with locationchange

"Wir begeben uns auf den von Bäumen gesäumten Weg, der zu den Wohnheimen führt."


"Die Kirschbäume spenden Schatten, und das Sonnenlicht schimmert durch die Lücken im Blattwerk. Das Licht erzeugt ein chaotisches Muster, gesprenkelt mit hellen Stellen, wo die Strahlen auf den Asphalt treffen."


"Rins Augen schweifen in alle Richtungen, außer in meine. Allmählich glaube ich, dass es sich dabei um Absicht handelt."


$ renpy.music.set_volume(0.7, 0.5, channel="ambient")
$ renpy.music.set_volume(0.6, 0.5, channel="music")

scene bg school_forest1 onlayer master
with locationskip

"Sie führt mich erneut zu dem Tor hinter der Schule, dann hindurch und in den Wald dahinter."
"Wie schon beim letzten Mal fühlt es sich so an, als würde uns der Wald mit seinen niedrigen Temperaturen und verringerter Sonneneinstrahlung verschlingen wie eine fleischfressende Pflanze."


scene bg school_forest2 onlayer master
with locationchange

"Wir gehen bergauf, denselben verschlungenen Pfad entlang wie letztes Mal. Er windet sich um Bäume und Steine, Wurzeln und Felsen, vorbei an wucherndem Dickicht. Von irgendwoher hört man Vögel singen. Solisten für die summende Musik der Baumwipfel."


scene bg school_forestclearing onlayer master
with locationchange

"Wir gehen vorbei an der kleinen Lichtung mit dem großen Ahornbaum, der jetzt Sorgenbaum heißt. Der Weg wird erst steiler und flacht dann wieder ab."


scene bg school_forest2 onlayer master
with locationchange

"Ich muss ein paar Mal anhalten, um wieder zu Atem zu kommen und im Anschluss Rin nacheilen, die nicht anhält, um auf mich zu warten."


"Kurz darauf bin ich erneut atemlos."


$ renpy.music.set_volume(1.0, 0.5, channel="ambient")
$ renpy.music.set_volume(0.4, 0.5, channel="music")

scene bg school_hilltop_border onlayer master
with locationchange

"Plötzlich enden die Bäume und wir treten aus dem Wald. Die Grenze der Dickichts ist scharf und abrupt, als würde sie entlang einer unsichtbaren Linie verlaufen."


"Der Hügel steigt weiter vorne noch etwas an, aber von hier an bis zur Spitze ist es eine felsige Wiese mit einzelnen Grasbüscheln und Sträuchern, die so aussehen, als würden sie direkt aus den Steinen wachsen."


$ renpy.music.set_volume(1.5, 0.5, channel="ambient")
stop music fadeout 2.0
$ renpy.music.set_volume(1.0, 10.0, channel="music")

scene bg school_hilltop_spring onlayer master at Fullpan(15.0)
with locationchange

"Wir erreichen bald den höchsten Punkt, mit dem Wald im Rücken und einer Aussicht in alle Richtungen vor uns."


"Die Stadt liegt weit entfernt in der Stille des Nachmittags."


"Von hier aus hat man eine ziemlich gute Aussicht, und die Umgebung ist wundervoll. Ich frage mich, wie hoch wir sind."


"Ich atme die frische Luft ein und spüre, wie sich mein Herzschlag langsam wieder beruhigt. Ich glaube, ich habe es ein wenig übertrieben. Ein erhöhter Puls ist gefährlich für mich. Im Moment fühle ich mich jedoch gut."


"Der Wind frischt auf, fährt mir durch die Haare und bringt die Bäume unter uns in Schwingung. Das Gras wiegt sich im Wind, als die Brise über den Gipfel des Hügels fegt."


"Die Sonne scheint vom blauen Himmel, mit ein paar Wölkchen, die ihre Schatten ins Tal werfen. Die drückende Hitze von vorhin ist jetzt eine angenehme Wärme."


"Ich sehe mich genauer um. Die Kuppe des Hügels besitzt eine Schönheit, wie sie in der Natur oft vorkommt: Ungeplante Harmonie in der natürlichen Anordnung der Dinge."


"Am auffälligsten ist die Fülle an kleinen gelben Blumen. Sie sind buchstäblich überall auf der kleinen Wiese verteilt. Ich kann kann es mir nicht verkneifen, meine Begeisterung zu teilen."


hi "Wow. So viele Blumen."


show bg school_hilltop_spring onlayer master at right
show rin basic_absent onlayer master at center
with charaenter

rin "Ja. Kennst du die Sorte? Die werden wegfliegen."


hi "Ja. Löwenzahn."


show rin basic_awayabsent onlayer master
with charachange

rin "In der Schule gibt es nicht viele von denen, weil das Gras so oft geschnitten wird. Hier oben schneidet keiner das Gras."


"Die zerbrechlich aussehenden Blumen werden bald weiß und flauschig wie Baumwolle werden, und der Wind wird ihre Saat davontragen."


$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

scene ev dandelion onlayer master:
    yalign 0.5 xalign 0.5 zoom 0.8 subpixel True
    ease 20.0 zoom 0.9
with locationchange

"Ich bücke mich, um mir eine der kleinen, gelben Blumen genauer anzusehen, die sich still im Sonnenlicht baden. Bisher zeigt sie noch keine Anzeichen von Verfärbung. Sie wartet also noch darauf, sich zu verwirklichen."


"Ich fahre mit meinen Fingern über die zarten, gelben Blätter, fühle ihre weiche Oberfläche an meinen Fingerspitzen. Aus irgendeinem Grund macht es mich wehmütig. Ich höre, wie sich Rin von hinten nähert, stehe wieder auf und wende mich ihr zu."


stop ambient fadeout 3.0

scene bg school_hilltop_spring onlayer master at left
show rin basic_sad onlayer master at center
with locationchange

"Sie hat einen seltsamen Gesichtsausdruck."


hi "Stimmt etwas nicht?"


show rin basic_upset onlayer master
with charachange

rin "Ich weiß nicht. Es ist bloß…"


play music music_rin fadein 0.5

rinbabble "Du siehst nur immer so traurig aus und lässt dich leicht aus der Bahn werfen und es verwirrt mich und ich erinnere mich wirklich an nichts mehr von gestern außer dass du in mein Zimmer gekommen bist und dass deshalb ich der Grund dafür sein könnte und wenn ich der Grund war dann weiß ich glaube ich wieso, es ist weil Menschen nicht wirklich gerne mit mir sprechen und du könntest genauso sein und das wäre traurig ich kenne Leute und ich meine auch andere als Emi manchmal sagen dass ich seltsam bin und komisches Zeug rede also dachte ich ich könnte versuchen kein komisches Zeug zu sagen aber dadurch denke ich noch mehr und neue und komische und bunte Sachen das war kein gutes Wort aber vielleicht verstehst du es ja trotzdem und seltsame Sachen also wenn ich etwas sagen möchte weiß ich nicht wirklich wie und dann stimmen die Worte nicht mit den Gedanken überein weil etwas auf dem Weg schief geht aber es ist auch nicht so dass die Gedanken wirklich das sind was ich sagen sollte es ist mehr wie die Idee der Gedanken oder das Gefühl der Idee oder die Idee des Gefühls aber eigentlich ist es gar nichts davon weil es kein Wort dafür gibt solange ich kein neues erfinde was nicht wirklich hilfreich ist deshalb dachte ich ob es vielleicht besser ist Sachen zu machen als zu sagen weil ich gestern diese Pillen genommen habe und mich etwas komisch gefühlt habe und ich könnte etwas getan haben das ich nicht hätte tun sollen und davon abgesehen weiß ich nicht ob es besser gewesen wäre wenn ich den Gedanken hätte aussprechen können es gibt keine Telepathie die echte Telepathie ist nicht wahr ich glaube es wäre schrecklich und gleichzeitig nützlich aber jetzt würde es mir nichts ausmachen, weil Missverständnisse so einfach sind, aber Verstehen nicht und ich dachte—"


stop music
play sound sfx_pillow
with vpunch

"Ich greife sie an den Schultern und drücke fest zu, um sie zu unterbrechen. Ich habe nicht die Kapazität, um das alles auf einmal aufzunehmen."


$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

show rin basic_surprised onlayer master
with charachange

"Rin ist auf der Stelle still."


hi "Tief durchatmen."


hi "Ich bin dir nicht böse. Warum sollte ich? Ich bin nur etwas verwirrt, aber das ist schon okay."


"Ich frage mich, ob ich wieder ein Gesicht gemacht habe, das ihr nicht gefällt. Ich schätze, ich habe viel über gestern nachgedacht. Vielleicht sehe ich komisch aus. Ich wünschte, ich hätte immer einen Spiegel dabei."


hi "Du musst nicht alles auf einmal sagen. Ich höre auch zu, wenn du langsamer sprichst."


show rin basic_deadpanupset onlayer master
with charachange

rin "Es kam einfach aus mir heraus. Tut mir leid. Es ist alles wieder in Ordnung. Ich wollte bloß etwas sagen, nur nicht so viel."


play music music_innocence fadein 10.0

show rin negative_worried onlayer master
with charachange

rin "Es ist komisch, nicht wahr?"


"Sie sieht mich mit einer erstaunlich schüchternen Miene an, die ich bisher noch nie gesehen habe. Ich kann nicht anders, als etwas zu lachen."


hi "Ja, es ist komisch."


hi "Du bist ein ziemlich seltsamer Mensch, aber daran ist nichts verkehrt."


hi "Danke, dass du dir Gedanken um mich gemacht hast, aber ich werde mich bessern. Ich habe es dir gestern schon gesagt, aber ich schätze, daran erinnerst du dich auch nicht mehr."


show rin relaxed_nonchalant onlayer master
with charachange

rin "Tue ich nicht. Ich frage mich, was ich noch alles vergessen habe. Hoffentlich nichts Wichtiges wie meinen Namen. Das wäre schlimm."


hi "Na ja, du hast mich geküsst."


show rin relaxed_surprised onlayer master
with charachange

rin "Habe ich?"


hi "Ja, hast du. Auf die Lippen."


"Ich versuche, diese Worte wie nebenbei zu sagen, aber ich befürchte, dass ich wieder rot werden könnte."


show rin relaxed_doubt onlayer master
with charachange

rin "Hast du mich getreten?"


hi "Nein! Warum sollte ich das tun?"


show rin basic_deadpancontemplation onlayer master
with charachange

rin "Dann ist alles in Ordnung, nicht wahr? Es ist okay, stimmt's? Ich habe meinen Namen nicht vergessen."


hi "Ja, es ist alles in Ordnung."


"Ich wünschte, ich wäre wortgewandter und hätte eine schlagfertigere Antwort darauf, aber mir fällt nichts ein. Glücklicherweise hat Rin noch mehr zu sagen. Irgendwie fühle ich mich dadurch erleichtert."


show rin negative_confused onlayer master
with charachange

rin "Ich glaube, ich sollte mich entschuldigen. Ich kann wirklich schlecht mit Menschen umgehen."


show rin negative_spaciness onlayer master
with charachange

rin "Manche Dinge sind schwer zu verstehen – wie Quallen. Verstehst du Quallen?"


hi "Ich… ich glaube nicht."


show rin negative_sad onlayer master
with charachange

rin "Menschen sind für mich wie Quallen. Ich verstehe nichts."


"Jetzt ist es an ihr, ein Gesicht zu machen, das ich nicht wirklich gerne sehe."


show rin basic_sad onlayer master
with charachange

label de_choiceR16:

menu:
    with menueffect
    rin "Ich hatte nie wirklich Freunde."
    "Was ist mit mir?":




        return m1
    "Was ist mit Emi?":


        return m2

label de_R16a:

hi "Nee. Ich bin doch schon mal dein Freund."


hi "Ich meine, denk doch darüber nach. Wir reden schon viel miteinander, und wir haben uns gestritten und uns wieder versöhnt."


hi "Das nennt man Freundschaft."


label de_R16b:

hi "Was ist mit Emi?"


show rin basic_surprised onlayer master
with charachange

"Sie hält einen Moment inne, als müsste sie unerwartete Denkleistungen vollbringen."


show rin basic_awayabsent onlayer master
with charachange

rin "Emi… kümmert sich um mich. Ich weiß eigentlich gar nicht warum."


show rin negative_annoyed onlayer master
with charachange

rin "Aber mit ihr kann ich nicht wirklich reden. Nicht so. Es ist, als wäre ihr Kopf aus Seifenschaum und Marshmallows. Oder vielleicht liegt es auch an mir. Aber ich mag sie."


hi "Sie ist richtig nett, nicht wahr?"


show rin basic_absent onlayer master
with charachange

rin "Ja."


hi "Ich möchte auch dein Freund sein."


hi "Ich höre dir zu, wenn du reden willst. Wenn nicht, kann ich einfach still neben dir sitzen."


hi "Und ich möchte dir auch erzählen, was ich denke."


hi "Wir sollten definitiv Freunde werden."



label de_R16c:

show rin basic_deadpanamused onlayer master
with charachange

rin "Es ist wirklich nett von dir, das zu sagen."


show rin basic_awayabsent onlayer master
with charachange

rin "Ich konnte Pinseln und Farben und Leinwänden immer alles erzählen. Sie sind meine besten Freunde."


show rin basic_lucid onlayer master
with charachange

rin "Mit Menschen ist das schwerer. Ich muss Worte benutzen. Das fällt mir schwer."


hi "Ja, ich weiß, du hast es mir gesagt. Wie du immer vergisst."


show rin basic_absent onlayer master
with charachange

"Rin nickt mir wortlos zu, und ich wage es, ihr ein aufmunterndes Lächeln zu zeigen. Ich hoffe, ich mache es richtig. Sie zeigt keinerlei Reaktion."


"Ich bin wirklich froh. Die Distanz, die Rin zwischen sich und alles andere bringt, hat mich verunsichert, seit ich sie das erste Mal getroffen habe. Wenn wir echte Freunde werden, bin ich mir sicher, sie besser verstehen zu können."


"Ich bin mir sicher, dass wir auf diesem Weg die Kluft zwischen uns überwinden können."


show rin basic_awayabsent onlayer master
with charachange

"Rin bekommt von meinen Gedanken nichts mit. Sie scheint tief in Gedanken zu sein und wandert zwischen den gelben Blumen umher, die die grasbewachsene Kuppe des Hügels bedecken. Das macht nichts."


$ renpy.music.set_volume(0.4, 2.0, channel="music")
play ambient sfx_parkambience fadein 7.0

scene bg school_hilltop_spring_ss onlayer master at left
with shorttimeskip

"Die Zeit vergeht. Der Wind lässt das hohe Gras sanft schwanken. Rin summt ein kleines Lied vor sich hin, so leise, dass ich nicht erkennen kann, welches es ist – wenn es überhaupt irgendeines ist."


"Eine stärkere Böe zieht über die Kuppe, und das Geräusch der Bäume im Wind begräbt das Lied unter sich."


"Ich schaue auf meine Uhr, mehr aus Gewohnheit als sonst irgendwas. Es ist jetzt 16:30 am Samstag."


show rin basic_awayabsent_ss onlayer master at center
with charaenter

"Rin blickt zum Horizont mit ihrem merkwürdigen, leeren Blick, als ob sie überhaupt nichts ansehen würde. Ihre Pupillen sind dunkel und ruhig wie ein paar tiefe, stille Tümpel."


$ renpy.music.set_volume(0.7, 6.0, channel="music")


label de_R16d:

hi "Ich denke, ich werde aus dem Kunstklub austreten. Es wurde mir klar, als wir letzte Woche unseren Streit hatten."


hi "Es ist gut, dass ich es versucht habe, aber es ist einfach nicht mein Ding, verstehst du? Ich hatte mehr Spaß daran, dich besser kennenzulernen, als tatsächlich irgendetwas Künstlerisches zu machen."


hi "Aber ich will dein Freund bleiben. Wäre das in Ordnung?"


show rin basic_deadpan_ss onlayer master
with charachange

rin "Klar. Es wurde sowieso langsam ziemlich unheimlich, wie du mich die ganze Zeit angestarrt hast."


"Ihr Kommentar macht mich augenblicklich nervös, aber ich schaffe es zu antworten."


hi "Das tut mir leid."


show rin basic_deadpandelight_ss onlayer master
with charachange

rin "Schon okay, ich bin daran gewöhnt. Du bist nicht der Erste, der mir gerne beim Malen zusieht."


show rin basic_absent_ss onlayer master
with charachange

rin "Wirst du was anderes machen?"


hi "Ich weiß nicht. Wahrscheinlich nicht."



label de_R16e:

show rin relaxed_doubt_ss onlayer master
with charachange

rin "Es wird dir bald besser gehen, oder?"


hi "Klar."


show rin relaxed_nonchalant_ss onlayer master
with charachange

rin "Weißt du, ich glaube, mir auch. Ich werde mit dieser Freundin von Herrn Nomiya reden und sie bitten, meine Sachen bei sich auszustellen. Ich werde hart arbeiten, um das alles zu schaffen."


show rin basic_lucid_ss onlayer master
with charachange

rin "Ich habe das gerade entschieden, weißt du? Aber ich glaube, ich wusste es schon die ganze Zeit."


show rin basic_deadpannormal_ss onlayer master
with charachange

rin "Ich hatte dieses Gefühl jetzt schon eine lange Zeit, dass ich mich verändern werde. Selbst wenn ich es hasse und ich es nicht will, selbst wenn ich es wollte, ich würde mich verändern."


show rin basic_deadpanupset_ss onlayer master
with charachange

rin "Als wäre ich so, wie ich jetzt bin, noch nicht genug. Ich denke, das ist ein guter Weg, es zu tun. Er ist wie eine gerade Linie."


show rin basic_deadpancontemplation_ss onlayer master
with charachange

rin "Als hätte ich alles in meinem Leben nur dafür gelernt. Es ist nur Kunst, und es ist das einzige, womit ich mich wirklich auskenne. Ich weiß, was ich tun werde, also ist es gut. Ich habe überhaupt keine Angst."


show rin basic_deadpansurprised_ss onlayer master
with charachange

rin "Ich fühle mich wie immer. Ist das seltsam?"


hi "Nein. Überhaupt nicht."


stop ambient fadeout 2.0
$ renpy.music.set_volume(1.4, 4.0, channel="music")

window hide

scene black onlayer master
with shuteye

window show

"Ich schließe meine Augen und gebe dem unwiderstehlichen Gefühl nach, das die gesamte Woche über immer stärker wurde."


"Ich treibe aufwärts, an die Oberfläche meines eigenen Lebens."


"Der Druck, unter Wasser zu sein, verschwindet langsam, und das schwerelose Gefühl wird stärker."


"Ich durchbreche die Wasseroberfläche, erhebe meinen Kopf in das Sonnenlicht und atme tief ein, als wäre es das erste Mal in einer langen, langen Zeit."


scene bg school_hilltop_spring_ss onlayer master at left
show rin basic_deadpandelight_close_ss onlayer master at center
with openeye

"Meine Lungen füllen sich mit Sauerstoff, und ich öffne meine Augen und sehe Rins friedliches, entschlossenes Gesicht."


stop music fadeout 10.0
$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_hilltop_border_ss onlayer master
with shorttimeskip

"Wir laufen langsam und vorsichtig den Hang hinunter, um einen Sturz zu vermeiden, Rin an der Spitze und ich ein paar Schritte hinterher."


"Rin kann das mit Sicherheit. Selbst wenn nicht, wird sie einen Weg finden."


"Ich bin mir sicher, dass ich meinen Kopf von jetzt an auch über Wasser halten kann."


"Die Sonne geht in unserem Rücken unter und taucht die Welt in ein orangenes Flammenmeer."


"Ich schaue weiter auf den Hinterkopf des rothaarigen Mädchens, das ein paar Schritte vor mir den Weg entlang schreitet."


"Wenn es nur das ist… Diese Entfernung zwischen uns ist definitiv in meiner Reichweite."


window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
