label de_H3:

window hide None

scene black onlayer master
with dissolve

$ renpy.music.set_volume(0.0, 0.0, channel="ambient")
play sound sfx_alarmclock

with Pause(1.2)

play sound sfx_impact2

window show

"Mein Wecker kreischt mir in die Ohren, nur um schnell von meiner Faust zum Schweigen gebracht zu werden."


scene bg school_dormhisao onlayer master
with openeye

"Mein Körper wechselt in den Autopiloten und schleppt mein unterbewusstes Selbst aus dem Bett und in meine Uniform."


"Wie immer stehen meine Pillenfläschchen geduldig auf meinem Schreibtisch und warten darauf, dass ich sie nehme und meine tägliche Dosis an Medizin heraussuche; siebzehn Pillen am Tag."


scene bg school_scienceroom onlayer master at bgright
with locationskip

"Bevor ich mich versehe, öffne ich die Tür zu Klasse 3-3 und bin froh zu sehen, dass ich nicht der Einzige bin, der anscheinend von der Festwoche ein bisschen verkatert ist."


"Jedes Gesicht im Klassenzimmer sieht ausgemergelt aus. Jetzt, wo das Fest vorbei ist, wirkt es so, als hätte jeder seine Lebensziele erreicht."


"Ohne etwas zu haben, für das es sich zu leben lohnt, haben sich die Schüler darauf verlassen, dass ihre Instinkte allein sie zum Unterricht führen."


"Oder vielleicht interpretiere ich auch zu viel hinein."


"Langsam begebe ich mich zu meinem Stuhl, und erst dann merke ich, warum es im Zimmer so ruhig ist."


"Die Stühle neben meinem sind herrlich unbesetzt; die lauteste Gebärdendolmetscherin der Welt ist noch nicht da."


play sound sfx_doorslam
play music music_running

show misha hips_grin onlayer master:
    yalign 1.0 xanchor 0.0 xpos 1.0
    easein 0.3 xanchor 1.0
with vpunch

"Gerade als ich mich hinsetzen will, fliegt die Tür auf und bringt eine strahlende Misha zum Vorschein – mit vom dramatischen Auftritt noch auf und ab wippenden Haarlocken und in den Himmel gestreckten Armen."


show misha hips_laugh onlayer master at right
with charachange

mi "Ju-huuu~! Es ist alles vorbei!"


"Anscheinend sind nicht alle von der Depression nach dem Fest betroffen."


"Der Rest der Klasse funkelt sie böse an und denkt sich offenbar dasselbe wie ich."


show misha sign_confused onlayer master
with charachange

"Immer noch starr im Eingang stehend und die Arme immer noch in der Luft, sieht sie nervös in die Runde."


"Es ist offensichtlich, dass sie die miese Stimmung spürt, aber nicht ganz weiß, was sie tun soll."


show misha sign_confused onlayer master at center
with ease_decel

"Plötzlich fällt sie ruckartig nach vorne."


show misha perky_sad onlayer master
with charachange

mi "Hey!"


show shizu invis behind misha onlayer master:
    yalign 1.0 xanchor 0.5 xpos 1.0
with None

show misha perky_sad onlayer master at twoleft
show bg school_scienceroom onlayer master at center
show shizu adjust_happy onlayer master at tworight
with dissolvecharamove

"Als sie in das Klassenzimmer stolpert, gibt sie den Blick auf Shizune frei, deren Arm immer noch ausgestreckt ist, nachdem sie Misha geschubst hat."


show shizu basic_normal onlayer master
with charachange

shi "…"


hi "Danke für die Belustigung, aber solltet ihr Zwei euch nicht setzen?"


show shizu behind_frown onlayer master
with charachange

shi "…"


"Immer noch leicht peinlich berührt, braucht Misha ein paar Sekunden, um zu begreifen, dass sie übersetzen muss."


show misha sign_smile onlayer master
with charachange

mi "Oh! Ja! Shicchan sagt, sie ist nicht gerade glücklich darüber, dass du uns letzte Woche sitzengelassen hast."


show misha cross_frown onlayer master
with charachange

mi "Wir waren sehr beschäftigt!"


hi "Ach ja? Was ist mit allem, was ich schon für euch getan habe?"


show shizu cross_angry onlayer master
with charachange

shi "…"


show misha hips_grin onlayer master
with charachange

mi "Sie sagt, das zählt nur für Mitglieder des Schülerrats. Da du abgelehnt hast, schuldet sie dir nichts."


show misha hips_grin_close onlayer master
with characlose

"Misha beugt sich näher zu mir und flüstert mir verschwörerisch ins Ohr."


mi "Eigentlich glaube ich, dass sie nur ein bisschen sauer ist, weil du nicht den Tag mit ihr verbracht hast."


show misha hips_smile_close onlayer master
with charachange

mi "Für deine Arbeit letzte Woche ist sie dir aber wirklich dankbar."


show shizu behind_frustrated onlayer master
with charachange

"Shizune spürt, dass über sie gesprochen wird, und klopft mit ihren Fingern leicht auf den Tisch, bis Misha sich zu ihr umdreht."


show misha sign_smile onlayer master
with charadistant

show shizu basic_angry onlayer master
with charachange

show misha hips_grin onlayer master
with charachange

show shizu adjust_blush onlayer master
with charachange

"Von der schnellen Gebärdensprache kann ich nichts verstehen, aber durch Shizunes leicht beschämten Gesichtsausdruck und Mishas schlecht kontrolliertes Lachen kann ich es mir vorstellen."


stop music fadeout 8.0

"Während die beiden sich unterhalten, öffnet sich die Tür erneut, aber dieses Mal in einer viel angemesseneren Geschwindigkeit."


show hanako invis onlayer master at offscreenright
with None

show bg school_scienceroom onlayer master at bgleft
show shizu basic_normal onlayer master at Transform(xpos=0.42)
show misha hips_smile onlayer master at Transform(xpos=0.18)
show hanako emb_downtimid onlayer master at right
with dissolvecharamove

"Hanako betritt leise den Raum und zieht die Tür hinter sich zu."


show hanako emb_timid onlayer master
with charachange

"Sie lugt unter ihrem Haar hervor und sieht sich schnell im Klassenzimmer um."


"Unsere Augen treffen sich und sie erstarrt plötzlich. Sie schließt ihre Augen, atmet tief durch und geht dann herüber zu meinem Tisch."


show hanako cover_distant onlayer master
with charachange

ha "G-Guten Morgen Hisao."


hi "Morgen Hanako. Du bist ein bisschen spät, was?"


show hanako basic_normal onlayer master
with charachange

ha "Ich… hab mit Lilly gesprochen."


show hanako basic_worry onlayer master
with charachange

ha "Ü-über heute."


hi "Ah, du hast also ihre Liste bekommen? In dem Fall können wir ja direkt nach dem Unterricht los."


show hanako emb_smile onlayer master
with charachange

ha "S-Sicher."


hi "Ich freu mich drauf."


"Hanako zeigt mir kurz ihr verlegenes Lächeln und geht dann flugs zu ihrem Platz."


scene bg school_scienceroom onlayer master at bgright
with shorttimeskip

play music music_normal fadein 3.0

"Während des Unterrichts wird klar, dass nicht nur die Schüler von dem Fest ein bisschen niedergeschlagen sind."


"Mutou gibt uns einfach eine Liste mit Aufgaben aus dem Lehrbuch und setzt sich dann hinter seinen Schreibtisch."


"Für einen Moment vergesse ich die kurze Mittagspause, so langweilig ist der Tag."


play sound sfx_normalbell

"Er ist einschläfernd, und jeder wirkt überrascht, als die Glocke zum Ende des Unterrichts läutet."


show shizu basic_normal onlayer master at tworight
show misha perky_smile onlayer master at twoleft
with charaenter

"Als ich meine Taschen zusammenpacke, flankieren mich Shizune und Misha und setzen mich fest."


show misha hips_grin onlayer master
with charachange

mi "Sag mal, Hicchan, es ist immer noch nicht zu spät, um beizutreten. Nach dem Fest gibt es jede Menge Papierkram für uns zu erledigen…"


hi "Äh, tut mir leid Misha. Ich… hab schon was vor…"


show hanako invis onlayer master at offscreenright
with None

show bg school_scienceroom onlayer master at center
show shizu basic_normal onlayer master at Transform(xpos=0.42)
show misha hips_grin onlayer master at Transform(xpos=0.18)
show hanako cover_distant onlayer master at right
with dissolvecharamove

"Als ob sie das Stichwort gehört hätte, taucht Hanako mit einer kleinen Tasche hinter mir auf und versucht, Augenkontakt mit der Außenwelt zu vermeiden."


show misha cross_laugh onlayer master
with charachange

"Mishas Augen werden groß, dann lacht sie los."


mi "BWAHAHA! Du bist aber schnell, was Hicchan~? Wir werden dein Date nicht länger stören! Bwahahaha!"


show shizu behind_blank onlayer master
with charachange

"Hinter der grölenden Misha sehe ich, wie Shizune viel zu wenig Interesse an dem Ganzen zeigt. Vielleicht fasse ich das falsch auf, aber ich glaube, sie ignoriert mich absichtlich."


show hanako emb_downtimid_close onlayer master
with characlose

"Ich spüre ein sanftes Zupfen an meinem Hemd, drehe mich um und sehe, wie Hanako starr auf den Boden blickt."


show hanako emb_timid_close onlayer master
with charachange

ha "L-Lass uns…"


hi "Klar. Shizune, Misha, bis später."


hi "Und ich bin immer noch nicht am Schülerrat interessiert."


show misha cross_grin onlayer master
with charachange

mi "Spielverderber."


stop music fadeout 2.0

hide misha onlayer master
hide shizu onlayer master
with charaexit

show bg school_scienceroom onlayer master at bgleft
show hanako emb_timid_close onlayer master at center
with charamove

"Misha und Shizune ziehen sich auf den Gang zurück und unterhalten sich vergnügt in Gebärdensprache."


hi "Hast du alles? Lass uns losgehen."


play music music_soothing fadein 4.0

scene bg school_gate onlayer master
with locationskip

"Eine Flut aus Schülern strömt aus den Schultoren und auf die Straße zum Dorf."


"Es ist ein bisschen komisch. Es ist fast der gleiche Anblick wie bei jeder anderen Oberschule, aber die Illusion lässt wegen des einen oder anderen Rollstuhls oder einer fehlenden Gliedmaße nach."


"Mir fällt aber auf, dass niemand allein ist."


scene bg school_road onlayer master
with locationchange

show hanako emb_downsad_close onlayer master at center
with charaenter

"Und als Hanako und ich durch die Tore gehen, merke ich, dass sie dichter neben mir läuft."


"Nicht so nah, dass man es als „eng” bezeichnen könnte, aber sie hält auch nicht ihren üblichen Sicherheitsabstand."


"Ich schätze, wir sind noch nicht vertraut genug, als dass sie mir so nahe kommen würde, wie sie es bei Lilly tut."


"Aber auch wenn sie mir physisch nur ein kleines Stück nähergekommen ist, scheint sie mental einen weiten Weg zurückgelegt zu haben."


"Sie umklammert die Lederriemen ihrer Tasche so stark, dass ihre Knöchel weiß werden. Ihren Kopf hält sie gesenkt und ihren Mund fest geschlossen."


"Sie wirkt fast so, als würde man sie zum ersten Mal zum Büro des Direktors bringen."


"Bei dem Gedanken versuche ich, ein Kichern zu unterdrücken, aber es ist zwecklos."


show hanako emb_timid_close onlayer master
with charachange

ha "W-Was ist los…?"


"Ich schätze, es hat keinen Sinn, es zu verschweigen…"


hi "Tut mir leid. Für einen Moment hat es so gewirkt, als würdest du Ärger bekommen."


show hanako defarms_strain_close onlayer master
with charachange

ha "W-W-Was meinst du?"


hi "Ich glaube, du solltest dich ein bisschen entspannen. Wir gehen nicht allzu weit weg, und es sind nur Schüler in der Nähe, stimmt's?"


show hanako def_worry_close onlayer master
with charachange

ha "S-Stimmt."


"Ich bin ein bisschen beunruhigt darüber zu sehen, dass Hanako so aufgeregt ist."


hi "Und du machst das jede Woche, richtig?"


show hanako basic_worry_close onlayer master
with charachange

ha "J-Ja. Mit Lilly."


"Natürlich. „Mit Lilly.” Ich frage mich, ob sie die Schule jemals ohne sie verlassen hat?"


"Auf den ersten Blick wirkt es nicht so schlimm, aber Hanako ist in erheblichem Maß von Lilly abhängig."


"Wenn sie nicht einmal damit zurechtkommt, die Schule ohne sie zu verlassen, wie hätte sie dann überlebt, wenn sich die zwei nie getroffen hätten?"


"Hätte sie jemand anderen gefunden, an den sie sich hängen kann? Und was hat sie zu Lilly gezogen?"


"War es ihre fehlende Sehkraft, oder war Lilly einfach nur so nett, ihr zu helfen?"


"Ich frage mich, ob irgendjemand anderes geeignet gewesen wäre."


hi "Na ja, ich bin da. Außerdem gehen wir nicht weit. Es ist vorbei, bevor du es merkst."


show hanako emb_downsmile_close onlayer master
with charachange

"Hanakos Knöchel nehmen langsam wieder Farbe an, als sie versucht, ein kleines Lächeln zu verstecken, aber diese Anstrengung scheint ein weiteres Gespräch zu verhindern."


"Wir laufen Seite an Seite entlang der sich schlängelnden Straße in Richtung Dorf. Die Schülermenge lichtet sich, als wir den Gehweg entlanggehen."


"Schnellere Schüler gehen voraus und die weniger mobilen fallen zurück, sodass sich die Menschenmenge nach und nach auflöst."


scene bg suburb_konbiniext onlayer master
with locationskip

"Als wir den Mini-Markt erreichen, sind wir so gut wie allein."


scene bg suburb_konbiniint onlayer master
with locationchange

"Hanako benutzt mich als Schild zwischen sich und dem Angestellten, während sie durch die engen Gänge geht und eine Auswahl an Artikeln in ihren Korb legt."


"Brot, Milch, Tee… Thymian?"


"Was für ein Mini-Markt verkauft Kräuter?"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve

n "\n\nAndererseits scheint an diesem Dorf nichts normal zu sein – was rückblickend vielleicht gar nicht so schlecht ist."


n "Alles ist so anders und unangenehm… Es ist sicher nicht gut, sich zu viele Gedanken darüber zu machen."


n "Wenn ich darüber nachdenke, erinnert mich das an Hanako."


n "Egal wie sehr man es versucht, man kann ihren Narben nicht entkommen; sie unterbrechen meinen Gedankengang immer noch, wenn ich sie sehe."


n "So sehr ich es auch nicht einsehen möchte, ich glaube, ich zwinge mich dazu, sie nicht zu beachten."


n "Nicht, dass ich selbst ohne Narben wäre. Die gezackte Linie auf meinem Brustbein wird nie komplett verschwinden."


n "Ich habe nur den Vorteil, sie leicht verstecken zu können."


n "\nAber gewissermaßen erinnern mich unsere Narben daran, dass wir alle nicht ohne Grund an diesem Ort sind."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

window show

"…"


"Hanako wirft einen letzten Gegenstand in ihren Korb und hält ihn mir dann, zusammen mit ein paar Geldscheinen, schüchtern hin."


show hanako emb_downtimid_close onlayer master at center
with charaenter

ha "K-K-Könntest du b-bitte…"


"Ich brauche einen Moment, um zu verstehen, was sie mir sagen will."


hi "Oh, du willst, dass ich bezahle?"


show hanako emb_downsad_close onlayer master
with charachange

"Sie nickt, sieht aber nicht auf."


"Ich schätze, diese Aufgabe fällt für gewöhnlich Lilly zu."


hi "Sicher. Lass mich nur ein paar Sachen holen…"


"Rasch hole ich ein paar grundlegende Dinge für mich selbst und gehe dann mit Hanako im Schlepptau zur Kasse."


"Der Angestellte nickt mir uninteressiert zu, als er die Artikel einscannt."


