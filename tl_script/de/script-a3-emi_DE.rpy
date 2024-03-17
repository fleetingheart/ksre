label de_E16:

window hide None

scene bg school_scienceroom onlayer master
with fade

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 3.0

n "\n\n\nMutous ganzen Unterricht hindurch dreht sich mir alles."


n "Ich gehe heute Abend aus."


n "Mit Emi."


n "Und sie will sogar meine Freundin sein."


n "Ein Date…"


n "Und dann hat sie mich geküsst."


n "Dieser Kuss. Immer wieder denke ich daran zurück, spiele ihn in meinen Gedanken wieder und wieder ab."


n "Alles an diesem Moment fühlte sich so richtig an."


n "\nIch drifte ab, versunken in Gedanken an Emi."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve
window show

show muto normal onlayer master
with charaenter

mu "Nakai? Hallo?"


"Es scheint, als wäre ich ein wenig zu weit abgedriftet."


hi "Hä? Was?"


show muto irritated onlayer master
with charachange

mu "Oh Schreck! Ein Fall von Amnesie!"


mu "Kann jemand schnell den Chefpfleger holen?"


"Die Klasse lacht über Mutous Scherz."


hi "Tut mir leid."


show muto normal onlayer master
with charachange

mu "Hmm, kommt nicht wieder vor und so, richtig?"


hi "Genau."


"Mutous Gesichtsausdruck hellt sich deutlich auf."


show muto smile onlayer master
with charachange

mu "Nun, das ist schön zu hören!"


mu "Wäre doch schlimm, wenn mein Musterschüler sich plötzlich hängen lassen würde, oder?"


hide muto onlayer master
with charaexit

"Ich denke, meine Leistungen waren in Ordnung, aber zum Musterschüler reicht es doch sicher nicht, oder?"


"Ich bin mir ziemlich sicher, dass das ein Fach ist, in dem jeder einigermaßen gut ist. Man muss doch nur Formeln auswendig lernen."


"Wie ich versprochen habe, gelingt es mir für den Rest der Stunde, aufmerksam zu sein."


stop music fadeout 2.0

show muto normal onlayer master
with shorttimeskip

play sound sfx_normalbell

mu "Nakai, kann ich mal kurz mit dir reden?"


"Ob ich jetzt Ärger kriege wegen vorhin?"


hi "Äh, klar."


hi "Ist es wegen vorhin?"


show muto irritated onlayer master
with charachange

"Mutou sieht einen Moment lang aufrichtig verwirrt aus."


mu "Wie bitte?"


"Er legt seinen Kopf zur Seite und denkt einen Moment lang nach."


show muto smile onlayer master
with charachange

mu "Ach das! Nein, nein, das hat damit gar nichts zu tun."


mu "Ich wollte dich nur etwas fragen."


hi "Worum geht's?"


show muto normal onlayer master
with charachange

mu "Nichts Schlimmes, ich habe mich nur gefragt, wie deine Pläne für die Zeit nach dem Abschluss aussehen."


play music music_another fadein 2.0

mu "Willst du studieren?"


hi "Ja, ich denke schon. Ich wüsste nicht, was dagegen sprechen sollte."


mu "Schon darüber nachgedacht, was du studieren willst?"


hi "Noch nicht wirklich, nein. Ich dachte, mir fällt schon was ein, wenn es soweit ist."


show muto smile onlayer master
with charachange

"Mutou lacht."


mu "Du nimmst die Dinge, wie sie kommen, hm?"


mu "Ich würde dir ja davon abraten, aber das ist genau das, was ich auch gemacht habe, als ich zur Uni gegangen bin."


mu "Na ja, nicht wirklich."


mu "Ich wusste, dass ich eine Naturwissenschaft studieren wollte, aber ich war mir nicht sicher welche."


mu "Bin dann bei Physik gelandet, aber es hätte genauso gut Astronomie oder sonst was werden können."


show muto irritated onlayer master
with charachange

mu "Ehrlich gesagt habe ich erst mit Chemie angefangen, aber es gab so viele…"


"Mutou verstummt und runzelt die Stirn."


"Es dauert einen Moment bis er den Faden wiedergefunden hat, und ich warte geduldig, bis er fortfährt."


show muto normal onlayer master
with charachange

mu "Na ja, jedenfalls habe ich auch eine Menge Physik gemacht, weil mich das interessiert hat, aber ich war mir nicht sicher, ob das was für mich ist."


show muto smile onlayer master
with charachange

mu "Also bin ich zur Chemie zurückgekehrt und jetzt bin ich hier, nicht wahr?"


show muto smile onlayer master
with charachange

"Er lächelt mich enthusiastisch an, als ob er von mir erwarten würde, dass ich bestätige, dass wir hier sind."


"Irgendwie habe ich das Gefühl, dass Mutou mit diesem Gespräch auf irgendetwas hinaus wollte, aber ich kann mir beim besten Willen nicht denken worauf."


hi "Tut mir leid, ich kann Ihnen nicht folgen."


"Mutou runzelt die Stirn, kratzt sich am Kinn und schaut mich verblüfft an. Dann schnippt er mit den Fingern, als ob ihm gerade wieder eingefallen wäre, worauf er hinaus wollte."


mu "Richtig! Ja! Du!"


hi "Ich?"


mu "Ja! Du solltest dir überlegen, eine Naturwissenschaft zu studieren!"


mu "Du bist fantastisch darin."


mu "Es sei denn, du würdest lieber direkt Mathematik studieren."


show muto irritated onlayer master
with charachange

"Mutou zieht eine Grimasse."


mu "Bin kein großer Fan von reiner Mathematik. Ich mochte die Experimente immer lieber als die Beweise."


hi "Sie meinen, ich sollte an der Universität Naturwissenschaften studieren?"


"Die Frage scheint Mutou aus dem Konzept zu bringen."


show muto normal onlayer master
with charachange

mu "Na ja, so was in der Richtung."


show muto smile onlayer master
with charachange

mu "Du könntest auch dem Naturwissenschaftsklub beitreten!"


mu "Das Problem ist, dass es nicht wirklich einen Naturwissenschaftsklub gibt."


mu "Aber es könnte einen geben!"


mu "Du könntest sogar ein Gründungsmitglied sein!"


mu "Ein Gründervater!"


mu "Natürlich müsstest du noch weitere Mitglieder finden."


show muto normal onlayer master
with charachange

mu "Na ja, nur wenn du willst."


mu "Wir könnten auch erst mal nur zu zweit anfangen."


mu "Und, äh…"


show muto smile onlayer master
with charachange

mu "Ich könnte dir Sachen zum Lesen geben, und dann könnten wir darüber sprechen."


mu "Äh, und ich könnte dir auch helfen, dich auf die Universität vorzubereiten und so was."


show muto irritated onlayer master
with charachange

mu "Warte mal!"


"Mutou kramt in seiner Aktentasche herum und wirft mir ein Buch zu."


show muto smile onlayer master
with charachange

mu "Lies das."


mu "Wenn du es interessant findest, können wir es besprechen."


"„Eine Kurze Geschichte der Zeit?”"


"Ich weiß nicht, ob ich das wirklich lesen will, aber Mutou scheint ziemlich enthusiastisch zu sein."


hi "Worum geht's da?"


show muto normal onlayer master
with charachange

mu "Raum. Zeit. Raumzeit. Schwarze Löcher und so was."


mu "Und es ist gar nicht langweilig. Du sollst nur mal reinschauen, ob dich so was interessiert, verstehst du?"


mu "Bleib nach dem Unterricht einfach noch einen Moment da, dann können wir darüber reden, oder ich zeige dir im Labor, wie man Sprengstoff herstellt."


show muto smile onlayer master
with charachange

"Er winkt ab, als er meinen fragenden Gesichtsausdruck bemerkt."


mu "Nur ein Scherz, tut mir leid."


mu "Na ja, ich habe dich, glaube ich, fürs Erste lange genug aufgehalten."


mu "Mach dir Gedanken über eine Karriere als Naturwissenschaftler. Ich glaube, du hättest Spaß daran."


hi "Äh, okay. Mach ich. Danke für das Buch."


stop music fadeout 14.0

scene bg school_hallway3 onlayer master
with locationchange

"Ich verlasse den Klassenraum und schaue auf die Uhr. Noch viel Zeit totzuschlagen, bis Emi mit dem Training fertig ist."


"Dann werde ich mir dieses Buch wohl mal anschauen… Ich sollte wahrscheinlich auch duschen."


"Es gehört sich doch, vor einem Date zu duschen, oder?"


"Ich gehe zurück zum Wohnheim."


scene bg school_dormhisao onlayer master
with locationskip

"Ich frage mich sowieso, wo ich Emi treffen soll."


"Sie sagte „nach dem Training”, aber sie sagte nicht, wo wir uns treffen."


"Ich denke, ich sollte einfach am Sportplatz vorbeischauen; das ist wahrscheinlich sowieso das Beste."


"Wenn sie noch duschen muss, kann ich ja einfach in ihrem Zimmer warten oder so."


"Oder im Flur – ich denke, das wäre wohl besser."


"Ich gehe kurz duschen und nehme danach meine Medikamente."


"Und nun zu diesem Buch."


stop music

scene black onlayer master
with dissolve


label de_E17:

scene black onlayer master
with None

scene bg school_dormhisao onlayer master
with vpunch

"Ich wache erschrocken auf."


"Verdammt! Wie spät ist es?"


"Ein Blick auf die Uhr und ich stelle fest, dass ich fast eine Stunde geschlafen habe."


hi "Gott sei Dank."


"Emis Training sollte bald fertig sein."


"Ich ziehe meine Freizeitklamotten an und gehe zum Sportplatz."


scene bg school_track onlayer master
with locationskip

"Irgendwie habe ich das Gefühl, dass wir nicht groß ausgehen werden."


"Emi scheint mir nicht der Typ für so was zu sein."


"Dennoch gibt es sicher vieles, was ich noch nicht über Emi weiß."


"Obwohl wir uns nun so nahe stehen, habe ich immer noch das Gefühl, sie nicht so gut zu kennen, wie ich sollte."


"Na ja, ich habe viel Zeit, um das zu ändern."


"Um ehrlich zu sein freue ich mich darauf, sie besser kennenzulernen."


"Ich bin so in meine Gedanken versunken, dass ich kaum bemerke, dass ich schon am Sportplatz angekommen bin."


"Emi ist nirgends zu sehen."


"Ich sehe nicht einmal eine Spur der restlichen Leichtathletikmannschaft."


"Das könnte peinlich werden."


"Ich will mich gerade zum Mädchenwohnheim aufmachen, als ich jemanden rufen höre."


emi "Hey, Hisao!"


play music music_emi fadein 1.0

show emicas smile onlayer master at center
with charaenter

"Ich drehe mich um und sehe Emi, wie sie mit ihrer Sporttasche über der Schulter auf mich zuläuft."


"Sie trägt nun auch Freizeitkleidung; eine kurze Hose und ein olivgrünes Top."


"Ihre Laufprothesen hat sie gegen ein paar Beine ausgetauscht, die etwas echter aussehen, aber trotzdem kaum jemanden täuschen dürften."


"Emi scheint das nichts auszumachen, und darüber muss ich lächeln."


show emicas happy onlayer master
with charachange

emi "Hey, du bist gekommen!"


show emicas closedsmile onlayer master
with charachange

emi "Ich meine, ich war mir sicher, dass du kommen würdest, aber…"


show emicas closedsmile_up_close onlayer master
with characlose

"Plötzlich umarmt sie mich sanft, und ich schaffe es nicht, mir das größte Grinsen dieser Welt zu verkneifen."


hi "Natürlich bin ich gekommen!"


hi "Ich wäre schön blöd, wenn nicht, oder?"


"Emi denkt einen Moment lang darüber nach."


show emicas grin_up_close onlayer master
with charachange

emi "Weißt du, du hast Recht."


show emicas wink_up_close onlayer master
with charachange

emi "Ich meine, ich bin schon ziemlich toll."


"Als Antwort zucke ich mit den Schultern."


hi "Meiner Meinung nach ja."


show emicas blush_up_close onlayer master
with charachange

"Es war nur ein spontaner Kommentar, deshalb wundert es mich, dass er Emi auf dem falschen Fuß zu erwischen scheint."


show emicas smile_up_close onlayer master
with charachange

"Sie wird rot und lächelt mich herzlich an, bevor sie mich auf meinen Mund küsst."


"Nun hat sie mich auf dem falschen Fuß erwischt."


show emicas grin onlayer master
with charadistant

"Emi tritt einen Schritt zurück, verlagert ihr Gewicht auf ihre Ferse und sieht sehr zufrieden mit sich aus."


"Mein Gehirn sucht nach einer angemessenen Erwiderung."


hi "…"


hi "Ich sollte dir öfter Komplimente machen."


show emicas happy_up onlayer master
with vpunch

"Emi lacht und gibt mir einen scherzhaften Schubs."


show emicas closedsmile onlayer master
with charachange

emi "Idiot."


show emicas weaksmile_up_close onlayer master
with characlose

"Ich lege einen Arm um Emis Schultern und bin froh, als sie sich sofort an mich lehnt, als sei es das Natürlichste der Welt."


hi "Also, wohin geht's?"


show emicas awayfrown_up_close onlayer master
with charachange

emi "Um ehrlich zu sein, weiß ich das nicht genau."


show emicas neutral_up_close onlayer master
with charachange

emi "Wo gehen denn die Leute in dieser Gegend hin, wenn sie ein Date haben?"


"Das ist eine verdammt gute Frage."


hi "Ich habe keine Ahnung."


hi "Warum gehen wir nicht einfach runter zum Aura-Markt und holen uns irgendwas zum Mitnehmen."


"Emis Gesicht hellt sich bei dem Vorschlag auf."


show emicas happy_up_close onlayer master
with charachange

emi "Ein Picknick!"


show emicas wink_up_close onlayer master
with charachange

emi "Ich glaube, damit hast du ins Schwarze getroffen, Hisao."


scene bg school_gate onlayer master
with locationskip

"Emi legt ihren Arm um meine Hüfte, und wir machen uns auf den Weg zum Schultor."


"Ich habe nicht die geringste Ahnung, was in so einer Situation von mir erwartet wird, aber zumindest scheint es Emi genauso zu gehen."


scene bg suburb_roadcenter onlayer master
with locationskip

"Obwohl es ein sehr angenehmes Gefühl ist, mit Emi zusammen zu sein, bin ich doch etwas nervös."


"Was, wenn ich einen Fehler mache?"


"Ich will mich ja nicht zum Affen machen."


scene bg suburb_konbiniext onlayer master
with locationchange

"Auf dem Weg zum Aura-Markt erzählt mir Emi von ihrem Training."


"Ich sage nur wenig und genieße einfach die Wärme, die von ihr ausgeht."


"Ein paar Passanten schauen uns seltsam an, aber das macht mir nichts aus."


"Am Ende kaufen wir etwas Brot und Fertignudeln. Dass wir letztere im Park gar nicht zubereiten können, fällt uns erst zu spät auf."


show emicas weaksmile onlayer master
with charaenter

emi "Macht nichts. Die mache ich dann irgendwann zum Mittagessen."


hi "Gute Idee."


stop music fadeout 2.0
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg suburb_park onlayer master
with locationskip

"Nachdem wir uns einmal kurz verlaufen – wofür ich einzig und allein Emi die Schuld gebe – finden wir den Park."


"Sie gibt natürlich mir die Schuld."


show emicas smile onlayer master:
    center
    easein 1.0 ypos 1.13
with charaenter

"Wir finden einen schönen Platz unter einem Baum und setzen uns. Ich lehne mich gegen den Baumstamm, Emi sitzt mir gegenüber."


play music music_ease fadein 3.0

hi "Ich glaube, wir hätten eine Decke oder so was zum Draufsetzen mitbringen sollen, hmm?"


show emicas smile_up onlayer master:
    ypos 1.13
with Dissolve(0.2)

show emicas smile onlayer master
with charachange

"Emi zuckt mit den Schultern."


show emicas closedsmile onlayer master
with charachange

emi "Stört mich nicht."


hi "Mich auch nicht."


show emicas grin_up onlayer master
with charachange

"Emi wirft mir eine Packung Brot zu, und wir fangen an zu essen."


"Currybrot. Interessant."


"Ich habe anscheinend nicht wirklich darauf geachtet, was ich im Laden eingepackt habe."


show emicas wink_up onlayer master
with charachange

emi "Hey, Hisao. Du siehst aus, als wäre dein Brot ein wenig scharf."


"Ich schüttele meinen Kopf und versuche vergeblich, mein Image als harter Kerl zu bewahren."


hi "Nö, nicht wirklich."


show emicas closedsmile_up onlayer master
with charachange

emi "Ah ja. Deshalb ist dein Gesicht also plötzlich so rot."


hi "Ja, genau. Es schmeckt so fade, dass es… äh… mein Blut zum Kochen gebracht hat."


hi "Wegen der Enttäuschung."


show emicas happy onlayer master
with charachange

"Emi lacht und schluckt den Rest ihres Brotes hinunter."


show emicas wink onlayer master
with charachange

emi "Na ja, wenn du es nicht verträgst, esse ich es gern für dich."


hi "Hey, nur weil du deins so schnell runtergeschlungen hast, heißt das nicht, dass ich dir meins geben muss."


show emicas pout onlayer master
with charachange

"Emi tut wieder so, als würde sie schmollen, und ich verschlucke mich vor Lachen fast an meinem Brot."


emi "Och, komm schon, Hisao!"


show emicas awayfrown onlayer master
with charachange

emi "Solltest du dich nun nicht darum kümmern, dass ich genug zu essen bekomme?"


emi "Wir sind doch jetzt zusammen!"


show emicas pout onlayer master
with charachange

emi "Obwohl…"


"Emi sieht plötzlich etwas bedrückt aus."


show emicas frown_up onlayer master
with charachange

emi "Irgendwie fühle ich mich nicht anders als vorher."


hi "Hm? Wie meinst du das?"


show emicas awayfrown onlayer master
with charachange

emi "Warum ist das jetzt ein Date?"


emi "Es ist doch im Grunde nichts anderes als das, was wir sonst auch gemacht hätten."


emi "Aber das hier sollte sich anders anfühlen. Als wir vorher zusammen gegessen haben, waren wir Freunde, und nun sind wir mehr als das."


hi "Du hörst dich an wie Rin."


show emicas happy onlayer master
with charachange

"Emi lacht und grinst mich an."


show emicas closedsmile_up onlayer master
with charachange

emi "Na ja, kann sein, dass sie mich auf diesen Gedanken gebracht hat."


show emicas closedsmile onlayer master
with charachange

emi "Wir haben uns schon mal über so was unterhalten."


hi "Wirklich? Über mich?"


show emicas grin onlayer master
with charachange

emi "Nicht wirklich. Nur… nur so generell."


show emicas neutral onlayer master
with charachange

emi "Rin glaubt, dass der Übergang von einer Freundschaft in eine Beziehung in den meisten Fällen völlig willkürlich ist."


emi "Als ob es dazwischen gar keinen Unterschied gäbe."


hi "Mir fällt auf Anhieb mindestens einer ein."


hi "In einer Freundschaft küsst man sich nicht ganz so viel."


show emicas blush onlayer master
with charachange

"Zum zweiten Mal heute wird Emi rot und kichert."


show emicas closedsmile onlayer master
with charachange

emi "Da hast du wohl Recht."


hi "Genau. Bei solchen Dingen habe ich immer Recht."


show emicas weaksmile_up onlayer master
with charachange

"Emi rollt ihre Augen und lacht."


emi "Dann bist du wohl ziemlich schlau, was?"


"Ich nicke zustimmend."


hi "Jepp."


hi "Das sagt sogar Mutou. Er meint, ich sollte nach meinem Abschluss irgendwas naturwissenschaftliches studieren."


show emicas neutral onlayer master
with charachange

"Emi hebt eine Augenbraue."


emi "Ach wirklich?"


hi "Ja, ich denke, vielleicht sollte ich das wirklich machen."


"Wirklich – je mehr ich darüber nachdenke, desto mehr gefällt mir die Idee."


"Ich nehme mir vor, später noch einmal intensiver darüber nachzudenken."


hi "Und was hast du nun nach deinem Abschluss vor?"


hi "Willst du immer noch laufen?"


show emicas awayfrown onlayer master
with charachange

"Emi zuckt mit den Schultern und sieht ein wenig unentschlossen aus."


show emicas frown onlayer master
with charachange

emi "Weiß nicht. Wenn ich gut genug bin und eine Mannschaft finde, warum nicht?"


hi "Das heißt, du bist dir nicht sicher?"


show emicas neutral onlayer master
with charachange

emi "Ich habe… nicht wirklich darüber nachgedacht, um ehrlich zu sein."


hi "Wirklich?"


hi "Das solltest du aber. So lange ist es nicht mehr bis zum Abschluss."


show emicas awayfrown onlayer master
with charachange

"Emi rutscht nervös hin und her."


emi "Na ja… Bis dahin dauert es ja noch eine Weile, oder?"


show emicas neutral onlayer master
with charachange

emi "Außerdem habe ich so viele andere Dinge zum Nachdenken."


show emicas grin_up_close onlayer master
with vpunch

"Emis Augen blitzen übermütig auf, und plötzlich ist sie über mir und presst mich gegen den Baum."


show emicas smile_up_close onlayer master
with charachange

emi "Zum Beispiel muss ich dafür sorgen, dass das hier ein richtigs Date ist, nicht wahr?"


show emicas closedsmile_up_close onlayer master
with charachange

emi "Ich meine, wenn wir uns nicht küssen, ist es kein echtes Date, oder?"


hi "Ich denke sch— mmmph." with vpunch


"Erdbeeren und Curry. Nicht die beste Kombination, aber ich denke, das macht mir nichts aus."


show emicas grin onlayer master
with charadistant

"Emi setzt sich auf meine Beine und grinst mich an."


emi "So. Damit wäre der Wissenschaft genüge getan, nicht wahr?"


"Vor meinem geistigen Auge sehe ich Mutou ernsthaft nicken und etwas auf einer Liste abhaken."


"Die Vorstellung bringt mich zum Lachen."


show emicas neutral onlayer master
with charachange

emi "Hmm, ich gebe zu – das ist das erste Mal, dass ich sehe, wie jemand auf einen Kuss mit Lachen reagiert."


emi "Sollte ich mich nun beleidigt fühlen?"


hi "Hey, nein, nein."


hi "Ich bin mir sicher, dass der Wissenschaft genüge getan wurde."


show emicas happy_up onlayer master
with charachange

"Emi strahlt mich an, und es fällt meinem Gehirn zunehmend schwerer, einwandfrei zu funktionieren."


emi "Oh, gut!"


"In diesem Moment fällt mir auf, dass Emi des Rest meines Currybrotes geklaut hat, während ich von der Vorstellung von Lehrern mit Klemmbrettern abgelenkt war."


hi "Hey!"


show emicas blush onlayer master
with charachange

"Emi versucht unschuldig auszusehen, aber da sie sich gerade das letzte Stück Brot in den Mund geschoben hat, scheint es nicht zu funktionieren."


emi "Hmf? 'fuldigung, konnte nift widerftehen."


hi "Diebin!"


show emicas neutral onlayer master
with charachange

"Ein Schulterzucken ist ihre einzige Antwort."


hi "Du hast deine weiblichen Reize gegen mich eingesetzt!"


"Ich hatte zwar sowieso nicht so viel Hunger, aber es geht ums Prinzip."


show emicas pout onlayer master
with charachange

"Der Begriff „weibliche Reize” scheint Emi zu verwirren, aber nach einem Moment Überlegen scheint sie zu verstehen."


show emicas angry_up onlayer master
with charachange

emi "Hab ich gar nicht!"


show emicas frown_up onlayer master
with charachange

emi "Du hast gelacht! Bei weiblichen Reizen fängt man nicht an zu lachen!"


"Ich glaube, dem kann ich nicht widersprechen."


hi "Das ändert nichts an deinem Diebstahl."


show emicas happy onlayer master
with charachange

"Emi lacht über meinen verletzten Tonfall und gibt mir einen verspielten Schubs."


show emicas closedsmile onlayer master
with charachange

emi "Okay, du kannst die Fertignudeln haben."


hi "Soll das ein Witz sein? Das Zeug schmeckt furchtbar!"


hi "Wenn überhaupt, dann solltest du das Zeug essen – als Strafe!"


show emicas wink onlayer master
with charachange

"Noch ein Lachen von dem Mädchen, das auf meinen Beinen sitzt…"


"… die im Übrigen inzwischen beide eingeschlafen sind."


show expression im.Composite((295,1200), (0,0), "sprites/emicas/emicas_wink.png") as emicas onlayer master:
    xalign 0.5 yanchor 0.5 ypos 1.13 subpixel True
    easeout 0.8 rotate -90
with None

show expression im.Composite((295,1200), (0,0), "sprites/emicas/emicas_blush.png") as emicas onlayer master:
    xalign 0.5 yanchor 0.5 ypos 1.13 subpixel True
    easeout 0.8 rotate -90

with Dissolve(0.2)
with Pause(0.6)

hide emicas onlayer master
with vpunch

"Ich bewege eins meiner Beine, um das Blut wieder zum Laufen zu kriegen, womit ich unbeabsichtigt Emi aus dem Gleichgewicht bringe, sodass sie mit einem erschrockenen Ausruf zur Seite fällt."


hi "Ups! Das tut mir leid."


hi "Meine Beine sind eingeschlafen."


"Emi bleibt kichernd auf dem Boden liegen."


"Ich stehe etwas wackelig auf und spüre, wie das Gefühl in meine Beine zurückkehrt."


"Mein Blick wandert über die Landschaft und landet schließlich auf Emi, die immer noch nicht aufgestanden ist."


scene ev emi_parkback onlayer master:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    ease 10.0 zoom 1.0
with locationchange

"Ihre Haare bedecken das Gras um ihren Kopf herum, ihre Arme sind ausgebreitet und ein helles Lachen sprudelt aus ihrem Mund."


"Alles, was Emi ausmacht, scheint in diesem Bild auf einen Punkt gebracht zu sein."


"Ihre Energie, ihr Temperament, ihr kindliches Kichern."


"Ich verspüre den Drang, mich einfach so neben sie ins Gras zu legen. In diesem Moment würde ich wirklich nichts lieber tun als das."


"Leider ist die Sonne schon am Untergehen, und es ist wohl an der Zeit für uns, zurück zum Wohnheim zu gehen."


"Emi hätte vielleicht die Energie, die ganze Nacht hier zu bleiben, aber ich glaube, ich könnte das nicht."


"Außerdem rufen mich meine Hausaufgaben."


"Es wäre doch sinnlos, sich Gedanken über die Uni und solche Dinge zu machen, und dann alles schleifen zu lassen, oder?"


"Ich reiche Emi eine Hand, um ihr aufzuhelfen."


hi "Wir sollten besser gehen."


show ev emi_parkback_frown onlayer master
with charachange

"Emi verzieht das Gesicht."


emi "Du hast Recht."


scene bg suburb_park onlayer master
with locationchange

show emicas weaksmile_close onlayer master:
    center
    ypos 1.2
    easein 0.5 ypos 1.0
with charaenter

"Sie nimmt meine Hand, und ich ziehe sie hoch und in meine Arme."


"Dieses Mal bin ich derjenige, der sie küsst – es ist mir nicht möglich, der Versuchung zu widerstehen."


hi "Weißt du, eigentlich will ich noch gar nicht gehen."


show emicas closedsmile_close onlayer master
with charachange

emi "Ja, ich auch nicht."


show emicas grin_up_close onlayer master
with charachange

emi "Aber wenn wir nicht bald zurück in der Schule sind, kriegen wir wahrscheinlich Ärger."


"Emi pikst mich in die Rippen."


show emicas wink_up_close onlayer master
with charachange

emi "Und du musst bestimmt noch Hausaufgaben machen."


hi "Da hast du leider völlig Recht."


hide emicas onlayer master
with charaexit

"Ich lege meinen Arm um ihre Schultern und wir machen uns auf den Rückweg – ab und zu unterbrochen von Lachanfällen, während unser Gespräch von Thema zu Thema springt."


"Wir reden über alles – vom Laufen, über die Schule bis hin zu dem seltsamen Geruch eines der Arbeiter in der Cafeteria."


stop ambient fadeout 2.0

scene bg school_dormext_full onlayer master
with locationskip

"Viel zu schnell finden wir uns vor dem Mädchenwohnheim wieder."


show emicas closedsmile onlayer master at center
with charaenter

emi "Nun, ich denke, ich gehe dann mal."


hi "Sieht wohl so aus…"


show emicas grin_up onlayer master
with charachange

"Emi grinst mich wieder mit diesem übermütigen Ausdruck an."


emi "Und? Wirst du ohne mich überleben?"


"Ich lache."


hi "Ich bin sicher, ich kriege das irgendwie hin."


show emicas pout_up onlayer master
with charachange

emi "Wie furchtbar! Solltest du nicht so was sagen wie „Ich werde die Sekunden zählen, die wir voneinander getrennt sind?”"


hi "Nö, ich glaube nicht."


show emicas closedsmile_close onlayer master
with characlose

show emicas weaksmile onlayer master
with charadistant

"Emi zieht mich zu sich herunter, gibt mir einen kurzen Abschiedskuss und tritt dann – unerwartet schüchtern – einen Schritt zurück."


emi "Danke für das Abendessen."


emi "Es hat mir wirklich Spaß gemacht."


show emicas closedsmile onlayer master
with charadistant

emi "Das hat es wirklich."


hi "Mir auch."


hi "Ich denke, das sollten wir irgendwann mal wiederholen."


show emicas happy onlayer master
with charadistant

"Emi lacht über meine trockene Erwiderung und nickt."


emi "Also dann, morgen früh in alter Frische, okay?"


show emicas wink onlayer master
with charadistant

emi "Du musst schließlich das Brot abtrainieren."


hi "Natürlich. Obwohl du das meiste davon gegessen hast."


show emicas smile_up onlayer master
with charadistant

emi "Ja, trotzdem."


show emicas grin_up onlayer master
with charadistant

emi "Bis später, Hisao!"


stop music fadeout 3.0

show emicas invis onlayer master:
    xpos 0.6
with dissolvecharamove

hide emicas onlayer master
with None

"Als sich Emi umdreht, um hineinzugehen, fällt mir etwas Seltsames auf."


"Etwas so Seltsames, dass ich überrascht bin, dass es mir nicht schon früher aufgefallen ist."


"Sie humpelt leicht und schont ihr linkes Bein."


play music music_pearly fadein 8.0

hi "Hey, Emi!"


show emicas invis onlayer master at tworight
with None

show bg school_dormext_full onlayer master at bgleft
show emicas neutral onlayer master at center
with dissolvecharamove

emi "Hmm?"


hi "Ist mit deinem Bein alles in Ordnung?"


show emicas awayfrown onlayer master
with charachange

"Emi sieht verwirrt aus, oder zumindest tut sie so, als sei sie verwirrt."


show emicas frown onlayer master
with charachange

emi "Wovon redest du?"


hi "Dein linkes Bein. Du humpelst."


show emicas blush onlayer master
with charachange

show emicas frown onlayer master
with charachange

"Ganz kurz ist ein besorgter Ausdruck auf Emis Gesicht zu sehen."


"Entweder wollte sie nicht, dass ich es merke, oder sie dachte, ich würde es nicht bemerken, oder – und die Version wäre mir am liebsten – sie hat es einfach selbst nicht bemerkt."


show emicas neutral_up onlayer master
with charachange

emi "Ach… das."


"Sie zuckt lässig mit den Schultern."


show emicas awayfrown onlayer master
with charachange

emi "Das muss während des Picknicks etwas verrutscht sein."


show emicas wink onlayer master
with charachange

emi "Natürlich habe ich keine Ahnung, wie das passiert sein könnte."


"Ich denke an die Szene unter dem Baum zurück."


hi "Ah."


hi "Du hättest mir das sagen sollen, dann hätten wir anhalten und es richten können."


"Emi winkt ab."


show emicas smile_up onlayer master
with charachange

emi "Nee, so schlimm ist es nicht."


show emicas weaksmile_up onlayer master
with charachange

emi "Mach dir darüber keine Sorgen, okay Hisao?"


show emicas closedsmile_up onlayer master
with charachange

emi "Es ist alles in Ordnung."






label de_choiceE17:
menu:
    with menueffect
    "Warum habe ich das Gefühl, dass sie sich selbst damit ebenso überzeugen will wie mich?"
    "Nachhaken.":




        return m1
    "Es gut sein lassen.":


        return m2

label de_E17a:


hi "Bist du absolut sicher?"


hi "Willst du es nicht doch besser justieren, bevor du die Treppe hochgehst?"


hi "Du könntest dir sonst wehtun, oder?"


show emicas awayfrown_up onlayer master
with charachange

emi "Ich habe gesagt, es ist okay, Hisao."


show emicas frown onlayer master
with charachange

emi "Ernsthaft, mach dir keine Sorgen."


show emicas weaksmile onlayer master
with charachange

emi "Ich habe darin immerhin schon etwas Erfahrung."


hi "Ja, sicher."


"Emi grinst beschwichtigend."


show emicas grin onlayer master
with charachange

emi "Ehrlich, Hisao, ich freue mich, dass du dir Sorgen machst, aber es geht mir gut."



label de_E17b:


"Na ja, es ist sicher alles in Ordnung."


"Ich denke, wenn es ein Problem wäre, würde sie etwas sagen."


"Verdammt, wahrscheinlich wäre sie sogar verärgert, wenn ich länger darauf herumreite."



label de_E17x:

show emicas smile onlayer master
with charachange

emi "Nun muss ich aber wirklich los."


show emicas wink_up onlayer master
with charachange

emi "Deine Versuche, mich bei dir zu halten, sind zum Scheitern verurteilt."


hi "Heh, natürlich."


hi "Ich will wohl einfach nur den Abschied hinauszögern."


"Ein weiteres Grinsen strahlt über Emis Gesicht."


show emicas happy_up onlayer master
with charachange

emi "Gute Nacht, Hisao."


hi "Gute Nacht."


hide emicas onlayer master
with charaexit

stop music fadeout 5.0

"Während sie hineinhumpelt, hoffe ich, all ihrer Versicherungen zum Trotz, dass es ihr wirklich gut geht."


"Ich denke, das geht als ein erfolgreiches erstes Date durch."


"Verdammt, jeder Tag, der damit endet, dass Emi unter einem Baum auf mir sitzt und mich küsst, ist ein guter Tag, oder?"


"Ich gehe zurück auf mein Zimmer, danke allen Göttern, dass Kenji mich nicht Flur überfällt, und beginne mit meinen Hausaufgaben."


scene black onlayer master
with dissolve




label de_E18:

scene bg school_dormhisao onlayer master
with locationchange

play music music_night fadein 5.0

"Es ist viel zu früh am Morgen für meinen Geschmack."


"Dass ich heute Nacht kaum geschlafen habe, macht es auch nicht besser."


"Es schwirrten einfach zu viele Gedanken in meinem Kopf herum. Ich konnte keine Ruhe finden."


"Stattdessen habe ich die Szenen auf dem Dach, im Park und alles andere wieder und wieder vor meinem geistigen Auge ablaufen lassen."


"Irgendwo in meinem Hinterkopf ist immer noch die Furcht, dass das alles nur irgendein Scherz gewesen sein könnte."


"Dass ich Emi am Sportplatz treffe und sie so tut, als sei gestern nichts gewesen."


"Ich verdränge diese Gedanken, schmeiße mich in meine Trainingsklamotten und öffne die Tür."


scene bg school_track onlayer master
show emi basic_grin_gym onlayer master at center
with locationskip

"Emi wartet mit ihrem gewohnten Lächeln auf mich."


show emi basic_annoyed_gym onlayer master
with charachange

emi "Du bist zu spät!"


show emi basic_closedgrin_gym onlayer master
with charachange

emi "Oder zumindest bist du heute nicht zu früh."


show emi excited_hesitant_gym onlayer master
with charachange

emi "Bist du etwa müde?"


"Ich kratze mich verlegen am Hinterkopf."


hi "So was in der Richtung, ja."


hi "Viel zum Nachdenken gehabt und so."


show emi basic_closedgrin_gym onlayer master
with charachange

"Emi kichert über meine leichte Untertreibung."


show emi basic_grin_gym onlayer master
with charachange

emi "Na ja, ich habe auch nicht so gut geschlafen."


show emi excited_proud_gym onlayer master
with charachange

emi "Um ehrlich zu sein, war ich froh, dass du nicht zu früh warst, weil ich auch nicht zu früh war."


"Ich frage mich, ob wir aus den gleichen Gründen nicht schlafen konnten."


"Die Erinnerung an ihr weinendes Gesicht kommt in mir auf."


hi "Was hat dich wachgehalten?"


show emi sad_shy_gym onlayer master
with charachange

"Emis Grinsen verschwindet, aber sie bemerkt meinen neugierigen Blick und zwingt sich zu einem Lächeln."


show emi sad_grin_gym onlayer master
with charachange

emi "Nichts Wichtiges."


"Es ist offensichtlich, dass sie mir etwas verschweigt."


"Die Frage ist, sollte ich nachhaken?"


"Es ist klar, dass irgendetwas sie schon länger bedrückt."


"Ich will ihr helfen, aber würde das nicht einfach nur als aufdringlich rüberkommen?"


"Ich muss ihr aber zeigen, dass sie mir wichtig ist."


hi "Bist du sicher?"


hi "Wenn dich etwas bedrückt, bin ich da, um dir zu helfen, das Problem zu lösen."


show emi basic_closedhappy_gym onlayer master
with charachange

"Emi lacht, aber es ist nicht ihr gewöhnliches Lachen. Es ist irgendwie scharf – fast schon bitter."


show emi sad_grin_gym onlayer master
with charachange

emi "Das Problem zu lösen?"


emi "Ich glaube nicht, dass man das lösen kann, Hisao."


"Ein Beinahegrinsen spielt um ihre Lippen."


"Es sieht aus, als hätte sie resigniert."


show emi sad_pout_gym onlayer master
with charachange

emi "Ich glaube eh nicht, dass du mir helfen könntest."


"Das tut weh."


"Ich will ihr gegenüber nicht sagen, dass es weh tut, aber es ist so."


"Merkt sie denn nicht, dass ich für sie da sein will?"


hi "Na ja, ich werde dich nicht unter Druck setzen."


hi "Aber ich bin für dich da, wenn du später entscheidest, dass du darüber reden möchtest."


hi "Vielleicht hilft es ja doch."


show emi sad_shy_gym onlayer master
with charachange

"Ich sehe, wie es hinter Emis Stirn arbeitet."


"Es scheint, als ob sie es mir erzählen will, sich aber nicht sicher ist, ob sie es kann."


hi "Hey, vergiss es einfach erst mal, okay?"


hi "Wir haben noch unser Training vor uns."


"Sobald ich das Training erwähne, findet Emi zu ihrer normalen Persönlichkeit zurück – das ist etwas, mit dem sie umgehen kann."


show emi basic_closedhappy_gym onlayer master
with charachange

emi "Genau!"


show emi basic_grin_gym onlayer master
with charachange

emi "Beeil dich mit dem Aufwärmen, Hisao!"


show emi excited_proud_gym onlayer master
with charachange

emi "Wir müssen langsam mal anfangen!"


play ambient sfx_emipacing

hide emi onlayer master
with easeoutleft

stop ambient fadeout 3.0

"Sie läuft los wie ein geölter Blitz – viel schneller, als ich es von ihr gewohnt bin."


scene bg school_track_on onlayer master
with locationchange

scene bg school_track_running onlayer master
with Dissolve(2.0)

"Trotzdem muss ich mit ihr Schritt halten und gehe wieder einmal unvorsichtigerweise an meine Grenzen."


"Irgendwie fühlt sich das befreiend an, als ob mein Herz nicht mehr so wichtig wäre."


"Ich will laut lachen; es ist, als ob ich über mich selbst hinauswachsen würde."


"Docs Warnungen, es nicht zu übertreiben, kommen mir in den Sinn, aber ich ignoriere sie."


"Dieses Gefühl, diese Bereitschaft, einen Herzanfall für so etwas triviales wie ein Morgentraining zu riskieren, ist gar nicht typisch für mich."


"Oder etwa doch?"


"Oder besser – sollte es das sein?"


"Klar, ich habe ein schwaches Herz."


"Ich werde nie so schnell oder so ausdauernd sein wie Emi."


"Wahrscheinlich würde ich so gut nicht einmal mit einem gesunden Herz werden."


stop music fadeout 6.0

"Als wir um die letzte Kurve laufen, spüre ich, wie meine Beine lauthals protestieren, aber ich ignoriere sie."


"Ich beschleunige und beende den Lauf mit einem Sprint, bei dem ich sogar fast Emi einhole."


"So weit wäre es natürlich nie gekommen."


"Trotzdem fühle ich mich erstaunlich gut."


"Ja, meine Beine fühlen sich an, als würden sie jeden Moment in Flammen aufgehen, und ich kann mich kaum aufrecht halten."


"Aber irgendetwas hat sich heute verändert."


"Und das verdanke ich alles dem Mädchen, das mich grinsend an der Ziellinie erwartet."


scene bg school_track_on onlayer master
show emi basic_grin_gym onlayer master at center
with locationchange

play music music_emi fadein 1.0

hi "Ich glaube, das war etwas schneller als sonst."


"Meine Bemerkung wird mit einem Grinsen und einem Schulterzucken quittiert."


show emi excited_proud_gym onlayer master
with charachange

emi "Sonst denkst du noch, ich würde dich von nun an schonen, oder?"


show emi basic_closedgrin_gym onlayer master
with charachange

emi "Aber du bist gut mitgekommen."


hi "Na ja, ich hätte es nicht ohne dich geschafft."


show emi basic_confused_gym_close onlayer master
with characlose

"Immer noch euphorisch von dem Lauf und erfüllt von Dankbarkeit, nehme ich Emi in den Arm."


hi "Danke."


hi "Wirklich, ich sage das nicht einfach so."


hi "Ich stehe in deiner Schuld."


show emi basic_hes_gym_close onlayer master
with charachange

"Emi scheint ein wenig verlegen zu sein und zappelt nervös."


emi "Sei nicht albern, Hisao."


show emi basic_grin_gym_close onlayer master
with charachange

emi "Irgendjemand musste dich doch da rausholen, oder?"


show emi basic_closedgrin_gym_close onlayer master
with charachange

emi "Und es ist ja nicht so, als würdest du nichts für mich tun, stimmt's?"


show emi basic_grin_gym_close onlayer master
with charachange

emi "Ich brauchte einen Trainingspartner, weißt du noch?"


show emi basic_shock_gym_close onlayer master
with charachange

"Ich schüttele meinen Kopf, ohne Emi loszulassen. Sie hört auf, zu zappeln und schaut nur noch mit einem errötenden Gesicht zu mir auf. Das ist schon fast untypisch für sie."


hi "Nein, das ist nicht wahr."


hi "Du wolltest einen Trainingspartner, aber du hättest keinen gebraucht."


hi "Wenn ich am Tag nach dem Schulfest nicht hier aufgetaucht wäre, wärst du trotzdem gelaufen, oder?"


hi "Aber anders herum wäre es nicht so gewesen."


hi "Vor dem Schulfest habe ich mich nur ein paar Mal hier hinaus gequält."


hi "Und ohne dich hätte ich vermutlich danach gar nichts mehr getan."


show emi basic_closedgrin_gym_close onlayer master
with charachange

"Emi lächelt mich an und stupst mit dem Finger gegen meine Brust."


show emi excited_proud_gym_close onlayer master
with charachange

emi "Du bist einfach ziemlich faul, Hisao."


hi "Hey, ich habe dir gerade ein Kompliment gemacht!"


show emi sad_grin_gym_close onlayer master
with charachange

emi "Na ja, dann… Keine Ursache."


hi "Irgendwie werde ich mich bei dir revanchieren."


show emi basic_hes_gym_close onlayer master
with charachange

emi "Oh, äh, na ja…"


show emi basic_closedgrin_gym_close onlayer master
with charachange

emi "Du weißt, dass das nicht nötig ist."


show emi basic_happyblush_gym_close onlayer master
with charachange

emi "Ich meine… Ich mag dich irgendwie, Hisao."


show emi sad_grin_gym_close onlayer master
with charachange

emi "Und morgens mit dir laufen zu können, ist auch nicht gerade etwas, was ich als Last empfinden würde, also…"


"Für jemanden, der so oft gelobt wird, scheint sie Dankbarkeit kaum gewöhnt zu sein."


"Mir fällt nichts weiter ein, und wir verstummen."


"Ich fühle wie Emi atmet – ihre feuchte Kleidung, ihr Geruch."


"Bei jedem anderen würde es stinken."


"Zu Emi passt es wie nichts anderes."


"Ihre Haut ist kühl, schweißnass, und sie schaudert leicht in dem kühlen Wind."


show emi excited_amused_gym_close onlayer master
with charachange

"Fast ohne zu überlegen beuge ich mich hinab zu Emis Mund, der sich bereits auf meinen eigenen zubewegt."


"Ihre Lippen sind weich, und sie summt fröhlich vor sich hin, als wir uns küssen, was Vibrationen von ihrem Mund auf meinen überträgt."


"Alles an diesem Augenblick fühlt sich so… richtig an. Wir passen perfekt zueinander."


show emi basic_grin_gym_close onlayer master
with charachange

"Der Kuss endet, und ich lasse meine Arme sinken."


show emi basic_closedgrin_gym_close onlayer master
with charachange

"Emi lächelt mich warm an und kichert wieder."


show emi basic_closedhappy_gym onlayer master
with charadistant

emi "Komm schon, Hisao, wir sollten besser zu Doc gehen."


stop music fadeout 1.0

"Dann passiert es."


show emi basic_closedhappy_gym onlayer master:
    ease 0.25 ypos 1.05
    ease 0.25 ypos 1.0
with None

show emi excited_sad_gym onlayer master:
    ease 0.25 ypos 1.05
    ease 0.25 ypos 1.0
with Dissolve(0.25)

"Als sie sich umdreht, um loszugehen, stößt sie einen kurzen Schrei aus und stolpert vornüber."


hi "Emi!"


play music music_rain fadein 2.0

show emi excited_sad_gym_close onlayer master
with characlose

"Ich springe vorwärts, um sie zu stützen und stelle besorgt fest, dass sie dasselbe Bein schont wie gestern Abend."


hi "Dein Bein…"


show emi basic_hes_gym onlayer master
with charadistant

"Emi scheint in Panik zu geraten und stößt mich von sich."


emi "Es ist okay!"


"Sie muss in meinem Gesicht gelesen haben, wie mich ihre Reaktion verletzt hat, denn sie entschuldigt sich sofort."


show emi basic_shock_gym onlayer master
with charachange

emi "Tut mir leid, tut mir leid!"


emi "Ich wollte dich nicht so wegstoßen!"


show emi basic_closedsweat_gym onlayer master
with charachange

emi "Ich war nur…"


"Sie sucht nach Worten."


show emi sad_depressed_gym onlayer master
with charachange

emi "Es war nichts, wirklich."


hi "Hey, ist schon in Ordnung."


"Sie ist so verstört, dass ich beschließe, das Thema zu wechseln."


"Aber ich habe dieses kalte Gefühl in der Magengrube, das einfach nicht weggehen will."


"Ich habe versucht, ihr zu helfen, und sie hat mich weggestoßen."


"Ich schiebe diese Gedanken beiseite, lächle und konzentriere mich auf Emi."


hi "Ich will nur nicht, dass du dich verletzt, das ist alles."


show emi sad_pout_gym onlayer master
with charachange

emi "Du musst dir keine Sorgen um mich machen, ehrlich."


show emi sad_grin_gym onlayer master
with charachange

emi "Es geht mir gut!"


"Ja, das sagst du zwar, aber ich glaube dir nicht."



label de_E18a:


"Warum sagst du mir nicht, was los ist?"


"Es ist, als ob meine Versuche, ihr zu helfen, sie verärgern."


"Was soll ich davon halten?"



label de_E18b:


"Ich mache mir trotzdem Sorgen um dich, und nun habe ich auch noch ein schlechtes Gewissen, weil ich gestern nichts gesagt habe."


"Ich hätte zumindest fragen sollen."


"Hätte sie gestern Abend genauso reagiert?"


"Ich werde es wahrscheinlich nie erfahren."



label de_E18x:

stop music fadeout 2.0

scene bg school_nursehall onlayer master
with locationskip

"Ich versuche immer noch, mir darüber klar zu werden, was eigentlich passiert ist, als wir vor Docs Büro ankommen."


"Emi hebt ihre Hand zum Klopfen, dann zögert sie und dreht sich mit einem schuldbewussten Lächeln zu mir um."


show emi sad_grin_gym onlayer master:
    yalign 1.0 xanchor 0.5 xpos 0.47
    easein 0.5 center
with charaenter

emi "Hey, kannst du mir einen Gefallen tun?"


hi "Natürlich."


show emi excited_proud_gym onlayer master at center
with charachange

emi "Kannst du Doc sagen, dass ich später bei ihm vorbeischaue?"


show emi basic_grin_gym onlayer master
with charachange

emi "Mir ist gerade eingefallen, dass ich… noch ein paar Sachen vor dem Unterricht zu erledigen habe."


show emi sad_grin_gym onlayer master
with charachange

emi "Ich muss mich wirklich beeilen."


show emi sad_shyblush_gym onlayer master
with charachange

"Ich schaue sie forschend an, und sie windet sich unter meinem Blick."


"Ja, sie will offensichtlich nur Doc aus dem Weg gehen."


"Ihr Bein…"


"Wie auch immer. Ich habe gesagt, dass ich ihr helfe, also werde ich das auch tun."


"Aber ich werde dafür sorgen, dass sie heute noch bei Doc vorbeischaut."


hi "Ja, okay. Ich sage ihm Bescheid."


show emi excited_smile_gym onlayer master
with charachange

"Emi sieht aus, als hätte ich ihr gerade ein Pony zu Weihnachten geschenkt."


show emi excited_joy_gym onlayer master
with charachange

emi "Vielen Dank!"


show emi excited_amused_gym onlayer master
with charachange

emi "Du bist der Beste, Hisao!"


show emi excited_amused_gym_close onlayer master
with characlose

"Meine Belohnung für meine Beteiligung an ihrer Lüge ist ein Kuss, und allein das ist es wert – zumindest rede ich mir das ein."


hide emi onlayer master
with charaexit

"Während Emi zum Ausgang läuft und versucht, sich ihr Humpeln nicht anmerken zu lassen, klopfe ich an Docs Tür."


nk "Ah, Hisao. Komm rein."


play music music_nurse fadein 1.0

scene bg school_nurseoffice onlayer master
show nurse neutral onlayer master at center
with locationchange

nk "Emi ist heute gar nicht bei dir."


show nurse fabulous onlayer master
with charachange

nk "Sie ist doch nicht schon wieder krank, oder?"


"Seinem Tonfall nach zu urteilen, glaubt er nicht wirklich an diese Möglichkeit."


hi "Äh, sie sagte, dass sie noch etwas erledigen muss, und dass sie deshalb nicht kommen kann, aber sie wird später vorbeikommen."


show nurse concern onlayer master
with charachange

"Doc seufzt verärgert."


nk "Also wirklich, dieses Mädchen…"


hi "Hmm?"


show nurse neutral onlayer master
with charachange

nk "Sie geht mir aus dem Weg."


nk "Als sie gestern hier war, war sie so schnell weg, dass sie nicht mal ihre Prothesen abgenommen hat. Und jetzt das."


"Na ja, zumindest bin ich nicht der einzige, dem Emi keine Sorgen machen will."


"Das ist… ein Trost? Vielleicht."


"Dennoch habe ich das Gefühl, ich sollte etwas wegen ihres Beines sagen. Ich habe zwar gesagt, dass ich für sie Lügen würde, aber er muss sich das wirklich ansehen."


hi "Jetzt wo Sie es erwähnen – sie hat heute ziemlich schlimm gehumpelt."


hi "Und gestern Abend auch."


show nurse concern onlayer master
with charachange

"Bei den Worten „gestern Abend” legt sich Docs Stirn in Falten."


nk "Und was genau habt ihr beide gestern Abend gemacht?"


hi "Wir waren, äh… zusammen aus."


show nurse fabulous onlayer master
with charachange

"Doc hebt seine Augenbraue, als würde ihn das überraschen."


nk "Wirklich? Interessant."


hi "Hä?"


show nurse neutral onlayer master
with charachange

nk "Ach nichts."


"Er schaut mich nachdenklich an, dann grinst er."


show nurse grin onlayer master
with charachange

nk "Glaubst du, du könntest deinen Einfluss als ihr Freund spielen lassen, um sie dazu zu bringen, heute noch zu mir zu kommen?"


hi "Natürlich!"


hi "Das hatte ich sowieso vor."


hi "Ich glaube, sie ist wirklich verletzt und tut nur so, als wäre alles in Ordnung."


show nurse neutral onlayer master
with charachange

nk "Hmm, ja. Das tut sie manchmal."


nk "Sie hat Angst, dass ich ihr das Laufen verbiete."


hi "Werden Sie das tun?"


show nurse concern onlayer master
with charachange

nk "Nur ungern, aber wenn es so schlimm ist, dass sie humpelt, dann…"


nk "Ich muss einfach selbst sehen, was los ist, bevor ich das entscheiden kann."


hi "Ach so."


"Emi das Laufen verbieten? Unvorstellbar."


"Ich weiß nicht, wie sie das überstehen sollte."


"Kein Wunder, dass sie nicht zugeben will, dass sie verletzt ist."


hi "Na ja, ich sorge dafür, dass sie herkommt."


show nurse neutral onlayer master
with charachange

nk "Gut. Ach und bevor ich's vergesse…"


show nurse grin onlayer master
with charachange

"Er grinst mich wieder auf seine leicht bedrohliche Weise an."


nk "Vergiss nicht, dass ich weiß, welche Medikamente du nimmst."


show nurse neutral onlayer master
with charachange

nk "Sei vorsichtig mit Emi, verstanden?"


"Wow. Nun sieht er sogar ernst aus."


hi "Verstanden."


hi "Emi nicht verletzen. Würde mir nicht im Traum einfallen."


show nurse grin onlayer master
with charachange

nk "Großartig!"


show nurse fabulous onlayer master
with charachange

nk "Wir wollen doch nicht, dass du etwas segnest."


hi "Hä?"


show nurse grin onlayer master
with charachange

nk "Schon gar nicht das Zeitliche."


show nurse concern onlayer master
with charachange

"Er runzelt unzufrieden die Stirn."


nk "Hörte sich in meinem Kopf besser an…"


show nurse neutral onlayer master
with charachange

nk "Na ja, jedenfalls…"


show nurse grin onlayer master
with charachange

nk "Raus hier, bevor du deine erste Stunde verpasst!"


nk "Ich bin mir sicher, dass du viel zu tun hast. Hopp!"


stop music fadeout 6.0

"Als ich das Büro verlasse, sehe ich, wie Doc sein Handy herausholt und eine Nummer wählt."


show nurse concern onlayer master
with charachange

nk "Meiko, dein Gör von einer Tochter macht mal wieder…"


"Ich sollte besser zurück auf mein Zimmer gehen, sonst komme ich wirklich noch zu spät."


"Hey, hätte er nicht eigentlich meinen Puls prüfen sollen?"




label de_E19:

scene bg school_scienceroom onlayer master
with shorttimeskip

play sound sfx_normalbell

"Die Schulglocke läutet zur Mittagspause, und ich raffe mich aus dem Halbschlaf auf, in den ich während des Vormittags versunken bin."


"Ich bin ein wenig erschöpft, wegen meines Schlafmangels letzte Nacht und des erhöhten Tempos bei meinem Lauf heute Morgen."


$ renpy.music.set_volume(0.15, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_staircase1 onlayer master
with locationskip

"Trotzdem nehme ich auf dem Weg zum Dach mehrere Stufen auf einmal."


"Da ist jetzt so ein aufregendes Gefühl, zusätzlich zu der Vorfreude auf ein Mittagessen mit Freunden."


play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg school_roof onlayer master
with locationchange

"Klar sind Emi und Rin immer noch meine Freunde, aber Emi ist nun mehr als das."


"Rin ist zurück an ihrem üblichen Platz auf dem Dach, als wäre sie nie fort gewesen."


scene ev rin_roof_boredom onlayer master
show hisao rin_roof onlayer master
with locationchange

hi "Sieht aus, als würde es dir wieder besser gehen."


show ev rin_roof_surprised onlayer master
with charachange

"Eine hochgezogene Augenbraue ist die Belohnung für meine Worte."


rin "Besser als was?"


play music music_rin fadein 6.0

hi "Äh… Besser als gestern."


show ev rin_roof_nonchalant onlayer master
with charachange

"Rin denkt ernsthaft über meine Frage nach."


rin "Ich bin mir nicht sicher."


rin "Ich glaube, ich habe mich für einen Teil von Gestern ziemlich gut gefühlt, aber es ist alles ein bisschen vage."


hi "Zu viel von der Medizin?"


show ev rin_roof_doubt onlayer master
with charachange

rin "Na ja, ich habe geschlafen. Und das ist normalerweise ziemlich gut."


show ev rin_roof_boredom onlayer master
with charachange

rin "Aber ich kann mich nicht erinnern, wie es sich anfühlt zu schlafen, weil ich dabei nicht wach bin."


rin "Das ist ein echtes Problem."


show ev rin_roof_nonchalant onlayer master
with charachange

rin "Allerdings… Wenn ich wüsste, wie gut es sich anfühlt, könnte ich vielleicht gar nicht mehr schlafen."


rin "Aber auf diese Weise versuche ich es weiter, also hilft es mir vielleicht dabei, nicht zu übermüden."


hi "Ein ewiges Mysterium, das dich Nachts schlafen lässt?"


show ev rin_roof_boredom onlayer master
with charachange

rin "Vielleicht ist Mysterium das falsche Wort. Nichtgreifbarkeit würde es vielleicht besser beschreiben."


hi "Verstehe."


"Nein, ich verstehe gar nichts. Ich habe keine Ahnung, wovon sie redet, aber das ist okay – das ist fast immer so."


show ev rin_roof_doubt onlayer master
with charachange

rin "Erinnerst du dich daran, wie sich Schlaf anfühlt?"


rin "Zum Beispiel gestern. Erinnerst du dich daran, wie du dich gestern beim Schlafen gefühlt hast?"


hi "Na ja, ich habe ehrlich gesagt gestern nicht viel geschlafen."


show ev rin_roof_nonchalant onlayer master
with charachange

rin "Hmm."


rin "Vielleicht, weil du dich unterbewusst daran erinnerst?"


hi "Eigentlich liegt es wohl eher daran, dass ich mir Sorgen um Emi gemacht habe."


show ev rin_roof_surprised onlayer master
with charachange

rin "Macht sich Emi nicht selbst schon genug Sorgen um sich?"


"Das hatte ich so noch gar nicht bedacht, aber es stimmt mich nachdenklich."


hi "Stimmt, aber würde sie um Hilfe bitten, wenn sie sie bräuchte?"


show ev rin_roof_doubt onlayer master
with charachange

"Rin runzelt die Stirn, und ich hebe eine Augenbraue. Werde ich eine normale Antwort kriegen?"


rin "Wahrscheinlich nicht. Gibt es etwas, weswegen sie um Hilfe bitten sollte?"


hi "Zum einen ihr Bein."


"Das scheint Rin zu interessieren."


show ev rin_roof_disgust onlayer master
with charachange

rin "Bein?"


hi "Es ist verletzt, aber sie will damit nicht zu Doc gehen."


"Rin schüttelt missbilligend den Kopf."


show ev rin_roof_doubt onlayer master
with charachange

rin "Du musst sie dazu bringen."


show ev rin_roof_nonchalant onlayer master
with charachange

rin "So wie sie mich dazu bringt, zum Unterricht zu gehen. Zu ihrem eigenen Besten."


rin "Sonst könnte sie ihre Beine wieder verlieren, und das wäre ziemlich bizarr."


rin "Etwas zweimal zu verlieren."


show ev rin_roof_doubt onlayer master
with charachange

rin "Besonders, wenn man es zwischendurch nicht wiedergefunden hat."


rin "Es sei denn, Prothesen zählen als 'wiedergefunden'."


show ev rin_roof_nonchalant onlayer master
with charachange

rin "Aber das ist eine andere Art von 'verloren', oder?"


hi "Ich denke schon."


show ev rin_roof_boredom onlayer master
with charachange

rin "Hmm. Ich frage mich…"


stop music fadeout 0.5

show emi rin_roof onlayer master
with charaenter

emi "Was fragst du dich?"


scene bg school_roof onlayer master
show emi basic_grin onlayer master at center
with locationchange

"Emi scheint sich an Rin und mich herangeschlichen zu haben, obwohl Rin nicht sonderlich überrascht aussieht. Was wohl wiederum auch nicht wirklich überraschend ist."


show bg school_roof onlayer master at bgleft
show emi basic_grin onlayer master at twoleft
with charamove

show rin basic_deadpannormal onlayer master:
    tworight
    ypos 1.25
    easein 0.5 ypos 1.2
with charaenter

"Rin schafft es geschickt, sich aufrecht hinzusetzen, indem sie ihren Oberkörper nach vorn wirft und sich mit Hilfe des Impulses aufrichtet."


show rin basic_absent onlayer master:
    ypos 1.2
with charachange

hi "Dein Bein. Wie fühlt es sich an?"


show emi sad_annoyed onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Das bringt mir ein Stirnrunzeln und einen bösen Blick ein."


emi "Es ist okay, denke ich."


show emi sad_shy onlayer master
with charachange

emi "Kein Grund, sich Sorgen zu machen."


show rin basic_absent onlayer master
with charachange

hi "Sag das Doc."


hi "Er besteht darauf, dass du bei ihm vorbeischaust, weißt du?"


show emi sad_pout onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Emi schmollt, als hätte man sie gerade unter Hausarrest gestellt."


emi "Er macht sich zu viele Sorgen."


show emi basic_grin onlayer master
with charachange

emi "Ist doch keine große Sache – nur ein bisschen wund."


"Ich gebe mir Mühe, nicht frustriert die Augen zu rollen."


show rin basic_absent onlayer master
with charachange

hi "Wenn es nichts ist, dann solltest du ihn doch ohne Probleme besuchen können, oder?"


show emi basic_annoyed onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Emi fixiert mich argwöhnisch."


emi "Hat er dir das eingeredet?"


show rin basic_absent onlayer master
with charachange

hi "Na ja, vielleicht. Ein bisschen."


hi "Aber darum geht es nicht. Ich hätte dich auch so daran erinnert, zu ihm zu gehen."


hi "Es wäre doch furchtbar, wenn du dich ernsthaft verletzen würdest, und ich hätte nichts dagegen getan."


hi "Das würde alles noch viel schlimmer machen, und ich will nicht, dass du dich verletzt, weißt du?"


hi "Halt mich für verrückt, aber mir wäre es lieber, du wärst glücklich und gesund."


show emi sad_grin onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Mit jedem Satz schmilzt Emis Stirnrunzeln ein wenig mehr zusammen, und am Ende grinst sie sogar – wenn auch ein wenig scheu."


play music music_daily fadein 4.0

emi "Na ja, wenn du es so sagst, dann werde ich wohl zu ihm gehen müssen."


show emi excited_proud onlayer master
with charachange

emi "Sonst machst du dir nur immer weiter Sorgen und jammerst mir die Ohren voll, oder?"


show rin basic_absent onlayer master
with charachange

hi "Genau. Ich werde dir andauernd damit auf die Nerven gehen, und das könnte unsere Dates beeinträchtigen."





hi "„Wie ist das Essen, Hisao?” „Geh zu Doc, Emi.”"


hi "„Wie war dein Tag, Hisao?” „Geh zu Doc, Emi.”"


hi "„Hisao, wie findest du mein Negli-” {b}„Geh zu Doc, Emi.”{/b}"



hi "Siehst du? Gar nicht gut."


show emi basic_closedhappy onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Emi kichert bei meinem Versuch, ihre Mädchenstimme zu imitieren und schubst mich freundschaftlich."


show emi excited_amused onlayer master
with vpunch

emi "So hoch ist meine Stimme auch nicht, du Idiot."


show rin basic_deadpan onlayer master
show emi excited_circle onlayer master
with charachange

rin "Ich fand es ziemlich gut."


with Pause(3.0)

"Emi und ich starren Rin eine Weile an, bevor ich anfange zu lachen."


show emi sad_annoyed onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Emi verschränkt ihre Arme und schmollt, als ob sie beleidigt wäre."


show emi sad_angry onlayer master
with charachange

emi "Ihr seid beide Idioten."


show rin basic_absent onlayer master
with charachange

hi "Solche abscheulichen Verunglimpfungen von Euch, junge Dame."


hi "Es trifft mich zutiefst, dass ihr mich einen Idioten nennen würdet."


hi "Fürwahr, ich… Ich weiß nicht, was ich davon halten soll."


show emi basic_annoyed onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Emi streckt mir die Zunge heraus."


emi "Esel."


show emi basic_grin onlayer master
with charachange

emi "Also, Rin, wie läuft es denn so im Kunstklub?"


show rin basic_surprised onlayer master
with charachange

"Rin scheint von diesem plötzlichen Themawechsel genauso überrascht zu sein wie ich und lässt sich eine Minute Zeit mit der Antwort."


show rin basic_lucid onlayer master
with charachange

rin "Ich glaube, alles ist in Ordnung."


show rin basic_deadpancontemplation onlayer master
with charachange

rin "Auch wenn Nomiya mir immer sagt, ich soll mir mehr Mühe geben."


show rin relaxed_nonchalant onlayer master
with charachange

rin "Aber ich glaube, er versteht meine Methoden nicht."


show emi sad_annoyed onlayer master
with charachange

emi "Er kam mir immer schon etwas unheimlich vor."


show rin basic_lucid onlayer master
with charachange

"Rin denkt eine Weile über diese Bemerkung nach."


show rin basic_awayabsent onlayer master
with charachange

rin "Ist mir nie richtig aufgefallen."


show rin basic_deadpancontemplation onlayer master
with charachange

rin "Aber ich achte meistens nicht auf ihn; vielleicht liegt es daran."


hi "Wie oft trefft ihr euch?"


show emi basic_closedgrin onlayer master
with charachange

emi "Willst du beitreten, Hisao?"


show rin basic_absent onlayer master
with charachange

hi "Was? Nein, ich habe mich schon entschieden, einem anderen Klub beizutreten."


show emi excited_happy onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Wirklich? Welchem denn?"


show rin basic_absent onlayer master
with charachange

hi "Na ja, ehrlich gesagt ist es nicht wirklich ein Klub…"


show emi excited_proud onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Oh, du bist dem Teeklub beigetreten?"


show rin basic_absent onlayer master
with charachange

hi "Nein, ich… äh… bin dem Naturwissenschaftsklub beigetreten… denke ich."


show emi basic_confused onlayer master
show rin basic_awayabsent onlayer master
with charachange

"Emi sieht hochgradig verwirrt aus."


emi "Wir haben einen Naturwissenschaftsklub?"


show rin basic_absent onlayer master
with charachange

hi "Äh, nicht wirklich. Ich bin das einzige Mitglied."


show emi basic_closedhappy onlayer master
show rin basic_awayabsent onlayer master
with charachange

emi "Hisao, das ist kein Klub. Das bist du in deinem Zimmer beim Bücher Lesen."


hi "Nein, ich meine, es sind nur ich und Mutou."


hi "Ich bin nur bisher der einzige Schüler."


show emi basic_confused onlayer master
show rin basic_lucid onlayer master
with charachange

emi "Mutou? Echt?"


"Ihr scheint etwas einzufallen."


show emi basic_happy onlayer master
with charachange

emi "Oh, habt ihr darüber gestern gesprochen? Dein Treffen mit Mutou?"


hi "Ja, das war wohl unser erstes Treffen, denke ich."


show emi basic_closedgrin onlayer master
with charachange

"Emi kichert."


show emi basic_grin onlayer master
with charachange

emi "Streber."


hi "Hey, ich kann nichts dafür, dass ich so schlau bin."


show emi excited_proud onlayer master
with charachange

emi "Weißt du, ich hätte deine Hilfe schon vor Jahren gebrauchen können."


emi "Du hättest deinen Herzanfall früher haben sollen, Hisao."


"Ich lache, und bemerke dann, dass dies eine der seltenen Gelegenheiten ist, wo ich über meinen Herzanfall lachen konnte."


hi "Ja, hinterher…"


show emi sad_grin onlayer master
with charachange

emi "Ja…"


play sound sfx_warningbell

"Das Läuten der Glocke beendet unser Gespräch."


hi "Hmm, wir brechen wohl besser auf."


show emi basic_grin onlayer master
with charachange

emi "Ja, denke ich auch."


show emi excited_amused onlayer master:
    xpos 0.45
with dissolvecharamove

emi "Komm schon, Rin, du auch."


show rin basic_surprised onlayer master
with vpunch

"Rin ist anscheinend kurz weggenickt, daher versetzt Emi ihr einen unsanften Stoß."


show rin basic_deadpanupset onlayer master
with charachange

rin "Beinahe hätte ich es gehabt."


show emi basic_closedgrin onlayer master
with charachange

emi "Tut mir leid, aber du musst zum Unterricht."


show rin relaxed_nonchalant onlayer master at tworight
with dissolvecharamove

rin "Finde ich nicht, aber vielleicht schaffe ich es ja, wenn ich im Unterricht etwas schlafe."


show rin relaxed_boredom onlayer master
with charachange

rin "Ein Ortswechsel ist bei solchen Dingen oft sehr hilfreich."


"Weder Emi noch ich fragen sie, wovon sie redet."


stop music fadeout 3.0
stop ambient fadeout 2.0
scene bg school_hallway3 onlayer master
with locationskip

"Als wir an meinem Klassenzimmer ankommen, gibt Emi mir einen schnellen Kuss und verschwindet mit Rin im Schlepptau den Flur hinunter."


show shizu behind_blank onlayer master:
    tworight
    xpos 0.8
    easein 0.5 tworight
show misha perky_smile onlayer master:
    twoleft
    xpos 0.2
    easein 0.5 twoleft
with charaenter

"Ich wende mich der Klassenzimmertür zu und stehe Shizune und Misha gegenüber."


play music music_shizune fadein 1.0

show shizu adjust_happy onlayer master
with charachange

shi "…"


"Misha kämpft tapfer gegen einen Lachanfall, während sie Shizunes Vortrag übersetzt."


show misha hips_grin onlayer master
with charachange

mi "Wir sind zwar erfreut – um nicht zu sagen begeistert – zu sehen, wie schnell du neue Freunde gefunden hast und Beziehungen eingegangen bist – und noch dazu mit so einem süßen Mädel, Hicchan~…"


"Ich denke, der letzte Teil kam wahrscheinlich von Misha."


show shizu basic_normal onlayer master
with charachange

shi "…"


show misha hips_frown onlayer master
with charachange

mi "Nichtsdestotrotz sehen wir uns dazu gezwungen, dich freundlich daran zu erinnern, dass öffentliche Zuneigungsbekundungen strikt verboten sind – Wirklich? Wie schade, Shicchan – laut Abschnitt acht der Verhaltensregeln im Schülerhandbuch."


show shizu adjust_smug onlayer master
with charachange

shi "…"


show misha sign_smile onlayer master
with charachange

mi "In diesem Fall jedoch, könnte das Unwissen über diese Regel deinen Verstoß entschuldigen, und da wir heute großzügig sind…"


show shizu behind_smile onlayer master
with charachange

shi "…"


show misha hips_smile onlayer master
with charachange

mi "… und die Formulare, die notwendig wären, um euch beide zu bestrafen, nur die bereits immense Arbeitsbelastung, die auf uns – den einzigen Mitgliedern des Schülerrats – lastet, verschlimmern würde…"
mi "… und weil ihr Zwei einfach zu süß zusammen seid~!"


show shizu adjust_happy onlayer master
with charachange

shi "…"


show misha hips_grin onlayer master
with charachange

mi "Deshalb ist dies eine formelle Verwarnung, und bitte seht in Zukunft von solchen Zurschaustellungen ab. Zumindest wenn Shicchan euch sehen kann, Hicchan~!"


"Das ganze Geschwafel ist so lächerlich, dass ich einfach im gleichen Stil antworten muss."


hi "Nun, ich für meinen Teil fühle mich erleuchtet."


hi "Ich bitte vielmals um Entschuldigung für meine unbedachten Handlungen."
hi "Ich werde mir Mühe geben, in Zukunft meine niederen Instinkte besser zu unterdrücken, die, wie ich fürchte, diese unangebrachte öffentliche Zuneigungsbekundung verursacht haben."


hi "Es ist mitnichten mein Wunsch, einen bereits überarbeiteten Schülerrat mit solch trivialen Angelegenheiten zu belasten und werde mein Bestes tun, um euer Leben zukünftig in dieser Hinsicht zu erleichtern."


hi "Zumindest wenn Shizune hinschaut."


"Den letzten Teil sage ich mit einem Zwinkern in Mishas Richtung, die daraufhin endgültig ihren Kampf gegen den Lachanfall verliert."


show misha cross_laugh onlayer master
with charachange

mi "Wahaha~!"


show misha cross_grin onlayer master
with charachange

mi "Sehr gut gesagt, Hicchan~!"


"Ich kichere selbst ein wenig, und wir betreten den Klassenraum."


stop music fadeout 2.0
scene bg school_scienceroom onlayer master
with shorttimeskip

"Der Unterricht verläuft ereignislos, und nach Schulschluss bin ich wieder allein mit Mutou."


show muto smile onlayer master at center
with charaenter

mu "So, es sieht so aus, als wären wir alle versammelt für das zweite Treffen des Naturwissenschaftsklubs."


play music music_another fadein 2.0
show muto normal onlayer master
with charachange

mu "Oder ist es das erste? Was denkst du, sollten wir gestern als ein Treffen zählen?"


hi "Na ja, wir haben den Klub gestern gegründet, oder nicht?"


hi "Das ist doch eine Klubangelegenheit, also können wir das gestern ruhig als Treffen ansehen."


show muto smile onlayer master
with charachange

"Mutou lächelt auf seine übliche hölzerne und unbeholfene Art. Ich frage mich, ob die Muskeln in seinem Gesicht für ein natürliches Lächeln einfach falsch geformt sind."


mu "Du hast wirklich Talent für so was, denke ich. Ich meine logisches Denken."


hi "Kann sein…"


show muto normal onlayer master
with charachange

mu "Ein Wissenschaftler spricht mit Autorität, Hisao. Die Antwort wäre gewesen „Ja, das habe ich.”"


mu "Wenn die Welt wissen will, wie sie funktioniert, sagen wir es ihr. Auch wenn wir nicht mehr als eine ordentliche Hypothese haben."


show muto smile onlayer master
with charachange

mu "Aber wir müssen uns trotzdem überzeugend anhören, weil wir die Spezialisten auf diesem Gebiet sind, richtig?"


"Er lacht, um sein unbeholfenes Lächeln über seinen unbeholfenen Witz zu kaschieren. Ich gebe mir Mühe, nicht das Gesicht zu verziehen, aber ich glaube, ich hatte keinen Erfolg."


show muto normal onlayer master
with charachange

mu "Das ist natürlich kompletter Unsinn."


mu "Sicher, wir wissen eine Menge, aber niemand ist ein Experte dafür, wie die Welt funktioniert – schon allein weil sich niemand sicher sein kann. Ohne Sicherheit keine Experten."


mu "Aber wir tun manchmal gerne so als ob."


hi "Aber es gibt doch auch Dinge, deren wir uns sicher sein können, oder?"


mu "Ja… Aber auch nein."


mu "Wir wissen zum Beispiel, dass es die Schwerkraft gibt."


"Zur Demonstration nimmt Mutou einen Bleistift und lässt ihn fallen."


mu "Siehst du? Immer noch da. Aber es ist gut, das ab und zu mal zu überprüfen."


mu "Deshalb gibt es immer noch Forscher, die sich mit der Schwerkraft beschäftigen."


show muto smile onlayer master
with charachange

mu "Wir sind uns ziemlich sicher, dass wir wissen, wie sie funktioniert, aber es gibt immer die Möglichkeit, dass irgendetwas nicht so ist, wie wir denken."


mu "Also muss man prüfen und prüfen und prüfen. Das ist die Essenz der Wissenschaft, Hisao."


"Die ganze Zeit habe ich wie gebannt zugehört. Mutou scheint bei diesem Thema richtig enthusiastisch zu sein… denke ich. Manchmal ist das schwer zu sagen."


"Wie die Welt funktioniert…"


"Wie Menschen funktionieren."


"Wie das Universum funktioniert."


"All diese Fragen beantworten zu können."


"Und je nachdem welche Richtung ich einschlage, könnte ich sogar auf etwas stoßen, um mein Herz in Ordnung zu bringen. Na ja, das ist wohl eher nicht meine wahre Priorität."


"Als wir anfangen, das Buch zu diskutieren, das er mir gestern gegeben hat, finde ich, dass mich das Thema viel mehr interessiert als mein Herzfehler."


show muto normal onlayer master
with shorttimeskip

"Bevor wir uns versehen, ist eine Stunde vorbei."


mu "Nun, lass uns das Treffen für heute beenden, in Ordnung?"


mu "Das nächste Treffen machen wir… morgen, oder äh… übermorgen."


"Er überlegt einen Moment."


mu "Sagen wir übermorgen. Ich muss noch eine Menge Tests benoten."


hi "Okay. Bis dann."


scene bg school_hallway3 onlayer master
with locationchange

stop music fadeout 5.0

"Als ich den Klassenraum verlasse, fällt mir auf, dass ich heute Abend noch gar nichts vorhabe."


"Emi und ich haben nichts geplant, also…"


"Ich denke, ich gehe in die Bibliothek. Immer noch besser, als in meinem Zimmer Hausaufgaben zu machen."


scene black onlayer master
with locationskip_in



label de_E20:

play music music_happiness fadein 2.0
scene bg school_library onlayer master
with locationskip_out

"Die Bibliothek fühlt sich immer kühler an als der Rest des Gebäudes."


"Wahrscheinlich damit die Bücher nicht durch übermäßige Hitze oder Feuchtigkeit beschädigt werden."


"Bücher sind ziemlich widerstandsfähig, aber wenn man sie in gutem Zustand erhalten will, muss man sich ein wenig Mühe geben."


"Ich habe einige Bücher, die so zerlesen sind, dass die Seiten fast herausfallen."


"Es scheint unmöglich zu sein, sie noch zu lesen, aber wenn man sie sorgfältig behandelt…"


"Ich gehe zum Schalter, wo Yuuko gerade mit irgendetwas beschäftigt ist."


show yuuko neutral_up onlayer master at center
with charaenter

"Sie lächelt mir zu und winkt, als sie mich kommen sieht."


show yuuko closedhappy_down onlayer master
with charachange

yu "Hallo, Hisao."


show yuuko happy_down onlayer master
with charachange

yu "Schön, dich zu sehen! Wonach suchst du denn heute?"


hi "Nichts Spezielles, denke ich. Ich wollte einfach nicht zurück auf mein Zimmer gehen, das ist alles."


show yuuko neutral_down onlayer master
with charachange

"Yuuko nickt."


show yuuko smile_up onlayer master
with charachange

yu "Na ja, wenn du nichts zu tun hast, könntest du mir vielleicht helfen, nach etwas zu suchen?"


hi "Klar, was brauchst du denn?"


stop music fadeout 5.0

show yuuko worried_up onlayer master
with charachange

"Yuuko legt einen Finger auf ihre Lippen und schaut sich vorsichtig um."


"Sie scheint zu schauen, ob uns jemand zuhört."


yu "Komm näher."


show yuuko worried_up_close onlayer master
with characlose

"Ich trete zögernd ein paar Schritte näher. Ihr Verhalten macht mich etwas nervös."


"Yuuko senkt ihre Stimme zu einem verschwörerischen Flüstern."


show yuuko neutral_up_close onlayer master
with charachange

yu "Ich suche den Bücherdieb von Yamaku."


play music music_tension fadein 0.5

hi "Wen?"


show yuuko panic_up_close onlayer master
with charachange

yu "Psst! Die Wände haben Ohren, Hisao!"


yu "Könnten sie zumindest."


show yuuko worried_down_close onlayer master
with charachange

yu "Aber hör zu! Diese fehlenden Bücher – erinnerst du dich?"


hi "Äh, ja?"


show yuuko worried_up_close onlayer master
with charachange

yu "Nu, sie fehlen nicht einfach nur, sie wurden gestohlen!"


yu "Ich bin davon überzeugt!"


hi "Du hast schon mal so was in der Richtung gesagt, aber warum bist du dir so sicher?"


"Yuuko kommt näher und flüstert noch leiser – falls das überhaupt möglich ist."


show yuuko closedhappy_down_close onlayer master
with charachange

yu "Weil ich eines seiner Verstecke gefunden habe!"


hi "Du hast was?"


"Yuuko schaut mich triumphierend an."


show yuuko happy_up_close onlayer master
with charachange

yu "Ich habe eines seiner Verstecke gefunden! Es war unter einer der Treppen im Jungenwohnheim!"


yu "Drei der Bücher, die ich gesucht hatte – alle da!"


show yuuko closedhappy_up_close onlayer master
with charachange

yu "Ich hatte schon vorher einen Dieb vermutet, aber das ist der Beweis!"


hi "Also hast du die Bücher wieder?"


show yuuko panic_up_close onlayer master
with charachange

"Yuuko sieht aus, als hätte ich gerade vorgeschlagen, sie solle nackt herumlaufen."


yu "Bist du verrückt?"


show yuuko worried_down_close onlayer master
with charachange

yu "Er darf nicht wissen, dass ich ihm auf der Spur bin! Er könnte untertauchen und sich seiner Festnahme entziehen!"


hi "A-ha… Und wozu brauchst du dann meine Hilfe?"


"Yuuko schaut sich nochmals in der Bibliothek um und kommt noch näher."


show yuuko neutral_down_close onlayer master
with charachange

yu "Du musst für mich spionieren."


hi "Spionieren?"


yu "Genau, du weißt schon, wenn du im Wohnheim bist."


show yuuko closedhappy_down_close onlayer master
with charachange

yu "Auf verdächtige Aktivitäten achten."


"Was genau zählt denn in diesem Fall als verdächtig?"


"Ich meine, Kenji ist ein ziemlich verdächtiger Kerl, aber er geht ja kaum zum Unterricht, da wird er kaum in die Bibliothek schleichen, um Bücher zu stehlen."


"Na ja, es kann ja nicht schaden, zuzustimmen, oder? Zumindest kann ich so diese verrückte Unterhaltung beenden."


hi "Klar, kann ich machen. Kein Problem."


show yuuko closedhappy_down onlayer master
with charadistant

"Yuuko richtet sich auf und klatscht aufgeregt in die Hände."


yu "Großartig!"


show yuuko worried_down onlayer master
with charachange

yu "Nun rede schnell über was anderes, falls jemand hereinkommt!"


stop music fadeout 2.0

show yuuko happy_down onlayer master
with charachange

yu "Wie läuft es so in der Schule?"


hi "Äh, eigentlich ziemlich gut."


hi "Morgens laufe ich immer ein paar Runden mit-"


show yuuko closedhappy_up onlayer master
with charachange

yu "Emi Ibarazaki, stimmt's?"


play music music_comedy fadein 2.0

hi "Äh, ja."


hi "Woher weißt du das?"


show yuuko smile_down onlayer master
with charachange

yu "Ich habe euch zwei im Shanghai bedient, erinnerst du dich?"


show yuuko closedhappy_down onlayer master
with charachange

yu "Ich dachte mir, wenn du mit irgendjemandem läufst, dann wahrscheinlich mit ihr."


"Sie sieht zufrieden mit sich selbst aus."


hi "Beeindruckend."


hi "Jedenfalls… Ja, wir laufen Morgens zusammen."


hi "Und, äh, wir sind nun auch zusammen."


show yuuko closedhappy_up onlayer master
with charachange

"Yuuko klatscht wieder aufgeregt in die Hände."


yu "Wirklich? Das ist großartig!"


yu "Ich wette, ihr Zwei gebt ein tolles Paar ab!"


show yuuko neutral_down onlayer master
with charachange

yu "Ich liebe es, zu sehen, wie Menschen einander finden, weißt du?"


yu "Als du damals ins Shanghai gekommen bist, dachte ich mir sogar, „Ich frage mich, ob der Junge mit einem dieser Mädchen zusammenkommen wird.”"


hi "… Wirklich?"


"Yuuko scheint nicht zu bemerken, dass ich das ein wenig befremdlich finde, und nickt bestätigend."


show yuuko closedhappy_down onlayer master
with charachange

yu "Ja! Ich wusste, dass du mit einer von ihnen zusammenkommen würdest, weißt du?"


show yuuko neutral_down onlayer master
with charachange

yu "Ich habe ein Auge für so was."


show yuuko worried_down onlayer master
with charachange

yu "Allerdings…"


"Ihr Gesicht verdunkelt sich leicht."


yu "Ich selbst habe nicht so viel Erfolg."


hi "Ach, ich bin mir sicher, dass das nicht stimmt."


show yuuko neutral_down onlayer master
with charachange

yu "Oh doch, es stimmt."


yu "Ich habe da mal diesen Kerl getroffen…"


show yuuko smile_down onlayer master
with charachange

yu "Wir haben uns wirklich gut verstanden, aber es stellte sich heraus, dass er jünger war als ich."


show yuuko neutral_up onlayer master
with charachange

yu "Und das war etwas komisch, aber nicht wirklich schlimm."


yu "Aber dann ist er eines Tages einfach verschwunden, und ich habe ihn seitdem nicht wiedergesehen."


hi "Hmm. Das hört sich ziemlich seltsam an."


show yuuko worried_up onlayer master
with charachange

yu "Nicht wahr?"


show yuuko neurotic_down onlayer master
with charachange

yu "Ich hoffe, ich habe nichts falsch gemacht…"


"Ich muss ihr einfach ein wenig Mut machen."


hi "Ich bin mir sicher, dass es nicht an dir lag."


stop music fadeout 4.0

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_phone
show yuuko panic_up onlayer master
with vpunch

"Ich will sie noch weiter beruhigen, aber wir schrecken beide zusammen, als es in meiner Tasche plötzlich klingelt."


show yuuko worried_down onlayer master
with charachange

"Yuuko seufzt, während ich das Telefon aus meiner Tasche hole. Mir ist es ein wenig peinlich, indirekt für den Radau verantwortlich zu sein."


scene bg school_library_yuuko_blurred onlayer master
show phone mobile onlayer master:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)