"Ich nehme an, uns einfach zu ignorieren, ist eine Möglichkeit, mit den Besonderheiten der Yamaku umzugehen; es kommen wohl viele Schüler hierher, weil der Laden der Schule am nächsten ist."


"Die Angestellten müssen wohl alle ihre eigene Art haben, wie sie mit uns umgehen. Oder vielleicht auch nicht; vielleicht bin ich der Einzige, der zweimal über meine ungewöhnlichen Mitschüler nachdenkt."


stop music fadeout 2.0

scene bg suburb_konbiniext_ss onlayer master
with locationchange

"Sobald wir bezahlt haben, gehen Hanako und ich zurück auf die Straße."


scene bg school_road_ss onlayer master
with locationskip

play music music_tranquil fadein 10.0

"Die Straße ist jetzt so gut wie verlassen. Die Schüler, die vorhin mit uns ins Dorf gegangen sind, sind nirgends zu sehen. Bisher scheint keiner auf dem Rückweg zur Schule zu sein."


"Und da auf der Straße vor uns nur die Schule liegt, scheint sonst niemand in der Nähe zu sein."


show hanako def_worry_close_ss onlayer master at center
with charaenter

"Die Leere zeigt sich an Hanako; in beiden Armen trägt sie jeweils eine Tasche, ihren Kopf hält sie nicht mehr gebeugt, sondern aufrecht…"


"Fast als würde sie den Spaziergang genießen."


hi "Also, warum diese ganzen seltsamen Sachen? Mischgewürz? Wozu braucht man das denn in der Schule?"


show hanako basic_normal_close_ss onlayer master
with charachange

ha "Manchmal… mach ich… ganz gerne was zu essen."


hi "Gut, ja, das mach ich auch, aber… Gewürze?"


hi "Das ist ein bisschen professioneller, meinst du nicht?"


show hanako emb_blushing_close_ss onlayer master
with charachange

ha "N-Nicht wirklich."


hi "Also ich find's cool. Du musst mir das mal irgendwann zeigen."


show hanako emb_smile_close_ss onlayer master
with charachange

ha "S-Sicher."


"Sie scheint sich nicht allzu sicher zu sein, aber sie zu drängen, erscheint mir nicht sehr klug."


"Zumindest wirkt sie um einiges fröhlicher, als sie es auf dem Weg hier hinunter war."


"Allein das hebt ein bisschen meine Laune."


scene bg school_dormext_full_ss onlayer master
with shorttimeskip

show hanako basic_normal_close_ss onlayer master at center
with charaenter

"Vor dem Mädchenwohnheim klauben Hanako und ich unsere jeweiligen Einkäufe aus den Einkaufstüten."


"Im Vergleich wirken meine Sachen richtig schlicht."


hi "Ich sag dir, du beschämst mich damit richtig…"


show hanako defarms_shock_close_ss onlayer master
with charachange

ha "N-Nein tu ich nicht… Ich mach nur…"


hi "Ich mach nur Spaß."


show hanako def_worry_close_ss onlayer master
with charachange

hi "Ich hab einen Berg an Hausaufgaben, den ich letzte Woche liegengelassen habe. Ich muss jetzt los."


hi "Kriegst du es allein hin, das in dein Zimmer zu schaffen?"


show hanako cover_bashful_close_ss onlayer master
with charachange

ha "J-Ja."


hi "Sicher? Gut. Ich seh dich morgen."


show hanako basic_smile_close_ss onlayer master
with charachange

ha "T-Tschüss."


hide hanako onlayer master
with charaexit

stop music fadeout 7.0

"Unsere Wege trennen sich, und ich gehe zurück in mein Zimmer."


scene bg school_dormhisao_ss onlayer master
with locationskip

"Berge aus Papier liegen auf meinem Schreibtisch und betteln darum, bearbeitet zu werden. Durch den ganzen Trubel letzte Woche hatte ich kaum Zeit, das aufzuholen."


"Ich habe versucht, mit dem Lernen dranzubleiben, während ich im Krankenhaus war, aber manches von dem Zeug habe ich noch nie gesehen – nicht einmal früher in meiner alten Schule."


"Völlig unvorbereitet reiße ich den Verschluss einer Getränkedose auf und mache ich an die Arbeit."


scene black onlayer master
with dissolve



label de_H4:

scene black onlayer master
with None

play music music_daily fadein 6.0

scene bg school_dormhisao onlayer master
with locationchange

"Die Tage werden jetzt wirklich immer heißer."


"Heute Morgen bin ich schweißgebadet aufgewacht."


"Als die Schüler die Wohnheime zum Frühstück und zum anschließenden Unterricht verlassen, scheint die Sonne schon in voller Pracht; seltsamerweise bringt mich das in gute Laune."


"Es ist noch nicht einmal acht, trotzdem habe ich das Gefühl, dass das einer dieser angenehmen, ruhigen und warmen Tage wird."


"Wenn ich nicht in einer Schule wäre, bei der jede Abwesenheit für ein Zeichen einer lebensbedrohlichen Situation gehalten wird, würde ich mir überlegen, den ganzen Tag zu schwänzen und mich einfach nur in den Schulgärten zu entspannen."


"Ja, heute wird ein echter Faulenzertag."


"Als ich mich ausstrecke, halte ich für einen Moment inne und denke über die Ermahnung nach, die mir Doc zum Sport treiben gegeben hat. Vielleicht hätte ich das morgendliche Jogging beibehalten sollen."


"Mit jemandem wie Emi zu laufen, wäre zwar ein bisschen anspruchsvoll gewesen, aber wenn ich mich an mein eigenes Tempo halten würde…"


"Ach, wem mache ich etwas vor? Ohne jegliche Motivation könnte ich mich an so etwas eh nicht halten."


"Es ist nicht so, als würde ich den ganzen Tag herumsitzen. Zum Mini-Markt und zurück gehen zählt als Training, oder? Besonders der Weg den Hügel hoch…"


"Ja, das ist kein Problem. Im Vergleich zu den Monaten, die ich im Krankenhaus gelegen habe, kriege ich reichlich Bewegung."


scene bg school_scienceroom onlayer master
with shorttimeskip

"Anscheinend bin ich nicht der Einzige, der den Tag zu schätzen weiß."


"Fast jeder Schüler aus der Klasse blickt durch das Fenster und in den verlockenden Himmel."


"Sogar der unerschütterlichen Shizune scheint ihr üblicher Elan für Schularbeiten zu fehlen."


"Misha hat sogar – so frech wie immer – die oberen Knöpfe ihres Hemds geöffnet und fächert sich selbst mit einem Notizblock an."


"Ich muss wohl gestarrt haben, weil sie mir jetzt die Zunge herausstreckt."


"Allerdings macht sie keine Anstalten aufzuhören, und sie gibt sich auch keine Mühe, es zu verbergen."


play sound sfx_normalbell

"Das Mittagsläuten scheint jeden zu überraschen, und das Klassenzimmer lehrt sich viel langsamer als sonst."


"Die Hitze scheint allen den Wind aus den Segeln zu nehmen."


stop music fadeout 8.0

"Na ja, fast jedem."


show hanako emb_emb onlayer master
with charaenter

ha "H-Hisao?"


hi "Hey Hanako, was kann ich heute für dich tun?"


"Hanako hat bereits eine Essensbox in der Hand."


"Man muss kein Detektiv sein, um zu verstehen, worauf das hinauslaufen soll."


show hanako emb_smile onlayer master
with charaenter

ha "Ähm… willst du wieder mit uns essen?"


show hanako basic_bashful onlayer master
with charaenter

ha "Ich… ich hab genug für alle mitgebracht…"


hi "Spitze. Du brauchst aber deswegen nicht so steif sein."


show hanako basic_normal onlayer master
with charaenter

ha "Ah… stimmt."


hi "Ich nehme an, wir gehen in unser Teezimmer?"


show hanako cover_worry onlayer master
with charaenter

ha "B-Bitte."


show hanako basic_normal onlayer master
with charaenter

ha "Lilly sagte, sie trifft uns dort, also sollten wir… wir…"


hi "Sollten wir?"


show hanako emb_smile onlayer master at center
with charaenter

ha "… sollten wir zusammen vorausgehen…"


hi "Klingt nach 'ner guten Idee. Diese Hitze hat mich ziemlich hungrig gemacht."


"Hanako seufzt erleichtert, und ich packe meine Sachen zusammen."


scene bg school_miyagi onlayer master
with locationskip

play music music_happiness fadein 1.0

"Wie immer ist die Atmosphäre des Teezimmers erfrischend, weil es so wirkt, als wäre es vom Rest der Welt abgeschnitten."


"Andererseits scheint der übliche Schullärm etwas dezenter zu sein; höchstwahrscheinlich wegen Faulheit, die durch die Hitzeerschöpfung noch gefördert wird."


"Hanako breitet langsam ihr Essen auf dem Tisch aus und ist dabei bei jeder kleinen Bewegung höchst konzentriert, als ob sie sich ablenken wollte."


"Es ist kaum zu merken, aber an ihrem Verhalten kann ich erkennen, dass sie alles mit äußerster Sorgfalt vorbereitet hat."


hi "Ich schätze, Lilly ist noch nicht da. Sollen wir ohne sie anfangen?"


show hanako emb_timid onlayer master:
    center
    ypos 1.17
with charaenter

ha "S-Sie wird bald da sein…"


show hanako emb_downtimid onlayer master
with charachange

"Hanako kämpft mit dem Deckel des Reisbehälters."


hi "Warte, lass mich dir helfen…"


"Ich nehme Hanako den Behälter aus den Händen und versuche, den Deckel mit Gewalt aufzumachen."


"So sehr ich mich auch bemühe, er scheint festzuklemmen."


hi "Lass mich raten, hast du den Deckel draufgelegt, während der Reis noch heiß war?"


show hanako emb_sad onlayer master
with charachange

ha "J-Ja. Ich war in Eile."


"Ich stelle den Behälter zwischen uns auf den Tisch."


hi "Hab ich mir gedacht. Sieht so aus, als wäre er festgeklemmt. Wir werden heißes Wasser brauchen, um ihn aufzukriegen."


hi "Aber das könnte hier drin ein Problem werden. Wir würden alles nass machen."


li "Na wenn das so ist. Wie wäre es, wenn ich zur heutigen Mahlzeit etwas beisteuere?"


show lilly invis onlayer master at left
with None

show hanako emb_smile onlayer master:
    tworight
    ypos 1.17
show bg school_miyagi onlayer master at bgright
show lilly basic_cheerful onlayer master at twoleft
with dissolvecharamove

"An der Tür steht Lilly und hält lächelnd eine Tüte voll mit allerlei Brötchen und Gebäck hoch. Ich kann nicht anders, als auch zu lächeln."


show lilly basic_smileclosed onlayer master
with charachange

li "Da ihr Zwei meinetwegen eure Pläne umwerfen musstet, dachte ich, ich bringe eine Kleinigkeit mit."


hi "Danke, Lilly. Warte, lass mich dir helfen…"


show lilly basic_smileclosed onlayer master at Transform(ypos=1.2)
with charamove

"Mit ein wenig Hilfe findet Lillys Brötchensortiment auch seinen Platz auf Hanakos reisloser Servierplatte. Um das Bild zu vervollständigen, mache ich noch schnell etwas Tee."


hi "Schön, ich freu mich richtig darauf."


show hanako emb_downtimid onlayer master
with charachange

"Als ich einen Bissen nehme, bemerke ich, wie Hanako ihr Bestes versucht, nicht so auszusehen, als würde sie mich beobachten."


"Es ist nichts besonderes, aber andererseits kann ich mich nicht wirklich beschweren. Ich bin ziemlich faul, wenn es darum geht, für mich selbst zu kochen."


hi "Nicht schlecht. Du hast das aus den Sachen gemacht, die du gestern gekauft hast?"


show hanako emb_blushtimid onlayer master
with charachange

ha "J-Ja."


"Hanakos Augen schreien mich regelrecht an und betteln um irgendeine Art von Bewertung."


hi "Also das war es auf jeden Fall wert. Danke, Hanako."


show hanako cover_bashful onlayer master
with charachange

ha "Nach… nach gestern wollte ich… dir das zeigen…"


hi "Schon okay. Ich war nur ein bisschen über die Sachen überrascht, die du gekauft hast."


show lilly basic_weaksmile onlayer master
with charachange

li "Hanako mochte es schon immer, beim Essen zu experimentieren. Ich finde es gut… meistens."


"Obwohl Lillys Lächeln sich nicht verändert, sagt mir der leichte Wechsel in ihrer Stimmlage, dass früher nicht immer alles so gut geworden ist."


"Außerdem ist es nicht so, als hätte Hanako viele Testesser…"


stop music fadeout 7.0

"Warte mal… hat Lilly gewartet, bis ich anfange? Sie hat erst begonnen zu essen, als ich gesagt habe, dass es ganz gut ist…"


"Ihr freches Grinsen sagt mir, dass sie das bewusst getan hat. Ich muss einen Weg finden, wie ich ihr in Zukunft eins auswischen kann, um das wieder wettzumachen."


hi "Na ja, es schmeckt, und das ist alles, was zählt, oder?"


show hanako basic_smile onlayer master
with charachange

ha "G-Genau."


show lilly basic_smileclosed onlayer master
with charachange

"Lilly, die zufrieden damit ist, nicht die Erste zu sein, die Hanakos Kreation probiert, beginnt vor ihren Augen zu essen."


"Ich ertappe mich dabei, wie ich zu starren beginne, als ich sie beobachte. Ihre Essstäbchen berühren sanft die Servierplatte, während sie mit den Spitzen vorsichtig darauf herumstochert, das Essen ausfindig macht und es dann geschickt aufsammelt."


"Wenn man die Umstände nicht kennen würde, könnte man denken, sie wäre ein Kind, das mit seinem Essen spielt."
"Obwohl sie es mit solcher Sorgfalt und Gedankenlosigkeit tut, dass es offensichtlich ist, dass sie diese Art von Mahlzeit immer so zu sich nimmt."


"Da ich nicht zu kurz kommen will, beginne ich auch zu essen."


show hanako emb_downsmile onlayer master
with charachange

"Hanako geht das Ganze anders an. Sie wartet bis Lilly und ich unsere Teller gefüllt haben, bevor sie sich schnell ihre Portion schnappt."


show hanako emb_smile onlayer master
with shorttimeskip

play music music_dreamy fadein 4.0

"In kürzester Zeit ist alles leer, bis auf den immer noch verschlossenen Reisbehälter."


show lilly basic_smile onlayer master
with charachange

li "Danke Hanako, jetzt bin ich satt."


show hanako basic_smile onlayer master
with charachange

ha "N-Nein… Ich danke dir für die Brötchen…"


hi "Ja, ohne die wäre es eine Katastrophe gewesen."


show lilly basic_planned onlayer master
with charachange

li "Nichts zu danken."


show lilly basic_weaksmile onlayer master
with charachange

li "Aber jetzt muss ich zurück. Man vergisst so leicht die Zeit, wenn man hier isst."


hi "Ja. Ich verstehe, was du meinst. Wir räumen hier noch auf und kommen dann nach."


show lilly basic_smileclosed onlayer master at twoleft
with dissolvecharamove

li "Also dann, ich wünsche euch einen schönen Tag."


hide lilly onlayer master
with charaexit

show hanako basic_smile onlayer master:
    center
    ypos 1.17
show bg school_miyagi onlayer master at center
with charamove

"Lilly klopft mit ihrem Gehstock den stillen Gang entlang, als sie uns verlässt."


"Hanako und ich packen schnell unsere Sachen zusammen, bleiben aber sitzen und warten darauf, dass es läutet."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene bg misc_sky onlayer master at Fullpan(20.0)
with locationchange

"Gemeinsam schauen wir aus dem Fenster in den endlosen blauen Himmel."


play sound sfx_warningbell

"Wenn die Schulglocke nicht läuten würde, hätte ich schwören können, dass die Zeit stehen geblieben ist."


"In mir baut sich das Verlangen auf, den Unterricht zu schwänzen."


"Ich werfe einen Blick auf Hanako, die auch keine Anzeichen macht, sich zu bewegen."


ha "Jetzt… noch nicht…"


$ renpy.music.set_volume(1.0, 3.0, channel="music")