hi "Emi? Was gibt's?"


emi "Oh Gott sei Dank ich habe dich noch nie angerufen also wusste ich nicht ob die Nummer funktioniert oder ob du abhebst und ich kann nicht—"


$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play music music_pearly fadein 2.0

hi "Whoa, Emi, ganz langsam."


hi "Was ist los?"


"Einen Moment lang ist es am anderen Ende der Leitung still. Ich höre nur Emis schweren Atem, als sie versucht, sich zu beruhigen."


"Irgendetwas hat sie furchtbar aufgewühlt, und langsam wühlt es auch mich auf."


emi "Kannst du einfach…"


emi "Kannst du vorbeikommen?"


emi "Jetzt? Oder zumindest bald?"


emi "Ich muss mit dir reden – ich brauche dich."


"In ihrer Stimme liegt ein flehender Unterton, den ich so noch nie von ihr gehört habe."


hi "Natürlich, ich bin sofort da."


hi "Halt durch, okay?"


"In meiner Aufregung fange ich an, Dinge zu sagen, die keinen Sinn ergeben."


emi "Okay. Ich warte auf dich."


hi "Bis gleich."


show phone mobile onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_library onlayer master
show yuuko worried_down onlayer master at center
show phone mobile onlayer master:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone onlayer master
with None

with charaexit

"Ich drücke den Knopf, um das Gespräch zu beenden, stecke das Telefon zurück in meine Tasche, entschuldige mich bei Yuuko für meinen abrupten Aufbruch und mache mich auf den Weg."



scene bg school_girlsdormhall onlayer master
with locationskip

"Vielleicht hätte ich irgendwann auf die Uhr geschaut und darüber nachgedacht, wie es aussieht, wenn ein Junge um diese Zeit ins Mädchenwohnheim geht."


"Im Moment ist aber das einzige, was mir durch den Kopf geht, herauszufinden, was mit Emi los ist und wie ich ihr helfen kann."


play sound sfx_doorknock2

"Ich klopfe an ihre Tür und werde mit einem gedämpften „Komm rein” begrüßt."


scene bg school_dormemi onlayer master at left
with locationchange

"Irgendetwas stimmt ganz und gar nicht, als ich die Szene vor mir betrachte."


"Emi ist da, soviel ist richtig."


"Aber sie sitzt in einem Rollstuhl."


"Und ihre Beine fehlen. Ich schaue mich in dem Zimmer um und sehe sie in einer Ecke liegen, als ob sie jemand dorthin geworfen hätte."


show emiwheel weaksmile onlayer master at center
with charaenter

"Emi reagiert mit einem schiefen Grinsen auf mein Erscheinen. Es scheint, als sei sie gleichzeitig froh mich zu sehen und total verzweifelt."


emi "Hi, Hisao."


"Es sieht so aus, als hätte sie geweint, aber wenn, dann hat sie nun aufgehört."


"Ich bemerke, dass ich ein wenig außer Atem bin. Ich habe auf dem Weg hierher immer zwei Stufen auf einmal genommen."


"Meinem Herz scheint die Anstrengung aber nichts ausgemacht zu haben. Ich merke mir diesen glückliche Tatsache für später."


"Für irgendwann, wenn ich nicht sprachlos meine in einem Rollstuhl sitzende Freundin anstarre."


"Ich merke, dass ich noch immer nicht auf ihre Begrüßung reagiert habe, und mein Gehirn nimmt langsam wieder Fahrt auf."


hi "Emi? Was ist passiert?"


show emiwheel pout onlayer master
with charachange

emi "Ich hätte wohl auf dich hören sollen, Hisao."


show emiwheel sad onlayer master
with charachange

emi "Mein Bein hat eine böse Entzündung. Ich darf die nächsten paar Wochen nicht laufen."


"Sie lacht mit einer Bitterkeit, die ich nie von ihr hören wollte."


show emiwheel frown onlayer master
with charachange

emi "Heh, ich kann nicht einmal damit gehen."


emi "Ich hätte eine Krücke benutzen und das andere Bein behalten können, aber ich fand das sinnlos."


show emiwheel awayfrown onlayer master
with charachange

emi "Warum hüpfen? Man kann mit einem Bein nicht rennen."


show emiwheel pout onlayer master
with charachange

emi "Auf diese Weise kann ich wenigstens… Ich weiß nicht… Schnell rollen oder so was."


hi "J-Ja, das ist doch gut, oder?"


"Mein linkischer Versuch, die positive Seite zu sehen, ist nicht wirklich effektiv, auch wenn sie sich darüber zu freuen scheint."


"Emi zuckt mit den Schultern."


show emiwheel awayfrown onlayer master
with charachange

emi "Es ist nur… irgendwie lästig."


show emiwheel frown onlayer master
with charachange

emi "Ich meine, wir können nicht mal mehr zum Essen aufs Dach. Kein Zugang für Rollstühle."


hi "Schon, aber das ist doch nicht so schlimm, oder?"


hi "Ich meine, wir können immer noch zusammen essen, und das ist doch das Wichtige."


show emiwheel weaksmile onlayer master
with charachange

"Wieder dieses schiefe Grinsen. Es schmerzt, es zu sehen."


emi "Wahrscheinlich, ja."


show emiwheel frown onlayer master
with charachange

emi "Aber wie gesagt, es ist lästig."


show emiwheel awayfrown onlayer master
with charachange

emi "Ich meine, ich habe keinen Rollstuhl mehr benutzt, seit…"


stop music fadeout 10.0

"Sie überlegt einen Moment."


show emiwheel pout onlayer master
with charachange

emi "Vielleicht sieben Jahre? Irgendwas in der Richtung."


emi "Eine lange Zeit."


show emiwheel weaksmile onlayer master
with charachange

emi "Ich fürchte, ich bin ein wenig aus der Übung."


hi "Na ja, zum Glück ist es nur vorübergehend, oder?"


"Emi nickt."


show emiwheel neutral onlayer master
with charachange

emi "Oh ja, natürlich."


emi "Es ist nicht so, als ob ich sie für immer verloren hätte."


show emiwheel awayfrown onlayer master
with charachange

emi "Aber es geht mir trotzdem tierisch auf den Zeiger."


"Ich nicke mitfühlend."


"Viel mehr kann ich ja leider nicht tun."


"Was soll ich sagen? „Ich hab's dir doch gleich gesagt?”"


"Schließlich {b}habe{/b} ich ihr gesagt, sie soll mit dem Bein zu Doc gehen."


"Aber als es mir aufgefallen ist, war es sowieso zu spät."


hi "Brauchst du mit irgendwas Hilfe?"


hi "Äh, das heißt, kann ich dir mit irgendwas helfen?"


show emiwheel closedsmile onlayer master
with charachange

"Emi schüttelt den Kopf, und ihr normales Grinsen kommt ein bisschen zum Vorschein."


emi "Nö, ich komme ganz gut zurecht."


show emiwheel grin onlayer master
with charachange

emi "Aber wenn du mir ins Bett helfen würdest, müsste ich nicht selbst rüberrollen."


"Ich kann nicht verhindern, dass mir das Blut ins Gesicht schießt."


"Emi kichert."


play music music_heart fadein 0.5

show emiwheel wink onlayer master
with charachange

emi "Du bist so was von prüde, Hisao."


hi "Ich bin nicht prüde! Ich will nur nicht eine junge Frau wie dich ausnutzen."


hi "Das gehört sich nicht für einen Gentleman."


hide emiwheel onlayer master
with charaexit

show bg school_dormemi onlayer master at right
with charamove

"Ich rolle Emis Stuhl zu ihrem Bett, hebe sie heraus und lege sie hinein. Sie macht es sich schnell bequem und setzt sich auf die Bettkante."


show emi basic_grin onlayer master:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter

"Sie ist sogar ein wenig schwerer als sie aussieht. Es wäre natürlich unhöflich von mir, das auszusprechen."


hi "Mann, du bist ziemlich schwer."


play sound sfx_pillow
show comic vfx2 onlayer master
show emi excited_amused onlayer master:
    center
    ypos 1.1
with hpunch

with Pause(0.5)

show comic vfx2 onlayer master:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)

"Emi wirft ein Kissen nach mir."


show emi basic_closedgrin onlayer master
with charachange

emi "Esel."


hi "Nur eine Feststellung, nichts weiter."


hi "Muss an all dem Gerenne liegen."


show emi sad_shy onlayer master
with charachange

"Als ich das Laufen erwähne, fällt Emis Grinsen etwas zusammen."


show emi sad_pout onlayer master
with charachange

emi "Na ja, wenigstens muss ich mir darüber in nächster Zeit keine Gedanken machen, hmm?"


show emi sad_grin onlayer master
with charachange

emi "Vielleicht nehme ich etwas ab."


hi "Das macht man doch, um abzunehmen, oder? Mit dem Sport aufhören?"



show emi basic_closedgrin onlayer master
with charachange

emi "Ich bin mir ziemlich sicher, dass Doc das empfehlen würde."


hi "Wo wir gerade davon sprechen – wirst du Morgens trotzdem zum Sportplatz kommen?"


hi "Ich würde nur ungern all-"


show emi sad_depressed onlayer master
with charachange

emi "Ach, scheiße…"


"Emis plötzlicher Ausruf ist mehr ein Gemurmel als etwas zu profanes, aber ich schaue schockiert zu ihr hinüber."


"Sie sitzt vornüber gebeugt, die Hände vor ihrem Gesicht, und versucht zu verbergen, dass sie weint."


"Natürlich macht ihr Schluchzen das aber ziemlich offensichtlich."


hi "Hey, tut mir leid."


hi "Vergiss, dass ich etwas gesagt habe, okay?"


show emi sad_depressed_close onlayer master at center
with characlose

"Ich lege vorsichtig einen Arm um sie und ziehe sie an mich heran."


"Ich weiß nicht, was ich sonst sagen oder tun könnte. Wie tröstet man jemanden, der gerade wieder seine Beine verloren hat?"


show emi sad_pout_close onlayer master
with charachange

"Emi umarmt mich und bleibt eine Weile in dieser Position."


hi "Tut mir leid."


hi "Ich bin nicht wirklich gut im Trösten, fürchte ich."


emi "Sag das nicht."


emi "Es geht mir gut, wirklich."


"Ihre Stimme ist ein wenig schwer zu verstehen, weil ihr Gesicht an meine Brust gepresst ist. Ich streichele ihr beruhigend über den Kopf."


hi "Das ist die richtige Einstellung."


hi "Du wirst das schon überstehen, das weiß ich."


hi "Außerdem bin ich ja da, um dir zu helfen, weißt du noch?"


show emi sad_shy_close onlayer master
with charachange

"Emi hebt ihren Kopf und starrt mich aus verweinten Augen an."


show emi sad_grin_close onlayer master
with charachange

emi "Kannst du das? Kannst du das wirklich?"


"Sie grinst mich schief an, und etwas funkelt in ihren Augen."


"Ich weiß nicht, ob sie sich über mich lustig macht oder nicht."


hi "Natürlich. Ich meine, klar, du bist ein wenig schwer, aber{w=0.5}{nw}"


play sound sfx_impact

show emi excited_amused_close onlayer master
with vpunch

extend " uff!"


"Mein geistreicher Kommentar wird unterbrochen, als sich Emis Lippen plötzlich auf meine pressen. Ich bin überrascht, und zur Belohnung stoße ich mir den Kopf an der Wand hinter ihrem Bett."


hi "Autsch."


show emi basic_hes onlayer master
with charadistant

"Emi setzt sich auf und versucht besorgt auszusehen. Stattdessen sieht sie aus, als würde sie jeden Moment loslachen."


emi "Alles okay?"


show emi excited_proud onlayer master
with charachange

emi "Sorry!"


"Ich reibe mir den Hinterkopf und grinse zurück."


hi "Da hab ich gerade nicht aufgepasst."


hi "Wird das zur Gewohnheit? Muss ich mir noch mehr Standpauken von Shizune und Misha anhören?"


"Als ich das Duo erwähne, kichert Emi."


show emi basic_closedgrin onlayer master
with charachange

emi "Also ehrlich, diese beiden…"


show emi basic_grin onlayer master
with charachange

emi "Wenn ich es nicht wüsste, würde ich nie darauf kommen, warum sie immer mit so einer herrschsüchtigen Person herumhängt."


hi "Von welcher der beiden reden wir?"


show emi basic_closedhappy onlayer master
with charachange

emi "Du weißt genau, wen ich meine, Hisao. Misha ist ja wohl kaum herrschsüchtig."


hi "Und was ist der Grund?"


show emi basic_confused onlayer master
with charachange

emi "Hm?"


hi "Der Grund, warum Misha immer mit Shizune herumhängt."


show emi basic_closedgrin onlayer master
with charachange

"Emi winkt lächelnd ab."


emi "Keine Ahnung."


hi "Aha."


show emi basic_grin onlayer master
with charachange

emi "Na ja, du scheinst jedenfalls die ursprüngliche Frage vergessen zu haben, oder?"


hi "Ach ja, das stimmt wohl."


hi "Hättest du was dagegen, mich das nächste Mal vorzuwarnen?"


hi "Sonst kriege ich früher oder später 'ne Gehirnerschütterung."


"Ich bekräftige das, indem ich mir nochmals den Hinterkopf reibe."


show emi excited_amused onlayer master
with charachange

"Emi kichert."


emi "Du könntest einen Helm tragen."


show emi excited_proud onlayer master
with charachange

emi "Einige der Schüler hier tun das, weißt du?"


stop music fadeout 1.0

hi "Oder ich könnte mich einfach rächen!"


play sound sfx_pillow

show emi excited_circle onlayer master
with vpunch

"Ich greife nach einem der Kissen neben mir und ziehe es Emi über den Kopf."


show expression im.Composite((295,1200), (0,0), "sprites/emi/emi_excited_circle.png") as emi onlayer master:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.8 ypos 1.25 rotate -90
with None

show expression im.Composite((295,1200), (0,0), "sprites/emi/emi_excited_sad.png") as emi onlayer master:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.8 ypos 1.25 rotate -90

with Dissolve(0.5)
with Pause(0.3)

play sound sfx_impact

hide emi onlayer master
with vpunch

"Emi kippt vom Bett und landet mit einem dumpfen Schlag auf dem Boden."


show emi sad_pout onlayer master:
    center
    ypos 1.2
    ease 1.0 ypos 1.0
with Dissolve(1.0)

"Ihre Arme erscheinen sofort wieder auf dem Bett und sie zieht sich wieder herauf."


"Sie hat wirklich überraschend viel Kraft in diesem kleinen Körper."


"Ihr Gesicht ist gesenkt und von mir abgewendet, und einen Moment lang denke ich, ich könnte ihr wehgetan haben."


hi "Emi? Alles in Ordnung?"


hi "Hast du dir den—{w=0.3}{nw}"


show emi excited_smile_close onlayer master
with vpunch

"Eine Hand schießt nach oben und greift meinen Kragen. Mit einem scharfen Ruck zieht sie mich nach vorne, ihr Gesicht ist nur noch wenige Zentimeter von meinem entfernt, und sie grinst frech."


hi "Emi…?"


show emi excited_smile_close onlayer master:
    subpixel True
    linear 0.1 ypos 1.7 zoom 2.0 
with None

scene white onlayer master
with Dissolve(0.1)

play sound sfx_impact

scene black onlayer master
with Dissolve(0.75)

"Sie gibt mir eine heftige Kopfnuss. Ihre Stirn trifft meine mit einem lauten Schlag."


scene bg school_dormemi onlayer master at right
show emi basic_closedgrin onlayer master at center
with openeye

"Ich gehe auf Abstand und reibe meinen schmerzenden Kopf, während Emi siegreich grinst."


show emi basic_grin onlayer master
with charachange

emi "Wie gefällt dir {b}das{/b} als Rache?"


play music music_running

hi "Unfair!"


hi "Du kannst für Rache keine Rache nehmen!"


"Für jemanden, der keine Beine hat, ist Emi überraschend agil."


show emi basic_grin onlayer master:
    center
    parallel:
        "emi basic_closedgrin" with Dissolve(0.2, alpha=True)
    parallel:
        easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi onlayer master
with None

"Ich schwinge das Kissen nach ihr, aber sie weicht flink aus und trifft mich mit einem anderen Kissen."


"Natürlich ist sie im Nachteil. Im Gegensatz zu ihr kann ich aufstehen."


scene black onlayer master
with vpunch

"Uff!"


window hide

show evh emi_grinding_victorytall onlayer master:
    xalign 0.5 yalign 1.0 subpixel True
    easein 12.0 yalign 0.0

with Dissolve(1.0)

with Pause(6.0)

window show

"Sieht aus, als könnte ich das doch nicht. Emi hat mich zu Fall gebracht und sitzt nun auf mir, während ich auf dem Rücken liege. Ich bin mir noch nicht einmal sicher, wie sie das geschafft hat."


emi "Gewonnen!"


"Ihre Augen funkeln schelmisch. Ich wurde vollständig besiegt – und das von einem Mädchen, dass nicht mal annähernd so groß ist wie ich."


"Allerdings ist es wohl gar nicht so schlimm, besiegt zu werden. Emi sitzt auf meiner Hüfte, und das ist etwas, was weder ich noch mein Körper so ohne Weiteres ignorieren können."


scene bg school_dormemi onlayer master
with locationchange

"Ich öffne meinen Mund, aber Emi ist schneller. Bevor ich auch nur ein Wort sagen kann, presst sie ihre Lippen auf meine. Ich leiste keinen Widerstand – warum sollte ich auch?"


"Das ist… irgendwie anders."


"Sie weicht kurz zurück, knabbert an meiner Unterlippe und schlingt dann ihre Arme um mich. Ihre Zunge dringt forschend in meinen Mund ein. Ich spüre, wie eine Wärme meinen Körper durchströmt, und mein Herz beginnt schneller zu schlagen."


"Meine Wahrnehmung verschwimmt, und ich merke nur noch, wie meine Hand an Emis Bluse nach oben wandert. Emi zieht scharf Luft ein, als ich ihre Brust erreiche, dann kichert sie, und dann-"


scene evh emi_grinding_victory onlayer master
with locationchange

"Ich starre in das Gesicht einer grinsenden Emi."


emi "Ich hab's dir doch gesagt. Damit habe ich jetzt zweimal gewonnen."


hi "Was? Das zählt nicht. Du hast deine weiblichen Reize eingesetzt."


show evh emi_grinding_wink onlayer master
with charachange

emi "„In der Liebe und im Krieg ist alles erlaubt”, nicht wahr?"


emi "Ha, und du wirst sogar rot! Ich wusste gar nicht, dass du so einer bist, Hisao."


hi "Du weißt schon, dass du genauso rot geworden bist. Wahrscheinlich, weil du so prüde bist."


"Sogar ich muss zugeben, dass es ziemlich dämlich ist, so etwas zu einer Frau zu sagen, die gerade auf mir sitzt und die bis vor ein paar Sekunden ihre Zunge in meinem Mund hatte."


show evh emi_grinding_grin onlayer master
with charachange

emi "Ich und prüde?"


emi "Nun, dann schauen wir mal, wer zuerst rot wird, oder?"


"Ich bin mir nicht sicher, ob ihr Ton mir Angst macht oder mich erregt, aber diese Frage hat sich schnell erledigt."



label de_E20h:

show evh emi_grinding_half_undress onlayer master
with charachange

show evh emi_grinding_half_grin onlayer master
with charachange

"Mit einer geübten Bewegung zieht sie sich ihre Bluse über den Kopf und wirft sie achtlos beiseite. Ihr BH und ihr Rock liegen kurz darauf auch auf dem Boden."


emi "Ha!"


"Ich versuche, nicht rot zu werden. Es ist ziemlich schwierig."


hi "Eskalation, hm?"


show evh emi_grinding_off_yawn onlayer master
with charachange

"Ich ziehe mein Hemd aus, was aufgrund meiner Position etwas schwieriger ist. Emi tut so, als ob sie gähnen würde."


emi "Da musst du dir schon mehr Mühe ge-"


show evh emi_grinding_off_closesurprise onlayer master
with charachange
stop music fadeout 3.0

emi "Ah…!"


"Meine Hände streichen zärtlich über Emis nackte Haut und bringen sie zum Schaudern. Es sieht so aus, als würden meine Hände wieder selbständig handeln."
"Wenn meine Position es mir erlauben würde, würde ich sie wahrscheinlich selbst ganz ausziehen."


"Ich will noch anmerken, dass Emi anfängt rot zu werden, aber wir nähern uns beide sehr schnell dem Punkt, von dem es kein Zurück mehr gibt. Worte versiegen, und ich fühle meine Arme erschlaffen."


play music music_one fadein 0.5

"Aber keiner von uns ist auf dieses plötzliche, neue Gefühl vorbereitet."


show evh emi_grinding_off_closearoused onlayer master
with charachange

"Eine unbeschreibliche Hitze durchfährt mich, die anscheinend sowohl von mir als auch von Emi stammt."


"Eine Hand auf meiner Brust, um ihr Gleichgewicht zu halten, und die andere Hand, um sicherzustellen, dass ich nicht entkommen kann, sieht sie sehr zufrieden mit sich aus."


show evh emi_grinding_off_aroused onlayer master
with charachange

"Und dann, nach einem Moment des Zögerns, bewegt sie sich."


"Und bewegt sich noch einmal."


"Und noch einmal."


"Emi atmet stoßweise, und auch meine Atmung wird immer schneller."


"Ihr Körper zittert, während er gegen meinen reibt, und ich fühle, wie sie die Balance verliert. Es muss ihr schwerer fallen stabil zu bleiben, weil ihr die Beine zum Abstützen fehlen."


show evh emi_grinding_off_closesurprise onlayer master
with charachange

"Ich gebe ihr so gut es geht Halt, indem ich mit meinen Händen ihr Hinterteil festhalte. Es ist stramm und kräftig."


"Logisch, so viel wie sie rennt. Ich spüre das kraftvolle Spiel ihrer Muskeln unter meiner Hand."


"Was ich nicht bedacht habe, ist, dass mein Versuch, sie zu stabilisieren, dazu führt, dass sie etwas nach vorn rutscht, und, na ja… Es fühlt sich unglaublich an."


show evh emi_grinding_off_arousedclosed onlayer master
with charachange

"Ihr Höschen reibt gegen meine Hose, und es dauert nicht lange, bis wir einen Rhythmus gefunden haben."


"Aber Emi weigert sich, ihn einzuhalten. Mal wird sie schneller, mal langsamer, mal hört sie für eine gefühlte Ewigkeit ganz auf."
"Ich weiß nicht, ob sie das macht, um mit mir zu spielen, oder ob es sich für sie besser anfühlt, aber inzwischen ist mir das egal."


"Die Hitze zwischen uns wird immer intensiver, und ich kann ein Keuchen nicht zurückhalten. Das scheint Emi nur weiter anzuspornen."


"Ich fange an, ihre Bewegungen mit meinen eigenen zu unterstützen, was dazu führt, dass ihre bescheidenen Brüste zu meinen Bewegungen auf und ab hüpfen. Ihr Atem wird schneller, und meiner beschleunigt sich ebenfalls immer weiter."


"Mit geschlossenen Augen öffnet sie ihre Lippen erwartungsvoll. Ich schaffe es eben so, mich für einen Moment aufzurichten. Unsere Lippen suchen einander; ihre Brust an meine gepresst, als unser Schweiß sich vermischt."


"Als ich mich wieder fallen lasse, sind meine Hosen mit Schweiß durchtränkt. Ich würde sie ausziehen, wenn wir dafür nicht mit dem, was wir tun, aufhören müssten."


"Und ich will nicht damit aufhören, diesen wachsenden Druck, dieses Tingeln in meinem Hinterkopf."


"Emi bewegt sich schneller und schneller. Sie atmet schwer, ihre Stimme anscheinend unfähig, ihre Gefühle auszudrücken. Ihr Körper hingegen schafft das problemlos."


show evh emi_grinding_off_come onlayer master
with charachange

"Plötzlich bäumt sie sich auf, während mir selbst der Atem wegbleibt, und schiebt sich ein letztes Mal kraftvoll gegen mich. In mir wallt ein Gefühl auf, von dem ich nicht wusste, dass es existiert."


scene white onlayer master
with Dissolve(3.0)

"Meine Wahrnehmung verschwimmt, und ich gebe mich diesem Höhepunkt der Gefühle hin. Einige Sekunden lang, besteht die Welt aus nichts anderem als diesem großartigen Gefühl von Emi und mir – zusammen."


show evh emi_grinding_off_end onlayer master
with Dissolve(1.0)

"Und dann… ist es vorbei. Die Welt ist wieder im Fokus, und ich schaue in die Augen des Mädchens über mir."


"Einige Minuten lang spricht keiner von uns. Das Geräusch unseres Atems füllt den Raum, erschöpft von dieser Erfahrung."


"Schließlich bewegt sie sich widerwillig von mir herunter und lehnt sich gegen die Wand. Ich setze mich neben sie."


label de_E20x:

scene bg school_dormemi onlayer master at right
with locationchange

show eminude smile_close onlayer master
with charachange

emi "Nun… Bin ich rot geworden?"


hi "Hab ich nicht drauf geachtet."


hi "Und ich?"


show eminude neutral_close onlayer master
with charachange

"Emi zuckt mit den Schultern, immer noch ein wenig schwer atmend."


show eminude weaksmile_close onlayer master
with charachange

emi "Hab auch nicht drauf geachtet."


hi "Nun, vielleicht sollten wir-"


play sound sfx_dooropen

stop music fadeout 0.3

show rin basic_deadpan behind eminude onlayer master:
    center
    xpos 1.0 xanchor 0.0 alpha 0.0 subpixel True
    easein 0.5 right alpha 1.0
show eminude blush_close onlayer master
with vpunch

rin "Ich muss dein Fenster benutzen."


"Mein erster Instinkt ist, mich zu verstecken, aber dann merke ich, dass ich immer noch total erschöpft bin und dass Emi oben ohne neben mir sitzt. Weglaufen ist sinnlos."


show rin basic_awayabsent onlayer master:
    right alpha 1.0
with charachange

show rin basic_absent onlayer master
with charachange

show rin basic_awayabsent onlayer master
with charachange

"Rins Blick wandert über Emi und mich hinweg und fixiert sich auf das Fenster."


show rin basic_deadpannormal onlayer master
with charachange

rin "Da war eine Wolke."


play music music_comedy fadein 0.5

show eminude neutral_close onlayer master
with charachange

emi "Eine Wolke?"


show rin basic_lucid onlayer master
with charachange

"Rin nickt."


show rin relaxed_nonchalant onlayer master
with charachange

rin "Ich habe sie von meinem Fenster aus beobachtet, aber sie ist nicht in meinem Fenster geblieben."


show rin negative_spaciness onlayer master
with charachange

rin "Also muss ich dein Fenster benutzen."


show eminude closedsmile_close onlayer master
with charachange

"Emi rutscht ein wenig nach hinten. Ich muss husten, um mein Kichern zu verbergen."


emi "Wie lange musst du mein Fenster benutzen?"


emi "Wir sind… äh…"


show eminude wink_close onlayer master
with charachange

emi "Beschäftigt."


"Dieses Mal kann ich mein Lachen nicht unterdrücken."


show rin negative_annoyed onlayer master
with dissolvecharamove

"Rin ignoriert Emi und mich und starrt aus dem Fenster."


show rin basic_deadpanupset onlayer master
with charachange

"Ihre Schultern senken sich, und sie sieht enttäuscht aus."


rin "Hmm."


rin "Sie hat sich in etwas anderes verwandelt."


rin "Schade."


show eminude grin_close onlayer master
with charachange

"Emi hat Mühe, ernst zu bleiben."


emi "Das tut mir leid, Rin."


show eminude pout_close onlayer master
with charachange

emi "Könnten wir nun bitte ein wenig Privatsphäre haben?"


show rin relaxed_nonchalant onlayer master
with charachange

with Pause(0.2)

show rin relaxed_nonchalant onlayer master:
    easeout 1.0 xpos 1.0 alpha 0.0 xanchor 0.0 subpixel True 
with Pause(1.0)

play sound sfx_doorclose

hide rin onlayer master
with None

"Rin zuckt mit den Schultern, also ob sie sagen wollte „Könnt ihr das?” Dann zieht sie mit ihrem Fuß die Tür hinter sich ins Schloss."


show eminude happy_close onlayer master
with charachange

"Wir brechen beide in schallendes Gelächter aus. Es ist unmöglich, anders auf Rins bizarres Timing zu reagieren."


"Nachdem unser Gelächter verklungen ist, schaue ich Emi an. Wir sehen beide schrecklich aus."


stop music fadeout 5.0

hi "Nun."


show eminude neutral_close onlayer master
with charachange

"Emi hebt eine Augenbraue."


emi "Nun?"


hi "Nochmal?"


show eminude wink_close onlayer master
with charachange

"Emi grinst und lacht; dann nickt sie."


show eminude grin_close onlayer master
with charachange

emi "Wir sollten aber dieses Mal besser vorher die Klamotten loswerden."


$ suppress_window_after_timeskip = True

scene black onlayer master
with dissolve


label de_E21:

window hide None

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao onlayer master
with openeye

window show

"Das Sonnenlicht scheint durch mein Fenster, kurz bevor mein Wecker die morgendliche Stille zerstört."


play music music_dreamy fadein 6.0

"Ich bin wie erschlagen."


"Ich erinnere mich daran, was gestern Abend geschehen ist, und spüre, wie mir das Blut ins Gesicht schießt."


"Das war ein ereignisreicher Abend – und es erklärt auch, warum ich so erschöpft bin."


"Auf dem Weg zurück war ich ziemlich… angespannt, wenn ich mich recht erinnere."


"Weil meine Hose… schmutzig war, hatte ich sie im Bad abgewaschen, bevor ich zurück zu meinem Zimmer gegangen bin."


"Aber da war immer noch ein ziemlich offensichtlicher Fleck auf der Vorderseite."


"Zum Glück bin ich auf dem Rückweg außer Kenji niemandem begegnet."


"Und er hat nichts bemerkt."


"Na ja, abgesehen davon, dass ich irgendwo in seiner Nähe war."


"Natürlich hat er mich gefragt, wie mein Abend gelaufen ist, und ob ich irgendetwas Wichtiges in Erfahrung gebracht hätte."


"Ich weiß gar nicht mehr, ob ich ihm eine Antwort gegeben habe; ich war zu müde, um mich darum zu kümmern."


"Und ich gebe zu, dass ich mich heute Morgen ziemlich ausgelaugt fühle."


"Trotzdem – Emi hat mir versprochen, mich auf dem Sportfeld zu treffen, und ich will sie nicht enttäuschen."


scene bg school_track onlayer master
show emiwheel weaksmile onlayer master at center
with locationskip

"Als ich dort ankomme, wartet sie wirklich auf mich."


"Sie tut ihr Bestes, um fröhlich auszusehen, obwohl sie im Rollstuhl sitzt."


"Ich winke ihr zu und beginne mit dem Aufwärmen."


hi "Du bist früh dran."


show emiwheel frown onlayer master
with charachange

"Emi runzelt die Stirn und schüttelt den Kopf."


show emiwheel angry onlayer master
with charachange

emi "Lächerlich."


emi "{b}Du{/b} bist zu spät."


show emiwheel grin onlayer master
with charachange

emi "Verschlafen, Hisao?"


show emiwheel wink onlayer master
with charachange

emi "So kaputt?"


"Na, zumindest scheint sie wieder mehr sie selbst zu sein."


"Und wie erwartet schreckt sie nicht davor zurück, unsere… Aktivitäten von gestern zu erwähnen."


hi "Hey, du hast Glück, dass ich es überhaupt hierher geschafft habe."


hi "Diese ganze kardiovaskuläre Aktivität gestern Abend… Ich war kurz davor, hinterher Doc einen Besuch abzustatten."


show emiwheel wink onlayer master
with charachange

"Emi lacht laut auf, dann macht sich plötzlich ein besorgter Ausdruck auf ihrem Gesicht breit."


show emiwheel blush onlayer master
with charachange

stop music fadeout 8.0

emi "Hey, das ist nicht, äh…"


emi "Ich meine, du bist nicht…"


hi "Komm, spuck's aus."


show emiwheel awayfrown onlayer master
with charachange

emi "Es ist nur, dass es ziemlich schwer zu erklären wäre, wenn du einen Anfall hättest, während wir…"


hi "Oh."


hi "{b}Oh.{/b}"


"Jetzt wo sie es erwähnt – das ist eine berechtigte Sorge."


"Gestern Abend hatte ich gar nicht daran gedacht. Natürlich nicht – andere Dinge waren mir in dem Moment wichtiger."


hi "Na ja, ich glaube nicht, dass irgendwas, was wir… äh… {b}machen{/b}, anstrengender ist, als das Laufen Morgens, und das überstehe ich auch, also…"


show emiwheel frown onlayer master
with charachange

"Emi überlegt."


show emiwheel evil onlayer master
with charachange

"In ihren Augen leuchtet ein verschlagenes Glitzern auf."


play music music_emi fadein 2.0

emi "Sag mal…"


hi "Hmm?"


show emiwheel grin onlayer master
with charachange

"Das Leuchten verschwindet und sie grinst mich reumütig an."


"Ich kann mir nicht helfen, aber ich werde irgendwie misstrauisch."


show emiwheel happy onlayer master
with charachange

emi "Ich glaube, ich habe ein Paar Handschuhe vergessen."


hi "Wozu brauchst du Handschuhe?"


show emiwheel smile onlayer master
with charachange

"Emi deutet auf den Rollstuhl, in dem sie sitzt."


emi "Dafür natürlich!"


show emiwheel wink onlayer master
with charachange

emi "Klar, normal rumfahren kann ich auch ohne, aber ich will schließlich auch trainieren."


show emiwheel grin onlayer master
with charachange

emi "Und wenn man so schnell fahren will, braucht man Handschuhe, wenn man keine Blasen kriegen will."


hi "Und jetzt? Machst du einen Rückzieher? Muss ich allein laufen?"


show emiwheel awayfrown onlayer master
with charachange

"Emi überlegt eine Minute – zumindest tut sie so."


show emiwheel closedsmile onlayer master
with charachange

emi "Hmm… Wenn ich mich recht erinnere, liegen ein paar Handschuhe in dem Materialschuppen."


"Also will sie es ernsthaft versuchen."


"Aber in ihrer normalen Schuluniform? Ich hätte erwartet, dass sie für so was ihre Sportklamotten anzieht."


hi "Warte mal, wie kommen die dahin?"


show emiwheel frown onlayer master
with charachange

"Emi schaut mich fragend an."


emi "Im Ernst? Du hast keine Ahnung, warum in dem Materialschuppen an einer Schule für Behinderte Rennhandschuhe sind?"


"Nun, wenn sie es so sagt, ergibt es natürlich Sinn."


hi "Hey, ich bin immer noch neu hier. Ich muss mich noch eingewöhnen."


show emiwheel grin onlayer master
with charachange

emi "Ich denke, ich kann es dir dieses Mal noch durchgehen lassen."


show emiwheel wink onlayer master
with charachange

emi "Und jetzt komm, ich brauche deine Hilfe."


"Ich kann mir zwar nicht vorstellen wozu, aber ich hatte schließlich auch keine Ahnung, warum Rennhandschuhe in dem Schuppen sein sollten, also gehe ich nicht weiter darauf ein."


scene bg school_sportsstoreext onlayer master
with locationchange

"Emi schafft es mit Leichtigkeit, zu dem Schuppen zu kommen, auch wenn sie leise grummelt."


"Es ist irgendwie süß."


"Ich beeile mich ein wenig, um die Tür als Erster zu erreichen. Sie zu öffnen ist für mich leichter als für sie."


play sound sfx_door_creak

show emiwheel neutral onlayer master:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter

"Ich öffne die Tür, und Emi will hineinfahren, nur um an der Türschwelle abrupt anzuhalten."


"Es scheint, als wäre die Schwelle zu hoch, als dass sie allein darüber fahren könnte."


show emiwheel awayfrown onlayer master:
with charachange

show emiwheel awayfrown onlayer master:
    center
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    ease 0.2 xpos 0.5
with Pause(1.0)

"Sie versucht es ein paar Mal ohne Erfolg; dann hält sie inne und starrt die Schwelle entnervt an."


show emiwheel angry onlayer master at center
with charaenter

emi "Blöder Rollstuhl."


show emiwheel frown onlayer master
with charachange

emi "Hisao, kannst du mir bitte helfen?"


hi "Klar, kein Problem."


scene bg school_sportsstoreroom onlayer master
with locationchange

"Für mich ist es einfach, Emi über die Schwelle zu schieben, auch wenn sie dabei leicht durchgeschüttelt wird."


show emiwheel blush_close_ni onlayer master at center
with charaenter

emi "Hey, vorsichtig!"


hi "Ups! 'Tschuldigung."


"Ich passe einen Moment lang nicht auf, wohin ich laufe, und ramme Emis Rollstuhl gegen eine Matte."


play sound sfx_impact

show expression im.Composite((425,1200), (0,0), night("sprites/emiwheel/close/emiwheel_blush_close.png")) as emiwheel onlayer master:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.5 ypos 1.4 rotate 70

with vpunch

hide emiwheel onlayer master
with None

"Sie schreit überrascht auf und stürzt vorwärts aus ihrem Stuhl."


"Einen Moment lang herrscht Stille, während ich entsetzt schaue, was ich angerichtet habe, und Emi mich anstarrt."


emi "Hisao…"


hi "Ja?"


emi "Versprich mir, dass du niemals in einem Krankenhaus arbeiten wirst."


hi "Entschuldige! Das war keine Absicht!"


"Emi kichert und streckt mir eine Hand entgegen."


emi "Würdest du mir bitte zurück in den Rollstuhl helfen, Hisao?"


show emi basic_closedgrin_close_ni onlayer master:
    center
    ypos 1.2
    easein 0.5 ypos 1.0
with charaenter

"Als ich mich vorbeuge, um Emi aufzuhelfen, grinst sie triumphierend, zieht mich zu sich herab und gibt mir einen Kuss, der uns beide den Rollstuhl ganz schnell vergessen lässt."


play sound sfx_door_creak

"Als ich versuche, mich etwas bequemer hinzulegen, stoße ich gegen den Rollstuhl, der daraufhin nach draußen rollt, während die Tür hinter ihm zuschwingt."


play sound sfx_rustling

hide emi onlayer master
show eminude smile_close_ni onlayer master at center
with charachange

"Na ja, jedenfalls kann jetzt keiner mehr hereinschauen – was gut ist, weil meine Hände gerade dabei sind, Emis Bluse und Rock auszuziehen."


"Ich bin überrascht, als ich bemerke, dass sie vergessen hat, einen BH anzuziehen. Hat sie das geplant?"


show eminude blush_close_ni onlayer master
with charachange

"Ihre Arme schlingen sich unter meinen Achseln hindurch und ruhen dann auf meinen Schultern, während ich ihren Hals küsse – besonders einen Punkt wo Hals und Schulter zusammenkommen, den ich gestern Abend gefunden habe."


emi "D-Du bist richtig gut gew-hee!"


hi "Ich geb mir Mühe."


show eminude frown_close_ni onlayer master
with charachange

"Emi legt ihre Hand auf meine Brust und schiebt mich mit Bestimmtheit zurück. Ich schaue sie verwirrt an."


emi "Ich muss dir ein Geständnis machen, Hisao."


hi "Ja?"


"Jetzt, wo ich etwas Abstand habe, beschließe ich, meine Aufmerksamkeit ihren Brüsten zuzuwenden."


show eminude blush_close_ni onlayer master
with vpunch

"Als sie versucht zu sprechen, werden ihre Worte immer wieder von Kichern unterbrochen. Ich finde das unglaublich süß."


show eminude wink_close_ni onlayer master
with charachange

emi "Ich be-he he benutze gar keine a-ah! Handschuhe."


"Meine gemurmelte Antwort ist mehr an ihre Brust gerichtet als an ihr Gesicht."


hi "Hätte ich mir denken können…"


"Worte werden schnell unnötig."


show eminude closedsmile_close_ni onlayer master
with vpunch

"Emis Bewegungen sind wie wild, als ob sie seit heute Morgen etwas zurückhalten musste und nun ein Ventil gefunden hat."


"Ihre Aggressivität überrascht mich. Sie reißt mir beinahe mein Hemd vom Leib, während sie versucht, die dominierende Position zu erlangen."


"Ich für meinen Teil muss zugeben, dass ihr Verhalten mich ansteckt. Ich wehre mich, und wir rollen und ringen, während ich ihre Brüste liebkose und sogar während ihre Finger sich in meine Schultern krallen und ich vergesse, wo wir sind."


show eminude blush_ni onlayer master
with vpunch

"So sehr, dass ich direkt von der Matte herunterrolle und auf etwas lande, das klein und ziemlich hart ist."


hi "Autsch!"


show eminude weaksmile_ni onlayer master
with charachange

"Emi – mit rotem Gesicht und etwas schwer atmend – schaut mich an und lacht laut auf."


emi "Tut mir leid, entschuldige. Alles in Ordnung?"


hi "Ja, ich glaube schon. Ich weiß aber nicht, worauf ich gelandet bin…"


"Ich greife unter meinen Rücken, bringe das schmerzhafte Objekt hervor und inspiziere es genauer."


stop music fadeout 0.2

"„Gleitgel. Limonengeschmack.”"


"Moment, was?"


play music music_running

show eminude happy_ni onlayer master
with charachange

"Emi schaut zu mir auf und fängt an – falls das möglich ist – noch lauter zu lachen."


hi "Irgendwie glaube ich nicht, dass… dass das irgendwas mit Leichtathletik zu tun hat."


show eminude closedsmile_ni onlayer master
with charachange

emi "Oh Mann, ich weiß, wem das gehört!"


hi "Was?"


show eminude wink_ni onlayer master
with charachange

emi "Das gehört dem Teamkapitän!"


"Ah, mein alter Erzfeind. Zumindest so etwas ähnliches."


hi "Woher weißt du, dass das ihm gehört?"


show eminude awayfrown_ni onlayer master
with charachange

"Es scheint, als hätte ich eine dumme Frage gestellt, oder zumindest denkt Emi das."


show eminude frown_ni onlayer master
with charachange

emi "Weil er derjenige ist, der mir gesagt hat, dass dieser Schuppen ein guter Ort ist für… Wie nannte er es?"


show eminude pout_ni onlayer master
with charachange

emi "„Heimliche Zusammenkünfte.”"


hi "Oh? Hat er dich zu einer eingeladen oder was?"


show eminude happy_ni onlayer master
with charachange

"Emi lacht immer noch."


"Ich gebe zu, dass der Anblick einer nackten, lachenden Emi wunderschön ist."


"Trotz meiner gezielten Fragen, will ich das Thema eigentlich so schnell wie möglich beenden und da weitermachen, wo wir aufgehört haben."


show eminude closedsmile_ni onlayer master
with charachange

emi "Hisao, der Teamkapitän ist schwul."


"Hä?"


hi "Wirklich? Und ich habe am Anfang gedacht, ihr Zwei wärt ein Paar."


show eminude awayfrown_ni onlayer master
with charachange

emi "Na ja… Ich war ein wenig verknallt in ihn, als ich dem Team beigetreten bin, aber er war nicht interessiert."


show eminude frown_ni onlayer master
with charachange

emi "Offensichtlich."


show eminude neutral_ni onlayer master
with charachange

emi "Aber wir sind gute Freunde, denke ich."


show eminude grin_ni onlayer master
with charachange

emi "Ich meine, er hat mir immerhin von all dem erzählt."


hi "Ich traue mich kaum zu fragen…"


"Es fällt mir wirklich schwer, aber ich tue es trotzdem."


hi "… aber wozu braucht er das, äh… Gleitgel?"


hi "Ich meine, er macht doch nicht… äh…"


"Wie zur Hölle schafft Emi es, nicht rot zu werden?"


show eminude wink_ni onlayer master
with charachange

emi "Offensichtlich benutzt er es für, du weißt schon."


show eminude evil_ni onlayer master
with charachange

emi "Anal."


"Ich versuche, ein Kichern zu unterdrücken."


"Es gelingt mir nicht."


show eminude happy_ni onlayer master
with charachange

"Emi kichert ebenfalls."


hi "Und er {b}erzählt{/b} dir von all dem?"


show eminude awayfrown_ni onlayer master
with charachange

"Emi zuckt mit den Schultern."


show eminude neutral_ni onlayer master
with charachange

emi "Ja, klar."


stop music fadeout 10.0

show eminude closedsmile_ni onlayer master
with charachange

emi "Er ist ziemlich begeistert von der ganzen Sache."


emi "Sagt, es sei ein unvergleichliches Gefühl."


hi "A… ha."


"Die Luft in dem Schuppen scheint mit einer fürchterlichen Art von Neugier aufgeladen zu sein."


hi "Das ist ja interessant."


hi "Ich nehme an, ich muss ihm das wohl einfach glauben."


show eminude neutral_ni onlayer master
with charachange

emi "Na ja…"


"Draußen hören die Vögel auf zu zwitschern."


"Der Wind legt sich."


"Irgendwo trinkt ein Mann eine Tasse Kaffee. Er erstarrt mit der Tasse an den Lippen."


show eminude neutral_ni onlayer master
with charachange

emi "Wir könnten…"


extend " es vielleicht…"


show eminude blush_ni onlayer master
with charachange

emi "versuchen."


play music music_one fadein 5.0

"Mein Unterkiefer löst sich plötzlich spontan und fällt zu Boden."


hi "W-Was?"


"Endlich errötet auch Emi und reibt sich verlegen den Hinterkopf."


show eminude pout_ni onlayer master
with charachange

emi "Na ja, es ist nur, dass wir wirklich nicht… Wir können nicht das machen, was wir gestern gemacht haben, weißt du?"


emi "Es wäre ein wenig… Es wäre nicht sicher, weißt du?"


show eminude weaksmile_ni onlayer master
with charachange

emi "Ich meine, es war schon gestern nicht gerade eine tolle Idee."


show eminude closedsmile_ni onlayer master
with charachange

emi "Also dachte ich, wir könnten das probieren, um zu sehen, ob es, äh…"


hi "Ob es genauso gut ist?"


show eminude weaksmile_ni onlayer master
with charachange

emi "Na ja, äh, ja. So in etwa."


hi "Hm."


label de_E21h:

scene evh emi_shed_base1 onlayer master
show emi emi_shed_grin onlayer master
show hisao emi_shed_neutral onlayer master
show evh_l emi_shed_up onlayer master
show evh_r emi_shed_down onlayer master
with shorttimeskip

emi "Vorsichtig!"


hi "Bist du dir wirklich sicher?"


"Ich knie hinter Emi, die über ihre Schulter zu mir schaut und etwas rot aussieht."


"Na ja, nachdem wir beschlossen hatten, es durchzuziehen, mussten wir wieder in Stimmung kommen."


"Dann haben wir die Flasche Gleitgel leer gemacht, und…"


"Nun sind wir hier."


show emi emi_shed_hesitant onlayer master
with charachange

emi "Ja, ich bin sicher! Komm schon, bevor ich genug Zeit habe, mehr darüber nachzudenken."


"Emi atmet noch immer etwas schwer, und ihre Antwort ist fast schon ungeduldig."


"Ich denke, das ist normal. Wir sind beide ganz nah dran, und dieses Gerede zögert es nur hinaus."


"Ich glaube, wir beide sind gerade vorübergehend nicht ganz zurechnungsfähig."


"Zumindest wird das meine Verteidigung sein."


"Ich versuche nicht zu sehr über die Einzelheiten dessen nachzudenken, worauf ich mich da einlassen werde."


"Das wird sicher nicht sehr sauber sein."


show evh emi_shed_base2 onlayer master
show hisao emi_shed_closed onlayer master
with charachange

"Ich atme tief ein – mehr zu meiner Beruhigung als zu ihrer – und dringe langsam ein."


"Da ist eine Menge Widerstand; es ist, als ob unsere Körper es nicht wirklich durchziehen wollten."


show emi emi_shed_shock onlayer master
with hpunch

"Emis ganzer Körper verkrampft sich, und da ich zu dem Zeitpunkt erst teilweise drin bin, fühlt es sich überraschend gut an, wenn auch etwas seltsam."


"Andererseits sieht Emi aus, als wäre ihr das unangenehm."


"Ihr Ausdruck ist fast schon komisch."


show hisao emi_shed_neutral onlayer master
with charachange

hi "Soll ich aufhören?"


"Emis Atem stockt, und sie braucht ein paar Sekunden länger als sonst, um zu antworten."


show emi emi_shed_closed onlayer master
with charachange

emi "N-Nein, mach weiter. Es fühlt sich nur komisch an."


"Sie kichert."


"Ich kann es ihr nicht verübeln. Ich bin überrascht, dass ich überhaupt einen Satz herausbekommen habe."


show hisao emi_shed_closed onlayer master
with charachange

"Es ist… heiß."


"Fühlt sich extrem seltsam an."


"Das Gel glitzert unnatürlich."


"Das ist unangenehm."


"Ich dringe langsam weiter in sie ein und achte dabei aufmerksam auf Emis Atmung."


show evh emi_shed_base3 onlayer master
show emi emi_shed_hesitant onlayer master
with charachange

"Ich bin nun ganz drin und zögere. Emi schaut wieder zu mir zurück, und beißt sich auf die Unterlippe."


emi "Versuchst du nun, dich zu bewegen, oder hocken wir weiter rum und fühlen uns dämlich?"


show hisao emi_shed_neutral onlayer master
with charachange

hi "Nein, ich wollte dir nur eine Chance geben, dich daran zu gewöhnen."


"Das ergibt keinen Sinn."


"Wie sind wir überhaupt auf diese Idee gekommen?"


show emi emi_shed_grin onlayer master
with charachange

emi "Ich glaube, daran kann man sich nicht einfach gewöhnen, Hisao."


show emi emi_shed_hesitant onlayer master
with charachange

emi "Versuch dich zu bewegen. Vielleicht wird es besser?"


"Sie scheint zu zweifeln, aber mit Sicherheit will sie nicht aufgeben, nachdem wir schon so weit gekommen sind."


show emi emi_shed_closed onlayer master
with charachange

"Ich beginne mit einer langsamen Bewegung, die anscheinend sowohl für mich als auch für Emi in Ordnung ist, da sie ihre Augen schließt, um sich auf dieses neue Gefühl zu konzentrieren."


"Während ich meinen Rhythmus finde, kommt dieses Gefühl der Schwerelosigkeit von gestern zurück."


show hisao emi_shed_closed onlayer master
with charachange

"Ich schließe meine Augen und versuche mich in diesem Gefühl zu verlieren, nur…"


"Irgendetwas stimmt nicht."


"Emi gibt kein Geräusch von sich."


"Ich habe sehr schnell gelernt, dass Emi nicht gerade leise ist, wenn sie sich wohlfühlt."


show hisao emi_shed_neutral onlayer master
with charachange

"Ich öffne die Augen und sehe, dass Emi versucht, in Stimmung zu kommen, aber für sie scheint es einfach nicht zu funktionieren."


"Ihre Augen sind geschlossen, und sie beißt sich auf die Lippe, aber es sieht mehr so aus, als würde sie es ertragen anstatt es zu genießen."


"Ein Gesichtsausdruck, der sagt: „Das war ein Reinfall, aber hoffentlich ist es bald vorbei.”"


"Das bringt mich ein wenig in die Bredouille."


"Ehrlich gesagt, will ich nicht aufhören."


"Aber gleichzeitig scheint es Emi nicht viel zu bringen – und wenn doch, kommt sie viel langsamer als ich."


"Ich fühle mich schlecht. Ich will, dass Emi das auch genießen kann."


show evh_r emi_shed_up onlayer master
show emi emi_shed_shock onlayer master
with charachange

"Ich strecke einen Arm nach vorne und spiele mit Emis Brust, was sie überrascht."


show hisao emi_shed_sweat onlayer master
with charachange

"Dadurch wird sie auf einmal um einiges enger, was bei mir wiederum eine Welle der Erregung auslöst."


show evh emi_shed_base4 onlayer master
show hisao emi_shed_neutral onlayer master
show emi emi_shed_closed onlayer master
show evh_l emi_shed_down onlayer master
with charachange

"Mein scharfes Einatmen scheint Emi zu amüsieren, aber kurz darauf stöhnt sie selbst auf, als ich meine andere Hand an ihrer Vorderseite nach unten bewege und sanft die weichen Haare zwischen ihren Beinen streichele."


"Die Bewegungen meiner Hüfte werden heftiger, während die Bemühungen meiner Hände an Emis Vorderseite die Geräusche hervorrufen, die ich gewohnt bin."


show hisao emi_shed_sweat onlayer master
with charachange

"Ich konzentriere mich einzig und allein auf das Gefühl meiner Hände."
"Eine davon ist nun feucht und glitschig, die andere gleitet über weicher Haut. Ich spüre Gänsehaut, ein Zittern, Schweiß… Als ihr eigener Höhepunkt näherkommt, wird sie enger, bis ich einfach nicht mehr-"


"Neinichkannwirklichnicht"


show hisao emi_shed_closed onlayer master
with charachange

"OhGottentschuldigeEmiichmuss"


"Ich stoße ein letztes Mal zu, meine Finger fest um Emis Nippel, und stoße zwischen ihre Beine."


window hide

play sound sfx_flash
with SilentWhiteout(0.1,0.0,0.1)
play sound sfx_flash
with SilentWhiteout(0.1,0.0,0.4)
with GenericWhiteout(0.5,1.0,4.0)

window show

"Emis Rücken krümmt sich und sie bäumt sich auf. Ein hoher, mädchenhafter Schrei, der von den Wänden widerhallt, und ich spüre, wie die Welle meines Höhepunktes alle anderen Gefühle in meinem Körper auslöscht."


show evh_l emi_shed_up onlayer master
show evh_r emi_shed_down onlayer master
with charachange

"Emis Arme geben nach und sie fällt nach vorne. Dabei werden wir relativ unsanft getrennt, und Schmerz schießt durch etwas, was mir sehr lieb ist."


label de_E21x:

play sound sfx_impact

scene bg school_sportsstoreroom onlayer master
with vpunch

"Durch den plötzlichen Übergang von Genuss zu Schmerz verliere ich meine Balance und falle nach vorn auf Emi."


stop music fadeout 2.0

emi "Au!"


hi "Au."


"Ich rolle schnell von Emi herunter und setze mich auf. Ich atme schwer und versuche, den Schmerz in meinen Weichteilen zu ignorieren."


"Emi schreit kurz auf, als sie zur Seite rollt. Sie schnappt sich ein paar Taschentücher, die wir vorher bereitgelegt hatten, und säubert sich, bevor sie ihr Höschen wieder anzieht und sich gegen eine Wand lehnt."


"Immer noch schwer atmend setze ich mich neben sie an die Wand. Das Gefühl des kalten Zements an meinem schwitzenden Rücken ist angenehm."


show eminude sad_close_ni onlayer master at center
with charaenter

emi "Das am Ende hat {b}wehgetan{/b}!"


hi "Ja, ich, äh…"


hi "Das war wohl keine so tolle Idee."


"Emi windet sich, um ohne allzu große Schmerzen neben mir sitzen zu können. So wie sie das Gesicht verzieht, klappt es nicht wirklich."


show eminude pout_close_ni onlayer master
with charachange

emi "Ja, ich werde dem Teamkapitän was erzählen."


show eminude angry_close_ni onlayer master
with charachange

emi "Er hat eindeutig gelogen."


play music music_ease

"Plötzlich wird mir die totale Lächerlichkeit der Situation bewusst, und ich fange an zu lachen."


show eminude happy_close_ni onlayer master
with charachange

"Emi schüttelt den Kopf und lacht mit mir."


show eminude grin_close_ni onlayer master
with charachange

emi "Hey, Hisao."


hi "Ja?"


show eminude pout_close_ni onlayer master
with charachange

emi "Wir machen das nie wieder, stimmt's?"


hi "Ja, ich glaube, meine Neugier, was das angeht, ist gestillt."


"Emi nickt zufrieden."


show eminude closedsmile_close_ni onlayer master
with charachange

emi "Gut."


show eminude smile_close_ni onlayer master
with charachange

emi "Ich glaube, wir sollten einfach bei den Grundlagen bleiben, du nicht auch?"


show eminude blush_close_ni onlayer master
with charachange

emi "Ich meine, das Meiste von all dem ist für mich sowieso neu."


hi "Was meinst du mit „das Meiste?”"


show eminude grin_close_ni onlayer master
with charachange

"Emi grinst schelmisch."


show eminude closedsmile_close_ni onlayer master
with charachange

emi "Das werde ich nie erzählen."


"Mir kommt ein unangenehmer Gedanke."


"Noch unangenehmer ist der Gedanke, Emi danach fragen zu müssen."


"Aber nach dem, was wir gerade getan haben, sollte es ein Kinderspiel sein."


hi "Hey, gibt es hier ein Waschbecken?"


hi "Ich würde mich gerne, äh…"


hi "Ein wenig waschen."


show eminude blush_close_ni onlayer master
with charachange

"Emi schaut mich mit offenem Mund an."


emi "Im {b}Waschbecken{/b}?"


hi "Na ja, eine andere Möglichkeit gibt es nicht, oder?"


hi "Und es, äh… Sonst könnte ein Geruch entstehen."


hi "Den Doc bemerken könnte."


"Das ist das unangenehmste Gespräch, das ich je hatte."


show eminude closedsmile_close_ni onlayer master
with charachange

emi "Du hast Recht."


show eminude grin_close_ni onlayer master
with charachange

emi "Ja, es gibt… Es ist an der hinteren Wand."


show eminude smile_close_ni onlayer master
with charachange

emi "Es ist sicher auch etwas Seife da."


hi "Danke."


hide eminude onlayer master
with charaexit

"Es gibt wirklich etwas Handseife – besser als nichts."


"Aber kein Handtuch. Sieht aus, als müsste mich von der Luft trocknen lassen."


show eminude grin_ni onlayer master at center
with charaenter

emi "Fertig?"


hi "Ja, das muss fürs erste reichen. Es ist ja nicht so, als würde ich nicht noch mal duschen, nachdem wir bei Doc waren."


show eminude weaksmile_ni onlayer master
with charachange

emi "Freut mich zu hören."


show eminude wink_ni onlayer master
with charachange

emi "Und jetzt hilf mir, meine Klamotten zu finden. Du hast sie irgendwohin geworfen."


hi "Hey, du warst auch nicht besser! Wie soll ich das Loch in meinem Hemd erklären, hm?"


show eminude closedsmile_ni onlayer master
with charachange

emi "Sorry, ich war wohl ein wenig aufgeregt vorhin."


scene bg school_sportsstoreroom onlayer master
with shorttimeskip

"Es dauert eine Weile, aber schließlich sind wir beide mehr oder weniger angezogen."


"Da ist ein hektischer Moment, in dem wir beide nicht wissen, wo Emis Rollstuhl ist, aber ich erinnere mich, dass er durch die Tür gerollt ist, und rette ihn."


show emiwheel neutral_close_ni onlayer master at center
with charaenter

emi "Und dieses Mal bitte ein wenig vorsichtiger, wenn wir durch die Tür gehen, ja?"


show emiwheel awayfrown_close_ni onlayer master
with charachange

emi "Momentan habe ich eine Abneigung gegen Bodenwellen."


hi "Ich wünschte, wir hätten das nie ausprobiert."


show emiwheel grin_close_ni onlayer master
with charachange

"Emi zuckt mit den Schultern und grinst."


show emiwheel wink_close_ni onlayer master
with charachange

emi "Na ja, einen Versuch war's wert, oder?"


show emiwheel closedsmile_close_ni onlayer master
with charachange

emi "Und außerdem war es ein gutes Training, oder?"


"Das kann ich nicht bestreiten."


scene bg school_nursehall onlayer master
with shorttimeskip

"Auf dem Weg zu Docs Büro bemerke ich, wie Emi immer wieder in ihrem Sitz hin und her rutscht."


show emiwheel awayfrown onlayer master
with charachange

emi "Gott, fühlt sich das komisch an."


show emiwheel neutral onlayer master
with charachange

emi "Nur gut, dass ich gerade im Rollstuhl sitze, Hisao."


hi "Warum das?"


show emiwheel weaksmile onlayer master
with charachange

emi "Weil ich so Doc nicht erklären muss, warum ich so komisch laufe."


hi "Oh."


hi "Wir machen das nie wieder."


scene bg school_nurseoffice onlayer master
show nurse fabulous onlayer master at center
with locationchange

"Doc ist zumindest so nett, die Abdrücke, die Emi auf meinen Schultern hinterlassen hat, nicht zu kommentieren."


"Es sagt auch nichts dazu, dass Emi andauernd in ihrem Rollstuhl hin und her rutscht."


"Entweder er hat es nicht bemerkt, oder er wollte es nicht bemerken."


"Auf jeden Fall werde ich eine Weile lang aufpassen müssen, dass er mir kein Zyanid in meine Medikamente mixt."


"Nur um sicherzugehen."


stop music fadeout 4.0
scene bg school_dormhisao onlayer master
with locationskip

"Ich dusche länger als üblich, nur um sicher zu sein, das die letzten Überreste unseres kleinen „Experiments” beseitigt sind. Dann falle ich auf mein Bett."


"Der Unterricht beginnt in zwanzig Minuten, also kann ich sicher noch ein kleines Schläfchen halten."


scene black onlayer master
with shuteye



label de_E22:

scene black onlayer master
with dissolve

with Pause(5.0)

play sound sfx_doorknock

"Klopf klopf."


"Wer ist da?"


play sound sfx_doorknock

"Klopf klopf."


"So geht der Witz aber nicht."


play sound sfx_doorknock

"Klopf klopf."


"Ich hab doch schon gefragt, wer da ist!"


"Viel wichtiger, wie spät ist es?"


"Und noch viel wichtiger, welcher Tag…?"


scene bg school_dormhisao onlayer master
with openeyefast

"Mit einem Schlag bin ich hellwach – zum einen, weil das Klopfen immer noch nicht aufgehört hat, zum anderen, weil es Mittag ist."


"An einem Schultag."


"Jetzt, wo ich komplett wach bin, weiß ich auch wieder, warum ich eingeschlafen bin."


"Diese Entschuldigung benutze ich lieber nicht bei Herrn Mutou."


"„Tut mir leid, dass ich nicht im Unterricht war. Ich habe sexuell mit meiner Freundin experimentiert, und das hat mich ausgelaugt.”"


"Ja, das kommt sicher gut an."


play sound sfx_doorknock

"Ich frage mich, wie lange dieses Klopfen noch weitergeht."


"Vielleicht sollte ich die Tür öffnen."


play sound sfx_dooropen

scene bg school_dormhallway onlayer master
show kenji tsun onlayer master at center
with locationchange

"Irgendwie bin ich nicht überrascht, Kenji vor der Tür zu sehen."


"Aber es sieht so aus, als wäre Kenji überrascht, mich zu sehen."


ke "Was zum Teufel tust du hier, Mann?"


play music music_kenji fadein 0.5

hi "Na ja, ich habe geschlafen."


show kenji neutral onlayer master
with charachange

"Kenji nickt verständnisvoll."


show kenji happy onlayer master
with charachange

ke "KO geschlagen. Ich verstehe."


show kenji tsun onlayer master
with charachange

ke "Ich hab dir ja gesagt, du sollst mit dieser Ibarazaki vorsichtig sein, Mann."


ke "So was passiert, wenn du nicht aufpasst."


"Er versucht einen Blick auf meinen Hinterkopf zu erhaschen."


show kenji neutral onlayer master
with charachange

ke "Hat sie dir etwas über den Schädel gezogen?"


ke "Oder war es ein Schlafmittel?"


hi "Hör auf mich anzufassen."


with flash

"Kenji holt eine Taschenlampe hervor und leuchtet mir in die Augen."


ke "Hast du eine Gehirnerschütterung?"


hi "Ich wurde nicht KO geschlagen."


show kenji happy onlayer master
with charachange

ke "Vielleicht erinnerst du dich einfach nicht."


"Dieses Gespräch ist einfach nur sinnlos."


hi "Nein, ich hatte nur einen anstrengenden Morgen und bin eingeschlafen."


show kenji tsun onlayer master
with charachange

ke "Was auch immer, Mann."


ke "Wenn du es dir nicht eingestehen willst, kann ich dich nicht zwingen."


ke "Aber du musst bei diesem Mädchen aufpassen. Sie ist gefährlich."


hi "Was?"


show kenji rage onlayer master
with charachange

ke "Es ist gefährlich, in ihrer Nähe zu sein; sie ist eine ihrer gefährlichsten Agentinnen!"


ke "Wenn du nicht vorsichtig bist, kann Gott weiß was passieren!"


ke "Sie hat schon stärkere Männer als dich zu Fall gebracht!"


hi "Wovon zum Teufel sprichst du?"


hi "Sie ist kein Agent von irgendwas, und sie hat mich auch nicht KO geschlagen, okay?"


hi "Und ich bezweifle sehr, dass sie irgendwen zu Fall gebracht hat."


show kenji tsun onlayer master
with charachange

"Kenji sieht fast beleidigt aus."


"Ich habe keine Ahnung warum."


ke "Du glaubst mir nicht?"


ke "Das ist hart, Mann. Echt hart."


ke "Ich versuche doch nur auf dich aufzupassen. Das machen Freunde doch, oder?"


"Wir sind Freunde? Ich hatte ja keine Ahnung."


"Allerdings frage ich mich, ob Kenji weiß, was Freundschaft überhaupt bedeutet."


"So wie er da vor mir steht, tut er mir irgendwie leid."


"Vielleicht glaubt er ja wirklich, er würde auf mich aufpassen."


hi "Ich weiß, ich weiß."


hi "Tut mir leid. Danke für die Warnung."


"Als Zeichen der Versöhnung strecke ich ihm meine Hand entgegen."


show kenji neutral_close onlayer master
with characlose

"Kenji schüttelt sie vorsichtig, so als könne sie eventuell in Flammen stehen."


"Ein paar Sekunden herrscht eine unbehagliche Stille, bis Kenji bemerkt, dass er immer noch meine Hand schüttelt."


show kenji happy_close onlayer master
with charachange

ke "Wie auch immer, du musst mir einen Gefallen tun."


hi "Was für einen Gefallen? Ich habe kein Geld…"


ke "Doch hast du. Du hast Geld in deiner Schreibtischschublade unter dem schwarzen Notizblock. Für Notfälle."


hi "Hast du mein Zimmer durchsucht?"


show kenji neutral_close onlayer master
with charachange

ke "Das ist nicht wichtig."


ke "Ich brauche sowieso kein Geld."


"Er wird plötzlich sehr ernst."


show kenji tsun_close onlayer master
with charachange

ke "Ich werde bald eine größere Operation starten."


ke "Wenn ich Erfolg habe, wird die ganze Verschwörung aufgedeckt."


ke "Aber es ist gefährlich, also musst du etwas für mich tun, falls ich nicht zurück komme."


hi "Äh, klar, Mann. Alles was du willst."


"Was zum Teufel hat er vor?"


"Sollte ich jemanden warnen?"


show kenji neutral_close onlayer master
with charachange

ke "Wenn ich verschwinde, warte drei Tage und schicke dann mein Tagebuch an die Zeitungen."


ke "Es ist unter einem falschen Boden in einer meiner Schreibtischschubladen versteckt."


hi "Wie komme ich in dein Zimmer? Ich habe keinen Schlüssel."


show kenji tsun_close onlayer master
with charachange

"Kenji schaut mich an, als wäre ich verrückt."


ke "Dann knack das Schloss. Du weißt doch, wie man das macht, oder?"


ke "Es ist sehr wichtig, so etwas schon möglichst früh zu lernen!"


hi "Äh, ja, natürlich weiß ich, wie das geht."


hi "Klar werde ich das für dich tun. Wenn du verschwindest."


"Ich glaube nicht, dass ich Kenjis Tagebuch lesen will."


"Jedenfalls scheint Kenji froh zu sein, dass ich zugestimmt habe."


show kenji happy_close onlayer master
with charachange

ke "Klasse, Mann. Großartig."


ke "Man sieht sich. Ich hab noch Sachen zu erledigen."


stop music fadeout 5.0

show kenji happy_close onlayer master:
    easeout 0.5 xpos 0.7 alpha 0.0
with Pause(0.5)

hide kenji onlayer master
with None

"Und dann rennt er den Gang entlang und ist verschwunden."


"Das hörte sich so endgültig an."


"Ich hoffe, ich muss nicht seine letzten Wünsche erfüllen."


scene bg school_dormhisao onlayer master
with locationchange

play sound sfx_doorclose

"Ich schüttele meinen Kopf, schließe die Tür und gehe zurück zu meinem Bett."


"Ich sollte wahrscheinlich zum Unterricht gehen, auch wenn ich nur noch den halben Tag mitkriege."


"Aber ich bin schon den ganzen Vormittag nicht im Unterricht gewesen…"


"Und wollte noch mehr von diesem Hawking-Buch lesen, das Herr Mutou mir geliehen hat…"


"Ich bin sicher, er wird das verstehen."


with shorttimeskip

play sound sfx_hammer

"Klopf klopf."


"Dieses Mal reißt mich das Geräusch aus meinem Buch."


"Das Gefühl ist so ähnlich wie aufgeweckt zu werden."


hi "Wer ist da?"


emi "Ich! Freust du dich nicht?"


play music music_emi fadein 4.0

"Die Stimme kommt nur gedämpft durch die Tür, aber es ist eindeutig Emi."


play sound sfx_dooropen

scene bg school_dormhallway onlayer master
show emiwheel smile onlayer master at center
with locationchange

"Ich springe auf und öffne grinsend die Tür."


hi "Hey! Schön, dich wiederzusehen!"


show emiwheel grin onlayer master
with charachange

"Emi grinst zurück und starrt mich von ihrem Rollstuhl aus an."


show emiwheel closedsmile onlayer master
with charachange

emi "Ja, du hättest mich früher gesehen, aber der verdammte Aufzug war kaputt."


show emiwheel pout onlayer master
with charachange

emi "Ich musste warten, bis sie ihn repariert hatten."


show emiwheel awayfrown onlayer master
with charachange

emi "Man sollte meinen, sie würden so was besser in Stand halten, aber neiiin…"


"Ich kichere leise über ihren irritierten Gesichtsausdruck und bitte sie herein."


scene bg school_dormhisao onlayer master
with locationchange

"Sie rollt ohne Probleme herein, und mit meiner Hilfe hüpft sie auf das Bett."


show emi basic_closedgrin onlayer master:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter

emi "Na also. Viel gemütlicher als dieser dumme Rollstuhl."


show emi basic_grin onlayer master:
    ypos 1.1
with charachange

"Ein zufriedenes Seufzen hängt in der Luft, und eine Minute lang starren wir uns nur gegenseitig an."