scene bg school_miyagi onlayer master
show hanako basic_smile onlayer master:
    center
    ypos 1.17
with shorttimeskipsilent

"Die Zeit zwischen dem ersten und dem zweiten Läuten vergeht in Sekundenschnelle."


hi "Wir sollten wirklich los… Sie werden ausflippen und einen Suchtrupp bilden, wenn wir schwänzen…"


show hanako basic_distant onlayer master
with charachange

"Hanako seufzt."


show hanako basic_normal onlayer master
with charachange

ha "Du hast Recht."


show hanako basic_normal onlayer master at center
with charamove

"Langsam steht sie auf, und ich tue es ihr gleich."


scene bg school_staircase2 onlayer master
with locationskip

"Schweigend begeben wir uns über die alte Treppe in den zweiten Stock und von dort zu unserem Klassenzimmer."



scene bg school_hallway3 onlayer master
with locationchange

play sound sfx_dooropen

"Ich öffne die Tür und betrete vor Hanako den Klassenraum. Schon im Voraus senke ich entschuldigend den Kopf."


scene bg school_scienceroom onlayer master at center
with locationchange

stop music fadeout 5.0

hi "Entschuldigen Sie die Verspätung."


play sound sfx_doorclose

"Ich werde weder von ernsten Worten begrüßt noch von einer verärgerten Anweisung mich hinzusetzen. Stattdessen einfach nur von einer Stille, die entsteht, wenn ungefähr fünfzehn Schüler versuchen, nicht zu lachen."


"Mutou ist wie immer zu spät und noch nicht da. Die Tatsache, dass Hanako und ich zusammen gekommen sind, ist jedoch total offensichtlich."


show misha hips_grin onlayer master at center
with charaenter

mi "Pff… pffwa…"


"Das macht dann wohl ungefähr vierzehn Schüler, die es versuchen, und eine Schülerin, die es nicht schafft."


play music music_comedy

show misha cross_laugh onlayer master
with charachange

mi "Pft-bwahahaha! Das Liebespärchen kehrt zurück~!"


show misha hips_laugh onlayer master
with charachange

mi "WAHAHAHA~!"


hi "Ja, danke. Du kannst jetzt wieder runterkommen."


hide misha onlayer master
show hanako invis_close onlayer master:
    center
    xpos 1.0
with charaexit

show bg school_scienceroom onlayer master at bgleft
show hanako emb_downsad_close onlayer master:
    xpos 0.8
with dissolvecharamove

"Ich gehe durch die Tür und bemerke, dass sich Hanako eng an meinen Rücken gepresst vor der Klasse versteckt."


show hanako invis_close onlayer master:
    xpos 0.7
with dissolvecharamove

"Als ich mich meinem Tisch nähere, löst sie sich schließlich von mir und geht steif zu ihrem eigenen. Ihre Anstrengungen, die Gegenwart der anderen gedanklich auszublenden, sind ziemlich klar in ihrem Gesicht zu erkennen."


scene bg school_scienceroom onlayer master at bgright
with charamove

"Ich werfe kurz einen Blick zur Tür, um zu sehen, ob der Lehrer schon kommt, mache einen Ausflug zu Hanakos Tisch und flüstere ihr ins Ohr."


hi "Mach dir keine Gedanken um Misha, sie ist immer so. Ich hatte heute Spaß. Mach dir nichts draus, okay?"


"Hanako nickt hinter ihren verschränkten Armen mit dem Kopf, aber zeigt immer noch nicht ihr Gesicht."


play sound sfx_dooropen

show muto invis onlayer master at tworight
with None

show muto normal onlayer master at center
show bg school_scienceroom onlayer master at center
with dissolvecharamove

"Ich will noch da bleiben und sie weiter trösten, aber Mutou sucht sich genau diesen Moment aus, um das Zimmer zu betreten. Mitten in seiner Vorlesung, als hätte er im Gang begonnen, sie zu halten."


show muto smile onlayer master at center
with charaenter

mu "… was natürlich direkt proportional zu der Ladung, aber umgekehrt proportional zum Quadrat der Entfernung…"


hide muto onlayer master
with charaexit

play sound sfx_doorclose

"Er ist so in seinen Vortrag vertieft, dass er gar nicht bemerkt, wie ich mich von Hanakos Tisch zurück zu meinem Platz schleiche."


"Während Mutou weiter schwafelt, lehnt sich Misha zu mir herüber."


show misha invis onlayer master at offscreenleft
with None

show misha perky_smile_close onlayer master:
    xanchor 0.5 xpos 0.16
with dissolvecharamove

mi "Der Lehrer hat deine Verspätung vielleicht nicht bemerkt, aber ich schon."


"Das war durch die Show, die du gerade abgezogen hast, offensichtlich."


show misha hips_grin_close onlayer master
with charachange

mi "Mir wurde aufgetragen, dich heute vom Haken zu lassen, aber nur unter einer Bedingung."


hi "Oh? Und die wäre?"


show misha sign_smile_close onlayer master
with charachange

mi "Du musst uns heute Nachmittag helfen~!"


"Ich recke meinen Hals, um über Mishas Schulter zu schauen."


"Shizune stellt praktischerweise keinen Augenkontakt mit mir her."


hi "Gut. Nur heute."


hi "Ich hab euch schon gesagt, dass ich dem Rat nicht beitreten werde, weißt du noch?"


show misha hips_grin_close onlayer master
with charachange

mi "Natürlich! Das könnte man als Tat unter Zwang… ähm, unter Zwang…"


show misha perky_confused_close onlayer master
with charachange

"Sie sieht nach unten auf ihren Notizblock und sucht augenscheinlich nach der Stelle in ihrem Skript."


show misha hips_grin_close onlayer master
with charachange

mi "… erachten und wäre somit gegen die Vorschriften."


hi "Wie ungewöhnlich für euch, so auf die Vorschriften zu achten."


show misha sign_smile_close onlayer master
with charachange

mi "Man sollte sich an die Regeln halten!"


show misha perky_smile_close onlayer master
with charachange

mi "Es ist nur so, dass es nicht für jede Situation eine Regel gibt, deshalb kann man sie manchmal vernachlässigen."


hi "Und trotzdem wundert ihr Zwei euch, warum sonst keiner im Schülerrat sein will…"


stop music fadeout 3.0

show misha hips_frown_close onlayer master
with charachange

with Pause(0.3)

show misha invis onlayer master at offscreenleft
with dissolvecharamove

hide misha onlayer master
with None

"Nachdem sie mir ihre Zunge herausgestreckt hat, wendet sich Misha wieder ihrem Buch zu, und wir kämpfen uns durch die letzte Hälfte unseres Schultages."


with shorttimeskip

play sound sfx_normalbell

show shizu invis_close onlayer master at offscreenright
show misha invis_close onlayer master at offscreenleft
with None

show misha hips_smile_close onlayer master at twoleft
show shizu behind_blank_close onlayer master at tworight
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

"Bevor ich überhaupt aufstehen kann, haben Misha und Shizune ihre Hände auf meine beiden Schultern gelegt."


hi "Hey, ich hab doch gesagt, dass ich euch helfen werde, Mann…"


play music music_shizune fadein 1.0

show misha hips_grin_close onlayer master
with charachange

mi "Das ist nur zur Sicherheit, Hisao, zur Sicherheit~!"


show hanako invis behind shizu onlayer master at offscreenright
with None

show misha hips_smile_close onlayer master at Transform(xpos=0.17)
show shizu behind_blank_close onlayer master at Transform(xpos=0.5)
show bg school_scienceroom onlayer master at bgleft
show hanako emb_timid onlayer master:
    xanchor 0.5 xpos 0.9
with dissolvecharamove

ha "H-Hisao?"


"Hanako versucht zaghaft den Raum zu verlassen, indem sie um uns herumgeht, und ich erkenne plötzlich, dass das meine einzige Chance sein könnte zu entkommen."


hi "Oh hey Hanako. Was ist los?"


show shizu basic_angry_close onlayer master
with charachange

shi "…"


show misha hips_frown_close onlayer master
with charachange

mi "Hey, was lässt dich glauben, dass du Zeit zum Plaudern hast?"


hi "Ach entspann dich, das dauert nicht lange… Entschuldige Hanako, was wolltest du sagen?"


show hanako emb_downtimid onlayer master
with charachange

ha "Ich… ich wollte in die Bibliothek, und… und ich dachte…"


"Hanakos Daumen spielen miteinander, und ihre Augen huschen durch den Raum. Sie sieht alles andere an, nur uns nicht."


show misha sign_smile_close onlayer master
with charachange

mi "Tut mir leid Hanako, aber Hisao muss mit uns kommen. Er hat noch was zu tun."


show shizu behind_smile_close onlayer master
with charachange

shi "…"


show misha hips_grin_close onlayer master
with charachange

mi "Oh! Aber du kannst auch helfen, wenn du willst."


show hanako cover_worry onlayer master
with charachange

ha "Ähm…"


label de_choiceH4:
menu:
    with menueffect
    mi "Also, wie sieht's aus, Hisao?"
    "Was denkst du, Hanako?":




        return m1
    "Ich hab heute schon genug für den Rat gemacht.":


        return m2


label de_H5_1:


show bg school_scienceroom onlayer master at bgleft
show hanako cover_worry onlayer master:
    xanchor 0.5 xpos 0.9
show shizu behind_smile_close onlayer master at Transform(xanchor=0.5, xpos=0.5)
show misha hips_grin_close onlayer master at Transform(xanchor=0.5, xpos=0.17)
with None

hi "Was sagst du, Hanako? Wenn wir alle helfen, sollte es nicht lange dauern."


show hanako emb_timid onlayer master
with charachange

"Hanakos unruhiges Gezappel beantwortet meine Frage, bevor sie die Worte aussprechen kann."


show hanako emb_downtimid onlayer master
with charachange

ha "Ich… ich muss wirklich los…"


"Na ja, das war zu erwarten. Sieht so aus, als wären es wieder nur die Mädchen vom Rat und ich."


"Es ist einfacher, mich damit abzufinden, dass ich einen weiteren Nachmittag in dem kleinen Schülerratsbüro mit Arbeit verbringen werde."


hi "Ich treff dich später, okay?"


show hanako emb_smile onlayer master
with charachange

ha "O-Okay."


stop music fadeout 3.0

show misha hips_grin_close onlayer master at twoleft
show shizu behind_smile_close onlayer master at tworight
show hanako invis onlayer master at offscreenright
show bg school_scienceroom onlayer master at center
with dissolvecharamove

show misha hips_smile_close onlayer master at twoleft
hide hanako onlayer master
with charachange

mi "So! Jetzt, da wir die Verabschiedung hinter uns haben, ist es Zeit, etwas zu tun!"


scene bg school_hallway3 onlayer master
with locationchange

"Misha und Shizune schleppen mich zum Schülerratsbüro, ohne auch nur einmal meine Schultern loszulassen."


"Es tut mir ein bisschen leid, dass ich Hanako so stehengelassen habe, aber wenn das der Preis ist, um ihr Misha vom Hals zu schaffen, sei's drum."


scene bg school_council onlayer master
with locationchange

hi "Also dann, was haben wir heute vor?"


show misha sign_smile onlayer master at center
with charaenter

play music music_ease fadein 8.0

mi "Eine Nachbesprechung!"


hi "Hä? Sollte man so etwas nicht abhalten, nachdem man etwas gemacht hat?"


show misha hips_grin onlayer master
with charachange

mi "Japp! Wir müssen alle Informationen vom Fest sortieren, sodass Shicchan mit den Lehrern eine Nachbesprechung abhalten kann."


show misha hips_grin onlayer master at twoleft
show bg school_council onlayer master at bgleft
with charamove

show shizu adjust_happy onlayer master at tworight
with charaenter

"Shizune lässt einen großen Berg Papierkram auf den Schreibtisch vor mir fallen und lächelt kurz."


show misha hips_smile onlayer master
with charachange

mi "Du musst die hier in zwei Stapel auseinandersortieren."


show misha sign_smile onlayer master
with charachange

mi "Einen für Finanzielles wie Einkünfte, einen für Feedback, einen für positives Feedback, vielleicht einen für Sachen, die aussehen, als könnten sie nächstes Jahr zum Problem werden, einen für Probleme, die man wohl nicht beheben kann…"


hi "Das sind ein paar mehr als zwei Stapel…"


show misha perky_confused onlayer master
with charachange

mi "Was? Oh, richtig. Ja, ich dachte, es würden nur zwei Stapel werden. Mein Fehler."


hi "Ah ja. Und was macht ihr Zwei, während ich das mache?"


show misha hips_grin onlayer master
show shizu adjust_smug onlayer master
with charachange

mi "Nun ja, wir haben die Mittagspause verpasst, weil wir diese ganzen Berichte gesammelt haben, darum werden wir was zu Essen holen."


"Warum habt ihr sie nicht gleich sortiert, während ihr sie eingesammelt habt…"


"Glücklicherweise setzt sich mein Selbstverteidigungsmechanismus in Gang und hält mich davon ab, meinen Mund aufzumachen und meine Situation noch weiter zu verschlimmern."


show misha perky_confused onlayer master
with charachange

mi "Eh?"


show misha perky_sad onlayer master
with charachange

mi "Das ist doch nicht fair!"


show shizu behind_blank onlayer master
with charachange

shi "…"


"Ich war so darin vertieft, mich über die unfaire Verteilung der Arbeit aufzuregen, dass ich nicht gemerkt habe, dass Shizune noch weiter Handzeichen gemacht hat."


"Wenn es Misha nicht so herausgeplatzt wäre, hätte ich es wohl gar nicht gemerkt."


show shizu adjust_smug onlayer master
with charachange

show shizu basic_normal onlayer master
with charachange

show shizu behind_blank onlayer master
with charachange

"Shizune gibt Misha anscheinend eine ziemlich lange Reihe an Befehlen, und keiner davon sieht erfreulich aus."


show misha sign_sad onlayer master
with charachange

show misha perky_sad onlayer master
with charachange

show misha perky_sad onlayer master at Transform(ypos=1.15)
with charamove

"Nachdem sie zu einem Entschluss gekommen ist, gibt sie einige Handzeichen an Shizune zurück und setzt sich dann neben mich an den Schreibtisch."


show shizu adjust_happy onlayer master
with charachange

hide shizu onlayer master
with charaexit

show misha perky_sad onlayer master at Transform(xpos=0.5)
show bg school_council onlayer master at center
with charamove

"Shizune winkt uns beiden noch zu, bevor sie durch die Tür verschwindet."


hi "Was war das denn gerade?"


show misha perky_confused onlayer master
with charachange

mi "Shicchan hatte Angst, du würdest alles falsch machen, wenn du nicht beaufsichtigt wirst."


show misha perky_sad onlayer master
with charachange

mi "Und da sie dir nicht sagen kann, wie du alles vermasselst, soll ich hierbleiben. Aaach… mist. Ich wollte mit Shicchan mitgehen!"


show misha cross_smile onlayer master
with charachange

mi "Aber sie wird uns Essen mitbringen~!"


show misha cross_grin onlayer master
with charachange

mi "Ist das nicht toll?"


"Mishas Unbekümmertheit ist einfach unglaublich. Von tief deprimiert zu überglücklich wegen ein paar Kalorien."


"Es ist schwer vorzustellen, wie jemand so funktionieren kann."


hi "Na ja, es hätte schlimmer sein können."


hi "Also, was sollen wir machen?"


show misha sign_smile onlayer master
with charachange

mi "Sortieren."


hi "So viel hab ich verstanden."


show misha hips_smile onlayer master
with charachange

mi "Okay, lass uns einfach damit anfangen, Stapel zu machen. Wir kriegen später raus, für was die Stapel stehen."


hi "Okay…"


show misha perky_smile onlayer master
with charachange

"Wir fangen an, die Zettel in immer kompliziertere Stapel aufzuteilen."


"Zuerst sind es nur einfache Kategorien: Finanzen, Feedback, Ereignisberichte…"


"Dann teilen sie sich auf in gute und schlechte Berichte, und noch weiter, bis es aussieht, als hätten wir die Zettel einfach nur auf den Schreibtisch geschmissen."


hi "Das ist hoffnungslos."


show misha perky_confused onlayer master
with charachange

mi "Hä? Warum? Wir machen doch, was uns gesagt wurde, oder?"


hi "Ja, aber es sieht aus, als würden wir nur ein Durcheinander machen."


show misha hips_grin onlayer master
with charachange

mi "Nein, ich glaube, wir haben viel geschafft. Shicchan kann den Rest ausarbeiten."


show misha cross_grin onlayer master
with charachange

mi "Wir können also jetzt aufhören, glaube ich."


"Es ist fast, als hätte Mishas Vernunft mit Shizune das Zimmer verlassen."


"Trotzdem, es hat keinen Sinn, dagegen anzureden."


show misha sign_smile onlayer master
with charachange

mi "Also…"


show misha cross_smile onlayer master
with charachange

mi "Was ist mit dir und Hanako?"


hi "Mir und Hanako?"


show misha hips_smile onlayer master
with charachange

mi "Du warst heute mit ihr zusammen, oder nicht~?"


show misha hips_grin onlayer master
with charachange

mi "Ist da was im Gange? Irgendwelche Gerüchte, die du mir vorenthältst~?"


hi "Wenn ich dir erzählen würde, wie es in meinem Leben läuft, dann wären das keine Gerüchte, oder?"


show misha perky_confused onlayer master
with charachange

mi "Schätze nicht…"


hi "Wir sind nur Freunde, glaube ich."


hi "Warum interessiert dich das so? Ich dachte, du und Shizune, ihr mögt sie nicht…"


show misha cross_frown onlayer master
with charachange

mi "Das stimmt nicht wirklich. Du weißt, Shicchan und Lilly kommen nicht gut miteinander aus."


mi "Und da man Hanako nicht wirklich von Lilly wegbekommt, reden wir nicht viel mit ihr."


show misha sign_smile onlayer master
with charachange

mi "Aber das heißt nicht, dass ich mir um sie keine Sorgen machen kann."


hi "Von welchen Sorgen sprichst du?"


show misha perky_sad onlayer master
with charachange

mi "Na ja, sie trifft sich nie mit jemand anderem, oder? Das ist nicht gut, Hicchan!"


"Wenn Shizune und Lilly sich nicht mögen, weil „ihre Persönlichkeiten unterschiedlich sind”, dann will ich gar nicht daran denken, wie Misha und Hanako miteinander auskommen würden…"


show misha perky_confused onlayer master
with charachange

mi "Ich meine, wir sitzen so oder so alle im selben Boot, stimmt's~?"


hi "Na ja, ich denke schon."


show misha sign_smile onlayer master
with charachange

mi "Dieses eine Mal, als sie mitten im Unterricht gegangen ist, ist Shicchan zum Lehrer gegangen und hat gefragt, was deswegen unternommen wird."


show misha sign_confused onlayer master
with charachange

mi "Er sagte, dass jeder Schüler hier besondere Bedürfnisse hat, und dass Shicchan sich darüber keine Gedanken machen sollte."


show misha perky_confused onlayer master
with charachange

mi "Hanako macht nie bei Gruppenarbeiten mit; sie haut einfach ab."


mi "Ist das nicht genug, um sich Sorgen zu machen?"


hi "Ich glaube, du hast Recht. Sie sagt immer noch kaum was, wenn wir reden."


show misha perky_sad onlayer master
with charachange

mi "Tja, das ist mehr, als ich geschafft habe. Shicchan und ich haben es beide versucht, als sie hierherkam, aber sie bekam Schiss und ist weggelaufen."


"Ich überlege, ob ich Misha erzähle, dass dasselbe mit mir passiert ist, aber sie scheint in ihre Überlegungen vertieft zu sein."


"Misha zuzuhören, wenn sie nicht von Shizune beeinflusst wird, ist… interessant."


show misha cross_frown onlayer master
with charachange

mi "Ich denke, sie muss kapieren, dass den Leuten hier egal ist, wie sie aussieht, und dass sie uns vertrauen kann."


show misha cross_smile onlayer master
with charachange

mi "Wenn sie das könnte, würde es mir beim Gedanken an sie viel besser gehen."


"Ich glaube, ich war noch nie so lange mit Misha zusammen, ohne dass sie irgendetwas gestikuliert hat."


"Wenn sie mit Shizune unterwegs ist, fuchtelt sie ständig mit ihren Händen herum und erklärt ihr alles."


"Eine solche Anstrengung beansprucht wahrscheinlich sogar einen scharfsinnigen Verstand."


"Und sehen wir den Tatsachen ins Auge; Misha ist nicht die Hellste."


hi "Nun, ich werde für dich auf sie aufpassen."


hi "Aber du solltest dich wohl für vorhin entschuldigen. Hanako ist nicht der Typ für diese Art von Witz."


show misha perky_confused onlayer master
with charachange

mi "Oh? Oh~!"


show misha perky_sad onlayer master
with charachange

mi "Hab ich gar nicht gemerkt. Entschuldige."


hi "Sag das nicht mir, lass es sie einfach wissen."


show misha perky_smile onlayer master
with charachange

mi "Geht klar. Das Erste, was ich morgen mache, ist mit ihr zu reden."


hi "Gut."


play sound sfx_doorslam
with vpunch

"Ein Radau an der Tür kündigt die Rückkehr von Shizune an."


"Ich schätze, sie weiß nicht wirklich, wie viel Krach sie macht."


show misha hips_grin onlayer master
with charachange

mi "Oh, Shicchan! Du bist zurück!"


show shizu invis onlayer master at Transform(xanchor=0.5, xpos=1.0)
with None

show misha hips_grin onlayer master at Transform(xpos=0.3)
show shizu behind_blank onlayer master at tworight
show bg school_council onlayer master at bgleft
with dissolvecharamove

"Shizune taucht auf, vollbeladen mit Produkten vom Mini-Markt."


show shizu basic_normal2 onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Da war noch was vom Fest übrig. Da das hier offiziell eine Festangelegenheit ist, war ich ein bisschen großzügig."


show misha hips_grin onlayer master
with charachange

mi "Gute Idee Shicchan – zehn Punkte."


hi "Ist das wirklich erlaubt?"


show shizu cross_angry onlayer master
with charachange

shi "…"


show misha cross_frown onlayer master
with charachange

mi "Für jemanden, der sich weigert, uns beizutreten, scheinst du ein ungesundes Interesse an den Methoden dieses Rates zu haben."


show misha cross_grin onlayer master
show shizu adjust_smug onlayer master at tworight
with charachange

mi "Ich werde deine Unverschämtheit bestrafen, indem ich deinen Anteil an dem Festmahl rationiere."


hi "Schon gut, schon gut. Ich hab verstanden."


show misha perky_smile onlayer master
show shizu adjust_happy onlayer master at Transform(ypos=1.15)
with dissolvecharamove

"Misha schiebt die vielen Papierstapel auf eine Seite, um Platz für den Berg an Essen zu machen, den Shizune ausbreitet."


"Während ich zusehe, wie meine schwere und doch vergeudete Arbeit zerstört wird, begreife ich, dass es kein Wunder ist, dass diese beiden Hilfe brauchen."


"Die Mahlzeit aus dem Mini-Markt ist nicht sonderlich schmackhaft, aber wenigstens ist sie sättigend."


show shizu behind_smile onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "Danke für die Hilfe heute. Meistens erfinden wir die Berichte für das Lehrerkollegium einfach."


show misha perky_smile onlayer master
with charachange

mi "Dieses Jahr können wir wenigstens einige Überschriften für die Nachbesprechung erfinden, die von Bedeutung sind."


hi "Seid ihr sicher, dass das hier keine korrupte Organisation ist?"


show misha hips_grin onlayer master
with charachange

mi "Ganz und gar nicht. Wir halten uns an die Vorschriften. Es ist nicht unsere Schuld, wenn die Vorschriften nicht genau genug sind."


hi "Ich dachte, das wäre die Definition von Korruption…"


show misha hips_smile onlayer master
with charachange

mi "Du denkst zu viel nach~!"


hi "Weißt du was? Wahrscheinlich hast du Recht."


hi "Wie auch immer, ich muss los…"


hi "… also, wenn ich gehen darf."


show shizu adjust_smug onlayer master
with charachange

shi "…"


show misha hips_grin onlayer master
with charachange

mi "Deine Arbeit wird für ausreichend erachtet. Du darfst gehen."


hi "Gut, danke."


hi "Wisst ihr, wenn ihr den Punkt „kostenloses Essen” mehr hervorheben würdet als den Punkt „wahnsinnig viel Arbeit”, dann hättet ihr wahrscheinlich mehr Neuzugänge."


stop music fadeout 6.0

show misha sign_smile onlayer master
with charachange

show shizu behind_blank onlayer master
with charachange

mi "Da hast du vielleicht nicht ganz Unrecht."


hi "Na ja, denkt darüber nach."


hi "Und denk über das nach, über was wir geredet haben… Du musst es Shizune nicht sagen, wenn du nicht willst."


show misha perky_confused onlayer master
with charachange

mi "Was? Oh, richtig. Ich versuche, mich morgen mit ihr zu treffen."


show misha perky_smile onlayer master
with charachange

mi "Nacht, Hicchan."


hi "Nacht Misha, Shizune."


scene black onlayer master
with dissolve


label de_H5_2:

show bg school_scienceroom onlayer master at bgleft
show hanako cover_worry onlayer master:
    xanchor 0.5 xpos 0.9
show shizu behind_smile_close onlayer master at Transform(xanchor=0.5, xpos=0.5)
show misha hips_grin_close onlayer master at Transform(xanchor=0.5, xpos=0.17)
with None

hi "Hey, Shizune. Ich weiß, dass ich gesagt habe, ich würde helfen. Aber ich hab vergessen, dass ich schon was vorhatte. Außerdem hab ich letzte Woche schon mehr als genug getan, oder nicht?"


hi "Ich verspreche, dass ich das irgendwann wiedergutmache."


show misha sign_confused_close onlayer master
with charachange

show shizu basic_frown_close onlayer master
with charachange

show misha perky_smile_close onlayer master
with charachange

show shizu behind_blank_close onlayer master
with charachange

"Shizune und Misha entlassen mich aus ihrem Griff und führen ein langes, tiefes und stilles Gespräch."


show misha sign_smile_close onlayer master
with charachange

mi "Na ja, da hast du nicht ganz Unrecht. Um ehrlich zu sein, wollten wir den Rest des Budgets für Kuchen ausgeben."


show misha cross_laugh_close onlayer master
with charachange

mi "Wenn du also nicht da bist, ist das umso besser. Mehr Kuchen für uns. Wahahaha~!"


stop music fadeout 6.0

show shizu invis onlayer master at offscreenleft
with dissolvecharamove

show misha invis onlayer master at offscreenleft
with dissolvecharamove

hide shizu onlayer master
hide misha onlayer master
with None

"Shizune macht eine Kehrtwende und marschiert zur Tür. Misha folgt ihr nach draußen."


hi "Na, das war viel einfacher, als ich gedacht hatte. Letzte Woche waren die zwei wie Bluthunde. Oder Gefängniswärter."


hi "Oder vielleicht von Bluthunden abstammende Gefängniswärter…"


"Ich kann nicht glauben, dass ich das gerade gedacht habe, geschweige denn, dass ich es laut ausgesprochen habe. Ich glaube, ich sollte mich von Kenji fernhalten."


hi "… Egal. Wie auch immer, sollen wir in die Bibliothek gehen?"


show hanako basic_smile onlayer master
with charachange

ha "S-Sicher."


play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3 onlayer master
show crowd onlayer master
with locationchange

"Hanako folgt mir durch die immer noch vollgestopften Flure zur Bibliothek und nutzt mich auf dem Weg als Schutzschild."


stop ambient fadeout 0.5
play music music_happiness fadein 2.0

scene bg school_library onlayer master
show hanako invis onlayer master at offscreenright
show yuuko neutral_down onlayer master at center
with locationchange

show hanako basic_worry onlayer master at tworight
with dissolvecharamove

"Sobald wir durch die Tür gegangen sind, stürzt Hanako auf den Schalter zu, wo Yuuko gerade dabei ist, Bücher zu stapeln."


show hanako emb_emb onlayer master
with charachange

"Bevor ich sie einhole, hat Hanako ihr schon etwas ins Ohr geflüstert."


show yuuko neurotic_up onlayer master
with charachange

yu "Ähm, du würdest das bei den Sachbüchern finden, aber ich weiß nicht, wo genau. Wenn du willst, kann ich nachsehen…"


show hanako emb_downsad onlayer master
with charachange

ha "S-Schon gut."


hi "Hey Yuuko, worum geht's hier eigentlich?"


show yuuko neutral_down onlayer master
with charachange

yu "Oh, Hisao… Hanako sucht nur ein Buch über…"


show hanako emb_blushing onlayer master
with charachange

ha "N-Nichts…"


hi "Ein Buch über nichts? In der Sachbuchabteilung?"


show hanako def_strain onlayer master
with charachange

ha "Ich… ich hab nur…"


show yuuko neurotic_up onlayer master
with charachange

"Ich werfe einen Blick auf Yuuko. Sie sieht aus, als würde sie unter dem Druck, Hanakos Geheimnis für sich zu behalten, bald explodieren."


hi "Yuuko, was hat…"


show yuuko happy_down onlayer master
with charachange

yu "Schach! Sie sucht ein Schachbuch!"


"Gedanklich mache ich mir eine Notiz, dass ich Yuuko niemals wichtige Dinge anvertrauen darf."


show hanako defarms_shock onlayer master
with charachange

ha "Y-Yuuko…"


show yuuko panic_up onlayer master
with charachange

yu "Es tut mir leid Hanako… Es ist mir einfach rausgerutscht…"


hi "Na ja, es ist kein Geheimnis mehr. Komm schon, ich helfe dir. Ich sollte meine Fähigkeiten auch mal wieder auffrischen."


show hanako def_worry onlayer master
with charachange

ha "O-Okay."


hide yuuko onlayer master
with charaexit

show hanako def_worry onlayer master at center
show bg school_library onlayer master at bgleft
with charamove

"Beschämt verschwindet Yuuko hinter dem Schalter, als Hanako und ich uns in die Tiefen der Sachbuchabteilung begeben."


"Ich weiß, dass es ein System geben soll, um die Bücher zu kategorisieren. Ich weiß allerdings nicht, wie es irgendwer entschlüsseln soll, ohne sein halbes Leben damit zu verbringen, es zu erforschen."


"Deswegen sind wahrscheinlich alle Bibliothekare, die ich kenne, Neurotiker."




"Zum Ende des Ganges hin, zwischen den Büchern über Kartentricks und ein paar Büchern über Kinderspiele, steht ein einzelnes Buch mit dem Titel „Schachtaktiken für Meister”."


show hanako basic_bashful onlayer master
with charachange

"Bevor ich es mir greifen kann, hat Hanako das Buch schon in den Händen und klammert es an ihre Brust."


hi "Gut, ich glaube, das ist dann deins. Was dagegen, wenn ich es mir ausleihe, wenn du fertig bist?"


show hanako cover_worry onlayer master
with charachange

ha "N-Nein. Ich… ich hab nur noch nicht wirklich gegen jemanden außer L-Lilly gespielt, darum dachte ich…"


"Mist. Es ist nicht so, als hätte ich versucht, Hanako absichtlich zu besiegen oder so, aber anscheinend hat sie es sich zu Herzen genommen."


"Andererseits heißt das wenigstens, dass sie wieder mit mir spielen will. Das ist ein Plus, oder?"


hi "Ha, na ja, es ist ja nicht so, als wäre ich ein Meister oder so was; ich hab bloß ein bisschen gespielt, bevor…"


"Mir fällt auf, dass ich Hanako noch nichts über meinen Zustand erzählt habe. Ich zögere ein bisschen und entscheide mich dazu, meine Spuren zu verwischen. Das ist ein Gespräch für einen anderen Tag."


hi "… bevor ich hierhergekommen bin."


stop music fadeout 6.0

show hanako cover_distant onlayer master
with charachange



ha "Geht… geht's dir gut?"


hi "Ja, ich hab mich nur an etwas erinnert…"