"In diesem Moment bemerke ich die Ringe um Emis Augen."


"Sie sind nicht sehr dunkel, aber sie waren mit Sicherheit vorher nicht da."


"Bevor ich danach fragen kann, fixiert mich Emi mit einem schelmischen Blick."


show emi excited_happy onlayer master
with charachange

emi "So, ich habe bemerkt, dass du heute nicht beim Mittagessen warst."


emi "Um genau zu sein, habe ich dich überhaupt nicht gesehen."


show emi excited_proud onlayer master
with charachange

emi "Was ist passiert, hmm?"


hi "Eingeschlafen."


hi "Ich bin gar nicht vor Mittag aufgewacht, und das auch nur, weil Kenji mich geweckt hat."


show emi excited_amused onlayer master
with charachange

emi "Und warum warst du so müde?"


hi "Anstrengendes Training heute morgen. War auch etwas unangenehm."


show emi basic_closedhappy onlayer master
with charachange

"Emi hustet – ein halb lachendes, halb verlegenes Geräusch."


show emi basic_happy onlayer master
with charachange

emi "Erinner mich daran, dass wir das nicht noch einmal machen."


hi "Kein Problem. Um ehrlich zu sein, war es für mich auch nicht so toll."


hi "Wir lassen das einfach in Zukunft bleiben."


hi "Tut es… äh… Tut es noch weh?"


show emi basic_confused onlayer master
with charachange

"Emi starrt mich ungläubig an."


hi "Was? Das ist eine berechtigte Frage!"


show emi sad_grin onlayer master
with charachange

emi "Das ist eine der Fragen, von denen ich nie gedacht hätte, dass sie mir einmal jemand stellen wird."


hi "Na ja, ich hätte nie gedacht, dass ich sie einmal jemandem stellen würde, also sind wir quitt."


show emi basic_closedhappy onlayer master
with charachange

"Emi lacht."


emi "Sieht so aus, nicht wahr?"


stop music fadeout 5.0

show emi sad_shy onlayer master
with charachange

emi "Na ja, weil du gefragt hast: Ja, es tut noch ein wenig weh."


show emi sad_pout onlayer master
with charachange

emi "Wir werden das nie wieder tun."


hi "Kein Einspruch von mir."


"Sie gähnt, und ich schaue sie fragend an."


hi "Müde?"


show emi sad_grin onlayer master
with charachange

"Emi nickt schläfrig."


play music music_serene fadein 8.0

show emi sad_depressed onlayer master
with charachange

emi "Hab nicht gut geschlafen."


"Nicht gut geschlafen?"


"Ich merke, dass sie mir noch nicht einmal das erzählen wollte, denn sie erschrickt, als wäre sie beim Lügen ertappt worden und fügt hastig hinzu,"


show emi basic_closedgrin onlayer master
with charachange

emi "Es ist aber nicht so schlimm."


hi "Was ist los?"


show emi basic_grin onlayer master
with charachange

"Emi zuckt mit den Schultern und weigert sich, mehr zu sagen."


hi "Stress wegen der Prüfungen?"


"Ein weiteres Schulterzucken, aber nach einer Pause nickt Emi zögerlich."


show emi sad_shy onlayer master
with charachange

emi "Äh, ja, wahrscheinlich."


emi "Um ehrlich zu sein, bin ich deswegen hier."


"Sie sieht von Moment zu Moment unglücklicher aus."


"Natürlich nicht so offensichtlich, aber ihr Blick ist gesenkt, sie windet sich, und ihre Stimme ist ganz leise."


show emi sad_pout onlayer master
with charachange

emi "Wir äh, wir können nicht mehr so viel zusammen rumhängen."


hi "Hä? Warum?"


"Emi holt tief Luft, als hätte sie das einstudiert."


show emi sad_shy onlayer master
with charachange

emi "Weil ich mit dir zusammen zu viel Spaß habe."


emi "Und ich kann mich nicht konzentrieren, wenn du in meiner Nähe bist."


emi "Wenn jetzt bald die Prüfungen sind, kann ich… kann ich mir diese Ablenkung nicht leisten."


show emi sad_depressed onlayer master
with charachange

emi "Ansonsten werden meine Noten ziemlich lausig sein, fürchte ich."


hi "Ich könnte dir beim Lernen helfen…"


show emi sad_grin onlayer master
with charachange

"Sie lächelt mich an. Es ist offensichtlich, dass ihr die Situation so wenig gefällt wie mir."


emi "Das wäre toll, aber wir würden nicht wirklich lernen, oder?"


show emi sad_shy onlayer master
with charachange

emi "Ich meine, sogar jetzt versuche ich, mit dir zu reden, aber im Grunde will ich einfach nur… äh…"


show emi sad_shyblush onlayer master
with charachange

emi "Nicht reden."


hi "Ah."


hi "Ich verstehe. Überwältigt von meiner wilden Männlichkeit."


show emi basic_grin onlayer master
with charachange

"Das entlockt ihr zumindest ein Grinsen."


"Emi schüttelt den Kopf."


show emi basic_closedgrin onlayer master
with charachange

emi "Idiot. Du bist so selbstverliebt."


hi "Na ja, ich bin schon ziemlich unwiderstehlich."


show emi sad_shyblush onlayer master
with charachange

emi "Äh, mehr oder weniger. Denke ich."


show emi sad_grin onlayer master
with charachange

emi "Also, so sieht's aus, Hisao."


emi "Mit dir habe ich zu viel Spaß, und wenn ich mich auf die Prüfungen vorbereiten will, muss ich allein sein."


hi "Hey, das ist schon okay."


"Das scheint ihr wirklich auf dem Herzen gelegen zu haben."


"Außerdem sind es ja nur ein paar Wochen. Und wir sehen uns immer noch morgens und beim Mittagessen."


hi "Wir können uns auch einfach in der Schule treffen, kein Problem."


hi "Und nach den Prüfungen gehen wir zusammen aus, um zu feiern, dass sie vorbei sind, okay?"


show emi basic_closedgrin onlayer master
with charachange

"Emi grinst; der Vorschlag scheint ihr zu gefallen."


show emi basic_happy onlayer master
with charachange

emi "Ja, klar! Das hört sich großartig an!"


show emi excited_amused_close onlayer master at center
with characlose

"Also ob sie das Ende dieses Gespräches signalisieren will, lehnt sie sich nach vorne und küsst mich."


"Den Rest der Nacht verschwenden wir keinen Gedanken mehr an die Prüfungen."


stop music fadeout 2.0

scene black onlayer master
with dissolve



label de_E23:

window hide None

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_night fadein 4.0

scene bg school_library_bw onlayer master
with locationchange

nvl clear
nvl show dissolve

n "\n\nEs ist schon seltsam, wie einfach es für Emi und mich ist, uns nach dem Unterricht nicht mehr zu treffen."


n "Ich würde sogar sagen, dass es mir ein wenig Angst macht."


n "Genauso natürlich wie wir zusammen gekommen sind, so problemlos verläuft auch unsere Trennung."


n "Na ja, das stimmt nicht so ganz."


n "Nach unserer letzten gemeinsamen Nacht waren wir beide ziemlich down."


n "Und wir sehen uns ja noch jeden Morgen zum Laufen – wirklich nur zum Laufen."


n "Und zum Mittagessen. Die Mittagspausen mit ihr genieße ich besonders."


n "Dann haben wir genug Zeit, um über alles mögliche zu reden, während unsere morgendlichen Treffen ziemlich mechanisch ablaufen."


n "Wahrscheinlich, weil Emi unsere Dummheiten in dem Lagerschuppen wiedergutmachen will."


n "Aber egal wie viel Blödsinn wir beim Mittagessen machen, bin ich doch trotzdem ein wenig besorgt um sie."


nvl clear

n "\n\nSie wirkt nun öfter abgelenkt, und mir ist mehr als einmal aufgefallen, dass sie ziemlich nervös ist."


n "Ich hätte nie gedacht, dass sie sich so viele Gedanken über die Prüfungen machen würde, aber die scheinen sie ganz schön mitzunehmen."


n "Obwohl sie noch gar nicht angefangen haben."


n "Das ist nur das Warmlaufen, das Atemholen vor dem Startschuss."


n "Morgen geht es erst richtig los."


n "Mit den Prüfungen, meine ich."


n "Ich selbst mache mir über die Prüfungen gar nicht so viele Sorgen."


n "Ich weiß nicht genau warum. Ich meine, sie sind schon ziemlich wichtig; meine Noten werden meine Chancen beeinflussen, auf eine gute Uni zu kommen."


n "Himmel, wenn ich sie zu sehr auf die leichte Schulter nehme, könnte das meine Karrierechancen ruinieren."


n "Aber so kurz davor bin ich einfach zuversichtlich, dass ich sie gut hinter mich bringen werde."


nvl clear

n "\n\n\n\n\n\nMutou denkt jedenfalls, dass die Naturwissenschaftsprüfung für mich kein Problem sein wird."


n "Oder wie er es ausdrückt: „Über meine Prüfung solltest du dir am wenigsten Sorgen machen, Hisao. Die ist für dich kein Problem.”"


n "Allerdings ist das Mutou, der mir das erzählt."


n "Sein Lob impliziert irgendwie, dass alles, was schlechter ist als ein perfektes Ergebnis, eine Enttäuschung für ihn wäre, und deshalb mache ich mir mehr Gedanken über diese Prüfung, als ich eigentlich sollte."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_library onlayer master
with locationchange

window show

"Aus diesem Grund bin ich auch nach Unterrichtsschluss noch in der Bibliothek und brüte über einem Schulbuch."


"Ziemlich einfache Dinge; ein paar Formeln zur Geschwindigkeit, etwas über Reibung…"


"Ein Kinderspiel verglichen mit der gefürchteten Englischprüfung. Ich war noch nie gut mit Fremdsprachen…"


"Während ich noch einmal durch meine Notizen blättere, beginnen meine Gedanken abzuschweifen."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\nWenn diese Prüfungen vorbei sind, sollte alles wieder leichter werden."


n "Bald machen wir unseren Abschluss."


n "Dann hoffentlich zur Uni."


n "Ich erinnere mich an meinen fehlgeschlagenen Versuch, herauszufinden, was Emi nach der Schule machen will."


n "Hmm, sie ist dem Thema ziemlich geschickt ausgewichen, wenn ich mich recht erinnere."


n "Verdammt, es scheint, als ob sie jedes Mal das Thema wechselt, wenn ich zu direkt frage."


n "Oder mich auf… andere Art ablenkt."


n "Wie vor ein paar Tagen in der Mittagspause, als Rin nicht da war…"


n "Heh."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide None
window show None

stop music fadeout 0.2

show yuuko happy_up onlayer master
with vpunch

yu "Ich hab's geschafft!"


"Yuukos triumphierender Schrei reißt mich aus meinen Gedanken."


hi "Gah!"


show yuuko panic_up onlayer master
with charachange

"Yuuko scheint ihr Gefühlsausbruch extrem unangenehm zu sein."


play music music_happiness fadein 2.0

yu "Oh Gott!"


show yuuko panic_down onlayer master
with charachange

yu "Es tut mir so leid! Ich habe nur gerade – und ich war wirklich nicht – es ist nur, dass-"


"Während sie noch nach Worten sucht, versuche ich, sie schnell zu beruhigen, bevor sie sich zu sehr aufregt."


hi "Hey, schon gut."


"Meine Worte scheinen keine Wirkung zu haben."


"Yuuko steigert sich immer mehr in etwas hinein."


show yuuko panic_up onlayer master
with charachange

yu "Und das ist eine Bibliothek, und ich sollte nicht-"


hi "Schon gut, beruhige dich einfach."


show yuuko cry_down onlayer master
with charachange

yu "Und ich bin ein ganz schlechtes Vorbild, und nun werden sie mich feuern, weil ich einfach nichts richtig machen kann-"


hi "YUUKO!" with vpunch


show yuuko worried_up onlayer master
with charachange

"Schreien scheint zu helfen, obwohl ich mir die Missbilligung von einigen anderen Schülern in der Bibliothek zuziehe."


"Yuuko versteift sich wie ein Soldat, der gerade einen Befehl von seinem kommandierenden Offizier erhalten hat."


show yuuko neurotic_up onlayer master
with charachange

yu "Tut mir leid! Tut mir leid!"


hi "Beruhige dich, ist schon okay."


hi "Du hast mich nur ein wenig erschrecke, und das auch nur, weil ich geträumt habe, anstatt zu lernen."


hi "Also hast du mir im Grunde geholfen, wieder zur Sache zu kommen."


"Das ist eine glatte Lüge, aber es scheint zu helfen."


show yuuko worried_down onlayer master
with charachange

"Yuuko atmet tief durch und scheint sich ein wenig zu beruhigen."


"Obwohl sie immer noch sehr nervös zu sein scheint. Wo habe ich das in letzter Zeit schon mal gesehen?"


hi "Also, warum warst du überhaupt so aufgeregt?"


show yuuko neutral_up_close onlayer master
with characlose

yu "Der Bücherdieb von Yamaku!"


"Erstaunlicherweise gelingt es Yuuko, ihre ganze Aufregung in einem Flüstern zum Ausdruck zu bringen."


show yuuko closedhappy_up_close onlayer master
with charachange

yu "Ich glaube, ich weiß, wer es ist!"


show yuuko happy_down_close onlayer master
with charachange

yu "Ich habe einen anonymen Hinweis zu seiner Identität erhalten!"


yu "Also habe ich ein wenig spioniert, und ich glaube, der Hinweisgeber hatte Recht!"


hi "Ach wirklich? Und wer war dieser, äh, Bücherdieb?"


show yuuko worried_down_close onlayer master
with charachange

"Yuuko schließt ihren Mund, und schüttelt entschieden den Kopf."


yu "Nein, das kann ich dir nicht sagen."


hi "Warum nicht?"


show yuuko worried_up_close onlayer master
with charachange

yu "Das ist eine Sache zwischen mir und dem Bücherdieb."


yu "Ich kann nicht riskieren, dass du ihn warnst, dass ich auf seiner Spur bin."


yu "Er könnte seine Karten zu früh aufdecken und die Fliege machen."


yu "Dann säße ich ganz tief in der Tinte."


"Wann hat Yuuko angefangen zu reden wie ein Detektiv in einem Film noir?"


hi "Ich würde ihn nicht warnen! Warum sollte ich das tun?"


show yuuko neutral_down onlayer master
with charadistant

yu "Wenn du das fragen musst, dann brauchst du es nicht zu wissen."


hi "Das ergibt keinen Sinn, aber gut."


hi "Ich denke, Glückwünsche sind angebracht?"


show yuuko closedhappy_down onlayer master
with charachange

yu "Danke!"


show yuuko worried_up onlayer master
with charachange

yu "Äh, wofür?"


hi "Äh, die Sache mit dem Bücherdieb?"


show yuuko smile_down onlayer master
with charachange

"Yuuko nickt und lächelt mich dankbar an."


yu "So! Du lernst also für die Prüfungen?"


hi "Na ja, das hatte ich jedenfalls vor. Es klappt aber nicht so richtig."


show yuuko worried_down onlayer master
with charachange

yu "Wirklich? Fehlt dir ein bestimmtes Buch?"


show yuuko panic_up onlayer master
with charachange

yu "Es tut mir wirklich leid!"


yu "Ich wollte schon seit Wochen die Regale aufräumen, aber immer kommt mir was dazwischen!"


yu "Es tut mir so leid!"


hi "Hey, warte!"


hi "Das ist es nicht. Ich habe mein Buch hier."


"Um das zu unterstreichen und Yuuko hoffentlich zu beruhigen, deute ich auf das Lehrbuch vor mir."


hi "Ich bin nur dauernd abgelenkt, das ist alles."


show yuuko worried_up onlayer master
with charachange

yu "Liegt es an dem Lärm hier drin?"


yu "Ich versuche ja strenger zu sein, was den Lärmpegel angeht, aber ich schaffe es einfach nicht, Leute anzuschreien…"


show yuuko worried_down onlayer master
with charachange

yu "Ich meine, haben sie es nicht schon schwer genug im Leben, ohne dass ich hier meine Autorität heraushängen lasse?"


hi "Nein, es liegt auch nicht am Lärm, versprochen."


hi "Ich mache mir nur…"


"Verdammt, ich weiß es nicht."


"Sorgen um Emi."


"Sorgen um uns."


"Sorgen darüber, was nach unserem Abschluss passieren wird."


hi "Emi ist in letzter Zeit etwas seltsam."


show yuuko worried_up onlayer master
with charachange

yu "Wie meinst du das?"


hi "Na ja, du weißt, dass wir zusammen sind?"


hi "Ich bin mir nur nicht sicher, ob wir auch wirklich, du weißt schon…"


hi "… ein Paar sind. Ich bin mir nicht sicher, ob wir mehr sind als Freunde."


"Obwohl Freunde normalerweise nicht das tun, was wir tun."


"Körperlich sind wir ein Paar."


"Zumindest paaren wir uns."


hi "Es ist, als ob sie jedes Mal, wenn ich mehr über ihr Leben oder ihre Pläne für die Zukunft herausfinden will, der Frage ausweicht."


hi "Zum Beispiel habe ich neulich beim Mittagessen mit ihr über ein paar Unis geredet, die ich mir angeschaut hatte."


hi "Und ich habe sie gefragt, „Hast du dir in letzter Zeit irgendwelche Unis angeschaut?”"


hi "Sie zuckt nur mit den Schultern, sagt nein, und wenn ich sie nach dem Warum frage, sagt sie, dass sie nicht so weit vorausplant."


hi "Ich frage sie, warum nicht, und sie…"


"Ich begreife plötzlich was ich gerade erzählen will und beschließe, besser den Mund zu halten."


show yuuko neutral_up onlayer master
with charachange

yu "Was hat sie gemacht?"


hi "Äh, sie hat das Thema gewechselt."


hi "Wollte nicht darüber reden."


show yuuko neutral_down onlayer master
with charachange

yu "Vielleicht ist es ein unangenehmes Thema für sie?"


yu "Oder sie denkt einfach, es erklärt sich von selbst."


hi "Ja, aber das ist nicht alles."


hi "Immer, wenn ich versuche herauszufinden, was sie bedrückt, wechselt sie auch das Thema."


hi "Es ist, als ob sie gern mit mir zusammen wäre, mich aber nicht an sich heranlassen wolle."


"Jetzt, wo ich es ausgesprochen habe, fühle ich mich noch schlimmer."


"Yuuko denkt über das nach, was ich gesagt habe."


show yuuko worried_down onlayer master
with charachange

yu "Weißt du, mir scheint es so, als wäre es dir mit der Beziehung weit ernster als ihr."


"Ich kann fast den Eisklumpen fühlen, der sich in meinem Magen bildet."


"Sie hat Recht."


"Genauso sieht es aus."


hi "Aber ist es wirklich so? Ich meine…"


show yuuko panic_up onlayer master
with charachange

yu "Tut mir leid! Ich rede nur Blödsinn!"


yu "Du solltest von mir keine Ratschläge annehmen; du kennst mich ja kaum!"


show yuuko cry_down onlayer master
with charachange

yu "Ich bin nur die Bibliothekarin, und ich bin Single, also kannst du dir ja denken, dass ich keine Ahnung habe, wovon ich rede!"


hi "Nein, ich denke…"


hi "Ich denke, du hast Recht."


"Auch wenn es weh tut, darüber nachzudenken."


"Yuuko scheint verzweifelt nach einer Möglichkeit zu suchen, mich zu trösten."


show yuuko neutral_down onlayer master
with charachange

yu "Äh, schau mal."


show yuuko smile_down onlayer master
with charachange

yu "Ich liege wahrscheinlich komplett falsch, aber wenn du ganz sicher gehen willst, wie total falsch ich liege, solltest du vielleicht einfach mit ihr reden?"


yu "Wenn ihr mal allein seid, sprich sie einfach darauf an."


show yuuko closedhappy_down onlayer master
with charachange

yu "Und lass sie nicht das Thema wechseln!"


hi "Ja, vielleicht sollte ich das tun."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nOder vielleicht sollte ich mich einfach mit dem zufrieden geben, was ich habe."


n "Immerhin haben wir doch Spaß, wenn wir zusammen sind, oder?"


n "Und das gemeinsame Laufen ist schön, und die anderen Aktivitäten sind schön, und mit ihr zu reden ist auch schön…"


n "Muss ich ihr wirklich näherkommen? Was ich habe, ist doch ziemlich gut."


n "Aber das ist dämlich."


n "Ich will ihr näherkommen."


n "Ich will ihr helfen können, was immer sie auch bedrückt."


n "Aber… Vielleicht sollte ich warten, bis die Prüfungen vorbei sind."


n "Vielleicht ist sie ja besser gelaunt, wenn der Stress vorüber ist."


n "Wenn das alles ist, dann brauche ich mir ja keine Sorgen mehr zu machen."


n "Aber wenn nicht, dann… Na ja…"


n "Darüber mache ich mir Gedanken, wenn es soweit ist."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear
window show

stop music fadeout 5.0

"Ich danke Yuuko für ihre Ratschläge und gehe zurück in mein Zimmer."


scene bg school_hallway2 onlayer master
with locationchange

"Vielleicht kann ich mich hier besser aufs Lernen konzentrieren."


scene black onlayer master
with dissolve



label de_E24:

scene bg school_hallway3 onlayer master
with locationskip
play music music_tranquil fadein 3.0

"Ich verlasse den Raum, nachdem ich meine letzte Prüfung abgegeben habe, und atme erleichtert auf."


"Wie ich gehofft hatte, waren die Prüfungen nicht so schlimm. Ich konnte alles problemlos hinter mich bringen – bis auf die Englischprüfung."


"Und sogar die ging einigermaßen."


"Ich frage mich, wie Emi abgeschnitten hat."


"Vor allem will ich wissen, wie es ihr geht; heute beim Mittagessen hat sie furchtbar ausgesehen."


"Ich meine, sie war schon froh, aus dem Rollstuhl 'raus zu sein, aber sie war so erschöpft."


"Irgendetwas belastet sie, und ich beginne daran zu zweifeln, dass es nur die Prüfungen waren."


"Aber sollte ich sie darauf ansprechen?"


"Jemand klopft mir auf die Schulter und unterbricht so meine Gedanken."


show muto smile onlayer master at center
with charaenter

mu "Hey, Hisao."


label de_choiceE24:
menu:
    with menueffect
    mu "Hast du einen Moment Zeit?"
    "Ich denke, ich kann ein paar Minuten abzweigen.":




        return m1
    "Nein, ich habe gerade andere Sorgen.":


        return m2

label de_E24a:




hi "Ja, ich habe Zeit. Ich habe nichts Wichtiges vor oder so."


show muto normal onlayer master
with charachange

"Mutou hebt eine Augenbraue, als ob er daran zweifeln würde, dann winkt er mich zurück in den Klassenraum."


hide muto onlayer master
with charaexit

scene bg school_scienceroom onlayer master
with locationchange

show muto normal onlayer master at center
with charaenter

mu "Ich wollte eine Rückmeldung von dir, wenn das möglich ist."


mu "Ich weiß, dass dieser Kurs nicht ganz deinem Niveau entsprach…"


hi "Machen Sie sich keine Sorgen. Dafür war der Naturwissenschaftsklub sehr anspruchsvoll."


show muto smile onlayer master
with charachange

mu "Hmm, war er das?"


show muto normal onlayer master
with charachange

mu "Nun, eigentlich ist es das, worüber ich mit dir reden wollte."


mu "Denkst du, es hat dir etwas gebracht? Nur für mich zur Orientierung."


hi "Nun… Ja, es war eine tolle Möglichkeit, über den Unterrichtsstoff hinauszugehen. Es hat definitiv etwas gebracht."


show muto smile onlayer master
with charachange

"Mutou scheint sehr erfreut über meine Antwort zu sein."


mu "Großartig! Genau das hatte ich gehofft."


mu "Weißt du, Hisao, ich bin sehr froh, dass du hierher gekommen bist. Es ist immer gut, einen Schüler zu haben, der sich für das Fach interessiert, das man unterrichtet."


mu "Irgendwie ist es dann leichter, mit den anderen Schülern fertigzuwerden."


mu "Und du bist ein kluger Kopf. Bei Naturwissenschaften bist du so richtig in deinem Element – wie ein Fisch im Wasser oder eine ähnliche Metapher."


hi "Äh, danke."


hi "Sie waren eine große Hilfe. Besonders mit dem ganzen Uni-Zeug."


show muto normal onlayer master
with charachange

mu "Da ist noch etwas, Hisao."


mu "Ein kleiner Rat, von Wissenschaftler zu Wissenschaftler."


hi "Was für ein Rat?"


mu "Was tut ein Wissenschaftler?"


hi "Er beobachtet seine Umgebung."


show muto smile onlayer master
with charachange

mu "Genau. Sehr gut."


show muto normal onlayer master
with charachange

mu "Eine ganz einfache Frage, aber die meisten Leute können sie nicht beantworten. Das ist das Wesentliche an einem Wissenschaftler, Hisao."


mu "Wir beobachten, was ist, und versuchen, es zu erklären."


mu "Aber was ist, wenn du etwas nicht erklären kannst?"


mu "Was soll ein Wissenschaftler tun, wenn er etwas nicht beobachten kann?"


mu "Wie können wir zum Beispiel von Quarks wissen, wenn noch niemand wirklich eines gesehen hat? Oder von Schwarzen Löchern, bei denen es unmöglich ist, sie direkt zu beobachten?"


hi "Na ja, die Instrumente heutzutage sind ziemlich…"


show muto irritated onlayer master
with charachange

"Mutou winkt verärgert ab."


mu "Nein, das meinte ich nicht."


mu "Das sind Werkzeuge. Ich versuche dir, eine Philosophie zu vermitteln."


show muto normal onlayer master
with charachange

mu "Denk nach. Wenn du etwas nicht direkt beobachten kannst, wie kannst du es sonst beobachten?"


hi "Äh, raten?"


mu "Wie? Wie würdest du die Bewegung eines Quarks erraten? Worauf basierst du deine Vermutung?"


"Natürlich."


"Ich hätte schon früher darauf kommen sollen."


hi "Die Dinge, die es beeinflusst."


show muto smile onlayer master
with charachange

"Mutou klatscht aufgeregt in die Hände."


mu "Ja, genau. Gut."


mu "Merk dir das, Hisao."


show muto normal onlayer master
with charachange

mu "Wenn du etwas nicht direkt untersuchen kannst, liegt das daran, dass du falsch an die Sache herangehst."


mu "Du musst dir einen anderen Blickwinkel suchen, um die Wahrheit zu finden. Und wenn das nicht hilft, dann suche nach Auswirkungen."


mu "Das ist es, was es bedeutet, ein Wissenschaftler zu sein. Wir hören nie auf, nach Antworten zu suchen. Wir nehmen nie etwas als gegeben hin."


mu "Beobachten, Experimentieren und weiter Beobachten."


mu "Es gibt vieles da draußen, das keinen Sinn ergibt, Hisao. Deine Aufgabe ist es, diesen Sinn zu ergründen."


mu "Ich hoffe, dass du zumindest das von hier mitgenommen hast."


hi "Ich denke, das werde ich mir merken können."


show muto smile onlayer master
with charachange

"Mutou lächelt zufrieden."


mu "Gut. Und nun genieße deine Freizeit. Du hast sie dir verdient."


stop music fadeout 8.0

scene bg school_hallway3 onlayer master
with locationchange

"Ich verlasse den Raum leicht verwirrt."


"Wie ist er darauf gekommen?"


"Obwohl…"


"Gehe ich die Sache mit Emi vielleicht falsch an?"


"Wenn sie nicht mit mir reden will, gibt es vielleicht einen anderen Weg?"




label de_E24b:

hi "Um ehrlich zu sein, habe ich wirklich etwas zu tun…"


show muto normal onlayer master
with charachange

mu "Ja? Na ja."


mu "Ich wollte nur kurz deine Meinung zu unserem Naturwissenschaftsklub hören. Aber ich denke, das hat Zeit bis später."


mu "Genieß deine Pause, okay?"


hi "Danke, das werde ich."


"Ich würde wirklich gerne mit Mutou reden, aber ich habe gerade andere Dinge im Kopf."


"Emi, um genau zu sein. Was soll ich mit ihr machen?"


"Kann ich sie wirklich einfach so fragen?"




label de_E24c:

scene bg school_dormhisao onlayer master
with locationskip

"Die Frage schwirrt mir weiter im Kopf herum, auch nachdem ich wieder auf meinem Zimmer bin."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nWas, wenn sie wütend wird?"


n "Und was, wenn ich mir das alles nur eingebildet habe?"


n "Wenn ich zu ihr gehe und mich weigere zu gehen, bevor sie mir erzählt hat, was los ist, komme ich dann nicht als zu anhänglich herüber?"


n "Ich will wegen so was keinen Streit mit ihr anfangen."


n "Vielleicht sollte ich einfach erst mal nichts tun und schauen, wie es ihr morgen geht, bevor ich etwas unternehme."


n "Wäre es so schlimm, die Sache auf sich beruhen zu lassen?"


n "Es ist ja nicht so, als ob wir uns nicht gut verstehen würden."


n "Aber, so seltsam sich das auch anhören mag, ich will ihr wirklich… helfen."


n "Ich weiß nicht einmal, wobei oder ob sie überhaupt Hilfe braucht."


n "Aber ich will ihr helfen."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

play sound sfx_doorknock

stop music fadeout 2.0

nvl clear
nvl hide dissolve

window show

"Plötzlich schreckt mich ein Klopfen an meiner Tür auf."


play sound sfx_dooropen

scene bg school_dormhallway onlayer master
show kenji neutral onlayer master at center
with locationchange

"Ich öffne die Tür und sehe Kenji im Gang stehen."


hi "Oh, du bist es."


play music music_kenji

show kenji tsun onlayer master
with charachange

ke "„Du bist es?” Das ist alles?"


ke "Wenn du eine Ahnung hättest, was ich durchgemacht habe, dann würdest du dich mehr freuen, mich zu sehen, Kumpel."


ke "Ich meine, das war eine epische du-hättest-mich-nie-wieder-sehen-können Scheiße."


ke "Und du benimmst dich, als wäre ich gerade mal zum Laden gegangen, um Milch zu kaufen."


show kenji happy onlayer master
with charachange

ke "Du bist eiskalt, Hisao. Ich respektiere so was."


hi "Äh, danke?"


show kenji neutral onlayer master
with charachange

ke "Immer auf Nummer sicher gehen. Keine Emotionen zeigen."


ke "Lass niemanden in deine Karten schauen."


ke "Es sei denn, es ist Zeit, die Karten offen zu legen – oder du hast schlechte Karten."


ke "Dann solltest du aussteigen, oder deine Gewinne kassieren."


show kenji happy onlayer master
with charachange

ke "Verstehst du das?"


hi "Ja, das ergibt Sinn."


hi "Ich nehme an, deine, äh, Mission war erfolgreich?"


show kenji tsun onlayer master
with charachange

ke "Wow, du bist aber sehr neugierig."


ke "So was kannst du doch nicht einfach so aussprechen! Die Sache ist gerade in einer extrem schwierigen Phase!"


ke "Ein falscher Zug und BAM! Die Invasion gelingt!"


hi "Ich dachte, du wolltest die Verschwörung für alle offen legen?"


ke "Sie ist größer als ich dachte; ich muss meine Diagramme aktualisieren."


ke "Und wahrscheinlich auch einige meiner Puppen austauschen."


show kenji happy onlayer master
with charachange

ke "Willst du mir helfen? Ich habe noch Whiskey von… irgendwo."


ke "Du kannst mir erzählen, was du bei deiner Untersuchung herausgefunden hast."


hi "Äh, besser nicht. Ich… Äh, ich treffe sie nachher noch."


hi "Da muss ich hin. Ich darf keinen Verdacht erregen."


show kenji neutral onlayer master
with charachange

"Kenji nickt zustimmend."


ke "Immer noch ganz diskret, hm? Okay, Mann, ich respektiere das."


ke "Viel Glück."


hi "Äh, danke."


hide kenji onlayer master
with charaexit

stop music fadeout 4.0

"Für meine geistige Gesundheit gehe ich einfach mal davon aus, dass er mir Glück für mein Gespräch mit Emi wünscht."


"Und wenn ich etwas schiele, dann passt die ganze Kartenanalogie, von der er geredet hat, auch hier."


"Zeit, die Karten auf den Tisch zu legen."


"Oder besser: Schauen, ob ich Emi dazu bringen kann."


"Das Ziel nun vor Augen mache ich mich auf den Weg zu Emis Zimmer."


scene bg school_girlsdormhall onlayer master
with locationskip

play sound sfx_doorknock2

"Ich renne die Treppen zu ihrem Zimmer hoch und klopfe an ihre Tür."


emi "W-Wer ist da?"


play music music_drama fadein 8.0

"Hm? Das ist seltsam. Ihre Stimme hört sich so erstickt an."


hi "Hey, ich bin's. Ich dachte, ich schaue mal vorbei."


emi "Hisao?"


emi "Komm rein!"


"Ich drücke die Türklinke, nur um festzustellen, dass die Tür verschlossen ist."


"Das wird ja immer seltsamer."


hi "Äh, deine Tür ist abgeschlossen."


emi "Ach ja, tut mir leid. Gib mir 'ne Minute."


show emi basic_grin onlayer master:
    tworight
    xpos 0.8
    easein 0.5 tworight
with charaenter

"Einige Minuten später öffnet Emi grinsend die Tür."


emi "Tut mir leid, ich musste erst meine Beine anziehen. Ich habe geschlafen."


"Trotz ihres Grinsens ist irgendetwas nicht in Ordnung."


"Emis Augen sind leicht gerötet, und es sieht aus, als hätte sie geweint."


hi "Hey, kein Problem."


hi "Äh, geht es dir gut?"


show emi sad_shy onlayer master at tworight
with charachange

emi "Hm? Ja, mir geht's gut!"


hi "Es ist nur, dass du so aussiehst, als hättest du geweint…"


"Oh ja, Hisao. Das war eine tolle Einleitung."


show emi sad_grin onlayer master at tworight
with charachange

emi "Was? Nö, mir geht's gut. Ich freue mich nur, dich zu sehen."


scene ev emi_firstkiss onlayer master
with flash

"Sie unterstreicht das mit einem langen Kuss, während die Tür hinter uns ins Schloss fällt."


"Ich weiß, was sie jetzt tun will, und mir ist auch schmerzhaft bewusst, wie sehr ich es ebenfalls tun will, aber…"


scene bg school_dormemi onlayer master at left
show emi excited_amused_close onlayer master at center
with locationchange

"Ich beende den Kuss mit einem Akt eiserner Selbstkontrolle, der mich beinahe umbringt."


hi "Hey, warte."


show emi basic_confused_close onlayer master
with charachange

"Emi schaut mich verwirrt an."


emi "Hä? Auf was warten?"


hi "Wir müssen reden."


show emi sad_grin_close onlayer master
with charachange

emi "Sollte das nicht mein Spruch sein?"


show emi sad_shy_close onlayer master
with charachange

emi "Und ist das normalerweise nicht etwas Schlechtes?"


"Sie hat Recht."


"Normalerweise ist es die Einleitung für eine Trennung."


"Oder der Anfang eines Streits."


hi "Vielleicht kann es dieses Mal etwas Gutes sein."


hi "Äh, das hoffe ich zumindest."


show emi sad_shyblush_close onlayer master
with charachange

emi "A… ha."


show emi basic_grin_close onlayer master
with charachange

emi "Können wir wenigstens ins Bett gehen? Ich bin den ersten Tag wieder auf den Dingern und muss mich erst wieder daran gewöhnen."


show emi basic_closedgrin_close onlayer master
with charachange

emi "Außerdem hat Doc gesagt, ich soll sie nicht so häufig benutzen, weil das Laufen sie so stark belastet."


hi "Dann müssen wir wohl."


"Es ist eine Falle. Wir beide wissen es, aber es ist uns egal."


"Allerdings ist es sehr schwer, wütend zu werden, wenn man mit dem Objekt seiner Begierde im Bett liegt. Das könnte also auch ein Grund sein."


hide emi onlayer master
with charaexit

show bg school_dormemi onlayer master at right
with charamove

show emi basic_grin_close onlayer master:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter

"Ich lege Emis Beine neben das Bett, setze mich neben sie und lege einen Arm um ihre Schultern."


"Schweigend genießen wir beide es einfach ein paar Minuten lang, so zusammen sein zu können."


"Aber dann muss ich natürlich den Moment ruinieren, indem ich den Mund aufmache."


hi "Schau mal, ich weiß… dass du in letzter Zeit einiges durchgemacht hast."


hi "Und ich will dir helfen."


hi "Ich dachte, es wären nur die Prüfungen, die dir Sorgen gemacht haben, aber jetzt komme ich in dein Zimmer, und du hast geweint, und das bringt mich um."


hi "Aber ich kann nichts tun, wenn du nicht mit mir darüber redest."


show emi basic_closedgrin_close onlayer master:
    ypos 1.1
with charachange

emi "Ich habe dir doch gesagt, dass es mir gut geht."


hi "Nein, dir geht es nicht gut. Es ist offensichtlich, dass dich etwas bedrückt."


hi "Du weißt, dass du es mir sagen kannst."


"In Emis Stimme klingt ein klein wenig Spannung mit."


show emi sad_shy_close onlayer master
with charachange

emi "Warum reicht es dir nicht, wenn ich dir sage, dass es mir gut geht?"


show emi sad_annoyed_close onlayer master
with charachange

emi "Du machst dir Sorgen, ich habe verstanden. In Ordnung."


emi "Aber es geht mir gut, und es gibt nichts, worüber du dir Sorgen machen müsstest."


hi "Nicht schlafen und geistesabwesender sein als Rin… Das sieht mir nicht aus, als ginge es dir gut."


hi "Ich will… dir doch nur helfen."


emi "A-ha."


hi "Ja, ich mag es nicht, dich so zu sehen."


hi "Ich will, dass du glücklich bist, weißt du?"


show emi basic_annoyed_close onlayer master
with charachange

"Ich habe das Gefühl, das kam nicht so an wie geplant, denn Emi fixiert mich mit einem eisigen Blick."


emi "Du willst mich also reparieren, Hisao?"


"Sie wird nun definitiv wütend."


show emi sad_grit_close onlayer master
with charachange

emi "Kommst auf deinem weißen Ross angeritten und rettest die Prinzessin?"


emi "Beendest die Albträume und die Phantomschmerzen?"


show emi sad_angry_close onlayer master
with charachange

emi "Bringst das Verlorene zurück?"


show emi sad_depressed_close onlayer master
with charachange

"Ihr Stimme überschlägt sich, und Tränen strömen über ihre Wangen."


emi "Nun, das kannst du nicht."


show emi sad_pout_close onlayer master
with charachange

emi "{b}Niemand{/b} kann das."


emi "Niemand wird es je können."


"Ich bin so geschockt von ihrem verbalen Angriff, dass mir die Worte fehlen."


"Eine Zeit lang sagt keiner von uns etwas."


"Ich bin überrascht, dass Emi mich näher zu sich heranzieht, anstatt mich wegzustoßen."


"Sie holt tief Luft und fängt wieder an zu reden."


show emi sad_shy_close onlayer master
with charachange

emi "Es tut mir leid."


show emi sad_depressed_close onlayer master
with charachange

emi "Es ist nur… Da sind diese Albträume."


emi "Über den Unfall."


"Ah. Der Unfall. Ich hätte es mir denken können."