"Wenn ich so darüber nachdenke, sollte ich keine Angst haben, Hanako von meinem Zustand und meiner Zeit im Krankenhaus zu erzählen. Ihren Narben nach zu urteilen, hat sie vermutlich einige Zeit in einem Krankenhausbett verbracht."


"Aber aus irgendeinem Grund schaffe ich es nicht, darüber zu reden. Zumindest nicht heute und nicht so kurzfristig."


"Um das Gespräch zu beenden, nehme ich wahllos eines der Bücher vom Regal."




"Es ist irgendein Buch über die schnellsten Achterbahnen der Welt…"


"… 1982 veröffentlicht. Na ja, nicht sehr aktuell, aber es sollte wenigstens interessant sein."


hi "Gut, wir haben jetzt beide Bücher. Wollen wir uns hinsetzen?"


show hanako cover_bashful onlayer master
with charachange

"Hanako nimmt mir anscheinend den Bluff ab, und wir gehen zur Leseecke im hinteren Teil der Bibliothek."


hide hanako onlayer master
with charaexit

"Keiner von uns sagt etwas; wir machen einfach unsere Bücher auf und fangen an zu lesen."


"Ich versuche mein Buch zu lesen, aber anscheinend waren die Achterbahnen von 1982 nicht annähernd so groß wie die, die in den Jahrzehnten danach gebaut wurden."


"Die meisten, die aufgezählt werden, sind aus Holz. Irgendwie scheint mir das nicht wirklich sicher zu sein."


"Falls ich mit etwas fahre, das möglicherweise gefährlich ist, will ich, dass es aus Stahl gemacht ist – oder irgendeiner Legierung aus der Zukunft, die große Worte wie „Titan” oder „Ruthenium” beinhaltet."


"Ich verliere schnell das Interesse und meine Augen wandern durch den Lesebereich, um dann bei Hanako zu verweilen."


show ev hana_library_read_std onlayer master:
    truecenter zoom 1.0 subpixel True
    easein 20.0 zoom 1.05
with locationskip

"Hanako scheint in ihr Buch vertieft zu sein. Sie blättert die Seiten vor und zurück, als ob sie sicher gehen will, was sie gerade gelesen hat."


"Ich frage mich, ob das tatsächlich hilft, oder ob sie sich selbst zu viel auflädt."


"Unterbewusst streicht sie sich ihre Haare aus dem Gesicht und gibt damit den Blick auf ihre Narben frei."


"Ich bin mir hier immer noch nicht sicher, was die Benimmregeln angeht. Ist es in Ordnung, nach ihren Narben zu fragen? Wie lange war sie im Krankenhaus? Geht sie immer noch zum Arzt?"


"Das sind wohl alles Fragen, die man jemandem stellen würde, der gerade an deine Schule gewechselt ist – übertragen auf die hiesigen Gegebenheiten."


"Aber bis jetzt bin ich von niemandem direkt danach gefragt worden. Na ja, außer Rin, aber ich glaube nicht, dass ich sie als Anleitung für korrektes Sozialverhalten verwenden sollte."


"Vorerst halte ich einfach meinen Mund. Wenn jemand will, dass du etwas weißt, dann wird er es dir erzählen. Auf das Thema zu drängen, bringt Hanako vielleicht dazu, sich wieder tiefer in sich selbst zu vergraben."


scene bg school_library_ss onlayer master
show yuuko worried_up_ss onlayer master at center
with shorttimeskip

yu "Ähm… entschuldigt die Unterbrechung, aber ich muss die Bibliothek jetzt schließen."


play music music_tranquil fadein 3.0

hi "Schon?"


"Ich schaue auf meine Uhr. Während ich in Gedanken verloren war, sind irgendwie fast zwei Stunden vergangen."


show yuuko smile_down_ss onlayer master
with charachange

yu "Wollt ihr diese Bücher ausleihen? Das kann ich auf dem Weg raus machen…"


show hanako invis onlayer master:
    xpos 0.9 xanchor 0.5 ypos 1.17 yanchor 1.0
with None

show hanako basic_worry_ss onlayer master:
    xpos 0.7
show bg school_library_ss onlayer master at bgleft
show yuuko smile_down_ss onlayer master at twoleft
with dissolvecharamove

ha "B-Bitte."


hi "Ich bin fertig. Ich werde das hier beim Rausgehen zurücklegen. Es war nicht so interessant wie ich zuerst dachte."


show hanako emb_timid_ss onlayer master at tworight
with dissolvecharamove

"Hanako markiert sich die Stelle, an der sie war, mit einem Stück Papier und steht auf. Die Mädchen gehen zum Schalter, und ich bringe mein Buch zu dem – nach meinem besten Wissen – richtigen Regal zurück."


show yuuko neurotic_up_ss onlayer master
with charachange

"Yuuko scannt Hanakos Buch mit routinierter Genauigkeit und schafft es trotzdem, es zu vermasseln."


show yuuko neutral_down_ss onlayer master
with charachange

yu "Oh… geht doch. Aller guten Dinge sind drei. Da das ein Sachbuch ist, kannst du es nur für eine Woche haben."


show hanako basic_smile_ss onlayer master
with charachange

ha "D-Das ist okay."


scene bg school_hallway2 onlayer master
with locationchange

"Yuuko schaltet den Bibliothekscomputer aus und treibt uns zur Tür hinaus."


show yuuko panic_up onlayer master at twoleft
show hanako def_worry onlayer master at tworight
with charaenter

yu "Argh! Ich dachte nicht, dass es schon so spät ist…"


hi "Aber du hast uns doch gesagt, dass du schließen musst…"


show yuuko worried_up onlayer master
with charachange

yu "Ja, ich weiß, aber das war, bevor ich auf die Uhr geschaut habe!"


show yuuko neurotic_up onlayer master
with charachange

yu "Bis dann."


hide yuuko onlayer master
with easeoutleft

"Yuuko läuft den Gang entlang, während sie ihre Handtasche wie eine Luftschlange hinter sich herzieht."


show hanako def_worry onlayer master at center
show bg school_hallway2 onlayer master at bgleft
with dissolvecharamove

hi "Ich schätze, alle Bibliothekare sind Neurotiker."


show hanako emb_timid onlayer master
with charachange

ha "Was?"


hi "Ach, schon gut. Ich hab nur gerade gedacht, dass ich noch nie einen Bibliothekar getroffen habe, der sich seine Zeit einteilen konnte, egal wie gut sie mit ihren Büchern umgehen konnten."


show hanako basic_smile onlayer master
with charachange

ha "Oh… Ich w-weiß, was du meinst…"


"Hanako lächelt belustigt. Das war nicht als Witz gedacht, aber ich muss sie wohl an einen anderen Bibliothekar erinnert haben… oder so…"


show hanako cover_worry onlayer master
with charachange

ha "Ich… ich muss zurück."


hi "Ja, ich auch. Ich hab nicht gemerkt, dass es so spät ist. Danke, dass ich dir Gesellschaft leisten durfte."


show hanako basic_bashful onlayer master
with charachange

ha "K-Keine Ursache."


hi "Ich gehe jetzt sowieso zu den Wohnheimen. Hast du was dagegen, wenn ich dich begleite?"


show hanako emb_blushing onlayer master
with charachange

ha "O-Okay."


hide hanako onlayer master
with charaexit

"Hanako geht voraus, und ich muss ein kurzes Stück joggen, um an ihre Seite zu kommen."


scene bg school_dormext_full_ss onlayer master
with locationchange

show hanako def_worry_ss onlayer master at center
with charaenter

"Wir gehen durch die Gärten und kommen schließlich vor den Wohnheimen an."


hi "Mann, du gehst ziemlich schnell. Ich hab früher in einem Fußballverein gespielt, und du schaffst es, mich abzuhängen."


stop music fadeout 6.0

show hanako emb_downsmile_ss onlayer master at center
with charaenter

"Ich bereue irgendwie, das gesagt zu haben. Es hat weniger mit ihrer Geschwindigkeit zu tun als mit der Tatsache, dass mein Zustand meine Fitness erheblich verschlechtert hat."


"Hanakos Reaktion ist seltsam. Ich habe einen peinlichen Versuch erwartet, ihre Geschwindigkeit herunterzuspielen, aber sie wird nur rot, während sie auf ihre Füße schaut und lächelt."


"Stille breitet sich zwischen uns aus. Das passiert oft, wenn man mit Hanako zusammen ist, aber es fühlt sich diesmal anders an als sonst. Nach ein paar Sekunden versuche ich, das Schweigen zu brechen."


hi "Also dann. Ich seh dich morgen im Unterricht?"


show hanako emb_smile_ss onlayer master
with charachange

ha "S-Sicher."


hide hanako onlayer master
with charaexit

"Hanako winkt kurz zum Abschied, bevor sie durch die Türen des Wohnheims geht. Für eine Weile stehe ich da und schaue sie an, dann mache ich mich auf den Weg zu meinem Zimmer."


scene black onlayer master
with dissolve



label de_H6:

scene bg school_dormhisao onlayer master
with locationchange

"Zwitschernde Vögel."


"Normalerweise wäre das eine gute Zeit, um über die Schönheit der Natur nachzudenken."


"Aber es ist 6 Uhr früh."


play sound sfx_pillow

scene black onlayer master
with Dissolve(0.2)

"Ich drücke mir das Kissen auf den Kopf und werfe mich mit dem Gesicht voran auf die Matratze, in der Hoffnung, dass mich der Aufschlag augenblicklich in den Schlaf zurückschickt."


"Vergeblich."


"Ich drehe und wende mich, aber der Schlaf will einfach nicht zu mir zurückkommen."


play music music_daily fadein 10.0

scene bg school_dormhisao onlayer master
with locationchange

"Also gut Natur, du hast gewonnen. Siehst du? Ich stehe jetzt auf…"


"Der fehlende Schlaf macht meine Gedanken träge, und es gibt nur ein Heilmittel dagegen; ein schönes, herzhaftes Frühstück."


$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_cafeteria onlayer master
with locationchange

"Es wäre schön, der Erste zu sein."


"Sich als Erster auf den dampfend heißen Berg aus Essen zu stürzen und zu sitzen, wo ich will…"


"Es wäre schön gewesen."


"Aber obwohl ich außergewöhnlich früh aufgestanden bin, bin ich hinter den fleißigsten Schülern zurückgeblieben."


"Ich schätze, hier stehen Einige früh auf – aus dem einen oder anderen Grund."


"Einige Schüler in Sportklamotten drängen sich um einen Tisch und diskutieren eifrig ihre Strategien, während sie zwischendurch Essen hinunterschlingen."


"In dem Speisesaal sind etliche verschlafene Schüler verteilt, die wahrscheinlich am selben Problem leiden wie ich – lautstarke Vögel."


"Und, natürlich, sind da noch die Leute, die es tatsächlich mögen, so früh aufzustehen. Diejenigen, deren Taschen mit Schulbüchern und fertigen Hausaufgaben vollgestopft sind."


"Es ist schwer, solche Leute nicht zu hassen. Sogar noch schwerer, wenn man selbst müde ist."


"Ich suche mir ein bekanntes Gesicht in der spärlichen Menschenmenge und gehe zum nächsten Tisch."


"Lilly sitzt dort allein und tastet behutsam mit ihrer Gabel auf einem kleinen Teller mit Eiern herum."


"Ihre Bewegungen sind präzise wie ein Uhrwerk. Es ist fast schade, sie zu unterbrechen."


"Ich frage mich, ob das die Art und Weise ist, wie Blinde mit ihren Gedanken abschweifen? Einfach Bewegungen in vorbestimmten Mustern folgen, die über Jahre hinweg erlernt wurden."
"So wie eine sehende Person essen würde, während sie eine Zeitung liest."


hi "Guten Morgen, Lilly. Hab nicht erwartet, dass du so früh hier bist."


show lilly basic_surprised onlayer master:
    center
    ypos 1.2
with charaenter

li "Oh, Hisao. Du hast mich erschreckt. Ich wusste nicht, dass du so früh frühstückst."


hi "Tu ich nicht. Das heute ist eine Ausnahme. Ich würde viel lieber zu spät zur Schule kommen als zu früh zum Frühstück."


show lilly basic_weaksmile onlayer master
with charachange

"Als ich beginne zu essen, seufzt Lilly leicht über meine offen zugegebene Unpünktlichkeit."


"Es dauert nicht lange, bis sie in ihr gedankenloses Dahinknabbern zurückfällt."


"Jeder kurzen Bewegung fehlt es an Energie. Ich nehme an, das ist ungefähr so, als würde man seine Augen herumwandern lassen, während man irgendwas Alltägliches macht."


"Aber nach ein paar Wiederholungen des Essen suchen/Essen finden Kreislaufs legt Lilly ihre Gabel ab und tupft sich ihre Lippen mit einer Serviette ab."


stop music fadeout 6.0
stop ambient fadeout 6.0

show lilly basic_concerned onlayer master
with charachange

li "Hisao, darf ich dir eine Frage stellen?"


"Verdammt. Alles, was ich will, ist etwas Essen und ungefähr vier Stunden Schlaf. Und niemand sagt „darf ich dir eine Frage stellen”, nur um eine einfache Frage zu stellen."


hi "Klar."


show lilly basic_listen onlayer master
with charachange

li "Siehst du Hanako als Freund?"


"Huh, das hört sich nach einer Suggestivfrage an."


hi "Ich… denke, ja. Warum fragst du?"


show lilly basic_weaksmile onlayer master
with charachange

li "Kein bestimmter Grund."


show lilly basic_displeased onlayer master
with charachange

play music music_serene fadein 8.0

li "Ich habe allerdings noch eine Frage. Warum siehst du sie als Freund?"


"Das geht weit über meinen Horizont hinaus. Was will sie von mir hören?"


hi "Ich weiß nicht genau. Ich glaube, es ist, weil sie ein bisschen anders ist, in ihrer Art mit Menschen umzugehen…"


show lilly basic_reminisce onlayer master
with charachange

li "Hmm. Seit ich sie kenne, hat sie nie wirklich Kontakte geknüpft."


show lilly basic_concerned onlayer master
with charachange

li "Sie scheint sich nicht für andere zu interessieren und ich glaube, ihre Erscheinung wirkt ein bisschen Abschreckend."


hi "Echt? Ich dachte, so was wollte man hier, na ja, vermeiden. Diskriminierung und so."


show lilly basic_listen onlayer master
with charachange

li "Hmm, wie soll ich sagen…"


"Nachdenklich runzelt sie ihre Stirn. Eine Bewegung, bei der ich leicht besorgt darüber bin, was sie für Gedanken spinnt."


show lilly basic_weaksmile onlayer master
with charachange

li "Ich würde sagen, du bist ein bisschen naiv."


"Naiv? Ich wäre beleidigt, wenn sie nicht ein zynisches Grinsen im Gesicht hätte."


hi "Ich… verstehe."


show lilly basic_reminisce onlayer master
with charachange

li "Obwohl Yamaku einen stärkeren Gemeinschaftssinn als andere Schulen hat, ist sie weit davon entfernt, konfliktfrei zu sein."


show lilly basic_displeased onlayer master
with charachange

li "Am Ende können Regeln die menschliche Natur nicht abschaffen – nur unterdrücken."


"Das habe sogar ich bemerkt."


"Nur kleine Sachen, wie zum Beispiel, dass sich bestimmte Leute und Cliquen in den Gängen aus dem Weg gehen. Es ist wirklich nicht anders als auf meiner alten Schule."


"Sogar Lilly und Shizune könnte man als bittere Rivalen bezeichnen, obwohl sie beide recht verständnisvolle Menschen sind."


"Na ja, zumindest die Misha-gefilterte Shizune; wer weiß, was wirklich mit ihren Fingern und hinter ihrer Brille abgeht."


hi "Ich glaube, du hast Recht. Aber als ich zuerst hierherkam, war alles ein bisschen schockierend."


hi "Ich habe die ganze Zeit Fehler gemacht, oder zumindest habe ich das gedacht. Wie zum Beispiel, als wir uns das erste Mal getroffen haben und ich „ich seh schon” zu dir sagte."


hi "Ich wusste nicht, ob das als unhöflich gilt, darum hab ich versucht, das einfach im Hinterkopf zu behalten. Menschen unterschiedlich behandeln und so."