"Er hat sie immerhin ihre Beine gekostet, aber natürlich redet sie nie darüber."


show emi sad_pout_close onlayer master
with charachange

emi "Und normalerweise komme ich gut damit zurecht, weil ich laufen kann."


emi "Laufen hilft mir besser als alles andere, mich abzulenken."


emi "Ich muss an nichts anderes denken, während ich laufe."


emi "Ich konzentriere mich nur darauf zu atmen, auf meinen Rhythmus."


emi "Es macht es leichter. Das Leben ist leichter."


show emi sad_shy_close onlayer master
with charachange

emi "Immer nur vorwärts, weißt du? Nichts sonst ist wichtig, nur um die nächste Kurve zu kommen."


emi "Und dann ist es die nächste Kurve und die nächste und die nächste, bis ich nicht mehr weiterlaufen kann, nicht mehr denken kann, oder irgendwas tun kann, außer langsamer zu werden und zu gehen, bis ich wieder zu Atem komme."


emi "Und danach ist nichts anderes mehr wichtig."


show emi basic_annoyed_close onlayer master
with charachange

emi "Aber ich habe zu lange in diesem verdammten Rollstuhl festgesessen. Kein Ventil."


show emi sad_shy_close onlayer master
with charachange

emi "Heute ist es einfach ein wenig übergekocht."


hi "Du hättest mit mir darüber reden können, weißt du?"


hi "Du hättest es nicht allein durchstehen müssen."


show emi sad_grin_close onlayer master
with charachange

"Emi lächelt traurig, als ob sie versuchen würde, einem Kind zu erklären, dass man sich an Feuer verbrennen kann."


emi "Doch, das musste ich. Und ich muss es immer noch."


hi "Aber warum?"


hi "Warum musst du das allein durchstehen?"


hi "Warum vertraust du mir nicht genug, um mich dir helfen zu lassen?"


"Wieder dieses Lächeln."


show emi excited_amused_close onlayer master
with charachange

show emi sad_grin_close onlayer master
with charachange

"Emi lehnt sich zu mir und küsst mich auf die Wange – eine fast schon mütterliche Geste."


"Sie lässt ihren Mund nahe an meinem Ohr und vertraut mir etwas an."


show emi sad_shy_close onlayer master
with charachange

emi "Weil, Hisao."


emi "Weil ich schon einmal alles verloren habe, was mir wichtig war."


show emi sad_depressed_close onlayer master
with charachange

emi "Ich weiß nicht, was ich tun würde, wenn das noch einmal passieren würde."


"Sie zögert, als wäre sie sich unsicher, ob sie weiterreden soll oder nicht."


"Ich spüre, wie sich wieder der Eisblock in meinem Magen bildet."


"Sie fährt fort."


show emi sad_shy_close onlayer master
with charachange

emi "Deshalb kann ich mich nicht auf dich verlassen."


emi "Oder auf Doc."


emi "Oder auf irgendjemand anderen."


show emi sad_pout_close onlayer master
with charachange

emi "Nur auf mich."


emi "So muss es sein."


"Nach dieser kurzen Ansprache schaut sie zu Boden und hält ihren Handrücken vor ihren Mund."


"Dieses Gespräch ist offensichtlich vorüber. Ich suche nach Worten, aber mir fällt nichts ein."


hi "Ich…"


hi "Vielleicht sollte ich fürs erste gehen."


hi "Ich muss noch… Sachen… erledigen."


"Emi schaut nicht einmal zu mir auf."


"Sie hört sich müde an, oder erleichtert."


"Ich weiß nicht, welches von beiden."


emi "Okay, Hisao."


emi "Geh und erledige deine Sachen."


emi "Wir sehen uns morgen."


hide emi onlayer master
with charaexit

with Pause(0.2)

show bg school_dormemi onlayer master at left
with charamove

"Ich stehe auf und gehe zur Tür. An der Schwelle bleibe ich stehen."


hi "Hey, Emi…"


show emi sad_shy onlayer master at tworight
with charaenter

emi "Ja?"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\nTausend Dinge, die ich sagen will."


n "Ich bin zu verwirrt, um auch nur eines davon auszusprechen."


n "Nachdem sie zugegeben hat, dass sie mich niemals an sich heranlassen wird, fühle ich mich, als wäre {b}meine{/b} Welt gerade in Trümmer gefallen."


n "Was ist bei diesem Unfall passiert?"


n "Ich weiß, dass sie ihre Beine verloren hat, aber das scheint ihr nie etwas ausgemacht zu haben."


n "Was ist damals passiert?"


n "Was macht diesem Mädchen solche Angst, dass sie keine Hilfe annehmen will – nicht einmal von jemandem, den sie liebt?"


n "Ich weiß es nicht."


n "\nAber ich will es wissen."


n "Ich will es so sehr wissen, dass diese Verweigerung einer Antwort sich wie ein Messer in meinem Magen anfühlt."


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve
window show

emi "Hisao?"


emi "Was wolltest du sagen?"


"Ich stehe immer noch auf der Türschwelle."


hi "… Nichts."


hi "Schon gut."


scene bg school_girlsdormhall onlayer master
with locationchange

play sound sfx_doorclose
stop music fadeout 6.0

"Und ich schließe die Tür."


"Und gehe den Gang entlang."


"Die Treppen hinunter."


scene bg school_dormext_full_ni onlayer master
with locationskip

"Zur Tür hinaus."


"In die Dunkelheit."


scene bg school_dormhisao_ni onlayer master
with locationskip

play music music_night fadein 1.0

"Irgendwie finde ich wieder zurück in mein eigenes Zimmer. Meine Gedanken drehen sich im Kreis."


window hide
nvl clear
nvl show dissolve

n "\n\nIch weiß nicht, wie ich damit umgehen soll."


n "Ich dachte, dass vorwärts zu schauen etwas Gutes sei."


n "Die Vergangenheit, die man nicht ändern kann, hinter sich lassen. In der Gegenwart leben und in die Zukunft schauen."


n "\n\nNach dieser… Sache mit Emi bin ich mir nicht mehr so sicher."


n "Sie hat die Wahrheit gesagt. Es ist einfacher, zur nächsten Kurve zu schauen, den zurückgelegten Weg zu ignorieren."


n "Sich keine Sorgen über die Gegner machen, die man zurückgelassen hat. Keinen Gedanken an die Zuschauer auf der Tribüne verschwenden."


n "Und leider auch keine Zeit, sich um die langsameren Teamkameraden zu kümmern."


nvl clear
nvl hide dissolve
window show

"Ich lasse mich auf mein Bett fallen und starre in eine Ecke meiner Zimmerdecke, als stünden dort die Antworten geschrieben, die ich suche."


"Natürlich habe ich nicht dieses Glück."


window hide
nvl clear
nvl show dissolve

n "\n\n\n\n\nSie rennt im wahrsten Sinne des Wortes vor etwas davon – aber habe ich das nicht auch getan, als ich versucht habe, meinen Krankenhausaufenthalt zu verdrängen?"


n "Es geht mir besser, aber meine Gesundheit wird nicht auf magische Weise wieder zurückkommen."


n "\nBei Emi sind es anstelle eines Herzens zwei Beine, aber die werden auch nicht auf magische Weise wiederhergestellt werden."


n "\nVielleicht wird keiner von uns je mehr 'geheilt' sein als jetzt."


nvl clear
nvl hide dissolve
window show

"Das Zimmer wird immer dunkler, bis ich nicht mehr erkennen kann, ob ich wirklich in eine Ecke schaue."




label de_E25:

scene bg school_dormhisao onlayer master
with shorttimeskip

"Auf eine schlaflose Nacht folgt viel zu schnell der Morgen."


"Ist es das, was Emi nachts immer durchmacht?"


"Auf die Wand oder die Decke starren. Versuchen, nicht mehr daran zu denken – was auch immer es ist."


"In meinem Fall ist sie es."


"Der Eisblock in meinem Magen ist immer noch da."


window hide
nvl clear
nvl show dissolve

n "\n\n„Ich kann mich nicht auf dich verlassen.”"


n "\nWorte, so beiläufig ausgesprochen."


n "Fast als ob sie mich aufziehen wollte, als ob sie mich zurechtweisen wollte für die Behauptung, die Erde sei flach."


n "\n„So muss es sein.”"


n "\nDas ist einfach beschissen!"


n "Ich fühle mich so hundeelend, dass ich beinahe das Training ausfallen lasse."


n "Aber das wäre dumm von mir. Es ist nichts, was ich tun sollte, nur um sie zu sehen."


n "Klar, das war der ursprüngliche Grund, aber jetzt ist da noch mehr."


nvl clear

n "\n\n\n\nDas Laufen selbst hat angefangen, mir Spaß zu machen."


n "Es gibt schlimmere Arten, sein Blut in Bewegung zu bringen."


n "Nach der ersten Woche hätte ich nie gedacht, dass ich das einmal sagen würde, aber-"


n "\nIch fühle mich nach dem Laufen viel besser. Nach dem Motto „Was immer ich heute sonst noch tun werde, zumindest das habe ich schon getan.”"


n "Es hilft mir auch beim Wachwerden, und Emi hat selbst gesagt, dass ihr Laufen hilft, den Kopf frei zu bekommen. Vielleicht wird es auch mir helfen."


n "\n Das hoffe ich zumindest."


nvl clear
nvl hide dissolve

scene bg school_track onlayer master
with locationskip

window show

"Der Morgen ist kühl und klar, wenn auch etwas feucht. Sieht so aus, als würde sich der Sommer bemerkbar machen."


"Als ich ankomme, ist Emi bereits bei ihren Dehnübungen und begrüßt mich mit einem Lächeln und einem Winken."


show emi basic_closedgrin_gym onlayer master at center
with charaenter

emi "Hey, Hisao!"


"Sie so munter zu sehen, ist wie ein Tritt in die Eier."


"Wie kann sie nach gestern nur so fröhlich sein?"


show emi excited_amused_gym_close onlayer master
with characlose

"Ich winke halbherzig zurück und bin überrascht, mit einer Umarmung begrüßt zu werden."


show emi sad_shy_gym_close onlayer master
with charachange

emi "Hey, wegen gestern Abend."


"Jetzt kommt's."


stop music fadeout 1.0

show emi basic_grin_gym_close onlayer master
with charachange

emi "Ich wollte mich bei dir bedanken."


show emi excited_happy_gym_close onlayer master
with charachange

emi "Ich konnte zum ersten Mal seit Langem wieder richtig gut schlafen, und ich glaube, es ist wegen unserer Unterhaltung."


show emi basic_closedgrin_gym_close onlayer master
with charachange

emi "Also, danke."


play music music_rain fadein 4.0

"Wie kann sie nur besser schlafen nach unserem Gespräch?"


"Im Grunde hat sie mir gesagt, dass sie mich nicht näher an sich heranlassen wird."


"Und das hat ihr geholfen zu schlafen?"


"Entschuldigung, aber was zum Teufel soll {b}das{/b} denn?"


"Entweder bemerkt Emi meine Verblüffung nicht oder sie will sie nicht bemerken."


"Ich verstehe sie einfach nicht mehr."


hi "Oh, kein Problem. Schön, dass es geholfen hat."


"Ich schaffe es gerade noch, das Gift aus meiner Stimme herauszuhalten, aber ich glaube, ich sollte besser jetzt loslaufen, bevor ich etwas Dummes sage."


scene bg school_track_on onlayer master
with locationchange

"Emi scheint auch bereit zu sein, und nach wenigen Augenblicken laufen wir auch schon um das Sportfeld."


"Ich sehe, dass sie wirklich entspannter ist."


scene ev emi_run_face onlayer master:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 20.0 zoom 1.1
with flash

"Sie läuft wieder mit den geschmeidigeren Bewegungen, die ich noch aus der Zeit kenne, wo wir uns kennengelernt haben."


"Es ist ein Riesenunterschied zu der Verbissenheit, mit der sie sich die letzten Tage über die Laufbahn gequält hat."


"Unser Gespräch scheint ihr wirklich geholfen zu haben."


"Zu schade, dass es mir nicht geholfen hat."


"Ich komme langsam in meinen Laufrhythmus und muss an die Zeit denken, wo ich es mir nicht leisten konnte, an irgendetwas anderes zu denken, als daran, meinen Atem ruhig und meine Beine in Bewegung zu halten."


"Diese Tage gehören wohl der Vergangenheit an."


"Zumindest für die ersten paar Runden."


scene bg school_track_running onlayer master
with Dissolve(2.0)

"Verärgert über meinen ausbleibenden Erfolg erhöhe ich mein Tempo."


"Ah, da ist dieses brennende Gefühl in meinen Beinen."


"Der Atem, der keuchend aus meiner Brust kommt, das Klopfen meines Herzens. Auf das ich immer noch aufpassen muss."


"Aber es scheint stärker geworden zu sein; ich kann spüren, wie es Blut durch meine Adern pumpt."


"Es pocht in meinen Ohren, aber anstatt in Panik zu verfallen, wie an jenem Tag im Schnee, versetzt mich das in Hochstimmung."


"Ja, es funktioniert! Mein Herz, der tödliche Fehler, der mich hierher gebracht hat, hat sich gebessert."


"Ich kann nun vorwärts schauen, und vielleicht kann ich eines Tages aufhören, mir so viele Sorgen zu machen."


"In diesem Moment ist es egal, dass ich keine Ahnung habe, wie es mit Emi und mir weitergehen soll."


"Alles, was zählt, ist, dass sich meine Arme und Beine weiter im Rhythmus bewegen."


"Nichts anderes."


show bg school_track_on onlayer master
with locationchange

"Als ich auf die Zielgerade einbiege, erkenne ich, dass Laufen wirklich hilft – wenn auch nicht so viel wie ich gehofft hatte."


"Ich fühle mich besser, und während ich noch ein paar Runden zum Abkühlen gehe, kann ich den gestrigen Abend aus einer etwas weniger emotionalen Perspektive betrachten."


"Emi will also, dass ich Abstand von ihr halte."


"Das kann ich nicht."


"Es muss einen anderen Weg geben, irgendeinen Kompromiss, den wir aushandeln können."


"Ich bin mir aber nicht sicher, wie so ein Kompromiss aussehen könnte."


"Verdammt, und ich hatte mich schon fast optimistisch gefühlt."


show emi excited_joy_gym onlayer master at center
with charaenter

emi "Guter Lauf, Hisao! Du hast dich wirklich verbessert!"


"Guter Lauf. Das ist alles, was ich fürs Erste erwarten kann, oder?"


"Herzlichen Glückwunsch, Hisao. Du bist erbärmlich."


"Ich muss meine Einstellung ändern."


hi "Na ja, du weißt doch. Ich bin einfach toll."


"Und trotzdem sage ich immer wieder Dinge, die ich nicht meine."


"Sehr bald werde ich meine Probleme genauso gut verstecken können wie Emi."


show emi basic_closedgrin_gym onlayer master
with charachange

emi "Das denke ich auch."


"Warum tut sie mir das an? Warum sagt sie so etwas mit so viel echter Zuneigung in ihrer Stimme, dass mein Herz einen Sprung macht?"


"Sie meint es nicht ernst. Das kann nicht ihr Ernst sein."


"Ich bin wohl doch nicht so gut, wie ich dachte, denn Emi schaut mich prüfend an."


show emi basic_confused_gym onlayer master
with charachange

emi "Hey, alles in Ordnung?"


show emi basic_hes_gym onlayer master
with charachange

emi "Vielleicht sollten wir zu Doc gehen, hm?"


hi "Ja, ich will dir ja hier nicht zusammenbrechen."


"Emi sieht aus, als wäre sie ein wenig schockiert von meinem verbitterten Ton."


show emi basic_shock_gym onlayer master
with charachange

emi "Sag so was nicht!"


show emi sad_shy_gym onlayer master
with charachange

emi "Das ist dir schon einmal passiert, erinnerst du dich?"


"Warum tut sie so liebevoll?"


"Im Grunde ist es ihr egal, das hat sie doch gestern klargemacht."


"Aber trotzdem entschuldige ich mich, obwohl ich das eigentlich nicht müsste. Obwohl sie wahrscheinlich einfach nur schauspielert."


hi "Heh, tschuldigung."


hi "Komm, gehen wir zu Doc."


"Den ganzen Weg über kann ich mich nicht beruhigen."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\n\nJedes Mal, wenn ich denke, ich wäre über letzte Nacht hinweg, sagt oder tut Emi irgendetwas Nettes, und ich bin wieder ganz am Anfang."


n "Die Erinnerung daran, wie sie dieses Gespräch beendet hat, verfolgt mich."


n "Es war, als hätte sie das Messer in der Wunde noch ein letztes Mal umgedreht und mir die letzte Hoffnung genommen, aus uns könnte einmal mehr werden als jetzt."


n "Und was sind wir schon im Moment? Kaum mehr als Freunde, die zufällig auch ficken."


n "Und es ist ja auch nicht so, als würde ich die Zeit, die wir zusammen verbringen, nicht genießen. Habe ich gestern selbst gesagt."


n "Beinahe hätte ich das Thema gar nicht angeschnitten, wäre einfach zu ihr ins Bett gehüpft und hätte den Dingen ihren Lauf gelassen, oder nicht?"


stop music fadeout 2.0

nvl clear
nvl hide dissolve

scene bg school_nursehall onlayer master
with shorttimeskip

window show

"Mit diesen Gedanken immer noch in meinem Kopf stehe ich vor Docs Büro, während er Emi untersucht."


"Emi stürzt aus der Tür, gibt mir einen Kuss und rennt dann davon – wahrscheinlich zum Duschen."


"Währenddessen winkt Doc mich herein, um mit dem rituellen Check-up zu beginnen."


$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_nurse fadein 0.5

scene bg school_nurseoffice onlayer master
show nurse neutral onlayer master at center
with locationchange

nk "Irgendwelche Probleme heute?"


hi "Nö. Ich habe mich heute sogar etwas mehr angestrengt als sonst, und es scheint, als hätte ich es vertragen."


show nurse grin onlayer master
with charachange

nk "So viel Risikobereitschaft bin ich von dir gar nicht gewohnt, Hisao."


nk "Du hängst zu viel mit Emi herum. Sie färbt auf dich ab, und das ist nicht unbedingt etwas Gutes."


"Als er Emis Namen erwähnt, verfinstert sich meine Miene, obwohl ich mir Mühe gebe, mir nichts anmerken zu lassen."


show nurse fabulous onlayer master
with charachange

nk "Hmm. Das ist ja ganz was Neues, nicht wahr?"


show nurse neutral onlayer master
with charachange

nk "Sonst ist deine Reaktion auf Emis Namen immer ein Grinsen und keine gerunzelte Stirn."


show nurse concern onlayer master
with charachange

nk "Was genau ist zwischen euch vorgefallen? Emi scheint nichts davon zu wissen, was auch immer es sein mag."


show nurse neutral onlayer master
with charachange

nk "Sie sah entspannter aus, als ich sie seit Wochen gesehen habe, und das ist ungewöhnlich zu dieser Zeit des Jahres."


hi "Was meinen Sie damit?"


show nurse fabulous onlayer master
with charachange

nk "Womit?"


hi "Mit „zu dieser Zeit des Jahres.” Ich versuche herauszufinden, was sie bedrückt, aber sie verschließt sich, sobald ich das Thema anschneide."


hi "Dann, gestern Abend, hat sie gesagt-"


show nurse neutral onlayer master
with charachange

nk "Lass mich raten. Sie will es dir nicht sagen, weil sie sagt, dass sie dir nicht vertrauen kann?"


nk "Und nun bist du so fertig, weil du dachtest, ihr Zwei wäret viel mehr als sie zu denken scheint, richtig?"


hi "Äh, mehr oder weniger."


hi "Woher zum Teufel wissen Sie das?"


show nurse grin onlayer master
with charachange

nk "Hisao, ich bin Pfleger. Es ist mein Job, solche Dinge zu wissen."


show nurse neutral onlayer master
with charachange

nk "Außerdem kenne ich Emi nun lange genug, um zu wissen, dass sie so etwas tun würde; das ist typisch für sie."


"Er sagt das in diesem halb liebevollen, halb frustrierten Ton, der passender wäre, wenn ihm eine Zigarette aus dem Mundwinkel hängen würde."


"Wie die Dinge stehen, scheint er bereit zu sein, mit einem Kugelschreiber auszukommen."


show nurse fabulous onlayer master
with charachange

label de_choiceE25:
menu:
    with menueffect
    nk "Hisao, hättest du etwas dagegen, wenn ich dir einen Rat gebe?"
    "Klar, warum nicht?":




        return m1
    "Nein, das ist mein Problem.":


        return m2


label de_E25a:



"Was hat Mutou gestern gesagt?"


"„Wenn du etwas nicht direkt beobachten kannst, dann beobachte seine Umgebung?”"


"Einen Versuch ist es Wert."


"Ich wette, Doc kennt Emi besser als ich."


hi "Klar, ich bin ganz Ohr."


hi "Um ehrlich zu sein, weiß ich nicht mehr weiter."


hi "Ich habe keine Ahnung, wie ich damit umgehen soll."


show nurse grin onlayer master
with charachange

nk "Darauf wäre ich nie gekommen."


"Er grinst, während er das sagt. Ich glaube, er macht einen Scherz."


show nurse neutral onlayer master
with charachange

nk "Schau mal, es ist so: Emi ist… stur."


show nurse grin onlayer master
with charachange

nk "Das solltest du inzwischen wissen, und wenn nicht, dann bist du ziemlich unaufmerksam, aber das will ich dir nicht unterstellen."


hi "Dafür bin ich sehr dankbar."


show nurse neutral onlayer master
with charachange

nk "Jedenfalls, wenn sie entschieden hat, dass sie nicht darüber reden will, was passiert ist, dann wird sie nicht darüber reden, was passiert ist."


nk "Hat sie jemals irgendetwas darüber erzählt, was sie bedrückt? Vielleicht ein Hinweis?"


hi "Nun, sie hat gesagt, sie hätte Albträume über den Unfall…"


show nurse fabulous onlayer master
with charachange

nk "Wirklich? Du machst also Fortschritte. Das ist gut."


show nurse neutral onlayer master
with charachange

nk "Na ja, ich denke, so viel kann ich dir erzählen, ohne meine Nicht-Einmischungs-Regeln, was Emis dämliche Entscheidungen angeht, zu verletzen."


show nurse concern onlayer master
with charachange

nk "Bald ist der Jahrestag ihres Unfalls."


nk "Zu dieser Zeit ist sie immer depressiv, weil es ein sehr traumatisches Ereignis war, wenn man bedenkt, was sie verloren hat."


hi "Das ist die andere Sache. Sie tat so, als hätte sie mehr verloren als nur ihre Beine. Was ist passiert?"


show nurse fabulous onlayer master
with charachange

nk "Wow! Nein, da halte ich mich raus. Das wirst du jemand anderen fragen müssen, denn in dieses Hornissennest werde ich nicht stechen."


show nurse neutral onlayer master
with charachange

nk "Wenn Emi es dir erzählen will, dann wird sie das tun, wenn sie bereit ist."


nk "Du musst nur Geduld haben, das ist alles."


hi "Warum helfen Sie mir mit all dem?"


show nurse grin onlayer master
with charachange

nk "Weil du ihr gut tust. Sie vertraut dir, auch wenn sie das nicht wahrhaben will."


nk "Und von allen hier an der Schule hast du die besten Chancen, ihr durch diese schwere Zeit zu helfen."


show nurse neutral onlayer master
with charachange

nk "Von mir wird sie keine Hilfe annehmen, aber vielleicht von dir, wenn du es nicht vermasselst."


show nurse fabulous onlayer master
with charachange

nk "Also vermassle es nicht, verstanden?"



label de_E25b:


"Einen Rat? Wozu denn? Ich kann doch sowieso nichts daran ändern."


hi "Wissen Sie, ich glaube nicht, dass Sie irgendetwas sagen könnten, was helfen würde."


show nurse neutral onlayer master
with charachange

nk "Man kann nie wissen, Hisao."


hi "Nein, ich denke, ich habe eine recht gute Vorstellung davon, was los ist."


hi "Emi ist in einigen Belangen einfach nur stur, und das stört mich, aber ich werde darüber hinwegkommen."


hi "Machen Sie sich keine Sorgen um uns."


show nurse concern onlayer master
with charachange

"Doc scheint mir nicht zu glauben, aber er zuckt nur mit den Schultern."


nk "Wie du willst, Kleiner."




label de_E25c:

$ renpy.music.set_volume(0.3, 0.0, channel="sound")
play sound sfx_hammer

"Ich öffne meinen Mund, um zu antworten, aber ein Klopfen an der Tür unterbricht mich."


emi "Hey, seid ihr immer noch da drin?"


show nurse grin onlayer master
with charachange

nk "Nur einen Moment, Emi."


nk "Wir müssen nur schnell unsere Hosen wieder anziehen."


$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorslam

show emi invis onlayer master:
    tworight
    xpos 1.0
with None

show bg school_nurseoffice onlayer master at bgleft
show nurse grin onlayer master at twoleft
show emi basic_annoyed_gym onlayer master at tworight
with dissolvecharamove

"Die Tür fliegt auf, und Emi starrt Doc zornig an."


emi "Arschloch."


show nurse fabulous onlayer master
with charachange

nk "Ich wollte dir keine unbegründeten Hoffnungen machen."


hi "Hey, können wir… mich da aus dem Spiel lassen?"


hi "Was ist überhaupt los, Emi? Hast du was vergessen?"


"Ich versuche ihr gegenüber einen fröhlicheren Ton anzuschlagen."


"Kein Grund, sie zu verärgern. Das „Alles-ist-gut” Spiel kann ich auch spielen."


show emi sad_grin_gym onlayer master at tworight
with charachange

emi "Ehrlich gesagt, ja. Ich wollte dich noch was fragen."


hi "Ja? Was denn?"


show emi basic_happy_gym onlayer master
with charachange

emi "Willst du mich mal zu Hause besuchen?"


show emi basic_closedgrin_gym onlayer master
with charachange

emi "Meine Mutter kocht, und ich dachte, du würdest vielleicht gerne mitkommen."


show nurse grin onlayer master
with charachange

nk "Na klar, ich komme gern."


show emi basic_closedgrin_gym onlayer master:
    parallel:
        "emi excited_proud_gym" with Dissolve(0.2, alpha=True)
    parallel:
        ease 0.2 xpos 0.6
        ease 0.2 tworight
with Pause(0.5)

"Emi boxt Doc spielerisch gegen den Arm."


emi "Nicht du, du Idiot. Du warst letzte Woche erst da."


show emi sad_grin_gym onlayer master at tworight
with charachange

emi "Ich habe mit Hisao gesprochen."


show nurse neutral onlayer master
with charachange

nk "Oh? Interessant! Du wirst der Mutter vorgestellt!"


hi "Ich würde sehr gerne kommen, Emi. Danke."


show nurse fabulous onlayer master
with charachange

"Doc hebt eine Augenbraue, sagt aber nichts."


emi "Toll! Ich bin in meinem Zimmer. Komm vorbei, wenn du geduscht und dich umgezogen hast, und wir nehmen den Bus!"


hi "Hört sich gut an. Bis gleich!"


stop music fadeout 2.0

show emi excited_amused_gym_close onlayer master
with characlose

"Dieses Mal bin ich es, der sie schnell küsst, bevor ich aus dem Zimmer renne."


scene bg school_dormhisao onlayer master
with locationskip

"Was für eine interessante Entwicklung."


"Vielleicht kommen wir uns ja doch näher."


"Vielleicht ist Emi ja endlich bereit, sich ein wenig zu öffnen."


"Oder vielleicht ist sie einfach nur höflich und will sich mit der Einladung für gestern Abend entschuldigen."


"Toll. Nun weiß ich nicht, ob ich aufgeregt, nervös oder niedergeschlagen sein soll."


"Ich entscheide mich für eine Kombination aus allen dreien und springe unter die Dusche."


scene black onlayer master
with dissolve

$ suppress_window_after_timeskip = True



label de_E26:

window hide None
$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_businterior fadein 2.0

scene ev busride onlayer master
with locationchange

nvl clear
nvl show dissolve

n "\n\n\nIch glaube, ich fahre nicht gerne mit Bussen."


n "Im Grunde bin ich mir sogar ziemlich sicher."


n "Sie schwanken sehr viel, sie riechen komisch, und man spürt jedes Schlagloch in der Straße."


n "Darauf freue ich mich wirklich nicht."


n "\nAußerdem machen Emis Beine ein klackendes Geräusch, das die Aufmerksamkeit aller anderen im Bus auf uns lenkt."


n "Sie trägt wieder kurze Hosen, hat aber lange Socken über ihre Prothesen gezogen, damit sie nicht zu sehr auffallen."


n "Das ändert aber nichts an den seltsamen Blicken, wenn ihre Beine mit einem hörbaren Klonk aneinander stoßen."


nvl clear

n "\n\n\nIch rutsche nervös auf meinem Sitz hin und her, und Emi hebt fragend eine Augenbraue."


n "Die Blicke scheinen sie nicht zu stören – oder sie bemerkt gar nicht, dass die Leute sie anstarren."


n "Ich bin mir sicher, dass sie schon oft blöd angestarrt worden ist. Nach einer gewissen Zeit fällt einem das wohl nicht mehr auf."


n "\n\nNicht, dass sie mir das erzählen würde, wenn ich sie fragte."


n "Dazu kommt, dass mir nicht nur wegen des Busses unwohl ist."


n "Ich komme einfach nicht damit zurecht, dass Emi scheinbar versucht, mir näher zu kommen, während sie mich gleichzeitig auf Distanz hält."


nvl clear



label de_E26a:

n "\n\n\nDoc hat gesagt, sie vertraut mir, auch wenn es nicht so aussieht."


n "Aber ich bin mir nicht sicher, ob ich Doc vertrauen kann."


n "Er will Emi beschützen, genau wie ich sie beschützen will, und ich würde sicher eine Menge sagen, um sie gut aussehen zu lassen, wenn mich jemand nach ihr fragen würde."


n "\nAlso vielleicht tut er genau das."


n "Allerdings schien er wirklich ehrlich überrascht zu sein, dass Emi mich eingeladen hat…"


n "Vielleicht hat unsere Unterhaltung gestern Abend ja mehr geholfen, als ich dachte, aber ich mache mir immer noch Sorgen."


label de_E26b:

stop ambient fadeout 12.0

nvl clear

n "\n\n\nDie Eltern zu treffen ist ein großer Schritt, oder?"


n "Ich habe ihre Mutter zwar schon einmal getroffen, aber das war nur als Bekanntschaft."


n "Nun bin ich Emis Freund – mit allem, was dazugehört."


n "Ich fühle mein Herz in meiner Brust klopfen, ein Echo jenes verschneiten Nachmittags, der sich anfühlt, als hätte er in einem früheren Leben stattgefunden."


n "Nur, dass ich damals nicht wusste, was passiert; außerdem hatte ich keine Medikamente, die das Schlimmste verhindern konnten."


n "Was meinen Gesundheitszustand angeht habe ich seit damals große Fortschritte gemacht, und zum zweiten Mal heute habe ich das Gefühl, ich könnte vielleicht doch noch ein normales Leben führen – oder zumindest so normal wie eben möglich."


n "\nWenn ich nun noch meine Beziehung genauso in den Griff kriegen könnte wie mein Herz, ginge es mir großartig."


stop ambient fadeout 1.5
window hide None

nvl clear
nvl hide dissolve

scene bg city_street4 onlayer master
show emicas smile_close onlayer master at center
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

window show

emi "So, wir sind da."


play music music_soothing fadein 2.0

"Gleich nachdem wir aus dem Bus gestiegen sind, greift Emi sich meine Hand und beginnt, die Straße entlang zu laufen."


show emicas wink_up_close onlayer master
with charachange

emi "Komm schon, wir haben noch ein paar Blocks, bis wir da sind."


hi "Was? Oh, okay."


scene bg city_alley onlayer master
with locationchange

stop ambient fadeout 12.0

"Ich folge Emi in eine Seitenstraße. Ihrem Gang zufolge ist sie gut gelaunt."


"Dafür, dass wir einfach nur gehen, gibt sie ein recht schnelles Tempo vor."


"Scheint, als wäre sie auch etwas nervös."


hi "Also… Macht deine Mutter das öfter?"


show emicas neutral_close onlayer master at center
with charaenter

emi "Nö, nicht allzu oft. Mama spielt nicht gern die Gastgeberin."


hi "Ach ja?"


show emicas awayfrown_close onlayer master
with charachange

emi "Ja, Papa war immer derjenige, der sie gedrängt hat, Leute einzuladen."


"Diese plötzliche und unerwartete Erwähnung ihres Vaters überrascht mich."


"Und ihrem Gesichtsausdruck nach zu urteilen bin ich nicht sicher, ob sie vorhatte, ihn zu erwähnen. Ich glaube, sie hat ihn bisher nur ein einziges Mal erwähnt."


"Alles, woran ich mich erinnere, ist, dass Emis Mutter mir gesagt hat, dass er nicht mehr da ist."


hi "Ja? Deine Mutter ist also lieber allein?"


show emicas happy_up_close onlayer master
with charachange

"Emi lacht. Entweder ist sie erleichtert, dass ich nicht nach ihrem Vater gefragt habe, oder sie findet meine Frage wirklich lustig."


emi "Nein, gar nicht! Ihretwegen bin ich so ein kontaktfreudiger Mensch, weißt du?"


show emicas closedsmile_close onlayer master
with charachange

emi "Sie ist nur lieber Gast als Gastgeber. Sie sagt, das sei nicht so stressig."


hi "Offensichtlich war sie noch nie bei der Mutter ihrer Freundin zum Essen."


"Emi kichert wieder und kann sich ein Sticheln nicht verkneifen."


show emicas wink_close onlayer master
with charachange

emi "Nervös, Hisao?"


show emicas smile_close onlayer master
with charachange

emi "Brauchst du nicht zu sein! Ist doch keine große Sache! Einfach nur Essen bei mir zu Hause, das ist alles!"


hi "Ja, aber hast du jemals deinen Freund mitgebracht?"


"Ich muss gestehen, dass ein Teil von mir sich vor der Antwort auf diese Frage fürchtet."


"Ich weiß nur sehr wenig über Emis frühere Beziehungen. Ich weiß nicht einmal, ob es frühere Beziehungen gab."


show emicas awayfrown_close onlayer master
with charachange

emi "Nein, ich denke nicht."


show emicas frown_close onlayer master
with charachange

emi "Hey, vielleicht ist das ja doch eine größere Sache…"


hi "Oh, gut, jetzt bin ich doppelt nervös."


"Aber um ehrlich zu sein, bin ich ziemlich froh, dass ich der Erste bin."


"Vielleicht ist unsere Beziehung ja doch etwas Besonderes."


stop ambient
stop music fadeout 10.0

scene bg emi_houseext onlayer master
with locationchange

play sound sfx_hammer

"Ermutigt von diesem Gedanken bin ich deutlich ruhiger, als Emi schließlich an ihre Haustür klopft."


show emicas grin_up onlayer master at center
with charaenter

emi "Hallo Mutti! Mach auf, wir sind da!"


show bg emi_houseext onlayer master at bgleft
show emicas grin_up onlayer master at twoleft
with charamove

show meiko smile onlayer master at tworight
with charaenter

"Die Tür öffnet sich, und Frau Ibarazaki grinst ihre Tochter an. Das Grinsen sieht dem von Emi überraschend ähnlich."


"Daran werde ich mich nie gewöhnen."


show meiko wink onlayer master
with charachange

emm "Weißt du, normalerweise warten die Leute ein paar Minuten, bevor sie anfangen, die Tür anzuschreien."


show emicas pout_up onlayer master
with charachange

emi "Und die meisten Mütter begrüßen ihre Töchter, anstatt sie sofort zu kritisieren."


show meiko happy onlayer master
with charachange

emm "Ah, natürlich. Willkommen zu Hause, Liebes. Ich hab dich vermisst."


play music music_another fadein 0.5

scene bg emi_kitchen onlayer master
with locationchange

"Eine liebevolle Umarmung später sind wir drinnen, und erst jetzt scheint Emis Mutter einzufallen, dass ich auch da bin."


show meiko smile onlayer master at center
with charaenter

emm "Hallo Hisao. Wie geht es dir?"


hi "Ganz gut, danke. Es ist schön, sich mal eine Zeit lang keine Gedanken über die Schule machen zu müssen."


show meiko happy onlayer master
with charachange

emm "Ach ja, eure Prüfungen sind vorbei, nicht war? Da seid ihr beide sicher erleichtert."


hi "Stimmt, mir ist ein Stein vom Herzen gefallen."


show bg emi_kitchen onlayer master at bgright
show meiko happy onlayer master at tworight
with charamove

show emicas happy onlayer master at twoleft
with charaenter

emi "Mir auch! Ich glaube, ich habe letzte Nacht zum ersten Mal seit Wochen wieder richtig gut geschlafen."


"Wenn diese Nachricht eine Überraschung für Emis Mutter ist, lässt sie sich nichts anmerken. Aber aus ihrer Antwort kann ich dennoch Interesse heraushören."


show meiko smile onlayer master
with charachange

emm "Wirklich? Es freut mich, das zu hören, Emi. Du weißt, dass ich mir Sorgen mache, wenn du so angespannt bist wegen… der Prüfungen."


"Offensichtlich weiß Emis Mutter etwas, was ich nicht weiß – oder besser, sie weiß nicht, dass Emi mir von den Albträumen erzählt hat."


"Es ist interessant, zu beobachten, wie Frau Ibarazaki ihre Tochter deckt. Dieser Schutzinstinkt, sicherzustellen, dass ich nicht mehr erfahre, als Emi mir erzählen will."



label de_E26e:

"Anscheinend hat Emi mehr mit Quarks gemeinsam als ich dachte."


"Bewegt sich schnell, unmöglich durch direkte Beobachtung zu verstehen, dennoch hat sie einen Einfluss auf jeden, mit dem sie Kontakt hat."


label de_E26f:

"Ich frage mich, ob Frau Ibarazaki herausfinden wird, dass ich von den Albträumen weiß – oder hält sie einfach alles vor jedem geheim?"


show emicas weaksmile onlayer master
with charachange

emi "Ja, es war dieses Jahr nicht so schlimm wie früher; Hisao hat mir geholfen, mich zu konzentrieren."


"Okay, ich weiß, dass das nicht stimmt. Sie hat in der Prüfungswoche außerhalb der Schulzeit sogar den Kontakt völlig abgebrochen!"


"Aber… Tagsüber haben wir uns gesehen. Und sie hat mir mehr als einmal gesagt, dass unser Training morgens das einzige war, worauf sie sich während der Prüfungswoche gefreut hat. Also ist es vielleicht gar keine so große Lüge."


"Jedenfalls fühle ich mich ein wenig besser, wenn ich höre, dass meine Anwesenheit zumindest ein bisschen geholfen hat."


"Emis Mutter hebt eine Augenbraue. Entweder sie glaubt Emi nicht, oder sie ist genauso überrascht wie ich."


show meiko happy onlayer master
with charachange

emm "Nun, dann ist es ja anscheinend gut, dass ihr beide euch so nahesteht."


show meiko smile onlayer master
with charachange

emm "Ich würde dir ja sagen, du sollst dich gut um meine Tochter kümmern, Hisao, aber es sieht so aus, als würdest du das schon tun."


show emicas closedsmile onlayer master
with charachange

"Emi grinst und scheint stolz zu sein, dass sie es geschafft hat, mich bei ihrer Mutter so positiv darstellen."