hi "Also hab ich das nicht getan. Ich hab mir gesagt, dass Hanako und du und alle anderen einfach normal sind, und ich hab versucht, das Offensichtliche zu ignorieren."


hi "Ich redete mit Hanako wie mit jedem anderen auch, und darum sind wir Freunde geworden."


hi "Zumindest glaube ich, dass es so abgelaufen ist."


hi "Aber weißt du, allein dadurch, dass ich so etwas laut ausspreche, fühle ich mich schon schuldig."
hi "Als ob man sich besonders anstrengen müsste, um Hanako, oder dich, oder irgendjemanden hier als normal zu betrachten. Ich glaube nicht, dass das richtig ist."


show lilly basic_smileclosed onlayer master
with charachange

li "Hisao, ich glaube, du bist naiv – aber ich glaube auch, dass du ein guter Mensch bist. Das ist vielleicht eine deiner besseren Eigenschaften."


hi "Ich… vermute… ich kann das als Kompliment auffassen…"


show lilly basic_smile onlayer master
with charachange

li "Sag mal, bist du heute Abend frei?"


hi "Wenn Hausaufgaben nicht zählen, dann bin ich so frei wie der Wind."


show lilly basic_cheerful onlayer master
with charachange

li "Würdest du dann gerne mit Hanako und mir Tee trinken?"


hi "Äh, ich hab im Moment nicht so viel Geld. Ausgehen fällt daher…"


show lilly basic_smile onlayer master
with charachange

li "Oh, ich habe nicht gemeint, dass wir ausgehen. Nur hier, heute Abend."


hi "Man kann hier am Abend in die Klassenzimmer?"


show lilly basic_giggle onlayer master
with charachange

li "Nein, das meinte ich nicht. Hanako und ich machen oft zusammen Teepartys in meinem Zimmer. Bitte, komm ruhig nach Sonnenuntergang vorbei."


hi "Klar, das ist wohl kein Problem. Welche Zimmernummer hast du?"


show lilly basic_smileclosed onlayer master
with charachange

li "225, Zimmer 25 im zweiten Stock."



hi "Okay, geht klar."


show lilly basic_weaksmile onlayer master
with charachange

li "Na dann, ich sollte losgehen. Als Klassensprecherin habe ich vor dem Unterricht noch ein paar Dinge zu erledigen."


show lilly basic_cheerful onlayer master at center
with dissolvecharamove

li "Bis heute Abend, Hisao."


hi "Ja, bis später dann."


hide lilly onlayer master
with charaexit

stop music fadeout 8.0

"Moment mal… Ich bin gerade eingeladen worden, Abends das Zimmer eines Mädchens zu besuchen? Ist das überhaupt erlaubt?"


"Es gibt hier eine Ausgangssperre, aber ich habe noch nichts von Besuchsregeln für die Schlafzimmer gehört."


"Das ist genug, um mein unausgeschlafenes Gehirn wieder in Gang zu bringen."


"Dazu noch dieses lauwarme Frühstück, und schon bin ich putzmunter."


scene bg school_scienceroom onlayer master
with locationskip

"Widerwillig gehe ich zum Unterricht, immer noch ein bisschen aufgeregt bei der Aussicht darauf, die Regeln zu brechen."


"Ich fühle mich ein bisschen wie ein Kind, das vorhat, nachts aus seinem Fenster zu klettern."


"Na ja, das geht vielleicht ein bisschen zu weit, aber wenn man eine Einladung zu einer Party mit sechs bis sieben Stunden langen Vorlesungen vergleicht, dann weiß ich, was gewinnt."


"Misha und Shizune tun auch nur wenig, das meiner Langeweile Abhilfe verschafft. Sie sind ausnahmsweise mal dazu entschlossen, tatsächlich Mutous Aufgaben abzuarbeiten."


scene bg school_scienceroom_ss onlayer master
with shorttimeskip

play sound sfx_normalbell

"Dennoch neigt sich der Tag letztendlich seinem Ende zu."


scene bg school_dormhisao_ss onlayer master
with locationskip

"Ich eile in mein Zimmer, um mich zu waschen und meine Haare zu kämmen. Zum Glück bin ich nicht Kenji in die Arme gelaufen."


scene bg school_dormext_full_ss onlayer master
with locationchange

"Schon bald verlasse ich das Jungenwohnheim."




label de_H7:

scene bg school_girlsdormhall onlayer master
with locationskip

play sound sfx_doorknock2

"Nervös klopfe ich an die Tür mit der Nummer 225 und schaue noch einmal auf die Uhr."


li "Bist du das, Hisao? Die Tür ist auf, du kannst reinkommen."


"Lillys Stimme trällert durch die Tür und beruhigt meine Nerven."


"Das ist das erste Mal, dass ich nach Sonnenuntergang in das Zimmer eines Mädchens eingeladen wurde."


"Obwohl ich weiß, dass das eine Einladungen ohne Hintergedanken ist, hält das meine Fantasie nicht davon ab, angesichts der Möglichkeiten verrückt zu spielen."


"Ein Junge. Zwei Mädchen. In einem Zimmer. Mit einem Teeservice."


"Wenn ich es so sage, hört es sich leicht verdächtig an."


"Ich seufze leicht, um mich zu beruhigen, lege sachte meine Hand auf die Türklinke, öffne die Tür und recke meinen Kopf, um hineinzusehen."


play sound sfx_dooropen

window hide

scene white onlayer master
with dissolve

with Pause(0.1)

play music music_one fadein 10.0

scene ev lilly_bedroom onlayer master:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with Dissolve(4.0)

window show

"Die Tür öffnet sich ganz, und ich erhasche einen ersten Blick auf Lillys Zimmer."


"Ihre Einrichtung wirkt fast antik, aber die nackten Wände und matten Oberflächen sind kaum geschmückt. In der Mitte des Zimmers ist ein niedriger Tisch, auf dem ein kleines Teeservice steht."


"Es wirkt, als hätte alles in diesem Raum seinen eigenen Platz. Vielleicht mit Ausnahme der etlichen Bücherstapel, die an der Wand aufgestapelt sind."


"Mein Gesichtssinn ist nicht der einzige, der angeregt wird; es liegt ein schwacher Geruch in der Luft. Nagellack, Parfum, Schminke… Es fällt schwer, ihn anders zu beschreiben als „mädchenhaft”."


"Meine Augen verschaffen sich einen kurzen Überblick über das Zimmer, bevor sie sich auf die Mädchen richten."


scene ev lilly_bedroom_large onlayer master:
    xpos -130 ypos -400 subpixel True
    acdc_warp 4.0 ypos -600
with flash

"Lilly sitzt neben dem kleinen Tisch. Sie trägt einen sehr dunkelblauen Schlafanzug. Einen dunkelblauen Schlafanzug mit Shorts, die sehr viel von ihren verführerischen, hellen Beinen zeigen."


show ev lilly_bedroom_large onlayer master:
    ease 1.0 ypos -300 xpos -830
    acdc_warp 12.0 ypos 0 xpos -830
with None

"Ihr gegenüber sitzt Hanako in einem biederen, hellrosa Nachthemd."


"Ihre Hände liegen starr zwischen ihren Beinen, ihre Schultern sind nach vorne gerichtet und ihr Kopf nach unten. Als ob sie versuchen würde, sich darin zu verstecken."


"Sie könnte das leicht tun; es sieht aus, als wäre es zwei Nummern zu groß für sie."


"Wellen von Flanell legen sich über ihren Körper und lassen sie aussehen wie ein Kind, das mit den Kleidern seiner Eltern Verkleiden spielt."


"Sie sieht auf, um sicherzugehen, dass ich es bin. Die Züge eines dünnen Lächelns zeigen sich in ihrem Gesicht, bevor sie so schnell wieder verschwinden, dass ich mir gar nicht sicher bin, ob sie überhaupt da waren."


show ev lilly_bedroom_large onlayer master:
    ease 1.0 xpos -130 ypos -400
with None

li "Es bringt nichts, wenn du in der Tür stehenbleibst, Hisao."


scene bg school_dormlilly onlayer master
show lilly basic_smile_paj onlayer master:
    twoleft
    ypos 1.2
show hanagown distant onlayer master:
    tworight
    ypos 1.17
with locationchange

play sound sfx_doorclose
stop music fadeout 10.0

"Ich mache einen Schritt in dem Raum und schließe die Tür hinter mir."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Hmm, ich fürchte, das Zimmer ist wirklich etwas klein für uns Drei. Willst du dich setzen?"


"Langsam gehe ich zum Tisch und setze mich hin, wobei ich mir Mühe gebe, nichts umzustoßen."


"Außerdem kann ich nicht anders, als einen kurzen Blick in Lillys Oberteil zu werfen, als ich mich niedersetze."


"Ohne Augenlicht zu sein, wäre ein schreckliches Schicksal."


show lilly basic_smileclosed_paj onlayer master
with charachange

li "Also, wie wär's mit etwas Tee. Hanako, könntest du bitte einschenken?"


show hanagown normal_blush onlayer master
with charachange

ha "S-Sicher. Hi… sao… möchtest…"


show hanagown distant_blush onlayer master
with charachange

ha "… möchtest du…"


show hanagown worry_blush onlayer master
with charachange

ha "… möchtest du gerne…"


hi "Ich hätte liebend gerne etwas Tee. Brauchst du Hilfe?"


show hanagown normal_blush onlayer master
with charachange

ha "N-Nein, geht schon…"


show hanagown smile onlayer master
with charachange

ha "Danke…"


play music music_dreamy fadein 2.0

show lilly basic_giggle_paj onlayer master
with charachange

"Lilly fällt es bei der Nervosität ihrer Gefährtin schwer, ein Lächeln zurückzuhalten. Das kann ich ihr nicht wirklich verübeln."


show hanagown distant onlayer master
with charachange

hi "Anstrengender Tag?"


show hanagown smile onlayer master
with charachange

ha "J-Ja."


show lilly basic_smileclosed_paj onlayer master
with charachange

"Ich mache es mir auf meinem Platz gegenüber des Schranks gemütlich."


"Zu meiner Linken ist die in blau gekleidete Lilly, und zu meiner Rechten sitzt die rosarote Hanako."


show teaset onlayer master:
    xalign 0.5 yanchor 0.5 ypos 0.6 alpha 1.0
    easein 0.5 ypos 0.5
with charaenter

"Das Teeservice auf dem Tisch sieht sowohl nett als auch zweckmäßig aus; rot bemalt mit einem Blumenmotiv."


"Im Vergleich zu Lillys schlichter aber weitgehend niveauvoll wirkender Einrichtung sieht es merkwürdig aus, was mich darauf schließen lässt, dass Hanako es vielleicht ausgesucht hat."


"Es ertönt ein leises „Kling”, als Hanako beim Einschenken versehentlich mit der Teekanne an eine Tasse stößt."


show hanagown worry onlayer master
show lilly basic_displeased_paj onlayer master
with None

show teaset onlayer master:
    easeout 0.5 alpha 0.0 ypos 0.6
with Pause(0.5)

hide teaset onlayer master
with None

"Scharf atmet sie ein; sie muss wirklich nervös sein, da sich eigentlich niemand über so etwas Gedanken machen würde."


show hanagown worry_blush onlayer master
with charachange

"Hanako zittert wegen ihres Fehlers."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Schon okay, Hanako. Kein Grund, nervös zu sein."


show hanagown normal onlayer master
with charachange

"Hanako scheint durch Lillys beruhigende und sanfte Worte etwas Zuversicht zu finden und füllt geschickt die nächsten zwei Tassen."


show hanagown normal_blush onlayer master
with charachange

ha "Bitte sehr, Hisao… Lilly."


"Hanako stellt behutsam eine Tasse mit Untertasse vor Lilly und mich. An so einen Service könnte ich mich gewöhnen."


show lilly basic_smile_paj onlayer master
with charachange

li "Danke, Hanako."


hi "Ja, danke."


show hanagown smile onlayer master
with charachange

ha "B-Bitte."


show lilly basic_smileclosed_paj onlayer master
with charachange

"Lilly tastet nach ihrer Tasse, und als sie sie gefunden hat, nippt sie vorsichtig daran."


"Ich tue es ihr gleich. Dieser Tee schmeckt ein wenig besser als der Tee, den wir sonst in der Schule haben."


hi "Der ist gut. Er ist so anders als jeder Tee, den ich bisher getrunken habe…"


show lilly basic_ara_paj onlayer master
show hanagown normal_blush onlayer master
with charachange

li "Sieht so aus, als hättest du den richtigen ausgesucht, Hanako."


show lilly basic_smileclosed_paj onlayer master
with charachange

li "Gut gemacht, auch wenn es gewagt war."


show hanagown smile onlayer master
with charachange

"Hanakos Lächeln kommt zurück, doppelt so breit."


"Trotz ihres entstellten Gesichtes, könnte man ihr Lächeln nicht anders beschreiben als „süß”."


show hanagown distant_blush onlayer master
with charachange

ha "Ich bin froh, dass du ihn magst…"


"Hanako wird endlich lockerer und nimmt einen kleinen Schluck aus ihrer Tasse."



label de_H7a:

$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide
nvl clear
nvl show dissolve

n "Ich denke an das Gespräch mit Misha vor ein paar Tagen zurück."


n "Muss man sich über Hanakos Verhalten Sorgen machen? Oder ist sie einfach nur schüchtern?"


n "Und dann war da noch Lilly heute Morgen."


n "Sie schienen beide aufrichtig besorgt, und sie kennen die Situation besser als ich."


n "Aber, ernsthaft, wie könnte ich überhaupt helfen?"


n "Ich bin kein plastischer Chirurg, also kann ich bei ihrem Aussehen auch nicht helfen. Ein Psychologe, der sie kontaktfreudiger machen kann, bin ich auch nicht."


n "Also was zum Teufel wollen Lilly und Misha von mir?"


n "Es ist frustrierend. Hanako und ich werden von uns aus schnell zu Freunden, und deswegen ist es so, als würde jeder von mir wollen, dass ich all ihre Probleme löse."


n "Und ich habe keine Ahnung, wie ich das tun soll."


n "Niemand kann mein Herz heilen, oder Lillys Augen oder irgendwen, der an dieser Schule ist."


n "Ich sehe jedoch nichts Schlechtes darin, mich mit Hanako näher anzufreunden. Jetzt, wo sie sich mir mehr öffnet, gefällt es mir irgendwie, Zeit mit ihr zu verbringen."


$ renpy.music.set_volume(1.0, 1.0, channel="music")
nvl clear
nvl hide dissolve
window show



label de_H7b:

$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide
nvl clear
nvl show dissolve

n "\n\n\n\nIrgendetwas daran lässt mich über Lillys Frage beim Frühstück nachdenken."


n "Warum bin ich mit Hanako befreundet?"


n "Lilly scheint sich ernsthaft um Hanakos Wohlbefinden zu sorgen, aber es ist nicht so, als könnte ich irgendetwas tun, um ihr zu helfen."


n "Soweit ich sagen kann, wird sie von ihren Narben nicht körperlich behindert. Und jeder, den ich getroffen habe, scheint seine Behinderung bis zu einem gewissen Grad überwunden zu haben."


n "Ich habe keine Hintergedanken dabei, mit Hanako herumzuhängen, wir haben einfach nur ähnliche Interessen."


n "\nReicht das nicht?"


$ renpy.music.set_volume(1.0, 1.0, channel="music")
nvl clear
nvl hide dissolve
window show




label de_H7c:

show lilly basic_smile_paj onlayer master
with charachange

li "Also, Hisao, amüsierst du dich?"


"Lillys Worte reißen mich aus meinem Tagtraum, und ich brauche eine Sekunde, um mich zu erinnern, wo ich bin."


"Ich bin in einem Raum mit zwei Mädchen in ihren Schlafanzügen. So etwas sollte man genießen."


hi "Ja, es ist entspannend. Fast so, als wäre ich nicht mehr in der Schule. Macht ihr das öfter?"


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Ziemlich oft, aber nicht so oft, wie wir Tee im Schulgebäude trinken."


"Wenn man bedenkt, dass sie das fast jeden Tag machen, ist das keine große Überraschung."


"Als ich einen weiteren Schluck aus meiner Tasse nehmen will, merke ich, dass sie leider leer ist."