hi "Ich würde eher sagen, Ihre Tochter kümmert sich gut um mich. Sie hat mich dazu gebracht, regelmäßig zu trainieren."


hi "Seit ich sie getroffen habe, bin ich wahrscheinlich sogar aktiver als vor…"


"Ich habe noch nie darüber nachgedacht, und auch die Ironie ist mir noch nie so bewusst geworden."


"Vor meinem Herzanfall war ich nicht wirklich aktiv. Gelegentliche Fußballspiele zählen nicht, dafür waren sie zu selten."


"Und jetzt, wo ich sicher weiß, dass ich ein schwaches Herz habe, {b}jetzt{/b} laufe ich jeden Tag und fordere mit Hilfe meiner Medikamente mein Schicksal heraus."


"Ich lache leise, dann wird mir bewusst, dass ich meinen Satz nicht beendet hatte."


hi "Na ja, vor meinem Herzanfall und meiner Ankunft an dieser Schule."


"Ich kann das einfach so locker sagen. Es gab eine Zeit, da hätte ich mir zweimal überlegt, ob ich überhaupt über meine Probleme sprechen sollte."


"Aber jetzt? Jetzt scheint es einfach nur lächerlich zu sein, sich darüber Gedanken zu machen – besonders in Gegenwart von Emi und ihrer Mutter."


"Wenn Emi ganz ungezwungen über ihre Behinderung reden kann, kann ich das auch."


"Ich erinnere mich an das Leichtathletikturnier, wo Emi sich selbst als das schnellste Wesen auf keinen Beinen bezeichnet hat."


"Ihr offensichtlicher Verlust hat ihr anscheinend nie etwas ausgemacht – zumindest nicht in der Öffentlichkeit."


"Im Rollstuhl zu sitzen hat sie frustriert, das weiß ich. Aber sogar damit ist sie allein fertig geworden, obwohl ich mir Mühe gegeben habe, ihr zu helfen."


show meiko happy onlayer master
with charachange

emm "Emi hat so eine Art, die die aktive Seite in Menschen zum Vorschein bringt. Ich habe nie herausgefunden, wie sie das anstellt."


"Ein Teil davon ist sicher dieser Hundeblick."


show meiko smile onlayer master
with charachange

emm "Es wundert mich gar nicht, dass sie es geschafft hat, dich zum Training zu überreden."


emm "Wenn Rin nicht genauso stur wäre wie sie, bin ich mir sicher, dass Emi sie auch dazu gebracht hätte, mit euch zu laufen."


show emicas happy onlayer master
with charachange

emi "Oh, da fällt mir ein… Ich soll dich von Rin grüßen."


scene bg emi_dining onlayer master
with locationchange

"Das Gespräch läuft eine Weile ohne mich weiter, während wir uns zum Essen ins Wohnzimmer begeben."


"Es riecht sehr lecker hier drinnen, und die Auswahl, die Emis Mutter vorbereitet hat, ist beeindruckend."


show meiko smile onlayer master at tworight
show emicas happy_up onlayer master at twoleft
with charaenter

emi "Wow, du hast ja genug gemacht, um eine Armee zu verköstigen!"


show meiko happy onlayer master
with charachange

emm "Ist es zu viel? Na ja, ihr könnt ja ein paar Reste mitnehmen, wenn ihr geht."


hi "Das hört sich großartig an! Das Essen in der Cafeteria kann man nicht allzu lange aushalten. Etwas Selbstgemachtes wäre eine willkommene Abwechslung."


show emicas smile onlayer master
with charachange

emi "Wie er schon sagte. Danke, Mutti."


"Das Essen schmeckt genauso gut wie es riecht, und während wir Essen, verebbt unser Gespräch."


"Emi attackiert ihren Teller mit dem üblichen Enthusiasmus, und ich gebe zu, dass ich auch ein gutes Tempo vorlege."


show meiko wink onlayer master
with charachange

emm "Also Hisao, ich habe gehört, dass du und meine Tochter euch sehr nahe steht, hmm?"


"Der Drang, etwas zu sagen wie „Nicht wirklich” ist so stark, dass ich schon den Mund öffne, um es zu sagen, aber ich kann mich gerade noch bremsen."


"Wir stehen uns nahe, so viel ist sicher. Ich meine, Emi hat mich hierher eingeladen oder etwa nicht?"


"Zum Glück scheinen sowohl Emi als auch ihre Mutter meine Reaktion so zu interpretieren, dass ich überrascht bin, und nicht, dass ich beinahe etwas Gemeines gesagt hätte."


hi "Hey, das stimmt wohl. Ich für meinen Teil gebe den morgendlichen Trainings die Schuld."


show emicas pout_up onlayer master
with charachange

emi "Das hört sich ja an, als wäre das etwas Schlimmes, Hisao."


show meiko smile onlayer master
with charachange

emm "Na ja, ich bin jedenfalls erleichtert."


hi "Warum das?"


show meiko worry onlayer master
with charachange

emm "Emi war immer sehr beliebt, aber sie hatte nie viele enge Freunde."


"Das ist mir neu. Ich habe Emi schon oft in den Gängen mit Klassenkameraden reden sehen."


"Und zumindest die gesamte Leichtathletikmannschaft scheint sie zu vergöttern… Aber es stimmt schon, dass sie beim Mittagessen immer mit Rin und mir allein ist."


"Nicht gerade, was man von einem beliebten Mädchen erwarten würde. Andererseits habe ich aus erster Hand erfahren, dass sie Leute nur ungern an sich heranlässt, also bin ich nicht wirklich überrascht."


show meiko serious onlayer master
with charachange

emm "Ich hatte schon meine Zweifel."


show emicas awayfrown_up onlayer master
with charachange

"Emi rollt ihre Augen und grummelt etwas, was ich nicht ganz verstehen kann."


stop music fadeout 1.0

hi "Hm?"


show emicas neutral_up onlayer master
with charachange

emi "Was?"


hi "Was hast du gerade gesagt?"


show emicas blush onlayer master
with charachange

emi "Nichts."


show meiko happy onlayer master
with charachange

"Frau Ibarazaki verschluckt sich vor Lachen an ihrem Getränk."


play music music_comedy fadein 0.5

emm "Du bist zu viel mit Doc zusammen, Emi."


emm "Ich muss ein ernstes Wort mit ihm reden, wenn er anfängt, meine Tochter zu verderben."


hi "Irgendwie glaube ich nicht, dass das sehr effektiv wäre."


show emicas evil onlayer master
with charachange

emi "Das Meiste hab ich sowieso von dir und nicht von Doc."


show meiko smile onlayer master
with charachange

emm "Hör nicht auf sie, Hisao. Sie ist eine geborene Lügnerin."


show emicas awayfrown onlayer master
with charachange

emi "Hmpf. Ja genau."


hi "Oh, ich weiß nicht, Emi. Ich denke, deine Mutter hat irgendwie Recht."


show emicas angry_up onlayer master
with charachange

emi "Was? Du Verräter! Du sollst hier meine Partei ergreifen!"


hi "Ja, aber bei deinem Bein hast du gelogen, nach dem Tu-{w=0.3}{nw}"


with vpunch

extend " Autsch!"


"Ein Tritt gegen das Schienbein von einem Fuß, der unverkennbar aus Plastik ist, unterbricht mich, aber nicht bevor Frau Ibarazakis Augenbrauen in die Höhe schießen."


show meiko serious onlayer master
with charachange

emm "Was ist mit deinem Bein?"


show emicas awayfrown onlayer master
with charachange

emi "Es war nicht so schlimm, es war nur… Ich war nur, äh, eineZeitlangimRollstuhl."


"Emis Mutter entziffert schnell die letzten gemurmelten Worte – ich vermute, sie hat Erfahrung mit so etwas – und schaut Emi besorgt an."


show meiko worry onlayer master
with charachange

emm "Also deshalb hat er in letzter Zeit nie zurückgerufen…"


emm "Oh Emi… Ich weiß, wie sehr du Rollstühle hasst."


emm "Kein Wunder, dass du in letzter Zeit so schlecht gelaunt warst."


show emicas frown onlayer master
with charachange

hi "Ja, sie ist viel fröhlicher, wenn sie auf ihren Beinen steht."


show meiko serious onlayer master
show emicas awayfrown onlayer master
with charachange

emm "Natürlich! Sie hat nach dem Unfall schon genug Zeit im Rollstuhl verbracht."


show emicas frown onlayer master
with charachange

hi "Sie hat die Prothesen nicht sofort bekommen?"


show meiko worry onlayer master
show emicas awayfrown onlayer master
with charachange

emm "Nein, die Wunden mussten erst verheilen, bevor sie mit der Art Therapie anfangen durfte, die man braucht, um sich an diese Dinger zu gewöhnen."


emm "Insbesondere weil sie damit rennen wollte."


show emicas frown onlayer master
with charachange

hi "Das wusste ich gar nicht."


show emicas weaksmile_up onlayer master
with charachange

emi "Ja, es war beschissen. Oh, hast du Rins Wandbild auf dem Schulfest gesehen?"


"Bei Emis plötzlichem Themawechsel fällt mir – etwas verspätet – auf, dass sie die ganze Zeit, als ihre Mutter und ich geredet haben, unruhig hin und her gerutscht ist."


"Ich hätte mir denken können, dass es ihr unangenehm ist, über den Unfall zu reden. Auch wenn nur ihre Mutter hier ist."


show meiko serious onlayer master
with charachange

emm "Nein, ich konnte doch am Schulfest nicht kommen, weißt du das nicht mehr?"


show meiko happy onlayer master
with charachange

emm "Aber ich habe es beim Turnier von Weitem gesehen. Sah ziemlich seltsam aus."


show emicas closedsmile onlayer master
with charachange

emi "Ich glaube, das ist mehr oder weniger was sie wollte. Sie hat immer gesagt, es wäre wie ein Traum. Oder sie wollte es wie einen Traum aussehen lassen."


show meiko smile onlayer master
with charachange

emm "Rins Kunst ist eine Sache, die ich wohl niemals verstehen werde."


show emicas wink onlayer master
with charachange

emi "Das überrascht mich nicht. Ich glaube, Rin erwartet gar nicht, dass man sie versteht."


show emicas grin onlayer master
with charachange

emi "Sie hat mir mal erzählt, dass Kunst Leuten hilft, Dinge zu verstehen, die sie sonst nicht verstehen würden, aber trotzdem glaubt sie selbst nicht, dass es so ist."


"Ich bin überrascht, dass Emi so ausführlich mit Rin darüber gesprochen hat, dass sie Rin tatsächlich ihre Meinung entlocken konnte – was auch immer das bedeutet."


"Obwohl ich nicht glaube, dass Rin Emis Meinung aus ihr herausbekommen würde, selbst wenn sie es wollte."


"Es sei denn, Emi erzählt mir absichtlich nichts – das ist zwar wahrscheinlich aber trotzdem ein unangenehmer Gedanke."


"Ich hänge diesen unangenehmen Gedanken eine Weile nach und verpasse den nächsten Teil des Gesprächs."


show meiko serious onlayer master
with charachange

emm "Hey, Emi, was ich dich fragen wollte…"


show emicas neutral onlayer master
with charachange

emi "Hm?"


show meiko worry onlayer master
with charachange

emm "Wirst du dieses Jahr deinen Vater besuchen?"


stop music fadeout 3.0

"So wie sie es sagt, könnte man meinen, dass Emis Mutter über das Wetter redet. So wie Emi reagiert, reden die beiden aber offensichtlich nicht über das Wetter."


show emicas awayfrown onlayer master
with charachange

"Sie verzieht das Gesicht und zuckt leicht mit dem Kopf zurück, als hätte man ihr gerade ins Gesicht geschlagen."


show emicas sad onlayer master
with charachange

emi "Können wir später darüber reden?"


"Ihre Stimme hört sich brüchig an, angestrengt. Es sieht aus, als hätte die Frage sie stark mitgenommen."


"Es sieht aus, als hätte Frau Ibarazaki falsch eingeschätzt, wie nahe Emi und ich uns stehen."


"Es scheint, dass man über einige Dinge besser nicht redet, wenn ich dabei bin. Ihr Vater ist eines dieser Dinge."


"Der Unfall, bei dem sie ihre Beine verloren hat, gehört wahrscheinlich auch dazu, wenn man von ihrer Reaktion auf meine Unterhaltung mit ihrer Mutter vorhin ausgeht."


"Es dauert nicht lange, bis Emis Mutter merkt, dass sie Mist gebaut hat."


show meiko happy onlayer master
with charachange

emm "Natürlich können wir das, Liebes. Tut mir leid, dass ich es erwähnt hatte, ich wollte es nur wissen, damit ich den Termin-"


show emicas neutral onlayer master
with charachange

emi "Schon in Ordnung. Mach dir keine Sorgen."


"Emi sieht nervös aus, als wäre ihr ihre Reaktion peinlich. Ich muss gestehen, dass ihre Reaktion mich verwirrt."


"Sie hat ihren Vater mir gegenüber heute schon erwähnt! Das ist nicht mal zwei Stunden her!"


"Warum erzeugt eine einfache Frage, wann sie ihren Vater besuchen will, eine so starke Reaktion?"


"Es sei denn, die Gelassenheit, die sie angeblich durch unser Gespräch gestern Abend gewonnen hat, ist plötzlich verflogen."


"Oder es hat nicht so viel geholfen, wie sie dachte. Oder behauptet hat."


show emicas weaksmile onlayer master
with charachange

emi "Ich, äh, bin gleich wieder da. Muss mal für kleine Mädchen."


hide emicas onlayer master
with charaexit

show bg emi_dining onlayer master at bgleft
show meiko smile onlayer master at center
with dissolvecharamove

"Emi steht abrupt auf und verlässt den Tisch. Frau Ibarazaki und ich bleiben allein zurück."


"Ich bin mir unsicher. Soll ich ihr nachgehen, oder soll ich hier warten?"


"Es ist offensichtlich, dass Emi nicht wegen eines kleinen Geschäftes weggegangen ist. Irgendetwas bedrückt sie, und ich muss wissen, was das ist."




label de_choiceE26:
menu:
    with menueffect
    "Wie stelle ich das an?"
    "Geh ihr nach.":




        return m1
    "Rede mit ihrer Mutter.":


        return m2


label de_E26c:

"Der einzige Weg, das herauszufinden, ist, zur Quelle zu gehen. Und die Quelle tut gerade so, als müsste sie zur Toilette."


scene bg emi_kitchen onlayer master
with locationchange

"Ich entschuldige mich höflich und gehe in diese Richtung, treffe Emi aber nicht im Bad an, sondern in der Küche, direkt neben dem Wohnzimmer."


show emicas sad onlayer master
with charaenter

"Emi hat die Tür offen gelassen, und als ich näherkomme, sehe ich, dass sie sich auf den Tisch stützt und versucht, sich zu beruhigen – ein Versuch, der scheitert, sobald ich den Mund öffne."


hi "Sieht aus, als wäre es nicht so dringend gewesen."


show emicas angry onlayer master
with charachange

"Emi schreckt auf und starrt mich an."


show emicas angry_up onlayer master
with charachange

emi "Was machst du hier? Ich bin nicht hierher gekommen, weil ich Gesellschaft wollte."


hi "Ich wollte dir nur helfen. Du sahst aus, als wärst du ziemlich durch den Wind."


show emicas awayfrown onlayer master
with charachange

emi "Hab ich nicht gesagt, es ist nichts? Außerdem haben wir doch schon klargestellt, dass du mir nicht helfen kannst."


hi "Nein, wir haben klargestellt, dass du ein Sturkopf bist."


show emicas angry onlayer master
with charachange

emi "Du sei mal ganz still. Du bist mir schließlich nachgelaufen."


hi "Das ist etwas anderes! Ich will dir helfen mit… was auch immer dein Problem ist."


show emicas awayfrown onlayer master
with charachange

emi "Das ist lustig, denn {b}ich{/b} will einfach, dass du mich allein lässt."


hi "Aber warum? Warum kannst du mir nicht vertrauen?"


show emicas frown onlayer master
with charachange

emi "Wir haben schon darüber gesprochen, Hisao. Ich muss damit allein fertig werden."


hi "Das akzeptiere ich nicht! Du brauchst meine Hilfe, du willst sie nur nicht annehmen!"


"Das habe ich vielleicht etwas unglücklich ausgedrückt."


show emicas angry onlayer master
with charachange

emi "Brauchen? Ich {b}brauche{/b} deine Hilfe?"


play music music_tragic fadein 0.5

show emicas angry_up onlayer master
with charachange

emi "Na dann ist es ja gut, dass wir uns getroffen haben, nicht wahr? Denn sonst wäre ich ja nur ein kaputter Mensch, oder?"


emi "Nein, es ist verdammt noch mal gut, dass Hisao aufgetaucht ist, um mich zu retten! Denn Gott weiß, ich kann mich nicht selbst retten, nicht wahr?"


emi "Ich bin ja nur das arme, emotional geschädigte Mädchen ohne Beine, richtig?"


hi "Emi, du weißt, dass ich nicht so-"


show emicas angry onlayer master
with charachange

emi "Wirklich? Wenn du wirklich nicht so denken würdest, dann wärst du wohl nicht hier, um mir zu erzählen, dass ich deine Hilfe brauche."


emi "Ich habe es in meinem Leben auch ohne deine Hilfe recht weit gebracht."


hi "Also bedeutet dir unsere Beziehung überhaupt nichts? Ich bin nur der Typ, mit dem du abhängst?"


show emicas awayfrown onlayer master
with charachange

emi "Du bist mein Freund, Hisao, nicht mein Retter."


hi "Natürlich nicht, das ist ja offensichtlich. Du willst ja nicht einmal in Betracht ziehen, dass ich dir helfen könnte, oder?"


hi "Du frisst einfach alles in dich hinein und hoffst, dass Laufen deine Probleme lösen wird, oder du kommst mich besuchen, und wir haben Spaß, bis es dir wieder besser geht."


hi "Das ist nicht was ein gesunder Mensch tut, Emi. Das ist nicht, worum es in einer Beziehung geht."


show emicas frown onlayer master
with charachange

emi "Nun, das ist, worum es mir in einer Beziehung geht, Hisao."


show emicas sad onlayer master
with charachange

emi "Ich wünschte-"


"Sie scheint ihre Worte noch einmal zu überdenken. In ihrem Gesicht flackert kurz Schmerz auf, Zweifel. Einen Moment lang habe ich den Eindruck, sie fängt gleich an zu weinen."


show emicas frown onlayer master
with charachange

"Aber der Moment geht vorbei, und sie fasst sich wieder. Was auch immer sie sich wünscht, bleibt unausgesprochen."


emi "Hisao, es ist… Ich kann das momentan einfach nicht."


hi "Was? Ein ernsthaftes Gespräch führen? Offen sein? Ehrlich sein? An irgendjemand anderen denken als an dich selbst und an deine Probleme?"


show emicas angry_up onlayer master
with charachange

emi "Was weißt du von meinen Problemen? Nichts! Du weißt nicht, was ich durchgemacht habe, also tu nicht so als ob."


hi "Ich weiß, dass du Albträume hast, und ich weiß, dass dein Vater weg ist. Was ist mit ihm passiert?"


show emicas sad_up onlayer master
with charachange

"Emis Kopf zuckt zurück, als hätte ich sie geschlagen. Der spröde Unterton ist wieder in ihrer Stimme."


show emicas sad onlayer master
with charachange

emi "Das reicht."


"Das ist dämlich. Das gesamte Gespräch lang blockt Emi mich einfach immer wieder ab."


hi "Was? Nicht einmal diese Frage willst du beantworten? Gut, behalt deine Geheimnisse. Nimm sie meinetwegen mit ins Grab."


show emicas blush onlayer master
with charachange

"Emis Augen weiten sich. Als sie wieder spricht, ist ihre Stimme tief und bedrohlich."


show emicas grit onlayer master
with charachange

emi "Verschwinde aus meinem Haus, Hisao."


"Die plötzliche Änderung ihres Tones reißt mich aus meiner selbstgerechten Wut, und mit Schrecken wird mir bewusst, was ich gerade gesagt habe."


hi "Emi, so habe ich das nicht-"


stop music fadeout 2.0

show emicas angry onlayer master
with charachange

emi "Ich habe gesagt, du sollst {b}verschwinden{/b}, Hisao."


emi "Sag meiner Mutter, dass sie ein wundervolles Essen gekocht hat, aber du hast noch eine andere Verabredung, und verschwinde aus meinem Haus."


"Sie zittert jetzt – vor Wut, Trauer oder Entschlossenheit. Ihre Stimme ist immer noch tief und kontrolliert. Fast ein Knurren."


"Ich versuche, ihr einen Arm auf die Schulter zu legen, um mich dafür zu entschuldigen, dass ich zu weit gegangen bin, aber sie weicht mir aus."


show emicas angry_up onlayer master
with charachange

emi "Verschwinde."


show bg emi_dining onlayer master at bgleft
show meiko serious onlayer master at center
with locationchange

"Was bleibt mir übrig? Ich gehe aus der Küche ins Wohnzimmer, entschuldige mich bei Frau Ibarazaki und verlasse das Haus."


$ suppress_window_after_timeskip = True

scene black onlayer master
with dissolve





label de_E26d:

"Am Tisch herrscht erst einmal eine unangenehme Stille, nachdem Emi hinausgerannt ist. Ich weiß nicht was ich sagen soll."


show meiko serious onlayer master
with charachange

"Emis Mutter seufzt und bricht das Schweigen."


play music music_moonlight fadein 5.0

emm "Tut mir leid, Hisao. Ich vergesse manchmal, dass Emi bei einigen Themen sehr empfindlich ist."


emm "Und ich habe auch noch über die Sache mit dem Rollstuhl gesprochen…"


hi "Sollte ich ihr nachgehen?"


show meiko worry onlayer master
with charachange

emm "Um Himmels Willen, nein! Sie ist ja nicht rausgelaufen, um das Gespräch fortzuführen, oder?"


hi "Aber wenn sie Probleme hat, sollte ihr nicht jemand helfen?"


show meiko serious onlayer master
with charachange

emm "Bei jedem anderen würde ich sagen Ja. Aber meine Tochter ist störrisch wie ein Esel, und wenn sie allein sein will, ist es besser, sie allein zu lassen."


emm "Sonst würde sie wahrscheinlich etwas sagen, was sie später bedauert, und dann würdest du etwas sagen, was du später bedauerst, und es wäre mir lieb, wenn dein Besuch nicht damit endet, dass einer von euch beiden wütend aus dem Haus stürmt."


show meiko happy onlayer master
with charachange

emm "Wenn das passieren würde, wäre ich eine furchtbare Gastgeberin, nicht wahr? Ich habe mich heute schon einmal zum Narren gemacht."


hi "Schon in Ordnung. Ich hätte wohl den Rollstuhl nicht erwähnen sollen."


show meiko serious onlayer master
with charachange

"Frau Ibarazaki runzelt die Stirn. Offensichtlich stört sie Emis diesbezügliches Schweigen mehr, als sie sich anmerken lassen will."


emm "Ich wünschte, sie würde das nicht tun. Ich mache mir nur noch mehr Sorgen, weißt du?"


hi "Sie macht das öfter?"


show meiko smile onlayer master
with charachange

emm "Was? Zur Toilette rennen? Nein, nicht wirklich. Ihrer Mutter Verletzungen verschweigen? Na ja, das kommt schon häufiger vor."


emm "Jedes Mal, wenn ich sie bei einer solchen Lüge erwische, versichert sie mir, dass sie es mir nur nicht gesagt hat, weil es nicht so schlimm war."


hi "Wenn es hilft: Ich bin sicher, der einzige Grund, warum ich davon wusste, ist, dass ich sie jeden Tag gesehen habe."


show meiko happy onlayer master
with charachange

"Das lockt ein trockenes Lachen aus ihr hervor. Frau Ibarazaki seufzt ein wenig traurig."


show meiko smile onlayer master
with charachange

emm "Sie will immer noch keine Leute an sich heranlassen, hm? Ich hoffe ja immer noch, dass sie darüber hinwegkommt."


emm "Es ist schon irgendwie komisch. In so vielen Belangen hat sie sich so gut von dem Unfall erholt…"


show meiko serious onlayer master
with charachange

emm "Ich denke, manche Dinge wird man nie vollständig los."


"So wie es aussieht, bedrückt sie diese Sache immer noch."


"Aber sie scheint ein wenig mehr Bereitschaft zu zeigen, über den Unfall zu sprechen, wenn Emi nicht in der Nähe ist."


hi "Ich habe eine Frage, wenn das in Ordnung ist."


show meiko smile onlayer master
with charachange

emm "Ja?"


hi "Was hat Emi bei dem Unfall noch verloren? Doc sagte, sie ist jedes Jahr so, wenn der Unfall sich jährt, und sie will mit mir nicht darüber reden…"


show meiko happy onlayer master
with charachange

emm "Also dachtest du, ich würde es dir sagen, hmm?"


hi "Äh, ja. Das hatte ich gehofft."


show meiko serious onlayer master
with charachange

emm "Na ja, da gibt es nur ein Problem, weißt du?"


hi "Lassen Sie mich raten: Sie haben Emi versprochen, dass sie es niemandem erzählen, von dem sie nicht will, dass er es weiß, und Sie wissen nicht, ob sie will, dass ich es weiß?"


emm "So was Ähnliches. Ich habe Emi versprochen, dass sie diejenige ist, die die ganze Geschichte erzählt."


hi "Aber ist das nicht wichtig? Ich meine, es hatte offensichtlich starke Auswirkungen auf sie, wenn sie so lange nach dem Unfall immer noch darunter leidet."


show meiko worry onlayer master
with charachange

emm "Das ist wahr. Es hatte einen lange andauernden Effekt auf sie. Es gibt einige Dinge, über die sie wahrscheinlich nie wirklich hinwegkommen wird."


"Einen Moment lang sieht Frau Ibarazaki unglaublich traurig aus, als ob eine alte Wunde ihr zu schaffen machen würde."


emm "Ich glaube, es gibt einige Dinge, über die ich wohl auch nie hinwegkommen werde…"


show meiko happy onlayer master
with charachange

"Noch ein trockenes Lachen, und mit einem Kopfschütteln verscheucht Emis Mutter die Erinnerung."


show meiko smile onlayer master
with charachange

emm "Schau mal, da ist etwas, was du unbedingt verstehen musst – über die Art, wie Emi über den Unfall denkt."


hi "Und das wäre?"


emm "Es war keine große Sache."


stop music fadeout 1.0

"Irgendwie schaffe ich es zu verhindern, dass meine Kinnlade herunterklappt, aber es kostet mich einige Anstrengung."


"Das ist wohl das Lächerlichste, was ich je gehört habe."


hi "Wie bitte?"


play music music_sadness fadein 3.0

show meiko serious onlayer master
with charachange

emm "Gut, vielleicht ist es nicht {b}so{/b} einfach, aber es ist eine ziemlich gute Zusammenfassung. Emi glaubt, dass der Unfall sie nicht geprägt hat und dass alles, was sie verloren hat, sie auch nicht geprägt hat."


emm "Sie ist nicht „das Mädchen, das seine Beine verloren hat,” sie ist „das schnellste Wesen auf keinen Beinen.” Ihr Optimismus und ihre Energie haben bei dem Unfall keinen Schaden gelitten, wenn man sie nach ihrer Meinung fragt."


hi "Aber da ist noch mehr, nicht wahr? Ich meine, gestern Abend hat sie mir gesagt, sie will sich nicht auf mich verlassen, weil es dann schmerzhafter wäre, mich zu verlieren."


show meiko smile onlayer master
with charachange

emm "Nicht wirklich. Du sagtest, sie will dir nicht von dem Unfall erzählen, obwohl du sie danach gefragt hast."


emm "Der Grund, warum sie dir nicht davon erzählt, ist, dass es für sie nichts ist, was für dich wichtig ist. Auch wenn sie nicht fürchterliche Angst hätte, jemandem zu nahe zu kommen, würde sie trotzdem nicht darüber reden."


hi "Sie hat Angst, mir zu nahe zu kommen?"


show meiko happy onlayer master
with charachange

emm "Oh Gott, ja. Auch wenn sie immer davon redet, dass der Unfall ihr nicht geschadet hat, hat sie doch gelernt, wie schnell alles vorbei sein kann."


show meiko smile onlayer master
with charachange

emm "Also lässt sie die Leute nicht an sich heran, und sie wird sich sicherlich gegen jede Andeutung wehren, sie könne nicht allein damit fertig werden."


hi "Aber ich glaube, das kann sie {b}nicht{/b}."


show meiko serious onlayer master
with charachange

emm "Ach nein? Bist du sicher, dass du mit meiner Tochter ausgehst und nicht mit jemand anderem? Glaub mir, Hisao, sie kann allein damit fertigwerden."


hi "Aber sie hat Albträume und schläft nicht gut, und-"


show meiko smile onlayer master
with charachange

emm "Und so ist es jedes Jahr. Meinst du, wenn sie nicht allein damit fertig werden würde, glaubst du wirklich, sie wäre immer noch am Leben? Sie hätte sich umgebracht oder etwas ähnlich Melodramatisches."


hi "Also sollte ich nicht versuchen, ihr zu helfen?"


show meiko serious onlayer master
with charachange

emm "Das habe ich nicht gesagt! Ich hasse es, meine Tochter so zu sehen, und zu wissen, dass sie jemanden hat, auf den sie sich verlassen kann, würde mich sehr erleichtern."


emm "Du musst nur verstehen, dass Hilfe anzunehmen allem widerspricht, was Emi über sich und die Welt im Allgemeinen denkt."


emm "Wenn du dennoch deine Hilfe anbieten willst, ist das deine Sache. Ganz ehrlich würde ich mich freuen, aber es wäre dumm von mir, dich nicht zu warnen. Es wird nicht einfach."


show meiko smile onlayer master
with charachange

emm "Du musst nur Geduld mit ihr haben. Sie steht dir bereits näher als jedem anderen, den sie je auf der Yamaku getroffen hat."


hi "Na ja, ich habe nicht den Eindruck, dass wir uns wirklich nahe stehen."


show bg emi_dining onlayer master at center
show meiko serious onlayer master at tworight
with dissolvecharamove

show emicas evil onlayer master at twoleft
with charaenter

stop music fadeout 0.3

emi "Gut, das macht den nächsten Teil einfacher."


"Bei Emis Stimme kriege ich beinahe einen Herzanfall."


hi "Whoa! Ich habe dich gar nicht zurückkommen hören, Emi."


show emicas angry onlayer master
with charachange

emi "Wie praktisch."


hi "Warte, hast du gelauscht?"


show emicas angry_up onlayer master
with charachange

emi "Nein. Ich bin wohl genau im richtigen Moment zurückgekommen."


show meiko worry onlayer master
with charachange

emm "Emi, Hisao war nur-"


"Emi hebt einen Finger und unterbricht ihre Mutter."


show emicas grit onlayer master
with charachange

emi "Dabei zu gehen? Ja, ich weiß."


"Emi zittert nun vor Wut und schaut ihre Mutter vorwurfsvoll an."


emm "Emi, mach dich nicht lächerlich, wir haben nur-"


show emicas angry_up onlayer master
with charachange

emi "Du hast es {b}versprochen{/b}!"


play music music_rain fadein 0.5

"Der Schmerz in diesem letzten Wort ist beinahe unerträglich für mich. Die Vorstellung, dass ich ihr so sehr wehtun könnte, ist wie ein Tritt in die Magengrube."


"Emis Mutter scheint es ähnlich zu gehen."


emm "Und ich habe dieses Versprechen gehalten! Hör mir einfach zu, es gibt keinen Grund, irgendjemanden aus dem Haus zu werfen."


"Emis Mutter scheint sowohl wütend wegen des Zornausbruchs ihrer Tochter zu sein als auch peinlich berührt, dass ich ihn miterleben musste."


"Ich denke, es gibt nur eine Lösung für dieses Problem."


hi "Schon okay. Ich gehe."


emm "Nein, wirklich, das ist nicht nötig…"


hi "Keine Sorge. Danke für das Essen, Frau Ibarazaki, und für die Ratschläge."


show meiko serious onlayer master
with charachange

emm "Es war mir ein Vergnügen, Hisao. Es tut mir leid, dass wir nicht bis zum Nachtisch gekommen sind."


hi "Schon in Ordnung. Ich muss sowieso auf meine Ernährung achten."


hi "Auf wiedersehen, Emi, Frau Ibarazaki."


"Die Förmlichkeit unseres Gesprächs und die Tatsache, dass ich wirklich aufbreche, scheinen Emis Wut verrauchen zu lassen."


show emicas frown onlayer master
with charachange

emi "Nein, warte. Es tut mir leid, ich war so… und nach gestern Abend dachte ich… Du musst nicht gehen, ich nehme es zurück, es ist okay-"


"Ich kann mir ein kleines Lächeln nicht verkneifen. Sie schafft es kaum, ihre Entschuldigung zu artikulieren, und ich würde wirklich gerne bleiben…"


"Aber ich glaube nicht, dass das im Moment gut wäre. Ich muss darüber nachdenken, was ihre Mutter gesagt hat und wie ich weiter mit unserer Beziehung umgehen soll."


"Außerdem will ich nicht riskieren, Emi in ihrem gegenwärtigen Zustand noch weiter zu verärgern."


hi "Nein, ich denke, es ist besser, wenn ich gehe. Du siehst ziemlich mitgenommen aus, und… Na ja, ich würde sicher nur wieder versuchen, dir zu helfen. Ich weiß, du magst das nicht, also gehe ich lieber."


show emicas sad onlayer master
with charachange

emi "Aber-"


hi "Hey, ist kein Problem. Du willst doch keinen Ritter auf einem weißen Ross, richtig? Versprich mir nur eines, okay?"


show emicas frown onlayer master
with charachange

emi "Was?"


hi "Sei nicht böse auf deine Mutter, okay? Sie hat mir nur ein paar Ratschläge gegeben, das ist alles."


show emicas sad onlayer master
with charachange

"Emi nickt zögernd, als ob dieses einfache Konzept alles ist, was sie im Moment begreifen kann. Sie ist so fürchterlich aus dem Gleichgewicht, aber ich kann momentan nichts daran ändern."


emi "Okay."


hi "Wir sehen uns dann morgen, okay? Laufen morgen früh. Nicht vergessen!"


"Ich kann sehen, dass meine Entscheidung, zu gehen, Emi wehgetan hat. Aber so wie die Dinge stehen, kann ich nichts für sie tun, und ich weiß, dass sie zu stur ist, um zuzugeben, dass sie will, dass ich dableibe."


"Ich beobachte, wie verschiedene Emotionen über Emis Gesicht huschen, als sie versucht, alles, was gerade passiert ist, zu verarbeiten."


show emicas weaksmile onlayer master
with charachange

"Kurz darauf ist da wieder dieser ruhige Gesichtsausdruck – wie gestern Abend – und diese Stimme, die sich so viel Mühe gibt, gelassen zu klingen."


emi "Klar, Hisao. Man sieht sich."


"Wir versuchen gerade beide, keine Emotionen zu zeigen, und es fällt mir schwer, meine Fassade aufrecht zu halten. Darum drehe ich mich um und gehe zur Tür hinaus."


stop music fadeout 7.0

scene bg emi_houseext onlayer master
with locationskip

"Ich schließe sie langsam hinter mir. Als sie ins Schloss fällt, halte ich einen Moment inne, meine Hand immer noch auf dem Türknauf."


"Habe ich gerade die richtige Entscheidung getroffen? Hätte ich bleiben und versuchen sollen, die Sache zu klären?"


"Nein, nicht so. Nicht vor ihrer Mutter. Trotz allem würde ich Emis Mutter gerne vor der Wut abschirmen, die gestern Abend zu Tage getreten ist."


"Obwohl sie es wahrscheinlich gewohnt ist, will mein Beschützerinstinkt Emis Image als fröhliches Mädchen nicht zerstören."


"Erschrocken stelle ich fest, dass meine Hand immer noch auf dem Türknauf liegt. Ich ziehe sie zurück, stecke sie in meine Tasche und gehe die langsam dunkler werdende Straße entlang."


scene bg school_dormhisao onlayer master
with shorttimeskip

play music music_pearly fadein 1.0

"Ich atme tief aus."


"Das Warten bis morgen früh wird nicht einfach."


"Auf jeden Fall muss ich mir überlegen, was ich zu Emi sage. Ich muss mich entschuldigen, und ich muss irgendwie zu ihr durchdringen."


"Was das angeht, spukt mir noch etwas anderes im Kopf herum, während ich auf dem Weg zurück auf mein Zimmer bin."


"Der Brief mit Iwanakos Entschuldigung."


"Als ich ihn erhalten habe, war ich so mit meinem neuen Leben beschäftigt, dass ich ihn nicht einmal richtig gelesen habe."


"Jetzt, wo ich mich in einer ähnlichen Situation befinde, ist meine Neugier wieder geweckt. Was wollte sie mich so dringend wissen lassen?"


"Ihre Gedanken zu lesen, könnte mir zumindest helfen, meine zu ordnen."


"Ich erinnere mich, dass ich ihn weggeworfen habe. Verdammt, wo habe ich das Ding hingeworfen?"


"Ich suche unter meinem Schreibtisch. Dort finde ich nichts, also suche ich an unzugänglicheren, unwahrscheinlicheren Orten."


"…"


"Na ja, zumindest weiß ich nun, wo diese Socke ist, die ich gesucht hatte."


"Aber immer noch kein Brief."


"Als ich meinen Arm unter meinen Nachttisch stecke, fühle ich etwas Zerknittertes zwischen dem Tisch und der Wand klemmen."


"Mit ein wenig Anstrengung kriege ich es bald zu fassen und bringe es ans Tageslicht."


"Bingo."


scene ev hisao_letter_open onlayer master
with locationchange

"Ich setze mich an meinen Schreibtisch und breite das zerknüllte Papier vor mir aus. Mit einer schnellen Bewegung schalte ich meine Tischlampe ein."


"Ich überfliege die einleitenden Phrasen und suche nach der Stelle, wo ich aufgehört hatte zu lesen. Ah, hier ist sie."


window hide

$ written_note("Es gibt noch andere Dinge, die ich dir sagen will. Ich schreibe dir, weil ich das Gefühl hatte, dass ich dir nach dem Vorfall im Winter noch vieles hätte sagen sollen. Ich bedaure wirklich, dass ich es dir nicht persönlich sagen konnte, und ich habe dafür keine Entschuldigung.\n\n\n\n\n")


$ written_note("Die Wahrheit ist, immer wenn ich dich im Krankenhaus besucht habe, war ich sehr besorgt um dich. Ich rede nicht über deine Gesundheit. Du schienst dich immer mehr von mir zu entfernen und den Mut zu verlieren. Ich bin sicher, das ist ganz normal, nachdem so etwas passiert, aber irgendwie hatte ich das Gefühl, dass du damals irgendetwas aufgegeben hast. Glück, vielleicht?\n")


window show

"Glück aufgegeben…"


"Das hört sich unangenehm vertraut an."


window hide

$ written_note("Ich wollte irgendwie meine Gefühle zum Ausdruck bringen, aber ich habe einfach nicht die richtigen Worte gefunden. Ich konnte nichts sagen, um dich zu trösten. Es tut mir wirklich leid, dass ich dich nicht unterstützen konnte, als du mich am nötigsten gebraucht hast. Zumindest kann ich jetzt, nach so langer Zeit, ehrlicher sein.\n\n\n\n")


$ written_note("Wenn ich zu diesen stillen Tagen im Februar und März zurückkehren könnte, würde ich dir sagen, dass du dich nicht aufgeben sollst. Vielleicht hättest du dich nicht so weit von mir entfernt, wenn ich einfach nur etwas gesagt hätte. Ich hoffe, du hast es auch ohne mich geschafft, wieder auf die Beine zu kommen.\n\n\n\n")


$ written_note("Jetzt, wo die Entfernung zwischen uns auch physisch ist, fühlt sich alles irgendwie endgültiger an. Ich frage mich, ob wir uns irgendwann einmal wiedersehen. Vielleicht wäre es besser, wenn nicht? Trotzdem, wenn du mir antworten willst, schreib mir bitte zurück. Ich würde wirklich gerne erfahren, wie es dir an deiner neuen Schule geht. Ich wünsche dir alles Gute.\n\nDeine Iwanako")


window show

"Nachdem ich den Brief zu Ende gelesen habe, streiche ich ihn vorsichtig glatt und lege ihn auf meinem Schreibtisch ab."


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\n\nVielen Dank, Iwanako. Ich wollte auf deine Frage an diesem verschneiten Wintertag mit „ja” antworten, aber ich kam nie dazu."


n "Als wir uns wiedersahen, war es zu spät."


n "Zumindest dachte ich das. Was wäre passiert, wenn ich mich anders verhalten hätte, damals in diesem bedrückend sterilen Krankenzimmer?"


n "Es tut mir leid. Es ist sinnlos, sich jetzt darüber Gedanken zu machen, aber es ist genauso sinnlos, es vergessen zu wollen."


n "Ich bin wer ich bin, wegen allem, was mir passiert ist, und allem, was ich noch erleben will. Gegenwart, Zukunft und Vergangenheit."


stop music fadeout 2.0

n "\n\nUnd die Vergangenheit hat mich vielleicht gerade etwas Wichtiges gelehrt."


$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve






label de_E27:

window hide None

scene black onlayer master
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao onlayer master
with openeye

window show

"Mein Wecker klingelt, und ich drehe mich um und schalte ihn aus. Meine Augen öffnen sich schläfrig und starren auf die Decke."


play music music_night fadein 1.0

window hide
nvl clear
nvl show dissolve

n "\n\nWas mache ich nun? Stehe ich auf, gehe runter zum Sportplatz und tue so, als wäre nichts passiert?"


n "Wird Emi überhaupt da sein? Nach dem, was gestern Abend passiert ist, bezweifele ich das."


n "Und wenn sie da wäre, was würde ich dann tun? Unseren Streit vergessen, nur damit das Problem wieder auftaucht, wann immer sie irgendetwas bedrückt?"


n "Ich weiß, dass ich gestern Abend zu viel gesagt habe – besonders was ihren Vater angeht."


n "Aber war irgendetwas, was ich gesagt habe, wirklich so falsch? Sie wird mich nicht an sich heranlassen – niemals – und sie wird mit allem allein fertig werden müssen."


n "Nichts, was ich tue, nichts, was ich sage, wird das ändern. Sie wird sich nicht ändern, und sie hat sich bereits entschieden, mich auf Abstand zu halten."


n "\nKann ich mich wirklich dazu durchringen, dorthin zu gehen und sie zu treffen, in dem festen Wissen, dass wir nie mehr sein werden als jetzt?"


nvl clear
nvl hide dissolve

scene black onlayer master
with shuteye

window show

"Nein. Das kann ich nicht. Nicht heute. Ich drehe mich um und schlafe weiter."


"Sie ist wahrscheinlich sowieso nicht da."


scene bg school_cafeteria onlayer master
with shorttimeskip

"Ein ähnlicher Gedankengang spielt sich zur Mittagszeit in meinem Kopf ab, und ich gehe in der Cafeteria essen – allein."


"Ich will sie nicht sehen; schon bei dem Gedanken wird mir schlecht."


scene bg school_track_ni onlayer master
with shorttimeskip

"An diesem Abend gehe ich trainieren. Zum ersten Mal, seit Emi nach dem Leichtathletikturnier krank geworden ist, bin ich solo."


"Den Besuch bei Doc lasse ich ausfallen, nur falls er nach Emi fragen sollte."


"Über sie reden will ich auch nicht."


scene bg school_hallway3 onlayer master
with shorttimeskip

"Am nächsten Tag läuft es genauso. Wecker aus. Im Bett bleiben. Allein essen, allein laufen."


"Um die Zeit zu füllen, die ich sonst mit Emi verbringen würde, fange ich an, mehr zu lesen."


"Es funktioniert überraschend gut, bis ich mich dabei ertappe, wie ich mich in einer Toilette verstecke, weil ich sie in der Pause den Gang entlanglaufen sehe."


"Wenn sie mich bemerkt hat, hat sie es sich nicht anmerken lassen – aber sie lässt sich ja nie etwas anmerken."


"Mit Sicherheit nicht gegenüber den anderen Mädchen in ihrer Klasse, die fröhlich mit ihr reden."


"Oder gegenüber den anderen Mitgliedern des Leichtathletikteams."


"Und besonders nicht mir gegenüber."


"Wecker aus. Im Bett bleiben."


scene bg school_scienceroom onlayer master
show muto normal onlayer master at center
with shorttimeskip

"Mutou und ich führen ein langes Gespräch darüber, ob die Stringtheorie plausibel ist oder nicht. Ich selbst glaube nicht daran."


"Mehr als vier Dimensionen kann ich noch akzeptieren. Aber vibrierende Strings im subatomaren Bereich? Das ist etwas zu weit hergeholt."


"Sieht so aus, als wäre ich nicht der einzige, der so denkt. Anscheinend ist die Theorie nicht so belastbar wie man einmal dachte."


"Mutou sagt, das liegt nur daran, dass noch niemand herausgefunden hat, wie man die Daten korrekt interpretieren muss."


$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop

scene bg school_roof onlayer master
with shorttimeskip

"Allein essen."


"Das Dach ist heute verlassen. Ich frage mich kurz, wo Rin und Emi sind, aber ich schiebe die Frage beiseite. Wichtig ist nur, dass sie nicht hier sind, sodass ich nicht mit ihnen reden muss."


"Da ich niemanden zum Reden habe, habe ich ein Buch zum Lesen mitgebracht."


"Das Wetter wird besser; es wird sogar ein bisschen heiß."


"Hoffentlich wird es gegen Abend kühler; ein kühle Brise stärkt diese Hoffnung."


stop ambient fadeout 2.0

scene bg school_track_on_ni onlayer master
with shorttimeskip

"Allein laufen."


"Es ist wirklich kühler am Sportplatz. Keine Spur von Emi, genau wie ich gehofft hatte."


"Ich wärme mich auf, beginne mein übliches Pensum, und versuche dabei die Abwesenheit meiner Trainingspartnerin zu ignorieren."


"Immer wieder driften meine Gedanken ab zu diesem hellen Lachen, diesem unverschämten Grinsen, diesen großen, freundlichen Augen, ihrem unglaublich durchtrainierten Körper-"


scene bg school_track_running_ni onlayer master
with Dissolve(1.0)

"Ich erhöhe die Geschwindigkeit, um meinen Kopf frei zu kriegen. Die Entfernung zwischen mir und den Kurven schmilzt dahin, und ich finde die Geschwindigkeit, bei der ich an nichts denken kann, außer an meine Beine und wie sie schmerzen."


"Ich schaue auf meine Uhr, als ich aus der letzten Kurve komme und stelle fest, dass meine Zeit sich verbessert hat."


show bg school_track_on_ni onlayer master
with Dissolve(2.0)

"Mein Herz fühlt sich heute etwas hibbelig an, also drehe ich ein paar Extrarunden zum Abkühlen – nur um sicherzugehen."


"Kein Grund, Doc darauf aufmerksam zu machen. Es geht mir gut. Ich gebe zu, diese Einstellung erinnert mich sehr an Emi."


"Ich muss einfach hoffen, dass ich irgendwann nicht mehr so viel an sie denken muss."


scene bg school_dormhisao onlayer master
with shorttimeskip

"Ich lese ein weiteres Buch zu Ende, bevor ich an diesem Abend zu Bett gehe. Ich muss morgen in der Bibliothek vorbeischauen."


play sound sfx_switch

show bg school_dormhisao_ni onlayer master
with Dissolve(0.2)

with Pause(0.5)

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 3.5

scene black onlayer master
with shuteye

window hide

with Pause(2.0)
play sound sfx_alarmclock
scene bg school_dormhisao onlayer master
with openeye

window show

"Ich weiß nicht, warum ich meinen Wecker immer noch auf diese Zeit gestellt lasse, aber er weckt mich wieder am nächsten Morgen. Trotzdem schalte ich ihn aus und schlafe weiter."


scene bg school_scienceroom onlayer master
show misha perky_smile onlayer master at center
with shorttimeskip

play music music_pearly fadein 1.0

"An diesem Nachmittag, als ich zu einem weiteren einsamen Mittagessen in die Cafeteria gehen will (Ich habe ein neues Buch über ein paar Gauner im alten Persien, das ich unbedingt lesen will) stellen sich mir plötzlich Misha und…"


"Hm. Sieht aus, als wäre es nur Misha."


show misha hips_smile onlayer master
with charachange

mi "Gehst du wieder allein essen, Hicchan~?"


show misha sign_smile onlayer master
with charachange

mi "Weißt du, wir haben es bemerkt~!"


hi "Wir?"


show misha hips_grin onlayer master
with charachange

mi "Ja! Shicchan und ich haben bemerkt, dass du in letzter Zeit häufiger allein bist!"


show misha hips_smile onlayer master
with charachange

mi "Sie wollte, dass ich herausfinde warum, also habe ich ihr gesagt, ich würde dich fragen!"


hi "Wundert mich, dass sie mich nicht selbst fragt."


show misha perky_smile onlayer master
with charachange

mi "Das wollte sie auch, aber sie wollte mit dem ganzen Papierkram vorankommen. Es gibt viel zu tun, weil das Trimester bald zu Ende ist, weißt du~!"


hi "Warum seid ihr eigentlich plötzlich so an meinem Wohlergehen interessiert?"


show misha sign_smile onlayer master
with charachange

mi "Ah, Shicchan sagte: „Es ist die Pflicht des Schülerrats, auf die emotionale Gesundheit seiner Schüler zu achten!"
mi "Wenn wir zulassen, dass ein Schüler in De-pressionen verfällt, ohne etwas dagegen zu tun, hätten wir unsere Pflichten in unverzeihlicher Weise vernachlässigt!”"


hi "Na dann ist das ja ganz einfach. Ich bin nicht deprimiert."


show misha perky_confused onlayer master
with charachange

mi "Aber du isst allein, und niemand hat dich und Emi in letzter Zeit zusammen gesehen! Irgendwas ist passiert, nicht wahr, Hicchan~?"


"Mishas Stimme nimmt einen strengeren Ton an, aber irgendwie schafft sie es, das gewohnte Trällern am Ende ihrer Sätze beizubehalten."




label de_choiceE27:
menu:
    with menueffect
    "Ich presse meine Lippen zusammen und überlege, wie ich am besten Antworte."
    "Die Sache herunterspielen.":




        return m1
    "Nachgeben und mit Misha reden.":


        return m2







label de_E27a:
"Ich bin nicht sicher, ob ich mit dem Schülerrat über so private Angelegenheiten reden will."


hi "Nichts besonderes."


show misha cross_frown onlayer master
with charachange

mi "Hicchan, Lügen ist etwas ganz Schlimmes~!"


"Sie kauft es mir nicht ab."


"Okay, erzähl ihr etwas – aber nicht zu viel."


hi "Wir hatten eine Meinungsverschiedenheit, die wir noch nicht ausgeräumt haben."


show misha perky_confused onlayer master
with charachange

mi "Ja? Warum nicht?"


hi "Weil… Ich will nicht darüber reden, okay?"


hi "Es ist nichts Schlimmes, okay? Es geht mir gut."


show misha perky_sad onlayer master
with charachange

mi "Und Emi? Geht es ihr auch gut, Hicchan?"


stop music fadeout 4.0

"Mishas Stimme hat nun einen ziemlich ernsten Unterton. Das ist doch lächerlich."


hi "Ich weiß nicht, okay? Ich habe nicht gefragt. Es ist alles gerade ziemlich kompliziert."


show misha hips_frown onlayer master
with charachange

mi "Was für ein Mann bist du eigentlich? Sobald etwas nicht ganz nach Plan geht, läufst du davon?"


play music music_rain fadein 4.0

"Mishas plötzlicher Ausbruch überrascht mich völlig."


show misha cross_frown onlayer master
with charachange

mi "Shicchan würde so etwas feige nennen, und sie hätte auch noch Recht damit!"


mi "Ihr Zwei standet euch sehr nahe. Ihr wart glücklich zusammen! Und nun ziehst du den Schwanz ein und gibst kampflos auf?"


mi "Du solltest bereit sein, um deine Freundin zu kämpfen, Hisao!"


"Ich glaube, gerade Shizune durch Misha sprechen zu hören. Es würde mich nicht überraschen, wenn Shizune ihr ein Skript gegeben hätte, nach dem sie dieses Gespräch abhängig von meinen Antworten führen soll."


"Misha zeigt mit ihrem Arm auf die Tür des Klassenraums."


show misha sign_smile onlayer master
with charachange

mi "Nun mach dich raus und bring die Sache in Ordnung!"


hi "Äh, wir haben noch Nachmittagsunterricht…"


"Das scheint Misha nicht umstimmen zu können."


show misha hips_smile onlayer master
with charachange

mi "Dann eben nach dem Unterricht! Du solltest auf mich hören, Hicchan! Es ist wichtig, solche Dinge nicht auf sich beruhen zu lassen!"


hi "Warum?"


show misha cross_frown onlayer master
with charachange

"Misha schaut mich missbilligend an."



mi "Hat sie dir nichts bedeutet, Hisao? Das ist wichtig oder etwa nicht?"


"Hmm. Sie hat Recht."


"Sie hat mir etwas bedeutet… Nein, sie bedeutet mir immer noch viel."


"Oder etwa nicht?"


hi "Okay. Ich spreche nach dem Unterricht mit ihr."


show misha hips_grin onlayer master
with charachange

mi "Großartig~! Ich werde Shicchan dann sagen, dass es dir wieder gut geht~!"


"Ihre Stimme klingt wieder normal. Das heißt dann wohl, dass Misha mir nicht mehr böse ist."


hide misha onlayer master
with charaexit

"Sie winkt und verschwindet auf den Gang, und ich gehe zum Mittagessen."


scene bg school_scienceroom onlayer master
with shorttimeskip

"Während der Nachmittagsunterricht sich dem Ende zuneigt, bereite ich mich auf die bevorstehende Aufgabe vor."


"Ich muss mit Emi reden; zumindest damit hatte Misha Recht. Das Problem zu ignorieren wird uns nicht weiterhelfen."


"Zumindest muss ich mich für meine Worte entschuldigen."


"Ich überlege, ob ich zu ihrem Zimmer gehen sollte, aber sie ist wahrscheinlich noch auf dem Sportplatz."


scene bg school_courtyard onlayer master
with locationskip

"Auf den Stufen am Eingang des Hauptgebäudes und dem Weg zum Sportplatz komme ich mir vor wie auf dem Weg zu meiner Hinrichtung."


"Ich habe dieses furchtbare Gefühl im Magen, dass alles furchtbar schief gehen wird, und dass ich nichts erreichen werde."


"Außer vielleicht der Beziehung, die Emi und ich hatten, den Rest zu geben."


stop music fadeout 2.0

scene bg school_track onlayer master
with locationskip

"Dort läuft sie – wie erwartet – ihre Runden um den Sportplatz, nachdem alle anderen schon Duschen und Abendessen gegangen sind."


"Ich winke nicht oder mache mich sonst irgendwie bemerkbar. Ich setze mich einfach auf die Tribüne und schaue ihr beim Laufen zu."


show emi basic_confused_gym onlayer master:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter

"Es dauert ein paar Runden, bis sie mich bemerkt. Sie hält abrupt an und ihre Augen weiten sich überrascht."


show emi basic_annoyed_gym onlayer master at center
with charachange

show emi basic_grin_gym onlayer master
with charachange

"Die Überraschung weicht allerdings schnell Ärger, bevor sie ihr Gesicht hinter einer Maske versteckt, die – wie ich weiß – undurchdringlich ist."


emi "Was tust du hier?"


"Nicht ganz die Reaktion, die ich erhofft hatte, aber in dieser Situation kann ich nicht zu viel erwarten."


hi "Ich wollte dich für das, was ich neulich gesagt habe, um Verzeihung bitten."


show emi basic_confused_gym onlayer master
with charachange

emi "Neulich?"


show emi basic_closedgrin_gym onlayer master
with charachange

"Sie lacht ungläubig auf."


play music music_sadness fadein 0.5

show emi basic_grin_gym onlayer master
with charachange

emi "Das ist fast eine Woche her, Hisao."


hi "Ja, na ja… besser spät als nie, oder?"


show emi sad_annoyed_gym onlayer master
with charachange

"Emi verschränkt ihre Arme und starrt mich kühl an, als ob sie meine Gedanken erraten wollte. Schließlich nickt sie."


show emi sad_grin_gym onlayer master
with charachange

emi "Hmmph. Da hast du wohl Recht. Schnee von gestern. Ich vergebe dir."


show emi basic_grin_gym onlayer master
with charachange

emi "Ist das alles?"


show emi basic_grin_gym onlayer master:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi onlayer master
with None

"Ihre fast schon ungeduldige Frage kommt so unerwartet, dass sie schon eine halbe Bahn gelaufen ist, bevor ich reagieren kann."


hi "Nein, warte!"


show emi basic_annoyed_gym onlayer master:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter

"Emi hält an, dreht sich um und geht zu mir zurück. Sie atmet ein wenig schwer und scheint sich über meine Unterbrechung zu ärgern."


emi "Was?"


"Okay, ich muss das irgendwie wiedergutmachen. Ich muss wissen, woran ich bin, vielleicht sogar unsere Beziehung reparieren."


hi "Kannst du dich wenigstens hinsetzen?"


show emi sad_annoyed_gym onlayer master at center
with charachange

emi "Ich denke, wir können auch so reden."


hi "Okay, klar. Schau mal, was uns beide angeht…"


"Ich überlege, wie ich das, was ich sagen will, am besten in Worte fassen soll."


"Aber bevor ich sie leidenschaftlich anflehen kann, mir noch eine Chance zu geben, hat Emi bereits gesprochen."


show emi sad_shy_gym onlayer master
with charachange

emi "Es gibt kein uns mehr, Hisao."


hi "Warum nicht?"


show emi sad_pout_gym onlayer master
with charachange

emi "Wir passen einfach nicht zueinander."


"Sie sagt so etwas Ungeheuerliches, ohne mir dabei in die Augen zu schauen."


hi "Das glaube ich dir nicht! Wir passen großartig zusammen!"


show emi basic_annoyed_gym onlayer master
with charachange

emi "Das sagt derjenige, der sich gerade dafür entschuldigt hat, dass er letzte Woche aus meinem Haus geworfen wurde."


hi "Wir haben uns gestritten! Ich habe etwas wirklich unglaublich Dummes gesagt und mich dafür entschuldigt!"


show emi sad_angry_gym onlayer master
with charachange

emi "Und wie oft haben wir schon über das Problem gesprochen, das den Streit ausgelöst hat? Wie oft habe ich dir gesagt, dass es eine Grenze gibt, die ich nicht überschreiten würde, und wie oft hast du versucht, sie zu überschreiten?"


hi "Weil diese Grenze dumm war!"


show emi sad_annoyed_gym onlayer master
with charachange

"Emi rollt mit den Augen, verschränkt die Arm vor der Brust, und legt ihren Kopf auf die Seite."


emi "Merkst du es nicht selbst, Hisao? Deshalb passen wir nicht zueinander!"


"Ihre Stimme wird etwas weicher, und sie streicht mir ihrer Hand über meine Wange."


show emi sad_grin_gym_close onlayer master
with characlose

emi "Du bist ein netter Kerl, aber mit uns beiden wird es einfach nichts."


"Mir wird fast schwindlig, als ich begreife, dass sie das geübt hat. Vielleicht jeden Tag, seit ich ihr Haus verlassen habe."


"Sogar das Streicheln meiner Wange wirkt einstudiert, wie aus einem Film."


"Sie hatte nie vor, mir eine weitere Chance zu geben."


"Verdammt, es hätte sie wahrscheinlich nicht gestört, wenn sie mich nie wieder gesehen hätte."


hi "Das war's also? Nichts zu sagen, außer „Hey, es war schön, aber nun tschüß?”"


show emi basic_closedgrin_gym_close onlayer master
with charachange

"Das scheint Emi weit mehr zu amüsieren als von mir beabsichtigt. Ihr Lachen hört sich sehr morbide an."


emi "So lebe ich mein Leben, Hisao. Das solltest du inzwischen wissen."


show emi sad_grin_gym_close onlayer master
with charachange

emi "Und es war schön."


"Ein trauriges Lächeln. Sie schaudert leicht und das Lächeln verschwindet."


show emi sad_shy_gym_close onlayer master
with charachange

emi "Aber nun ist es vorbei. Und es ist besser so."


"Ich will losbrüllen, sie anschreien. Sie zur Räson bringen, ihr zeigen, dass das alles dumm ist. Dass sie nur Angst vor mir hat, Angst davor, jemandem nahe zu sein."


"Ich will ihr sagen, dass ich sie liebe und dass ich sie nicht einfach so aufgeben kann."


"Nur… Es wäre sinnlos. Sie hat sich entschieden. Es ist vorbei."


hi "In Ordnung."


show emi sad_grin_gym_close onlayer master
with charachange

"Emi nickt zufrieden. Ich würde am liebsten auf irgendetwas einschlagen."


emi "Gut."


show emi basic_grin_gym_close onlayer master
with charachange

"Ihre Miene hellt sich auf, als sie wieder ihre falsche Fröhlichkeit zur Schau trägt."


emi "Wir sehen uns, Hisao."


hi "Nein, das werden wir nicht. Du wirst es nicht einmal versuchen."


show emi basic_grin_gym_close onlayer master:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi onlayer master
with None

"Sie zuckt mit den Schultern, als wollte sie sagen: „Wie du meinst”, und wendet mir wieder den Rücken zu. Dann fängt sie wieder an, mit hoher Geschwindigkeit um den Sportplatz zu laufen."


"Ich fühle mich wie betäubt. Das war es. Das Ende unserer Beziehung. Zumindest ein Abschluss."


"Emi läuft wieder an mir vorbei, ohne mich eines Blickes zu würdigen. Sie läuft nun viel schneller, und ich muss unwillkürlich an unser erstes gemeinsames Training denken."


"Ich bin gerannt, um dich einzuholen – um zu beweisen, dass ich nicht so schwach war, wie ich war. Aber das ist nicht gut für mich ausgegangen, nicht wahr?"


"Und nun läufst du wieder zu schnell für mich, und wieder habe ich die Wahl, hinter dir herzulaufen."


"Aber das werde ich nicht. Nicht dieses Mal. Du würdest mich niemals aufholen lassen."


stop music fadeout 6.0

scene bg school_dormhisao onlayer master
with shorttimeskip

"Ich weiß später nicht mehr, wie ich vom Sportplatz auf mein Zimmer gekommen bin oder welches Buch ich noch gelesen habe."


"Bevor ich schlafen gehe, stelle ich meinen Wecker um. Emi und ich hatten unsere letzte Begegnung."


scene black onlayer master
with shuteye

"Nach diesem Tag sprechen wir nicht mehr miteinander."




label de_E27b:


"Na ja, ich denke, es kann nicht schaden, mit jemandem über mein Problem zu reden. Vielleicht hat Misha ja sogar einen Rat für mich."


hi "Wir hatten einen Streit bei ihr zu Hause."


hi "Ich habe versucht, ihr näher zu kommen, und sie wollte das nicht, und…"


hi "Ich habe etwas Dummes gesagt, und sie hat mich hinausgeworfen."


show misha perky_sad onlayer master
with charachange

mi "Hast du seitdem mit ihr gesprochen?"


"Misha sieht ehrlich besorgt aus. Ich bin überrascht. Ich hatte fast erwartet, dass sie das Thema wechselt, nachdem sie herausgefunden hat, was los ist."


"Es überrascht mich noch mehr, wie leicht es mir fällt, ihr alles zu erzählen."


hi "Nein, habe ich nicht. Ich kann mich seitdem einfach nicht dazu bringen, ihr ins Gesicht zu schauen."


hi "Ich habe mich voll und ganz zum Narren gemacht, und wahrscheinlich hasst sie mich nun. Besonders, weil ich sie seitdem nicht mehr getroffen habe."


show misha sign_smile onlayer master
with charachange

mi "Du bist ziemlich dämlich, Hicchan."


stop music fadeout 4.0

"Das hört sich nicht nach einem Ratschlag an."


hi "Hm?"


show misha hips_frown onlayer master
with charachange

"Misha stemmt ihre Hände in die Hüften und beginnt eine Rede, wie ich sie eher von Shizune erwartet hätte."


mi "Die Lösung für dein Problem ist simpel! Du musst zu ihr gehen und dich entschuldigen! Die Sache auf sich beruhen zu lassen, macht alles nur schlimmer!"


mi "Du kannst nicht wissen, dass sie dich hasst, solange sie es dir nicht sagt! Solange hast du keine Beweise, dass deine Angst begründet ist!"


mi "Und wenn sie dir wirklich etwas bedeutet, solltest du dir dann keine Sorgen machen, wie es ihr bei all dem geht?"


play music music_innocence fadein 1.0

"Erschrocken stelle ich fest, dass sie Recht hat. Ich habe meinen Wecker nicht umgestellt, weil ein Teil von mir zusammen mit Emi laufen will."


"Ich habe mein Training fortgesetzt, weil ich weiß, dass Emi sich Sorgen um mich machen würde, wenn ich meine Gesundheit vernachlässigen würde."


"Als ich gestern auf das Dach gegangen bin, hatte ich irgendwie gehofft, dass sie dort sein würde, und war dann enttäuscht, als sie es nicht war."


hi "Ich bin ein Idiot."


show misha hips_grin onlayer master
with charachange

mi "Genau, Hicchan~!"


show misha sign_smile onlayer master
with charachange

mi "So~! Und nun gehst du so bald wie möglich zu ihr und entschuldigst dich bei ihr, okay~?"


"Ich öffne den Mund, um zu sagen, dass ich sofort losgehe, aber die Mittagsglocke läutet, und mir fällt ein, dass ich immer noch Nachmittagsunterricht habe."


hi "Ich gehe zu ihr, sobald der Unterricht vorbei ist. Versprochen."


hi "Und, äh, danke für die Ratschläge…"


show misha hips_grin onlayer master
with charachange

"Misha strahlt mich an, als wäre ich ein Kind, das gerade das ABC gelernt hat."


mi "Gut! Ich werde Shicchan dann sagen, dass es dir wieder gut geht~!"


hi "Äh, ja. Tu das."


hide misha onlayer master
with charaexit

"Mit einem Winken (und unter völliger Missachtung der Tatsache, dass alle anderen gerade zurückkommen anstatt zu gehen) verlässt Misha den Klassenraum."


"Sie und Shizune haben wohl wieder mit dem Schülerrat zu tun."


scene bg school_scienceroom onlayer master
with shorttimeskip

"Während der Nachmittag voranschreitet, warte ich ungeduldig auf das Ende des Unterrichts. Ich muss {b}jetzt{/b} mit Emi reden."


"Ich muss das wieder in Ordnung bringen. Auch wenn Emi mich jetzt hasst, muss ich mich zumindest entschuldigen."


"Zumindest das schulde ich ihr."


"Sollte ich vor ihrem Zimmer auf sie warten? Nein, das würde zu lange dauern. So wie ich Emi kenne, kann ich sie auf dem Sportplatz finden."


"Ich habe noch keine Idee, was ich sagen soll, wenn ich dort ankomme, aber es beruhigt mich, dass Emi wahrscheinlich auch keinen Plan für eine solche Situation hätte."


"Einfach improvisieren. Nicht nervös sein und einfach zum Sportplatz gehen. Der Rest findet sich von allein."


scene bg school_track onlayer master
with shorttimeskip

"Der Sportplatz taucht vor mir auf, und noch einmal überfällt mich die Nervosität. Ich widerstehe dem Drang, mich umzudrehen und zu gehen; stattdessen stelle ich befriedigt fest, dass ich Recht hatte. Emi ist noch da."


"Ich mache mich nicht sofort bemerkbar; stattdessen setze ich mich auf die Tribüne, schaue ihr beim Laufen zu und denke an unsere früheren Begegnungen."


show emi basic_confused_gym onlayer master:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter

"Nach ein paar Runden um den Platz bemerkt Emi mich und hält abrupt an. Ihr überraschter Gesichtsausdruck weicht schnell einem zornigen."


show emi basic_annoyed_gym onlayer master at center
with charachange

emi "Was tust du hier?"


"Nicht ganz die Reaktion, die ich erhofft hatte, aber in dieser Situation kann ich nicht zu viel erwarten."


hi "Ich wollte dich für das, was ich neulich gesagt, habe um Verzeihung bitten."


show emi basic_confused_gym onlayer master
with charachange

emi "Neulich?"


show emi basic_closedgrin_gym onlayer master
with charachange

"Sie lacht ungläubig auf."


play music music_sadness fadein 0.5

show emi basic_grin_gym onlayer master
with charachange

emi "Das ist fast eine Woche her, Hisao."


hi "Ja, na ja… besser spät als nie, oder?"


show emi sad_annoyed_gym onlayer master
with charachange

"Emi verschränkt ihre Arme und starrt mich kühl an, als ob sie meine Gedanken erraten wollte. Schließlich nickt sie."


show emi sad_grin_gym onlayer master
with charachange

emi "Hmmph. Da hast du wohl Recht. Schnee von gestern. Ich vergebe dir."


show emi basic_grin_gym onlayer master
with charachange

emi "Ist das alles?"


show emi basic_grin_gym onlayer master:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi onlayer master
with None

"Ihre fast schon ungeduldige Frage kommt so unerwartet, dass sie schon eine halbe Bahn gelaufen ist, bevor ich reagieren kann."


hi "Nein, warte!"


scene bg school_track_on onlayer master
with locationchange

"Sie scheint mich nicht gehört zu haben – oder sie will mich nicht hören – und so nehme ich die Verfolgung auf, ohne mich darum zu kümmern, dass ich dafür komplett falsch angezogen bin."


scene bg school_track_running onlayer master
with Dissolve(2.0)

"Meine Füße tun mir weh, und mein Hemdkragen fühlt sich an wie eine Schlinge um meinen Hals, aber ich laufe ihr trotzdem hinterher, denn wenn ich das nicht tue, verliere ich meine Chance."


"Emi hat noch nicht wirklich beschleunigt, was wahrscheinlich der einzige Grund ist, warum ich es schaffe, sie einzuholen, die Hand auszustrecken und ihr auf die Schulter zu klopfen, kurz bevor meine Beine aufgeben und mich zum Anhalten zwingen."


scene bg school_track_on onlayer master
with Dissolve(2.0)

"Überraschenderweise (glücklicherweise?) scheint sich das ganze Training ausgezahlt zu haben. Ja, ich bin außer Atem, aber zumindest versucht mein Herz nicht aktiv, aus meinem Brustkasten hervorzubrechen."


show emi basic_confused_gym_close onlayer master at center
with charaenter

"Meine Berührung auf ihrer Schulter hat Emi zum Anhalten gebracht, und obwohl sie einen Moment lang besorgt aussieht, als sie mich nach Atem ringen sieht, scheint auch sie ganz gut beurteilen zu können, wozu ich fähig bin."


"Deshalb ist ihre Sorge auch schnell wieder vorbei."


show emi basic_annoyed_gym_close onlayer master
with charachange

emi "Was?"


"Sie scheint so verärgert zu sein, dass ich immer noch da bin, dass ich fast den Mut verliere – aber das habe ich schon viel zu oft."


hi "Ich muss es noch erklären. Warum ich die Sache nicht auf sich beruhen lassen kann."


show emi sad_annoyed_gym_close onlayer master
with charachange

"Emi verschränkt die Arme und wippt mit einer ihrer Beinprothesen, als ob sie ungeduldig mit dem Fuß wippen würde. Obwohl sie so wütend ist und ich so nervös bin, sieht sie doch wunderschön aus."


emi "In Ordnung, Hisao. Erklär's mir."


hi "Die Sache ist, ich weiß, dass du sehr empfindlich bist, was den Unfall und deinen Vater angeht."


"Ich kann das Zucken in Emis Gesicht sehen, als ich die beiden Dinge erwähne, die uns immer weiter auseinander getrieben haben – oder die mir zumindest das Gefühl gegeben haben, wir würden auseinander treiben."


hi "Aber ich denke, genau deshalb will ich mehr über diese Dinge wissen."


hi "Weil ich sehe, wie sehr sie dich belasten, und ich will für dich da sein, um dich zu trösten."


hi "Ich fühle mich elend, wenn ich sehe, wie du nicht schlafen kannst und deprimiert bist – und sag nicht, dass das nicht stimmt. Ich weiß es, okay?"


hi "Ich erinnere mich an die Nacht, als du mit mir eingeschlafen bist und diesen Albtraum hattest, und dass du froh warst, dass ich da war, als du aufgewacht bist."


hi "Genauso will ich immer für dich da sein, wenn du mich brauchst."


show emi sad_depressed_gym_close onlayer master
with charachange

"Ihre ernste Fassade beginnt etwas zu bröckeln, aber Emi unterbricht mich, bevor ich fortfahren kann."


emi "Hör… Hör bitte auf. Wir können uns nicht mehr treffen, okay?"


show emi sad_pout_gym_close onlayer master
with charachange

"Nun ist sie nervös. Sie schaut überall hin, nur nicht auf mich. Ich bin überrascht, dass sie nicht davonläuft – sie weiß, dass ich sie nie einholen könnte…"


emi "Wir sind nicht… Wir passen einfach nicht zueinander."


hi "Das ist nicht wahr, und das weißt du auch."


show emi sad_shy_gym_close onlayer master
with charachange

emi "Nein, es ist wahr. Du bist zu-"


hi "Ich weiß. Ich weiß, das ich dich zu sehr gedrängt habe, mir von deiner Vergangenheit zu erzählen."


hi "Wenn du es mir noch nicht erzählen kannst, dann lass mich wenigstens für dich da sein, auch wenn ich den Grund nicht kenne."


hi "Es ist okay, versprochen. Ich werde nicht fragen, warum du Trost brauchst, sondern ihn dir einfach so geben."


show emi sad_depressed_gym_close onlayer master
with charachange

"Emi schüttelt den Kopf, und Tränen scheinen in ihren Augenwinkeln zu lauern."


emi "Hör auf, das zu sagen!"


hi "Warum? Weil du Angst hast, du könntest mein Angebot annehmen?"


show emi sad_pout_gym_close onlayer master
with charachange

emi "Ich habe keine Angst!"


"Ich kann den tadelnden Unterton nicht ganz aus meiner Stimme heraushalten, als ich antworte."


hi "Doch, hast du. Das hast du mir selbst erzählt, erinnerst du dich? Das macht nichts. Wirklich nicht."


hi "Aber ich denke, jemand, der es schafft, so einen Unfall zu überstehen und immer noch so energiegeladen und fröhlich ist wie du, der wird auch entschlossen genug sein, dieser Angst entgegenzutreten."


show emi sad_angry_gym_close onlayer master
with charachange

emi "Entschlossenheit? Was weißt du schon von Entschlossenheit?"


hi "Ich weiß, dass da ein Mädchen ist, das so entschlossen ist, sich um einen Fremden zu kümmern, dass sie auf dem Schulfest sein Essen geklaut hat."


hi "Ich weiß, dass da ein Mädchen ist, das so entschlossen ist, mir mit meinen Problemen zu helfen, dass sie ein komplettes Ernährungs- und Trainingsprogramm zusammengestellt hat…"
hi "… und das ganze dann auch noch mit mir zusammen durchgezogen hat – sogar als sie selbst nicht laufen konnte."


hi "Entschlossen genug, mich trotz aller Albträume auf Abstand zu halten, weil sie dachte, das wäre der richtige Weg."


hi "Allerdings gibt es da etwas, das dieses entschlossene Mädchen nicht eingeplant hat. Nämlich, dass ich genauso entschlossen sein könnte, sie vor Leid zu bewahren."


hi "Ich habe mich in dich verliebt, und ich weigere mich, das kaputtgehen zu lassen, weil du Angst hast, mich zu verlieren."


show emi excited_sad_gym_close onlayer master
with charachange

"In diesem Moment zerbricht der letzte Rest von Emis Selbstbeherrschung, und plötzlich finde ich mich in ihren Armen wieder, während sie weint."


emi "Warum tust du das? Warum kannst du mich nicht einfach in Ruhe lassen?"


show ev emi_forehead onlayer master
with dissolve

"Ich drücke sie fest an mich und küsse ihren Kopf."


hi "Es tut mir leid, Emi. Du hast mir geholfen, als ich hier angekommen bin, und nun muss ich dir helfen. Das ist nur fair."


emi "Du bist ein hoffnungsloser Fall, wusstest du das?"


"Sie schluckst kurz und zittert ein wenig."


hi "Ist ja lustig; das gleiche könnte ich über dich sagen."


emi "Kannst du etwas für mich tun, Hisao?"


hi "Alles, was du willst."


scene bg school_track_on onlayer master
show emi sad_shy_gym_close onlayer master at center
with charachange

emi "Kannst du jetzt bitte gehen?"


"Es fühlt sich an, als hätte sie mir gerade ein Messer in die Brust gestoßen."


hi "Gehen?"


show emi sad_pout_gym_close onlayer master
with charachange

emi "Ich muss… Ich muss nachdenken, okay?"


emi "Ich kann dir noch nicht alles erzählen. Ich habe immer noch Angst, und wenn du da bist, kann ich nicht klar denken."


emi "Aber tu mir noch einen Gefallen."


hi "Welchen?"


show emi sad_grin_gym_close onlayer master
with charachange

emi "Komm morgen früh zu unserem Training, okay?"


"Ich lächle und fühle mich so gut wie schon lange nicht mehr."


hi "Natürlich. Ich würde es um nichts in der Welt versäumen."


show emi sad_grin_gym onlayer master
with charadistant

"Emi tritt langsam – fast widerstrebend – einen Schritt zurück. Sie schnieft ein wenig und grinst mich dann an – mit einem echten Lächeln, das den Sportplatz erleuchtet und das verblassende Licht des Abends überstrahlt."


show emi basic_grin_gym onlayer master
with charachange

emi "Bis morgen, Hisao."


hi "Okay."


show emi excited_amused_gym_close onlayer master
with characlose

show emi basic_grin_gym onlayer master
with charadistant

"Plötzlich lehnt sie sich nach vorne und drückt einen sanften Kuss auf meine Lippen. Dann weicht sie schüchtern wieder zurück."


show emi basic_grin_gym onlayer master:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi onlayer master
with None

"Sie dreht sich um und fängt wieder an zu laufen, und ich weiß, dass unser Gespräch vorbei ist."


"Meine Lippen kribbeln immer noch von der Wärme dieses kurzen Kusses und der Erinnerung an andere, längere Küsse."


"Mit federnden Schritten gehe ich zurück auf mein Zimmer."


"Wenn morgen früh mein Wecker klingelt, werde ich aufstehen."


stop music fadeout 2.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