hi "Das war lecker. Danke Hanako, Lilly."


show hanagown smile onlayer master
with charachange

ha "Keine Ursache."


show lilly basic_smile_paj onlayer master
with charachange

li "Ja, du bist herzlichst willkommen, Hisao. Es ist schön eine dritte Person hier zu haben."


hi "Also, sobald ihr jemanden braucht, um diese Stelle zu füllen, bin ich jederzeit verfügbar. Jederzeit."


"In solchen Momenten muss man sicher gehen, dass man seinen Standpunkt klarmacht."


stop music fadeout 8.0
show lilly basic_sleepy_paj onlayer master
with charachange

"Lilly entfährt ein Gähnen, das sie erfolglos mit ihrer Hand versteckt."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Verzeihung. Ich glaube, ich bin ein bisschen müde."


show hanagown distant onlayer master
with charachange

ha "Ich glaube, wir sind alle ein bisschen müde…"


show lilly basic_ara_paj onlayer master
with charachange

li "Hmm… Ich glaube, du hast Recht, Hanako."


show lilly basic_weaksmile_paj onlayer master
with charachange

li "Wir sollten wirklich ins Bett; wir haben morgen alle Unterricht."


hi "Ja… Ich sollte gehen."


show lilly basic_smile_paj onlayer master
with charachange

li "Danke, dass du da warst, Hisao."


show hanagown normal onlayer master
with charachange

ha "D-Danke. Kommst du wieder?"


hi "Nicht einmal eine ganze Armee könnte mich davon abhalten."


show lilly basic_cheerful_paj onlayer master
with charachange

li "Ich bin beeindruckt von deiner Entschlossenheit, Hisao."


hi "So oder so, du hast Recht. Wir sollten besser los."


"Ich stehe auf und mache mich auf den Weg zur Tür."


show hanagown normal onlayer master at tworight
with dissolvecharamove

"Hinter mir steht Hanako vorsichtig auf."


"Ich bleibe stehen und sehe sie an."


hi "Kommst du mit mir mit?"


play music music_comedy fadein 0.5

show hanagown normal_blush onlayer master
with charachange

"Hanako wird sofort rot wie eine Tomate."


show hanagown distant_blush onlayer master
with charachange

ha "Nein… ich… nicht… Das ist… nicht mein…"


hi "Schon gut, ich mach nur Spaß."


show hanagown smile onlayer master
with charachange

ha "Oh… okay… Gute Nacht…"


show lilly basic_smileclosed_paj onlayer master
with charachange

li "Gute Nacht, Hanako. Gute Nacht, Hisao."


hi "Gute Nacht zusammen."


"Und damit ist unsere Teeparty vorbei."


scene bg school_girlsdormhall onlayer master
with locationchange

"Ich bin mir immer noch nicht sicher, ob es das ist, was ich laut Lilly für Hanako tun soll, aber ich will sie nicht enttäuschen."


"Ich warte, bis die Tür hinter uns zu ist, bevor ich mich zu Hanako drehe."


show hanagown distant_blush onlayer master
with charaenter

hi "Hey, Hanako, weißt du, du musst in meiner Gegenwart nicht nervös sein oder so."


hi "Ich meine, wir sind Freunde, oder?"


show hanagown normal_blush onlayer master
with charachange

ha "R-Richtig. Wir sind… Freunde."


hi "Wenn du jemals was unternehmen willst oder so, lass es mich wissen. Wir müssen immer noch unser die Schach-Revanche nachholen, weißt du noch?"


show hanagown distant onlayer master
with charachange

ha "S-Sicher…"


show hanagown normal onlayer master
with charaenter

ha "A-Aber ich glaube nicht, dass du gewinnst…"


hi "Es würde keinen Spaß machen, wenn es einfach wäre."


show hanagown smile onlayer master
with charachange

"Hanako entfährt ein gedämpfter Lacher, aber sie könnte genauso gut auch ausgeatmet haben."


ha "G-Gute Nacht Hisao…"


show hanagown invis onlayer master at tworight
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

hide hanako onlayer master
with None

stop music fadeout 5.0

"Mit diesen Worten zieht sich Hanako schnell in ihr Zimmer zurück, das neben Lillys liegt."


"Ich mache mich auf den Weg zurück in mein Zimmer, aber schon durch so etwas Simples wie Gehen werde ich müde."


scene bg school_dormhisao onlayer master
with locationskip

"Ich schaffe es gerade so zu meinem Zimmer, bevor mich eine Welle der Erschöpfung erfasst."


play sound sfx_switch

scene bg school_dormhisao_ni onlayer master
with Dissolve(0.2)

"Ich schleudere meine Schuhe weg, falle ins Bett und schlafe ein, sobald mein Kopf auf das Kissen trifft."


scene black onlayer master
with dissolve


label de_H8:

scene bg school_dormhallway onlayer master
with locationchange

"Ich ziehe meine Tür zu, bereit für einen weiteren Unterrichtstag."


show kenji invis onlayer master at twoleft
with None

show kenji neutral_close onlayer master at center
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

ke "Gut geschlafen?"


play music music_kenji fadein 0.5

"Das plötzliche Auftreten von Kenji lässt mich aufschrecken, und ich schaffe es nur mit Mühe, nicht mit ihm zusammenzustoßen."


"Ich weiß, dass er schlecht sieht, aber er kennt mich doch jetzt. Muss er mir immer noch so nahekommen?"


show kenji neutral onlayer master
with charadistant

hi "Oh. Ja. Wie ein Baby."


show kenji tsun onlayer master
with charachange

ke "Verdammt, warum sagen das alle? Hast du jemals ein Baby schlafen gehört?"


ke "Sie schreien. Die ganze Nacht. Jede Nacht. Babys schlafen nicht gut, nie."


"Und das war's mit meiner entspannten Stimmung. Ich muss daran denken, bei Kenji niemals Redewendungen zu benutzen."


hi "Schon gut, ich verstehe, was du meinst. Das war nur eine Redewendung."


show kenji neutral onlayer master
with charachange

ke "Ja, klar, wie auch immer. Wo warst du letzte Nacht? Jemand musste mir einen Gefallen tun, aber du warst nicht da."


"Für den Bruchteil einer Sekunde überlege ich, ob ich Kenji die Wahrheit sage; dass ich bei Hanako und Lilly war."


"Glücklicherweise vergeht dieser Bruchteil einer Sekunde so schnell, wie er gekommen war."


hi "Ich war bloß aus. Hab mich ein wenig in der Gegend umgesehen und so. Du weißt schon, Aufklärung."


show kenji happy onlayer master
with charachange

ke "Guter Mann, gut. Ich wusste, du bist einer, der vorausplant…"


hi "Wie auch immer, was war das für ein Gefallen?"


show kenji neutral onlayer master
with charachange

ke "Ich wollte mir was zu Essen holen, aber ich hab Kleingeld gebraucht."


hi "Warte, was? Ich hab dir letzte Woche Geld gegeben, und du hast es mir noch nicht zurückgezahlt!"


show kenji tsun onlayer master
with charachange

ke "Tz, und ich dachte schon, du wärst cool."


"Kenji fingert in seiner Hosentasche herum und zieht seine Brieftasche hervor."


"Während er die 400 Yen auszählt, kann ich eindeutig mindestens zwei 10.000-Yen-Scheine sehen."


hi "Hey, was soll das? Warum leihst du dir Geld von mir, wenn du so viel Kohle hast?"


"Kenji faucht ein bisschen, als er begreift, dass ich ihn durchschaut habe."


ke "Geh mir nicht auf die Nerven, Mann. Es bringt Unglück, einen großen Schein für weniger als die Hälfte seines Werts anzubrechen. Das ist der Grundsatz der Magnaten."


ke "Das Abendessen von gestern Nacht wird mir sieben Jahre Pech bringen. Sieben Jahre!"


show kenji happy onlayer master
with charachange

ke "Findest du nicht, dass das Grund genug ist, jemandem auszuhelfen? Meine Strafe wäre geringer, wenn ich das Zeug einfach gestohlen hätte."


"Mein gesunder Menschenverstand schreit mich an, etwas zu ihm zu sagen, aber zum Glück kann ich mich zurückhalten."


"Über so etwas mit Kenji zu reden, würde bloß zu noch mehr und noch komplizierteren Diskussionen führen."


hi "Ja, schätze, du hast Recht. Vielleicht solltest du so was besser planen?"


show kenji neutral onlayer master
with charachange

ke "Ja Mann, ich weiß. Aber ich hab einfach so viel zu tun, es ist anstrengend. Und du bist auch nicht mehr da, also bin ich auf mich allein gestellt."


ke "Wir sollten zusammenhalten wie Brüder, weißt du noch?"


hi "Ja ja, hab verstanden. Globale Verschwörung und so. Ich halt die Augen offen."


show kenji neutral_close onlayer master
with charachange

"Kenji kommt mir nah genug, dass ich einen Hauch seiner Knoblauchfahne abbekomme."


show kenji tsun_close onlayer master
with charachange

ke "Solltest du machen, Mann. Du verbringst schon weniger Zeit hier. Das ist das Erste, was die machen."


ke "Die versuchen, uns voneinander zu trennen. Teile und herrsche. Das hat Sun Tzu gesagt."


hi "Verstanden. Jetzt muss ich los. Ich hab Unterricht. Kommst du?"


show kenji neutral_close onlayer master
with charachange

ke "Nee, ich bin müde. Ich bin die ganze Nacht aufgeblieben, nur um sicherzugehen, dass nichts passiert, nachdem ich den Schein kleingemacht hab."


hi "Vernünftig wie immer, wie ich sehe."


show kenji tsun_close onlayer master
with charachange

ke "Wie auch immer. Nacht."


stop music fadeout 3.0

show kenji invis onlayer master at twoleft
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

"Kenji huscht zurück in sein Zimmer, und ich kann hören, wie er seine Schlösser zuschlägt, während ich den Gang entlanggehe."




label de_H9:

scene bg school_dormhallway onlayer master
with None

scene bg school_scienceroom onlayer master
show muto smile onlayer master at center
with shorttimeskip

play music music_daily fadein 4.0

mu "… das ist der Grund, warum manche Leute ihre Zunge nicht einrollen können, oder warum ihr zweiter Zeh länger ist als ihr großer Zeh."


"Mutou schenkt uns ein halbmondförmiges Lächeln. Er ist offensichtlich Stolz auf seine Ausführung über rezessive Gene."


"Aber egal wie beeindruckt er von der Wissenschaft ist, die beschreibt, was wir sind – das Klassenzimmer scheint in einen Dämmerzustand gefallen zu sein."


"Warum ist es so, dass eine schlechte Erklärung sogar die interessantesten Dinge wertlos erscheinen lässt?"


show muto irritated onlayer master
with charachange

"Ich kann sehen, wie Mutou in sich zusammenfällt, als er begreift, dass nichts von dem, was er in der letzten halbe Stunde gesagt hat, angekommen ist."


$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 4.0

"Geflüsterte Gespräche unterbrechen die Stille, und wie eine Lawine wird der Geräuschpegel immer lauter."


show muto normal onlayer master
with charachange

"Geschlagen gibt uns Mutou ein paar Fragen aus dem Buch auf und macht sich daran, die Tafel sauberzumachen."


hide muto onlayer master
with charaexit

"Fast wie erwartet packt Hanako ihre Sachen zusammen und geht, sobald Gespräche und Gelächter zu hören sind."


"Der anfängliche Schock zu beobachten, wie jemand so offen die Schule schwänzt, ebbt langsam ab, aber das hält mich nicht davon ab, mir Gedanken zu machen."


"Geht sie, weil sie nicht will, dass jemand mit ihr spricht? Oder ist es nur der Gedanke, dass Menschen in ihrer Nähe ihre Ruhe zunichte machen?"


play sound sfx_normalbell
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

"Bevor ich weiter darüber nachdenken kann, klingelt die Mittagsglocke. Ich frage mich, ob sie einfach die Gelegenheit genutzt hat, um früher zu gehen."


"Der übliche Lärm von Studenten, die Bücher fürs Mittagessen austauschen, hallt durch den Raum. Während Misha abgelenkt ist, schnappe ich mir mein Mittagsessen und verlasse den Klassenraum."


stop ambient fadeout 1.0

scene bg school_miyagi onlayer master
show lilly basic_smileclosed onlayer master:
    center
    ypos 1.2
with locationskip

"Lilly sitzt schon im Teezimmer und breitet allein das Mittagessen aus."


hi "Hanako ist also noch nicht hier?"


show lilly basic_smile onlayer master
with charachange

li "Oh, Hisao, wie geht's dir? Ich habe Hanako seit heute morgen nicht getroffen, fürchte ich."


"Stimmt, Hanako und Lilly wohnen nebeneinander."


"Irgendwie glaube ich, dass ihre Morgengespräche ein wenig vernünftiger sind als Kenjis Gefasel."


hi "Das ist komisch. Sie ist früh aus dem Unterricht raus, da dachte ich, sie würde hierherkommen."


show lilly basic_displeased onlayer master
with charachange

li "Sie verlässt den Unterricht also immer noch früher…"


hi "Hä? Ja, ich hab das ein paar Mal bei ihr gesehen."


show lilly basic_sad onlayer master
with charachange

stop music fadeout 7.0

"Lilly lässt ihren Kopf ein bisschen hängen, und ihre Stimme klingt besonders niedergeschlagen. Es erinnert sehr an jemanden, der es gewohnt ist, schlechte Nachrichten zu hören."


li "Ich war mir so sicher, dass sie damit aufhören würde, als ihr Zwei Freunde geworden seid."


show lilly basic_weaksmile onlayer master
with charachange

li "Jeder hat so sein eigenes Tempo, nehme ich an."


hi "Na ja, ich hab darüber heute selbst schon nachgedacht. Warum genau geht sie denn?"


show lilly basic_reminisce onlayer master
with charachange

li "Da bin ich mir selbst nicht ganz sicher. Ich persönlich glaube, dass sie nicht in eine Situation kommen will, in der sie mit jemandem reden muss."


"Ich erinnere mich an unser erstes Treffen, als ich dachte, sie sieht aus wie ein in die Ecke getriebenes Tier. Vielleicht war das nicht weit von der Wahrheit entfernt."


hi "Aber es scheint für sie in Ordnung zu sein, mit dir zu reden, und mit mir… ein bisschen…"


show lilly basic_displeased onlayer master
with charachange

li "Es ist ein bisschen komplizierter. Ich denke, das Erste, wonach die meisten Menschen sie fragen, sind wahrscheinlich ihre Narben und die Geschichte dahinter."


li "Sie spricht mit mir selten darüber, aber ich habe mitbekommen, dass sie nicht gerne daran zurückdenkt. Was auch immer damals passiert ist."


show lilly basic_reminisce onlayer master
with charachange

li "Den Unterricht verlassen und vor Gesprächen davonlaufen ist ihre Vorsorgemaßnahme, wenn man so will."


hi "Hm… und wie erklärt das dann, dass sie mit mir spricht?"


show lilly basic_weaksmile onlayer master
with charachange

li "Du hast es gestern beim Frühstück selbst gesagt; du hast versucht, ihre Narben zu ignorieren. Sobald sie gemerkt hat, dass du sie nicht danach fragen wirst, wurde sie dir gegenüber offener."


hi "Hm, ich glaube, du hast Recht. Vielleicht. Ich weiß nicht. Du kennst sie besser als ich, darum verlasse ich mich auf dich."


play music music_normal fadein 3.0

show lilly basic_giggle onlayer master
with charachange

li "Ich würde mir darüber keinen Kopf machen. Ich bin sicher, du wirst sie bald genauso gut kennen wie ich."


show lilly basic_smileclosed onlayer master
with charachange

li "Ich freue mich über die Aussicht auf einen neuen Freund für sie. Ihr Zwei habt so ähnliche Interessen…"


hi "Na ja, Lesen ist nicht wirklich ein Mannschaftssport. Es ist allerdings schön, Gesellschaft zu haben."


show lilly basic_smile onlayer master
with charachange

li "Darauf will ich hinaus. Hanako ist im Herzen immer noch ein normaler Mensch. Sie mag in solchen Zeiten auch Gesellschaft."


hi "Hm, verstehe. Glaube ich. Um ehrlich zu sein, verwirrt ihr beide mich immer noch ein bisschen."


show lilly basic_smileclosed onlayer master
with charachange

li "Das ist nur natürlich, Hisao. Wir kennen uns noch nicht so lange; es ist unsinnig zu erwarten, dass du uns verstehst, genauso wie wir dich nicht verstehen können."


show lilly basic_weaksmile onlayer master
with charachange

li "Aber beim Freunde werden ist das doch der halbe Spaß, oder?"


hi "Ja, ja das ist es."


show lilly basic_giggle onlayer master
with charachange

li "Obwohl… ich nehme an, da ist die Sache, dass wir unterschiedlichen Geschlechts sind. Männer und Frauen scheinen sich einander recht oft zu verwirren."


"Während sie das sagt, kichert sie leicht bei dem Gedanken an die merkwürdigen kleinen Details des Lebens."


show lilly basic_cheerful onlayer master
with charachange

li "Ich hoffe, es stört dich nicht, aber ich fange jetzt an zu essen."


hi "Nein, mach nur. Ich glaube, ich esse auch was. Ich hab ein paar Bücher, die ich noch in der Bibliothek abgeben will, bevor der Unterricht anfängt; ich leg also besser los."


show lilly basic_smileclosed onlayer master
with charachange

li "Da findest du wahrscheinlich auch Hanako. Falls du sie siehst, kannst du ihr sagen, dass sie heute Nacht noch bei mir vorbeischauen soll? Ich würde gerne mit ihr reden."


hi "Du kommst nicht mit?"


show lilly basic_weaksmile onlayer master
with charachange

li "Leider ist nachher eine Klassensprechersitzung. Ich bin also weg, sobald ich mit dem Essen fertig bin."


hi "Okay, falls ich sie in der Bibliothek nicht treffe, dann sage ich es ihr im Unterricht. Ich bin sicher, sie ist nach dem Mittagessen wieder da."


"Als wir anfangen zu essen, werden wir still, und ich denke kurz über unser Gespräch nach."


"Ich dachte immer, dass Hanakos Schüchternheit daher kommt, weil sie wegen ihrer Narben unsicher ist."


"Aber das ist eine ziemlich oberflächliche Betrachtungsweise."


"Gerade als ich dachte, ich hätte den Durchblick bei Lilly und Hanako, stelle ich fest, dass ich noch weiter davon entfernt bin als am Anfang."


"Wegen ihrer Sitzung isst Lilly schnell auf. Ich mache ihr keine Vorwürfe."


"Shizune ist höchstwahrscheinlich dort, und ich bezweifle, dass sie ihr die Genugtuung eines neuen Streits geben will."


show lilly basic_smile onlayer master
with charachange

li "Ich muss los. Morgen gleiche Zeit?"


hi "Gleiche Zeit, gleicher Ort. Ich sollte besser auch los; ich will nicht zu spät kommen."


show lilly cane_smileclosed onlayer master
with charachange

show lilly cane_smileclosed onlayer master at center
with charamove

stop music fadeout 4.0

"Lilly lächelt sanft, nimmt ihren Gehstock und geht hinaus auf den Gang."




label de_H10:

scene bg school_hallway2 onlayer master
with locationchange

"Ich drehe Lilly meinen Rücken zu, als wir in entgegengesetzte Richtungen gehen. Aus irgendeinem Grund hoffe ich, dass sie nicht wieder in einen Streit mit Shizune gerät."


"So sehr ich Lilly auch mag, Shizune und Misha waren mir sehr behilflich dabei, mich einzufinden – selbst wenn die Hälfte unserer Gespräche aus schlecht verschleierten Versuchen besteht, mich anzuwerben."


"Andererseits kenne ich sie beide kaum. Vielleicht waren sie ja früher mal Anführerinnen irgendeines Geheimbundes, aber ihre Liebe zueinander trieb sie auseinander…"


"Mann, ich muss aufhören, billige Romane zu lesen. Das lässt mein Hirn eingehen. Entweder das, oder ich muss von Kenji und seinem schlechten Einfluss wegkommen."


"Es ist traurig, dass ich beides kaum mehr unterscheiden kann."


scene bg school_library onlayer master at right
with locationskip

play music music_happiness fadein 2.0

"Ich lasse meine Bücher in den Rückgabekorb fallen. Ihr Aufprall macht ein befriedigendes Geräusch."


play sound sfx_impact2

show yuuko panic_up onlayer master
with vpunch

"Yuuko scheint jedoch nicht so begeistert zu sein wie ich."


yu "H-Hisao! Du hast mich erschreckt!"


hi "Entschuldige, ich dachte, du wärst daran mittlerweile gewöhnt. Oder ist die Analphabetenquote hier so hoch, dass sich niemand Bücher ausleiht?"


show yuuko worried_up onlayer master
with charachange

yu "Was? Nein, ich glaube, jeder hier kann einwandfrei lesen…"


hi "Ja… schon gut."


"Es gibt manche Schlachten, die man nicht gewinnen kann. Witze zu erklären, ist eine davon. Mein Vater hat mir das auf die harte Tour gezeigt."


hi "Sag mal Yuuko, hast du Hanako gesehen? Sie ist früher aus dem Unterricht raus, aber sie war nicht in ihrem üblichen Versteck."


show yuuko closedhappy_down onlayer master
with charachange

yu "Ich glaube, ich hab gesehen, wie sie sich vor dem Mittagessen reingeschlichen hat."


show yuuko panic_up onlayer master
with charachange

yu "Oh! Aber ich sollte das niemandem sagen!"


hi "Ich hab dir gerade erzählt, dass ich gesehen hab, wie sie gegangen ist. Kein Grund, hysterisch zu werden…"


show yuuko smile_down onlayer master
with charachange

yu "Oh… natürlich. Sie ist wahrscheinlich hinten."


hi "Danke. Sind in letzter Zeit neue Bücher reingekommen?"


show yuuko worried_up onlayer master
with charachange

yu "Nein, tut mir leid. Ich lasse es dich aber wissen, wenn wir welche bekommen."


hi "Okay."


"Wenn ich eines über Bibliothekare weiß, Teilzeit oder sonst wie, ist es, dass sie Leute schätzen, die ehrliches Interesse an ihrer Arbeit haben."


hide yuuko onlayer master
with charaexit

show bg school_library onlayer master at Fullpan(10.0, dir="left")
with None

"Ich gehe den mir jetzt bekannten Weg entlang zu Hanakos Leseecke, wobei ich ein paar Bücher mitnehme."


"Manchmal ist es schwer für mich, ein Buch in den Regalen zu entdecken, das mich interessiert. Der Name eines Autors und ein Titel bestehend aus zwei Wörtern sagen in einem Meer aus Wörtern, die sich ähneln, nicht viel aus."


"Deswegen lese ich manchmal Bücher erneut, die ich schon einmal gelesen habe. Besser auf ein Lieblingsbuch gesetzt als auf einen Neuling."


"Ein unbekannter Titel eines bekannten Autors lugt zwischen den Buchrücken seiner Nachbarn hervor. Ich nehme das Buch aus dem Regal."


"Wenigstens kenne ich das Buch selbst noch nicht."


scene ev hana_library_read_std onlayer master
with locationskip

"Wie erwartet sitzt Hanako, tief in einer Ausgabe von „Dance Dance Dance” versunken, auf ihrem Sitzsack."


hi "Hi Hanako. Wie geht's?"


"Ich kämpfe gegen Drang an nachzufragen, warum sie den Unterricht früher verlassen hat. Wenn Lillys Vermutung richtig ist, dann könnte danach zu fragen den gegenteiligen Effekt haben."


"Besser ich lasse es für den Moment sein. Manchmal ist der beste Weg, eine Antwort von jemandem zu bekommen, nie danach zu fragen."


show ev hana_library_smile_std onlayer master
with charachange

ha "Hallo, H-Hisao. Mir geht's gut."


"Irgendetwas stimmt nicht, und nach ein paar Sekunden begreife ich, was es ist. Hanako lächelt."


"Sie sieht aus, als wäre sie erfreut, mich zu sehen. Es ist eine schöne Abwechslung zu der gewohnten, instinktiv verängstigten Reaktion. Und es ist etwas, von dem ich hoffe, mehr davon zu sehen, wenn wir uns besser kennenlernen."


hi "Schön zu hören. Wie ist das Buch? Hab gehört, es sei eine echte Erfahrung."


ha "E-Es ist gut… glaube ich."


ha "Ich hab gerade erst angefangen, daher weiß ich n-nicht wirklich."


hi "Verständlich. Halt mich auf dem Laufenden; ich leihe es mir vielleicht aus, wenn du fertig bist."


ha "S-Sicher."


"Es sind noch gut fünfzehn Minuten von der Mittagspause übrig. Nicht genug, um so richtig in ein Buch einzutauchen, aber zu viel, um nur herumzustehen und nichts zu tun."


show ev hana_library_read_std onlayer master
with charachange

"Und Hanako liest schon wieder, da glaube ich kaum, dass ich ein Gespräch mit ihr anfangen kann."


"Tja, ich mache es mir wohl besser gemütlich."


play sound sfx_pillow

"Ich setze mich auf einen Sitzsack und schlage mein Buch auf."


"Der vertraute Stil des Autors springt mir schon ab der ersten Zeile entgegen. Als die Sätze zu Absätzen werden, werde ich ein bisschen lockerer."


stop music fadeout 8.0

"Aber egal wie ich es versuche, ich schaffe es irgendwie nicht, in die Atmosphäre des Buches einzutauchen."


"Zum Teil weil ich kaum Zeit habe, aber noch ablenkender ist Hanako."


show ev hana_library_std onlayer master
with charachange

show ev hana_library_read_std onlayer master
with charachange

"Ungefähr alle zehn Sekunden schielt sie über ihr Buch, aber wenn unsere Blicke sich treffen, duckt sie sich schnell wieder dahinter."


"Ich schätze, sie wollte doch über etwas reden."


scene bg school_library onlayer master
with locationskip

hi "Was ist los? Du siehst aus wie ein Erdmännchen, das Ausschau hält."


show hanako emb_blushing onlayer master:
    center
    ypos 1.17
with charaenter

ha "N-… es ist nichts."


hi "Ich hab's dir schon mal gesagt, „nichts” heißt „etwas”, wenn du es so sagst."


show hanako cover_worry onlayer master
with charachange

"Hanako windet sich ein wenig auf ihrem Sitzsack, in der Hoffnung, durch einen Positionswechsel die Wörter zu finden, die sie sucht."


show hanako emb_downsad onlayer master
with charachange

ha "Ich… ich hatte einen Unfall."


hi "Unfall? Gerade eben? Bist du in Ordnung?"


show hanako emb_sad onlayer master
with charachange

"Hanako schüttelt ihren Kopf, und ihre Haare wallen in violetten Haarbüscheln über einen Hintergrund aus blassem und dunklem Fleisch um ihre Schultern."


show hanako emb_downsad onlayer master
with charachange

ha "N-Nein. Als ich kleiner war."


play music music_hanako

"Die Erkenntnis trifft mich wie ein Schlag ins Gesicht."


ha "Als… als ich…"


hi "Ist schon gut, Hanako. Du musst mir nichts erzählen, wenn du nicht willst…"


"Wieder schüttelt sie ihren Kopf."


show hanako emb_sad onlayer master
with charachange

ha "N-Nein. Ich will… Ich muss es dir sagen."


scene ev hanako_crayon1 onlayer master:
    truecenter zoom 1.0 subpixel True
    linear 20.0 zoom 1.05
with locationskip

ha "Als ich klein war… hat es bei uns gebrannt."


ha "M-Mein Haus b-brannte ab, und ich… ich habe es fast nicht überlebt."


show ev hanako_crayon2 onlayer master:
    linear 8.0 zoom 1.05
with charachange

ha "D-Danach… war ich allein…"


scene bg school_library onlayer master
show hanako emb_downsad_close onlayer master:
    center
    ypos 1.1
with locationskip

"Hanakos Augen glänzen im trüben Licht der Bibliothek, und ich greife nach ihrer Hand."


hi "Schon gut, Hanako. Du musst nicht weitererzählen."


show hanako emb_sad_close onlayer master
with charachange

ha "A-Aber… ich muss…"


hi "Warum? Was ist der Grund?"


show hanako cover_distant_close onlayer master
with charachange

ha "L-Letzte Nacht hat Lilly mir v-von deinem Herzen erzählt…"


show hanako cover_worry_close onlayer master
with charachange

ha "U-Und ich… ich dachte, das ist nicht f-fair."


hi "Fair?"


show hanako emb_blushing_close onlayer master
with charachange

ha "D-Dass ich über dich Bescheid wusste, a-aber du nicht über mich…"


"Ich drücke Hanakos Hand etwas fester."


hi "Red keinen Unsinn. Aber ja, ich habe ein Herzleiden."


"Ich lehne mich etwas näher zu Hanako."


hi "Was ich Lilly nicht gesagt habe, ist, dass ich meinen ersten Herzanfall hatte, als ein Mädchen mir ihre Liebe gestanden hat."


"Ich lächle ein bisschen, um die Spannung zu lösen."


show hanako cover_worry_close onlayer master
with charachange

ha "E-Echt?"


hi "Echt. Ich hab aber schon eine Weile nichts von ihr gehört, darum denke ich, dass der Zug wohl abgefahren ist."


"Ich weiß, dass er abgefahren ist. Was das letzte Mal passiert ist, als ich sie gesehen habe, kann man einfach nicht anders interpretieren."
"Nichts mehr von ihr zu hören, hat mir in mancher Hinsicht geholfen, diese Phase meines Lebens hinter mir zu lassen."


hi "Also, jetzt wissen wir beide etwas mehr über den anderen. Aber du musst nicht darüber reden, wenn du nicht willst."


"Tatsächlich fühle ich mich ein bisschen schlecht dabei, nur über den ganzen Vorfall nachzudenken. Ich spüre geradezu, wie die Desinfektionsmittel des Krankenhauses wieder in meiner Nase brennen."


"Ich kann mir vorstellen, dass Hanako gerade das gleiche durchmacht."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nAls ich im Krankenhaus war, bin ich einmal zur Station für Brandverletzte gegangen – nur einmal. Mir war langweilig, also habe ich einen Spaziergang durch alle Stationen gemacht."


n "Ich ging durch die Onkologie und war der Meinung, ich könnte es aushalten. Aber als ich zu den Brandverletzten kam, machte ich kehrt und ging zurück zu meinem Bett."


n "Wenn man daran denkt, dass Hanako Monate an so einem Ort verbracht hat und nichts als verbrannte Haut, starke Desinfektionsmittel und sterilisierte Luft gerochen hat…"


n "Die wirklich schweren Fälle wurden in isolierten Kapseln behandelt, in die nichts von außen eindringen konnte. Das hätte bedeutet, ohne Lesen auskommen zu müssen."


n "\nIch wäre durchgedreht, hätte ich im Krankenhaus nicht meine Bücher gehabt."


n "Und sie sagte, sie war allein…"


n "Sind ihre Eltern gestorben? Ich muss Lilly danach fragen. Ich kann mir vorstellen, dass ich aus Versehen etwas Dummes sage."


stop music fadeout 2.0

nvl clear
nvl hide dissolve

show hanako emb_timid_close onlayer master
with charachange

window show

ha "D-Danke, Hisao."


show hanako emb_downtimid_close onlayer master
with charachange

ha "Ich… ich hab nicht vielen Leuten davon erzählt."


hi "Um ehrlich zu sein, hab ich auch nicht vielen Leuten von meinen… Umständen erzählt."


show hanako cover_smile_close onlayer master
with charachange

ha "D-Dann werde ich es auch n-niemandem sagen."


hi "Abgemacht."


play sound sfx_warningbell

"Ich ändere meinen Griff um Hanakos Hand in ein Händeschütteln, als die Schulglocke durch das Fenster tönt."


hi "Na dann gehen wir besser zurück zum Unterricht, was?"


show hanako basic_bashful_close onlayer master
with charachange

ha "S-Sicher."

$ renpy.music.set_volume(1.0, 0.0, channel="music")

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
